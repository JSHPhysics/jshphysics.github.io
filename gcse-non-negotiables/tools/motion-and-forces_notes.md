# Topic 2 — Motion and forces: SOP notes

Build: `python3 tools/build_motion_and_forces.py && python3 tools/build_manifest.py`.
Modules: `mf_nn_a.py`, `mf_nn_b.py`, `mf_tricky_a.py`, `mf_tricky_b.py` (from the
LEH U4 page), `mf_keywords.py` (key words, N3L momentum chain, extra cards),
`mf_exam.py` (everything added at SOP steps 2–6, listed below).

## Rules for this page (author-approved; keep in every edit)

- Content was ported from the LEH U4 page (`LEH-U4-Forces-and-motion-revision/`); the two are now separate and need not be kept in step.
- Tags: momentum sections, `circular-motion` and `inertial-mass` carry H (2.20–2.26, 2.31); braking ∝ v² carries P (2.32P/2.33P).
- T12 applies the seven-step practical recipe to the trolley practical and links to Topic 1 T6 for the recipe itself; do not duplicate the recipe.
- x = ½gt² is not on the equation list and is not presented as expected in the exam.
- Conservation of momentum is explained through Newton's third law (T8), as the author asked.

## Step 1 — lists approved

Author approved the N1–N15 / T1–T13 lists (2026-11-16) with two additions:
explaining conservation of momentum through Newton's third law, and
questions that practise key words against mark-scheme wording.

## Step 2 — checked against the content list and examiners' reports

Spec points 2.1–2.33 all covered. Checked against the specification: only
2.32P and 2.33P are Physics-only (`braking-v-squared` tagged P); the
Higher-only statements are 2.20–2.22 (circular motion, inertial mass),
2.23–2.26 (momentum) and 2.31, so those sections carry the H tag.

Reports read: Paper 1H June 2022, June 2023, June 2025 (Pearson
`1ph0-1h-pef-*.pdf`); June 2023 1H mark scheme (PMT mirror). Findings
that touch this topic, and what was done with each:

| Series / Q | Examiner's comment | Action |
|---|---|---|
| 2023 Q2(b)(iv) | Constant velocity → acceleration is zero; many wrote "constant" | `t2-n9-q7` choice; flashcard |
| 2023 Q2(b)(i) | Describe a speed investigation (4): measure distance, time, speed = d/t, change the variable, repeat, graph | `t2-n8-q7` written with 6-row mark scheme (any 4) |
| 2023 Q3(b) | Free fall: majority scored 0 — did not pick the right equation or realise a = g | `t2-t3-q7` group: choose the equation, then calculate; flashcard |
| 2023 Q5(e) | Continue v–t graph below axis from 18 s; vertical line / line to the left not accepted | `t2-t1-q5` draw question (checked) ; flashcard |
| 2023 Q9(a) | Momentum unit kg m/s required; only issue was standard form with negative indices | `t2-n14-q7` numeric in standard form (H) |
| 2023 Q9(b), 2022 Q7(c)(i) | F = Δp/t: ms not converted to s; change of direction ignored (vector) | `t2-t9-q8` group (H): Δp with reversal, then F with 70 ms; two flashcards |
| 2023 Q9(c) | 6-mark levelled scheme: L3 = two procedure details + one statement; indicative content listed | `explain_levels` box in T12 with the statement/procedure table and the level descriptors; flashcard |
| 2022 Q3(a)(i) | "Why safer to drive slowly on a wet road" — needed physics (friction, braking distance), not road-safety talk | `t2-n15-q8` written |
| 2022 Q3(a)(ii) | m/s → km/h: convert one unit at a time | `t2-n2-q7` numeric; flashcard |
| 2022 Q3(a)(iii) | Reaction time to 2 s.f.; s.f. instruction lost marks | `t2-n15-q9` numeric with s.f. in the walkthrough |
| 2022 Q7(c)(ii), 2025 Q8(a)(iii) | N3L in a collision "deceptively difficult": must name both forces on the two different bodies, same type | `t2-t5-q7` written; the existing N3L chain in T8 already names both forces; flashcard |
| 2025 Q2(a)(i) | Used the weight instead of the resultant force in F = ma | `t2-n10-q7` numeric; "Careful" wording already in N10 explain; flashcard |
| 2025 Q6(b)(ii) | Tangent gradient at a point | already T2 (curved graphs) — no change |
| general | "Show that" → one more d.p.; "from rest" → u = 0; full marks for correct answer without working; no power-of-ten errors; g = 9.8 accepted | covered in Topic 1 T1/T2 and the EWAU convention; T3 explain already says "from rest means u = 0" |

## Step 3 — redraft

No list items removed. The additions above were placed in existing sections
rather than new ones so numbering stays N1–N16 (N16 = key words) and T1–T14.

## Step 4 — every calculation and standard explanation present

Calculations: speed (2.5), acceleration (2.6), v² − u² = 2ax (2.7), graph
gradient and area (2.8–2.9), F = ma (2.15), W = mg (2.17), p = mv (2.23),
conservation (2.24), F = Δp/t (2.27), stopping distances (2.28–2.33),
estimation (2.11) — all have a calculation type and section numerics.

Written explanations: scalar/vector distinction; N1L and resultant force;
N3L pairs vs balanced forces; inertial mass (2.18); circular motion (2.16);
terminal velocity; conservation of momentum via N3L; safety features via
F = Δp/t; reaction-time and stopping-distance factors; the core practical
(2.19) with the seven steps and the levelled scheme.

## Steps 5–6 — questions against real exam questions

Key-word questions (`mf_keywords.py`) use the mark-scheme forms: "rate of
change of velocity", "speed in a given direction", "force needed to
stop … / change its velocity … equal and opposite", "momentum before =
momentum after (closed system)", with the credited key words in bold.
Command words follow the Edexcel list (Topic 1 T1): state, describe,
explain, calculate, show that, estimate, draw, plot.

## Step 7 — blind check

A separate agent recomputed every stored answer and checked every
definition and model explanation against mark-scheme wording without
seeing the authoring modules. Findings (all fixed): the skydiver tangent gave 4 m/s² at the instant of
jumping, contradicting a = g with no air resistance — curve regenerated
with terminal velocity 50 m/s and initial gradient 10; t2-t10-q4 stored
74.2 against a walkthrough of 74 — now whole-number Highway Code
arithmetic; a flashcard mixed GPE (Topic 3) into the weight card — now
weight only; the reaction-time section claimed Edexcel expect students to
use x = ½gt², which is not on the equation list — reworded. The checker
also could not verify the H/P tags, which led to the spec check above
(circular motion and inertial mass gained H).

## Step 8 — headless test

Playwright: expand all cards, enter every numeric answer and click every
correct choice through the UI, check for KaTeX errors and horizontal
overflow at 390px, open the booklet. Run before the push.
