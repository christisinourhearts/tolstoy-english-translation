<!-- Working brief for R003 translator passes (final, through R003.12, 2026-10-20). Paths refer to the temporary workspace where drafts were prepared. -->

# Brief: translating Tolstoy's *Circle of Reading* (Круг чтения), batch R003

You are translating files of Tolstoy's *Circle of Reading* (1906, vol. 41 of the 90-volume edition) from the audited Russian into English, for a scholarly translation repository. The result must be faithful, plain, contemporary English, checked block by block against the Russian. The bar is high: this text is published and audited.

## Inputs (all under /home/claude/r003)

- `r003_work/drafts/<name>.json` — one file per Russian source file: `rp` (source path), `title_ru`, `subtitle_ru`, and `blocks`: a list in source order. Each block has `i`, `kind`, `ru` (the exact Russian Markdown block), and either `en` (for structural blocks: page marker, date, section number, separator — copy these exactly) or `site_draft` (an existing English website translation of that block, or `null` if none exists).
- `r003_work/jan_examples/` — finished January files in the target style (`*_Circle_of_Reading*.md`), and two of their Russian sources (`*_Krug_chtenija_*.md`) to compare side by side. **Read at least `v41_071_072_Circle_of_Reading.md` against `v41_071_072_Krug_chtenija_daily_jan_5_2.md`, and skim `v41_052_053_Circle_of_Reading_January.md` and `v41_022_025_Circle_of_Reading_January.md` before starting.**
- `r003_work/ref/TRANSLATION.md` (the constitution: read §§4–7), `DECISIONS.md` (D0001–D0005), `TERMINOLOGY.md`, `NAMES.md`.
- `check.py` — run `python3 check.py <name> [<name> ...]` after writing each output. Fix every ERROR. Look at every warning and fix it unless it is deliberate.

## Output

For each assigned file write `/home/claude/r003/out/<name>.json` (same `<name>` as the draft file):

```json
{
  "rp": "<copy of rp>",
  "subtitle_en": "1 February",
  "note": "One to three sentences for the translation_note front-matter field: the decisions a reader of the English would want to know (key terms, names, attributions, anything restored that the website draft had dropped). Every Russian word in the note gets transliteration and meaning: «дух» (dukh, 'spirit').",
  "flags": [],
  "blocks": ["<English for block 0>", "<English for block 1>", "..."]
}
```

- `blocks` has **exactly** one string per Russian block, in order.
- `subtitle_en`: daily files → the date ("1 February"); weekly readings → English of `subtitle_ru` with the title and authorship, e.g. «Будда. Изложил Л.Н.Толстой» → "The Buddha. Retold by L. N. Tolstoy"; «Разум.I. А. Шопенгауэра. II. Ф. А. Страхова» → "Reason. I. By A. Schopenhauer. II. By F. A. Strakhov"; «Молитва. Льва Толстого» → "Prayer. By Leo Tolstoy". Use the English title the body uses for its heading.
- `flags`: list any passage where the Russian itself looks damaged (OCR/transcription error, not mere difficulty), as `"[i] description"`. Do not repair the Russian silently; translate what is there and flag it. Empty list if none.

## Method — for every text block

1. Read the Russian first. Then read `site_draft`.
2. The site draft is only a first draft. It often paraphrases, smooths, modernizes, drops words, adds glosses, uses "their" for Tolstoy's generic "his", or merges/splits sentences. Revise it until every Russian word and clause is accounted for and nothing is added. If it is already accurate and natural, keep it — do not churn wording for its own sake.
3. If `site_draft` is `null`, translate fresh from the Russian.
4. Reproduce the block's Markdown shape exactly (`check.py` enforces this):
   - Same number of lines. Russian `> ` quote lines stay `> ` lines; the blank quote line `>` stays `>`.
   - Page markers (`<!-- vol. 41, p. 76 -->`) stay at the same position in the sentence (move them only to the nearest equivalent word boundary).
   - Italics: Tolstoy's italics matter. When a Russian line is italic, the English line is italic. When the Russian italics are chopped into segments around punctuation (`*А*, *Б*. *В*`), you may italicize the whole English span as one: `*A, B. C*`. Partial italics inside a sentence stay on the corresponding English words.
   - Headings (`#`), numbers, separators unchanged.

