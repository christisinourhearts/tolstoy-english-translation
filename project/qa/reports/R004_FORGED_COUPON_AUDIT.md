# R004.02 — *The Forged Coupon*: audit and retranslation (2026-10-26)

**Source:** `corpus/works/v36_005_053_Falshivyj_kupon.md` (vol. 36, pp. 5–53, 1880/1904), SHA-256 `bd85c3ff…ec4835`, verified against the committed blob in the local clone of the audited Russian repository.
**English:** `translations/works/v36_005_053_The_Forged_Coupon.md`. **Romanian:** `tolstoy-romanian-translation`, `translations/works/v36_005_053_Cuponul_fals.md`.
**Website:** `forged-coupon/index.html` (reading text and the English–Russian parallel edition) and `forged-coupon/romanian.html` now carry the same text.

## Method

1. The website English (version 1.0, 29 September 2026) and Romanian pages were extracted and aligned with the 565 Russian paragraphs, using the English–Russian parallel edition already on the site. The site splits them into 1,017 display paragraphs with speaker labels; the repository keeps Tolstoy's paragraphs.
2. Source-forward revision of both languages together, chapter by chapter, by eleven same-model subagents working from aligned packets under one brief (gauntlet steps 1–4). Every website paragraph was kept, corrected, or retranslated against the Russian. Recurring terms were then harmonized across chapters.
3. Fresh-session audit of the finished English and, separately, of the Romanian, source-forward and reverse (eight subagents; independence: `fresh-session`, same model family). English: 1 hard defect (земский начальник, *zemsky nachal'nik*, "land captain", had been "zemstvo chief") and 25 soft points, 24 adopted. Romanian: 7 hard defects (five grammar, one sense, the «Разве можно?» leitmotif) and 43 soft points, all adopted.
4. Mechanical validation: 49/49 page markers in sequence and at the source paragraph positions; footnotes [^1]–[^4] in place; `validate_translation.py` and `validate_coverage.py` 0 errors in both repositories.

## What was wrong with the old website text

The English had had a careful first edition, but the revision still classed about 300 English corrections as hard defects; the Romanian, about 490. The Romanian had been damaged by an automatic conversion to perfectul compus that also turned infinitives and nouns into participles («nu a putut a dormit», *he could not have-slept*; «de a luptat împotriva», *of to-fought against*), and it was more abridged than the English, with clauses dropped and a few lines invented.

| Part, ch. | Russian | Old website | Now |
|---|---|---|---|
| I, II | валить? (*valit'?*, "shall I go ahead?"), Makhin asking | "Shall we do it?" | "shall I go ahead?" |
| I, II | Как же... (*Kak zhe*, "But how…") | "Of course..." | "But how..." |
| I, VI | the sazhen of wood stacked as five "quarters" (RO) | split "to keep a small profit" | Ivan Mironov's trick restored |
| I, IX | Будь с ними хорош, и они будут хороши (*bud' s nimi khorosh…*, "be good to them and they will be good"), free indirect | quoted, "they'll treat you properly" | unquoted, as Tolstoy |
| I, XII | недоброжелательство к себе отца (*the father's ill will toward him*) (RO) | the priest's hostility toward the father | the father's ill will toward him |
| I, XV | кроме царя, который один жалел народ (*except the Tsar, who alone pitied the people*) | "whom he still believed to be just" | "who alone pitied the people and was just" |
| I, XVI | хромой, безногий портной (*a lame, legless tailor*) | "a tailor who had difficulty walking" | "a lame, legless tailor" |
| I, XXI | прося свидания (*asking for a visit*, with Tyurin) | asking to be received by the minister | asking for a visit |
| I, XXII; II, XIV | Tolstoy's French | translated in the body, "in French" added | French kept, with footnotes |
| II, I | Не надивлюсь на него (*I can't marvel at him enough*) (RO) | «Nu mă mai mir de el» ("I'm no longer surprised at him") | «Mă tot minunez de el» |
| II, II | the suicide attempt (RO) | cut; «A hotărît să se omoare» invented | restored |
| II, III | Stepan's reasoning on Matthew 25; the two Gospel references | cut | restored |
| II, VII | обратил палача (*converted the executioner*); он не вошел в душу Степана (*he did not enter Stepan's soul*) | "made him renounce his work"; "did not understand him" | restored, with the dropped sentences |
| II, IX | the escape | about a dozen sentences dropped; the historic present undone (RO) | restored |
| II, XI | the telegram scene; коллежский асессор (*Collegiate Assessor*) | reported speech made dialogue; «consilier colegial» (RO) | as in the Russian |
| II, XIV | что дальше, то хуже (*the further it went, the worse*) | "the more direct he became" | "the further it went, the worse" |
| II, XVI | how it had affected him | "how Maria Semyonovna had changed him" (invented) | "how it had affected him" |

Names now follow D0003 and Tolstoy's own forms: Fyodor (not Fedor), Yeropkina, the Liventsovs (not "Livenzov"), Pyotr Nikolaich where Tolstoy writes Николаич (*Nikolaich*) and Pyotr Nikolayevich only where he writes Николаевич.

## Choices left for Andrei

- цыган (*tsygan*): "Gypsy" throughout (the site had "Roma" and "Romani"). Tolstoy uses one ordinary word; "Roma" can be restored everywhere if preferred.
- Romanian: купон = «cupon» and the title «Cuponul fals» (decided by Andrei, 26 October 2026; the site had «hîrtie de valoare»).
- Romanian народный дом (*narodny dom*, "People's House"): «casa poporului», which a Romanian reader may hear as Ceaușescu's building; «casa norodului» is an alternative.
- Romanian земский начальник: «șef de zemstvă» (the English now has "land captain"); сотский / десятский transliterated «sotski» / «desiatski».
- Website speaker labels: "Pyotr Nikolaich", "The Tsar", "The Sovereign's mother" (were Nikolayevich and Emperor).
- The peasant's mangled фатера (*fatera*, for квартира, "apartment") is "partment" / «partament»; аблакат (*ablakat*, "advocate") is plain "lawyer" / «avocat».
- Vasily's misspelled letter (II, XVII) is marked lightly in English ("You done me…") and written in plain popular Romanian.

## Print checks (non-blocking)

See `project/qa/source_suspected/v36_005_053_Falshivyj_kupon.json`: an empty `<sup></sup>` after «2 1/2» (p. 5), italic «что» (p. 26), «fillete» (p. 32), the sentence split by the p. 17 page marker, and letter slips read correctly under D0009 (e.g. «модод», «рассвенет», «о» for «с»).
