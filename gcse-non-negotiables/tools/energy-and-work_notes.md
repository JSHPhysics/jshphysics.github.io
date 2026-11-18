# Topics 3 and 8 — Energy, work and power: SOP notes

Build: `python3 tools/build_energy_and_work.py && python3 tools/build_manifest.py`.
Modules: `en_nn_a.py` (N1–N6), `en_nn_b.py` (N7–N11), `en_keywords.py` (N12,
18 definitions, flashcards), `en_tricky_a.py` (T1–T6), `en_tricky_b.py`
(T7–T11, flashcards). The seven calculation types already in the file are
embedded (`EMBEDS` in the build script).

One page, two spec topics: the page declares `subtopics` 3 and 8 and every
section carries `subtopic` so the "Both · Topic 3 · Topic 8" picker can
show one at a time (the author asked for this after approving the lists).
Topic 3 only: N10 insulation, N11 resources, T9 trends. Topic 8 only: N6
work, N7 power, T4 work the hard way, T5 power the hard way. Everything
else is shared.

## Rules for this page (author-approved; keep in every edit)

- T9 is trends only: comparing energy sources is not on the spec, so no "which source is best" questions.
- The page has a sub-topic picker (Both · Topic 3 · Topic 8): every section must declare `subtopic` (`["3"]`, `["8"]` or both); a type embedded in a hidden section hides with it.
- Energy is described in stores and pathways; "burning fuel" wording follows the blind-check fix in the notes below.

## Step 1 — lists approved

Author approved the N1–N12 / T1–T11 lists (2026-11-17) with one change:
T9 is "patterns and trends" only — comparing sources is not required.

## Step 2 — checked against the content list and examiners' reports

Spec (issue used: the copy at trafalgarschool.org.uk; numbering 3.1–3.14,
8.1–8.15): no statement in Topics 3 or 8 is Higher-only or Physics-only,
so no H/P tags. Every statement is covered: 3.1/8.8 GPE (N4), 3.2/8.9 KE
(N5), 3.3/8.2 diagrams (N3), 3.4/3.6/8.3 conservation (N2), 3.5/8.1 the
five situations (T1), 3.7/3.8/8.10/8.11 dissipation (N9, T8), 3.9/3.10
lubrication, insulation, walls (N10, T8), 3.11/8.15 efficiency (N8, T6),
3.12 increasing efficiency (T6), 3.13 resources (N11), 3.14 trends (T9),
8.4 ways of changing energy (N1), 8.5–8.7 work (N6, T4), 8.12–8.14 power
(N7, T5).

Reports and mark schemes read: 1H June 2022 report, 1H June 2023 mark
scheme, 1H June 2024 mark scheme, 1H June 2025 report, 2H June 2022 report,
2H June 2023 mark scheme, 2H June 2024 mark scheme, 2H June 2025 report.
(The 1H and 2H June 2023 reports were not reachable; their mark schemes
were used instead.)

