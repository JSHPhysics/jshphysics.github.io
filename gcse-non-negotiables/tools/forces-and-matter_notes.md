# Topic 15 — Forces and matter: SOP notes

Build: `python3 tools/build_forces_and_matter.py && python3 tools/build_manifest.py`.
Modules: `fm_diagrams.py` (two forces on a spring, the spring practical
with its graph, pressure normal to every surface with the aeroplane
window, two tanks of different density, where upthrust comes from, and
wood / ice / steel floating or sinking — painted with the `--ink` /
`--accent` variables and placed in N1, N6, N8, N10, N12 and T7),
`fm_nn.py` (N1–N13, N13 = key words), `fm_tricky.py` (T1–T7 and the
flashcards; the force–extension, compression, atmospheric-height and
pressure–depth graphs are `graph()` specs in the two modules). The five
existing calculation types are embedded: `hooke` in N3 (`hooke-nn`),
`elastic` in N4 (`energy-stored`), `fx-graph` in N5 (`linear-nonlinear`),
`pressure` in N7 (`pressure-nn`), `liquid` in N11 (`liquid-pressure`).
No type changes its boards.

## Rules for this page (author-approved; keep in every edit)

- **Tiers.** From the Pearson spec (the school checklist covers Paper 1
  only; the bold was read from a listing that keeps it): 15.1–15.6 are
  both tiers and both sciences — N1–N6, T1–T3 untagged; 15.7P–15.17P
  are Physics only — N7–N12 and T4–T7 carry P; only **15.14P** (the
  liquid-column equation) is Higher, so N11 carries H and P and the
  `liquid` type keeps its Higher badge. The Physics-only key words
  (pressure, fluid, atmospheric pressure, upthrust, floating) are marked
  in the N13 table and their questions tagged P.
- **Extension, not length, in metres.** Every spring calculation writes
  $x$ = loaded − unloaded first and converts mm or cm to m before
  $F = kx$ or $E = \tfrac{1}{2}kx^2$. The 2023 and 2025 reports' errors
  (1600 N for 1.6 N; $k$ 100 times too small; energy 100 times too
  large) are quoted, with the partial credit each kept.
- **Pressure areas.** Total contact area ($n$ × one foot), squared unit
  conversions (1 mm² = 10⁻⁶ m²), and the difference in pressure when a
  surface has fluid on both sides. "Weight (force) spread over a larger
  area → less pressure" is the explanation; "mass spread out" is not.
- **Fluid pressure is normal to the surface**, drawn from the point on
  the surface, towards it; total pressure = liquid + atmosphere.
- **Height vs depth graphs.** Atmosphere: falls, non-linear, quote
  numbers, less air above / smaller weight of air / less dense; gravity
  is not the reason. Liquid: straight, proportional to depth, intercept
  = atmospheric pressure; denser liquid steeper from the same intercept.
- **The liquid-column equation** is $P = h\rho g$ with $\rho$ in kg/m³
  (not 10): sense-check the answer — 10 m of water ≈ 100 kPa.
- **Upthrust = weight of fluid displaced**, from the pressure difference
  between the bottom and top faces. The 2025 chain (loss in weight →
  weight of fluid displaced → volume → density) is written stage by stage
  with its marks. Floating is explained by forces (upthrust = weight) or
  by density **with the displaced-volume link** (the 2022 second mark);
  "it is light" is neither.
- Equations: $F = kx$, $E = \tfrac{1}{2}kx^2$, $P = F/A$ and
  $P = h\rho g$ are on the list; checklists say "use".

## Step 1 — lists approved

Author approved N1–N13 / T1–T7 (2026-11-20, "go ahead").

## Step 2 — checked against the content list and examiners' reports

Spec 15.1–15.17P from the Pearson PDF (all seventeen statements read);
the Higher-only marker (15.14P alone) from a listing that preserves the
spec's bold. Coverage: 15.1 (N1), 15.2 (N2), 15.3 (N3 + type, T1), 15.4
(N4 + type, T2), 15.5 (N5 + type, T2), 15.6 (N6, T3), 15.7P (N9, T5),
15.8P/15.9P (N8, T4), 15.10P/15.11P (N7 + type, T4), 15.12P/15.13P (N10,
T5), 15.14P (N11 + type), 15.15P/15.16P (N12, T6), 15.17P (N12, T7).

