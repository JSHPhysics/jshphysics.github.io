"""
en_nn_a.py — Topics 3 and 8 (Energy): the non-negotiables N1–N6.

N1 Energy stores and pathways      N4 Gravitational potential energy
N2 Conservation of energy          N5 Kinetic energy
N3 Energy transfer diagrams        N6 Work done

Each section says which spec topic it belongs to with `subtopic`
(["3"], ["8"] or ["3", "8"]); the build script passes that through.
Spec numbering follows the Edexcel 1PH0 specification (issue 3).
"""

from revlib import (
    choice, diagram, ewau, explain, fact, group, mark_scheme, marks, numeric,
    practice, section, sf, worked, written,
)

G = 10

# ---------------------------------------------------------------------
# N1 · Energy stores and pathways
# ---------------------------------------------------------------------

STORES_TABLE = (
    "<table class='tbl'><tr><th>Store</th><th>Energy is in this store when…</th><th>Example</th></tr>"
    "<tr><td><b>Kinetic</b></td><td>an object is moving</td><td>a moving car</td></tr>"
    "<tr><td><b>Gravitational potential</b></td><td>an object is raised above the ground</td><td>a book on a shelf</td></tr>"
    "<tr><td><b>Elastic potential</b></td><td>something is stretched, squashed or bent</td><td>a stretched spring, a drawn bow</td></tr>"
    "<tr><td><b>Thermal</b></td><td>something is hot (its particles move faster)</td><td>a cup of tea</td></tr>"
    "<tr><td><b>Chemical</b></td><td>energy can be released by a chemical reaction</td><td>food, fuel, a battery</td></tr>"
    "<tr><td><b>Nuclear</b></td><td>energy can be released from the nucleus of an atom</td><td>uranium fuel, the Sun</td></tr>"
    "<tr><td><b>Electrostatic</b></td><td>charges are separated or pushed together</td><td>a charged balloon near a wall</td></tr>"
    "<tr><td><b>Magnetic</b></td><td>magnets or magnetic materials are pulled apart or pushed together</td><td>two magnets held apart</td></tr></table>"
)

PATHWAYS_TABLE = (
    "<table class='tbl'><tr><th>Pathway (how energy is transferred)</th><th>What is happening</th><th>Example</th></tr>"
    "<tr><td><b>Mechanically</b></td><td>a force does work on an object</td><td>pushing a trolley, lifting a box</td></tr>"
    "<tr><td><b>Electrically</b></td><td>a current flows through a component</td><td>a battery powering a motor</td></tr>"
    "<tr><td><b>By heating</b></td><td>energy moves from a hotter object to a cooler one</td><td>a kettle element heating water</td></tr>"
    "<tr><td><b>By radiation</b></td><td>energy is carried by waves (light, sound, infrared)</td><td>the Sun warming the ground</td></tr></table>"
)

