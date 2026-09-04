# Russian Source Stress Test

Date: 2026-08-31

## Purpose

This test asks a different question from the repository's existing deep audit.
The existing audit establishes that the Tolstoy Digital TEI was converted into
Markdown without meaningful loss. This stress test asks whether there is reason
to suspect that the *upstream digital Russian itself* is broadly damaged or
unreliable relative to the 90-volume printed edition.

The result is encouraging: **no substantive source corruption was found in the
sample.** This is evidence of high corpus reliability, not a claim that every
character in more than 46,000 printed pages has been independently re-proofread.

## Existing evidence inside the Russian repository

The Russian release already contains an unusually strong TEI-to-Markdown audit.
Its release metadata reports:

- 16,573 generated documents checked;
- 10,721,002 main-body source words checked;
- 0 main-body failures;
- 59,205 footnotes preserved, with 0 footnote-content failures;
- 51,162 source page breaks and 51,162 Markdown page markers;
- 17,812 direct editorial notes separately audited;
- normalized/corrected TEI readings selected independently by the auditor.

The audit records one harmless upstream XML anomaly: a stray literal Latin `s`
after a complete editorial-note paragraph in
`texts/letters/v69_161_V_I_ObedkovuiI_I_Ponomarevu.xml`. The meaningful note is
preserved and the orphan character is not emitted. It also records one figure
note represented as figure text rather than a footnote; its wording is retained.

This establishes the **TEI -> Markdown** link very strongly. It does not, by
itself, prove the original **printed edition -> digital transcription** link.

## External provenance check

The official Tolstoy 90-volume site states that all 90 printed volumes were
scanned in cooperation with Yasnaya Polyana and the Russian State Library. More
than 46,000 pages were then recognized, and more than 3,000 volunteers corrected
OCR errors through three proofreading stages before the electronic volumes were
published. The site also states that the printed edition's orthography and
punctuation are preserved in that electronic edition.

Primary reference:
https://tolstoy.ru/online/90/58/

This is strong provenance, though provenance alone cannot rule out surviving
transcription errors.

## Stratified corpus spot-check

A passage was sampled from each of 31 volumes distributed across the complete
set:

`1, 5, 9, 13, 18, 21, 25, 29, 33, 37, 41, 45, 46, 48, 50, 52, 54, 56, 58, 59, 62, 65, 68, 71, 74, 77, 80, 83, 86, 89, 90`

The samples deliberately crossed different textual conditions rather than only
checking polished fiction. They included:

- finished literary prose;
- draft and variant material;
- *Azbuka* / children's prose;
- *Krug chteniya* material;
- diaries and notebooks;
- correspondence;
- old orthography;
- editorial bracket completions;
- French and German passages;
- Tolstoy-authored English containing his own spelling and grammar mistakes.

For all 31 sampled volumes, the local Markdown passage could be reconciled with
the corresponding published 90-volume text. **No omission, inserted sentence,
semantic substitution, truncation, or displaced passage was found.**

### Apparent discrepancies investigated

Three cases initially looked suspicious and were deliberately chased down.

**Volume 33 — `Канцелярия комисии прошений`.** The modernized Markdown search
string did not initially appear in the official page. Opening the actual passage
showed the printed old-orthography reading `Канцелярія комисіи прошеній`, at the
expected location in the "Записи и вопросы, относящиеся к «Воскресению»"
section. This is an expected normalization difference, not corruption.

**Volume 48 — editorial square brackets.** An apparent loss of brackets in a
sample was traced to the temporary sampling helper used for search: it stripped
Markdown punctuation, including `[` and `]`, before searching. The repository
itself retains the bracketed editorial completion. This was a test-harness issue,
not a corpus issue.

