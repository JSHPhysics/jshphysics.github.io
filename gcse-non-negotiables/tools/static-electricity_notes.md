# Topic 11 — Static electricity: SOP notes

Build: `python3 tools/build_static_electricity.py && python3 tools/build_manifest.py`.
Modules: `se_diagrams.py` (rubbing a rod with a cloth, the three force
cases, induction on a neutral object, earthing through a wire, the
electrostatic sprayer, fuelling with the bonding wire, the two field
diagrams — all painted with the `--ink` / `--accent` variables and placed
in the N1–N7 explain parts), `se_nn.py`
(N1–N8, N8 = key words), `se_tricky.py` (T1–T7 and the flashcards). The
topic has no calculation types (`EMBEDS = {}`, `types` empty): nothing in
11.1P–11.10P is a calculation. The home-page card therefore shows the
section count only (`app.js` leaves out "0 calculations" when a topic has
sections) and uses the `static-field` figure added to `figures.js`.

## Rules for this page (author-approved; keep in every edit)

- **Whole topic is Physics-only.** Every section carries P; nothing is H
  (11.1P–11.10P are all P in the Pearson spec and none is bold). Under
  the Foundation filter the P badge stays — P is not a tier.
- **Force → acceleration.** Any explanation of why two charged objects
  move apart or together says *like charges repel (or unlike attract), so
  a force is exerted on X (away from / towards Y), so X accelerates away
  (towards)*. The examiners are tight on linking the force to the
  acceleration and on saying which object the force acts on; "they repel"
  alone is not a full answer. T1 is built round this chain and every
  model answer on the page that describes movement uses it.
- **Only electrons move.** Charging by friction is always written as
  electrons transferred from one object to the other; the object that
  gains electrons becomes negative, the one that loses them positive.
  Positive charge never moves in a solid; "charge flows" is used only for
  conduction through a metal or a wire to earth.
- Sparks and shocks: a build-up of charge (an insulator, or a conductor
  that is not earthed) → a large potential difference → electrons jump
  across the gap through the air. Earthing is a conducting path that
  lets the excess electrons flow to earth (or up from earth) so the
  charge cannot build up.
- Field lines show the direction of the force on a **positive** charge:
  out of positive, into negative; the uniform field between plates is
  drawn as straight, equally spaced lines with arrows from + to −.
- No equations in this topic; nothing is to be memorised beyond the
  definitions in N8.

## Step 1 — lists approved

