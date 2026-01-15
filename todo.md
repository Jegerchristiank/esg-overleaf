# TODO — ESG-rapportering i sundhedssektoren

Denne liste er lineær og kan krydses af fra top til bund.

## 0. Forberedelse og rammer (nu)
- [x] Kompiler projektet med XeLaTeX/LuaLaTeX og noter alle warnings.
- [x] Udfyld dato og metadata på forsiden i `main.tex`.
- [x] Bekræft at `KUstyle.sty` + `preamble.tex` ikke konflikter (ingen dublerede pakker).
- [x] Fastlæg label-konvention og navngivning; brug `sec:`, `subsec:`, `fig:`, `tab:`, `eq:`, `app:`.
- [x] Afgør om der skal bruges `siunitx`, `booktabs`, `longtable`; tilføj kun hvis nødvendigt og dokumentér hvorfor.
- [x] Opret makroer for gentagne begreber/forkortelser i `preamble.tex` (fx ESG, CSRD, SMV, MVP).
- [x] Definér en enkel tabelstandard (caption, kilde, note) som du bruger konsekvent.
- [x] Definér figurstandard (filformat, opløsning, caption, kildeangivelse, label).

## 1. Kilde- og datagrundlag
- [x] Gennemgå `references-beskrivelse.txt` og pensum; markér hvilke kilder der skal bruges hvor.
- [x] Udbyg `references.bib` med komplette metadata for alle centrale kilder.
- [x] Indsaml officielle dokumenter: CSRD/ESRS, EU-taksonomien, GRI-standards; læg URL + accessed i .bib.
- [x] Saml empiriske tal og cases fra sundhedssektoren (miljøpåvirkning, affald, energi, arbejdsvilkår).
- [x] Indsamle data til case om egen virksomhed: produktbeskrivelse, målgruppe, processer, økonomi (skabelon i `noter/case-egen-virksomhed.md`).
- [x] Indsamle tekniske detaljer til MVP: arkitektur, datamodel, integrationspunkter, automatisering.
- [x] Opret en "påstand → kilde"-matrix i noter, så hver claim kan spores.

## 2. Disposition og argument-kæde
- [x] Skriv en kort argument-kæde (1-2 linjer pr. hovedsektion): hvad etableres, hvad bruges, hvad konkluderes.
- [x] Skriv punktdisposition for hver undersektion (3-7 bullets) før du skriver prosa.
- [x] Afklar hvilke tabeller/figurer der er nødvendige, og hvor de placeres.

## 3. Indledning (opgaver/02)
### 3.1 Overordnet indledning
- [x] Skriv en kort indledende brotekst i `opgaver/02/02-indledning.tex` der rammesætter problemet og rapportens bidrag.
- [x] Indsæt klare referencer til hovedproblemet og til afsnittene via `\ref`.

### 3.2 Baggrund og motivation
- [x] Udfyld `opgaver/02/02-01-baggrund-og-motivation.tex` med sektorens udfordringer og hvorfor ESG er relevant nu.
- [x] Understøt centrale udsagn med citations (CSRD/GRI/empiri).

### 3.3 Formål og forskningsspørgsmål
- [x] Udfyld `opgaver/02/02-02-formaal-og-forskningssporgsmaal.tex` med klart formål og 2-4 forskningsspørgsmål.
- [x] Tjek at hvert spørgsmål besvares eksplicit i analyse/konklusion.

### 3.4 Problemformulering
- [x] Skriv præcis problemformulering i `opgaver/02/02-03-problemformulering.tex`.
- [x] Afgræns begreber (ESG, SMV, ESG-as-a-Service) allerede her.

### 3.5 Afgrænsning
- [x] Skriv afgrænsning i `opgaver/02/02-04-afgraensning.tex`: hvad er ikke inkluderet, og hvorfor.
- [x] Begrunde afgrænsninger med praksis- eller metodehensyn.

### 3.6 Rapportens opbygning
- [x] Udfyld `opgaver/02/02-05-rapportens-opbygning.tex` med kort overblik over kapitlerne og formål.

## 4. Kontekst og rammer (opgaver/03)
### 4.1 Overblik
- [x] Skriv sektionens intro i `opgaver/03/03-kontekst-og-rammer.tex` med formål og struktur.

### 4.2 ESG-rapportering i sundhedssektoren
- [x] Udfyld `opgaver/03/03-01-esg-rapportering-i-sundhedssektoren.tex` med definitioner og branchens status.
- [x] Indsæt relevante tal/cases og forklar deres betydning.

### 4.3 Regulatoriske rammer (CSRD, EU-taksonomien, GRI)
- [x] Udfyld `opgaver/03/03-02-regulatoriske-rammer-csrd-eu-taksonomien-og-gri.tex`.
- [x] Beskriv krav, scope, tidslinje og væsentlighed.
- [x] Overvej en tabel, der sammenligner rammerne (krav, målgruppe, data).

### 4.4 SMV'er og behovet for forenkling
- [x] Udfyld `opgaver/03/03-03-smver-og-behovet-for-forenkling.tex` med SMV-perspektiv, ressourcer og barrierer.
- [x] Understøt med empiriske kilder.

