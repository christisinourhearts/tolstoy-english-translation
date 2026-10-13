# Editorial Decisions Log

This file records translation and editorial choices with corpus-wide consequences. It complements `TRANSLATION.md`: the constitution states the general rules; this ledger preserves the concrete decisions that caused those rules to be interpreted or refined.

Each decision should record the date, scope, decision, reason, examples, and whether it supersedes an earlier practice. Do not delete superseded decisions; mark them as superseded so the history remains visible.

## D0001 — Conservative fidelity before stylistic smoothing

**Date:** 2026-08-31  
**Scope:** corpus-wide  
**Status:** active

### Decision

When a source construction, image, repetition, or concrete expression is unusual in English but remains intelligible, prefer a conservative rendering that preserves the source's shape and imagery. “Clear contemporary English” is not permission to replace a concrete Tolstoyan phrase with a smoother abstraction merely because the abstraction is more idiomatic or elegant.

Stylistic smoothing is warranted when a close rendering would genuinely confuse an English reader, misstate the grammatical relation, or sound accidental in a way the source does not. When both a conservative and a freer rendering are intelligible, default toward the conservative one.

### Reason

Tolstoy often writes with deliberate directness and concrete phrasing. The project values recoverability of his actual wording over translatorly polish. A slightly strange but clear phrase may carry more of the source than a fluent abstraction.

### P002 examples

The cold audit had proposed several style-only smoothings. After editorial review, the conservative forms were restored:

- `со всем миром людей` → **“the whole world of people”**, not “all humanity.”
- `должна совершенно плотно срастись` → **“must grow completely and tightly into”**, not “must become completely fused with.”
- `суеверие большинства так называемых ученых` → **“the superstition of most of the so-called learned men”**, rather than recasting it as “the belief held by most of the so-called scholars.”
- `дойду ли я когда-нибудь до того, чтобы не зависеть...` remains **“Will I ever reach the point of depending on no external circumstances?”** rather than being normalized further.

The separate correction of the imperial form of address `Высокородию` remains in force because that was a precision correction, not a stylistic smoothing.

### Operational consequence

Cold audits should not change wording merely to remove a calque if the close English is intelligible and accurately preserves the source. A style-only proposed change should be treated as non-blocking and, when consequential, recorded here before adoption.

## D0002 — Tolstoy's own Gospel renderings and his key terms

**Date:** 2026-10-08  
**Scope:** *The Gospel in Brief* (R002.01) and any later unit that quotes or paraphrases the Gospels in Tolstoy's own Russian (e.g. the large *Harmony and Translation of the Four Gospels*, *What I Believe*)  
**Status:** active

### Decision

