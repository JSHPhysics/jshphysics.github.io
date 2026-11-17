# Topic 7 — Astronomy: SOP notes

Build: `python3 tools/build_astronomy.py && python3 tools/build_manifest.py`.
Modules: `as_diagrams.py` (circular orbit with velocity and force arrows;
the two life cycles as a flow chart), `as_types.py` (the one calculation
type, `weight-elsewhere`, added because the topic had none), `as_nn.py`
(N1–N9, N9 = key words), `as_tricky.py` (T1–T7 and the flashcards). The
type is embedded in N2 (`EMBEDS`).

## Step 1 — lists approved

Author approved the N1–N9 / T1–T7 lists (2026-11-17) as drafted
("Approved, go").

## Step 2 — checked against the content list and examiners' reports

Spec (copy at trafalgarschool.org.uk, 7.1P–7.19P). Every statement is
Physics-only and none is Higher-only, so every section carries P and
none H. Coverage: 7.1P (N2, T7), 7.2P/7.3P (N1), 7.4P (T1), 7.5P (N3, T2),
7.6P/7.7P (N4, T2), 7.8P–7.10P (N6, T4), 7.11P/7.12P (N5), 7.13P (N6, T3),
7.14P/7.15P (N6, T4), 7.16P (N7), 7.17P (T5), 7.18P (N7), 7.19P (N8, T6).

Reports and mark schemes read: 1H June 2022 report, 1H June 2023 mark
scheme, 1H June 2024 mark scheme, 1H June 2025 report.

| Series / Q | Examiner / scheme | Where it went |
|---|---|---|
| 1H 2022 Q6(b)(i),(ii) | z and v calculations: mixing standard form and ordinary numbers lost the arithmetic; use the "show that" value | N5 explain, T3 explain and q1c, q4 |
| 1H 2022 Q6(b)(iii) | two spectra: more distant galaxy's lines at longer wavelength → greater red-shift (1); greater red-shift → faster → more distant galaxies faster → expansion (1) | T3 table, worked, q1 |
| 1H 2022 Q6(c) | telescopes on satellites: "stated the location without explaining why it matters" — must give atmosphere absorbs / distorts | N8 explain and worked, T6 explain and q6 |
| 1H 2023 Q4(d) | protostar → main sequence: gravity causes collapse; raises temperature until fusion; gravity and outward pressure balance; "fission" scored nothing | T5 table, worked, q3, q6 |
| 1H 2024 Q1(c)(ii) | red-shift, any 3: galaxies moving away; more distant → bigger red-shift; more distant → faster | N5 explain and q4 |
| 1H 2024 Q9(a) | circular motion: resultant force towards centre; accelerating because direction continuously changing / resultant force / velocity is a vector; "centripetal" alone ignored | N4 explain and worked, T2 chain 1 |
| 1H 2025 Q7(d) | constant temperature: rate of emission = rate of absorption | (Topic 5 T6 already covers it) |
| 1H 2025 Q10(a) | mass, not age, decides a black hole — "older stars" the common error | N7 explain and q2 |
| 1H 2025 Q10(c) | 6-mark Big Bang evidence levels: L3 = at least one piece of evidence described and linked to the aspect it supports (CMB "across the sky" → definite beginning; red-shift → expansion), the other identified; isolated statements = L1 | N6 explain and worked, T4 explain, worked, q6 |

## Step 3 — redraft

Findings written straight into the sections. The speed–radius link is
kept in the GCSE form throughout (for a stable orbit, smaller radius ↔
higher speed; if the speed changes the radius must change): the questions
compare two stable orbits rather than describing a thruster burn, which in
real orbital mechanics raises the orbit and would contradict the spec's
qualitative statement.

## Step 4 — every calculation and standard explanation present

Calculations: W = m g on another body; g from W and m; m from W and g;
Earth weight ↔ other-body weight via the mass and via ratios; z = Δλ/λ
and v = z c when the equations are supplied. Explanations: what the
Solar System consists of and the planets in order; why g differs (mass
and radius); mass unchanged, newton meter vs beam balance; the four kinds
of orbit and the two satellite orbits; comets' speed; circular motion
(velocity a vector, force towards the centre, speed unchanged, speed vs
radius); Doppler and red-shift; red-shift → expansion; both theories;
the CMB prediction and why it decided; both life cycles and the balance
inside a star; the history of observing; why telescopes go to space and
the disadvantages; geocentric → heliocentric and Galileo's evidence.

## Step 7 — blind check

A separate agent recomputed every numeric answer (17 of 17 correct,
including the type's seven), checked every choice, every model answer,
the tags, the flashcard section ids, the HTML/TeX and both SVGs by
computation (every velocity arrow tangential, every gravity arrow to the
centre). Findings, all fixed: as-t3-q1c carried a 0.2 % tolerance (the
field is a fraction), which would have failed 0.0494 — removed, so the
default 2 % applies; the white-dwarf row said it stops shrinking because
matter cannot be packed denser (false; degeneracy is beyond GCSE) —
clause cut; T1 said Galileo saw a full Venus (unobservable; gibbous is
what he saw and what disproves the geocentric model) — reworded to agree
with as-t1-q4; Galileo dated 1609 in N8 and 1610 in T1 — both now
1609–10; the N2 worked example duplicated the embedded type's p1 (900 kg,
3330 N) — now a 1200 kg lander, 4440 N; an orphan sentence in N5 about
standard form now says what it refers to; a redundant default tolerance
removed from as-n5-q5; `factsBlurb` added to SCHEMA.md (the app reads it
but it was undocumented). The agent queried the spec numbers on the star
sections; checked against the spec PDF: 7.16P Sun-like, 7.17P balance,
7.18P massive, 7.19P observing and telescopes — as in the file.

## Step 8 — headless test

Playwright at 1180 px: 10 section numerics, 31 choices and the 6 type
practice answers entered through the UI and marked correct; no KaTeX
errors; 3 diagrams render; P badges on all 16 sections; 84 flashcards. At
390 px no sideways scroll; the booklet modal offers the notes mode.