Reports and mark schemes read: 2H June 2022 report (school mirror), 2H
June 2023 mark scheme (PMT), 2H June 2024 mark scheme (PMT; Pearson's
report for that series came back garbled), 2H June 2025 report
(Pearson). The spring core practical has not been a 6-mark method
question on 2H in 2022–2025; its method marks come from 2023 Q7.

| Series / Q | Examiner / scheme | Where it went |
|---|---|---|
| 2H 2022 Q3(c) | wood floats: "less dense than water and would float" (most); the second mark, "less water would be displaced", rarely scored | N12 explain, T7 explain and q1, facts |
| 2H 2022 Q4(a)(i) | donkey's weight on four hooves: "not correctly calculating the area as 4 × area of one hoof" was the common mistake (1 of 2) | N7 explain and worked, T4 table and q1 |
| 2H 2022 Q4(a)(ii) | camel's feet: greater surface area, exerts less pressure; "mass spread out" unworthy of the second mark — force or weight spread out would have scored | N7 explain and q5, T4 explain and q5 |
| 2H 2022 Q4(c) | pressure–depth line for sea water: density up → pressure up; steeper gradient; linear; air-pressure intercept | N10 explain and q3, T5 table and worked |
| 2H 2023 Q7(a)(i) | $F = kx$, 260 N/m × 6.2 mm: selection and substitution (1), evaluation (1), 2 s.f. (1) = 1.6 N; 1600 N two marks | N3 worked, T1 table |
| 2H 2023 Q7(a)(ii) | change in length: read the top of the spring against the ruler (1), read again pressed down (1), subtract (1); alternative 0.39 = 260 × change, 1.5 mm with the unit | N3 explain, N6 worked, T1 explain and q2 |
| 2H 2023 Q7(a)(iii) | a change to locate the top of the spring accurately (1) and how it is used (1); parallax; ignore unqualified accuracy / precision | N6 table and q2, T3 explain and q2 |
| 2H 2023 Q7(b) | reading the graph's units: "6 N up"; distractors summed the weights | T2 explain |
| 2H 2023 Q4(a)(i)–(iii) | 80 000 − 23 000 = 57 000 Pa; $F = PA$ = 80 000 × 0.094 = 7500 N (57 000 substituted: 1 mark max); force less on the small window, pressure the same | N8 explain, worked and q4; T4 table |
| 2H 2023 Q4(a)(iv) | arrow towards the outside (1), normal to the surface at X (1) | N8 explain and figure |
| 2H 2023 Q4(b)(i)–(ii) | height up → pressure down (1), non-linear (1), use of numerical data (1); explanation any one of less dense / smaller weight of air above / lower temperature | N9 explain and worked, T5 table |
| 2H 2023 Q6(c) | floating ball: upthrusts equal (1); weight of ball = weight of water displaced, sea water more dense, smaller volume displaced to give the same weight (any three) | N12 worked, T6 explain and q3 |
| 2H 2024 Q4(a) | force direction: normal to the surface, towards it | N8 explain |
| 2H 2024 Q4(b) | $F = PA$: substitution (1), 576 N (1), rounded to 2 s.f. 580 N (1) | N8 q5, T4 table and q4 |
| 2H 2024 Q4(c) | pressure decreases as height increases / negative correlation (1), non-linear — curved, not proportional, gradient changes (1); reading 30–34 kPa; % change (74 − 104)/104 × 100 = −29 %, dividing by 74 one mark | N9 explain, T5 table and q3 |
| 2H 2025 Q1(a)(i) | $h$ from $P = h\rho g$: most rearranged correctly; some used 10 for the density of water and got 35 m — "look at the result of a calculation to see if the value makes sense" | N11 explain, worked and q5, facts |
| 2H 2025 Q1(a)(ii) | pressure/force arrow at X: downward arrow from or to the point; an arrow too far from the point scored zero | N8 explain |
| 2H 2025 Q1(c) | $P = F/A$: forgetting mm² → m² gave "an answer that was a million times too large" (1 of 2) | N7 explain, T4 table and q2 |
| 2H 2025 Q1(d) | the force below a bigger hole is greater | N10 explain |
| 2H 2025 Q8(b)(i) | energy from the area under the graph: convert cm to m (1), read the points (1), area (1); not converting gave 100 times too large, two marks for clear working | N4 explain, T1 table, T2 table |
| 2H 2025 Q8(b)(ii) | spring constant: extension in cm given as N/m was 100 times too small (1 of 2); substituting the energy into $E = \tfrac{1}{2}kx^2$ accepted as an alternative | N3 explain, T1 table and q5 |
| 2H 2025 Q9(a)(i) | upthrust (1), equal to the weight of liquid displaced (1), liquid more dense than air (1); "only a very few candidates correctly linked the loss in weight with the weight of liquid displaced" | T6 explain and q2 |
| 2H 2025 Q9(a)(ii) | four stages: loss in weight 2 N (1), volume $1.43 \times 10^{-4}$ m³ (1), density equation with the block's weight (1), $4.9 \times 10^{3}$ kg/m³ (1), error carried forward; starting from 5 N scored 3 of 4; "less confidence in the application of Archimedes' principle" | T6 table, worked, q1 and q4 |