### 4.5 ESG-as-a-Service som servicekoncept
- [x] Udfyld `opgaver/03/03-04-esg-as-a-service-som-servicekoncept.tex` med definition, værdiforslag og afgrænsning.
- [x] Positionér konceptet ift. SaaS/outsourcing og regulatorisk compliance.

## 5. Teoretisk ramme (opgaver/04)
### 5.1 Overblik
- [x] Skriv intro til teori-sektionen i `opgaver/04/04-teoretisk-ramme.tex` og begrund teorivalg.

### 5.2 Standardisering og organisationer (Brunsson)
- [x] Udfyld `opgaver/04/04-01-standardisering-og-organisationer-brunsson.tex` med kernebegreber og relevans.
- [x] Link teorien til ESG-rapportering som standardiseringspraksis.

### 5.3 Policy- og governanceperspektiver
- [x] Udfyld `opgaver/04/04-02-policy-og-governanceperspektiver.tex` med politiske og institutionelle rammer.
- [x] Vis hvordan governance påvirker ESG-implementering.

### 5.4 Økonomiske og kommercielle perspektiver
- [x] Udfyld `opgaver/04/04-03-oekonomiske-og-kommercielle-perspektiver.tex` med business case, value creation, stakeholder/shareholder.
- [x] Indsæt centrale citationer (f.eks. Friedman, ESG-performance studier).

### 5.5 Opsamling af den teoretiske ramme
- [x] Udfyld `opgaver/04/04-04-opsamling-af-den-teoretiske-ramme.tex` med en syntese og forventede analytiske greb.

## 6. Metode (opgaver/05)
### 6.1 Overblik
- [x] Skriv metode-intro i `opgaver/05/05-metode.tex` med metodevalg og begrundelser.

### 6.2 Design og tilgang
- [x] Udfyld `opgaver/05/05-01-design-og-tilgang.tex` med forskningsdesign (case, udviklingsprojekt, kvalitativ/kvantitativ).
- [x] Afklar hvordan teori, empiri og software kobles.

### 6.3 Datagrundlag og kilder
- [x] Udfyld `opgaver/05/05-02-datagrundlag-og-kilder.tex` med datatyper, kilder, kvalitet og begrænsninger.
- [x] Overvej en tabel over datakilder og vurderet kvalitet.

### 6.4 Case: egen virksomhed som pilot
- [x] Udfyld `opgaver/05/05-03-case-egen-virksomhed-som-pilot.tex` med beskrivelse af casen og dens relevans.
- [x] Afklar bias og hvad casen repræsenterer.

### 6.5 Etik, compliance og kvalitet
- [x] Udfyld `opgaver/05/05-04-etik-compliance-og-kvalitet.tex` (GDPR, datasikkerhed, transparens).
- [x] Dokumentér hvordan kvalitet og sporbarhed sikres.

### 6.6 Begrænsninger
- [x] Udfyld `opgaver/05/05-05-begraensninger.tex` med metodiske begrænsninger og konsekvenser.

## 7. Software og MVP (opgaver/06)
### 7.1 Overblik
- [x] Skriv sektionens intro i `opgaver/06/06-software-og-mvp.tex` med formål og struktur.

### 7.2 Formål og krav
- [x] Udfyld `opgaver/06/06-01-formaal-og-krav.tex` med forretningsmål og krav (funktionelle og ikke-funktionelle).
- [x] Overvej en kravtabel med prioritering.

### 7.3 Systemoversigt og arkitektur
- [x] Udfyld `opgaver/06/06-02-systemoversigt-og-arkitektur.tex`.
- [x] Indsæt arkitekturdiagram (figur) med forklarende caption og kilde/egen fremstilling.

### 7.4 Datamodel og ESG-indikatorer
- [x] Udfyld `opgaver/06/06-03-datamodel-og-esg-indikatorer.tex` med dataskema og mapping til CSRD/GRI.
- [x] Indsæt tabeller med indikatorer og målemetoder.

### 7.5 Dataindsamling og automatisering
- [x] Udfyld `opgaver/06/06-04-dataindsamling-og-automatisering.tex` med pipeline, integrationer og validering.
- [x] Beskriv datakvalitet og audit trail.

### 7.6 Brugerflow og rapportoutput
- [x] Udfyld `opgaver/06/06-05-brugerflow-og-rapportoutput.tex` med processer, UI-flow, outputformater.
- [x] Indsæt mockups eller flowdiagrammer som figurer.

### 7.7 Demonstration og evaluering
- [x] Udfyld `opgaver/06/06-06-demonstration-og-evaluering.tex` med testscenarier, resultater og begrænsninger.
- [x] Relatér evalueringen til kravene fra 7.2.

## 8. Analyse (opgaver/07)
### 8.1 Overblik
- [x] Skriv analyse-intro i `opgaver/07/07-analyse.tex` med fokus og metodekobling.

