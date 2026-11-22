# Topic 6 — Radioactivity: SOP notes

Build: `python3 tools/build_radioactivity.py && python3 tools/build_manifest.py`.
Modules: `ra_diagrams.py` (penetration, Rutherford scattering, chain
reaction), `ra_nn_a.py` (N1–N5), `ra_nn_b.py` (N6–N10, N10 = key words),
`ra_tricky.py` (T1–T9 and the flashcards). The six calculation types
already in the file are embedded (`EMBEDS`).

## Rules for this page (author-approved; keep in every edit)

- No Higher-only content. The spec copy's P on 6.28/6.30 is overruled by the school checklist the author approved: N9 and T2 are untagged; P starts at 6.33P (T5–T9).
- Internal sources for tumours can be sealed gamma as well as beta/alpha (June 2024 scheme) — keep that in the table, checklist, question and flashcard.
- The nucleus is "tens of thousands of times smaller" than the atom (10⁻¹⁵ m against 10⁻¹⁰ m); the chain-reaction drawing is uncontrolled and its footer says so.

## Step 1 — lists approved

Author approved the N1–N10 / T1–T9 lists (2026-11-17) as drafted.

## Step 2 — checked against the content list and examiners' reports

Spec (copy at trafalgarschool.org.uk, 6.1–6.46P). No Higher-only
statements. The spec copy marks 6.28 and 6.30 with P but the school
checklist (which the author approved for tiering) has them for all;
followed the checklist, so N9 and T2 are untagged and P starts at 6.33P
(T5–T9). Every statement is covered: 6.1–6.9 (N1–N3), 6.10–6.16 (N4, N5),
6.17 (T1), 6.18–6.22 (N6), 6.23–6.27 (N7, T3), 6.28/6.30 (N9, T2),
6.29/6.31/6.32 (N8, T4), 6.33P (T5), 6.34P/6.35P (T6), 6.36P (T9),
6.37P–6.42P (T7), 6.43P–6.46P (T8).

Reports and mark schemes read: 1H June 2022 report, 1H June 2023 mark
scheme, 1H June 2024 mark scheme, 1H June 2025 report.

| Series / Q | Examiner / scheme | Where it went |
|---|---|---|
| 1H 2022 Q4(a)(ii) | 6-min / 6-day tracers: link to the scan ("technician could not take a reading"; patient exposed for days); "too fast / too slow" alone scores nothing | T2 explain and q1 |
| 1H 2022 Q4(a)(iii) | two precautions must be different kinds; gloves + masks = one; lead credited, aluminium ignored | N8 explain and q2 |
| 1H 2022 Q4(b)(i) | control rods absorb neutrons; most confused them with the moderator | T7 explain and q2 |
| 1H 2022 Q4(b)(iii) | energy chain: KE of fission fragments → thermal (coolant) → steam → KE of turbine; few got both marks | T7 explain and q4 |
| 1H 2022 Q8(a) | 0.15 nm → 1.5 × 10⁻¹⁰ m "was difficult" | N1 q4 |
| 1H 2022 Q8(b)(ii) | most through → empty space; few back through 180° → dense small nucleus; Bohr electrons ignored | T1 table, worked, q2 |
| 1H 2022 Q8(c) | marble-and-weight model and its limitations (no charge, not to scale, 2-D) | T1 q6 |
| 1H 2023 Q7(a)(i) | isotope = same atomic number | N2 explain and q2 |
| 1H 2023 Q7(b) | plot a decay curve from a table | (types: decay-graph) |
| 1H 2023 Q10(a)(ii) | RTG: long half-life + a reason (mission length, cannot replace) | T2 q2 |
| 1H 2023 Q10(c) | 6-mark chain reaction / control rods / moderator levels: L3 = detail on two + mention of the third | T7 explain and worked |
| 1H 2024 Q4(a) | gamma is the one applied internally | T5 explain |
| 1H 2024 Q4(b)(i) | PET: annihilate; two gamma; opposite directions; detected; same time; time difference → position | T6 explain, worked, q3 |
| 1H 2024 Q4(b)(ii) | PET isotopes made nearby: short half-life, decays rapidly, used shortly after production | T6 explain and q2 |
| 1H 2024 Q4(c) | irradiation: does not make it radioactive; stopped by shielding; source outside; stops when removed | N8 table, T4 |
| 1H 2024 Q4(d)(i) | half-life from a graph: horizontal line at half, read the time (1 + 1) | N7 explain, T3 |
| 1H 2024 Q8(a),(b) | alpha charge +2; ionisation = loss/gain of electrons, "knocking electrons out" | N4 explain and q5, N3 |
| 1H 2024 Q8(c) | background count method: GM tube and counter, no sources, counts in a time, divide, repeat, average | N5 explain and q3 |
| 1H 2024 Q8(d)(iv) | beta symbol with −1; numbers balance | N6 explain |
| 1H 2025 Q4(b)(i) | percentage remaining from a curve: read the real starting value | T3 explain and q4 |
| 1H 2025 Q4(b)(ii) | positron meets electron: annihilate; release (a pair of) gamma rays | T6 q1 |
| 1H 2025 Q4(c) | fission of one nucleus: a well-structured explanation | T7 q1 |
| 1H 2025 Q9(b) | β⁺ asked, β⁻ described — the common error | N6 explain and q2 |
| 1H 2025 Q9(c) | 6-mark alpha vs gamma: L3 needs the effect of each decay on the nucleus | N4 worked |
| 1H 2025 Q10(b)(i) | fusion: "nuclei", not "atoms" or "particles" | T8 explain and q6 |