Author approved the N1–N8 / T1–T7 lists (2026-11-18, "onwards to topic
11") and added the force → acceleration rule above ("the examiners are
quite tight on the language of linking forces to acceleration"). T1 was
re-centred on it before anything was written.

## Step 2 — checked against the content list and examiners' reports

Spec 11.1P–11.10P (the Pearson PDF and the trafalgarschool copy could
not be fetched this session — the web tool now asks for provenance
approval on both and timed out — so the statements were taken from the
copy read for the earlier topics). Coverage: 11.1P/11.2P (N1, T1),
11.3P (N2, T1), 11.4P (N3, T2, T3), 11.5P (N4, T3), 11.6P (N5, T5),
11.7P/11.8P (N6, T4), 11.9P (N7), 11.10P (N7, T6, T7).

Reports and mark schemes read: 2H June 2023 report (Q1), 2H June 2024
mark scheme (Q1), 2H June 2025 report and scheme (Q4). The 2022 2H
report (mossleyhollins mirror) also prompted for provenance and was not
read.

| Series / Q | Examiner / scheme | Where it went |
|---|---|---|
| 2H 2023 Q1(a)(ii) | charging a plastic base by rubbing: electrons transferred from the base to the cloth (1), friction as the cause (1); "many omitted friction" | N1 explain and worked, T1 |
| 2H 2023 Q1(b) | a metal star touched to the cloth is charged by conduction, not friction — "friction charges insulators, not conductors" | N1 explain, N8 |
| 2H 2023 Q1(c) | induced charges on a dust particle near a positive base: the near-side negative scored, the fully correct diagram also shows the far-side positive — "the total numbers of positive and negative charges still balance" | N3 explain and diagram, T2 explain |
| 2H 2024 Q1(a) | identifying charges from attraction and repulsion: X attracted to Y and Z repelled from Y; repulsion is the only test of a charge | N2 explain and questions |
| 2H 2024 Q1(b) | electric field: "a region where (electric) charge experiences a force" (1); attraction or repulsion / direction of the force on a positive charge (1); "electricity" ignored | N7 explain and q1, T7, N8 |
| 2H 2024 Q1(c)(i) | field-line direction: arrows away from the positive charge | N7, T6 |
| 2H 2024 Q1(c)(ii) | field strength from a diagram: lines get further apart as distance increases, so the field is weaker | N7 explain, T6 |
| 2H 2025 Q4(a) | field between two plates: straight lines with arrows from the positive to the negative plate — 2; correct lines with the arrows reversed — 1 | N7 explain and worked, T6 table and flashcard |
| 2H 2025 Q4(b)(ii) | "a positive charge would be induced on the surface of the metal tube" — full marks for the induced charge on the near surface | T2 explain |
| 2H 2025 Q4(b)(iv) | earthed metal tube loses its charge: "the tube is a conductor, so charge flows through the metal and the connecting wire to earth"; leaving out "conductor" lost a mark; charge moves only "if it has somewhere to go" | N4 explain and worked, N6, T3 |

## Step 3 — redraft

The force → acceleration chain was written into every model answer that
describes an object moving (T1's worked balloons and q1–q6, N2's
questions, T2's water-stream and balloon-on-a-wall worked examples).
Conduction versus friction (2023 Q1(b)) added to N1; "conductor" as a
scoring word added to the earthing answers (2025 Q4(b)(iv)); the
reversed-arrows penalty (2025 Q4(a)) added to the T6 table.

## Step 4 — every calculation and standard explanation present

No calculations in the topic. Explanations: charging by friction and
why only insulators keep the charge; conduction; the three force cases
and identifying a charge by repulsion; induction with both induced
charges drawn; shocks from a car door and from a trolley; lightning;
earthing a positive and a negative object; the sprayer's three
advantages with their reasons; the fuelling danger-and-precaution
6-marker with a levels box; the field definition; radial and uniform
field diagrams and reading strength from line spacing; explaining
attraction, repulsion and sparks with the field idea; the key words.

## Step 7 — blind check

A separate agent, given only the JSON and `SCHEMA.md`, checked every
choice index against its explanation (27 of 27 agree), every mark table
against its total, every worked example's step count against its marks,
the tags (all P, no H), the ids, the cross-references, the flashcard
section ids, HTML and `$` balance, and the fuse / recall words (clean).
Findings, all fixed before the push:

- Physics: the car-door worked example and flashcard called the door
  "earthed (through the tyres)" while N6 says tyres insulate — now "a
  conductor at a different potential"; T2 called a stream of water a
  conductor with free electrons — now ions and the molecules shift; T6
  said there is "a gap of no field" between two like charges — now one
  point midway where the field is zero; the N1 figure's "equal + and −"
  rod and cloth were drawn with unequal counts (5+/4−, 3+/2−) — now
  5+/5− and 3+/3− before, 5+/7− and 3+/1− after; se-n4-q4 and se-n7-q6
  gave the charge no sign but answered for one — the models now cover
  both; N2's "attraction identifies X" now says the 2024 objects were all
  stated to be charged; the lightning-conductor "point lets charge leak
  away quietly" (three places) replaced by the field being strongest at
  the point, so the strike is led there.
- Force → acceleration: se-n2-q4 (hanging balls) stopped at "the forces
  push the balls apart" while T1 answered the same scenario with the
  acceleration link; T2's water-stream worked example stopped at "the
  stream bends"; N3's balloon-on-a-wall did not say which object the
  force acts on; N2's "a light object moves more" is now "accelerates
  more ($a = F/m$)".
- Language: three "the charge flows" in the friction section (explain,
  se-n1-q3, a flashcard) are now "the electrons flow"; se-kw-q4 asked
  for "charging by induction" though the object stays neutral — now
  "attraction by induction" (the spec's term).
- Structure: the key-words kicker was a bare "11" — now "11.1P–11.10P";
  se-n7-q1 duplicated se-kw-q1 word for word — se-n7-q1 is now the 2024
  2-mark version (definition + what a line's direction shows); the howto
  line about EWAU calculations removed (no calculations in this topic);
  `static-field` added to the figure list in `SCHEMA.md` (both sites).
- Wording: T5's title promised three advantages but listed four — now
  "each advantage with its reason", and the N5 flashcard lists all four;
  the T6 marking verdict "0 or 1 depending on the examiner" now commits
  to 1 of 2 with the reason; the sprayer nozzle "at a high pd" is now "at
  a high potential (a large pd relative to earth)"; the 2023 "base"
  flashcard now says what the base was.

Left as they were: "charge flows" in the earthing and bonding text (the
2025 scheme's own words); the three `\text{… + to −}` strips (KaTeX
renders them, 0 errors).

## Step 8 — headless test

`check_topic.js`: no stored numerics (none in the topic); 30 of 30
choices entered through the UI and marked correct; no KaTeX errors; 7
diagrams render; 15 P badges; 64 flashcards; booklet offers the notes
mode; at 390 px nothing scrolls sideways, no card is wider than the
screen and nothing sticks out.

## Revisions

### 2026-11-22 — exam-wording verification against the question database

A separate agent compared the page with `Question DB/by-topic/topic-11.md`
(9 questions, 31 marked parts, 2H 2018–2026) and grepped the whole bank
for sparks, lightning, fuelling and shocks (none set). Changes:

| Reference | Change | Scheme |
|---|---|---|
| static-electricity / charging-friction (explain) | the 2023 star question described as marked: electrons transferred to the metal, metal is a conductor, electrons travel through the person to earth (the cloth loses its charge; the star is earthed, not "charged by conduction") | 2H June 2023 Q1(b) |
| static-electricity / charge-forces (explain) | testing a charge now has the third mark — handle the object without discharging it — and the positive / negative / uncharged test with two rods | 2H Nov 2020 Q4(a)(iii); June 2026 Q1(c) |
| static-electricity / charge-forces, electron-force-chains (explain, se-t1-q2, se-t1-q5), flashcards | the author's chain is kept word for word; the claims that examiners *mark* the acceleration link and *mark down* "moves" are replaced by what the schemes credit beyond "they repel": **X is in Y's electric field** (2018, 2025) and the **result the question asks about** (2019 "so the spray is wider"); the field link added to the chain flashcard | 2H June 2018 Q4(c)(i); June 2025 Q4(b)(ii); June 2019 Q1(a)(ii); Nov 2021 Q1(c)(ii) |
| static-electricity / se-n3-q4, se-t2-q1, induction worked | induction chain in the credited words: a charge is **induced** → on the side **closest** → **opposite charges attract**; the near-force-beats-far-force argument kept as the reason, not a mark | 2H June 2018 Q4(a)(ii); June 2022 Q1(c) |
| static-electricity / earthing (explain) | the 2025 tube question as marked (does not become charged: conductor + connected to earth) | 2H June 2025 Q4(b)(iv) |
| static-electricity / se-n5-q2, sprayers-explain flashcard, static-uses worked | the earth wire conducts electrons so charge does not accumulate on the target (2019's two marks); the 2022 leaf points (electrons move between earth and leaf; the back of the leaf) replace "less wasted" in the marked steps | 2H June 2019 Q1(a)(iii); June 2022 Q1(c) |
| static-electricity / se-t5-q5, flashcard | the "coated patches repel further droplets" mechanism removed (no analogue; contradicts the earthing scheme) | 2H June 2019 Q1(a)(iii) |
| static-electricity / static-dangers, fuelling-question (blurb, title, table, flashcards), lede | no fuelling / spark / 6-mark question exists on Topic 11 in 2018–2025 — reframed as the 6-marker it could become; "Level 3", "Also accepted", "scores nothing" removed | bank 2018–2026 |
| static-electricity / electric-fields, fields-explain | the 2024 definition was 1 mark with alternative wordings; the 2025 soot scheme quoted as written; schemes ask for at least three lines; "fields interact / overlap" added, "repel earns nothing extra in a fields question" | 2H June 2024 Q1(b); June 2025 Q4(b)(ii), Q4(a); June 2022 Q1(a); June 2018 Q4(c)(i) |
| static-electricity / field-diagrams (table, worked) | lines need not touch the plates (2025); one reversed arrow or arrows both ways loses the direction mark | 2H June 2025 Q4(a); June 2019 Q1(b); Nov 2020 Q4(b)(iii) |

For the author: the standing rule (like charges repel → force on X away
from Y → X accelerates away) is unchanged on the page; what changed is
the claim about marking, since no 2H scheme 2018–2025 credits
"accelerates" or penalises "moves". No stored answer changed;
`check_topic.js static-electricity` passes on both tiers. H list in the
report: "electrons carry a negative charge" as a separate mark (2018
Q4(a)(i)), the gold-leaf electroscope (Nov 2021 Q1), the disc tapped to
earth that ends positive (Nov 2020 Q4(b)), force against distance
("inverse square law scores 2", 2018 Q4(c)(ii)), the supplied-equation
field calculation (2024 Q1(c)(iii)), "more lines = larger charge" (Nov 2021
Q1(c)(i)), "charge becomes zero… ignore becomes positive" (2025 Q4(b)(iii)).
