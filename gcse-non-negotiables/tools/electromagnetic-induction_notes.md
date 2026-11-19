# Topic 13 — Electromagnetic induction: SOP notes

Build: `python3 tools/build_electromagnetic_induction.py && python3 tools/build_manifest.py`.
Modules: `ei_diagrams.py` (magnet into a coil with the meter kick, the
alternator and dynamo side by side, the three output graphs, the
loudspeaker and microphone in section, the transformer, the national
grid, the falling-magnet practical — painted with the `--ink` /
`--accent` variables and placed in the explain parts of N1, N3, N4, N5,
N7 and T8), `ei_nn.py` (N1–N10, N10 = key words; `INDUCTION_CHAIN`,
`INDUCTION_LEAD`, `SPEAKER_CHAIN`), `ei_tricky.py` (T1–T8 and the
flashcards). The three existing calculation types are embedded: `turns`
in N6 (`turns-ratio`), `tx-power` in N8 (`transformer-power`), `loss` in
N9 (`transmission-loss`).

## Rules for this page (author-approved; keep in every edit)

- **The standard chains are the author's, word for word.** The
  four-step induction chain is `EXAM.induction` in
  `induction/src/build.mjs` (GCSE level; the A-level steps there are not
  used on this site) and the seven-step loudspeaker chain is
  `EXAM.speaker` in `simple-motor/src/build.mjs`. They must stay
  identical there and here (`INDUCTION_CHAIN`, `SPEAKER_CHAIN`). One
  line was added in front of the induction chain, with the author's
  approval (2026-11-19), for the case where the magnet moves and the
  coil is still: *"The magnet moves relative to the coil (either may
  move)."* (`INDUCTION_LEAD`) — it stands **in place of step 1** (which
  says the wire or coil moves), and steps 2–4 follow unchanged. The
  motor chains live in Topic 12.
- **Induces, never produces.** A pd is *induced*; a current *flows* if
  the circuit is closed. "Produces" was rejected by the June 2025
  examiners and is not used for an induced pd anywhere on the page.
- **Tiers.** From the Pearson spec (the school checklist covers Paper 1
  only): 13.1P, 13.2, 13.3P, 13.5, 13.6, 13.7P, 13.11P Higher only →
  N1, N2, N3, N5, N6, N9, T1, T2, T3, T5, T6, T8 carry H; 13.4P, 13.8,
  13.9, 13.10 both tiers → N4, N7, N8, T4, T7 and the key words are
  untagged (with the Higher key-word questions and the 13.11P questions
  in T7 tagged individually). The P statements give P on N1, N3, N4, N6,
  N9, T3, T4, T6 and the two 13.11P questions in T7. **`tx-power` is
  now both tiers** (13.10 is not a bold statement and the equation is on
  the Foundation list); `turns` (13.7P) and `loss` (13.11P) stay Higher.
  Under the Foundation filter the page shows N4, N7, N8, N10, T4 and T7.
- **Changing** is the word in the transformer explanation (the field in
  the core is changing — the mark most often lost in June 2025), and the
  dynamo's d.c. is "one direction, rising and falling", never "steady".
- Equations: the two transformer equations and $P = IV$, $P = I^2R$ are
  on the list; checklists say "use".

## Step 1 — lists approved

Author approved N1–N10 / T1–T8 (2026-11-19, "Looks good"), with the
reminder to lift his standard explanations from the induction page, and
accepted the two proposals in the same message: `tx-power` to both tiers,
and the lead line for a moving magnet in front of his chain.

## Step 2 — checked against the content list and examiners' reports

