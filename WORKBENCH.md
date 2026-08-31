# Workbench

This is the persistent handoff ledger. A new session should read `TRANSLATION.md`, this file, and `translation_manifest.jsonl` before doing corpus work.

## Source snapshot

Russian source release: 2026-08-18  
Source repository: `tolstoy-russian-md-audited`

## Current state

Pilot batch P001 is active. Source-integrity preflight passed: 15,766 records checked, 0 missing, 0 changed.

## Last completed unit

P001.6 — `corpus/azbuka/v21_109_110_Pozharnye_sobaki.md`

Stages: translation complete; fidelity audit PASS; English edit complete; final source audit PASS; apparatus translated; mechanical validation PASS.

## Active batch

P001 — see `qa/batches/P001.md`.

## Current unit

`corpus/krug_chtenija/v41_011_013_Krug_chtenija_daily_jan_1_1.md`

Stage: not started.

## Next action

Translate the 1 January `Krug chteniya` entry from the Russian compiled text, preserving attribution and the compiled/adapted wording rather than silently substituting canonical English originals. Then audit the result against the source, validate, update the manifest/report/workbench, and commit. After that, perform the post-pilot review and STOP.
