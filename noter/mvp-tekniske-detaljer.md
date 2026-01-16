# MVP tekniske detaljer (opsummering)

Kildegrundlag: InternalSoftwareSpec2026, InternalSoftwareDetails2026.

## Arkitektur (oversigt)
- Monorepo (pnpm) med Turbo som task-runner.
- Frontend: Next.js (apps/web), React, PDF-rendering via @react-pdf/renderer.
- Backend: Node HTTP server (apps/backend) med PostgreSQL via pg og drizzle-orm.
- Shared package: @org/shared med typer, beregninger og schema-validering (zod).

## Datamodel (persistens)
- wizard_storage (id, active_profile_id, updated_at).
- wizard_profiles (id, name, state, profile, created_at, updated_at, history, responsibilities, version).
- wizard_audit_log (id, profile_id, timestamp, user_id, version, changes) med indeks paa profile_id og timestamp.

## Integrationer og endpoints
- Backend: GET/PUT /wizard/snapshot (auth via Authorization: Bearer token).
- Frontend: fetchWizardSnapshot/persistWizardStorage med no-store cache.
- Report export: PDF, CSRD-pakke (JSON), XBRL (XML) samt optional POST til ekstern report API.

## Automatisering og kvalitet
- Autosave debounce (AUTOSAVE_DELAY) i useWizard.
- Audit log genereres ved ændringer; version increment ved diff.
- Beregningsmotor: moduleCalculators (runA1..runD2) og aggregateResults til live-resultater.

