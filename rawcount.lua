local files = {
  "opgaver/02.tex",
  "opgaver/03.tex",
  "opgaver/04.tex",
  "opgaver/05.tex",
  "opgaver/06.tex",
  "opgaver/07.tex",
  "opgaver/08.tex",
  "opgaver/09.tex",
  "opgaver/10.tex",
}

local function read_file(path)
  local f = io.open(path, "r")
  if not f then return "" end
  local content = f:read("*a")
  f:close()
  return content or ""
end

local function strip_comments(text)
  text = text:gsub("\\\\%%", "__PERCENT__")
  text = text:gsub("%%[^\n]*", "")
  text = text:gsub("__PERCENT__", "\\\\%%")
  return text
end

local function remove_env(text, env_pattern)
  local pattern = "\\\\begin%s*{" .. env_pattern .. "}%s*(%b[])?%s*[%s%S]-\\\\end%s*{" .. env_pattern .. "}"
  return text:gsub(pattern, " ")
end

local function remove_cmd(text, cmd)
  for _ = 1, 3 do
    text = text:gsub("\\\\" .. cmd .. "%s*%b[]%s*%b{}", " ")
    text = text:gsub("\\\\" .. cmd .. "%s*%b{}", " ")
  end
  return text
end

local function clean(text)
  text = strip_comments(text)

  text = remove_env(text, "table")
  text = remove_env(text, "table%*")
  text = remove_env(text, "figure")
  text = remove_env(text, "figure%*")

  text = text:gsub("\\\\caption%s*%b[]%s*%b{}", " ")
  text = text:gsub("\\\\caption%s*%b{}", " ")

  text = text:gsub("[Tt]abel%s*\\\\ref%s*%b{}", " ")
  text = text:gsub("[Ff]igur%s*\\\\ref%s*%b{}", " ")
  text = text:gsub("[Ff]ig%.?%s*\\\\ref%s*%b{}", " ")
  text = text:gsub("[Bb]ilag%s*\\\\ref%s*%b{}", " ")

  local cite_cmds = {
    "parencite", "parenciteshort", "textcite", "textcitefull", "cite", "citep",
    "citet", "citeauthor", "citeyear", "footcite", "parencites", "autocite"
  }
  for _, cmd in ipairs(cite_cmds) do
    text = remove_cmd(text, cmd)
  end

  local ref_cmds = { "ref", "autoref", "cref", "Cref", "eqref", "pageref", "nameref" }
  for _, cmd in ipairs(ref_cmds) do
    text = remove_cmd(text, cmd)
  end

  local other_cmds = { "label", "addcontentsline", "addtocontents", "addtocounter" }
  for _, cmd in ipairs(other_cmds) do
    text = remove_cmd(text, cmd)
  end

  text = text:gsub("\\\\begin%s*%b{}", " ")
  text = text:gsub("\\\\end%s*%b{}", " ")
  text = text:gsub("\\\\item%s*%b[]", " ")
  text = text:gsub("\\\\item", " ")

  text = text:gsub("\\\\[A-Za-z@]+%*?", "")
  text = text:gsub("\\\\", " ")

  text = text:gsub("{", "")
  text = text:gsub("}", "")
  text = text:gsub("%$", "")

  text = text:gsub("%s+", " "):gsub("^%s+", ""):gsub("%s+$", "")
  return text
end

local all = ""
for _, path in ipairs(files) do
  local content = read_file(path)
  if content and content ~= "" then
    all = all .. " " .. clean(content)
  end
end

all = all:gsub("%s+", " "):gsub("^%s+", ""):gsub("%s+$", "")
local count = #all
local pages = count / 2400

tex.sprint("\\gdef\\RawCharCount{" .. count .. "}")
tex.sprint(string.format("\\gdef\\RawPageCount{%.2f}", pages))
texio.write_nl("log", "RAW_CHAR_COUNT: " .. count)
texio.write_nl("log", string.format("RAW_PAGE_ESTIMATE: %.2f", pages))
