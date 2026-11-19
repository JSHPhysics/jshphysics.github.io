# Topic 14 — Particle model: SOP notes

Build: `python3 tools/build_particle_model.py && python3 tools/build_manifest.py`.
Modules: `pm_diagrams.py` (the three states, the density practical's
three set-ups, a cold and a hot gas in the same box, the same gas in half
the volume, the Celsius–kelvin ladder, the specific-heat-capacity rig —
painted with the `--ink` / `--accent` variables and placed in the explain
parts of N1, N3, N9, N10, N11 and T6), `pm_nn.py` (N1–N12, N12 = key
words), `pm_tricky.py` (T1–T8 and the flashcards; the heating, cooling
and melting-ice graphs are `graph()` specs there). The seven existing
calculation types are embedded: `density` in N2 (`density-nn`), `shc`,
`latent` and `change-of-state` in N7 (`thermal-equations`), `temperature`
in N10 (`kelvin-nn`), `boyle` in N11 (`compressing-gas`), `heating-graph`
in T4 (`heating-cooling-graphs`).

## Rules for this page (author-approved; keep in every edit)

- **Tiers.** From the Pearson spec (the school checklist covers Paper 1
  only): only **14.20P** (doing work on a gas) is Higher only, and
  **14.16P–14.20P** are Physics only. So N11 (`compressing-gas`) carries
  P; T8 (`work-on-gas`, the bicycle pump) carries H and P; T7's volume
  and force-on-a-surface questions are tagged P individually; T2's
  upthrust group (Topic 15 fluids) is tagged P. Everything else is both tiers and
  untagged. **`boyle` is now both tiers** (14.19P is not a bold
  statement; author-approved 2026-11-19); the three Higher-only questions
  inside the pre-existing types (`change-of-state-p5`, `-p6`,
  `heating-graph-p5`) were left as they were.
- **Particle motion in the words that score.** Solid: *vibrate about
  fixed positions*; liquid: *move around / flow over each other*; gas:
  *fast, straight lines, random directions*. A change of state is
  written before → joining word → after, with the particles as the
  subject. Bulk properties ("takes the shape of the container"), "lots
  of energy" and "closer together" earn nothing (2023 Q3, 2025 Q5).
- **The measuring-cylinder method, never the eureka can.** The volume
  of an irregular solid is read before and after, fully immersed,
  subtracted; the displacement can scored nothing (2023 Q3(d)).
- **SI units, sensible rounding.** Density work stays in kg and m³
  unless told to convert; 1 g/cm³ = 1000 kg/m³; answers keep the
  significant figures of the data (0.0047 m³ is not 0.005 m³ — 2025).
- **A cooling curve's flat section is freezing**, at the melting point,
  with energy transferred *from the wax to the surroundings*; the
  "why is it long" marks are latent heat ≫ specific heat capacity with
  the values quoted (2025 Q5(c)(iii)).
- **"Energy to the surroundings / container / heater parts"**, never
  "energy is lost" or "not 100 % efficient", for a shortfall in a
  temperature rise (2024 Q9(c)(ii)).
- **Thermal insulation is not electrical insulation** (2025 Q3(d)).
- **Two chains, kept apart.** Temperature at constant volume: faster →
  more often *and harder*. Volume at constant temperature: shorter path
  → more often, *not harder*. State the condition each time.
- Equations: $\rho = m/V$, $\Delta Q = mc\Delta\theta$, $Q = mL$,
  $T(\text{K}) = \theta(°\text{C}) + 273$ and $P_1V_1 = P_2V_2$ are on
  the list; checklists say "use".

## Step 1 — lists approved

Author approved N1–N12 / T1–T8 (2026-11-19, "go ahead"), including the
proposal to drop `boyle`'s Higher badge. The blind check (step 7) split
the bicycle pump out of T7 into its own Higher-Physics section, so the
page has T1–T9.

## Step 2 — checked against the content list and examiners' reports

Spec 14.1–14.20P from the Pearson PDF, Higher-only set confirmed from
the docbrown.info summary ("(HT only)" on 14.20P alone). Coverage: 14.1
(N1, T1), 14.2 (N2 + type, T2), 14.3 (N3, T2, T3), 14.4 (N4), 14.5 (N5,
T1), 14.6/14.7 (N6, T4, T5), 14.8/14.9 (N7 + three types, T4, T5),
14.10 (N8), 14.11 (T6), 14.12/14.13 (N9, T7), 14.14/14.15 (N10 + type,
T8), 14.16P–14.19P (N11 + type, T7), 14.20P (T8).

Reports and mark schemes read: 2H June 2023 report (Q3, Q4), 2H June
2024 mark scheme (Q3, Q4, Q9), 2H June 2025 report (Q3(d), Q5, Q9).

