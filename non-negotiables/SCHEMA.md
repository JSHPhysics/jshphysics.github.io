# The Non-negotiables — topic file schema and style guide

Every topic is one JSON file in `data/`. The app loads `data/manifest.json`
and then each topic file it lists. A topic file contains calculation
**types**; each type has one **worked example** and six **practice questions**.

"Non-negotiable" means a straightforward calculation that every A-level
physics student must be able to do without thinking: pick the equation,
substitute, rearrange if needed, evaluate, give the unit. Nothing multi-stage
beyond two steps, no extended "explain" parts, no data analysis.

## File layout

```json
{
  "id": "kinematics",
  "title": "Kinematics",
  "subtitle": "SUVAT, projectiles and motion graphs",
  "order": 20,
  "types": [ ...calculation types... ]
}
```

- `id` — lowercase kebab-case, matches the file name (`data/kinematics.json`).
- `order` — integer used to sort topics in the sidebar (gaps of 10 between topics).

## Calculation type

```json
{
  "id": "suvat-one-equation",
  "name": "Using a single SUVAT equation",
  "equations": ["v = u + at", "s = ut + ½at²", "v² = u² + 2as", "s = ½(u + v)t"],
  "boards": ["AQA", "OCR A", "OCR B", "Edexcel", "WJEC"],
  "method": "List s, u, v, a, t. Cross out the one you don't know and aren't asked for; pick the equation without it. Take the direction of initial motion as positive.",
  "commonErrors": [
    "Forgetting that a = −9.81 m s⁻² when 'up' is positive",
    "Using v² = u² + 2as and forgetting to square-root at the end"
  ],
  "worked": { ...worked example... },
  "practice": [ ...exactly six practice questions... ]
}
```

- `id` — kebab-case, unique within the file.
- `name` — what a teacher would call this skill, under ~60 characters.
- `equations` — the equation(s) the type uses, as plain text (see Notation).
- `boards` — which boards examine this type. Use the full list for core
  content; narrow it only for genuinely board-specific content.
  Valid values: `"AQA"`, `"OCR A"`, `"OCR B"`, `"Edexcel"`, `"WJEC"`.
- `method` — two or three sentences: how to recognise the type and the
  recipe for doing it.
- `commonErrors` — two to four one-line pitfalls.

## Worked example

```json
{
  "id": "suvat-one-equation-w",
  "question": "A car accelerates uniformly from 4.0 m s⁻¹ to 16 m s⁻¹ over a distance of 60 m. Calculate its acceleration.",
  "steps": [
    "Known: u = 4.0 m s⁻¹, v = 16 m s⁻¹, s = 60 m. Unknown: a. Not needed: t.",
    "The equation without t is v² = u² + 2as.",
    "Rearrange: a = (v² − u²) / 2s",
    "a = (16² − 4.0²) / (2 × 60) = (256 − 16) / 120 = 240 / 120",
    "a = 2.0 m s⁻²"
  ],
  "answer": { "value": 2.0, "unit": "m s⁻²" }
}
```

- `steps` — four to seven short lines. The first line identifies knowns and
  unknowns; the last line states the answer with its unit. Show the
  substituted numbers explicitly.

## Practice question

```json
{
  "id": "suvat-one-equation-p1",
  "question": "A ball is thrown vertically upwards at 12 m s⁻¹. Calculate the maximum height it reaches. Take g = 9.81 m s⁻².",
  "hint": "At the top, v = 0. You know u, v and a and want s.",
  "walkthrough": [
    "u = 12 m s⁻¹, v = 0, a = −9.81 m s⁻², find s.",
    "v² = u² + 2as → s = (v² − u²) / 2a",
    "s = (0 − 144) / (2 × −9.81) = −144 / −19.62",
    "s = 7.3 m"
  ],
  "answer": { "value": 7.34, "unit": "m" },
  "boards": ["AQA", "OCR A", "OCR B", "Edexcel", "WJEC"]
}
```