section_n1 = section(
    "stores-pathways", "nn", "Energy stores and pathways", "3.3, 8.1, 8.4",
    equations=[r"\text{8 stores}", r"\text{4 pathways}"],
    blurb="Energy is kept in <b>stores</b> and moved between them along <b>pathways</b>. Every energy answer in the exam is built from these two lists.",
    checklist=[
        "Name all eight energy stores and give an example of each",
        "Name the four pathways (mechanically, electrically, by heating, by radiation)",
        "Describe an energy change as: energy is transferred from the ___ store of ___ to the ___ store of ___, by ___",
    ],
    parts=[
        explain(
            "The eight stores",
            "<p>A <b>store</b> is a way of holding energy. Edexcel uses eight of them, and the names matter: write <i>kinetic energy store</i>, not \"movement energy\".</p>" + STORES_TABLE +
            "<p>There is no \"light energy\", \"sound energy\" or \"electrical energy\" store. Light, sound and electricity are <b>pathways</b> — ways energy moves from one store to another.</p>",
        ),
        explain(
            "The four pathways",
            "<p>Energy is <b>transferred</b> between stores in one of four ways:</p>" + PATHWAYS_TABLE +
            "<p>A full description names the store the energy leaves, the store it ends up in, and the pathway. The sentence to learn: <b>energy is transferred from the chemical store of the battery to the kinetic store of the motor, electrically.</b></p>",
        ),
        worked(
            "Describing a transfer",
            "A battery-powered toy car accelerates along the floor. Describe the energy transfer. (2 marks)",
            [
                "<b>Which store does the energy start in?</b> The battery — a <b>chemical</b> store.",
                "<b>Which store does it end up in?</b> The moving car — a <b>kinetic</b> store.",
                "<b>Which pathway?</b> A current flows from the battery to the motor, so the transfer is <b>electrical</b>; the motor then transfers it <b>mechanically</b> to the car.",
                "<b>Answer:</b> Energy is transferred from the <b>chemical store</b> of the battery to the <b>kinetic store</b> of the car, <b>electrically</b> (via the motor). One mark for the two stores, one for the pathway.",
            ],
        ),
        practice("Stores and pathways", [
            choice("en-n1-q1", "A stretched catapult is released and fires a stone. Which store is the energy in before release?",
                   ["Kinetic", "Elastic potential", "Gravitational potential", "Chemical"], 1,
                   "The stretched rubber holds energy in its elastic potential store. When it is released, energy is transferred mechanically to the kinetic store of the stone."),
            choice("en-n1-q2", "Which of these is a pathway, not a store?",
                   ["Thermal", "Nuclear", "By heating", "Magnetic"], 2,
                   "\"By heating\" is one of the four pathways. Thermal, nuclear and magnetic are stores."),
            choice("en-n1-q3", "A candle burns and lights a room. Which description is in the form the mark scheme credits?",
                   ["Chemical energy turns into light energy", "Energy is transferred from the chemical store of the wax to the thermal store of the surroundings, by heating and by radiation (light)", "The candle uses up its energy as light and heat", "Heat energy is made from the wax"], 1,
                   "Name the starting store, the finishing store and the pathway. \"Light energy\" and \"heat energy\" are not stores, and energy is never \"used up\" or \"made\"."),
            written("en-n1-q4", "A ball is thrown straight up. Describe the energy transfer as it rises. (2)",
                    marks(["Energy is transferred from the <b>kinetic store</b> of the ball to its <b>gravitational potential store</b>…",
                           "…<b>mechanically</b> (the force of gravity does work on the ball). Some energy is also transferred to the <b>thermal store of the air</b> by air resistance."]),
                    lines=3, hint="Store it leaves → store it goes to → pathway."),
            written("en-n1-q5", "State the eight energy stores. (2)",
                    marks(["Kinetic, gravitational potential, elastic potential, thermal…", "…chemical, nuclear, electrostatic, magnetic. (All eight for 2 marks; six or seven for 1.)"]),
                    lines=3),
            choice("en-n1-q6", "A kettle boils water. Which pathway transfers energy from the element to the water?",
                   ["Electrically", "By heating", "Mechanically", "By radiation"], 1,
                   "Energy reaches the element electrically; the hot element then transfers energy to the cooler water by heating. The question asks about element → water."),
        ]),
    ],
)
section_n1["subtopic"] = ["3", "8"]

# ---------------------------------------------------------------------
# N2 · Conservation of energy and closed systems
# ---------------------------------------------------------------------

