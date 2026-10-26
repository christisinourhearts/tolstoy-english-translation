# Workbench

This is the persistent handoff ledger. A fresh session should read, in this order:

1. `project/docs/HANDOFF_NEW_CHAT.md`
2. `project/docs/TRANSLATION.md`
3. `project/metadata/DECISIONS.md`
4. `project/docs/WORKBENCH.md`
5. `project/docs/RECOVERY_RECONSTRUCTION.md`
6. `project/qa/batches/P004.md`
7. `project/qa/batches/P005.md`
8. `project/translation_manifest.jsonl`

## Source snapshot

Russian source release: 2026-08-18  
Source repository: `tolstoy-russian-md-audited`

The authoritative Russian repository must remain read-only. The surviving baseline records that the exact audited snapshot passed the full source/hash check in the pre-loss runtime (15,766 checked; 0 missing; 0 changed) and the P003/P004 preflights. In the current recovery runtime the Russian ZIP is physically mounted and the full source/hash gate has been rerun successfully: 15,766 checked, 0 missing, 0 changed. A future runtime should repeat the same gate against whatever Russian ZIP is actually mounted before resuming.

## Completed work

### P001

- 7 / 7 units accepted.
- Full translate → fidelity audit → English edit → final source audit workflow completed.
- Post-pilot review in `project/qa/reports/P001_REVIEW.md`.

### Russian source stress test

- Stratified source-integrity sampling completed across 31 volumes.
- No evidence of systemic corruption found.
- Report: `project/qa/reports/SOURCE_STRESS_TEST.md`.
- Two later *New Azbuka* segmentation truncations were independently confirmed and recorded in `project/metadata/source_errata.yml`.

### P002

- 25 / 25 units accepted.
- 25 / 25 structured bilingual coverage records passed.
- 10-unit cold fidelity audit completed (40% of P002; ~1,766 source words).
- Cold audit found 0 substantive omissions, 0 unsupported substantive additions, 0 reversed meanings, and 0 speaker/reference errors.
- Four style-only smoothings from the cold audit were subsequently reverted under Decision D0001 in favor of more conservative fidelity.
- Reports: `project/qa/reports/P002_REVIEW.md` and `project/qa/reports/P002_COLD_AUDIT.md`.


### P003 cold fidelity audit

- Completed on **16 deliberately difficult units** (32% of P003; ~3,219 source words).
- Result: **PASS AFTER REVISION**.
- Because defects clustered in the works category, all 8 P003 works were audited. Six required correction: one omitted running-prose clause, 14 omitted footnote/deleted-apparatus passages, one flattened deletion state, and one compressed/mispositioned variant-apparatus structure.
- Eight difficult non-works units (letters, diaries, notes, *Azbuka*, and *Circle of Reading*) required no translation correction.
- `project/tools/validate_translation.py` was hardened to reject reviewed footnoted units whose apparatus is still `not_started` and reviewed units that lose source `~~` deletion markup.
- Full report: `project/qa/reports/P003_COLD_AUDIT.md`.

### Translation policy hardening

- Decision D0001 adopted: conservative fidelity before stylistic smoothing.
- Preserve unusual but intelligible concrete Tolstoy phrasing rather than replacing it with smoother abstractions.
- Example settled decision: keep “the whole world of people” rather than “all humanity.”
- Permanent decisions ledger: `project/metadata/DECISIONS.md`.
- `SOURCE_SUSPECTED` protocol added.
- Automatic source-boundary suspicion detector added as `project/tools/preflight_boundaries.py`.

## Flagship edition: *The Death of Ivan Ilyich*

- Started 2026-10-06 under D0004 (drafted as a local "D0003"). Records in `project/editions/ivan-ilyich/`.
- Source verified; glossary and name table drafted; pilot unit IVI-02-001 complete.
- Next: segment and translate the rest of chapter II (pilot), then review EDITIONS.md.
- This runs alongside the sampled batches; P008.48 remains the next sampled unit.

## Current corpus state

*Counts in this section are as of the P008.47 checkpoint. Reader commissions (R001, R002) and the 2026-10-13 decisions are recorded further down.*

