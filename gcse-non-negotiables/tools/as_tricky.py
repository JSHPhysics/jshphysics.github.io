"""
as_tricky.py — Topic 7 (Astronomy): the tricky bits T1–T7 and the
flashcards. Every section is Physics-only.

T1 From geocentric to heliocentric   T5 How a star stays stable (and stops)
T2 Explaining orbits                 T6 Space telescopes: for and against
T3 The red-shift argument            T7 Weight and g the hard way
T4 Why the CMB decided it
"""

from revlib import (
    choice, diagram, explain, fact, group, mark_scheme, marks, numeric,
    practice, section, worked, written,
)
import as_diagrams as dg

# ---------------------------------------------------------------------
# T1 · Models of the Solar System
# ---------------------------------------------------------------------

section_t1 = section(
    "solar-system-models", "tricky", "From an Earth-centred to a Sun-centred Solar System", "7.4P",
    equations=[r"\text{geocentric: Earth at the centre}", r"\text{heliocentric: Sun at the centre}"],
    blurb="For two thousand years the Earth was at the centre of everything. The model changed when better observations — Galileo's telescope above all — showed things that could not be orbiting the Earth.",
    tags=["P"],
    checklist=[
        "Describe the geocentric and heliocentric models",
        "Explain how observations, especially with the telescope, led to the Sun-centred model",
        "Explain why a scientific model is changed",
    ],
    parts=[
        explain(
            "Two models and what changed them",
            "<table class='tbl'><tr><th></th><th>Geocentric (Ptolemy, ancient Greece)</th><th>Heliocentric (Copernicus 1543, Galileo, Kepler)</th></tr>"
            "<tr><td>Centre</td><td>the <b>Earth</b>, not moving</td><td>the <b>Sun</b></td></tr>"
            "<tr><td>What orbits what</td><td>the Sun, Moon, planets and stars all circle the Earth</td><td>the planets, including the Earth, orbit the Sun; the Moon orbits the Earth; the Earth spins once a day</td></tr>"
            "<tr><td>Orbits</td><td>circles, with extra circles (epicycles) added to fit the planets' wandering paths</td><td>first circles, then <b>ellipses</b> (Kepler) once accurate measurements showed circles did not fit</td></tr>"
            "<tr><td>Why believed</td><td>it matches what you see: the sky turns, the Earth feels still</td><td>it is simpler, and it <b>predicts observations</b> the geocentric model cannot</td></tr></table>"
            "<p><b>The observations that changed the model</b> — the point the spec wants (7.4P):</p>"
            "<ol><li>Planets sometimes appear to <b>move backwards</b> (retrograde motion). Geocentric models needed epicycles to fake this; in a heliocentric model it happens naturally when the faster-moving Earth overtakes an outer planet.</li>"
            "<li><b>Galileo's telescope (1609–10)</b> showed <b>four moons orbiting Jupiter</b> — bodies that plainly did <b>not</b> orbit the Earth, so not everything does.</li>"
            "<li>The telescope also showed <b>Venus has phases</b> like the Moon, including gibbous (nearly full) ones — impossible if Venus always lay between the Earth and the Sun, as the geocentric model had it, but expected if Venus goes <b>round the Sun</b>.</li>"
            "<li>Better measurements (Tycho Brahe, Kepler) showed planets move in <b>ellipses</b>, at speeds that change along the orbit; later Newton's gravity explained why.</li></ol>"
            "<p><b>The general lesson:</b> a model is accepted while it explains the observations; when new, better evidence (here from a new instrument) <b>cannot be explained</b> by the old model but <b>can</b> by a new one, the model changes. The same test decides between the Big Bang and Steady State (T4).</p>",
        ),
        worked(
            "The 3-mark 'explain how observations changed the model'",
            "Explain how the invention of the telescope led to the geocentric model being replaced by the heliocentric model. (3 marks)",
            [
                "The telescope let Galileo see <b>four moons orbiting Jupiter</b>…",
                "…which showed that <b>not everything orbits the Earth</b>, as the geocentric model claimed; he also saw Venus go through <b>phases</b>, which needs Venus to orbit the Sun.",
                "These observations <b>could not be explained</b> by the Earth-centred model but <b>were predicted</b> by the Sun-centred model, so the evidence supported the heliocentric model and it replaced the old one.",
            ],
        ),
        practice("Models of the Solar System", [
            written("as-t1-q1", "Describe the geocentric model of the Solar System. (2)",
                    marks(["The <b>Earth is at the centre</b> and does not move.", "The Sun, Moon, planets (and stars) all <b>orbit the Earth</b>."]), lines=2),
            written("as-t1-q2", "Describe the heliocentric model of the Solar System. (2)",
                    marks(["The <b>Sun is at the centre</b>.", "The planets, including the Earth, <b>orbit the Sun</b> (in ellipses); the Moon orbits the Earth."]), lines=2),
            choice("as-t1-q3", "Which observation showed that not everything orbits the Earth?",
                   ["The Sun rising in the east", "Moons seen orbiting Jupiter", "The Moon's phases", "The seasons"], 1,
                   "Galileo's four moons of Jupiter plainly circled Jupiter, not the Earth."),
            written("as-t1-q4", "Explain why the phases of Venus supported the heliocentric model. (2)",
                    marks(["Venus was seen to show a <b>full set of phases</b>, including nearly full…",
                           "…which is only possible if Venus <b>orbits the Sun</b> and is sometimes on the far side of it from the Earth — the geocentric model could not produce this."]), lines=3),
            written("as-t1-q5", "Explain why scientists replace one model with another. (2)",
                    marks(["New observations (often from new instruments) are made that the old model <b>cannot explain</b>…",
                           "…while the new model <b>explains or predicts</b> them, so it has more supporting evidence."]), lines=2),
            choice("as-t1-q6", "In the heliocentric model, the shape of a planet's orbit is…",
                   ["a perfect circle", "an ellipse (slightly flattened circle)", "a square", "a straight line"], 1,
                   "Kepler showed the orbits are ellipses; for the planets they are very close to circles."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T2 · Explaining orbits
# ---------------------------------------------------------------------

section_t2 = section(
    "orbit-explain", "tricky", "Explaining orbits: the words the marks are on", "7.5P, 7.6P, 7.7P",
    equations=[r"\text{velocity} \ne \text{speed}", r"\text{closer} \Rightarrow \text{stronger gravity} \Rightarrow \text{faster}"],
    blurb="Three questions come up again and again: why a satellite at steady speed is accelerating, why a closer orbit is faster, and why a comet speeds up and slows down. Each has a particular chain of words.",
    tags=["P"],
    checklist=[
        "Explain circular motion using 'velocity is a vector' and 'force towards the centre'",
        "Link orbital radius to orbital speed, both ways round",
        "Describe how a comet's speed changes around its orbit, and why",
    ],
    parts=[
        explain(
            "Three chains",
            diagram(dg.orbit_svg(), 600, 260, "Velocity along the orbit, gravity towards the centre, always at right angles.") +
            "<p><b>Chain 1 — constant speed but accelerating:</b> velocity is a <b>vector</b> → the <b>direction</b> of motion is <b>continuously changing</b> → so the <b>velocity is changing</b> → a changing velocity is an <b>acceleration</b> → it needs a <b>resultant force</b> → that force is <b>gravity</b>, acting <b>towards the centre</b>. Trap: \"it is accelerating because it is speeding up\" — it is not; and \"centripetal force\" on its own was ignored in June 2024 — name the force (gravity) and its direction.</p>"
            "<p><b>Chain 2 — radius and speed:</b> closer to the central body → <b>stronger gravitational force</b> → a tighter turn is needed → <b>higher speed</b> for a stable orbit. The spec's wording (7.7P): <i>if the speed of an orbiting body changes, the radius of its orbit must change too</i> — faster → smaller orbit; slower → larger orbit. Trap: students write \"closer orbits are slower because they have less distance to travel\". Less distance per orbit is why the <i>period</i> is shorter, but the <i>speed</i> is higher.</p>"
            "<p><b>Chain 3 — comets:</b> highly elliptical orbit → gravitational force from the Sun is <b>stronger when closer</b> → the comet <b>speeds up as it falls towards the Sun</b> (gravitational potential store → kinetic store) and <b>slows as it climbs away</b> → fastest at the closest point, slowest at the furthest. Trap: a comet's orbit is not a circle, so its speed is <b>not</b> constant, unlike a planet's.</p>"
            "<p><b>Geostationary explained:</b> there is only one height (about 36 000 km) at which the orbital period is exactly 24 hours; placed there above the equator, moving the same way the Earth turns, a satellite stays over one point. Lower → period shorter → it drifts ahead of the ground.</p>",
        ),
        worked(
            "Radius and speed, both ways",
            "Satellite A orbits the Earth at a height of 400 km; satellite B at 20 000 km. (a) State which satellite moves faster. (b) Explain your answer. (c) A third satellite, C, is in a stable orbit at a higher speed than A. State how the radius of C's orbit compares with A's. (4 marks)",
            [
                "<b>(a)</b> Satellite <b>A</b> (the lower one).",
                "<b>(b)</b> A is <b>closer</b> to the Earth, so the <b>gravitational force</b> on each kilogram is <b>stronger</b>; a stronger force bends the path more sharply, which needs a <b>higher speed</b> for a stable circular orbit.",
                "<b>(c)</b> C's orbit has a <b>smaller radius</b> than A's: a stable orbit at a higher speed needs the stronger gravity found closer in. (If a body's speed changes, the radius of its stable orbit must change too.)",
            ],
        ),
        practice("Explaining orbits", [
            written("as-t2-q1", "A satellite moves in a circular orbit at constant speed. Explain why there must be a resultant force on it, and state what provides the force. (3)",
                    mark_scheme([
                        ("Vector", "Velocity is a vector; the satellite's <b>direction is continuously changing</b>, so its <b>velocity is changing</b>."),
                        ("Acceleration", "A change in velocity is an <b>acceleration</b>, and an acceleration needs a <b>resultant force</b>."),
                        ("Force", "The force is <b>gravity</b>, acting <b>towards the centre</b> of the Earth."),
                    ]), lines=4),
            choice("as-t2-q2", "A student says: \"The Moon's velocity is constant because its speed is constant.\" Why is this wrong?",
                   ["Its speed is not constant", "Velocity includes direction, and the Moon's direction keeps changing", "The Moon does not move", "Velocity and speed are the same"], 1,
                   "Steady speed round a circle is a changing velocity."),
            written("as-t2-q3", "Explain why a planet closer to the Sun must move faster than one further away to stay in a stable orbit. (2)",
                    marks(["Closer to the Sun the <b>gravitational force</b> is <b>stronger</b>.",
                           "A stronger force makes the path curve more tightly, so a <b>higher speed</b> is needed to keep a stable (circular) orbit of that smaller radius."]), lines=3),
            written("as-t2-q4", "A comet's orbit is highly elliptical. Describe how its speed changes during one orbit and explain why. (3)",
                    mark_scheme([
                        ("Pattern", "It is <b>fastest when nearest the Sun</b> and slowest when furthest away."),
                        ("Falling in", "As it approaches the Sun the <b>gravitational force increases</b> and does work on it: energy is transferred from the <b>gravitational potential store to the kinetic store</b>."),
                        ("Climbing out", "Moving away, gravity slows it: kinetic → gravitational potential."),
                    ]), lines=4),
            choice("as-t2-q5", "A satellite is moved from a high orbit to a lower one. Its speed…",
                   ["decreases", "increases", "stays the same", "becomes zero"], 1,
                   "Smaller radius → stronger gravity → faster."),
            written("as-t2-q6", "Explain why a geostationary satellite must be placed at one particular height. (2)",
                    marks(["Its <b>period must be 24 hours</b> to match the Earth's rotation, so that it stays above the same point.",
                           "The orbital speed (and so the period) depends on the <b>radius</b>, so only one height gives a 24-hour period (lower → faster → shorter period)."]), lines=3),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T3 · The red-shift argument
# ---------------------------------------------------------------------

section_t3 = section(
    "redshift-argument", "tricky", "The red-shift argument, step by step", "7.11P, 7.12P, 7.13P",
    equations=[r"\text{longer } \lambda \Rightarrow \text{moving away} \Rightarrow \text{further} = \text{faster} \Rightarrow \text{expanding}"],
    blurb="Red-shift questions give you two spectra, or a table of galaxies, and ask what they show. The marks are on a fixed chain: longer wavelength → moving away → more distant means faster → expanding. Miss a link and the mark goes.",
    tags=["P"],
    checklist=[
        "Compare two spectra and say which galaxy is further away and why",
        "Write the full chain from observation to 'the Universe is expanding'",
        "Explain why red-shift alone does not decide between Big Bang and Steady State",
    ],
    parts=[
        explain(
            "The chain, and the exam traps",
            "<p>The June 2022 Paper 1H question (Q6) gave the spectra of two galaxies and asked students to explain how they showed the Universe is expanding. The scheme:</p>"
            "<table class='tbl'><tr><th>Mark</th><th>What to write</th></tr>"
            "<tr><td>1</td><td>The lines in the <b>more distant</b> galaxy's spectrum are at <b>longer wavelengths</b> — it has the <b>greater red-shift</b>.</td></tr>"
            "<tr><td>2</td><td>Greater red-shift means it is <b>moving away faster</b>; so <b>more distant galaxies move away faster</b>, which is what an <b>expanding</b> Universe looks like.</td></tr></table>"
            "<p>Spell out each arrow. Common losses: saying \"the galaxy is red-shifted\" without saying what that shows; saying \"moving away\" without the distance–speed link; saying \"expanding\" with no evidence. Writing \"the light gets redder\" is not the same as \"the wavelength is longer\".</p>"
            "<p><b>Why expansion:</b> if <b>every</b> galaxy is moving away from us, and the further ones faster, either we are at the centre of a huge explosion (we are not — every galaxy sees the same thing) or <b>space itself is stretching</b>, carrying all the galaxies apart. Dots on a balloon being inflated: every dot sees every other move away, the more distant ones faster.</p>"
            "<p><b>Why red-shift does not settle the argument:</b> both the Big Bang and the Steady State theory describe an <b>expanding</b> Universe, so both predict red-shift. Red-shift is evidence <b>for expansion</b>, not for the Big Bang alone. What decided it was the CMB (T4).</p>"
            "<p><b>The calculations</b> (if a question supplies the equations): $z = \\dfrac{\\Delta\\lambda}{\\lambda}$, and recession velocity $v = z \\times c$ with $c = 3 \\times 10^8$ m/s. The 2022 report: candidates mixed standard form with ordinary numbers (656 nm with 6.56 × 10⁻⁷ m) and lost the arithmetic; keep every wavelength in the same form, and use the \"show that\" value in the next part if there is one.</p>",
        ),
        worked(
            "Two spectra",
            "The spectrum of light from galaxy X shows a hydrogen line at 660 nm; from galaxy Y the same line is at 700 nm. In the laboratory the line is at 656 nm. Explain which galaxy is further from Earth and how these observations support the idea of an expanding Universe. (4 marks)",
            [
                "<b>Both</b> lines are at <b>longer wavelengths</b> than 656 nm, so both galaxies are <b>red-shifted</b> and <b>moving away</b> from us.",
                "Y's line is shifted <b>more</b> (44 nm against 4 nm), so Y has the <b>greater red-shift</b> and is moving away <b>faster</b>.",
                "The <b>more distant</b> a galaxy, the <b>greater</b> its red-shift — so <b>Y is further away</b>.",
                "More distant galaxies receding faster is what is seen when <b>space itself is expanding</b>, carrying the galaxies apart.",
            ],
        ),
        practice("The red-shift argument", [
            group("as-t3-q1", "A spectral line is at 486 nm in the laboratory. In the light from galaxy P it is at 490 nm; from galaxy Q it is at 510 nm.", [
                written("as-t3-q1a", "State which galaxy is further from Earth. (1)", marks(["<b>Q</b>."]), lines=1),
                written("as-t3-q1b", "Explain your answer. (2)",
                        marks(["Q's line has the <b>longer wavelength</b> / <b>bigger red-shift</b> (24 nm against 4 nm), so Q is moving away faster…",
                               "…and <b>more distant galaxies have the bigger red-shift</b> (move away faster)."]), lines=3),
                numeric("as-t3-q1c", "The red-shift z = (change in wavelength) ÷ (original wavelength). Calculate z for galaxy Q.", 0.049, "",
                        "Δλ = 510 − 486 nm.", [r"$z = \dfrac{510 - 486}{486} = \dfrac{24}{486} = 0.049$ (2 s.f.)."]),
            ]),
            written("as-t3-q2", "Explain how the red-shift of light from distant galaxies provides evidence that the Universe is expanding. (3)",
                    mark_scheme([
                        ("Observation", "The light from distant galaxies is <b>red-shifted</b>: its wavelength is <b>longer</b> than from the same source on Earth."),
                        ("Meaning", "So the galaxies are <b>moving away</b> from us."),
                        ("Pattern", "The <b>more distant</b> the galaxy the <b>greater</b> the red-shift, so the faster it recedes — every galaxy moving apart from every other is an <b>expanding</b> Universe."),
                    ]), lines=4),
            choice("as-t3-q3", "Why does red-shift NOT prove the Big Bang theory on its own?",
                   ["It is not real", "The Steady State theory also describes an expanding Universe and so also predicts red-shift", "Only nearby galaxies show it", "It only applies to stars"], 1,
                   "Red-shift is evidence for expansion, which both theories include."),
            numeric("as-t3-q4", "A galaxy has a red-shift z = 0.02. Its recession velocity is given by v = z × c, where c = 3 × 10⁸ m/s. Calculate v.", 6000000, "m/s",
                    "Multiply; 0.02 × 3 × 10⁸.", [r"$v = 0.02 \times 3 \times 10^8 = 6 \times 10^6$ m/s (6000 km/s)."]),
            written("as-t3-q5", "A student writes: \"Red-shift means the galaxies are moving away from the Earth, so the Earth is at the centre of the Universe.\" Explain why the conclusion is wrong. (2)",
                    marks(["If <b>space itself is expanding</b>, every galaxy moves away from every other — an observer in <b>any</b> galaxy sees the same red-shift pattern.",
                           "So the observation does not put the Earth at a centre; there is no centre (the balloon analogy)."]), lines=3),
            choice("as-t3-q6", "The light from a distant galaxy shows a hydrogen line at a longer wavelength than in the laboratory. What is the correct phrase for the mark?",
                   ["\"The light has turned red\"", "\"The wavelength has increased — the light is red-shifted — so the galaxy is moving away\"", "\"The galaxy is red\"", "\"The frequency has increased\""], 1,
                   "Name the change in wavelength and what it shows."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T4 · Why the CMB decided it
# ---------------------------------------------------------------------

section_t4 = section(
    "cmb-decides", "tricky", "Why the CMB decided between the two theories", "7.9P, 7.10P, 7.14P, 7.15P",
    equations=[r"\text{predicted} + \text{observed} + \text{rival cannot explain} \Rightarrow \text{accepted}"],
    blurb="The 6-mark Big Bang question is lost by students who list facts without linking them. The structure is: what each theory says, what was predicted, what was found, which theory is left standing.",
    tags=["P"],
    checklist=[
        "Describe what the CMB is and where it comes from in the Big Bang picture",
        "Explain why the CMB supports the Big Bang but not the Steady State theory",
        "Describe how a theory becomes the accepted one",
    ],
    parts=[
        explain(
            "The argument, in the order the marks want it",
            "<ol><li><b>Two theories, both with expansion.</b> Big Bang: the Universe began from a tiny, hot, dense point and has expanded and cooled since. Steady State: it has always existed, expanding, with new matter continually created to fill the gaps, so it looks the same for ever.</li>"
            "<li><b>Red-shift fits both.</b> Both say space is expanding, so both predict galaxies receding, faster when further. Red-shift cannot choose between them.</li>"
            "<li><b>The Big Bang made a prediction.</b> If the early Universe was hot and dense, it was full of high-energy radiation. As space expanded, that radiation was <b>stretched to longer wavelengths</b> (red-shifted enormously) — it should now be faint <b>microwaves</b>, coming equally from <b>every direction</b>, with a temperature a few degrees above absolute zero.</li>"
            "<li><b>The prediction was found.</b> In 1964 Penzias and Wilson detected microwave radiation from all directions in the sky — the <b>cosmic microwave background</b> — at about 2.7 K, just as predicted.</li>"
            "<li><b>Steady State had no explanation.</b> A Universe that has always looked the same has no hot early phase to leave radiation behind. The theory could not account for the CMB.</li>"
            "<li><b>So the Big Bang became the accepted model</b> (7.10P): it is the theory with <b>more supporting evidence</b> — both red-shift and the CMB — and it made a <b>prediction that was confirmed</b>. That is how a scientific model is judged.</li></ol>"
            "<p>The June 2025 levels (Q10(c), 6 marks): <b>Level 3</b> — at least one piece of evidence <b>described and linked</b> to the aspect of the theory it supports (the CMB \"across the sky\" → a hot early Universe, a definite beginning; red-shift → expansion), with the other identified; <b>Level 1</b> — isolated statements (\"there is red-shift\", \"there is CMB\"). The report: students knew the names of the evidence but did not say <i>what each showed</i>.</p>"
            "<p>Word traps: the CMB is <b>microwave</b> radiation, not light and not \"radio waves from the Big Bang\"; it comes from <b>all directions</b>, not from one place; and the Big Bang was not an explosion <i>in</i> space — it was the start of the expansion <i>of</i> space.</p>",
        ),
        worked(
            "Comparing the theories (6 marks)",
            "Scientists once supported two theories of the Universe, the Big Bang and the Steady State. Explain how evidence led to the Big Bang theory becoming the accepted theory. (6 marks)",
            [
                "<b>Both theories</b> say the Universe is <b>expanding</b>; the Big Bang says it began from a tiny, hot, dense point, the Steady State says it has always existed with new matter continually created.",
                "<b>Red-shift</b>: light from distant galaxies has longer wavelengths, more so the more distant the galaxy, showing galaxies are moving apart — the Universe is expanding. This <b>supports both</b> theories.",
                "The Big Bang theory <b>predicted</b> that radiation left over from the hot early Universe should still be detectable, stretched by the expansion to <b>microwave</b> wavelengths and coming from <b>all directions</b>.",
                "The <b>cosmic microwave background</b> was then <b>discovered</b>, matching that prediction — evidence for a hot, dense beginning.",
                "The Steady State theory <b>could not explain</b> the CMB, because it has no hot early Universe.",
                "So the Big Bang theory has <b>more supporting evidence</b> (red-shift and the CMB) and a confirmed prediction, and it became the accepted model.",
            ],
        ),
        practice("Why the CMB decided it", [
            written("as-t4-q1", "Describe what the cosmic microwave background radiation is. (2)",
                    marks(["<b>Microwave</b> radiation detected coming from <b>all directions</b> in space (at the same temperature, about 2.7 K).",
                           "It is the radiation <b>left over from the hot early Universe</b>, stretched to microwave wavelengths by the expansion."]), lines=2),
            written("as-t4-q2", "Explain why the CMB supports the Big Bang theory. (3)",
                    mark_scheme([
                        ("Prediction", "The Big Bang theory says the early Universe was <b>hot and dense</b> and full of radiation."),
                        ("Stretching", "As the Universe <b>expanded</b>, that radiation was stretched to <b>longer (microwave) wavelengths</b> and should be seen coming from everywhere."),
                        ("Match", "Microwave radiation <b>is</b> detected from all directions, as <b>predicted</b> — so it is evidence for a hot beginning."),
                    ]), lines=4),
            written("as-t4-q3", "Explain why the discovery of the CMB led scientists to reject the Steady State theory. (2)",
                    marks(["The Steady State theory says the Universe has <b>always existed</b> and looked the same, with <b>no hot early phase</b>…",
                           "…so it <b>cannot explain</b> where the CMB comes from, while the Big Bang theory predicted it."]), lines=3),
            choice("as-t4-q4", "Which statement about the Big Bang is correct?",
                   ["It was an explosion of matter into empty space", "It was the start of the expansion of space itself, from a tiny, hot, dense state", "It happened at the centre of the Universe", "It created the Steady State"], 1,
                   "Space itself expanded; there is no centre."),
            written("as-t4-q5", "A theory makes a prediction that is later observed. Explain why this makes scientists more confident in the theory. (2)",
                    marks(["The observation was <b>not known</b> when the theory was made, so the theory was not simply built to fit it.",
                           "The theory <b>explains</b> something a rival theory cannot — it has <b>more supporting evidence</b>, so it becomes the accepted model."]), lines=3),
            choice("as-t4-q6", "A student's 6-mark answer says: \"There is red-shift. There is CMB. So the Big Bang is right.\" Which level would this reach?",
                   ["Level 3 — full marks", "Level 1 — isolated statements with no links", "Level 2", "It would score zero"], 1,
                   "Each piece of evidence must be described and linked to what it shows."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T5 · How a star stays stable (and stops)
# ---------------------------------------------------------------------

section_t5 = section(
    "star-balance", "tricky", "How a star forms, stays stable, and stops", "7.16P, 7.17P",
    equations=[r"\text{gravity (in)} = \text{pressure from fusion (out)}"],
    blurb="The questions are 'explain how a star forms', 'explain why a main sequence star is stable' and 'explain what happens when the fuel runs out'. All three are the same two forces: gravity pulling in, the pressure of hot gas pushing out.",
    tags=["P"],
    checklist=[
        "Explain how gravity forms a protostar and starts fusion",
        "Explain the balance that keeps a main sequence star stable",
        "Explain what changes when the hydrogen runs out, for both masses of star",
    ],
    parts=[
        explain(
            "Gravity versus pressure",
            "<table class='tbl'><tr><th>Stage</th><th>Gravity</th><th>Outward pressure</th><th>Result</th></tr>"
            "<tr><td>Nebula → protostar</td><td>pulls the gas and dust together</td><td>small</td><td>the cloud <b>collapses</b>; compressing it makes it <b>denser and hotter</b> (gravitational potential → thermal)</td></tr>"
            "<tr><td>Fusion starts</td><td>still pulling in</td><td>core hot enough (millions of °C) for <b>hydrogen nuclei to fuse into helium</b>, releasing energy</td><td>the energy heats the gas, whose <b>pressure pushes outwards</b></td></tr>"
            "<tr><td>Main sequence</td><td>inward</td><td>outward, from the hot gas</td><td><b>balanced</b> — the star is <b>stable</b> and the same size for billions of years</td></tr>"
            "<tr><td>Hydrogen runs out</td><td>wins in the core</td><td>falls</td><td>the <b>core contracts and heats</b> until <b>helium</b> fuses; the extra energy pushes the <b>outer layers out</b> — a <b>red giant</b> (or supergiant)</td></tr>"
            "<tr><td>Fuel gone (Sun-like)</td><td>wins</td><td>none — no fusion</td><td>the core shrinks to a <b>white dwarf</b>, which slowly cools</td></tr>"
            "<tr><td>Fuel gone (massive)</td><td>wins suddenly</td><td>none</td><td>the core collapses in seconds — <b>supernova</b>; the remnant is a <b>neutron star</b> or, if gravity is strong enough to beat everything, a <b>black hole</b></td></tr></table>"
            "<p>The June 2023 scheme (Q4(d), explaining how a protostar becomes a main sequence star): <b>gravity</b> causes the cloud to <b>collapse</b>; the collapse <b>raises the temperature</b> until <b>fusion</b> starts; the star is stable because <b>gravity and the outward pressure from fusion balance</b>. \"Fission\" instead of fusion scored nothing — fusion <i>joins</i> small nuclei, fission <i>splits</i> large ones. Say <b>nuclei</b> (hydrogen nuclei fuse), not \"atoms\" or \"particles\".</p>",
        ),
        worked(
            "The 3-mark stability explanation",
            "Explain how a protostar becomes a main sequence star, and why a main sequence star remains the same size for billions of years. (3 marks)",
            [
                "<b>Gravity</b> pulls the gas and dust of the protostar inwards, <b>compressing</b> it and making the core <b>hotter and denser</b>.",
                "When the core is hot enough, <b>hydrogen nuclei fuse</b> to form helium, <b>releasing energy</b> — the star is now a main sequence star.",
                "It stays the same size because the <b>outward pressure</b> of the hot gas, kept up by fusion, <b>balances the inward force of gravity</b>.",
            ],
        ),
        practice("How a star stays stable", [
            written("as-t5-q1", "Explain how a nebula becomes a protostar. (2)",
                    marks(["<b>Gravity</b> pulls the particles of gas and dust together, so the cloud <b>collapses</b> and becomes denser.",
                           "Compressing the gas transfers energy to its thermal store: it gets <b>hotter</b> (but fusion has not yet started)."]), lines=2),
            written("as-t5-q2", "Explain why a main sequence star is stable. (2)",
                    marks(["<b>Fusion</b> of hydrogen into helium releases energy, so the hot gas exerts an <b>outward pressure</b>.",
                           "This outward pressure <b>balances the inward pull of gravity</b>, so the star neither expands nor collapses."]), lines=2),
            choice("as-t5-q3", "What process releases the energy in a main sequence star?",
                   ["Nuclear fission of uranium", "Nuclear fusion of hydrogen nuclei into helium", "Burning hydrogen gas", "Gravity alone"], 1,
                   "Fusion: small nuclei join. Fission is splitting, and it is not what powers stars."),
            written("as-t5-q4", "Explain what happens to a star like the Sun when the hydrogen in its core runs out. (3)",
                    mark_scheme([
                        ("Balance lost", "Fusion in the core slows, so the outward pressure falls and <b>gravity wins</b>: the <b>core contracts</b> and gets hotter."),
                        ("New fusion", "The core becomes hot enough for <b>helium</b> to fuse into heavier elements."),
                        ("Expansion", "The extra energy pushes the <b>outer layers outwards</b>; they expand and cool — the star becomes a <b>red giant</b>."),
                    ]), lines=4),
            written("as-t5-q5", "Explain why a star much more massive than the Sun ends in a supernova while the Sun will not. (2)",
                    marks(["A more massive star has <b>much stronger gravity</b>, so when fusion stops its core <b>collapses</b> suddenly and violently…",
                           "…and the collapse blows the outer layers away in a <b>supernova</b>; the Sun's gravity is too weak for this, so its core just shrinks to a white dwarf."]), lines=3),
            choice("as-t5-q6", "A student writes: \"The star is stable because gravity is balanced by nuclear fission.\" What is wrong?",
                   ["Nothing", "Stars are powered by fusion, not fission", "Gravity is not involved", "Stars are never stable"], 1,
                   "Fusion joins hydrogen nuclei; fission splits heavy nuclei and does not happen in stars."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T6 · Space telescopes: for and against
# ---------------------------------------------------------------------

section_t6 = section(
    "space-telescopes", "tricky", "Telescopes in space and telescopes for other wavelengths", "7.19P",
    equations=[r"\text{above the atmosphere: no absorption, no distortion}"],
    blurb="'State and explain' questions on telescopes are marked on the reason, not the location. 'It is in space' earns nothing; 'it is above the atmosphere, which absorbs infrared' earns the marks.",
    tags=["P"],
    checklist=[
        "Give the advantages of a telescope above the atmosphere, each with its reason",
        "Give the disadvantages of a space telescope",
        "Explain why telescopes for radio, infrared, X-ray and other wavelengths are used",
    ],
    parts=[
        explain(
            "The arguments and their reasons",
            "<table class='tbl'><tr><th>Advantage of a space telescope</th><th>Because…</th></tr>"
            "<tr><td>can observe <b>infrared, ultraviolet, X-rays, gamma rays</b></td><td>the <b>atmosphere absorbs</b> most of these, so they never reach the ground</td></tr>"
            "<tr><td><b>sharper</b> images</td><td>no <b>distortion</b> (twinkling) from moving air of varying density refracting the light</td></tr>"
            "<tr><td>sees <b>fainter</b> objects</td><td>no <b>light pollution</b> from towns, no scattered daylight, no clouds or dust — observations possible all the time</td></tr></table>"
            "<table class='tbl'><tr><th>Disadvantage</th><th>Because…</th></tr>"
            "<tr><td>very <b>expensive</b></td><td>launching a telescope into orbit costs far more than building one on a mountain</td></tr>"
            "<tr><td>hard to <b>repair or upgrade</b></td><td>astronauts or robots have to reach it (Hubble was serviced; Webb, 1.5 million km away, cannot be)</td></tr>"
            "<tr><td><b>size</b> limited</td><td>it must fit in a rocket, so the mirror is smaller than the biggest ground telescopes (Webb's unfolds)</td></tr></table>"
            "<p>The 2022 report (Q6(c)): the question asked why some telescopes are on satellites; many \"stated the location without explaining why it matters\". Write <b>where</b> (above the atmosphere) <b>and the consequence</b> (no absorption / distortion / pollution).</p>"
            "<p><b>Other wavelengths</b> (and why bother): objects emit at wavelengths set by their temperature and processes — <b>cool dust and gas</b> clouds where stars form glow in <b>infrared</b>; very <b>hot</b> gas round black holes and in supernova remnants gives <b>X-rays</b>; <b>radio</b> telescopes see through dust and detect the CMB (microwaves) and pulsars; radio and some infrared pass through the atmosphere, so those telescopes can be on the ground (radio dishes are huge for that reason). Each wavelength reveals something the others cannot, so a complete picture needs them all.</p>",
        ),
        worked(
            "State and explain",
            "The James Webb Space Telescope observes infrared radiation from an orbit far from the Earth. (a) Explain why it had to be placed in space. (b) Give two disadvantages of placing a telescope in space. (4 marks)",
            [
                "<b>(a)</b> The Earth's <b>atmosphere absorbs</b> most infrared radiation, so a ground telescope would receive very little…",
                "…above the atmosphere all the infrared reaches the telescope, undistorted by the air and unaffected by clouds and light pollution.",
                "<b>(b)</b> It is very <b>expensive</b> to build and launch…",
                "…and it <b>cannot be repaired or upgraded</b> if something goes wrong (and its size is limited by the rocket).",
            ],
        ),
        practice("Space telescopes", [
            written("as-t6-q1", "Explain one advantage of placing an optical telescope in orbit around the Earth. (2)",
                    marks(["It is <b>above the atmosphere</b>…", "…so the light is not <b>distorted</b> by moving air (or dimmed by clouds / light pollution), giving sharper, clearer images."]), lines=2),
            written("as-t6-q2", "Explain why an X-ray telescope cannot be used on the ground. (2)",
                    marks(["X-rays from space are <b>absorbed by the atmosphere</b>…", "…so they do <b>not reach the ground</b> — the telescope must be above the atmosphere to detect them."]), lines=2),
            choice("as-t6-q3", "Which type of telescope works well on the ground because its waves pass through the atmosphere?",
                   ["X-ray", "Gamma ray", "Radio", "Ultraviolet"], 2,
                   "Radio waves (and visible light) pass through the atmosphere; most IR, UV, X and gamma do not."),
            written("as-t6-q4", "Give two disadvantages of space telescopes compared with ground-based telescopes. (2)",
                    marks(["Much more <b>expensive</b> (launch costs).", "<b>Difficult or impossible to repair</b>, maintain or upgrade; size limited by the rocket."]), lines=2),
            written("as-t6-q5", "Explain why astronomers use telescopes that detect infrared as well as telescopes that detect visible light. (2)",
                    marks(["Some objects — <b>cool</b> clouds of dust and gas where stars form — emit mostly <b>infrared</b> and little visible light, and infrared passes through dust that blocks light.",
                           "So the infrared telescope reveals objects and detail that a visible-light telescope <b>cannot see</b>."]), lines=3),
            choice("as-t6-q6", "A student answers \"telescopes are put on satellites because they are in space\". Why does this score nothing?",
                   ["Telescopes are never on satellites", "It gives the location but not the reason — the atmosphere's absorption or distortion must be mentioned", "Satellites cannot carry telescopes", "The answer is too long"], 1,
                   "The 2022 report's exact complaint."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T7 · Weight and g the hard way
# ---------------------------------------------------------------------

section_t7 = section(
    "weight-hard", "tricky", "Weight and g the hard way: ratios, rearranging and the balance trap", "7.1P",
    equations=[r"g = \dfrac{W}{m}", r"m = \dfrac{W}{g}", r"\dfrac{W_{\text{Moon}}}{W_{\text{Earth}}} = \dfrac{g_{\text{Moon}}}{g_{\text{Earth}}}"],
    blurb="The easy question gives m and g. The harder ones give a weight on one body and ask about another, give g as a fraction of Earth's, or ask what two different balances would read. The mass is the fixed point in all of them.",
    tags=["P"],
    checklist=[
        "Find g from a weight and a mass, and a mass from a weight and g",
        "Convert a weight on one body to the weight on another via the mass",
        "Use ratios: g a fraction of Earth's, so weight the same fraction",
        "Explain what a beam balance and a newton meter would read on the Moon",
    ],
    parts=[
        explain(
            "Three routes and a trap",
            "<p><b>Route 1 — via the mass.</b> Weight on Earth → mass ($m = W \\div 10$) → weight elsewhere ($W = m \\times g$). The mass is the bridge: it never changes.</p>"
            "<p><b>Route 2 — ratios.</b> Weight is proportional to $g$ for a fixed mass, so if $g_{\\text{Moon}}$ is 1/6 of Earth's, every weight on the Moon is 1/6 of its Earth value: 600 N → 100 N, no mass needed. \"g on Mars is 0.38 times g on Earth\" → multiply Earth weights by 0.38.</p>"
            "<p><b>Route 3 — finding g.</b> Drop or weigh a known mass: $g = W \\div m$. From a newton meter reading of 7.4 N for a 2 kg mass on Mars, $g = 3.7$ N/kg. Unit <b>N/kg</b> (the same as m/s², the acceleration of free fall there).</p>"
            "<p><b>The balance trap.</b> A <b>newton meter / spring balance</b> measures the <b>force</b> pulling the spring — the weight — so it reads <b>less on the Moon</b>. A <b>beam balance</b> (scales with standard masses on the other side) compares the pull of gravity on two masses <b>at the same place</b>; both are reduced by the same factor, so it balances at the <b>same mass</b> as on Earth. Bathroom scales are spring balances marked in kg assuming Earth's $g$: on the Moon they would read a sixth of your mass — wrongly.</p>"
            "<p><b>Why g differs</b> (the explain mark): $g$ at a surface depends on the body's <b>mass</b> and its <b>radius</b>; a more massive body pulls harder, a larger radius puts the surface further from the centre and weakens the pull. In orbit $g$ is smaller but not zero — astronauts float because they and their spacecraft are <b>falling together</b>, not because there is no gravity.</p>",
        ),
        worked(
            "Via the mass, then ratios",
            "An astronaut weighs 720 N on Earth (g = 10 N/kg). (a) Calculate his weight on the Moon (g = 1.6 N/kg). (b) On Mars g is 0.38 times its value on Earth. Calculate his weight on Mars without finding his mass again.",
            [
                r"<b>(a)</b> Mass: $m = \dfrac{W}{g} = \dfrac{720}{10} = 72$ kg.",
                r"On the Moon: $W = m \times g = 72 \times 1.6 = 115$ N (3 s.f.).",
                r"<b>(b)</b> Weight is proportional to $g$ for the same mass: $W_{\text{Mars}} = 0.38 \times 720 = 274$ N (3 s.f.).",
            ],
        ),
        practice("Weight the hard way", [
            numeric("as-t7-q1", "A rock weighs 24 N on the Moon (g = 1.6 N/kg). Calculate its weight on Earth (g = 10 N/kg).", 150, "N", "Mass first.",
                    [r"$m = \dfrac{24}{1.6} = 15$ kg.", r"On Earth $W = 15 \times 10 = 150$ N."]),
            numeric("as-t7-q2", "A newton meter reads 11.1 N when a 3 kg mass hangs from it on Mars. Calculate g on Mars.", 3.7, "N/kg", "g = W ÷ m.",
                    [r"$g = \dfrac{W}{m} = \dfrac{11.1}{3} = 3.7$ N/kg."]),
            numeric("as-t7-q3", "On Jupiter g is 2.5 times its value on Earth. A probe weighs 400 N on Earth. Calculate its weight on Jupiter.", 1000, "N", "Weight scales with g.",
                    [r"$W_{\text{Jupiter}} = 2.5 \times 400 = 1000$ N (or: m = 40 kg, W = 40 × 25 = 1000 N)."]),
            group("as-t7-q4", "An astronaut takes a 1 kg mass, a beam balance with standard masses, and a newton meter to the Moon (g = 1.6 N/kg).", [
                numeric("as-t7-q4a", "Calculate the newton meter reading when the 1 kg mass hangs from it on the Moon.", 1.6, "N", "W = m × g.",
                        [r"$W = 1 \times 1.6 = 1.6$ N (it read 10 N on Earth)."]),
                written("as-t7-q4b", "Explain what the beam balance shows when the 1 kg mass is placed on one side and a 1 kg standard mass on the other. (2)",
                        marks(["It <b>balances</b> — it still shows 1 kg.",
                               "Both masses are pulled by the <b>same (reduced) g</b>, so their weights are reduced equally and the balance compares <b>masses</b>, which have not changed."]), lines=3),
            ]),
            numeric("as-t7-q5", "A planet has g = 15 N/kg. A person weighs 900 N there. Calculate the person's mass.", 60, "kg", "m = W ÷ g.",
                    [r"$m = \dfrac{900}{15} = 60$ kg — the same mass anywhere."]),
            written("as-t7-q6", "Explain why astronauts in the International Space Station appear weightless even though g there is about 8.7 N/kg. (2)",
                    marks(["Gravity still acts on them (their weight is about 87% of its value on the ground) — that is what keeps the station in orbit.",
                           "They float because they and the station are <b>falling (accelerating) towards the Earth together</b>, so nothing pushes up on them — there is no reaction force to feel."]), lines=3),
        ]),
    ],
)

SECTIONS = [section_t1, section_t2, section_t3, section_t4, section_t5, section_t6, section_t7]

# ---------------------------------------------------------------------
# Flashcards (the key-word definitions are added by as_nn.FACTS_KW)
# ---------------------------------------------------------------------

FACTS = [
    # Solar System
    fact("What does the Solar System consist of?", "The Sun, eight planets with their natural satellites (moons), dwarf planets, asteroids and comets (plus artificial satellites).", "solar-system"),
    fact("Name the eight planets in order from the Sun.", "Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune.", "solar-system"),
    fact("What is a dwarf planet? Give an example.", "A body that orbits the Sun and is round but has not cleared its orbit of other objects — Pluto, Ceres, Eris.", "solar-system"),
    fact("Where is the asteroid belt?", "Between Mars and Jupiter.", "solar-system"),
    fact("Which four planets are small and rocky, and which four are gas giants?", "Rocky: Mercury, Venus, Earth, Mars. Gas giants: Jupiter, Saturn, Uranus, Neptune.", "solar-system"),
    # Weight
    fact("What is the equation for weight?", "W = m × g (weight = mass × gravitational field strength).", "weight-elsewhere-nn"),
    fact("Does your mass change on the Moon? Does your weight?", "Mass: no, it is the same everywhere. Weight: yes, it is about a sixth, because g on the Moon is about 1.6 N/kg.", "weight-elsewhere-nn"),
    fact("What does g at the surface of a body depend on?", "The body's mass (more mass → larger g) and its radius (larger radius → smaller g).", "weight-elsewhere-nn"),
    fact("g on the Earth, Moon, Mars and Jupiter?", "Earth 10 N/kg; Moon 1.6 N/kg; Mars 3.7 N/kg; Jupiter 25 N/kg.", "weight-elsewhere-nn"),
    fact("Which reads differently on the Moon: a newton meter or a beam balance?", "The newton meter (it measures weight). The beam balance compares masses and reads the same.", "weight-elsewhere-nn"),
    # Orbits
    fact("Describe the orbits of the planets.", "Near-circular (slightly elliptical) orbits around the Sun, roughly in one plane, at almost constant speed.", "orbits"),
    fact("Describe the orbit of a comet.", "Highly elliptical around the Sun; fastest when closest to the Sun, slowest when furthest.", "orbits"),
    fact("What does a moon (natural satellite) orbit?", "A planet.", "orbits"),
    fact("What is a geostationary orbit, and what is it used for?", "An orbit above the equator with a 24-hour period, so the satellite stays over one point — TV and communications.", "orbits"),
    fact("What is a low polar orbit used for, and why?", "Weather, imaging and mapping: the satellite passes over the poles every ~90 min while the Earth turns beneath it, so it covers the whole surface.", "orbits"),
    fact("Why does a comet speed up near the Sun?", "The Sun's gravitational force increases as it gets closer; energy is transferred from the gravitational potential store to the kinetic store.", "orbits"),
    fact("What force keeps a satellite in orbit?", "Gravity (the Earth's gravitational pull), acting towards the centre of the Earth.", "orbits"),
    # Circular orbits
    fact("A planet in a circular orbit has constant speed. Is its velocity constant?", "No — its direction is continuously changing, so its velocity is changing (velocity is a vector).", "circular-orbits"),
    fact("Why is a body in a circular orbit accelerating?", "Its velocity is changing (direction changes continuously); the acceleration is towards the centre, caused by gravity.", "circular-orbits"),
    fact("In which direction does gravity act on an orbiting body, relative to its velocity?", "Towards the centre — at right angles to the velocity — so it changes the direction but not the speed.", "circular-orbits"),
    fact("How are orbital radius and orbital speed linked for a stable orbit?", "Smaller radius → stronger gravity → higher speed needed. So if an orbiting body's speed changes, its orbital radius must change too (spec 7.7P).", "circular-orbits"),
    fact("Why does Mercury orbit faster than Neptune?", "It is much closer to the Sun, so the gravitational force on it is stronger and a higher speed is needed for a stable orbit.", "circular-orbits"),
    # Red-shift
    fact("A wave source moves away from you. What happens to the observed wavelength and frequency?", "Wavelength increases; frequency decreases.", "redshift"),
    fact("A wave source moves towards you. What happens to the observed wavelength and frequency?", "Wavelength decreases; frequency increases (blue-shift for light).", "redshift"),
    fact("What is red-shift?", "The increase in wavelength of light from a source moving away — spectral lines shifted towards the red end.", "redshift"),
    fact("How does a galaxy's red-shift depend on its distance?", "The more distant the galaxy, the greater its red-shift — so the faster it is moving away.", "redshift"),
    fact("What does the red-shift of galaxies tell us about them?", "They are moving away from us; more distant ones faster.", "redshift"),
    # Big Bang
    fact("Describe the Big Bang theory.", "The Universe began about 13.8 billion years ago from a very small, hot, dense point and has been expanding and cooling ever since.", "big-bang"),
    fact("Describe the Steady State theory.", "The Universe has always existed and always will; it expands, but new matter is continually created so it always looks the same.", "big-bang"),
    fact("What two pieces of evidence support the Big Bang?", "Red-shift of galaxies (expansion) and the cosmic microwave background (a hot beginning).", "big-bang"),
    fact("Which evidence fits both theories, and which fits only the Big Bang?", "Red-shift fits both (both have expansion); the CMB fits only the Big Bang.", "big-bang"),
    fact("What is the CMB?", "Cosmic microwave background: microwave radiation from all directions in space, left over from the hot early Universe and stretched by the expansion.", "big-bang"),
    fact("Why did the Big Bang become the accepted theory?", "It predicted the CMB, which was then discovered; the Steady State theory could not explain it — so the Big Bang has more supporting evidence.", "big-bang"),
    fact("How does red-shift show the Universe is expanding?", "All distant galaxies are moving away, and the further they are the faster — exactly what is seen if space itself is expanding everywhere.", "big-bang"),
    # Stars
    fact("Life cycle of a star like the Sun?", "Nebula → protostar → main sequence star → red giant → white dwarf → black dwarf.", "star-cycles"),
    fact("Life cycle of a star much more massive than the Sun?", "Nebula → protostar → main sequence star → red supergiant → supernova → neutron star or black hole.", "star-cycles"),
    fact("What decides how a star ends its life?", "Its mass (not its age).", "star-cycles"),
    fact("What is a nebula?", "A cloud of dust and gas in space from which stars form.", "star-cycles"),
    fact("What happens in a protostar?", "Gravity pulls the cloud together; it becomes denser and hotter, but fusion has not yet started.", "star-cycles"),
    fact("What happens in a main sequence star?", "Hydrogen nuclei fuse into helium, releasing energy; the star is stable.", "star-cycles"),
    fact("What is a red giant?", "A star whose core hydrogen has run out: the core contracts and heats, helium fuses, and the outer layers expand and cool.", "star-cycles"),
    fact("What is a white dwarf?", "The small, very hot, dense core left after a Sun-like star sheds its outer layers; no fusion; slowly cooling.", "star-cycles"),
    fact("What is a supernova?", "The explosion of a massive star when its core collapses at the end of its life.", "star-cycles"),
    fact("What is left after a supernova?", "A neutron star — or a black hole if the star was massive enough.", "star-cycles"),
    fact("What is a black hole?", "The remnant of the most massive stars; gravity so strong that not even light can escape.", "star-cycles"),
    fact("Why is a main sequence star stable?", "The outward pressure of the hot gas (from fusion) balances the inward pull of gravity.", "star-balance"),
    fact("How does a protostar become a main sequence star?", "Gravity collapses the cloud, raising the temperature until hydrogen nuclei fuse; then gravity and the outward pressure balance.", "star-balance"),
    fact("Fusion or fission in stars?", "Fusion — small nuclei (hydrogen) join to make helium. Fission (splitting large nuclei) does not power stars.", "star-balance"),
    fact("Why does a star become a red giant when its hydrogen runs out?", "The core contracts and heats until helium fuses; the extra energy pushes the outer layers out, which expand and cool.", "star-balance"),
    # Observing
    fact("How have methods of observing the Universe changed?", "Naked eye → optical telescopes (bigger lenses and mirrors) → photography → telescopes for other wavelengths (radio, IR, X-ray) → telescopes in space → digital detectors and computers.", "observing"),
    fact("Why are some telescopes placed in space?", "Above the atmosphere there is no absorption of IR, UV and X-rays, no distortion by moving air, and no clouds or light pollution — sharper images, all wavelengths.", "observing"),
    fact("Give two disadvantages of a space telescope.", "Very expensive to build and launch; hard or impossible to repair or upgrade (and size limited by the rocket).", "space-telescopes"),
    fact("Which wavelengths does the atmosphere block?", "Most infrared, ultraviolet, X-rays and gamma rays. Visible light and radio waves get through.", "space-telescopes"),
    fact("Why use telescopes for wavelengths other than light?", "Different objects emit at different wavelengths: cool dust in infrared, very hot gas in X-rays; radio sees through dust. Each reveals what the others cannot.", "space-telescopes"),
    fact("What did Galileo's telescope show, and why did it matter?", "Four moons orbiting Jupiter and the phases of Venus — things that could not be explained by an Earth-centred model.", "solar-system-models"),
    # Models
    fact("What is the geocentric model?", "The Earth at the centre, not moving; the Sun, Moon, planets and stars orbit the Earth.", "solar-system-models"),
    fact("What is the heliocentric model?", "The Sun at the centre; the planets, including the Earth, orbit the Sun in ellipses; the Moon orbits the Earth.", "solar-system-models"),
    fact("Why do scientists replace one model with another?", "New observations that the old model cannot explain but the new model can — the new model has more supporting evidence.", "solar-system-models"),
    # Exam chains
    fact("The red-shift chain for the marks?", "Lines at longer wavelength → red-shifted → moving away → more distant galaxies have bigger red-shift so move faster → the Universe is expanding.", "redshift-argument"),
    fact("Why does red-shift alone not prove the Big Bang?", "Both the Big Bang and the Steady State theory describe an expanding Universe, so both predict red-shift.", "redshift-argument"),
    fact("What does Level 3 need in the 6-mark Big Bang evidence question?", "At least one piece of evidence described AND linked to what it shows (CMB → hot beginning; red-shift → expansion), the other identified. Isolated statements are Level 1.", "cmb-decides"),
    fact("Three word traps about the Big Bang and CMB?", "CMB is microwaves (not light or radio); it comes from all directions (not one place); the Big Bang was the expansion of space, not an explosion in space.", "cmb-decides"),
    fact("'Telescopes are on satellites because they are in space' — why no marks?", "It gives the location but not the reason: say the atmosphere absorbs or distorts the radiation.", "space-telescopes"),
    fact("Convert a weight on Earth to a weight on the Moon.", "Mass first (m = W ÷ 10), then W = m × 1.6. Or use the ratio: Moon weight = Earth weight × 1.6/10.", "weight-hard"),
    fact("Why do astronauts in the ISS float, when g there is about 8.7 N/kg?", "They and the station are falling towards the Earth together, so nothing pushes up on them — gravity is still acting and keeps them in orbit.", "weight-hard"),
]
