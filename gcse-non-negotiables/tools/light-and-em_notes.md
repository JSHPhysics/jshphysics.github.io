# Topic 5 — Light and the electromagnetic spectrum: SOP notes

Build: `python3 tools/build_light_and_em.py && python3 tools/build_manifest.py`.
Modules: `le_diagrams.py` (the ray diagrams as SVG), `le_types.py` (the two
calculation types the topic did not have: `em-wave-speed`, `lens-power`),
`le_nn_a.py` (N1–N6), `le_nn_b.py` (N7–N11, N11 = key words), `le_tricky.py`
(T1–T10 and the flashcards).

## Step 1 — lists approved

Author approved the N1–N11 / T1–T10 lists (2026-11-17) with three notes,
all applied: no critical-angle formula — the definition, the i–r graph
(critical angle where r = 90°) and the method; the radiation practical can
be a Leslie cube or painted cans of hot water; the refraction practical
is the traditional glass-block one, and students must be able to describe
the method for i against r and the method for finding the critical angle.

## Step 2 — checked against the content list and examiners' reports

Spec (copy at trafalgarschool.org.uk, 5.1–5.24): Physics-only 5.1P–5.6P
and 5.15P–5.19P → P tag on N1, N3, N4, N5, N10, T3, T4, T6, T7. Higher-only
(from a school checklist, bold not visible in the spec copy): 5.13, 5.16P–
5.18P, 5.23 → H on T5 and T6, and on the two 5.23 questions in T8. N2
(refraction) is untagged because 5.9 and 5.14 are for everyone.

Reports and mark schemes read: 1H June 2022 report, 1H June 2023 mark
scheme, 1H June 2024 mark scheme, 1H June 2025 report.

| Series / Q | Examiner / scheme | Where it went |
|---|---|---|
| 1H 2025 Q5(a) | refraction procedure (4): candidates described refraction instead of the procedure; a diagram first helps | T1 explain and worked; T10 worked |
| 1H 2025 Q5(b)(iii) | multi-step v = fλ with standard-form subtraction and mixed units | T9 explain, worked and q2 |
| 1H 2025 Q7(a) | lens power: shorter focal length / more curved (thicker, fatter) = higher power; "stronger" too vague (2022) | N5 explain, worked and q3 |
| 1H 2025 Q7(b) | example of a real and a virtual image "answered poorly" | T4 explain and q3 |
| 1H 2025 Q7(c) | critical angle (3): what happens at it and beyond | N3 worked; T3 |
| 1H 2025 Q7(d), 1H 2023 Q8(b)(ii) | thermal equilibrium (4): absorbs, emits, rate rises with temperature, constant when rates equal; "rate" compulsory; "heat" allowed | T6 explain, worked, q1 |
| 1H 2025 Q3(b)(i) | "sound" given as an EM wave | N6 explain and q2 |
| 1H 2024 Q4(a) | gamma not applied externally (uses) | N8 |
| 1H 2024 Q5(a)(i) | UVC: highest frequency but fully absorbed by the atmosphere | N9 explain and q5; T5 |
| 1H 2024 Q5(a)(ii) | f from 280 nm: 1.07 × 10¹⁵ Hz | em-wave-speed p3 |
| 1H 2024 Q5(b) | fluorescence (4): UV absorbed → electrons to higher level → fall back → visible light | T8 explain and q2 |
| 1H 2024 Q6(a) | law applies to all surfaces; reflection practical marks: mark positions, draw the normal perpendicular, label angles from the normal, protractor; "angle of refraction" rejected | N1 explain, q3; T1 |
| 1H 2024 Q6(b)(i) | ray entering along the normal: 90° to surface / i = 0 | N2 |
| 1H 2024 Q6(b)(ii) | critical angle method (3): increase i in the glass; until r = 90° / grazes / TIR just begins; that i is the critical angle; repeat and average | T3 explain and q2; T10 q2 |
| 1H 2024 Q6(c) | why virtual: cannot be projected / rays do not pass through it / same side / upright; "not real" ignored | T4 explain and q2; N11 |
| 1H 2023 Q6(b) | refraction caused by a change in speed; sound speeds up, light slows down entering water | N2 explain and q6; T2 |
| 1H 2023 Q6(c) | two EM waves + a use or effect showing energy transfer (credited pairs) | N8 explain and q4 |
| 1H 2023 Q8(a)(i) | ray along the normal does not bend | N2 q1 |
| 1H 2023 Q8(a)(ii) | critical angle from a graph (3): extend the curve, to r = 90°, read i | T3 graph, worked, q1, q4 |
| 1H 2023 Q8(b)(i) | black vs white surfaces: better absorber / better reflector | T7 explain and q6 |
| 1H 2022 Q1(b) | magnification from a diagram: same scale, no parallax; increase magnification: fatter lens / shorter f / change object distance | T4 explain and q5 |
| 1H 2022 Q1(c) | focal length: candidates stopped at 1/f | lens-power type, T9 |
| 1H 2022 Q9(b)(i) | v = fλ: GHz not converted | em-wave-speed type, N6 |
| 1H 2022 Q9(c) | X-rays vs radio (6, levelled): Level 3 needs production — "very few knew the oscillation of electrons in circuits was the source of radio waves" | T8 explain and worked |

No question on colour (5.3P), the spectrum order as such, or the radiation
practical's method appeared in these four series; those follow the spec.

## Step 3 — redraft

Findings were written straight into the sections. The user's three notes
reshaped T1, T3, T7 and T10.

## Step 4 — every calculation and standard explanation present

Calculations: v = fλ with c (type + N6 + T9), P = 1/f (type + N5 + T9),
magnification (T4), t = d/v (T9). Explanations: reflection and the two
kinds; refraction and its cause; speed/wavelength/frequency; critical
angle, TIR, optical fibres; colour; lens power and shape; the four lens
cases and real/virtual; EM wave properties and energy transfer; spectrum
order; uses; dangers; emission and temperature; thermal balance and the
Earth; surfaces; radio waves and atoms; fluorescence; both practicals.

## Steps 5–6 — questions against real exam questions

Numbers and situations from the papers above: 280 nm UV; 1.07 × 10¹⁵ Hz;
magnification 2.6; critical angle from a graph at ~42°; the Ceres
equilibrium; black and white plates; the UVC question.

## Step 7 — blind check

A separate agent recomputed every answer (sections and the two new
types) and read every explanation and diagram label against mark-scheme
wording without seeing the authoring. Findings, all fixed: em-wave-speed
p3's walkthrough quoted the scheme's "anything rounding to 1.1 × 10¹⁵" but
the checker would reject 1.1e15 — tolerance set to 5%; the worked example
stored 0.167 but wrote 0.17 — now 0.167 (3 s.f.), and it called a 1.8 GHz
phone signal radio waves while N8 files phones under microwaves — now
microwaves; the lens-power questions in T9 and the radiation-practical plan
in T10 are Physics-only inside untagged sections — now carry question-level
P badges; N6 said slowing down "is what refraction is" — now "is why they
refract"; T4 now says magnification is not on the equation list; the T5
table said "tan" where it meant "sunburnt". The checker also verified the
nine SVGs numerically (Snell ratio 1.49 in the block, lens images against
the lens formula).

## Step 8 — headless test

Playwright: every section numeric (12) and choice (37) and every type
question (12) entered through the UI and marked correct; no KaTeX errors;
no sideways scroll at 390 px; nine diagrams and three graphs render; the
booklet modal offers the notes mode; badges P and H show.
