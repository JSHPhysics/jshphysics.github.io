"""
en_tricky_b.py — Topics 3 and 8 (Energy): the tricky bits T7–T11 and
the flashcards.

T7  Energy graphs                  T10 Multi-step energy chains
T8  Explaining dissipation         T11 Apply the seven steps
T9  Energy resources: trends
"""

from revlib import (
    axis, choice, data, ewau, explain, fact, graph, group, label, line,
    mark_scheme, marks, numeric, practice, section, sf, shade, worked, written,
)

G = 10

# ---------------------------------------------------------------------
# T7 · Energy graphs
# ---------------------------------------------------------------------

# Force–distance graph: constant 40 N for 0–3 m, then falling linearly to 0 at 5 m
graph_fd = graph(
    axis("distance in m", 5, 1), axis("force in N", 50, 10),
    [line([[0, 40], [3, 40], [5, 0]])],
    "A force–distance graph: 40 N from 0 to 3 m, then a straight line down to zero at 5 m.",
    shade_list=[shade(0, 0, 5)],
)
work_fd = 40 * 3 + 0.5 * 2 * 40

# Energy–time graph for a motor: straight line through origin, 600 J at 12 s
graph_et = graph(
    axis("time in s", 12, 2), axis("energy transferred in J", 600, 100),
    [line([[0, 0], [12, 600]])],
    "A straight-line energy–time graph from the origin to (12 s, 600 J).",
)
power_et = 600 / 12

# KE against v² for a 2 kg trolley: gradient = ½ m = 1
graph_kv = graph(
    axis("speed² in m²/s²", 10, 2), axis("kinetic energy in J", 10, 2),
    [data([[1, 1.1], [2, 1.9], [4, 4.1], [6, 5.9], [8, 8.1], [9, 9.0]]), line([[0, 0], [10, 10]])],
    "Kinetic energy plotted against speed squared: points close to a straight line through the origin with gradient 1.",
)

section_t7 = section(
    "energy-graphs", "tricky", "Energy graphs: areas and gradients", "8.6, 8.13, 3.2",
    equations=[r"\text{area under } F\text{–}d \text{ graph} = \text{work done}", r"\text{gradient of } E\text{–}t \text{ graph} = \text{power}", r"\text{gradient of } KE\text{–}v^{2} \text{ graph} = \tfrac{1}{2} m"],
    blurb="Three graphs carry energy information: the area under a force–distance graph is the work done, the gradient of an energy–time graph is the power, and a graph of KE against v² is a straight line whose gradient is half the mass.",
    checklist=[
        "Find work done from the area under a force–distance graph (split it into rectangles and triangles)",
        "Find power from the gradient of an energy–time graph",
        "Explain why KE against v² is a straight line through the origin and read the mass from it",
        "Convert centimetres on a graph axis to metres before finding an area",
    ],
    parts=[
        explain(
            "Which graph gives what",
            "<table class='tbl'><tr><th>Graph</th><th>Read off</th><th>How</th></tr>"
            "<tr><td>force (N) against distance (m)</td><td>work done (J)</td><td><b>area</b> under the line — because work = $F \\times d$</td></tr>"
            "<tr><td>energy (J) against time (s)</td><td>power (W)</td><td><b>gradient</b> — because $P = E \\div t$</td></tr>"
            "<tr><td>force (N) against extension (m)</td><td>elastic potential energy (J)</td><td><b>area</b> under the line (Topic 15 — same idea)</td></tr>"
            "<tr><td>KE (J) against speed² (m²/s²)</td><td>mass (kg)</td><td>straight line through the origin, <b>gradient $= \\tfrac{1}{2} m$</b></td></tr></table>"
            "<p>For an area, split the shape into a rectangle and a triangle; the triangle is ½ × base × height. <b>Check the axis units first</b>: if the distance axis is in cm, convert to m before multiplying, or the answer is 100 times too big (the June 2025 report: \"the most common error was to forget to convert the extension from cm to m\" on exactly this kind of area).</p>",
        ),
        worked(
            "Work done from a force–distance graph",
            "The graph shows the force on a sledge against the distance it is pulled. Calculate the total work done.",
            [
                r"<b>Rectangle (0–3 m):</b> $40 \times 3 = 120$ J.",
                r"<b>Triangle (3–5 m):</b> $\tfrac{1}{2} \times 2 \times 40 = 40$ J.",
                r"<b>Total work done = area:</b> $120 + 40 = 160$ J.",
            ],
            graph=graph_fd,
        ),
        practice("Energy graphs", [
            numeric("en-t7-q1", "Use the graph to calculate the work done over the 5 m.", work_fd, "J", "Rectangle plus triangle.",
                    [r"$40 \times 3 = 120$ J; $\tfrac{1}{2} \times 2 \times 40 = 40$ J; total $160$ J."], graph=graph_fd),
            numeric("en-t7-q2", "The graph shows the energy transferred by a motor against time. Calculate the power of the motor.", power_et, "W", "Gradient = energy ÷ time.",
                    [r"Gradient $= \dfrac{600 - 0}{12 - 0} = 50$ W."], graph=graph_et),
            group("en-t7-q3", "A student measures the kinetic energy of a trolley at different speeds and plots KE against speed².", [
                choice("en-t7-q3a", "What does the shape of the graph show?",
                       ["KE is proportional to speed", "KE is proportional to speed² (straight line through the origin)", "KE is constant", "KE is inversely proportional to speed²"], 1,
                       "A straight line through the origin means the quantities are directly proportional: $\\text{KE} \\propto v^2$, as $\\text{KE} = \\tfrac{1}{2} m v^2$ predicts.", label="a"),
                numeric("en-t7-q3b", "Use the gradient of the line to find the mass of the trolley.", 2, "kg", "Gradient $= \\tfrac{1}{2} m$, so $m = 2 \\times$ gradient.",
                        [r"Gradient $= \dfrac{10}{10} = 1$ J per m²/s²; $\tfrac{1}{2} m = 1$ so $m = 2$ kg."], label="b"),
            ], graph=graph_kv),
            numeric("en-t7-q4", "A force–extension graph for a spring is a straight line from the origin to (8 cm, 20 N). Calculate the energy stored in the spring at 8 cm extension.",
                    0.5 * 0.08 * 20, "J", "Area of the triangle, with the extension in metres.",
                    [r"$8\ \text{cm} = 0.08$ m.", r"Area $= \tfrac{1}{2} \times 0.08 \times 20 = 0.8$ J. Using 8 instead of 0.08 gives 80 J — 100 times too big."]),
            choice("en-t7-q5", "On a graph of energy transferred against time, a steeper line means…",
                   ["more energy in total", "a greater power", "a longer time", "less energy"], 1,
                   "Gradient = energy ÷ time = power."),
        ]),
    ],
)
section_t7["subtopic"] = ["3", "8"]

