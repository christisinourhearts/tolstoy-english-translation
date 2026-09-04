# P002 Post-Batch Review

## Result

P002 is complete. Twenty-five short units were translated, edited, rechecked against the source, mechanically validated, given structured bilingual coverage records, and committed as individual Git checkpoints.

Approximate source-body volume: **3,466 words**.

Category mix:

- 3 works — 579 words
- 5 letters — 626 words
- 4 diary entries — 469 words
- 2 notebook/note files — 227 words
- 8 *New Azbuka* texts — 686 words
- 3 *Krug chteniya* sections — 879 words

Postflight state:

- P002 accepted units: **25 / 25**
- P002 structured coverage records: **25 PASS**
- English corpus reviewed translations after P002: **32**
- Mechanical validation: **0 errors**
- Source snapshot: **15,766 checked; 0 missing; 0 changed by hash**
- Confirmed source-QA errata: **2**

## What the batch discovered

### 1. A valid file and hash do not guarantee a complete textual segment

Two initially selected *New Azbuka* files ended in the middle of ordinary sentences. Checking volume 21 confirmed that the stories continue on the next printed page even though the individual Markdown records stop at the page boundary. They were quarantined rather than translated:

- `corpus/azbuka/v21_056_056_Myshka_vyshla_guljat.md`
- `corpus/azbuka/v21_059_059_Odin_tsar_stroil.md`

This is the most important P002 finding. The Russian corpus remains a strong translation source, but small-file segmentation needs a boundary sanity check. Both cases are recorded in `metadata/source_errata.yml` and `qa/source_suspected/`.

### 2. Foreign-language letters require body-language detection independent of YAML

`v59_024_T_A_Ergolskoj.md` is catalogued as Russian at the file level, but Tolstoy's letter body is French and the Russian material is editorial apparatus. The English translation therefore records French as the body source language and Russian separately as apparatus.

### 3. Physical manuscript damage must remain visible

`v59_035_Gr_S_N_Tolstomu.md` survives on a torn sheet. The English preserves incomplete words and lines rather than guessing the missing text. A smooth reconstructed letter would be less faithful than a visibly broken translation.

### 4. Editorial mistakes should not be silently corrected

During P002 an editorial note containing the printed year `849` was initially normalized to `1849`. The fidelity pass checked the edition and restored `849` in the English apparatus because the corpus is translating the source actually present, not silently emending it. Where a correction is genuinely required, it should be explicit and traceable.

### 5. Rough notebooks should remain rough

The diary and notebook material confirmed that contemporary English does not mean polishing fragments into essays. Illegible spans, unfinished syntax, lists, and abrupt transitions remain visible where they belong to the source state.

### 6. Child-reader prose benefits from restraint

The *New Azbuka* texts translated cleanly when ordinary short English words and simple syntax were preferred. The process must resist adding explanatory morals, modernizing details, or importing familiar versions of stories such as *Little Red Riding Hood*.

### 7. Russian wordplay sometimes has no honest one-to-one English solution

`The Blind Man and the Deaf Man` depends partly on Russian sound-confusions. The English preserves the literal meanings and the mistaken responses, and the coverage record documents the lost sound relationship. Inventing a different English pun would make the result more entertaining but less textually accountable.

### 8. *Krug chteniya* needs a compilation rule

Attributed passages in *Krug chteniya* should be translated from Tolstoy's compiled Russian wording. Restoring a famous English Bible translation, an English-language original, or another standard edition could erase Tolstoy's selection, shortening, translation, or adaptation. External originals are useful for interpretation and attribution, not as silent replacements for the Russian source object.

## What changed in the constitution after P002

`TRANSLATION.md` now explicitly adds:

1. a segmentation/boundary sanity check for small corpus files;
2. a rule that Tolstoy's compiled wording in *Krug chteniya* is the translation source;
3. a rule for untranslatable wordplay: preserve semantic action and record the loss rather than inventing a new joke.

The earlier P002 additions remain in force: formal `SOURCE_SUSPECTED` handling and structured bilingual coverage proofs.

## Remaining limitations

The structured coverage records make acceptance much more auditable, but they do not by themselves constitute an independent second translator. P002's semantic fidelity passes were performed during the same working run that produced the translations. Periodic cold audits in a fresh context remain desirable, especially before publication or after large production runs.

The source-integrity stress test and P002 together also show that source QA should remain continuous. The corpus should not be globally distrusted because two segmented files were incomplete, but neither should a clean repository-level audit be treated as proof that every independently segmented item is complete.

## Recommended scale after P002

The 25-unit batch was operationally safe. For short materials, the next production batch can reasonably increase to about **50 units**, preferably capped by total source volume (roughly 7,000–10,000 words) rather than file count alone.

Before or alongside P003, add an automated preflight that flags candidate source files whose body appears to begin or end mid-sentence or whose page-boundary segmentation looks suspicious. Such a detector should only create review candidates; it must not declare corruption automatically.

Long works should continue to use smaller logical sections even when the repository retains a one-file final identity.

## Disposition

**P002: PASS.**

The process is ready for a larger short-text batch, with continuous source-suspicion checks and periodic independent/cold fidelity review.