section_n2 = section(
    "conservation", "nn", "Conservation of energy and closed systems", "3.4, 3.6, 8.3",
    equations=[r"\text{total energy in} = \text{total energy out}", r"\text{useful} + \text{wasted} = \text{input}"],
    blurb="Energy cannot be created or destroyed. It is only ever transferred between stores, so the total before equals the total after.",
    checklist=[
        "State the law of conservation of energy in the mark-scheme words",
        "State what a closed system is and what it means for the total energy",
        "Use \"input = useful + wasted\" to find a missing energy value",
    ],
    parts=[
        explain(
            "The law, in the words that score",
            "<p><b>Energy cannot be created or destroyed. It can only be transferred from one store to another.</b> That is the whole law; learn it word for word.</p>"
            "<p>Two things follow from it:</p><ul>"
            "<li>In a <b>closed system</b> — one where no energy gets in or out — the <b>total energy does not change</b>, however much is moved between stores inside it.</li>"
            "<li>In any transfer, <b>energy input = useful energy output + wasted energy</b>. If 100 J goes into a lamp and 5 J comes out as light, 95 J has been wasted (dissipated) — it has not disappeared.</li></ul>"
            "<p>\"Energy is lost\" scores nothing on its own. Say where it went: <i>dissipated to the thermal store of the surroundings</i>.</p>",
        ),
        worked(
            "Finding the wasted energy",
            "A motor is supplied with 600 J of energy and lifts a load, giving it 450 J of gravitational potential energy. Calculate the energy wasted, and say where it goes. (3 marks)",
            [
                r"<b>Conservation:</b> input = useful + wasted, so wasted = input − useful.",
                r"<b>Working:</b> wasted $= 600 - 450 = 150$ J.",
                "<b>Where it goes:</b> the 150 J is <b>dissipated</b> — transferred by heating (friction in the motor, the current in its wires) to the <b>thermal store of the surroundings</b>.",
                "The total is still 600 J: 450 J in the gravitational store of the load plus 150 J in the thermal store of the surroundings.",
            ],
        ),
        practice("Conservation", [
            written("en-n2-q1", "State the law of conservation of energy. (1)",
                    marks(["Energy <b>cannot be created or destroyed</b>; it can only be <b>transferred</b> from one store to another."]), lines=2),
            numeric("en-n2-q2", "A lamp is supplied with 40 J of energy each second and transfers 8 J of it as light. Calculate the energy wasted each second.",
                    40 - 8, "J", "Input = useful + wasted.",
                    [r"wasted $= 40 - 8 = 32$ J, transferred by heating to the thermal store of the surroundings."]),
            choice("en-n2-q3", "What is meant by a closed system?",
                   ["A system with no moving parts", "A system where no energy can enter or leave", "A system where energy is used up", "A system with no friction"], 1,
                   "A closed system is one where no energy is transferred in or out, so its total energy stays constant."),
            numeric("en-n2-q4", "A ball is dropped with 12 J in its gravitational store. Just before it lands it has 10.5 J in its kinetic store. Calculate the energy transferred to the thermal store of the air.",
                    12 - 10.5, "J", "The total is still 12 J; the missing part went to the air by air resistance.",
                    [r"$12 - 10.5 = 1.5$ J has been transferred to the thermal store of the air (and the ball) by the air resistance doing work."]),
            written("en-n2-q5", "A student says \"the pendulum stops swinging because its energy has been used up\". Explain what is wrong with this statement. (2)",
                    marks(["Energy <b>cannot be destroyed</b> or used up — the total is conserved.",
                           "The pendulum's energy has been <b>dissipated</b>: transferred to the <b>thermal store of the surroundings</b> (by air resistance and friction at the pivot), where it is spread out and no longer useful."]),
                    lines=3),
        ]),
    ],
)
section_n2["subtopic"] = ["3", "8"]

# ---------------------------------------------------------------------
# N3 · Energy transfer diagrams (Sankey)
# ---------------------------------------------------------------------

SANKEY_SVG = (
    # input: 40 px tall (100 J); useful carries on 30 px tall (75 J); wasted band 10 px (25 J) bends down
    "<rect x='20' y='50' width='140' height='40' style='fill:var(--accent);opacity:0.25;stroke:var(--accent);stroke-width:1.5'/>"
    "<polygon points='160,50 300,50 300,35 350,65 300,95 300,80 160,80' style='fill:var(--accent);opacity:0.25;stroke:var(--accent);stroke-width:1.5'/>"
    "<polygon points='150,80 160,80 160,160 172,160 155,185 138,160 150,160' style='fill:var(--line);opacity:0.35;stroke:var(--line);stroke-width:1.5'/>"
    "<text x='30' y='44' font-size='15' style='fill:var(--ink)'>input 100 J</text>"
    "<text x='200' y='30' font-size='15' style='fill:var(--accent);font-weight:700'>useful 75 J</text>"
    "<text x='185' y='140' font-size='14' style='fill:var(--ink-2)'>wasted 25 J</text>"
    "<text x='185' y='158' font-size='12' style='fill:var(--ink-2)'>(thermal store of the surroundings)</text>"
    "<text x='30' y='108' font-size='12' style='fill:var(--ink-2)'>widths 100 : 75 : 25</text>"
)

