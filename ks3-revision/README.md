# KS3 Revision

Self-guiding revision booklets for Key Stage 3 physics, built on the same
app shell as [The Non-negotiables](../non-negotiables/): every point on a
revision checklist gets an explanation, a worked example whose steps are
revealed one at a time, and practice questions checked as the student goes
— with hints, EWAU walkthroughs, tap-to-draw graphs, flip-card key facts,
a traffic-light self-check per section, and a printable booklet with or
without answers.

**Topics:** P3 Motion (speed, graph skills, distance–time graphs,
acceleration, speed–time graphs) — 6 sections, 62 questions.

## Running it

The page loads its data with `fetch`, so it has to be served over HTTP
rather than opened straight from disk.

- **GitHub Pages:** lives at `jshphysics.github.io/ks3-revision/`. No build step.
- **Locally:** `python3 -m http.server` inside this folder, then open
  `http://localhost:8000`.

## Layout

```
index.html              the page shell
css/app.css             the Non-negotiables stylesheet plus the booklet blocks
css/fonts.css           self-hosted Bricolage Grotesque and JetBrains Mono
js/app.js               routing, rendering, answer checking, drawing, progress, booklet
js/graphs.js            exam-style graphs from a declarative spec (shared with the Non-negotiables)
vendor/                 KaTeX and the fonts (no CDN requests at all)
data/manifest.json      list of topic files
data/<topic>.json       one file per topic (generated — edit the build script instead)
tools/build_<topic>.py  the source of truth for a topic: run it to regenerate the JSON
tools/ramp.svg          the light-gate diagram inlined into p3-motion.json
```

## Editing or adding content

1. Edit `tools/build_p3_motion.py` (maths is written as raw-string KaTeX
   between `$…$`, everything else is HTML) and run it from this folder:
   `python3 tools/build_p3_motion.py`.
2. Reload the page.

To add a topic, copy the build script, give the topic a new `id` and
`order`, write it to `data/<id>.json`, and add a line to
`data/manifest.json`. With more than one topic the site shows a home grid.

## Question types

| type      | what the student does                              | marked by                                |
|-----------|-----------------------------------------------------|------------------------------------------|
| `numeric` | types a number; unit shown on the answer line       | the app (2% tolerance; spots ×10 and sign slips) |
| `choice`  | picks an option                                     | the app                                  |
| `written` | writes on paper, compares with the model answer     | the student ("Yes, got it" / "Not yet")  |
| `draw`    | taps points onto a grid (or draws on paper)         | the app when `check` is true, else the student |

Progress, self-checks and the paper/blueprint theme are stored in the
browser (localStorage) per device.
