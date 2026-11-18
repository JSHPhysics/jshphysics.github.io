# Revising a published topic from feedback

The playbook for the loop after students have used a page: a comment
comes in, the page is changed, tested and pushed. Read `../CLAUDE.md`
(Standing rules) and `SOP.md` first; this file is only the mechanics.

## 1. Find what the comment is about

Every card, question and figure on the site has a small **# ref** button
(added by `addReferenceButtons()` in `js/app.js`). Clicking it copies a
reference and shows it in a toast. Students quote that reference:

| Reference | Means |
|---|---|
| `forces-and-their-effects / winch` | the section with id `winch` on the Topic 9 page (deep link `#forces-and-their-effects/winch`) |
| `forces-and-their-effects / winch / fe-t7-q3d` | the question with id `fe-t7-q3d` in that section (`data-qid` in the DOM) |
| `forces-and-their-effects / winch / figure 2` | the second figure (diagram or graph) in DOM order inside that section card, counting from the top of the card and excluding figures inside an embedded calculation card |
| `forces-and-their-effects / moment / moment-p3` | a calculation type's practice question (the type card `moment`) |

Question ids are stable and never renumbered: `fe-t7-q3d` is Topic 9
("fe"), tricky-bits section 7, question 3, part d; type questions are
`<type>-w` (worked) and `<type>-p1` … `-p6`. Find the Python that owns it
with grep: `grep -rn "fe-t7-q3d" tools/`.

Module prefixes: `kc_` Topic 1, `mf_` 2, `en_` 3+8, `wv_` 4, `le_` 5,
`ra_` 6, `as_` 7, `fe_` 9 (10–15 follow when written).

## 2. Edit the source, never the JSON

`data/<topic>.json` is generated. Change the module (`fe_tricky.py` and so
on) or the diagram module, then rebuild:

    python3 tools/build_<topic>.py && python3 tools/build_manifest.py

The build runs the validator; fix anything it prints. Keep ids as they
are so references students have already quoted stay valid; if a question
is removed, leave its id unused rather than reusing it.

## 3. Decide how much checking the change needs

- **Wording only** (a sentence, a label, a typo): rebuild, run the
  headless check (step 4), push.
- **A number, an answer, a model answer, a diagram, a tag**: rebuild,
  headless check, and a blind re-check of that section by a separate
  agent given only the JSON and `SCHEMA.md` (SOP step 7) before pushing.
- **A new section or question**: the full SOP, starting with the
  author's approval of what it will contain.

Whatever the change, re-read the page's **Rules for this page** block at
the top of `tools/<topic>_notes.md` first; several of them exist because a
plausible-looking edit would break them (no critical-angle formula on
Topic 5, no comparing energy sources on Topics 3+8, no thruster burns on
Topic 7, the Level 2 / Level 3 shape of the winch answer on Topic 9).

## 4. Test

Serve the repo root and run the check script on the topic:

    cd <repo root>
    python3 -m http.server 8791 &
    node gcse-non-negotiables/tools/check_topic.js <topic-id> [--filter Foundation]

It enters every stored answer through the UI, counts KaTeX errors,
checks the phone width and the booklet, and exits 1 on any failure.
`--shots <dir> --sections a,b` saves screenshots of named sections to
look at. Playwright with Chromium must be installed (`require('playwright')`
from the directory you run in).

## 5. Record and push

- Add a dated line to the topic's `tools/<topic>_notes.md` under a
  "Revisions" heading: the reference quoted, what was changed and why.
- If the change made a new rule for the page, add it to the **Rules for
  this page** block; if it is a rule for every page, add it to the
  Standing rules in `../CLAUDE.md`.
- Commit as the author (see Standing rules for the identity and the
  trailer lines), `git fetch` first, push to `main`. Pages rebuilds in
  about a minute.

## Shared files

`js/app.js`, `css/app.css`, `css/sections.css`, `tools/validate.py`,
`tools/build_manifest.py` and `SCHEMA.md` are shared with the A-level
site in `../non-negotiables/`. Any change to one is copied to the other
in the same commit, and the A-level site is loaded once afterwards to
check it still renders (`check_topic.js <topic> --site non-negotiables`).
