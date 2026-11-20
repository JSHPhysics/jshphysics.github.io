"""
fm_tricky.py — Topic 15 (Forces and matter): the tricky bits T1–T7 and
the flashcards.

T1 Extension, not length               T5 Pressure–height and pressure–depth graphs [P]
T2 Force–extension graphs the hard way T6 Upthrust the hard way [P]
T3 The spring practical 6-marker       T7 Floating and sinking in the mark-scheme words [P]
T4 Pressure calculations the hard way [P]
"""

from revlib import (
    axis, choice, curve, dashed, diagram, ewau, explain, fact, graph, group, label, line,
    mark, mark_scheme, marks, numeric, practice, section, worked, written,
)
import fm_diagrams as dg

# ---------------------------------------------------------------------
# T1 · Extension, not length
# ---------------------------------------------------------------------

section_t1 = section(
    "extension-not-length", "tricky", "Extension, not length — and in metres", "15.3, 15.6",
    equations=[r"x = l - l_0", r"1 \text{ mm} = 10^{-3} \text{ m}, \ 1 \text{ cm} = 10^{-2} \text{ m}"],
    blurb="Half the lost marks in this topic are one of two slips: using the length of the spring where the equation wants the extension, and leaving the extension in centimetres or millimetres when the spring constant is in newtons per metre. The 2023 and 2025 reports show both, and show what partial credit remains.",
    checklist=[
        "Turn a pair of lengths, or a pair of ruler readings, into an extension",
        "Convert mm and cm to m before using $F = kx$ or $E = \\tfrac{1}{2} k x^2$",
        "Recognise an answer that is 100 or 1000 times out and know which conversion was missed",
    ],
    parts=[
        explain(
            "Two slips and what they cost",
            "<table class='tbl'><tr><th>Slip</th><th>Where it showed</th><th>Cost</th><th>Avoid it</th></tr>"
            "<tr><td>using the <b>length</b> as $x$</td><td>a spring \"12 cm long with a 4 N load\" — the extension is the loaded length minus the unloaded length, which the question gives elsewhere</td><td>the substitution mark and the answer</td><td>write $x = l - l_0$ first and find both lengths before anything else</td></tr>"
            "<tr><td>$x$ left in <b>cm</b> in $F = kx$</td><td>June 2025 Q8(b)(ii): \"use the extension in cm and give the value as N/m\"</td><td>answer 100 times too small; one mark of two</td><td>cm → m is ÷ 100; mm → m is ÷ 1000</td></tr>"
            "<tr><td>$x$ left in cm in $E = \\tfrac{1}{2} k x^2$</td><td>June 2025 Q8(b)(i): \"forget to convert the extension from cm to m\"</td><td>answer 100 times too large (the square makes it 10 000, but $k$ was also found in cm); two marks of three for clear working</td><td>convert <b>before</b> squaring</td></tr>"
            "<tr><td>mm not converted in $F = kx$</td><td>June 2023 Q7(a)(i): 1600 N instead of 1.6 N</td><td>two marks of three</td><td>6.2 mm = $6.2 \\times 10^{-3}$ m</td></tr></table>"
            "<p>Ruler readings work the same way: the June 2023 scheme (Q7(a)(ii)) gave one mark each for reading the position with <b>no load</b>, reading it <b>with the load</b>, and <b>subtracting</b>. If the question gives you the spring constant and the force instead, the change in length comes from $x = F \\div k$ — the alternative the scheme allowed (\"0.39 = 260 × change in length\", 1.5 mm, <b>with the unit shown</b>).</p>",
        ),
        worked(
            "Length to extension to metres",
            "A spring is 50 mm long unloaded and 68 mm long carrying a 4.5 N weight. Calculate its spring constant in N/m. (3 marks)",
            [
                "Extension $x = 68 - 50 = 18$ mm.",
                "$x = 18 \\times 10^{-3} = 0.018$ m.",
                "$k = F \\div x = 4.5 \\div 0.018 = 250$ N/m.",
            ],
        ),
        practice("Extension, not length", [
            numeric("fm-t1-q1", "A spring is 15.0 cm long with no load and 21.0 cm long with a load of 3.0 N. Calculate the spring constant.", 50, "N/m",
                    "Extension = 6.0 cm = 0.060 m.",
                    [r"$x = 21.0 - 15.0 = 6.0$ cm $= 0.060$ m"] + ewau(r"k = F \div x", r"k = 3.0 \div 0.060", "50", "N/m")),
            numeric("fm-t1-q2", "A spring of spring constant 260 N/m is pressed with a force of 0.39 N. Calculate the change in its length, in mm.", 1.5, "mm",
                    "$x = F \\div k$ in metres, then × 1000.",
                    [r"$x = F \div k = 0.39 \div 260 = 1.5 \times 10^{-3}$ m"] + ewau(r"x = F \div k", r"x = 0.39 \div 260 = 1.5 \times 10^{-3} \text{ m}", "1.5", "mm (the June 2023 Q7(a)(ii) alternative; the unit must be shown)")),
            choice("fm-t1-q3", "A student uses $x = 4$ cm in $E = \tfrac{1}{2} k x^2$ with k in N/m. The energy comes out…",
                   ["100 times too large", "10 000 times too large ($4^2 = 16$ instead of $0.04^2 = 0.0016$)", "correct", "100 times too small"], 1,
                   "The square makes the cm slip worse: convert first."),
            numeric("fm-t1-q4", "The pointer on a spring reads 3.2 cm with no load and 9.7 cm with a 2.6 N load. Calculate the energy stored in the spring.", 0.0845, "J",
                    "Extension in m, then $\\tfrac{1}{2} F x$.",
                    [r"$x = 9.7 - 3.2 = 6.5$ cm $= 0.065$ m"] + ewau(r"E = \tfrac{1}{2} F x", r"E = \tfrac{1}{2} \times 2.6 \times 0.065", "0.085", "J (0.0845)")),
            choice("fm-t1-q5", "A spring constant comes out as 2.5 N/m for a stiff lab spring that needs about 2.5 N to stretch it 1 cm. The slip was…",
                   ["the force in kN", "the extension in cm: 2.5 ÷ 1 instead of 2.5 ÷ 0.01, so the true value is 250 N/m", "the length used", "no slip"], 1,
                   "100 times too small = cm left in."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T2 · Force–extension graphs the hard way
# ---------------------------------------------------------------------

t2_lin = [[0, 0], [5, 2.5], [10, 5], [15, 7.5], [20, 10]]
t2_curve = [[round(20 + 1.5 * i, 2), round(10 + 3.2 * (1 - 2.0 ** (-(1.5 * i) / 5.0)), 2)] for i in range(11)]
graph_t2 = graph(
    axis("extension in cm", 40, 5), axis("force in N", 14, 2),
    [line(t2_lin), curve(t2_curve), dashed([[20, 0], [20, 10]]), dashed([[0, 10], [20, 10]])],
    "Force against extension: a straight line from the origin to 20 cm and 10 N, then a curve flattening towards 13 N at 35 cm.",
)

compress_pts = [[0, 0], [1, 30], [2, 60], [3, 90], [4, 120]]
graph_compress = graph(
    axis("compression in mm", 5, 1), axis("force in N", 140, 20),
    [line(compress_pts)],
    "Force against compression for a stiff spring: a straight line from the origin to 4 mm and 120 N.",
)

section_t2 = section(
    "fx-graphs-hard", "tricky", "Force–extension graphs the hard way: gradient, area, limits and compressions", "15.4, 15.5",
    equations=[r"k = \text{gradient (linear part only)}", r"E = \text{area} = \tfrac{1}{2} F x \text{ (linear part)}"],
    blurb="A force–extension graph answers three questions — how stiff (the gradient), how much energy (the area), and where Hooke's law stops (the end of the straight line) — but only if you read the right part. The gradient is k only on the straight part; the area is a triangle only on the straight part; and a compression graph is the same picture with a different label.",
    checklist=[
        "Find k from the gradient of the linear part, with the extension converted to metres",
        "Find the energy stored from the area under the line, as a triangle on the linear part or by counting beyond it",
        "Locate the limit of proportionality and say what changes past it",
    ],
    parts=[
        explain(
            "Three readings from one graph",
            "<table class='tbl'><tr><th>Wanted</th><th>Read</th><th>Watch</th></tr>"
            "<tr><td>spring constant</td><td><b>gradient</b> of the <b>straight</b> part: pick two points far apart on the line, $k = \\Delta F \\div \\Delta x$</td><td>$x$ in metres; if extension is on the $y$-axis the gradient is $1 \\div k$; beyond the limit the gradient is not $k$ (the spring is not obeying Hooke's law there)</td></tr>"
            "<tr><td>energy stored / work done</td><td><b>area under the line</b> up to the extension asked for: on the straight part a <b>triangle</b>, $\\tfrac{1}{2} F x$ (= $\\tfrac{1}{2} k x^2$)</td><td>past the limit the area is a triangle plus a curved strip — estimate by counting squares; the June 2025 scheme (Q8(b)(i)) gave the three marks for converting to metres, reading the correct points and calculating the area</td></tr>"
            "<tr><td>limit of proportionality</td><td>the point where the <b>straight line ends</b></td><td>beyond it: non-linear, Hooke's law no longer applies, each extra newton gives more extension than before; the elastic limit is a little further on</td></tr></table>"
            "<p><b>Compression graphs</b> are read the same way: force against compression (how much shorter), with the same $k$ for the same spring — 2023 Q7 was a spring <b>pressed</b> by 6.2 mm. <b>Check the axes and their units</b> before reading anything off. A graph that is a straight line but <b>not through the origin</b> is linear but not proportional — say so if asked.</p>",
        ),
        worked(
            "All three readings",
            "The graph shows force against extension for a spring. (a) Find the spring constant. (b) Find the energy stored at an extension of 20 cm. (c) State what happens beyond 20 cm. (5 marks)",
            [
                "(a) Straight part: 10 N at 20 cm $= 0.20$ m; $k = 10 \\div 0.20 = 50$ N/m.",
                "(b) Area of the triangle to 20 cm: $E = \\tfrac{1}{2} \\times 10 \\times 0.20$…",
                "…$E = 1.0$ J (check: $\\tfrac{1}{2} \\times 50 \\times 0.20^2 = 1.0$ J).",
                "(c) 20 cm is the <b>limit of proportionality</b>: beyond it the graph is <b>non-linear</b>, extension is no longer proportional to force…",
                "…each extra newton produces a larger extension than before, and the gradient there is no longer the spring constant.",
            ],
            graph=graph_t2,
        ),
        practice("Force–extension graphs", [
            group("fm-t2-q1", "Use the force–extension graph (straight to 20 cm, then curved).", [
                numeric("fm-t2-q1a", "Calculate the energy stored at an extension of 10 cm.", 0.25, "J",
                        "Read the force at 10 cm on the straight line (5 N); triangle area with $x$ in m.",
                        [r"at 10 cm, $F = 5$ N; $x = 0.10$ m"] + ewau(r"E = \tfrac{1}{2} F x", r"E = \tfrac{1}{2} \times 5 \times 0.10", "0.25", "J"), label="a"),
                choice("fm-t2-q1b", "A student finds the spring constant from the points (35 cm, 12.8 N): $k = 12.8 \\div 0.35 = 37$ N/m. This is wrong because…",
                       ["the extension should be in cm", "the point is beyond the limit of proportionality, where the gradient is not the spring constant (use the straight part: 50 N/m)", "the force should be doubled", "it is not wrong"], 1,
                       "Only the linear part gives k.", label="b"),
                choice("fm-t2-q1c", "The energy stored at 30 cm is…",
                       ["$\\tfrac{1}{2} \\times 12.4 \\times 0.30 = 1.86$ J exactly", "more than $\\tfrac{1}{2} \\times 12.4 \\times 0.30 = 1.86$ J, because the curve lies above the straight line from the origin to that point — count squares (about 2.1 J)", "1.0 J", "zero because Hooke's law does not apply"], 1,
                       "Triangle to 20 cm (1.0 J) plus the strip under the curve (about 1.1 J): more than the single triangle.", label="c"),
            ], graph=graph_t2),
            group("fm-t2-q2", "The graph shows force against compression for a stiff spring in a bicycle pump.", [
                numeric("fm-t2-q2a", "Calculate the spring constant.", 30000, "N/m",
                        "4 mm = 0.004 m.",
                        [r"at 4 mm, $F = 120$ N; $x = 4 \times 10^{-3}$ m"] + ewau(r"k = F \div x", r"k = 120 \div (4 \times 10^{-3})", "30\\,000", "N/m"), label="a"),
                numeric("fm-t2-q2b", "Calculate the energy stored when the spring is compressed by 3 mm.", 0.135, "J",
                        "$\\tfrac{1}{2} F x$ with $F = 90$ N at 3 mm.",
                        [r"at 3 mm, $F = 90$ N; $x = 3 \times 10^{-3}$ m"] + ewau(r"E = \tfrac{1}{2} F x", r"E = \tfrac{1}{2} \times 90 \times 3 \times 10^{-3}", "0.135", "J"), label="b"),
            ], graph=graph_compress),
            choice("fm-t2-q3", "On a graph of extension (y) against force (x), the spring constant is…",
                   ["the gradient", "1 ÷ the gradient", "the area", "the intercept"], 1,
                   "Axes swapped: gradient = $x \\div F = 1/k$."),
            written("fm-t2-q4", "A force–extension graph for a rubber band is a curve from the origin. State what this shows, and how the energy stored could still be found. (2)",
                    marks(["The extension is <b>not proportional</b> to the force — the band does <b>not obey Hooke's law</b> (no linear region, so no single spring constant).", "The energy stored is still the <b>area under the curve</b>, found by counting squares."]), lines=2),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T3 · The spring practical 6-marker
# ---------------------------------------------------------------------

section_t3 = section(
    "spring-plan", "tricky", "Planning the spring practical: the 6-mark method and the seven steps", "15.6",
    equations=[r"\text{independent: force; dependent: extension}", r"F = kx \Rightarrow \text{straight line through the origin, gradient } k"],
    blurb="A method question on the spring practical wants named apparatus, the two readings that make an extension, a range of loads, the graph and what to take from it, and one accuracy point. The seven steps give all of it in order; the trap is to describe measuring the length rather than the extension.",
    checklist=[
        "Plan the investigation with the seven steps: variables, relationship, change, measure, use, accuracy, repeat",
        "Say how the result is used: plot force against extension, straight line through the origin, gradient = spring constant, area = work done",
        "Write a 6-mark method from the plan",
    ],
    parts=[
        explain(
            "The seven steps for a spring",
            "<table class='tbl'><tr><th>Step</th><th>How does the extension of a spring depend on the force applied?</th></tr>"
            "<tr><td><b>1 Variables</b></td><td>independent: the <b>force</b> (the weight hung on the spring); dependent: the <b>extension</b>; control: the same spring, loads added one at a time without jerking, the same ruler</td></tr>"
            "<tr><td><b>2 Relationship</b></td><td>$F = k x$: force proportional to extension (within the limit); a graph of force against extension should be a <b>straight line through the origin</b> with gradient $k$</td></tr>"
            "<tr><td><b>3 Change</b></td><td>hang 100 g masses one at a time: 1 N, 2 N, … up to 6 N or more (at least six values, evenly spaced)</td></tr>"
            "<tr><td><b>4 Measure</b></td><td>the position of a pointer on the bottom of the spring against a vertical mm ruler, <b>with no load and with each load</b>; extension = reading − no-load reading; force = weight of the masses ($W = mg$)</td></tr>"
            "<tr><td><b>5 Use</b></td><td>plot force against extension; a straight line through the origin shows Hooke's law; the <b>gradient is the spring constant</b>; the <b>area</b> under the line to any extension is the work done stretching the spring</td></tr>"
            "<tr><td><b>6 Accuracy</b></td><td>read the pointer <b>at eye level</b> (no parallax); clamp the ruler vertical and the stand to the bench; let the spring settle before reading; stay <b>below the elastic limit</b> (check the spring returns to its no-load reading); wear eye protection</td></tr>"
            "<tr><td><b>7 Repeat</b></td><td>repeat the readings while unloading (and again) and take a mean extension for each force</td></tr></table>"
            "<p>In the 2022–2025 Paper 2H series read for this page the spring practical was not the 6-mark method question, but its parts were marked: the 2023 three marks for <b>two readings and a subtraction</b>, and the 2023 accuracy mark for a change that locates the end of the spring and <b>how it is used</b> (\"ignore unqualified references to accuracy or precision\" — say <i>what</i> the pointer or eye-level reading prevents: parallax).</p>",
        ),
        worked(
            "The 6-mark method",
            "Describe an investigation to find the spring constant of a spring. (6 marks)",
            [
                "Clamp the spring from a stand with a <b>metre ruler</b> (mm) clamped vertically beside it and a pointer fixed to the bottom of the spring; read the pointer's position with <b>no load</b>.",
                "Hang a 100 g mass (1.0 N) on the spring, let it settle, and read the pointer again; <b>extension = reading − no-load reading</b>.",
                "Add masses one at a time to at least 6 N, recording the extension for each force.",
                "Read the pointer <b>at eye level</b> to avoid parallax; check the spring returns to the no-load reading when unloaded so that the elastic limit was not passed.",
                "Plot <b>force against extension</b>: a straight line through the origin shows the extension is proportional to the force.",
                "The <b>spring constant is the gradient</b> of the line ($k = F \\div x$ with $x$ in metres); repeat while unloading and use the mean.",
            ],
        ),
        practice("Planning the spring practical", [
            written("fm-t3-q1", "Plan an investigation into how the extension of a spring depends on the force applied to it. (6)",
                    mark_scheme([
                        ("Variables", "Independent: the force (weight hung on the spring); dependent: the extension; control: the same spring and ruler, loads added gently."),
                        ("Relationship", "$F = kx$: a graph of force against extension should be a straight line through the origin, gradient $k$."),
                        ("Change", "Add 100 g masses one at a time to give forces of 1 N to 6 N or more."),
                        ("Measure", "Pointer position on a vertical mm ruler with no load and with each load; extension = reading − no-load reading."),
                        ("Use", "Plot force against extension; straight line through the origin confirms Hooke's law; gradient = spring constant; area = work done."),
                        ("Accuracy", "Read at eye level with a pointer (no parallax); ruler vertical; let the spring settle; stay below the elastic limit."),
                        ("Repeat", "Repeat on unloading and take a mean extension for each force."),
                    ], total=6, extra=["Any six of the seven points."]), lines=7),
            choice("fm-t3-q2", "Which accuracy statement would the 2023 examiners credit?",
                   ["Be accurate", "Use a pointer on the spring and read it at eye level so there is no parallax error", "Measure precisely", "Use a good ruler"], 1,
                   "Say what the change is and what it prevents; unqualified 'accuracy' is ignored."),
            written("fm-t3-q3", "A student records the length of the spring for each load and plots force against length. Explain what is wrong and how the spring constant can still be found. (2)",
                    marks(["Hooke's law is about the <b>extension</b>, so force against length does not pass through the origin: the <b>gradient is still $k$</b> (each extra newton adds the same extra length)…", "…but to get extensions, <b>subtract the no-load length</b> from every reading and replot (or read $k$ from the gradient of the force–length line directly)."]), lines=2),
            choice("fm-t3-q4", "Why are readings also taken while the masses are removed one at a time?",
                   ["To save time", "To check the spring returns to its original length (no inelastic distortion) and to give repeat readings for a mean", "Because the masses are heavy", "To find the elastic limit"], 1,
                   "Unloading readings are the repeat and the elastic-limit check."),
            numeric("fm-t3-q5", "In the practical, six 100 g masses stretch the spring from a pointer reading of 215 mm to 275 mm. Taking $g = 10$ N/kg, calculate the spring constant.", 100, "N/m",
                    "Force = 0.6 kg × 10; extension = 60 mm.",
                    [r"$F = 0.600 \times 10 = 6.0$ N; $x = 275 - 215 = 60$ mm $= 0.060$ m"] + ewau(r"k = F \div x", r"k = 6.0 \div 0.060", "100", "N/m")),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T4 · Pressure calculations the hard way [P]
# ---------------------------------------------------------------------

section_t4 = section(
    "pressure-hard", "tricky", "Pressure calculations the hard way: total area, square millimetres, force from pressure, and pressure differences", "15.10P, 15.11P, 15.8P",
    equations=[r"A_{\text{total}} = n \times A_{\text{one}}", r"1 \text{ mm}^2 = 10^{-6} \text{ m}^2, \ 1 \text{ cm}^2 = 10^{-4} \text{ m}^2"],
    blurb="$P = F/A$ is easy until the area is in the wrong unit, split over four feet, or on both sides of a surface. The four papers' errors: forgetting to multiply by four hooves (2022), leaving mm² in (2025 — a million times out), not rounding to two significant figures when asked (2024), and using the pressure difference where the question wanted the force of the cabin air alone (2023).",
    tags=["P"],
    checklist=[
        "Use the total contact area: number of feet, legs or tyres × the area of one",
        "Convert cm² and mm² to m² (squared conversions) before substituting",
        "Use $F = PA$, and a pressure difference when there is fluid on both sides",
    ],
    parts=[
        explain(
            "Four papers, four traps",
            "<table class='tbl'><tr><th>Trap</th><th>What the examiners saw</th><th>What to do</th></tr>"
            "<tr><td><b>Total area</b></td><td>June 2022 Q4(a)(i): \"the most common mistake was not correctly calculating the area as 4 × area of one hoof\" (1 of 2 marks)</td><td>count the contacts: four hooves, two feet, three legs of a stool; area = $n \\times$ one</td></tr>"
            "<tr><td><b>mm² and cm²</b></td><td>June 2025 Q1(c): forgetting to convert mm² to m² gave \"an answer that was a million times too large\" (1 of 2)</td><td>square the length conversion: 1 mm = $10^{-3}$ m so 1 mm² = $10^{-6}$ m²; 1 cm² = $10^{-4}$ m²</td></tr>"
            "<tr><td><b>Rounding</b></td><td>June 2024 Q4(b): substitution (1), evaluation 576 N (1), <b>rounded to 2 s.f.</b> 580 N (1)</td><td>when the question says \"to 2 significant figures\", the rounding is a mark on its own</td></tr>"
            "<tr><td><b>Difference</b></td><td>June 2023 Q4(a)(i)–(ii): net pressure $80\\,000 - 23\\,000 = 57\\,000$ Pa; the force of the <b>cabin air</b> on the window used 80 000 (substituting 57 000 there earned only the substitution mark)</td><td>read which force the question wants: one side's pressure, or the net</td></tr></table>"
            "<p>And the explanation version (2022 Q4(a)(ii)): larger area → the <b>weight (force) is spread over a larger area</b> → <b>less pressure</b>. Two marks: the larger area, and the weight spread over it giving less pressure; \"mass spread out\" earned neither.</p>",
        ),
        worked(
            "Four feet and square millimetres",
            "An elephant weighs 50 000 N and stands on four feet, each with an area of 1200 cm². A woman weighing 600 N stands on one stiletto heel of area 1.0 cm². Compare the pressures. (4 marks)",
            [
                "Elephant: total area $= 4 \\times 1200 = 4800$ cm² $= 0.48$ m².",
                "$P = F \\div A = 50\\,000 \\div 0.48 = 104\\,000$ Pa (100 kPa, 2 s.f.).",
                "Heel: $A = 1.0$ cm² $= 1.0 \\times 10^{-4}$ m²; $P = 600 \\div (1.0 \\times 10^{-4}) = 6.0 \\times 10^{6}$ Pa.",
                "The heel exerts about <b>60 times</b> the pressure of the elephant, because its force acts on a far smaller area.",
            ],
        ),
        practice("Pressure the hard way", [
            numeric("fm-t4-q1", "A table weighs 320 N and stands on four legs. Each leg has a base of area 16 cm². Calculate the pressure on the floor.", 50000, "Pa",
                    "Total area = 4 × 16 cm², in m².",
                    [r"$A = 4 \times 16 = 64$ cm² $= 64 \times 10^{-4} = 6.4 \times 10^{-3}$ m²"] + ewau(r"P = F \div A", r"P = 320 \div (6.4 \times 10^{-3})", "50\\,000", "Pa")),
            numeric("fm-t4-q2", "A nail is hit with a force of 50 N. The point of the nail has an area of 0.25 mm². Calculate the pressure at the point, in Pa.", 2e8, "Pa",
                    "0.25 mm² $= 0.25 \\times 10^{-6}$ m².",
                    [r"$A = 0.25 \times 10^{-6} = 2.5 \times 10^{-7}$ m²"] + ewau(r"P = F \div A", r"P = 50 \div (2.5 \times 10^{-7})", r"2.0 \times 10^{8}", "Pa")),
            numeric("fm-t4-q3", "The air inside a car tyre is at 250 kPa and the atmospheric pressure outside is 100 kPa. The inner end of the tyre valve has an area of $1.2 \\times 10^{-5}$ m². Calculate the net force on the valve.", 1.8, "N",
                    "Net pressure × area.",
                    [r"net $P = 250\,000 - 100\,000 = 150\,000$ Pa"] + ewau(r"F = P A", r"F = 150\,000 \times 1.2 \times 10^{-5}", "1.8", "N outward")),
            numeric("fm-t4-q4", "A pressure of $2.3 \\times 10^{5}$ Pa acts on a surface of area $3.1 \\times 10^{-3}$ m². Calculate the force, to 2 significant figures.", 710, "N",
                    "713 N rounds to 710 N.",
                    ewau(r"F = P A", r"F = 2.3 \times 10^{5} \times 3.1 \times 10^{-3}", "713 = 710", "N (2 s.f.)")),
            written("fm-t4-q5", "Explain why a tractor with wide tyres can drive over soft ground that a car with narrow tyres would sink into. (3)",
                    marks(["The wide tyres have a much <b>larger area</b> in contact with the ground.", "The tractor's <b>weight (force) is spread over this larger area</b>.", "Pressure = force ÷ area, so the <b>pressure</b> on the ground is <b>smaller</b> and the ground is not pushed in as far."]), lines=3),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T5 · Pressure–height and pressure–depth graphs [P]
# ---------------------------------------------------------------------

depth_fresh = [[0, 100], [5, 150], [10, 200], [15, 250], [20, 300]]
depth_sea = [[0, 100], [5, 151.5], [10, 203], [15, 254.5], [20, 306]]
graph_depth = graph(
    axis("depth in m", 20, 5), axis("total pressure in kPa", 320, 40),
    [line(depth_fresh), line(depth_sea)],
    "Total pressure against depth: two straight lines from 100 kPa at the surface, fresh water reaching 300 kPa at 20 m and sea water slightly steeper, reaching 306 kPa.",
    labels=[label(10.5, 150, "fresh water: the lower line", "start"), label(5, 232, "sea water: the upper line", "start")],
)

section_t5 = section(
    "pressure-graphs", "tricky", "Pressure–height and pressure–depth graphs: describing, comparing and reading them", "15.7P, 15.12P, 15.13P",
    equations=[r"\text{height: a curve falling, gradient shrinking}", r"\text{depth: a straight line rising from atmospheric pressure}"],
    blurb="Two graphs that look alike and behave differently. Pressure against height in the atmosphere is a curve: it falls, and falls more slowly as the air thins. Pressure against depth in a liquid is a straight line: it rises in proportion to depth, starting from atmospheric pressure at the surface, and a denser liquid gives a steeper line from the same start.",
    tags=["P"],
    checklist=[
        "Describe the pressure–height graph: direction, non-linear, with numbers from the graph",
        "Describe the pressure–depth graph: straight, proportional increase, intercept = atmospheric pressure",
        "Compare the lines for two liquids: steeper for the denser one, same intercept",
    ],
    parts=[
        explain(
            "The two graphs and their marks",
            "<table class='tbl'><tr><th></th><th>Pressure against height (atmosphere)</th><th>Pressure against depth (liquid)</th></tr>"
            "<tr><td><b>Shape</b></td><td>a <b>curve</b> falling: <b>non-linear</b>, the gradient becomes less steep with height</td><td>a <b>straight line</b> rising: linear, pressure proportional to depth (plus the constant atmosphere)</td></tr>"
            "<tr><td><b>Why</b></td><td>less air above → less weight → lower pressure; and the air is less dense higher up, so each km removes less weight</td><td>the weight of the column of liquid above grows in proportion to its height; the liquid's density does not change with depth</td></tr>"
            "<tr><td><b>Intercept</b></td><td>about 100 kPa at sea level</td><td><b>atmospheric pressure</b> at the surface (depth 0), the same whatever the liquid</td></tr>"
            "<tr><td><b>Marks seen</b></td><td>2023 Q4(b): decrease with height (1), non-linear (1), use of numerical data (1); 2024 Q4(c): decreases as height increases / negative correlation (1), non-linear — curved, not proportional, gradient changes (1); a reading within a range; a percentage change</td><td>2022 Q4(c): density up → pressure up (1), <b>steeper gradient</b> (1), still <b>linear</b> (1), <b>same intercept, the air pressure</b> (1)</td></tr></table>"
            "<p><b>Percentage change</b> (2024 Q4(c)(iii)): (new − old) ÷ old × 100 — the scheme gave one mark for the substitution and one for the evaluation, and only one mark for dividing by the new value instead. <b>Reading a graph</b>: say the two values you read and show the subtraction; a reading within the scheme's range scores even if the line is hard to read.</p>",
        ),
        worked(
            "Fresh water and sea water on one graph",
            "The graph shows total pressure against depth for fresh water and sea water. Describe the two lines and explain the differences and similarities. (4 marks)",
            [
                "Both lines are <b>straight</b>: the pressure increases <b>in proportion</b> to the depth, because the weight of liquid above grows with the height of the column.",
                "Both start at <b>100 kPa</b> at the surface — the <b>atmospheric pressure</b>, which is the same whatever the liquid.",
                "The sea-water line is <b>steeper</b> (306 kPa against 300 kPa at 20 m): sea water is <b>denser</b>, so the same column has more weight.",
                "At any depth the sea-water pressure is higher by the extra weight of the denser column above — only 6 kPa at 20 m, because the densities differ by just 3 %.",
            ],
            graph=graph_depth,
        ),
        practice("Pressure graphs", [
            group("fm-t5-q1", "Use the graph of total pressure against depth.", [
                numeric("fm-t5-q1a", "Read the total pressure at a depth of 10 m in fresh water.", 200, "kPa",
                        "Read up from 10 m to the lower line.",
                        ["At 10 m the fresh-water line is at 200 kPa."], label="a"),
                numeric("fm-t5-q1b", "Calculate the percentage increase in total pressure from the surface to 20 m in fresh water.", 200, "%",
                        "$(300 - 100) \\div 100 \\times 100$.",
                        [r"increase $= 300 - 100 = 200$ kPa", r"percentage $= 200 \div 100 \times 100 = 200$ %"], label="b", tolerance=0.03),
                choice("fm-t5-q1c", "Why do both lines start at 100 kPa rather than at zero?",
                       ["Because the water has weight", "Because the atmosphere presses on the surface of the water: the total pressure at depth 0 is atmospheric pressure", "Because the graph is non-linear", "Because of upthrust"], 1,
                       "The intercept is the air pressure.", label="c"),
            ], graph=graph_depth),
            written("fm-t5-q2", "Describe the difference between a graph of pressure against height in the atmosphere and a graph of pressure against depth in a lake. (3)",
                    marks(["Height: the pressure <b>decreases</b> as height increases; depth: the pressure <b>increases</b> with depth.", "Height: the graph is <b>non-linear</b> (a curve, less steep higher up, because the air is less dense there); depth: the graph is a <b>straight line</b> (pressure proportional to depth, the water's density being constant).", "Both start from <b>atmospheric pressure</b>, about 100 kPa, at the surface."]), lines=3),
            choice("fm-t5-q3", "In 2024 the percentage change in pressure was calculated as $(74 - 104) \\div 104 \\times 100 = -29$ %. A student who divided by 74 instead…",
                   ["scored full marks", "scored one mark (−41 %), because the change must be divided by the original value", "scored zero", "was given the benefit of the doubt"], 1,
                   "Divide by the starting value."),
            written("fm-t5-q4", "A pressure–height graph for the atmosphere is described by a student as 'inversely proportional'. Comment on this. (2)",
                    marks(["The relationship is not inversely proportional in the strict sense (pressure × height is not constant — at zero height the pressure is 100 kPa, not infinite).", "The accurate description is a <b>negative, non-linear</b> relationship: pressure decreases as height increases and the fall per kilometre gets smaller. (The 2023 scheme, Q4(b)(i), accepted 'inversely proportional' for the non-linear mark \"in this context\" — a loose way of saying this.)"]), lines=2),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T6 · Upthrust the hard way [P]
# ---------------------------------------------------------------------

section_t6 = section(
    "upthrust-hard", "tricky", "Upthrust the hard way: apparent weight, volume and density, and the floating ball", "15.15P, 15.16P",
    equations=[r"\text{upthrust} = W_{\text{air}} - W_{\text{in fluid}}", r"V = \dfrac{\text{upthrust}}{\rho_{\text{fluid}}\,g}"],
    blurb="The 2025 Archimedes question had four stages and the examiners said candidates rarely linked them: the loss in weight is the upthrust; the upthrust is the weight of fluid displaced; that gives the volume displaced, which is the object's volume; and the object's weight and volume give its density. Each stage is a mark, and each carries forward.",
    tags=["P"],
    checklist=[
        "Link the apparent loss in weight to the upthrust and to the weight of fluid displaced",
        "Find the volume of an object from the upthrust and the fluid's density, then its density",
        "Explain why the upthrust on a floating object equals its weight whatever the liquid",
    ],
    parts=[
        explain(
            "The four-stage chain",
            "<table class='tbl'><tr><th>Stage</th><th>Equation</th><th>June 2025 Q9(a)(ii)</th></tr>"
            "<tr><td>1 loss in weight = upthrust = weight of fluid displaced</td><td>upthrust $= W_{\\text{air}} - W_{\\text{fluid}}$</td><td>2 N (one mark); starting from the wrong value (5 N) lost this mark only</td></tr>"
            "<tr><td>2 volume of fluid displaced = volume of the object</td><td>$V = \\text{upthrust} \\div (\\rho_{\\text{fluid}}\\, g)$</td><td>$1.43 \\times 10^{-4}$ m³ (one mark)</td></tr>"
            "<tr><td>3 mass of the object from its weight in air</td><td>$m = W_{\\text{air}} \\div g$</td><td>the density equation with the block's weight (one mark)</td></tr>"
            "<tr><td>4 density</td><td>$\\rho = m \\div V$</td><td>$4.9 \\times 10^{3}$ kg/m³ (one mark), error carried forward</td></tr></table>"
            "<p>The report: \"partial credit could be obtained by successfully completing each stage\", and on the explanation part (Q9(a)(i)) \"only a very few candidates correctly linked the loss in weight with the <b>weight of liquid displaced</b>\" — the marks were upthrust (1), equal to the weight of liquid displaced (1), and the liquid being <b>more dense than air</b> (1), which is why the object weighs less in the liquid than in air (there is an upthrust from the air too, but it is tiny). The paper's summary: \"less confidence was shown in the application of Archimedes' principle\".</p>"
            "<p><b>The floating ball</b> (June 2023 Q6(c)): a ball floating in fresh water and in sea water has the <b>same upthrust</b> in both — equal to its <b>weight</b>, because it floats. The difference is in <b>how much</b> liquid it must displace: sea water is denser, so a <b>smaller volume</b> of it weighs the same as the ball, so less of the ball is under the surface. Three of the four scheme points: weight of ball = weight of water displaced; sea water more dense; smaller volume displaced to produce the same weight.</p>",
        ),
        worked(
            "Density from apparent weight",
            "A metal block weighs 9.0 N in air and 7.0 N when fully submerged in a liquid of density 1200 kg/m³. $g = 10$ N/kg. Calculate the density of the block. (4 marks)",
            [
                "Upthrust $= 9.0 - 7.0 = 2.0$ N = weight of liquid displaced.",
                "Mass of liquid displaced $= 2.0 \\div 10 = 0.20$ kg, so its volume $= 0.20 \\div 1200 = 1.67 \\times 10^{-4}$ m³ — the block's volume.",
                "Mass of the block $= 9.0 \\div 10 = 0.90$ kg.",
                "$\\rho = m \\div V = 0.90 \\div (1.67 \\times 10^{-4}) = 5400$ kg/m³ ($5.4 \\times 10^{3}$).",
            ],
        ),
        practice("Upthrust the hard way", [
            group("fm-t6-q1", "A stone weighs 6.0 N in air and 4.0 N when hanging fully under water (density 1000 kg/m³). $g = 10$ N/kg.", [
                numeric("fm-t6-q1a", "State the upthrust on the stone.", 2.0, "N",
                        "Loss in weight.",
                        [r"upthrust $= 6.0 - 4.0 = 2.0$ N"], label="a"),
                numeric("fm-t6-q1b", "Calculate the volume of the stone.", 2e-4, "m³",
                        "Upthrust = weight of water displaced; mass $= 2.0 \\div 10$; $V = m \\div \\rho$.",
                        [r"mass of water displaced $= 2.0 \div 10 = 0.20$ kg", r"$V = m \div \rho = 0.20 \div 1000 = 2.0 \times 10^{-4}$ m³"], label="b"),
                numeric("fm-t6-q1c", "Calculate the density of the stone.", 3000, "kg/m³",
                        "Mass of the stone = 6.0 ÷ 10.",
                        [r"$m = 6.0 \div 10 = 0.60$ kg"] + ewau(r"\rho = m \div V", r"\rho = 0.60 \div (2.0 \times 10^{-4})", "3000", "kg/m³"), label="c"),
            ]),
            written("fm-t6-q2", "Explain why an object appears to weigh less when it is hanging in a liquid than when it is hanging in air. (3)",
                    marks(["In the liquid there is an <b>upthrust</b> on the object, which supports part of its weight, so the force on the string is smaller.", "The upthrust is equal to the <b>weight of liquid displaced</b> by the object.", "The liquid is <b>much more dense than air</b>, so the liquid displaced weighs far more than the air the object displaced — the upthrust in air is negligible."]), lines=3),
            written("fm-t6-q3", "A wooden block floats in water and then in oil, which is less dense than water. Compare the upthrust on the block in the two liquids, and explain whether more or less of the block is below the surface in the oil. (4)",
                    marks(["The upthrust is the <b>same</b> in both: the block floats, so in each liquid the upthrust <b>equals the block's weight</b>.", "Floating: the <b>weight of liquid displaced = the weight of the block</b>.", "Oil is <b>less dense</b> than water…", "…so a <b>larger volume</b> of oil must be displaced to have the block's weight: <b>more</b> of the block is below the surface in the oil."]), lines=4),
            choice("fm-t6-q4", "A student starts the 2025 chain with an upthrust of 5 N (the weight in the liquid) instead of 2 N (the loss in weight). According to the report, this…",
                   ["scored zero", "lost one mark, with the rest carried forward (3 of 4)", "lost two marks", "scored full marks"], 1,
                   "Each stage is credited; an error is carried forward."),
            numeric("fm-t6-q5", "A hot-air balloon has a volume of 2500 m³. The surrounding air has a density of 1.2 kg/m³ and $g = 10$ N/kg. Calculate the upthrust on the balloon.", 30000, "N",
                    "Upthrust = weight of air displaced $= \\rho V g$.",
                    [r"mass of air displaced $= \rho V = 1.2 \times 2500 = 3000$ kg", r"upthrust $= 3000 \times 10 = 30\,000$ N (the balloon rises if its total weight is less than this)"]),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T7 · Floating and sinking in the mark-scheme words [P]
# ---------------------------------------------------------------------

section_t7 = section(
    "floating-words", "tricky", "Floating and sinking in the mark-scheme words", "15.17P",
    equations=[r"\text{floats: weight} = \text{upthrust, less dense than the fluid}", r"\text{sinks: weight} > \text{upthrust even fully immersed}"],
    blurb="There are two correct ways to explain floating — compare the weight with the upthrust, or compare the object's density with the fluid's — and the marks come from completing whichever you start. The mark the 2022 examiners said was rarely scored is the link between them: a less dense object displaces less than its own volume of fluid to match its weight.",
    tags=["P"],
    checklist=[
        "Explain floating and sinking by comparing weight with upthrust",
        "Explain floating and sinking by comparing densities, with the displaced-volume link",
        "Apply it to ships, submarines and balloons",
    ],
    parts=[
        explain(
            "Two routes, one link",
            diagram(dg.floating_svg(), 660, 272, "Wood floating high, ice floating low and steel sunk, each with its upthrust and weight arrows.") +
            "<table class='tbl'><tr><th>Route</th><th>Floats</th><th>Sinks</th></tr>"
            "<tr><td><b>Forces</b></td><td>the object displaces enough fluid for the <b>upthrust to equal its weight</b> before it is fully immersed; the forces balance and it stays at the surface</td><td>even <b>fully immersed</b> the fluid displaced weighs less than the object: <b>upthrust < weight</b>, a resultant downward force, and it sinks (accelerates down)</td></tr>"
            "<tr><td><b>Density</b></td><td>the object is <b>less dense</b> than the fluid, so its own volume of fluid would weigh more than it — it needs to displace <b>less than its own volume</b> (the 2022 second mark)</td><td>the object is <b>more dense</b> than the fluid: its own volume of fluid weighs less than it, so it cannot displace enough</td></tr></table>"
            "<p>The June 2022 report (Q3(c)): \"most candidates understood that wood is less dense than water and would float\" — one mark — but \"not many scored a second mark for explaining that <b>less water would be displaced</b>\". That second idea is the bridge between the two routes, and a question that says <i>explain</i> wants it. For the force route, say both forces and which is larger; \"it is lighter\" or \"it has air in it\" on its own is neither route.</p>"
            "<p><b>Applications</b>: a <b>steel ship</b> floats because the hull encloses air, so the ship's <b>average density</b> (steel + air) is less than water's and its shape displaces a large volume; load it and it sits lower, displacing more. A <b>submarine</b> floods its tanks with water to increase its weight above the upthrust (sinks), and blows them out with air to reduce it (rises); at a steady depth, weight = upthrust. A <b>hot-air balloon</b> is less dense than the cooler air around it, so the upthrust from the air it displaces exceeds its weight.</p>",
        ),
        worked(
            "Why the cork rises",
            "A cork is held under water and released. Explain, in terms of forces, what happens and why. (3 marks)",
            [
                "Fully submerged, the cork displaces its own volume of water; the <b>upthrust equals the weight of that water</b>, which is <b>greater than the cork's weight</b> because cork is less dense than water.",
                "So there is a <b>resultant upward force</b> on the cork and it <b>accelerates upwards</b>.",
                "At the surface it rises partly out of the water, displacing less, until the upthrust has fallen to <b>equal its weight</b> — then it floats, with the forces balanced.",
            ],
        ),
        practice("Floating and sinking", [
            written("fm-t7-q1", "A plastic ball (density 950 kg/m³) and a glass marble (density 2500 kg/m³) are dropped into water. Explain, in terms of density and the water displaced, why one floats and the other sinks. (3)",
                    marks(["The plastic ball is <b>less dense than water</b>: its own volume of water would weigh more than it, so it needs to displace <b>less than its own volume</b> of water for the upthrust to equal its weight — it floats (95 % submerged).", "The marble is <b>more dense than water</b>: even fully immersed it displaces only its own volume of water, which weighs <b>less than the marble</b>…", "…so the upthrust is less than its weight and there is a resultant downward force: it sinks."]), lines=3),
            written("fm-t7-q2", "Explain, in terms of forces, why a solid steel ball sinks in water. (2)",
                    marks(["Even when fully immersed the ball displaces only its own volume of water, and that water weighs <b>less than the ball</b> (steel is denser than water), so the <b>upthrust is less than the weight</b>.", "There is a <b>resultant downward force</b>, so the ball accelerates downwards — it sinks."]), lines=2),
            choice("fm-t7-q3", "A loaded ship sits lower in the water than an empty one because…",
                   ["the water is denser", "its weight is greater, so it must displace more water for the upthrust to equal the larger weight", "the upthrust is smaller", "steel is heavier than water"], 1,
                   "More weight, more water to displace."),
            written("fm-t7-q4", "Describe how a submarine dives and surfaces. (2)",
                    marks(["To <b>dive</b> it lets water into its ballast tanks: its <b>weight increases</b> until it is greater than the upthrust (which stays the same, the volume being fixed), so it sinks.", "To <b>surface</b> it pumps air into the tanks, pushing the water out: its weight falls below the upthrust and it rises; at a steady depth weight = upthrust."]), lines=2),
            choice("fm-t7-q5", "Which answer would NOT earn a floating mark?",
                   ["Wood is less dense than water", "The upthrust equals the block's weight", "The block is light", "Less water is displaced than the block's own volume"], 2,
                   "'Light' is neither a density nor a force comparison."),
        ]),
    ],
)

SECTIONS = [section_t1, section_t2, section_t3, section_t4, section_t5, section_t6, section_t7]

# ---------------------------------------------------------------------
# Flashcards (the key-word definitions are added by fm_nn.FACTS_KW)
# ---------------------------------------------------------------------

FACTS = [
    # N1
    fact("Why does distorting an object need more than one force?", "One force is a resultant and accelerates the whole object; two forces in different directions change its shape.", "two-forces"),
    fact("The second force on a spring hung from a clamp?", "The clamp pulls up while the weight pulls down.", "two-forces"),
    fact("The three kinds of distortion?", "Stretching, compression, bending.", "two-forces"),
    # N2
    fact("Elastic distortion?", "The object returns to its original shape and size when the forces are removed.", "elastic-inelastic"),
    fact("Inelastic distortion?", "Permanent — the object does not return to its original shape.", "elastic-inelastic"),
    fact("Elastic limit?", "The point beyond which the spring no longer returns to its original length when unloaded.", "elastic-inelastic"),
    # N3
    fact("Hooke's law as an equation?", "$F = kx$: force = spring constant × extension (extension in m, k in N/m).", "hooke-nn"),
    fact("What does the spring constant tell you?", "The force per metre of extension — stiffness; unit N/m.", "hooke-nn"),
    fact("x in $F = kx$ is…", "The extension (change in length), not the length; in metres.", "hooke-nn"),
    fact("6.2 mm in metres?", "$6.2 \\times 10^{-3}$ m (1600 N instead of 1.6 N lost a mark in 2023).", "hooke-nn"),
    # N4
    fact("Energy stored in a stretched spring?", "$E = \\tfrac{1}{2} k x^2$, extension in metres; also the area under the F–x line.", "energy-stored"),
    fact("Why the ½ in $E = \tfrac{1}{2} k x^2$?", "The force grows from zero to $kx$ as it stretches, so the average force is half the final force.", "energy-stored"),
    fact("Double the extension: energy stored?", "Four times — $E \\propto x^2$.", "energy-stored"),
    # N5
    fact("A linear force–extension graph through the origin shows…", "Force is directly proportional to extension (Hooke's law); gradient = k.", "linear-nonlinear"),
    fact("Beyond the limit of proportionality?", "The graph curves (non-linear): extension no longer proportional to force; each extra newton gives more extension.", "linear-nonlinear"),
    fact("A rubber band's force–extension graph?", "A curve from the start — it does not obey Hooke's law.", "linear-nonlinear"),
    # N6
    fact("Spring practical: how is the extension measured?", "Pointer position on a vertical mm ruler with no load and with the load; subtract (2023: three marks).", "spring-practical"),
    fact("Spring practical: accuracy points?", "Read at eye level with a pointer (parallax); ruler vertical; let it settle; stay below the elastic limit; repeat unloading.", "spring-practical"),
    fact("From the force–extension graph of the practical?", "Gradient = spring constant; area under the line = work done stretching.", "spring-practical"),
    fact("How to check the elastic limit was not passed?", "Remove the masses and check the pointer returns to the no-load reading.", "spring-practical"),
    # N7
    fact("Pressure equation and unit?", "$P = F \\div A$; pascals (1 Pa = 1 N/m²).", "pressure-nn"),
    fact("Large area means…", "Small pressure for the same force: snowshoes, wide tyres, camel feet.", "pressure-nn"),
    fact("Explaining a camel's feet (2022)?", "Larger area → weight (force) spread over a larger area → less pressure. 'Mass spread out' did not score.", "pressure-nn"),
    fact("1 cm² and 1 mm² in m²?", "$10^{-4}$ m² and $10^{-6}$ m².", "pressure-nn"),
    # N8
    fact("Direction of the force from a fluid on a surface?", "At right angles (normal) to the surface, towards it.", "fluid-pressure"),
    fact("Total pressure at a depth in a liquid?", "Pressure due to the liquid + atmospheric pressure.", "fluid-pressure"),
    fact("Force on a surface from a pressure?", "$F = PA$; with fluid on both sides, use the difference in pressure.", "fluid-pressure"),
    fact("Two windows, same cabin pressure, different sizes?", "Same pressure, larger force on the larger window.", "fluid-pressure"),
    # N9
    fact("Why does atmospheric pressure fall with height?", "Less air above → smaller weight of air pressing down; the air is also less dense higher up.", "atmospheric-height"),
    fact("Shape of pressure against height?", "A curve falling: non-linear, the fall per km shrinks as the air thins.", "atmospheric-height"),
    fact("Atmospheric pressure at sea level?", "About 100 kPa — the weight of the air above each m².", "atmospheric-height"),
    fact("Marks for describing the height graph (2023, 2024)?", "Pressure decreases as height increases; non-linear; use numbers from the graph.", "atmospheric-height"),
    # N10
    fact("Why does pressure in a liquid increase with depth?", "A taller column of liquid above the point has more weight.", "depth-density"),
    fact("Why does pressure in a liquid increase with density?", "The same column of a denser liquid has more mass, so more weight.", "depth-density"),
    fact("Sea water on a pressure–depth graph (2022)?", "Steeper line, still straight, same intercept (atmospheric pressure).", "depth-density"),
    fact("Why is a dam thicker at the bottom?", "The water is deepest there, so the pressure and the force per m² are greatest.", "depth-density"),
    # N11
    fact("Pressure due to a column of liquid?", "$P = h \\rho g$: height × density × g.", "liquid-pressure"),
    fact("Difference in pressure between two depths?", "$\\Delta P = \\Delta h \\rho g$ — the atmosphere cancels.", "liquid-pressure"),
    fact("The 2025 density trap?", "Using 10 instead of 1000 kg/m³ for water gave a 35 m pool; check the result makes sense (10 m of water ≈ 100 kPa).", "liquid-pressure"),
    # N12
    fact("Why is there an upthrust?", "Pressure increases with depth, so the pressure on the bottom face is greater than on the top: a resultant upward force.", "upthrust-floating"),
    fact("Size of the upthrust?", "Equal to the weight of fluid displaced by the object.", "upthrust-floating"),
    fact("Condition for floating?", "Upthrust = weight: the object displaces its own weight of fluid before it is fully immersed (less dense than the fluid).", "upthrust-floating"),
    fact("Why does a steel ship float?", "Hull plus enclosed air is less dense than water; its shape displaces a large volume, enough to weigh as much as the ship.", "upthrust-floating"),
    # T1
    fact("Answer 100 times too small for k?", "The extension was left in cm (2025).", "extension-not-length"),
    fact("Length given, extension wanted?", "Extension = loaded length − unloaded length; convert to m.", "extension-not-length"),
    # T2
    fact("Where on the graph is the gradient equal to k?", "Only on the straight (linear) part.", "fx-graphs-hard"),
    fact("Energy past the limit of proportionality?", "Still the area under the line — a triangle plus a curved strip; count squares.", "fx-graphs-hard"),
    fact("Extension on the y-axis: the gradient is…", "$1 \\div k$.", "fx-graphs-hard"),
    # T3
    fact("Spring practical: independent and dependent variables?", "Independent: force (weight added); dependent: extension.", "spring-plan"),
    fact("Spring practical: expected graph?", "Force against extension: straight line through the origin, gradient = k.", "spring-plan"),
    # T4
    fact("Pressure under four feet?", "Area = 4 × the area of one foot (2022: forgetting the 4 cost a mark).", "pressure-hard"),
    fact("Area left in mm² in $P = F/A$?", "Answer a million times too large (2025).", "pressure-hard"),
    fact("'To 2 significant figures' in a pressure question?", "The rounding is its own mark (2024: 576 N → 580 N).", "pressure-hard"),
    # T5
    fact("Percentage change in pressure?", "(new − old) ÷ old × 100; dividing by the new value scored one mark (2024).", "pressure-graphs"),
    fact("Height graph vs depth graph?", "Height: curve, falling, non-linear. Depth: straight line, rising, intercept = atmospheric pressure.", "pressure-graphs"),
    # T6
    fact("The 2025 Archimedes chain?", "Loss in weight = upthrust = weight of fluid displaced → volume displaced = object's volume → mass from weight in air → density.", "upthrust-hard"),
    fact("Why does an object weigh less in a liquid than in air?", "Upthrust = weight of liquid displaced; the liquid is much denser than air, so the upthrust is much larger.", "upthrust-hard"),
    fact("A ball floating in fresh and in sea water: the upthrusts?", "Equal — each equals the ball's weight; less sea water needs displacing because it is denser.", "upthrust-hard"),
    # T7
    fact("The 2022 second mark for 'why does wood float'?", "Less water is displaced than the wood's own volume (because wood is less dense).", "floating-words"),
    fact("Sinking in terms of forces?", "Even fully immersed, upthrust < weight: a resultant downward force.", "floating-words"),
    fact("How does a submarine dive?", "Floods its tanks so its weight exceeds the (unchanged) upthrust.", "floating-words"),
]