- Reviewed English translations: **316**.
- P001: 7 complete.
- P002: 25 complete.
- P003: **50 / 50 complete and individually Git-committed**.
- P004: **50 / 50 represented**. P004.01–30 are the original accepted packaged files; P004.31–50 are fresh, explicitly labelled recovery reconstructions after workspace loss.
- P005: **50 / 50 restored and reviewed**. P005.01–20 and P005.23–50 are fresh documented recovery reconstructions from the mounted audited Russian snapshot; P005.21–22 remain the surviving recovery-package artifacts.
- P006: **50 / 50 complete and reviewed**. P006.46–50 are fresh reconstructions from the exact audited Russian witness; the corrected Primer quarantine remains in force.
- P007: **50 / 50 complete and reviewed**. P007.47–50 are the final four *Circle of Reading* units.
- P008: **47 / 50 reviewed**. The corrected deterministic P008 selection is frozen in `project/qa/batches/P008.md`; next is P008.48.
- Approximate reviewed source-body words: **90,729**.
- Confirmed source errata: **43**; source-verified anomalies: **5**.
- Existing structured coverage records: **322**, currently validating with 0 errors (P001 used the older unstructured audit format).

`python project/tools/status.py` should reproduce the manifest counts.

### Recovery status

- Read `project/docs/RECOVERY_RECONSTRUCTION.md` before continuing.
- P004 recovery report: `project/qa/reports/P004_RECOVERY_AUDIT.md`.
- P005 batch reconstruction: `project/qa/batches/P005.md`.
- P005 translation restoration target: **complete through P005.50**. A fresh P005 periodic cold-fidelity sample remains pending because the lost-runtime cold audit cannot be transferred to reconstructed English files.
- The authoritative Russian source ZIP mounted successfully. Full source/hash validation passes: **15,766 checked, 0 missing, 0 changed**; at the P008.47 checkpoint the full translation validator passes **329 English files with 0 errors** and only the two longstanding intentional-Cyrillic warnings.

## P003 status

Batch file: `project/qa/batches/P003.md`.

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

P003 translation production is complete, and its deliberately difficult cold fidelity audit was subsequently completed with PASS AFTER REVISION. P004 was then selected and worked through P004.30 before the packaged checkpoint, with P004.31–50 now represented by the documented recovery reconstruction.

## Exact source verification completed

In the pre-loss 2026-08-31 runtime, the uploaded Russian snapshot was successfully mounted and checked. `project/tools/check_source.py` checked all **15,766** manifest sources with **0 missing** and **0 changed**. P003.01–08 were also confirmed individually against their recorded SHA-256 hashes; all eight matched exactly, so none was reopened.

The P003 boundary preflight scanned the exact snapshot. Only P003.39 and P003.45 were MEDIUM; inspection showed that both apparent nonterminal endings are caused by deletion markup with punctuation inside the deleted span, with neighboring page units independently segmented. They are retained as intentional draft boundaries, not `SOURCE_SUSPECTED`.

P003.20 triggered `SOURCE_SUSPECTED` for a different reason: the audited Markdown has a bare numeral `3` after `карандашом` but no `[^3]` definition. Volume 75 pp. 209–210 confirms that this is a footnote marker and supplies the omitted note. The Russian snapshot remains unchanged; the English restores the verified footnote under the manifest-declared structural override documented in `project/metadata/source_errata.yml`.

P003.21 also triggered `SOURCE_SUSPECTED`: its Markdown apparatus contains a spurious bare `3.` immediately before the p. 106 marker. Volume 77 pp. 105–106 confirms that the apparatus ends after note 2 and p. 106 begins with letter 117. The English omits only that non-substantive numeral, preserves the page marker, and records the erratum explicitly.

P003.26 triggered `SOURCE_SUSPECTED` because the audited Markdown preserves marker and definition [^1] after Latin `Memento` but leaves the definition empty. The official volume 48 text supplies the gloss `Помни,` (“Remember,”). The English restores that verified gloss only, retains the original Russian source hash, and leaves the Russian repository unchanged.