Spec 13.1P–13.11P read from the Pearson PDF (`gcse-physics-spec.pdf`;
the bold marking does not survive extraction, so the Higher-only set was
confirmed from the docbrown.info summary, which marks "(HT only)" on
13.1P, 13.2, 13.3P, 13.5, 13.6, 13.7P and 13.11P). Coverage: 13.1P (N1,
T1, T8), 13.2 (N2, T1, T2, T8), 13.3P (N3, T3), 13.4P (N4, T4), 13.5/13.6
(N5, T5), 13.7P (N6 + type, T5, T6), 13.8/13.9 (N7, T7), 13.10 (N8 +
type, T6), 13.11P (N9 + type, T7).

Reports and mark schemes read: 2H June 2023 report (Q8(a)(iii), Q10),
2H June 2024 mark scheme (Q10), 2H June 2025 report (Q6).

| Series / Q | Examiner / scheme | Where it went |
|---|---|---|
| 2H 2023 Q8(a)(iii) | regenerative braking: answers gave "detail of dynamo construction such as split ring commutators without mentioning an electric current or recharging the battery"; credit for the device acting as a dynamo causing a current that recharges the battery, energy from the kinetic store | N3 explain, T1 explain and q4 |
| 2H 2023 Q10(a)(ii) | dynamo harder to turn with a lamp: "the lamp would increase resistance" is wrong (a lamp has far less resistance than a voltmeter); wanted "the lamp required an energy transfer to produce light" from extra work turning; also "an induced current in the rotating coil … produces a magnetic field" opposing the motion — "very few examples"; "turned more" too vague | N2 explain, T2 whole section |
| 2H 2023 Q10(b) | transformer calculations: "almost all answered this question correctly" | N6, T6 |
| 2H 2023 Q10(c) | compare loudspeaker and microphone, 6 marks: Level 2 described the speaker more fully; Level 3 needed the interaction between the coil's field and the magnet's field, and for the microphone "how electromagnetic induction is a result of a coil moving in a magnetic field"; one device may be less complete if both are referenced | N4 explain, T4 whole section |
| 2H 2024 Q10(a)(i) | magnet falling through a coil, 3 marks (any three): field lines cut / changing field; induces a voltage or current; the voltmeter measures the induced pd (two marks); electrons in the wire experience a force; the induced pd changes magnitude and direction as the magnet passes | N1 explain and q1, T1 explain, worked and questions |
| 2H 2024 Q10(a)(ii) | practical steps, 4 marks (any four): different heights; metre rule; height in steps (5 cm); record the maximum reading; repeat and average; voltmeter on a.c.; plot reading against height; move the coil / different tubes | T8 whole section |
| 2H 2024 Q10(b) | transformer 11 000 V → 230 V, 6 marks: construction (closed iron core, primary with many more turns), operation (a.c. → changing field in core → a.c. induced in secondary), step-down, ratio 48:1; Level 3 needs all three with one tolerated weak | N5, N6 explain, T5 whole section |
| 2H 2025 Q6(a)(i) | how a.c. in the primary induces a.c. in the secondary, 3 marks: a.c. in primary; changing field in the core; alternating pd induced in the secondary; "marks were usually lost by not stating the magnetic field in the core was changing"; "produces" not accepted, "induces" required; "confusion between a p.d. being induced and a p.d. being produced" | N1 explain, N5 explain, worked and q2, q5, T1, T5 |
| 2H 2025 Q6(a)(ii) | transformer calculation: confident substitution and rearrangement; a few used the pd–current equation instead of the turns equation | N6 explain, T6 explain and q5 |
| 2H 2025 Q6(c) | commutator; many described a dynamo for a motor — "the motor does not produce a current" | (Topic 12 T7; the reverse trap noted in N3) |

## Step 3 — redraft

T1 was built round the 2024 falling-magnet marks with the lead line;
T2 made its own section because the field-opposes-motion mark was so
rarely given; T4's table puts the two chains side by side with the
Level 3 requirement for each; T5 carries the 2024 levels; T6's table
says which transformer equation from what the question gives.

## Step 4 — every calculation and standard explanation present