**Volume 58 — `арелигиозным развращением людей`.** An initial web index lookup
failed to find the unusual word `арелигиозным`. Opening/searching the correct
volume showed the exact old-orthography phrase
`арелигіознымъ развращеніемъ людей` on printed pp. 47–48. A separately hosted
PDF of volume 58 also exposes the same wording. The unusual word is genuinely
in the edition; it is not a corrupted OCR token invented by the repository.

A fourth case, volume 54 (`слабо и гибко, как ребенок` in the Lao-Tzu passage),
was initially found in the wrong part of the site's commentary. A direct search
at the diary passage and a PDF-text check both confirmed the repository reading.

## PDF / alternate-witness checks

The online HTML comparison is useful but is not fully independent: Tolstoy
Digital and the official online 90-volume text are related descendants of the
same digitization project. To make the test harder, selected difficult passages
were also checked against PDF/text witnesses hosted separately or against other
independent textual repositories.

Confirmed examples include:

- Volume 13: rough note material located in a separately hosted `13-photo.pdf`;
- Volume 21: *Azbuka* passage `птицы поклевали все крошки хлеба` in the Wikimedia
  PDF of volume 21;
- Volume 37: Tolstoy's own English draft of *The Hostelry*, including deliberate
  forms such as `andsometime spoiled things aut of selfish spite`, in a PDF copy;
- Volume 54: the Lao-Tzu diary passage `слабо и гибко, как ребенок` in a PDF copy;
- Volume 58: `арелигіознымъ развращеніемъ людей` in the Wikimedia/PDF witness;
- Volume 59: early French correspondence, including `J'ai cru un tems...`, in a
  PDF copy of the volume;
- Volume 62: the letter beginning `Хороня Петю...` also agrees with the Russian
  Virtual Library text;
- Volume 80: the French passage naming `Rousseau, Pascal, Kant, Emerson,
  Channing` agrees with the official volume PDF and Wikimedia/Wikisource witness.

Where the web tooling exposed PDF text layers, the wording agreed. The tooling
could not reliably render the large-volume PDF page images as screenshots in
this session (large-file/cache failures), so this should **not** be described as
an exhaustive visual facsimile audit of the printed pages.

## What this test supports

The evidence now forms several layers:

1. The 90-volume edition has a documented scan/OCR/proofreading history involving
   the Russian State Library, Tolstoy institutions, ABBYY, and three correction
   stages.
2. A 31-volume stratified spot-check found no substantive mismatch between the
   local corpus and the published 90-volume text.
3. Difficult passages in several volumes also agree with separately hosted PDF
   or independent text witnesses.
4. The repository's own exhaustive audit strongly verifies TEI-to-Markdown
   completeness, including notes and page boundaries.

Taken together, this gives **high confidence that the Russian repository is a
sound translation base and is not systemically broken.**

It does not prove that no isolated upstream typo or scholarly misreading survives
anywhere in the 90 volumes. At this corpus size, occasional source-level errors
should be assumed possible.

## Recommended production rule

Do not delay translation for a page-by-page re-proofreading of all 90 volumes.
Instead add a source-suspicion gate to the translation workflow.

A unit should be marked `SOURCE_SUSPECTED` when the Russian contains a reading
that is unexpectedly ungrammatical, semantically incoherent, internally
contradictory, anomalous in a name/number/date, or otherwise looks more like
transcription damage than Tolstoy's deliberate roughness.

When that occurs:

1. stop translation of the affected passage;
2. identify the volume and printed page from the preserved page marker;
3. compare the 90-volume page and, where useful, another witness;
4. record the result in a source-errata ledger;
5. never silently "repair" the authoritative Russian repository;
6. if a source error is confirmed, record both the digital reading and verified
   printed reading, and state which reading the English translation follows.

This gives a better balance than either blind trust or re-proofreading 46,000+
pages before translation can begin.

## Current disposition

**PASS for proceeding to the next translation pilot, with a source-suspicion
protocol added before large-scale production.**

No confirmed substantive erratum was discovered by this stress test, so no
`source_errata.yml` entry is required yet.