section_n3 = section(
    "sankey", "nn", "Energy transfer diagrams", "3.3, 8.2",
    equations=[r"\text{width of arrow} \propto \text{energy}", r"\text{in} = \text{useful} + \text{wasted}"],
    blurb="A Sankey diagram shows an energy transfer as arrows whose <b>width</b> is proportional to the energy. Useful energy goes straight on; wasted energy bends away (usually down).",
    checklist=[
        "Read the input, useful and wasted energies from a Sankey diagram, using widths or labels",
        "Draw a Sankey diagram to scale from given energy values",
        "Work out the efficiency from a Sankey diagram",
    ],
    parts=[
        explain(
            "Reading and drawing one",
            diagram(SANKEY_SVG, 400, 200, "A Sankey diagram for a 75% efficient motor. The input arrow (100 J) splits: the useful arrow carries on (75 J); the wasted arrow bends down (25 J). Widths are in proportion: 100 : 75 : 25.") +
            "<p>Rules:</p><ul><li>The input arrow starts on the left; its width represents the <b>total energy in</b>.</li>"
            "<li><b>Useful</b> output arrows carry straight on to the right; <b>wasted</b> output arrows bend off (down).</li>"
            "<li>Widths add up: the output widths together equal the input width, because energy is conserved.</li>"
            "<li>Label every arrow with the store or the pathway and the number of joules (or the power in watts).</li></ul>"
            "<p>To draw one: choose a scale (say 1 square = 10 J), draw the input arrow that many squares wide, then split it so each branch has the right number of squares.</p>",
        ),
        worked(
            "Numbers from a diagram",
            "A Sankey diagram for a kettle shows an input arrow 20 squares wide, a useful arrow (thermal store of the water) 18 squares wide and a wasted arrow 2 squares wide. The input is 2000 J. Find the useful energy, the wasted energy and the efficiency.",
            [
                r"<b>Scale:</b> 20 squares = 2000 J, so 1 square = 100 J.",
                r"<b>Useful:</b> $18 \times 100 = 1800$ J. <b>Wasted:</b> $2 \times 100 = 200$ J. Check: $1800 + 200 = 2000$ J ✓",
                r"<b>Efficiency:</b> $\dfrac{\text{useful}}{\text{total}} = \dfrac{1800}{2000} = 0.9$, or 90%.",
            ],
        ),
        practice("Sankey diagrams", [
            numeric("en-n3-q1", "A Sankey diagram for a lamp has an input arrow 10 squares wide and a useful (light) arrow 2 squares wide. The input is 50 J. Calculate the wasted energy.",
                    50 - 50 * 2 / 10, "J", "Wasted width = $10 - 2 = 8$ squares; 1 square = 5 J.",
                    [r"1 square $= 50 \div 10 = 5$ J.", r"Wasted $= 8 \times 5 = 40$ J (thermal store of the surroundings)."]),
            numeric("en-n3-q2", "A motor's Sankey diagram shows 300 J in, 120 J to the kinetic store of the load and the rest wasted. Calculate the width of the wasted arrow if the input arrow is 15 squares wide.",
                    (300 - 120) / 20, "squares", "Find the wasted energy first, then the scale.",
                    [r"Wasted $= 300 - 120 = 180$ J.", r"Scale: $300 \div 15 = 20$ J per square.", r"Width $= 180 \div 20 = 9$ squares."]),
            choice("en-n3-q3", "In a Sankey diagram, what does the width of an arrow represent?",
                   ["The time the transfer takes", "The amount of energy transferred", "The speed of the transfer", "The temperature"], 1,
                   "Width is proportional to energy (or power). The length means nothing."),
            written("en-n3-q4", "Draw a Sankey diagram for an electric motor supplied with 500 J that transfers 350 J usefully to the gravitational store of a load. Describe what you drew. (3)",
                    mark_scheme([
                        ("Input", "An input arrow labelled <b>500 J</b> (electrical / total input) on the left."),
                        ("Useful", "A straight-on arrow labelled <b>350 J, gravitational potential store of the load</b>."),
                        ("Wasted", "A branch bending down labelled <b>150 J, thermal store of the surroundings</b> (by heating / friction)."),
                        ("Scale", "Widths in proportion 500 : 350 : 150 (e.g. 10 : 7 : 3 squares)."),
                    ], total=3), lines=4, hint="Three arrows, three labels, widths in proportion."),
        ]),
    ],
)
section_n3["subtopic"] = ["3", "8"]