# ---------------------------------------------------------------------
# T8 · Explaining dissipation and insulation (the written marks)
# ---------------------------------------------------------------------

section_t8 = section(
    "explain-dissipation", "tricky", "Explaining dissipation, insulation and lubrication", "3.7, 3.8, 3.9, 3.10, 8.10, 8.11",
    equations=[r"\text{name the store} + \text{name the pathway} + \text{say ``rate''}"],
    blurb="The 2- to 4-mark \"explain\" questions in this topic are all the same shape: what is wasted, where it goes, and (for insulation) what reduces the rate. Here is the shape, and the phrases the mark schemes reject.",
    checklist=[
        "Explain why a real transfer gives less useful energy than calculated",
        "Explain why a temperature rise is less than predicted (energy transferred to the surroundings)",
        "Explain an insulation result in terms of thermal conductivity and rate",
        "Never write \"energy is lost\", \"not 100% efficient\" or \"sound\" as the whole answer",
    ],
    parts=[
        explain(
            "The answer shape, and the banned phrases",
            "<p>Every one of these answers is: <b>(1) what is wasted → (2) which store it goes to → (3) by which pathway → (4) the consequence.</b></p>"
            "<p>Example — <i>why is the water's temperature rise less than calculated from the heater's energy?</i> (1) Not all the energy supplied goes to the water; (2) some is transferred to the thermal store of the container and the surroundings; (3) by heating; (4) so less energy is in the water's thermal store and $\\Delta\\theta = \\dfrac{E}{m c}$ is smaller.</p>"
            "<p>The June 2024 scheme for that question: \"Do not accept unqualified <b>energy is lost / wasted</b>, <b>not 100% efficient</b>, or arguments about <b>sound</b>.\" Two of those four points, properly linked, scored both marks; \"the brick transfers thermal energy to the surroundings\" scored 2 on its own because it names the store, the direction and the pathway.</p>"
            "<p><b>Insulation answers</b> need the word <b>rate</b>: insulation (low thermal conductivity, trapped air) <b>reduces the rate</b> of energy transfer to the surroundings; it never stops it. If an experiment compares insulators, the one whose water cools <b>least in the same time</b> is the best insulator, because the rate of transfer through it is lowest.</p>"
            "<p><b>Lubrication answers</b> need the word <b>friction</b>: oil reduces friction between the surfaces, so less work is done against friction, so less energy is transferred to the thermal store, so more of the input is useful (higher efficiency).</p>",
        ),
        worked(
            "A four-mark explain",
            "A student heats a metal block with an electric heater and calculates the expected temperature rise. The measured rise is smaller. Explain why. (3 marks)",
            [
                "<b>What is wasted:</b> not all the energy supplied by the heater goes into the <b>block</b>…",
                "<b>Where and how:</b> …some is transferred by <b>heating</b> to the <b>thermal store of the surroundings</b> (the air, the bench, the heater's own casing)…",
                "<b>Consequence:</b> …so the block's thermal store gains <b>less energy</b> than was supplied, and since temperature rise is proportional to the energy gained, the rise is <b>smaller</b> than calculated.",
            ],
        ),
        practice("Explain questions", [
            written("en-t8-q1", "A ball bearing is dropped into a tube of oil and its temperature rise is measured. The rise is smaller than the value calculated from the GPE lost. Explain why. (2)",
                    marks(["Not all the GPE lost is transferred to the <b>thermal store of the ball</b>…",
                           "…some is transferred to the <b>thermal store of the oil and the surroundings</b> (by friction / heating), so the ball's temperature rises less."]), lines=3),
            written("en-t8-q2", "Explain why wrapping a beaker of hot water in bubble wrap makes it cool more slowly. (3)",
                    mark_scheme([
                        ("Conductivity", "Bubble wrap has a <b>low thermal conductivity</b> (it traps <b>air</b>, which is a poor conductor)."),
                        ("Rate", "So the <b>rate</b> of energy transfer by heating from the water to the surroundings is <b>reduced</b>."),
                        ("Consequence", "Less energy leaves the water's thermal store each second, so its temperature falls more slowly."),
                    ]), lines=4),
            written("en-t8-q3", "A student says \"the motor is only 60% efficient because energy is lost\". Rewrite this as an answer that would score. (2)",
                    marks(["40% of the energy supplied is transferred to the <b>thermal store of the motor and the surroundings</b>…",
                           "…<b>by friction</b> in the bearings and <b>by heating</b> in the wires (dissipated), so only 60% reaches the kinetic store of the load."]), lines=3),
            choice("en-t8-q4", "In an insulation experiment, three beakers of hot water lose 8 °C, 12 °C and 20 °C in the same 10 minutes. Which conclusion is correct?",
                   ["The 20 °C beaker has the best insulation because more energy was transferred", "The 8 °C beaker has the best insulation because the rate of energy transfer through its insulation was lowest", "They are all the same because the time was the same", "The 12 °C beaker is best because it is in the middle"], 1,
                   "Best insulator = smallest temperature drop in the same time = lowest rate of energy transfer."),
            written("en-t8-q5", "Explain why a car engine gets hot, in terms of energy. (2)",
                    marks(["<b>Friction</b> between the moving parts does work, transferring energy to the <b>thermal store of the engine</b>; the burning fuel also transfers energy to it by heating.",
                           "This energy is <b>dissipated</b> — it is not transferred to the kinetic store of the car — which is why the engine's temperature rises (and why engines are oiled and cooled)."]), lines=3),
            written("en-t8-q6", "Explain how adding oil to a bicycle chain increases the efficiency of the bicycle. (3)",
                    mark_scheme([
                        ("Friction", "The oil <b>reduces friction</b> between the chain and the cogs."),
                        ("Less wasted", "So less work is done against friction and <b>less energy is transferred to the thermal store</b> of the surroundings."),
                        ("Efficiency", "So a <b>larger fraction</b> of the cyclist's energy is transferred usefully to the kinetic store — the efficiency increases."),
                    ]), lines=4),
        ]),
    ],
)
section_t8["subtopic"] = ["3", "8"]

