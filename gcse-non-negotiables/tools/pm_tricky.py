"""
pm_tricky.py — Topic 14 (Particle model): the tricky bits T1–T8 and
the flashcards.

T1 Particle-motion answers that score     T5 SHC versus SLH in words and numbers
T2 Density the hard way                   T6 The water core practical 6-marker
T3 The density practical 6-marker         T7 Explaining gas pressure [part P]
T4 Heating and cooling graphs             T8 Doing work on a gas [H, P]
                                          T9 Kelvin traps
"""

from revlib import (
    axis, choice, dashed, diagram, ewau, explain, fact, graph, group, line,
    mark, mark_scheme, marks, numeric, practice, section, worked, written,
)
import pm_diagrams as dg

# ---------------------------------------------------------------------
# T1 · Particle-motion answers that score
# ---------------------------------------------------------------------

section_t1 = section(
    "motion-words", "tricky", "Particle answers that score: motion, not bulk properties", "14.1, 14.5",
    equations=[r"\text{arrangement} + \text{movement}", r"\text{say what the particles do, not what the stuff does}"],
    blurb="Two examiners' reports in three years said the same thing: students describe the material (it flows, it takes the shape of the container, it melts) when the question asked about the particles. Each state has one movement phrase that scores; a change of state needs the before, the after and the word that joins them.",
    checklist=[
        "Give the scoring movement phrase for each state",
        "Describe a change of state as a change in motion: before → joining word → after",
        "Avoid the three answers that earn nothing: bulk properties, 'lots of energy', describing a different change",
    ],
    parts=[
        explain(
            "What scored and what did not",
            "<table class='tbl'><tr><th>Question</th><th>Scored</th><th>Did not score</th></tr>"
            "<tr><td>2023 Q3(c)(ii): motion of particles in a <b>liquid</b> (2)</td><td>\"<b>flow over each other</b>\"; \"move around\"; moving with a <b>range of speeds</b> in random directions; \"move freely\" (1 mark only, says nothing more about the motion)</td><td>\"with lots of energy\" (imprecise); \"take the shape of the container\" (bulk property); descriptions of <b>melting</b> (the wrong question)</td></tr>"
            "<tr><td>2025 Q5(b): change in motion as liquid wax <b>freezes</b> (2)</td><td>\"now only <b>vibrate in fixed positions</b>\" (both marks); \"<b>no longer move past each other</b>\"; \"<b>slow down</b> / lose kinetic energy\"</td><td>\"become <b>closer together</b>\" (arrangement, not motion — \"not enough for a mark\"); a description of melting</td></tr>"
            "<tr><td>2024 Q9(b): heating a gas in a sealed can — which does <b>not</b> change</td><td>the <b>mean distance</b> between particles (fixed volume, fixed number)</td><td>speed, energy, pressure — these all rise</td></tr></table>"
            "<p><b>The template for a change of state</b>: <i>before</i> (the motion in the first state) → <i>the joining word</i> (\"gain energy and speed up\" / \"lose energy and slow down\") → <i>after</i> (the motion in the second state). Melting: \"vibrate about fixed positions → gain energy → <b>leave their fixed positions and move around / flow over each other</b>\". Boiling: \"move around, touching → gain enough energy to <b>break away</b> from each other → <b>move fast in straight lines, far apart</b>\". Condensing and freezing: the same lines read backwards, with \"lose energy / slow down\". Keep the particles the subject of every sentence: \"the <b>particles</b> …\", never \"the wax …\".</p>",
        ),
        worked(
            "Boiling, as the particles",
            "Water is heated until it boils. Describe the changes in the arrangement and movement of the particles. (3 marks)",
            [
                "<b>Before</b>: in the liquid the particles are <b>touching</b>, in no pattern, and <b>move around / flow over each other</b>.",
                "<b>Joining</b>: as the water is heated the particles <b>gain energy and move faster</b>, until at the boiling point they have enough energy to <b>break away</b> from their neighbours.",
                "<b>After</b>: in the gas they are <b>far apart</b> and move <b>fast in straight lines in random directions</b>.",
            ],
        ),
        practice("Particle answers", [
            written("pm-t1-q1", "Steam condenses on a cold window. Describe the change in the motion of the water particles. (2)",
                    marks(["In the steam the particles move <b>fast in straight lines</b>, far apart; on the cold glass they <b>lose energy and slow down</b>.", "In the liquid they are <b>touching</b> and <b>move around / flow over each other</b> (no longer in straight lines)."]), lines=2),
            choice("pm-t1-q2", "A question asks about the motion of particles as a liquid freezes. Which answer earns nothing?",
                   ["They slow down", "They now only vibrate in fixed positions", "They become closer together", "They no longer move past each other"], 2,
                   "2025: arrangement, not motion — 'not enough for a mark'."),
            choice("pm-t1-q3", "'The particles have lots of energy' as a description of a liquid's particles is…",
                   ["full marks", "imprecise — it says nothing about how they move", "a bulk property", "correct for a gas only"], 1,
                   "2023 report: imprecise phrases scored nothing."),
            written("pm-t1-q4", "Describe the motion of the particles in a solid, and how it changes when the solid is heated but does not melt. (2)",
                    marks(["The particles <b>vibrate about fixed positions</b>.", "When heated they <b>vibrate faster / with a larger amplitude</b> (more kinetic energy) but stay in their fixed positions."]), lines=2),
            choice("pm-t1-q5", "Which sentence keeps the particles as the subject, as the mark scheme wants?",
                   ["The wax gets harder as it cools", "The wax stops flowing", "The particles slow down and then only vibrate in fixed positions", "The wax becomes a solid"], 2,
                   "Say what the particles do, not what the wax does."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T2 · Density the hard way
# ---------------------------------------------------------------------

section_t2 = section(
    "density-hard", "tricky", "Density the hard way: rearranging, units, rounding and scale readings", "14.2, 14.3",
    equations=[r"V = \dfrac{m}{\rho}", r"m = \rho V", r"1 \text{ cm}^3 = 10^{-6} \text{ m}^3"],
    blurb="The density questions that lose marks are not the ones where you divide two numbers. They rearrange for volume, give a mass in grams and a density in kg/m³, want a reading off a measuring-cylinder scale, or hand you a volume from an upthrust and expect you to carry it into $\\rho = m/V$. And the rounding mark is real.",
    checklist=[
        "Rearrange $\\rho = m/V$ for m or V and substitute with the units matching",
        "Read a measuring-cylinder scale correctly and take a difference",
        "Carry a volume found earlier (from a difference, or from an upthrust) into the density",
    ],
    parts=[
        explain(
            "The four traps",
            "<table class='tbl'><tr><th>Trap</th><th>What the examiners saw</th><th>What to do</th></tr>"
            "<tr><td><b>Rearranging</b></td><td>2024 Q3(a): $V = m \\div \\rho$ — a mark for the substitution or the rearrangement, a mark for the evaluation (1.57 cm³)</td><td>write the rearranged equation first, then substitute; both earn credit even if the arithmetic slips</td></tr>"
            "<tr><td><b>Units</b></td><td>2023 Q3(b): kg and m³ converted to g and cm³ \"with incorrect powers of ten\"</td><td>stay in SI; if you must convert, 1 g/cm³ = 1000 kg/m³, 1 cm³ = $10^{-6}$ m³, 1 g = $10^{-3}$ kg</td></tr>"
            "<tr><td><b>Rounding</b></td><td>2025 Q5(c)(i): 0.0047 m³ rounded to 0.005 m³ — \"poor practice\"</td><td>keep the significant figures of the data (two or three); never round to one figure</td></tr>"
            "<tr><td><b>Scale reading</b></td><td>2024 Q3(d): a measuring cylinder read before and after (1350 and 1750 cm³) — the volume is the <b>difference</b>, 400 cm³</td><td>read the bottom of the meniscus on both, subtract, check the unit on the scale</td></tr></table>"
            "<p><b>The upthrust route</b> (Topic 15 meets Topic 14, June 2025 Q9(a)): weigh an object in air and in water; the difference is the <b>upthrust</b>, which equals the <b>weight of water displaced</b>; so the mass of water displaced $= \\text{upthrust} \\div g$, and its volume = that mass ÷ 1000 kg/m³ — and that is the <b>volume of the object</b>. Then $\\rho = m \\div V$ for the object (the mass from its weight in air). The scheme gave $1.43 \\times 10^{-4}$ m³ and $4.9 \\times 10^3$ kg/m³, with error carried forward from the volume into the density.</p>",
        ),
        worked(
            "Grams, cubic centimetres and a density in kg/m³",
            "A metal cube has sides of 2.0 cm and a mass of 21.6 g. Calculate its density in kg/m³. (3 marks)",
            [
                "$V = 2.0 \\times 2.0 \\times 2.0 = 8.0$ cm³ $= 8.0 \\times 10^{-6}$ m³; $m = 21.6$ g $= 0.0216$ kg.",
                "$\\rho = m \\div V = 0.0216 \\div (8.0 \\times 10^{-6})$.",
                "$\\rho = 2700$ kg/m³ (aluminium) — or 2.7 g/cm³ × 1000.",
            ],
        ),
        practice("Density the hard way", [
            numeric("pm-t2-q1", "A gold ring has a mass of 6.2 g. The density of gold is 19 300 kg/m³. Calculate the volume of the ring in m³.", 3.2e-7, "m³",
                    "$V = m \\div \\rho$, with the mass in kg.",
                    [r"$m = 6.2$ g $= 0.0062$ kg"] + ewau(r"V = m \div \rho", r"V = 0.0062 \div 19\,300", r"3.2 \times 10^{-7}", "m³ (0.32 cm³)")),
            numeric("pm-t2-q2", "A measuring cylinder contains water to the 1350 cm³ mark. A stone is lowered in and the water rises to 1750 cm³. The stone's mass is 1.08 kg. Calculate its density in kg/m³.", 2700, "kg/m³",
                    "Volume = 1750 − 1350 cm³, then into m³.",
                    [r"$V = 1750 - 1350 = 400$ cm³ $= 4.0 \times 10^{-4}$ m³"] + ewau(r"\rho = m \div V", r"\rho = 1.08 \div (4.0 \times 10^{-4})", "2700", "kg/m³")),
            group("pm-t2-q3", "An object weighs 7.0 N in air and 5.6 N when fully submerged in water. Density of water = 1000 kg/m³; $g = 10$ N/kg.", tags=["P"], parts=[
                numeric("pm-t2-q3a", "Calculate the upthrust on the object.", 1.4, "N",
                        "Weight in air − weight in water.",
                        [r"upthrust $= 7.0 - 5.6 = 1.4$ N"], label="a", tags=["P"]),
                numeric("pm-t2-q3b", "The upthrust equals the weight of water displaced. Calculate the volume of the object.", 1.4e-4, "m³",
                        "Mass of water $= \\text{upthrust} \\div g$; volume = mass ÷ density of water.",
                        [r"mass of water displaced $= 1.4 \div 10 = 0.14$ kg", r"$V = m \div \rho = 0.14 \div 1000 = 1.4 \times 10^{-4}$ m³ — the object's volume"], label="b", tags=["P"]),
                numeric("pm-t2-q3c", "Calculate the density of the object.", 5000, "kg/m³",
                        "Mass of the object $= \\text{weight in air} \\div g$.",
                        [r"$m = 7.0 \div 10 = 0.70$ kg"] + ewau(r"\rho = m \div V", r"\rho = 0.70 \div (1.4 \times 10^{-4})", "5000", "kg/m³"), label="c", tags=["P"]),
            ]),
            choice("pm-t2-q4", "A calculation gives a volume of 0.0047 m³ from data to two significant figures. The answer to write is…",
                   ["0.005 m³", "0.0047 m³", "0.00 m³", "4.7 m³"], 1,
                   "2025 report: rounding to one figure was 'unnecessary and poor practice'."),
            numeric("pm-t2-q5", "Air has a density of 1.2 kg/m³. Calculate the mass of air in a hall 12 m × 8.0 m × 4.0 m.", 460, "kg",
                    "Volume first, then $m = \\rho V$.",
                    [r"$V = 12 \times 8.0 \times 4.0 = 384$ m³"] + ewau(r"m = \rho V", r"m = 1.2 \times 384", "460", "kg (461)")),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T3 · The density practical 6-marker
# ---------------------------------------------------------------------

section_t3 = section(
    "density-plan", "tricky", "Planning the density practical: the 6-mark method, and the eureka-can trap", "14.3",
    equations=[r"\text{mass on a balance; volume by ruler or displacement}", r"\rho = m \div V \text{ (or the gradient of } m \text{ against } V)"],
    blurb="A method question on density wants the measuring-cylinder method, named apparatus and the subtraction — and when the question gives a measuring cylinder, that is the method to describe: in 2023 a displacement can scored nothing. The seven-step recipe fits the investigation version: does the density of a material depend on the size of the sample? Mass against volume, and the gradient is the density.",
    checklist=[
        "Write a 6-mark method for the density of an irregular solid and a liquid, with named apparatus",
        "Plan an investigation of mass against volume for a material using the seven steps",
        "Explain why the gradient of a mass–volume graph is the density",
    ],
    parts=[
        explain(
            "The method marks, and the investigation",
            "<p><b>The method question</b>: the marks are for named apparatus (<b>balance</b>, <b>measuring cylinder</b>, <b>ruler</b>), the <b>readings</b> taken (mass; volume before and after; the dimensions), the <b>processing</b> (subtract the volumes; multiply the dimensions; $\\rho = m \\div V$) and one <b>accuracy</b> point (meniscus at eye level, fully submerged, dry before weighing, repeat the lengths). The June 2023 report: the measuring-cylinder method with before, after and subtract scored; the <b>displacement (eureka) can</b> \"scored nothing\" — the question had given a measuring cylinder, and the can is a different method, fine for an object too big for a cylinder but not the one asked for — and measurements \"not relevant to volume, such as the metal's mass\" earned nothing in a volume question.</p>"
            "<table class='tbl'><tr><th>Step</th><th>Does the density of a material depend on the size of the sample?</th></tr>"
            "<tr><td><b>1 Variables</b></td><td>independent: the <b>volume</b> of the sample (different-sized blocks of the same material); dependent: its <b>mass</b>; control: the same material, the same balance, dry samples</td></tr>"
            "<tr><td><b>2 Relationship</b></td><td>$\\rho = m \\div V$, so $m = \\rho V$: mass should be <b>proportional to volume</b> and a graph of $m$ against $V$ a straight line through the origin with <b>gradient = density</b></td></tr>"
            "<tr><td><b>3 Change</b></td><td>use five or more blocks of the material of different sizes (or add identical cubes one at a time)</td></tr>"
            "<tr><td><b>4 Measure</b></td><td>mass with a balance; volume with a ruler ($l \\times w \\times h$) or by displacement in a measuring cylinder</td></tr>"
            "<tr><td><b>5 Use</b></td><td>plot mass against volume; draw the line of best fit; the <b>gradient</b> is the density; a straight line through the origin shows the density does not depend on size</td></tr>"
            "<tr><td><b>6 Accuracy</b></td><td>zero the balance; measure each length in several places and average; read the meniscus at eye level</td></tr>"
            "<tr><td><b>7 Repeat</b></td><td>repeat each mass and volume reading and take a mean</td></tr></table>",
        ),
        worked(
            "The 6-mark method",
            "Describe how to find the density of an irregular stone and of a sample of oil. (6 marks)",
            [
                "<b>Stone, mass</b>: measure its mass with a <b>balance</b> (zeroed first).",
                "<b>Stone, volume</b>: put water in a <b>measuring cylinder</b> and read the volume; lower the stone in so it is <b>completely submerged</b>; read the new volume; <b>subtract</b> to get the stone's volume.",
                "<b>Oil, mass</b>: put an empty measuring cylinder on the balance and <b>zero it</b> (or record its mass); pour in the oil; read the mass (subtracting the cylinder if needed).",
                "<b>Oil, volume</b>: read the volume of the oil from the cylinder's scale.",
                "<b>Calculate</b>: density = mass ÷ volume for each ($\\rho = m / V$).",
                "<b>Accuracy</b>: read the meniscus at eye level; use a large volume of oil; dry the stone before weighing (or weigh it first); repeat and average.",
            ],
        ),
        practice("Planning the density practical", [
            written("pm-t3-q1", "Plan an investigation to find out whether the density of a material depends on the size of the sample. (6)",
                    mark_scheme([
                        ("Variables", "Independent: the volume (size) of the sample; dependent: its mass; control: the same material, the same balance."),
                        ("Relationship", "$m = \\rho V$: mass should be proportional to volume; the gradient of a mass–volume graph is the density."),
                        ("Change", "Use at least five samples of the same material of different sizes."),
                        ("Measure", "Mass with a balance; volume with a ruler ($l \\times w \\times h$) or by displacement in a measuring cylinder (before, after, subtract)."),
                        ("Use", "Plot mass against volume; a straight line through the origin shows the density is the same for every size; gradient = density."),
                        ("Accuracy", "Zero the balance; measure each length in several places; read the meniscus at eye level; fully submerge."),
                        ("Repeat", "Repeat each reading and take a mean."),
                    ], total=6, extra=["Any six of the seven points."]), lines=7),
            choice("pm-t3-q2", "A 2023 question gave a measuring cylinder and asked how to find the volume of an irregular metal object. A description of a eureka (displacement) can…",
                   ["scored full marks", "scored nothing — the measuring-cylinder method the question gave was wanted", "is the only valid method", "scored one mark for the apparatus"], 1,
                   "Describe the method the question gives: before, after, fully immersed, subtract. (A displacement can is a fair method for an object too big for a cylinder.)"),
            written("pm-t3-q3", "A student plots the mass of five blocks of the same wood against their volume and gets a straight line through the origin. Explain what the line shows and how to find the density from it. (2)",
                    marks(["Mass is <b>proportional to volume</b>: the density is the same for every block (does not depend on size).", "The <b>gradient</b> (mass ÷ volume) is the density of the wood."]), lines=2),
            choice("pm-t3-q4", "Why is the object lowered gently so it is completely under the water?",
                   ["So the water does not get warm", "So the full volume of the object is displacing water and none splashes out", "So the balance reads correctly", "So the object does not dissolve"], 1,
                   "Any part above the water, or any splash, makes the volume reading too small."),
            written("pm-t3-q5", "State two accuracy points for finding the density of a liquid with a measuring cylinder and a balance. (2)",
                    marks(["Read the <b>bottom of the meniscus at eye level</b>.", "Use a <b>large volume</b> of liquid (smaller percentage error) / zero the balance with the empty cylinder on it / repeat and average."]), lines=2),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T4 · Heating and cooling graphs
# ---------------------------------------------------------------------

heating_points = [[0, -20], [1, 0], [9, 0], [19, 100], [20, 100]]
graph_heating = graph(
    axis("time in min", 20, 2), axis("temperature in °C", 120, 20, mn=-20),
    [line(heating_points), dashed([[0, 0], [20, 0]])],
    "Heating graph for 0.10 kg of ice: temperature rises from minus 20 to 0 degrees in the first minute, flat at 0 degrees from 1 to 9 minutes, rises to 100 degrees at 19 minutes, flat at 100 degrees to 20 minutes.",
    marks_list=[mark(5, 0, "melting", drop=False, dy=-10), mark(19.5, 100, "boiling", drop=False, dx=-62, dy=-10)],
)

cooling_points = [[0, 80], [2, 60], [8, 60], [12, 30]]
graph_cooling = graph(
    axis("time in min", 12, 2), axis("temperature in °C", 100, 20),
    [line(cooling_points)],
    "Cooling curve for liquid wax: temperature falls from 80 to 60 degrees in 2 minutes, stays at 60 degrees from 2 to 8 minutes, then falls to 30 degrees at 12 minutes.",
)

x_points = [[0, 20], [3, 80], [9, 80], [15, 140]]
graph_x = graph(
    axis("time in min", 16, 2), axis("temperature in °C", 160, 20),
    [line(x_points)],
    "Heating graph for 0.050 kg of substance X with a 20 W heater: temperature rises from 20 to 80 degrees in the first 3 minutes, stays at 80 degrees from 3 to 9 minutes, then rises to 140 degrees at 15 minutes.",
)

section_t4 = section(
    "heating-cooling-graphs", "tricky", "Heating and cooling graphs: what a flat section means, and the 2025 cooling-curve marks", "14.6, 14.7, 14.9",
    equations=[r"\text{flat section: change of state, } Q = m L", r"\text{sloping section: } \Delta Q = m c \Delta\theta"],
    blurb="A temperature–time graph for a steady heater has sloping parts (the temperature rises, $\\Delta Q = m c \\Delta \\theta$) and flat parts (a change of state at constant temperature, $Q = m L$). Reading the graph is one skill; explaining why the flat part is flat, and why it is long, is where the 2025 marks were lost.",
    checklist=[
        "Read a melting or boiling point and the length of a flat section from a heating or cooling graph",
        "Explain why the temperature stays constant during a change of state",
        "Explain why a flat section is longer than the sloping ones using the latent heat and specific heat capacity values",
    ],
    parts=[
        explain(
            "Reading the graph, and explaining it",
            "<p><b>Sloping section</b>: the energy supplied raises the temperature — the particles move faster. <b>Flat section</b>: the energy supplied changes the state — it separates the particles (potential energy) and the kinetic energy, and so the temperature, does not change. Its <b>height</b> is the melting or boiling point; its <b>length</b> is how long the change took, so with a steady heater of power $P$, the energy for the change is $E = P t$ and $L = E \\div m$. A <b>cooling</b> curve is the same picture upside down: the flat section is <b>freezing</b> (or condensing), at the same temperature as melting, with the energy going <b>out</b> to the surroundings.</p>"
            "<p>The June 2025 report (Q5(c)(iii), a cooling curve for wax with a table of its specific heat capacity and specific latent heat, 3 marks): the marks were for saying that the <b>latent heat is much larger than the specific heat capacity</b> — \"much more energy is needed to change state than to change temperature\" — <b>quoting the values</b> from the table to support it; and that energy is <b>transferred from the wax to the surroundings</b> (the wax is cooling, so the energy goes out). A fourth idea, that the rate of transfer is about the same throughout so a larger energy takes a longer time, \"was rarely seen\". Many candidates \"described melting rather than freezing\" — on a cooling curve the flat part is the wax <b>freezing</b>.</p>"
            "<p><b>Why flat sections are long</b>: for water, $L_{\\text{fusion}} = 334\\,000$ J/kg against $c = 4200$ J/kg °C — melting 1 kg of ice takes as much energy as warming the water by about 80 °C; boiling it ($L_{\\text{vap}} = 2\\,260\\,000$ J/kg) takes over five times more than warming it from 0 to 100 °C.</p>",
        ),
        worked(
            "The ice graph",
            "The graph shows the temperature of 0.10 kg of ice heated by a 70 W heater. Use the graph to find the specific latent heat of fusion of ice. (3 marks)",
            [
                "The flat section at 0 °C (melting) runs from 1 min to 9 min: $t = 8$ min $= 480$ s.",
                "Energy supplied during melting: $E = P t = 70 \\times 480 = 33\\,600$ J.",
                "$L = Q \\div m = 33\\,600 \\div 0.10 = 336\\,000$ J/kg (about $3.4 \\times 10^5$ J/kg).",
            ],
            graph=graph_heating,
        ),
        practice("Heating and cooling graphs", [
            group("pm-t4-q1", "The graph shows the temperature of 0.050 kg of a solid substance X, heated by a 20 W heater, against time.", [
                numeric("pm-t4-q1a", "State the melting point of X.", 80, "°C",
                        "The flat section.",
                        ["The flat section is at 80 °C."], label="a"),
                numeric("pm-t4-q1b", "Use the graph to calculate the specific latent heat of fusion of X.", 144000, "J/kg",
                        "Length of the flat section in seconds × power, then ÷ mass.",
                        [r"flat section 3 min to 9 min: $t = 6$ min $= 360$ s", r"$E = P t = 20 \times 360 = 7200$ J"] + ewau(r"L = Q \div m", r"L = 7200 \div 0.050", "144\\,000", "J/kg"), label="b"),
                written("pm-t4-q1c", "Explain why the temperature stays at 80 °C from 3 min to 9 min even though the heater is still supplying energy. (2)",
                        marks(["X is <b>melting</b>: the energy supplied is used to <b>separate the particles / break them out of their fixed positions</b> (increase their potential energy)…", "…<b>not</b> to make them move faster, so their kinetic energy and the temperature do not change until all of X has melted."]), lines=2, label="c"),
            ], graph=graph_x),
            group("pm-t4-q2", "The graph shows the temperature of liquid wax as it cools in a beaker. Specific heat capacity of wax = 2100 J/kg °C; specific latent heat of fusion of wax = 180 000 J/kg.", [
                numeric("pm-t4-q2a", "State the freezing point of the wax.", 60, "°C",
                        "The flat section.",
                        ["The flat section is at 60 °C."], label="a"),
                written("pm-t4-q2b", "Explain why the flat section lasts longer than the time taken to cool from 80 °C to 60 °C. (3)",
                        marks(["The <b>specific latent heat</b> (180 000 J/kg) is <b>much larger</b> than the specific heat capacity (2100 J/kg °C): changing the state releases far more energy per kg than cooling by 20 °C ($2100 \\times 20 = 42\\,000$ J/kg).", "Energy is <b>transferred from the wax to the surroundings</b> at roughly the <b>same rate</b> throughout…", "…so transferring the larger amount of energy (freezing) <b>takes longer</b>."]), lines=3, label="b"),
                choice("pm-t4-q2c", "What is happening to the wax between 2 min and 8 min?",
                       ["It is melting", "It is freezing: changing from liquid to solid at constant temperature", "It is boiling", "It is cooling as a liquid"], 1,
                       "2025: many described melting — on a cooling curve the flat part is freezing.", label="c"),
            ], graph=graph_cooling),
            choice("pm-t4-q3", "On a heating graph for a steady heater, the energy needed for the change of state is found from…",
                   ["the height of the flat section", "power × the length (time) of the flat section", "the gradient of the flat section", "the time at the end of the flat section"], 1,
                   "$E = P t$ with t the length, not the end time; in seconds."),
            choice("pm-t4-q4", "Why does a cooling curve for a pure substance have a flat section at the same temperature as its heating curve?",
                   ["Cooling is slower", "Freezing happens at the melting point: the same change of state, with the latent heat given out instead of taken in", "The thermometer sticks", "It is a different substance"], 1,
                   "Melting point = freezing point."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T5 · SHC versus SLH in words and numbers
# ---------------------------------------------------------------------

section_t5 = section(
    "shc-vs-slh", "tricky", "Specific heat capacity versus specific latent heat: the comparisons, and \"why was the rise smaller?\"", "14.6–14.9",
    equations=[r"\Delta\theta = \dfrac{\Delta Q}{m c}", r"\text{energy to the surroundings} \Rightarrow \text{smaller rise}"],
    blurb="Three question shapes mix the two quantities: compare two substances from their values, say what happens to a given energy, and explain why the measured temperature rise is smaller than the calculated one. The last has a mark-scheme answer — energy transferred to the surroundings, or to the heater and container — and two phrasings the scheme ignores.",
    checklist=[
        "Compare two substances from their specific heat capacities or latent heats",
        "Calculate a temperature rise from an energy, then explain why the real rise is smaller",
        "Say where the 'missing' energy went in the mark-scheme words",
    ],
    parts=[
        explain(
            "Comparing, predicting, explaining the shortfall",
            "<table class='tbl'><tr><th>Shape</th><th>How to answer</th></tr>"
            "<tr><td><b>Compare</b>: oil $c = 2000$, water $c = 4200$ J/kg °C — same mass, same energy</td><td>$\\Delta\\theta = \\Delta Q \\div (m c)$: the oil's temperature rises <b>more</b> (about 2.1 times as much) because less energy is needed per degree; or, the same temperature rise needs <b>less</b> energy for the oil</td></tr>"
            "<tr><td><b>Compare</b>: $L_{\\text{fusion}}$ (334 kJ/kg) and $L_{\\text{vap}}$ (2260 kJ/kg) for water</td><td>boiling needs <b>far more</b> energy per kg than melting: the particles must separate completely, not just leave their fixed positions</td></tr>"
            "<tr><td><b>Predict</b>: 0.50 kg of water receives 21 000 J</td><td>$\\Delta\\theta = 21\\,000 \\div (0.50 \\times 4200) = 10$ °C</td></tr>"
            "<tr><td><b>Explain the shortfall</b>: the measured rise is less than the calculated one</td><td>some of the energy is <b>transferred to the surroundings</b> (the air, the bench) and to the <b>container, heater and thermometer</b>, so <b>less energy goes into the water</b> than the heater supplied</td></tr></table>"
            "<p>The June 2024 scheme (Q9(c)(ii), 2 marks: why the actual rise was smaller than calculated): \"energy transferred to the <b>surroundings</b>\" (1); \"energy transferred to <b>heater parts / container</b>\" (1); \"<b>ignore</b> 'energy is lost'\" and \"ignore 'heater not 100 % efficient'\" — say <b>where</b> the energy went, with a destination. The reverse version — the calculated $c$ comes out <b>too high</b> — has the same cause: the energy you put into $\\Delta Q$ was the heater's, but the water only got part of it, so dividing the full energy by the (smaller) rise overestimates $c$.</p>",
        ),
        worked(
            "Calculated and measured",
            "A 50 W heater runs for 5.0 minutes in 0.25 kg of water ($c = 4200$ J/kg °C). (a) Calculate the expected temperature rise. (b) The measured rise is 11 °C. Explain why. (4 marks)",
            [
                "(a) $E = P t = 50 \\times 300 = 15\\,000$ J.",
                "$\\Delta\\theta = \\Delta Q \\div (m c) = 15\\,000 \\div (0.25 \\times 4200) = 14$ °C (14.3).",
                "(b) Some of the heater's energy is <b>transferred to the surroundings</b> (the air and the bench)…",
                "…and some to the <b>beaker, the heater itself and the thermometer</b>, so less than 15 000 J went into the water and its rise is smaller.",
            ],
        ),
        practice("SHC versus SLH", [
            numeric("pm-t5-q1", "A 60 W heater runs for 4.0 minutes in 0.20 kg of a liquid. The temperature rises by 30 °C. Calculate the specific heat capacity of the liquid (assume all the energy goes into the liquid).", 2400, "J/kg °C",
                    "$E = P t$ first (t in seconds), then $c = E \\div (m \\Delta \\theta)$.",
                    [r"$E = P t = 60 \times 240 = 14\,400$ J"] + ewau(r"c = \Delta Q \div (m \Delta\theta)", r"c = 14\,400 \div (0.20 \times 30)", "2400", "J/kg °C")),
            written("pm-t5-q2", "In the heater experiment above (60 W for 4.0 minutes, 0.20 kg of liquid, a 30 °C rise), the true specific heat capacity of the liquid is smaller than the value calculated from these figures. Explain why. (2)",
                    marks(["Some of the heater's energy is <b>transferred to the surroundings</b> (air, bench) and to the <b>container, heater and thermometer</b>, so <b>less energy went into the liquid</b> than $P t$.", "The temperature rise is therefore smaller than it would be for the full energy, and dividing the full energy by the smaller rise gives a value of $c$ that is <b>too large</b>."]), lines=2),
            choice("pm-t5-q3", "Equal masses of oil ($c = 2000$ J/kg °C) and water ($c = 4200$ J/kg °C) receive the same energy. Which is true?",
                   ["The water's temperature rises more", "The oil's temperature rises more, about twice as much", "Both rise by the same amount", "The oil boils"], 1,
                   "$\\Delta \\theta = \\Delta Q \\div (m c)$: smaller c, bigger rise."),
            choice("pm-t5-q4", "Which explanation of a smaller-than-expected temperature rise would the 2024 scheme ignore?",
                   ["Energy was transferred to the surroundings", "Energy was transferred to the beaker and heater", "The heater is not 100 % efficient", "Energy heated the thermometer"], 2,
                   "'Not 100 % efficient' and 'energy is lost' were ignored — name the destination."),
            written("pm-t5-q5", "Explain why the specific latent heat of vaporisation of water (2 260 000 J/kg) is much larger than its specific latent heat of fusion (334 000 J/kg). (2)",
                    marks(["Boiling must <b>separate the particles completely</b> (overcome the forces between them so they are far apart), whereas melting only lets them <b>leave their fixed positions</b> while still touching.", "Separating them fully needs <b>far more energy per kilogram</b>, so $L_{\\text{vap}}$ is much larger."]), lines=2),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T6 · The water core practical 6-marker
# ---------------------------------------------------------------------

melting_points = [[0, -10], [1, 0], [7, 0], [10, 30]]
graph_melting = graph(
    axis("time in min", 10, 1), axis("temperature in °C", 40, 10, mn=-10),
    [line(melting_points), dashed([[0, 0], [10, 0]])],
    "Temperature of crushed ice against time while heated: rises from minus 10 to 0 degrees in the first minute, flat at 0 degrees from 1 to 7 minutes, then rises to 30 degrees at 10 minutes.",
)

section_t6 = section(
    "water-practical", "tricky", "The water core practical: the specific heat capacity 6-marker and the melting-ice graph", "14.11",
    equations=[r"c = \dfrac{\Delta Q}{m\,\Delta\theta}", r"\Delta Q = E = P t \text{ (or } I V t\text{)}"],
    blurb="Core practical 14.11 has two halves: heat ice and watch the temperature hold at 0 °C while it melts; heat water with an electric heater and find its specific heat capacity. The 2024 paper set the second as a 6-marker and the levels are in the report: Level 3 needs the temperature change, the energy, and how c comes out of them.",
    checklist=[
        "Write the apparatus and steps for finding the specific heat capacity of water by electrical heating",
        "Say what Level 3 needs: Δθ measured, energy measured or calculated, c from $\\Delta Q = m c \\Delta \\theta$",
        "Describe the melting-ice half and sketch its graph",
    ],
    parts=[
        explain(
            "The 2024 levels",
            diagram(dg.shc_svg(), 660, 275, "The specific heat capacity practical: an immersion heater and a thermometer in a lagged beaker of water, a joulemeter (or ammeter and voltmeter) and a stopwatch.") +
            "<p>The June 2024 scheme (Q9(d), 6 marks): <b>apparatus</b> — immersion heater, power supply, <b>balance</b>, <b>thermometer</b>, <b>stopwatch</b>, <b>joulemeter</b> (or ammeter and voltmeter), insulated container, stirrer; <b>steps</b> — measure the <b>mass</b> of water on the balance; record the <b>initial temperature</b>; switch on and time with the stopwatch; stir; record the <b>final temperature</b>; read the <b>energy</b> from the joulemeter (or $E = I V t$, or $P t$); <b>rearrange</b> $\\Delta Q = m c \\Delta\\theta$ to $c = \\Delta Q \\div (m \\Delta\\theta)$; or plot temperature against energy and use the gradient. <b>Level 3</b> (5–6 marks) needs the <b>temperature change</b>, the <b>energy supplied</b> and how to find $c$ from them; Level 2 is a method with gaps; Level 1 is apparatus with no coherent method. \"<b>Ignore</b> Bunsen burner\" — the energy from a flame cannot be measured.</p>"
            "<table class='tbl'><tr><th>Step</th><th>Specific heat capacity of water</th></tr>"
            "<tr><td><b>1 Variables</b></td><td>measure: mass of water, initial and final temperature, energy supplied (or current, pd and time); control: lagging, lid, stirring, the same beaker</td></tr>"
            "<tr><td><b>2 Relationship</b></td><td>$\\Delta Q = m c \\Delta\\theta$, so $c = \\Delta Q \\div (m \\Delta\\theta)$</td></tr>"
            "<tr><td><b>3 Change</b></td><td>let the heater run (e.g. 10 minutes), or take readings every minute to plot a graph</td></tr>"
            "<tr><td><b>4 Measure</b></td><td>mass on a balance (zero with the empty beaker); temperatures with the thermometer; energy on the joulemeter or $E = I V t$ with an ammeter, voltmeter and stopwatch</td></tr>"
            "<tr><td><b>5 Use</b></td><td>$c = \\Delta Q \\div (m \\Delta\\theta)$; or plot temperature against energy — gradient $= 1 \\div (m c)$</td></tr>"
            "<tr><td><b>6 Accuracy</b></td><td><b>lag</b> the beaker and use a <b>lid</b> (less energy to the surroundings); <b>stir</b> so the thermometer reads the whole water; read the thermometer at eye level; a larger mass and longer time give larger, less uncertain readings</td></tr>"
            "<tr><td><b>7 Repeat</b></td><td>repeat and average, or take the gradient of the graph through many points</td></tr></table>"
            "<p><b>The melting-ice half</b>: crushed ice in a beaker, thermometer in, heat gently (or let it stand), record the temperature every minute. The temperature rises to 0 °C and then <b>stays at 0 °C while the ice melts</b>, though energy is still going in; once it has all melted, the water warms. The flat section is the evidence that a change of state happens at a constant temperature.</p>",
        ),
        worked(
            "The Level 3 method",
            "Describe a method to find the specific heat capacity of water using an electric heater. (6 marks)",
            [
                "Measure the <b>mass</b> of water in an insulated beaker with a <b>balance</b> (zero the balance with the empty beaker).",
                "Put an <b>immersion heater</b> and a <b>thermometer</b> in the water, with a lid; record the <b>initial temperature</b>.",
                "Switch on the heater and start a <b>stopwatch</b>; stir; after a measured time (say 10 minutes) record the <b>final temperature</b>.",
                "Measure the <b>energy supplied</b> with a <b>joulemeter</b>, or from the ammeter and voltmeter readings: $E = I V t$.",
                "Calculate the <b>temperature change</b> $\\Delta\\theta$ = final − initial; then $c = \\Delta Q \\div (m \\Delta\\theta)$.",
                "To reduce energy transferred to the surroundings, lag the beaker and use a lid; repeat, or plot temperature against energy and use the gradient.",
            ],
        ),
        practice("The water practical", [
            written("pm-t6-q1", "A student puts a beaker of water on a tripod, heats it with a Bunsen burner for five minutes and records the temperature before and after. She says she cannot now calculate the specific heat capacity of the water. Explain why, and describe the changes to her method that would let her find it. (6)",
                    mark_scheme([
                        ("Why not", "She has no value for the <b>energy supplied</b>: a Bunsen burner's energy transfer cannot be measured (and much of it heats the air and the beaker), so $\\Delta Q$ in $\\Delta Q = m c \\Delta\\theta$ is unknown — the mass of water may also be unmeasured."),
                        ("Heater", "Replace the burner with an <b>immersion heater</b> in the water, connected to a power supply through a <b>joulemeter</b> (or an ammeter and voltmeter with a stopwatch so that $E = I V t$)."),
                        ("Mass", "Measure the <b>mass</b> of the water with a balance (zeroed with the empty beaker)."),
                        ("Temperatures", "Record the initial temperature, stir, and record the final temperature: $\\Delta\\theta$ = final − initial."),
                        ("Calculate", "Rearrange: $c = \\Delta Q \\div (m \\Delta\\theta)$ — or take readings every minute and plot temperature against energy, using the gradient."),
                        ("Accuracy", "Lag the beaker and use a lid so that nearly all the measured energy goes into the water; repeat."),
                    ], total=6, extra=["Marked by levels, not per row: Level 3 (5–6) needs the reason (no measured energy), the temperature change, the energy supplied and how $c$ is found from them; Level 2 is a method with gaps."]), lines=8),
            group("pm-t6-q2", "The graph shows the temperature of crushed ice in a beaker as it is heated steadily.", [
                written("pm-t6-q2a", "Explain the shape of the graph between 1 min and 7 min. (2)",
                        marks(["The ice is <b>melting</b>: the temperature stays at <b>0 °C</b> (the melting point) while the state changes.", "The energy supplied goes into <b>separating the particles from their fixed positions</b> (potential energy), not into increasing their speed, so the temperature does not rise."]), lines=2, label="a"),
                choice("pm-t6-q2b", "What does the graph show after 7 min?",
                       ["The ice is still melting", "All the ice has melted and the water is warming up", "The water is boiling", "The ice is freezing"], 1,
                       "Once the change of state is complete the energy raises the temperature again.", label="b"),
            ], graph=graph_melting),
            choice("pm-t6-q3", "Why is a Bunsen burner not accepted as the heater in this method?",
                   ["It is too hot", "The energy it supplies to the water cannot be measured", "It cannot heat water", "It is not allowed in the lab"], 1,
                   "You need the energy: joulemeter, or I, V and t."),
            written("pm-t6-q4", "State two ways to reduce the energy transferred to the surroundings in this experiment, and why that matters. (3)",
                    marks(["<b>Lag</b> (insulate) the beaker.", "Use a <b>lid</b> (reduces convection and evaporation from the surface).", "If energy goes to the surroundings the water gets less than the heater supplied, the temperature rise is too small, and the calculated $c$ is <b>too large</b>."]), lines=3),
            numeric("pm-t6-q5", "In the experiment, 0.50 kg of water rises from 18 °C to 38 °C while the joulemeter reads 44 000 J. Calculate the value of c this gives.", 4400, "J/kg °C",
                    "$c = \\Delta Q \\div (m \\Delta \\theta)$.",
                    ewau(r"c = \Delta Q \div (m \Delta\theta)", r"c = 44\,000 \div (0.50 \times 20)", "4400", "J/kg °C (a little above 4200, because some energy went to the beaker and surroundings)")),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T7 · Explaining gas pressure
# ---------------------------------------------------------------------

section_t7 = section(
    "explaining-pressure", "tricky", "Explaining gas pressure: temperature, volume, and the force on the walls", "14.12, 14.13, 14.16P–14.19P",
    equations=[r"\text{hotter: faster} \rightarrow \text{more frequent and harder}", r"\text{smaller: shorter path} \rightarrow \text{more frequent (not harder)}"],
    blurb="Every gas-pressure explanation is the same chain — particles, collisions with the walls, force, pressure — with one link changed. Temperature changes how fast the particles hit; volume changes how often. Keep the two straight, and say which quantity was held constant. (Doing work on a gas, the Higher Physics step, has the next section to itself.)",
    checklist=[
        "Write the temperature chain (constant volume) and the volume chain (constant temperature) without mixing them",
        "Say which single link changes between the two chains",
        "Explain the force a gas exerts on a surface, and why a tyre or balloon holds its shape",
    ],
    parts=[
        explain(
            "The two chains side by side",
            "<table class='tbl'><tr><th>Change</th><th>Held constant</th><th>Chain</th></tr>"
            "<tr><td><b>Temperature up</b></td><td>volume (and mass)</td><td>particles move <b>faster</b> → collide with the walls <b>more often</b> and <b>harder</b> (greater force each) → greater total force on the walls → <b>pressure up</b></td></tr>"
            "<tr><td><b>Volume down</b> [P]</td><td>temperature (and mass)</td><td>particles have <b>less distance to travel</b> between the walls → collide with the walls <b>more often</b> (same speed, so <b>not harder</b>) → more collisions per second on a smaller area → <b>pressure up</b>; $P_1 V_1 = P_2 V_2$</td></tr>"
            "<tr><td><b>Force on a surface</b> [P]</td><td>—</td><td>collisions exert a force <b>at right angles</b> to the surface; force = pressure × area; a balloon stays inflated because the inside gas pushes out on the rubber more than the outside air pushes in</td></tr></table>"
            "<p>The common mix-up is a volume answer that says the particles hit \"harder\" — at constant temperature they do not: same speed, same force per collision, just more of them. The other is forgetting the condition: $P_1 V_1 = P_2 V_2$ needs a <b>fixed mass</b> at <b>constant temperature</b>, and \"heating raises the pressure\" needs a <b>fixed volume</b> (a sealed rigid container). A balloon in the sun expands instead, because its volume is free to change — and a balloon in a cold room shrinks, for the same reason in reverse.</p>",
        ),
        worked(
            "The cold balloon",
            "An inflated balloon is left in a cold room overnight and is smaller in the morning. Explain why, in terms of particles. (3 marks)",
            [
                "The air particles inside the balloon <b>lose energy and slow down</b> as the air cools.",
                "They collide with the inside of the balloon <b>less often and less hard</b>, so the force on the rubber from the inside falls.",
                "The balloon is not rigid: the outside air pushes the rubber in until the inside pressure matches again, so it is the <b>volume</b> that decreases (in a sealed rigid can the volume could not change, and the pressure would fall instead).",
            ],
        ),
        practice("Explaining gas pressure", [
            written("pm-t7-q1", "A sealed, rigid can of air is warmed. Explain why the pressure inside it increases. (3)",
                    marks(["The particles gain energy and move <b>faster</b>.", "They collide with the walls <b>more often</b> and <b>harder</b> (a greater force in each collision).", "The volume is fixed, so a greater total force on the same area: the <b>pressure increases</b>."]), lines=3),
            written("pm-t7-q2", "The temperature chain and the volume chain both end with a higher pressure. State the one link that is different between them, and why. (2)",
                    marks(["Temperature up (constant volume): the particles hit the walls more often <b>and harder</b>, because they are <b>moving faster</b>.", "Volume down (constant temperature): the particles hit the walls more often but <b>not harder</b>, because their <b>speed is unchanged</b> — they simply have less distance to travel between the walls."]), lines=2, tags=["P"]),
            choice("pm-t7-q3", "A gas is compressed at constant temperature. Which statement is WRONG?",
                   ["The particles hit the walls more often", "The particles hit the walls harder", "The particles have less distance to travel between collisions with the walls", "The pressure increases"], 1,
                   "Same temperature, same speed, same force per collision.", tags=["P"]),
            choice("pm-t7-q4", "A balloon in the sun gets bigger; a sealed rigid can in the sun gets a higher pressure. Why the difference?",
                   ["The balloon's air gets hotter", "The balloon's volume is free to change, so the extra force from the faster particles pushes the rubber out; the can's volume cannot change, so the pressure rises instead", "The can has more particles", "The balloon is not sealed"], 1,
                   "Same chain inside both; what is held constant differs."),
            written("pm-t7-q5", "Explain how the gas in a car tyre exerts a force on the inside of the tyre. (2)",
                    marks(["The gas particles move randomly and <b>collide with the inner surface</b> of the tyre; each collision exerts a small <b>force at right angles</b> to the surface.", "The total of all the collisions per unit area is the pressure; <b>force = pressure × area</b> on each part of the tyre wall, which holds the tyre's shape."]), lines=2, tags=["P"]),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T8 · Doing work on a gas [H, P]
# ---------------------------------------------------------------------

section_t8 = section(
    "work-on-gas", "tricky", "Doing work on a gas: why a bicycle pump gets warm", "14.20P",
    equations=[r"\text{work done on the gas} \rightarrow \text{particles rebound faster} \rightarrow \text{KE up} \rightarrow \text{temperature up}"],
    blurb="Push a piston in and you do work on the gas: the particles bounce off the moving piston faster than they arrived, their kinetic energy rises, and so does the temperature — a bicycle pump warms up even though nothing is heating it. The chain has one step the temperature chain in the last section does not: where the energy came from.",
    tags=["H", "P"],
    checklist=[
        "Explain why doing work on a gas increases its temperature",
        "Explain why a gas compressed quickly ends up at a higher pressure for two reasons",
        "Say what 'doing work on the gas' means in terms of the piston and the particles",
    ],
    parts=[
        explain(
            "The work-done link",
            "<table class='tbl'><tr><th>Step</th><th>What to write</th></tr>"
            "<tr><td><b>1</b></td><td>pushing the piston in <b>does work on the gas</b> (a force moves through a distance): energy is transferred <b>to</b> the gas</td></tr>"
            "<tr><td><b>2</b></td><td>particles that collide with the <b>moving</b> piston <b>rebound faster</b> than they arrived (like a ball hit by a moving bat)</td></tr>"
            "<tr><td><b>3</b></td><td>the particles' average <b>kinetic energy increases</b></td></tr>"
            "<tr><td><b>4</b></td><td>so the <b>temperature of the gas increases</b> — nothing heated it; the energy came in as work</td></tr>"
            "<tr><td><b>5</b></td><td>(if asked about the pressure) the faster particles hit the walls more often and harder, <b>and</b> the volume is smaller so they hit more often for that reason too — the pressure rises by more than $P_1 V_1 = P_2 V_2$ predicts, because the temperature is not constant</td></tr></table>"
            "<p>The reverse happens too: a gas that <b>expands and pushes a piston out does work</b> on the piston, its particles rebound from the retreating piston <b>more slowly</b>, and its temperature <b>falls</b> — which is why an aerosol can feels cold as it empties and why a bicycle tyre's air cools as it is let out. The spec statement is 14.20P: \"explain why doing work on a gas can increase its temperature, including a bicycle pump\" — Higher Physics only.</p>",
        ),
        worked(
            "The bicycle pump",
            "A bicycle pump is used with its outlet blocked. The handle is pushed in quickly. Explain why the air inside becomes hotter and its pressure rises. (4 marks)",
            [
                "Pushing the handle in <b>does work on the air</b>: the moving piston transfers energy to the particles that collide with it, so they <b>rebound faster</b>.",
                "The particles' <b>kinetic energy increases</b>, so the <b>temperature of the air rises</b> (the pump feels warm).",
                "The faster particles collide with the walls <b>more often and harder</b>, so the pressure rises…",
                "…and the <b>volume is smaller</b>, so the particles also hit the walls more often because they have less distance to travel — both effects raise the pressure.",
            ],
        ),
        practice("Doing work on a gas", [
            written("pm-t8-q1", "In a diesel engine the air in the cylinder is compressed very quickly by the piston and becomes hot enough to ignite the fuel. Explain why the air gets so hot. (3)",
                    marks(["The piston moving in <b>does work on the air</b>: energy is transferred to the gas.", "Particles colliding with the <b>moving piston rebound faster</b> than they arrived, so the particles' <b>kinetic energy increases</b>.", "A higher average kinetic energy of the particles is a <b>higher temperature</b> — and the compression is so quick that little energy is transferred to the surroundings meanwhile."]), lines=3),
            choice("pm-t8-q2", "'Doing work on a gas' means…",
                   ["heating the gas with a flame", "a force (the piston) moving through a distance into the gas, transferring energy to it", "letting the gas expand", "cooling the gas"], 1,
                   "Work = force × distance, into the gas."),
            written("pm-t8-q3", "The air let out of a bicycle tyre feels cold. Explain why, in terms of the particles. (2)",
                    marks(["The escaping air <b>expands</b> and <b>does work</b> pushing the surrounding air out of the way: energy is transferred <b>from</b> the gas.", "Its particles <b>lose kinetic energy</b> (they rebound more slowly from the retreating boundary), so the <b>temperature falls</b>."]), lines=2),
            choice("pm-t8-q4", "A gas is compressed quickly to half its volume. Compared with compressing it slowly at constant temperature, the final pressure is…",
                   ["the same — $P_1 V_1 = P_2 V_2$ always", "higher, because the work done has also raised the temperature, so the particles hit harder as well as more often", "lower", "zero"], 1,
                   "Quick compression: the temperature is not constant, so the equation underestimates the pressure."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T9 · Kelvin traps
# ---------------------------------------------------------------------

section_t9 = section(
    "kelvin-traps", "tricky", "Kelvin traps: changes, negatives, and when °C is fine", "14.14, 14.15",
    equations=[r"\Delta T(\text{K}) = \Delta\theta(°\text{C})", r"T(\text{K}) = \theta(°\text{C}) + 273"],
    blurb="Four small things cost kelvin marks: converting a temperature change (don't — it is the same number), writing a negative kelvin temperature (impossible), adding 273 to a Celsius value inside $\\Delta Q = m c \\Delta \\theta$ (unnecessary, and wrong if you do it to only one of the two temperatures), and treating a Celsius value as if doubling it doubled anything physical.",
    checklist=[
        "Leave a temperature change alone when switching scales",
        "Spot an impossible temperature",
        "Explain why only the kelvin scale has a real zero",
    ],
    parts=[
        explain(
            "The four traps",
            "<table class='tbl'><tr><th>Trap</th><th>Right</th></tr>"
            "<tr><td>\"The temperature rose from 20 °C to 50 °C. What is the rise in K?\" — answered 303 K</td><td>A <b>change</b> is the same on both scales: <b>30 K</b>. Only an actual temperature gets the 273.</td></tr>"
            "<tr><td>A calculated temperature of −20 K</td><td>Impossible: 0 K is the lowest temperature. Check the arithmetic (probably subtracted 273 from a value that was already in kelvin, or added where you should have subtracted).</td></tr>"
            "<tr><td>Converting to kelvin before using $\\Delta Q = m c \\Delta\\theta$</td><td>Not needed: the equation uses the <b>change</b>, which is the same in °C. Converting both temperatures and subtracting gives the same $\\Delta\\theta$; converting only one is wrong by 273.</td></tr>"
            "<tr><td>\"40 °C is twice as hot as 20 °C\"</td><td>No: the Celsius zero is just the freezing point of water, not zero energy. 20 °C → 40 °C is 293 K → 313 K, about 7 % more. Only the <b>kelvin</b> scale starts where the particles have the least possible movement, so only kelvin values can be compared as ratios.</td></tr></table>"
            "<p>Why the kelvin scale matters: its zero is <b>absolute zero</b>, where the particles have the least possible movement and a gas would exert no pressure. On the Celsius scale that point is −273 °C, so Celsius values can be negative and cannot be compared as multiples; kelvin values can. Converting is only ever adding or subtracting 273.</p>",
        ),
        worked(
            "All three at once",
            "Liquid nitrogen boils at 77 K. (a) Convert this to °C. (b) A sample is warmed from 77 K to 20 °C; find the temperature rise in K. (c) A student writes the rise as 216 °C and the final temperature as −56 K. Say what is wrong with each. (4 marks)",
            [
                "(a) $77 - 273 = -196$ °C.",
                "(b) 20 °C $= 20 + 273 = 293$ K; rise $= 293 - 77 = 216$ K.",
                "(c) The rise of 216 K is also a rise of <b>216 °C</b> — that part is right, because a change is the same on both scales.",
                "But <b>−56 K is impossible</b>: no temperature is below 0 K. The student has subtracted 273 from a value that was already in kelvin; the final temperature is 293 K (20 °C).",
            ],
        ),
        practice("Kelvin traps", [
            numeric("pm-t9-q1", "Water is heated from 15 °C to 65 °C. State the temperature rise in kelvin.", 50, "K",
                    "A change is the same on both scales.",
                    [r"$65 - 15 = 50$ °C $= 50$ K"]),
            numeric("pm-t9-q2", "A gas is cooled from 450 K to −23 °C. Calculate the fall in temperature in kelvin.", 200, "K",
                    "Convert −23 °C to K first, then subtract.",
                    [r"$-23 + 273 = 250$ K", r"fall $= 450 - 250 = 200$ K"]),
            choice("pm-t9-q3", "A student finds a temperature of −30 K in a calculation. This means…",
                   ["the gas is very cold", "a mistake — no temperature is below 0 K", "the gas is a solid", "the pressure is negative"], 1,
                   "Absolute zero is the floor."),
            choice("pm-t9-q4", "0.50 kg of water is warmed from 10 °C to 30 °C ($c = 4200$ J/kg °C). The correct energy calculation is…",
                   ["$0.50 \\times 4200 \\times 303$", "$0.50 \\times 4200 \\times 20$", "$0.50 \\times 4200 \\times (303 - 10)$", "$0.50 \\times 4200 \\times 283$"], 1,
                   "$\\Delta\\theta = 20$ °C $= 20$ K; converting only one temperature is wrong by 273."),
            written("pm-t9-q5", "Explain why 40 °C is not 'twice as hot' as 20 °C, and state the scale on which such a comparison would make sense. (2)",
                    marks(["The Celsius zero (the freezing point of water) is not zero energy: the particles still have plenty of movement at 0 °C, so Celsius values cannot be compared as ratios (20 °C → 40 °C is 293 K → 313 K).", "The <b>kelvin</b> scale starts at absolute zero, where the particles have the least possible movement, so only kelvin values can be compared as multiples."]), lines=2),
        ]),
    ],
)

SECTIONS = [section_t1, section_t2, section_t3, section_t4, section_t5, section_t6, section_t7, section_t8, section_t9]

# ---------------------------------------------------------------------
# Flashcards (the key-word definitions are added by pm_nn.FACTS_KW)
# ---------------------------------------------------------------------

FACTS = [
    # N1
    fact("Movement of particles in a solid?", "Vibrate about fixed positions.", "three-states"),
    fact("Movement of particles in a liquid (the phrase that scores)?", "Move around / flow over each other, in random directions, still touching.", "three-states"),
    fact("Movement of particles in a gas?", "Fast, in straight lines, in random directions; far apart; colliding with each other and the walls.", "three-states"),
    fact("Arrangement in a solid, liquid, gas?", "Solid: regular, touching, fixed positions. Liquid: irregular, touching, no fixed positions. Gas: random, far apart.", "three-states"),
    fact("Why can a gas be compressed but a liquid cannot?", "Gas particles are far apart with empty space between them; liquid particles are already touching.", "three-states"),
    # N2
    fact("Density equation and SI unit?", "$\\rho = m \\div V$; kg/m³.", "density-nn"),
    fact("1 g/cm³ in kg/m³?", "1000 kg/m³ (multiply g/cm³ by 1000).", "density-nn"),
    fact("Density of water?", "About 1000 kg/m³ (1 g/cm³).", "density-nn"),
    fact("Units advice from the 2023 report?", "Use SI units unless told to convert; converting to g and cm³ went wrong with powers of ten.", "density-nn"),
    fact("Rounding advice from the 2025 report?", "Keep the significant figures of the data; rounding 0.0047 m³ to 0.005 m³ was 'poor practice'.", "density-nn"),
    # N3
    fact("Volume of a regular block?", "Measure length, width and height with a ruler; $V = l \\times w \\times h$.", "density-practical"),
    fact("Volume of an irregular solid?", "Measuring cylinder: read the water volume, lower the object in fully submerged, read again, subtract.", "density-practical"),
    fact("Mass and volume of a liquid?", "Empty measuring cylinder on a balance, zero it, pour in the liquid: mass from the balance, volume from the scale.", "density-practical"),
    fact("The eureka-can trap?", "When the question gives a measuring cylinder, describe that method: in 2023 a displacement can scored nothing there.", "density-practical"),
    fact("Accuracy points for the cylinder method?", "Read the bottom of the meniscus at eye level; fully submerge; lower gently; dry before weighing or weigh first.", "density-practical"),
    # N4
    fact("Why is a solid usually denser than its liquid?", "Particle spacing is smaller — more particles per unit volume; same mass per particle.", "density-states"),
    fact("Why is a gas about 1000 times less dense than a liquid?", "Particles far apart (about ten times further in each direction): far fewer per m³.", "density-states"),
    fact("The exception to 'solid denser than liquid'?", "Ice is less dense than water (open lattice) — it floats.", "density-states"),
    # N5
    fact("The six changes of state?", "Melting, freezing, boiling/evaporating, condensing, sublimating (solid → gas), deposition (gas → solid).", "changes-of-state"),
    fact("Why is mass conserved in a change of state?", "The same particles are present before and after — none created or destroyed; only arrangement and movement change.", "changes-of-state"),
    fact("Physical change vs chemical change?", "Physical: no new substance, reversible, original properties recovered. Chemical: new substances formed.", "changes-of-state"),
    fact("Boiling vs evaporating?", "Boiling: throughout the liquid at the boiling point. Evaporating: from the surface at any temperature.", "changes-of-state"),
    fact("Which changes give energy out?", "Freezing and condensing (and deposition).", "changes-of-state"),
    # N6
    fact("Two things heating can do to a system?", "Raise its temperature (particles move faster, KE up) or change its state (particles separate, PE up, temperature constant).", "shc-slh-defined"),
    fact("Define specific heat capacity.", "The energy needed to raise the temperature of 1 kg of a substance by 1 °C.", "shc-slh-defined"),
    fact("Define specific latent heat.", "The energy needed to change the state of 1 kg of a substance without a change in temperature.", "shc-slh-defined"),
    fact("Difference between SHC and SLH?", "SHC: temperature change, no change of state. SLH: change of state, no temperature change.", "shc-slh-defined"),
    fact("SHC of water?", "4200 J/kg °C — large, so water heats and cools slowly.", "shc-slh-defined"),
    fact("Latent heats of water?", "Fusion 334 000 J/kg; vaporisation 2 260 000 J/kg.", "shc-slh-defined"),
    # N7
    fact("Equation for a temperature change?", "$\\Delta Q = m c \\Delta\\theta$ — Δθ is the change, same in °C or K.", "thermal-equations"),
    fact("Equation for a change of state?", "$Q = m L$ — no Δθ; fusion or vaporisation as appropriate.", "thermal-equations"),
    fact("Ice at −10 °C to water at 20 °C: how many stages?", "Three: warm the ice (c of ice), melt it ($L_f$), warm the water (c of water); add.", "thermal-equations"),
    fact("Heater running for a time: first step?", "$E = P t$ (t in seconds), then the thermal equation.", "thermal-equations"),
    # N8
    fact("How does thermal insulation work?", "Low thermal conductivity, usually by trapping air (poor conductor, cannot convect in pockets): slower conduction and convection.", "insulation"),
    fact("Examples of thermal insulation?", "Lagging, loft and cavity-wall insulation, double glazing, a lid, a vacuum flask.", "insulation"),
    fact("Cable's plastic coating — thermal insulation?", "No: electrical insulation. Waste heating in a cable is reduced by lowering its resistance (2025).", "insulation"),
    fact("How does a vacuum flask reduce transfer?", "No particles in the vacuum: no conduction or convection; silvered surfaces reduce radiation.", "insulation"),
    # N9
    fact("Why does a gas exert a pressure?", "Particles move fast and randomly, collide with the walls; each collision exerts a force; total force per unit area is the pressure.", "gas-pressure"),
    fact("Heating a gas at constant volume: the chain?", "Particles faster → collide with the walls more often and harder → greater total force → pressure increases.", "gas-pressure"),
    fact("Which statement earns nothing about gas pressure?", "'Particles collide with each other more' — only collisions with the walls count.", "gas-pressure"),
    fact("Sealed can heated: what does not change?", "The mean distance between particles (fixed volume, fixed number).", "gas-pressure"),
    # N10
    fact("What is absolute zero?", "The lowest possible temperature, −273 °C (0 K): particles have the least possible movement; gas pressure would be zero.", "kelvin-nn"),
    fact("°C to K?", "Add 273. K to °C: subtract 273.", "kelvin-nn"),
    fact("A temperature change of 20 °C in kelvin?", "20 K — changes are the same on both scales.", "kelvin-nn"),
    fact("Melting and boiling points of water in K?", "273 K and 373 K.", "kelvin-nn"),
    # N11
    fact("Reducing volume at constant temperature: the chain?", "Less distance between walls → more frequent collisions (same speed, not harder) → higher pressure.", "compressing-gas"),
    fact("The equation for a gas at constant temperature?", "$P_1 V_1 = P_2 V_2$ — fixed mass, constant temperature.", "compressing-gas"),
    fact("Direction of the force a gas exerts on a surface?", "At right angles to the surface; force = pressure × area.", "compressing-gas"),
    # T1
    fact("Template for a change-of-state motion answer?", "Before (motion in state 1) → joining word (gain/lose energy, speed up/slow down) → after (motion in state 2); particles as the subject.", "motion-words"),
    fact("Three answers that earn nothing about particle motion?", "Bulk properties (takes the shape of the container), 'lots of energy', and describing a different change (melting when asked about freezing).", "motion-words"),
    # T2
    fact("Volume from an upthrust?", "Upthrust = weight of water displaced; mass of water $= \\text{upthrust} \\div g$; volume = mass ÷ 1000 kg/m³ = object's volume.", "density-hard"),
    fact("Measuring-cylinder volume of an object?", "Final reading − initial reading.", "density-hard"),
    # T3
    fact("Mass–volume graph for one material?", "A straight line through the origin; gradient = density; shows density does not depend on size.", "density-plan"),
    # T4
    fact("Flat section on a heating graph?", "A change of state at constant temperature: height = melting/boiling point; length × power = energy for the change.", "heating-cooling-graphs"),
    fact("Why is the flat section long (2025)?", "Latent heat ≫ specific heat capacity (quote the values); energy transferred from the wax to the surroundings at about the same rate, so more energy takes longer.", "heating-cooling-graphs"),
    fact("Flat section on a cooling curve?", "Freezing (or condensing) — not melting; same temperature as the melting point; energy given out.", "heating-cooling-graphs"),
    # T5
    fact("Why was the measured temperature rise smaller than calculated (2024)?", "Energy transferred to the surroundings and to the container/heater parts. Ignore 'energy lost' and 'not 100 % efficient'.", "shc-vs-slh"),
    fact("Same energy, same mass, smaller c?", "Larger temperature rise: $\\Delta\\theta = \\Delta Q \\div (m c)$.", "shc-vs-slh"),
    # T6
    fact("SHC-of-water practical: apparatus?", "Immersion heater, power supply, balance, thermometer, stopwatch, joulemeter (or ammeter and voltmeter), insulated beaker with lid, stirrer.", "water-practical"),
    fact("SHC-of-water practical: Level 3 needs?", "The temperature change, the energy supplied (joulemeter or $I V t$), and $c = \\Delta Q \\div (m \\Delta\\theta)$.", "water-practical"),
    fact("Why not a Bunsen burner?", "The energy it supplies cannot be measured.", "water-practical"),
    fact("Melting-ice half of the practical shows?", "Temperature holds at 0 °C while the ice melts even though energy is supplied: a change of state at constant temperature.", "water-practical"),
    # T7
    fact("Why does a bicycle pump get warm?", "Work is done on the gas; particles rebound from the moving piston faster; their KE and the temperature rise.", "work-on-gas"),
    fact("Air let out of a tyre feels cold — why?", "The expanding gas does work on its surroundings; its particles lose KE; the temperature falls.", "work-on-gas"),
    fact("Volume chain: harder or more often?", "More often only — same temperature, same speed, same force per collision.", "explaining-pressure"),
    fact("A balloon in the sun vs a sealed can in the sun?", "Same chain inside; the balloon's volume is free to change so it expands, the can's is fixed so its pressure rises.", "explaining-pressure"),
    # T8
    fact("Is 40 °C twice as hot as 20 °C?", "No: the Celsius zero is not zero energy (293 K → 313 K). Only kelvin values can be compared as ratios.", "kelvin-traps"),
    fact("Converting to kelvin inside $\\Delta Q = m c \\Delta\\theta$?", "Not needed — the equation uses the change, the same in °C and K; converting only one temperature is wrong by 273.", "kelvin-traps"),
]
