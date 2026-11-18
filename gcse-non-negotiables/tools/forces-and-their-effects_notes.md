# Topic 9 — Forces and their effects: SOP notes

Build: `python3 tools/build_forces_and_their_effects.py && python3 tools/build_manifest.py`.
Modules: `fe_diagrams.py` (free body, interaction pair, 3-4-5 resultant,
resolving a pull, closed triangle, spanner moment, balanced beam, crowbar,
meshing gears, hand winch), `fe_nn.py` (N1–N10, N10 = key words),
`fe_tricky.py` (T1–T8 and the flashcards). The two existing calculation
types (`moment`, `balance`) are embedded in N6 and N7 (`EMBEDS`).

## Rules for this page (author-approved; keep in every edit)

- 9.3 (scale drawings, resolving, equilibrium by drawing) and 9.5 (resultant on an isolated object or system) are Higher-only: T1–T4 carry H, and the one 9.5 question in N5 (the car-and-trailer system) carries a question-level H. 9.6P–9.9P are Physics-only: N6–N8 and T5–T7 carry P; the two Physics-only key-word questions carry P.
- The winch section (T7) is built on the author's point about June 2025 2H Q9(b): an equation in general form ("moment = force × distance") reached Level 2; the same equation written in the parts of the machine ("moment of the handle = effort × length of handle"), or said in words, reached Level 3 — any of the listed equations would do. Keep the two-column table and the Level 3 model answer in that shape.
- Gears: the force between the teeth is the same on both wheels; the moment is proportional to radius; "turns × teeth is the same for both gears" (never "turns ratio = teeth ratio").
- On a picture of a situation a contact force is drawn at the point of contact; on a free body diagram every force is drawn from the centre. Both rules stay, each labelled with its diagram type.
- The 2025 winch question paper itself was not seen; the winch is modelled as handle on small gear Y, Y driving large gear X, X on the drum.

## Step 1 — lists approved

