# R002 Cold Fidelity Audit — R002.01 *The Gospel in Brief*

## Result

**PASS AFTER REVISION.** An independent cold audit compared the whole English text of R002.01 against the audited Russian source, paragraph by paragraph. It covered the preface, the introduction, chapters I–XII and the conclusion. Nothing was sampled. The audit found **19 defects**, all small and local, and fixed them in **22 text replacements** across chapters II–X and XII. Chapters I and XI, the preface, the introduction and the conclusion needed no change.

After revision the unit contains:

- **0 known substantive omissions**;
- **0 unsupported substantive additions**;
- **0 reversed relations, lost negations or shifts of modality**;
- **0 wrong speakers, subjects or referents**;
- **0 verse-reference or number errors introduced by the translation** (three wrong references belong to the printed edition and are reproduced as printed; see the print check);
- **0 structural losses** (138/138 page markers and every heading, verse prefix and table row are unchanged).

The defects were scattered rather than systematic. None changed the argument of a chapter. The most serious ones changed a modal verb, a tense, a referent or a key predication inside a single verse (see *Most serious findings*).

## Scope and identity

- Source: `corpus/works/v24_801_938_Kratkoe_izlozhenie_Evangelija_Predislovie.md` (vol. 24, pp. 801–938), SHA-256 `87ff4a14066b3250011bb748bb10f8fc754e5eef251af4b75de1320d82abf203`. The hash was verified on a fresh clone with `core.autocrlf=false` before the audit began.
- English: `translations/works/v24_801_938_The_Gospel_in_Brief.md`, branch `gospel-in-brief` at commit `06ce582` (PR #3).
- Romanian cross-check: `tolstoy-romanian-translation`, branch `gospel-in-brief` (PR #1), `translations/works/v24_801_938_Evanghelia_pe_scurt.md` at `f9e5254`. It was read only; nothing was edited.
- Scope: **the full text**. That is 1,619 blank-line-separated blocks: headings, the prayer table as one block, verse and prose paragraphs, and page-marker-only blocks. The production record counts 1,632 because it counts the table rows separately.

## What "cold" and "independent" mean here

This auditor did not write the translation and worked in a separate session from the one that produced it. The production coverage record and source-suspected file were skimmed once at setup, to find the scope and the six flagged readings. They were not used as a checklist: every verdict below comes from the direct Russian→English comparison. The audit is independent of the production context. It is still a model audit, not verification by a human Russian reader.

## Method

The method is the same as in P002/P003, applied to the whole text instead of a sample.

1. **Source-forward pass.** The Russian and English were aligned block by block (the alignment is exact, 1,619 = 1,619). Each Russian paragraph was read first, then the English was checked for omissions (including short words, negations and intensifiers), unsupported additions, reversed or shifted meaning, wrong speaker or referent, KJV or other familiar-Bible wording, consistency of the fixed terms (разумение, начало, благо, сын человеческий, царство Божие / небесное, воля отца, соблазн, личность, жизнь, дух), smoothing contrary to D0001, and the copying of references and numbers.
2. **Mechanical checks.** Every Arabic number, Roman numeral and book abbreviation in every paragraph was compared between Russian and English. There were 0 unexplained differences: the only two flags were «І-й» → "1st" and «IV века» → "4th century". A word search of the English for KJV markers (*verily, unprofitable, ravening, thee, hath, behold, publican, Pharisee, righteous…*) followed up every hit against the Russian.
3. **English-only read.** The English was read through on its own for ungrammatical or unclear sentences. These were fixed only where the fix stays at least as close to the Russian.
4. **Romanian cross-check.** All 1,619 English and Romanian blocks were read side by side. Wherever they read the Russian differently in meaning, the Russian decided. The cross-check turned up three English defects that the source-forward pass had missed (#691, #1299, and the confirmation of #1500).
5. **Print check** of the six flagged readings (see below).

Paragraph numbers (`#n`) below are 0-based block indexes in the aligned files, so a reviewer can find them again by splitting either file on blank lines after the front matter.

## Counts

| Category | Defects found | Fixed | Notes |
|---|---:|---:|---|
| Omissions | 2 | 2 | #332 «закисла»; #1446 «дворников» |
| Additions | 1 | 1 | #1210 unsupported "His" |
| Reversals / shifted meaning (incl. modality, tense, referent) | 7 | 7 | #191, #311, #691, #804, #1299, #1447, #1500 |
| Reference errors (introduced by the translation) | 0 | 0 | 3 wrong references are the printed edition's own, reproduced as printed |
| Terminology (incl. KJV reversion, D0002) | 3 | 3 | #453 "ravening", #1034 "unprofitable", #674 понять/разумение rule; "righteous" in #1210 is counted under Additions |
| D0001 smoothing / intensification | 2 | 2 | #516, #1074 |
| Style / grammar (English-only read) | 4 | 4 | #365, #680, #790, #941 |
| **Total** | **19** | **19** | 22 string replacements in 10 chapter commits |

Non-blocking alternatives that were recorded but not changed are listed at the end.

## Most serious findings

1. **#191, Mark VII, 12 (ch. II): modality reversed.** «И тогда можете не кормить отца и мать» had become "you may not feed your father and mother". Most readers take this as a prohibition, which inverts Jesus' charge that tradition *releases* people from feeding their parents. Now: "you need not feed".
2. **#1447, content of ch. XII: tense changed.** The witnesses testify «что Иисус хвалился тем, что он уничтожил иудейскую веру» (past, perfective: that he *had destroyed* it). The English said "would do away with", a future taken from the canonical temple saying. Now: "had done away with".
3. **#1210, content of ch. X: addition and terminology.** «Невинность и справедливость останавливали их» does not say whose innocence and justice. The English added "His" and used the KJV-coloured "righteousness"/"righteous" for справедливость/справедлив. Now: "Innocence and justice held them back", "whether this man is just or not just".
4. **#804, content of ch. VII: key predication weakened.** «потому что я сын человеческий — то же, что и отец» asserts "I am the son of man" and then equates the son of man with the father. "I, the son of man, am the same as the father" turned the first claim into an appositive. Now: "because I am the son of man—the same as the father".
5. **#1500, John XVIII, 36 (ch. XII): referent shifted.** «мои подданные бились бы за меня и не дались бы архиереям»: the subjects themselves would not have given in to the bishops. The English said "would not have let me fall into the bishops' hands". Now: "would not have given way to the bishops".

## All findings

Each entry gives the Russian, the old English, the new English and the reason.

### Chapter II

**#191 — Mark VII, 12** (reversal: modality)
- RU: «12. И тогда можете не кормить отца и мать.»
- Old: "12. And then you may not feed your father and mother."
- New: "12. And then you need not feed your father and mother."
- Reason: можете не = you are free not to. English "may not" reads as a prohibition. The Romanian ("puteți să nu-i hrăniți") has it right.

### Chapter III

**#311 — John III, 11** (shifted meaning)
- RU: «Пойми ты, что не мудрости какие-нибудь толкую я»
- Old: "Understand that I am not interpreting some kind of mysteries;"
- New: "Understand that I am not interpreting some kind of clever wisdom;"
- Reason: мудрости are clever or abstruse "wisdoms", not тайны. "Mysteries" brings in a sacramental or esoteric sense. Romanian: "vreo înțelepciune deosebită".

**#332 — Matt. XIII, 33** (omission)
- RU: «а ждет, чтобы она сама закисла и поднялась»
- Old: "but waits for it to rise and swell by itself."
- New: "but waits for it to ferment and rise by itself."
- Reason: закисла (sour, ferment) had been dropped and replaced by a doublet. Romanian: "să dospească singur și să crească".

### Chapter IV

**#365 — content of ch. IV** (style: ungrammatical)
- RU: «Исполняет волю отца не тот, кто призывает имя Бога, а тот, кто делает дела добра.»
- Old: "He fulfills the will of the father, not who calls on the name of God, but who does deeds of good."
- New: "It is not he who calls on the name of God who fulfills the will of the father, but he who does deeds of good."
- Reason: the English was ungrammatical. The new version keeps the contrast and adds nothing.

**#453 — Matt. VII, 15** (terminology: KJV reversion)
- RU: «а внутри они волки хищные»
- Old: "but inside they are ravening wolves."
- New: "but inside they are predatory wolves."
- Reason: "ravening wolves" is the KJV phrase word for word, against D0002. хищный = predatory.

### Chapter V

**#516 — John IV, 38** (D0001)
- RU: «то получаем награду — жизнь невременную»
- Old: "we receive a reward—a life not bounded by time."
- New: "we receive a reward—a non-temporal life."
- Reason: Tolstoy coins невременная as the negation of временная, which is "temporal" throughout. The paraphrase hid that link. Romanian: "viața nevremelnică".

### Chapter VI

**#674 — Luke XI, 28** (terminology)
- RU: «блаженны всегда только те, которые поняли разумение отца и хранят его»
- Old: "…those who have understood the understanding of the father…"
- New: "…those who have comprehended the understanding of the father…"
- Reason: TERMINOLOGY.md requires понять = "comprehend" where it takes разумение as object. The rule was applied at John I, 12 but missed here.

**#680 — Mark IV, 40** (style)
- RU: «Нет в вас веры в жизнь духа.»
- Old: "There is no faith in you in the life of the spirit."
- New: "There is no faith in the life of the spirit in you."
- Reason: the old word order was clumsy. The new one keeps the same words and the same sense.

**#691 — Luke IX, 24** (shifted meaning; found through the Romanian cross-check)
- RU: «А кто если и погубит плотскую жизнь, исполняя волю отца, тот спасет истинную жизнь.»
- Old: "But whoever, even if he ruins his fleshly life, fulfills the will of the father, will save the true life."
- New: "But whoever, in fulfilling the will of the father, ruins even his fleshly life will save the true life."
- Reason: исполняя is the manner of the losing. The old English made fulfilling the main condition and the losing a concession. Romanian: "…chiar dacă își va pierde viața trupească, împlinind voia tatălui…".

**#790 — Matt. XXI, 29** (style: ungrammatical)
- RU: «не тот в воле отца, кто говорит: я в воле отца, — а тот, кто делает то, что хочет отец»
- Old: "…not he is in the will of the father who says: I am in the will of the father—but he who does what the father wants."
- New: "…the one in the will of the father is not he who says: I am in the will of the father—but he who does what the father wants."

### Chapter VII

**#804 — content of ch. VII** (shifted meaning: predication)
- RU: «…потому что я сын человеческий — то же, что и отец.»
- Old: "…because I, the son of man, am the same as the father."
- New: "…because I am the son of man—the same as the father."
- Reason: see *Most serious findings* no. 4. The Romanian has the same appositive shift.

**#941 — John XI, 25, repeated** (style: punctuation)
- RU: «и всякий, кто живет и верит в меня, тот не умрет»
- Old: "and everyone, who lives and believes in me, will not die."
- New: "and everyone who lives and believes in me will not die."
- Reason: the comma follows Russian punctuation rules, but in English it makes the clause non-restrictive. The first occurrence (#911) already had no comma.

### Chapter VIII

**#1034 — Luke XVII, 10** (terminology: KJV reversion)
- RU: «думайте, что мы негодные работники»
- Old: "think: we are unprofitable workmen;"
- New: "think: we are worthless workmen;"
- Reason: "unprofitable" is the KJV word ("unprofitable servants"). негодный = worthless, as at Luke XVIII, 13 (#263, «негодного» = "worthless").

### Chapter IX

**#1074 — content of ch. IX** (D0001: intensification)
- RU: «И потому они, как гробы нарядные: снаружи красно, а внутри мерзость.»
- Old: "…like gaudy coffins: outwardly fair…"
- New: "…like dressed-up coffins: outwardly fair…"
- Reason: нарядный = dressed up, decorated. It has none of the pejorative force of "gaudy". Romanian: "morminte împodobite".

### Chapter X

**#1210 — content of ch. X** (addition; terminology)
- RU: «Невинность и справедливость останавливали их… нам не нужно рассуждать о том, справедлив или не справедлив этот человек»
- Old: "His innocence and righteousness held them back… whether this man is righteous or not righteous"
- New: "Innocence and justice held them back… whether this man is just or not just"
- Reason: "His" settles an ambiguity the Russian leaves open: the innocence could be Jesus' and the justice could be the judges' own sense of it. справедливость/справедлив = justice/just, while "righteous" belongs to праведный (kept at #1441 and #1532). Romanian: "Nevinovăția și dreptatea… drept sau nu este drept".

**#1299 — John XIII, 18** (referent; found through the Romanian cross-check)
- RU: «потому что один только из вас, тех, кому я умыл ноги и который ел хлеб со мной, один из вас погубит меня»
- Old: "…only one of you, of those whose feet I have washed and who have eaten bread with me—one of you will destroy me."
- New: "…only one of you, of those whose feet I have washed, he who has eaten bread with me—one of you will destroy me."
- Reason: который is singular and refers to the one who will destroy him. The English made it plural ("who have eaten"). Romanian: "care a mâncat".

### Chapter XII

**#1446 — content of ch. XII** (omission of a specific word)
- RU: «и на вопросы дворников о том, не был ли и он с Иисусом»
- Old: "to the questions of the men in the courtyard"
- New: "to the questions of the yard servants"
- Reason: дворник = yard servant, the household staff of the courtyard. "The men in the courtyard" drops that. The Romanian ("oamenilor din curte") has the same loss.

**#1447 — content of ch. XII** (reversal: tense)
- RU: «свидетели показывали, что Иисус хвалился тем, что он уничтожил иудейскую веру»
- Old: "the witnesses testified that Jesus had boasted that he would do away with the Jewish faith."
- New: "the witnesses testified that Jesus had boasted that he had done away with the Jewish faith."
- Reason: see *Most serious findings* no. 2. Romanian: "se lăuda că a nimicit".

**#1500 — John XVIII, 36** (referent)
- RU: «Если бы я был царем земным, то мои подданные бились бы за меня и не дались бы архиереям.»
- Old: "…my subjects would fight for me and would not have let me fall into the bishops' hands."
- New: "…my subjects would fight for me and would not have given way to the bishops."
- Reason: the subjects are the ones who would not yield. Romanian: "nu s-ar da arhiereilor".

## Print check of the six flagged readings

**Done. All six readings are confirmed against the printed vol. 24.**

The audit session itself could not reach a scan: the network egress policy blocked `tolstoy.ru`, `rusneb.ru`, `archive.org` and `ru.wikisource.org`. On 2026-10-08 the commissioner downloaded the printed volume as a PDF from tolstoy.ru (vol. 24, Moscow 1957; <http://tolstoy.ru/upload/iblock/fc8/fc861b6c67031b717c12ad598777513a.pdf>) and checked pp. 801–938 locally. Every reading matches the printed page, so **none of them is a transcription error in the digital source**.

| # | Reading | Printed vol. 24 | Status | English |
|---|---|---|---|---|
| 1 | John VI, 35 (p. 856) | «…тот не будет никогда знать **вражды**» | Confirmed as printed | "enmity", kept |
| 2 | Last Supper reference (p. 914) | «Мф. XXVI, 21; **Марк. XIX, 18**» | Confirmed as printed; the reference error is the edition's own (canonical Mark XIV, 18) | Reproduced as printed |
| 3 | Barabbas passage (p. 932) | «**Мф. XXVI, 20.** И когда услыхали это архиереи…» | Confirmed as printed; the edition's own error (canonical Matt. XXVII, 20) | Reproduced as printed |
| 4 | Widow's mite (p. 870) | «**Лук. XII, 41.** Случилось раз…» | Confirmed as printed; the edition's own error (canonical Mark XII, 41) | Reproduced as printed |
| 5 | John X, 31 (p. 883) | «взялись за камни, чтобы **добить** его» | Confirmed as printed | "finish him off", kept |
| 6 | Havet (p. 813) | «Jesus Christi n'avait rien de chritien. A Souris…» | Confirmed as printed (the digital "n'avaitrien" only lacks the printed space) | Kept, space restored |

**Correction to this audit's earlier inference.** Before the print check, this report took Tolstoy's large *Harmony* in the same volume as an internal witness. Its wording at p. 332 (жаждать) and p. 506 (побить) was treated as "strong evidence" of transcription errors in the Brief. The print shows that inference was wrong. The Brief's printed text really reads вражды and добить. Where it differs from the *Harmony*, the difference lies in Tolstoy's text or in the edition, not in the digital copy. The English correctly follows the printed Brief. The *Harmony* evidence is still worth noting for a scholarly apparatus: the Brief's вражды stands where the *Harmony* has thirst, and its Лук. XII, 41 is cited as Mark in the *Harmony*. No erratum is recorded against the source.

The source-suspected file is now `SOURCE_VERIFIED`. The manifest flag `print_witness_check_pending` has been replaced by `print_witness_checked_vol24`, with `source_qa_status: source_verified`.

## English–Romanian discrepancy list

The Romanian was read in full against the English. Below is every place where the two read the same Russian **differently in meaning**, with the verdict reached from the Russian. Differences of wording only were not listed. That includes Romanian Bible register, *fericiți* for блаженны, and *Simon* for Семен (noted once below).

| # | Passage | Russian | English | Romanian | Verdict / who needs a fix |
|---|---|---|---|---|---|
| 54 | Preface | «в том, чтó проповедывал этот человек такое особенное, что заставило людей выделить его» | "what this man preached that was so special that it made people single him out" | "ceea ce propovăduia acest om **atât de deosebit**" (attaches "so special" to the man) | EN right (stressed чтó; такое особенное qualifies what he preached). **RO fix.** |
| 132 | Luke IV, 11 | «воля отца моего духа» | "my father of the spirit" | "tatălui spiritului meu" (father of my spirit) | Genuine ambiguity; both defensible. No fix. |
| 142–144 | John I, 40–42 | «Семен» | Semyon | Simon | Not a meaning difference; RO flattens Tolstoy's everyday name form (NAMES.md keeps it in EN). RO may consider. |
| 191 | Mark VII, 12 | «можете не кормить» | (old) "may not feed" | "puteți să nu-i hrăniți" | RO right. **EN fixed.** |
| 233 | John IV, 25 | «Он тогда всё расскажет» | "He will tell everything then" | "ne va spune totul" (adds "us") | Minor RO addition. |
| 274 | Matt. XII, 20 | «чтобы правда восторжествовала над ложью» | "truth … over falsehood" | "dreptatea … minciuna" (justice) | правда means both truth and justice, but against ложь the sense is "truth". EN closer; RO optional review. |
| 311 | John III, 11 | «не мудрости какие-нибудь» | (old) "mysteries" | "vreo înțelepciune deosebită" | RO right. **EN fixed.** |
| 332 | Matt. XIII, 33 | «закисла и поднялась» | (old) "rise and swell" | "să dospească … și să crească" | RO right. **EN fixed.** |
| 586 | John VI, 35 | «вражды» | "enmity" | "dușmănia" | Both translate as read; confirmed against print. No fix. |
| 638 | Matt. XII, 24 | «бесится» | "is raving" | "e îndrăcit" (possessed) | Both defensible. No fix. |
| 669, 782–786, 1237–1239 | Anointing passages | «масло» | "oil" | "mir" (chrism) | RU has plain масло (мѵро only at #1213). Minor RO wording. |
| 674 | Luke XI, 28 | «поняли разумение» | (old) "understood the understanding" | "au priceput înțelegerea" | RO follows the comprehend convention. **EN fixed.** |
| 691 | Luke IX, 24 | «кто если и погубит плотскую жизнь, исполняя волю отца» | (old) made "fulfills" the main verb | keeps the participle | RO closer. **EN fixed.** |
| 796 | ch. VII content | «сам ли он есть Христос» | "whether he himself was the Christ" | "că el însuși este Hristosul" (that he is) | EN right (ли = whether). **RO fix.** |
| 804 | ch. VII content | «я сын человеческий — то же, что и отец» | (old) appositive | same appositive | Both shifted. **EN fixed; RO should make the same fix.** |
| 898 | John IX, 19 | «Это ли ваш сын…» | question | statement | ли marks a question. **RO fix** (minor). |
| 935 | John X, 31 | «добить» | "finish him off" | "ca să-l omoare" (to kill him) | Print confirms добить (finish off). RO flattens it to plain "kill". **RO fix** (e.g. "ca să-l omoare de tot / să-l doboare"). |
| 1074 | ch. IX content | «гробы нарядные» | (old) "gaudy coffins" | "morminte împodobite" | RO closer. **EN fixed.** |
| 1085 | Matt. XVIII, 8 | «отвертит лапу» | "twists off its paw" | "își răsucește laba" (twists its paw) | отвертит = twists off, and the image depends on the severing. **RO fix.** |
| 1210 | ch. X content | «Невинность и справедливость … справедлив» | (old) "His innocence and righteousness … righteous" | "Nevinovăția și dreptatea … drept" | RO right. **EN fixed.** |
| 1299 | John XIII, 18 | «и который ел хлеб со мной» (sg.) | (old) "who have eaten" (pl.) | "care a mâncat" (sg.) | RO right. **EN fixed.** |
| 1446 | ch. XII content | «дворников» | (old) "the men in the courtyard" | "oamenilor din curte" | Both lose дворник. **EN fixed; RO may adopt "slugile/argații din curte".** |
| 1447 | ch. XII content | «хвалился тем, что он уничтожил» | (old) "would do away with" | "se lăuda că a nimicit" | RO right. **EN fixed.** |
| 1451 | ch. XII content | «повели на лобное место» | "the place of the skull" | "locul de execuție" | Genuine ambiguity (the Golgotha gloss vs. the Russian public execution place). Both defensible. |
| 1472 | Matt. XXVI, 74 | «клясться и божиться» | "swear and call God to witness" | "să se jure și să se blesteme" (curse himself) | божиться = swear by God. **RO fix** (minor). |
| 1500 | John XVIII, 36 | «не дались бы архиереям» | (old) "let me fall into the bishops' hands" | "nu s-ar da arhiereilor" | RO right. **EN fixed.** |

Summary: **26 discrepancy points.** In 12 the English needed (and received) a fix: #191, #311, #332, #674, #691, #804, #1074, #1210, #1299, #1446, #1447 and #1500 (#804 and #1446 also need a Romanian fix). The Romanian needs a fix at 7 points (#54, #796, #804, #898, #935, #1085, #1472), plus optional review at 4 (#142, #233, #274, oil/mir). The rest are genuine ambiguities or handling of the flagged readings.

## Non-blocking alternatives (recorded, not changed)

- #131 Luke IV, 10: the initial «А» ("And") is not rendered. Trivial.
- #194, #373, #375 "woe" for беда/горе: ordinary English, kept.
- #437 Matt. VI, 25 «жизнь мудренее пищи» → "a more wondrous thing". мудреный is closer to "more intricate". The Romanian has the same choice ("mai de mirare"). Possible future refinement.
- #850 John VIII, 14 «то все-таки моя правда» → "still the truth is mine". The idiom means "I am in the right". Kept as the literal, intelligible reading under D0001.
- #1111 Matt. XIX, 5 "cleaves" for «прилепляется»: Tolstoy keeps the Synodal word here, so a parallel register is justified.
- #1423 John XVI, 28 "You have understood that understanding…". Here разумение is the subject, not the object of понять, so the ledger rule does not strictly apply.
- #1467 Matt. XXVI, 69 «ты тоже с Иисусом Галилейским» → "you too were with". The verb is supplied; "are with" is also possible.
- #1537 «радуйся, царь иудейский» → "hail" (greeting sense, cf. #1456 "greetings"). The Romanian keeps the literal "bucură-te".
- "perdition" (погибель) and "abomination" (мерзость) are ordinary dictionary equivalents, kept.

## Verdict

**PASS AFTER REVISION.** R002.01 stays `reviewed`, with `cold_audit_status: pass_after_revision` and `source_qa_status: source_verified`. All six previously flagged readings are confirmed against printed vol. 24 and translated or reproduced as printed. No open source questions remain for this unit.
