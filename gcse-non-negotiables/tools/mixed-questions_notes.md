# Mixed-topic questions (Paper 1 and Paper 2): SOP notes

Build: `python3 tools/build_mixed_questions.py && python3 tools/build_manifest.py`
writes **two pages**, `data/mixed-paper-1.json` ("Mixed-topic
questions: Paper 1", order 160) and `data/mixed-paper-2.json` ("Mixed-
topic questions: Paper 2", order 161) — the author asked for one page
per paper on 2026-11-21, after a single `mixed-questions` page had been
pushed the evening before (that topic id is gone; its section and
question ids live on unchanged in the two pages). Modules: `mx_p1.py`
(`join_section(stem)`, the M1 opener built once per page with its own
question ids — `mx-m1-q…` on Paper 1, `mx-j2-q…` on Paper 2 — and the
Paper 1 blends P1-1 … P1-6), `mx_p2.py` (the Paper 2 blends P2-1 … P2-8
and the flashcards for both pages; `facts_for()` in the build script
gives each page the cards of its own sections, so the M1 cards appear on
both). Neither page has calculation types or diagrams of its own; the
graphs (force–extension, decay curve, cooling curve, weight–extension)
are `graph()` specs in the modules. The build script writes each topic
file whole from `TOPIC_P1` / `TOPIC_P2` — there is no pre-existing JSON
to preserve. Both cards use the `measurements` figure.

## Rules for this page (author-approved; keep in every edit)

- **What the pages are.** Not extra topics: one page per paper of the
  blends that the June 2023, 2024 and 2025 papers set, one section per
  recurring blend, each built as *the join* (the quantity one stage hands to the
  next), a chain table (stage → equation → what it hands over → what to
  watch), a worked example modelled on the real question with new
  numbers, and a multi-part practice group. The physics of each stage
  lives on its topic page; this page practises the hand-over. New
  blends from later papers go in as new sections (ids stable).
- **Bands.** Each page: `start` (prefix M: M1 only) then `p1` (prefix
  "P1-") or `p2` (prefix "P2-"). Section ids are the blend's name
  (`gpe-ke-speed`, `one-object` …; `join` on both pages); question ids
  `mx-m1-q…` / `mx-j2-q…` for the two openers, `mx-a<n>-q…` for Paper 1
  blends, `mx-b<n>-q…` for Paper 2 blends — unique across both files,
  which `build_manifest.py` checks.
- **Tiers.** Sections are untagged where the blend is both-tier;
  where the whole blend is Higher or Physics only the section is
  tagged: `momentum-force-ke` [H], `induction-neighbours` [H],
  `thermal-balance` [H], `stopping-energy` [P],
  `pressure-force-particles` [P], `upthrust-density-moments` [P]. Parts carry their topic's tag: momentum and
  $v^2 - u^2 = 2ax$ and scale-drawing resultants H; braking ∝ $v^2$,
  PET, the loudspeaker/microphone comparison P; the transformer chain
  and turns ratio H P. A worked example in an untagged section stays
  both-tier: Higher steps inside it are marked [H] in the text and the
  both-tier result does not depend on them.
- **Four habits** (M1): find the join; match units at the join (kJ → J,
  cm → m, g → kg, minutes → seconds, kWh → J); carry forward and label
  every stage (error carried forward is how the schemes mark chains);
  check the number makes sense.
- **Language carried over from the topic pages**: "transferred to the
  surroundings / the container", never "energy is lost"; "a pd is
  induced", never "produced"; the standard induction, loudspeaker and
  motor chains are the author's (Topic 12 / 13 pages); $E = mc^2$ is
  described as *supplied* — it is not on the equation list.
- **Evaluate questions** (charging-time claims): calculate, compare with
  the claim in a sentence, conclude — the comparison is the mark.

## Step 1 — lists approved

Author approved M0 + P1-1 … P1-6 + P2-1 … P2-8 and the page name
`mixed-questions` / "Mixed-topic questions" (2026-11-20, "Yes, go
ahead").

## Step 2 — the papers read, question by question

| Paper | Blended questions and what they chain | Section |
|---|---|---|
| 1H June 2025 Q6 | skier: height from $\Delta GPE$ → acceleration over 200 m to 27 m/s ($v^2 - u^2 = 2ax$) → "explain how to determine the energy dissipated" | P1-1 |
| 2H June 2025 Q2 | trolley: mass from 4.1 J and 26 cm → expected velocity → one way to reduce the gap → a student's power (48 kg, 2.9 m, 3.4 s, 2 s.f.) | M1 worked, P2-5 |
| 1H June 2025 Q8 | kick: momentum with unit → contact time from 2700 N → Newton's third law → trolleys sticking together | P1-2 |
| 1H June 2025 Q9(a)(iii) | KE of a beta particle ($9.1 \times 10^{-31}$ kg, $3.8 \times 10^{6}$ m/s) | P1-2 |
| 1H June 2025 Q5(b) | light glass → air: wavelength increases, frequency unchanged; change in speed of blue light from $f$, 470 nm and 350 nm | P1-4 |
| 1H June 2025 Q4 | fluorine-18 curve at 150 min; positron meets electron; one neutron and one uranium nucleus; 4.4 GW : 8.9 GW to 2 s.f. | P1-5 |
| 1H June 2025 Q10(b) | describe fusion; mass decrease for $3.9 \times 10^{26}$ J with $E = mc^2$ and $c$ supplied | P1-5 |
| 1H June 2025 Q7(d) | why Ceres' average temperature stays constant (4) | P1-6 |
| 2H June 2025 Q5 | wax: all liquid between which points; particle motion on freezing; volume of 3.9 kg at 830 kg/m³; volume on solidifying at 930; why R–S is longer with $L = 190$ kJ/kg and $c = 2.1$ kJ/kg °C | P2-1 |
| 2H June 2024 Q3 | 14.1 g copper at 8.96 g/cm³; solid denser than liquid; vaporise 60.0 g of water; a volume off a jug | P2-1 |
| 2H June 2024 Q4 | direction of the water's force; skate $4.8 \times 10^{7}$ Pa × $1.2 \times 10^{-5}$ m² to 2 s.f.; height graph; 104 → 74 kPa %; density with height by particles | P2-2 |
| 2H June 2023 Q4 | aeroplane window: difference, $F = PA$, the larger window, the arrow, the height graph and its reason | P2-2 |
| 2H June 2025 Q8 | springs: why the vertical one is longer; extension = added weight; energy from the area to 8 cm; $k$ with unit; two vectors on a 5 N block; resultant of 4 N and 5 N | P2-3 |
| 2H June 2023 Q7 | pen spring 260 N/m × 6.2 mm; change in length; accuracy; hook's force 6 N up; resultant of 30 N and 40 N | P2-3 |
| 2H June 2025 Q9 | newton-meter in liquid vs air; density of the block from a $1.4 \times 10^{3}$ kg/m³ liquid (four stages); the winch 6-marker | P2-4 |
| 2H June 2023 Q6 | push-up pivot; arm in equilibrium; muscle force with 15 N added; ball in fresh and sea water | P2-4 |
| 2H June 2023 Q9 | pulley: weight from 3000 J over 2.0 m; total work at 64 %; another reason for waste; the 6-mark efficiency-vs-weight plan "include how you will use your measurements" | P2-5 |
| 2H June 2024 Q7 | distance from $W = Fd$ (7440 J, 645 N); experiment to find GPE gained naming the devices; height from 5.8 J and 320 g; a reason the motor is under 100 % | P2-5 |
| 2H June 2023 Q8 | electric car: KE; battery time; regenerative braking; evaluate the charging claim with $t = E \div (IV)$; charge moved | P2-6 |
| 2H June 2025 Q6 | toothbrush: current in the secondary; turns from 230 V, 1.5 V, 1840; the diode; the commutator | P2-7 |
| 2H June 2023 Q10 | dynamo: how it was turned; harder with a lamp; secondary pd; loudspeaker vs microphone (6) | P2-7 |
| 2H June 2024 Q10 | falling magnet and its investigation; 11 000 V → 230 V transformer (6) | P2-7 |
| 2H June 2024 Q9 | brick: rise from 210 kJ, 5.8 kg, 860 J/kg °C; why smaller; the SHC-of-water 6-marker | P2-8 |

Sources: the June 2025 1H and 2H, June 2024 2H and June 2023 2H
question papers (PMT mirror), read with the web tool, plus the reports
and schemes already recorded in the topic notes files (Topics 2, 3+8,
5, 6, 7, 9, 10, 13, 14, 15). The stopping-distance blend (P1-3) is the
only section not taken from a 2023–2025 question; it is the standard
Topic 2 / Topic 3 join the author's Topic 2 page already teaches in
words, here with the numbers.

## Step 3 — redraft

M1 states the four habits with the 2025 error-carried-forward example
and works the 2025 trolley question in full. Each blend's table names
what each stage hands over and the unit it must be in; the worked
examples keep the shape of the real question (same parts, same order)
with new numbers; the practice groups ask the whole chain in one go,
with a written part in the mark-scheme words. P2-7 points to the
Topic 12 / 13 pages for the author's standard chains rather than
reprinting them, and uses them in the model answers.

## Step 4 — every chain present

GPE → KE → speed → acceleration / dissipation; momentum → force → KE
and conservation; KE → braking distance → stopping distance;
$v = f\lambda$ across a boundary; half-life → fraction, $E = mc^2$
supplied, power ratio; radiation balance; mass → volume → latent heat
→ SHC on a cooling curve; pressure → force (normal), height graph →
particles; graph → energy and $k$ → free-body → resultant; loss in
weight → volume → density → moments; work → efficiency → total, GPE →
height, power, the pulley plan; KE, battery time, $E = IVt$, $Q = It$,
regenerative braking; dynamo, transformer chain, turns, diode, grid,
loudspeaker vs microphone; $E = IVt$ → $\Delta\theta$ → $c$ → why
smaller, the SHC-of-a-block 6-marker.

## Step 7 — blind check

A separate agent, given only the JSON and `SCHEMA.md`, recomputed every
numeric answer (all agreed), checked every choice, model answer, tag,
id and flashcard. Twenty-six findings, all acted on before the push:

- **Marking**: the ratio question's tolerance would have rejected the
  unrounded 10.34 (now 5 %); two nm answers whose walkthroughs ended in
  metres (now end in nm); a turns count stored as 200.7 (now 200);
  seven redundant tolerances removed. The wax cooling curve's flat
  section was 7 min against 6 min of cooling, contradicting the
  "same rate, three times the energy" explanation — now 6 min against
  2 min, the ratio of the two energies.
- **Tiering** (the page's main lesson): a worked example in an untagged
  section is both-tier content, so the Higher steps came out of the
  GPE and springs worked examples (their H-tagged practice parts stay),
  the Higher equations left the strips and checklists, and the H-only
  flashcard went; the momentum blend and the induction blend are
  Higher content throughout (both set on the Higher papers) and are
  tagged H, with the beta-particle KE moved to the nuclear section;
  stopping-by-energy is 2.33P and is tagged P; thermal balance is H
  only, with the star question P; three spec kickers corrected.
- **House rules**: `$v^2 - u^2 = 2$ax` half-TeX in three places,
  `\sqrt(` for `\sqrt{}`, and about thirty plain-text equations in
  hints, checklists, blurbs and a group stem (the step-0 pattern does
  not catch `F = PA` or `Q = It`); "the dynamo produces a pd" →
  "a pd is induced in the dynamo".
- **Attribution and consistency**: the pulley worked example used the
  2023 numbers unchanged (now a crate, 4000 J over 2.5 m); a choice
  attributed this page's 8 N / 6 N / 2 N to the 2025 paper; the
  floating-ball comparison promised in a checklist had no question
  (added, mx-b4-q4); "one object, four topics" was one topic (now
  "four stages"). The 2025 Q5(b) and Q2(a)(iii) attributions were
  queried and re-checked against the paper outline — both stand.
- **Wording**: "ignore gravity" → "do not say gravity is weaker higher
  up"; two strings pulling a spring → a block pulled along a table;
  the greenhouse question re-framed as 5.23's "factors that determine
  the temperature of the Earth"; "Archimedes" → "upthrust-to-density".

## Step 8 — headless test

After the split (2026-11-21): `check_topic.js mixed-paper-1` — 22 of 22
numerics, 5 of 5 choices, 21 flashcards, 48 ref buttons; `mixed-paper-2`
— 30 of 30, 7 of 7, 23 flashcards, 66 ref buttons; both pass with and
without `--filter Foundation`, no KaTeX errors, nothing sticks out at
390 px; the home page shows the two cards last ("Paper 1 · Topics 1–7",
"Paper 2 · Topics 8–15"). The single-page run before the split:

`check_topic.js mixed-questions` with and without `--filter Foundation`
(re-run after the blind-check fixes): 50 of 50 numerics and 10 of 10
choices marked correct on the Higher view; 39 of 39 and 9 of 9 under
Foundation (P1-2, P1-6 and P2-7 hidden, and the H parts inside their
groups); no KaTeX errors; 0 plain-text maths in
prose fields after the converter wrapped 66 expressions, four "½ m v²"
hints and fourteen Unicode exponents were done by hand, and eight
double-wrapped `ewau` equations put back; 5 graphs, 41 flashcards,
108 ref buttons; booklet offers the notes mode; at 390 px nothing
scrolls sideways. The home page shows the new card last ("All topics ·
Mixed-topic questions · 15 sections").

## Revisions

### 2026-11-22 — exam-wording verification against the question database

Two separate agents compared the pages with the June 2023–2025 questions
they are modelled on (`Question DB/index.json`, read part by part) and
their analogues in other series — 31 questions for Paper 1, 41 for Paper 2.
No stored number or physics error; every June 2025 citation matched the
scheme's parts and marks. Changes:

| Reference | Change | Scheme |
|---|---|---|
| mixed-paper-1 / join table, flashcard "Stage 1 wrong" (both pages) | error carried forward: method marks always, the evaluation usually ("no ecf for evaluation" in one 2025 part) | 1H June 2025 Q6(a)(ii), Q8(a)(ii); 2H Q2(a)(ii) |
| mixed-paper-1 / join worked (c), mx-m1-q1c; opener worked step 3 (both pages) | "not 'energy is lost'" → the mark is for the destination; the $v^2$ line is its own mark | 2H June 2019 Q2(b)(iv); 1H June 2024 Q2(c)(i); 2H June 2025 Q2(a)(ii) |
| mixed-paper-1 / gpe-ke-speed (explain, table), mx-a1-q1d | "a smoother runway" → the scheme's list (lubricate, air track, steeper, streamline); the $v^2 = u^2 + 2ax$ stage loses its H (spec 2.8 is both tiers, as on the Topic 2 page) | 2H June 2025 Q2(a)(iii); spec 2.8 |
| mixed-paper-1 / nuclear-energy table, **mx-a5-q3** | the answer and the unit share one mark in the E = mc² question; mx-a5-q3 re-set so the 2 s.f. answer can be shown (61 ÷ 5.6 = 11; stored answer 10 → 11) | 1H June 2025 Q10(b)(ii), Q4(d) |
| mixed-paper-1 / thermal-balance (checklist, explain) | "rate" is a mark on its own; the four marks as the scheme writes them (emission increases with temperature) | 1H June 2025 Q7(d); June 2023 Q8(b)(ii) |
| mixed-paper-2 / one-object (explain, worked, mx-b1-q3, table), mx-b1-q1 | the 2025 wax question described as set (R–S shorter than Q–R); the credited sentence "specific heat capacity is much less than specific latent heat" with both values; mass into Q = mL in kg (60.0 g scored 1 of 2) — mx-b1-q1 now gives 250 g | 2H June 2025 Q5(e); June 2024 Q3(c) |
| mixed-paper-2 / pressure-force-particles (table, mx-b2-q2), flashcard | use the pressure the question names, net only when asked (the net force was capped at 1 of 2 in 2023); lower temperature as the third reason; "non-linear" wordings and two data pairs | 2H June 2023 Q4(a)(ii), Q4(c)(i)–(ii); Nov 2021 Q4(c)(ii) |
| mixed-paper-2 / springs-forces-energy (explain, table, worked, mx-b3-q1c, mx-b3-q2), flashcard | k with a consistent unit (0.45 N/cm scored full marks; no unit = 1); the free-body second mark is "label 5 N on both arrows"; the extension trap is Z − Y (loaded minus unloaded vertical length) | 2H June 2025 Q8(b), Q8(c)(ii), Q8(d) |
| mixed-paper-2 / mx-b4-q2 | "apparent loss in weight" | 2H June 2025 Q9(a)(i) |
| mixed-paper-2 / work-efficiency-power (explain), mx-b5-q1d, mx-b5-q3 | the 2023 numbers as set (1800 J over 1.2 m); friction and heating as the two reasons, sound ignored; the 2 s.f. line is its own mark | 2H June 2023 Q9(a); June 2024 Q7(d); June 2025 Q2(b) |
| mixed-paper-2 / electrical-energy-store (worked, table), mx-b6-q2 | KE in the unit asked for (153 600 J scored 1 of 2 against "in kJ"); "Comment on" not "Evaluate"; "energy that would otherwise be wasted" | 2H June 2023 Q8(a), Q8(c), Q8(d) |
| mixed-paper-2 / induction-neighbours (table), mx-b7-q1b, mx-b7-q3 | the commutator's first mark (connects the coil to the battery); the dynamo force comes from the interaction of fields, "greater resistance" ignored; the loudspeaker chain's changing field and the amplitude link | 2H June 2025 Q6(d); June 2023 Q10(b), Q10(d); Nov 2020 Q7(a) |
| mixed-paper-2 / electricity-into-heat (explain) | the second heating-effect mark: the ions vibrate more | 2H June 2018 Q8(c) |

One stored answer changed (mx-a5-q3: 10 → 11, with new data). Both pages
pass `check_topic.js` on both tiers. Noted for the author: the Paper 1
stopping-distances-as-energy section has no June 2023–2025 1H analogue
(nearest 2019 Q1, 2018 Q6(d), June 2026 Q3 with no scheme yet) — its
physics stands, its claim to be a recurring blend does not; the opener's
worked example gives the runway height in metres where the real 2025
question gave 26 cm (the cm → m conversion carried a mark). H lists in
both reports: the freezing-motion 2-marker (2025 Q5(b)), "pressure is the
same" on a smaller window (2023 Q4(a)(iii)), the GPE experiment (2024
Q7(b)), the momentum-and-energy collision 6-marker's energy half (1H 2024
Q9(c)), Δv = fΔλ as the accepted alternative (1H 2025 Q5(b)(iii)).