P003.28 triggered `SOURCE_SUSPECTED` because the audited filename, subtitle, creation field, and manifest metadata say 1883 while the file's source-edition citation says `Дневник 1884 г.` Volume 49 places the 17/29 May entry on pp. 94–95 inside the 1884 diary, and its manuscript description and commentary independently cite the 1884 agenda and correspondence. The stable source path and original hash are retained, English metadata uses verified 1884, both readings are recorded in `project/metadata/source_errata.yml`, and the Russian snapshot remains unchanged.

P003.29 triggered `SOURCE_SUSPECTED` because the audited Markdown retains footnote [^1], «Можно прочесть: истопил», after `потом` but omits the printed `[?]` uncertainty marker that belongs immediately after that reference. Official volume 50 p. 40 reads `потом[34] [?] пришел Желтов`, with note 34 `Можно прочесть: истоп[ил]`. The English restores only the verified uncertainty marker, translates the existing note, retains the original source hash, and leaves the Russian snapshot unchanged.

P003.33 triggered `SOURCE_SUSPECTED` because the audited entry has `Овеянниково` while neighboring 1894 entries usually use `Овсянниково`. Official volume 52 confirms `Овеянниково` on p. 138 in this exact entry. The reading is therefore source-verified, not corrected; English preserves it as “Oveyannikovo,” retains the original source hash, and leaves the Russian repository unchanged.

P003.50 triggered `SOURCE_SUSPECTED` because the audited Markdown misplaces the p. 155/item 3 boundary after the Lucy Mallory attribution, effectively merging the two Mallory selections under item 2 and leaving a stranded `3` before item 4. Official volume 42 shows p. 155 beginning with item 3 before the second Mallory passage. English restores only that verified structure, retains the original source hash, and leaves the Russian repository unchanged.


P004.09 triggered `SOURCE_SUSPECTED`: the audited Markdown retains reference numerals 3 and 4 in Tolstoy's 3 August 1844 petition but omits the official edition's long Soviet editorial notes 3 and 4. Volume 59 confirms that Tolstoy's petition itself is complete. The Russian witness remains unchanged; English translates all material present in the audited Markdown but does not import the omitted later editorial apparatus, and the defect is recorded in `project/metadata/source_errata.yml`.

P004.03 triggered `SOURCE_SUSPECTED`: the audited Markdown and the upstream Tolstoy Digital TEI omit the main-text continuation after `сыграв` in item 5 of *A Temporary Method for the Study of Music*. Official volume 1 pp. 241–242 restores `раза два неизвестныя ноты, стараться сыграть наизусть` and textual note 169 `Написано: сыграть.` English restores only that verified material under an exact manifest-declared footnote exception; the Russian snapshot remains unchanged.

## Public-domain provenance pilot

A contained pilot has been completed for `corpus/notes/v48_342_346_Zapisi_No_2_i_3_1870.md` (Volume 48, printed pp. 342–346). The pilot lives under `project/provenance/pd_core_pilot/` and uses the printed 90-volume scan as the primary textual authority, with the existing Tolstoy Digital-derived Russian Markdown retained only as a comparison witness.

The scan comparison confirmed that the old source's `orthography_mode: reg` can erase editorial distinctions by silently expanding printed bracket completions: `Андр[ей]` → `Андрей`, `на[до]` → `надо`, `кот[орого]` → `которого`, and `пролетар[иата]` → `пролетариата`. The pilot also separates Tolstoy-authored manuscript material from later editorial apparatus instead of inheriting the upstream CC BY-SA package wholesale.

The already accepted English body for this unit required no substantive wording changes. After YAML, page comments, footnote markers, apparatus, and whitespace are normalized away, the accepted English body and the provenance-rebased pilot body match exactly. The accepted `corpus/` file and source manifest remain untouched.

This pilot supports a rebase strategy rather than discarding accepted English work: create a scan-authoritative public-domain Russian core, preserve the current Russian corpus as a licensed comparison witness, and revalidate English units against the clean core. Before scaling corpus-wide, run a second pilot on an already-reviewed published literary work.

## NEXT ACTION

