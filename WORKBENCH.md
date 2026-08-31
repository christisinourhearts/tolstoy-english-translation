# Workbench

This is the persistent handoff ledger. A new session should read `TRANSLATION.md`, this file, `qa/batches/P001.md`, `qa/reports/P001_REVIEW.md`, and `translation_manifest.jsonl` before doing corpus work.

## Source snapshot

Russian source release: 2026-08-18  
Source repository: `tolstoy-russian-md-audited`

## Current state

Pilot batch P001 is complete. A post-P001 Russian source-integrity stress test is also complete.

- Units: 7 / 7 accepted.
- Fidelity audits: 7 / 7 PASS.
- Mechanical validation: 7 English files checked, 0 errors.
- Source-integrity postflight: 15,766 records checked, 0 missing, 0 changed.
- English corpus status after P001: 7 reviewed translations; 1 source-already-English record; 15,758 untranslated records.
- Source stress test: 31 volumes sampled across the 90-volume edition; 0 substantive mismatches; 0 confirmed source errata.
- Source-integrity disposition: PASS, with a `SOURCE_SUSPECTED` verification protocol recommended before scaling.

See `qa/reports/P001_REVIEW.md` for pilot findings and `qa/reports/SOURCE_STRESS_TEST.md` for the Russian-source stress test.

## Last completed unit

P001.7 — `corpus/krug_chtenija/v41_011_013_Krug_chtenija_daily_jan_1_1.md`

Stages: translation complete; fidelity audit PASS; English edit complete; final source audit PASS; mechanical validation PASS.

## Active batch

None. P001 is closed.

## Current unit

None.

## NEXT ACTION

Human review of P001 and the source stress test; then incorporate approved P001/source-integrity rule changes before P002.
