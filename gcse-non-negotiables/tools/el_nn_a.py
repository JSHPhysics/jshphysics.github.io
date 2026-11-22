"""
el_nn_a.py — Topic 10 (Electricity and circuits): the non-negotiables N1–N6.

N1 Charge and current           N4 Potential difference and energy (E = QV)
N2 Circuit diagrams and meters  N5 Resistance and V = IR
N3 Charge, current, time (Q=It) N6 Series and parallel
"""

from revlib import (
    axis, choice, curve, diagram, ewau, explain, fact, graph, group, line,
    mark_scheme, marks, numeric, practice, section, worked, written,
)
import el_diagrams as dg

# ---------------------------------------------------------------------
# N1 · Charge and current
# ---------------------------------------------------------------------

section_n1 = section(
    "charge-current", "nn", "Charge and current: what is actually moving", "10.1, 10.8",
    equations=[r"I = \dfrac{Q}{t}", r"\text{1 A} = \text{1 C/s}"],
    blurb="Everything in this topic is electrons moving through metal. Current is how much charge passes a point each second; the charge is carried by electrons, which are part of every atom.",
    checklist=[
        "State the position, relative mass and charge of protons, neutrons and electrons",
        "Define current as the rate of flow of charge, and state that in metals it is a flow of electrons",
        "State the direction of conventional current and of electron flow",
    ],
    parts=[
        explain(
            "The atom, and what moves",
            "<table class='tbl'><tr><th>Particle</th><th>Where</th><th>Relative mass</th><th>Relative charge</th></tr>"
            "<tr><td><b>Proton</b></td><td>nucleus</td><td>1</td><td>+1</td></tr>"
            "<tr><td><b>Neutron</b></td><td>nucleus</td><td>1</td><td>0</td></tr>"
            "<tr><td><b>Electron</b></td><td>shells around the nucleus</td><td>very small (about 1/2000)</td><td>−1</td></tr></table>"
            "<p>An atom has equal numbers of protons and electrons, so it is neutral. In a <b>metal</b>, the outer electrons are not tied to one atom: they are <b>free electrons</b> that can drift through the lattice of positive ions. That drift is an electric current.</p>"
            "<p><b>Electric current is the rate of flow of charge</b>: how many coulombs pass a point each second. $I = Q \\div t$; one ampere is one coulomb per second. In metals the moving charges are <b>electrons</b>; in a solution they can be ions. Electrons carry negative charge, so they move from the <b>negative</b> terminal to the positive; <b>conventional current</b> is drawn the other way, from + to −, and every diagram and rule in this topic uses conventional current.</p>"
            "<p>The electrons do not travel fast — about a millimetre a second — but they all start moving at once when the switch closes, so the lamp lights at once.</p>",
        ),
        worked(
            "Define and explain",
            "(a) State what is meant by an electric current. (b) Explain what carries the current in a copper wire. (3 marks)",
            [
                "<b>(a)</b> The <b>rate of flow of charge</b> — the charge passing a point per second.",
                "<b>(b)</b> Copper is a metal, so it has <b>free electrons</b> not bound to particular atoms…",
                "…which <b>drift through the metal</b> when a potential difference is applied; the moving (negative) electrons are the current.",
            ],
        ),
        practice("Charge and current", [
            choice("el-n1-q1", "Which row is correct for an electron?",
                   ["In the nucleus, mass 1, charge +1", "In the nucleus, mass 1, charge 0", "Around the nucleus, very small mass, charge −1", "Around the nucleus, mass 1, charge −1"], 2,
                   "Electrons are in the shells, tiny in mass, charge −1."),
            written("el-n1-q2", "State what is meant by electric current. (1)",
                    marks(["The <b>rate of flow of charge</b> (charge flowing per second)."]), lines=1),
            written("el-n1-q3", "Explain why metals conduct electricity. (2)",
                    marks(["Metals contain <b>free (delocalised) electrons</b> that are not bound to individual atoms.",
                           "When a potential difference is applied these electrons <b>drift through the metal</b> — a flow of charge, which is a current."]), lines=2),
            choice("el-n1-q4", "In which direction do electrons move in a circuit, and in which direction is conventional current drawn?",
                   ["Both from + to −", "Electrons from − to +; conventional current from + to −", "Both from − to +", "Electrons from + to −; conventional current from − to +"], 1,
                   "Electrons are negative, so they leave the negative terminal; convention runs the other way."),
            written("el-n1-q5", "Explain why an atom is electrically neutral. (1)",
                    marks(["It has <b>equal numbers of protons and electrons</b>, whose charges (+1 and −1) cancel."]), lines=1),
            choice("el-n1-q6", "A current of 1 A means…",
                   ["1 coulomb passes a point every second", "1 joule is transferred every second", "1 electron passes every second", "the pd is 1 volt"], 0,
                   "Ampere = coulomb per second."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N2 · Circuit diagrams and meters
# ---------------------------------------------------------------------

section_n2 = section(
    "circuit-symbols", "nn", "Circuit diagrams, symbols and meters", "10.2, 10.4, 10.7",
    equations=[r"\text{ammeter in series}", r"\text{voltmeter in parallel}"],
    blurb="Thirteen symbols to draw from memory, straight wires with square corners, and the two rules that come up every year: the ammeter goes in series with the component, the voltmeter across it.",
    checklist=[
        "Draw the symbols for cell, battery, switch, lamp, resistor, variable resistor, ammeter, voltmeter, motor, diode, LED, thermistor and LDR",
        "Draw a complete circuit with an ammeter in series and a voltmeter in parallel with a component",
        "State what each meter measures and its unit",
    ],
    parts=[
        explain(
            "The symbols",
            diagram(dg.symbols_svg(), 700, 360, "The circuit symbols named in the specification (10.2). The long thin line of a cell is its positive terminal.") +
            "<p>Draw circuits with a <b>ruler</b>: straight wires, right-angled corners, no gaps, symbols on the wire (not floating beside it). A <b>cell</b> is one; a <b>battery</b> is two or more cells joined. The <b>long thin line</b> is the positive terminal. Conventional current leaves it and goes round to the short thick line.</p>",
        ),
        explain(
            "The two meters",
            diagram(dg.meters_svg(), 760, 270, "An ammeter in series with the lamp; a voltmeter in parallel with (across) it.") +
            "<p>An <b>ammeter</b> measures <b>current</b> in <b>amps (A)</b>. It goes <b>in series</b> with the component, so the same current that goes through the component goes through the meter. A <b>voltmeter</b> measures the <b>potential difference</b> in <b>volts (V)</b> <b>across</b> a component, so it goes <b>in parallel</b> with it — one lead each side.</p>"
            "<p>The June 2023 report (Q2(a)): the voltmeter was \"often across the variable resistor or the battery\" instead of the component asked for, and \"a voltmeter is never connected in series\". The June 2024 scheme (Q8(a), 3 marks): variable resistor in series, ammeter in series with the lamp, voltmeter in parallel with the lamp — one mark each. The June 2025 report (Q10(c)): \"a misplaced voltmeter\" kept answers at Level 1.</p>",
        ),
        worked(
            "Drawing the circuit",
            "Draw a circuit diagram to measure the current in a resistor and the potential difference across it, using a cell, a switch, an ammeter and a voltmeter. (3 marks)",
            [
                "One loop: <b>cell → switch → ammeter → resistor → back to the cell</b>, all in series.",
                "The <b>voltmeter</b> drawn as a separate branch with one lead on <b>each side of the resistor</b> — <b>across the resistor only</b>, not across the ammeter. (When the resistor is the only component, across the battery reads the same and the Nov 2021 scheme (Q8(a)(i)) accepted it; once there is a variable resistor in the loop it does not — the 2023 complaint.)",
                "Correct symbols: circle-A and circle-V, rectangle for the resistor, long-and-short lines for the cell, a gap with a hinged line for the switch.",
            ],
        ),
        practice("Symbols and meters", [
            choice("el-n2-q1", "How is a voltmeter connected to measure the pd across a lamp?",
                   ["In series with the lamp", "In parallel with the lamp", "In series with the cell", "Anywhere in the circuit"], 1,
                   "Across the component: one lead each side."),
            choice("el-n2-q2", "How is an ammeter connected to measure the current in a lamp?",
                   ["In parallel with the lamp", "In series with the lamp", "Across the cell", "It does not matter"], 1,
                   "In the same loop as the lamp, so the lamp's current passes through it."),
            written("el-n2-q3", "Describe how to draw the symbol for (a) a diode and (b) a thermistor. (2)",
                    marks(["<b>(a)</b> A <b>triangle pointing along the wire</b> with a <b>bar</b> across its tip (current passes in the direction of the triangle).",
                           "<b>(b)</b> A <b>resistor rectangle</b> with a <b>bent line</b> drawn through it (an LDR is the rectangle with two arrows pointing in)."]), lines=2),
            written("el-n2-q4", "Explain why a voltmeter must not be connected in series with a lamp. (2)",
                    marks(["A voltmeter has a <b>very high resistance</b>.", "In series it would <b>almost stop the current</b>, so the lamp would not light and the reading would be meaningless."]), lines=2),
            choice("el-n2-q5", "On a cell symbol, which line is the positive terminal?",
                   ["The short thick line", "The long thin line", "Either", "Neither — the symbol has no polarity"], 1,
                   "Long thin = positive."),
            written("el-n2-q6", "A student draws a voltmeter across the battery to measure the pd across a resistor in a circuit with a variable resistor. Explain why the reading is wrong. (1)",
                    marks(["The pd across the battery is <b>shared</b> between the variable resistor and the resistor, so the voltmeter reads the <b>total</b>, not the resistor's share — it must be across the resistor only."]), lines=2),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N3 · Charge, current and time
# ---------------------------------------------------------------------

section_n3 = section(
    "charge-nn", "nn", "Charge, current and time: Q = I × t", "10.9, 10.10, 10.11",
    equations=[r"Q = I \times t", r"\text{current in} = \text{current out at a junction}"],
    blurb="Charge in coulombs is current times time. Two rules go with it: nothing flows unless the circuit is closed, and charge is never lost at a junction — the currents into it equal the currents out.",
    checklist=[
        "Use $Q = I \\times t$, with time in seconds and current in amps (convert mA)",
        "State that a closed circuit with a source of pd has a current",
        "Use conservation of current at a junction",
    ],
    parts=[
        explain(
            "The equation and the two rules",
            "<p>$Q = I \\times t$: charge (C) = current (A) × time (s). A 2 A current for 1 minute moves $2 \\times 60 = 120$ C. Two conversions catch people out: <b>minutes to seconds</b>, and <b>mA to A</b> (divide by 1000). The June 2025 report (Q4(c)): many \"made no attempt at conversion from mA to A\" and lost the evaluation mark; the same in Q10(a)(i). Write $2.5$ mA $= 0.0025$ A before you substitute.</p>"
            "<p><b>Closed circuit</b> (10.10): a current needs a <b>complete loop</b> of conductors <b>and</b> a <b>source of potential difference</b> (cell, battery, supply). Open the switch and the loop is broken — the current is zero everywhere in that loop at once.</p>"
            "<p><b>Conservation of current</b> (10.11): charge cannot pile up or vanish at a junction, so the <b>total current into a junction equals the total current out</b>. 0.5 A into a junction that splits two ways with 0.2 A in one branch means 0.3 A in the other. The June 2024 scheme (Q2(a)) tested exactly this: the currents in the branches must add up to the current from the battery.</p>",
        ),
        worked(
            "Charge with a conversion",
            "A current of 250 mA flows in a lamp for 4 minutes. Calculate the charge that passes through the lamp.",
            ewau(r"Q = I \times t", r"Q = 0.25 \times 240", "60", "C — 250 mA = 0.25 A and 4 min = 240 s before substituting"),
        ),
        practice("Charge and current", [
            numeric("el-n3-q1", "A current of 3 A flows for 2 minutes. Calculate the charge.", 360, "C", "Time in seconds.", ewau(r"Q = I \times t", r"Q = 3 \times 120", "360", "C")),
            numeric("el-n3-q2", "A charge of 90 C passes through a resistor in 30 s. Calculate the current.", 3, "A", "$I = Q \\div t$.", [r"$I = \dfrac{Q}{t} = \dfrac{90}{30} = 3$ A."]),
            numeric("el-n3-q3", "A current of 40 mA flows for 5 minutes. Calculate the charge.", 12, "C", "40 mA = 0.040 A; 5 min = 300 s.", ewau(r"Q = I \times t", r"Q = 0.040 \times 300", "12", "C")),
            choice("el-n3-q4", "At a junction, 0.8 A flows in. One branch carries 0.3 A. The other carries…",
                   ["0.8 A", "0.3 A", "0.5 A", "1.1 A"], 2,
                   "Current in = current out: $0.8 - 0.3 = 0.5$ A."),
            written("el-n3-q5", "State the two things needed for there to be a current in a circuit. (2)",
                    marks(["A <b>closed (complete) circuit</b> — an unbroken loop of conductors.", "A <b>source of potential difference</b> (a cell, battery or power supply) in the loop."]), lines=2),
            numeric("el-n3-q6", "How long does a current of 0.5 A take to move 600 C of charge?", 1200, "s", "$t = Q \\div I$.", [r"$t = \dfrac{Q}{I} = \dfrac{600}{0.5} = 1200$ s (20 minutes)."]),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N4 · Potential difference and energy
# ---------------------------------------------------------------------

section_n4 = section(
    "pd-energy", "nn", "Potential difference: energy per coulomb, and E = Q × V", "10.5, 10.6",
    equations=[r"V = \dfrac{E}{Q}", r"E = Q \times V", r"\text{1 V} = \text{1 J/C}"],
    blurb="A volt is a joule per coulomb. The potential difference across a component is the energy transferred by each coulomb of charge that passes through it — which is why $E = Q \\times V$, and why a 12 V battery does more with the same charge than a 1.5 V cell.",
    checklist=[
        "Define potential difference as energy transferred per unit charge, and the volt as a joule per coulomb",
        "Use $E = Q \\times V$, and combine it with $Q = I \\times t$",
        "Explain what the pd across a component tells you",
    ],
    parts=[
        explain(
            "What a volt is",
            "<p><b>Potential difference</b> (pd, also called voltage) across a component is the <b>energy transferred per unit charge</b> passing through it: $V = E \\div Q$. So the <b>volt is a joule per coulomb</b>: across a 6 V lamp, every coulomb that passes transfers 6 J of energy (to light and heat). Rearranged, $E = Q \\times V$: energy transferred (J) = charge moved (C) × pd (V).</p>"
            "<p>Across the <b>source</b>, the pd is the energy given <i>to</i> each coulomb (from the chemical store of the cell); across a <b>component</b>, it is the energy taken <i>from</i> each coulomb. Round a series circuit, the energy given per coulomb equals the energy taken per coulomb in total — the pds across the components add up to the pd of the source (N6).</p>"
            "<p>The June 2024 scheme (Q8(d), 2 marks): \"potential difference is energy transferred per unit charge passed\" (1), \"so the units of pd are J/C\" (1). Say both halves.</p>"
            "<p>With $Q = I \\times t$, $E = I \\times t \\times V$ — the same as 10.27's $E = I \\times V \\times t$ (N10).</p>",
        ),
        worked(
            "Energy from charge and pd",
            "A charge of 50 C passes through a motor connected across a 12 V battery. Calculate the energy transferred to the motor.",
            ewau(r"E = Q \times V", r"E = 50 \times 12", "600", "J"),
        ),
        practice("Potential difference", [
            written("el-n4-q1", "State what is meant by potential difference, and state what one volt is equivalent to. (2)",
                    marks(["The <b>energy transferred per unit charge</b> (per coulomb) passing through a component.", "So the volt is a <b>joule per coulomb</b> (J/C)."]), lines=2),
            numeric("el-n4-q2", "A charge of 20 C passes through a 230 V heater element. Calculate the energy transferred.", 4600, "J", "$E = Q \\times V$.", ewau(r"E = Q \times V", r"E = 20 \times 230", "4600", "J")),
            numeric("el-n4-q3", "A lamp transfers 90 J when 15 C passes through it. Calculate the pd across it.", 6, "V", "$V = E \\div Q$.", [r"$V = \dfrac{E}{Q} = \dfrac{90}{15} = 6$ V."]),
            numeric("el-n4-q4", "A 1.5 V cell drives 0.2 A for 5 minutes. Calculate the energy transferred.", 90, "J", "$Q = I t$ first, then $E = Q V$.",
                    [r"$Q = I \times t = 0.2 \times 300 = 60$ C.", r"$E = Q \times V = 60 \times 1.5 = 90$ J."]),
            choice("el-n4-q5", "A 9 V battery and a 1.5 V cell each push 10 C through a lamp. Which transfers more energy, and why?",
                   ["The cell, because it is smaller", "The battery, because each coulomb transfers 9 J instead of 1.5 J", "The same, because the charge is the same", "The cell, because it lasts longer"], 1,
                   "$E = QV$: 90 J against 15 J."),
            written("el-n4-q6", "Explain what the reading on a voltmeter across a resistor tells you. (2)",
                    marks(["The <b>potential difference</b> across the resistor…", "…which is the <b>energy transferred</b> (to the thermal store) <b>by each coulomb</b> of charge passing through it."]), lines=2),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N5 · Resistance and V = IR
# ---------------------------------------------------------------------

section_n5 = section(
    "ohm-nn", "nn", "Resistance and V = I × R", "10.12, 10.13",
    equations=[r"V = I \times R", r"R = \dfrac{V}{I}"],
    blurb="Resistance is how hard it is to push current through something: the pd needed per amp. More resistance in a circuit means less current for the same pd, and a variable resistor is how you change it on purpose.",
    checklist=[
        "Use $V = I \\times R$ in all three forms, with the ohm as the unit",
        "Explain how changing the resistance changes the current, and how a variable resistor does it",
        "Convert mA and kΩ before substituting",
    ],
    parts=[
        explain(
            "Resistance",
            "<p>$V = I \\times R$: pd (V) = current (A) × resistance (Ω). Resistance is the <b>ratio of pd to current</b>, $R = V \\div I$ — the number of volts needed to drive one amp. A 1 Ω component passes 1 A with 1 V across it; a 100 Ω one needs 100 V for the same current.</p>"
            "<p><b>Changing resistance changes current</b> (10.12): for a fixed pd, <b>more resistance → less current</b>, in inverse proportion (double R, halve I). A <b>variable resistor</b> is a long coil of resistance wire with a sliding contact: moving the slider puts <b>more or less wire</b> in the circuit, changing the resistance and so the current — which is how a dimmer, a volume control and the core practical work. The June 2023 report (Q2(b)(iv)): the variable resistor <b>increases the resistance</b> of the circuit, so it <b>keeps the current small (or constant)</b>, and it is the <b>current that heats the wire</b> — any two of those three links scored; \"slows the current\" is ignored, \"adjust the variable resistor to keep the current constant\" on its own was worth two marks, and many confused it with a thermistor.</p>"
            "<p>Units trap: kΩ × 1000 to Ω, mA ÷ 1000 to A. $6$ V across $2$ kΩ gives $I = 6 \\div 2000 = 0.003$ A $= 3$ mA.</p>",
        ),
        worked(
            "Resistance from V and I",
            "A pd of 6.0 V across a resistor gives a current of 9.1 mA. Calculate the resistance.",
            [r"Convert: $9.1$ mA $= 0.0091$ A.", r"$R = \dfrac{V}{I} = \dfrac{6.0}{0.0091} = 659.3\ldots = 660$ Ω (2 s.f.) — the June 2024 scheme's own numbers (Q2(b)(iii)); it allows any value that rounds to 660."],
        ),
        practice("V = IR", [
            numeric("el-n5-q1", "A current of 0.4 A flows through a 30 Ω resistor. Calculate the pd across it.", 12, "V", "$V = I \\times R$.", ewau(r"V = I \times R", r"V = 0.4 \times 30", "12", "V")),
            numeric("el-n5-q2", "A 12 V battery is connected across a 240 Ω resistor. Calculate the current.", 0.05, "A", "$I = V \\div R$.", [r"$I = \dfrac{V}{R} = \dfrac{12}{240} = 0.05$ A (50 mA)."]),
            numeric("el-n5-q3", "A pd of 4.5 V gives a current of 6 mA in a resistor. Calculate its resistance.", 750, "Ω", "6 mA = 0.006 A.", [r"$R = \dfrac{V}{I} = \dfrac{4.5}{0.006} = 750$ Ω."]),
            written("el-n5-q4", "Explain how a variable resistor is used to reduce the current in a circuit. (2)",
                    marks(["Moving the slider puts <b>more resistance wire into the circuit</b>, <b>increasing the resistance</b> of the circuit…",
                           "…and for the same pd a larger resistance gives a <b>smaller current</b> ($I = V/R$)."]), lines=2),
            choice("el-n5-q5", "The resistance in a circuit is doubled while the pd stays the same. The current…",
                   ["doubles", "halves", "stays the same", "becomes zero"], 1,
                   "$I = V/R$: inverse proportion."),
            numeric("el-n5-q6", "A 3.3 kΩ resistor carries a current of 2 mA. Calculate the pd across it.", 6.6, "V", "Convert both units first.", [r"$V = I \times R = 0.002 \times 3300 = 6.6$ V."]),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N6 · Series and parallel
# ---------------------------------------------------------------------

section_n6 = section(
    "circuits-nn", "nn", "Series and parallel circuits: the rules", "10.3, 10.11, 10.14, 10.15",
    equations=[r"\text{series: } I \text{ same},\ V_1 + V_2 = V,\ R = R_1 + R_2", r"\text{parallel: } V \text{ same},\ I_1 + I_2 = I,\ R < \text{smallest}"],
    blurb="Series: one loop, one current, the pd shared, the resistances add. Parallel: branches, the same pd across each, the currents add, and the total resistance is less than any branch. The explanations are marked on why, not just what.",
    checklist=[
        "State the series and parallel rules for current, pd and resistance",
        "Explain why adding a resistor in series increases the total resistance and in parallel decreases it",
        "Calculate currents, pds and resistances in series circuits",
    ],
    parts=[
        explain(
            "The rules",
            diagram(dg.series_parallel_svg(), 660, 250, "Two lamps in series and two in parallel.") +
            "<table class='tbl'><tr><th></th><th>Series</th><th>Parallel</th></tr>"
            "<tr><td><b>Current</b></td><td>the <b>same</b> at every point (one path)</td><td><b>splits</b> at the junction: the branch currents <b>add up</b> to the supply current</td></tr>"
            "<tr><td><b>Potential difference</b></td><td><b>shared</b> between the components: their pds <b>add up</b> to the supply pd — the bigger resistance takes the bigger share</td><td>the <b>same</b> across every branch (each branch is connected straight across the supply)</td></tr>"
            "<tr><td><b>Resistance</b></td><td><b>adds</b>: $R = R_1 + R_2$ — more than any one</td><td><b>less than the smallest</b> branch resistance</td></tr>"
            "<tr><td>Switch / break</td><td>one switch controls everything; one broken component stops all</td><td>each branch can have its own switch; a broken branch leaves the others working</td></tr></table>"
            "<p><b>Why series increases resistance:</b> the current has to pass through <b>both</b> resistors one after the other — more wire to push through — so the same pd drives less current: higher total resistance.</p>"
            "<p><b>Why parallel decreases resistance:</b> adding a branch gives the current <b>another path</b>; the same pd drives current through both branches at once, so the <b>total current increases</b> while the pd is unchanged — a smaller total resistance ($R = V/I$). The June 2024 scheme (Q2(b)(iv), 3 marks, for a resistor <i>removed</i> from parallel): total resistance <b>increases</b> (1) because the current <b>decreases</b> (1) while the <b>voltage stays the same</b> (1); \"fewer paths for the current\" accepted.</p>"
            "<p>Edexcel asks you to <b>calculate</b> in <b>series</b> circuits (10.15) and to <b>explain</b> parallel ones (10.14): you are not expected to use the $1/R$ formula. The June 2025 report (Q10(c)): Level 1 answers \"confused resistance and voltage\" — keep the three quantities separate.</p>",
        ),
        worked(
            "A series calculation",
            "A 6 V battery is connected in series with a 10 Ω resistor and a 20 Ω resistor. Calculate (a) the total resistance, (b) the current, (c) the pd across each resistor.",
            [
                r"<b>(a)</b> Series: $R = 10 + 20 = 30$ Ω.",
                r"<b>(b)</b> $I = \dfrac{V}{R} = \dfrac{6}{30} = 0.2$ A — the same current through both.",
                r"<b>(c)</b> $V_{10} = I \times R = 0.2 \times 10 = 2$ V; $V_{20} = 0.2 \times 20 = 4$ V. Check: $2 + 4 = 6$ V, the battery's pd. The larger resistor takes the larger share.",
            ],
        ),
        practice("Series and parallel", [
            choice("el-n6-q1", "Two lamps are in parallel across a 6 V battery. The pd across each lamp is…",
                   ["3 V", "6 V", "12 V", "it depends on the lamps"], 1,
                   "Each branch is connected straight across the supply."),
            numeric("el-n6-q2", "A 12 V supply drives a current through a 40 Ω and a 20 Ω resistor in series. Calculate the current.", 0.2, "A", "Add the resistances first.", [r"$R = 40 + 20 = 60$ Ω.", r"$I = \dfrac{12}{60} = 0.2$ A."]),
            numeric("el-n6-q3", "In the circuit above, calculate the pd across the 40 Ω resistor.", 8, "V", "$V = I \\times R$ for that resistor.", [r"$V = 0.2 \times 40 = 8$ V (and $0.2 \times 20 = 4$ V across the other: $8 + 4 = 12$ V)."]),
            written("el-n6-q4", "Explain why adding a second resistor in parallel with the first decreases the total resistance of the circuit. (3)",
                    mark_scheme([
                        ("Paths", "The second resistor gives the current <b>another path</b> (more routes through the circuit)."),
                        ("Current", "The pd across the combination is <b>unchanged</b>, but the <b>total current increases</b> (the branch currents add)."),
                        ("Resistance", "Same pd, more current, so the total resistance ($R = V/I$) is <b>smaller</b> — less than either resistor on its own."),
                    ]), lines=4),
            choice("el-n6-q5", "Three identical lamps are in series across a 9 V battery. The pd across each is…",
                   ["9 V", "3 V", "27 V", "1 V"], 1,
                   "Equal resistances share the pd equally."),
            written("el-n6-q6", "Give two reasons why the lights in a house are wired in parallel rather than in series. (2)",
                    marks(["Each lamp gets the <b>full mains pd</b> (so it works at its normal brightness)…", "…and each can be <b>switched independently</b>; if one fails the others stay on."]), lines=2),
            numeric("el-n6-q7", "Two resistors in parallel across a 6 V supply carry 0.3 A and 0.2 A. Calculate the current from the supply.", 0.5, "A", "Currents add at the junction.", [r"$0.3 + 0.2 = 0.5$ A."]),
        ]),
    ],
)

SECTIONS = [section_n1, section_n2, section_n3, section_n4, section_n5, section_n6]
