# Brief for topic authors

You are writing ONE topic file for "The GCSE Non-negotiables", a practice
website for Edexcel GCSE Physics (1PH0) students, Foundation and Higher. A non-negotiable is a straightforward
calculation that every student must be able to do fluently. The site shows,
for each calculation type, one worked example and six practice questions
with a hint, a step-by-step walkthrough and an auto-checked numeric answer.

Project root: `/home/claude/gcse-non-negotiables/`

## Read first

`SCHEMA.md` in the project root is the contract for the JSON file: structure,
GCSE notation, standard values, tiers, and the verification rule. Read all
of it before writing anything.

## What to produce

1. `data/<topic-id>.json` — the topic file, following SCHEMA.md exactly.
2. `tools/calc_<topic-id>.py` — a Python script that computes every answer in
   your file (worked example + six practice questions for every type) from
   the question data using the standard constants in SCHEMA.md, and prints
   each answer rounded to 3 s.f. with its question id. Every `answer.value`
   in the JSON must come from this script's output, never from mental
   arithmetic. If a question needs a two-step calculation, compute it in
   two steps in the script too.
3. Run `python3 tools/validate.py data/<topic-id>.json` and fix every problem
   until it prints `OK`.

Do not create or edit any other file.

## Coverage

Your topic brief lists the calculation types to include. Cover every one of
them. You may add up to two more types if a genuine non-negotiable for this
topic is missing from the list, and you may rename types, but keep to
one skill per type — if a type on the list is really two separate skills
students would practise separately, split it.

Keep every type to the single-equation or two-equation level. Anything
that needs an extended argument, a graph to be drawn, or several
sub-parts belongs elsewhere; leave it out.

## Quality bar

- **Variety.** Across the seven questions in a type use seven different
  contexts (lab, sport, vehicles, space, household, industry, biology,
  music…) and clearly different numbers. Never reuse the worked example's
  numbers in a practice question.
- **Progression.** p1–p2 direct substitution; p3–p4 need a rearrangement
  or a unit conversion (mm, cm², kN, μA, nm, kWh, minutes…); p5–p6 are
  two-step (combine two equations, or find an intermediate quantity first).
- **One numeric answer per question.** No "state and explain", no
  multi-part questions, no "show that". If a question could be answered in
  more than one unit, state the required unit in the question.
- **Realistic numbers.** Sensible magnitudes for the context; answers that
  come out as tidy 2–3 s.f. values where possible.
- **Hints unblock, they do not solve.** One sentence: which equation, what
  is zero, what to convert, what to rearrange.
- **Walkthroughs are honest working.** The lines show the substituted
  numbers, and the final line is the answer with unit, rounded as the
  student should round it (usually 3 s.f.). The walkthrough's final value
  must agree with `answer.value`.
- **Standard constants only.** Use the exact values in SCHEMA.md so the
  stored answer matches a student working from a data sheet. If a question
  needs any other value (a specific density, resistivity, wavelength, mass
  of a planet…), give it in the question text.
- **Notation.** Plain text with Unicode superscripts/subscripts, `×` for
  multiplication, units with spaces (`m s⁻¹`). No LaTeX, no HTML, no
  Markdown inside JSON strings.
- **Tolerance.** The app marks an entry correct within 2% of `answer.value`.
  Set `"tolerance": 0.05` on a question only when rounding an intermediate
  quantity legitimately shifts the final answer by more than 2%.
- **Tier tags.** `boards` is `["Foundation", "Higher"]` for content on both
  tiers and `["Higher"]` for Higher-only content (your topic brief says
  which). A Foundation student sees only Foundation-tagged items. Within a
  Foundation type, p5–p6 may carry `"boards": ["Higher"]` if the two-step
  version needs a Higher-only rearrangement; otherwise keep every question
  on both tiers.
- **GCSE register.** Everyday contexts and numbers, no standard form unless
  the physics needs it, units in slash form (`m/s`). Hints and walkthroughs
  in plain words a 15-year-old reads without help. Where Edexcel gives the
  equation in words on the equation sheet, the method names it in words
  too ("change in velocity divided by time taken").
- **UK English**, and the register of a good textbook: direct, concrete,
  no filler.

## Final reply

When the validator passes, reply with: the topic id, the list of type ids
with their names, the total question count, and any decisions you made that
the project lead should know about (types added, split, or dropped; board
tags you narrowed; questions you gave a wider tolerance). Nothing else.