## Step 3 — redraft

Findings written straight into the sections.

## Step 4 — every calculation and standard explanation present

Calculations: nuclide notation, balancing, half-life (fraction, time,
graph, with background, backwards, ratio), corrected count, nm → m.
Explanations: atom and neutrality; isotopes; ions; radiations compared;
background and detection; the five decays; half-life and randomness;
dangers, precautions, contamination vs irradiation; each spec use with
reasons; the three atomic models and the scattering evidence; tumours;
PET; fission, chain reaction, moderator and control rods, energy chain,
waste; fusion and its conditions; nuclear power for and against.

## Step 7 — blind check

A separate agent recomputed every answer and read every explanation and
the three diagrams. Findings, all fixed: the atom text said the nucleus is
1/10 000 of the atom while quoting 10⁻¹⁰ and 10⁻¹⁵ m — now "tens of
thousands of times smaller"; the tumours section said internal sources
are beta/alpha only while citing the June 2024 scheme that gamma is the
radiation applied internally — table, equations, checklist, q2 and the
flashcard now allow a sealed gamma source; the chain-reaction drawing
shows two neutrons going on (uncontrolled) while its footer said
"controlled" — footer reworded; a garbled sentence in N6 about β⁺
reworded.

## Step 8 — headless test

Playwright: 11 section numerics and 29 choices entered through the UI and
marked correct; no KaTeX errors; no sideways scroll at 390 px; 10 graphs
and 3 diagrams render; P badges on T5–T9; the booklet modal offers the
notes mode.

## Revisions

### 2026-11-22 — exam-wording verification against the question database

A separate agent compared the page with `Question DB/by-topic/topic-06.md`
(28 questions, 25 with schemes; two question images opened). Changes:

| Reference | Change | Scheme |
|---|---|---|
| radioactivity / radiation-types (explain, worked) | "alpha is the weakest scores nothing" → a comparison in the right dimension scores ("more ionising than gamma" was a mark alone); the compare worked warns that Nov 2021 ignored range, penetration and ionisation — nature and the change in A and Z first | 1H June 2019 Q8(a)(ii); Nov 2021 Q9(d); June 2025 Q9(c) |
| radioactivity / ra-n4-q6 | method controls: source in front of (not in) the tube, same time, same distance; aluminium absorbs the beta | 1H June 2018 Q3(a); June 2024 Q8(d)(iii); Nov 2021 Q3(c)(i) |
| radioactivity / ra-n6-q5, flashcard | gamma: element does not change; rearranges, loses energy, becomes more stable | 1H Nov 2021 Q9(c); June 2025 Q9(c) |
| radioactivity / dangers-precautions (explain) | "gloves and masks scored one" because masks are ignored, not because both are PPE; distance added | 1H June 2022 Q4(a)(iii) |
| radioactivity / uses table, ra-n9-q4 | gamma very penetrating → kills bacteria → preserves / sterilises | 1H Nov 2021 Q9(b) |
| radioactivity / atomic-model (explain), ra-t1-q6 | the 2022 scattering scheme quoted as written (three observations, three conclusions; small angles / large angles, not 180°); credited model limitations (2D, one marble, same speed) | 1H June 2022 Q8(b)(ii), Q8(c)(ii) |
| radioactivity / half-life-hard (blurb) | the hard forms actually set (graph → percentage, half-lives in years, fractions); background-in-graph noted as the core-practical method | 1H June 2024 Q4(d)(i); June 2025 Q4(b)(i); June 2019 Q3(c); Nov 2020 Q7(c) |
| radioactivity / tumours (explain) | the 2024 options were radio waves, not UV (image checked) | 1H June 2024 Q4(a) |
| radioactivity / pet-scanners (explain), ra-t6-q1 | "collide" credited; "meet / combine / interact / attract / light" ignored | 1H June 2025 Q4(b)(ii) |
| radioactivity / fission-reactor (explain) | the "detail on two, mention the third" level rule removed; three strands to cover | 1H June 2023 Q10(c) |
| radioactivity / fusion (explain, worked, ra-t8-q2, flashcard) | kinetic energy **overcomes the repulsion** as its own point; **E = mc² added** as a supplied equation with the 2025 Sun example and the unit mark | 1H June 2018 Q10(a)(i); Nov 2020 Q4(c); June 2025 Q10(b)(ii) |
| radioactivity / nuclear-power (title, blurb, explain, worked) | "Evaluate" is never the command word in the bank — now "the for-and-against question" with Discuss (Nov 2020) / Compare (Nov 2021) / add to the lists (June 2026); the unsupported "caps the level" rule removed; the 2020 credited points added | 1H Nov 2020 Q8(c); Nov 2021 Q10(b); June 2026 Q4(c) |

No stored answer changed; `check_topic.js radioactivity` passes on both
tiers. H list in the report: the two-rock GM method as a practice question
(2018 Q3(a)), the beta-absorption investigation (2024 Q8(d)), count rate as
a gradient and "random, not 'difficult to predict'" (Nov 2020 Q7(e)),
plotting a decay curve (2018 Q3(b), 2023 Q7(b)), the longer-half-life
sample being more dangerous (2024 Q4(d)(ii)), eating contaminated food
(Nov 2021 Q9(a)), the 2019 tumour 4-marker's exact lines, electron capture
(SAM Q6(c)). Also flagged: ra-t2-q3's "thin sheet" gauge argues from beta
being stopped by a few mm of aluminium, which the 2024 investigation
contradicts — consider steel plate.