| Series / Q | Examiner / scheme | Where it went |
|---|---|---|
| 2H 2023 Q3(b) | density in SI units: candidates converted kg and m³ to g and cm³ "and often used incorrect powers of ten"; "use SI units in all calculations unless instructed specifically to convert" | N2 explain and q5, T2 table |
| 2H 2023 Q3(c)(ii) | motion of particles in a liquid: "flow over each other" scored; "move freely" one mark, "added nothing further about the motion"; imprecise "lots of energy", bulk properties and descriptions of melting not credited; range of speeds | N1 explain and q2, T1 table and q3 |
| 2H 2023 Q3(d) | volume of an irregular metal: measure the water volume before, metal fully immersed, subtract — "many scored full marks"; "describing a displacement (Eureka) can … scored nothing"; the metal's mass "not relevant to volume" | N3 explain, worked and q2, T3 explain and q2 |
| 2H 2023 Q4 | pressure is force per unit area; atmospheric pressure falls with height because there is less air above | (Topic 15 — removed from this page at the blind check) |
| 2H 2024 Q3(a) | $V = m/\rho$: substitution or rearrangement (1), evaluation (1), 1.57 cm³ | T2 table |
| 2H 2024 Q3(b) | solid denser than liquid: particle spacing in the solid is less / more tightly packed / more particles per unit volume | N4 explain and worked |
| 2H 2024 Q3(c) | $Q = mL$: substitution (1), evaluation (1), $1.36 \times 10^5$ J | N7 explain |
| 2H 2024 Q3(d) | scale reading: "reading off scale either 1750 or 1350 seen" (1), 400 cm³ (1); estimates within 1300–1400 / 1700–1800 accepted | N3 explain, T2 table and q2 |
| 2H 2024 Q4(c), (d) | pressure–height not linear; density of air falls with height, particles further apart; ignore gravity | (Topic 15 — removed from this page at the blind check) |
| 2H 2024 Q9(a) | solid → gas is sublimation | N5 explain and q1 |
| 2H 2024 Q9(b) | heating a sealed can: the mean distance between particles does not change | N9 q5, T1 table |
| 2H 2024 Q9(c)(i) | $\Delta\theta = \Delta Q/(mc)$: rearrangement and substitution (1), evaluation (1), 42 °C | N7 explain |
| 2H 2024 Q9(c)(ii) | why the rise was smaller (a storage-heater brick): not all the energy goes to / stays in the brick; energy transferred to the storage heater parts (1); to the surroundings (1); ignore "lost", ignore "not 100 % efficient" | T5 explain, worked, q2, q4 |
| 2H 2024 Q9(d) | SHC of water, 6 marks: apparatus (heater, supply, balance, thermometer, stopwatch, joulemeter or ammeter and voltmeter, insulated container, stirrer); steps (mass, initial and final temperature, time, energy, rearrange $\Delta Q = mc\Delta\theta$, or graph); Level 3 needs $\Delta\theta$, the energy and how $c$ is found; ignore Bunsen | T6 whole section |
| 2H 2025 Q3(d) | a cable's thick plastic coating is electrical, not thermal, insulation: "wasted heat can only be reduced by lowering resistance" | N8 explain and q2 |
| 2H 2025 Q5(b) | wax freezing, motion: "now only vibrate in fixed positions" both marks; "no longer move past each other", "slow down / lose energy" scored; "closer together" not enough | N1 explain and worked, T1 table |
| 2H 2025 Q5(c)(i) | volume from density: substitution and evaluation; rounding 0.0047 m³ to 0.005 m³ "unnecessary and actually poor practice" | N2 explain, worked and T2 q4 |
| 2H 2025 Q5(c)(ii) | the same mass of wax has a smaller volume as a solid than as a liquid | N4 explain and q4 |
| 2H 2025 Q5(c)(iii) | cooling curve, 3 marks: latent heat ≫ specific heat capacity, cite the values; energy transferred from the wax to the surroundings; rate about the same so more energy takes longer ("rarely seen"); many described melting rather than freezing | T4 explain, q2b, q2c |
| 2H 2025 Q9(a)(ii) | upthrust → volume of water displaced $1.43 \times 10^{-4}$ m³ → density $4.9 \times 10^3$ kg/m³, error carried forward | T2 explain and q3 |

## Step 3 — redraft

T1 was built round the two reports' lists of what did and did not score,
with the before → joining word → after template; T2 collects the four
traps (rearranging, units, rounding, scale reading) in one table and
carries the 2025 upthrust chain as a three-part question; T3 gives the
displacement-can trap its own choice question and applies the seven
steps to the mass–volume investigation (gradient = density); T4 carries
the 2025 cooling-curve marks and a heating graph whose numbers (70 W,
0.10 kg, 1-8-10 minute sections) give $L = 336\,000$ J/kg and $c =
4200$ J/kg °C back; T5 has the 2024 "ignore" list; T6 the 2024 levels
and apparatus; T7 the four chains in one table with the condition for
each; T8 the work-done link with the pump and its reverse; T9 the kelvin traps
(all on 14.14–14.15 — the pressure law is not on the spec).

## Step 4 — every calculation and standard explanation present

