# P002 Cold Fidelity Audit

## Result

**PASS.** A fresh direct source-to-English audit was performed on 10 deliberately difficult P002 units, representing 40% of the batch and approximately 1,766 rough source-body words.

The audit found:

- **0 omitted substantive source passages**
- **0 unsupported substantive English additions**
- **0 reversed logical relations or lost negations**
- **0 wrong speakers, subjects, names, numbers, or dates**
- **0 lost headings, page markers, or footnote structures** in the sample
- **1 minor source-precision correction** in an imperial-era form of address
- **4 minor contemporary-English clarity edits**, none changing substantive meaning

No sampled unit needed to be demoted from `reviewed` status.

## What “cold” means here

This pass was conducted by comparing the selected final English files directly against the Russian/source files without consulting their earlier P002 coverage records or translation reasoning before reaching the audit verdicts. The earlier QA records were therefore not used to tell the auditor what to look for.

This is a useful fresh-pass control, but it is **not** equivalent to an audit by a separately instantiated model or an independent human Russian reader. Periodic audits by genuinely separate contexts/models remain valuable at publication scale.

## Selection

The sample was intentionally weighted toward difficult cases rather than random easy prose:

1. `corpus/works/v07_132_132_Filosofskij_otryvok.md`
2. `corpus/letters/v59_024_T_A_Ergolskoj.md`
3. `corpus/letters/v59_035_Gr_S_N_Tolstomu.md`
4. `corpus/diaries/v46_032_033_1847_06_16.md`
5. `corpus/notes/v48_342_342_Zapis_No_1_1863.md`
6. `corpus/azbuka/v21_026_026_Slepoj_i_gluhoj.md`
7. `corpus/azbuka/v21_053_054_Krasnaja_shapochka.md`
8. `corpus/krug_chtenija/v41_013_015_Krug_chtenija_daily_jan_1_2.md`
9. `corpus/krug_chtenija/v41_016_017_Krug_chtenija_daily_jan_1_4.md`
10. `corpus/works/v01_246_246_Dlja_chego_pishut_ljudi.md`

This includes unfinished philosophy, a French letter with Russian apparatus, a physically torn letter, a morally unpleasant early diary entry, an illegible manuscript note, untranslatable sound-play, a familiar fairy tale where interpolation would be tempting, two compilation entries containing attributed quotations, and a manuscript sentence whose construction the editors explicitly say was disrupted by a later insertion.

## Per-unit findings

### 1. Philosophical Fragment — PASS

The English accounts for every fragment of the source. The most awkward constructions remain awkward rather than being reconstructed into a finished philosophical argument. No hidden explanatory matter was introduced. No change required.

### 2. Letter to T. A. Yergolskaya — PASS after minor precision correction

Tolstoy's French body is complete and accurately represented, and the Russian editorial apparatus is separately translated.

One small precision issue was found in the address on the reverse. `Ея Высокородію` had been rendered `Her Well-Born`; the more exact historical rank-style distinction is `Her High Born`. This was corrected. The body of Tolstoy's letter was unchanged.

### 3. Torn letter to Count S. N. Tolstoy — PASS

The translation does not reconstruct words lost with the torn sheet. Partial words and broken lines remain visibly incomplete, while complete surviving clauses are represented. Both editorial notes and Tolstoy footnotes remain present. No change required.

### 4. Diary, 16 June 1847 — PASS

All of Tolstoy's claims, including the misogynistic content, remain present without euphemism or intensification. The deleted/source-error notes are retained. The opening question received a purely syntactic contemporary-English smoothing (`reach the point where I depend...`); its meaning is unchanged.

### 5. Note No. 1, 1863 — PASS

Both illegible spans remain explicit. The broken syntax around the first illegible span has not been repaired by invention. The emotionally harsh self-description is preserved. No change required.

### 6. The Blind Man and the Deaf Man — PASS

All narrative actions and mistaken responses are present. The Russian sound relations (`стручист` / `стучит`, and the later mishearing) cannot be reproduced literally without inventing different English jokes; the English preserves the semantic action instead. No change required.

### 7. Little Red Riding Hood — PASS

The audit specifically checked for contamination from the familiar Western version of the story. None was found. Tolstoy's short version remains complete: the cakes and butter, mushrooms and berries, the latch, the grandmother's death, Little Red Riding Hood's death, and the wolf's final departure are all represented. No rescuer or moral has been added. No change required.

### 8. Circle of Reading, 2 January — PASS

All five numbered sections, attributions, Tolstoy framing sentences, and page divisions are represented. No quotation was silently replaced with a familiar external English original. `so-called learned men` was changed to `so-called scholars` for contemporary English; this is a style clarification, not a substantive correction.

### 9. Circle of Reading, 4 January — PASS

Tolstoy's opening and closing reflections and all six attributed selections are present. No source quotation has been restored from an external standard edition. Two awkward calques were clarified: `the whole world of people` became `all humanity`, and `grow completely and tightly into` became `become completely fused with`. The source claims are unchanged.

### 10. Why Do People Write? — PASS

The source's argument is complete in English. The strange unfinished construction in the first paragraph remains strange because the source note explicitly says that Tolstoy's later insertion disrupted the sentence. The translation correctly resists “fixing” that manuscript state. No change required.

## Structural cross-check

For all 10 sampled files, a mechanical source/target comparison found matching sequences/counts for all applicable:

- preserved volume/page markers;
- headings;
- footnote references and definitions;
- large Markdown block structure.

Mechanical agreement is not semantic proof, but in combination with the direct bilingual pass it provides an additional omission warning layer.

## Assessment

The important result is not that every English phrase is uniquely optimal. Several could legitimately be phrased another way. The important result for corpus reliability is that this difficult 40% sample contained no evidence of the failure mode the project is primarily designed to prevent: material silently disappearing, new meaning being supplied, or Tolstoy's thought being substantially changed during smoothing.

The cold pass did still find a real small error and several unnecessary calques, which is evidence that the extra layer is useful rather than ceremonial.

## Recommendation

P002 remains accepted. Before P003:

1. keep periodic cold audits as a formal corpus rule;
2. add the planned automatic boundary-suspicion preflight for small source files;
3. run P003 at roughly 50 short units / 7,000–10,000 source words;
4. cold-audit a difficult sample after P003, with a genuinely separate model/context where available.
