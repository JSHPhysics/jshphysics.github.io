# The GCSE Non-negotiables — topic file schema and style guide

Every topic is one JSON file in `data/`. The app loads `data/manifest.json`
and then each topic file it lists. A topic file contains calculation
**types**; each type has one **worked example** and six **practice questions**.

"Non-negotiable" means a calculation that every Edexcel GCSE Physics (1PH0)
student must be able to do without thinking: pick the equation from the
equation sheet (or recall it), substitute, rearrange if needed, evaluate,
give the unit. Nothing beyond two steps, no extended "explain" parts.

## File layout

```json
{
  "id": "kinematics",
  "title": "Kinematics",
  "subtitle": "SUVAT, projectiles and motion graphs",
  "order": 20,
  "figure": "kinematics",
  "types": [ ...calculation types... ]
}
```

- `id` — lowercase kebab-case, matches the file name (`data/kinematics.json`).
- `order` — integer used to sort topics in the sidebar (gaps of 10 between topics).
- `figure` — optional; the id of the animated drawing (from `js/figures.js`) shown on the
  topic's card and cover. Defaults to the topic `id`. Available ids: measurements,
  kinematics, forces, momentum-energy, materials, waves, quantum, electricity,
  circular-shm, thermal-gases, gravitational-fields, electric-fields-capacitors,
  magnetic-fields-induction, magnetism, nuclear-particles, astrophysics, and the
  GCSE variants circuit, particle-model, half-life and motion-graph.

## Calculation type

```json
{
  "id": "acceleration",
  "name": "Acceleration from a change in velocity",
  "equations": ["a = (v − u) / t"],
  "boards": ["Foundation", "Higher"],
  "method": "Acceleration is the change in velocity divided by the time it takes. Work out v − u first, then divide by t. Keep the units: m/s divided by s gives m/s².",
  "commonErrors": [
    "Dividing the final velocity by the time instead of the change in velocity",
    "Forgetting to convert minutes to seconds before dividing"
  ],
  "worked": { ...worked example... },
  "practice": [ ...exactly six practice questions... ]
}
```

- `id` — kebab-case, unique within the file.
- `name` — what a teacher would call this skill, under ~60 characters.
- `equations` — the equation(s) the type uses, as plain text (see Notation).
- `boards` — the tiers this type is examined at. Foundation content (which
  Higher students also sit) is `["Foundation", "Higher"]`; Higher-only
  content is `["Higher"]`. Valid values: `"Foundation"`, `"Higher"`.
- `method` — two or three sentences: how to recognise the type and the
  recipe for doing it.
- `commonErrors` — two to four one-line pitfalls.

## Worked example

```json
{
  "id": "acceleration-w",
  "question": "A car speeds up from 4 m/s to 16 m/s in 6 s. Calculate its acceleration.",
  "steps": [
    "Known: u = 4 m/s, v = 16 m/s, t = 6 s. Unknown: a.",
    "a = (v − u) / t",
    "a = (16 − 4) / 6 = 12 / 6",
    "a = 2 m/s²"
  ],
  "answer": { "value": 2, "unit": "m/s²" }
}
```

- `steps` — four to seven short lines. The first line identifies knowns and
  unknowns; the last line states the answer with its unit. Show the
  substituted numbers explicitly.

## Practice question

```json
{
  "id": "acceleration-p5",
  "question": "A ball is thrown straight up at 12 m/s. Calculate how high it rises before it stops. Take g = 10 m/s².",
  "hint": "At the top v = 0. Use v² − u² = 2 × a × x with a = −10 m/s².",
  "walkthrough": [
    "u = 12 m/s, v = 0, a = −10 m/s², find x.",
    "v² − u² = 2 × a × x → x = (v² − u²) / (2 × a)",
    "x = (0 − 144) / (2 × −10) = −144 / −20",
    "x = 7.2 m"
  ],
  "answer": { "value": 7.2, "unit": "m" },
  "boards": ["Higher"]
}
```

- `id` — `<type-id>-p1` … `<type-id>-p6`. The worked example is `<type-id>-w`.
- `question` — self-contained; include every value needed, including any
  constant that is not on the standard list below.
- `hint` — one sentence that unblocks a stuck student without doing the
  question: which equation, which quantity is zero, what to rearrange.
- `walkthrough` — three to six lines of working, same style as the worked
  example `steps`.
- `answer.value` — a JSON number (never a string). GCSE answers are usually
  exact or tidy (choose data so they are); otherwise give three significant
  figures. The app checks a student's entry against this with a 2%
  tolerance by default, so a student rounding to 2 s.f. is still marked
  correct.
  Add `"tolerance": 0.05` (fraction) only where rounding in intermediate
  steps legitimately produces a wider spread.
- `answer.unit` — plain text unit (see Notation). Use `""` for dimensionless.
- `boards` — optional on a question; defaults to the type's `boards`.
  Add `["Higher"]` on a question in a Foundation type only when that one
  question needs Higher-only content (a rearrangement Foundation students
  are not expected to do, or a Higher-only equation).

Six practice questions must progress: p1–p2 direct substitution, p3–p4 need
a rearrangement or a unit conversion (cm to m, g to kg, minutes to seconds,
km/h to m/s, kJ, mA …), p5–p6 are two-step (find one quantity then use it,
or combine two equations). All six use different contexts and different
numbers; none reuses the worked example's numbers. GCSE students meet
numbers in context: use everyday, realistic values (a 60 kg cyclist, a 2 kW
kettle, a 1.5 V cell), and avoid standard form except where the physics
needs it (speed of light, atomic scales).

