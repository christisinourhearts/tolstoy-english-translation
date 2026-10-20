# Verifiable Translation Page
## Design and Editorial Specification for Christ Is in Our Hearts

**Working title:** Verifiable Translation  
**Primary use case:** Leo Tolstoy editions published by Christ Is in Our Hearts  
**First candidate:** *The Death of Ivan Ilyich*  
**Format:** Public web page accompanying the printed and digital edition  
**Purpose:** Let any reader inspect how the translation was made, line by line, without requiring knowledge of Russian.

---

# 1. Core Principle

The page should make a simple promise:

> **You do not have to trust the translation blindly. You can inspect it.**

The aim is not to overwhelm the reader with machinery. The ordinary reader should be able to read a clear English text with almost no friction. A curious reader should be able to open progressively deeper layers until, if desired, they can inspect:

- the Russian source text;
- a literal word-by-word gloss;
- grammatical structure;
- lexical alternatives;
- idioms and cultural context;
- the published English translation;
- earlier translation drafts;
- audit comments;
- disputed passages;
- reasons for final choices;
- consistency notes across the whole work;
- source-edition information;
- the complete audit history.

The page should therefore operate on the principle of **progressive disclosure**.

At the surface: a beautiful reading page.

Underneath: an unusually deep critical apparatus.

The reader should never be forced to see the machinery, but none of it should be hidden.

---

# 2. Editorial Philosophy

The project should not present machine assistance as a mark of authority.

It should present **verification** as the source of authority.

The page should therefore avoid claims such as:

- "AI-powered translation"
- "AI-enhanced Tolstoy"
- "the most accurate translation"
- "perfect translation"
- "definitive translation"

Instead, it should show the evidence that allows readers to make their own judgment.

Recommended editorial language:

> This edition was produced with the assistance of contemporary language models and repeatedly checked against Tolstoy's Russian text. The complete source, translation notes, and audit trail are published here so that readers can examine the decisions for themselves.

A shorter version may appear in the printed book:

> **About this translation**  
> The Russian source text, line-by-line notes, and full translation audit for this edition are freely available at christisinourhearts.com.

The page should embody a broader publishing principle:

> **Free text. Paid object. Open evidence.**

---

# 3. Primary User Types

The interface should work for several kinds of readers without forcing one experience on everyone.

### Casual reader

Wants to read Tolstoy in English.

Needs:

- clean typography;
- minimal interruption;
- occasional explanatory notes;
- simple access to the original when curious.

### Curious reader

Does not know Russian but wants to understand why a sentence was translated a certain way.

Needs:

- Russian line;
- literal gloss;
- explanation of key words;
- concise translation rationale.

### Russian-speaking reader

Can judge some or all of the translation independently.

Needs:

- exact Russian base text;
- source citation;
- paragraph alignment;
- variant readings where relevant;
- direct access to disputed passages.

### Translator / scholar

Wants the complete editorial record.

Needs:

- grammatical notes;
- lexical alternatives;
- recurring-term index;
- version history;
- audit results;
- unresolved uncertainties;
- textual-source details;
- machine-readable export.

---

# 4. Overall Page Structure

The page should be one continuous document with four conceptual levels.

## Level 0 — Orientation

At the top:

**THE DEATH OF IVAN ILYICH**

Verifiable Translation

Leo Tolstoy  
Translated and edited by Andrei Evanghelușcă

Then a very brief explanation:

> This page contains the complete English translation together with Tolstoy's Russian text and the editorial record behind the translation. Read normally, or open any passage to inspect how it was translated.

Below this:

- READ
- TRANSLATION NOTES
- AUDIT
- SOURCE
- ABOUT THIS EDITION

These should behave like section anchors rather than separate pages whenever possible.

The default state should be **READ**.

---

# 5. Reading View

The reading view should remain visually calm.

Each paragraph appears normally in English.

Example:

> Ivan Ilyich's life had been very simple, very ordinary, and very terrible.

Beside or beneath each paragraph is a small, quiet disclosure control.