# ---------------------------------------------------------------------
# T9 · Energy resources: patterns and trends
# ---------------------------------------------------------------------

TREND_TABLE = (
    "<table class='tbl data'><tr><th>Year</th><th>Coal %</th><th>Gas %</th><th>Nuclear %</th><th>Wind and solar %</th><th>Other renewables %</th></tr>"
    "<tr><td>2000</td><td>40</td><td>35</td><td>20</td><td>0</td><td>5</td></tr>"
    "<tr><td>2010</td><td>30</td><td>40</td><td>18</td><td>5</td><td>7</td></tr>"
    "<tr><td>2020</td><td>2</td><td>38</td><td>16</td><td>30</td><td>14</td></tr></table>"
    "<p class='small'>Electricity generation by source for an imaginary country, as a share of the total. Exam tables are real; this one is made up for practice.</p>"
)

section_t9 = section(
    "resources-trends", "tricky", "Energy resources: patterns and trends", "3.14",
    equations=[r"\text{describe the trend} \rightarrow \text{explain it}"],
    blurb="The spec asks you to explain patterns and trends in the use of energy resources. The question gives a table or graph; you describe what it shows — with numbers — and give reasons.",
    checklist=[
        "Describe a trend from a table or graph, quoting figures",
        "Give reasons for a trend (cost, climate change, running out, technology)",
        "Separate \"describe\" (what the data shows) from \"explain\" (why)",
    ],
    parts=[
        explain(
            "How to answer a trends question",
            "<p><b>Describe</b> = say what the numbers do, using them: \"coal fell from 40% in 2000 to 2% in 2020, while wind and solar rose from 0% to 30%\". A description with no figures from the data is worth less.</p>"
            "<p><b>Explain</b> = give reasons. The ones examiners accept for the usual trends:</p><ul>"
            "<li>Fossil fuel use is falling because burning them releases <b>carbon dioxide</b> (climate change) and other pollution, governments have set targets, and they are <b>non-renewable</b> and will run out.</li>"
            "<li>Renewables are rising because the <b>technology has improved and got cheaper</b> (wind turbines, solar cells), and because they produce no carbon dioxide while generating.</li>"
            "<li>Gas has replaced coal first because it produces <b>less carbon dioxide per unit of energy</b> and gas power stations are quick to start and stop.</li>"
            "<li>Total energy use in the world is rising because the <b>population</b> and the amount of <b>technology</b> per person are rising; in some countries it is falling because appliances are more <b>efficient</b>.</li></ul>"
            "<p>You do not need to compare sources against each other — just read the data and explain the change.</p>" + TREND_TABLE,
        ),
        worked(
            "Describe and explain",
            "Use the table to describe how the use of coal and of wind and solar changed between 2000 and 2020, and suggest reasons. (4 marks)",
            [
                "<b>Describe coal:</b> coal's share <b>fell</b> from 40% to 2% — most of the fall after 2010.",
                "<b>Describe wind and solar:</b> wind and solar <b>rose</b> from 0% to 30%, rising faster after 2010.",
                "<b>Reason 1:</b> coal produces a lot of <b>carbon dioxide</b> (and sulfur dioxide), so it has been phased out to reduce climate change and pollution.",
                "<b>Reason 2:</b> wind turbines and solar cells have become <b>cheaper and more efficient</b>, and produce no carbon dioxide while generating.",
            ],
        ),
        practice("Trends", [
            written("en-t9-q1", "Use the table above to describe how the use of gas changed from 2000 to 2020. (2)",
                    marks(["Gas <b>rose</b> from 35% in 2000 to 40% in 2010…",
                           "…then <b>fell slightly</b> to 38% in 2020 — roughly constant overall (figures needed)."]), lines=3),
            written("en-t9-q2", "Suggest two reasons why the use of renewable energy sources has increased in many countries. (2)",
                    marks(["The technology (wind turbines, solar cells) has become <b>cheaper</b> / more efficient.",
                           "Renewables produce <b>no carbon dioxide</b> while generating, so they help meet climate-change targets; fossil fuels are also <b>running out</b>."]), lines=3),
            choice("en-t9-q3", "A graph shows a country's total energy use rising steadily for 30 years. Which is a valid explanation?",
                   ["Energy is being created", "The population and the number of devices per person have increased", "Renewables are more efficient", "Fossil fuels are cheaper"], 1,
                   "More people using more technology means more energy transferred. The other options do not explain a rise in total use."),
            written("en-t9-q4", "Explain why gas power stations have often replaced coal power stations rather than being replaced by renewables straight away. (2)",
                    marks(["Gas produces <b>less carbon dioxide per unit of energy</b> than coal (it is \"cleaner\"), so it cuts emissions quickly.",
                           "Gas power stations are <b>reliable and can be started quickly</b> to meet demand when wind and solar are not generating."]), lines=3),
            written("en-t9-q5", "Describe the trend in nuclear power in the table above. (1)",
                    marks(["Nuclear <b>fell slowly</b> from 20% to 16% (a small, steady decrease)."]), lines=2),
        ]),
    ],
)
section_t9["subtopic"] = ["3"]

