# PD-core pilot audit — volume 48, pp. 342–346

## Evidence chain

**Primary visual authority for this pilot:** page images from the scanned 1952 volume 48, PDF pages 372–376 (printed pages 342–346).

**Comparison witness only:** `tolstoy-russian-md-audited/corpus/notes/v48_342_346_Zapisi_No_2_i_3_1870.md`, SHA-256 `8849c8a0052527371a65546811f55371febca50bc494bce2bf17e298ffb3331f`.

**English preservation test:** accepted English file SHA-256 `03926dcbc45bb7695597383c28dd3eb7c96502ea5dc9faf80ff5e3d171c70ae6`.

## Page-by-page findings

| Printed page | PDF page | Scan-visible issue | Existing Russian Markdown | Pilot treatment |
| --- | ---: | --- | --- | --- |
| 342 | 372 | `Андр[ей]` is printed with an editorial bracket completion | `Андрей` | preserve `Андр[ей]` |
| 343 | 373 | six manuscript variants/deletions are exposed in footnotes; one is printed `ули[цу]` | variants retained, but `ули[цу]` becomes `улицу` and Soviet note labels disappear into Markdown strikeout | retain the Tolstoy readings; use project-neutral labels; preserve `ули[цу]` |
| 344 | 374 | `драм[а]` plus deleted `известном` and `немыслима` are apparatus readings | retained | retained with neutral factual labels |
| 345 | 375 | `на[до]`, `кот[орого]`, and deleted `сатирич[еского]` are visibly bracketed | main text silently normalized to `надо`, `которого`; deleted form normalized to `сатирического` | preserve printed brackets |
| 346 | 376 | `пролетар[иата]` is visibly bracketed; a pencil marginal note is reported in the footnote | main text silently normalized to `пролетариата`; marginal note retained with translated Soviet descriptive sentence | preserve bracket completion; independently label it “Pencil note in the left margin” |

## What is Tolstoy and what is editorial here?

The main sentences, crossed-out manuscript words, and marginal pencil words are attributable to Tolstoy. The edition supplies other layers: section organization, transcription choices, bracketed completions, footnote numbering, and prose descriptions such as “Зачеркнуто” or “На полях этого абзаца...”.

For the pilot, the new file treats those layers differently:

- Tolstoy-authored wording is retained.
- A visibly supplied completion remains visibly supplied (`[ ]`).
- The edition's prose apparatus labels are not copied; their factual function is restated in new project language.
- Bibliographic/page facts are recorded as provenance metadata.
- Tolstoy Digital's TEI path, license field, and normalization metadata are not used as the new file's authority.

## English rebase test

The existing reviewed English file and the pilot English file were compared mechanically after removing:

- YAML metadata;
- page comments;
- footnote markers;
- the final apparatus/notes section;
- insignificant whitespace differences.

**Result: exact normalized match.** No substantive English sentence changed.

The rebased copy changes provenance metadata, restores the scan's page break between pp. 345–346, and rewrites apparatus labels in independent factual language. The translation of Tolstoy's body remains untouched.

## Risk revealed by the pilot

The old Russian Markdown is safe enough to be an extremely useful witness, but it is not suitable to become a public-domain master merely by removing its license line. Its `reg` conversion can silently collapse editorial brackets and other source distinctions.

For ordinary published prose, most revalidation should be straightforward. Diaries, notebooks, drafts, variants, and manuscript-heavy material deserve a stricter scan-aware path because scholarly reconstruction is more frequent there.

## Recommended next experiment

Before scaling to all 15,766 Tolstoy-source records, run a second pilot on a **published literary work** rather than manuscript notes. That will tell us whether the expensive scan-aware handling can be concentrated on manuscript/apparatus-heavy categories while ordinary published works migrate more mechanically.