Recommended:

`RUSSIAN + NOTES`

or simply:

`INSPECT`

Avoid icons that make the page feel like software documentation.

When the reader expands a paragraph, the analytical material appears directly beneath it.

The English reading text should not shift dramatically when details are opened.

---

# 6. Passage Inspection Panel

Every independently auditable unit should have a stable ID.

Example:

`II-01-004`

Meaning:

- II = *Ivan Ilyich*
- 01 = chapter 1
- 004 = fourth aligned translation unit

Do not expose this prominently to casual readers, but show it in the detailed panel and URL fragment.

Example URL:

`/ivan-ilyich/verifiable#II-01-004`

This makes every sentence or paragraph independently linkable.

---

# 7. Default Expanded Passage

When a reader presses **INSPECT**, show only four things initially:

### ORIGINAL RUSSIAN

> Жизнь Ивана Ильича была самая простая и обыкновенная и самая ужасная.

### PUBLISHED TRANSLATION

> Ivan Ilyich's life had been very simple, very ordinary, and very terrible.

### LITERAL STRUCTURE

> The life of Ivan Ilyich was the most simple and ordinary and the most terrible.

### NOTE

> Tolstoy repeats the superlative structure — *самая ... самая* — joining the extreme ordinariness of the life to its horror. The English preserves the repetition rather than smoothing it away.

Then show:

`MORE DETAIL`

This second disclosure opens the full audit apparatus.

The point is that even the analytical layer should have progressive disclosure.

---

# 8. Full Audit Apparatus

When **MORE DETAIL** is opened, show the following subsections.

## 8.1 Word-by-word analysis

A compact table:

| Russian | Lemma | Grammar | Basic sense | Note |
|---|---|---|---|---|
| Жизнь | жизнь | noun, fem., nom. sg. | life | grammatical subject |
| Ивана | Иван | proper noun, gen. sg. | Ivan's / of Ivan | dependent on "life" |
| Ильича | Ильич | patronymic, gen. sg. | Ilyich's | completes the name |
| была | быть | verb, past, fem. sg. | was | agrees with жизнь |
| самая | самый | superlative marker | most / very | repeated later |
| простая | простой | adjective, fem. nom. sg. | simple | modifies жизнь |
| и | и | conjunction | and | — |
| обыкновенная | обыкновенный | adjective | ordinary, commonplace | tonal choice discussed below |
| и | и | conjunction | and | — |
| самая | самый | superlative marker | most / very | deliberate repetition |
| ужасная | ужасный | adjective | terrible, dreadful | stronger than merely "bad" |

On phones, this should collapse into stacked word cards rather than a horizontal table.

---

# 9. Literal Rendering

Each unit should include a deliberately awkward literal rendering.

Its purpose is semantic transparency, not literary quality.

Label it explicitly:

**LITERAL — NOT THE PUBLISHED TRANSLATION**

Example:

> The life of Ivan Ilyich was the most simple and ordinary and the most terrible.

Never polish the literal rendering until it becomes a competing translation.

It should reveal:

- syntax;
- repetitions;
- word order where meaningful;
- grammatical dependencies;
- omitted subjects;
- implied meanings.

---

# 10. Translation Decision

Every passage that required judgment should contain a short explanation.

Recommended heading:

**WHY THIS WORDING**

The note should answer only material questions.

Good:

> *Обыкновенная* can mean ordinary, usual, commonplace, or conventional. "Ordinary" was chosen because the paragraph is describing the social normality of Ivan Ilyich's life rather than condemning it as dull.

Bad:

> We chose "ordinary" because it sounds best.

The explanation should distinguish between:

- semantic necessity;
- idiomatic English;
- rhythm;
- register;
- ambiguity;
- interpretive choice.

---

# 11. Confidence / Dispute Status

Each translation unit may carry an editorial status.

Do not express this as a numeric percentage.

Recommended statuses:

**CLEAR**  
No meaningful ambiguity affecting the English.

**CHOICE**  
Several plausible English renderings exist; the edition makes an editorial choice.