1. Read `project/docs/RECOVERY_RECONSTRUCTION.md`, `project/qa/batches/P007.md`, and `project/qa/batches/P008.md`; the durable project state is validated through **P008.47**.
2. Verify the mounted Russian snapshot with `project/tools/check_source.py`; the checkpoint must remain at 15,766/15,766 with 0 missing and 0 changed.
3. Resume with **P008.48**: `corpus/krug_chtenija/v41_057_059_Krug_chtenija_daily_jan_4_4.md`. P007 is complete at 50/50 and P008.01–47 are already reviewed.
4. Keep Decision D0001 conservative-fidelity rule in force and retain the Russian witness as read-only.
5. Keep the fresh deliberately difficult P005 cold-fidelity sample pending as a separate audit task.
6. Keep one accepted unit per Git commit and package periodic full-repository checkpoints.


## Reader commissions (outside batch sequence)

Commissioned units are translated from the same audited witness under the same constitution, but they do not advance the deterministic P-batch selection.

### R001.01 — *Master and Man* (2026-10-07)

- Source: `corpus/works/v29_003_046_Hozjain_i_rabotnik.md` (vol. 29, pp. 3–46), SHA-256 `1e5299b6…0faf0d`, verified against a local clone of the audited Russian repository.
- English: `translations/works/v29_003_046_Master_and_Man.md` (~19,400 words).
- Gauntlet: translate → source-forward fidelity audit → revision → English edit → final source-to-target and reverse scan → mechanical validation. Coverage record PASS.
- 44/44 page markers in sequence; 409/409 paragraphs aligned.
- Seven non-substantive transcription artifacts recorded in `project/qa/source_suspected/v29_003_046_Hozjain_i_rabotnik.json`; print check against vol. 29 is a non-blocking follow-up.
- Translated and audited by one model in one context; a separate cold audit is recommended before publication-scale release.
- Also published on christisinourhearts.com at `/master-and-man/`, with a Romanian translation tracked in the separate `tolstoy-romanian-translation` repository.

### R002.01 — *The Gospel in Brief* (2026-10-08)

- Source: `corpus/works/v24_801_938_Kratkoe_izlozhenie_Evangelija_Predislovie.md` (vol. 24, pp. 801–938, 1881/1883), SHA-256 `87ff4a14…abf203`, verified against the committed blob in a local clone of the audited Russian repository. (On Windows, a clone with `core.autocrlf=true` changes the working-file hash; set `core.autocrlf=false` before verifying.)
- English: `translations/works/v24_801_938_The_Gospel_in_Brief.md` (~61,600 words including front matter; source ~48,700).
- Scope: preface, introduction (John I), twelve chapters, conclusion (First Epistle of John). Committed chapter by chapter on branch `gospel-in-brief`.
- Gauntlet: translate → source-forward fidelity audit (per-paragraph numbers/names/references/negation cross-check and length-ratio scan, every flag inspected) → revision (one omitted phrase restored, small additions removed) → English edit → final source-to-target and reverse scan → mechanical validation. Coverage record PASS.
- 138/138 page markers in sequence; 1632/1632 paragraphs aligned (headings, verse-number prefixes, and the 12-row prayer table line for line).
- Terminology and Gospel-rendering policy recorded as Decision D0002; terms in `TERMINOLOGY.md`, names in `NAMES.md`.
- Transcription artifacts and six readings translated as read but pending a printed-volume check (вражды in John VI, 35; Mark XIX, 18; Mt. XXVI, 20; Luke XII, 41; добить in John X, 31; the French Havet quotation) are recorded in `project/qa/source_suspected/v24_801_938_Kratkoe_izlozhenie_Evangelija_Predislovie.json`. The tolstoy.ru online vol. 24 page does not carry this text, so the print check is a non-blocking follow-up.
- Translated and audited by one model in one context.
- **Independent cold audit done (R002_CA01, 2026-10-08)** on branch `gospel-in-brief-cold-audit`. It covered the full text with a source-forward pass (not sampled), then an English-only read and a complete English–Romanian cross-check. It found and fixed 19 defects in chapter commits: 2 omissions, 1 addition, 7 reversals/shifted meaning, 0 reference errors, 3 terminology (incl. KJV reversion), 2 D0001, 4 style. Verdict **PASS AFTER REVISION**. Report: `project/qa/reports/R002_COLD_AUDIT.md`; record: `project/qa/cold_audit/corpus__works__v24_801_938_Kratkoe_izlozhenie_Evangelija_Predislovie.json`; manifest `cold_audit_status: pass_after_revision`.
- **Print check done (2026-10-08):** the commissioner checked the printed vol. 24 PDF from tolstoy.ru, and all six flagged readings match the print. They are confirmed as printed: вражды, добить, the edition's own wrong references (Mark XIX, 18; Mt. XXVI, 20; Luke XII, 41), and the Havet quotation. The cold audit's earlier *Harmony*-based guess (жажды, побить) is superseded. Source-suspected file `SOURCE_VERIFIED`; no open source questions for R002.01.
- The English–Romanian cross-check found points where the Romanian translation needs fixing (see the report's discrepancy list). They were not edited from this repository.

The P-batch NEXT ACTION above is unchanged.

## P005.01 recovery translation note

The early 1847 untitled philosophical fragment on volume 1, pp. 226–228 was freshly reconstructed in the repaired repository. The pinned source identity remains `21fffd4901f4b4c28c5df263f3ad13e1337b1002745fb5cc9d69abf034ccbec8`; because the audited Russian ZIP is not byte-mountable in this runtime, wording, variants, manuscript gaps, and all three notes were checked against the official 90-volume edition, while repository-wide byte validation remains pending until the exact Russian snapshot can be mounted. The two variants are preserved separately; the recurrent terms limited/unlimited, activity/inactivity, consciousness, and I/not-I are kept deliberately close. Two illegible spans and the unstable marginal syntax are not conjecturally repaired. Structured exhaustive coverage passes.


## P005.02 recovery translation note

The 1847 notebook text *On the Aim of Philosophy* (volume 1, pp. 229–232) was freshly reconstructed and reviewed after P005.01. Its pinned source hash is `c3bf414e36909ea3de18c17a1c1c4d8309e8df975df87b5ca294088944bb224e`. The official 90-volume witness was used to check the complete text and its one editorial note while the exact audited Russian ZIP remains unmountable. The a)–e) structure, internal numbering, shifts among generic person / oneself / you / I, bracketed manuscript expansions, and recurrent formation/activity/will/consciousness terminology are preserved closely. `бредом` remains the strong “delirium”; the Golden Rule is translated directly rather than replaced by a familiar biblical formula. Structured exhaustive coverage passes.

