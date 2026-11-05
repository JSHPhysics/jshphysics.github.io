# GCSE Revision

Self-guiding GCSE physics revision, built on the same app shell as
[The Non-negotiables](../non-negotiables/) and [KS3 Revision](../ks3-revision/):
every item gets an explanation, a worked example whose steps are revealed one
at a time, and practice questions checked as the student goes — with hints,
EWAU walkthroughs, exam-style graphs (including tangents to curves), flip-card
key facts, a traffic-light self-check per section, and a printable booklet
with or without answers.

What this site adds to the KS3 shell is **bands**: a topic's sections can be
grouped under headings, each with its own numbering prefix.

**Topics:** Topic 2 - Forces and Motion (LEH, U4) — Edexcel 1PH0 spec points
2.1–2.33P in three bands: *The non-negotiables* (N1–N15, recall and
single-step calculations), *The tricky bits* (T1–T13, multi-step
calculations, explanations and misconceptions) and *Key facts* (flip cards).
20 sections and 126 questions on the U4 page (29 and 182 in the modules).

## Running it

The page loads its data with `fetch`, so it has to be served over HTTP
rather than opened straight from disk.

- **GitHub Pages:** drop this folder into `jshphysics.github.io/` as
  `gcse-revision/` and add a card to `tools.json`. No build step.
- **Locally:** `python3 -m http.server` inside this folder, then open
  `http://localhost:8000`.

## Layout

```
index.html                     the page shell
css/app.css                    the KS3 stylesheet plus the band headings
css/fonts.css                  self-hosted Bricolage Grotesque and JetBrains Mono
js/app.js                      routing, rendering, answer checking, progress, booklet, bands
js/graphs.js                   exam-style graphs from a declarative spec (shared with the Non-negotiables)
vendor/                        KaTeX and the fonts (no CDN requests at all)
data/manifest.json             list of topic files
data/t2-forces-motion.json     generated — edit the build modules instead
tools/build_t2_forces_motion.py  assembles the topic, validates it, writes the JSON
tools/t2lib.py                 question and graph helpers
tools/t2_nn_a.py               N1–N8     tools/t2_nn_b.py       N9–N15
tools/t2_tricky_a.py           T1–T7     tools/t2_tricky_b.py   T8–T13 + key facts
```

## Editing or adding content

1. Edit the relevant `tools/t2_*.py` module. Maths is written as raw-string
   KaTeX between `$…$`; everything else is HTML. Every numeric answer is a
   Python expression, never a typed number.
2. Run `python3 tools/build_t2_forces_motion.py` from this folder. It checks
   ids, graph axes and answer types before it writes the JSON.
3. Reload the page.

To add a topic, copy the build script and its modules, give the topic a new
`id` and `order`, write it to `data/<id>.json`, and add a line to
`data/manifest.json`. With more than one topic the site shows a home grid.

## Hiding sections

`HIDDEN_SECTIONS` at the top of `tools/build_t2_forces_motion.py` lists
section ids that stay in the modules but are left out of the JSON (and whose
key-fact cards are dropped). The U4 page currently hides Newton's third law (and its balanced-forces section),
momentum, circular motion, inertial mass and the stopping-distance sections,
because those spec points are taught later. Remove an id from the set and
rebuild to publish it; the remaining sections renumber themselves.

## Bands

A topic may carry

```json
"bands": [ { "id": "nn", "prefix": "N", "title": "The non-negotiables", "blurb": "…" }, … ]
```

and each section a `"band": "nn"`. Sections are labelled `N1`, `N2` … within
their band; a heading goes above the first section of each band on the page,
in the pill bar, and as a divider page in the booklet. A topic without
`bands` behaves exactly like the KS3 site.

## Question types

| type      | what the student does                              | marked by                                |
|-----------|-----------------------------------------------------|------------------------------------------|
| `numeric` | types a number; unit shown on the answer line       | the app (2% tolerance; spots ×10 and sign slips) |
| `choice`  | picks an option                                     | the app                                  |
| `written` | writes on paper, compares with the model answer     | the student ("Yes, got it" / "Not yet")  |
| `group`   | a multi-part question sharing one stem and graph    | each part as above                       |

Progress, self-checks and the paper/blueprint theme are stored in the
browser (localStorage, under `gcse-*` keys so they do not clash with the
KS3 site on the same origin).

## Attribution

Joshua Stafford-Haworth · JSHPhysics · @educatorJSH