# ---------------------------------------------------------------------
# T10 · Multi-step energy chains
# ---------------------------------------------------------------------

q10_1_e = 2000 * 120
q10_1_u = 0.9 * q10_1_e
q10_2_e = 30 * G * 1.5
q10_2_p = q10_2_e / 1.2
q10_2_in = q10_2_p / 0.6
q10_3_ke = 0.5 * 1000 * 15 ** 2
q10_3_f = q10_3_ke / 25
q10_4 = 1.5e3 * 6 * 3600 / 0.2 / 1e6   # input = useful ÷ efficiency
q10_5_e = 60 * G * 0.4 * 50
q10_5_t = 2 * 60
q10_5_p = q10_5_e / q10_5_t

section_t10 = section(
    "energy-chains", "tricky", "Multi-step energy chains", "3.5, 3.11, 8.7, 8.13",
    equations=[r"E = P t \rightarrow \text{efficiency} \rightarrow \text{useful}", r"m g \Delta h \rightarrow P = E/t \rightarrow \text{input} = P/\text{eff}"],
    blurb="The 4- and 5-mark calculations chain three equations: energy from power and time, then efficiency, then where the useful energy goes — or GPE, then power, then input power from the efficiency. Write each step as its own EWAU.",
    checklist=[
        "Plan the chain before calculating: what do I know, what do I want, which equation joins them?",
        "Carry units through: $W \\times s = J$; $J \\div s = W$",
        "Estimate energies and powers in everyday situations to one significant figure",
    ],
    parts=[
        explain(
            "Planning a chain",
            "<p>Write down what you know and what you want, then find the equation on the list that contains the thing you want. If it also contains something you do not know, that is the step before. Three chains cover almost every question:</p>"
            "<table class='tbl'><tr><th>Chain</th><th>Steps</th></tr>"
            "<tr><td>Kettle</td><td>$E = P \\times t$ → useful $=$ efficiency $\\times E$ → (Topic 14) $\\Delta\\theta = E \\div (m c)$</td></tr>"
            "<tr><td>Motor lifting</td><td>$\\Delta GPE = m g \\Delta h$ → $P_{\\text{useful}} = E \\div t$ → $P_{\\text{in}} = P_{\\text{useful}} \\div$ efficiency</td></tr>"
            "<tr><td>Braking</td><td>$KE = \\tfrac{1}{2} m v^{2}$ → $F = KE \\div d$ (or $d = KE \\div F$)</td></tr></table>"
            "<p><b>Estimation.</b> \"Estimate\" means use sensible rounded values and give one or two significant figures. Values worth knowing: a person's mass about 70 kg; a flight of stairs about 3 m; a step 0.2 m; a kettle 2–3 kW; a car 1000–1500 kg at 13 m/s (30 mph); walking 1.5 m/s. A person climbing stairs in a few seconds has a power of a few hundred watts.</p>",
        ),
        worked(
            "A lift motor chain",
            "A lift motor is 60% efficient. It raises a 30 kg load through 1.5 m in 1.2 s. Calculate the electrical power supplied to the motor. ($g = 10$ N/kg)",
            [
                r"<b>Useful energy:</b> $\Delta GPE = m g \Delta h = 30 \times 10 \times 1.5 = 450$ J.",
                r"<b>Useful power:</b> $P = \dfrac{E}{t} = \dfrac{450}{1.2} = 375$ W.",
                r"<b>Input power:</b> efficiency $= \dfrac{\text{useful}}{\text{total}}$ so total $= \dfrac{375}{0.60} = 625$ W.",
                r"<b>Sense check:</b> input (625 W) is bigger than useful (375 W) ✓; the other 250 W heats the motor.",
            ],
        ),
        practice("Energy chains", [
            group("en-t10-q1", "A 2000 W kettle is 90% efficient and runs for 2 minutes.", [
                numeric("en-t10-q1a", "Calculate the energy supplied to the kettle.", q10_1_e, "J", "$E = P \\times t$ with t in seconds.",
                        ewau(r"E = P \times t", r"E = 2000 \times 120", "240\\,000", "J"), label="a"),
                numeric("en-t10-q1b", "Calculate the energy transferred to the thermal store of the water.", q10_1_u, "J", "useful = 0.9 × total.",
                        ewau(r"\text{useful} = \text{efficiency} \times \text{total}", r"\text{useful} = 0.90 \times 240\,000", "216\\,000", "J"), label="b"),
                written("en-t10-q1c", "State where the rest of the energy goes. (1)",
                        marks(["To the <b>thermal store of the kettle body and the surroundings</b> (by heating)."]), lines=2, label="c"),
            ]),
            group("en-t10-q2", "A 60% efficient motor raises a 30 kg load through 1.5 m in 1.2 s. ($g = 10$ N/kg)", [
                numeric("en-t10-q2a", "Calculate the useful energy transferred.", q10_2_e, "J", "m g Δh.",
                        ewau(r"\Delta GPE = m g \Delta h", r"\Delta GPE = 30 \times 10 \times 1.5", "450", "J"), label="a"),
                numeric("en-t10-q2b", "Calculate the useful power output.", q10_2_p, "W", "$E \\div t$.",
                        ewau(r"P = \dfrac{E}{t}", r"P = \dfrac{450}{1.2}", "375", "W"), label="b"),
                numeric("en-t10-q2c", "Calculate the electrical power supplied.", sf(q10_2_in, 3), "W", "total = useful ÷ 0.6.",
                        ewau(r"\text{total} = \dfrac{\text{useful}}{\text{efficiency}}", r"\text{total} = \dfrac{375}{0.60}", "625", "W"), label="c"),
            ]),
            group("en-t10-q3", "A 1000 kg car travelling at 15 m/s brakes to a stop in 25 m.", [
                numeric("en-t10-q3a", "Calculate the kinetic energy of the car.", q10_3_ke, "J", "½ $m v^2$.",
                        ewau(r"KE = \tfrac{1}{2} m v^{2}", r"KE = \tfrac{1}{2} \times 1000 \times 15^{2}", "112\\,500", "J"), label="a"),
                numeric("en-t10-q3b", "Calculate the average braking force.", q10_3_f, "N", "Work done by brakes = KE; $F = E \\div d$.",
                        ewau(r"E = F \times d", r"112\,500 = F \times 25 \;\Rightarrow\; F = \dfrac{112\,500}{25}", "4500", "N"), label="b"),
                written("en-t10-q3c", "Describe the energy transfer that takes place as the car brakes. (2)",
                        marks(["From the <b>kinetic store</b> of the car…", "…to the <b>thermal store</b> of the brakes and surroundings, by <b>friction</b> (work done by the braking force)."]), lines=3, label="c"),
            ]),
            numeric("en-t10-q4", "A 1.5 kW solar panel array produces full power for 6 hours a day. It is 20% efficient. Estimate the energy that falls on the panels in that time, in MJ.",
                    sf(q10_4, 3), "MJ", "Useful energy = $P \\times t$ (in seconds); input = useful ÷ 0.2.",
                    [r"Useful $= 1500 \times 6 \times 3600 = 3.24 \times 10^{7}$ J.", r"Input $= \dfrac{3.24 \times 10^{7}}{0.20} = 1.62 \times 10^{8}$ J $= 162$ MJ."]),
            numeric("en-t10-q5", "Estimate the average power of a 60 kg student who climbs 50 steps, each 0.40 m high, in 2 minutes. ($g = 10$ N/kg)",
                    q10_5_p, "W", "Energy = m g × total height; time in seconds.",
                    [r"Height $= 50 \times 0.40 = 20$ m; $E = 60 \times 10 \times 20 = 12\,000$ J.", r"$P = \dfrac{12\,000}{120} = 100$ W."]),
            choice("en-t10-q6", "Which is the best estimate of the kinetic energy of a running adult?",
                   ["3 J", "300 J", "3000 J", "300 000 J"], 2,
                   "About 70 kg at about 8 m/s: $\\tfrac{1}{2} \\times 70 \\times 64 \\approx 2000$–3000 J. Order of magnitude is what an estimate is for."),
        ]),
    ],
)
section_t10["subtopic"] = ["3", "8"]

