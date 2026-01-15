# Case: egen virksomhed (dataindsamling)

Udfyld nedenstaaende felter, saa casen kan beskrives konsistent og sporbar.

## Produktbeskrivelse
- Kort produktpitch (2-4 linjer): ESG-as-a-Service-løsning gør det hurtigt at omsætte komplekse regulatoriske krav til sporbar dokumentation for sundhedsvirksomheder.
- Hvilket problem loeses og for hvem: Hjælper mindre og mellemstore sundhedsvirksomheder (klinikker, leverandører, biotek) og deres compliance-ansvarlige med at levere CSRD/ESRS/GRI-data uden at forstyrre driften.
- Centrale funktioner (MVP vs. fuld version): MVP opsamler data til energi, affald og sociale indikatorer, har audit-log, validationsregler og eksportere PDF/CSRD/XBRL; fuld version tilføjer integrationsgates mod indkøb/økonomi, benchmarkmodul og avancerede alerts.

## Maalgruppe og segmenter
- Primære kunder (branche, stoerrelse, rolle): Private klinikker, mindre hospitaler og medtech-leverandører med 50-500 ansatte, hvor CFO/compliance står med krav om ESG-data.
- Sekundaere kunder/interessenter: Revisorer, investorer, banker og myndigheder samt konsulenter, der understøtter SMV’er i ESG-modenhed.
- Kundeproblemer og pains: Fragmenterede datakilder, mangel på standardiserede måleprincipper og pres fra både CSRD/ESRS og bæredygtige leverandørkrav.

## Processer og leverance
- Hvordan leveres ydelsen (trin-for-trin): (1) Modulvalg og onboarding, (2) datakortlægning, (3) wizard-baseret indsamling med audit-log, (4) validering/modulberegninger og (5) rapport- og compliance-eksport.
- Dataindsamling: hvilke kilder og formater: Energital, affald og sociale KPI’er fra ERP/økonomi, HR- og facilities-systemer i Excel/CSV/API; data valideres med schema (Zod) og gemmes i wizard_storage med versionering.
- Rapportoutput: formater, frekvens, anvendelse: Genererer PDF-rapporter, CSRD/ESRS-pakker og XBRL, leveres kvartalsvist/årligt til bestyrelse, investorer, myndigheder og kunder.

## Okonomi
- Prisstruktur (abonnement, projekt, usage): Fast abonnement for standardmoduler, projektgebyr for integration og opsætning, samt usage-gebyr for ekstra eksport (XBRL/CSRD-pakker).
- Estimerede omkostninger (personer, drift, data): Team på produktleder, dataingeniør og ESG-analytiker + cloud-drift (database/API), support og løbende opdatering af beregningsmoduler.
- Forventet indtjening (kort/mellem sigt): 30-50 SMV’er på abonnement (~20-30 tkr/måned) med vækst via partnerskaber; mellemlang sigt tilføjes enterprise-salg og dataværdifunktioner.

## Afgrænsninger og antagelser
- Hvad er udeladt i casen og hvorfor: Casen indbefatter ikke ekstern assurance eller dyb klimatilføjelse (f.eks. fysiske reduktionsmodeller); fokus er på sporbarhed og compliance‑workflow til SMV’er.
- Antagelser, der skal dokumenteres: Antager at kunder kan levere basale energidata og at regulatoriske krav (CSRD/ESRS/Taxonomi) holder; antager også at leverandørdata kan repræsenteres med repræsentative emissionsfaktorer.