**DIFFICULT**  
The Russian permits materially different interpretations or contains unusual syntax, idiom, or textual uncertainty.

**TEXTUAL ISSUE**  
Different Russian editions or manuscripts contain a relevant variant.

These statuses should be quiet metadata, not warning graphics.

Example:

`STATUS: CHOICE`

A reader can filter the entire book to show only CHOICE, DIFFICULT, or TEXTUAL ISSUE passages.

---

# 12. Alternatives Considered

Only show alternatives where they matter.

Example:

**ALTERNATIVES CONSIDERED**

- commonplace
- ordinary
- conventional
- usual

Then explain why one was selected.

Do not automatically generate ten synonyms for every adjective. The feature should illuminate a decision, not advertise machine output.

---

# 13. Revision History

For important passages, show the translation's evolution.

Example:

**REVISION HISTORY**

**v1**
> Ivan Ilyich's life was the simplest and most ordinary and the most terrible.

**Semantic audit**
> Flagged the asymmetry created by "simplest" + "most ordinary."

**v2**
> Ivan Ilyich's life was very simple and ordinary, and very terrible.

**Style audit**
> Restored Tolstoy's repeated structure.

**Published**
> Ivan Ilyich's life had been very simple, very ordinary, and very terrible.

Only substantive revisions need to be shown.

Do not expose every punctuation tweak.

---

# 14. Audit Record

Each passage should store which audits it has passed.

Recommended audit taxonomy:

### S1 — Source Alignment
Russian text matched against the selected base edition.

### S2 — Semantic Fidelity
Meaning checked sentence by sentence.

### S3 — Omission Scan
Checked for lost words, clauses, sentences, repetitions, or modifiers.

### S4 — Addition Scan
Checked for ideas introduced in English but absent from the Russian.

### S5 — Grammar / Syntax
Cases, tense, aspect, subordination, participles, pronouns, and implied subjects checked.

### S6 — Lexical Consistency
Recurring Russian terms checked against their renderings elsewhere.

### S7 — Register / Tone
Social register, irony, simplicity, bureaucratic diction, religious vocabulary, and emotional intensity checked.

### S8 — Proper Names / References
Names, quotations, biblical references, institutions, titles, and historical references verified.

### S9 — English Readability
English revised for clarity and naturalness without knowingly altering semantic content.

### S10 — Cold Audit
Final Russian-to-English review performed without relying on previous rationales wherever practicable.

The passage panel may display:

`AUDIT: S1 S2 S3 S4 S5 S6 S7 S8 S9 S10`

But visually this should appear as understated checkmarks or a collapsed summary.

Clicking **VIEW AUDIT RECORD** reveals dates, notes, and changes.

---

# 15. Whole-Book Audit Dashboard

The AUDIT section should summarize the state of the entire edition.

Example:

## Audit status

**Complete text units:** 1,247  
**Source aligned:** 1,247 / 1,247  
**Semantic audit:** 1,247 / 1,247  
**Omission scan:** 1,247 / 1,247  
**Addition scan:** 1,247 / 1,247  
**Cold audit:** 1,247 / 1,247

**Units marked CHOICE:** 83  
**Units marked DIFFICULT:** 17  
**Textual issues:** 3  
**Open questions:** 0

Do not use a gamified progress ring.

Plain numbers are more credible.

If the translation is still being revised, show that honestly.

Example:

> This edition is under active review. Three passages remain unresolved.

---

# 16. Discrepancy Ledger

Include a public ledger of all meaningful issues discovered during auditing.

Example:

| Unit | Type | Issue | Resolution |
|---|---|---|---|
| II-03-041 | omission | adverb omitted in v1 | restored |
| II-04-017 | lexical | repeated term translated inconsistently | standardized |
| II-06-102 | syntax | subordinate clause initially attached incorrectly | corrected |
| II-09-033 | register | wording too formal | revised |

This is important.

The project should not merely publish evidence of success.

It should publish evidence that mistakes were found and corrected.