# ---------------------------------------------------------------------
# T11 · Apply the seven steps
# ---------------------------------------------------------------------

section_t11 = section(
    "planning-energy", "tricky", "Apply the seven steps: energy practicals", "3 and 8 suggested practicals",
    equations=[r"\text{7 steps: variables, equation, change, measure, use, accuracy, repeat + mean}"],
    blurb="The seven-step recipe from Topic 1 applied to the two suggested practicals in these topics: conservation of energy on a ramp, and the power of a person. The mark schemes for both are levelled, so procedure details are what move an answer up a level.",
    checklist=[
        "Write a full method for investigating conservation of energy (GPE → KE) on a ramp",
        "Write a full method for measuring a person's power by step-ups or stairs",
        "Give the processing steps: the equations and the comparison or graph",
    ],
    parts=[
        explain(
            "The seven steps, applied here",
            "<p>From <a href='#key-concepts/planning-practical'>Topic 1, T6</a>: (1) the two variables; (2) the equation that links them; (3) what you change and how, what you keep the same; (4) what you measure, how, with what; (5) what you do with the results; (6) one accuracy detail; (7) repeat <b>and calculate a mean</b>.</p>"
            "<p>The June 2023 Paper 2 pulley-efficiency plan was marked in levels: Level 3 (5–6) needed <b>at least two methods of obtaining data from correct use of equipment and at least two processing steps</b>, in a coherent order. So the data-collection steps and the calculation steps each need to be explicit: <i>measure the height with a metre rule</i>; <i>calculate the GPE from m g Δh</i>.</p>"
            "<table class='tbl'><tr><th>Step</th><th>Conservation of energy: trolley down a ramp</th><th>Power of a person: step-ups</th></tr>"
            "<tr><td>1 Variables</td><td>height released from (change); speed at the bottom (measure)</td><td>number of step-ups in a fixed time or time for a fixed number (measure); power (calculate)</td></tr>"
            "<tr><td>2 Equation</td><td>$m g \\Delta h$ and $\\tfrac{1}{2} m v^{2}$</td><td>$E = m g \\Delta h$; $P = E \\div t$</td></tr>"
            "<tr><td>3 Change</td><td>release height, with a ruler; same trolley, same ramp</td><td>(compare people, or steps of different height)</td></tr>"
            "<tr><td>4 Measure</td><td>mass with a balance; height with a metre rule; speed with a <b>light gate</b> and card at the bottom</td><td>mass with scales; step height with a metre rule; time with a stopwatch; count the steps</td></tr>"
            "<tr><td>5 Use</td><td>calculate GPE and KE; compare them (KE a little less) or plot KE against GPE</td><td>energy = weight × total height; power = energy ÷ time</td></tr>"
            "<tr><td>6 Accuracy</td><td>release from rest at a marked point; measure the vertical height, not along the ramp</td><td>full step each time; start the stopwatch on the first step</td></tr>"
            "<tr><td>7 Repeat</td><td>repeat each height three times and average the speed</td><td>repeat and average the time</td></tr></table>",
        ),
        worked(
            "Conservation of energy on a ramp",
            "Describe how a student could investigate whether the kinetic energy of a trolley at the bottom of a ramp equals the gravitational potential energy it loses. (6 marks)",
            [
                "<b>Step 1 — variables.</b> I will change the <b>height</b> the trolley is released from and measure its <b>speed</b> at the bottom; the trolley and the ramp stay the same.",
                r"<b>Step 2 — equations.</b> GPE lost $= m g \Delta h$; KE gained $= \tfrac{1}{2} m v^{2}$.",
                "<b>Step 3 — change.</b> Release the trolley from rest at five different heights, measured with a <b>metre rule</b> held vertically (the vertical height, not the distance along the ramp).",
                "<b>Step 4 — measure.</b> Measure the trolley's <b>mass with a balance</b>. Measure its <b>speed at the bottom with a light gate</b>: a card of known length on the trolley cuts the beam and the data logger records the time, speed = card length ÷ time.",
                "<b>Step 5 — use the results.</b> For each height calculate the GPE lost and the KE gained and <b>compare them</b> (or plot KE against GPE: a straight line of gradient 1 means energy is conserved; below it, some is dissipated).",
                "<b>Step 6 — accuracy.</b> Release the trolley from rest from the same marked point each time, without pushing it.",
                "<b>Step 7 — repeat.</b> Repeat each height three times <b>and calculate a mean</b> speed.",
            ],
        ),
        practice("Planning", [
            written("en-t11-q1", "Describe how a student could measure the power of a person doing step-ups onto a box. Include the measurements, the equipment and the calculation. (6)",
                    mark_scheme([
                        ("Variables", "Measure the <b>time</b> for a fixed number of step-ups (or count step-ups in a fixed time); calculate the power."),
                        ("Equations", "$E = m g \\Delta h$ (weight × height); $P = E \\div t$."),
                        ("Change", "If comparing: different people, same box; or the same person with boxes of different height."),
                        ("Measure", "<b>Mass</b> with bathroom scales; <b>height of the box</b> with a metre rule; <b>time</b> with a stopwatch; <b>count</b> the step-ups."),
                        ("Use", "Total height = height × number of step-ups; energy = weight × total height; <b>power = energy ÷ time</b>."),
                        ("Accuracy", "Stand fully upright on the box each time (full height); start and stop the watch on the same signal."),
                        ("Repeat", "<b>Repeat and calculate a mean</b> time."),
                    ], total=6), lines=8, hint="Seven steps; any six score. Say what each instrument measures."),
            written("en-t11-q2", "A student has a pulley system, a 1 kg load, a newton meter and a metre rule. Describe how the student could find the efficiency of the pulley system. (6)",
                    mark_scheme([
                        ("Variables", "Measure the <b>work done on the load</b> and the <b>work done by the student</b>; calculate efficiency = work on load ÷ work by student."),
                        ("Equations", "Work = force × distance (for both); GPE gained by load = m g Δh."),
                        ("Data 1", "Find the <b>weight</b> of the load (newton meter, or m g) and the <b>height it rises</b> (metre rule) → work on load = weight × height."),
                        ("Data 2", "Read the <b>force on the newton meter</b> while pulling steadily and measure the <b>distance the newton meter moves</b> (metre rule) → work by student = force × distance."),
                        ("Use", "Efficiency = (weight × height) ÷ (force × distance); repeat with different loads and plot efficiency against load."),
                        ("Accuracy", "Pull steadily (constant speed) so the force reading is steady; pull vertically."),
                        ("Repeat", "<b>Repeat and calculate a mean</b> for each load."),
                    ], total=6, extra=["June 2023 Paper 2 Q9(b): Level 3 needs at least two ways of obtaining data from the equipment and at least two processing steps, in a logical order."]), lines=8),
        ]),
    ],
)
section_t11["subtopic"] = ["3", "8"]

