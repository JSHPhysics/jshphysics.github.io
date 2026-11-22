# Topic 10 — Electricity and circuits: SOP notes

Build: `python3 tools/build_electricity_and_circuits.py && python3 tools/build_manifest.py`.
Modules: `el_diagrams.py` (symbol chart, meters, series/parallel, the I–V
practical circuit, the series and parallel test circuits, the plug, the
a.c./d.c. traces, the LDR sensing circuit — the circuit symbols are
drawn by helpers so every circuit uses the same symbols as the chart),
`el_nn_a.py` (N1–N6), `el_nn_b.py` (N7–N12, N12 = key words; the I–V and
LDR/thermistor graphs are `graph()` specs), `el_tricky.py` (T1–T9 and
the flashcards). The seven existing calculation types are embedded
(`EMBEDS`).

## Rules for this page (author-approved; keep in every edit)

- **A fuse melts.** The fuse wire heats up, melts and breaks the circuit.
  "Blows" is never written as a description of what a fuse does, anywhere
  on the site; fuses do not explode. The word appears only where it is
  flagged as the wrong word (N11, N12's "not this" column, T7's choice
  question).
- The whole topic is in Combined Science at both tiers: no section or
  question carries H or P.
- Edexcel asks for series circuits to be *calculated* (10.15) and
  parallel ones to be *explained* (10.14): parallel total resistance is
  found as V ÷ I from the branch currents, never from the 1/R formula.
