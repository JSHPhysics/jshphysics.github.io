# Topic 12 — Magnetism and the motor effect: SOP notes

Build: `python3 tools/build_magnetism_and_motor_effect.py && python3 tools/build_manifest.py`.
Modules: `mg_diagrams.py` (bar magnet and uniform field, the Earth with a
compass, the straight wire end on, the solenoid, the motor effect with the
two fields, Fleming's left-hand rule, three dots-and-crosses cases, the
d.c. motor end on with the split ring — all painted with the `--ink` /
`--accent` variables and placed in the explain parts of N3–N8, T5 and
T7), `mg_nn.py` (N1–N10, N10 = key words; `WIRE_CHAIN` and `chain_list`
are imported by the tricky module), `mg_tricky.py` (T1–T8 and the
flashcards; `MOTOR_CHAIN`). The existing calculation type `motor-force`
is embedded in N9 (`motor-force-nn`, the `-nn` suffix because the type
owns the plain id).

## Rules for this page (author-approved; keep in every edit)

- **The standard chains are the author's, word for word.** The five
  steps for a wire and the six for a motor are copied from the `EXAM`
  object in `simple-motor/src/build.mjs` (`EXAM.wire`, `EXAM.motor`) and
  must stay identical there, here (`WIRE_CHAIN`, `MOTOR_CHAIN`) and on
  the hairdryer page. If the wording changes anywhere, change it
  everywhere in the same commit. The loudspeaker chain (`EXAM.speaker`)
  is 13.4P and belongs to Topic 13, as does `EXAM.induction`.
- **Tiers.** From the Pearson spec (the school checklist covers Paper 1
  only): 12.1–12.9 both tiers; 12.10–12.14P Higher only, so N7, N8, N9,
  T5, T6 and T7 carry H and the two motor-effect key-word questions and
  the 2023 "interaction" question in T1 carry H individually; 12.14P is
  also Physics only, so T7 carries P. The `motor-force` type was already
  badged Higher. Under the Foundation filter the page shows N1–N6, N10,
  T1–T4 and T8.
- **Force → acceleration, here too.** Why a magnet moves: *the two
  magnetic fields interact, so there is a force on X (away from / towards
  Y), so X accelerates*; a floating or held magnet: *the magnetic force
  balances its weight, so the forces are balanced*. "Like poles repel"
  alone is not an answer (June 2023 Q5(b)).
- **Repulsion is the only test** for a magnet, and a test question
  needs the expected result stated (June 2025 Q7(b)(iv)).
- **The commutator** reverses the current in the coil every half turn
  *so that the coil keeps turning in the same direction* — both halves
  are needed; and a motor does not produce a current (June 2025 Q6(c)).
- **Directions.** Right-hand grip: current out of the page →
  anticlockwise field. Fleming: first finger Field N→S, second finger
  conventional Current, thumb Force; field left→right with current out
  of the page gives force up the page. Every direction answer on the page
  was checked against these.
- The spec has no recall equation in this topic; F = BIl is on the
  list, so checklists say "use".

## Step 1 — lists approved

Author approved N1–N10 / T1–T8 (2026-11-18, "yes, go ahead") with one
amendment: the motor-effect explanations must reuse his standard
explanation from the motor page (the `EXAM` chains above).

## Step 2 — checked against the content list and examiners' reports

Spec 12.1–12.14P read from the Pearson PDF (`gcse-physics-spec.pdf`,
fetched this session; the bold marking was not visible in the extracted
text, so the Higher-only set 12.10–12.14P was confirmed from the
docbrown.info summary of the same spec, which marks "(HT only)" on
12.10–12.14). Coverage: 12.1 (N1, T1, T2), 12.2/12.3 (N2, T2), 12.4
(N3, T3), 12.5/12.6 (N4, T4), 12.7/12.8 (N5, T3, T8), 12.9 (N6, T3,
T8), 12.10/12.11 (N7, T1), 12.12 (N8, T5), 12.13 (N9 + type, T6),
12.14P (T7).

Reports and mark schemes read: 2H June 2023 report (Q5), 2H June 2024
mark scheme (Q5), 2H June 2025 report (Q6(c), Q7).

| Series / Q | Examiner / scheme | Where it went |
|---|---|---|
| 2H 2023 Q5(a) | field lines around magnets: lines "never touch each other and never overlap or cross"; several from one point on a pole lost the mark; arrows away from N for both marks | N3 explain and worked, T3 table and marking, flashcards |
| 2H 2023 Q5(b) | one magnet floating above another: "repulsion" alone 1 mark; the second needs "the interaction between the two magnetic fields"; full marks also said the upward repulsive force balances gravity (equilibrium); an answer without gravity and equilibrium lost marks | N7 explain, T1 table, worked and questions |
| 2H 2023 Q5(c)(ii) | F = BIl: almost all candidates selected and used it correctly | N9 explain |
| 2H 2024 Q5(a)(i) | field direction at points around the Earth: up the page at the equator point, down the page on the far side, judged by eye within 10° | T4 explain and q1 |
| 2H 2024 Q5(a)(ii) | evidence for the Earth's field, any three: "Earth has a magnetic field"; "needle points in the direction of the field"; field goes into the Earth at the north pole / out at the south; parallel to the surface at the equator; "the core is magnetic / as if there were a magnet inside the Earth" | N4 explain, T4 explain, worked and q4, flashcard |
| 2H 2024 Q5(b)(ii) | reversing the force on a coil: "any clear action that will reverse the current" or "…reverse the poles" (swap the battery connections / turn the magnet around) | N8 explain and q3, T5 explain and q6 |
| 2H 2024 Q5(b)(iii) | B from F = BIl: "rearrangement and substitution (1)", "evaluation (1)", 0.58 T, anything rounding to 0.6 T, full marks without working | N9 explain, T6 explain and worked (1.2 A, 5.0 cm, 0.035 N → 0.58 T) |
| 2H 2025 Q6(c) | the commutator "was poorly explained": credit for reversing the current every half turn and for this letting the motor spin continuously; some said it stops wires tangling; "a surprisingly large number … attempted to describe a dynamo" — 1 of 3 because "the motor does not produce a current" | T7 explain, worked, q2, q3, q6, flashcards |
| 2H 2025 Q7(b)(ii–iii) | bar chart of nails against turns; describe the relationship; better answers noted it was not linear; "should be discouraged from using the term 'Inversely proportional'" unless one variable is proportional to the reciprocal of the other | T8 explain, q3, q4 |
| 2H 2025 Q7(b)(iv) | are the nails permanent magnets: one mark for a suitable test, one for the expected result; "pick up a paper clip" 1 of 2; full marks reversed one nail and found no attraction in any direction | N1 explain and worked, T2 whole section |
| 2H 2025 Q7(c) | an unfamiliar equation linking B and distance d, inverse square, 160 μT; finding the constant and stopping 1 of 3 | N5 explain, T6 table, q5 and q6 |

