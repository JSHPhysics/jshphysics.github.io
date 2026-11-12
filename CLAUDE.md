# jshphysics.github.io — notes for Claude

Static site served from `main` via GitHub Pages.

## File map

- `index.html` — gallery landing page (tool cards)
- `pedagogy.html` — "On the design of these tools" subpage with lightbox + hotspots
- `tools.json` — **single source of truth** for both pages. Both fetch this on load and build their content from it. The `_instructions` block at the top documents every field.
- `images/` — screenshots referenced by filename in `tools.json`
- `ks3-revision/`, `non-negotiables/`, `gcse-non-negotiables/`, `LEH-U4-Forces-and-motion-revision/` — the booklet/practice apps, each self-contained with its own README. `gcse-non-negotiables/` is the Non-negotiables app byte-for-byte (same `js/`, `css/`, `vendor/`) with its own `index.html`, `data/config.json` (title, lede, tier filter) and topic files; the app reads `data/config.json` on load, so keep the shared files in both folders identical when changing one. `LEH-U4-Forces-and-motion-revision/` (GCSE Revision; `gcse-revision/` is a redirect stub to it, kept so links shared before the rename still work) is the KS3 shell plus *bands* (sections grouped under headings with per-band numbering); content is authored in `tools/t2_*.py` and built with `tools/build_t2_forces_motion.py`. All three share one origin, so each uses its own localStorage prefix (`ks3-*`, `gcse-*`).
- `lessons/` — self-paced animated "Cover Lessons" (`distance-time-graphs/`, `reflection-refraction-tir/`), each a single `index.html`; `lessons/vendor/` is the shared self-hosted KaTeX. Built with the `animated-physics-lesson` skill from the artifact pages: the artifact HTML is wrapped in doctype/head/body and `vendor/` paths become `../vendor/`. Edit the source lesson and re-wrap rather than editing the copy here.
- `hairdryer-anatomy/` — "Hairdryer Anatomy": a single self-contained `index.html` (3D hairdryer and DC motor drawn live as SVG, plus a wiring diagram with a small 2D field solver). It is generated, not hand-written: the source (`geom.mjs`, `scene.js`, `field.mjs`, `live3d.js`, `page.css`, `build3d.mjs`) is kept in `hairdryer-anatomy/src/`. `build3d.mjs` there needs the Anatomy skill's kit (`iso-kit.mjs`, for its CSS and card markup) at the path in its import line; it writes `site/index.html`, which is copied to `hairdryer-anatomy/index.html`. Edit the source and rebuild rather than editing the built page. Uses the shared KaTeX at `../lessons/vendor/` and reads the gallery's `jsh-theme` localStorage key.
- `simple-motor/` — "Simple Motor and Loudspeaker": the school DC motor (split-ring commutator) as a 3D model with an end-on view and a step-through of the split ring, followed by a moving-coil loudspeaker cut in half. Generated the same way as `hairdryer-anatomy/`: source in `simple-motor/src/` (`geom.mjs`, `motor.js`, `speaker.js`, `page.css`, `build.mjs`), built page copied to `simple-motor/index.html`. `geom.mjs` is shared in spirit with the hairdryer page (same projection and mesh painter); if you change one, check the other. The AC generator and slip rings are not on this page; they belong to `induction/`.
- `induction/` — "Electromagnetic Induction": Part 1 is a bar magnet pushed through a coil (3D model, then a side view with the meter trace); Part 2 is a coil turned between two magnets, switchable between an AC generator (slip rings) and a dynamo (split ring), with the output graph. Generated the same way: source in `induction/src/` (`geom.mjs`, `machine.js`, `induction.js`, `touch.js`, `page.css`, `build.mjs`), built page copied to `induction/index.html`. `machine.js` is the motor page's coil-between-magnets model with the generator and dynamo kept in.
- `touch.js` (in each of the three `src/` folders, identical) holds the iPad code shared by these pages: the tilt buttons and the fit-to-screen sizing described under "iPad presentation notes". Keep the three copies the same.
- `annotate.html` — local-only authoring tool (NOT committed; see "Authoring annotations" below)
- `.claude/launch.json` — local-only, used by Claude Preview tooling. Don't commit.

To add or change a tool: edit only `tools.json`. No HTML changes needed.

