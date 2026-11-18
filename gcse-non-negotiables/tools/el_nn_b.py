"""
el_nn_b.py — Topic 10 (Electricity and circuits): the non-negotiables N7–N12.

N7  I–V characteristics            N10 Power and energy
N8  LDR and thermistor             N11 Mains electricity
N9  The heating effect             N12 Key words
"""

from revlib import (
    axis, choice, curve, diagram, ewau, explain, fact, graph, group, line,
    mark_scheme, marks, numeric, practice, section, worked, written,
)
import el_diagrams as dg


def iv_graphs():
    """The three I–V characteristics on one pair of axes each."""
    resistor = graph(axis("potential difference in V", 6, 2, mn=-6), axis("current in A", 0.6, 0.2, mn=-0.6),
                     [line([[-6, -0.6], [6, 0.6]])],
                     "Fixed resistor: a straight line through the origin — current proportional to pd, resistance constant (10 Ω here).",
                     labels=[{"x": 0.3, "y": 0.52, "text": "fixed resistor", "anchor": "start"}])
    # linear near the origin, flattening at higher pd: I = 0.28 V / (1 + 0.3 |V|)
    lamp_pts = [[x, round(0.28 * x / (1 + 0.3 * abs(x)), 4)] for x in [-6, -4.5, -3, -2, -1, -0.5, 0, 0.5, 1, 2, 3, 4.5, 6]]
    lamp = graph(axis("potential difference in V", 6, 2, mn=-6), axis("current in A", 0.6, 0.2, mn=-0.6),
                 [curve(lamp_pts)],
                 "Filament lamp: a curve that flattens as pd increases — the resistance increases as the filament gets hotter.",
                 labels=[{"x": 0.3, "y": 0.52, "text": "filament lamp", "anchor": "start"}])
    diode_pts = [[-6, 0], [-3, 0], [0, 0], [0.5, 0], [0.7, 0.02], [0.9, 0.08], [1.1, 0.2], [1.3, 0.38], [1.5, 0.6]]
    diode = graph(axis("potential difference in V", 6, 2, mn=-6), axis("current in A", 0.6, 0.2, mn=-0.6),
                  [curve(diode_pts)],
                  "Diode: no current for negative pd (very high resistance); for positive pd above about 0.7 V the current rises steeply (low resistance).",
                  labels=[{"x": 1.7, "y": 0.5, "text": "diode", "anchor": "start"}])
    return resistor, lamp, diode


IV_RESISTOR, IV_LAMP, IV_DIODE = iv_graphs()

# ---------------------------------------------------------------------
# N7 · I–V characteristics
# ---------------------------------------------------------------------

