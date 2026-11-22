# Topic 4 — Waves: SOP notes

Build: `python3 tools/build_waves.py && python3 tools/build_manifest.py`.
Modules: `wv_diagrams.py` (transverse and longitudinal drawings), `wv_nn.py`
(N1–N9, N9 = key words), `wv_tricky.py` (T1–T7 and the flashcards). The
five calculation types already in the file are embedded (`EMBEDS`).

## Rules for this page (author-approved; keep in every edit)

- Infrasound and the ear are H and P (4.17P/4.18P); the sonar/echo 6-mark scheme and seismic waves are H and P. Their flashcards live in the `sound-ear` section so they hide with it.
- All mechanical waves need a medium; the wavefront definition and the clap-echo method follow the blind-check wording in the notes below.

## Step 1 — lists approved

Author approved the lists (2026-11-17) as drafted (Topic 5 was done first
at his request). The sections were renumbered against the real spec
numbering while writing: the ear is 4.12P, ultrasound 4.13P, infrasound
4.14P, uses 4.15P, sound between media 4.16P, core practical 4.17.

## Step 2 — checked against the content list and examiners' reports

Spec (copy at trafalgarschool.org.uk, 4.1–4.17). Physics-only: 4.8P,
4.9P, 4.12P–4.16P. Higher-only (school checklist, approved by the author):
4.8P, the speed part of 4.10, 4.11, 4.12P–4.15P. Tags: N8 and T4 and T5
carry H and P; N7 and T3 are untagged because 4.9P/4.10/4.16P content is
mixed with 4.10 for all; 4.11's wavelength dependence is one line in N7.

Reports and mark schemes read: 1H June 2022 report, 1H June 2023 mark
scheme, 1H June 2024 mark scheme, 1H June 2025 report.

| Series / Q | Examiner / scheme | Where it went |
|---|---|---|
| 1H 2023 Q1(a) | f = 330 ÷ 0.011 = 30 000 Hz; 30/300/3000 = 1 mark | N4 worked and q1 |
| 1H 2023 Q1(b) | bat echo 18 ms: halve the time or the distance; 5.94 (no halving) = 3 of 4 | T4 explain, worked, q1 |
| 1H 2023 Q6(a) | reaction time 0.23 s is 63% of 0.36 s over 120 m; improve by increasing the distance | N6 explain and q2 |
| 1H 2023 Q6(b) | refraction caused by a change in speed; sound speeds up, light slows down entering water | N7, T3 |
| 1H 2024 Q10(a) | ultrasound and infrasound are longitudinal | N3, N8 |
| 1H 2024 Q10(c) | carpets/curtains absorb more, less reflected; wood and paint reflect; "echoes" accepted | N7 explain, worked, q4 |
| 1H 2024 Q10(d) | 6-mark sonar: ultrasound pulse, travels, reflected by sea bed, time measured, speed known, d = v t, halved; two of ultrasound/pulse/halving/calculation for L3 | T4 explain and q5 |
| 1H 2025 Q1(b) | distance in the diagram must be doubled | T4 explain |
| 1H 2025 Q1(c) | why infrasound is not heard: frequency too low, or a named part of the ear does not respond | N8 explain and worked |
| 1H 2025 Q3(a)(iii) | ripple speed: time a crest over a distance, or count waves for f then v = fλ | N6 explain and q4 |
| 1H 2025 Q3(b)(i) | "sound" given as an EM wave | N3 q6 |
| 1H 2025 Q3(b)(ii) | rock in an S wave: oscillations perpendicular to the direction of travel | N3 q4, T2 |
| 1H 2025 Q3(b)(iii) | two-step seismic distance with units | (numbers not reproduced; T5 stays qualitative) |
| 1H 2022 Q9(b)(i) | v = fλ: GHz not converted; substitute first then rearrange | N4 explain |
| 1H 2022 Q10(a)(ii) | why the ear detects a limited range: sensitivity / size; frequency confused with loudness | N2 trap, N8 q3 |
| 1H 2022 Q10(b) | crack in a bar: echo earlier from the crack; far-end pulse smaller because energy already reflected; amplitude ↔ energy | T4 explain and q6 |
| 1H 2022 Q10(c) | seismic 6-marker: observations alone = Level 1; conclusions (liquid core, density change) needed | T5 explain, worked, q4, q5 |

## Step 3 — redraft

Findings written straight into the sections.

## Step 4 — every calculation and standard explanation present

Calculations: v = fλ, v = x/t, T = 1/f and counting, echo distances with
halving, string loops and ripple wavelengths (types + N4, N5, T1, T4,
T6). Explanations: energy not matter and the evidence; the definitions;
transverse/longitudinal with the credited phrase; measuring methods; the
four boundary effects; refraction of waves; the ear and its range;
ultrasound uses; seismic conclusions; the core practical; three plans.