That makes the audit believable.

---

# 17. Recurring-Term Index

Tolstoy often builds meaning through recurring vocabulary.

Create an index showing important Russian words and every significant translation choice.

Example:

## жизнь — life

Occurrences: 74

Primary rendering:
- life

Other renderings:
- existence — 2
- living — 1

Notes:
> Translation varies only where English grammar requires it.

Other likely indexed terms:

- жизнь — life
- смерть — death
- правда — truth / rightness
- ложь — lie / falsity
- добро — good
- зло — evil
- любовь — love
- совесть — conscience
- страдание — suffering
- ужас — horror / terror
- должный / должен — ought / must
- настоящий — real / genuine / true

The exact list should be work-specific.

---

# 18. Search and Filters

Readers should be able to search:

- Russian word;
- Russian lemma;
- English word;
- unit ID;
- chapter;
- editorial note.

Filters:

- show only passages with notes;
- show only CHOICE;
- show only DIFFICULT;
- show only TEXTUAL ISSUE;
- show passages revised after publication;
- show passages with biblical / literary references.

A scholar should be able to type:

`обыкновенный`

and see every occurrence together with its English renderings.

---

# 19. Source Edition Section

The SOURCE section should state exactly what Russian text was used.

Include:

- edition title;
- editor;
- volume;
- publisher;
- city;
- year;
- page range if applicable;
- repository or archive;
- stable URL if available;
- date accessed;
- file checksum where a local source file was used.

Example structure:

## Russian base text

**L. N. Tolstoy, Complete Collected Works in 90 Volumes**  
Volume XXVI  
Moscow: State Publishing House, 1936

Digital source: [repository]

Downloaded: YYYY-MM-DD

SHA-256:

`xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

If a correction was made to an obvious OCR error, record it.

---

# 20. Textual Variants

Where different authoritative Russian editions differ, show the variants.

Example:

**TEXTUAL VARIANT**

Edition A:
> [Russian]

Edition B:
> [Russian]

Published translation follows:
> Edition A

Reason:
> [brief explanation]

Do not invent a critical apparatus where none is needed.

Use this only for genuine textual differences.

---

# 21. Translation Methodology

The methodology section should explain the workflow clearly without technological sales language.

Suggested structure:

## How this translation was made

1. A verified Russian base text was established.
2. A fresh English translation was produced with language-model assistance.
3. The English was aligned with the Russian in discrete audit units.
4. Each unit was checked for semantic accuracy.
5. Separate scans were performed for omissions and additions.
6. Difficult grammar and vocabulary were independently re-examined.
7. Recurring vocabulary was checked across the complete work.
8. The English underwent a style pass constrained by the Russian.
9. A final cold audit was conducted against the source.
10. Material corrections and disputed passages were recorded publicly.

Then state plainly:

> Language models were used as translation and analytical tools. Their output was not treated as authoritative. The Russian source text remained the controlling text throughout the editorial process.

This is a stronger statement than vague phrases such as "AI assisted."

---

# 22. Human Responsibility

Include a named-responsibility statement.

Recommended:

> **Editorial responsibility**  
> Andrei Evanghelușcă selected the published wording, established the editorial principles of the edition, reviewed disputed passages, and approved the final text.

Avoid implying that a machine bears responsibility for the edition.

---

# 23. Machine Assistance Disclosure

Keep this precise and calm.

Possible wording:

> **Use of language models**  
> Contemporary language models were used in producing and auditing this translation. They assisted with translation drafts, grammatical analysis, lexical comparison, consistency checks, and error detection. Because language-model output can be wrong, no model output was treated as evidence by itself; decisions were checked against the Russian source.

Optional additional sentence:

> Readers may inspect the evidence for individual translation decisions throughout this page.

---

# 24. What the Audit Does Not Prove

This section is important for intellectual honesty.

Recommended copy:

> No audit can make a literary translation mechanically objective. Russian words may permit more than one defensible English rendering, and rhythm, tone, implication, and literary effect cannot always be preserved simultaneously. The purpose of this apparatus is therefore not to prove that every sentence is the only possible translation. It is to make the basis of the edition visible.

This could live under ABOUT THIS EDITION.

---

# 25. Reader Corrections

Readers should be able to report a possible error on any unit.

Button:

`REPORT A TRANSLATION ISSUE`

The form should automatically include the unit ID.

Fields:

- What appears to be wrong?
- Suggested interpretation
- Optional source / dictionary / reference
- Contact email optional

Do not provide a public comment section beneath every sentence.

That would make the page noisy and difficult to moderate.

Instead, verified corrections can be added to the audit ledger.

---

# 26. Correction Policy

Publish a short correction policy.

Example:

> Substantive corrections are incorporated into the online text as they are verified. The previous wording remains visible in the revision history. Changes affecting a printed edition are listed by edition and printing.

For printed books:

**First printing — 2027**  
Corrections after printing:
- II-04-017
- II-09-033

This lets the website become a living errata sheet.

---

# 27. Versioning

Every public edition should have a version number.

Example:

`Translation version 1.0 — 14 February 2027`

Minor correction:

`1.0.1`

Substantial revision:

`1.1`

New printed edition:

`2.0`

The page should always say which digital text corresponds to which printed edition.

---

# 28. Printed Book Integration

The physical book should contain a short note near the copyright page.

Suggested structure:

---

### VERIFY THIS TRANSLATION

The complete Russian source, line-by-line commentary, revision history, and audit record for this edition are freely available online.

**christisinourhearts.com/ivan-ilyich**

[QR CODE]

Translation version 1.0

---

The QR code should point to a permanent canonical URL, not a temporary campaign link.

The URL should also be printed because QR codes are not archival.

---

# 29. Visual Language

The verifiability apparatus should belong visually to Christ Is in Our Hearts rather than looking like a developer console.

Recommended character:

- dark mode compatible;
- Google Sans Flex for interface / metadata;
- readable serif or existing site reading typeface for literary text if desired;
- restrained red accent;
- large white or warm-white reading text;
- Russian text slightly muted but never low-contrast;
- thin rules rather than boxed cards everywhere;
- generous vertical spacing;
- no gradients;
- no glossy "AI" imagery;
- no robot icons;
- no score gauges;
- no green/red correctness indicators.

The page should feel closer to a beautifully typeset critical edition than a SaaS dashboard.

---

# 30. Hierarchy of Typography

Suggested hierarchy:

### Work title
Large, restrained.

### English literary text
Primary visual element.

### Russian original
Slightly smaller or equal size, visually distinct by spacing rather than decorative treatment.

### Literal rendering
Smaller and muted.

### Editorial notes
Sans-serif, compact.

### Metadata
Small sans-serif uppercase or small caps.

Example:

`ORIGINAL RUSSIAN`

`LITERAL`

`WHY THIS WORDING`

`AUDIT RECORD`

The reader should always know whether they are looking at Tolstoy, the published English translation, or editorial commentary.

---

# 31. Color Use

Use red only for structural emphasis.

Possible uses:

- unit numbers;
- expansion indicators;
- headings;
- links;
- disputed-passage marker;
- active filter.

Never color the English translation red to indicate error.

Corrections should be explained verbally.

---

# 32. Mobile Design

The page must be designed mobile-first because many readers will arrive from a QR code in the physical book.

Important mobile behaviors:

- Russian and English stack vertically.
- Word-analysis tables become word cards.
- No horizontal scrolling for normal use.
- Expanded notes remember their open state while navigating nearby units.
- Sticky bottom control may offer:
  - ENGLISH
  - RUSSIAN
  - NOTES
- Chapter navigation should remain one tap away.
- URL fragments should jump precisely to the selected unit.
- Long grammatical notes should default collapsed.

Avoid placing the English and Russian in side-by-side columns on narrow screens.

---

# 33. Desktop Design

Desktop can optionally provide a parallel mode.

Toggle:

`READING` / `PARALLEL`

Parallel mode:

| Russian | English |
|---|---|
| source paragraph | published paragraph |

Clicking either side opens the full note below both columns.

Do not make parallel view the default.

Reading should remain the primary experience.

---

# 34. Deep-Linking

Every audit unit must have:

- permanent ID;
- anchor URL;
- copy-link button.

Example:

`christisinourhearts.com/ivan-ilyich/verifiable#II-07-083`