Author approved the N1–N10 / T1–T8 lists (2026-11-18) with one addition:
the June 2025 Paper 2H winch 6-marker (Q9(b)) is T7, and the Level 2 /
Level 3 distinction he described — an equation written in general form
("moment = force × distance") reached Level 2; the same equation written
in the parts of the machine ("moment of the handle = effort × length of
handle"), or said in words, got into Level 3; any of the listed equations
would do — is the centre of that section (the two-column table).

## Step 2 — checked against the content list and examiners' reports

Spec (copy at trafalgarschool.org.uk, 9.1–9.10). 9.6P–9.9P Physics-only;
9.3 and 9.5 Higher-only (bold in the Pearson spec; the school checklist
used for Topics 1–7 covers Paper 1 only, so the spec is the source here).
Coverage: 9.1a/b (N1, T8), 9.1c (N2), 9.2 (N3), 9.3 (T1, T2, T3), 9.4 (N4),
9.5 (N5, T3, T4), 9.6P/9.7P (N6, T5), 9.8P (N7, T5), 9.9P (N8, T6, T7),
9.10 (N9, T8).

Reports and mark schemes read: 2H June 2022 report, 2H June 2023 report,
2H June 2024 mark scheme, 2H June 2025 report and mark scheme. The 2025
question paper itself could not be opened (Pearson's copy gone, the PMT
mirror needs the author's permission), so the winch is modelled as the
standard layout — handle on small gear Y, Y driving large gear X, X on the
drum — which matches every line of the scheme's indicative content.

| Series / Q | Examiner / scheme | Where it went |
|---|---|---|
| 2H 2022 Q6(b)(i) | "most common detracting mistake was not converting cm to m" | N6 explain |
| 2H 2022 Q6(b)(ii) | separate moment calculations for each force, then summed | T5 explain |
| 2H 2022 Q6(b)(iii) | principle of moments: "just saying clockwise moments = anticlockwise moments would not score" — totals must be stated | N7 explain, N10 |
| 2H 2023 Q4(a)(iv) | force arrow must start/end at the point where it acts; normal force perpendicular to the surface | N1 explain |
| 2H 2023 Q5(b) | floating magnet: fields interact; repulsion balances weight; "magnetic fields" only in terms of repelling | N1 explain and worked |
| 2H 2023 Q6(b)(i) | principle of moments questions "expect a calculation of moments using force × distance", not ratios | N7 explain and q4 |
| 2H 2023 Q6(b)(ii) | biceps 212 N: total-moment or extra-force route | T6 explain and q5 |
| 2H 2023 Q7(a)(ii–iii) | "say how it will improve, not why" | N9 explain |
| 2H 2023 Q9(a)(iii) | wasted work other than friction: lifting rope/pulley, stretching rope; "heat" and "squeaky wheels" are friction | T8 explain and q2 |
| 2H 2024 Q1(b) | electric field = region where a charge experiences a force | N1 explain |
| 2H 2024 Q4(a) | normal contact force arrow perpendicular to the surface | N1 |
| 2H 2024 Q6(a) | unit of moment N m | N6 explain and q2 |
| 2H 2024 Q6(b)(i) | principle: 1 mark "sum of clockwise = sum of anticlockwise (about the same point)", 1 mark "for a system in equilibrium" | N7 explain, q1, N10 |
| 2H 2024 Q6(b)(ii) | F2 = F1 d1 / d2, 75 N | N7 worked pattern |
| 2H 2024 Q6(c) | gear ratio 3× → one third the rate; add a 10-tooth gear (half the teeth) to double the speed | N8 explain and q5 |
| 2H 2025 Q2(a)(iii) | reduce friction: a method ("lubricate the wheels"), not a reason — general answers scored nothing | N9 explain, worked, q2; T8 |
| 2H 2025 Q8(b)(iii) | free body diagram: vectors through the centre of the block, labelled with size; edge arrows penalised | N4 explain and q2 |
| 2H 2025 Q8(c) | resultant by scale drawing (parallelogram / second vector) or Pythagoras; direction + size within tolerance | T1 explain |
| 2H 2025 Q9(b) | winch 6-marker: indicative content (sizes, equations, links "moment of effort = effort × length of handle", "work done on load = load × distance raised"); errors: work confused with moment (capped L2), "force of Y on X increased", sizes without effect (L1); L3 example answer uses the distance argument | T7 whole section, T6 |

## Step 3 — redraft

Findings written straight into the sections. The forearm (2023) is used
as the distance-multiplier example in T6 rather than as a separate
section.

## Step 4 — every calculation and standard explanation present

Calculations: resultant along a line; resultant and components by scale
drawing with Pythagoras check; moment = F d; principle of moments with
one or several forces, a beam's weight, a pivot off-centre, tipping and
counterweights; pivot force; lever effort/load and distances moved; gear
turn ratios; the winch end to end (load moment → tooth force → handle
moment → effort, and work per turn). Explanations: contact and
non-contact forces and fields; interaction pairs vs balanced forces;
vector vs scalar with examples; free body diagram rules; zero resultant
and motion; perpendicular distance; principle of moments wording; levers
and gears as force/speed multipliers; work the same through a machine;
the Level 2 / Level 3 distinction; friction direction, size, energy,
methods and uses; lubrication.

## Step 7 — blind check

A separate agent recomputed every numeric answer (44 of 44 correct,
including the winch worked example and the five-part fe-t7-q3 from first
principles), every worked-example and diagram figure (88/88), every choice
and model answer, the tags, the flashcard section ids and the HTML/TeX.
Findings, all fixed: fe-t7-q3d's tolerance would have failed 0.13 m (now
5 %); `resultant-line` was labelled 9.5 (a Higher statement) while holding
Foundation content — relabelled, and its car-and-trailer system question
tagged H; the force-arrow rule in N1 (at the point of contact) and the
free-body rule in N4 (from the centre) now say which diagram each applies
to; "turns ratio = teeth ratio" reworded as turns × teeth the same for
both gears (three places); the 2023 biceps sentence no longer reads as
212 N for a 4.8 N m moment; the N6 checklist no longer says "recall" an
equation; the two Physics-only key-word questions tagged P; a "(T6)"
cross-reference that moves under the Foundation filter replaced with the
section's name; gravitational field strength dropped from the vector
list; the 50° marked on the angled-spanner drawing, the lever and winch
drawings put to scale, the beam's turning arcs drawn in the right sense;
the door worked example's part (b) made its own step. The keyword
flashcards' `<b>` tags are fine: the app renders fact answers through
`prose()` as HTML, as in every earlier topic.

Found while fixing the diagrams: the app never defines `--ink` (its ink
colour is `--line`), so every diagram stroke painted with `var(--ink)`
since Topic 5 computed to `none` (the winch rope was invisible) and fills
to black whatever the colour scheme. `figure.diagram { --ink: var(--line) }`
in `sections.css` (copied to `non-negotiables/`) fixes all topics in both
light and dark mode; checked on the winch and the Topic 7 orbit.

## Step 8 — headless test

Playwright at 1180 px: 30 section numerics, 34 choices and the 12 type
practice answers entered through the UI and marked correct; no KaTeX
errors; 10 diagrams render; P badges on N6–N8 and T5–T7, H on T1–T4; 90
flashcards. At 390 px no sideways scroll; the booklet modal offers the
notes mode.
