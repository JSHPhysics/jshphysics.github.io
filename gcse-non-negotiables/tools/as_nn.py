"""
as_nn.py — Topic 7 (Astronomy): the non-negotiables N1–N9. Every section
is Physics-only (the whole topic is), so each carries the P tag.

N1 The Solar System            N6 Big Bang, Steady State and the evidence
N2 Weight and g elsewhere      N7 Life cycles of stars
N3 Orbits                      N8 Observing the Universe
N4 Circular orbits and gravity N9 Key words
N5 Moving sources and red-shift
"""

from revlib import (
    choice, diagram, ewau, explain, fact, mark_scheme, marks, numeric,
    practice, section, worked, written,
)
import as_diagrams as dg

G_VALUES = "<table class='tbl data'><tr><th>Body</th><th>g in N/kg</th><th>Weight of 60 kg</th></tr><tr><td>Earth</td><td>10 (9.8)</td><td>600 N</td></tr><tr><td>Moon</td><td>1.6</td><td>96 N</td></tr><tr><td>Mars</td><td>3.7</td><td>222 N</td></tr><tr><td>Jupiter</td><td>25</td><td>1500 N</td></tr></table>"

# ---------------------------------------------------------------------
# N1 · The Solar System
# ---------------------------------------------------------------------

section_n1 = section(
    "solar-system", "nn", "The Solar System", "7.2P, 7.3P",
    equations=[r"\text{Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune}"],
    blurb="One star, eight planets in a fixed order, and everything else that orbits the Sun: moons round the planets, dwarf planets, asteroids and comets.",
    tags=["P"],
    checklist=[
        "Recall what the Solar System consists of",
        "Recall the eight planets in order from the Sun",
        "Distinguish a planet, a dwarf planet, a natural satellite, an asteroid and a comet",
    ],
    parts=[
        explain(
            "What is in it",
            "<table class='tbl'><tr><th>Object</th><th>What it is</th><th>Examples</th></tr>"
            "<tr><td><b>The Sun</b></td><td>the star at the centre; almost all the mass of the Solar System; everything else orbits it</td><td></td></tr>"
            "<tr><td><b>Planets</b> (eight)</td><td>large bodies in near-circular orbits round the Sun, massive enough to have cleared their orbits</td><td><b>M</b>ercury, <b>V</b>enus, <b>E</b>arth, <b>M</b>ars, <b>J</b>upiter, <b>S</b>aturn, <b>U</b>ranus, <b>N</b>eptune — <i>My Very Easy Method Just Speeds Up Naming</i></td></tr>"
            "<tr><td><b>Natural satellites</b> (moons)</td><td>bodies that orbit a planet</td><td>the Moon; Jupiter's Io, Europa, Ganymede, Callisto</td></tr>"
            "<tr><td><b>Dwarf planets</b></td><td>orbit the Sun and are round, but have not cleared their orbits of other objects</td><td>Pluto, Ceres, Eris</td></tr>"
            "<tr><td><b>Asteroids</b></td><td>rocky lumps, mostly in the asteroid belt between Mars and Jupiter</td><td>Vesta</td></tr>"
            "<tr><td><b>Comets</b></td><td>icy bodies in long, highly elliptical orbits; grow a tail of gas and dust near the Sun</td><td>Halley's comet</td></tr>"
            "<tr><td><b>Artificial satellites</b></td><td>spacecraft put into orbit round the Earth (or another body)</td><td>ISS, weather and communications satellites</td></tr></table>"
            "<p>The four inner planets are small and rocky; the four outer planets are gas giants, much larger and further apart.</p>",
        ),
        worked(
            "Planet or not?",
            "Pluto was called a planet until 2006 and is now a dwarf planet. State what Pluto has in common with the planets and what makes it a dwarf planet. (2 marks)",
            [
                "<b>In common:</b> it <b>orbits the Sun</b> and is massive enough to be <b>round</b>.",
                "<b>Dwarf:</b> it has <b>not cleared its orbit</b> of other objects — it shares its region with many similar icy bodies — so it does not meet the definition of a planet.",
            ],
        ),
        practice("The Solar System", [
            written("as-n1-q1", "List the eight planets in order of increasing distance from the Sun. (2)",
                    marks(["Mercury, Venus, Earth, Mars…", "…Jupiter, Saturn, Uranus, Neptune. (All eight in order for 2; one slip for 1.)"]), lines=2),
            choice("as-n1-q2", "Which of these is a natural satellite?",
                   ["Mars", "The Moon", "Ceres", "Halley's comet"], 1,
                   "A natural satellite (moon) orbits a planet."),
            written("as-n1-q3", "State the difference between a planet and a dwarf planet. (1)",
                    marks(["A planet has <b>cleared its orbit</b> of other objects; a dwarf planet orbits the Sun and is round but has <b>not</b> cleared its orbit."]), lines=2),
            choice("as-n1-q4", "Where are most asteroids found?",
                   ["Between Earth and Mars", "Between Mars and Jupiter", "Beyond Neptune", "Inside Mercury's orbit"], 1,
                   "The asteroid belt lies between the inner rocky planets and the gas giants."),
            written("as-n1-q5", "State what the Solar System consists of. (2)",
                    marks(["The <b>Sun</b> and the <b>eight planets</b> with their <b>natural satellites</b> (moons)…", "…plus <b>dwarf planets</b>, <b>asteroids</b> and <b>comets</b> (and artificial satellites)."]), lines=2),
            choice("as-n1-q6", "Which planet is furthest from the Sun?",
                   ["Uranus", "Saturn", "Neptune", "Pluto"], 2,
                   "Neptune is the eighth planet; Pluto is a dwarf planet."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N2 · Weight and g elsewhere
# ---------------------------------------------------------------------

section_n2 = section(
    "weight-elsewhere-nn", "nn", "Weight and g on other bodies", "7.1P",
    equations=[r"W = m \times g", r"g_{\text{Moon}} \approx 1.6\ \text{N/kg}"],
    blurb="Your mass is the same on the Moon; your weight is a sixth of what it is here, because the Moon's gravitational field strength is a sixth of the Earth's. g depends on the mass and the radius of the body you are standing on.",
    tags=["P"],
    checklist=[
        "Explain why weight and g differ from one body to another (mass and radius of the body)",
        "State that mass does not change from place to place",
        "Calculate weights and g values for other bodies",
    ],
    parts=[
        explain(
            "Why g is different",
            "<p><b>Weight</b> is the force of gravity on an object: $W = m \\times g$. The <b>mass</b> $m$ is the amount of matter and is the <b>same everywhere</b>. The <b>gravitational field strength</b> $g$ is the force per kilogram at that place, and it is different on each body.</p>"
            "<p>$g$ at the surface of a body depends on <b>the body's mass</b> (more mass → stronger pull) and <b>its radius</b> (further from the centre → weaker pull). The Moon has about 1/80 of the Earth's mass but only about 1/4 of its radius, which works out at $g \\approx 1.6$ N/kg — about a sixth. Jupiter is far more massive, so even with its large radius $g$ is about 25 N/kg.</p>" + G_VALUES +
            "<p>A <b>newton meter</b> (spring balance) reads the weight, so it reads less on the Moon; a <b>beam balance</b> compares masses, so it reads the same. Gravity does not stop in orbit: $g$ is a little smaller at the height of the ISS (about 8.7 N/kg), and that gravity is what keeps it in orbit (N4).</p>",
        ),
        worked(
            "Weight on Mars",
            "A lander has a mass of 1200 kg. On Mars g = 3.7 N/kg. Calculate the lander's weight on Mars and compare it with its weight on Earth.",
            ewau(r"W = m \times g", r"W = 1200 \times 3.7", "4440", "N on Mars — on Earth it is 1200 × 10 = 12 000 N; the mass is 1200 kg in both places"),
        ),
        practice("Weight and g", [
            written("as-n2-q1", "Explain why an astronaut weighs less on the Moon than on Earth, even though her mass is the same. (2)",
                    marks(["Weight = mass × gravitational field strength, and the Moon's <b>g is smaller</b> (about 1.6 N/kg against 10 N/kg)…",
                           "…because the Moon has much <b>less mass</b> than the Earth (and a smaller radius), so its gravitational pull on each kilogram is weaker."]), lines=3),
            numeric("as-n2-q2", "A 75 kg astronaut stands on the Moon (g = 1.6 N/kg). Calculate her weight.", 120, "N", "W = m × g with the Moon's g.",
                    ewau(r"W = m \times g", r"W = 75 \times 1.6", "120", "N")),
            choice("as-n2-q3", "A 10 kg box is taken from Earth to Mars. Which is correct?",
                   ["Its mass and weight both fall", "Its mass stays 10 kg; its weight falls from 100 N to 37 N", "Its mass falls; its weight stays the same", "Nothing changes"], 1,
                   "Mass is the same everywhere; weight follows g."),
            numeric("as-n2-q4", "An object weighs 180 N on a planet where g = 9.0 N/kg. Calculate its weight on Earth (g = 10 N/kg).", 200, "N", "Mass first: m = W ÷ g.",
                    [r"$m = \dfrac{180}{9.0} = 20$ kg.", r"On Earth $W = 20 \times 10 = 200$ N."]),
            written("as-n2-q5", "State two things that the value of g at the surface of a planet depends on. (2)",
                    marks(["The <b>mass</b> of the planet.", "The <b>radius</b> of the planet (distance from its centre to the surface)."]), lines=2),
            choice("as-n2-q6", "An astronaut takes a beam balance and a newton meter to the Moon. Which reading changes?",
                   ["Both", "Neither", "The newton meter (it measures weight)", "The beam balance (it measures mass)"], 2,
                   "A newton meter measures force; a beam balance compares masses, which do not change."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N3 · Orbits
# ---------------------------------------------------------------------

section_n3 = section(
    "orbits", "nn", "Orbits: moons, planets, comets and artificial satellites", "7.5P",
    equations=[r"\text{planets, moons: near-circular}", r"\text{comets: highly elliptical}"],
    blurb="Everything in orbit is held there by gravity. Planets and moons go round in near-circles at nearly steady speed; comets follow long ellipses and speed up near the Sun; artificial satellites are put where their job needs them.",
    tags=["P"],
    checklist=[
        "Describe the orbits of planets, moons, comets and artificial satellites",
        "Describe geostationary and polar (low) orbits and what each is used for",
        "Explain why a comet speeds up as it approaches the Sun",
    ],
    parts=[
        explain(
            "The four kinds",
            "<table class='tbl'><tr><th>Body</th><th>Orbits</th><th>Shape and speed</th></tr>"
            "<tr><td><b>Planets</b> (and dwarf planets, asteroids)</td><td>the Sun</td><td><b>near-circular</b> (slightly elliptical) orbits, all in roughly the same plane and the same direction; speed almost constant; the further out, the slower and the longer the year</td></tr>"
            "<tr><td><b>Moons</b> (natural satellites)</td><td>a planet</td><td>near-circular; the Moon takes about 27 days</td></tr>"
            "<tr><td><b>Comets</b></td><td>the Sun</td><td><b>highly elliptical</b>: far out for most of the orbit, then a fast swing round the Sun; <b>fastest when closest</b> to the Sun, slowest when furthest; grow a tail near the Sun</td></tr>"
            "<tr><td><b>Artificial satellites</b></td><td>the Earth (or a planet being studied)</td><td><b>geostationary</b>: high (36 000 km), above the equator, period <b>24 hours</b> so it stays over the same point — TV and communications; <b>polar / low orbit</b>: a few hundred km up, period about 90 minutes, passes over the whole surface as the Earth turns — weather, imaging, mapping</td></tr></table>"
            "<p>Why a comet speeds up: as it falls towards the Sun, gravity does work on it — energy is transferred from its gravitational potential store to its kinetic store — and the gravitational force is stronger closer in; on the way out the reverse happens.</p>",
        ),
        worked(
            "Choosing a satellite orbit",
            "Explain why a satellite used to relay television signals is put in a geostationary orbit, while a weather satellite is put in a low polar orbit. (3 marks)",
            [
                "<b>Geostationary:</b> its period is <b>24 hours</b>, the same as the Earth's rotation, so it <b>stays above the same point</b> on the equator — a fixed dish on a roof can point at it permanently.",
                "<b>Polar, low:</b> it circles every ~90 minutes while the <b>Earth turns beneath it</b>, so over a day it <b>passes over the whole surface</b> and can photograph everywhere.",
                "<b>Height:</b> a low orbit is also <b>closer</b>, so the images are more detailed.",
            ],
        ),
        practice("Orbits", [
            written("as-n3-q1", "Describe the orbit of a comet and how its speed changes. (2)",
                    marks(["A <b>highly elliptical</b> (very elongated) orbit around the Sun.", "It is <b>fastest when closest to the Sun</b> and slowest when furthest away."]), lines=2),
            choice("as-n3-q2", "A geostationary satellite…",
                   ["orbits over the poles every 90 minutes", "stays above the same point on the equator with a 24-hour period", "does not move", "orbits the Moon"], 1,
                   "Same period as the Earth's rotation, above the equator."),
            written("as-n3-q3", "Explain why a comet speeds up as it approaches the Sun. (2)",
                    marks(["The Sun's <b>gravitational force</b> on it increases as it gets closer, pulling it faster…",
                           "…energy is transferred from its <b>gravitational potential store to its kinetic store</b> (gravity does work on it)."]), lines=2),
            choice("as-n3-q4", "Which best describes the orbit of a planet?",
                   ["A perfect circle", "Near-circular (slightly elliptical) around the Sun", "Highly elliptical", "A straight line"], 1,
                   "Planets' orbits are ellipses very close to circles."),
            written("as-n3-q5", "State what keeps a satellite in orbit around the Earth. (1)",
                    marks(["The <b>force of gravity</b> (the Earth's gravitational pull on the satellite), acting towards the centre of the Earth."]), lines=2),
            written("as-n3-q6", "Give one use of a satellite in a low polar orbit and explain why that orbit suits the use. (2)",
                    marks(["Use: <b>weather forecasting / Earth imaging / mapping</b>.",
                           "The satellite passes over the poles every ~90 min while the Earth rotates underneath, so it <b>scans the whole surface</b> each day, and being low it sees detail."]), lines=3),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N4 · Circular orbits and gravity
# ---------------------------------------------------------------------

section_n4 = section(
    "circular-orbits", "nn", "Circular orbits: changing velocity at constant speed", "7.6P, 7.7P",
    equations=[r"\text{gravity} \perp \text{velocity} \Rightarrow \text{direction changes, speed does not}", r"\text{smaller radius} \Rightarrow \text{higher speed}"],
    blurb="A planet in a circular orbit moves at a steady speed but its velocity is changing all the time, because its direction is. The force of gravity, always towards the centre, is what changes it. Closer orbits need higher speeds.",
    tags=["P"],
    checklist=[
        "Explain how gravity changes a planet's velocity while its speed stays constant",
        "Explain why a body in a circular orbit is accelerating",
        "State how orbital speed and orbital radius are linked for a stable orbit",
    ],
    parts=[
        explain(
            "Velocity changes, speed does not",
            diagram(dg.orbit_svg(), 600, 260, "A planet in a circular orbit: the velocity is along the orbit, the force of gravity is towards the Sun — always at right angles to the velocity.") +
            "<p><b>Velocity is a vector</b>: speed <i>and</i> direction. In a circular orbit the <b>speed is constant</b> but the <b>direction is changing continuously</b>, so the <b>velocity is changing</b>, so the planet is <b>accelerating</b> — towards the centre. An acceleration needs a resultant force, and that force is <b>gravity</b>, acting <b>towards the Sun</b>, <b>at right angles to the velocity</b>. Because it is at right angles it does no work: it <b>changes the direction</b> of the motion but <b>not the speed</b>.</p>"
            "<p>The June 2024 marks (Q9(a)): the resultant force on a body in circular motion points <b>towards the centre</b> (not along the motion, no vertical component for a horizontal circle); it is accelerating because \"its <b>direction is continuously changing</b>\" or \"there is a <b>resultant force</b>\" or \"<b>velocity is a vector</b>\". \"Centripetal force\" on its own was ignored.</p>"
            "<p><b>Speed and radius</b> (7.7P, qualitative): for a stable orbit the gravitational force must be exactly enough to keep bending the path into a circle. Closer to the Sun gravity is stronger, so the orbit must be <b>faster</b>; further out it is weaker, so the orbit is <b>slower</b>. Put the other way: <b>if the speed of an orbiting body increases, it must move to a smaller radius to stay in a stable orbit</b>; if it slows, to a larger one. That is why Mercury races round in 88 days and Neptune takes 165 years.</p>",
        ),
        worked(
            "The 3-mark explanation",
            "A satellite moves in a circular orbit at constant speed. Explain why its velocity is changing and what causes the change. (3 marks)",
            [
                "<b>Velocity is a vector</b>, with direction as well as size; in a circle the <b>direction is continuously changing</b>, so the velocity changes even though the speed does not.",
                "<b>A changing velocity is an acceleration</b>, which needs a <b>resultant force</b>.",
                "That force is <b>gravity</b>, acting <b>towards the centre</b> of the Earth, at <b>right angles to the velocity</b> — so it changes the direction but not the speed.",
            ],
        ),
        practice("Circular orbits", [
            written("as-n4-q1", "A planet orbits the Sun at constant speed. Explain why it is accelerating. (2)",
                    marks(["Its <b>direction is continuously changing</b>, and velocity is a vector, so its <b>velocity is changing</b>.",
                           "A change in velocity is an acceleration (there is a resultant force — gravity — towards the Sun)."]), lines=2),
            choice("as-n4-q2", "In which direction does the force of gravity act on a planet in a circular orbit?",
                   ["Along the direction of motion", "Towards the centre (the Sun)", "Away from the Sun", "There is no force"], 1,
                   "Towards the centre, at right angles to the velocity."),
            written("as-n4-q3", "Explain why the force of gravity changes a planet's velocity but not its speed. (2)",
                    marks(["Gravity acts <b>towards the centre</b>, <b>at right angles to the velocity</b>.",
                           "A force at right angles to the motion <b>changes the direction</b> (bends the path) but does no work along the motion, so the <b>speed stays the same</b>."]), lines=3),
            choice("as-n4-q4", "Two satellites are in stable circular orbits. Satellite X moves faster than satellite Y. Which is correct?",
                   ["X has the smaller orbital radius", "X has the larger orbital radius", "Both have the same radius", "Speed and radius are not linked"], 0,
                   "A higher speed needs a stronger gravitational pull to hold the circle, which means being closer in."),
            written("as-n4-q5", "Mercury orbits the Sun faster than Neptune. Explain why, in terms of gravity. (2)",
                    marks(["Mercury is <b>much closer</b> to the Sun, so the <b>gravitational force</b> on it is much <b>stronger</b>.",
                           "A stronger force bends the path more sharply, so a <b>higher speed</b> is needed for a stable circular orbit at the smaller radius."]), lines=3),
            choice("as-n4-q6", "Which statement about a body in a circular orbit is true?",
                   ["Its speed and velocity are both constant", "Its speed is constant but its velocity changes", "Its velocity is constant but its speed changes", "Neither is constant"], 1,
                   "Constant speed, changing direction → changing velocity."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N5 · Moving sources and red-shift
# ---------------------------------------------------------------------

section_n5 = section(
    "redshift", "nn", "Moving sources and red-shift", "7.11P, 7.12P",
    equations=[r"\text{source moving away} \Rightarrow \lambda \uparrow,\ f \downarrow", r"\text{further galaxy} \Rightarrow \text{bigger red-shift}"],
    blurb="A wave source moving away from you stretches its waves: longer wavelength, lower frequency. Light from almost every distant galaxy is stretched towards the red end of the spectrum — and the further the galaxy, the more it is stretched.",
    tags=["P"],
    checklist=[
        "Describe how the observed wavelength and frequency change when a source moves away or towards an observer",
        "Describe red-shift in the light from galaxies and how it depends on distance",
        "Describe what is seen in the spectrum (lines shifted towards the red)",
    ],
    parts=[
        explain(
            "The Doppler effect and red-shift",
            "<p>When a <b>wave source moves relative to an observer</b>, the observed wavelength and frequency change. Moving <b>away</b>: each wave is emitted a little further off than the last, so the waves arrive <b>stretched out</b> — <b>longer wavelength, lower frequency</b>. Moving <b>towards</b>: squashed — <b>shorter wavelength, higher frequency</b>. You hear it in the drop in pitch of a siren as it passes.</p>"
            "<p><b>Red-shift:</b> light from distant galaxies has <b>longer wavelengths</b> than light from the same elements in a laboratory on Earth — the dark lines in its spectrum are <b>shifted towards the red end</b>. So the galaxies are <b>moving away</b> from us. And the <b>more distant</b> the galaxy, the <b>bigger its red-shift</b>, so the <b>faster it is moving away</b>.</p>"
            "<p>The June 2024 scheme (Q1(c)(ii), 3 marks): red-shift means the galaxies are <b>moving away</b>; <b>more distant</b> galaxies have a <b>bigger</b> red-shift; more distant galaxies are <b>moving faster</b>. A question may give the equation $z = \\dfrac{\\Delta\\lambda}{\\lambda}$ (change in wavelength ÷ original wavelength); it is not on the equation list, so it will be supplied. When calculating with it, keep both wavelengths in the same form — both in nm, or both in metres in standard form — the 2022 report's advice (the arithmetic is in T3).</p>",
        ),
        worked(
            "Reading a red-shifted spectrum",
            "A hydrogen line is at 656 nm in the laboratory and at 668 nm in the light from a galaxy. State what this tells you about the galaxy, and what you would expect for a galaxy twice as far away. (3 marks)",
            [
                "<b>Observation:</b> the line has a <b>longer wavelength</b> than on Earth — it is <b>red-shifted</b>.",
                "<b>Meaning:</b> the galaxy is <b>moving away</b> from us.",
                "<b>Further galaxy:</b> a <b>larger</b> red-shift (the line at a longer wavelength still), because more distant galaxies are moving away <b>faster</b>.",
            ],
        ),
        practice("Red-shift", [
            written("as-n5-q1", "A source of waves moves away from an observer. State what happens to the observed wavelength and frequency. (2)",
                    marks(["Wavelength <b>increases</b> (longer).", "Frequency <b>decreases</b> (lower)."]), lines=2),
            written("as-n5-q2", "State what is meant by red-shift. (1)",
                    marks(["The <b>increase in wavelength</b> of light from a source (galaxy) that is <b>moving away</b> — its spectral lines are shifted towards the red end of the spectrum."]), lines=2),
            choice("as-n5-q3", "Galaxy A is further from Earth than galaxy B. Which is correct?",
                   ["A has a smaller red-shift than B", "A has a larger red-shift than B and is moving away faster", "Both have the same red-shift", "A is moving towards us"], 1,
                   "Red-shift increases with distance."),
            written("as-n5-q4", "Describe how the red-shift of light from galaxies depends on their distance from Earth. (2)",
                    marks(["Light from (almost) all galaxies is red-shifted — they are <b>moving away</b>.", "The <b>further</b> the galaxy, the <b>greater</b> the red-shift (the faster it recedes)."]), lines=2),
            numeric("as-n5-q5", "A spectral line at 500 nm on Earth appears at 520 nm in light from a galaxy. The red-shift z = (change in wavelength) ÷ (original wavelength). Calculate z.", 0.04, "",
                    "Δλ = 20 nm; keep both in nm.", [r"$z = \dfrac{520 - 500}{500} = \dfrac{20}{500} = 0.04$."]),
            choice("as-n5-q6", "A star's light is blue-shifted. What does this show?",
                   ["It is moving away", "It is moving towards us", "It is very hot", "It is very far away"], 1,
                   "Towards → shorter wavelength → blue-shift (a few nearby galaxies, e.g. Andromeda, do this)."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N6 · Big Bang, Steady State, evidence
# ---------------------------------------------------------------------

section_n6 = section(
    "big-bang", "nn", "Big Bang, Steady State, and the evidence", "7.8P, 7.9P, 7.10P, 7.13P, 7.14P, 7.15P",
    equations=[r"\text{evidence: red-shift + CMB}", r"\text{Big Bang accepted: more supporting evidence}"],
    blurb="Two theories once competed to explain an expanding Universe. Red-shift fits both; the cosmic microwave background fits only the Big Bang. That is why the Big Bang is the accepted model.",
    tags=["P"],
    checklist=[
        "Compare the Big Bang and Steady State theories",
        "Describe the two pieces of evidence: red-shift and the CMB",
        "Explain why red-shift is evidence for expansion and how both theories account for it",
        "Explain why the discovery of the CMB led to the Big Bang being accepted",
    ],
    parts=[
        explain(
            "The two theories and the two pieces of evidence",
            "<table class='tbl'><tr><th></th><th>Big Bang</th><th>Steady State</th></tr>"
            "<tr><td>The Universe</td><td>began about 13.8 billion years ago from a <b>very small, very hot, very dense</b> point and has been <b>expanding</b> (and cooling) ever since</td><td>has <b>always existed</b> and always will; it is expanding, but <b>new matter is continually created</b> so it looks the same at all times</td></tr>"
            "<tr><td>Explains red-shift?</td><td><b>yes</b> — space is expanding, so galaxies move apart</td><td><b>yes</b> — space is expanding, so galaxies move apart</td></tr>"
            "<tr><td>Explains the CMB?</td><td><b>yes</b> — predicted it: the leftover radiation from the hot early Universe, stretched to microwaves by the expansion</td><td><b>no</b> — gives no reason for it</td></tr>"
            "<tr><td>Status</td><td><b>accepted</b> model</td><td>abandoned</td></tr></table>"
            "<p><b>Red-shift → expansion</b> (7.13P): the light from distant galaxies is red-shifted, so they are <b>moving away</b>; the <b>further away</b> a galaxy, the <b>faster</b> it recedes. That is what you see from any point in a space that is <b>expanding everywhere</b> — like dots on an inflating balloon. Running it backwards, everything was once together: a beginning.</p>"
            "<p><b>The CMB</b> (cosmic microwave background, 7.15P): faint <b>microwave radiation coming from every direction in the sky</b>, at the same temperature everywhere (about 2.7 K). The Big Bang theory <b>predicted</b> it: the early Universe was hot and full of radiation, and the expansion has stretched that radiation to microwave wavelengths. When it was <b>discovered (1964)</b> it matched the prediction; Steady State had no explanation, so the Big Bang became the <b>accepted model</b> — it is the theory with <b>more supporting evidence</b> (7.10P).</p>"
            "<p>The June 2025 6-marker (Q10(c)): Level 3 needs <b>at least one piece of evidence described and linked to the aspect of the Big Bang it supports</b>, and the other identified — red-shift linked to <b>expansion</b>, the CMB (microwaves \"across the sky\") linked to a <b>definite beginning</b> (a hot early Universe). Isolated statements were Level 1.</p>",
        ),
        worked(
            "The 6-mark answer",
            "Describe the evidence that supports the Big Bang theory. (6 marks)",
            [
                "<b>Red-shift — observation:</b> light from distant galaxies has <b>longer wavelengths</b> than the same light on Earth; the further the galaxy, the <b>bigger the red-shift</b>.",
                "<b>Red-shift — what it shows:</b> the galaxies are <b>moving away</b>, and the more distant ones faster, so the <b>Universe is expanding</b>; traced back, everything was once in one place — a beginning.",
                "<b>CMB — observation:</b> faint <b>microwave radiation</b> is detected coming from <b>all directions</b> in the sky, at almost the same intensity everywhere.",
                "<b>CMB — what it shows:</b> the Big Bang predicted it as the <b>radiation left over from the hot, dense early Universe</b>, stretched to microwaves by the expansion; the Steady State theory could not explain it.",
                "<b>Conclusion:</b> red-shift fits both theories, the CMB fits only the Big Bang, so the Big Bang has <b>more supporting evidence</b> and is the accepted model.",
            ],
        ),
        practice("Big Bang", [
            written("as-n6-q1", "Describe the Big Bang theory. (2)",
                    marks(["The Universe began from a <b>very small, hot, dense</b> point (about 13.8 billion years ago)…", "…and has been <b>expanding</b> (and cooling) ever since."]), lines=2),
            written("as-n6-q2", "State two differences between the Big Bang theory and the Steady State theory. (2)",
                    marks(["Big Bang: the Universe had a <b>beginning</b>; Steady State: it has <b>always existed</b>.",
                           "Steady State: <b>new matter is continually created</b> as it expands so it always looks the same; Big Bang: no new matter — the Universe cools and spreads out."]), lines=3),
            written("as-n6-q3", "Explain how red-shift provides evidence that the Universe is expanding. (3)",
                    mark_scheme([
                        ("Observation", "Light from distant galaxies is <b>red-shifted</b> (longer wavelength), so they are <b>moving away</b> from us."),
                        ("Pattern", "The <b>further</b> away the galaxy, the <b>bigger</b> the red-shift, so the <b>faster</b> it is moving away."),
                        ("Conclusion", "That is exactly what is seen if <b>space itself is expanding</b> everywhere, carrying the galaxies apart."),
                    ]), lines=4),
            written("as-n6-q4", "Explain why the discovery of the cosmic microwave background radiation led to the Big Bang theory becoming the accepted model. (3)",
                    mark_scheme([
                        ("What", "Microwave radiation is detected <b>from all directions</b> in space."),
                        ("Predicted", "The Big Bang theory had <b>predicted</b> it: radiation from the <b>hot early Universe</b>, stretched to microwave wavelengths by the expansion."),
                        ("Decides", "The Steady State theory <b>could not explain</b> it, so the Big Bang had <b>more supporting evidence</b> and was accepted."),
                    ]), lines=4),
            choice("as-n6-q5", "Which piece of evidence is explained by the Big Bang theory but NOT by the Steady State theory?",
                   ["Red-shift of galaxies", "The cosmic microwave background", "The existence of stars", "The orbits of planets"], 1,
                   "Both theories include expansion (so both explain red-shift); only the Big Bang predicts the CMB."),
            written("as-n6-q6", "Explain how the Steady State theory accounts for the red-shift of galaxies. (2)",
                    marks(["It also says the Universe is <b>expanding</b>, so galaxies move apart and their light is red-shifted.",
                           "It adds that <b>new matter is continually created</b> in the gaps, so the Universe keeps the same average density and appearance for ever."]), lines=3),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N7 · Life cycles of stars
# ---------------------------------------------------------------------

section_n7 = section(
    "star-cycles", "nn", "The life cycles of stars", "7.16P, 7.18P",
    equations=[r"\text{nebula} \rightarrow \text{protostar} \rightarrow \text{main sequence} \rightarrow \ldots"],
    blurb="All stars start the same way, from a collapsing cloud of gas and dust. What happens at the end depends on mass: a Sun-like star swells into a red giant and fades as a white dwarf; a much heavier one explodes as a supernova and leaves a neutron star or a black hole.",
    tags=["P"],
    checklist=[
        "Describe the life cycle of a star of similar mass to the Sun, stage by stage",
        "Describe the life cycle of a star with a mass much larger than the Sun",
        "State what decides which path a star takes",
    ],
    parts=[
        explain(
            "The two paths",
            diagram(dg.life_cycle_svg(), 660, 275, "The life cycles of stars. Every star passes through nebula, protostar and main sequence; its mass decides what happens next.") +
            "<table class='tbl'><tr><th>Stage</th><th>What is happening</th></tr>"
            "<tr><td><b>Nebula</b></td><td>a huge <b>cloud of dust and gas</b> (mostly hydrogen); <b>gravity</b> pulls it together</td></tr>"
            "<tr><td><b>Protostar</b></td><td>the collapsing cloud gets <b>denser and hotter</b> as gravitational potential energy is transferred to thermal energy</td></tr>"
            "<tr><td><b>Main sequence star</b></td><td>the core is hot enough for <b>hydrogen nuclei to fuse into helium</b>, releasing energy; the star is <b>stable</b> because the outward pressure from the hot gas balances gravity; the Sun is here, for about 10 billion years</td></tr>"
            "<tr><td colspan='2'><b>Star of similar mass to the Sun</b></td></tr>"
            "<tr><td><b>Red giant</b></td><td>the hydrogen in the core runs out; the core contracts and heats, helium fuses into heavier elements, and the outer layers <b>expand and cool</b> (red)</td></tr>"
            "<tr><td><b>White dwarf</b></td><td>the outer layers drift away; the small, very hot, dense core is left with <b>no fusion</b>, slowly cooling…</td></tr>"
            "<tr><td><b>Black dwarf</b></td><td>…until it no longer glows</td></tr>"
            "<tr><td colspan='2'><b>Star with a mass much larger than the Sun</b></td></tr>"
            "<tr><td><b>Red supergiant</b></td><td>as the red giant, but far bigger; fusion makes heavier and heavier elements, up to iron</td></tr>"
            "<tr><td><b>Supernova</b></td><td>the core collapses suddenly and the star <b>explodes</b>, scattering the elements (and making the ones heavier than iron)</td></tr>"
            "<tr><td><b>Neutron star</b> or <b>black hole</b></td><td>the core left behind is a tiny, incredibly dense <b>neutron star</b> — or, for the <b>most massive</b> stars, a <b>black hole</b>, whose gravity is so strong that not even light escapes</td></tr></table>"
            "<p>The June 2025 report (Q10(a)): the key variable deciding the end of a star is its <b>mass</b> — not its age. \"Older stars are more likely to become black holes\" was the common wrong answer; the heaviest stars have the <i>shortest</i> lives.</p>",
        ),
        worked(
            "A Sun-like star",
            "Describe the life cycle of a star of similar mass to the Sun. (4 marks)",
            [
                "<b>Nebula → protostar:</b> <b>gravity</b> pulls a cloud of dust and gas together; it gets denser and hotter, forming a protostar.",
                "<b>Main sequence:</b> when the core is hot enough, <b>hydrogen fuses into helium</b>; the star is stable for billions of years, the outward pressure balancing gravity.",
                "<b>Red giant:</b> when the hydrogen runs out, the core contracts and the outer layers <b>expand and cool</b>; helium fuses into heavier elements.",
                "<b>White dwarf → black dwarf:</b> the outer layers are shed, leaving a hot dense core with no fusion that <b>cools</b> into a white dwarf and eventually a black dwarf.",
            ],
        ),
        practice("Life cycles", [
            written("as-n7-q1", "Put these stages in order for a star like the Sun: white dwarf, nebula, red giant, main sequence, protostar. (1)",
                    marks(["Nebula → protostar → main sequence → red giant → white dwarf (→ black dwarf)."]), lines=2),
            choice("as-n7-q2", "What decides whether a star ends as a white dwarf or as a neutron star / black hole?",
                   ["Its age", "Its mass", "Its distance from Earth", "Its colour when it formed"], 1,
                   "Mass. The most massive stars have the shortest lives and the most violent ends."),
            written("as-n7-q3", "Describe what happens in a main sequence star, and why it is stable. (2)",
                    marks(["<b>Hydrogen nuclei fuse into helium</b> in the core, releasing energy.",
                           "It is stable because the <b>outward pressure</b> of the hot gas (thermal expansion) <b>balances the inward pull of gravity</b>."]), lines=2),
            written("as-n7-q4", "Describe the final stages of a star with a mass much greater than the Sun. (3)",
                    mark_scheme([
                        ("Supergiant", "It expands into a <b>red supergiant</b>, fusing heavier elements."),
                        ("Supernova", "It then <b>explodes as a supernova</b>, scattering elements into space."),
                        ("Remnant", "The core left behind is a <b>neutron star</b>, or a <b>black hole</b> if the star was massive enough."),
                    ]), lines=4),
            choice("as-n7-q5", "What is a protostar?",
                   ["A star that has run out of hydrogen", "A collapsing cloud of gas that is heating up but has not yet started fusion", "The remains of a supernova", "A small cool star"], 1,
                   "Gravity compresses and heats the cloud until fusion can begin."),
            written("as-n7-q6", "State what a white dwarf is and what eventually happens to it. (2)",
                    marks(["The small, very hot, dense <b>core</b> left when a Sun-like star sheds its outer layers; <b>no fusion</b> takes place in it.",
                           "It slowly <b>cools and fades</b>, eventually becoming a <b>black dwarf</b>."]), lines=2),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N8 · Observing the Universe
# ---------------------------------------------------------------------

section_n8 = section(
    "observing", "nn", "How we observe the Universe, and why some telescopes are in space", "7.19P",
    equations=[r"\text{naked eye} \rightarrow \text{optical telescopes} \rightarrow \text{photography} \rightarrow \text{all wavelengths} \rightarrow \text{space}"],
    blurb="From eyes to Galileo's telescope to orbiting observatories that see in radio, infrared and X-rays. Each step let us see fainter, further and in more of the spectrum — and the atmosphere is the reason the biggest step was leaving the ground.",
    tags=["P"],
    checklist=[
        "Describe how methods of observing the Universe have changed over time",
        "Explain why some telescopes are placed outside the Earth's atmosphere",
        "Give a disadvantage of space telescopes",
    ],
    parts=[
        explain(
            "The timeline, and the atmosphere problem",
            "<ol><li><b>Naked eye:</b> for most of history — positions of stars and planets, no detail.</li>"
            "<li><b>Optical telescopes</b> (Galileo, 1609–10): magnified images — moons of Jupiter, phases of Venus, craters on the Moon. Bigger lenses and <b>mirrors</b> (Newton's reflecting telescope) collect more light, so fainter and more distant objects can be seen.</li>"
            "<li><b>Photography</b> (1800s): long exposures record far fainter objects than the eye and give a permanent record to measure and compare.</li>"
            "<li><b>Telescopes for other wavelengths</b> (1930s on): <b>radio</b>, <b>infrared</b>, <b>ultraviolet</b>, <b>X-ray</b> and gamma telescopes reveal objects and processes invisible in light — cool dust clouds in infrared, black holes' surroundings in X-rays, the CMB in microwaves.</li>"
            "<li><b>Telescopes in space</b> (Hubble 1990, James Webb 2021): above the atmosphere.</li>"
            "<li><b>Computers and digital detectors</b>: far more sensitive than film, and able to process huge amounts of data.</li></ol>"
            "<p><b>Why go above the atmosphere:</b> the atmosphere <b>absorbs</b> most infrared, ultraviolet, X-rays and gamma rays, so those can only be observed from space; moving air <b>distorts</b> the light (stars twinkle), blurring images; <b>clouds</b>, dust and <b>light pollution</b> get in the way. In space there is a clear view of every wavelength, day and night. The 2022 report: say <b>that</b> the telescope is in space <b>and why</b> — \"candidates stated the location without explaining why it matters\".</p>"
            "<p><b>Disadvantages:</b> very <b>expensive</b> to build and launch; <b>hard or impossible to repair</b> or upgrade; size limited by the rocket.</p>",
        ),
        worked(
            "Why in space",
            "Explain why some telescopes are placed on satellites rather than on the Earth's surface. (2 marks)",
            [
                "<b>Where:</b> a satellite telescope is <b>above the Earth's atmosphere</b>.",
                "<b>Why:</b> so the light it collects is not <b>absorbed</b> (the atmosphere blocks most infrared, UV and X-rays) or <b>distorted</b> by the air, clouds, dust and light pollution — giving sharper images and access to wavelengths that never reach the ground.",
            ],
        ),
        practice("Observing", [
            written("as-n8-q1", "Describe two ways in which methods of observing the Universe have changed over time. (2)",
                    marks(["From the naked eye to <b>telescopes</b> (larger lenses and mirrors collecting more light), and to <b>photography / digital detectors</b> recording fainter objects.",
                           "From visible light only to telescopes for <b>other wavelengths</b> (radio, infrared, X-ray), and from the ground to <b>telescopes in space</b>."]), lines=3),
            written("as-n8-q2", "Explain why an infrared telescope must be placed in space. (2)",
                    marks(["The Earth's <b>atmosphere absorbs</b> most infrared radiation…", "…so very little reaches the ground; above the atmosphere the telescope receives it all."]), lines=2),
            choice("as-n8-q3", "Which is a disadvantage of a space telescope compared with one on the ground?",
                   ["Images are distorted by the atmosphere", "It cannot observe infrared", "It is very expensive and difficult to repair", "It can only be used at night"], 2,
                   "The others are disadvantages of ground telescopes."),
            written("as-n8-q4", "Give two advantages of a telescope in orbit over one on a mountain top. (2)",
                    marks(["No <b>absorption</b> of wavelengths (infrared, UV, X-ray) by the atmosphere.",
                           "No <b>distortion</b> / twinkling from moving air, no clouds or light pollution — sharper images, usable all the time."]), lines=2),
            choice("as-n8-q5", "What did Galileo's telescope reveal that supported the Sun-centred model?",
                   ["The red-shift of galaxies", "Moons orbiting Jupiter and the phases of Venus", "The CMB", "Neptune"], 1,
                   "Things that clearly did not orbit the Earth (T1)."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N9 · Key words
# ---------------------------------------------------------------------

DEFINITIONS = [
    ("Natural satellite", "A body that <b>orbits a planet</b> (a moon).", "\"a planet\""),
    ("Artificial satellite", "A <b>man-made object</b> placed in orbit around the Earth (or another body).", "\"a star\""),
    ("Dwarf planet", "A body that <b>orbits the Sun</b> and is round but has <b>not cleared its orbit</b> of other objects.", "\"a small planet\""),
    ("Comet", "An <b>icy</b> body in a <b>highly elliptical</b> orbit around the Sun, fastest when nearest the Sun.", "\"a shooting star\""),
    ("Orbit", "The <b>path</b> of one body around another, held by <b>gravity</b>.", "\"going round\" with no force"),
    ("Geostationary orbit", "An orbit above the equator with a <b>period of 24 hours</b>, so the satellite stays over the same point.", "\"a satellite that does not move\""),
    ("Gravitational field strength g", "The <b>force of gravity per kilogram</b> at a place, in N/kg; it depends on the body's mass and radius.", "\"gravity\""),
    ("Red-shift", "The <b>increase in wavelength</b> of light from a source moving <b>away</b> — spectral lines shifted towards the red end.", "\"the light turns red\""),
    ("Cosmic microwave background (CMB)", "<b>Microwave radiation</b> coming from <b>all directions</b> in space — left over from the hot early Universe.", "\"radiation from the Sun\""),
    ("Big Bang theory", "The Universe began from a <b>very small, hot, dense</b> point and has been <b>expanding</b> ever since.", "\"an explosion in space\""),
    ("Steady State theory", "The Universe has <b>always existed</b>, expanding while <b>new matter is created</b> so it always looks the same.", "\"the Universe does not change\""),
    ("Nebula", "A <b>cloud of dust and gas</b> in space from which stars form.", "\"a galaxy\""),
    ("Protostar", "A collapsing cloud that is <b>heating up</b> under gravity but has <b>not yet started fusion</b>.", "\"a young star that shines\""),
    ("Main sequence star", "A star in the stable stage, <b>fusing hydrogen into helium</b>, with outward pressure balancing gravity.", "\"a normal star\""),
    ("Red giant", "A star whose core hydrogen has run out: the <b>outer layers expand and cool</b>.", "\"a big red star\""),
    ("White dwarf", "The small, hot, dense <b>core</b> left by a Sun-like star, with <b>no fusion</b>, slowly cooling.", "\"a dead star\""),
    ("Supernova", "The <b>explosion</b> of a massive star at the end of its life.", "\"a new star\""),
    ("Neutron star", "The tiny, <b>extremely dense</b> core left after a supernova.", "\"a star made of neutrons\" alone"),
    ("Black hole", "The remnant of the most massive stars: gravity so strong that <b>not even light can escape</b>.", "\"a hole in space\""),
]


def definitions_table():
    html = "<table class='tbl'><tr><th>Term</th><th>What to write (mark-scheme form)</th><th>Not this</th></tr>"
    for term, definition, wrong in DEFINITIONS:
        html += "<tr><td><b>" + term + "</b></td><td>" + definition + "</td><td>" + wrong + "</td></tr>"
    html += "</table>"
    return html


section_keywords = section(
    "keywords-astronomy", "nn", "Key words: state what is meant by…", "7",
    equations=[r"\text{definition, word for word}"],
    blurb="One-mark definitions in the form of words the mark schemes credit. The bold words are the ones the marks are attached to.",
    tags=["P"],
    checklist=[
        "Define natural and artificial satellite, dwarf planet, comet, orbit and geostationary",
        "Define red-shift, the CMB, and the two theories",
        "Define each stage of the life cycle of stars",
    ],
    parts=[
        explain("The definitions", "<p>\"<b>State what is meant by</b>\" asks for the definition. Learn these as sentences.</p>" + definitions_table()),
        practice("Key words", [
            written("as-kw-q1", "State what is meant by red-shift. (1)",
                    marks(["The <b>increase in the wavelength</b> of light from a source that is <b>moving away</b> from the observer."]), lines=2),
            written("as-kw-q2", "State what is meant by a main sequence star. (1)",
                    marks(["A stable star <b>fusing hydrogen into helium</b> in its core, with the outward pressure balancing gravity."]), lines=2),
            written("as-kw-q3", "State what is meant by the cosmic microwave background radiation. (1)",
                    marks(["<b>Microwave radiation</b> detected coming from <b>every direction</b> in space, left over from the early Universe."]), lines=2),
            choice("as-kw-q4", "Which is the correct definition of a geostationary orbit?",
                   ["Any orbit over the equator", "An orbit with a 24-hour period above the equator, so the satellite stays over one point", "An orbit over the poles", "An orbit that never moves"], 1,
                   "Period = the Earth's rotation period."),
            written("as-kw-q5", "State what is meant by a nebula. (1)",
                    marks(["A <b>cloud of dust and gas</b> in space (from which stars form)."]), lines=2),
            written("as-kw-q6", "State what is meant by a supernova. (1)",
                    marks(["The <b>explosion</b> of a star much more massive than the Sun at the end of its life."]), lines=2),
            choice("as-kw-q7", "A student writes \"the Big Bang was an explosion in space\". What is wrong with this?",
                   ["Nothing", "Space itself began expanding from a tiny, hot, dense point — it was not an explosion into existing space", "It was a quiet event", "It happened on Earth"], 1,
                   "The expansion is of space, not of matter through space."),
            written("as-kw-q8", "State what is meant by a black hole. (1)",
                    marks(["The remnant of a very massive star whose <b>gravity is so strong that not even light can escape</b> from it."]), lines=2),
        ]),
    ],
)

FACTS_KW = [fact("State what is meant by: " + term.lower() + ".", definition, "keywords-astronomy") for term, definition, wrong in DEFINITIONS]

SECTIONS = [section_n1, section_n2, section_n3, section_n4, section_n5, section_n6, section_n7, section_n8, section_keywords]
