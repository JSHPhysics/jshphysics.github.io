# Topic 1 — Key concepts of physics: SOP notes

Build: `python3 tools/build_key_concepts.py && python3 tools/build_manifest.py`
(keeps the six existing calculation types untouched and embeds them).
Modules: `kc_nn.py` (N1–N9), `kc_keywords.py` (N10, the 18
Working-Scientifically terms), `kc_tricky.py` (T1–T8), `kc_facts.py`
(flashcards), shared helpers in `revlib.py`.

This topic was written before the SOP was recorded (2026-11-16), so it
has no evidence table; the examiner findings it carries are in the
sections themselves.

## Rules for this page (author-approved; keep in every edit)

- Students are given the **full** equation list in the exam (the
  post-COVID arrangement), so there is no recall/given split anywhere on
  the site. N6 is "The equation list: choosing the right equation": the
  whole list by topic, with selection as the skill. Never tell students an
  equation must be memorised; checklists say "use", not "recall".
- T6 holds the author's seven-step recipe for the 6-mark planning
  question (variables → formula → change → measure → use the result → one
  accuracy detail → repeat and calculate a mean; questions stay at 6
  marks, any six of the seven points). Other topics apply it to their own
  practicals and link here for the recipe; they do not restate it.
- Standard form (N5) is H.
- The moment equation is on the equation list like every other (an early
  blind-check note that it was "recall" is superseded by the rule above).

## Step 7 — blind check

A separate agent checked the file and found three things, all fixed: a
stored value, a graph/text mismatch, and the moment-equation note above.

## Step 8 — headless test

Every numeric and choice answer entered through the UI and marked
correct; no KaTeX errors; no sideways scroll at 390 px; booklet modal
offers the notes mode.

## Revisions

### 2026-11-22 — exam-wording verification against the question database