SECTIONS = [section_t7, section_t8, section_t9, section_t10, section_t11]

# ---------------------------------------------------------------------
# Flashcards
# ---------------------------------------------------------------------

FACTS = [
    fact("Name the eight energy stores.", "Kinetic, gravitational potential, elastic potential, thermal, chemical, nuclear, electrostatic, magnetic.", "stores-pathways"),
    fact("Name the four pathways.", "Mechanically (a force does work), electrically (a current), by heating, by radiation (light, sound).", "stores-pathways"),
    fact("Is \"light energy\" a store?", "No. Light is a pathway (radiation). So are sound and electricity. Energy carried by light ends up in a thermal store.", "stores-pathways"),
    fact("The sentence for describing any energy change?", "Energy is transferred from the ___ store of ___ to the ___ store of ___, by ___ (mechanically / electrically / by heating / by radiation).", "stores-pathways"),
    fact("Law of conservation of energy?", "Energy cannot be created or destroyed; it can only be transferred from one store to another.", "conservation"),
    fact("What is a closed system?", "One where no energy enters or leaves, so the total energy stays the same.", "conservation"),
    fact("input, useful and wasted energy are related how?", "input = useful + wasted. Wasted energy is dissipated to the thermal store of the surroundings.", "conservation"),
    fact("In a Sankey diagram, what does arrow width show?", "The amount of energy (or power). Useful arrows carry straight on; wasted arrows bend away. Widths add up.", "sankey"),
    fact("Equation for change in GPE, with units?", "$\\Delta \\text{GPE} = m \\times g \\times \\Delta h$. J = kg × N/kg × m. Δh is the change in vertical height.", "gpe"),
    fact("Value of g on Earth?", "10 N/kg (also written 10 m/s²).", "gpe"),
    fact("A trolley is raised 26 cm. What goes into m g Δh?", "0.26 m. Convert centimetres to metres first — the most common error in the examiners' reports.", "gpe"),
    fact("Equation for kinetic energy, with units?", "$\\text{KE} = \\tfrac{1}{2} \\times m \\times v^2$. J = kg × (m/s)².", "ke"),
    fact("Calculator order for KE?", "Square the speed, multiply by the mass, halve it.", "ke"),
    fact("Speed doubles: KE?", "Four times bigger ($\\text{KE} \\propto v^2$). Trebles: nine times.", "ke"),
    fact("How to find v from KE?", "$v^2 = 2 \\times \\text{KE} \\div m$, then take the square root. Stopping at v² loses the last mark.", "ke"),
    fact("Equation for work done, with units?", "$E = F \\times d$. $J = N \\times m$. The distance moved in the direction of the force.", "work"),
    fact("What is 1 joule?", "The work done when a force of 1 N moves something 1 m: 1 J = 1 N m.", "work"),
    fact("Work done and energy transferred?", "They are the same thing: work done = energy transferred (mechanically).", "work"),
    fact("Carrying a bag horizontally at constant height: work against gravity?", "Zero — the bag does not move in the direction of the weight.", "work"),
    fact("How to measure the work done by a force?", "Read the force on a newton meter; measure the distance moved with a metre rule; multiply.", "work"),
    fact("Define power.", "The rate at which energy is transferred (or work is done): energy transferred per second.", "power-nn"),
    fact("Equation for power, with units?", "$P = E \\div t$ (or $W \\div t$). $W = J \\div s$.", "power-nn"),
    fact("What is 1 watt?", "1 joule per second.", "power-nn"),
    fact("Power of a person climbing stairs: which energy?", "$E = m g \\Delta h$ — use the weight ($m \\times g$), not the mass, then $P = E \\div t$.", "power-nn"),
    fact("2 kW, 3 MJ, 2 minutes, 1.5 hours in base units?", "2000 W; 3 000 000 J; 120 s; 5400 s.", "power-nn"),
    fact("Equation for efficiency?", "efficiency = useful energy out ÷ total energy in (or useful power ÷ total power). No unit; a decimal or a percentage.", "efficiency-nn"),
    fact("55% in the efficiency equation is…", "0.55. Never 55.", "efficiency-nn"),
    fact("Can efficiency be more than 1?", "No. Useful output can never exceed input (conservation of energy). An answer above 1 means a mistake.", "efficiency-nn"),
    fact("Total input from useful output and efficiency?", "total = useful ÷ efficiency. The input is always bigger than the useful output.", "efficiency-nn"),
    fact("Where does wasted energy end up?", "In the thermal store of the surroundings, spread out so it cannot be used — dissipated.", "dissipation"),
    fact("Why do mechanical processes become wasteful?", "Friction and air resistance do work and raise the temperature, dissipating energy by heating the surroundings.", "dissipation"),
    fact("Phrases that score nothing for wasted energy?", "\"Energy is lost\", \"used up\", \"not 100% efficient\", \"sound\" on its own. Name the store and the pathway instead.", "dissipation"),
    fact("How does lubrication reduce unwanted energy transfer?", "Oil reduces friction between moving surfaces, so less work is done against friction and less energy goes to the thermal store.", "insulation"),
    fact("How does thermal insulation reduce unwanted energy transfer?", "An insulator has low thermal conductivity, so it reduces the rate of energy transfer by heating to the surroundings.", "insulation"),
    fact("Two things that affect how fast a building cools?", "Wall thickness (thicker → slower) and thermal conductivity of the walls (lower → slower).", "insulation"),
    fact("What is thermal conductivity?", "How quickly energy is transferred through a material by heating. Metals high; air, foam, wool low.", "insulation"),
    fact("Where must the thermometer be in an insulation experiment?", "In the water (not the air), so the water's temperature is what is compared.", "insulation"),
    fact("Renewable energy source?", "One replaced as fast as it is used — will not run out: bio-fuel, wind, hydroelectricity, tides, the Sun.", "resources"),
    fact("Non-renewable energy source?", "One being used faster than it is replaced — will run out: fossil fuels (coal, oil, gas) and nuclear fuel.", "resources"),
    fact("How does a fossil-fuel power station work?", "Fuel burns → heats water to steam → steam turns a turbine → turbine turns a generator → electricity.", "resources"),
    fact("The seven sources named in the spec?", "Fossil fuels, nuclear fuel, bio-fuel, wind, hydroelectricity, the tides, the Sun.", "resources"),
    fact("Energy changes: object projected upwards?", "Kinetic store → gravitational potential store, mechanically (gravity does work); some to the thermal store of the air by air resistance.", "store-changes"),
    fact("Energy changes: moving object hits an obstacle?", "Kinetic store → thermal store of object and obstacle (and elastic store while deformed), mechanically; a little by sound.", "store-changes"),
    fact("Energy changes: object accelerated by a constant force?", "Chemical store of whatever provides the force → kinetic store of the object, mechanically (the force does work).", "store-changes"),
    fact("Energy changes: vehicle slowing down?", "Kinetic store → thermal store of brakes, tyres, road and surroundings, by friction (mechanically, then heating).", "store-changes"),
    fact("Energy changes: electric kettle boiling water?", "Electrically to the element, then by heating to the thermal store of the water; some to the kettle body and surroundings.", "store-changes"),
    fact("Speed of a falling object from its height (no air resistance)?", "$m g \\Delta h = \\tfrac{1}{2} m v^2$ → $v = \\sqrt{2 g \\Delta h}$. The mass cancels.", "gpe-ke"),
    fact("Why is the measured speed at the bottom of a ramp less than calculated?", "Friction and air resistance do work, transferring some energy to the thermal store of the surroundings.", "gpe-ke"),
    fact("A way to make the measured speed closer to the calculated one?", "A method: oil the axles, steepen the runway, streamline the trolley. \"Reduce friction\" alone is a reason, not a method.", "gpe-ke"),
    fact("Why is braking distance ∝ speed²?", "The brakes must do work equal to the KE ($F \\times d = \\tfrac{1}{2} m v^2$); with a constant force, $d \\propto v^2$.", "work-hard"),
    fact("Work done pushing a box up a ramp vs GPE gained?", "Work = push × distance along the ramp; $\\text{GPE} = m g$ × vertical height. The difference is dissipated by friction.", "work-hard"),
    fact("Work done vs moment of a force?", "Both are force × distance, but work uses the distance moved; a moment uses the perpendicular distance from the pivot. Different things.", "work-hard"),
    fact("Chain for the power of a motor lifting a load?", "$E = m g \\Delta h$ → $P = E \\div t$ → input power = P ÷ efficiency.", "power-hard"),
    fact("Measure your own power?", "Weight from mass on scales; height of stairs with a metre rule; time with a stopwatch; E = weight × height; $P = E \\div t$; repeat and average.", "power-hard"),
    fact("Two stages of 40% and 90% efficiency: overall?", "$0.40 \\times 0.90 = 0.36$ (36%). Multiply the decimals.", "efficiency-hard"),
    fact("How can efficiency be increased?", "Reduce the wasted transfer: lubricate (friction), insulate (heating), streamline (air resistance), LEDs instead of filament lamps.", "efficiency-hard"),
    fact("Area under a force–distance graph?", "The work done (energy transferred). Convert cm on the axis to m first.", "energy-graphs"),
    fact("Gradient of an energy–time graph?", "The power.", "energy-graphs"),
    fact("Graph of KE against v²?", "A straight line through the origin; gradient $= \\tfrac{1}{2} m$.", "energy-graphs"),
    fact("The four-part shape of a dissipation explanation?", "What is wasted → which store it goes to → by which pathway → the consequence.", "explain-dissipation"),
    fact("Why is a measured temperature rise less than calculated?", "Not all the energy supplied goes to the object; some is transferred by heating to the thermal store of the surroundings.", "explain-dissipation"),
    fact("Describe vs explain a trend?", "Describe: what the numbers do, quoting figures. Explain: the reasons (carbon dioxide, cost, running out, technology).", "resources-trends"),
    fact("Why has renewable use increased?", "Cheaper, more efficient technology; no carbon dioxide while generating; climate targets; fossil fuels running out.", "resources-trends"),
    fact("Estimates: person, stairs, kettle, car?", "70 kg; 3 m; 2–3 kW; 1000–1500 kg at 13 m/s (30 mph). A person climbing stairs: a few hundred watts.", "energy-chains"),
    fact("Level 3 in a 6-mark plan needs…", "At least two ways of getting data from correct use of equipment and at least two processing steps, in a logical order.", "planning-energy"),
]
