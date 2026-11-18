"""
el_tricky.py — Topic 10 (Electricity and circuits): the tricky bits T1–T9
and the flashcards.

T1 Core practical: I–V for a resistor and a lamp   T6 Energy and power the hard way
T2 Testing series and parallel circuits          T7 Mains safety explained
T3 Explaining the I–V curves                     T8 Explaining with electrons
T4 Circuit calculations the hard way             T9 The seven steps for this topic
T5 Sensing circuits
"""

from revlib import (
    choice, diagram, explain, fact, group, mark_scheme, marks, numeric,
    practice, section, worked, written,
)
import el_diagrams as dg

# ---------------------------------------------------------------------
# T1 · Core practical: I–V characteristics
# ---------------------------------------------------------------------

section_t1 = section(
    "iv-practical", "tricky", "Core practical: I–V characteristics of a resistor and a filament lamp", "10.17a",
    equations=[r"\text{vary } V \text{ with the variable resistor; read } I \text{ and } V;\ R = V/I"],
    blurb="The circuit is three marks on its own, the method is a 6-marker, and the examiners' complaints are the same every year: voltmeter in the wrong place, no way of varying the pd, no negative values, no mention of the resistor warming up.",
    checklist=[
        "Draw the circuit: supply, variable resistor and ammeter in series with the component, voltmeter across it",
        "Describe the method, including how the pd is varied and how negative values are obtained",
        "State the precautions: switch off between readings, repeat and average",
    ],
    parts=[
        explain(
            "The circuit and the method",
            diagram(dg.iv_practical_svg(), 760, 280, "The circuit for 10.17a. The variable resistor changes the current and so the pd across the component.") +
            "<ol><li><b>Set up</b> the circuit: supply, <b>variable resistor</b>, <b>ammeter</b> and the <b>component</b> (resistor first) in series; <b>voltmeter across the component</b>.</li>"
            "<li><b>Adjust the variable resistor</b> to the lowest current; record the <b>current</b> (A) and the <b>pd</b> (V).</li>"
            "<li>Move the slider to <b>increase the pd in steps</b> (say 0.5 V), recording I and V each time, up to the component's rated pd.</li>"
            "<li><b>Reverse the connections</b> to the supply (swap the leads) and repeat, to get the <b>negative</b> values.</li>"
            "<li><b>Switch off between readings</b> (or take them quickly) so the component does not warm up and change its resistance; <b>repeat</b> each reading and take a <b>mean</b>.</li>"
            "<li>Replace the resistor with the <b>filament lamp</b> and repeat.</li>"
            "<li><b>Plot I (y) against V (x)</b>; the shape gives the resistance behaviour; $R = V/I$ at any point.</li></ol>"
            "<p>Control variables: the same component, the same temperature (as far as possible), the same meters. The June 2024 scheme (Q8(a)) gave one mark each for the variable resistor in series, the ammeter in series with the lamp and the voltmeter in parallel with the lamp; Q8(b)(i) credited data-logging for \"collecting data in a short time\" or \"simultaneous current and voltage readings\" — \"more accurate\" was ignored. The June 2022 report (Q2(c), the same circuit used on a length of resistance wire): \"labelling and inserting the resistance wire carefully was the key to scoring maximum marks\" — draw and label every component.</p>",
        ),
        worked(
            "The 6-mark method",
            "Describe how to investigate how the current in a filament lamp varies with the potential difference across it. (6 marks)",
            [
                "<b>Circuit:</b> connect the lamp in <b>series</b> with an <b>ammeter</b>, a <b>variable resistor</b> and a d.c. supply; connect a <b>voltmeter across the lamp</b>.",
                "<b>Vary:</b> use the <b>variable resistor</b> to change the pd across the lamp in equal steps from 0 up to its rated pd.",
                "<b>Measure:</b> at each setting record the <b>pd</b> from the voltmeter and the <b>current</b> from the ammeter.",
                "<b>Reverse:</b> swap the connections to the supply and repeat, so that negative pds and currents are recorded.",
                "<b>Reliability:</b> repeat each reading and calculate a mean; switch off between readings so the lamp's temperature does not drift.",
                "<b>Analyse:</b> plot current (y) against pd (x); a curve that flattens shows the resistance increasing; calculate $R = V/I$ at points to confirm.",
            ],
        ),
        practice("The I–V practical", [
            written("el-t1-q1", "Describe the circuit used to find how the current in a resistor depends on the pd across it. (3)",
                    marks(["The resistor, an <b>ammeter</b> and a <b>variable resistor</b> in <b>series</b> with a (d.c.) supply.", "A <b>voltmeter in parallel</b> with (across) the resistor only.", "The variable resistor is adjusted to change the pd across (and current in) the resistor."]), lines=3),
            choice("el-t1-q2", "How are the negative-pd values on the I–V graph obtained?",
                   ["By using a bigger resistor", "By reversing the connections to the supply", "By reading the voltmeter upside down", "They cannot be obtained"], 1,
                   "Reverse the supply (or use a reversing switch)."),
            written("el-t1-q3", "Explain why the circuit should be switched off between readings when investigating a resistor. (2)",
                    marks(["A current <b>heats</b> the resistor (electrons colliding with ions)…", "…and a hotter resistor has a <b>higher resistance</b>, so the readings would not be for one fixed resistance — the graph would curve."]), lines=2),
            written("el-t1-q4", "A student uses a data logger instead of meters. Give one advantage. (1)",
                    marks(["Readings of current and pd are taken <b>at the same instant</b> / many readings in a short time / the graph is produced immediately (not \"more accurate\")."]), lines=1),
            choice("el-t1-q5", "In the I–V practical, what is the independent variable?",
                   ["The current", "The pd across the component", "The resistance", "The temperature"], 1,
                   "You set the pd (with the variable resistor) and measure the current."),
            written("el-t1-q6", "State why a variable resistor is included in the circuit. (1)",
                    marks(["To <b>change the pd across</b> (and the current in) the component, so a range of readings can be taken."]), lines=1),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T2 · Testing series and parallel circuits
# ---------------------------------------------------------------------

section_t2 = section(
    "series-parallel-practical", "tricky", "Testing series and parallel circuits (10.17b)", "10.16, 10.17b",
    equations=[r"\text{series: } V_1 + V_2 = V_{\text{cell}}", r"\text{parallel: } I_1 + I_2 = I_{\text{cell}}"],
    blurb="The 2025 6-marker: describe how to test resistors in series and in parallel. Level 3 needed both circuits drawn with the meters in the right places, the expected readings, and the rules stated as what you would find.",
    checklist=[
        "Draw the series and parallel test circuits with meters in the right places",
        "State what readings to take and what they show",
        "Describe what happens to lamps in series and in parallel when one is removed",
    ],
    parts=[
        explain(
            "The two test circuits",
            diagram(dg.test_circuits_svg(), 700, 285, "Testing two resistors in series and in parallel: where the meters go and what they show.") +
            "<p><b>Series test:</b> two resistors in one loop with the cell; an <b>ammeter</b> anywhere in the loop (move it round to show the current is the <b>same everywhere</b>); a <b>voltmeter across each resistor</b> and across the cell: the two pds <b>add up</b> to the cell's pd, the bigger resistor taking the bigger share. Add a third resistor and the current falls — resistances add.</p>"
            "<p><b>Parallel test:</b> the two resistors in separate branches; an <b>ammeter in each branch</b> and one by the cell: the branch currents <b>add up</b> to the cell current; a voltmeter across either branch reads the <b>same as the cell</b>. Add a branch and the cell current rises — total resistance falls.</p>"
            "<p>The June 2025 report (Q10(c), 6 marks): Level 3 answers had \"correct circuit diagrams for both arrangements, with ammeters and voltmeters placed correctly\", included <b>expected values</b>, and explained \"voltage sharing\" in series, \"the current being shared between branches\" in parallel and \"the same current throughout the series circuit\". Level 2 had one circuit done properly; Level 1 \"a misplaced voltmeter and no parallel circuit\". The spec also asks you to explain the <b>design</b> of such circuits (10.16): every component you add is there to measure one quantity, and the meters must not change what they measure (voltmeter high resistance, ammeter low).</p>"
            "<p><b>Lamps:</b> two identical lamps in series each get half the pd and are dim; unscrew one and the other goes out. In parallel each gets the full pd and is bright; unscrew one and the other is unaffected. The June 2022 report (Q2(b)): to say which circuit's lamp is brighter you need both the <b>pd</b> argument (the pd across it is halved in series) and the <b>power</b> argument — most gave one \"but rarely both\".</p>",
        ),
        worked(
            "The 6-mark description",
            "Describe how a student could test the rules for current and potential difference in series and parallel circuits using two resistors, a cell, ammeters and voltmeters. (6 marks)",
            [
                "<b>Series circuit:</b> connect the two resistors and an ammeter in one loop with the cell; a voltmeter across each resistor and one across the cell.",
                "Move the ammeter to different positions: the <b>current is the same</b> at every point. The voltmeter readings across the two resistors <b>add up</b> to the reading across the cell (e.g. 2 V + 4 V = 6 V): the pd is shared.",
                "<b>Parallel circuit:</b> connect the two resistors in separate branches across the cell; an ammeter in each branch and one next to the cell; a voltmeter across each branch.",
                "The branch currents <b>add up</b> to the cell current (e.g. 0.3 A + 0.6 A = 0.9 A): the current is shared. Each voltmeter reads the <b>same</b> as the cell (6 V): the pd is the same across every branch.",
                "<b>Resistance:</b> in series the current is <b>smaller</b> than with one resistor (resistances add); in parallel the cell current is <b>larger</b> (total resistance is less than either).",
                "Check with $V = IR$ for each resistor in each circuit; repeat readings to be sure.",
            ],
        ),
        practice("Series and parallel tests", [
            written("el-t2-q1", "Describe where to connect the meters to show that the current is the same everywhere in a series circuit. (2)",
                    marks(["Connect an <b>ammeter in series</b> at one point and record the current…", "…then move it to <b>other points</b> in the loop (or use several ammeters) and show the readings are the <b>same</b>."]), lines=2),
            written("el-t2-q2", "Two lamps are connected in series to a cell. One lamp is unscrewed. Explain what happens to the other lamp. (2)",
                    marks(["It <b>goes out</b>.", "There is only <b>one path</b>; removing a lamp <b>breaks the circuit</b>, so there is no current anywhere in it."]), lines=2),
            choice("el-t2-q3", "Two identical lamps are connected in parallel instead of in series across the same cell. Each lamp is…",
                   ["dimmer, because the current is shared", "brighter, because each now has the full pd of the cell across it", "the same brightness", "off"], 1,
                   "Full pd → more current in each → more power."),
            written("el-t2-q4", "Explain why a lamp is brighter in a parallel circuit than when the same two lamps are in series. (3)",
                    mark_scheme([
                        ("pd", "In parallel each lamp has the <b>full pd</b> of the cell across it; in series the pd is <b>shared</b> (halved for identical lamps)."),
                        ("Current", "With a larger pd across it the lamp carries a <b>larger current</b> ($I = V/R$)."),
                        ("Power", "Power $= I \\times V$ is larger, so more energy is transferred per second — brighter."),
                    ]), lines=4),
            written("el-t2-q5", "In the parallel test, the ammeter next to the cell reads 0.9 A and one branch carries 0.3 A. State what the other branch carries and the rule this shows. (2)",
                    marks(["<b>0.6 A</b>.", "The branch currents <b>add up</b> to the current from the cell (current is conserved at a junction)."]), lines=2),
            choice("el-t2-q6", "Why is a voltmeter's resistance made very high?",
                   ["So it can carry a large current", "So that it takes almost no current and does not change the circuit it measures", "To make it cheaper", "So it can be used in series"], 1,
                   "A meter must not change what it measures."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T3 · Explaining the I–V curves
# ---------------------------------------------------------------------

section_t3 = section(
    "iv-explain", "tricky", "Explaining the I–V curves, and the gradient trap", "10.18, 10.24",
    equations=[r"R = \dfrac{V}{I}\ \text{at the point — not the gradient}"],
    blurb="Describing the curve is two marks; explaining it is the hard part. The lamp's curve comes from temperature → ion vibration → collisions; the diode's from one-way conduction. And resistance is V ÷ I at a point — the gradient of the curve is not the resistance.",
    checklist=[
        "Explain why a filament lamp's resistance rises with pd in terms of electrons and ions",
        "Explain why a fixed resistor's graph is a straight line and a diode's is one-sided",
        "Find resistance from an I–V graph correctly, and explain why the gradient is not the resistance",
    ],
    parts=[
        explain(
            "Three explanations",
            "<p><b>Fixed resistor</b> (at constant temperature): the current is <b>proportional</b> to the pd — double the pd, double the current — so $V/I$ is the same at every point: <b>constant resistance</b>, a straight line through the origin, the same in both directions. (Ohm's law.)</p>"
            "<p><b>Filament lamp:</b> as the pd rises, the current rises and the filament gets <b>hotter</b> (electron–ion collisions, N9). Hotter means the <b>ions vibrate more</b>, so the electrons <b>collide with them more often</b> and it is harder for the current to get through: the <b>resistance increases</b>. Each extra volt gives less extra current, so the graph <b>flattens</b>. Say the chain: pd ↑ → current ↑ → temperature ↑ → ions vibrate more → more collisions → resistance ↑.</p>"
            "<p><b>Diode:</b> made so that current can pass in <b>one direction only</b>. Reverse-biased, its resistance is <b>very high</b> and the current is zero; forward-biased, once the pd passes about 0.7 V its resistance becomes <b>low</b> and the current rises steeply.</p>"
            "<p><b>The gradient trap.</b> On an I–V graph (I on the y-axis) the gradient is $I/V = 1/R$, not $R$ — and for a curve the gradient at a point is not even that. The resistance at a point is <b>$R = V \\div I$ using the coordinates of the point</b>. The 2024 scheme accepted \"the gradient decreases as pd increases, so resistance increases\" as a <i>comparison</i>, but a numerical resistance must come from V/I. If the axes are the other way round (V against I), the gradient of a straight line is R.</p>",
        ),
        worked(
            "Explain the lamp",
            "Explain why the resistance of a filament lamp increases as the potential difference across it increases. (3 marks)",
            [
                "A larger pd drives a <b>larger current</b>, and the current <b>heats the filament</b> (energy transferred by electrons colliding with the lattice ions).",
                "At a higher temperature the <b>ions vibrate more</b>, so the electrons <b>collide with them more frequently</b>.",
                "More collisions make it harder for charge to flow for a given pd: the <b>resistance increases</b> — so the I–V graph flattens.",
            ],
        ),
        practice("Explaining the curves", [
            written("el-t3-q1", "Explain why the I–V graph for a fixed resistor at constant temperature is a straight line through the origin. (2)",
                    marks(["The current is <b>directly proportional</b> to the pd (doubling V doubles I).", "So $V/I$ — the <b>resistance</b> — is <b>constant</b> at every point (the ions vibrate the same amount throughout, so collisions do not change)."]), lines=2),
            choice("el-t3-q2", "A student finds the gradient of a filament lamp's I–V curve at a point and calls it the resistance. Why is this wrong?",
                   ["Gradients are never used in physics", "Resistance at a point is V ÷ I from the point's coordinates; the gradient of I against V is 1/R for a straight line and not R at all for a curve", "The lamp has no resistance", "The gradient should be in ohms"], 1,
                   "Read the two coordinates and divide."),
            written("el-t3-q3", "Explain why a diode's I–V graph shows zero current for negative values of pd. (2)",
                    marks(["A diode conducts in <b>one direction only</b>.", "For pd in the reverse direction its <b>resistance is very high</b>, so the current is (almost) zero."]), lines=2),
            group("el-t3-q4", "A filament lamp's I–V graph gives 0.10 A at 0.5 V and 0.40 A at 4.0 V.", [
                numeric("el-t3-q4a", "Calculate the resistance at 0.5 V.", 5, "Ω", "V ÷ I.", [r"$0.5 \div 0.10 = 5$ Ω."]),
                numeric("el-t3-q4b", "Calculate the resistance at 4.0 V.", 10, "Ω", "V ÷ I.", [r"$4.0 \div 0.40 = 10$ Ω."]),
                written("el-t3-q4c", "Explain the difference between the two values. (2)",
                        marks(["At 4.0 V the current is larger, so the filament is <b>hotter</b>…", "…the ions vibrate more and the electrons <b>collide with them more often</b>, so the resistance is <b>higher</b>."]), lines=2),
            ]),
            choice("el-t3-q5", "Which graph shape shows a component whose resistance decreases as the pd increases?",
                   ["A straight line through the origin", "A curve that gets steeper as pd increases", "A curve that flattens as pd increases", "A horizontal line"], 1,
                   "Steeper → more current per volt → lower resistance (e.g. a thermistor warming up)."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T4 · Circuit calculations the hard way
# ---------------------------------------------------------------------

section_t4 = section(
    "circuits-hard", "tricky", "Circuit calculations the hard way", "10.14, 10.15",
    equations=[r"\text{series: find } R_{\text{total}}, \text{ then } I, \text{ then each } V = IR", r"\text{parallel: same } V \text{ on each branch; } I = V/R \text{ per branch}"],
    blurb="Three resistors in series, a pd to find across one of them, a current to find in one branch, a cell of unknown pd: the questions that need two steps. The method is always the same — write what is the same (current in series, pd in parallel) and work outwards from it.",
    checklist=[
        "Find the current and each pd in a series circuit with several resistors",
        "Find the current in each branch of a parallel circuit and the supply current",
        "Explain the effect of adding or removing a resistor on current and total resistance",
    ],
    parts=[
        explain(
            "The method",
            "<p><b>Series:</b> (1) add the resistances; (2) $I = V_{\\text{supply}} \\div R_{\\text{total}}$ — this current is the same through everything; (3) each component's pd is $V = I \\times R$; (4) check the pds add up to the supply. The pd is shared <b>in proportion to the resistances</b>: 10 Ω and 30 Ω in series across 8 V take 2 V and 6 V. Removing a resistor from a series circuit <b>lowers</b> the total resistance, so the current <b>rises</b> and the pd across each remaining resistor rises.</p>"
            "<p><b>Parallel:</b> (1) the pd across every branch is the supply pd; (2) each branch current is $I = V \\div R_{\\text{branch}}$; (3) the supply current is the <b>sum</b> of the branch currents; (4) if asked, the total resistance is $R = V_{\\text{supply}} \\div I_{\\text{supply}}$ — and it comes out <b>smaller than the smallest branch</b>. Removing a branch <b>lowers</b> the supply current and <b>raises</b> the total resistance (the June 2024 3-marker, N6).</p>"
            "<p><b>Mixed circuits</b> go beyond what Edexcel asks you to calculate, but one idea covers them: a parallel pair behaves like one resistor of the value found in step (4), which then sits in series with the rest.</p>"
            "<p>Units: mA to A and kΩ to Ω before anything else; and give the pd across a component, not \"the voltage of the resistor\".</p>",
        ),
        worked(
            "Series with three, and a parallel pair",
            "(a) A 9 V battery drives a current through 10 Ω, 20 Ω and 15 Ω resistors in series. Calculate the pd across the 20 Ω resistor. (b) The same battery is connected across a 30 Ω and a 60 Ω resistor in parallel. Calculate the current from the battery and the total resistance of the pair.",
            [
                r"<b>(a)</b> $R = 10 + 20 + 15 = 45$ Ω; $I = \dfrac{9}{45} = 0.2$ A; $V_{20} = 0.2 \times 20 = 4$ V. (Check: $2 + 4 + 3 = 9$ V.)",
                r"<b>(b)</b> Each branch has 9 V across it: $I_{30} = \dfrac{9}{30} = 0.3$ A, $I_{60} = \dfrac{9}{60} = 0.15$ A; supply current $= 0.3 + 0.15 = 0.45$ A.",
                r"Total resistance $= \dfrac{V}{I} = \dfrac{9}{0.45} = 20$ Ω — less than either branch, as it must be.",
            ],
        ),
        practice("Circuits the hard way", [
            group("el-t4-q1", "A 12 V supply is connected to a 4 Ω, a 6 Ω and a 14 Ω resistor in series.", [
                numeric("el-t4-q1a", "Calculate the current in the circuit.", 0.5, "A", "Total R first.", [r"$R = 4 + 6 + 14 = 24$ Ω; $I = 12 \div 24 = 0.5$ A."]),
                numeric("el-t4-q1b", "Calculate the pd across the 14 Ω resistor.", 7, "V", "V = I × R.", [r"$V = 0.5 \times 14 = 7$ V."]),
            ]),
            group("el-t4-q2", "A 6 V battery is connected across a 20 Ω resistor and a 30 Ω resistor in parallel.", [
                numeric("el-t4-q2a", "Calculate the current in the 20 Ω resistor.", 0.3, "A", "Full 6 V across it.", [r"$I = 6 \div 20 = 0.3$ A."]),
                numeric("el-t4-q2b", "Calculate the current from the battery.", 0.5, "A", "Add the branch currents.", [r"$I_{30} = 6 \div 30 = 0.2$ A; total $= 0.3 + 0.2 = 0.5$ A."]),
                numeric("el-t4-q2c", "Calculate the total resistance of the parallel pair.", 12, "Ω", "R = V ÷ I for the whole thing.", [r"$R = 6 \div 0.5 = 12$ Ω — smaller than 20 Ω."]),
            ]),
            numeric("el-t4-q3", "Two resistors, 5 Ω and 15 Ω, are in series. The pd across the 5 Ω resistor is 1.5 V. Calculate the pd of the supply.", 6, "V", "Find the current from the 5 Ω first; it is the same in the 15 Ω.",
                    [r"$I = 1.5 \div 5 = 0.3$ A.", r"$V_{15} = 0.3 \times 15 = 4.5$ V; supply $= 1.5 + 4.5 = 6$ V."]),
            written("el-t4-q4", "A third identical lamp is added in series to two lamps already in series with a cell. Explain what happens to the brightness of the lamps. (3)",
                    mark_scheme([
                        ("Resistance", "The total resistance of the circuit <b>increases</b> (resistances add in series)."),
                        ("Current", "The pd of the cell is unchanged, so the current <b>decreases</b> ($I = V/R$); the pd is now shared three ways."),
                        ("Brightness", "Less current and less pd across each lamp means less power ($P = IV$): all three are <b>dimmer</b>."),
                    ]), lines=4),
            choice("el-t4-q5", "Resistors of 2 Ω, 3 Ω and 6 Ω are connected in parallel. The total resistance is…",
                   ["11 Ω", "between 2 Ω and 6 Ω", "less than 2 Ω", "exactly 2 Ω"], 2,
                   "Always less than the smallest branch (it is 1 Ω here)."),
            numeric("el-t4-q6", "A 3 kΩ and a 1 kΩ resistor are in series across a 12 V supply. Calculate the pd across the 3 kΩ resistor.", 9, "V", "Shared in proportion: 3 : 1.", [r"$I = 12 \div 4000 = 0.003$ A; $V = 0.003 \times 3000 = 9$ V (three quarters of 12 V)."]),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T5 · Sensing circuits
# ---------------------------------------------------------------------

section_t5 = section(
    "sensing-circuits", "tricky", "Sensing circuits: how an LDR or thermistor switches something", "10.19, 10.20, 10.21",
    equations=[r"\text{series pair: the bigger resistance takes the bigger share of the pd}"],
    blurb="An LDR or thermistor on its own just changes resistance. Put it in series with a fixed resistor and the pd across the resistor changes with light or temperature — which is what a sensor circuit uses. The explanation is pd sharing, in words.",
    checklist=[
        "Describe a circuit to explore how an LDR's or thermistor's resistance varies",
        "Explain how the pd across the fixed resistor changes as the light or temperature changes",
        "Apply it to an automatic light, a thermostat or a fire alarm",
    ],
    parts=[
        explain(
            "Exploring and using the variation",
            diagram(dg.sensing_svg(), 760, 310, "An LDR in series with a fixed resistor: the output pd across the resistor rises when it gets brighter.") +
            "<p><b>Exploring the variation</b> (10.21): to measure how the resistance of an LDR changes with light, put the LDR in a circuit with an <b>ammeter in series and a voltmeter across it</b>, change the light level (a lamp at different distances, or layers of tracing paper), and calculate $R = V/I$ each time. For a thermistor, put it in a <b>water bath</b> with a thermometer and change the temperature; take the readings quickly at each temperature. The June 2022 report (Q8(c)): \"very few\" could improve the method of measuring the thermistor's temperature — keep the thermistor <b>fully in the water</b>, <b>stir</b>, read the temperature <b>at the moment</b> the meters are read, and let the bath settle at each temperature.</p>"
            "<p><b>Using it — the pd-sharing argument.</b> Two components in series share the supply pd <b>in proportion to their resistances</b>. With an LDR in series with a fixed resistor:</p>"
            "<ul><li>In the <b>dark</b> the LDR's resistance is <b>high</b>, so it takes <b>most</b> of the pd and the fixed resistor gets <b>little</b>.</li>"
            "<li>In the <b>light</b> the LDR's resistance is <b>low</b>, so it takes <b>little</b> of the pd and the fixed resistor gets <b>most</b>.</li></ul>"
            "<p>So the pd across the fixed resistor is a signal that follows the light level; it can switch a lamp (via a transistor or relay — not on the spec) when it crosses a set value. Swap the components and the signal rises in the <b>dark</b> instead: a night light. The same circuit with a <b>thermistor</b> gives a pd that follows temperature: a <b>thermostat</b> switches a heater off when the pd across the resistor rises past a value; a <b>fire alarm</b> switches a bell on.</p>",
        ),
        worked(
            "Explain the night light",
            "A night light uses a sensing circuit: a fixed resistor in series with an LDR, with the lamp's control connected across the LDR. Explain why the lamp comes on when it gets dark. (3 marks)",
            [
                "As it gets dark the <b>resistance of the LDR increases</b>.",
                "The LDR and the fixed resistor are in series and <b>share the supply pd in proportion to their resistances</b>, so the LDR's share — the <b>pd across the LDR — increases</b>.",
                "When the pd across the LDR rises above the switching value, the control <b>switches the lamp on</b>; in daylight the LDR's resistance and share of pd are low and the lamp stays off.",
            ],
        ),
        practice("Sensing circuits", [
            written("el-t5-q1", "Describe how to investigate how the resistance of a thermistor changes with temperature. (4)",
                    mark_scheme([
                        ("Circuit", "Thermistor in series with an <b>ammeter</b> and a supply; a <b>voltmeter across</b> the thermistor."),
                        ("Temperature", "Place the thermistor in a <b>water bath</b> with a thermometer; change the temperature by heating (or adding ice); stir and let it settle."),
                        ("Readings", "At each temperature read the <b>pd and current</b> (quickly, at the moment the temperature is read) and calculate $R = V/I$."),
                        ("Result", "Repeat over a range of temperatures and plot resistance against temperature: the resistance <b>decreases</b> as temperature rises."),
                    ]), lines=5),
            choice("el-t5-q2", "An LDR is in series with a fixed resistor across a 6 V supply. When it gets brighter, the pd across the fixed resistor…",
                   ["decreases", "increases", "stays at 3 V", "becomes zero"], 1,
                   "The LDR's resistance falls, so its share of the pd falls and the resistor's share rises."),
            written("el-t5-q3", "A thermistor is in series with a fixed resistor across a battery. Explain how the pd across the fixed resistor changes when the thermistor is warmed. (3)",
                    mark_scheme([
                        ("Thermistor", "Warming the thermistor <b>decreases its resistance</b>."),
                        ("Sharing", "In series the pd is shared <b>in proportion to the resistances</b>, so the thermistor takes a <b>smaller share</b>."),
                        ("Resistor", "So the pd across the fixed resistor <b>increases</b> (the current in the circuit also increases)."),
                    ]), lines=4),
            written("el-t5-q4", "Suggest how the circuit above could be used as a fire alarm. (2)",
                    marks(["When a fire raises the temperature, the thermistor's resistance falls and the <b>pd across the fixed resistor rises</b>.",
                           "When that pd rises past a set value it <b>switches on</b> the alarm (bell / buzzer) connected across the resistor."]), lines=2),
            choice("el-t5-q5", "To make a lamp come on in the dark, where should the lamp's control be connected in an LDR–resistor series circuit?",
                   ["Across the fixed resistor (its pd rises in the light)", "Across the LDR (its pd rises in the dark)", "Across the battery", "It makes no difference"], 1,
                   "The component whose share of pd rises in the dark is the LDR."),
            written("el-t5-q6", "A student measuring a thermistor's resistance holds it in the air above the hot water bath. Explain why the results are unreliable and how to improve the method. (2)",
                    marks(["The thermistor is <b>not at the temperature the thermometer reads</b> (the air is cooler / its temperature is uncertain).",
                           "Keep the thermistor <b>fully submerged</b> next to the thermometer bulb, stir, and read the meters at the moment the temperature is read."]), lines=3),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T6 · Energy and power the hard way
# ---------------------------------------------------------------------

section_t6 = section(
    "power-hard", "tricky", "Energy and power the hard way: ratings, fuses and time", "10.27, 10.29, 10.31, 10.42",
    equations=[r"I = \dfrac{P}{V}", r"E = P \times t", r"t = \dfrac{E}{P}"],
    blurb="The multi-step questions: a power rating on a label to the current and the right fuse; a battery's stored energy to how long it lasts; a comparison of two appliances. Every one is a chain of the four power equations with a unit conversion in the middle.",
    checklist=[
        "Find the current an appliance draws from its power rating and choose a fuse",
        "Find the energy transferred or the time taken from a power rating",
        "Compare appliances by power rating and energy transferred",
    ],
    parts=[
        explain(
            "Chains and traps",
            "<table class='tbl'><tr><th>Question</th><th>Chain</th></tr>"
            "<tr><td>which fuse for a 2.3 kW heater on 230 V?</td><td>$I = P/V = 2300/230 = 10$ A → the next standard rating above: <b>13 A</b> (standard fuses 3 A, 5 A, 13 A)</td></tr>"
            "<tr><td>how long will a 12 V, 50 A h car battery run a 60 W lamp?</td><td>stored energy $= Q \\times V$ with $Q = 50 \\times 3600 = 180\\,000$ C → $E = 2.16$ MJ → $t = E/P = 36\\,000$ s = 10 h</td></tr>"
            "<tr><td>energy in a day from a 100 W bulb left on</td><td>$E = P \\times t = 100 \\times 86\\,400 = 8.64$ MJ</td></tr>"
            "<tr><td>does the battery charge in 6 hours at 10 A, 400 V, 126 MJ?</td><td>$t = E/(IV) = 126 \\times 10^6 / 4000 = 31\\,500$ s = 8.75 h → no (or: energy in 6 h $= IVt = 86.4$ MJ &lt; 126 MJ)</td></tr></table>"
            "<p>Traps: <b>kW to W</b>, <b>MJ to J</b>, <b>hours and minutes to seconds</b> — the June 2023 report's main complaint on the charging question (Q8(b)(i)); and a comparison only scored when the <b>unit</b> of the calculated time was stated. Fuse choice: the <b>lowest standard rating above</b> the normal current — too low and it melts in normal use; too high and it does not protect.</p>"
            "<p><b>Power ratings and stored energy</b> (10.42): a 3 kW kettle changes the supply's energy store three times as fast as a 1 kW heater; over the same time it transfers three times the energy. $E = P \\times t$ is the whole of it.</p>",
        ),
        worked(
            "Rating → current → fuse",
            "A hair dryer is rated 1800 W, 230 V. (a) Calculate the current it draws. (b) Choose a fuse from 3 A, 5 A and 13 A and explain the choice. (c) Calculate the energy transferred in 4 minutes.",
            [
                r"<b>(a)</b> $I = \dfrac{P}{V} = \dfrac{1800}{230} = 7.8$ A.",
                "<b>(b)</b> <b>13 A</b>: the lowest standard rating <b>above</b> 7.8 A. A 5 A fuse would melt in normal use; 13 A melts only if a fault raises the current.",
                r"<b>(c)</b> $E = P \times t = 1800 \times 240 = 432\,000$ J (432 kJ).",
            ],
        ),
        practice("Energy and power the hard way", [
            group("el-t6-q1", "A toaster is rated 920 W at 230 V.", [
                numeric("el-t6-q1a", "Calculate the current in the toaster.", 4, "A", "I = P ÷ V.", [r"$I = 920 \div 230 = 4$ A."]),
                choice("el-t6-q1b", "Which fuse should its plug have?",
                       ["3 A", "5 A", "13 A", "4 A"], 1,
                       "Lowest standard rating above 4 A is 5 A."),
            ]),
            numeric("el-t6-q2", "A 2.5 kW heater is used for 1.5 hours. Calculate the energy transferred, in MJ.", 13.5, "MJ", "W and seconds, then convert.", [r"$E = 2500 \times 5400 = 13\,500\,000$ J $= 13.5$ MJ."]),
            numeric("el-t6-q3", "A battery stores 54 000 J. How long can it run a 15 W lamp? Give your answer in minutes.", 60, "min", "t = E ÷ P in seconds, then ÷ 60.", [r"$t = 54\,000 \div 15 = 3600$ s $= 60$ minutes."]),
            numeric("el-t6-q4", "A charger supplies 2 A at 5 V to a phone for 3 hours. Calculate the energy transferred.", 108000, "J", "E = I V t with t in seconds.", [r"$E = 2 \times 5 \times 10\,800 = 108\,000$ J (108 kJ)."]),
            written("el-t6-q5", "Explain why a 13 A fuse should not be used in the plug of a lamp that draws 0.3 A. (2)",
                    marks(["The fuse only melts when the current <b>exceeds 13 A</b>…", "…so a fault that raised the lamp's current to, say, 5 A would <b>not melt it</b>: the lamp could overheat or catch fire without the supply being cut. A 3 A fuse is needed."]), lines=2),
            numeric("el-t6-q6", "An electric car motor draws 150 A at 400 V. Calculate the energy transferred in 10 minutes, in MJ.", 36, "MJ", "P = IV, then E = Pt.", [r"$P = 150 \times 400 = 60\,000$ W; $E = 60\,000 \times 600 = 36\,000\,000$ J $= 36$ MJ."]),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T7 · Mains safety explained
# ---------------------------------------------------------------------

section_t7 = section(
    "mains-safety", "tricky", "Mains safety explained: the chains the marks are on", "10.37, 10.38, 10.39, 10.41",
    equations=[r"\text{fault} \rightarrow \text{large current to earth} \rightarrow \text{fuse melts} \rightarrow \text{circuit broken}"],
    blurb="Every safety question is a chain of three or four links, and each link is a mark. The words that score are fixed: low-resistance path, large current, the fuse wire melts, the circuit is broken, the case cannot become live. 'Blows' is never written.",
    checklist=[
        "Write the fuse chain: current exceeds rating → wire melts → circuit broken → appliance disconnected",
        "Write the earth-wire chain: fault → case live → low-resistance path → large current → fuse melts → safe",
        "Explain double insulation, the live-wire switch and the live–earth danger in the same style",
    ],
    parts=[
        explain(
            "The chains",
            "<table class='tbl'><tr><th>Question</th><th>The chain (one mark a link)</th></tr>"
            "<tr><td>what the fuse does when the current is too large</td><td>current <b>exceeds the fuse rating</b> → the fuse wire <b>heats up and melts</b> → the circuit is <b>broken</b> → the appliance is <b>disconnected from the live supply</b></td></tr>"
            "<tr><td>how the earth wire protects the user</td><td>the earth wire connects the <b>metal case</b> to earth → if the live touches the case, the earth wire gives a <b>low-resistance path</b> → a <b>large current</b> flows to earth → the <b>fuse melts</b> and breaks the circuit → the case <b>cannot stay live</b>, so no shock</td></tr>"
            "<tr><td>why the fuse/switch is in the live wire</td><td>the live wire is at <b>230 V</b> → breaking it <b>isolates</b> the whole appliance from the supply → nothing inside is live when off; in the neutral the appliance would <b>stay at 230 V</b></td></tr>"
            "<tr><td>why no earth wire on a plastic-cased appliance</td><td><b>double insulated</b>: the case is an <b>insulator</b> and cannot become live, so there is nothing to earth</td></tr>"
            "<tr><td>why a live–earth connection is dangerous</td><td><b>230 V between live and earth</b> → a person (or water) touching the live provides a <b>path to earth</b> → a <b>large current flows through them</b> → electric shock (or heating → fire)</td></tr>"
            "<tr><td>fuse versus circuit breaker</td><td>both break the circuit when the current is too large; the breaker <b>trips faster</b> and can be <b>reset</b>, a fuse must be <b>replaced</b></td></tr></table>"
            "<p>Choose the fuse rating <b>just above</b> the normal current (T6). The June 2025 scheme (Q3(c)(ii)): \"the fuse wire melts\" + \"breaks the circuit\" — the answers that lost a mark did not say what the fuse <i>does</i>. The same paper credited \"circuit breaker\", \"earth wire\", \"cable clamp\" and \"insulation\" as other safety devices (Q3(c)(iii)).</p>",
        ),
        worked(
            "The 6-mark safety explanation",
            "A metal-cased kettle is connected to the mains with a three-core cable and a fused plug. Explain how the design keeps the user safe if the live wire inside the kettle comes loose and touches the case. (6 marks)",
            [
                "The <b>live wire</b> is at <b>230 V</b>; if it touches the metal case, the case would become live and a user touching it would get a shock.",
                "The case is connected to the <b>earth wire</b>, which is at 0 V and provides a <b>low-resistance path</b> from the case to earth.",
                "So a <b>large current</b> flows from the live wire, through the case and the earth wire, to earth.",
                "The large current exceeds the rating of the <b>fuse</b> in the live wire, so the fuse wire <b>heats up and melts</b>…",
                "…which <b>breaks the circuit</b> and disconnects the kettle from the live supply; the case cannot remain at 230 V.",
                "The fuse is in the <b>live wire</b> so that, once it has melted, no part of the kettle is still connected to 230 V; the <b>insulation</b> on each wire and the <b>cable clamp</b> make the fault unlikely in the first place.",
            ],
        ),
        practice("Mains safety", [
            written("el-t7-q1", "Explain how the earth wire and the fuse together protect a user if the live wire touches the metal case of an appliance. (4)",
                    mark_scheme([
                        ("Earth path", "The earth wire connects the case to earth, giving a <b>low-resistance path</b>."),
                        ("Current", "So a <b>large current</b> flows from the live wire through the case to earth."),
                        ("Fuse", "The large current makes the <b>fuse wire melt</b>…"),
                        ("Result", "…which <b>breaks the circuit</b>, disconnecting the appliance from the live supply so the case cannot stay live."),
                    ]), lines=5),
            choice("el-t7-q2", "A student writes: \"If there is a fault the fuse blows and protects the appliance.\" What should they have written?",
                   ["\"the fuse explodes\"", "\"the fuse wire melts, breaking the circuit\"", "\"the fuse switches off\"", "\"the fuse absorbs the current\""], 1,
                   "Melts — that is what happens; it does not explode."),
            written("el-t7-q3", "A hair dryer has a plastic case and a two-core cable with no earth wire. Explain why it is still safe. (2)",
                    marks(["It is <b>double insulated</b>: the case is made of an <b>insulator</b>…", "…so it <b>cannot become live</b> even if a wire inside comes loose, and there is nothing for an earth wire to protect."]), lines=2),
            written("el-t7-q4", "Explain why a fuse is placed in the live wire and not the neutral wire. (2)",
                    marks(["When the fuse melts in the live wire, the appliance is <b>disconnected from the 230 V</b> supply.",
                           "In the neutral wire the current would stop but the appliance would <b>remain connected to the live</b> — still dangerous to touch."]), lines=2),
            written("el-t7-q5", "Explain why using an electrical appliance with wet hands is dangerous. (2)",
                    marks(["Water (with dissolved substances) <b>conducts</b>, and there is a pd of 230 V between the live wire and earth.",
                           "A wet hand gives a <b>low-resistance path</b> from live to earth through the body, so a <b>large current</b> flows through the person — a shock."]), lines=2),
            choice("el-t7-q6", "Which is an advantage of a circuit breaker over a fuse?",
                   ["It melts more quickly", "It can be reset rather than replaced, and acts faster", "It does not need to be in the live wire", "It allows a larger current"], 1,
                   "Trips and resets."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T8 · Explaining with electrons
# ---------------------------------------------------------------------

section_t8 = section(
    "electron-model", "tricky", "Explaining with electrons: current, pd, resistance and heat", "10.5, 10.8, 10.23, 10.24",
    equations=[r"\text{current: electrons drift},\ \text{pd: energy per coulomb},\ \text{resistance: collisions}"],
    blurb="The 'explain' questions want the model behind the equations: what the electrons are doing, what the pd is paying for, why collisions mean resistance and heat. And a misconception to kill: the voltage is not 'used up' and the current is not 'used up' either.",
    checklist=[
        "Describe current, pd and resistance in terms of electrons, energy and collisions",
        "Explain why current is the same all round a series circuit",
        "Explain why the pd across components in series adds up to the supply pd",
    ],
    parts=[
        explain(
            "The model in four sentences",
            "<ul><li><b>Current:</b> free electrons drift through the metal when a pd is applied; the current is the <b>charge passing per second</b>. Electrons are not used up — the same number leave a lamp as enter it, which is why the <b>current is the same all round a series circuit</b> and why it is conserved at junctions.</li>"
            "<li><b>Potential difference:</b> the <b>energy transferred per coulomb</b>. The cell gives each coulomb a fixed amount of energy (its pd); each component takes some of it as the charge passes (the pd across it). The energy per coulomb given equals the energy per coulomb taken — so <b>the pds across series components add up to the cell's pd</b>. It is <b>energy</b> that is transferred, not voltage \"used up\" and not current \"used up\".</li>"
            "<li><b>Resistance:</b> electrons <b>collide with the ions</b> of the lattice; the more often, the harder it is to drive current for a given pd. Longer wire → more collisions → more resistance; thicker wire → more paths → less; hotter → ions vibrate more → more collisions → more.</li>"
            "<li><b>Heating:</b> each collision transfers energy from the electrons to the ions, which <b>vibrate more</b>: the resistor's temperature rises and the energy is <b>dissipated</b> to the surroundings as thermal energy. The June 2023 report (Q2(b)(iv)) praised \"fewer electrons per second collide with the ions\" as the reason a smaller current heats a wire less.</li></ul>",
        ),
        worked(
            "Series pd in terms of energy",
            "A 6 V battery is connected to two lamps in series. The pd across one lamp is 2 V. Explain, in terms of energy, why the pd across the other is 4 V. (3 marks)",
            [
                "The battery transfers <b>6 J to every coulomb</b> of charge that passes through it (pd = energy per coulomb).",
                "Each coulomb transfers <b>2 J</b> in the first lamp (its pd is 2 V)…",
                "…and the energy a coulomb carries round the circuit must all be transferred by the time it returns, so the other lamp transfers the remaining <b>4 J per coulomb</b>: 4 V. (Energy is conserved; the pds add up.)",
            ],
        ),
        practice("The electron model", [
            written("el-t8-q1", "A student says: \"The current is used up by the first lamp, so the second lamp in series is dimmer.\" Explain what is wrong with this. (2)",
                    marks(["Current is a flow of <b>electrons</b>, which are <b>not used up</b>: the same number per second leave the lamp as enter it, so the current is the <b>same</b> in both lamps.",
                           "What the lamps take from the charge is <b>energy</b> (pd); two identical lamps in series are equally bright (and both dimmer than one alone, because each has half the pd)."]), lines=3),
            written("el-t8-q2", "Explain, in terms of electrons, why a longer wire has a larger resistance. (2)",
                    marks(["Electrons moving through the wire <b>collide with the ions</b> of the lattice.", "In a longer wire there are <b>more collisions</b> on the way through, so it is harder to drive a current for the same pd — larger resistance."]), lines=2),
            choice("el-t8-q3", "The pd across a resistor is 3 V. This means…",
                   ["3 A flows through it", "each coulomb passing through it transfers 3 J", "it has a resistance of 3 Ω", "3 J is transferred every second"], 1,
                   "Volt = joule per coulomb."),
            written("el-t8-q4", "Explain why a smaller current makes a wire warm less. (2)",
                    marks(["A smaller current means <b>fewer electrons per second</b> pass through the wire…", "…so there are <b>fewer collisions</b> with the ions per second, less energy is transferred to the ions' vibration, and the wire's temperature rises less."]), lines=2),
            choice("el-t8-q5", "Why is the current the same at every point in a series circuit?",
                   ["Because the voltage is the same everywhere", "Because charge is conserved: electrons are not used up or stored, so the charge passing per second is the same at every point", "Because resistors have no effect", "Because the cell pushes equally"], 1,
                   "Conservation of charge."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T9 · The seven steps for this topic
# ---------------------------------------------------------------------

section_t9 = section(
    "planning-electricity", "tricky", "Planning a practical: the seven steps for electricity", "10.17, 10.21",
    equations=[r"\text{variables} \rightarrow \text{equation} \rightarrow \text{change} \rightarrow \text{measure} \rightarrow \text{use} \rightarrow \text{accuracy} \rightarrow \text{repeat}"],
    blurb="The seven-step recipe from Topic 1 (T6 there), applied to the two investigations this topic can ask for: how current depends on pd, and how a thermistor's resistance depends on temperature. Any six of the seven points for the six marks.",
    checklist=[
        "Write a plan for the I–V investigation using the seven steps",
        "Write a plan for the thermistor–temperature investigation using the seven steps",
        "Name the control variables for each",
    ],
    parts=[
        explain(
            "The recipe applied twice",
            "<table class='tbl'><tr><th>Step</th><th>Current against pd (resistor / lamp)</th><th>Thermistor resistance against temperature</th></tr>"
            "<tr><td><b>1 Variables</b></td><td>independent: pd across the component; dependent: current; control: the component, its temperature (switch off between readings)</td><td>independent: temperature; dependent: resistance; control: the thermistor, the supply pd</td></tr>"
            "<tr><td><b>2 Equation</b></td><td>$R = V \\div I$</td><td>$R = V \\div I$</td></tr>"
            "<tr><td><b>3 Change</b></td><td>adjust the variable resistor to set the pd in 0.5 V steps; reverse the supply for negative values</td><td>heat the water bath in 10 °C steps (or add ice), stirring and letting it settle</td></tr>"
            "<tr><td><b>4 Measure</b></td><td>pd with the voltmeter across the component, current with the ammeter in series</td><td>temperature with a thermometer beside the thermistor; pd across it and current in it at that moment</td></tr>"
            "<tr><td><b>5 Use the result</b></td><td>plot I against V; find R = V/I at points; straight line = constant R, curve = changing R</td><td>calculate R = V/I at each temperature; plot R against temperature</td></tr>"
            "<tr><td><b>6 Accuracy detail</b></td><td>switch off between readings so the component does not warm up; read the meters at the same instant</td><td>keep the thermistor fully submerged and stirred so it is at the measured temperature</td></tr>"
            "<tr><td><b>7 Repeat</b></td><td>repeat each pd and average the current</td><td>repeat each temperature and average the resistance</td></tr></table>",
        ),
        worked(
            "The thermistor plan",
            "Plan an investigation to find how the resistance of a thermistor changes with temperature. (6 marks)",
            [
                "<b>Variables:</b> change the temperature (independent), measure the resistance (dependent); use the same thermistor and supply throughout.",
                "<b>Circuit:</b> thermistor in series with an ammeter and a low-voltage supply, voltmeter across the thermistor; resistance from $R = V/I$.",
                "<b>Change:</b> put the thermistor in a beaker of water with a thermometer; heat it in steps of about 10 °C from 20 °C to 80 °C, stirring and letting the temperature settle each time.",
                "<b>Measure:</b> at each temperature read the thermometer, the voltmeter and the ammeter at the same moment.",
                "<b>Use:</b> calculate $R = V/I$ at each temperature and plot resistance against temperature.",
                "<b>Accuracy and repeats:</b> keep the thermistor fully under the water next to the thermometer bulb; repeat at each temperature and take a mean.",
            ],
        ),
        practice("Planning", [
            written("el-t9-q1", "Plan an investigation into how the current in a filament lamp depends on the potential difference across it. (6)",
                    mark_scheme([
                        ("Variables", "Independent: pd; dependent: current; control: the same lamp (and switch off between readings)."),
                        ("Equation", "$R = V/I$ to find the resistance at each point."),
                        ("Change", "Use a <b>variable resistor</b> in series to set the pd in equal steps; reverse the supply for negative values."),
                        ("Measure", "Voltmeter <b>across</b> the lamp, ammeter <b>in series</b>; read both at each setting."),
                        ("Use", "Plot I against V; the shape shows how the resistance changes."),
                        ("Accuracy / repeat", "Read both meters at the same instant; repeat and average."),
                    ], total=6, extra=["Any six of the seven points."]), lines=7),
            choice("el-t9-q2", "In the thermistor investigation, which is a control variable?",
                   ["The temperature", "The resistance", "The supply pd", "The current"], 2,
                   "Keep the supply (and the thermistor) the same; temperature is changed, resistance measured, current is part of the measurement."),
            written("el-t9-q3", "Give one accuracy detail for the thermistor investigation and explain why it matters. (2)",
                    marks(["Keep the thermistor <b>fully submerged</b> next to the thermometer bulb and <b>stir</b> the water.", "So that the thermistor is at the <b>temperature being recorded</b> — otherwise the resistance is matched to the wrong temperature."]), lines=2),
        ]),
    ],
)

SECTIONS = [section_t1, section_t2, section_t3, section_t4, section_t5, section_t6, section_t7, section_t8, section_t9]

# ---------------------------------------------------------------------
# Flashcards (the key-word definitions are added by el_nn_b.FACTS_KW)
# ---------------------------------------------------------------------

FACTS = [
    # N1
    fact("Position, mass and charge of a proton, neutron and electron?", "Proton: nucleus, 1, +1. Neutron: nucleus, 1, 0. Electron: shells, very small, −1.", "charge-current"),
    fact("What is electric current?", "The rate of flow of charge; in metals a flow of free electrons. 1 A = 1 C/s.", "charge-current"),
    fact("Which way do electrons move, and which way is conventional current?", "Electrons: − to +. Conventional current: + to −.", "charge-current"),
    fact("Why do metals conduct?", "They have free (delocalised) electrons that drift through the lattice when a pd is applied.", "charge-current"),
    # N2
    fact("Where does an ammeter go, and what does it measure?", "In series with the component; current, in amps.", "circuit-symbols"),
    fact("Where does a voltmeter go, and what does it measure?", "In parallel with (across) the component; potential difference, in volts.", "circuit-symbols"),
    fact("Which line of the cell symbol is positive?", "The long thin line.", "circuit-symbols"),
    fact("Why must a voltmeter never be in series?", "Its resistance is very high, so it would almost stop the current.", "circuit-symbols"),
    fact("How are a thermistor and an LDR drawn?", "Both a resistor rectangle: the thermistor with a bent line through it, the LDR with two arrows pointing in.", "circuit-symbols"),
    # N3
    fact("Equation linking charge, current and time?", "Q = I × t (C = A × s). Convert mA to A and minutes to seconds first.", "charge-nn"),
    fact("What is needed for a current to flow?", "A closed (complete) circuit and a source of potential difference.", "charge-nn"),
    fact("What happens to current at a junction?", "It is conserved: total current in = total current out.", "charge-nn"),
    # N4
    fact("What is potential difference?", "The energy transferred per unit charge (per coulomb) passing through a component. 1 V = 1 J/C.", "pd-energy"),
    fact("Equation linking energy, charge and pd?", "E = Q × V (J = C × V).", "pd-energy"),
    fact("What does the pd across a component tell you?", "How many joules each coulomb transfers in that component.", "pd-energy"),
    # N5
    fact("Equation linking pd, current and resistance?", "V = I × R; R = V ÷ I in ohms (Ω).", "ohm-nn"),
    fact("What happens to the current if the resistance in a circuit increases (same pd)?", "It decreases (I = V/R).", "ohm-nn"),
    fact("How does a variable resistor change the current?", "Moving the slider changes the length of resistance wire in the circuit, changing the resistance and so the current.", "ohm-nn"),
    fact("kΩ and mA — what do you do before substituting?", "kΩ × 1000 → Ω; mA ÷ 1000 → A.", "ohm-nn"),
    # N6
    fact("Series circuit: current, pd, resistance?", "Same current everywhere; pd shared (adds up to the supply, bigger R takes more); resistances add.", "circuits-nn"),
    fact("Parallel circuit: current, pd, resistance?", "Current splits at junctions (branch currents add up); same pd across every branch; total resistance less than the smallest branch.", "circuits-nn"),
    fact("Why does adding a resistor in series increase the total resistance?", "The current must pass through both, one after the other — more to push through, so less current for the same pd.", "circuits-nn"),
    fact("Why does adding a resistor in parallel decrease the total resistance?", "It gives the current another path; the pd is unchanged but the total current increases, so R = V/I is smaller.", "circuits-nn"),
    fact("Why are house lights wired in parallel?", "Each gets the full mains pd and can be switched independently; one failing leaves the rest on.", "circuits-nn"),
    # N7
    fact("I–V graph of a fixed resistor?", "A straight line through the origin: current proportional to pd, constant resistance.", "iv-characteristics"),
    fact("I–V graph of a filament lamp?", "A curve that flattens as pd increases (both directions): the resistance increases as the filament gets hotter.", "iv-characteristics"),
    fact("I–V graph of a diode?", "Zero current for reverse pd; for forward pd, nothing until about 0.7 V then a steep rise. Current in one direction only.", "iv-characteristics"),
    fact("How do you find the resistance at a point on an I–V graph?", "R = V ÷ I using the point's coordinates — not the gradient.", "iv-characteristics"),
    # N8
    fact("How does an LDR's resistance depend on light?", "It decreases as the light intensity increases (high in the dark).", "ldr-thermistor"),
    fact("How does a thermistor's resistance depend on temperature?", "It decreases as the temperature increases (NTC).", "ldr-thermistor"),
    fact("Uses of an LDR and a thermistor?", "LDR: automatic lights at dusk, screen brightness. Thermistor: thermostats, fire alarms, engine temperature sensors.", "ldr-thermistor"),
    fact("Thermistor vs variable resistor?", "Thermistor changes resistance by itself with temperature; a variable resistor is changed by hand.", "ldr-thermistor"),
    # N9
    fact("Why does a current heat a resistor?", "Electrons collide with the lattice ions, making them vibrate more — a higher temperature; the energy is dissipated to the surroundings.", "heating-effect"),
    fact("How do you reduce unwanted heating in wires?", "Use low-resistance wires: thick (large cross-section), short, good conductor (copper). Insulation does not reduce it.", "heating-effect"),
    fact("Devices that use the heating effect?", "Heaters, kettles, toasters, filament lamps, fuses.", "heating-effect"),
    # N10
    fact("What is power, and its unit?", "Energy transferred per second; watts (1 W = 1 J/s). P = E ÷ t.", "power-nn"),
    fact("The electrical power equations?", "P = I × V and P = I² × R.", "power-nn"),
    fact("Energy transferred by a device?", "E = I × V × t, or E = P × t (t in seconds).", "power-nn"),
    fact("Why is P = I × V?", "Each coulomb transfers V joules and I coulombs pass each second, so I × V joules per second.", "power-nn"),
    fact("What does a power rating tell you?", "How fast the device transfers energy from the supply: energy = power × time.", "power-nn"),
    # N11
    fact("d.c. vs a.c.?", "d.c.: charge moves in one direction only (cells, batteries). a.c.: the movement of charge changes direction repeatedly (the mains).", "mains"),
    fact("UK mains frequency and pd?", "50 Hz, about 230 V, a.c.", "mains"),
    fact("Live, neutral, earth: colours and pds?", "Live brown 230 V; neutral blue 0 V; earth green-and-yellow 0 V.", "mains"),
    fact("What does the live wire do? The neutral?", "Live carries the current to the appliance at 230 V; neutral completes the circuit back to the supply at 0 V.", "mains"),
    fact("What does a fuse do?", "Its thin wire melts when the current exceeds its rating, breaking the circuit. (It melts — it does not blow.)", "mains"),
    fact("What does a circuit breaker do?", "An automatic switch that trips when the current is too large; faster than a fuse and can be reset.", "mains"),
    fact("What does the earth wire do?", "Connects the metal case to earth; if the live touches the case, a large current flows through the low-resistance earth path and melts the fuse, so the case cannot stay live.", "mains"),
    fact("Why are switches and fuses in the live wire?", "Breaking the live wire disconnects the appliance from 230 V; in the neutral the appliance would stay live.", "mains"),
    fact("Why is a connection between live and earth dangerous?", "There is 230 V between them, so a large current flows through whatever makes the connection — a person gets a shock, a fault can start a fire.", "mains"),
    fact("What is double insulation?", "A plastic (insulating) case that cannot become live, so no earth wire is needed.", "mains"),
    # T1
    fact("The I–V practical circuit?", "Supply, variable resistor and ammeter in series with the component; voltmeter across the component.", "iv-practical"),
    fact("How do you get negative values in the I–V practical?", "Reverse the connections to the supply and repeat.", "iv-practical"),
    fact("Why switch off between readings in the I–V practical?", "So the component does not warm up and change its resistance.", "iv-practical"),
    fact("What is the variable resistor for in the I–V practical?", "To change the pd across (and current in) the component for a range of readings.", "iv-practical"),
    # T2
    fact("Series test: where do the meters go and what do they show?", "Ammeter anywhere in the loop (same current everywhere); voltmeter across each resistor — the pds add up to the cell's.", "series-parallel-practical"),
    fact("Parallel test: where do the meters go and what do they show?", "Ammeter in each branch (currents add up to the cell current); voltmeter across a branch reads the cell pd.", "series-parallel-practical"),
    fact("Two lamps in series, one removed?", "The other goes out: one path, the circuit is broken.", "series-parallel-practical"),
    fact("Why is a lamp brighter in parallel than in series with another?", "It has the full pd across it (not a share), so a larger current and a larger power P = IV.", "series-parallel-practical"),
    # T3
    fact("Why does a lamp's resistance rise with pd?", "More current → hotter filament → ions vibrate more → electrons collide with them more often → higher resistance.", "iv-explain"),
    fact("Why is a resistor's I–V graph straight?", "At constant temperature the collisions do not change, so current is proportional to pd and R is constant.", "iv-explain"),
    fact("Is the gradient of an I–V graph the resistance?", "No. With I on the y-axis the gradient of a straight line is 1/R; for a curve use R = V/I at the point.", "iv-explain"),
    # T4
    fact("Series method?", "Add the resistances → I = V/R → each pd = I × R → check they add up to the supply.", "circuits-hard"),
    fact("Parallel method?", "Supply pd across each branch → I = V/R per branch → add for the supply current → total R = V/I (less than the smallest branch).", "circuits-hard"),
    fact("Two resistors in series share the pd how?", "In proportion to their resistances: 10 Ω and 30 Ω across 8 V take 2 V and 6 V.", "circuits-hard"),
    # T5
    fact("LDR in series with a fixed resistor: what happens to the pds as it gets dark?", "The LDR's resistance rises, so it takes a bigger share of the pd; the pd across the fixed resistor falls.", "sensing-circuits"),
    fact("How does a thermistor thermostat work?", "Warmer → thermistor resistance falls → its share of pd falls, the fixed resistor's rises → past a set value the heater is switched off.", "sensing-circuits"),
    fact("How do you investigate a thermistor's resistance against temperature?", "Thermistor in a stirred water bath with a thermometer; ammeter in series, voltmeter across; R = V/I at each temperature.", "sensing-circuits"),
    # T6
    fact("How do you choose a fuse for an appliance?", "I = P/V, then the lowest standard rating (3 A, 5 A, 13 A) above that current.", "power-hard"),
    fact("Energy from a power rating?", "E = P × t with P in watts and t in seconds (kW × 1000; hours × 3600).", "power-hard"),
    fact("The commonest error in E = IVt questions?", "Not converting kW/MJ and minutes/hours to W, J and seconds; and not stating the unit of a calculated time.", "power-hard"),
    # T7
    fact("The fuse chain?", "Current exceeds the rating → fuse wire heats and melts → circuit broken → appliance disconnected from the live supply.", "mains-safety"),
    fact("The earth-wire chain?", "Live touches the case → earth wire is a low-resistance path → large current to earth → fuse melts → circuit broken → case cannot stay live.", "mains-safety"),
    fact("Fuse vs circuit breaker?", "Both break the circuit when the current is too large; a breaker trips faster and can be reset, a fuse melts and must be replaced.", "mains-safety"),
    fact("Why is a 13 A fuse wrong for a 0.3 A lamp?", "A fault current of a few amps would not melt it, so the lamp could overheat without the supply being cut.", "mains-safety"),
    # T8
    fact("Is current 'used up' by a lamp?", "No. Electrons are not used up; the current is the same before and after. What is transferred is energy (pd).", "electron-model"),
    fact("Why do pds in series add up to the cell's pd?", "The cell gives each coulomb a fixed energy; the components take it in shares; energy is conserved, so the shares add to the total.", "electron-model"),
    fact("Why does a longer wire have more resistance?", "More collisions between the electrons and the ions on the way through.", "electron-model"),
    fact("Why does a smaller current heat a wire less?", "Fewer electrons per second → fewer collisions with the ions per second → less energy to the ions' vibration.", "electron-model"),
    # T9
    fact("Variables in the I–V investigation?", "Independent: pd; dependent: current; control: the component and its temperature.", "planning-electricity"),
    fact("Variables in the thermistor investigation?", "Independent: temperature; dependent: resistance (from V/I); control: the thermistor and the supply pd.", "planning-electricity"),
    fact("The accuracy detail for the thermistor investigation?", "Thermistor fully submerged beside the thermometer, water stirred, meters read at the moment the temperature is read.", "planning-electricity"),
]
