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


### P003 cold fidelity audit

- Completed on **16 deliberately difficult units** (32% of P003; ~3,219 source words).
- Result: **PASS AFTER REVISION**.
- Because defects clustered in the works category, all 8 P003 works were audited. Six required correction: one omitted running-prose clause, 14 omitted footnote/deleted-apparatus passages, one flattened deletion state, and one compressed/mispositioned variant-apparatus structure.
- Eight difficult non-works units (letters, diaries, notes, *Azbuka*, and *Circle of Reading*) required no translation correction.
- `tools/validate_translation.py` was hardened to reject reviewed footnoted units whose apparatus is still `not_started` and reviewed units that lose source `~~` deletion markup.
- Full report: `qa/reports/P003_COLD_AUDIT.md`.

### Translation policy hardening

- Decision D0001 adopted: conservative fidelity before stylistic smoothing.
- Preserve unusual but intelligible concrete Tolstoy phrasing rather than replacing it with smoother abstractions.
- Example settled decision: keep “the whole world of people” rather than “all humanity.”
- Permanent decisions ledger: `metadata/DECISIONS.md`.
- `SOURCE_SUSPECTED` protocol added.
- Automatic source-boundary suspicion detector added as `tools/preflight_boundaries.py`.

## Current corpus state

- Reviewed English translations: **96**.
- P001: 7 complete.
- P002: 25 complete.
- P003: **50 / 50 complete and individually Git-committed**.
- Approximate reviewed source-body words: **17,713**.
- Confirmed source errata: **10**.
- Existing structured coverage records: **89**, currently validating with 0 errors (P001 used the older unstructured audit format).

`python tools/status.py` should reproduce the manifest counts.


### P004

- Batch selected and boundary-preflighted: 50 units, 46 CLEAR / 3 LOW / 1 MEDIUM / 0 HIGH.
- **14 / 50 accepted.**
- Last completed unit: **P004.14 — Letter to Count V. P. Tolstoy, 30 April 1854?**
- Next unit: **P004.15 — Letter to Prince G. V. Lvov, 15 January 1855.**

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
20. `corpus/letters/v75_298_F_A_Straxovu.md`
21. `corpus/letters/v77_116_S_V_Danilevichu.md`
22. `corpus/letters/v77_240_G_A_Novichkovu.md`
23. `corpus/letters/v78_215_T_A_Kuzminskoj.md`
24. `corpus/diaries/v50_022_022_1889_01_14.md`
25. `corpus/diaries/v57_096_096_1909_07_15.md`
26. `corpus/diaries/v48_042_043_1862_09_03.md`
27. `corpus/diaries/v48_059_060_1865_03_17.md`
28. `corpus/diaries/v49_094_095_1883_05_17.md`
29. `corpus/diaries/v50_040_040_1889_02_22.md`
30. `corpus/diaries/v51_014_015_1890_01_27.md`
31. `corpus/diaries/v57_011_012_1909_01_15.md`
32. `corpus/diaries/v49_058_058_1881_10_05.md`
33. `corpus/diaries/v52_138_138_1894_09_08.md`
34. `corpus/notes/v51_158_159_Zapisi_na_listah_1890.md`
35. `corpus/notes/v57_252_253_Zapisnaja_knizhka_1909_g_No_2.md`
36. `corpus/notes/v48_349_350_Zapis_No_7_1878.md`
37. `corpus/azbuka/v21_171_171_Telenok_na_ldu.md`
38. `corpus/azbuka/v21_274_274_Volk_i_jagnenok.md`
39. `corpus/azbuka/v21_342_343_Rasskaz.md`
40. `corpus/azbuka/v22_050_050_U_odnoj_baryni_byla_sobachenka.md`
41. `corpus/azbuka/v22_209_210_Telenok_na_ldu.md`
42. `corpus/azbuka/v22_562_563_Volk_i_jagnenok.md`
43. `corpus/azbuka/v21_207_207_Olen.md`
44. `corpus/azbuka/v21_243_243_Ptitsy_v_seti.md`
45. `corpus/azbuka/v21_348_348_Odin_malchik_uvidal_nischego.md`
46. `corpus/krug_chtenija/v41_536_537_Krug_chtenija_weekly_jul_4_Kamni.md`
47. `corpus/krug_chtenija/v41_045_047_Krug_chtenija_daily_jan_3_5.md`
48. `corpus/krug_chtenija/v41_081_082_Krug_chtenija_daily_feb_1_4.md`
49. `corpus/krug_chtenija/v41_183_185_Krug_chtenija_daily_mar_4_2.md`
50. `corpus/krug_chtenija/v42_154_155_Krug_chtenija_daily_oct_3_3.md`

Last completed unit: **P003.50 — 17 October.**

P003 translation production is complete. Per `qa/batches/P003.md`, the next required step is a deliberately difficult cold fidelity audit before selecting P004.

## Exact source verification completed

The uploaded Russian snapshot was successfully mounted and checked in the resumed runtime. `tools/check_source.py` checked all **15,766** manifest sources with **0 missing** and **0 changed**. P003.01–08 were also confirmed individually against their recorded SHA-256 hashes; all eight matched exactly, so none was reopened.

The P003 boundary preflight scanned the exact snapshot. Only P003.39 and P003.45 were MEDIUM; inspection showed that both apparent nonterminal endings are caused by deletion markup with punctuation inside the deleted span, with neighboring page units independently segmented. They are retained as intentional draft boundaries, not `SOURCE_SUSPECTED`.