## Style rules (from the constitution and decisions)

- Conservative fidelity (D0001): keep Tolstoy's concrete words, images, repetitions, sentence breaks, and plainness. Ordinary Russian → ordinary English. Do not intensify, soften, explain, or elevate. Long sentences may stay long. No archaism (no "thee/thou", "whilst", "thereupon") except in literal Church Slavonic quotations.
- Generic человек: "a person" / "man" as context requires, with Tolstoy's generic **he/his/him** (not "they/their" for a singular). люди = "people".
- American spelling (honor, labor, neighbor, realize, gray, center, toward, judgment). Serial comma.
- Punctuation: curly double quotes “ ”; straight apostrophe ' (people's, don't); em dash — with no spaces in running text. The Russian dialogue dash at the start of a speech line is kept as "— " exactly as in the January *Thief's Son* example.
- Abbreviations: т. е. = "that is,"; и т. д. = "and so on"; т. п. = "and the like".
- Numbers: keep digits where Tolstoy has digits.
- Terminology (`TERMINOLOGY.md`): совершенствование = "perfecting", самосовершенствование = "self-perfection", совершенство = "perfection"; личность = "personality", личная жизнь = "personal life"; разумение = "understanding"; благо = "the good"; царство Божие = "kingdom of God", царство небесное = "kingdom of heaven"; соблазн = "temptation"; сын человеческий = "son of man". разум = "reason"; дух = "spirit"; душа = "soul"; совесть = "conscience"; насилие = "violence"; зло = "evil"; добро = "good"; истина = "truth" (правда usually also "truth"; "right"/"justice" only where context demands).
- Gospel and Bible quotations (D0002): translate Tolstoy's Russian wording directly — never paste a KJV/NRSV verse. Follow the source's capitalization: отец → "father", сын → "son" when lowercase in Russian. "God" is capitalized in English. Pronouns for God/Christ follow the Russian (lowercase).
- Bible references: modern English book names and arabic numerals, with a final period: «*Мф. гл. 23, ст. 8—10.*» → `*Matthew 23:8–10.*`; «Лк.» Luke, «Мк.» Mark, «Ин.» John, «1 Ин.» 1 John, «Рим.» Romans, «1 Кор.» 1 Corinthians, «Иак.» James, etc. Use an en dash in verse ranges.
- Attributions (D0004/E1 and the book-wide rules): print what Tolstoy printed, translated. Surname only if he gives a surname only ("Carlyle.", "Laveleye."), never expanded from the website draft ("Thomas Carlyle" → "Carlyle." if the Russian is «Карлейль.»). «По Марку Аврелию.» → "After Marcus Aurelius." (По X = "After X."). «Из «Талмуда».» / «Из …» → "From the Talmud." / "From “…”." (titles of works in quotes as printed). Keep the attribution's italics and quote prefix as in the Russian line.
- Names: established English forms for well-known persons (Marcus Aurelius, Seneca, Epictetus, Confucius, Laozi, Lamennais, Pascal, Kant, Schopenhauer, Rousseau, Channing, Emerson, Thoreau, Ruskin, Carlyle, Amiel, Montaigne, La Bruyère, Henry George, the Talmud, the Dhammapada, the Brahmana, the Vedas, the Upanishads). Russian names per D0003 (ё → yo, initial Е → Ye). Check `NAMES.md`.
- Tolstoy's own unattributed thoughts (no attribution line) stay unattributed.

## Conventions settled in earlier batches (apply them)