## Notation (plain text, no LaTeX, no HTML)

GCSE papers and the Edexcel equation sheet use slash units and words, and
so do we:

- Units with a slash: `m/s`, `m/s²`, `kg/m³`, `N/kg`, `J/kg °C`, `J/kg`,
  `W`, `Ω`, `kWh`. Never `m s⁻¹`. A space between value and unit: `15 m/s`,
  `4200 J/kg °C`, `0.5 A`, `230 V`, `12 Ω`, `50 Hz`.
- Multiplication: `×`. Division in-line: `/`. Squares with Unicode: `v²`,
  `x²`, `m/s²`. Standard form, where unavoidable: `3 × 10⁸ m/s`.
- Equations in Edexcel's symbol form, e.g. `F = m × a`, `W = m × g`,
  `KE = ½ × m × v²`, `GPE = m × g × h`, `v² − u² = 2 × a × x`,
  `a = (v − u) / t`, `P = I × V`, `E = Q × V`, `V = I × R`, `p = m × v`,
  `F = (mv − mu) / t`, `ρ = m / V`, `ΔQ = m × c × Δθ`, `Q = m × L`,
  `v = f × λ`, `F = k × x`, `E = ½ × k × x²`, `M = F × d`, `p = F / A`,
  `P = h × ρ × g`, `P₁V₁ = P₂V₂`, `V_p / V_s = N_p / N_s`,
  `V_p × I_p = V_s × I_s`, `F = B × I × l`,
  `efficiency = useful energy output / total energy input`. Write the
  multiplication signs out as Edexcel does; the typesetter handles them.
- Edexcel's symbols: `x` for distance, `W` for weight (and for work done —
  say which in the method), `E` for energy, `Q` for charge (and for
  thermal energy in `ΔQ = mcΔθ`).
- Greek and special characters: `ρ`, `λ`, `θ`, `Δ`, `Ω`, `°C`, `μ`, `½`, `π`.
- UK English: `metre`, `centre`, `kilogram`.

## Standard values (students are told these; do not repeat them in the
question unless a different value is used)

```
g = 10 N/kg (= 10 m/s²)            speed of light = 3 × 10⁸ m/s
```

Everything else a question needs is stated in the question text: speed of
sound (340 m/s), density of water (1000 kg/m³), specific heat capacity of
water (4200 J/kg °C), mains voltage (230 V), and so on. Use g = 10 N/kg
in every walkthrough so stored answers match what a student gets.

## Verification rule

Every `answer.value` must be produced by running the calculation in Python,
not typed from memory. Write one script that computes all answers for the
file, print them, and copy the printed values into the JSON. Then run
`python3 tools/validate.py data/<topic>.json` and fix anything it reports.

## Graph questions

A worked example or practice question may carry a `graph`. The app draws it
as a clean exam-style graph (major and minor gridlines, numbered axes) below
the question text, and the print booklet includes it. Use graphs for the
skills students meet in papers as "use the graph to determine…": a gradient,
an area, an intercept, or the value at a marked point.

```json
"graph": {
  "x": { "label": "time in s", "min": 0, "max": 12, "step": 2 },
  "y": { "label": "velocity in m/s", "min": 0, "max": 30, "step": 5 },
  "series": [
    { "kind": "line", "points": [[0, 0], [6, 30], [9, 30], [12, 0]] },
    { "kind": "dashed", "points": [[6, 0], [6, 30]] }
  ],
  "marks": [ { "x": 6, "y": 30, "label": "X", "drop": true } ],
  "shade": [ { "series": 0, "from": 0, "to": 6 } ],
  "labels": [ { "x": 2, "y": 27, "text": "tangent at X" } ],
  "alt": "Velocity–time graph rising to 30 m/s at 6 s, flat to 9 s, falling to zero at 12 s"
}
```

- `x`, `y` — `label` uses the GCSE convention "quantity in unit"
  (`velocity in m/s`, `time in s`, `extension in cm`, `activity in Bq`), as
  Edexcel papers print it; it is typeset with KaTeX. `step` must divide `max − min` exactly, with at most 20 major
  divisions. Optional `minor` sets minor divisions per major step (default
  5 when there are ≤ 6 majors, 2 when ≤ 12, else 1).
- `series[].kind` — `line` (straight segments between the points), `curve`
  (smooth through the points; give 10–20 points computed by your script),
  `dashed` (construction line), `tangent` (drawn in the accent colour; give
  its two end points, chosen on gridline intersections so the student can
  read its gradient exactly), `data` (crosses; optional `fit` with two end
  points of a best-fit line).
- `marks` — labelled points. `drop: true` adds dotted lines to both axes.
  Optional `dx`, `dy` nudge the label.
- `shade` — a region under a series between two x-values (area questions).
  Optional `baseline` (default 0).
- `labels` — free text at a data coordinate.
- `alt` — one sentence describing the graph for screen readers and print.

Rules for graph questions:
- Everything the student must read off sits on a major gridline
  intersection, or is given in the question text. A tangent's end points
  are on gridline intersections.
- The question says what is drawn ("The tangent at X is shown").
- Values implied by the graph must agree with the stored answer: compute
  the answer from the same coordinates the graph uses, in your script.
- All points lie inside the axis ranges.
- Keep a plotted curve to the physical shape (an exponential decay must
  come from an exponential, computed in the script, not sketched).
