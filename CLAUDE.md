# jshphysics.github.io — notes for Claude

Static site served from `main` via GitHub Pages.

## File map

- `index.html` — gallery landing page (tool cards)
- `pedagogy.html` — "On the design of these tools" subpage with lightbox + hotspots
- `tools.json` — **single source of truth** for both pages. Both fetch this on load and build their content from it. The `_instructions` block at the top documents every field.
- `images/` — screenshots referenced by filename in `tools.json`
- `annotate.html` — local-only authoring tool (NOT committed; see "Authoring annotations" below)
- `.claude/launch.json` — local-only, used by Claude Preview tooling. Don't commit.

To add or change a tool: edit only `tools.json`. No HTML changes needed.

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
