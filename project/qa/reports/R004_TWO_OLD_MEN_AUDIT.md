# R004.01 — *Two Old Men*: audit and retranslation (2026-10-25)

**Source:** `corpus/works/v25_082_099_Dva_starika.md` (vol. 25, pp. 82–99, 1885), SHA-256 `ab0e08d0…5d3b2a`, verified against the committed blob in the local clone of the audited Russian repository.
**English:** `translations/works/v25_082_099_Two_Old_Men.md`. **Romanian:** `tolstoy-romanian-translation`, `translations/works/v25_082_099_Doi_batrani.md`.
**Website:** `two-old-men/index.html` and `two-old-men/romanian.html` now carry the same text.

## Method

1. The website English and Romanian pages were extracted and aligned with the 151 Russian paragraphs (the site splits dialogue into display paragraphs with speaker labels; the repository keeps Tolstoy's paragraphs).
2. Source-forward pass, paragraph by paragraph: each website sentence was kept, corrected, or retranslated against the Russian (gauntlet steps 1–3).
3. English edit, read as English (step 4).
4. Fresh-session audit of the finished English and, separately, of the Romanian, source-forward and reverse (independence: `fresh-session`, same model family). English: no hard defects, 22 soft points, 19 adopted. Romanian: 2 hard defects (an added «sfînt», "holy", in II; «astă-vară» for летось, *letos'*, "last summer", in XI) and about 20 grammar/idiom points; all hard ones and most others adopted.
5. Mechanical validation: 18/18 page markers in sequence and in the source paragraph positions; `validate_translation.py` and `validate_coverage.py` 0 errors (both repositories).

## Hard defects found in the previous website text

| Ch. | Russian | Old website | Now |
|---|---|---|---|
| Ep. | Господи (*Gospodi*, "Lord") | "Sir" | "Lord" |
| IV | Нема чого й взяти (Ukrainian, "there's nothing to take") | "Nothing to fetch it with" | "There's nothing here to take" |
| IV | а ми туточки (*a my tutochki*, "and we're here") | "and we're dying in here" | "and we're in here" |
| VI | the dream: the girl holds on (to the bag); the little one holds the foot-cloth | the girl holds the foot-cloth; "his other leg" | as in the Russian |
| VII | Кум Ефим и один дойдет (*kum Yefim i odin doydet*, "old friend Yefim will get there even alone"); отчего не дошел (*otchego ne doshel*, "why he hadn't got there") | "reach Jerusalem" added twice | no destination supplied |
| VII | оброк до смерти останется (*obrok do smerti ostanetsya*, "the vow will stay [on me] till death") | "remain in debt" | "the vow will stay on me till I die" |
| VIII | кидают (*kidayut*, "throw") | "lowered" | "thrown down" |
| VIII | Ефиму ноги обтер (*obter*, "wiped") | "washed … wiped" | "wiped" |
| VIII | заколоть (*zakolot'*, "to slay, stab") | "sacrifice" | "slay" |
| IX | рубль взял (*rubl' vzyal*, "took a ruble") | "borrowed" | "took" |
| X | странник в скуфье (*strannik v skuf'ye*, "pilgrim in the monk's cap") | "long-haired pilgrim" | "pilgrim in the monk's cap" |
| XI | его-то принял Господь (*yego-to prinyal Gospod'*, "him the Lord has accepted") | "the Lord certainly accepted his [labors]" | "him the Lord has accepted" |
| XII | Скучно нам без него (*skuchno nam bez nego*, "it's dreary for us without him"), said twice | once omitted | both kept |
| XII | отбывать каждому свой оброк (*otbyvat' kazhdomu svoy obrok*, "each to fulfill his own vow") | "his duty" | "his own vow" (the vow of ch. I and VII) |

Smaller restorations: the order "death and life" (II); Yelisey's switch to "you" (II) and Yefim's to "me" (IX); "soul" for душа (*dusha*) in II; the third "year before last" (XI); "crown" for венец (*venets*) in XII, echoing the crown of thorns in IX; "his bald pate … over his whole head" at every recurrence of лысина во всю голову (*lysina vo vsyu golovu*); блестит (*blestit*, "gleams") vs светится (*svetitsya*, "shines with light") in X; intensifiers removed ("something terrible", "certainly", "safer places"); "old Jerusalem", "Tsargrad".

The Romanian had parallel defects (e.g. «N-avem nici cu ce s-o aducem», «a zis ea în ucraineană», «nu-i mai puteau hrăni», «mîncat sau vîndut», «să-și jertfească fiul lui Dumnezeu», «pe a lui sigur a primit-o Domnul», «datoria» in the last sentence), all corrected; see its coverage record.

## Choices left for Andrei

- бахилки (*bakhilki*, a heelless leather footwear), II: "soft boots" / «încălțări noi de piele».
- хохлы, хохлатчина (*khokhly, khokhlatchina*, colloquial "Little Russians", "Little Russia"), III and VI: "Ukrainians", "the Ukrainian country". Tolstoy's colloquial word is not reproduced.
- The Ukrainian speech is in plain English/Romanian; the website end note now says that Tolstoy wrote it in Ukrainian.
- Царьград (*Tsar'grad*): "Tsargrad" / «Țarigrad» (instead of "Constantinople").
- «Не принимает душа» (*ne prinimayet dusha*, literally "the soul does not accept [it]"), IV: kept literally, "My soul won't take it."
- Romanian orthography with î for this unit (D0010 in the Romanian repository), matching the site; the other two Romanian units in the repository use â.

## Print checks (non-blocking)

See `project/qa/source_suspected/v25_082_099_Dva_starika.json`: «раба Божия» (*raba Bozhiya*, feminine "servant of God") in Yelisey's mouth (IV); «пити» (*pyty*, "to drink") for піти (*pity*, "to go") and Latin letters in the women's Ukrainian (VI); «дидко» (*dydko*) for "granddad" (XI); «па полу», «ВОТ», «II понял».