P003.20 triggered `SOURCE_SUSPECTED` for a different reason: the audited Markdown has a bare numeral `3` after `карандашом` but no `[^3]` definition. Volume 75 pp. 209–210 confirms that this is a footnote marker and supplies the omitted note. The Russian snapshot remains unchanged; the English restores the verified footnote under the manifest-declared structural override documented in `metadata/source_errata.yml`.

P003.21 also triggered `SOURCE_SUSPECTED`: its Markdown apparatus contains a spurious bare `3.` immediately before the p. 106 marker. Volume 77 pp. 105–106 confirms that the apparatus ends after note 2 and p. 106 begins with letter 117. The English omits only that non-substantive numeral, preserves the page marker, and records the erratum explicitly.

P003.26 triggered `SOURCE_SUSPECTED` because the audited Markdown preserves marker and definition [^1] after Latin `Memento` but leaves the definition empty. The official volume 48 text supplies the gloss `Помни,` (“Remember,”). The English restores that verified gloss only, retains the original Russian source hash, and leaves the Russian repository unchanged.

P003.28 triggered `SOURCE_SUSPECTED` because the audited filename, subtitle, creation field, and manifest metadata say 1883 while the file's source-edition citation says `Дневник 1884 г.` Volume 49 places the 17/29 May entry on pp. 94–95 inside the 1884 diary, and its manuscript description and commentary independently cite the 1884 agenda and correspondence. The stable source path and original hash are retained, English metadata uses verified 1884, both readings are recorded in `metadata/source_errata.yml`, and the Russian snapshot remains unchanged.

P003.29 triggered `SOURCE_SUSPECTED` because the audited Markdown retains footnote [^1], «Можно прочесть: истопил», after `потом` but omits the printed `[?]` uncertainty marker that belongs immediately after that reference. Official volume 50 p. 40 reads `потом[34] [?] пришел Желтов`, with note 34 `Можно прочесть: истоп[ил]`. The English restores only the verified uncertainty marker, translates the existing note, retains the original source hash, and leaves the Russian snapshot unchanged.

P003.33 triggered `SOURCE_SUSPECTED` because the audited entry has `Овеянниково` while neighboring 1894 entries usually use `Овсянниково`. Official volume 52 confirms `Овеянниково` on p. 138 in this exact entry. The reading is therefore source-verified, not corrected; English preserves it as “Oveyannikovo,” retains the original source hash, and leaves the Russian repository unchanged.

P003.50 triggered `SOURCE_SUSPECTED` because the audited Markdown misplaces the p. 155/item 3 boundary after the Lucy Mallory attribution, effectively merging the two Mallory selections under item 2 and leaving a stranded `3` before item 4. Official volume 42 shows p. 155 beginning with item 3 before the second Mallory passage. English restores only that verified structure, retains the original source hash, and leaves the Russian repository unchanged.


P004.09 triggered `SOURCE_SUSPECTED`: the audited Markdown retains reference numerals 3 and 4 in Tolstoy's 3 August 1844 petition but omits the official edition's long Soviet editorial notes 3 and 4. Volume 59 confirms that Tolstoy's petition itself is complete. The Russian witness remains unchanged; English translates all material present in the audited Markdown but does not import the omitted later editorial apparatus, and the defect is recorded in `metadata/source_errata.yml`.

P004.03 triggered `SOURCE_SUSPECTED`: the audited Markdown and the upstream Tolstoy Digital TEI omit the main-text continuation after `сыграв` in item 5 of *A Temporary Method for the Study of Music*. Official volume 1 pp. 241–242 restores `раза два неизвестныя ноты, стараться сыграть наизусть` and textual note 169 `Написано: сыграть.` English restores only that verified material under an exact manifest-declared footnote exception; the Russian snapshot remains unchanged.

## Public-domain provenance pilot

A contained pilot has been completed for `corpus/notes/v48_342_346_Zapisi_No_2_i_3_1870.md` (Volume 48, printed pp. 342–346). The pilot lives under `provenance/pd_core_pilot/` and uses the printed 90-volume scan as the primary textual authority, with the existing Tolstoy Digital-derived Russian Markdown retained only as a comparison witness.

The scan comparison confirmed that the old source's `orthography_mode: reg` can erase editorial distinctions by silently expanding printed bracket completions: `Андр[ей]` → `Андрей`, `на[до]` → `надо`, `кот[орого]` → `которого`, and `пролетар[иата]` → `пролетариата`. The pilot also separates Tolstoy-authored manuscript material from later editorial apparatus instead of inheriting the upstream CC BY-SA package wholesale.

The already accepted English body for this unit required no substantive wording changes. After YAML, page comments, footnote markers, apparatus, and whitespace are normalized away, the accepted English body and the provenance-rebased pilot body match exactly. The accepted `corpus/` file and source manifest remain untouched.

This pilot supports a rebase strategy rather than discarding accepted English work: create a scan-authoritative public-domain Russian core, preserve the current Russian corpus as a licensed comparison witness, and revalidate English units against the clean core. Before scaling corpus-wide, run a second pilot on an already-reviewed published literary work.

## NEXT ACTION

1. P004 is in production at 14/50 accepted units; resume with **P004.15**.
2. Keep the hardened validator and Decision D0001 conservative-fidelity rule in force.
3. Keep the audited Russian repository read-only as a CC BY-SA comparison witness. English translations remain separately licensed as `PROJECT-TBD`; do not infer ShareAlike status for the translation text from the witness metadata.
4. Continue translate → fidelity audit → conservative English edit → exhaustive coverage proof → mechanical validation → individual Git checkpoint.
5. Include difficult/source-structure material in periodic cold audits rather than relying only on per-unit production QA.
