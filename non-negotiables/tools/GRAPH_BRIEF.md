# Brief for graph-question authors

You are adding ONE new calculation type to an existing topic file of "The
Non-negotiables" (an A-level physics practice site): a graph-reading skill.
These are the "use the graph to determine…" questions every paper carries:
read a value at a marked point, find a gradient (often of a tangent), find
an area, or read an intercept, and then turn that into the physical quantity.

Project root: `/home/claude/non-negotiables/`

## Read first

1. `SCHEMA.md` — the whole file, and the **Graph questions** section at the
   end in particular. It defines the `graph` object you will write on every
   question.
2. `tools/AGENT_BRIEF.md` — the quality bar for questions, hints,
   walkthroughs and answers. It applies here unchanged.
3. The existing topic file you are editing, so your new type matches its
   style and does not duplicate an existing type.

## What to produce

For each topic you are assigned:

1. Append ONE new type to `data/<topic-id>.json` → `types` (at the end of the
   list). It has a worked example and six practice questions, and **every
   one of the seven carries a `graph`**. Give the type an id ending in
   `-graph` (e.g. `vt-graph`, `iv-graph`) and a name like "Reading a
   velocity–time graph". Its `boards` follow the topic brief below.
2. `tools/calc_<topic-id>_graph.py` — the script that computes every
   answer AND every plotted coordinate. Curves (exponentials, inverse
   squares, sinusoids) must be sampled by the script (10–20 points) and the
   answer computed from the same function, so the graph and the answer
   agree. Print the answers and paste them into the JSON.
3. Check each graph by rendering it:
   `node tools/render_graph.js '<graph json>' /tmp/<id>.svg` — it validates
   the spec and writes an SVG you can open (or just trust its validation).
4. Run `python3 tools/validate.py data/<topic-id>.json` until it prints OK.

Do not change existing types or any other file.

## Designing the seven questions

Each question has one numeric answer. Across the seven, cover the ways the
graph is used in this topic (see the topic notes): reading a value at a
marked point, gradient of a straight section, gradient of a drawn tangent,
area under a section, an intercept, and one two-step (read a gradient then
convert it to the quantity, e.g. gradient of ln A against t → λ → t½).

Make the graph honest and readable:
- Anything the student must read sits on a major gridline intersection
  (both coordinates), or is stated in the question.
- Choose axis ranges and steps so the plot fills the grid (the curve or
  line should use most of the width and height).
- Tangents: give two end points on gridline intersections, far apart
  (span at least half the plot width), marked with `kind: "tangent"`, and
  say in the question "The tangent to the curve at X is drawn." Mark X
  itself with a `marks` entry. The stored answer uses the tangent's
  gradient from those two end points.
- Areas: use `shade` to show the region, and say "the shaded area".
  Straight-line sections give exact areas; for a curve, either state the
  number of grid squares under it in the question or avoid area questions
  on curves.
- Mark points with letters (X, A, B, P). `drop: true` draws dotted lines to
  both axes when the student should read both coordinates.
- Axis labels in the "quantity / unit" form: `v / m s⁻¹`, `t / s`,
  `r / 10⁶ m`, `ln (A / Bq)`, `1 / r² / m⁻²`. Scaled axes (`× 10⁶ m`) are
  fine and realistic; make sure the question's walkthrough handles the
  scaling explicitly.
- Write an `alt` sentence for each graph.

Walkthroughs name the coordinates used: "Gradient of tangent = (30 − 0) /
(8.0 − 2.0) = 5.0 m s⁻²". Hints point at the graph feature: "Area under
the line between 0 and 6 s; the shape is a triangle."

## Final reply

When the validator passes for every file you touched, reply with: each
topic id, the new type id and name, how many of the seven questions use a
tangent / an area / an intercept / a marked value, and any decision the
project lead should know about. Nothing else.