# ---------------------------------------------------------------------
# N4 · Gravitational potential energy
# ---------------------------------------------------------------------

q4_1 = 2 * G * 1.5
q4_2 = 0.25 * G * 12
q4_3 = 1500 / (G * 5)
q4_4 = round(60 * G * (3 * 0.2))
q4_5 = 0.4 * G * 0.26

section_n4 = section(
    "gpe", "nn", "Gravitational potential energy", "3.1, 8.8",
    equations=[r"\Delta GPE = m \times g \times \Delta h", r"g = 10\ \text{N/kg}"],
    blurb="The energy in an object's gravitational potential store changes when its height changes. It depends on the mass, the gravitational field strength and the <b>change</b> in vertical height.",
    checklist=[
        "Select $\\Delta \\text{GPE} = m \\times g \\times \\Delta h$ from the equation list and say what each symbol is, with units",
        "Use the <i>change</i> in vertical height, in metres",
        "Rearrange for m or Δh",
    ],
    parts=[
        explain(
            "The equation and its traps",
            "<p>$$\\Delta GPE = m \\times g \\times \\Delta h$$</p>"
            "<table class='tbl'><tr><th>Symbol</th><th>Quantity</th><th>Unit</th></tr>"
            "<tr><td>$\\Delta GPE$</td><td>change in gravitational potential energy</td><td>J</td></tr>"
            "<tr><td>$m$</td><td>mass</td><td>kg</td></tr>"
            "<tr><td>$g$</td><td>gravitational field strength (10 N/kg on Earth)</td><td>N/kg</td></tr>"
            "<tr><td>$\\Delta h$</td><td><b>change in vertical height</b></td><td>m</td></tr></table>"
            "<p>The $\\Delta$ (delta) means <i>change in</i>. Three things the examiners' reports say cost marks:</p><ul>"
            "<li><b>Height in centimetres.</b> A trolley raised 26 cm is raised 0.26 m. Forgetting this makes the answer 100 times too big — the single most common error on this equation.</li>"
            "<li><b>The wrong height.</b> Use the <i>vertical</i> change in height, not the distance along a slope, and not the height above sea level unless that is the change.</li>"
            "<li><b>Mass in grams.</b> 320 g is 0.32 kg.</li></ul>"
            "<p>$m \\times g$ is the weight, so $\\Delta GPE = \\text{weight} \\times \\Delta h$ — the work done lifting it.</p>",
        ),
        worked(
            "GPE of a lifted mass",
            "A 2 kg mass is lifted from the floor onto a shelf 1.5 m high. Calculate the increase in its gravitational potential energy. ($g = 10$ N/kg)",
            ewau(r"\Delta GPE = m \times g \times \Delta h", r"\Delta GPE = 2 \times 10 \times 1.5", "30", "J"),
        ),
        practice("GPE", [
            numeric("en-n4-q1", "A 2.0 kg bag is lifted 1.5 m onto a table. Calculate the change in its GPE. ($g = 10$ N/kg)",
                    q4_1, "J", "$\\Delta \\text{GPE} = m \\times g \\times \\Delta h$, with h in metres.",
                    ewau(r"\Delta GPE = m \times g \times \Delta h", r"\Delta GPE = 2.0 \times 10 \times 1.5", "30", "J")),
            numeric("en-n4-q2", "A 250 g apple falls 12 m from a tree. Calculate the GPE it loses. ($g = 10$ N/kg)",
                    q4_2, "J", "250 g = 0.25 kg.",
                    ewau(r"\Delta GPE = m \times g \times \Delta h", r"\Delta GPE = 0.25 \times 10 \times 12", "30", "J")),
            numeric("en-n4-q3", "A crane gives a load 1500 J of GPE by lifting it 5.0 m. Calculate the mass of the load. ($g = 10$ N/kg)",
                    q4_3, "kg", "Rearrange: $m = \\Delta \\text{GPE} \\div (g \\times \\Delta h)$.",
                    ewau(r"\Delta GPE = m \times g \times \Delta h", r"1500 = m \times 10 \times 5.0 \;\Rightarrow\; m = \dfrac{1500}{50}", "30", "kg")),
            numeric("en-n4-q4", "A 60 kg student climbs three stairs, each 20 cm high. Calculate the increase in her GPE. ($g = 10$ N/kg)",
                    q4_4, "J", "Total vertical height = 3 × 0.20 m.",
                    [r"$\Delta h = 3 \times 0.20 = 0.60$ m (centimetres to metres first)."] + ewau(r"\Delta GPE = m \times g \times \Delta h", r"\Delta GPE = 60 \times 10 \times 0.60", "360", "J")),
            numeric("en-n4-q5", "A trolley of mass 0.40 kg is lifted onto a runway 26 cm above the bench. Calculate the increase in its GPE. ($g = 10$ N/kg)",
                    sf(q4_5, 3), "J", "26 cm = 0.26 m. The examiners' report says this conversion was the most common error.",
                    ewau(r"\Delta GPE = m \times g \times \Delta h", r"\Delta GPE = 0.40 \times 10 \times 0.26", "1.04", "J")),
            choice("en-n4-q6", "A ball rolls 4 m down a slope that drops 1 m vertically. Which height goes into $\\Delta \\text{GPE} = m g \\Delta h$?",
                   ["4 m", "1 m", "5 m", "3 m"], 1,
                   "Only the vertical change in height counts. The 4 m along the slope is the distance moved, which is a work-done quantity, not a height."),
        ]),
    ],
)
section_n4["subtopic"] = ["3", "8"]

