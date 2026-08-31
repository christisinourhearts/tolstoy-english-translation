# Workbench

This is the persistent handoff ledger. A new session should read `TRANSLATION.md`, this file, and `translation_manifest.jsonl` before doing corpus work.

## Source snapshot

Russian source release: 2026-08-18  
Source repository: `tolstoy-russian-md-audited`

## Current state

Pilot batch P001 is active. Source-integrity preflight passed: 15,766 records checked, 0 missing, 0 changed.

## Last completed unit

P001.2 — `corpus/works/v01_097_099_Detstvo_Varianty_teksta_Sovremennika_1852_g_No_9.md`

Stages: translation complete; fidelity audit PASS; English edit complete; final source audit PASS; mechanical validation PASS.

Important pilot finding: some files categorized as `works` consist primarily or entirely of scholarly variant apparatus; current manifest body/apparatus statuses do not model this cleanly. See `qa/batches/P001.md`.

## Active batch

P001 — see `qa/batches/P001.md`.

## Current unit

`corpus/letters/v59_008_T_A_Ergolskojigr_E_A_Tolstoj.md`

Stage: not started.

## Next action

Translate the 27 October 1848 letter. Detect its actual body language (French), translate the letter body into English, preserve the fact that the source letter is French, and separately translate the Russian editorial notes. Then audit, validate, update the manifest/report/workbench, and commit before advancing.