- Names: «Иосиф Мадзини» = "Giuseppe Mazzini", «Мадзини» = "Mazzini"; «магометане» = "Muslims", «магометанский» = "Muslim"; «Магомет» = "Muhammad"; «Лао-Тсе» = "Laozi"; «Талмуд.» = "*The Talmud.*"; «Дхаммапада» = "Dhammapada" (no article); labels like «Китайская мудрость.» = "*Chinese wisdom.*" (no article).
- More names/terms: «Люси Малори» = "Lucy Mallory"; «Коран» = "*The Quran.*"; «Бука» = "Buka"; «Карлейл(ь)» = "Carlyle"; «Рёскин» = "Ruskin". «господь» meaning God = "Lord" (capitalized, like "God"; "the Lord Sabaoth", "call Christ Lord"); pronouns for God/Christ stay lowercase.
- «воспитание» = "upbringing" where it is set against «образование» ("education"); «разум» = "reason", «ум» = "mind", «разумение» = "understanding".
- Psalms: give the English numbering (Synodal Ps. 89 = Psalm 90) and say so in the note.
- A period after a quoted title goes inside the quotes: `*From “Pious Thoughts.”*`.
- Nested quotation inside “ ” uses curly single quotes ‘ ’ (the checker's warning for this is acceptable).
- Dialogue: a speech line starts with "— "; the dashes around "said X" keep spaces ("— Well, — said Korney, — come on."), as in the January *Thief's Son*. Dashes in running narration are unspaced em dashes.
- An attribution printed without a final period stays without one.
- One-letter or obvious transcription slips (a missing/extra letter, a stray comma or asterisks): translate the evident sense and record the slip in `flags`.
- Wrong Bible reference (the quoted text is plainly from a different chapter/verse/book): give the **correct** reference in the English, and record the printed one in `flags` and in the `note` (e.g. "the source prints «Лк. гл. 26, ст. 18»; the text is Luke 16:18"). Verify against the Russian Synodal text, which you know well; if unsure, keep the printed reference and flag it.
- A wrong Bible reference inside Tolstoy's own sentence (not a reference line) stays as printed; explain it in the note and flag it.
- Anything else that may be a real print problem (missing section number, misplaced attribution): translate as printed and flag it.
- Use your own scratch subfolder (e.g. `/home/claude/r003/work_<yourfirstfile>/`) for helper scripts; other translators work in parallel in the same tree.

## Before you finish

- Run `python3 check.py` on all your files; all must pass with no unexplained warnings.
- Re-read each finished file once against the Russian, block by block, specifically hunting for: dropped clauses, added words, wrong negation, number/name errors, singular "they", British spellings, quotes pasted from a familiar Bible translation.
- Reply with: the list of files written, the count of blocks where you substantially revised the site draft vs kept it, every `flags` entry, and any convention question you were unsure about (with the choice you made).

## Appendices (R003.13)

Read `BRIEF.md` first; everything there still applies. These files are not calendar days. They are the Jubilee edition's appendices to *Circle of Reading*:

| file | content | `subtitle_en` |
|---|---|---|
| `v42_397_422_..._Mesjachnye_chtenija` | "Monthly readings": one long reading per month (some only cross-references) | `Monthly Readings` |
| `v42_423_438_..._Mysli_vypuschennye_...` | Thoughts the publisher left out of the first edition for censorship reasons, by date | `Thoughts Omitted by the Publisher for Censorship Reasons in the First Edition` (the file subtitle misprints «издеателем» for «издателем»: flag it) |
| `v42_439_469_..._Zapasnye_dni_...` | "Reserve days" of the first edition: numbered extra days with titles | `Reserve Days of the First Edition` |
| `v42_470_473_..._Varianty` | Variants (drafts) of the Preface | `Variants: Preface` |
| `v42_474_487_..._Varianty` | Variants of *Korney Vasiliev* | `Variants: Korney Vasiliev` |
| `v42_488_491_..._Varianty` | Variants of *Pascal* | `Variants: Pascal` |
| `v42_492_517_..._Varianty` | Variants of *What For?* | `Variants: What For?` |
| `v42_518_531_..._Varianty` | Variants of *The Divine and the Human* | `Variants: The Divine and the Human` |
| `v42_532_553_..._Nezakonchennoe_...` | The unfinished popular version of the book, by date | `Unfinished Popular Version` |

### Using earlier translations

- `site_draft` (when present) is the old website translation; treat it as in BRIEF.md.
- **`calendar_match`** (when present) is better: it is the finished, reviewed R003 translation of a closely matching Russian block elsewhere in the book (`ru` = that block's Russian, `en` = its English, `coverage` = share of your block's word triples found there). Where the Russian is identical, reuse that English word for word. Where the Russian differs (a draft wording, a variant), start from that English and change exactly what the Russian changes. This keeps the variants and the finished texts visibly comparable.
- For the variants, the finished English stories are in `r003_work/prior/` (out-format JSON; the Russian is in `r003_work/drafts/<same name>.json`): Korney Vasiliev, Pascal, What For?, The Divine and the Human. The finished Preface is `r003_work/ref/preface_en.md`. **Read the relevant one before starting** and use its names, forms of address, place names, and recurring phrases (e.g. Korney, Kuzma, Marfa, Agasha, Yevstigney; Józef Migurski, Albina, Rosołowski; Svetlogub, Mezhenetsky; check each name there).

### Variant markup (keep it exactly)

- Headings like `## \* № 1 (рук. № 1).` → `## \* No. 1 (MS. No. 1).`; `(рук. № 2, к гл. XII)` → `(MS. No. 2, to ch. XII)`; `(рук. № 1, гл. I)` → `(MS. No. 1, ch. I)`. Keep the `\*` (it marks a text first published in this edition).
- Footnote markers `[^n]` stay at the same place in the sentence (nearest equivalent word). Footnote definitions `[^n]: …` stay one per line, same numbers, same order.
- `~~…~~` is text Tolstoy deleted: translate it, keeping the `~~` around the corresponding English.
- Editorial labels (italic in the Russian, keep italic in English), use these consistently:
  - *Зач.:* / *Зачеркнуто:* → *Deleted:*; *далее зачеркнуто:* → *further deleted:*
  - *Переделано из:* → *Altered from:*
  - *Написано:* → *Written:*; *Описка вместо:* → *Slip of the pen for:*
  - *В подлиннике:* → *In the original:*
  - *Было:* → *Originally:*; *Вписано:* → *Inserted:*; *Над строкой:* → *Above the line:*; *Абзац редактора.* → *Paragraph break by the editor.* (for any other label, translate it plainly and list it in your reply)
- A note that quotes a single Russian word that the translation cannot show as a separate word (e.g. *Написано:* спеть, where the point is a spelling or grammatical slip) may give the English sense followed by the Russian in brackets: `*Written:* sing [спеть]`. Cyrillic is allowed there only; the checker's Cyrillic warning is then deliberate.
- Dates like `*1904. 28 августа.*` → `*1904. 28 August.*`.

### Other notes

- Cross-references: «См. Ламенэ, 20 декабря, 4 (стр. 360—361).» → "See Lamennais, 20 December, 4 (pp. 360–361)."; «См. т. 41, стр. 501—515.» → "See vol. 41, pp. 501–515."; «Недельное чтение после 27 октября» → "the weekly reading after 27 October".
- The long monthly readings (La Boétie, Škarvan, Bondarev, etc.) are fresh translations: same constitution, same care. Names: «Боэти» = La Boétie; «А. Шкарван» = A. Škarvan (Albert Škarvan, the Slovak doctor; print what the Russian prints); «Т. Бондарев» = T. Bondarev (Timofei Bondarev); «Петр Ольховик» = Pyotr Olkhovik.
- Attributions in these files follow the calendar conventions in BRIEF.md (surname only if printed so, etc.). Bible references in Roman numerals («Мф. VI, 19—21.») → `Matthew 6:19–21.` as usual.
- If a block is a draft of a thought that appears in the calendar but with different wording, translate the draft's wording (not the final one).