Sections (`section` field): `simulations` (§ 01), `lessons` (§ 02 "Cover Lessons"), `tools` (§ 03). Both pages have a grid/entry-list per section; card numbers run across all three in DOM order.

## Pedagogy lightbox + hotspots

Clicking any entry image on `/pedagogy.html` opens a full-size lightbox.

Each tool in `tools.json` may include an `annotations` array. Coordinates are percentages of the image's natural dimensions so they survive any rescale:

```json
"annotations": [
  {"x": 47.77, "y": 0.92, "w": 21.22, "h": 5.05, "title": "Title", "note": "Body."}
]
```

These render as numbered hotspots over the enlarged image. Tap one → info card slides in bottom-left with title + note. Tap another to switch; tap the image to dismiss the card; Esc closes card-first-then-lightbox; clicking the dark backdrop or the **Close · Esc** button closes everything.

Currently 63 annotations across the 13 images (Fantastic Flashcards and Curriculum Planner have the most — 9 each).

## Authoring annotations (offline tool)

`annotate.html` lets you drag rectangles on each image and write a title/note for each. Per author preference it stays local-only (not committed).

Workflow:
```powershell
python -m http.server 8765
# open http://localhost:8765/annotate.html
```

Pick a tool from the dropdown, drag rectangles on the image, write title + note (auto-saves to `localStorage`). Click **Copy all as JSON** when done and paste the JSON back to Claude — Claude will merge each image's annotations under the matching tool entry's `annotations` field in `tools.json`.

If `annotate.html` is missing on a fresh checkout, Claude can recreate it: single self-contained HTML file, dark UI, dropdown populated from `tools.json`, drag-to-draw rectangles on the image, sidebar form for title/note per rectangle, `localStorage` persistence keyed by image filename, two export buttons (current image, or all images as a `{filename: [...]}` map) that copy JSON to clipboard.

## iPad presentation notes

The site is shown to teachers/students from an iPad. The pedagogy lightbox has been hardened for iOS Safari:

- `viewport-fit=cover` + `env(safe-area-inset-*)` on all fixed-position elements (close button, hint, card)
- `100dvh` fallback for body min-height and lightbox image max-height (URL-bar crop)
- Position-fixed body scroll lock that preserves `scrollY` on close — `overflow:hidden` alone doesn't fully stop iOS rubber-banding
- `overscroll-behavior: contain` on the lightbox
- `-webkit-tap-highlight-color: transparent` (kills the grey iOS tap flash)
- 44px min tap targets + `touch-action: manipulation` on the close button, card close, and hotspots
- `-webkit-touch-callout: none` + `user-select: none` on the lightbox image (stops the iOS save/share sheet on long-press during a lesson)
- `@media (hover: none)` keeps hotspot outlines visibly present on touch (since touch users have no hover cue) and disables the `.entry-media` brightness-hover so it doesn't get stuck after a tap

`index.html` has NOT had the same pass — apply the same patterns if extending iPad support there.

`hairdryer-anatomy/`, `simple-motor/` and `induction/` have had their own pass, aimed at an iPad in landscape (most students use one that way):

- Every button is at least 44px tall with `touch-action: manipulation`; range sliders have a 44px hit area and a 28px thumb; tap highlight and long-press callout are off.
- Each figure card (`.iso-plate`) is shrunk by `fitAllPlates()` so the drawing and its controls fit on one screen (`window.innerHeight`), down to 45% at most. It runs at widths of 700px and over, on load, resize, rotation and late font load. Do not give a card more rows of controls without checking it still fits at 1080×720.
- A finger drag turns a model left and right only, because up-and-down is left for scrolling. Two round tilt buttons (`.hd-tilt`) appear on touch screens to tilt it instead.
- Tested in an emulated iPad (Chromium with touch, 1080×720 and 1194×834), not on a real device; animation smoothness on a real iPad is unverified.

## Entry image sizing

Entries on `pedagogy.html` used to use `aspect-ratio: 16/10` + `object-fit: cover`, which cropped anything that wasn't landscape. They now use JS sizing — each `.entry-media` is sized to the largest box that satisfies the image's own aspect ratio AND fits within `column-width × body-column-height`. Whichever cap binds first wins; the other dimension scales to maintain proportions. A `ResizeObserver` watches the body and the wrap column and re-fits on window resize, late font load, theme switch, etc. Empty/loading slots fall back to a 16:10 placeholder so the diagonal-stripe texture still has room.

