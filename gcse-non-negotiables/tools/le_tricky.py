"""
le_tricky.py — Topic 5 (Light and the EM spectrum): the tricky bits T1–T10
and the flashcards.

T1 Ray diagrams and the refraction practical   T6 Thermal balance (H, P)
T2 Explaining refraction                       T7 The radiation practical (P)
T3 TIR the hard way: finding the critical angle  T8 Radio waves and atoms
T4 Lens ray diagrams and images (P)            T9 EM calculations the hard way
T5 Absorb, transmit, reflect by wavelength (H)  T10 Apply the seven steps
"""

from math import asin, degrees, radians, sin

from revlib import (
    axis, choice, data, diagram, ewau, explain, fact, graph, group, label,
    mark_scheme, marks, numeric, practice, section, sf, worked, written,
)
import le_diagrams as dg

C = 3.0e8
N_GLASS = 1.5

# ---------------------------------------------------------------------
# T1 · Ray diagrams and the refraction core practical
# ---------------------------------------------------------------------

# air → glass data for the i–r graph (n = 1.5)
ir_in = [[i, round(degrees(asin(sin(radians(i)) / N_GLASS)), 1)] for i in (0, 10, 20, 30, 40, 50, 60, 70)]
graph_ir_in = graph(
    axis("angle of incidence i in °", 80, 10), axis("angle of refraction r in °", 50, 10),
    [data(ir_in)],
    "Angle of refraction plotted against angle of incidence for light entering a glass block: a curve through the origin that gets less steep; r is always smaller than i.",
)