- Resistance from an I–V graph is V ÷ I at the point, never the gradient
  (the 2024 scheme accepts "the gradient decreases so resistance
  increases" only as a comparison).
- Potential difference is "energy transferred per unit charge"; the
  volt is a joule per coulomb; current is "the rate of flow of charge".
- Spec kickers on section heads are written as ranges where there are
  more than four statements ("10.32–10.41"): a long comma list set the
  column width on phones and clipped every card (see Step 8).

## Step 1 — lists approved

Author approved the N1–N12 / T1–T9 lists (2026-11-18, "onwards to topic
10") with the fuse-language rule above.

## Step 2 — checked against the content list and examiners' reports

Spec (copy at trafalgarschool.org.uk, 10.1–10.42). No P statements; the
Pearson spec's bold could not be read from the text copy, and the topic
is CP10 in Combined Science at both tiers, so nothing is tagged.
Coverage: 10.1/10.8 (N1, T8), 10.2/10.4/10.7 (N2), 10.9–10.11 (N3),
10.5/10.6 (N4), 10.12/10.13 (N5), 10.3/10.14/10.15 (N6, T4), 10.16/10.17
(T1, T2, T9), 10.18 (N7, T3), 10.19–10.21 (N8, T5), 10.22–10.26 (N9, T8),
10.27–10.31/10.42 (N10, T6), 10.32–10.41 (N11, T7).

Reports and mark schemes read: 2H June 2022 report, 2H June 2023 report,
2H June 2024 mark scheme, 2H June 2025 report.

| Series / Q | Examiner / scheme | Where it went |
|---|---|---|
| 2H 2022 Q2(a) | R = V/I and P = V²/R "very high scoring" | N5, N10 |
| 2H 2022 Q2(b) | brighter lamp: needs the pd argument *and* the power argument — "rarely both" | T2 explain and q4 |
| 2H 2022 Q2(c) | practical circuit: "labelling and inserting the resistance wire carefully was the key" | T1 explain |
| 2H 2022 Q8(b)(i) | describe a trend: the trend *and* the non-linearity | N8 worked |
| 2H 2022 Q8(c)(i) | thermistor temperature method improvement: "very few scored" | T5 explain and q6 |
| 2H 2023 Q2(a) | voltmeter "often across the variable resistor or the battery"; "never connected in series" | N2 explain and q6 |
| 2H 2023 Q2(b)(iv) | variable resistor reduces current by increasing resistance; "slowing down the current" and "decreasing the resistance" rejected; confused with a thermistor; "fewer electrons per second collide with the ions" praised | N5 explain, N8, T8 |
| 2H 2023 Q8(b)(i) | E = IVt charging time: convert MJ and hours; a comparison only scores with the unit of the time stated | N10 explain, T6 |
| 2H 2024 Q2(a) | branch currents add to the battery current | N3 explain |
| 2H 2024 Q2(b)(i) | voltmeter in parallel with the resistors | N2 |
| 2H 2024 Q2(b)(iii) | R = 6.00 / 9.1 mA = 660 Ω; mA conversion | N5 worked |
| 2H 2024 Q2(b)(iv) | resistor removed from parallel: total resistance increases (1) because current decreases (1) and voltage stays the same (1); "fewer paths" | N6 explain and q4, T4 |
| 2H 2024 Q8(a) | I–V circuit: variable resistor in series, ammeter in series with the lamp, voltmeter in parallel with the lamp, 1 mark each | N2, T1 |
| 2H 2024 Q8(b)(i) | data logger: short time / simultaneous readings; "accuracy" ignored | T1 explain and q4 |
| 2H 2024 Q8(b)(ii) | lamp graph: current increases with pd (1); non-linear (1) | N7 explain and q2 |
| 2H 2024 Q8(b)(iii) | resistance from R = V/I at two points, or gradient decreasing as a comparison | N7 explain and worked, T3 |
| 2H 2024 Q8(d) | pd = energy transferred per unit charge (1); units J/C (1) | N4 explain and q1 |
| 2H 2025 Q3(b) | P = IV calculator slips ("250 ÷ 0.53") | N10 explain |
| 2H 2025 Q3(c)(ii) | fuse: wire melts (1) + breaks the circuit (1); answers not saying what the fuse does scored one | N11 explain and q3, T7 |
| 2H 2025 Q3(c)(iii) | other safety devices: circuit breaker, earth wire, cable clamp, socket covers, insulation | N11, T7 |
| 2H 2025 Q3(d) | thicker copper wire → lower resistance → carries current safely; "thicker insulation" wrong; "bigger" alone no marks | N9 explain and q4 |
| 2H 2025 Q4(c), Q10(a)(i) | mA not converted to A | N3 explain, N5 |
| 2H 2025 Q6(b) | diode: "allows current in one direction only"; "limits current" and "LED" scored nothing | N7 explain and q5 |
| 2H 2025 Q10(c) | series/parallel practical 6-marker: L3 both circuits with meters placed correctly, expected values, voltage sharing / current sharing / same current in series; L1 misplaced voltmeter, no parallel circuit, "confuses resistance and voltage" | T2 whole section, N6 |

## Step 3 — redraft

Findings written straight into the sections. The author's fuse rule
applied throughout: every fuse sentence says "melts".

## Step 4 — every calculation and standard explanation present

Calculations: Q = It (with mA and minutes), E = QV, V = IR (with mA and
kΩ), series totals and shares, parallel branch currents and total
resistance as V/I, resistance from an I–V graph at a point, P = E/t,
P = IV, P = I²R, E = IVt, E = Pt, current from a power rating and the
fuse choice, time from stored energy. Explanations: the atom and free
electrons; current, pd and resistance in the electron model; meter
placement; closed circuit and conservation of current; the volt; the
variable resistor; series and parallel rules and why; the three I–V
shapes and why; LDR and thermistor behaviour and the sensing-circuit pd
sharing; heating by collisions and low-resistance wires; the four power
equations; a.c./d.c.; the three wires; fuse, circuit breaker, earth
wire, switch in the live, live–earth danger, double insulation; the two
core practicals and the seven-step plans.

## Step 7 — blind check

A separate agent recomputed every stored answer (86 of 86 correct,
including all seven types), checked every choice, every model answer,
the tags, the flashcard section ids, the eight SVGs and the seventeen
graph specs, and searched for "blows" (every occurrence is flagged as
the wrong word; none describes a fuse). Findings, all fixed: el-t9-q1's
"any six" note had been passed as a string to `mark_scheme(extra=…)` and
came out as 28 one-letter bullets; two of the circuits type's practice
questions (p5, p6) carried a `Higher` board from when the types were
first written, hiding them under the Foundation filter — stripped in the
build (10.14/10.15 are at both tiers); the LDR flashcard read "ldr";
the 2022 Q2(c) citation in T1 now says it was the same circuit on a
resistance wire; "thermistor-like" in the night-light worked example;
"hundreds of kΩ" against a graph topping at 10 kΩ; the five section
graphs' axis labels now in the Edexcel "quantity in unit" form; the lede
said six equations (seven); "unit in base terms" in el-n4-q1; el-n10-q4
duplicated the worked example's 414 000 J. Spec sub-numbers were
re-checked against the fetched spec and stand (E = IVt is 10.27). The
charge and ohm types each have two practice questions with the same
answer (360 C, 12 V) from the original type data — left, since their
ids are live.

## Step 8 — headless test

`check_topic.js`: 79 section and type numerics and 38 choices entered
through the UI and marked correct; no KaTeX errors; 12 graphs and 8
diagrams render; no badges; 99 flashcards; booklet offers the notes
mode. At 390 px the page did not scroll sideways but every card was 490
px wide and clipped: the N11 head's comma list of ten spec numbers is
`white-space: nowrap` and set the column's minimum width. Fixed twice
over — `.skill-head .lessons` now wraps under 640 px (`sections.css`,
both sites) and the long kickers are written as ranges — and the check
script now fails when any card is wider than the phone screen, which
the earlier pages passed (350 px).

## Revisions

### 2026-11-22 — exam-wording verification against the question database

A separate agent compared 44 mark-scheme parts (`Question
DB/by-topic/topic-10.md`, 16 marked questions 2018–2025) with the page's
21 sections and 99 flashcards. Changes:

| Reference | Change | Scheme |
|---|---|---|
| electricity-and-circuits / circuit-symbols worked | voltmeter across the battery accepted when the resistor is the only component | 2H Nov 2021 Q8(a)(i) guidance |
| electricity-and-circuits / ohm-nn worked | 660 Ω is 2 s.f. (659.3…), not 3 | 2H June 2024 Q2(b)(iii) |
| electricity-and-circuits / ohm-nn (explain) | variable-resistor chain: increases resistance → keeps current small/constant → the current heats the wire; "slows" ignored not rejected | 2H June 2023 Q2(b)(iv) |
| electricity-and-circuits / series-parallel-practical (explain, worked, checklist) | lamp brightness: any three of five points, not "both arguments"; the 6-mark worked now makes the two comparisons the 2025 question asked for (cell current greater in parallel; pd across each resistor less in series) | 2H June 2022 Q2(b); June 2025 Q10(c) and Figure 23 |
| electricity-and-circuits / iv-characteristics (explain) | lamp alternative route needs "resistance increases" as well as the gradient; the diode question was two marks (battery supplies d.c. + one direction) | 2H June 2024 Q8(b)(iii); June 2025 Q6(b) |
| electricity-and-circuits / heating-effect (explain), el-n9-q4, worked | cable: any two of area / lower resistance / safely higher current, insulation a fallback mark, "thicker/wider" accepted; el-n9-q4 splits area and resistance and adds "less pd across the wires"; the heating worked is 2 marks and the dissipation step is marked as not a mark | 2H June 2025 Q3(d); Nov 2021 Q8(b)(iv); June 2018 Q8(b) |
| electricity-and-circuits / power-nn, power-hard (explain), flashcard | "comparison scored only with the unit" → the conclusion is an independent mark ("5.8 h is less than 6 h, so justified"), credited even on a wrong time; bare correct answer 2 of 3 | 2H June 2023 Q8(b)(i) |
| electricity-and-circuits / mains (explain), keywords Fuse, mains-safety (blurb, chains), el-t7-q1, el-t7-q2, flashcards | fuse second mark is "so the current stops" ("breaks the circuit" accepted); the claim that "blows" never scores is dropped — the house word stays **melts** (the scheme leads with it); earth-wire chains carry "keeps the case at earth potential (0 V)" (2019 Level 3 wording) | 2H June 2025 Q3(c)(ii); June 2019 Q10(b) |
| electricity-and-circuits / keywords d.c. and a.c. | "Not this" is the bare label: "it is d.c. / a.c." is not a description of the movement of charge | 2H June 2019 Q10(a)(ii) |

Note for the author: the 2025 scheme's guidance reads "allow fuse blows /
breaks circuit"; the page keeps *melts* as the only word it teaches and no
longer claims that "blows" fails. No stored answer changed;
`check_topic.js electricity-and-circuits` passes on both tiers. H list in
the report: "state the unit of charge" as its own mark (2025 Q4(c), "As"
accepted), deduce the arrangement from R = V/I (2018 Q8(c)), the doubling
test for "directly proportional" (2019 Q3(b)(ii)), parallel resistors
"trend + non-linear + two values" (Nov 2020 Q8(a)(iv)), "more precise =
more s.f." (2022 Q8(c)(ii)), variable resistor "in series" as the second
mark (2025 Q10(a)(ii)), a.c./d.c. differences in the movement of charge
(2019 Q10(a)(ii)), the 2 s.f. mark (2019 Q10(a)(i)).