## Conventions

- Push directly to `main` — no PR flow for this repo. GitHub Pages rebuilds in ~30–60s.
- Always `git fetch` before pushing — the author sometimes edits via the GitHub web UI between sessions, so local main can lag origin.
- Never commit `annotate.html` or `.claude/launch.json`.
- Commit format: short title, paragraph body explaining the **why**, trailer:
  `Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>`
- The `_instructions` block in `tools.json` is the canonical schema — keep it in sync with any new fields.
- Test locally before pushing: `python -m http.server 8765` from the repo root.

## Session log

### 2026-05-21 (Opus 4.7)

Big session — built out the entire pedagogy hotspot system end-to-end.

- **Bug fix**: pedagogy entry images weren't loading. Root cause was a deadlock between `loading="lazy"` and the slot's `display:none` empty state — lazy images inside a `display:none` parent never fire `onload`. Removed the lazy attribute.
- **Click-to-enlarge lightbox** added to pedagogy entries — dark backdrop, click/Esc to close.
- **`annotate.html` authoring tool** built (local-only, not committed). Author used it to annotate all 13 images.
- **Hotspot system shipped**: `tools.json` schema extended with `annotations`; pedagogy lightbox renders numbered overlay rectangles + info cards (63 hotspots across 13 images).
- **Hotspot styling softened** — thin dashed outline + small pin by default, prominent only on hover (mouse) or active (selected). `@media (hover: none)` keeps them visible enough on touch.
- **iPad/iOS Safari hardening pass** on the lightbox (see "iPad presentation notes").
- **Entry image sizing fix** — replaced cropping with JS aspect-fit (see "Entry image sizing").
- **Lede copy iterated**: now mentions cognitive-load minimisation + iPad/handwriting-first design priority.

### 2026-11-02 (Fable 5.1)

- Added **Cover Lessons** section (§ 02) to `index.html` and `pedagogy.html`; Tools renumbered § 03. `tools.json` `section` now accepts `lessons`; pedagogy kicker labels them "Lesson".
- Added `lessons/distance-time-graphs/` (KS3) and `lessons/reflection-refraction-tir/` (GCSE 5.1P) with shared `lessons/vendor/` KaTeX, plus `images/distance-time-lesson.png` and `images/optics-lesson.png`.
- Added `gcse-revision/` (GCSE Revision): the KS3 Revision shell with section *bands*, first topic "Topic 2 - Forces and Motion (LEH, U4)" (Edexcel 1PH0 2.1–2.33P, 29 sections, 182 questions, 26 graphs incl. tangents to curves). Card added to `tools.json` after KS3 Revision, plus `images/gcse-revision.png`. Tested headless (Playwright) before pushing: no console errors, answer checking, booklet PDF, phone width.
- Added `gcse-non-negotiables/` (The GCSE Non-negotiables): Edexcel 1PH0 calculation practice, 10 topics / 62 types / 434 questions, Foundation–Higher tier filter. To make it, the Non-negotiables app became config-driven (`data/config.json`: title, lede, filter label/options/default, print subtitle; `<html data-storage="…">` picks the localStorage prefix, `gcse-nn-` here, since both sites share this origin). Shared app files in `non-negotiables/` updated in step (slash units `m/s`, `°C` in unit slots, y-axis label overflow on graphs, punctuation glued to maths, GCSE drawing variants in `figures.js`, cross-file id check in `build_manifest.py`). Card added after The Non-negotiables, plus `images/gcse-non-negotiables.png`. Answers blind-checked by a second agent (`gcse-non-negotiables/tools/verify_gcse.py`, 0 discrepancies over 434).
- `gcse-revision/`: N13–N15 and T5–T10 (third law and its balanced-forces trap, momentum, circular motion, inertial mass, stopping distances) are hidden from the U4 page via `HIDDEN_SECTIONS` in the build script — content kept in the modules, re-enable by removing the id and rebuilding.

### 2026-11-05 (Fable 5.1)