## Step 3 — redraft

N1 draws the three cases (two forces, one force, a hook) so the second
force is named every time; N3 and T1 put the 2023 and 2025 unit slips
in tables with the credit each kept; N5's graph is the worked example's
and the practice group reads it three ways; N6 carries the 2023 method
marks as a table and the seven steps go to T3; N8 uses the 2023
aeroplane window for the normal-force picture and the pressure
difference; N9 and T5 separate the height curve from the depth line and
quote the 2023/2024/2022 marks for each; N11 carries the 2025 density
trap and the sense check; N12 splits why there is an upthrust (15.15P)
from its size (15.16P) and the floating condition (15.17P); T6 lays out
the 2025 four-stage chain with its marks; T7 gives both floating routes
and the 2022 bridge between them. The atmospheric-pressure-with-height
material removed from Topic 14 at its blind check lives in N9.

## Step 4 — every calculation and standard explanation present

Calculations: $F = kx$ for force, extension (in mm) and $k$, from
lengths and from ruler readings; $E = \tfrac{1}{2}kx^2$ and the triangle
area, including $k$ from $E$; gradient and area from force–extension
and force–compression graphs; $P = F/A$ with total areas, cm² and mm²,
$F = PA$ to 2 s.f., and a pressure difference; reading and percentage
change on the height graph and the depth graph; $P = h\rho g$ for
pressure, depth (with and without the atmosphere) and density, and
$\Delta P = \Delta h\rho g$; upthrust from $\rho V g$; the four-stage
density chain; a hot-air balloon's upthrust. Explanations: why two
forces; elastic vs inelastic and the elastic limit; Hooke's law and the
spring constant; why ½; linear vs non-linear and the limit of
proportionality; the practical's readings and accuracy; area → pressure
in the scoring words; normal force and the window; why atmospheric
pressure falls with height; depth and density; the dam; the sea-water
line; where upthrust comes from; apparent weight; the floating ball;
floating and sinking by forces and by density with the displaced-volume
link; ship, submarine, balloon; the key words.

## Step 7 — blind check

A separate agent, given only the JSON and `SCHEMA.md`, recomputed every
numeric answer (all agreed), checked every choice index, model answer,
tag, id and flashcard against the spec and the reports. Twenty-five
findings, all acted on before the push:

- **One real physics error**: the energy past the limit of
  proportionality was said to be *less* than the triangle to that point
  — the curve bends towards the extension axis, so it lies *above* the
  chord from the origin and the area is *more* (about 2.1 J against
  1.86 J); the choice corrected. Also $\Delta h\,\Delta\rho\,g$ for the
  gap between two liquids' lines (it is $h\,\Delta\rho\,g$) — the
  equation removed from that step, which also took 15.14P reasoning out
  of a both-tier section; "momentum carries the ball on" reworded.
- **Graph rules**: three readings were not on gridline intersections —
  the height axis now steps 1 km and 10 kPa, and the questions read 3 km
  (70 kPa, 30 %), 10 cm (5 N, 0.25 J) and 20 m (300 kPa, 200 %); the
  curved parts of three graphs were straight segments and are now
  sampled `curve` series (the validator wants eight points); a
  redundant tolerance removed.
- **Attribution**: the T4 blurb had the 2023 window error backwards
  (the question wanted the cabin air's force, 80 kPa; the difference
  earned only the substitution mark); the 2022 camel marks were called
  three in one place and two in another (two); the 2025 Q8(b) part
  labels were confirmed against the paper ((i) energy from the area,
  (ii) spring constant) and N4 now says why the energy error was 100×
  (the area $\tfrac{1}{2}Fx$ with $x$ in cm) rather than 10 000×; the
  2023 "inversely proportional in this context" acceptance is cited to
  Q4(b)(i); "the Topic 14 scheme" became "the June 2024 scheme
  (Q4(d))"; "the weight in water" became "in the liquid" (the 2025
  liquid was 1400 kg/m³); the claim about no 6-mark spring method in
  2022–2025 is limited to the papers read.
- **Tiering**: the five Physics-only key-word flashcards now belong to
  their P sections (`KW_HOME` in `fm_nn.py`) instead of the both-tier
  key-words section.
- **House rules**: the converter had left `$E = \tfrac{1}{2}$kx²` half
  in TeX in five places, and a dozen `F = kx` / `F = PA` / `= ρ V g`
  strings and four Unicode exponents (`4.8 × 10⁷`) in checklists, hints
  and question text that the step-0 check does not catch — all TeX
  now; "hooke's law" on a flashcard capitalised.
- **Duplicates**: fm-n3-q1 was `hooke-p1` in cm (now 60 N/m, 25 cm);
  fm-n4-q3 was `elastic-p2`'s catapult (now a toy launcher, 5.0 J); the
  N7 explain used the `pressure` worked example's numbers; fm-n5-q1a
  asked for the force the graph's own label gives (now the extension at
  12 N); fm-n6-q1 was a third 6-mark spring method (now a flawed method
  to improve); fm-t6-q3 was the N12 worked example (now water and oil,
  with the opposite outcome); fm-t7-q1 was fm-n12-q4 with new numbers
  (now a floating ball and a sinking marble); the stored mm answers'
  walkthroughs now end in mm; fm-n10-q3 carries the four 2022 marks.
- **Wording**: the opaque 2023 Q7(b) sentence cut; the tyre question
  moved from the contact patch to the valve (1.8 N); "(the moving end)"
  added to the 2023 quote about the top of the spring.

## Step 8 — headless test

`check_topic.js` with and without `--filter Foundation` (re-run after
the blind-check fixes): 68 of 68
numerics and 39 of 39 choices marked correct on the Higher view; 56 of
56 numerics and 38 of 38 choices under Foundation (N11 hidden, and with
it the `liquid` type; the other hidden numerics are the two pre-existing
Higher-only `elastic` questions); no KaTeX errors; 0 plain-text maths in
prose fields after the converter wrapped 46 expressions and nine lines
were done by hand (the liquid-column equation in a section title and a
part title made plain, three "P = hρg" the converter would have broken,
two "m = 40 mm" unit strings, two option texts); 6 diagrams, 16 graphs,
74 flashcards, 183 ref buttons; booklet offers the notes mode; at 390 px
nothing scrolls sideways, no card wider than the screen, nothing sticks
out. The limit-of-proportionality label on the N5 graph and the two
liquid labels on the T5 graph were moved clear of the lines after a
screenshot pass.

## Revisions