1. Tolstoy's Russian renderings of Gospel verses are translated directly from his wording. No English Bible (KJV or any other) is substituted, even where a familiar verse lies behind his text. This extends the precedent of P005.02 (the Golden Rule translated directly).
2. Where Tolstoy quotes the Church Slavonic text itself (the Lord's Prayer lines in the preface table and chapter subtitles; «изволися нам и св. духу»), the Slavonic is rendered literally in a slightly archaic register (*thy*, *art*, *hallowed be*) so that the language switch stays visible. His own plain-Russian paraphrases beside them use plain *your*.
3. Key terms are held constant across the whole work: разумение = “understanding”; начало = “source”; благо = “the good”; сын человеческий = “son of man”; царство Божие = “kingdom of God”; воля отца = “the will of the father”; соблазн = “temptation”. Source capitalization of отец/сын/дух/святой дух is followed. Details in `TERMINOLOGY.md`.
4. Tolstoy's deliberate Russifications are preserved, not normalized back to conventional biblical vocabulary: the Orthodox (Pharisees), the Old Believers (Sadducees), bishops (архиереи), the church (for the temple in Luke II), bathing (for baptism), hanged (for crucified, in the preface), birch seed (for mustard seed), grivnas and kopecks, Semyon (ch. I).

### Reason

The book's whole argument is carried by Tolstoy's re-wording of the Gospels. Substituting familiar scripture would silently undo his interpretation; normalizing his anachronisms would erase his deliberate point that the Gospel addresses Russian church life.

### Example

John I, 1 is «В основу и начало всего стало разумение жизни» → “The understanding of life became the foundation and source of all,” not “In the beginning was the Word.”

## D0003 — ё is rendered *yo*, and word-initial Е *Ye*, in personal names

**Date:** 2026-10-13 (drafted 2026-10-06 as a local "D0002" that was never pushed; renumbered because D0002 was taken)  
**Scope:** corpus-wide  
**Status:** active

### Decision

Render Russian ё as *yo* in personal names and patronymics even when the normalized source prints е: Федор → **Fyodor**, Петр → **Pyotr**, Семен → **Semyon**, Федорыч → **Fyodorych**. Render word-initial Е as *Ye*: Евстратов → **Yevstratov**, Елизавета → **Yelizaveta**, Екатерина → **Yekaterina**, Ермолаев → **Yermolaev** (as already in *Yergolskaya*). A widely established English form may be kept for well-known historical persons (e.g. the philosopher N. F. **Fedorov**), recorded in `NAMES.md`. Biblical persons keep their conventional English forms (D0002).

### Reason

The TEI normalized reading often prints е for ё, but the pronunciation is *yo*; word-initial Е is pronounced *ye*. Most of the corpus and the website already used *Fyodor* and *Yergolskaya*; the remaining *Fedor / Petr / Semenov / Evstratov / Elizaveta* forms were inconsistencies.

### Applied changes

- `Fedorych` → `Fyodorych` (1881-10-05 diary, NAMES.md, coverage note)
- `Petr` → `Pyotr`; `Evstratov / Evstratich` → `Yevstratov / Yevstratich` (letter to S. N. Tolstoy, 15 December 1850; diary 22 December 1850; coverage note)
- `Semenov` → `Semyonov` (letter to Goltsev, 1891; notebook 1888–1889; diary 1889-02-22; coverage notes)
- `Elizaveta, Ekaterina, Elena, Evgenia, Elagin, Ermolaev, Ermolov, Erofeyevich, Ekaterinoslav` → `Ye-` forms in the letters and notebooks where they occur, with matching coverage notes and manifest titles. English file names are unchanged so that paths stay stable.

## D0004 — Priority order, Tolstoy rules, and flagship editions

**Date:** 2026-10-13 (drafted 2026-10-06 as a local "D0003" that was never pushed; renumbered)  
**Scope:** corpus-wide  
**Status:** active

### Decision

Adopt the priority order (TRANSLATION.md §18), the Tolstoy rules T1–T11 (§19), the language-model failure checklist E1–E14 (§20), and independence levels (§21). Works published as verifiable editions on christisinourhearts.com receive a sentence-level apparatus under `project/editions/` (§22, `project/docs/EDITIONS.md`). American spelling and transliterated glosses for Russian in project prose are now explicit (§5).

### Reason

These rules came out of an audit of the website's *Death of Ivan Ilyich* page specification. Its showcase sentence had passed ten nominal checks while omitting Прошедшая история (*proshedshaya istoriya*, "the past history"), misplacing the chapter, and carrying a note that described the English inaccurately. The rules make such failures checkable.

### Example (IVI-02-001)

Прошедшая история жизни Ивана Ильича была самая простая и обыкновенная и самая ужасная.  
Literal: [The] past history of-[the]-life of-Ivan Ilyich was [the] most simple and ordinary and [the] most terrible.  
Adopted: **"The past history of Ivan Ilyich's life was the most simple and ordinary and the most terrible."**  
Rejected: Maude's "…and therefore most terrible" (E4: added connective); "very simple, very ordinary, and very terrible" (E2, T2, T3).