Calculations: the turns ratio for a pd or a number of turns; the
pd–current equation for a current (mA, kV); both chained; current from
P = IV; cable loss from P = I²R at two pds; frequency from period.
Explanations: the induction chain for a moving coil and a moving
magnet; the meter kick and its reversal; size and direction factors; the
opposing field and the harder-to-turn dynamo; alternator vs dynamo with
graphs; the loudspeaker and microphone chains; the transformer in three
marks and six; why no d.c.; the grid chain in words and with equations;
the seven steps for the practical; the key words.

## Step 7 — blind check

A separate agent, given only the JSON and `SCHEMA.md`, recomputed every
numeric answer (all agree, including the three embedded types), checked
every choice index, mark count and worked-example step count, the ids,
`facts[].section`, the embedded types' consistency, both chains word for
word, "produces" against the rule, and the SVG arrowheads and labels.
No physics or number errors. Findings, all fixed before the push:

- Tiering: T1 and T8 are 13.1P content but carried H without P — now
  H, P; ei-t5-q4 (the turns ratio, 13.7P) now P; ei-kw-q4 (step-down,
  13.6) now H. T6 mixed the Higher-Physics turns equation with two
  pure-13.10 questions (both tiers), so those two moved into N8 as
  ei-n8-q5 and ei-n8-q6 (before the first push, so no id was broken)
  and T6 stays H, P with its three remaining questions renumbered.
- Cross-references from both-tier sections to Higher ones (N4 → "T4",
  N8 → "N6"/"T6", T7 → "N9") renumber under the Foundation filter — now
  named by section.
- The chain: N1 said the lead line is followed by steps 2–4, while T1's
  list carried all four steps after it (step 1 — "the wire or coil moves"
  — is false when the magnet moves). T1 now matches N1: lead line, then
  steps 2–4. Recorded in the rules block above.
- "Produces": the dynamo worked-example stem said "produces a direct
  current" and six places said the induced field "opposes the change
  that produced it" — now "the output … is a direct current" and
  "caused it".
- Figures: the first figure's coil was wired with one lead to the meter
  (an open circuit while the text says closed) — now two leads; the
  generator brushes floated clear of the rings — now touching; the
  microphone panel said "→ current" — now "→ pd induced"; the practical
  figure said 5 cm steps while the text used 10 cm — now "equal steps".
- The 6-mark practice question in T4 duplicated its own worked example —
  now asks for the microphone with the difference from the speaker.
- Numbers and TeX: ei-n6-q3 stepped up to an unrealistic 1250 kV — now
  6400 turns and 400 kV; `$a \times 10^6 / b \times 10^3$` in five
  walkthroughs read as 10⁹ left to right — now `\dfrac`; plain-text
  equations in hints, checklists and flashcards (section hints and facts
  are rendered through the TeX pass) — now `$…$`, and the same fix
  applied to Topic 12's six hints and two flashcards.
- Wording: ei-t5-q2's distractor stated the correct rule; the "voltmeter
  … worth two of the marks" sentence; N2's "three for size" title with a
  fourth row; a "core that changes" definition; ei-t8-q5 with no
  context; N7 (both tiers) mentioned "current squared" (13.11P) — now
  "rises steeply".

Left as they were: the key-word table and its flashcards show under the
Foundation filter although most terms are Higher (the questions are
tagged; the definitions do no harm); the T3 "twice as fast" trace is
drawn 1.4× taller rather than 2× (a sketch); paraphrases of the chains
in worked examples and model answers, where the `<ol>` lists are
verbatim.

## Step 8 — headless test

`check_topic.js` with `--filter Foundation`: 33 of 33 numerics and 39
of 39 choices marked correct on the Higher view; 11 of 11 numerics and 11
of 11 choices under Foundation (N4, N7, N8 + `tx-power`, N10, T4, T7
shown); no KaTeX errors; 7 diagrams; 65 flashcards; 132 ref buttons;
booklet offers the notes mode; at 390 px nothing scrolls sideways, no
card wider than the screen, nothing sticks out.