## 2026-10-13 — Decisions D0003–D0005 and the *Circle of Reading* plan

- D0003 (ё → *yo*, initial Е → *Ye*) and D0004 (priority order, Tolstoy rules, E-codes, independence levels, flagship editions) applied; both had existed only as unpushed local patches.
- D0005: one basic translation titled *Circle of Reading*; the website Refuge is a labeled adaptation of it.
- TERMINOLOGY.md: совершенствование = "perfecting", самосовершенствование = "self-perfection".
- Website audit record: `calendar-of-wisdom/audits/2026-10-13-calendar-and-repos-audit.md` in the site folder.
- Pending: merge PR #4 (`gospel-in-brief-cold-audit`). The website page already carries its text fixes as of 2026-10-13.

### Next actions for *Circle of Reading*

1. ~~Reconcile the 31 files in `translations/circle_of_reading/` with the website Calendar data.~~ **Done 2026-10-13**: see `project/qa/reports/CIRCLE_OF_READING_RECONCILIATION_2026-10-13.md` (330 differing blocks judged; one text now).
2. (In progress: R003; January done 2026-10-13.) Translate the remaining *Krug chteniya* files from the audited Russian, or import the website paragraphs as first drafts, and put each through the full gauntlet (§15), with coverage records.
3. Generate the website's translation layer from this repository once the reconciliation is done.

## 2026-10-13 — R003.01: the rest of January