This allows a scholar, reader, or correction report to point to one exact sentence.

---

# 35. Citation

Offer a small **CITE THIS EDITION** section.

Possible formats:

- Chicago
- MLA
- plain citation

Include:

- Tolstoy;
- title;
- translator/editor;
- version;
- publisher / project;
- publication year;
- canonical URL;
- access date if appropriate.

Also allow citation of a specific unit.

---

# 36. Downloads

The page should eventually provide transparent data exports.

Possible downloads:

- English translation — HTML
- English translation — Markdown
- Russian source — TXT / Markdown
- Parallel text — TSV / CSV
- Translation units — JSON
- Audit ledger — CSV
- Full editorial apparatus — JSON or Markdown

This reinforces that the verification material is not merely decorative.

Suggested JSON unit structure:

```json
{
  "id": "II-01-004",
  "chapter": 1,
  "russian": "Жизнь Ивана Ильича была самая простая...",
  "published_english": "Ivan Ilyich's life had been...",
  "literal": "The life of Ivan Ilyich was...",
  "words": [
    {
      "surface": "Жизнь",
      "lemma": "жизнь",
      "grammar": "noun, feminine, nominative singular",
      "gloss": "life"
    }
  ],
  "status": "choice",
  "notes": [],
  "audits": {
    "source_alignment": true,
    "semantic": true,
    "omission": true,
    "addition": true,
    "syntax": true,
    "lexical_consistency": true,
    "register": true,
    "references": true,
    "style": true,
    "cold_audit": true
  },
  "revision_history": []
}
```

---

# 37. Technical Principle: Separate Content From Presentation

Do not hard-code all audit material directly into HTML.

Store the translation apparatus in structured source files.

Possible hierarchy:

```text
ivan-ilyich/
  metadata.json
  chapters/
    01.json
    02.json
    03.json
  audits/
    discrepancy-ledger.json
    recurring-terms.json
  source/
    russian.md
    source-metadata.json
```

The website should render these files.

Benefits:

- easier auditing;
- easier global edits;
- reproducible builds;
- easy exports;
- version control;
- easier comparison between editions.

---

# 38. Git / Public History

Optional but strongly aligned with the project:

Publish the structured translation repository publicly.

A reader could inspect:

- commit history;
- corrections;
- source files;
- audit scripts;
- version tags.

The web interface remains the humane reading experience.

GitHub remains the archival / technical layer.

Do not require normal readers to understand Git.

---

# 39. Audit Provenance

Every audit should ideally record:

- date;
- audit type;
- model/tool used where relevant;
- prompt/procedure version;
- human reviewer;
- result;
- correction made, if any.

Example:

```text
2027-01-18
Audit: S3 Omission Scan
Procedure: omission-audit-v2
Tool: language model
Result: possible omitted adverb flagged
Human review: confirmed
Action: restored adverb
```

This is especially valuable because models change over time.

The exact model name does not need to dominate the reader-facing page, but the technical record should preserve it where known.

---

# 40. Independent Audit Strategy

Where practical, important passages should be checked by a method that is partially independent from the original translation process.

Examples:

- a separate model instance;
- a different model family;
- a fresh prompt with no earlier translation rationale;
- dictionary / corpus checks;
- human Russian speaker review;
- comparison with reputable earlier translations;
- reverse semantic comparison.

The apparatus should distinguish:

**confirmation by repetition**

from

**independent evidence**.

This matters because repeatedly asking the same system the same question is not a genuinely independent audit.

---

# 41. Comparison With Earlier Translations

Where copyright permits quotation, the page may discuss earlier translations.