A separate agent compared the page with `Question DB/by-topic/topic-01.md`
(81 questions whose parts carry 1.x references) and an index.json sweep of
all 286 questions: every method / levelled part of 4+ marks (58), 277
short parts on the Working-Scientifically terms, and a command-word census
of the whole bank (Calculate 198, Explain 150, Which 107, Describe 99,
Give 96, Use 68, Draw 28, Suggest 21, Compare 10, Show that 9, Estimate 7,
Discuss 4, Devise 2, Deduce 2, Justify 1, Comment on 1, **Evaluate 0**;
161 of 177 Calculate schemes "award full marks for the correct answer
without working"). Changes — the marking model, not the recipe:

| Reference | Change | Scheme |
|---|---|---|
| key-concepts / si-units (blurb, explain), kc-n1-q3 | "hz / n marked wrong" → tolerated (hz, c accepted); a *wrong* unit fails (W/s); a consistent non-SI unit scores (2.68 g/cm³, 200 mC) | 1H June 2018 Q2(b); 2H June 2025 Q4(c); 1H Nov 2021 Q8(e)(i); 2H June 2023 Q3(b) |
| key-concepts / prefixes-nn (blurb) | a prefix slip costs the evaluation mark only; conversion is sometimes its own mark | 1H June 2023 Q1(a); June 2022 Q7(c)(i) |
| key-concepts / sig-figs (explain), flashcard | s.f. ignored unless asked; when asked, an independent mark for any value to that many figures (1.4 scores 2 of 3; 1.50 scores 2 of 3) | 1H June 2022 Q3(a)(iii); 2H June 2022 Q6(b)(i) |
| key-concepts / equation-sheet (explain, worked), reading-questions | g usually printed, 9.8 accepted; the speed of light is always printed | 2H June 2025 Q2(b) and the stems |
| key-concepts / rearranging-nn worked | the square-root slip costs one mark ("x² seen gains 2 marks"); substitution and rearrangement in either order | 2H Nov 2020 Q6(c); June 2024 Q7(a) |
| key-concepts / proportion table | percentage-change traps: divide by the original (−41% scored 1 of 2), the change not the remainder (71% scored 1 of 2), sign optional | 2H June 2024 Q4(c)(iii); 1H Nov 2020 Q6(a)(i) |
| key-concepts / ewau (table, explain), kc-n9-q1, kc-n9-q2 | "'2.6 m/s²' alone gets nothing" → a correct answer alone gets full marks; working is insurance; first mark is "selection and substitution"; unit only marked when "State the unit" (independent); kc-n9-q1 rebuilt (12 N alone = 0; 12 × 10 = 12 N scores the substitution) | 2H June 2023 Q2(c); 1H June 2023 Q9(a); June 2022 Q9(b)(i); June 2022 Q5(a)(i); 2H June 2025 Q4(c) |
| key-concepts / keywords-ws (Precise, Independent variable) | "to lots of decimal places" removed from non-scoring — Edexcel marked "more precise" as more s.f.; name the quantity | 2H June 2022 Q8(c)(ii); 1H June 2024 Q8(d)(ii) |
| key-concepts / command-words table, kc-t1-q4, kc-t1-q6, flashcard | **Evaluate → Discuss** (no 1PH0 paper uses Evaluate); Comment on, Use, Devise, Deduce rows added; Estimate as a calculation on given data marked to a range; Show that with a value that needs rounding (140 625 J ≈ 140 kJ; "do not accept 710 m"); Justify example = "random, not 'difficult to predict'"; Compare: similarities score | 1H Nov 2020 Q8(c); 2H June 2023 Q8(b)(i); 2H June 2019 Q3(b)(ii); 2H June 2018 Q8(c); 1H June 2022 Q8(a); 2H June 2024 Q3(d); 1H June 2022 Q5(a)(i); June 2024 Q7(a)(ii); Nov 2020 Q7(e)(ii); 2H June 2022 Q4(c) |
| key-concepts / reading-questions trap table, kc-t2-q6 | "hidden sign" → opposite directions: the real trap is the momentum change across a bounce (0.2 instead of 1.4 cost the evaluation mark); the sign on an answer line is optional | 1H June 2023 Q9(b); June 2022 Q7(c)(i) |
| key-concepts / multi-step (explain), kc-t3-q6 | rounded intermediates are usually forgiven ("accept 2, 2.2, 2.27, 2.3 for a throughout"), not always; question re-set with a coarse rounding | 1H June 2022 Q5(a)(ii); Nov 2020 Q5(a) |
| key-concepts / graph-skills (explain) | plotting tolerance ±1 small square; gradient method mark = two points on the line, then the tolerance; **tangent method added** for a curve; one line only ("tramlining" loses), judged against a band; why scattered points give only an estimate | 2H June 2022 Q4(b)(i)–(ii); 1H June 2025 Q2(b)(iii), Q6(b)(ii); Nov 2021 Q4(d)(iii) |
| key-concepts / proportionality (table, worked) | "inversely proportional" is not the safe phrase for a falling curve (allowed 2022, ignored 2025) — say decreases and non-linear; show the division or the doubling ("ignore simple quoting of data"); how to test for proportion by experiment | 2H June 2025 Q7(b)(iii); June 2022 Q8(b)(i); June 2019 Q3(b)(ii); Nov 2021 Q6(c) |
| key-concepts / planning-practical (explain, steps, kc-t6-q1, kc-t6-q2, intro) | "each step is a mark / one mark per row" → 6-mark method questions are **levelled** against indicative content (the seven steps cover it); repeat-and-mean as one phrase, credited as a pair, ignored as an *improvement*; the circuit diagram is credited; variable resistor in series to keep the current small; spring details (read both lengths and subtract; mm rule, pointer, smaller steps, larger range) | 1H June 2023 Q9(c); 2H June 2023 Q9(b); June 2024 Q9(d); 2H June 2018 Q10(b); June 2024 Q8(a); June 2023 Q2(b)(iv); Nov 2020 Q6(a)(ii)–(iii) |
| key-concepts / evaluating-methods (explain) | anomalous = much further from the mean (name the value, then that reason); "Explain one improvement" = improvement + matching reason, "more accurate / precise" refused; better resolution credited where the instrument is the limit; repeats ignored | SAM Q4(b); 1H June 2018 Q6(c); June 2019 Q6(a); 2H June 2022 Q8(c)(i); June 2024 Q8(b)(i) |
| key-concepts / estimation (blurb, explain) | "Estimate" = calculation on given approximate data or a graph read-off, marked to a range; the sensible-values table kept for sense-checking | 1H June 2022 Q8(a); 2H June 2024 Q3(d) |

No stored answer changed (kc-t3-q6 and kc-t2-q6 are written questions and
kept their ids). `check_topic.js key-concepts` passes on both tiers
(78 numerics, 40 choices). Topic 2's planning section was given the same
repeat / light-gate corrections in its own commit.