## Step 3 — redraft

T1 was rebuilt round the interaction mark and the force → balance
chain for the floating magnet; T2 was added as its own section because
the 2025 test question is a two-part answer students half-give; the
commutator answer in T7 was split into the two halves the report credits;
"inversely proportional" went into T8.

## Step 4 — every calculation and standard explanation present

Calculations: F = BIl forwards and rearranged for B, I and l (N9, the
type, T6), cm/mA/mN conversions, the length in the field, a coil of N
turns, I from V = IR first, the unfamiliar inverse-square equation.
Explanations: poles and the test; permanent vs induced and the core
material; field lines and the uniform field; plotting a field; the
Earth's field and its evidence; the wire's field and showing it; the
solenoid adding and cancelling; the five-step wire chain; Fleming's rule
and reversing; the six-step motor chain and the commutator; the seven
steps for the electromagnet; the key words.

## Step 7 — blind check

A separate agent, given only the JSON and `SCHEMA.md`, checked every
numeric answer against its walkthrough (all agree), every choice index
against its explanation, every written model against its mark count,
the tags, ids, cross-references and flashcard section ids, the SVG
arrowhead geometry of all eight figures against their captions (all
consistent), and the two standard chains against the author's wording.
Findings, all fixed before the push:

- **Two wrong directions.** The T5 worked example "Finding the current"
  (field right→left, force up) answered "out of the page"; the current
  is **into** the page. mg-t5-q4 (field down, force right) stored "into
  the page"; the current is **out** of the page. Both re-derived from the
  reference case (field left→right, current out → force up) and from
  F = I × B; the other six FLHR answers were checked and are right.
- Physics wording: T7 said the force on a coil side is largest when the
  coil is flat — it is the same size at every angle (the sides are always
  at right angles to the field); it is the turning effect that is largest
  flat and zero at the vertical. mg-t7-q5 said "half a turn" to reach the
  vertical — a quarter turn, now "turn to the vertical". T4's account of
  the 2024 points ("on the far side, down the page") was reworded so it
  no longer implies the surface field points south anywhere: read each
  arrow from the loop it lies on. T2's "no attraction (no repulsion)"
  parenthetical untangled to "no repulsion in either orientation".
- Choice with two defensible answers: mg-n1-q3's distractor "it points
  north when hung up" is itself a test for a magnet — replaced.
- The author's rules: mg-n7-q1 hedged "accelerates / moves" — now
  "accelerates"; the worked examples and mg-t7-q1 paraphrased the five-
  and six-step chains — now quote them verbatim with any extra detail in
  brackets after the step.
- Tiering: T1 is both tiers but its "fields interact" link is 12.11
  (Higher). mg-t1-q1 is now a 2-mark Foundation-safe chain (force on X
  away, X accelerates) with the interaction link marked "Higher" in the
  model; mg-t1-q2 keeps its H tag; the blurb says which link is Higher.
  N3's "(N7)" cross-reference moved under the Foundation filter (N10
  becomes N7 there) — now "the motor-effect section, Higher". The
  key-words blurb now says the commutator is Physics only too.
- Structure: T8's plan had six rows under "any six of the seven" — the
  relationship row added to the table, the strip, the worked example and
  the mark scheme (accuracy and repeat split into two rows); "the core
  does not warm" → "the coil does not heat up"; mg-t8-q5 no longer calls
  the current a control variable without knowing which investigation.
- Wording: a stray "Reversing:" label in mg-t4-q4; plain-text F = BIl
  and V = IR in the lede, blurbs and factsBlurb now `$…$` (checked that
  the lede renders KaTeX).

Left as they were: the flashcards abbreviate the chains with arrows
(summaries, not model answers); N5's "you will not be asked to recall
any equation for this" (true, and consistent with the equation-list
rule).

## Step 8 — headless test

`check_topic.js` with `--filter Foundation`: 15 of 15 numerics and 50 of
50 choices marked correct on the Higher view; 32 of 32 choices under
Foundation (N7–N9, T5–T7 hidden, N1–N6, N10, T1–T4, T8 shown); no KaTeX
errors; 8 diagrams; 75 flashcards; badges H×7 (incl. the type card) and
P×1; booklet offers the notes mode; at 390 px nothing scrolls sideways,
no card wider than the screen, nothing sticks out.