Do not create a giant competitive comparison for every sentence.

Use comparisons only where historically or editorially informative.

Possible section:

**OTHER TRANSLATIONS**

Maude:
> [short permitted quotation]

Garnett:
> [short permitted quotation]

Comment:
> Both suppress Tolstoy's repeated superlative. This edition retains it.

Where quotation rights are uncertain, paraphrase the difference instead.

---

# 42. AI Error Taxonomy

Because machine translation is involved, the audit should explicitly search for failure modes typical of language models.

Recommended categories:

### Hallucinated Addition
Meaning appears in English without basis in Russian.

### Silent Omission
Russian material disappears in English.

### Semantic Smoothing
A difficult or strange Russian expression becomes more conventional than the original.

### False Explicitness
Something implied in Russian is stated as a definite fact in English.

### Pronoun Resolution Error
Ambiguous or distant referent resolved incorrectly.

### Negation Error
Negation lost, added, or attached to the wrong clause.

### Aspect / Tense Flattening
Russian verbal aspect or temporal relation materially altered.

### Register Drift
Plain Russian becomes elevated English, or vice versa.

### Theological Normalization
Unusual Tolstoyan religious language silently converted into conventional church vocabulary.

### Synonym Drift
A recurring Russian term is translated differently without reason.

### Stylistic Beautification
Repetition, awkwardness, bureaucratic phrasing, or deliberate ugliness polished away.

### Interpretive Overreach
One plausible interpretation is presented as though the Russian explicitly states it.

These should become specific audit tests.

---

# 43. Tolstoy-Specific Audit Questions

For Tolstoy editions, every final audit should ask:

- Has repetition been preserved where rhetorically important?
- Has simple Russian been unnecessarily elevated?
- Has bureaucratic or legal language been made too elegant?
- Have theological terms been conventionalized?
- Have moral terms been made more abstract than Tolstoy's wording?
- Has irony been accidentally explained away?
- Have blunt statements been softened?
- Has an English idiom introduced imagery absent from the Russian?
- Have recurring terms been translated consistently enough for thematic patterns to remain visible?
- Has Tolstoy's deliberate syntactic awkwardness been "fixed" where it carries meaning?

These questions should appear in the internal audit protocol and may be summarized publicly.

---

# 44. Passage-Level Example — Full Mockup

Below is the intended content hierarchy for a single expanded unit.

---

## II-01-004

### PUBLISHED TRANSLATION

Ivan Ilyich's life had been very simple, very ordinary, and very terrible.

`INSPECT ▲`

### ORIGINAL RUSSIAN

Жизнь Ивана Ильича была самая простая и обыкновенная и самая ужасная.

### LITERAL

The life of Ivan Ilyich was the most simple and ordinary and the most terrible.

### WHY THIS WORDING

Tolstoy repeats *самая* ("most") before the first and final adjectives. The repetition links the extremity of Ivan Ilyich's ordinariness with the extremity of the horror. The published English keeps a parallel structure rather than compressing the sentence into smoother prose.

**Status:** CHOICE

`MORE DETAIL ▼`

### WORDS

| Russian | Lemma | Grammar | Sense |
|---|---|---|---|
| Жизнь | жизнь | noun, fem., nom. sg. | life |
| Ивана | Иван | proper noun, gen. sg. | Ivan's |
| Ильича | Ильич | patronymic, gen. sg. | Ilyich's |
| была | быть | past tense, fem. sg. | was |
| самая | самый | superlative marker | most |
| простая | простой | adjective | simple |
| и | и | conjunction | and |
| обыкновенная | обыкновенный | adjective | ordinary / commonplace |
| и | и | conjunction | and |
| самая | самый | superlative marker | most |
| ужасная | ужасный | adjective | terrible / dreadful |

### ALTERNATIVES CONSIDERED

**обыкновенная**
- ordinary
- commonplace
- usual
- conventional

"Ordinary" was selected because the passage concerns the normal social pattern of Ivan Ilyich's life rather than merely its dullness.

