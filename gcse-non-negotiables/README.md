# The GCSE Non-negotiables

A practice site for every calculation in Edexcel GCSE Physics (1PH0):
one worked example and six practice questions per calculation type, with
a hint, a step-by-step walkthrough and instant answer checking. Students
pick their tier (Foundation or Higher) and see only what their tier
examines; teachers can print any selection as a booklet, with or without
answers.

It is the sibling of [The Non-negotiables](../non-negotiables/) for
A-level and shares its code exactly: the only differences are
`data/config.json`, `index.html` and the topic files.

## Running it

The page loads its question data with `fetch`, so it has to be served over
HTTP rather than opened straight from disk.

- **GitHub Pages:** push this folder to a repository (or a subfolder of
  `jshphysics.github.io`) and it works as-is. No build step.
- **Locally:** `python3 -m http.server` inside this folder, then open
  `http://localhost:8000`.

## Layout

```
index.html             the page shell
css/app.css            layout, theme tokens (paper / blueprint), print booklet
css/figures.css        the topic drawings' look and motion
css/fonts.css          self-hosted Bricolage Grotesque and JetBrains Mono
js/app.js              routing, rendering, answer checking, progress, booklet
js/richmath.js         plain-text physics notation → KaTeX
js/figures.js          the animated technical drawings
js/graphs.js           exam-style graphs from a question's "graph" spec
vendor/                KaTeX and the fonts (no CDN requests at all)
data/config.json       site title, lede and the tier filter
data/manifest.json     list of topic files (generated — do not edit by hand)
data/<topic>.json      one file per topic; see SCHEMA.md for the format
tools/validate.py      checks a topic file against the schema
tools/build_manifest.py  validates every topic file and rewrites the manifest
tools/render_graph.js  renders a graph spec to SVG for checking
tools/calc_*.py        the scripts that produced every answer
tools/verify_*.py      independent re-derivations of samples of answers
SCHEMA.md              the topic-file contract and style guide
```

## Editing or adding questions

1. Edit `data/<topic>.json` (or add a new file). Keep to the format in
   `SCHEMA.md`: GCSE notation (`m/s`, `kg/m³`), the Edexcel equation forms,
   g = 10 N/kg, one numeric answer per question.
2. Run `python3 tools/build_manifest.py`. It validates every file and
   rewrites `data/manifest.json`. Fix anything it reports.
3. Reload the page.

To add a whole topic, create `data/<id>.json` with a unique `order` value
and run the build script; the sidebar picks it up automatically. A topic's
`figure` field chooses which drawing from `js/figures.js` it uses.

## Features

- **Tier filter** — Foundation or Higher. Types and individual questions
  carry tier tags; Foundation content is shown to both tiers, Higher-only
  content to Higher. The choice is remembered.
- **Answer checking** — accepts `2.4e-3`, `2.4 × 10⁻³`, `2.4x10^-3`,
  `1,200`, `35%`. Marks correct within 2% (so 2 s.f. rounding passes);
  spots power-of-ten slips and sign slips and says so.
- **Staged help** — hint, walkthrough, answer, each revealed on demand.
- **Progress** — stored in the browser (localStorage) per device; a
  "Reset progress" button clears it.
- **Search** — matches type names, equations and method text across all
  topics.
- **Print booklet** — current topic or all topics, filtered by tier;
  optional worked examples, method notes, hints and working space;
  answers omitted, final answers at the back, or full walkthroughs at
  the back. Use the browser's "Save as PDF".
- **Graphs** — questions can carry a declarative graph spec; the app draws
  it with major/minor gridlines, marked points, tangents and shaded areas.
- **Typeset maths** — KaTeX throughout, converted from the plain-text
  notation in the data files.
- **Paper and blueprint** — light and dark themes follow the system setting,
  with a manual toggle.
- **Deep links** — `#topic-id/type-id` jumps straight to a calculation type.

## Standard values

Answers use g = 10 N/kg (10 m/s²) and the speed of light 3 × 10⁸ m/s, as
on the Edexcel paper. Every other value a question needs (specific heat
capacities, speeds of sound, densities, latent heats) is stated in the
question text.

## Attribution

Joshua Stafford-Haworth · JSHPhysics · @educatorJSH