section_n7 = section(
    "iv-characteristics", "nn", "I–V characteristics: resistor, filament lamp, diode", "10.18",
    equations=[r"R = \dfrac{V}{I}\ \text{at each point}", r"\text{straight through the origin} \Leftrightarrow \text{constant } R"],
    blurb="Three graphs of current against pd to draw and to read. A straight line through the origin means constant resistance; a curve that flattens means the resistance is rising; a flat line at zero on one side means a diode.",
    checklist=[
        "Sketch the I–V graphs for a fixed resistor, a filament lamp and a diode",
        "State what each shape says about the resistance",
        "Find the resistance at a point on an I–V graph from R = V ÷ I",
    ],
    parts=[
        explain(
            "The three shapes",
            "<p>An <b>I–V graph</b> plots the <b>current</b> through a component (y) against the <b>pd</b> across it (x), for both directions of current (negative values on both axes). The resistance at any point is $R = V \\div I$ using the values <i>at that point</i>.</p>",
            graph=IV_RESISTOR,
        ),
        explain(
            "Filament lamp",
            "<p>The lamp's graph is a <b>curve</b> that gets <b>less steep</b> as the pd increases: each extra volt gives less extra current, so the <b>resistance increases</b> with pd. The filament is getting hotter (T3 explains why that raises the resistance). The June 2024 scheme (Q8(b)(ii)): \"as potential difference increases current increases\" (1) and \"non-linear — curve, changing gradient\" (1); Q8(b)(iii): resistance from $R = V/I$ at <b>two points</b> showing it increasing, or \"the gradient decreases as pd increases\" for 2 marks.</p>",
            graph=IV_LAMP,
        ),
        explain(
            "Diode",
            "<p>A <b>diode</b> conducts in <b>one direction only</b>: for negative pd the current is zero (very high resistance); for positive pd nothing happens until about 0.7 V, then the current rises steeply (low resistance). The June 2025 report (Q6(b)): the mark was for \"diodes allow current in one direction only\"; \"it limits the current\" and \"it is an LED indicator\" scored nothing.</p>",
            graph=IV_DIODE,
        ),
        worked(
            "Reading a resistance",
            "On a filament lamp's I–V graph, the current is 0.30 A at 1.5 V and 0.60 A at 6.0 V. Show that the resistance increases, and state what this tells you about the lamp.",
            [
                r"At 1.5 V: $R = \dfrac{V}{I} = \dfrac{1.5}{0.30} = 5.0$ Ω.",
                r"At 6.0 V: $R = \dfrac{6.0}{0.60} = 10$ Ω.",
                "The resistance has <b>doubled</b> as the pd rose — the filament is <b>hotter</b> at the higher pd and its resistance increases with temperature. (Do not use the gradient of the curve: resistance is V/I at the point, not the slope.)",
            ],
        ),
        practice("I–V graphs", [
            choice("el-n7-q1", "An I–V graph is a straight line through the origin. The component is…",
                   ["a filament lamp", "a diode", "a fixed resistor (constant resistance)", "a thermistor"], 2,
                   "Current proportional to pd: Ohm's law, constant resistance."),
            written("el-n7-q2", "Describe the I–V graph of a filament lamp and state what it shows about the lamp's resistance. (3)",
                    mark_scheme([
                        ("Trend", "As the pd increases the current <b>increases</b>…"),
                        ("Shape", "…but <b>not in proportion</b>: the graph is a <b>curve</b> whose gradient decreases (it flattens) at higher pd, the same shape in both directions."),
                        ("Resistance", "So the lamp's <b>resistance increases</b> as the pd (and the filament's temperature) increases."),
                    ]), lines=4),
            numeric("el-n7-q3", "From a resistor's I–V graph: at 4.0 V the current is 0.16 A. Calculate the resistance.", 25, "Ω", "R = V ÷ I at the point.", [r"$R = \dfrac{4.0}{0.16} = 25$ Ω."]),
            choice("el-n7-q4", "Which describes a diode's I–V graph?",
                   ["A straight line through the origin", "Zero current for one direction of pd, then a steep rise above about 0.7 V in the other", "A curve that flattens in both directions", "A horizontal line"], 1,
                   "One-way conduction with a threshold."),
            written("el-n7-q5", "Explain why a diode is connected between a transformer and a battery being charged. (2)",
                    marks(["A battery must be charged with <b>d.c.</b> — current in one direction only.", "A diode <b>allows current in one direction only</b>, so it stops the reverse half of the a.c. (it is not there to limit the current)."]), lines=2),
            group("el-n7-q6", "A filament lamp's I–V graph gives 0.20 A at 1.0 V and 0.50 A at 5.0 V.", [
                numeric("el-n7-q6a", "Calculate the resistance at 1.0 V.", 5, "Ω", "V ÷ I.", [r"$1.0 \div 0.20 = 5$ Ω."]),
                numeric("el-n7-q6b", "Calculate the resistance at 5.0 V.", 10, "Ω", "V ÷ I.", [r"$5.0 \div 0.50 = 10$ Ω — larger: the hotter filament has more resistance."]),
            ]),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N8 · LDR and thermistor
# ---------------------------------------------------------------------

LDR_GRAPH = graph(axis("light intensity", 10, 2), axis("resistance in kΩ", 10, 2),
                  [curve([[0.2, 10], [0.6, 7.4], [1, 5.6], [2, 3.6], [3, 2.6], [4, 2], [5, 1.6], [6, 1.3], [8, 1], [10, 0.8]])],
                  "LDR: the resistance falls as the light intensity rises.",
                  labels=[{"x": 6, "y": 6, "text": "LDR", "anchor": "start"}])
THERMISTOR_GRAPH = graph(axis("temperature in °C", 100, 20), axis("resistance in kΩ", 10, 2),
                         [curve([[0, 10], [10, 7.3], [20, 5.4], [30, 4], [40, 3], [50, 2.3], [60, 1.8], [70, 1.4], [80, 1.1], [90, 0.9], [100, 0.75]])],
                         "Thermistor (NTC): the resistance falls as the temperature rises.",
                         labels=[{"x": 60, "y": 6, "text": "thermistor", "anchor": "start"}])

section_n8 = section(
    "ldr-thermistor", "nn", "LDRs and thermistors", "10.19, 10.20",
    equations=[r"\text{LDR: brighter} \Rightarrow R \downarrow", r"\text{thermistor: hotter} \Rightarrow R \downarrow"],
    blurb="Two resistors whose resistance depends on the surroundings: an LDR's falls as the light gets brighter, a thermistor's falls as it gets hotter. Both are used to sense and switch.",
    checklist=[
        "Describe how the resistance of an LDR varies with light intensity",
        "Describe how the resistance of a (NTC) thermistor varies with temperature",
        "Give a use of each",
    ],
    parts=[
        explain(
            "Light-dependent resistor",
            "<p>An <b>LDR</b> (light-dependent resistor) has a resistance that <b>decreases as the light intensity increases</b>: very high in the dark, low in bright light (the graph is for one particular LDR). Uses: street lights and garden lights that come on at dusk, automatic brightness on a phone screen, burglar alarms triggered by a shadow.</p>",
            graph=LDR_GRAPH,
        ),
        explain(
            "Thermistor",
            "<p>A <b>thermistor</b> has a resistance that <b>decreases as the temperature increases</b> (the spec covers <b>negative temperature coefficient</b> thermistors only). Uses: thermostats in ovens, fridges and central heating; car engine-temperature sensors; fire alarms; a digital thermometer. The June 2023 report: many students described a <b>variable resistor</b> as if it were a thermistor — a variable resistor is changed <b>by hand</b>; a thermistor changes <b>by itself</b> with temperature.</p>"
            "<p>How the circuits that use them work — the pd sharing — is in T5.</p>",
            graph=THERMISTOR_GRAPH,
        ),
        worked(
            "Describe the graph",
            "Describe how the resistance of a thermistor changes with temperature, using the graph above. (2 marks)",
            [
                "As the temperature <b>increases</b> the resistance <b>decreases</b> (from 10 kΩ at 0 °C to under 1 kΩ at 100 °C).",
                "The change is <b>not linear</b>: the resistance falls steeply at first and then more slowly — the curve flattens.",
            ],
        ),
        practice("LDR and thermistor", [
            choice("el-n8-q1", "As the light falling on an LDR gets brighter, its resistance…",
                   ["increases", "decreases", "stays the same", "becomes infinite"], 1,
                   "Brighter → lower resistance."),
            choice("el-n8-q2", "As a thermistor gets hotter, its resistance…",
                   ["increases", "decreases", "stays the same", "becomes zero"], 1,
                   "NTC thermistor: hotter → lower resistance."),
            written("el-n8-q3", "Describe how the resistance of an LDR depends on light intensity, and give one use. (2)",
                    marks(["Its resistance <b>decreases as the light intensity increases</b> (high in the dark, low in bright light).", "Use: switching on street lights / garden lights at dusk; automatic screen brightness."]), lines=2),
            written("el-n8-q4", "State the difference between a thermistor and a variable resistor. (1)",
                    marks(["A thermistor's resistance changes <b>with temperature, by itself</b>; a variable resistor's is changed <b>by hand</b> (moving a slider)."]), lines=1),
            choice("el-n8-q5", "A thermistor is in series with a fixed resistor and an ammeter. The thermistor is warmed. The ammeter reading…",
                   ["decreases", "increases", "stays the same", "falls to zero"], 1,
                   "Thermistor resistance falls → total resistance falls → current rises."),
            written("el-n8-q6", "Give one use of a thermistor and explain why a thermistor is suitable for it. (2)",
                    marks(["A thermostat / oven or fridge temperature control / fire alarm / car temperature sensor.", "Its <b>resistance changes with temperature</b>, so the current (or pd) in its circuit changes with temperature and can switch a heater or alarm."]), lines=2),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N9 · The heating effect
# ---------------------------------------------------------------------

section_n9 = section(
    "heating-effect", "nn", "The heating effect of a current", "10.22–10.26",
    equations=[r"\text{electrons collide with ions} \Rightarrow \text{ions vibrate more} \Rightarrow \text{hotter}"],
    blurb="A current in a resistor heats it. The explanation is marked on collisions: electrons bump into the lattice ions, the ions vibrate more, and the energy ends up dissipated as thermal energy in the surroundings. Sometimes that is the point; often it is waste.",
    checklist=[
        "State that a current in a resistor transfers energy and heats it",
        "Explain the heating with collisions between electrons and the ions in the lattice",
        "Explain how low-resistance wires reduce unwanted energy transfer",
        "Give advantages and disadvantages of the heating effect",
    ],
    parts=[
        explain(
            "Why resistors get hot",
            "<p>When there is a current in a resistor there is an <b>energy transfer that heats the resistor</b> (10.22). Why (10.24): the free <b>electrons collide with the ions</b> in the metal's lattice as they are pushed through; each collision transfers energy to the ion, which <b>vibrates more</b> — and more vibration <i>is</i> a higher temperature. The electrical work done against the resistance is <b>dissipated as thermal energy</b> to the surroundings (10.23). That is also why a hot filament has a higher resistance: the ions vibrate more, so the electrons collide more often (T3).</p>"
            "<p><b>Reducing the waste</b> (10.25): energy transferred to heat in a wire is $I^2R$ per second, so use wires with <b>low resistance</b> — <b>thick</b> (large cross-section), <b>short</b>, made of a good conductor (<b>copper</b>). The June 2025 report (Q3(d)): the better cable has the <b>thicker copper wire</b> — lower resistance, so it carries a higher current safely with less heating; \"thicker <i>insulation</i> stops energy loss\" is wrong, and \"bigger\" alone scored nothing: say what is bigger and why it matters.</p>"
            "<table class='tbl'><tr><th>Heating effect wanted</th><th>Heating effect unwanted</th></tr>"
            "<tr><td>electric heaters, kettles, toasters, ovens, hair dryers; filament lamps (the filament glows); <b>fuses</b> (the wire melts when the current is too large)</td><td>wires and cables warming (wasted energy, lower efficiency); electronics overheating; fire risk if a cable carries too much current</td></tr></table>",
        ),
        worked(
            "The explain question",
            "Explain why a resistor gets hot when there is a current in it. (3 marks)",
            [
                "The current is a flow of <b>electrons</b> through the metal; they <b>collide with the ions</b> in the lattice.",
                "Each collision transfers energy to the ions, making them <b>vibrate more</b> — the resistor's temperature rises.",
                "The energy is transferred from the electrical pathway to the <b>thermal store</b> of the resistor and then <b>dissipated</b> to the surroundings.",
            ],
        ),
        practice("The heating effect", [
            written("el-n9-q1", "Explain, in terms of electrons and ions, why a wire gets warm when a current flows in it. (2)",
                    marks(["The moving <b>electrons collide with the ions</b> of the metal lattice.", "The collisions make the ions <b>vibrate more</b>, which is a rise in temperature (energy transferred to the thermal store)."]), lines=2),
            choice("el-n9-q2", "Which change to a cable reduces the energy wasted as heat for the same current?",
                   ["Thicker insulation", "A thicker copper wire", "A longer wire", "A thinner wire"], 1,
                   "Lower resistance → less I²R heating. Insulation does nothing to the resistance of the wire."),
            written("el-n9-q3", "Give one device that uses the heating effect of a current, and one situation where the heating effect is a disadvantage. (2)",
                    marks(["Use: a kettle / heater / toaster / filament lamp / fuse.", "Disadvantage: cables and components warming up wastes energy (lower efficiency) or risks fire / damage."]), lines=2),
            written("el-n9-q4", "Explain why thick copper wires are used to carry large currents. (3)",
                    mark_scheme([
                        ("Resistance", "A thicker wire (larger cross-sectional area) and a good conductor like copper have a <b>low resistance</b>."),
                        ("Heating", "The energy transferred to heat in the wire each second depends on the resistance ($P = I^2R$), so a low resistance means <b>less heating</b> for the same current."),
                        ("Safety", "So the wire can carry a large current <b>without overheating</b> (and less energy is wasted)."),
                    ]), lines=4),
            choice("el-n9-q5", "What happens to the energy transferred by a current in a resistor?",
                   ["It is stored in the resistor for ever", "It is dissipated as thermal energy to the surroundings", "It returns to the battery", "It becomes charge"], 1,
                   "Dissipated: spread to the surroundings as heat."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N10 · Power and energy
# ---------------------------------------------------------------------

section_n10 = section(
    "power-nn", "nn", "Power and energy: the four equations", "10.27–10.31, 10.42",
    equations=[r"P = \dfrac{E}{t}", r"P = I \times V", r"P = I^2 \times R", r"E = I \times V \times t"],
    blurb="Power is energy transferred per second, in watts. For an electrical device it is current × pd; for a resistor also current² × resistance. Energy is power × time — and a device's power rating tells you how fast its stored energy changes.",
    checklist=[
        "Define power as energy transferred per second, in watts",
        "Use P = E ÷ t, P = I × V, P = I² × R and E = I × V × t, choosing by what is given",
        "Relate a power rating to the energy transferred in a given time",
    ],
    parts=[
        explain(
            "Choosing the equation",
            "<p><b>Power</b> is the <b>energy transferred per second</b>: $P = E \\div t$, in <b>watts</b> (1 W = 1 J/s). A 2 kW kettle transfers 2000 J every second. A device's <b>power rating</b> (on its label) tells you how quickly it transfers energy from the mains or a battery: energy transferred $= P \\times t$ (10.42) — the higher the rating and the longer it runs, the more the energy store of the supply falls.</p>"
            "<table class='tbl'><tr><th>You know</th><th>Use</th></tr>"
            "<tr><td>current and pd</td><td>$P = I \\times V$ (10.30: the power transferred by any device is its current × the pd across it)</td></tr>"
            "<tr><td>current and resistance</td><td>$P = I^2 \\times R$ (a resistor's heating)</td></tr>"
            "<tr><td>energy and time</td><td>$P = E \\div t$</td></tr>"
            "<tr><td>current, pd and time</td><td>$E = I \\times V \\times t$</td></tr>"
            "<tr><td>power rating and time</td><td>$E = P \\times t$ — seconds, for joules</td></tr></table>"
            "<p>Why $P = IV$: each coulomb transfers $V$ joules, and $I$ coulombs pass each second, so $I \\times V$ joules per second. Why $P = I^2R$: substitute $V = IR$. The June 2025 report (Q3(b)): a straightforward $P = IV$ lost marks to calculator slips — \"250 ÷ 0.53\" instead of ×; write the substitution before pressing anything.</p>"
            "<p>Time in <b>seconds</b> unless the question works in hours; the June 2023 report (Q8(b)(i)) — the commonest error in an $E = IVt$ charging-time question was <b>not converting MJ to J and hours to seconds</b>, and a comparison only scored if the unit of the calculated time was stated.</p>",
        ),
        worked(
            "Power rating to current to energy",
            "A 2300 W kettle runs from the 230 V mains for 3 minutes. Calculate (a) the current in it and (b) the energy transferred.",
            [
                r"<b>(a)</b> $P = I \times V$, so $I = \dfrac{P}{V} = \dfrac{2300}{230} = 10$ A.",
                r"<b>(b)</b> $E = P \times t = 2300 \times 180 = 414\,000$ J $= 414$ kJ (or $E = IVt = 10 \times 230 \times 180$, the same).",
            ],
        ),
        practice("Power and energy", [
            numeric("el-n10-q1", "A lamp carries 0.25 A at 12 V. Calculate its power.", 3, "W", "P = I × V.", ewau(r"P = I \times V", r"P = 0.25 \times 12", "3", "W")),
            numeric("el-n10-q2", "A heater transfers 36 000 J in 2 minutes. Calculate its power.", 300, "W", "P = E ÷ t, t in seconds.", [r"$P = \dfrac{36\,000}{120} = 300$ W."]),
            numeric("el-n10-q3", "A current of 2 A flows in a 15 Ω resistor. Calculate the power dissipated.", 60, "W", "P = I² × R.", ewau(r"P = I^2 \times R", r"P = 2^2 \times 15", "60", "W")),
            numeric("el-n10-q4", "A 230 V motor draws 2 A for 5 minutes. Calculate the energy transferred.", 138000, "J", "E = I × V × t, t = 300 s.", ewau(r"E = I \times V \times t", r"E = 2 \times 230 \times 300", "138\\,000", "J")),
            written("el-n10-q5", "State what is meant by the power of an electrical device, and its unit. (2)",
                    marks(["The <b>energy transferred per second</b> (rate of energy transfer).", "Measured in <b>watts</b> (1 W = 1 J/s)."]), lines=2),
            numeric("el-n10-q6", "A 1.2 kW hair dryer is used for 5 minutes. Calculate the energy transferred.", 360000, "J", "P in W, t in s.", [r"$E = P \times t = 1200 \times 300 = 360\,000$ J (360 kJ)."]),
            numeric("el-n10-q7", "A 60 W lamp runs from 230 V. Calculate the current.", 0.26, "A", "I = P ÷ V.", [r"$I = \dfrac{60}{230} = 0.26$ A (2 s.f.)."], tolerance=0.03),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N11 · Mains electricity
# ---------------------------------------------------------------------

section_n11 = section(
    "mains", "nn", "Mains electricity: a.c., the three wires, fuses and earthing", "10.32–10.41",
    equations=[r"\text{UK mains: a.c., 50 Hz, about 230 V}", r"\text{live 230 V},\ \text{neutral 0 V},\ \text{earth 0 V}"],
    blurb="Cells give d.c.; the mains is a.c. at 50 Hz and about 230 V. Three wires come into every appliance — live, neutral and earth — and the fuse, the switch and the earth wire each have one job, marked in specific words. The fuse melts; it does not blow.",
    checklist=[
        "Explain the difference between direct and alternating current, with the UK values",
        "State the pd of the live, neutral and earth wires and the job of each",
        "Explain how a fuse, a circuit breaker and the earth wire make an appliance safe",
        "Explain why switches and fuses go in the live wire, and why a live–earth connection is dangerous",
    ],
    parts=[
        explain(
            "d.c. and a.c.",
            diagram(dg.ac_dc_svg(), 700, 280, "A d.c. supply keeps one direction; an a.c. supply reverses direction every half cycle.") +
            "<p><b>Direct current (d.c.)</b> is movement of charge in <b>one direction only</b>; cells and batteries supply d.c. <b>Alternating current (a.c.)</b> is movement of charge that <b>changes direction</b> repeatedly — the pd swings positive and negative. The UK <b>mains</b> is a.c. at a <b>frequency of 50 Hz</b> (50 cycles a second) and a pd of <b>about 230 V</b>. In the home, energy is transferred from the a.c. mains or from batteries to <b>motors</b> (kinetic) and <b>heating devices</b> (thermal) (10.32).</p>",
        ),
        explain(
            "The three wires and the safety parts",
            diagram(dg.plug_svg(), 760, 320, "Inside a UK plug: earth (green and yellow) to the top pin, live (brown) to the right pin through the fuse, neutral (blue) to the left pin.") +
            "<table class='tbl'><tr><th>Wire</th><th>Colour</th><th>pd</th><th>Job</th></tr>"
            "<tr><td><b>Live</b></td><td>brown</td><td><b>230 V</b> (alternating)</td><td>carries the current <b>to</b> the appliance from the supply; the dangerous one</td></tr>"
            "<tr><td><b>Neutral</b></td><td>blue</td><td><b>0 V</b></td><td>completes the circuit — carries the current <b>back</b> to the supply</td></tr>"
            "<tr><td><b>Earth</b></td><td>green and yellow</td><td><b>0 V</b></td><td>a <b>safety</b> wire connected to the metal case; carries no current unless there is a fault</td></tr></table>"
            "<p><b>Fuse:</b> a thin wire in the live wire, rated at a current a little above the appliance's normal current (3 A, 5 A, 13 A). If the current <b>exceeds the rating</b>, the fuse wire <b>heats up and melts</b>, which <b>breaks the circuit</b> and cuts off the current. Say <b>melts</b>: a fuse does not explode, and \"blows\" is not the physics. The June 2025 scheme (Q3(c)(ii)) gave two marks for \"the fuse wire melts\" and \"this breaks the circuit\"; answers that did not say what the fuse <i>does</i> scored one.</p>"
            "<p><b>Circuit breaker:</b> an automatic switch (an electromagnet) that <b>trips</b> when the current is too large; it does the fuse's job but faster, and it can be <b>reset</b> instead of replaced. The 2025 scheme accepted circuit breaker, earth wire, cable clamp, socket covers and insulation as safety devices \"other than a fuse\".</p>"
            "<p><b>Earth wire:</b> connected to the <b>metal case</b>. If a fault makes the live wire touch the case, the case would become live (230 V) and anyone touching it would get a shock. With the earth wire, the current flows through the <b>low-resistance earth path</b> instead — a <b>large current</b>, which <b>melts the fuse</b> and cuts the supply, and the case stays at 0 V. Appliances with plastic cases are <b>double insulated</b> and need no earth wire.</p>"
            "<p><b>Why the switch and fuse are in the live wire</b> (10.39): opening the switch (or melting the fuse) in the live wire <b>disconnects the appliance from the 230 V</b>, so nothing inside is live when it is off. In the neutral wire they would stop the current but leave the appliance <b>connected to 230 V</b> — still dangerous to touch.</p>"
            "<p><b>Live to earth</b> (10.41): there is a pd of <b>230 V</b> between the live wire and the earth (the ground, water pipes, a person standing on the floor). Any connection between them — a bare live wire touched by a person — gives a <b>large current through the connection</b>: an electric shock, or a fire. That is also why water (a conductor) and mains electricity are kept apart.</p>",
        ),
        worked(
            "Fuse and earth together",
            "A metal-cased heater has a fault: the live wire touches the case. Explain how the earth wire and the fuse protect the user. (4 marks)",
            [
                "The case is connected to the <b>earth wire</b>, a <b>low-resistance path</b> to the ground.",
                "So when the live wire touches the case, a <b>large current</b> flows from the live wire, through the case, to earth…",
                "…and the large current makes the <b>fuse wire melt</b>, which <b>breaks the circuit</b> and disconnects the heater from the live supply.",
                "The case therefore cannot stay at 230 V, so a user touching it does not get a shock.",
            ],
        ),
        practice("Mains electricity", [
            written("el-n11-q1", "Describe the difference between direct and alternating current, and state the frequency and pd of the UK mains. (3)",
                    mark_scheme([
                        ("d.c.", "Direct current: charge moves in <b>one direction only</b> (cells and batteries)."),
                        ("a.c.", "Alternating current: the movement of charge <b>changes direction</b> repeatedly (the pd alternates between + and −)."),
                        ("UK mains", "a.c. at <b>50 Hz</b> and about <b>230 V</b>."),
                    ]), lines=3),
            choice("el-n11-q2", "What are the pds of the live, neutral and earth wires?",
                   ["230 V, 230 V, 0 V", "230 V, 0 V, 0 V", "0 V, 230 V, 0 V", "230 V, 0 V, 230 V"], 1,
                   "Live alternates at 230 V; neutral and earth are at 0 V (earth potential)."),
            written("el-n11-q3", "Explain what a fuse does if the current in an appliance becomes too large. (2)",
                    marks(["The fuse wire <b>heats up and melts</b> when the current exceeds its rating…", "…which <b>breaks the circuit</b>, cutting off the current to the appliance (and the live supply)."]), lines=2),
            written("el-n11-q4", "Explain why the switch of an appliance is connected in the live wire and not the neutral wire. (2)",
                    marks(["In the live wire, opening the switch <b>disconnects the appliance from the 230 V supply</b>, so no part of it is live when switched off.",
                           "In the neutral wire the current would stop but the appliance would <b>still be connected to the live 230 V</b> — dangerous to touch."]), lines=3),
            written("el-n11-q5", "Explain the function of the earth wire. (3)",
                    mark_scheme([
                        ("Connection", "It connects the <b>metal case</b> of the appliance to earth (0 V), carrying no current normally."),
                        ("Fault", "If the live wire touches the case, the earth wire provides a <b>low-resistance path</b>, so a <b>large current</b> flows to earth…"),
                        ("Result", "…which <b>melts the fuse</b> and cuts off the supply; the case cannot become live, so the user is not shocked."),
                    ]), lines=4),
            choice("el-n11-q6", "Which statement about a circuit breaker is correct?",
                   ["It melts when the current is too large", "It is an automatic switch that trips when the current is too large and can be reset", "It increases the current", "It replaces the earth wire"], 1,
                   "A resettable electromagnetic switch; the fuse is the one that melts."),
            written("el-n11-q7", "Explain why it is dangerous to touch a bare live wire while standing on the ground. (2)",
                    marks(["There is a pd of about <b>230 V between the live wire and earth</b>.", "A person touching the wire <b>connects live to earth</b>, so a <b>large current flows through them</b> — an electric shock."]), lines=2),
            choice("el-n11-q8", "A fuse in a plug is rated 3 A. The appliance normally draws 2.5 A. Which is correct?",
                   ["The fuse is too small and will melt in normal use", "The fuse rating is just above the normal current, so it only melts if a fault raises the current", "A 13 A fuse would be safer", "Fuses do not have ratings"], 1,
                   "Choose the lowest standard rating above the normal current."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N12 · Key words
# ---------------------------------------------------------------------

DEFINITIONS = [
    ("Electric current", "The <b>rate of flow of charge</b>; in metals a flow of <b>electrons</b>. Unit ampere (A) = coulomb per second.", "\"the flow of electricity\""),
    ("Charge", "Carried by electrons (−) and protons (+); measured in <b>coulombs</b> (C); Q = I × t.", "\"the amount of current\""),
    ("Potential difference", "The <b>energy transferred per unit charge</b> passing through a component; the volt is a <b>joule per coulomb</b>.", "\"the push\" / \"the amount of electricity\""),
    ("Resistance", "The <b>ratio of pd to current</b> for a component, R = V ÷ I, in ohms (Ω); how hard it is to drive current through it.", "\"something that slows the current down\""),
    ("Series circuit", "Components connected <b>one after another in a single loop</b>: same current through each, pd shared.", "\"in a line\""),
    ("Parallel circuit", "Components connected in <b>separate branches</b> across the same two points: same pd across each, current shared.", "\"side by side\""),
    ("Ohmic conductor", "A component whose current is <b>proportional to the pd</b> across it (constant resistance): a straight I–V line through the origin.", "\"a resistor\""),
    ("Diode", "A component that allows current in <b>one direction only</b>.", "\"a one-way valve\" alone"),
    ("Thermistor", "A resistor whose resistance <b>decreases as its temperature increases</b>.", "\"a temperature sensor\""),
    ("LDR", "A light-dependent resistor: resistance <b>decreases as the light intensity increases</b>.", "\"a light sensor\""),
    ("Power", "The <b>energy transferred per second</b>; watt (W) = joule per second. P = E ÷ t = I × V.", "\"how strong it is\""),
    ("Direct current", "Movement of charge in <b>one direction only</b>; supplied by cells and batteries.", "\"a constant current\""),
    ("Alternating current", "Movement of charge that <b>changes direction</b> repeatedly; UK mains 50 Hz, about 230 V.", "\"current that goes up and down\""),
    ("Live wire", "The brown wire at <b>230 V</b> (alternating) that carries the current to the appliance; the switch and fuse are in it.", "\"the main wire\""),
    ("Neutral wire", "The blue wire at <b>0 V</b> that completes the circuit back to the supply.", "\"the safe wire\""),
    ("Earth wire", "The green-and-yellow wire at <b>0 V</b> connected to the <b>metal case</b>; a low-resistance path for a fault current so the fuse melts.", "\"the wire that stops shocks\" alone"),
    ("Fuse", "A thin wire in the live wire that <b>melts</b> when the current exceeds its rating, <b>breaking the circuit</b>.", "\"blows\" / \"explodes\""),
    ("Circuit breaker", "An automatic switch that <b>trips</b> (opens) when the current is too large; can be <b>reset</b>.", "\"a fuse\""),
]


def definitions_table():
    html = "<table class='tbl'><tr><th>Term</th><th>What to write (mark-scheme form)</th><th>Not this</th></tr>"
    for term, definition, wrong in DEFINITIONS:
        html += "<tr><td><b>" + term + "</b></td><td>" + definition + "</td><td>" + wrong + "</td></tr>"
    html += "</table>"
    return html


section_keywords = section(
    "keywords-electricity", "nn", "Key words: state what is meant by…", "10",
    equations=[r"\text{definition, word for word}"],
    blurb="One-mark definitions in the form of words the mark schemes credit. The bold words are the ones the marks are attached to.",
    checklist=[
        "Define current, charge, potential difference and resistance",
        "Define series, parallel, ohmic conductor, diode, thermistor, LDR and power",
        "Define d.c., a.c., live, neutral, earth, fuse and circuit breaker",
    ],
    parts=[
        explain("The definitions", "<p>\"<b>State what is meant by</b>\" asks for the definition. Learn these as sentences.</p>" + definitions_table()),
        practice("Key words", [
            written("el-kw-q1", "State what is meant by potential difference. (1)",
                    marks(["The <b>energy transferred per unit charge</b> (per coulomb) passing through a component."]), lines=1),
            written("el-kw-q2", "State what is meant by electric current. (1)",
                    marks(["The <b>rate of flow of charge</b>."]), lines=1),
            choice("el-kw-q3", "Which is the correct description of what a fuse does?",
                   ["It blows when the current is too high", "Its wire melts when the current exceeds its rating, breaking the circuit", "It stores charge", "It reduces the voltage"], 1,
                   "Melts and breaks the circuit."),
            written("el-kw-q4", "State what is meant by direct current. (1)",
                    marks(["Movement of charge in <b>one direction only</b>."]), lines=1),
            written("el-kw-q5", "State what is meant by the resistance of a component. (1)",
                    marks(["The <b>ratio of the pd across it to the current</b> through it (R = V ÷ I), in ohms."]), lines=1),
            choice("el-kw-q6", "Which describes a parallel circuit?",
                   ["Components in one loop with the same current", "Components in separate branches with the same pd across each", "A circuit with two cells", "A circuit with no switch"], 1,
                   "Branches across the same two points."),
            written("el-kw-q7", "State what is meant by electrical power. (1)",
                    marks(["The <b>energy transferred per second</b> by the device (in watts)."]), lines=1),
            written("el-kw-q8", "State the function of the live wire and the neutral wire. (2)",
                    marks(["Live: at <b>230 V</b>, carries the current <b>to</b> the appliance.", "Neutral: at <b>0 V</b>, <b>completes the circuit</b> back to the supply."]), lines=2),
        ]),
    ],
)

FACTS_KW = [fact("State what is meant by: " + (term if term.isupper() else term[0].lower() + term[1:]) + ".", definition, "keywords-electricity") for term, definition, wrong in DEFINITIONS]

SECTIONS = [section_n7, section_n8, section_n9, section_n10, section_n11, section_keywords]