### 8.2 ESG som organisationsstandard
- [x] Udfyld `opgaver/07/07-01-esg-som-organisationsstandard.tex` og koble til Brunsson/standardisering.
- [x] Peg på empiriske eksempler fra case/branche.

### 8.3 Værdiforslag og forretningsmodel
- [x] Udfyld `opgaver/07/07-02-vaerdiforslag-og-forretningsmodel.tex` (value proposition, kunder, kanaler).
- [x] Brug teori til at vurdere kommercialisering.

### 8.4 Prisfastsættelse og kundesegmentering
- [x] Udfyld `opgaver/07/07-03-prisfastsaettelse-og-kundesegmentering.tex` med segmenter, willingness-to-pay, pricing.
- [x] Understøt med data eller begrundede antagelser.

### 8.5 Organisatoriske og økonomiske implikationer
- [x] Udfyld `opgaver/07/07-04-organisatoriske-og-oekonomiske-implikationer.tex` med governance, ressourcer, ROI.
- [x] Sammenhold med regulative krav og SMV-begrænsninger.

### 8.6 Implementering i sundhedssektoren
- [x] Udfyld `opgaver/07/07-05-implementering-i-sundhedssektoren.tex` med barrierer, incitamenter og anbefalinger.
- [x] Relatér til eksisterende praksis og modenhed.

## 9. Diskussion (opgaver/08)
### 9.1 Overblik
- [x] Skriv diskussions-intro i `opgaver/08/08-diskussion.tex`.

### 9.2 Sammenhæng mellem teori, empiri og software
- [x] Udfyld `opgaver/08/08-01-sammenhaeng-mellem-teori-empiri-og-software.tex`.
- [x] Drøft, hvor MVP'en understøtter eller udfordrer de teoretiske antagelser.

### 9.3 Implikationer for SMV'er
- [x] Udfyld `opgaver/08/08-02-implikationer-for-smver.tex` med konsekvenser og praktiske implikationer.

### 9.4 Begrænsninger og alternative forklaringer
- [x] Udfyld `opgaver/08/08-03-begraensninger-og-alternative-forklaringer.tex` og diskuter bias.

## 10. Konklusion (opgaver/09)
- [x] Udfyld `opgaver/09/09-konklusion.tex` og besvar forskningsspørgsmålene punkt for punkt.
- [x] Opsummer hovedbidrag og centrale fund kort.

## 11. Perspektivering og anbefalinger (opgaver/10)
- [x] Udfyld `opgaver/10/10-perspektivering-og-anbefalinger.tex` med fremtidigt arbejde og anbefalinger.
- [x] Skeln tydeligt mellem empirisk baserede anbefalinger og normative vurderinger.

## 12. Resumé og Abstract (opgaver/00 og 01)
- [x] Skriv dansk resumé i `opgaver/00/00-resume.tex` når konklusionen er færdig.
- [x] Skriv engelsk abstract i `opgaver/01/01-abstract.tex` (samme struktur som resumé).

## 13. Bilag (opgaver/11)
- [x] Udfyld intro til bilag i `opgaver/11/11-bilag.tex`.
- [x] Indsæt projektbeskrivelse i `opgaver/11/11-01-projektbeskrivelse.tex`.
- [x] Tilføj supplerende figurer/tabeller i `opgaver/11/11-02-supplerende-figurer-og-tabeller.tex` og referér fra brødteksten.
- [x] Udfyld teknisk dokumentation i `opgaver/11/11-03-teknisk-dokumentation.tex` (arkitektur, datamodel, API, mv.).

## 14. Reference- og sporbarhedstjek
- [x] Gennemgå alle afsnit for påstande uden citation; tilføj `\parencite`/`\textcite`.
- [x] Tjek at alle labels er unikke og alle `\ref`/`\cref` peger korrekt.
- [x] Tjek at alle figurer/tabeller er nævnt i brødteksten og har informativ caption.
- [x] Fjern eller begrund eventuelle ubrugte labels.
- [x] Kør en reference-audit: indledning og diskussion skal kunne spores til data eller kilder.

## 15. Sprog, typografi og konsistens
- [x] Ensret fagbegreber og forkortelser; introducer første gang de bruges.
- [x] Ensret tal og enheder (decimalkomma, procent, valuta).
- [x] Tjek sprog på faste labels (fx "Indholdsfortegnelse") og ret til dansk hvis krævet.
- [x] Gennemgå for unødige manuelle spacing (fx `\\` eller `\vspace`) og fjern.
- [x] Tjek at tabeller bruger ens typografi (booktabs, ingen lodrette streger).
- [x] Tjek at figurer har tilstrækkelig opløsning og korrekt kildeangivelse.

## 16. Endelig kvalitetssikring og aflevering
- [ ] Kompiler med XeLaTeX/LuaLaTeX + biber indtil der ikke er warnings (kræver LaTeX-installation lokalt eller i Overleaf).
- [ ] Tjek sideantal (maks. 40 sider).
- [ ] Læs rapporten i PDF og tjek flow, overskrifter og henvisninger.
- [x] Foretag sidste sproglige korrektur (dansk og engelsk).
- [ ] Eksportér endelig PDF og aflever.