- `id` — `<type-id>-p1` … `<type-id>-p6`. The worked example is `<type-id>-w`.
- `question` — self-contained; include every value needed, including any
  constant that is not on the standard list below.
- `hint` — one sentence that unblocks a stuck student without doing the
  question: which equation, which quantity is zero, what to rearrange.
- `walkthrough` — three to six lines of working, same style as the worked
  example `steps`.
- `answer.value` — a JSON number (never a string) holding the answer to
  **three significant figures** (or more if the question's data justify it).
  The app checks a student's entry against this with a 2% tolerance by
  default, so a student rounding to 2 s.f. is still marked correct.
  Add `"tolerance": 0.05` (fraction) only where rounding in intermediate
  steps legitimately produces a wider spread.
- `answer.unit` — plain text unit (see Notation). Use `""` for dimensionless.
- `boards` — optional on a question; defaults to the type's `boards`.
  Add it only when a particular question is narrower than the type.

Six practice questions must progress: p1–p2 direct substitution, p3–p4 need
a rearrangement or a unit conversion (mm, kN, μs, kWh …), p5–p6 are two-step
(e.g. find one quantity then use it, or combine two equations). All six use
different contexts and different numbers; none reuses the worked example's
numbers.

## Notation (plain text, no LaTeX, no HTML)

- Multiplication: `×`. Division in-line: `/`. Powers of ten: `3.0 × 10⁸`.
- Superscripts and subscripts with Unicode: `m s⁻¹`, `m s⁻²`, `kg m⁻³`, `v²`,
  `½mv²`, `E = mc²`, `N₀`, `λ`, `ω`, `Δ`, `θ`, `ε₀`, `μ₀`, `π`, `√`.
- Units with a space between unit and value and a space between unit parts:
  `9.81 m s⁻²`, `2.4 × 10⁻³ kg`, `1.6 × 10⁻¹⁹ C`, `50 Ω`, `3.0 kΩ`, `°C`, `K`.
- Angles in degrees unless the quantity is angular velocity or phase.
- UK English: `metre`, `centre`, `analyse`, `programme` (for a plan).

## Standard constants (students are assumed to have these on a data sheet;
do not repeat them in the question unless a non-standard value is used)

```
g = 9.81 m s⁻²            c = 3.00 × 10⁸ m s⁻¹        e = 1.60 × 10⁻¹⁹ C
h = 6.63 × 10⁻³⁴ J s      G = 6.67 × 10⁻¹¹ N m² kg⁻²  k = 1.38 × 10⁻²³ J K⁻¹
R = 8.31 J mol⁻¹ K⁻¹      N_A = 6.02 × 10²³ mol⁻¹     ε₀ = 8.85 × 10⁻¹² F m⁻¹
μ₀ = 4π × 10⁻⁷ H m⁻¹      σ = 5.67 × 10⁻⁸ W m⁻² K⁻⁴   m_e = 9.11 × 10⁻³¹ kg
m_p = 1.67 × 10⁻²⁷ kg     m_n = 1.67 × 10⁻²⁷ kg       u = 1.66 × 10⁻²⁷ kg
1 u = 931.5 MeV/c²        1 eV = 1.60 × 10⁻¹⁹ J       Wien: 2.90 × 10⁻³ m K
1 AU = 1.50 × 10¹¹ m      1 ly = 9.46 × 10¹⁵ m        1 pc = 3.09 × 10¹⁶ m
Earth: M = 5.97 × 10²⁴ kg, R = 6.37 × 10⁶ m           Sun: M = 1.99 × 10³⁰ kg
```

Use exactly these values in walkthroughs so the stored answer matches what
a student with a standard data sheet will get.

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
  "x": { "label": "t / s", "min": 0, "max": 12, "step": 2 },
  "y": { "label": "v / m s⁻¹", "min": 0, "max": 30, "step": 5 },
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

- `x`, `y` — `label` uses the "quantity / unit" convention and plain-text
  notation (`v / m s⁻¹`, `r / 10⁶ m`, `ln (A / Bq)`); it is typeset with
  KaTeX. `step` must divide `max − min` exactly, with at most 20 major
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