## Step 7 — blind check

A separate agent recomputed every answer and read every explanation and
both diagrams. Findings, all fixed: the wavefront model answer in N2 q6
described a line along the direction of travel (points on neighbouring
waves) — now a line across one crest; the T1 worked example told students
to read a period off a graph the part could not show — now given as data;
0.23/0.36 is 64% not 63% — the travel time is now written as 0.364 s, which
is what the scheme used; "longitudinal waves need a medium" implied
transverse ones do not — now "all mechanical waves"; the infrasound key-word
question and the two ultrasound/infrasound flashcards were untagged —
question tagged H and P, facts re-homed to N8; a pointer to a clap-echo
method that T4 did not contain — the method is now written out in N6.

## Step 8 — headless test

Playwright: 23 section numerics and 20 choices entered through the UI and
marked correct; no KaTeX errors; no sideways scroll at 390 px; 10 graphs
and 2 diagrams render; the booklet modal offers the notes mode.

## Revisions

### 2026-11-22 — exam-wording verification against the question database

Every model answer, worked step, checklist, blurb and flashcard was
checked by a separate agent against the closest parts in the past-paper
question database (`Question DB/by-topic/topic-04.md`, 31 parts matched;
report in the session scratchpad). Changes, with the scheme that drove each:

| Reference | Change | Scheme |
|---|---|---|
| waves / transverse-longitudinal (explain) | slinky dropped as an exam example; EM wave / ripples / string given for transverse | 1H June 2025 Q3(b)(i): "ignore waves on a spring; ignore earthquake or seismic P or S" |
| waves / explain-wave-types (blurb, explain), wv-t2-q2, transverse-longitudinal, fact 31 | "up and down / side to side scores nothing" → it earns the oscillation mark; the comparison with the direction of travel is the second mark and the one dropped | 1H Nov 2021 Q2(b)(iii) "1 mark only"; June 2025 Q3(b)(ii) and June 2019 Q2(c)(ii) accept "up and down / forwards and backwards / shake" |
| waves / wv-t2-q1 | command word Explain → Describe | SAM Q1(a), Nov 2021 Q2(b)(iii), June 2025 Q3(b)(ii) all use Describe |
| waves / seismic (explain), wv-t5-q4, fact 40 | P-wave shadow: "sudden change in density → core denser" → refracted at a solid/liquid boundary → the core is liquid; solid inner core added (P waves through the centre arrive earlier) | 1H June 2022 Q10(c) indicative content; Nov 2020 Q10(d) |
| waves / seismic (blurb), fact 41 | "marked on the conclusions, not the observations" → observations credited, conclusions needed for the top level | June 2022 Q10(c) lists the observations as AO1 bullets |
| waves / measuring-wave-speed wv-n6-q4, core-practical-waves list | frequency step leads with counting waves in a measured time; "measure frequency" alone insufficient; not "one second" | June 2025 Q3(a)(iii) "'measure frequency' is not sufficient"; Nov 2021 Q2(b)(i) "ignore in one second" |
| waves / measuring-wave-speed checklist and Method B | improvement must carry its effect; "more accurate" alone not accepted | June 2019 Q6(a) "do not accept 'more accurate' without qualification"; Nov 2020 Q6(a)(iii) "with effect" |
| waves / sound-ear (explain) | "below 20 Hz" alone = 2 marks; named-part route needs the effect | June 2025 Q1(c) guidance |
| waves / echo-distances (explain) | scheme marks added beside the report quotes: 0.023 s = 2 of 3 (2025), 72 m = 1 of 2 (Nov 2020); halving is its own indicative bullet (2024 Q10(d)) | June 2025 Q1(b); Nov 2020 Q10(c); June 2024 Q10(d) |
| waves / wv-t4-q6 | crack: "reflected (or absorbed)" | June 2022 Q10(b)(ii) |

No stored numeric answer changed; `check_topic.js waves` passes on both
tiers (53 numerics, 20 choices, no KaTeX errors, phone width clean).
Not acted on (recorded for the author): the H list in the report — a
"describe how a vibrating fork makes a sound wave travel" question
(2018 Q5(a), 2019 Q6(b): "neighbouring particles vibrate"), the
ripple-frequency 3-marker, the scaled-diagram wavelength, the aerial
half-wavelength, reflection keeps its speed (Nov 2020 Q5(c)), the energy
budget at a boundary (2024 Q10(b)), "why the times vary" (Nov 2020
Q6(a)(ii)), the echo method as a 3-mark describe (Nov 2021 Q1(b)(ii)).
