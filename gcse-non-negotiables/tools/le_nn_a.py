"""
le_nn_a.py — Topic 5 (Light and the EM spectrum): the non-negotiables N1–N6.

N1 Reflection          N4 Colour
N2 Refraction          N5 Lenses
N3 Total internal reflection   N6 EM waves and v = fλ
"""

from revlib import (
    choice, diagram, ewau, explain, mark_scheme, marks, numeric, practice,
    section, sf, worked, written,
)
import le_diagrams as dg

C = 3.0e8

# ---------------------------------------------------------------------
# N1 · Reflection
# ---------------------------------------------------------------------

section_n1 = section(
    "reflection", "nn", "Reflection", "5.1P, 5.2P",
    equations=[r"\text{angle of incidence} = \text{angle of reflection}", r"\text{angles measured from the normal}"],
    blurb="Light reflects off a mirror so that the angle of reflection equals the angle of incidence. Both angles are measured from the <b>normal</b> — the line at right angles to the surface — never from the surface.",
    tags=["P"],
    checklist=[
        "State the law of reflection and draw the ray diagram with the normal",
        "Measure angles of incidence and reflection from the normal",
        "Explain the difference between specular and diffuse reflection",
    ],
    parts=[
        explain(
            "The law and the diagram",
            diagram(dg.reflection_svg(), 480, 270, "Reflection at a plane mirror. The normal is drawn first, at 90° to the mirror where the ray hits it; i and r are measured from the normal and are equal.") +
            "<p><b>Law of reflection:</b> the angle of incidence equals the angle of reflection. The <b>normal</b> is a line at <b>90° to the surface</b> at the point where the ray strikes. The angle of incidence $i$ is between the incident ray and the normal; the angle of reflection $r$ is between the reflected ray and the normal.</p>"
            "<p>In the exam the mark for a ray diagram is usually for the normal being drawn and the angles being marked from it, not for the rays: the June 2024 scheme for the reflection practical gave marks for \"draw the normal, perpendicular to the mirror at the point of reflection\" and \"label the angles of incidence and reflection measured from the normal\".</p>",
        ),
        explain(
            "Specular and diffuse reflection",
            "<p><b>Specular</b> reflection is from a <b>smooth</b> surface (a mirror, still water): parallel rays stay parallel after reflecting, because every ray meets a surface at the same angle, so you see a clear image.</p>"
            "<p><b>Diffuse</b> reflection is from a <b>rough</b> surface (paper, a wall): the law of reflection still holds for every ray, but the surface is at a different angle at each point, so the normals point in different directions and parallel rays are <b>scattered</b> in all directions — no image, but the surface can be seen from anywhere.</p>"
            "<p>The exam point: the law applies to <b>all</b> surfaces (June 2024 Q6(a)(i)). Rough surfaces do not break the law; their normals just vary.</p>",
        ),
        worked(
            "Explaining diffuse reflection",
            "Explain why you cannot see your reflection in a sheet of white paper, even though the paper reflects light. (2 marks)",
            [
                "<b>Surface:</b> the paper's surface is <b>rough</b> (uneven on a small scale), so the <b>normal is in a different direction at each point</b>.",
                "<b>Rays:</b> each ray still obeys the law of reflection, but parallel rays are reflected in <b>different directions (scattered)</b> — diffuse reflection — so no image forms.",
            ],
        ),
        practice("Reflection", [
            choice("le-n1-q1", "A ray hits a mirror at 30° to the mirror's surface. What is the angle of incidence?",
                   ["30°", "60°", "90°", "120°"], 1,
                   "Angles are measured from the normal, which is at 90° to the surface: 90° − 30° = 60°."),
            written("le-n1-q2", "State the law of reflection. (1)",
                    marks(["The <b>angle of incidence equals the angle of reflection</b> (both measured from the normal)."]), lines=2),
            written("le-n1-q3", "Describe how a student could show that the angle of incidence equals the angle of reflection using a ray box, a plane mirror, paper and a protractor. (3)",
                    mark_scheme([
                        ("Set up", "Stand the mirror on the paper, <b>mark its position</b>, shine a ray at it and <b>mark the incident and reflected rays</b> with crosses / draw along them."),
                        ("Normal", "Remove the mirror, join the crosses, and <b>draw the normal at 90° to the mirror line</b> at the point of reflection (using the protractor)."),
                        ("Measure", "<b>Measure the angles of incidence and reflection from the normal</b> with the protractor; repeat for several angles."),
                    ], extra=["June 2024 Q6(a)(ii): any three of mark the positions / draw the normal perpendicular to the mirror / label the angles from the normal / use a protractor. \"Angle of refraction\" is not accepted."]), lines=5),
            choice("le-n1-q4", "Which is the correct explanation of diffuse reflection?",
                   ["The surface breaks the law of reflection", "The surface is rough, so the normal points in different directions at different points and rays are scattered", "The surface absorbs all the light", "The rays reflect back along their own path"], 1,
                   "The law holds everywhere; it is the direction of the normal that varies on a rough surface."),
            written("le-n1-q5", "Explain why a calm lake gives a clear reflection of the hills but a rippled lake does not. (2)",
                    marks(["Calm water is a <b>smooth</b> surface: parallel rays reflect parallel (<b>specular</b> reflection), so an image forms.",
                           "Rippled water is <b>rough</b>: the normal differs from point to point so rays are <b>scattered</b> (diffuse reflection) and no clear image forms."]), lines=3),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N2 · Refraction
# ---------------------------------------------------------------------

section_n2 = section(
    "refraction", "nn", "Refraction", "5.1P, 5.9, 5.14",
    equations=[r"\text{into glass: slows down, bends towards the normal}", r"\text{out of glass: speeds up, bends away}", r"f \text{ unchanged}"],
    blurb="Light changes direction when it crosses a boundary between materials because its <b>speed changes</b>. Into glass or water it slows and bends towards the normal; out again it speeds up and bends away.",
    checklist=[
        "Draw the ray diagram for a ray through a rectangular glass block, with normals and angles",
        "State which way the ray bends entering and leaving glass, and why (speed change)",
        "State what happens to speed, wavelength and frequency on refraction",
    ],
    parts=[
        explain(
            "The ray diagram",
            diagram(dg.refraction_svg(), 480, 290, "A ray through a rectangular glass block. Entering: bends towards the normal (angle of refraction smaller than angle of incidence). Leaving: bends away by the same amount, so the emergent ray is parallel to the incident ray but shifted sideways.") +
            "<p>Three things every diagram must have: the <b>normal</b> at each surface (dashed, at 90° to the surface), the <b>angle of incidence</b> and <b>angle of refraction</b> marked from the normal, and <b>arrows</b> on the rays.</p>"
            "<p>A ray along the normal (angle of incidence 0°) goes straight through without bending — it still slows down, but there is no change of direction. That is the answer to the \"why does this ray not bend?\" question (June 2023 Q8(a)(i), June 2024 Q6(b)(i)).</p>",
        ),
        explain(
            "Why it bends: the speed changes",
            "<p><b>Refraction is caused by a change in speed.</b> Light travels more slowly in glass (or water) than in air. When a wavefront meets the boundary at an angle, the part that enters the glass first slows down first, so the wavefront swings round — the ray bends <b>towards the normal</b>. Leaving the glass, the first part out speeds up first, and the ray bends <b>away from the normal</b>.</p>"
            "<table class='tbl'><tr><th>On entering glass from air</th><th>Speed</th><th>Wavelength</th><th>Frequency</th></tr>"
            "<tr><td>light</td><td><b>decreases</b></td><td><b>decreases</b></td><td><b>stays the same</b></td></tr></table>"
            "<p>The frequency cannot change — it is set by the source. Since $v = f \\lambda$ and $f$ is fixed, the wavelength changes in proportion to the speed.</p>"
            "<p>Sound is the other way round: it travels <i>faster</i> in water than in air, so it bends <i>away</i> from the normal going in. The June 2023 scheme gave 3 marks for \"refraction is caused by a change in speed; sound speeds up entering water; light slows down entering water\".</p>",
        ),
        worked(
            "Explain the bend",
            "A ray of light enters a glass block at an angle. Explain why the ray changes direction. (2 marks)",
            [
                "<b>Cause:</b> light travels <b>more slowly in glass</b> than in air — the speed changes at the boundary.",
                "<b>Effect:</b> the side of the wavefront that enters first slows first, so the direction changes: the ray bends <b>towards the normal</b>. (Mentioning the wavelength getting shorter is extra; \"the glass is denser\" on its own is not an explanation.)",
            ],
        ),
        practice("Refraction", [
            choice("le-n2-q1", "A ray enters a glass block along the normal. What happens to it?",
                   ["It bends towards the normal", "It bends away from the normal", "It does not change direction (but it slows down)", "It is totally internally reflected"], 2,
                   "With the angle of incidence 0° there is no bending; the speed still drops."),
            written("le-n2-q2", "A ray of light passes from air into water at an angle. State what happens to its speed, its wavelength and its frequency. (3)",
                    marks(["Speed <b>decreases</b>.", "Wavelength <b>decreases</b>.", "Frequency <b>stays the same</b>."]), lines=3),
            written("le-n2-q3", "Explain why light bends when it passes from air into glass at an angle. (2)",
                    marks(["The light <b>slows down</b> (changes speed) as it enters the glass.",
                           "So the direction changes — the ray bends <b>towards the normal</b> (the part of the wavefront that enters first slows first)."]), lines=3),
            choice("le-n2-q4", "A ray enters a rectangular glass block at an angle and leaves through the opposite face. The emergent ray is…",
                   ["parallel to the incident ray but shifted sideways", "along the normal", "bent towards the normal", "at a larger angle than the incident ray"], 0,
                   "The two bends cancel (towards the normal in, away from it out), so the ray leaves parallel to the way it came in, displaced sideways."),
            written("le-n2-q5", "A ray of light enters a glass block with an angle of incidence of 40°. State whether the angle of refraction is bigger or smaller than 40°, and why. (2)",
                    marks(["<b>Smaller</b> — the ray bends <b>towards the normal</b>…", "…because light <b>slows down</b> in the glass."]), lines=3),
            written("le-n2-q6", "Sound and light both travel from air into water. Explain why they refract in opposite directions. (3)",
                    marks(["Refraction is caused by a <b>change in speed</b> at the boundary.",
                           "<b>Light slows down</b> entering water, so it bends <b>towards</b> the normal.",
                           "<b>Sound speeds up</b> entering water, so it bends <b>away from</b> the normal."]), lines=4),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N3 · Total internal reflection
# ---------------------------------------------------------------------

section_n3 = section(
    "tir", "nn", "Total internal reflection and the critical angle", "5.1P",
    equations=[r"\text{critical angle: } r = 90^{\circ}", r"i > c \Rightarrow \text{TIR}"],
    blurb="A ray trying to leave glass into air bends away from the normal. At the <b>critical angle</b> the refracted ray runs along the surface; beyond it the ray cannot get out and is <b>totally internally reflected</b>.",
    tags=["P"],
    checklist=[
        "State what the critical angle is (the definition, not a formula)",
        "Describe what happens below, at and above the critical angle, with a diagram",
        "State the two conditions for total internal reflection",
    ],
    parts=[
        explain(
            "Three cases",
            diagram(dg.tir_svg(), 540, 265, "A ray inside glass meeting the glass–air surface at three angles of incidence: below the critical angle it refracts out (bending away from the normal); at the critical angle the refracted ray runs along the surface (angle of refraction 90°); above it there is total internal reflection.") +
            "<p><b>Definition:</b> the <b>critical angle</b> is the <b>angle of incidence</b> (in the denser material, e.g. glass) <b>for which the angle of refraction is 90°</b> — the refracted ray travels along the boundary. For glass it is about 42°.</p>"
            "<p><b>Total internal reflection</b> happens when both conditions are met: (1) the light is travelling from a <b>denser</b> material towards a <b>less dense</b> one (glass → air, water → air); (2) the <b>angle of incidence is greater than the critical angle</b>. Then no light leaves: <i>all</i> of it is reflected inside, obeying the law of reflection.</p>"
            "<p>You do not need a formula for the critical angle at GCSE — the definition, the diagram and the three cases are what the questions test (June 2025 Q7(c), 3 marks: \"what happens at the critical angle and beyond it\").</p>",
        ),
        worked(
            "Describe what happens as the angle grows",
            "A ray of light inside a glass block hits the glass–air surface. Describe what happens to the ray as the angle of incidence is increased from 20° to 60°. The critical angle of the glass is 42°. (3 marks)",
            [
                "<b>Below 42°:</b> the ray <b>refracts out</b> of the glass into the air, bending <b>away from the normal</b> (angle of refraction bigger than angle of incidence); a weak reflected ray stays inside.",
                "<b>At 42° (the critical angle):</b> the angle of refraction is <b>90°</b> — the refracted ray travels <b>along the surface</b>.",
                "<b>Above 42°:</b> no light leaves; the ray is <b>totally internally reflected</b> back into the glass, with angle of reflection = angle of incidence.",
            ],
        ),
        practice("TIR", [
            written("le-n3-q1", "State what is meant by the critical angle. (1)",
                    marks(["The <b>angle of incidence</b> (in the denser medium) at which the <b>angle of refraction is 90°</b> (the refracted ray travels along the surface)."]), lines=2),
            written("le-n3-q2", "State the two conditions needed for total internal reflection. (2)",
                    marks(["Light travelling from a <b>more dense to a less dense</b> material (e.g. glass to air).",
                           "The <b>angle of incidence is greater than the critical angle</b>."]), lines=3),
            choice("le-n3-q3", "The critical angle for glass is 42°. A ray inside the glass meets the surface at an angle of incidence of 50°. What happens?",
                   ["It refracts out, bending towards the normal", "It refracts out, bending away from the normal", "It runs along the surface", "It is totally internally reflected"], 3,
                   "50° is above the critical angle, so all the light reflects back into the glass."),
            choice("le-n3-q4", "A ray inside water (critical angle 49°) meets the surface at 30°. What happens?",
                   ["Total internal reflection", "It refracts out into the air, bending away from the normal", "It runs along the surface", "It stops"], 1,
                   "30° is below the critical angle, so the ray leaves the water (and a little is reflected)."),
            written("le-n3-q5", "A ray inside a glass block reaches the surface at exactly the critical angle. Describe the refracted ray. (1)",
                    marks(["It travels <b>along the surface</b> of the glass — the angle of refraction is <b>90°</b>."]), lines=2),
            written("le-n3-q6", "Explain how light travels along an optical fibre without escaping, even when the fibre bends. (3)",
                    mark_scheme([
                        ("Boundary", "The light travels inside the glass core and meets the glass–air (or glass–cladding) boundary — going from a <b>denser to a less dense</b> material."),
                        ("Angle", "It meets the boundary at an angle of incidence <b>greater than the critical angle</b>…"),
                        ("TIR", "…so it is <b>totally internally reflected</b> each time, zig-zagging along the fibre; gentle bends keep the angle above the critical angle."),
                    ]), lines=4),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N4 · Colour
# ---------------------------------------------------------------------

section_n4 = section(
    "colour", "nn", "Colour: absorption and filters", "5.3P",
    equations=[r"\text{reflects its own colour, absorbs the rest}", r"\text{filter: transmits its own colour, absorbs the rest}"],
    blurb="White light is all the colours together. An object's colour is the colour it <b>reflects</b>; everything else is <b>absorbed</b>. A filter's colour is the colour it <b>transmits</b>.",
    tags=["P"],
    checklist=[
        "Explain the colour of an opaque object in white light (reflects / absorbs)",
        "Explain what a coloured filter does (transmits / absorbs)",
        "Predict what colour an object appears in coloured light",
    ],
    parts=[
        explain(
            "Absorb, reflect, transmit",
            diagram(dg.colour_svg(), 480, 240, "A red object reflects red light and absorbs all the other colours. In blue light there is no red to reflect: it absorbs everything and looks black.") +
            "<p><b>Opaque objects:</b> a red jumper <b>reflects red</b> light and <b>absorbs</b> the other colours. A white object reflects all colours; a black object absorbs all colours. Each colour is a different <b>wavelength</b> (frequency) of light, and a surface absorbs some wavelengths more than others — <i>differential absorption</i>.</p>"
            "<p><b>Filters:</b> a red filter <b>transmits red</b> light and <b>absorbs</b> all the other colours. White light through a red filter comes out red; red light through a blue filter — nothing (black).</p>"
            "<p><b>Coloured light:</b> an object can only reflect colours that are shining on it. A red object in blue light looks <b>black</b>; a white object in blue light looks <b>blue</b>.</p>",
        ),
        worked(
            "A colour explanation",
            "A blue car is parked under a yellow sodium street lamp (which gives out only yellow light). Explain what colour the car appears. (2 marks)",
            [
                "<b>What the car does:</b> the car's paint <b>reflects blue</b> light and <b>absorbs</b> other colours.",
                "<b>What light is available:</b> the lamp gives out <b>only yellow</b>, which the paint <b>absorbs</b>; there is no blue to reflect, so the car appears <b>black</b> (very dark).",
            ],
        ),
        practice("Colour", [
            written("le-n4-q1", "Explain why a green leaf looks green in white light. (2)",
                    marks(["The leaf <b>reflects green</b> light…", "…and <b>absorbs</b> all the other colours (wavelengths) in white light."]), lines=3),
            choice("le-n4-q2", "White light passes through a green filter. What comes out?",
                   ["White light", "Green light only — the filter absorbs the other colours", "All colours except green", "No light"], 1,
                   "A filter transmits its own colour and absorbs the rest."),
            choice("le-n4-q3", "A red shirt is viewed in green light. What colour does it appear?",
                   ["Red", "Green", "Black", "Yellow"], 2,
                   "Red fabric reflects only red; there is no red in green light, so it absorbs the green and reflects nothing."),
            written("le-n4-q4", "Explain why a white sheet of paper looks red when viewed through a red filter. (2)",
                    marks(["The filter <b>transmits only red</b> light and <b>absorbs</b> the other colours.",
                           "The white paper <b>reflects all colours</b>, including the red that reaches it (or: only red light from the paper gets through the filter to your eye)."]), lines=3),
            written("le-n4-q5", "State what happens to the light that is not reflected by a coloured object. (1)",
                    marks(["It is <b>absorbed</b> (transferred to the thermal store of the object)."]), lines=2),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N5 · Lenses
# ---------------------------------------------------------------------

section_n5 = section(
    "lenses", "nn", "Lenses: converging, diverging and power", "5.4P",
    equations=[r"P = \dfrac{1}{f}", r"f \text{ in m, } P \text{ in dioptres (D)}"],
    blurb="A converging (convex) lens brings parallel rays to a focus; a diverging (concave) lens spreads them out. The <b>focal length</b> is the distance from the lens to the focus, and the <b>power</b> is 1 ÷ focal length: a fatter, more curved lens has a shorter focal length and a higher power.",
    tags=["P"],
    checklist=[
        "Describe what converging and diverging lenses do to parallel rays, and define focal length",
        "Relate the power of a lens to its focal length and its shape",
        "Use $P = 1/f$ with f in metres and the unit D",
    ],
    parts=[
        explain(
            "Shape, focal length, power",
            "<p>A <b>converging</b> lens is fatter in the middle (convex). Rays parallel to its axis are refracted so they <b>meet at the principal focus F</b>. The <b>focal length</b> $f$ is the distance from the centre of the lens to F.</p>"
            "<p>A <b>diverging</b> lens is thinner in the middle (concave). Parallel rays <b>spread out</b> as if they had come from a focus on the near side; its focal length is counted as <b>negative</b>.</p>"
            "<p>$$P = \\dfrac{1}{f}$$ with $f$ in <b>metres</b> and $P$ in <b>dioptres (D)</b>. A lens of focal length 0.5 m has power 2 D; one of focal length 0.1 m has power 10 D.</p>"
            "<p><b>Shape and power:</b> the <b>more curved</b> (fatter, thicker in the middle, smaller radius of curvature) the lens, the <b>more it refracts</b> the light, the <b>shorter the focal length</b> and the <b>higher the power</b>. The June 2025 scheme accepted \"more curved\", \"thicker\" or \"fatter\" for a higher-power lens; the 2022 report warns that \"stronger\" is too vague because it could mean either kind of lens.</p>",
        ),
        worked(
            "Comparing two lenses",
            "Lens A has a focal length of 10 cm and lens B a focal length of 40 cm. Compare their power and their shape. (2 marks)",
            [
                r"<b>Power:</b> $P_A = \dfrac{1}{0.10} = 10$ D; $P_B = \dfrac{1}{0.40} = 2.5$ D. Lens A is four times as powerful.",
                "<b>Shape:</b> lens A is <b>more curved</b> (fatter in the middle), so it refracts light more and brings it to a focus closer to the lens — the <b>shorter focal length</b> goes with the <b>higher power</b>.",
            ],
        ),
        practice("Lenses", [
            written("le-n5-q1", "State what is meant by the focal length of a converging lens. (1)",
                    marks(["The distance from the (centre of the) lens to the <b>principal focus</b> — the point where rays parallel to the axis are brought together."]), lines=2),
            choice("le-n5-q2", "Which lens has the highest power?",
                   ["Focal length 0.5 m", "Focal length 0.25 m", "Focal length 0.1 m", "Focal length 1 m"], 2,
                   "$P = 1/f$: the shortest focal length (0.1 m, 10 D) is the most powerful."),
            written("le-n5-q3", "Describe how the power of a lens depends on its focal length and its shape. (2)",
                    marks(["The <b>shorter the focal length</b>, the <b>higher the power</b> ($P = 1/f$).",
                           "A <b>more curved</b> (fatter, thicker-in-the-middle) lens has a shorter focal length and so a higher power."]), lines=3),
            choice("le-n5-q4", "What does a diverging lens do to a beam of parallel rays?",
                   ["Brings them to a focus on the far side", "Spreads them out as if they came from a focus on the near side", "Leaves them parallel", "Reflects them"], 1,
                   "Diverging lenses spread rays; the focus is virtual, on the same side as the incoming light."),
            numeric("le-n5-q5", "A converging lens has a focal length of 12.5 cm. Calculate its power.", 1 / 0.125, "D",
                    "Convert to metres first.",
                    ewau(r"P = \dfrac{1}{f}", r"P = \dfrac{1}{0.125}", "8", "D")),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N6 · EM waves
# ---------------------------------------------------------------------

q6_3 = C / 2.4e9
q6_4 = C / 600e-9

section_n6 = section(
    "em-waves", "nn", "Electromagnetic waves", "5.7, 5.8",
    equations=[r"\text{transverse}", r"c = 3 \times 10^{8}\ \text{m/s in a vacuum}", r"v = f \times \lambda"],
    blurb="Radio waves, light and gamma rays are all the same kind of wave: <b>transverse</b> electromagnetic waves that all travel at the <b>same speed in a vacuum</b> and <b>transfer energy</b> from the source to whatever absorbs them.",
    checklist=[
        "State the three facts: transverse, same speed in a vacuum (3 × 10⁸ m/s), transfer energy from source to observer",
        "Give an example of an EM wave transferring energy",
        "Use $v = f \\times \\lambda$ with $c = 3 \\times 10^8$ m/s and the right prefixes",
    ],
    parts=[
        explain(
            "Three facts and an equation",
            "<ul><li>All EM waves are <b>transverse</b>: the oscillations are at right angles to the direction the wave travels.</li>"
            "<li>All EM waves travel at the <b>same speed in a vacuum</b>, $3 \\times 10^{8}$ m/s (and almost the same in air). They slow down in glass and water — which is why they refract.</li>"
            "<li>All EM waves <b>transfer energy from the source to the observer</b> (the absorber). The Sun's infrared warms your skin; a microwave oven's microwaves heat the water in food; a radio wave makes a current flow in an aerial. No particles travel — the wave carries the energy.</li></ul>"
            "<p>$$v = f \\times \\lambda$$ For an EM wave the speed is already known, so the question is always for $f$ or $\\lambda$: $f = \\dfrac{v}{\\lambda}$ or $\\lambda = \\dfrac{v}{f}$. Convert GHz ($\\times 10^{9}$), MHz ($\\times 10^{6}$) and nm ($\\times 10^{-9}$) first — the 2022 report: not converting gigahertz to hertz was the common error.</p>"
            "<p>Don't confuse EM waves with sound: sound is a <b>longitudinal</b> wave that needs a medium and travels at about 340 m/s in air. \"Name an electromagnetic wave\" answered with \"sound\" scored nothing in June 2025.</p>",
        ),
        worked(
            "Wavelength of a radio wave",
            "A radio station transmits at 98 MHz. Calculate the wavelength of its waves. (speed = 3 × 10⁸ m/s)",
            [r"<b>Convert:</b> $f = 98\ \text{MHz} = 98 \times 10^{6} = 9.8 \times 10^{7}$ Hz."]
            + ewau(r"v = f \times \lambda \;\Rightarrow\; \lambda = \dfrac{v}{f}", r"\lambda = \dfrac{3 \times 10^{8}}{9.8 \times 10^{7}}", "3.06", "m"),
        ),
        practice("EM waves", [
            written("le-n6-q1", "State three properties that all electromagnetic waves have in common. (3)",
                    marks(["They are all <b>transverse</b> waves.", "They all travel at the <b>same speed in a vacuum</b> (3 × 10⁸ m/s).", "They all <b>transfer energy</b> from a source to an observer (absorber)."]), lines=3),
            choice("le-n6-q2", "Which of these is NOT an electromagnetic wave?",
                   ["Microwaves", "Ultrasound", "Ultraviolet", "Gamma rays"], 1,
                   "Ultrasound is a high-frequency sound wave — longitudinal, needs a medium, about 340 m/s in air."),
            numeric("le-n6-q3", "A microwave oven uses a frequency of 2.4 GHz. Calculate the wavelength of the microwaves. ($v = 3 \\times 10^8$ m/s)",
                    sf(q6_3, 3), "m", "2.4 GHz = 2.4 × 10⁹ Hz; $\\lambda = v \\div f$.",
                    ewau(r"\lambda = \dfrac{v}{f}", r"\lambda = \dfrac{3 \times 10^{8}}{2.4 \times 10^{9}}", "0.125", "m")),
            numeric("le-n6-q4", "Orange light has a wavelength of 600 nm. Calculate its frequency. ($v = 3 \\times 10^8$ m/s)",
                    sf(q6_4, 2), "Hz", "600 nm = 6.0 × 10⁻⁷ m; type the answer as 5e14.",
                    ewau(r"f = \dfrac{v}{\lambda}", r"f = \dfrac{3 \times 10^{8}}{6.0 \times 10^{-7}}", "5.0 \\times 10^{14}", "Hz")),
            written("le-n6-q5", "Give an example that shows an electromagnetic wave transfers energy from a source to an observer. (2)",
                    marks(["Example with the wave named: e.g. <b>infrared</b> from the Sun (source)…",
                           "…is absorbed by your skin (observer), which <b>warms up</b> (energy transferred to its thermal store). Other examples: microwaves heating water in food; light making a solar cell produce a current; radio waves inducing a current in an aerial."]), lines=3),
            choice("le-n6-q6", "Light passes from air into glass. Which statement is correct?",
                   ["Its speed and frequency both decrease", "Its speed decreases, its wavelength decreases, its frequency stays the same", "Nothing changes", "Its speed increases"], 1,
                   "Frequency is fixed by the source; $v = f\\lambda$, so wavelength falls with speed."),
        ]),
    ],
)

SECTIONS = [section_n1, section_n2, section_n3, section_n4, section_n5, section_n6]
