#!/usr/bin/env python3
import argparse
import re
import socket
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)
REDIRECT_STATUSES = {301, 302, 303, 307, 308}


class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def normalize_url(url: str) -> str:
    url = url.strip()
    parts = urllib.parse.urlsplit(url)
    if not parts.scheme or not parts.netloc:
        return url
    try:
        netloc = parts.netloc.encode("idna").decode("ascii")
    except UnicodeError:
        netloc = parts.netloc
    path = urllib.parse.quote(parts.path, safe="/:@%+~,-._")
    query = urllib.parse.quote(parts.query, safe="=&%+:/?@;,.-_")
    fragment = urllib.parse.quote(parts.fragment, safe="")
    return urllib.parse.urlunsplit((parts.scheme, netloc, path, query, fragment))


def extract_urls(bib_path: Path) -> list[str]:
    content = bib_path.read_text(encoding="utf-8", errors="replace")
    urls = []
    pattern = re.compile(r"\burl\s*=\s*[{\"]([^\}\"\n]+)[\}\"]", re.IGNORECASE)
    for match in pattern.finditer(content):
        url = match.group(1).strip()
        if url:
            urls.append(url)
    return sorted(set(urls))


def check_url(url: str, timeout: float) -> tuple[int | None, str | None, str | None]:
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    }
    opener = urllib.request.build_opener(NoRedirectHandler())

    def request(method: str) -> tuple[int | None, str | None, str | None]:
        current_url = normalize_url(url)
        for _ in range(11):
            req = urllib.request.Request(current_url, headers=headers, method=method)
            if method == "GET":
                req.add_header("Range", "bytes=0-0")
            try:
                with opener.open(req, timeout=timeout) as resp:
                    return resp.status, resp.geturl(), None
            except urllib.error.HTTPError as err:
                if err.code in REDIRECT_STATUSES:
                    location = err.headers.get("Location")
                    if not location:
                        return err.code, err.geturl(), "Missing redirect location"
                    current_url = normalize_url(urllib.parse.urljoin(current_url, location))
                    if err.code == 303:
                        method = "GET"
                    continue
                return err.code, err.geturl(), None
            except (urllib.error.URLError, ssl.SSLError, socket.timeout) as err:
                return None, None, str(err)
        return None, None, "Redirect limit exceeded"

    status, final_url, error = request("HEAD")
    if error is None and status in (400, 401, 403, 405):
        status, final_url, error = request("GET")
    return status, final_url, error


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bib", default="references.bib")
    parser.add_argument("--report", default="link-check-report.txt")
    parser.add_argument("--timeout", type=float, default=30)
    parser.add_argument("--workers", type=int, default=6)
    args = parser.parse_args()

    bib_path = Path(args.bib)
    if not bib_path.exists():
        print(f"Missing bib file: {bib_path}", file=sys.stderr)
        return 1

    urls = extract_urls(bib_path)
    results = []

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        future_map = {pool.submit(check_url, url, args.timeout): url for url in urls}
        for future in as_completed(future_map):
            url = future_map[future]
            try:
                status, final_url, error = future.result()
            except Exception as err:  # noqa: BLE001
                results.append((url, None, None, str(err)))
                continue
            results.append((url, status, final_url, error))

    results.sort(key=lambda item: item[0])

    report_lines = ["URL link check (errors only; 2xx OK after redirects)"]
    for url, status, final_url, error in results:
        if error:
            report_lines.append(f"ERROR {url} :: {error}")
            continue
        if status is None:
            report_lines.append(f"ERROR {url} :: Unknown error")
            continue
        if 200 <= status <= 299:
            continue
        if final_url and final_url != url:
            report_lines.append(f"{status} {url} -> {final_url}")
        else:
            report_lines.append(f"{status} {url}")

    Path(args.report).write_text("\n".join(report_lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