### 2026-11-22 — exam-wording verification against the question database

A separate agent compared the page with `Question DB/by-topic/topic-15.md`
(17 questions, 15 with schemes) and the density / upthrust / force parts of
topic-14 and topic-09. No physics error; the defects were mark tariffs and
dropped scheme points. Changes:

| Reference | Change | Scheme |
|---|---|---|
| forces-and-matter / energy-stored (blurb, checklist), fm-t1-q3, flashcard | **bug**: four `"\tfrac"` strings carried a literal tab, so KaTeX could not render the fraction — now `\\tfrac` | — |
| forces-and-matter / elastic-inelastic (explain) | "deformation … accepted" unsupported — removed; "distortion" cited to the 2019 stem | 2H June 2019 Q8(b)(ii) |
| forces-and-matter / hooke-nn worked | the 2023 partial credits as given (1.61 N unrounded = 2 of 3; 1600 N = 2; 1612 N = 1) | 2H June 2023 Q7(a)(i) |
| forces-and-matter / energy-stored worked, pressure-nn worked | forward ½kx² is a 2-mark question (cm left in: 1 of 2); the four-hooves calculation is 2 marks with its partial credits | 2H June 2018 Q5(b)(ii); June 2022 Q4(a)(i) |
| forces-and-matter / extension-not-length table, fx-graphs-hard table | the 2025 cm slip was in the area ½Fx (14 J; 2 of 3), with forgetting the ½ also 2 of 3; converting is not a marking point; the ½kx² cm case is 2018 | 2H June 2025 Q8(b)(i); June 2018 Q5(b)(ii) |
| forces-and-matter / pressure-nn, pressure-hard (explain) | the camel scheme is any two of four (area / weight spread / less pressure / less likely to sink); "pressure is spread out" ignored | 2H June 2022 Q4(a)(ii) |
| forces-and-matter / atmospheric-height (explain), fm-n9-q1c, flashcard | the third credited reason, lower temperature, added; the ignore of g cited to 2023 Q4(b)(ii) | 2H June 2023 Q4(b)(ii); Nov 2021 Q4(b)(ii) |
| forces-and-matter / depth-density (explain), fm-n10-q3, fm-n10-q1; pressure-graphs (table, worked), fm-t5-q2 | the 2022 compare was 2 marks, any two of four; a total-pressure line is **linear with an intercept** (y = mx + c, the paper's own answer), not "pressure proportional to depth"; "more water" alone is ignored — say depth / weight of water above | 2H June 2022 Q4(b)(iii), Q4(c); Nov 2021 Q4(a)(ii) |
| forces-and-matter / fm-t5-q4 | "inversely proportional" accepted as a description of the fall, not for a named mark | 2H June 2023 Q4(b)(i) |
| forces-and-matter / fm-n12-q1 | 2 marks: pressure on the bottom greater than on the top (same area) → force on the bottom greater; the 2-mark alternative route noted | 2H June 2019 Q9(a)(iii) |
| forces-and-matter / upthrust-hard (explain), fm-t6-q2, flashcard | the 2025 explanation is 2 marks — "(apparent) loss in weight" = "weight of liquid displaced"; "more dense than air" is guidance, not a third mark | 2H June 2025 Q9(a)(i) |
| forces-and-matter / floating-words flashcard | the 2022 question was why the displacement method fails for wood | 2H June 2022 Q3(c) |

No stored answer changed; `check_topic.js forces-and-matter` passes on
both tiers. H list in the report: the 2019 block-lifted-out-of-water
6-marker and the Nov 2020 loaded-boat 6-marker (floating has been a
6-marker twice and the page has no 6-mark worked example), the rubber
band's unloading-line mark (2019 Q8(b)(ii)), the U-tube "no area in the
equation" (Nov 2020 Q10(b)(ii)), the hydraulic lift (2018 Q6(c)), the
spring-method improvements (Nov 2020 Q6(a)(iii)), the compression limit
(Nov 2020 Q6(a)(iv)), the vertical-spring Z − Y extension (2025 Q8(a)).
