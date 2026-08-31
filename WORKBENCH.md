# Workbench

This is the persistent handoff ledger. A fresh session should read, in this order:

1. `HANDOFF_NEW_CHAT.md`
2. `TRANSLATION.md`
3. `metadata/DECISIONS.md`
4. `WORKBENCH.md`
5. `qa/batches/P003.md`
6. `translation_manifest.jsonl`

## Source snapshot

Russian source release: 2026-08-18  
Source repository: `tolstoy-russian-md-audited`

The authoritative Russian repository must remain read-only. In the current resumed runtime, the exact uploaded Russian snapshot is mounted and has passed the full source/hash check (15,766 checked; 0 missing; 0 changed) and the P003 boundary preflight. A future runtime should repeat those checks against whatever Russian ZIP is actually mounted before resuming translation.

## Completed work

### P001

- 7 / 7 units accepted.
- Full translate → fidelity audit → English edit → final source audit workflow completed.
- Post-pilot review in `qa/reports/P001_REVIEW.md`.

### Russian source stress test

- Stratified source-integrity sampling completed across 31 volumes.
- No evidence of systemic corruption found.
- Report: `qa/reports/SOURCE_STRESS_TEST.md`.
- Two later *New Azbuka* segmentation truncations were independently confirmed and recorded in `metadata/source_errata.yml`.

### P002

- 25 / 25 units accepted.
- 25 / 25 structured bilingual coverage records passed.
- 10-unit cold fidelity audit completed (40% of P002; ~1,766 source words).
- Cold audit found 0 substantive omissions, 0 unsupported substantive additions, 0 reversed meanings, and 0 speaker/reference errors.
- Four style-only smoothings from the cold audit were subsequently reverted under Decision D0001 in favor of more conservative fidelity.
- Reports: `qa/reports/P002_REVIEW.md` and `qa/reports/P002_COLD_AUDIT.md`.

### Translation policy hardening

- Decision D0001 adopted: conservative fidelity before stylistic smoothing.
- Preserve unusual but intelligible concrete Tolstoy phrasing rather than replacing it with smoother abstractions.
- Example settled decision: keep “the whole world of people” rather than “all humanity.”
- Permanent decisions ledger: `metadata/DECISIONS.md`.
- `SOURCE_SUSPECTED` protocol added.
- Automatic source-boundary suspicion detector added as `tools/preflight_boundaries.py`.

## Current corpus state

- Reviewed English translations: **51**.
- P001: 7 complete.
- P002: 25 complete.
- P003: **19 / 50 complete and individually Git-committed**.
- Approximate reviewed source-body words: **10,019**.
- Confirmed source errata: **2**.
- Existing structured coverage records: **44**, currently validating with 0 errors (P001 used the older unstructured audit format).

`python tools/status.py` should reproduce the manifest counts.

## P003 status

Batch file: `qa/batches/P003.md`.

Completed and accepted:

1. `corpus/works/v90_122_122_Obschestvo_nezavisimyh.md`
2. `corpus/works/v34_143_143_Predislovie_k_The_Anatomy_of_Misery_Dzhona_Kenvorti.md`
3. `corpus/works/v26_457_458_Pechatnye_varianty_pervogo_izdanija_stati_Pora_opomnitsja_k_osnovnomu_tekstu.md`
4. `corpus/works/v34_343_344_Konspekt_Vospominanij.md`
5. `corpus/works/v90_093_094_Detskie_zabavy.md`
6. `corpus/works/v29_363_363_Kto_prav_Varianty.md`
7. `corpus/works/v37_005_005_Volk.md`
8. `corpus/works/v40_435_435_Zhizn_i_izrechenija_Krishny_Predislovie.md`
9. `corpus/letters/v60_095_N_A_Nekrasovu.md`
10. `corpus/letters/v61_151_M_N_Longinovu.md`
11. `corpus/letters/v62_372_A_A_Fetu.md`
12. `corpus/letters/v62_507_N_M_Nagornovu.md`
13. `corpus/letters/v64_152_I_L_Tolstomu.md`
14. `corpus/letters/v64_164_I_I_Petrovu.md`
15. `corpus/letters/v65_295_V_A_Golcevu.md`
16. `corpus/letters/v66_165_G_A_Ermolaevu.md`
17. `corpus/letters/v69_146_T_F_Gotojcevu.md`
18. `corpus/letters/v71_049_Inostrannymizdatelyamiperevodchikam.md`
19. `corpus/letters/v71_307_A_N_Dunaevu.md`

Last completed unit: **P003.19 — Letter to A. N. Dunaev, 7–8 November 1898.**

Next planned unit: **P003.20 — `corpus/letters/v75_298_F_A_Straxovu.md`**.

## Exact source verification completed

The uploaded Russian snapshot was successfully mounted and checked in the resumed runtime. `tools/check_source.py` checked all **15,766** manifest sources with **0 missing** and **0 changed**. P003.01–08 were also confirmed individually against their recorded SHA-256 hashes; all eight matched exactly, so none was reopened.

The P003 boundary preflight scanned the exact snapshot. Only P003.39 and P003.45 were MEDIUM; inspection showed that both apparent nonterminal endings are caused by deletion markup with punctuation inside the deleted span, with neighboring page units independently segmented. They are retained as intentional draft boundaries, not `SOURCE_SUSPECTED`.

## NEXT ACTION

1. Resume at **P003.20** and continue the existing finite workflow:
   translate → fidelity audit → conservative English edit → exhaustive bilingual coverage → mechanical validation → update manifest/workbench → Git commit.
2. Preserve the completed exact-source verification; do not reopen P003.01–19 without a concrete fidelity or source reason.
3. Inspect any future MEDIUM/HIGH boundary flag rather than automatically rejecting it.
4. After P003.50, stop and perform a deliberately difficult cold-audit sample before selecting P004.

Do not begin a new batch or retranslate completed units merely for stylistic variety. `metadata/DECISIONS.md` governs settled editorial choices.