# ---------------------------------------------------------------------
# N5 · Kinetic energy
# ---------------------------------------------------------------------

q5_1 = 0.5 * 1200 * 16 ** 2
q5_2 = 0.5 * 0.16 * 30 ** 2
q5_3 = (2 * 950 / 35) ** 0.5
q5_4 = 0.5 * 0.0575 * 50 ** 2
q5_5 = 0.5 * 70 * (36 * 1000 / 3600) ** 2

section_n5 = section(
    "ke", "nn", "Kinetic energy", "3.2, 8.9",
    equations=[r"KE = \tfrac{1}{2} \times m \times v^{2}"],
    blurb="The energy in a moving object's kinetic store. The speed is squared, so it matters far more than the mass.",
    checklist=[
        "Select $\\text{KE} = \\tfrac{1}{2} m v^2$ and say what each symbol is, with units",
        "Square the speed before multiplying — and only the speed",
        "Find v from KE: $v^2 = 2\\text{KE} \\div m$, then take the square root",
    ],
    parts=[
        explain(
            "The equation and its traps",
            "<p>$$KE = \\tfrac{1}{2} \\times m \\times v^{2}$$</p>"
            "<table class='tbl'><tr><th>Symbol</th><th>Quantity</th><th>Unit</th></tr>"
            "<tr><td>$KE$</td><td>kinetic energy</td><td>J</td></tr>"
            "<tr><td>$m$</td><td>mass</td><td>kg</td></tr>"
            "<tr><td>$v$</td><td>speed</td><td>m/s</td></tr></table>"
            "<p>Calculator order: <b>square the speed, multiply by the mass, halve it.</b> The examiners' reports list the two errors every year: forgetting to square $v$ (the June 2023 scheme gives 1 mark of 2 for that) and forgetting the ½.</p>"
            "<p>Write the equation out before you substitute — \"write out the equation to remind yourself of the square for velocity\" is the examiners' own advice.</p>"
            "<p>Going backwards: $v^{2} = \\dfrac{2 \\times KE}{m}$, then <b>square-root</b>. Stopping at $v^{2}$ (54 m/s instead of 7.4 m/s) loses the last mark.</p>",
        ),
        worked(
            "KE of a car",
            "A car of mass 1200 kg travels at 16 m/s. Calculate its kinetic energy. Give your answer in kJ.",
            ewau(r"KE = \tfrac{1}{2} \times m \times v^{2}", r"KE = \tfrac{1}{2} \times 1200 \times 16^{2} = \tfrac{1}{2} \times 1200 \times 256", "153\\,600\\ \\text{J} = 150", "kJ (to 2 s.f.)"),
        ),
        practice("Kinetic energy", [
            numeric("en-n5-q1", "A car of mass 1200 kg travels at 16 m/s. Calculate its kinetic energy in joules.",
                    q5_1, "J", "Square 16 first.",
                    ewau(r"KE = \tfrac{1}{2} m v^{2}", r"KE = \tfrac{1}{2} \times 1200 \times 16^{2}", "153\\,600", "J")),
            numeric("en-n5-q2", "A cricket ball of mass 160 g is bowled at 30 m/s. Calculate its kinetic energy.",
                    q5_2, "J", "160 g = 0.16 kg.",
                    ewau(r"KE = \tfrac{1}{2} m v^{2}", r"KE = \tfrac{1}{2} \times 0.16 \times 30^{2} = \tfrac{1}{2} \times 0.16 \times 900", "72", "J")),
            numeric("en-n5-q3", "A 35 kg child on a slide has 950 J of kinetic energy at the bottom. Calculate her speed. Give your answer to 2 significant figures.",
                    sf(q5_3, 2), "m/s", "$v^2 = 2 \\times \\text{KE} \\div m$, then square root.",
                    [r"$v^{2} = \dfrac{2 \times 950}{35} = 54.3$",
                     r"$v = \sqrt{54.3} = 7.37 = 7.4$ m/s (2 s.f.). Writing 54 m/s — forgetting the square root — scores 2 of the 3 marks."]),
            numeric("en-n5-q4", "A tennis ball of mass 57.5 g leaves a racket at 50 m/s. Calculate its kinetic energy. Give your answer to 2 significant figures.",
                    sf(q5_4, 2), "J", "57.5 g = 0.0575 kg; 50² = 2500.",
                    ewau(r"KE = \tfrac{1}{2} m v^{2}", r"KE = \tfrac{1}{2} \times 0.0575 \times 50^{2}", "71.9 = 72", "J (2 s.f.)")),
            numeric("en-n5-q5", "A 70 kg cyclist rides at 36 km/h. Calculate his kinetic energy.",
                    q5_5, "J", "36 km/$h = 10$ m/s. Convert the speed before squaring.",
                    [r"$36\ \text{km/h} = \dfrac{36\,000}{3600} = 10$ m/s."] + ewau(r"KE = \tfrac{1}{2} m v^{2}", r"KE = \tfrac{1}{2} \times 70 \times 10^{2}", "3500", "J")),
            choice("en-n5-q6", "A van doubles its speed. What happens to its kinetic energy?",
                   ["It doubles", "It halves", "It quadruples (×4)", "It stays the same"], 2,
                   "$\\text{KE} \\propto v^2$. Doubling v multiplies v² by 4. Trebling the speed would give nine times the KE."),
        ]),
    ],
)
section_n5["subtopic"] = ["3", "8"]

