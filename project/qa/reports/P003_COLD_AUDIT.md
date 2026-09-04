# P003 Cold Fidelity Audit

## Result

**PASS AFTER REVISION.** A direct source-to-English cold audit was performed on 16 deliberately difficult P003 units, representing **32% of the batch** and approximately **3,219 rough source-body words**. Because the first defects clustered in the works category, the sample was widened to include **all eight P003 works units**, plus eight difficult units from letters, diaries, notes, *Azbuka*, and *Circle of Reading*.

The audit found a real early-batch completeness problem in the works subgroup. Six of the eight works units required correction:

- **1 omitted Tolstoy running-prose clause** (P003.06);
- **14 omitted footnote/deleted-apparatus passages** across P003.02, P003.04, and P003.08;
- **1 flattened manuscript deletion state** (P003.01);
- **1 compressed/mispositioned variant-apparatus structure** (P003.03).

After correction, the sampled translations contain:

- **0 known substantive source omissions**;
- **0 unsupported substantive English additions**;
- **0 reversed logical relations or lost negations**;
- **0 wrong speakers, subjects, names, numbers, or dates**;
- **0 unresolved structural losses** in the sample.

The eight sampled non-works units required no translation correction. The known English/source structural differences in P003.20 and P003.29 were independently visible in the direct comparison and remain justified by their already verified source-erratum records.

## What “cold” means here

This was a fresh direct source-to-target and target-to-source pass, but it occurred in the **same model/runtime context** that produced the later P003 translations. It therefore should not be described as independent-model or human verification. The source and final English were compared directly rather than using the existing coverage records as a checklist; existing source-erratum records were consulted only where a target/source structural mismatch required reconciliation.

## Selection

The initial difficult sample was widened after the first defects appeared. Final sample:

1. P003.01 — `corpus/works/v90_122_122_Obschestvo_nezavisimyh.md`
2. P003.02 — `corpus/works/v34_143_143_Predislovie_k_The_Anatomy_of_Misery_Dzhona_Kenvorti.md`
3. P003.03 — `corpus/works/v26_457_458_Pechatnye_varianty_pervogo_izdanija_stati_Pora_opomnitsja_k_osnovnomu_tekstu.md`
4. P003.04 — `corpus/works/v34_343_344_Konspekt_Vospominanij.md`
5. P003.05 — `corpus/works/v90_093_094_Detskie_zabavy.md`
6. P003.06 — `corpus/works/v29_363_363_Kto_prav_Varianty.md`
7. P003.07 — `corpus/works/v37_005_005_Volk.md`
8. P003.08 — `corpus/works/v40_435_435_Zhizn_i_izrechenija_Krishny_Predislovie.md`
9. P003.18 — `corpus/letters/v71_049_Inostrannymizdatelyamiperevodchikam.md`
10. P003.20 — `corpus/letters/v75_298_F_A_Straxovu.md`
11. P003.27 — `corpus/diaries/v48_059_060_1865_03_17.md`
12. P003.29 — `corpus/diaries/v50_040_040_1889_02_22.md`
13. P003.35 — `corpus/notes/v57_252_253_Zapisnaja_knizhka_1909_g_No_2.md`
14. P003.39 — `corpus/azbuka/v21_342_343_Rasskaz.md`
15. P003.46 — `corpus/krug_chtenija/v41_536_537_Krug_chtenija_weekly_jul_4_Kamni.md`
16. P003.47 — `corpus/krug_chtenija/v41_045_047_Krug_chtenija_daily_jan_3_5.md`

## Corrections made

### P003.01 — Society of Independent People

The prior English flattened the source deletion `из членов ~~общества~~` into ordinary prose. The translation now preserves the manuscript state as `excluded from membership ~~in the society~~`. No surrounding meaning changed.

### P003.02 — Preface to *The Anatomy of Misery*

Footnote [^1] and its Russian gloss of the French Maistre quotation had been omitted. The marker and translated note are restored. Tolstoy's running prose was already complete.

### P003.03 — Printed Variants of *It Is Time to Understand!*

All Tolstoy variant readings were present, but the English had compressed away repeated page references and `in the first edition` labels, and the volume-26 p. 458 marker had drifted past the line-34 variant. The full apparatus pattern and correct page-marker position are restored.

### P003.04 — Outline of the *Memoirs*

All seven editorial footnotes were absent even though their markers belong to specific outline items. All seven markers and notes are now translated and restored. The 37-item outline itself did not require wording changes.

### P003.06 — *Who Is Right?* variants

One source clause had disappeared: `которыми был уставлен весь боковой стол`. The prior English replaced the missing material with an ellipsis. It now reads: `Especially tasty appetizers had been prepared for dinner, and the whole side table was covered with them.`

### P003.08 — Preface to *Life and Sayings of Krishna*

Six footnote markers and all six deleted-text notes were absent, including a long deleted cosmological passage and deleted formulations describing Krishna. They are now restored with deletion markup. The accepted running prose otherwise remained unchanged.

## Non-works findings

P003.18, .20, .27, .29, .35, .39, .46, and .47 passed without translation revision. The audit deliberately included mixed-language material, verified source overrides, telegraphic notebook prose, deletion/illegibility markup, an *Azbuka* draft with odd footnotes, and two longer *Circle of Reading* entries. No comparable completeness pattern appeared outside the early works subgroup.

## Tooling hardening

`tools/validate_translation.py` now adds two acceptance checks that would have caught major parts of this failure mode automatically:

1. a `reviewed` source with footnotes may no longer have `apparatus_translation_status: not_started`;
2. reviewed source/target files must preserve the count of `~~` deletion-markup delimiters.

These checks do not replace bilingual auditing, but they prevent the exact silent apparatus/deletion losses found in P003.01, .02, .04, and .08 from recurring unnoticed.

## Assessment

The cold audit changed the assessment of the first eight P003 units: their original coverage records were too optimistic about completeness. The defects were concentrated in manuscript/editorial apparatus, with one genuine running-prose omission. The rest of the sampled batch did not show the same pattern, and all identified defects have now been corrected.

P003 may remain accepted **after these revisions**, but P004 should retain the stronger validator and should not allow an accepted coverage record to claim `known_omissions: []` while source footnotes or deletion markup remain structurally unaccounted for.