| Series / Q | Examiner / scheme | Where it went |
|---|---|---|
| 2H 2025 Q2(a) | GPE → KE: cm not converted to m; square root dropped | T2 worked (1.6 kg trolley, 26 cm), N4 q5, the "four traps" table in T3 |
| 2H 2025 Q2(a)(iii) | "how to reduce the gap" wants a method, not "reduce friction" | T2 explain and q6; flashcard |
| 2H 2025 Q2(b) | power of a student: mass used instead of weight; s.f. confused with d.p.; 409.41 → 410 | N7 explain and q5 (48 kg, 2 s.f.), T5 explain |
| 2H 2025 Q8(b)(i) | area under F–x graph: extension in cm not converted | T7 explain and q4 |
| 2H 2025 Q9(b) | work done confused with moment of a force | T4 explain; flashcard |
| 2H 2024 Q7(a) | work done → distance to 3 s.f.; 11.53 scores 2 of 3 | N6 q2 |
| 2H 2024 Q7(b)(i) | method for GPE: balance/scales for mass, metre rule for height, zero the balance, same reference point, select GPE = mgh | N6 q6 (measuring work), T5 q6, T11 table |
| 2H 2024 Q7(b)(iii) | why energy out < in: friction / heating / to surroundings accepted; sound ignored | N9, T8 |
| 2H 2024 Q9(c)(ii) | temperature rise smaller than predicted: not all energy to the brick, transferred to surroundings; do not accept unqualified "lost", "not 100% efficient", sound | T8 explain, worked and q1 |
| 2H 2023 Q8(a)(i) | KE of a car in kJ; power-of-ten errors get 1 mark | N5 worked (1200 kg, 16 m/s) |
| 2H 2023 Q8(a)(ii) | t = E/P with MJ and kW, answer in hours; 7.2 = conversion error | N7 q4 |
| 2H 2023 Q8(a)(iii) | regenerative braking: kinetic store → chemical store of the battery | (Topic 8 is served by N1/T1 store language; no separate item) |
| 2H 2023 Q9(a)(i),(ii) | force from work; total work from 64% efficiency (2800 J) | N6 q3, N8 q3 |
| 2H 2023 Q9(a)(iii) | why more energy needed with a pulley: mass of pulley/rope, rope stretches; friction ignored | T4 q6 |
| 2H 2023 Q9(b) | 6-mark pulley-efficiency plan: L3 = two data methods + two processing steps | T11 explain and q2 |
| 2H 2022 Q7(a)(i),(ii) | GPE with km → m and 2 s.f.; KE: v not squared | N4, N5, T3 |
| 2H 2022 Q7(a)(iii) | work done by air resistance; work done against gravity; "as GPE decreases KE increases" wrong for a powered vehicle | T1 explain and q4 |
| 2H 2022 Q7(b)(ii) | input from 27% efficiency: "0.27 × input = output" | T6 explain and q1 |
| 1H 2025 Q6(a)(iii) | slope: GPE at top, KE at bottom, dissipated = difference | T2, T4 q5 |
| 1H 2024 Q2 | GPE → height; KE → speed (54.29 then 7.4; 54 scores 2 of 3); thermal store; efficiency 950/980 = 0.97 (97 or 0.97% scores 1) | N5 q3, N8 worked and q1, N9 |
| 1H 2024 Q10(b)(ii) | improving an insulating board: thickness, density, air gap; "add more insulation" rejected | N10 |
| 1H 2023 Q3(a) | GPE → height 2.6 m; KE 30 J (60.5 missing ½, 2.52 v not squared); impact: kinetic store → elastic / thermal / dissipated | T1 worked (ball hits wall), T3 table |
| 1H 2023 Q3(b) | drop height from impact speed via v² = 2gh | T2 q2 |
| 1H 2023 Q10(a)(i) | 7% × 1300 J = 91 J; 0.91 scores 1 | N8 q2 |
| 1H 2022 Q2(b) | insulation investigation: thermometer in the water; controls = volume of water, volume of insulator | N10 q5 |
| 1H 2022 Q2(c) | describe conductivity–density graph: non-linear, levels off, not two values | N10 explain and q6 |
| 1H 2022 Q5(b) | KE of aircraft in standard form; transfer on landing needs a pathway (friction / air resistance) | T3 q5, N9 |
| 1H 2022 Q9(b)(ii) | 55% used as 55; answer smaller than useful energy should prompt a check | N8 explain and q5, T6 q7 |

No question on energy resources or trends appeared in these eight
papers; N11 and T9 follow the spec wording.

## Step 3 — redraft

The findings were written straight into the sections (the lists were
drafted after the reports were read), so no separate exam-additions
module this time.

## Step 4 — every calculation and standard explanation present

Calculations: GPE, KE, work, power, efficiency (and their rearrangements),
GPE ↔ KE, work = KE for braking, chains (kettle, lift, braking), areas and
gradients, estimation. Written: the eight stores and four pathways, the
law and closed systems, the five situations, dissipation, lubrication,
insulation, wall thickness and conductivity, efficiency increase, the
seven sources and how each is used, trends, the two practicals.

## Steps 5–6 — questions against real exam questions

Numbers and situations were taken from the papers above where the mark
scheme was available (1200 kg at 16 m/s; 126 MJ at 17.5 kW; 1800 J over
1.2 m; 64%; 7440 J and 645 N; 5.8 J and 320 g; 950/980; 7% of 1300 J;
1.6 kg and 26 cm; 48 kg to 2 s.f.). Command words: state, describe,
explain, calculate, suggest, estimate.

## Step 7 — blind check

A separate agent recomputed every answer and read every explanation
against mark-scheme wording without seeing the authoring. Findings, all
fixed: en-t10-q4 stored 6.48 MJ (efficiency multiplied, not divided; the
walkthrough said 162) — now 162; en-n8-q3 walkthrough said ≈ 2800 against
a stored 2810 — now ≈ 2810 (3 s.f.); the N11 blurb said comparing sources
is not required, but 3.13 asks to compare the *ways they are used* —
reworded; en-n9-q1 called friction "a mechanical transfer, by heating"
(two pathways in one breath) — reworded; en-t8-q5 said burning fuel "does
work" — now transfers by heating; the Sankey figure's label gave pixel
widths 40 : 30 : 10 beside a caption saying 100 : 75 : 25 — now one set.
Noted, not changed: N12 key words is tagged both topics although some
terms belong to one.

## Step 8 — headless test

Playwright: every numeric and choice answer entered through the UI under
"Both" (72 numeric, 28 choice, all correct); the picker filters sections,
embedded types, flashcards and the progress count, and the choice
survives a reload; no KaTeX errors; no sideways scroll at 390 px; the
booklet modal offers the notes mode; the A-level site and Topic 2 are
unchanged.
