"""
fm_nn.py — Topic 15 (Forces and matter): the non-negotiables N1–N13.
Tiers from the Pearson spec: 15.1–15.6 both tiers and both sciences;
15.7P–15.17P Physics only; 15.14P (P = h ρ g) is the only Higher-only
statement.

N1 More than one force          N8 Pressure in a fluid: normal, plus atmosphere [P]
N2 Elastic and inelastic        N9 Atmospheric pressure with height [P]
N3 Hooke's law                  N10 Pressure in a liquid: depth and density [P]
N4 Energy stored                N11 P = h rho g [H, P]
N5 Linear and non-linear        N12 Upthrust, floating and sinking [P]
N6 The spring core practical    N13 Key words
N7 Pressure = force / area [P]
"""

from revlib import (
    axis, choice, curve, dashed, diagram, ewau, explain, fact, graph, group, line,
    mark, marks, numeric, practice, section, worked, written,
)
import fm_diagrams as dg

# ---------------------------------------------------------------------
# N1 · More than one force
# ---------------------------------------------------------------------

section_n1 = section(
    "two-forces", "nn", "Stretching, compressing or bending needs more than one force", "15.1",
    equations=[r"\text{one force: the object accelerates}", r"\text{two forces: it changes shape}"],
    blurb="To change the shape of an object you need at least two forces acting on it in different directions. One force on its own gives a resultant, and a resultant force accelerates the whole object instead of distorting it. The second force is often the one you forget: the hook holding the spring, the wall behind the ball, the table under the ruler.",
    checklist=[
        "Explain why a single force cannot stretch, compress or bend an object",
        "Identify both forces in a stretching, squashing or bending situation",
        "Describe the three kinds of distortion: stretching, compression, bending",
    ],
    parts=[
        explain(
            "Why two forces",
            diagram(dg.two_forces_svg(), 680, 220, "A spring pulled at both ends stretches; a spring with one force on it accelerates; a spring on a hook has the hook's pull and the weight.") +
            "<p>A force changes an object's <b>motion</b> or its <b>shape</b>. With <b>one</b> force there is a resultant, so the object as a whole <b>accelerates</b> (Topic 2) — it moves off rather than stretching. To <b>distort</b> it (stretch, compress or bend it) you need <b>more than one force</b>: forces in different directions that between them pull the parts of the object apart, push them together, or turn them. Pull both ends of a spring outward and it <b>stretches</b>; push both ends inward and it <b>compresses</b>; push the middle of a ruler one way while its ends are held the other way and it <b>bends</b>.</p>"
            "<p>The second force is usually supplied by whatever the object is attached to or resting on: the <b>hook</b> pulls up on a hanging spring while the <b>weight</b> pulls down; the <b>table</b> pushes up on a sponge you press; the <b>wall</b> pushes back on a ball thrown at it. In the exam, name <b>both</b>: \"the weight of the mass pulls the bottom of the spring down and the clamp pulls the top up, so the spring is stretched\".</p>",
        ),
        worked(
            "Naming both forces",
            "A student hangs a mass from a spring attached to a clamp. Explain why the spring stretches rather than simply moving downwards. (2 marks)",
            [
                "The <b>weight</b> of the mass pulls the bottom of the spring <b>down</b>, and the <b>clamp pulls the top up</b> — two forces in opposite directions.",
                "With a force at each end the spring cannot accelerate as a whole (the forces balance), so instead it <b>changes shape</b>: it stretches. One force alone would just accelerate it.",
            ],
        ),
        practice("More than one force", [
            written("fm-n1-q1", "Explain why you cannot stretch a spring by pulling on one end only. (2)",
                    marks(["Pulling one end gives a <b>single, unbalanced force</b>: a resultant.", "A resultant force <b>accelerates</b> the spring as a whole; to stretch it the other end must be held or pulled the other way, so that there are <b>two forces</b> in opposite directions."]), lines=2),
            choice("fm-n1-q2", "A sponge is squashed on a table. The two forces that compress it are…",
                   ["your hand and gravity", "your hand pushing down and the table pushing up", "gravity and air pressure", "the table and friction"], 1,
                   "The table supplies the second force."),
            written("fm-n1-q3", "Name the three ways an object can be distorted, and give an everyday example of each. (3)",
                    marks(["<b>Stretching</b> — a spring or elastic band pulled at both ends.", "<b>Compression</b> — a sponge or car spring squashed between two forces.", "<b>Bending</b> — a ruler or diving board pushed in the middle while its ends are held (or held at one end and pushed at the other)."]), lines=3),
            choice("fm-n1-q4", "A ball is thrown at a wall and squashes slightly on impact. The second force that compresses it is…",
                   ["gravity", "the push of the wall on the ball", "air resistance", "the thrower's hand"], 1,
                   "The back of the ball keeps moving forward while the wall pushes the front of the ball back: two forces."),
            choice("fm-n1-q5", "An object with a single force acting on it…",
                   ["stretches", "bends", "accelerates", "stays still"], 2,
                   "One force is a resultant force."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N2 · Elastic and inelastic distortion
# ---------------------------------------------------------------------

section_n2 = section(
    "elastic-inelastic", "nn", "Elastic and inelastic distortion", "15.2",
    equations=[r"\text{elastic: returns to its original shape}", r"\text{inelastic: permanently changed}"],
    blurb="An elastic distortion is undone when the forces are removed — the spring goes back to its original length. An inelastic distortion stays: the object is permanently changed. Every spring is elastic up to its elastic limit and inelastic beyond it.",
    checklist=[
        "Define elastic distortion and inelastic distortion",
        "State what the elastic limit is",
        "Give examples of materials that behave elastically and inelastically",
    ],
    parts=[
        explain(
            "Does it go back?",
            "<table class='tbl'><tr><th></th><th>Elastic distortion</th><th>Inelastic distortion</th></tr>"
            "<tr><td><b>Definition</b></td><td>the object <b>returns to its original shape and size when the forces are removed</b></td><td>the object <b>does not return</b> to its original shape: it is <b>permanently</b> distorted</td></tr>"
            "<tr><td><b>Examples</b></td><td>a spring within its elastic limit, an elastic band, a rubber ball, a diving board, a car's springs</td><td>modelling clay, a crushed can, a bent paperclip, a spring stretched too far (it stays longer)</td></tr>"
            "<tr><td><b>Energy</b></td><td>the work done stretching it is stored (elastic potential energy) and given back as it returns</td><td>the work done goes into rearranging the material and is not recovered</td></tr></table>"
            "<p>The <b>elastic limit</b> is the point beyond which the distortion stops being elastic: stretch a spring past it and it will not return to its original length. Up to the elastic limit the extension is also <b>proportional</b> to the force (Hooke's law, N3) for a spring — strictly the straight line ends at the <b>limit of proportionality</b>, just before the elastic limit, but for a GCSE spring the two are treated as the same point. The examiners' word is <b>distortion</b> (not \"deformation\", though that is accepted) and the two kinds are <b>elastic</b> and <b>inelastic</b>, not \"plastic\".</p>",
        ),
        worked(
            "Two springs",
            "Two identical springs are loaded. Spring A returns to 5.0 cm when unloaded; spring B stays at 6.2 cm. Explain the difference. (2 marks)",
            [
                "Spring A was distorted <b>elastically</b>: it returned to its original length when the force was removed, so it was not stretched beyond its <b>elastic limit</b>.",
                "Spring B was stretched <b>beyond its elastic limit</b>, so its distortion was <b>inelastic</b>: it is permanently longer.",
            ],
        ),
        practice("Elastic and inelastic", [
            written("fm-n2-q1", "State what is meant by an elastic distortion. (1)",
                    marks(["A change of shape that is <b>reversed when the forces are removed</b> — the object returns to its original shape and size."]), lines=1),
            choice("fm-n2-q2", "Which is an inelastic distortion?",
                   ["A trampoline bed springing back", "A squashed drinks can staying squashed", "An elastic band returning to size", "A diving board returning to level"], 1,
                   "Permanent change = inelastic."),
            written("fm-n2-q3", "A spring is stretched and does not return to its original length. State what has happened and why. (2)",
                    marks(["It has been distorted <b>inelastically</b> (permanently).", "Because it was stretched <b>beyond its elastic limit</b>."]), lines=2),
            choice("fm-n2-q4", "The elastic limit of a spring is…",
                   ["the force at which it snaps", "the point beyond which it no longer returns to its original length when unloaded", "its maximum length", "the length with no load"], 1,
                   "Beyond it, the distortion is inelastic."),
            choice("fm-n2-q5", "Which word do the mark schemes use for a change of shape?",
                   ["distortion", "destruction", "disruption", "declination"], 0,
                   "Elastic distortion / inelastic distortion."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N3 · Hooke's law
# ---------------------------------------------------------------------

section_n3 = section(
    "hooke-nn", "nn", "Hooke's law: force, extension and the spring constant", "15.3",
    equations=[r"F = k\,x", r"k = \dfrac{F}{x} \text{ in N/m}"],
    blurb="For a spring within its limit, the force is proportional to the extension: $F = kx$. The spring constant $k$ is the force per metre of extension, so a stiff spring has a large k. The equation is on the list; the marks are lost on x — it is the extension, not the length, and it must be in metres for k in N/m.",
    checklist=[
        "Use $F = kx$ to find force, extension or spring constant",
        "Use the extension (change in length), never the length, and convert cm or mm to m",
        "Explain what the spring constant tells you and give its unit",
    ],
    parts=[
        explain(
            "The equation and its trap",
            "<p><b>Hooke's law</b>: the extension of a spring is <b>directly proportional</b> to the force applied, as long as the limit of proportionality is not exceeded. As an equation, $F = k x$: force (N) = spring constant (N/m) × extension (m). The <b>spring constant</b> $k$ is the force needed for each metre of extension — a measure of <b>stiffness</b>. A car suspension spring might be 50 000 N/m; a lab spring 25 N/m. The same equation describes a <b>compression</b>: $x$ is then how much shorter the spring is.</p>"
            "<p><b>$x$ is the extension</b> — the change in length, stretched length − original length — not the length. The June 2023 scheme (Q7(a)(ii)) gave three marks for exactly this: read the position of the top of the spring against the ruler, read it again when pressed down, <b>subtract the two readings</b>. And it must be in <b>metres</b> when $k$ is in N/m: the June 2025 report (Q8(b)(ii)) saw candidates \"use the extension in cm and give the value as N/m\", which was \"100 times too small\" and scored one mark of two. 6.2 mm is $6.2 \\times 10^{-3}$ m; 4 cm is 0.04 m.</p>",
        ),
        worked(
            "A compressed spring",
            "A spring in a stapler has a spring constant of 260 N/m. It is compressed by 6.2 mm. Calculate the force on the spring. Give your answer to 2 significant figures. (3 marks)",
            [
                "$x = 6.2$ mm $= 6.2 \\times 10^{-3}$ m.",
                "$F = k x = 260 \\times 6.2 \\times 10^{-3} = 1.612$ N.",
                "$F = 1.6$ N (2 s.f.) — the June 2023 Q7(a)(i) marks were selection and substitution, evaluation, and the 2 s.f. answer; 1600 N (mm not converted) earned two of the three.",
            ],
        ),
        practice("Hooke's law", [
            numeric("fm-n3-q1", "A spring of spring constant 60 N/m is stretched by 25 cm. Calculate the force applied.", 15, "N",
                    "Convert 25 cm to m first.",
                    [r"$x = 25$ cm $= 0.25$ m"] + ewau(r"F = k x", r"F = 60 \times 0.25", "15", "N")),
            numeric("fm-n3-q2", "A spring is 8.0 cm long with no load and 11.0 cm long with a 6.0 N weight hanging from it. Calculate its spring constant.", 200, "N/m",
                    "Extension = 11.0 − 8.0 cm, in metres.",
                    [r"$x = 11.0 - 8.0 = 3.0$ cm $= 0.030$ m"] + ewau(r"k = F \div x", r"k = 6.0 \div 0.030", "200", "N/m")),
            numeric("fm-n3-q3", "A force of 12 N compresses a spring of spring constant 300 N/m. Calculate the compression in mm.", 40, "mm",
                    "$x = F \\div k$ gives metres; convert.",
                    [r"$x = F \div k = 12 \div 300 = 0.040$ m"] + ewau(r"x = F \div k", r"x = 12 \div 300 = 0.040 \text{ m}", "40", "mm")),
            choice("fm-n3-q4", "A spring is 12 cm long unstretched and 20 cm long when loaded with 4 N. A student writes $k = 4 \\div 0.20 = 20$ N/m. The mistake is…",
                   ["the force should be in kN", "the length was used instead of the extension (8 cm = 0.08 m, so $k = 50$ N/m)", "the answer should be in N/cm", "there is no mistake"], 1,
                   "Extension = loaded length − unloaded length."),
            choice("fm-n3-q5", "A spring constant of 500 N/m means…",
                   ["the spring breaks at 500 N", "a force of 500 N would stretch the spring by 1 m (within its limit): 5 N per cm", "the spring is 500 m long", "500 N is needed for any extension"], 1,
                   "Force per metre of extension — stiffness."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N4 · Energy stored
# ---------------------------------------------------------------------

section_n4 = section(
    "energy-stored", "nn", "The energy stored in a stretched spring", "15.4",
    equations=[r"E = \tfrac{1}{2}\,k\,x^2", r"E = \text{area under the } F\text{–}x \text{ line}"],
    blurb="Stretching a spring does work on it, and the work is stored as elastic potential energy: $E = \tfrac{1}{2} k x^2$. The ½ is there because the force grows from zero as the spring stretches, so the average force is half the final force — which is why the energy is also the area under the force–extension line.",
    checklist=[
        "Use $E = \tfrac{1}{2} k x^2$ to find the energy stored (or work done) in stretching a spring",
        "Square the extension in metres, not in centimetres",
        "Explain why the energy is the area under a force–extension graph",
    ],
    parts=[
        explain(
            "Work done stretching",
            "<p>The <b>work done</b> stretching a spring (within its limit) is stored as <b>elastic potential energy</b>: $E = \\tfrac{1}{2} k x^2$, energy (J) = ½ × spring constant (N/m) × extension² (m²). Why ½? Work = force × distance (Topic 8), but the force is <b>not constant</b>: it starts at zero and rises to $F = kx$ as the spring stretches, so the <b>average</b> force is $\\tfrac{1}{2} k x$ and the work is $\\tfrac{1}{2} k x \\times x$. On a force–extension graph that is the <b>area of the triangle</b> under the straight line, $\\tfrac{1}{2} \\times F \\times x$ — the same number.</p>"
            "<p>Two traps. <b>Convert the extension to metres first</b>: 10 cm squared is $0.10^2 = 0.010$ m², not 100 — the June 2025 report (Q8(b)(i), the area $\\tfrac{1}{2} F x$ with $x$ left in cm) saw answers \"100 times too large\"; with $\\tfrac{1}{2} k x^2$ the slip is squared, 10 000 times. And it is $x^2$, so <b>doubling the extension quadruples the energy</b>. The energy is returned when the spring is released (an elastic distortion): a catapult turns it into kinetic energy, a pogo stick into gravitational potential energy.</p>",
        ),
        worked(
            "Energy in a stretched spring",
            "A spring with a spring constant of 80 N/m is stretched by 25 cm. Calculate the energy stored in it. (3 marks)",
            [
                "$x = 25$ cm $= 0.25$ m.",
                "$E = \\tfrac{1}{2} k x^2 = \\tfrac{1}{2} \\times 80 \\times 0.25^2 = \\tfrac{1}{2} \\times 80 \\times 0.0625$.",
                "$E = 2.5$ J.",
            ],
        ),
        practice("Energy stored", [
            numeric("fm-n4-q1", "A spring of spring constant 150 N/m is compressed by 4.0 cm. Calculate the energy stored.", 0.12, "J",
                    "Square 0.040 m.",
                    [r"$x = 0.040$ m"] + ewau(r"E = \tfrac{1}{2} k x^2", r"E = \tfrac{1}{2} \times 150 \times 0.040^2", "0.12", "J")),
            numeric("fm-n4-q2", "A spring is stretched by 0.30 m and stores 9.0 J. Calculate its spring constant.", 200, "N/m",
                    "$k = 2E \\div x^2$.",
                    ewau(r"k = 2E \div x^2", r"k = 2 \times 9.0 \div 0.30^2", "200", "N/m")),
            numeric("fm-n4-q3", "A toy launcher's spring has a spring constant of 160 N/m and is compressed by 0.25 m. Calculate the maximum kinetic energy it could give a ball.", 5.0, "J",
                    "All the stored energy becomes KE.",
                    ewau(r"E = \tfrac{1}{2} k x^2", r"E = \tfrac{1}{2} \times 160 \times 0.25^2", "5.0", "J")),
            choice("fm-n4-q4", "The extension of a spring is doubled (within its limit). The energy stored…",
                   ["doubles", "quadruples", "halves", "stays the same"], 1,
                   "$E \\propto x^2$."),
            choice("fm-n4-q5", "A student finds $E = \\tfrac{1}{2} \\times 50 \\times 10^2 = 2500$ J for a spring stretched by 10 cm. The answer is…",
                   ["correct", "10 000 times too large: 10 cm = 0.10 m, so $E = 0.25$ J", "100 times too small", "twice too large"], 1,
                   "The extension must be squared in metres."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N5 · Linear and non-linear
# ---------------------------------------------------------------------

fx_points_lin = [[0, 0], [2, 4], [4, 8], [6, 12], [8, 16]]
fx_nonlin = [[round(8 + 0.5 * i, 2), round(16 + 4.0 * (1 - 2.0 ** (-(0.5 * i) / 1.3)), 2)] for i in range(9)]
graph_fx = graph(
    axis("extension in cm", 12, 2), axis("force in N", 20, 4),
    [line(fx_points_lin), curve(fx_nonlin), dashed([[8, 0], [8, 16]])],
    "Force against extension for a spring: a straight line through the origin up to 8 cm and 16 N, then a curve that bends over towards 20 N at 12 cm.",
    marks_list=[mark(8, 16, "limit of proportionality", drop=False, dx=-136, dy=-14)],
)

section_n5 = section(
    "linear-nonlinear", "nn", "Linear and non-linear force–extension graphs", "15.5",
    equations=[r"\text{straight line through the origin: } F \propto x", r"\text{curve: Hooke's law no longer applies}"],
    blurb="Force against extension for a spring is a straight line through the origin — linear, so force is proportional to extension and the gradient is the spring constant. Beyond the limit of proportionality the line curves: the same extra force gives more extension than before, and Hooke's law no longer applies. Rubber bands curve from the start.",
    checklist=[
        "Describe a linear force–extension relationship and what it shows",
        "Identify the limit of proportionality on a graph and describe the non-linear part",
        "Find the spring constant from the gradient of the linear part",
    ],
    parts=[
        explain(
            "Reading the shape",
            "<p><b>Linear</b> (a straight line through the origin): force is <b>directly proportional</b> to extension — double the force, double the extension — and the <b>gradient</b> of force against extension is the spring constant $k$. This is the region where Hooke's law applies. <b>Non-linear</b> (a curve): the extension is no longer proportional to the force. For a spring the curve begins at the <b>limit of proportionality</b>; beyond it each extra newton stretches the spring by more than before (the line bends towards the extension axis), and a little further on is the elastic limit, after which the spring will not return.</p>"
            "<p>Two things to say in words: \"<b>a straight line through the origin</b>, so force is proportional to extension\" (both parts — a straight line that does not pass through the origin is not proportional); and \"<b>beyond point P the graph is non-linear</b>, so the spring no longer obeys Hooke's law\". The graph can be drawn either way up: with extension on the $y$-axis the gradient is $1/k$, and the curve bends <b>upwards</b> past the limit. Check the axes before reading a gradient. A rubber band gives a curve from the start (and a different curve unloading) — it does not obey Hooke's law at all.</p>",
        ),
        worked(
            "Describing the graph",
            "The graph shows force against extension for a spring. Describe the relationship shown, and find the spring constant. (4 marks)",
            [
                "Up to 8 cm the graph is a <b>straight line through the origin</b>: force is <b>directly proportional</b> to extension (Hooke's law applies).",
                "Beyond 8 cm (the limit of proportionality, 16 N) the graph is <b>non-linear</b> — it curves — so the extension is no longer proportional to the force and each extra newton gives more extension.",
                "Spring constant = gradient of the straight part: $k = 16 \\div 0.080$ (8 cm in metres).",
                "$k = 200$ N/m.",
            ],
            graph=graph_fx,
        ),
        practice("Linear and non-linear", [
            group("fm-n5-q1", "Use the force–extension graph.", [
                numeric("fm-n5-q1a", "Use the graph to find the extension when the force is 12 N.", 6, "cm",
                        "Read across from 12 N to the straight line.",
                        ["On the straight line, 12 N is at an extension of 6 cm."], label="a"),
                numeric("fm-n5-q1b", "Calculate the energy stored in the spring at an extension of 6.0 cm.", 0.36, "J",
                        "Area of the triangle under the line up to 6 cm (force 12 N), with x in metres.",
                        [r"at 6.0 cm the force is 12 N; $x = 0.060$ m"] + ewau(r"E = \tfrac{1}{2} F x", r"E = \tfrac{1}{2} \times 12 \times 0.060", "0.36", "J"), label="b"),
                choice("fm-n5-q1c", "Which statement about the part of the graph beyond 8 cm is correct?",
                       ["Force is still proportional to extension", "The spring constant has increased", "Each extra newton of force produces a larger extension than before; Hooke's law no longer applies", "The spring has snapped"], 2,
                       "Non-linear: the line bends towards the extension axis.", label="c"),
            ], graph=graph_fx),
            written("fm-n5-q2", "A student plots extension against force for a spring and gets a straight line through the origin. State what this shows about the relationship, and how the spring constant is found from the graph. (2)",
                    marks(["Extension is <b>directly proportional</b> to force (Hooke's law): a straight line <b>through the origin</b>.", "With extension on the $y$-axis the gradient is $1 \\div k$, so $k = 1 \\div$ gradient (or read a pair of values and use $k = F \\div x$)."]), lines=2),
            choice("fm-n5-q3", "A force–extension graph is a straight line that does NOT pass through the origin. Force is…",
                   ["proportional to extension", "not proportional to extension (a linear relationship, but not a proportional one)", "inversely proportional", "equal to the extension"], 1,
                   "Proportional needs the line through the origin."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N6 · The spring core practical
# ---------------------------------------------------------------------

section_n6 = section(
    "spring-practical", "nn", "The spring core practical: extension against force, and the work done", "15.6",
    equations=[r"x = \text{loaded reading} - \text{unloaded reading}", r"k = \text{gradient of } F \text{ against } x"],
    blurb="Hang a spring from a clamp, note where its end is against a ruler, add masses one at a time and note the new position each time. The extension is the difference; the force is the weight added. Plot force against extension: the gradient is k and the area is the work done. The 2023 marks were for the two readings and the subtraction, and for reading at eye level.",
    checklist=[
        "Describe the method: apparatus, readings, how the extension is found",
        "State the accuracy points: eye level, pointer, zero reading, not past the limit",
        "Use the graph: gradient for k, area for the work done stretching",
    ],
    parts=[
        explain(
            "The method and its marks",
            diagram(dg.practical_svg(), 660, 270, "The spring practical: a spring on a clamp stand beside a vertical ruler, with the unloaded and loaded readings marked, and the force–extension graph with its gradient and area.") +
            "<table class='tbl'><tr><th>Step</th><th>What to write</th></tr>"
            "<tr><td><b>Apparatus</b></td><td>spring, clamp and stand, <b>metre ruler</b> (mm scale) clamped vertically, slotted <b>masses</b> and hanger, a pointer (a pin or splint fixed to the bottom of the spring), <b>safety glasses</b></td></tr>"
            "<tr><td><b>Zero reading</b></td><td>with <b>no load</b>, read the position of the bottom of the spring (the pointer) on the ruler</td></tr>"
            "<tr><td><b>Loading</b></td><td>add a 100 g mass (weight 1 N); read the new position; repeat adding one mass at a time, up to about 6 masses</td></tr>"
            "<tr><td><b>Extension</b></td><td>for each load, <b>extension = new reading − zero reading</b> (June 2023 Q7(a)(ii): read with no load, read with the load, <b>subtract</b>)</td></tr>"
            "<tr><td><b>Graph</b></td><td>plot <b>force</b> ($W = mg$) against <b>extension</b>; a straight line through the origin confirms Hooke's law; <b>gradient = $k$</b>; the <b>area</b> under the line up to an extension is the <b>work done</b> stretching the spring to it</td></tr>"
            "<tr><td><b>Accuracy</b></td><td>read the ruler <b>at eye level</b> with a pointer to avoid parallax (June 2023 Q7(a)(iii): a change \"to enable accurate location of the top of the spring\" (the moving end, in that question) and how it is used); ruler vertical and clamped; wait for the spring to stop moving; do not load past the elastic limit (check it returns to the zero reading when unloaded); repeat unloading as well as loading</td></tr></table>",
        ),
        worked(
            "Measuring the extension",
            "Describe how a student could measure the extension of a spring when a mass is hung from it. (3 marks)",
            [
                "Clamp a ruler vertically beside the spring and read the position of the <b>bottom of the spring</b> (a pointer) <b>with no load</b>.",
                "Hang the mass on the spring, wait for it to settle, and read the position of the pointer <b>again</b> — reading at eye level each time to avoid parallax.",
                "<b>Extension = loaded reading − unloaded reading</b> (in mm).",
            ],
        ),
        practice("The spring practical", [
            written("fm-n6-q1", "A student hangs masses on a spring and, for each mass, writes down the length of the spring read from a ruler held in her hand beside it, looking down at the scale from above. She then plots force against length. Give three improvements to her method and say what each improves. (3)",
                    marks(["<b>Clamp the ruler vertically</b> beside the spring (not hand-held), so the readings are from a fixed scale.", "Read the pointer <b>at eye level</b> (not from above), to avoid parallax error.", "Record the <b>no-load reading</b> and subtract it from each reading to get the <b>extension</b>, and plot force against extension — Hooke's law is about the extension, so the line should pass through the origin."]), lines=3),
            choice("fm-n6-q2", "Why is a pointer fixed to the bottom of the spring?",
                   ["To add weight", "So the position on the ruler can be read accurately at eye level, reducing parallax error", "To stop the spring swinging", "To hold the masses"], 1,
                   "2023 Q7(a)(iii): a change to locate the end of the spring accurately."),
            numeric("fm-n6-q3", "The pointer reads 142 mm with no load and 187 mm with 3.0 N hanging. Calculate the spring constant.", 67, "N/m",
                    "Extension = 187 − 142 mm, in metres.",
                    [r"$x = 187 - 142 = 45$ mm $= 0.045$ m"] + ewau(r"k = F \div x", r"k = 3.0 \div 0.045", "67", "N/m (66.7)")),
            written("fm-n6-q4", "Explain how the work done in stretching the spring to a given extension can be found from the force–extension graph. (2)",
                    marks(["Work done = <b>area under the line</b> up to that extension.", "For the straight part this is a triangle: $\\tfrac{1}{2} \\times$ force $\\times$ extension (extension in metres), the same as $\\tfrac{1}{2} k x^2$."]), lines=2),
            choice("fm-n6-q5", "Which precaution checks that the spring has not been stretched beyond its elastic limit?",
                   ["Using a longer ruler", "Removing the masses and checking the pointer returns to the zero reading", "Adding the masses quickly", "Using heavier masses"], 1,
                   "If it does not return, the last readings were past the limit."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N7 · Pressure = force / area [P]
# ---------------------------------------------------------------------

section_n7 = section(
    "pressure-nn", "nn", "Pressure: force per unit area", "15.10P, 15.11P",
    equations=[r"P = \dfrac{F}{A}", r"1 \text{ Pa} = 1 \text{ N/m}^2"],
    blurb="Pressure is the force per unit area: the same force on a smaller area is a larger pressure. Snowshoes, tractor tyres and camel hooves spread a weight over a large area; a knife edge, a drawing pin and a stiletto heel concentrate it. The equation is on the list; the marks are on the area — all of it, in m².",
    tags=["P"],
    checklist=[
        "Use $P = F/A$ to find pressure, force or area",
        "Explain a design in terms of area and pressure, in the words that score",
        "Convert cm² and mm² to m² before substituting",
    ],
    parts=[
        explain(
            "The equation and the explanation",
            "<p><b>Pressure</b> = force ÷ area, $P = F \\div A$, in <b>pascals</b> (1 Pa = 1 N/m²), with the force at right angles to the surface. A force of 800 N on 0.4 m² is 2000 Pa; the same 800 N on 0.0004 m² (the point of a stiletto heel) is 2 000 000 Pa. <b>Large area → small pressure</b>: snowshoes, skis, wide tyres, camel feet, the broad base of a dam, a wide strap. <b>Small area → large pressure</b>: a knife edge, a nail point, a drawing pin, football studs, an ice skate.</p>"
            "<p>The June 2022 report (Q4(a)(ii), why a camel's wide feet help on sand): the marks were for <b>the larger surface area</b> and for <b>less pressure</b> (or the weight spread over a larger area); \"the mass spread out\" was \"unworthy of a second mark\" — say <b>force or weight</b> spread over the area, and name the <b>pressure</b>. The same report's Q4(a)(i): a donkey's weight on <b>four hooves</b> — the area in $P = F \\div A$ is the <b>total</b> area in contact, 4 × one hoof; forgetting the four cost a mark. And the area must be in <b>m²</b>: 1 cm² = $10^{-4}$ m², 1 mm² = $10^{-6}$ m² (June 2025 Q1(c): an area left in mm² gave \"an answer that was a million times too large\").</p>",
        ),
        worked(
            "Pressure under four feet",
            "A donkey weighs 2000 N. Each hoof has an area of 50 cm². Calculate the pressure the donkey exerts on the ground when standing on all four hooves. (3 marks)",
            [
                "Total area $= 4 \\times 50 = 200$ cm² $= 200 \\times 10^{-4} = 0.020$ m².",
                "$P = F \\div A = 2000 \\div 0.020$.",
                "$P = 100\\,000$ Pa (100 kPa).",
            ],
        ),
        practice("Pressure", [
            numeric("fm-n7-q1", "A box weighs 450 N and its base is 0.30 m by 0.50 m. Calculate the pressure on the floor.", 3000, "Pa",
                    "Area = 0.30 × 0.50.",
                    [r"$A = 0.30 \times 0.50 = 0.15$ m²"] + ewau(r"P = F \div A", r"P = 450 \div 0.15", "3000", "Pa")),
            numeric("fm-n7-q2", "A drawing pin is pushed with a force of 8.0 N. The point has an area of 0.20 mm². Calculate the pressure at the point.", 4e7, "Pa",
                    "0.20 mm² $= 0.20 \\times 10^{-6}$ m².",
                    [r"$A = 0.20 \times 10^{-6} = 2.0 \times 10^{-7}$ m²"] + ewau(r"P = F \div A", r"P = 8.0 \div (2.0 \times 10^{-7})", r"4.0 \times 10^{7}", "Pa")),
            numeric("fm-n7-q3", "The pressure of the air on a window is 100 000 Pa. The window has an area of 0.80 m². Calculate the force on it.", 80000, "N",
                    "$F = P \\times A$.",
                    ewau(r"F = P A", r"F = 100\,000 \times 0.80", "80\\,000", "N")),
            written("fm-n7-q4", "Explain why a person wearing snowshoes does not sink into soft snow as far as a person in ordinary boots. (2)",
                    marks(["The snowshoes have a much <b>larger area</b> in contact with the snow, so the person's <b>weight is spread over a larger area</b>.", "Pressure = force ÷ area, so the <b>pressure</b> on the snow is <b>smaller</b> and the snow is not compressed as much."]), lines=2),
            choice("fm-n7-q5", "A student explains a camel's wide feet with 'its mass is spread out'. The 2022 examiners…",
                   ["gave full marks", "did not credit it: say the weight (force) is spread over a larger area, so the pressure is less", "gave a mark for 'mass'", "wanted the word 'density'"], 1,
                   "Force, not mass; and name the pressure."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N8 · Pressure in a fluid [P]
# ---------------------------------------------------------------------

section_n8 = section(
    "fluid-pressure", "nn", "Pressure in a fluid: the fluid plus the atmosphere, acting at right angles to every surface", "15.8P, 15.9P",
    equations=[r"\text{total pressure} = \text{fluid} + \text{atmospheric}", r"F = P\,A \text{ normal to the surface}"],
    blurb="A fluid is a liquid or a gas. The pressure at a point in a fluid is the pressure due to the fluid itself plus the atmospheric pressure on top of it, and it pushes at right angles (normal) to any surface it touches — walls, floor, a diver, the inside of a window. Force on a surface = pressure × area.",
    tags=["P"],
    checklist=[
        "State that the pressure in a fluid is due to the fluid and to the atmosphere",
        "Draw the force from a fluid's pressure at right angles to the surface, towards it",
        "Use $F = PA$, including a difference in pressure across a surface",
    ],
    parts=[
        explain(
            "Normal to the surface",
            diagram(dg.normal_svg(), 660, 275, "A tank of water with pressure arrows at right angles to every wall, longer with depth, and a block pushed on every face; an aeroplane window with 80 kPa inside and 23 kPa outside, so the net force is outward.") +
            "<p>A <b>fluid</b> (liquid or gas) has no fixed shape, so its pressure is not in one direction: at any point it pushes <b>equally in all directions</b>, and on any surface it produces a force <b>at right angles — normal — to that surface</b>. On the floor of a tank the force is downward; on a vertical wall, sideways; on a curved submarine hull, inward everywhere, perpendicular to the hull. The June 2023 scheme (Q4(a)(iv), the force of the cabin air on an aeroplane window) wanted the arrow <b>pointing towards the outside</b> and <b>normal to the surface at X</b>; the June 2024 scheme (Q4(a)) asked for the direction \"normal to the surface, acting towards the surface\". Draw the arrow <b>from the point on the surface</b>, perpendicular to it (2025 Q1(a)(ii): an arrow \"too far away from the point\" scored nothing).</p>"
            "<p>The <b>total pressure</b> at a depth in a liquid is the pressure <b>due to the liquid</b> plus the <b>atmospheric pressure</b> pressing on its surface (about 100 kPa at sea level). A surface with fluid on both sides feels the <b>difference</b>: the 2023 aeroplane window had 80 kPa inside and 23 kPa outside, so the net pressure was $80\\,000 - 23\\,000 = 57\\,000$ Pa outward, and the force on a 0.094 m² window from the inside was $F = P A = 80\\,000 \\times 0.094 = 7500$ N. A larger window at the same pressure gets a larger force (Q4(a)(iii): \"force is greater on the large window; pressure is the same\").</p>",
        ),
        worked(
            "The force on a window",
            "The air inside an aeroplane cabin is at 80 kPa and the air outside at 23 kPa. (a) Calculate the net pressure on a window. (b) A window has an area of 0.094 m². Calculate the force of the cabin air on it. (3 marks)",
            [
                "(a) net pressure $= 80\\,000 - 23\\,000 = 57\\,000$ Pa, acting outward (the June 2023 Q4(a)(i) answer).",
                "(b) $F = P A = 80\\,000 \\times 0.094$.",
                "$F = 7500$ N (7520 N), at right angles to the window, towards the outside.",
            ],
        ),
        practice("Pressure in a fluid", [
            choice("fm-n8-q1", "The force from the water on the sloping side of a swimming pool acts…",
                   ["vertically downwards", "at right angles to the sloping side, towards it", "horizontally", "upwards"], 1,
                   "Normal to the surface, whatever its angle."),
            numeric("fm-n8-q2", "The pressure inside a sealed container is 150 kPa and the atmospheric pressure outside is 100 kPa. The lid has an area of 0.020 m². Calculate the net force on the lid.", 1000, "N",
                    "Net pressure first, then $F = PA$.",
                    [r"net $P = 150\,000 - 100\,000 = 50\,000$ Pa"] + ewau(r"F = P A", r"F = 50\,000 \times 0.020", "1000", "N outward")),
            written("fm-n8-q3", "The pressure at the bottom of a lake is 'due to the water plus the atmosphere'. Explain what this means. (2)",
                    marks(["The water above the point presses down on it — the pressure <b>due to the liquid</b> (which increases with depth).", "The air above the lake presses down on the water's surface too, so the <b>atmospheric pressure</b> (about 100 kPa) is added to it: total = liquid + atmosphere."]), lines=2),
            choice("fm-n8-q4", "Two windows in the same cabin: one large, one small. Compared with the small window, the large one has…",
                   ["a greater pressure on it", "a greater force on it and the same pressure", "the same force", "a smaller force"], 1,
                   "$F = PA$; the pressure is the same everywhere in the cabin."),
            numeric("fm-n8-q5", "A pressure of $4.8 \\times 10^{7}$ Pa acts on a surface of area $1.2 \\times 10^{-5}$ m². Calculate the force, to 2 significant figures.", 580, "N",
                    "$F = PA$; 576 N rounds to 580 N.",
                    ewau(r"F = P A", r"F = 4.8 \times 10^{7} \times 1.2 \times 10^{-5}", "576 = 580", "N (2 s.f. — the June 2024 Q4(b) third mark was for the rounding)")),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N9 · Atmospheric pressure with height [P]
# ---------------------------------------------------------------------

height_points = [[0, 100], [1, 89], [2, 79], [3, 70], [4, 62], [5, 54], [6, 47], [7, 41], [8, 36], [9, 31], [10, 26]]
graph_height = graph(
    axis("height above sea level in km", 10, 1), axis("atmospheric pressure in kPa", 120, 10),
    [curve(height_points)],
    "Atmospheric pressure against height: 100 kPa at sea level falling to about 26 kPa at 10 km, curving so that the fall per kilometre gets smaller with height.",
)

section_n9 = section(
    "atmospheric-height", "nn", "Atmospheric pressure, and why it falls with height", "15.7P",
    equations=[r"\text{less air above} \rightarrow \text{less weight of air} \rightarrow \text{lower pressure}", r"\text{non-linear: the fall per km shrinks}"],
    blurb="The atmosphere presses on everything with about 100 kPa at sea level — the weight of all the air above. Climb, and there is less air above you, so less weight pressing down, so lower pressure; the air up there is also less dense. The graph is a curve, not a line, and the examiners want you to say so and to quote its numbers.",
    tags=["P"],
    checklist=[
        "Explain why atmospheric pressure decreases with height, in the mark-scheme words",
        "Describe a pressure–height graph: direction, non-linear, with numbers",
        "Explain where atmospheric pressure comes from",
    ],
    parts=[
        explain(
            "Less air above",
            "<p><b>Atmospheric pressure</b> is the pressure of the air: the <b>weight of the column of air above</b> a surface, spread over that surface, about <b>100 kPa</b> (100 000 N on every square metre) at sea level — plus the constant bombardment of air molecules (Topic 14), which is the same thing seen from the particle side. We do not feel it because the fluids inside us push out just as hard.</p>"
            "<p><b>Why it falls with height</b>: higher up there is <b>less air above</b> you, so a <b>smaller weight of air</b> presses down on each square metre, so the pressure is lower. The air is also <b>less dense</b> higher up — the particles are further apart — because it is not squeezed by as much air above it, and this is why the graph is a <b>curve</b>: each kilometre of thin high air weighs less than a kilometre of dense low air, so the pressure falls by less and less per kilometre. The June 2023 scheme (Q4(b)) gave marks for \"increase in height results in decrease in pressure\", \"<b>non-linear</b> relationship\" and \"<b>use of numerical data</b>\" from the graph, and for the explanation any one of \"air becomes <b>less dense</b>\", \"<b>smaller weight of air above</b>\"; the June 2024 scheme (Q4(c)) wanted \"as height increases pressure decreases\" (a negative correlation) and \"non-linear — curved, not proportional, the gradient changes\". Gravity getting weaker is <b>not</b> the reason (it barely changes over 10 km): the June 2024 scheme (Q4(d)) said to ignore it.</p>",
        ),
        worked(
            "Describing the graph",
            "The graph shows how atmospheric pressure changes with height. Describe the relationship shown. (3 marks)",
            [
                "As the height increases the pressure <b>decreases</b> (a negative correlation).",
                "The relationship is <b>non-linear</b>: the line is a curve, with the pressure falling by less per kilometre as the height increases (not proportional).",
                "Numbers: from 100 kPa at sea level to about 54 kPa at 5 km and 26 kPa at 10 km — the first 5 km lose 46 kPa, the next 5 km only 28 kPa.",
            ],
            graph=graph_height,
        ),
        practice("Atmospheric pressure", [
            group("fm-n9-q1", "Use the graph of atmospheric pressure against height.", [
                numeric("fm-n9-q1a", "Read the pressure at a height of 3 km.", 70, "kPa",
                        "Read up from 3 km.",
                        ["At 3 km the line is at 70 kPa."], label="a", tolerance=0.04),
                numeric("fm-n9-q1b", "Calculate the percentage decrease in pressure between sea level and 3 km.", 30, "%",
                        "$(100 - 70) \\div 100 \\times 100$.",
                        [r"fall $= 100 - 70 = 30$ kPa", r"percentage $= 30 \div 100 \times 100 = 30$ %"], label="b", tolerance=0.04),
                written("fm-n9-q1c", "Explain why the pressure decreases with height. (2)",
                        marks(["Higher up there is <b>less air above</b>, so a <b>smaller weight of air</b> presses down on each unit of area.", "The air higher up is also <b>less dense</b> (particles further apart), so each extra kilometre of height removes less weight — which is why the fall is non-linear."]), lines=2, label="c"),
            ], graph=graph_height),
            choice("fm-n9-q2", "Which is NOT a reason for lower atmospheric pressure at the top of a mountain?",
                   ["Less air above", "A smaller weight of air pressing down", "Gravity is much weaker there", "The air is less dense"], 2,
                   "Gravity hardly changes over a few km; the mark schemes ignore it."),
            written("fm-n9-q3", "State what causes atmospheric pressure. (1)",
                    marks(["The <b>weight of the air above</b> a surface pressing down on it (the air particles colliding with the surface)."]), lines=1),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N10 · Pressure in a liquid: depth and density [P]
# ---------------------------------------------------------------------

section_n10 = section(
    "depth-density", "nn", "Pressure in a liquid increases with depth and with density", "15.12P, 15.13P",
    equations=[r"\text{deeper} \rightarrow \text{more liquid above} \rightarrow \text{more pressure}", r"\text{denser} \rightarrow \text{heavier liquid above} \rightarrow \text{more pressure}"],
    blurb="The pressure at a point in a liquid comes from the weight of the liquid above it. Go deeper and there is a taller column above you; use a denser liquid and the same column weighs more. Either way the pressure rises — which is why dams are thicker at the bottom and why water from a lower hole jets out further.",
    tags=["P"],
    checklist=[
        "State that pressure in a liquid increases with depth and with the density of the liquid",
        "Explain both, in terms of the weight of the liquid above",
        "Apply it: dam walls, holes in a can, a diver's ears, sea water vs fresh water",
    ],
    parts=[
        explain(
            "The weight of the liquid above",
            diagram(dg.depth_svg(), 660, 275, "Two tanks filled to the same depth with fresh water and sea water; the pressure arrows on the walls lengthen with depth and are longer in the denser sea water.") +
            "<p>At a point in a liquid, the pressure due to the liquid is produced by the <b>weight of the liquid above</b> that point. <b>Deeper</b> means a <b>taller column of liquid</b> above, which weighs more, so the pressure is greater: a dam is built <b>thicker at the bottom</b>, where the pressure is largest; water jets out <b>further</b> from a hole low in a can than from one near the top (June 2025 Q1(d): the force below a bigger or deeper hole is greater); a diver's ears hurt as she descends. <b>Denser</b> liquid means the <b>same column has more mass</b>, so more weight, so more pressure: at the same depth, sea water (1030 kg/m³) presses harder than fresh water (1000 kg/m³), and mercury (13 600 kg/m³) harder still.</p>"
            "<p>The June 2022 report (Q4(c), a graph of pressure against depth for fresh water, asked how the line for sea water would differ): \"increasing the density increases the pressure\" — the line is <b>steeper</b> (a larger gradient), still <b>straight</b> (pressure proportional to depth), and starts from the <b>same intercept</b>, the <b>atmospheric pressure</b> at the surface. Those four points were the four marks.</p>",
        ),
        worked(
            "The dam",
            "Explain why a dam wall is built much thicker at the bottom than at the top. (3 marks)",
            [
                "The pressure in the water is caused by the <b>weight of the water above</b> each point.",
                "At the bottom of the dam the water is <b>deepest</b>: there is the <b>tallest column</b> of water above, so the pressure is <b>greatest</b> there.",
                "The force on each square metre of the wall (force = pressure × area) is therefore largest at the bottom, so the wall must be thickest there to withstand it.",
            ],
        ),
        practice("Depth and density", [
            written("fm-n10-q1", "A can has three holes in its side at different heights. Water jets out furthest from the lowest hole. Explain why. (2)",
                    marks(["The lowest hole is <b>deepest</b>, with the <b>most water above</b> it, so the <b>pressure</b> there is greatest.", "A greater pressure gives a greater force on the water at the hole, so it leaves faster and travels further."]), lines=2),
            choice("fm-n10-q2", "At the same depth, the pressure due to the liquid is greater in sea water than in fresh water because…",
                   ["sea water is deeper", "sea water is denser, so the same column of liquid above has more weight", "sea water is colder", "the atmosphere is heavier over the sea"], 1,
                   "Same height, more mass per m³."),
            written("fm-n10-q3", "A graph of pressure against depth is drawn for fresh water. Describe how the line for a denser liquid would differ. (4)",
                    marks(["At every depth the <b>pressure would be greater</b>: a denser liquid gives more pressure.", "It would be <b>steeper</b> (a larger gradient): the pressure increases faster with depth in the denser liquid.", "It would still be a <b>straight line</b> (pressure proportional to depth).", "It would start from the <b>same intercept</b> — the atmospheric pressure at the surface."]), lines=4),
            choice("fm-n10-q4", "Which pair both increase the pressure at a point in a liquid?",
                   ["Greater depth and greater density", "Greater depth and smaller density", "Smaller depth and greater density", "A wider container and a taller container"], 0,
                   "Taller column, heavier liquid."),
            choice("fm-n10-q5", "A diver descends from 5 m to 10 m. The pressure due to the water…",
                   ["halves", "doubles", "stays the same", "quadruples"], 1,
                   "Proportional to depth: twice the depth, twice the pressure due to the water (the total, with the atmosphere added, less than doubles)."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N11 · P = h rho g [H, P]
# ---------------------------------------------------------------------

section_n11 = section(
    "liquid-pressure", "nn", "The liquid-column equation, and the difference in pressure between two depths", "15.14P",
    equations=[r"P = h\,\rho\,g", r"\Delta P = \Delta h\,\rho\,g"],
    blurb="The pressure due to a column of liquid is height × density × g: a 10 m column of water (1000 kg/m³) gives 100 000 Pa, about one atmosphere. The equation is on the list; the marks are lost by using 10 for the density of water instead of 1000, and by not noticing an answer that cannot be right.",
    tags=["H", "P"],
    checklist=[
        "Use $P = h \\rho g$ to find the pressure due to a liquid, or the depth, or the density",
        "Find the difference in pressure between two depths",
        "Check that the answer makes sense (10 m of water ≈ 100 kPa)",
    ],
    parts=[
        explain(
            "Where it comes from, and the trap",
            "<p>A column of liquid of height $h$ and cross-section $A$ has volume $hA$, mass $\\rho h A$ and weight $\\rho h A g$; spread over the area $A$ at the bottom that is a pressure of $\\rho h g$ — the area cancels, so the pressure depends only on <b>depth</b>, <b>density</b> and <b>$g$</b>: $P = h \\rho g$. Pressure (Pa) = height (m) × density (kg/m³) × $g$ (10 N/kg). This is the pressure <b>due to the liquid</b>; the <b>total</b> pressure at that depth adds the atmospheric pressure on the surface. The <b>difference</b> in pressure between two depths is $\\Delta P = \\Delta h \\rho g$ with $\\Delta h$ the difference in depth — the atmosphere cancels out.</p>"
            "<p>The June 2025 report (Q1(a)(i), finding a height from a pressure): most candidates rearranged correctly, but some used <b>10 for the density of water</b> rather than $10^3$, and got <b>35 m</b> for the depth of a pool — \"the height of a large building\". The examiners' advice: \"<b>look at the result of a calculation to see if the value makes sense</b>\". The sense check: <b>10 m of water is about 100 kPa</b>, one atmosphere; a swimming pool is 1–3 m, so 10–30 kPa; the deepest ocean, 11 km, about 110 MPa.</p>",
        ),
        worked(
            "Depth from pressure",
            "The pressure due to the water at the bottom of a swimming pool is 35 kPa. Density of water = 1000 kg/m³, $g = 10$ N/kg. Calculate the depth of the pool. (2 marks)",
            [
                "$P = h \\rho g$, so $h = P \\div (\\rho g) = 35\\,000 \\div (1000 \\times 10)$.",
                "$h = 3.5$ m — a sensible depth for a pool. (With $\\rho = 10$ the answer would be 350 m: the 2025 mistake.)",
            ],
        ),
        practice("The liquid-column equation", [
            numeric("fm-n11-q1", "Calculate the pressure due to the sea water at a depth of 25 m. Density of sea water = 1030 kg/m³; $g = 10$ N/kg.", 257500, "Pa",
                    "$P = h \\rho g$.",
                    ewau(r"P = h \rho g", r"P = 25 \times 1030 \times 10", "257\\,500", "Pa (about 2.6 atmospheres)")),
            numeric("fm-n11-q2", "A diver moves from a depth of 4.0 m to a depth of 14.0 m in fresh water. Calculate the increase in pressure on the diver. ($\\rho = 1000$ kg/m³, $g = 10$ N/kg)", 100000, "Pa",
                    "$\\Delta P = \\Delta h \\rho g$ with $\\Delta h = 10$ m.",
                    [r"$\Delta h = 14.0 - 4.0 = 10.0$ m"] + ewau(r"\Delta P = \Delta h \rho g", r"\Delta P = 10.0 \times 1000 \times 10", "100\\,000", "Pa")),
            numeric("fm-n11-q3", "The pressure due to a liquid at a depth of 0.50 m is 6800 Pa ($g = 10$ N/kg). Calculate the density of the liquid.", 1360, "kg/m³",
                    "$\\rho = P \\div (h g)$.",
                    ewau(r"\rho = P \div (h g)", r"\rho = 6800 \div (0.50 \times 10)", "1360", "kg/m³")),
            numeric("fm-n11-q4", "The total pressure at the bottom of a tank of water is 128 kPa. Atmospheric pressure is 100 kPa. Calculate the depth of the water. ($\\rho = 1000$ kg/m³, $g = 10$ N/kg)", 2.8, "m",
                    "Subtract the atmosphere first: the liquid's share is 28 kPa.",
                    [r"pressure due to the water $= 128\,000 - 100\,000 = 28\,000$ Pa"] + ewau(r"h = P \div (\rho g)", r"h = 28\,000 \div (1000 \times 10)", "2.8", "m")),
            choice("fm-n11-q5", "A student calculates the depth of a pond as 400 m from $P = h \\rho g$. The most likely mistake is…",
                   ["using $g = 10$ N/kg", "using 10 instead of 1000 for the density of water (the depth is 4 m)", "forgetting the atmosphere", "using kPa"], 1,
                   "2025: look at the result and ask whether it makes sense."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N12 · Upthrust, floating and sinking [P]
# ---------------------------------------------------------------------

section_n12 = section(
    "upthrust-floating", "nn", "Upthrust equals the weight of fluid displaced; floating and sinking", "15.15P–15.17P",
    equations=[r"\text{upthrust} = \text{weight of fluid displaced}", r"\text{floats if upthrust can equal weight}"],
    blurb="Any object in a fluid feels an upward force — the upthrust — because the pressure on its lower surface is greater than on its upper surface. The upthrust equals the weight of the fluid the object displaces. If that can match the object's weight before it is fully under, it floats; if even fully immersed it cannot, the object sinks.",
    tags=["P"],
    checklist=[
        "Explain why there is an upthrust on an object in a fluid",
        "State that the upthrust equals the weight of fluid displaced",
        "Explain floating and sinking in terms of upthrust and weight, or of density",
    ],
    parts=[
        explain(
            "Where upthrust comes from, and what decides floating",
            diagram(dg.upthrust_svg(), 660, 284, "A submerged block with short pressure arrows on its top face and longer ones on its bottom face, and the free-body diagram of upthrust against weight.") +
            "<p><b>Why there is an upthrust</b> (15.15P): pressure in a fluid <b>increases with depth</b>, so the pressure on the <b>bottom</b> face of a submerged object is <b>greater</b> than on its <b>top</b> face. The forces on the sides cancel, but the upward force on the bottom is larger than the downward force on the top, leaving a <b>resultant upward force: the upthrust</b>. It acts on anything in a fluid — partly or fully immersed, in a liquid or a gas (a helium balloon is pushed up by the air).</p>"
            "<p><b>How big it is</b> (15.16P): the upthrust equals the <b>weight of the fluid displaced</b> by the object — the weight of the fluid that would have filled the space the object takes up. A 1 m³ block fully under water displaces 1000 kg of water, so the upthrust is 10 000 N whatever the block is made of. So an object weighed in air and then in water seems to <b>lose weight</b>: the loss is the upthrust, which is the weight of water displaced (the June 2025 Q9(a) chain).</p>"
            "<p><b>Floating and sinking</b> (15.17P): an object floats when the <b>upthrust equals its weight</b>. It sinks into the fluid until it has displaced fluid weighing as much as itself; if that happens before it is fully under, it <b>floats</b> with the rest above the surface; if even fully immersed the displaced fluid weighs less than the object, upthrust < weight and it <b>sinks</b>. In terms of density: an object <b>less dense</b> than the fluid floats (it can displace its own weight of fluid with only part of its volume); one <b>denser</b> sinks. A steel ship floats because the hull and the air inside it together are less dense than water — its shape displaces a large volume. The June 2022 report (Q3(c), a wood sample in water): \"wood is <b>less dense</b> than water and would <b>float</b>\" scored, but the second mark, \"<b>less water would be displaced</b>\" (than the wood's own volume), was rarely given.</p>",
        ),
        worked(
            "Fresh water and sea water",
            "A ball floats in fresh water and then in sea water. (a) Compare the upthrust on the ball in the two liquids. (b) Explain why less of the ball is under the surface in sea water. (4 marks)",
            [
                "(a) The upthrusts are <b>equal</b>: the ball floats in both, so in each case the upthrust equals the <b>weight of the ball</b> (June 2023 Q6(c)(i)).",
                "(b) Floating: the <b>weight of the ball = the weight of water displaced</b>.",
                "Sea water is <b>more dense</b> than fresh water…",
                "…so a <b>smaller volume</b> of sea water has the same weight, so <b>less sea water needs to be displaced</b> to support the ball, and less of the ball is below the surface (Q6(c)(ii)).",
            ],
        ),
        practice("Upthrust, floating and sinking", [
            written("fm-n12-q1", "Explain why there is an upward force on a stone held under water. (3)",
                    marks(["Pressure in the water <b>increases with depth</b>.", "So the pressure on the <b>bottom</b> of the stone is <b>greater</b> than on the top; the sideways forces cancel.", "The upward force on the bottom is larger than the downward force on the top, giving a <b>resultant upward force</b> — the upthrust."]), lines=3),
            choice("fm-n12-q2", "The upthrust on an object in a fluid is equal to…",
                   ["the weight of the object", "the weight of the fluid displaced by the object", "the volume of the object", "the pressure at its base"], 1,
                   "Weight of fluid displaced — in a liquid or a gas."),
            numeric("fm-n12-q3", "A block of volume 0.0020 m³ is fully submerged in water (density 1000 kg/m³; $g = 10$ N/kg). Calculate the upthrust on it.", 20, "N",
                    "Mass of water displaced $= \\rho V$; weight $= m g$.",
                    [r"mass of water displaced $= \rho V = 1000 \times 0.0020 = 2.0$ kg", r"upthrust = weight of water displaced $= 2.0 \times 10 = 20$ N"]),
            written("fm-n12-q4", "A block of wood of density 600 kg/m³ is placed in water. Explain, in terms of upthrust and weight, why it floats. (3)",
                    marks(["The wood is <b>less dense</b> than water, so its weight is less than the weight of the same volume of water.", "As it sinks into the water, the upthrust (the <b>weight of water displaced</b>) grows until it <b>equals the weight</b> of the wood…", "…which happens before the block is fully under — only part of its volume (60 %) needs to be submerged to displace its own weight of water — so it floats with the rest above the surface."]), lines=3),
            choice("fm-n12-q5", "A steel ship floats but a steel ball sinks because…",
                   ["the ship is lighter", "the ship's shape displaces a large volume of water, enough to weigh as much as the ship, before it is submerged; the ball cannot displace its own weight of water", "ships use special steel", "the sea is denser than fresh water"], 1,
                   "Hull plus air inside is less dense than water overall."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N13 · Key words
# ---------------------------------------------------------------------

DEFINITIONS = [
    ("Distortion", "A <b>change in the shape</b> of an object (stretching, compressing or bending) caused by forces.", "\"breaking\""),
    ("Elastic distortion", "A distortion that is <b>reversed when the forces are removed</b>: the object returns to its original shape and size.", "\"it stretches\""),
    ("Inelastic distortion", "A distortion that is <b>permanent</b>: the object does <b>not</b> return to its original shape when the forces are removed.", "\"plastic\" on its own"),
    ("Extension", "The <b>increase in length</b> of a spring: stretched length − original length.", "the length of the spring"),
    ("Spring constant", "The <b>force needed per unit extension</b>, $k = F \\div x$, in N/m — a measure of the spring's stiffness.", "\"how springy it is\""),
    ("Hooke's law", "The extension of a spring is <b>directly proportional to the force</b> applied, up to the limit of proportionality: $F = kx$.", "\"force = extension\""),
    ("Limit of proportionality", "The point on a force–extension graph beyond which the line is <b>no longer straight</b>: extension stops being proportional to force.", "confusing with breaking point"),
    ("Elastic limit", "The point beyond which a spring <b>no longer returns</b> to its original length when unloaded (its distortion becomes inelastic).", "\"where it snaps\""),
    ("Pressure (Physics only)", "The <b>force per unit area</b> acting at right angles to a surface: $P = F \\div A$, in pascals (N/m²).", "\"force\""),
    ("Fluid (Physics only)", "A <b>liquid or a gas</b>: a substance that can flow and takes the shape of its container.", "\"a liquid\" only"),
    ("Atmospheric pressure (Physics only)", "The pressure exerted by the <b>weight of the air above</b> a surface; about 100 kPa at sea level, decreasing with height.", "\"air\""),
    ("Upthrust (Physics only)", "The <b>upward force</b> on an object in a fluid, caused by the pressure being greater on its lower surface than its upper; equal to the <b>weight of fluid displaced</b>.", "\"the object being light\""),
    ("Floating (Physics only)", "An object floats when the <b>upthrust equals its weight</b> — it displaces its own weight of fluid before being fully immersed (it is less dense than the fluid).", "\"it is light\""),
]


def definitions_table():
    html = "<table class='tbl'><tr><th>Term</th><th>What to write (mark-scheme form)</th><th>Not this</th></tr>"
    for term, definition, wrong in DEFINITIONS:
        html += "<tr><td><b>" + term + "</b></td><td>" + definition + "</td><td>" + wrong + "</td></tr>"
    html += "</table>"
    return html


section_keywords = section(
    "keywords-matter", "nn", "Key words: state what is meant by…", "15.1–15.17P",
    equations=[r"\text{definition, word for word}"],
    blurb="One-mark definitions in the form of words the mark schemes credit. The two that lose marks most: extension is the change in length, not the length; and upthrust equals the weight of fluid displaced, not the weight of the object.",
    checklist=[
        "Define distortion, elastic and inelastic distortion, extension, spring constant and Hooke's law",
        "Define the limit of proportionality and the elastic limit",
        "Define pressure, fluid, atmospheric pressure, upthrust and floating",
    ],
    parts=[
        explain("The definitions", "<p>\"<b>State what is meant by</b>\" asks for the definition. Learn these as sentences.</p>" + definitions_table()),
        practice("Key words", [
            written("fm-kw-q1", "State what is meant by the spring constant of a spring. (1)",
                    marks(["The <b>force needed per unit (metre) of extension</b>, $k = F \\div x$, in N/m."]), lines=1),
            written("fm-kw-q2", "State what is meant by an inelastic distortion. (1)",
                    marks(["A change of shape that is <b>permanent</b>: the object does <b>not return</b> to its original shape when the forces are removed."]), lines=1),
            choice("fm-kw-q3", "Upthrust is equal to…",
                   ["the weight of the object", "the weight of the fluid displaced", "the volume of fluid displaced", "the density of the fluid"], 1,
                   "Weight of fluid displaced.", tags=["P"]),
            written("fm-kw-q4", "State what is meant by pressure. (1)",
                    marks(["<b>Force per unit area</b>, acting at right angles to a surface ($P = F \\div A$)."]), lines=1, tags=["P"]),
            choice("fm-kw-q5", "The extension of a spring is…",
                   ["its length", "the increase in its length from its original length", "its length in metres", "the force on it"], 1,
                   "Change in length."),
            choice("fm-kw-q6", "A fluid is…", ["a liquid", "a gas", "a liquid or a gas", "water"], 2, "Both flow and take the shape of their container.", tags=["P"]),
        ]),
    ],
)

KW_HOME = {"Pressure": "pressure-nn", "Fluid": "fluid-pressure", "Atmospheric pressure": "atmospheric-height", "Upthrust": "upthrust-floating", "Floating": "upthrust-floating"}


def kw_fact(term, definition):
    name = term.replace(" (Physics only)", "")
    stem = name if name.startswith("Hooke") else name[0].lower() + name[1:]
    return fact("State what is meant by: " + stem + ".", definition, KW_HOME.get(name, "keywords-matter"))


FACTS_KW = [kw_fact(term, definition) for term, definition, wrong in DEFINITIONS]

SECTIONS = [section_n1, section_n2, section_n3, section_n4, section_n5, section_n6, section_n7, section_n8, section_n9, section_n10, section_n11, section_n12, section_keywords]