### REVISION HISTORY

**v1**  
Ivan Ilyich's life was the simplest and most ordinary and the most terrible.

**v2**  
Ivan Ilyich's life was very simple and ordinary, and very terrible.

**Published**  
Ivan Ilyich's life had been very simple, very ordinary, and very terrible.

### AUDIT RECORD

- ✓ S1 Source Alignment
- ✓ S2 Semantic Fidelity
- ✓ S3 Omission Scan
- ✓ S4 Addition Scan
- ✓ S5 Grammar / Syntax
- ✓ S6 Lexical Consistency
- ✓ S7 Register / Tone
- ✓ S8 Proper Names / References
- ✓ S9 English Readability
- ✓ S10 Cold Audit

### EDITORIAL NOTE

No unresolved issue remains in this unit.

`COPY LINK`  
`REPORT ISSUE`

---

# 45. Page-Level Navigation

Recommended top navigation:

`READ  NOTES  AUDIT  SOURCE  ABOUT`

Within READ:

`CHAPTER 1 ▾`

Optional controls:

`TEXT SIZE`

`SHOW RUSSIAN`

`SHOW NOTES`

`PARALLEL VIEW`

Do not present dozens of controls at once.

Advanced controls can live in a single settings panel.

---

# 46. URL Architecture

Suggested:

```text
/ivan-ilyich/
/ivan-ilyich/read/
/ivan-ilyich/verifiable/
/ivan-ilyich/audit/
/ivan-ilyich/source/
/ivan-ilyich/about/
```

However, a single-page implementation is also acceptable:

```text
/ivan-ilyich/
  #read
  #audit
  #source
```

The crucial requirement is stable passage anchors.

---

# 47. Landing Copy

Possible concise introduction:

> **A translation you can inspect.**
>
> This edition of *The Death of Ivan Ilyich* is published together with its evidence. Open any passage to see Tolstoy's Russian, a literal rendering, lexical and grammatical notes, the reasons behind difficult translation choices, and the audit history of the published English.
>
> The complete translation and its critical apparatus are free to read.

Alternative, more restrained:

> This page contains the complete translation together with the Russian text and the editorial record behind it. Open any passage to inspect the wording, translation choices, and audit history.

The second is probably closer to the desired site tone.

---

# 48. What Not to Do

Avoid:

- "accuracy scores";
- automated confidence percentages;
- badges such as "100% verified";
- excessive colored status indicators;
- AI branding;
- animated translation effects;
- chatbot UI;
- forcing the Russian on readers who only want English;
- hiding corrections;
- claiming objectivity where genuine ambiguity exists;
- publishing machine explanations without human review;
- making every sentence look controversial;
- turning the page into a technical demo.

The remarkable thing should be the depth of evidence, not the interface.

---

# 49. Minimum Viable Version

For the first public implementation, build only:

1. complete English text;
2. aligned Russian paragraphs;
3. stable passage IDs;
4. literal renderings;
5. important translation notes;
6. audit status;
7. discrepancy ledger;
8. source information;
9. methodology;
10. report-error function.

Do not delay publication waiting for every advanced feature.

Later additions can include:

- word-level grammar;
- recurring-term index;
- full revision history;
- public data export;
- comparison mode;
- Git history integration.

---

# 50. Ideal Full Version

The mature version should allow someone who speaks no Russian to:

1. select any sentence;
2. see exactly which Russian words it represents;
3. understand the basic grammar;
4. identify where multiple translations are possible;
5. see why the published wording was chosen;
6. inspect whether previous audits found problems;
7. see earlier revisions;
8. compare recurring terms elsewhere in the book;
9. report a suspected mistake;
10. cite that exact translation unit permanently.

At that point the website is no longer merely a supplement to the book.

It becomes a **public critical apparatus for the translation**.

---

# 51. Guiding Sentence

Use this as the design test for every feature:

> **Does this help a reader inspect the translation rather than merely ask them to trust it?**

If yes, it belongs.

If it merely makes the process look sophisticated, remove it.