- R003 is the *Circle of Reading* translation batch (see `project/qa/batches/R003.md`). R003.01 covers the 9 January files that had no English: 25–31 January and weekly readings 1 (*The Thief's Son*) and 4 (*The Essence of Christian Teaching*). January is now complete in `translations/circle_of_reading/`.
- Method: the website text was the first draft; every block was checked against the audited Russian and revised; two blocks with no website counterpart (31 January opening) were translated fresh. Coverage records PASS; `validate_translation.py` and `validate_coverage.py` report 0 errors.
- The revised English was written back to the website data (124 units, run `2026-10-13-R003`, with revision history). Website attribution lines keep their display form (full names, no final period); the repository keeps the printed form (D0004).
- Fixed: `v41_050_052` weekly subtitle «Совершенствование» = “Perfecting”, not “Perfection”.
- R003.02–03 done the same day (see below).

## 2026-10-13 — R003.02–03: February and March

- 70 files (34 February, 36 March; about 36,700 Russian words), including the weekly readings *Reason*, *The Buddha*, *Self-Renunciation*, *The Free Man*, *The Archangel Gabriel*, *Prayer*, *Poor People*, *Union*, *A Sea Voyage*, *Non-Resistance to Evil by Violence*, *The Surat Coffeehouse*, and *Korney Vasiliev*. January–March of *Circle of Reading* are now complete in `translations/circle_of_reading/`.
- All 70 units reviewed. Resolved by decision (2026-10-13, recorded in `source_errata.yml`): 2 March «время»/«бремя» → "burden"; 11 March «Лк. гл. 26, ст. 18» → Luke 16:18; 18 February «Мф. гл. 8, ст. 35» → Mark 8:35.
- Source observations for 25 units are in `project/qa/source_suspected/`. Four still need a print check; they are listed in `project/qa/batches/R003.md`.
- Conventions settled: «Иосиф Мадзини» = "Giuseppe Mazzini"; «магометане» = "Muslims"; a period after a quoted title goes inside the quotes; one-letter transcription slips are translated in their evident sense and recorded.
- Fixed: weekly reading 3 heading «СОВЕРШЕНСТВОВАНИЕ» = "PERFECTING" (it was "SELF-PERFECTION"), in the repository and on the website.
- Website: 1,020 units updated in `02.js`/`03.js` with revision history (run `2026-10-13-R003`); weekly titles aligned with the headings.
- R003.04–05 done the same day (see below).

## 2026-10-13 — R003.04–05: April and May; three source decisions

- Decisions (Andrei Evanghelușcă, 2026-10-13), recorded in `source_errata.yml`: 2 March «время» → "burden" (unit now reviewed); 11 March «Лк. гл. 26, ст. 18» → Luke 16:18 (the quoted sentence is Luke 16:18 verbatim); 18 February «Мф. гл. 8, ст. 35» → Mark 8:35 (only Mark has "and the gospel's"). The English gives the correct reference; the note records the printed one. The brief now applies this rule to later batches.
- 70 files (34 April, 36 May; ~35,000 Russian words), all reviewed, including *Good* (Buka), *The Street Vendor* (Anatole France), *From a Letter* (Alexandre Dumas), *A Grain as Big as a Hen's Egg*, *Upbringing* (Mazzini) and *From a Letter on Upbringing*, *Death in the Hospital* (Dostoevsky), *The Law of Violence and the Law of Love* (Buka), *The Trial of Socrates and His Defense*. January–May are complete.
- «воспитание» = "upbringing" where Tolstoy sets it against «образование» ("education"); weekly reading 18 is now titled "Upbringing" on the website.
- Print checks for April–May are listed in `project/qa/batches/R003.md`.
- Website: 812 units updated in `04.js`/`05.js` (run `2026-10-13-R003`).
- Fixed in `build.py` tooling: Russian subtitles with escaped quotes (Socrates) are now read in full.
- R003.06 done the same day (see below).

## 2026-10-13 — R003.06: June

- 37 files (~31,000 Russian words), all reviewed, including Chekhov's *The Darling* with Tolstoy's *Afterword*, *Must It Be So?*, Avilova's *First Sorrow*, La Boétie's *Voluntary Servitude* (Tolstoy's abridgement), Dostoevsky's *The Eagle*, and Tolstoy's *Berries*. January–June (half the book) are complete.
- A wrong reference inside Tolstoy's own sentence (28 June, "verse 24 of chapter 8 of Luke" for Luke 8:21) is kept as printed and explained in the note; only reference lines are corrected.
- Print checks for June are listed in `project/qa/batches/R003.md` (notably 8 June: Confucius «равны», probably a dropped «не»).
- `R003_BRIEF.md` updated with the conventions settled so far.
- Website: 769 units updated in `06.js`; weekly titles aligned ("Must It Be So?", "First Sorrow", "Voluntary Servitude").
- R003.07–08 done the same day (see below).

## 2026-10-13 — R003.07–08: July and August

- 73 files (37 July, 36 August; ~34,000 Russian words), all reviewed. Weekly readings include Tolstoy's *Pascal*, Lamennais, *The Attitude of the First Christians to War*, the letter of the peasant Olkhovik, Hugo's *The Unbeliever* (tr. Tolstoy), Buka's *Repentance*, *The Great Bear (The Dipper)*, Turgenev's *The Sparrow*, Maupassant's *Solitude*, Nietzsche's *Catholicism and Christianity*, and the Henry George land reading. January–August are complete.
- Reference-line corrections: 11 July Luke 6:30–31 (printed 5:30–31); 21 August Matthew 6:7–8 (printed 6:9). Kept as printed in Tolstoy's sentence: 1 July "Matthew 24:14–30" (talents: Matthew 25).
- Print checks for July–August are listed in `project/qa/batches/R003.md` (several attributions printed before passages that seem to belong to them).
- Website: 857 units updated in `07.js`/`08.js`; weekly titles aligned.
- R003.09–11 done 2026-10-14 (see below).

## 2026-10-14 — R003.09–11: September, October, November; review queue

- 105 files (37 September, 34 October, 34 November; ~78,000 Russian words), all reviewed. Weekly readings include *Why Do Men Stupefy Themselves?*, Chekhov's *The Fugitive*, *The Power of Childhood*, *Petr Chelčický*, *The Death of Socrates*, *What For?*, Turgenev's *Living Relics*, *The Law of God and the Law of This World*, *Lamennais*, Rousseau's *Revelation and Reason*, *The Divine and the Human*, Chelčický's *Christianity and the Division of People*, *The Demands of Love*, and Hugo's *Bishop Myriel*. January–November are complete.
- The two longest stories were translated in consecutive parts (2 and 3), each part reading the earlier parts and their glossary first; part files are kept with the working drafts.
- New: `project/qa/R003_REVIEW_QUEUE.md` collects every open item from R003 (print checks, conventions to confirm, uncertain identifications, website notes) as a checklist for Andrei.
- Website: 1,789 units updated in `09.js`/`10.js`/`11.js`; verse and table lines that the site keeps as separate units were updated line by line (20 July Ovid, 12 August Musset/Sully Prudhomme, 15 July Gospel table); five site units whose Russian had been cut off at a footnote marker were restored in full; footnote glosses given inline in brackets on the site.
- Files to upload by FTP: `assets/data/calendar-of-wisdom/02.js`, `04.js`, `07.js`, `09.js`, `10.js`, `11.js`, `assets/data/calendar-of-wisdom.js`, `refuge/index.html`, `circle-of-reading/index.html`.
- R003.12 done 2026-10-20 (see below).

## 2026-10-20 — R003.12: December; the calendar is complete

- 40 files (~27,700 Russian words), all reviewed. Weekly readings: *Women* and *Sisters* (after Maupassant), Tolstoy's preface to *The Teaching of the Twelve Apostles* and the Didache, *Love One Another*, *Garrison and His “Proclamation”* and the Proclamation, Herzen's *The Damaged One*, and V. Olkhovsky on the Nazarenes. With this, every day and weekly reading of *Circle of Reading* (January–December) is translated and reviewed in `translations/circle_of_reading/`.
- Website: 636 units updated in `12.js`; three Herzen units whose Russian had been cut off at footnote markers restored in full; weekly titles aligned.
- `project/qa/R003_REVIEW_QUEUE.md` regenerated: decisions, conventions to confirm, uncertain names, 61 passages for a print check, website notes (including Andrei's idea of clickable underlined glosses instead of bracketed ones), and the remaining appendix files.
- Files to upload by FTP: `assets/data/calendar-of-wisdom/12.js`, `assets/data/calendar-of-wisdom.js`, `refuge/index.html`, `circle-of-reading/index.html` (plus any earlier files not yet uploaded).
- Next (if wanted): the appendix files (monthly readings, censored thoughts, reserve days, variants, unfinished exposition; ~47,000 words).

## 2026-10-22 — R003.13: the appendices of volume 42; *Circle of Reading* complete

- 9 files (~47,000 Russian words), all reviewed: *Monthly Readings* (Buka, La Boétie, Škarvan, Bondarev's *Industry and Idleness*), *Thoughts Omitted by the Publisher for Censorship Reasons in the First Edition*, *Reserve Days of the First Edition*, the variants of the Preface, *Korney Vasiliev*, *Pascal*, *What For?* and *The Divine and the Human*, and the *Unfinished Popular Version*.
- Translated fresh (no website text exists); where a passage coincides with the calendar or a finished story, the reviewed R003 English is reused and changed only where the Russian differs. Variant files keep the edition's apparatus (deletions `~~…~~`, footnotes, editorial labels).
- Records: manifest, path migration, coverage and `source_suspected` records; `R003.md` (R003.13), `R003_BRIEF.md` (appendix section); review queue updated (14 more print checks, appendix conventions and names).
- Removed the outdated repository copy of `tolstoy_verifiable_translation_page_spec.md` (Andrei's approval; the current spec lives with the website, an archived copy is in `__workshop/archive/`).
- Validators: 0 errors.

## 2026-10-25 — R004.01: *Two Old Men* (audit and retranslation)

- Source: `corpus/works/v25_082_099_Dva_starika.md` (vol. 25, pp. 82–99, 1885), SHA-256 `ab0e08d0…5d3b2a`.
- English: `translations/works/v25_082_099_Two_Old_Men.md`; Romanian companion in `tolstoy-romanian-translation` (`v25_082_099_Doi_batrani.md`).
- Method: the website English and Romanian were aligned with the 151 Russian paragraphs, used as first drafts, and checked and revised paragraph by paragraph (R003 method); then English edit, a fresh-session audit of each language, and mechanical validation. 18/18 page markers; coverage PASS; validators 0 errors.
- Fourteen hard defects in the old website text were corrected (among them «Нема чого й взяти», the dream in ch. VI, "the Lord accepted his [labors]" for «его-то принял Господь», and the last sentence's «оброк» as "duty" instead of "vow"). Report: `project/qa/reports/R004_TWO_OLD_MEN_AUDIT.md`; batch file `project/qa/batches/R004.md`.
- Website: `two-old-men/index.html` and `two-old-men/romanian.html` rewritten from the reviewed text (backups in `__workshop/two-old-men/`); Romanian dictionary and pronunciation caches rebuilt. Files to upload by FTP: `two-old-men/index.html`, `two-old-men/romanian.html`, `assets/data/romanian-story/two-old-men.js`, `assets/data/romanian-story/pronunciation/two-old-men.js`.
- Print checks pending (non-blocking): see `project/qa/source_suspected/v25_082_099_Dva_starika.json`.
- The P-batch NEXT ACTION above is unchanged.

## 2026-10-26 — R004.02: *The Forged Coupon* (audit and retranslation)

- Source: `corpus/works/v36_005_053_Falshivyj_kupon.md` (vol. 36, pp. 5–53, 1880/1904), SHA-256 `bd85c3ff…ec4835`.
- English: `translations/works/v36_005_053_The_Forged_Coupon.md`; Romanian companion in `tolstoy-romanian-translation` (`v36_005_053_Cuponul_fals.md`).
- Method: the website English and Romanian were aligned with the 565 Russian paragraphs (through the site's parallel edition), used as first drafts, and revised chapter by chapter against the Russian; terms harmonized; then a fresh-session audit of each language and mechanical validation. 49/49 page markers; footnotes [^1]–[^4] (the edition's translations of Tolstoy's French) translated; coverage PASS; validators 0 errors.
- Report: `project/qa/reports/R004_FORGED_COUPON_AUDIT.md`; batch file `project/qa/batches/R004.md`. Choices for Andrei are listed in the report (Gypsy/Roma, speaker labels, Romanian «casa poporului»).
- Website: `forged-coupon/index.html` (reading text and parallel English) and `forged-coupon/romanian.html` rewritten from the reviewed text (backups in `__workshop/forged-coupon/`).
- The P-batch NEXT ACTION above is unchanged.
