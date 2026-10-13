<!-- Working brief used for R003.02–03 (February–March 2026-10-13). Paths refer to the temporary workspace where the drafts were prepared. -->

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

## Before you finish

- Run `python3 check.py` on all your files; all must pass with no unexplained warnings.
- Re-read each finished file once against the Russian, block by block, specifically hunting for: dropped clauses, added words, wrong negation, number/name errors, singular "they", British spellings, quotes pasted from a familiar Bible translation.
- Reply with: the list of files written, the count of blocks where you substantially revised the site draft vs kept it, every `flags` entry, and any convention question you were unsure about (with the choice you made).