section_t1 = section(
    "ray-practical", "tricky", "Ray diagrams that score, and the refraction practical", "5.9, 5.1P",
    equations=[r"\text{normal first, angles from it, arrows on rays}"],
    blurb="The marks for a ray diagram are for the normal, the angles marked from it and the arrows — not for a pretty drawing. The core practical is the same diagram done with a ray box and a protractor.",
    checklist=[
        "Draw a ray diagram with the normal at each surface, angles marked from it and arrows on the rays",
        "Describe the method for investigating how the angle of refraction depends on the angle of incidence",
        "Describe the pattern in the i–r results (r < i entering glass; not proportional)",
    ],
    parts=[
        explain(
            "The rules for a ray diagram",
            "<ol><li>Draw the <b>normal</b> first: a dashed line at <b>90° to the surface</b> at the point where the ray hits (use a protractor or set square).</li>"
            "<li>Mark the <b>angle of incidence</b> between the incident ray and the normal, and the <b>angle of refraction</b> (or reflection) between the outgoing ray and the normal. Never measure from the surface.</li>"
            "<li>Put an <b>arrow</b> on every ray showing which way the light travels; rays are <b>straight</b> lines, drawn with a ruler.</li>"
            "<li>At a glass surface: towards the normal going in, away from the normal coming out; emergent ray parallel to the incident ray.</li></ol>"
            "<p>The June 2024 scheme for the reflection practical gave a mark for each of: marking the positions, drawing the normal perpendicular to the surface, labelling the angles from the normal, using a protractor. \"Angle of refraction\" written on a reflection diagram was rejected.</p>",
        ),
        explain(
            "The core practical: i against r in a glass block",
            "<p><b>Method</b> (what a 4-mark \"describe how\" answer needs — June 2025 Q5(a) was marked on whether \"a well-structured procedure that, if followed, would result in the correct ray being drawn\"):</p>"
            "<ol><li>Place the <b>rectangular glass block</b> on a sheet of paper and <b>draw round it</b>.</li>"
            "<li>Use a <b>ray box</b> (with a single-slit) to shine a <b>narrow ray</b> into one face at an angle.</li>"
            "<li>Mark the <b>incident ray</b> with two crosses (or a line) and the <b>emergent ray</b> where it leaves the block with two more.</li>"
            "<li><b>Remove the block</b>, join the crosses to draw the rays, and join the entry and exit points to draw the <b>refracted ray inside</b> the block.</li>"
            "<li>Draw the <b>normal</b> at the entry point with a protractor (90° to the face); <b>measure the angle of incidence and the angle of refraction</b> from the normal.</li>"
            "<li><b>Repeat</b> for several angles of incidence (e.g. 10° to 70°), and repeat each reading; <b>plot</b> angle of refraction against angle of incidence.</li></ol>"
            "<p>Draw a <b>labelled diagram</b> as part of the answer — the examiners say so every year.</p>"
            "<p><b>Results:</b> r is always <b>smaller</b> than i (the ray bends towards the normal); the graph is a <b>curve</b> through the origin that gets less steep — r is <i>not</i> proportional to i. A ray along the normal (i = 0) does not bend. The emergent ray is parallel to the incident ray.</p>",
            graph=graph_ir_in,
        ),
        worked(
            "Describing the method",
            "Describe how a student could use a ray box and a rectangular glass block to investigate how the angle of refraction depends on the angle of incidence. (4 marks)",
            [
                "<b>Set up:</b> put the block on paper, draw round it; shine a single narrow ray from the ray box into one face at an angle.",
                "<b>Record the rays:</b> mark the incident ray and the emergent ray with crosses; remove the block; join the crosses, and join entry point to exit point for the ray inside the glass.",
                "<b>Measure:</b> draw the normal at the entry point with a protractor; measure the angle of incidence and the angle of refraction from the normal.",
                "<b>Vary and plot:</b> repeat for at least five angles of incidence (repeat readings, average), and plot r against i.",
            ],
        ),
        practice("Diagrams and the practical", [
            written("le-t1-q1", "A student draws a ray diagram for light entering a glass block but measures the angles from the surface of the block. Explain what is wrong. (1)",
                    marks(["Angles of incidence and refraction are measured <b>from the normal</b> (the line at 90° to the surface), not from the surface."]), lines=2),
            written("le-t1-q2", "Describe how to find the path of a ray of light inside a glass block, given that you cannot see the ray inside the glass. (2)",
                    marks(["Mark where the ray <b>enters</b> the block and where it <b>leaves</b> (crosses on the incident and emergent rays, and the block's outline).",
                           "<b>Remove the block</b> and join the entry point to the exit point with a ruler — the straight line is the refracted ray."]), lines=3),
            choice("le-t1-q3", "A student plots angle of refraction against angle of incidence for light entering glass. Which describes the graph?",
                   ["A straight line through the origin: r is proportional to i", "A curve through the origin that gets less steep; r is always less than i", "A horizontal line", "A straight line with r greater than i"], 1,
                   "The ray bends towards the normal (r < i) and the relationship is not linear — the sine of the angles is."),
            written("le-t1-q4", "State two things the student should do to make the results of the refraction practical more accurate. (2)",
                    marks(["Use a <b>narrow</b> ray (single slit) and mark its position with crosses <b>far apart</b>, so the line through them is accurate; <b>draw the normal carefully</b> with a protractor / set square.",
                           "<b>Repeat</b> each angle and take a <b>mean</b>; work in a darkened room so the ray is clear."]), lines=3),
            choice("le-t1-q5", "Which piece of equipment is needed to measure the angle of refraction?",
                   ["A ruler", "A protractor", "A stopwatch", "A balance"], 1,
                   "Angles are measured with a protractor, from the normal."),
            written("le-t1-q6", "Describe how a student could show that the angle of incidence and the angle of refraction are not proportional. (2)",
                    marks(["Measure r for several values of i and <b>plot a graph</b> of r against i.",
                           "Proportional would give a <b>straight line through the origin</b>; the points lie on a <b>curve</b> (or i ÷ r is not constant), so they are not proportional."]), lines=3),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T2 · Explaining refraction
# ---------------------------------------------------------------------

section_t2 = section(
    "refraction-explain", "tricky", "Explaining refraction: speed, wavelength, frequency", "5.14",
    equations=[r"v \downarrow,\ \lambda \downarrow,\ f \text{ same}", r"\text{bend towards the normal when slowing}"],
    blurb="The explanation marks are for the <b>speed change</b> and what it does to the wavefront. Say which way the speed changes, which way the ray bends, and that the frequency does not change.",
    checklist=[
        "Explain refraction in terms of a change of speed at the boundary",
        "State which way light and sound refract going into water, and why they differ",
        "Explain why the wavelength changes but the frequency does not",
    ],
    parts=[
        explain(
            "The wavefront picture",
            "<p>Think of the wave as a line of marching soldiers hitting a boundary at an angle: the soldiers that reach the slow ground first slow down first, so the line <b>swings round</b> towards the normal. The ray — at right angles to the wavefronts — changes direction. That is refraction: it is <b>caused by the change of speed</b>, and it only changes the direction if the wave meets the boundary <b>at an angle</b>.</p>"
            "<table class='tbl'><tr><th>Wave entering water from air</th><th>Speed</th><th>Direction</th></tr>"
            "<tr><td>light</td><td>slows down</td><td>bends <b>towards</b> the normal</td></tr>"
            "<tr><td>sound</td><td>speeds up (about 1500 m/s in water, 340 m/s in air)</td><td>bends <b>away from</b> the normal</td></tr></table>"
            "<p><b>Frequency is fixed</b> by the source — the waves arrive at the boundary at a certain rate and leave it at the same rate; none can pile up or vanish. Since $v = f\\lambda$, if $v$ falls and $f$ is constant, $\\lambda$ falls in the same proportion: light's wavelength in glass is about two-thirds of its wavelength in air.</p>"
            "<p>What the examiners want written (June 2023 Q6(b), 3 marks): \"refraction is caused by a change in speed\"; the direction of the speed change for each wave; and nothing about transverse or longitudinal, which was ignored.</p>",
        ),
        worked(
            "A full explanation",
            "Explain why a ray of light bends towards the normal when it passes from air into glass, and state what happens to its wavelength and frequency. (4 marks)",
            [
                "<b>Speed:</b> light travels <b>more slowly in glass</b> than in air.",
                "<b>Direction:</b> the part of the wavefront that enters the glass first <b>slows down first</b>, so the wavefront turns and the ray bends <b>towards the normal</b>.",
                "<b>Frequency:</b> the frequency is <b>unchanged</b> — it is set by the source.",
                "<b>Wavelength:</b> because $v = f\\lambda$ and $v$ falls with $f$ constant, the wavelength <b>decreases</b>.",
            ],
        ),
        practice("Explaining refraction", [
            written("le-t2-q1", "Explain why a wave does not change direction when it crosses a boundary along the normal, even though it changes speed. (2)",
                    marks(["The whole wavefront reaches the boundary <b>at the same time</b>, so every part slows down (or speeds up) <b>together</b>.",
                           "There is no difference in speed along the wavefront to turn it, so the direction is unchanged — only the speed and wavelength change."]), lines=3),
            written("le-t2-q2", "Light passes from glass into air. State what happens to its speed, wavelength, frequency and direction. (4)",
                    mark_scheme([
                        ("Speed", "<b>Increases</b>."),
                        ("Wavelength", "<b>Increases</b>."),
                        ("Frequency", "<b>Unchanged</b>."),
                        ("Direction", "Bends <b>away from the normal</b> (if it meets the surface at an angle)."),
                    ]), lines=4),
            choice("le-t2-q3", "Why does the frequency of light not change when it enters glass?",
                   ["Glass has no effect on light", "The frequency is set by the source: waves leave the boundary at the same rate they arrive", "The speed does not change", "The wavelength does not change"], 1,
                   "Waves cannot pile up at a boundary; the rate in equals the rate out."),
            written("le-t2-q4", "A stick in a pond looks bent at the water surface. Explain why, in terms of refraction. (2)",
                    marks(["Light from the submerged part of the stick <b>speeds up</b> as it leaves the water and <b>bends away from the normal</b> at the surface.",
                           "The eye assumes the light travelled in a straight line, so the underwater part appears <b>higher / in a different position</b> than it is — the stick looks bent at the surface."]), lines=3),
            written("le-t2-q5", "Water waves slow down as they move from deep water into shallow water. State what happens to their wavelength and their frequency. (2)",
                    marks(["Wavelength <b>decreases</b> (the waves bunch up).", "Frequency <b>stays the same</b>."]), lines=2),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T3 · TIR the hard way: finding the critical angle
# ---------------------------------------------------------------------

critical = degrees(asin(1 / N_GLASS))
ir_out = [[i, round(degrees(asin(N_GLASS * sin(radians(i)))), 1)] for i in (0, 10, 20, 30, 35, 38, 40)]
graph_ir_out = graph(
    axis("angle of incidence in the glass i in °", 50, 10), axis("angle of refraction in the air r in °", 90, 10),
    [data(ir_out)],
    "Angle of refraction in air against angle of incidence in glass for light leaving a glass block: r is bigger than i and the curve steepens sharply towards r = 90°.",
)

section_t3 = section(
    "tir-hard", "tricky", "Finding the critical angle: method and graph", "5.1P, 5.9",
    equations=[r"\text{increase } i \text{ until } r = 90^{\circ}", r"\text{from a graph: read } i \text{ where } r = 90^{\circ}"],
    blurb="Two ways the exam asks for the critical angle: describe the experiment that finds it, or read it off an i–r graph by extending the curve to r = 90°. No formula needed.",
    tags=["P"],
    checklist=[
        "Describe how to find the critical angle with a semicircular glass block",
        "Find the critical angle from a graph of angle of refraction against angle of incidence",
        "Explain how optical fibres (and endoscopes) use total internal reflection",
    ],
    parts=[
        explain(
            "The method with a semicircular block",
            "<p>Use a <b>semicircular</b> glass block, because a ray aimed at the <b>centre of the flat face</b> enters through the curved face <b>along a normal</b> and so does not bend on the way in — all the refraction happens at the flat face.</p>"
            "<ol><li>Put the block on paper, draw round it and mark the <b>centre of the flat face</b>.</li>"
            "<li>Shine a narrow ray through the curved face <b>towards that centre</b>; mark the ray and the refracted ray that leaves the flat face.</li>"
            "<li><b>Increase the angle of incidence</b> in the glass (rotate the block or move the ray box) and watch the refracted ray bend further from the normal.</li>"
            "<li>Stop when the refracted ray <b>just runs along the flat surface</b> — the angle of refraction is <b>90°</b> (equivalently: when total internal reflection <b>just begins</b>).</li>"
            "<li><b>Measure the angle of incidence</b> from the normal with a protractor: that is the <b>critical angle</b>. Repeat and average.</li></ol>"
            "<p>These are exactly the June 2024 Q6(b)(ii) marks: increase the angle of incidence in the glass; until the refracted angle is 90° / the ray grazes the surface / TIR just begins; that angle of incidence is the critical angle; repeat and average.</p>",
        ),
        explain(
            "From a graph",
            "<p>A question may give angles of refraction (in air) for a ray <b>leaving</b> glass at several angles of incidence (in glass) and ask for the critical angle. The refracted angle is bigger than the incident angle and the curve steepens; it reaches <b>r = 90°</b> at the critical angle.</p>"
            "<p>The method the June 2023 scheme gave three marks for: <b>(1) extend (extrapolate) the curve</b> smoothly, <b>(2) until r = 90°</b>, <b>(3) read off the corresponding value of i</b> — drop a line to the i-axis and label it. For the data below the curve reaches 90° at about 42°.</p>",
            graph=graph_ir_out,
        ),
        worked(
            "Reading the critical angle",
            "Use the graph above to find the critical angle of the glass. (3 marks)",
            [
                "<b>Extend the curve</b> smoothly beyond the last point, following its steepening shape.",
                "<b>Find where it reaches r = 90°</b> — the top of the graph.",
                "<b>Read down to the i-axis:</b> about <b>42°</b>. Mark it on the graph: the examiner credits the construction lines.",
            ],
        ),
        practice("Critical angle", [
            numeric("le-t3-q1", "Use the graph to estimate the critical angle of the glass. (Extend the curve to r = 90° and read i.)", round(critical), "°",
                    "The curve climbs steeply after 38°; it reaches 90° just above 41°.",
                    [r"Extrapolating the curve to $r = 90^{\circ}$ gives $i \approx 42^{\circ}$ (anything from 40° to 44° is a reasonable reading)."], graph=graph_ir_out, tolerance=0.06),
            written("le-t3-q2", "Describe how a student could find the critical angle of a semicircular glass block using a ray box. (3)",
                    mark_scheme([
                        ("Aim", "Shine a ray through the curved face <b>towards the centre of the flat face</b> (so it does not bend on entry)."),
                        ("Increase", "<b>Increase the angle of incidence</b> (in the glass) until the refracted ray <b>runs along the flat surface</b> (r = 90°) / TIR just starts."),
                        ("Measure", "<b>Measure that angle of incidence</b> from the normal with a protractor — the critical angle; <b>repeat and average</b>."),
                    ]), lines=4),
            choice("le-t3-q3", "Why is a semicircular block used to find the critical angle rather than a rectangular one?",
                   ["It is cheaper", "A ray aimed at the centre of the flat face enters along a normal to the curved face, so it does not refract on the way in", "Semicircular glass has a bigger critical angle", "Rectangular blocks do not reflect"], 1,
                   "All the refraction then happens at one surface, the flat one, so the angle in the glass is the one you set."),
            written("le-t3-q4", "A graph of angle of refraction against angle of incidence is drawn for light leaving water. Describe how to use it to find the critical angle. (3)",
                    marks(["<b>Extend</b> (extrapolate) the curve…", "…to where the angle of refraction is <b>90°</b>…", "…and <b>read off the angle of incidence</b> at that point (drop a line to the i-axis)."]), lines=3),
            written("le-t3-q5", "An endoscope uses two bundles of optical fibres to look inside a patient. Explain how light travels along the fibres. (3)",
                    mark_scheme([
                        ("Boundary", "Light inside the glass fibre meets the glass–cladding (less dense) boundary…"),
                        ("Angle", "…at an angle of incidence <b>greater than the critical angle</b>…"),
                        ("TIR", "…so it is <b>totally internally reflected</b> again and again along the fibre; one bundle carries light in, the other carries the image out."),
                    ]), lines=4),
            choice("le-t3-q6", "For glass–air the critical angle is 42°; for water–air it is 49°. A ray in glass and a ray in water both meet the surface at 45°. What happens?",
                   ["Both refract out", "Both are totally internally reflected", "The ray in glass is totally internally reflected; the ray in water refracts out", "The ray in water is totally internally reflected; the ray in glass refracts out"], 2,
                   "45° is above glass's 42° (TIR) but below water's 49° (refracts out)."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T4 · Lens ray diagrams and images
# ---------------------------------------------------------------------

LENS_RULES = (
    "<ol><li>A ray <b>parallel to the axis</b> refracts through the <b>principal focus F</b> on the far side (converging) — or away from the lens as if from F on the near side (diverging).</li>"
    "<li>A ray through the <b>centre</b> of the lens goes <b>straight on</b> undeviated.</li>"
    "<li>(Converging only) a ray through F on the near side leaves <b>parallel</b> to the axis.</li></ol>"
    "<p>Where the two rays from the top of the object <b>cross</b>, the top of the image is. If they only cross when traced <b>backwards</b> (dashed), the image is <b>virtual</b>.</p>"
)

IMAGES_TABLE = (
    "<table class='tbl'><tr><th>Lens and object position</th><th>Image</th><th>Where</th><th>Used in</th></tr>"
    "<tr><td>Converging, object <b>beyond 2F</b></td><td>real, inverted, <b>smaller</b></td><td>between F and 2F on the far side</td><td>camera, eye</td></tr>"
    "<tr><td>Converging, object <b>at 2F</b></td><td>real, inverted, same size</td><td>at 2F on the far side</td><td>—</td></tr>"
    "<tr><td>Converging, object <b>between F and 2F</b></td><td>real, inverted, <b>magnified</b></td><td>beyond 2F on the far side</td><td>projector</td></tr>"
    "<tr><td>Converging, object <b>inside F</b></td><td><b>virtual</b>, upright, <b>magnified</b></td><td>same side as the object, further away</td><td>magnifying glass</td></tr>"
    "<tr><td>Diverging, any position</td><td><b>virtual</b>, upright, <b>smaller</b></td><td>same side as the object, nearer the lens</td><td>spectacles for short sight</td></tr></table>"
)

section_t4 = section(
    "lens-diagrams", "tricky", "Lens ray diagrams: real and virtual images", "5.5P, 5.6P",
    equations=[r"\text{magnification} = \dfrac{\text{image height}}{\text{object height}}", r"\text{real: can be projected; virtual: cannot}"],
    blurb="Two rays from the top of the object fix the image. Where they really cross, the image is real (projectable, inverted); where they only appear to come from, it is virtual (upright, cannot be put on a screen).",
    tags=["P"],
    checklist=[
        "Draw the ray diagram for a converging lens with the object beyond 2F, between F and 2F, and inside F",
        "Draw the ray diagram for a diverging lens",
        "Describe each image (real/virtual, upright/inverted, magnified/diminished) and give an example of a real and a virtual image",
        "Use magnification = image height ÷ object height, measured on the same scale",
    ],
    parts=[
        explain(
            "The three rules and the four cases",
            LENS_RULES +
            diagram(dg.converging_lens_svg(200, 70, "Converging lens, object beyond 2F"), 500, 300, "Object beyond 2F: the rays cross on the far side between F and 2F. The image is real, inverted and smaller — a camera.") +
            diagram(dg.converging_lens_svg(105, 70, "Converging lens, object between F and 2F"), 500, 300, "Object between F and 2F: the rays cross beyond 2F. The image is real, inverted and magnified — a projector.") +
            diagram(dg.converging_lens_svg(40, 70, "Converging lens, object inside F (magnifying glass)"), 500, 300, "Object inside F: the rays leave the lens spreading apart and only cross when traced back (dashed). The image is virtual, upright and magnified, on the same side as the object — a magnifying glass.") +
            diagram(dg.diverging_lens_svg(), 500, 300, "Diverging lens: the parallel ray spreads out as if from the near F. The rays never cross; traced back they give a virtual, upright, smaller image on the object's side.") +
            IMAGES_TABLE,
        ),
        explain(
            "Real or virtual — how to tell, and how to say it",
            "<p>A <b>real</b> image is where rays <b>actually meet</b>: it can be <b>projected onto a screen</b> and (for a single lens) it is <b>inverted</b> and on the <b>opposite side</b> of the lens from the object. A <b>virtual</b> image is where rays <b>appear to come from</b>: it <b>cannot be projected</b>, it is <b>upright</b>, and it is on the <b>same side</b> as the object.</p>"
            "<p>June 2024 Q6(c) gave the mark for any one of: cannot be projected onto a screen; the rays do not actually pass through it; formed where imaginary (traced-back) rays meet; same side as the object; upright. \"Not real\" on its own scored nothing. June 2025 Q7(b) asked for an example of each and was \"answered poorly\": real — the image on a camera sensor, on a cinema screen, on the retina; virtual — a magnifying glass, a plane mirror, spectacles.</p>"
            "<p><b>Magnification</b> $= \\dfrac{\\text{image height}}{\\text{object height}}$ (no unit). This one is not on the equation list — a question that needs it gives it. Measure both <b>on the same scale</b>, with your eye directly above the ruler — the 2022 report's two warnings. To <b>increase</b> the magnification of a magnifying glass: use a <b>fatter / more curved / shorter-focal-length</b> lens, or move the object (further from the lens, but still inside F).</p>",
        ),
        worked(
            "Describing an image",
            "An object is placed 5 cm from a converging lens of focal length 10 cm. Describe the image and name a device that uses the lens this way. (3 marks)",
            [
                "<b>Position:</b> the object is <b>inside F</b> (5 cm is less than the 10 cm focal length).",
                "<b>Image:</b> the rays leaving the lens diverge, so the image is <b>virtual</b>, <b>upright</b> and <b>magnified</b>, on the same side of the lens as the object.",
                "<b>Device:</b> a <b>magnifying glass</b>.",
            ],
        ),
        practice("Lens images", [
            choice("le-t4-q1", "An object is placed beyond 2F of a converging lens. The image is…",
                   ["real, inverted and smaller", "virtual, upright and magnified", "real, upright and magnified", "virtual, inverted and smaller"], 0,
                   "Beyond 2F: camera arrangement — real, inverted, diminished, between F and 2F on the far side."),
            written("le-t4-q2", "Explain how you can tell from a ray diagram that an image is virtual. (1)",
                    marks(["The rays <b>do not actually meet</b>: the image is where the rays <b>appear to come from</b> when traced backwards (dashed lines) — it <b>cannot be projected onto a screen</b>."]), lines=2),
            written("le-t4-q3", "Give one example of a real image and one example of a virtual image. (2)",
                    marks(["Real: the image on a <b>camera sensor</b> / <b>cinema screen</b> / the <b>retina</b> of the eye.",
                           "Virtual: the image in a <b>magnifying glass</b> / a <b>plane mirror</b> / through <b>spectacles</b>."]), lines=2),
            numeric("le-t4-q4", "In a ray diagram the object is 1.5 cm tall and the image is 3.9 cm tall. Calculate the magnification.", sf(3.9 / 1.5, 2), "",
                    "image height ÷ object height, same units.",
                    ewau(r"\text{magnification} = \dfrac{\text{image height}}{\text{object height}}", r"\text{magnification} = \dfrac{3.9}{1.5}", "2.6", "(no unit)")),
            written("le-t4-q5", "Describe two ways to increase the magnification produced by a magnifying glass. (2)",
                    marks(["Use a lens that is <b>more curved / fatter</b> (shorter focal length, higher power).",
                           "Change the <b>distance between the object and the lens</b> (move the object further from the lens, keeping it inside F). \"Stronger lens\" is too vague — say which way."]), lines=3),
            choice("le-t4-q6", "A diverging lens always produces an image that is…",
                   ["real and inverted", "virtual, upright and smaller than the object", "virtual and magnified", "real and magnified"], 1,
                   "Diverging lenses spread rays; the traced-back rays give a small upright virtual image."),
            written("le-t4-q7", "Describe how to draw the ray diagram for an object placed between F and 2F of a converging lens, and describe the image. (4)",
                    mark_scheme([
                        ("Ray 1", "From the top of the object, a ray <b>parallel to the axis</b>, refracted through <b>F on the far side</b>."),
                        ("Ray 2", "From the top of the object, a ray <b>through the centre</b> of the lens, straight on."),
                        ("Image", "The image is where the two rays <b>cross</b>, beyond 2F on the far side; draw it from the axis to the crossing point."),
                        ("Describe", "<b>Real, inverted, magnified</b> (as in a projector)."),
                    ]), lines=5),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T5 · Absorb, transmit, refract, reflect — by wavelength (H)
# ---------------------------------------------------------------------

section_t5 = section(
    "absorb-transmit", "tricky", "Absorb, transmit, refract or reflect: it depends on the wavelength", "5.13",
    equations=[r"\text{same material, different wavelengths, different behaviour}"],
    blurb="Whether a substance absorbs, transmits, refracts or reflects an electromagnetic wave depends on the wavelength. Glass is transparent to visible light but absorbs most ultraviolet; the atmosphere lets radio and visible through but blocks X-rays. These explain colour, greenhouses, sunburn through windows and more.",
    tags=["H"],
    checklist=[
        "Give examples of a substance that transmits one wavelength and absorbs another",
        "Explain an everyday effect (greenhouse, sunburn, microwave oven door) using absorption and transmission by wavelength",
        "Apply it to colour: which wavelengths a surface reflects and which it absorbs",
    ],
    parts=[
        explain(
            "Examples that come up",
            "<table class='tbl'><tr><th>Substance</th><th>Transmits</th><th>Absorbs / reflects</th><th>Consequence</th></tr>"
            "<tr><td>Window glass</td><td>visible light</td><td>absorbs most ultraviolet; absorbs long-wavelength infrared</td><td>you do not get sunburnt through a window; a greenhouse traps infrared</td></tr>"
            "<tr><td>The atmosphere</td><td>visible, radio, some infrared and microwaves</td><td>absorbs UVC, X-rays, gamma (and some infrared — the greenhouse effect)</td><td>X-ray telescopes must be in space; UVC never reaches us</td></tr>"
            "<tr><td>Water (and food)</td><td>visible</td><td>absorbs microwaves strongly, absorbs infrared</td><td>microwave ovens heat the water in food</td></tr>"
            "<tr><td>Metal</td><td>—</td><td>reflects radio and microwaves; absorbs or reflects light</td><td>the metal mesh in the oven door keeps microwaves in but lets light out (its holes are much smaller than the microwaves' wavelength)</td></tr>"
            "<tr><td>Skin</td><td>—</td><td>absorbs UV in the surface layer; infrared at the surface; X-rays pass through soft tissue</td><td>sunburn is a surface effect; X-rays image bone</td></tr>"
            "<tr><td>A coloured surface</td><td>—</td><td>reflects its own colour's wavelengths, absorbs the rest</td><td>colour (5.3P)</td></tr></table>"
            "<p><b>Refraction varies with wavelength too:</b> violet light slows more in glass than red, so it bends more — a prism spreads white light into a spectrum, and a lens does not bring every colour to exactly the same focus.</p>",
        ),
        worked(
            "A greenhouse",
            "Explain how a glass greenhouse stays warmer than the air outside. (3 marks)",
            [
                "<b>In:</b> glass <b>transmits</b> the Sun's <b>visible light</b> and short-wavelength infrared, which are <b>absorbed</b> by the soil and plants, warming them.",
                "<b>Re-emission:</b> the warm surfaces <b>emit infrared</b> of a <b>longer wavelength</b> (because they are much cooler than the Sun).",
                "<b>Trapped:</b> glass <b>absorbs</b> (does not transmit) this longer-wavelength infrared, so the energy is kept inside and the temperature rises.",
            ],
        ),
        practice("Absorb and transmit", [
            written("le-t5-q1", "Explain why you can see through a car window but do not get sunburnt through it. (2)",
                    marks(["Glass <b>transmits visible light</b>, so you can see through it…", "…but <b>absorbs most ultraviolet</b>, which is the radiation that causes sunburn."]), lines=3),
            written("le-t5-q2", "Explain why the door of a microwave oven has a metal mesh with small holes. (2)",
                    marks(["Metal <b>reflects microwaves</b>: the holes are much <b>smaller than the microwaves' wavelength</b> (about 12 cm), so the mesh keeps them inside the oven.",
                           "<b>Visible light</b> has a wavelength far smaller than the holes, so it is <b>transmitted</b> and you can see the food."]), lines=3),
            choice("le-t5-q3", "Why are X-ray telescopes placed on satellites?",
                   ["X-rays travel faster in space", "The atmosphere absorbs X-rays, so none reach a telescope on the ground", "Satellites are closer to the stars", "X-rays are reflected by the ground"], 1,
                   "The atmosphere transmits visible and radio but absorbs X-rays, gamma and UVC."),
            written("le-t5-q4", "A substance absorbs red light but transmits blue light. Describe what you would see looking through it at a white lamp, and explain. (2)",
                    marks(["The lamp would look <b>blue</b>.", "The white light contains all colours; the red is <b>absorbed</b> and the blue is <b>transmitted</b> to your eye (green and the rest depend on the substance — a blue filter absorbs those too)."]), lines=3),
            written("le-t5-q5", "A prism splits white light into a spectrum. Explain why. (2)",
                    marks(["The different colours (wavelengths) travel at <b>slightly different speeds</b> in the glass…",
                           "…so they are <b>refracted by different amounts</b> — violet slows most and bends most, red least — and spread out."]), lines=3),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T6 · Thermal balance and the Earth (H, P)
# ---------------------------------------------------------------------

section_t6 = section(
    "thermal-balance", "tricky", "Radiate what you absorb: constant temperature and the Earth", "5.16P, 5.17P, 5.18P",
    equations=[r"\text{rate of emission} = \text{rate of absorption} \Rightarrow \text{constant temperature}"],
    blurb="A body's temperature is set by the balance between the power it absorbs and the power it radiates. The 4-mark version of this question has appeared twice in three years, and the word <b>rate</b> is compulsory.",
    tags=["H", "P"],
    checklist=[
        "Explain why a body stays at a constant temperature when it radiates the same average power that it absorbs",
        "Explain what happens when the power radiated is more or less than the power absorbed",
        "Explain the factors that control the Earth's temperature (incoming radiation, reflection, absorption and re-emission by the atmosphere)",
    ],
    parts=[
        explain(
            "The four marks, in order",
            "<p>Every body <b>absorbs</b> radiation from its surroundings and <b>emits</b> radiation because of its own temperature. The rate at which it emits <b>increases with its temperature</b>. So:</p>"
            "<ul><li>If it absorbs power <b>faster</b> than it emits, its temperature <b>rises</b> — and as it warms it emits more, until…</li>"
            "<li>…the <b>rate of emission equals the rate of absorption</b>: the temperature is then <b>constant</b> (thermal equilibrium).</li>"
            "<li>If it emits <b>faster</b> than it absorbs, its temperature <b>falls</b> until the two rates are equal again.</li></ul>"
            "<p>The June 2023 scheme (Q8(b)(ii), 4 marks) and the June 2025 report (Q7(d), the dwarf planet Ceres) credit the same four points: <b>(1)</b> the body absorbs radiation; <b>(2)</b> it also emits radiation; <b>(3)</b> the rate of emission increases with temperature; <b>(4)</b> the temperature is constant when the rate of emission equals the rate of absorption. The word <b>rate</b> must appear in (3) or (4); \"heat\" is accepted for radiation.</p>"
            "<p><b>The Earth</b> absorbs radiation from the Sun (mostly visible) and emits infrared to space; its average temperature is set by that balance. Factors: <b>clouds and ice reflect</b> some incoming radiation back to space (less absorbed → cooler); <b>greenhouse gases</b> (carbon dioxide, methane, water vapour) <b>absorb some of the outgoing infrared and re-emit it</b>, some back towards the surface (less escapes → warmer); more greenhouse gas moves the balance to a <b>higher</b> temperature.</p>",
        ),
        worked(
            "The equilibrium answer",
            "A black metal plate is placed in sunlight. Its temperature rises for a while and then stays constant. Explain why. (4 marks)",
            [
                "<b>(1)</b> The plate <b>absorbs</b> radiation from the Sun.",
                "<b>(2)</b> It also <b>emits</b> radiation (infrared) because of its temperature.",
                "<b>(3)</b> At first it absorbs faster than it emits, so it warms up; the <b>rate of emission increases as its temperature rises</b>.",
                "<b>(4)</b> The temperature stops rising when the <b>rate of emission equals the rate of absorption</b> — constant temperature.",
            ],
        ),
        practice("Thermal balance", [
            written("le-t6-q1", "Explain why the temperature of a planet with no atmosphere stays roughly constant. (4)",
                    mark_scheme([
                        ("Absorbs", "The planet <b>absorbs</b> radiation from its star."),
                        ("Emits", "It also <b>emits</b> radiation (infrared)."),
                        ("Rate", "The <b>rate of emission increases with temperature</b>."),
                        ("Balance", "Its temperature is constant because the <b>rate of emission equals the rate of absorption</b>."),
                    ]), lines=5, hint="Four points; the word rate must be in there."),
            choice("le-t6-q2", "A body radiates more power than it absorbs. What happens?",
                   ["Its temperature rises", "Its temperature falls until the rates are equal", "Its temperature stays the same", "It stops radiating"], 1,
                   "Net energy leaves, so it cools; cooling reduces its emission until balance is restored."),
            written("le-t6-q3", "Explain how an increase in carbon dioxide in the atmosphere can raise the Earth's average temperature. (3)",
                    mark_scheme([
                        ("Outgoing IR", "The Earth's surface <b>emits infrared</b> radiation towards space."),
                        ("Absorbed", "Carbon dioxide <b>absorbs</b> some of this infrared and <b>re-emits</b> it, some of it <b>back towards the surface</b>, so less escapes."),
                        ("New balance", "The Earth then emits less than it absorbs, so its temperature <b>rises</b> until the rate of emission to space again equals the rate of absorption — at a <b>higher</b> temperature."),
                    ]), lines=4),
            written("le-t6-q4", "Explain how an increase in cloud or ice cover could lower the Earth's temperature. (2)",
                    marks(["Clouds and ice <b>reflect</b> more of the incoming radiation from the Sun back into space.",
                           "So the Earth <b>absorbs less</b> power while still emitting; its temperature falls until the rate of emission equals the (lower) rate of absorption."]), lines=3),
            written("le-t6-q5", "A cup of coffee is left on a desk. Describe how the rates at which it absorbs and emits radiation compare, and what happens to its temperature. (2)",
                    marks(["It <b>emits more</b> radiation than it absorbs from the cooler room (emission rate rises with temperature).",
                           "So its temperature <b>falls</b>, and keeps falling until it emits at the same rate as it absorbs — room temperature."]), lines=3),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T7 · The radiation core practical (P)
# ---------------------------------------------------------------------

section_t7 = section(
    "radiation-practical", "tricky", "Core practical: how a surface affects radiation", "5.19P",
    equations=[r"\text{matt black: best emitter and best absorber}", r"\text{shiny silver: worst of both}"],
    blurb="Does the colour and finish of a surface change how much it radiates and how much it absorbs? Yes: matt black is best at both, shiny silver worst. Two experiments — a Leslie cube or painted cans of hot water for emission; cans in front of a heater for absorption.",
    tags=["P"],
    checklist=[
        "Describe the emission experiment (Leslie cube or painted cans of hot water) and its control variables",
        "Describe the absorption experiment (painted cans facing a heater or lamp)",
        "State and explain the results: matt black best emitter and absorber, shiny worst",
    ],
    parts=[
        explain(
            "Emission: which surface radiates most?",
            "<p><b>Leslie cube:</b> a hollow metal cube whose four faces are different — <b>matt black, shiny black, white, shiny silver</b>. Fill it with <b>hot water</b> and hold an <b>infrared detector</b> (or thermometer with a blackened bulb) the <b>same distance</b> from each face in turn; the detector reads highest for the <b>matt black</b> face and lowest for the <b>shiny silver</b> one.</p>"
            "<p><b>Painted cans:</b> the same with four identical cans painted different colours and finishes, each filled with the <b>same volume of water at the same starting temperature</b>; record the <b>temperature every minute</b> with a thermometer in each. The <b>matt black can cools fastest</b> (it emits most), the shiny silver can slowest.</p>"
            "<p><b>Controls:</b> same volume of water, same starting temperature, same can size, same distance from the detector, same time; a lid on each can so evaporation does not confuse the result. <b>Why hot water?</b> The hotter the surface, the more it radiates, so the differences are easier to measure.</p>",
        ),
        explain(
            "Absorption: which surface warms fastest?",
            "<p>Put the painted cans (with cold water, or metal plates with a thermometer attached) the <b>same distance</b> from a <b>radiant heater or lamp</b> and record the temperature every minute. The <b>matt black</b> can warms up fastest — it <b>absorbs</b> most of the radiation; the <b>shiny silver</b> can warms slowest — it <b>reflects</b> most.</p>"
            "<p><b>Results to learn:</b> matt black is the best <b>emitter</b> and the best <b>absorber</b>; shiny silver is the worst emitter and the worst absorber (the best reflector); white is a good reflector, poor absorber; matt surfaces beat shiny ones. A good absorber is always a good emitter.</p>"
            "<p>The June 2023 scheme (Q8(b)(i), 2 marks) accepted any one full comparison: \"black is a better absorber\", \"white is a better reflector\", \"black absorbs the radiation and white reflects it\".</p>",
        ),
        worked(
            "Explaining the result",
            "Two identical cans of hot water, one painted matt black and one shiny silver, are left to cool. Explain why the matt black can cools faster. (2 marks)",
            [
                "<b>Emission:</b> a <b>matt black surface is a better emitter</b> of infrared radiation than a shiny silver one (which is a poor emitter / good reflector).",
                "<b>So:</b> the black can transfers energy to the surroundings <b>at a greater rate</b>, its thermal store empties faster, and its temperature falls faster.",
            ],
        ),
        practice("Radiation practical", [
            written("le-t7-q1", "Describe how a student could use a Leslie cube to compare the infrared radiated by different surfaces. (3)",
                    mark_scheme([
                        ("Set up", "Fill the cube with <b>hot water</b> (the faces are matt black, shiny black, white and shiny silver)."),
                        ("Measure", "Hold an <b>infrared detector</b> (or thermometer) the <b>same distance</b> from each face in turn and record its reading."),
                        ("Compare / control", "Compare the readings; keep the distance, the time and the water temperature the same for each face; repeat."),
                    ]), lines=4),
            choice("le-t7-q2", "Which surface is the best emitter of infrared radiation?",
                   ["Shiny silver", "White", "Matt black", "Shiny black"], 2,
                   "Matt black emits (and absorbs) most; shiny silver least."),
            written("le-t7-q3", "Four cans painted differently are placed at the same distance from a heater. State two variables that must be kept the same and the measurement that should be made. (3)",
                    marks(["Same <b>volume of water</b> / same <b>starting temperature</b> / same <b>size of can</b> / same <b>distance</b> from the heater (any two).",
                           "Measure the <b>temperature</b> of the water in each can <b>at regular time intervals</b> (e.g. every minute) with a thermometer."]), lines=3),
            written("le-t7-q4", "Explain why the inside of a vacuum flask is silvered. (2)",
                    marks(["A shiny silver surface is a <b>poor emitter</b> of infrared, so the hot contents radiate less energy away…",
                           "…and a <b>good reflector</b>, so radiation from outside is reflected rather than absorbed — the drink stays hot (or cold) for longer."]), lines=3),
            written("le-t7-q5", "A student's results show the white can cooled faster than the shiny silver can. Explain whether this is expected. (2)",
                    marks(["<b>Yes</b>: white is a better emitter than shiny silver (shiny silver is the poorest emitter)…",
                           "…so the white can radiates energy away faster and cools faster; the order expected is matt black fastest, then white, then shiny silver slowest."]), lines=3),
            written("le-t7-q6", "Explain why black cars get hotter than white cars in the sun. (2)",
                    marks(["A black surface is a <b>good absorber</b> of radiation (and a poor reflector); a white surface <b>reflects</b> most of it.",
                           "So the black car's thermal store gains energy from sunlight at a greater rate and its temperature rises more."]), lines=3),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T8 · Radio waves and atoms
# ---------------------------------------------------------------------

section_t8 = section(
    "radio-atoms", "tricky", "Where the waves come from: circuits, atoms and nuclei", "5.23, 5.24",
    equations=[r"\text{radio: oscillating current in an aerial}", r"\text{visible / UV / X: electrons changing levels}", r"\text{gamma: the nucleus}"],
    blurb="Radio waves are made by oscillating currents and can make currents when absorbed; most other EM waves come from changes inside atoms, and gamma rays from the nucleus. \"Very few candidates knew\" the first part, says the 2022 report.",
    checklist=[
        "State that radio waves are produced by oscillations in electrical circuits and can induce oscillations (an alternating current) in a receiving aerial",
        "State that changes in atoms (electrons moving between energy levels) and nuclei generate radiation over a wide range of frequencies",
        "Explain fluorescence as absorption then re-emission at a longer wavelength",
    ],
    parts=[
        explain(
            "Producing and absorbing",
            "<p><b>Radio waves</b> are produced when an <b>alternating current</b> flows in an aerial: the <b>oscillating electrons</b> radiate waves of the <b>same frequency</b> as the current. When a radio wave is absorbed by a receiving aerial it does the reverse: it <b>induces an oscillating current</b> (an alternating voltage) of the same frequency, which the receiver amplifies. That is the 2022 Q9(c) Level-3 point: \"electron oscillation in circuits\" is the source of radio waves.</p>"
            "<p><b>Changes in atoms:</b> when an electron in an atom <b>drops to a lower energy level</b> it emits a wave whose frequency depends on the energy difference — visible light, ultraviolet, or X-rays for the big jumps in heavy atoms. Absorbing a wave does the opposite: it can <b>lift an electron to a higher level</b> (or, with enough energy, remove it — ionisation). <b>Gamma rays</b> come from changes in the <b>nucleus</b> (Topic 6).</p>"
            "<p><b>Fluorescence</b> (June 2024 Q5(b), 4 marks): <b>ultraviolet is absorbed</b> by electrons → they move to a <b>higher energy level</b> (become excited) → they <b>fall back</b> to a lower level, emitting energy → as <b>visible light</b> (a different, lower frequency than the UV absorbed). Security marks and fluorescent lamps use this.</p>",
        ),
        worked(
            "Compare how X-rays and radio waves are produced",
            "Compare X-rays and radio waves: their position in the spectrum, one use of each, and how each is produced. (6 marks, levelled)",
            [
                "<b>Position:</b> both are electromagnetic (transverse, same speed in a vacuum); X-rays have a much <b>higher frequency and shorter wavelength</b> than radio waves (the two ends of the spectrum).",
                "<b>Uses:</b> X-rays — medical imaging of bones, airport security; radio — broadcasting and communications.",
                "<b>Production:</b> X-rays come from <b>electrons changing energy levels</b> in atoms (or being stopped suddenly); radio waves come from <b>electrons oscillating in a circuit</b> (an alternating current in an aerial).",
                "The 2022 scheme: Level 1 compared uses only; Level 2 added frequency or wavelength; Level 3 also explained the production — the part \"very few candidates knew\".",
            ],
        ),
        practice("Sources of radiation", [
            written("le-t8-q1", "Describe how radio waves are produced by a transmitter and detected by a receiver. (2)",
                    marks(["An <b>alternating current</b> (oscillating electrons) in the transmitting aerial <b>produces</b> radio waves of the same frequency.",
                           "When the waves reach the receiving aerial they are absorbed and <b>induce an alternating current</b> (oscillation) of the same frequency in it."]), lines=3, tags=["H"]),
            written("le-t8-q2", "Explain how a fluorescent security mark on a bank note glows under ultraviolet light. (4)",
                    mark_scheme([
                        ("Absorb", "The <b>ultraviolet is absorbed</b> by electrons in the ink."),
                        ("Excite", "The electrons move to a <b>higher energy level</b> (become excited)."),
                        ("Fall", "They <b>fall back</b> to a lower level, emitting energy…"),
                        ("Visible", "…as <b>visible light</b> (lower frequency / longer wavelength than the UV) — fluorescence."),
                    ]), lines=5),
            choice("le-t8-q3", "Gamma rays are produced by…",
                   ["electrons oscillating in a wire", "changes in the nucleus of an atom", "electrons moving between energy levels", "hot surfaces"], 1,
                   "Gamma comes from the nucleus; electrons between levels give visible, UV and X-rays; oscillating currents give radio."),
            written("le-t8-q4", "State what happens in an atom when it emits visible light. (1)",
                    marks(["An <b>electron drops from a higher energy level to a lower one</b>, emitting the energy difference as a wave (photon) of visible light."]), lines=2),
            choice("le-t8-q5", "A radio wave of frequency 100 MHz is absorbed by an aerial. What does it produce in the aerial?",
                   ["A steady direct current", "An alternating current of frequency 100 MHz", "Heat only", "Light"], 1,
                   "The absorbed wave induces oscillations at the wave's own frequency.", tags=["H"]),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T9 · EM calculations the hard way
# ---------------------------------------------------------------------

q9_1 = 1.5e11 / C
q9_2_lo = C / 7.0e-7
q9_2_hi = C / 4.0e-7
q9_2 = q9_2_hi - q9_2_lo
q9_3 = C / 1.2e-2
q9_4 = 2.4e9 * 0.125
q9_5 = (C / 1.5e-7) * 1  # not used directly

section_t9 = section(
    "em-calc-hard", "tricky", "EM calculations the hard way", "5.7, 5.4P",
    equations=[r"v = f \lambda", r"t = \dfrac{d}{v}", r"P = \dfrac{1}{f}"],
    blurb="The same equation, with the units and the standard form turned up: nanometres, gigahertz, a range of frequencies, a time for light to travel, and powers of lenses from focal lengths in centimetres.",
    checklist=[
        "Handle nm, GHz, MHz and standard form in v = fλ",
        "Find a range of frequencies by subtracting two standard-form values",
        "Find the time for light to travel a distance (t = d ÷ v) in standard form",
        "Convert cm to m before P = 1/f, and give lens power with a sign",
    ],
    parts=[
        explain(
            "Standard form without losing marks",
            "<p>Use the <b>×10ˣ</b> key, never \"× 10 ^\": $3$ ×10ˣ $8$ ÷ $2.8$ ×10ˣ $(-)7$. Write the answer in standard form with the right number of significant figures ($1.07 \\times 10^{15}$ Hz), not as a string of zeros.</p>"
            "<p><b>Subtracting in standard form</b> (June 2025 Q5(b)(iii) — \"keeping control of the standard form and mixed units\"): write both numbers with the <b>same power of ten</b> first. $7.5 \\times 10^{14} - 4.3 \\times 10^{14} = 3.2 \\times 10^{14}$. If the powers differ, convert one: $7.5 \\times 10^{14} - 9.0 \\times 10^{13} = 7.5 \\times 10^{14} - 0.9 \\times 10^{14} = 6.6 \\times 10^{14}$.</p>"
            "<p><b>Time for light to travel:</b> $t = \\dfrac{d}{v}$ with $v = 3 \\times 10^{8}$ m/s and $d$ in metres (km × 1000). Sun to Earth, $1.5 \\times 10^{11}$ m: $t = 500$ s, about 8 minutes.</p>"
            "<p><b>Lens power:</b> 20 cm is 0.20 m; $P = 1/0.20 = 5$ D. A diverging lens has a negative focal length and so a negative power. Finish the calculation — the 2022 report: candidates stopped at $1/f$ without working out $f$.</p>",
        ),
        worked(
            "A frequency range",
            "Visible light has wavelengths from 400 nm to 700 nm. Calculate the range of frequencies of visible light. (v = 3 × 10⁸ m/s) (3 marks)",
            [
                r"<b>Convert:</b> $400\ \text{nm} = 4.0 \times 10^{-7}$ m; $700\ \text{nm} = 7.0 \times 10^{-7}$ m.",
                r"<b>Two frequencies:</b> $f = \dfrac{v}{\lambda}$: $\dfrac{3 \times 10^{8}}{4.0 \times 10^{-7}} = 7.5 \times 10^{14}$ Hz and $\dfrac{3 \times 10^{8}}{7.0 \times 10^{-7}} = 4.3 \times 10^{14}$ Hz.",
                r"<b>Range:</b> $7.5 \times 10^{14} - 4.3 \times 10^{14} = 3.2 \times 10^{14}$ Hz (same power of ten, then subtract).",
            ],
        ),
        practice("Hard calculations", [
            numeric("le-t9-q1", "The Sun is 1.5 × 10¹¹ m from the Earth. Calculate the time for light to reach the Earth. (v = 3 × 10⁸ m/s)", q9_1, "s",
                    "t = d ÷ v.",
                    ewau(r"t = \dfrac{d}{v}", r"t = \dfrac{1.5 \times 10^{11}}{3 \times 10^{8}}", "500", "s (about 8 minutes)")),
            numeric("le-t9-q2", "Visible light has wavelengths from 400 nm to 700 nm. Calculate the range of frequencies. Type the answer as 3.2e14. (v = 3 × 10⁸ m/s)", sf(q9_2, 2), "Hz",
                    "Two frequencies, same power of ten, subtract.",
                    [r"$f_{400} = \dfrac{3 \times 10^{8}}{4.0 \times 10^{-7}} = 7.5 \times 10^{14}$ Hz; $f_{700} = \dfrac{3 \times 10^{8}}{7.0 \times 10^{-7}} = 4.3 \times 10^{14}$ Hz.", r"Range $= 7.5 \times 10^{14} - 4.3 \times 10^{14} = 3.2 \times 10^{14}$ Hz."]),
            numeric("le-t9-q3", "A microwave link uses waves of wavelength 1.2 cm. Calculate their frequency in GHz. (v = 3 × 10⁸ m/s)", sf(q9_3 / 1e9, 2), "GHz",
                    "1.2 cm = 0.012 m; f = v ÷ λ in Hz, then ÷ 10⁹.",
                    [r"$f = \dfrac{3 \times 10^{8}}{0.012} = 2.5 \times 10^{10}$ Hz.", r"$2.5 \times 10^{10} \div 10^{9} = 25$ GHz."]),
            numeric("le-t9-q4", "Show that microwaves of frequency 2.4 GHz and wavelength 12.5 cm travel at about 3 × 10⁸ m/s: calculate v. Type the answer as 3e8.", q9_4, "m/s",
                    "v = f × λ with both in base units.",
                    ewau(r"v = f \times \lambda", r"v = 2.4 \times 10^{9} \times 0.125", "3.0 \\times 10^{8}", "m/s")),
            group("le-t9-q5", "A pair of spectacles has one converging lens of focal length 50 cm and one diverging lens of focal length −25 cm.", [
                numeric("le-t9-q5a", "Calculate the power of the converging lens.", 1 / 0.5, "D", "0.50 m.",
                        ewau(r"P = \dfrac{1}{f}", r"P = \dfrac{1}{0.50}", "2", "D"), label="a", tags=["P"]),
                numeric("le-t9-q5b", "Calculate the power of the diverging lens.", -1 / 0.25, "D", "Keep the sign; −0.25 m.",
                        ewau(r"P = \dfrac{1}{f}", r"P = \dfrac{1}{-0.25}", "-4", "D"), label="b", tags=["P"]),
            ], tags=["P"]),
            numeric("le-t9-q6", "A lens has a power of 12.5 D. Calculate its focal length in centimetres.", 100 / 12.5, "cm",
                    "f = 1 ÷ P in metres, then × 100. Finish the calculation.",
                    [r"$f = \dfrac{1}{P} = \dfrac{1}{12.5} = 0.08$ m.", r"$0.08 \times 100 = 8$ cm."], tags=["P"]),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T10 · Apply the seven steps
# ---------------------------------------------------------------------

section_t10 = section(
    "planning-light", "tricky", "Apply the seven steps: the two core practicals", "5.9, 5.19P",
    equations=[r"\text{7 steps: variables, equation, change, measure, use, accuracy, repeat + mean}"],
    blurb="The seven-step recipe from Topic 1 applied to the refraction practical (i against r, and the critical angle) and the radiation practical (surface against rate of cooling), as 6-mark method questions.",
    checklist=[
        "Write a full method for investigating how the angle of refraction depends on the angle of incidence",
        "Write a full method for investigating how the surface of a can affects how fast it cools",
        "Include the processing step: the graph or comparison that answers the question",
    ],
    parts=[
        explain(
            "The seven steps, applied here",
            "<p>From <a href='#key-concepts/planning-practical'>Topic 1, T6</a>: (1) the two variables; (2) the equation or relationship; (3) what you change and how, what you keep the same; (4) what you measure, how, with what; (5) what you do with the results; (6) one accuracy detail; (7) repeat <b>and calculate a mean</b>.</p>"
            "<table class='tbl'><tr><th>Step</th><th>Refraction: i against r</th><th>Radiation: surface against cooling</th></tr>"
            "<tr><td>1 Variables</td><td>angle of incidence (change); angle of refraction (measure)</td><td>surface finish (change); temperature drop in a set time (measure)</td></tr>"
            "<tr><td>2 Relationship</td><td>r increases with i, but not in proportion; r < i entering glass</td><td>better emitter → faster cooling</td></tr>"
            "<tr><td>3 Change</td><td>angle of incidence, by rotating the ray box / block; same block, same face</td><td>four cans: matt black, white, shiny silver, shiny black; same can size, volume, start temperature</td></tr>"
            "<tr><td>4 Measure</td><td>i and r from the normal with a protractor, after marking the rays with crosses</td><td>temperature every minute with a thermometer in each can</td></tr>"
            "<tr><td>5 Use</td><td>plot r against i; describe the curve</td><td>plot temperature against time; compare gradients / drops in 10 minutes</td></tr>"
            "<tr><td>6 Accuracy</td><td>narrow single-slit ray; crosses far apart; darkened room</td><td>lids on cans; same distance from heater and from each other; start readings at the same temperature</td></tr>"
            "<tr><td>7 Repeat</td><td>repeat each angle and average r</td><td>repeat the run and average the drops</td></tr></table>",
        ),
        worked(
            "The refraction practical in full",
            "Describe how a student could investigate how the angle of refraction of light entering a glass block depends on the angle of incidence. (6 marks)",
            [
                "<b>Step 1 — variables.</b> I will change the <b>angle of incidence</b> and measure the <b>angle of refraction</b>, using the same glass block throughout.",
                "<b>Step 2 — relationship.</b> I expect r to increase with i but to stay smaller than i, because light bends towards the normal as it slows in the glass.",
                "<b>Step 3 — change.</b> Put the block on paper and draw round it; aim a narrow ray from the ray box at one face and change the angle of incidence by rotating the ray box, from about 10° to 70° in 10° steps.",
                "<b>Step 4 — measure.</b> Mark the incident and emergent rays with crosses, remove the block, join the crosses and the entry–exit points; draw the normal at the entry point with a protractor and <b>measure i and r from the normal</b> with the protractor.",
                "<b>Step 5 — use the results.</b> Plot a graph of angle of refraction against angle of incidence and describe its shape.",
                "<b>Step 6 — accuracy.</b> Use a single narrow slit on the ray box and put the crosses far apart along each ray so the lines are accurate; work in a dim room.",
                "<b>Step 7 — repeat.</b> Repeat each angle three times <b>and calculate a mean</b> angle of refraction.",
            ],
        ),
        practice("Planning", [
            written("le-t10-q1", "Describe how a student could investigate how the surface of a container affects how quickly the water inside it cools. (6)",
                    mark_scheme([
                        ("Variables", "Change the <b>surface</b> (matt black, shiny silver, white…); measure the <b>temperature drop in a fixed time</b> (or time to drop a set amount)."),
                        ("Relationship", "Expect the better emitter (matt black) to cool fastest."),
                        ("Change", "Four identical cans painted differently, each with the <b>same volume of water at the same starting temperature</b>, same distance apart."),
                        ("Measure", "<b>Temperature</b> with a thermometer in each can <b>every minute</b> for 10 minutes."),
                        ("Use", "Plot <b>temperature against time</b> for each can and compare the gradients / total drops."),
                        ("Accuracy", "Lids on the cans (no evaporation); read the thermometer at eye level; start all cans at exactly the same temperature."),
                        ("Repeat", "<b>Repeat and calculate a mean</b> drop for each surface."),
                    ], total=6), lines=8, hint="Seven steps; any six score.", tags=["P"]),
            written("le-t10-q2", "Describe how a student could find the critical angle of a semicircular glass block. (6)",
                    mark_scheme([
                        ("Variables", "Change the <b>angle of incidence</b> in the glass; observe the <b>refracted ray</b> at the flat face; find the angle where it just disappears."),
                        ("Relationship", "The critical angle is the angle of incidence at which the angle of refraction is 90°; above it, total internal reflection."),
                        ("Change", "Aim the ray through the curved face at the <b>centre of the flat face</b>; increase the angle of incidence by rotating the block on the paper."),
                        ("Measure", "Mark the rays; draw the normal at the centre of the flat face; <b>measure the angle of incidence with a protractor</b> when the refracted ray <b>runs along the surface</b>."),
                        ("Use", "That angle is the critical angle; (optionally) plot r against i and read i where r = 90°."),
                        ("Accuracy", "Narrow ray; mark crosses far apart; make sure the ray really passes through the centre of the flat face so it is not refracted on entry."),
                        ("Repeat", "<b>Repeat and calculate a mean</b> critical angle."),
                    ], total=6), lines=8),
        ]),
    ],
)

SECTIONS = [section_t1, section_t2, section_t3, section_t4, section_t5, section_t6, section_t7, section_t8, section_t9, section_t10]

# ---------------------------------------------------------------------
# Flashcards
# ---------------------------------------------------------------------

FACTS = [
    fact("Law of reflection?", "Angle of incidence = angle of reflection, both measured from the normal.", "reflection"),
    fact("What is the normal?", "A line at 90° to the surface at the point where the ray hits. Draw it first; measure every angle from it.", "reflection"),
    fact("Specular vs diffuse reflection?", "Specular: smooth surface, parallel rays stay parallel, an image forms. Diffuse: rough surface, normals vary, rays scattered, no image. The law holds for both.", "reflection"),
    fact("Which way does light bend entering glass?", "Towards the normal — because it slows down.", "refraction"),
    fact("Which way does light bend leaving glass?", "Away from the normal — because it speeds up. The emergent ray is parallel to the incident ray.", "refraction"),
    fact("What causes refraction?", "A change in speed at the boundary. The part of the wavefront that changes speed first turns the wave.", "refraction"),
    fact("Refraction: what happens to speed, wavelength, frequency (light into glass)?", "Speed decreases, wavelength decreases, frequency unchanged.", "refraction"),
    fact("A ray along the normal?", "Does not change direction (angle of incidence 0°). It still slows down.", "refraction"),
    fact("Sound entering water?", "Speeds up (≈1500 m/s from 340 m/s) and bends away from the normal — the opposite of light.", "refraction"),
    fact("Define the critical angle.", "The angle of incidence (in the denser medium) at which the angle of refraction is 90° — the refracted ray runs along the surface.", "tir"),
    fact("Two conditions for total internal reflection?", "Light going from a denser to a less dense material, and angle of incidence greater than the critical angle.", "tir"),
    fact("Critical angle of glass, roughly?", "About 42°. Water about 49°.", "tir"),
    fact("What happens at i = critical angle, and above it?", "At it: refracted ray along the surface (r = 90°). Above it: total internal reflection — all the light reflects inside.", "tir"),
    fact("Why does a red object look red?", "It reflects red light and absorbs all the other colours.", "colour"),
    fact("What does a blue filter do?", "Transmits blue light and absorbs the other colours.", "colour"),
    fact("A red object in blue light looks…", "Black: there is no red to reflect, so it absorbs the blue.", "colour"),
    fact("Converging lens: what does it do?", "Brings parallel rays together to a focus (principal focus F). Convex, fatter in the middle.", "lenses"),
    fact("Diverging lens: what does it do?", "Spreads parallel rays out as if from a focus on the near side. Concave, thinner in the middle. Negative focal length.", "lenses"),
    fact("Power of a lens equation and unit?", "P = 1/f, f in metres, P in dioptres (D). Converging positive, diverging negative.", "lenses"),
    fact("Power and shape?", "More curved (fatter, thicker in the middle) → shorter focal length → higher power.", "lenses"),
    fact("Three properties shared by all EM waves?", "Transverse; same speed in a vacuum (3 × 10⁸ m/s); transfer energy from source to observer.", "em-waves"),
    fact("Speed of EM waves in a vacuum?", "3 × 10⁸ m/s. Use it as v in v = fλ.", "em-waves"),
    fact("Prefixes: GHz, MHz, nm?", "× 10⁹, × 10⁶, × 10⁻⁹.", "em-waves"),
    fact("EM spectrum in order of increasing frequency?", "Radio, microwaves, infrared, visible, ultraviolet, X-rays, gamma. (Raging Martians Invaded Venus Using X-ray Guns.)", "spectrum"),
    fact("Which end has the longest wavelength? the highest frequency?", "Radio: longest wavelength, lowest frequency. Gamma: shortest wavelength, highest frequency.", "spectrum"),
    fact("Visible light: colours in order of increasing frequency?", "Red, orange, yellow, green, blue, indigo, violet (red ≈ 700 nm, violet ≈ 400 nm).", "spectrum"),
    fact("Why is the spectrum described as continuous?", "No gaps between the groups; the groups overlap at their edges.", "spectrum"),
    fact("Uses of radio waves?", "Broadcasting, communications, satellite transmissions.", "uses"),
    fact("Uses of microwaves?", "Cooking, communications (mobile phones), satellite transmissions.", "uses"),
    fact("Uses of infrared?", "Cooking, thermal imaging, short-range communications, optical fibres, TV remote controls, security systems.", "uses"),
    fact("Uses of ultraviolet?", "Security marking, fluorescent lamps, detecting forged bank notes, disinfecting water.", "uses"),
    fact("Uses of X-rays?", "Observing the internal structure of objects, airport security scanners, medical X-rays.", "uses"),
    fact("Uses of gamma rays?", "Sterilising food and medical equipment, detecting and treating cancer.", "uses"),
    fact("How does danger vary across the spectrum?", "Potential danger increases with increasing frequency.", "dangers"),
    fact("Harm from microwaves? infrared?", "Microwaves: internal heating of body cells. Infrared: skin burns.", "dangers"),
    fact("Harm from ultraviolet? X-rays and gamma?", "UV: damage to surface cells and eyes → skin cancer, eye conditions. X and gamma: mutation or damage to cells → cancer.", "dangers"),
    fact("Does a cold object emit radiation?", "Yes — all bodies emit, mostly infrared at everyday temperatures.", "thermal-radiation"),
    fact("Hotter body: what changes about its radiation?", "Intensity increases; peak wavelength gets shorter (red → yellow → white hot).", "thermal-radiation"),
    fact("Four marks for \"why is its temperature constant\"?", "Absorbs radiation; also emits radiation; rate of emission rises with temperature; constant when rate of emission = rate of absorption. Say rate.", "thermal-balance"),
    fact("Body radiates more than it absorbs?", "Its temperature falls (until the rates balance). Less than it absorbs: temperature rises.", "thermal-balance"),
    fact("How do greenhouse gases warm the Earth?", "They absorb some of the infrared the surface emits and re-emit it, some back down, so less escapes; the balance moves to a higher temperature.", "thermal-balance"),
    fact("How do clouds and ice cool the Earth?", "They reflect incoming radiation back to space, so less is absorbed.", "thermal-balance"),
    fact("Best emitter and absorber of radiation?", "Matt black. Worst: shiny silver (best reflector).", "radiation-practical"),
    fact("Leslie cube: what is it?", "A metal cube with matt black, shiny black, white and shiny silver faces, filled with hot water; a detector at equal distance from each face compares emission.", "radiation-practical"),
    fact("Controls in the cooling-cans experiment?", "Same volume of water, starting temperature, can size, distance; lids on; read every minute.", "radiation-practical"),
    fact("How are radio waves produced?", "By an alternating current (oscillating electrons) in an aerial; when absorbed they induce an alternating current of the same frequency in a receiving aerial.", "radio-atoms"),
    fact("Where do visible, UV and X-rays come from in an atom?", "Electrons dropping from a higher to a lower energy level. Gamma rays come from the nucleus.", "radio-atoms"),
    fact("Fluorescence in four steps?", "UV absorbed by electrons → raised to a higher level → fall back → emit visible light (lower frequency).", "radio-atoms"),
    fact("Time for light from the Sun?", "t = d/v = 1.5 × 10¹¹ ÷ 3 × 10⁸ = 500 s, about 8 minutes.", "em-calc-hard"),
    fact("Subtracting in standard form?", "Write both with the same power of ten first, then subtract the front numbers.", "em-calc-hard"),
    fact("Refraction practical: the six steps?", "Draw round the block; narrow ray in; crosses on incident and emergent rays; remove block and join; normal + protractor for i and r; repeat angles and plot r against i.", "ray-practical"),
    fact("Why a semicircular block for the critical angle?", "A ray aimed at the centre of the flat face enters along a normal to the curved face, so it does not bend on entry.", "tir-hard"),
    fact("Critical angle from an i–r graph?", "Extend the curve to r = 90° and read off i.", "tir-hard"),
    fact("Converging lens, object beyond 2F?", "Real, inverted, smaller, between F and 2F on the far side (camera).", "lens-diagrams"),
    fact("Converging lens, object between F and 2F?", "Real, inverted, magnified, beyond 2F on the far side (projector).", "lens-diagrams"),
    fact("Converging lens, object inside F?", "Virtual, upright, magnified, same side as the object (magnifying glass).", "lens-diagrams"),
    fact("Diverging lens image?", "Always virtual, upright and smaller, on the object's side.", "lens-diagrams"),
    fact("Real vs virtual image?", "Real: rays actually meet, can be projected on a screen, inverted. Virtual: rays only appear to come from it, cannot be projected, upright.", "lens-diagrams"),
    fact("Magnification equation?", "image height ÷ object height (same scale, no unit).", "lens-diagrams"),
    fact("Why no sunburn through glass?", "Glass transmits visible light but absorbs most ultraviolet.", "absorb-transmit"),
    fact("Why are X-ray telescopes in space?", "The atmosphere absorbs X-rays (and gamma and UVC); it transmits visible and radio.", "absorb-transmit"),
]
