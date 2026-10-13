# *Circle of Reading* reconciliation — 13 October 2026

Decision D0005 requires one basic translation of *Krug chteniya* (Круг чтения, "Circle of Reading"). Until now there were two English texts of the same passages:

- the 31 files in `translations/circle_of_reading/`, which went through the gauntlet, D0001, and cold audits;
- the website's Calendar data, which had one full review on 3 October 2026 and an independent sample review on 13 October 2026.

This report records how the two were merged into one text.

## Method

1. Each repository file was aligned with its audited Russian file, block by block. Each Russian block was then matched to the website unit with the same Russian text, after normalization.
2. Of 548 matched paragraph and attribution blocks, 330 differed in wording; differences only in quotation marks or dash spacing were ignored. The 330 differing blocks are 276 paragraphs and 54 short lines (attributions, references, headings).
3. Each differing block was judged Russian-first against both English versions, using the priority order (P1–P7), the Tolstoy rules (T1–T11), and the model-failure codes (E1–E14). The outcome was one of:
   - the repository wording;
   - the website wording;
   - a merged or corrected wording, when neither version was right on its own.

   Every entry records its reason.
4. The resulting text was written to both places: the website's data (with per-unit revision history, run `2026-10-13-circle-of-reading-reconciliation`) and these 31 files.

## Results

| Outcome | Blocks |
|---|---|
| Repository wording kept | 236 |
| Website wording adopted | 23 |
| Merged or corrected | 71 |

- **Repository blocks changed:** 70, in 23 files.
- **Website units changed:** 436. That includes the book-wide attribution rules below, which apply beyond these 31 files.
- **After the merge:** no wording differences remain between the two texts for these passages.

### Typical reasons

- **Repository better:** conservative fidelity (D0001's own examples, such as "the whole world of people" and the January 2 opening). Also restored modality and particles: "unless", "only", "also", "surely". Correct terms: "infants", "Christian teaching", "dodder", "recruiting office", "higher".
- **Website better:** the self-perfection decision; "will not have time" (не успеете, *ne uspeete*); "Fear" (Бойтесь, *Boytes'*); "the sun" rather than "sunlight".
- **Neither alone:** restored doublings ("greater and greater", "more and more"); distinct verbs that one version had merged ("destroy" and "ruin"; "peace" and "calm"); "spiteful" for злой (*zloy*); "American Indians" for индейцы (*indeytsy*).
- **Structure:** four places where the repository had joined two Russian paragraphs into one were split again (P3).

### Book-wide attribution rules (website)

- По X (*Po X*) is rendered "After X." (77 + 10 lines).
- Из «…» (*Iz «…»*) is rendered "From “….”" (30 lines).
- Ламенэ (*Lamene*) is rendered "Lamennais" (23 lines).
- Biblical references use the modern English form ("Matthew 20:25–28"). Where Psalm numbering differs, the Russian number comes first and the English Bible number follows in brackets.

## Not yet done

- **Emphasis:** the Russian italics, marking Tolstoy's own thoughts, survive in the repository but not in the website data. The website should carry this emphasis too.
- **Quotation marks:** typographic differences were left as they are.

The per-block ledger, with the Russian, both earlier English versions, the final text, and the reason, is in `CIRCLE_OF_READING_RECONCILIATION_2026-10-13.json`.