# ---------------------------------------------------------------------
# N6 · Work done
# ---------------------------------------------------------------------

q6_1 = 50 * 4
q6_2 = 7440 / 645
q6_3 = 1800 / 1.2
q6_4 = 20 * 10 * 2.5
q6_5 = 400 * 0.5

section_n6 = section(
    "work", "nn", "Work done = force × distance", "8.5, 8.6, 8.7",
    equations=[r"E = F \times d", r"\text{work done} = \text{energy transferred}", r"1\ \text{J} = 1\ \text{N m}"],
    blurb="When a force moves something, it does <b>work</b>, and the work done is the energy transferred. The distance is the distance moved <b>in the direction of the force</b>.",
    checklist=[
        "State that work done = energy transferred, and that 1 J = 1 N m",
        "Select $E = F \\times d$ and use the distance in the direction of the force",
        "Describe how to measure the work done by a force (newton meter and metre rule)",
    ],
    parts=[
        explain(
            "Work is energy transferred by a force",
            "<p>$$E = F \\times d$$</p><p>work done (J) = force (N) × distance moved <b>in the direction of the force</b> (m).</p>"
            "<p>Work done is a way of transferring energy <b>mechanically</b>. Push a box 3 m with a 50 N force and you have done $50 \\times 3 = 150$ J of work — 150 J has been transferred from your chemical store to the box (its kinetic store, and the thermal store of the floor by friction).</p>"
            "<p><b>Work done = energy transferred.</b> One joule is the work done when a force of one newton moves something one metre: $1\\ \\text{J} = 1\\ \\text{N m}$.</p>"
            "<p>The distance must be <b>in the direction of the force</b>. Carrying a bag horizontally at constant height does no work against gravity, because the weight acts vertically and the bag does not move vertically. Lifting it does: work = weight × height, which is why $m g \\Delta h$ is the GPE equation.</p>"
            "<p><b>Measuring it:</b> pull the object with a <b>newton meter</b> and read the force; measure the distance moved with a <b>metre rule</b>; multiply.</p>",
        ),
        worked(
            "Work done pushing a box",
            "A student pushes a box 4.0 m along the floor with a steady force of 50 N. Calculate the work done. (2 marks)",
            ewau(r"E = F \times d", r"E = 50 \times 4.0", "200", "J"),
        ),
        practice("Work done", [
            numeric("en-n6-q1", "A force of 50 N pushes a trolley 4 m. Calculate the work done.",
                    q6_1, "J", "$E = F \\times d$.",
                    ewau(r"E = F \times d", r"E = 50 \times 4", "200", "J")),
            numeric("en-n6-q2", "A cyclist does 7440 J of work against a resistive force of 645 N. Calculate the distance moved. Give your answer to 3 significant figures.",
                    sf(q6_2, 3), "m", "Rearrange: $d = E \\div F$. The 2024 mark scheme gave 11.53 m only 2 of 3 marks — round to 3 s.f.",
                    ewau(r"E = F \times d", r"7440 = 645 \times d \;\Rightarrow\; d = \dfrac{7440}{645}", "11.5", "m (3 s.f.)")),
            numeric("en-n6-q3", "A pulley system does 1800 J of work lifting a load through 1.2 m. Calculate the force on the load.",
                    q6_3, "N", "$F = E \\div d$.",
                    ewau(r"E = F \times d", r"1800 = F \times 1.2 \;\Rightarrow\; F = \dfrac{1800}{1.2}", "1500", "N")),
            numeric("en-n6-q4", "A 20 kg box is lifted 2.5 m. Calculate the work done against gravity. ($g = 10$ N/kg)",
                    q6_4, "J", "The force needed is the weight, $m \\times g$.",
                    [r"Weight $= m \times g = 20 \times 10 = 200$ N."] + ewau(r"E = F \times d", r"E = 200 \times 2.5", "500", "J")),
            numeric("en-n6-q5", "A brake pad presses on a wheel with a friction force of 400 N while the wheel rim moves 50 cm past it. Calculate the work done by friction.",
                    q6_5, "J", "50 cm = 0.5 m.",
                    ewau(r"E = F \times d", r"E = 400 \times 0.5", "200", "J — transferred to the thermal store of the brakes")),
            written("en-n6-q6", "Describe how a student could measure the work done in pulling a wooden block across a bench. (3)",
                    mark_scheme([
                        ("Force", "Pull the block with a <b>newton meter</b> (force meter) and read the <b>force</b> while it moves steadily."),
                        ("Distance", "Measure the <b>distance</b> the block moves with a <b>metre rule</b>."),
                        ("Calculate", "Work done = <b>force × distance</b> (in the direction of the force)."),
                    ]), lines=4, hint="Two measurements with named instruments, then the equation."),
            choice("en-n6-q7", "A waiter carries a tray horizontally across a room at constant height and constant speed. How much work does he do against gravity?",
                   ["Weight × distance across the room", "Zero", "Weight × height of the tray", "Mass × distance"], 1,
                   "The weight acts vertically and the tray does not move vertically, so no work is done against gravity. (He does a little work against air resistance.)"),
        ]),
    ],
)
section_n6["subtopic"] = ["8"]

SECTIONS = [section_n1, section_n2, section_n3, section_n4, section_n5, section_n6]