Calculations: density, mass and volume from $\rho = m/V$ in g/cm³ and
kg/m³ with conversions; a difference of cylinder readings; the upthrust
route to a volume and a density; $\Delta Q = mc\Delta\theta$ for energy
and for $\Delta\theta$; $Q = mL$; a three-stage ice-to-warm-water sum;
$E = Pt$ into both; $c$ and $L$ from a heating graph; K ↔ °C; a change
in K; doubling the pressure via kelvin; $P_1V_1 = P_2V_2$ for a volume
and a pressure. Explanations: the three states' arrangement and
movement and every change of state as motion; why solids are denser;
mass conservation and physical vs chemical; the SHC and SLH definitions
and difference; why a flat section is flat and why it is long; the
shortfall in a temperature rise; insulation and the vacuum flask; the
pressure chain, the temperature chain, the volume chain, the force on a
surface, work done on a gas; atmospheric pressure with height; absolute
zero; why the gas laws need kelvin; the two 6-mark methods and the seven
steps; the key words.

## Step 7 — blind check

A separate agent, given only the JSON and `SCHEMA.md`, recomputed every
numeric answer (all agree), checked every choice index, model answer,
tag, id and flashcard against the spec and the reports. Twenty-seven
findings, all acted on before the push:

- **Off spec**: half of the kelvin section rested on the pressure law
  ($p \propto T$ at constant volume), which 14.13 keeps "qualitative
  only". The "doubling the pressure" worked example and three questions
  are replaced by on-spec traps (a change in K, a negative kelvin, the
  one-temperature-converted $\Delta Q = mc\Delta\theta$ error, "twice
  as hot"); the N10 sentence about the gas laws now says only that the
  kelvin zero is a real zero. Atmospheric pressure with height (2023 and
  2024 Q4) is Topic 15 fluids, not Topic 14 — removed from T7 and the
  flashcards (the evidence is kept in the table above for Topic 15).
- **Tiering**: the bicycle pump (14.20P, Higher Physics) sat in a
  both-tier section as its worked example and a flashcard, so under the
  Foundation filter it stayed visible. It now has its own section, T8
  `work-on-gas` [H, P], with the reverse case (expanding gas cools);
  kelvin traps moved to T9 — one section more than the approved list,
  for the tier rule. The upthrust group carries P on the group as well
  as its parts. "At right angles" (14.17P) taken out of the both-tier N9
  and the key-word definition; it stays in N11 and T7's P row.
- **Numbers**: a 6000 J/kg °C liquid (none exists) is now 2400; the
  63.2 kg answer that the section had just told students to round is
  stored as 63; a redundant tolerance removed; 2.7 g/cm³ appeared five
  times (and pm-n2-q1 was the `density` type's worked example) — copper
  8.9, a 2.6 stone, 2500 kg/m³ and a hall of air now; the `compressing-
  gas` worked example no longer mirrors the `boyle` one. The 2024 Q3(d)
  readings 1350 and 1750 cm³ were queried and re-checked against the PMT
  copy of the scheme: "reading off scale either 1750 or 1350 seen" (1),
  "400 (cm³)" (1) — kept, worded as a scale reading rather than a
  cylinder.
- **Duplicates**: the eureka-can question in N3 and T3, the compress-
  to-half question in N11 and T7, the SHC-of-water 6-marker asked again
  after its worked example, the pump question repeating its worked
  example, and the ice graph reused in T4's first group — each given a
  different question (N3: which measurement is not needed; T7: which link
  differs between the chains; T6: a Bunsen-burner method to fix, marked
  by levels; T4: a substance-X graph, $L = 144\,000$ J/kg).
- **House rules**: `P₁V₁ = P₂V₂` with Unicode subscripts in a checklist
  and a question (the check's pattern missed them), "÷ g" in three
  places, a double-wrapped `$$Q = mL$$` — all TeX now. "Topic 9" for
  pressure = force/area → Topic 15.
- **Wording**: every "the eureka can scored nothing" now says *when the
  question gives a measuring cylinder* — the can is a fair method for an
  object too big for one; the six changes of state agree across the
  title, strip and flashcard; the brick sentence; "question 1" → the
  data restated; the SVG's hyphen for −273 °C.

## Step 8 — headless test

`check_topic.js` with and without `--filter Foundation` (re-run after
the blind-check fixes): 68 of 68 numerics and 45 of 45 choices marked
correct on the Higher view; 65 of 65 numerics and 43 of 43 choices under
Foundation (T8 hidden; the three hidden numerics are the pre-existing
Higher-only type questions); no KaTeX errors after one equation strip the converter had
wrapped in `$` was put back; 0 plain-text maths in prose fields after the
converter wrapped 39 expressions and three lines were done by hand;
6 diagrams, 11 graphs, 80 flashcards, 197 ref buttons; booklet offers the
notes mode; at 390 px nothing scrolls sideways, no card wider than the
screen, nothing sticks out. The heating graph's "boiling" label was
clipped at the right edge of the plot and now sits left of its marker.