- `gcse-revision/` renamed to `LEH-U4-Forces-and-motion-revision/` at the author's request (students get that URL); `gcse-revision/index.html` is now a redirect stub that carries the `#topic/section` hash across. Card URL in `tools.json` updated; screenshot filename unchanged.
- U4 revision: new tricky-bits section `planning-practical` (T6, "Planning a practical: the 6-mark method question") — the author's seven-step recipe (variables → formula → change → measure → use the result → one accuracy detail → repeat and calculate a mean; questions stay at 6 marks, any six of the seven points), a worked force–acceleration answer, and two 6-mark written questions whose model answers are mark-scheme tables built by `mark_scheme()` in `t2_tricky_b.py`. Page now 21 sections / 128 questions.

### 2026-11-11 (Fable 5.2)

- Added `hairdryer-anatomy/` (Hairdryer Anatomy) as a Simulations card after Upthrust Derivation, plus `images/hairdryer-anatomy.png`. Three figures: a turnable 3D dryer with a working switch and solid / see-through / hidden casing; the DC motor enlarged, with a strip-down animation, N/S and +/− labels; and an end-on wiring diagram (three coils in a ring, three commutator segments, two brushes) with current dots and crosses, force arrows, and a field shown as curved lines, straight lines or a computed solution. Restyled from the artifact to the site's Fraunces / IBM Plex cream-and-ink look. Tested from a local server before pushing: no console errors, KaTeX renders, no sideways scroll at phone width.

### 2026-11-12 (Fable 5.2)

- Added `simple-motor/` (Simple Motor and Generator) as a Simulations card after Hairdryer Anatomy, plus `images/simple-motor.png`. One coil between two magnets; a Machine switch changes it between a DC motor with a split ring and an AC generator with slip rings. Force arrows and current markers vanish while the brushes are over the gaps in the split ring. Fig 3 steps through the rings stage by stage (seven stages for each machine); a comparison table sits at the bottom.
- `hairdryer-anatomy/`: the 3D projection in `geom.mjs` was mirror-imaged (left-handed), so the 3D motor turned the opposite way to its own wiring diagram. Fixed (`flat()` now uses the viewer's true right-hand direction) and the screenshot retaken. The wiring diagram (Fig 3) was always correct.
- `simple-motor/`: added a moving-coil loudspeaker at the end of the page (`speaker.js`): Fig 4 is the speaker cut in half in 3D so the W-shaped magnet (centre N pole, outer S ring) and the coil in the gap can be seen; Fig 5 is the flat cross-section with the signal graph and sound leaving the cone. Pitch, volume and a current-by-hand slider. Also fixed the site copy showing both machines' notes at once (`[hidden]` was being overridden by `display:grid`).
- `simple-motor/`: removed the AC generator / slip-ring mode, its notes and the split-ring versus slip-rings table at the author's request, because the generator now has its own induction page (built as an artifact, not yet pushed here). Page and card renamed "Simple Motor and Loudspeaker"; URL unchanged. Screenshot retaken.
- `simple-motor/` and `hairdryer-anatomy/`: added "exam-style explanation" boxes in the author's own wording (numbered chains of reasoning students can reproduce). Motor page: "motor effect on a single wire" and "motor effect in a motor" after Fig 1, "motor effect in a loudspeaker" after Fig 5. Hairdryer page: "motor effect in a motor" after Fig 3. The text lives in the `EXAM` object in each build file (`examBox` / `examSection`); keep the wording identical across pages when it changes. The induction artifact carries the matching "Induction" box.
- `hairdryer-anatomy/`: marked as extension content at the author's request. It goes beyond A-level and is for interest only, not for students to memorise. The page has an "Extension · beyond A-level" notice under the lede (`.hd-ext`) pointing students to the exam-style box and to `simple-motor/` for the motor they need to know; the gallery card says so in its description and carries an `Extension` tag in place of the GCSE / A-Level level tags (convention recorded in `tools.json` `tagConventions`). Keep that framing in any future edit to the page or card.
- iPad landscape pass on `hairdryer-anatomy/`, `simple-motor/` and `induction/` (see "iPad presentation notes"): 44px controls, larger slider thumbs, figures fitted to one screen, tilt buttons for touch, iOS tap fixes. Shared code in `touch.js`.
- Added `induction/` (Electromagnetic Induction) as a Simulations card after Simple Motor and Loudspeaker, plus `images/induction.png`. Open point: step 1 of its exam-style box says the wire or coil moves, while Part 1 of the page moves the magnet; the author has not yet said whether to reword it.
