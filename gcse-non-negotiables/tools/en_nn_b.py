"""
en_nn_b.py — Topics 3 and 8 (Energy): the non-negotiables N7–N11.

N7  Power                          N10 Reducing unwanted transfers
N8  Efficiency                     N11 Energy resources
N9  Dissipation
"""

from revlib import (
    choice, ewau, explain, mark_scheme, marks, numeric, practice, section, sf,
    worked, written,
)

G = 10

# ---------------------------------------------------------------------
# N7 · Power
# ---------------------------------------------------------------------

q7_1 = 3000 / 20
q7_2 = 2000 * 60
q7_3 = 60 * G * 4 / 8
q7_4 = 126e6 / 17.5e3
q7_5 = 48 * G * 3.0 / 3.5

section_n7 = section(
    "power-nn", "nn", "Power: the rate of energy transfer", "8.12, 8.13, 8.14",
    equations=[r"P = \dfrac{E}{t}", r"P = \dfrac{W}{t}", r"1\ \text{W} = 1\ \text{J/s}"],
    blurb="Power is <b>how fast</b> energy is transferred — the energy transferred (or work done) each second. A more powerful motor does the same job in less time.",
    checklist=[
        "Define power as the rate at which energy is transferred (or work is done)",
        "State that 1 watt = 1 joule per second",
        "Select $P = E \\div t$ and use the time in seconds",
    ],
    parts=[
        explain(
            "Definition and equation",
            "<p><b>Power is the rate at which energy is transferred</b> (or the rate at which work is done). \"Rate\" means <i>per second</i>.</p>"
            "<p>$$P = \\dfrac{W}{t} \\qquad P = \\dfrac{E}{t}$$</p><p>power (W) = work done (J) ÷ time taken (s), or energy transferred (J) ÷ time taken (s).</p>"
            "<p><b>One watt is one joule per second</b>: $1\\ \\text{W} = 1\\ \\text{J/s}$. A 2000 W kettle transfers 2000 J to the water every second. A 60 kg student who climbs a 3 m flight of stairs in 3 s transfers $60 \\times 10 \\times 3 = 1800$ J in 3 s, a power of 600 W.</p>"
            "<p>Traps: the time must be in <b>seconds</b> (2 minutes is 120 s; 2 hours is 7200 s); kW means $\\times 1000$ and MJ means $\\times 10^{6}$. When a question gives a <b>mass</b> and asks for the power of someone climbing, the energy is $m g \\Delta h$ — the June 2025 report says \"a very common error was to use the given value of mass (48 kg) rather than weight\".</p>",
        ),
        worked(
            "Power of a motor",
            "A motor lifts a 20 kg load through 3.0 m in 12 s. Calculate the power of the motor. ($g = 10$ N/kg)",
            [r"<b>Energy transferred:</b> $\Delta GPE = m g \Delta h = 20 \times 10 \times 3.0 = 600$ J."]
            + ewau(r"P = \dfrac{E}{t}", r"P = \dfrac{600}{12}", "50", "W"),
        ),
        practice("Power", [
            numeric("en-n7-q1", "A kettle transfers 3000 J in 20 s. Calculate its power.",
                    q7_1, "W", "$P = E \\div t$.",
                    ewau(r"P = \dfrac{E}{t}", r"P = \dfrac{3000}{20}", "150", "W")),
            numeric("en-n7-q2", "A 2 kW heater runs for 1 minute. Calculate the energy transferred.",
                    q7_2, "J", "2 kW = 2000 W; 1 minute = 60 s.",
                    ewau(r"E = P \times t", r"E = 2000 \times 60", "120\\,000", "J")),
            numeric("en-n7-q3", "A 60 kg student runs up a flight of stairs 4 m high in 8 s. Calculate her power. ($g = 10$ N/kg)",
                    q7_3, "W", "Energy = m g Δh = weight × height, then divide by the time.",
                    [r"$E = m g \Delta h = 60 \times 10 \times 4 = 2400$ J."] + ewau(r"P = \dfrac{E}{t}", r"P = \dfrac{2400}{8}", "300", "W")),
            numeric("en-n7-q4", "A car battery stores 126 MJ. The charger supplies 17.5 kW. Calculate the time to charge it fully, in hours.",
                    q7_4 / 3600, "h", "$t = E \\div P$ gives seconds; divide by 3600 for hours.",
                    [r"$t = \dfrac{E}{P} = \dfrac{126 \times 10^{6}}{17.5 \times 10^{3}} = 7200$ s.", r"$7200 \div 3600 = 2.0$ h. (The 2023 scheme gave 7.2 — a time-conversion error — one mark of two.)"]),
            numeric("en-n7-q5", "A student of mass 48 kg climbs a flight of stairs 3.0 m high in 3.5 s. Calculate her power. Give your answer to 2 significant figures. ($g = 10$ N/kg)",
                    sf(q7_5, 2), "W", "Use her weight ($48 \\times 10 = 480$ N), not her mass, in the energy calculation.",
                    [r"$E = m g \Delta h = 48 \times 10 \times 3.0 = 1440$ J."] + ewau(r"P = \dfrac{E}{t}", r"P = \dfrac{1440}{3.5}", "411.4 = 410", "W (2 s.f.)")),
            choice("en-n7-q6", "What is meant by a power of 500 W?",
                   ["500 J of energy is stored", "500 J of energy is transferred every second", "500 N of force is applied", "The motor runs for 500 s"], 1,
                   "Power is the rate of energy transfer: watts are joules per second."),
            written("en-n7-q7", "Two cranes lift the same load to the same height. Crane A takes 20 s, crane B takes 10 s. Compare the work done and the power of the two cranes. (2)",
                    marks(["The <b>work done is the same</b> for both (same force × same distance).",
                           "Crane B has <b>twice the power</b>, because it transfers the same energy in half the time (power = work done ÷ time)."]),
                    lines=3),
        ]),
    ],
)
section_n7["subtopic"] = ["8"]

# ---------------------------------------------------------------------
# N8 · Efficiency
# ---------------------------------------------------------------------

q8_1 = 950 / 980
q8_2 = round(0.07 * 1300)
q8_3 = 1800 / 0.64
q8_4 = 3000 / 5000
q8_5 = 0.55

section_n8 = section(
    "efficiency-nn", "nn", "Efficiency", "3.11, 8.15",
    equations=[r"\text{efficiency} = \dfrac{\text{useful energy out}}{\text{total energy in}}", r"\text{efficiency} = \dfrac{\text{useful power out}}{\text{total power in}}"],
    blurb="Efficiency is the fraction of the energy supplied that ends up where you wanted it. It is a number between 0 and 1 (or 0% and 100%) — never more.",
    checklist=[
        "Select the efficiency equation and use useful over total",
        "Give efficiency as a decimal or a percentage (× 100), and use the decimal in calculations",
        "Check: efficiency can never be more than 1 (100%)",
    ],
    parts=[
        explain(
            "The equation and the percentage trap",
            "<p>$$\\text{efficiency} = \\dfrac{\\text{useful energy transferred}}{\\text{total energy supplied}}$$</p>"
            "<p>The same equation works with <b>power</b> instead of energy. The answer has <b>no unit</b>: it is a fraction (0.6) or a percentage (60%).</p>"
            "<p>The trap, straight from the examiners' reports: a 55% efficient oven is <b>0.55</b> in the equation, not 55. The June 2023 scheme gave \"0.91 or 0.9\" (7% turned into 0.07 and then the answer divided by 100 again — a power-of-ten slip) one mark of two, and the 2022 report says of the wrong answers \"the answer was sometimes smaller than the useful energy, which should have prompted a check.\"</p>"
            "<p>Rearrangements you will need:</p><ul>"
            "<li>useful out = efficiency × total in</li>"
            "<li><b>total in = useful out ÷ efficiency</b> — the input is always <i>bigger</i> than the useful output</li>"
            "<li>wasted = total in − useful out</li></ul>",
        ),
        worked(
            "Efficiency of a motor",
            "A motor is supplied with 980 J and gives a load 950 J of gravitational potential energy. Calculate the efficiency of the motor.",
            ewau(r"\text{efficiency} = \dfrac{\text{useful energy out}}{\text{total energy in}}", r"\text{efficiency} = \dfrac{950}{980}", "0.97", "(no unit) — or 97%"),
        ),
        practice("Efficiency", [
            numeric("en-n8-q1", "A motor is supplied with 980 J and transfers 950 J usefully. Calculate its efficiency as a decimal.",
                    sf(q8_1, 2), "", "Useful ÷ total.",
                    ewau(r"\text{efficiency} = \dfrac{\text{useful}}{\text{total}}", r"\text{efficiency} = \dfrac{950}{980}", "0.97", "no unit (97%)"), tolerance=0.02),
            numeric("en-n8-q2", "A radioisotope generator is 7% efficient and is supplied with 1300 J. Calculate the useful energy output.",
                    q8_2, "J", "7% = 0.07.",
                    ewau(r"\text{useful} = \text{efficiency} \times \text{total}", r"\text{useful} = 0.07 \times 1300", "91", "J")),
            numeric("en-n8-q3", "A pulley system is 64% efficient. It does 1800 J of useful work on a load. Calculate the total work put in.",
                    sf(q8_3, 2), "J", "total = useful ÷ efficiency; the input must come out bigger than 1800 J.",
                    ewau(r"\text{efficiency} = \dfrac{\text{useful}}{\text{total}}", r"0.64 = \dfrac{1800}{\text{total}} \;\Rightarrow\; \text{total} = \dfrac{1800}{0.64}", "2812.5 \\approx 2800", "J (2 s.f., as the data; the June 2023 2H scheme, Q9(a)(ii), accepts 2812.5)")),
            numeric("en-n8-q4", "A 5000 W engine delivers 3000 W of useful power. Calculate its efficiency as a percentage.",
                    q8_4 * 100, "%", "Useful power ÷ total power, × 100.",
                    ewau(r"\text{efficiency} = \dfrac{\text{useful power}}{\text{total power}}", r"\text{efficiency} = \dfrac{3000}{5000} = 0.6", "60", "%")),
            numeric("en-n8-q5", "An oven is 55% efficient. It transfers 660 kJ usefully to the food. Calculate the total energy supplied, in kJ.",
                    660 / q8_5, "kJ", "55% is 0.55 in the equation. Check the answer is bigger than 660 kJ.",
                    ewau(r"\text{total} = \dfrac{\text{useful}}{\text{efficiency}}", r"\text{total} = \dfrac{660}{0.55}", "1200", "kJ")),
            choice("en-n8-q6", "A student calculates the efficiency of a motor as 1.4. What should they conclude?",
                   ["The motor is very good", "They have made a mistake: efficiency cannot be more than 1", "The motor creates energy", "The units are wrong"], 1,
                   "Useful output can never exceed the input (conservation of energy), so efficiency is at most 1 (100%). Usually the useful and total values have been swapped."),
            written("en-n8-q7", "State what is meant by the efficiency of a device. (1)",
                    marks(["The <b>fraction</b> (or percentage) of the <b>energy supplied</b> that is <b>transferred usefully</b> — useful energy out ÷ total energy in."]), lines=2),
        ]),
    ],
)
section_n8["subtopic"] = ["3", "8"]

# ---------------------------------------------------------------------
# N9 · Dissipation
# ---------------------------------------------------------------------

section_n9 = section(
    "dissipation", "nn", "Dissipation: where the wasted energy goes", "3.7, 3.8, 8.10, 8.11",
    equations=[r"\text{wasted energy} \rightarrow \text{thermal store of the surroundings}"],
    blurb="In every transfer some energy ends up spread out in the surroundings as thermal energy, where it cannot be got back. That is <b>dissipation</b>, and it is why nothing is 100% efficient.",
    checklist=[
        "State that wasted energy is dissipated to the thermal store of the surroundings",
        "Explain why a mechanical process becomes wasteful when it raises the temperature",
        "Give the pathway (friction, air resistance, heating of wires) in an example",
    ],
    parts=[
        explain(
            "What dissipated means",
            "<p>When energy is transferred, some of it always goes somewhere you did not want. A motor gets warm; a sliding box heats the floor; a lamp's wires heat up. In every case the energy is <b>transferred by heating to the thermal store of the surroundings</b>. It spreads out among so many particles that it can never be gathered up and used again. That spreading is <b>dissipation</b>.</p>"
            "<p>The spec wording: <b>mechanical processes become wasteful when they cause a rise in temperature, dissipating energy by heating the surroundings.</b> Friction and air resistance are the usual causes — they do work, and the work done ends up as thermal energy.</p>"
            "<p>The mark schemes are strict about the wording. The June 2024 scheme (2H Q9(b)(ii)) <b>ignores</b> unqualified \"energy is lost / wasted\", \"not 100% efficient\" and arguments about sound; earlier schemes let \"lost\" through, so never rely on it. Say <b>which store</b> it goes to and <b>how</b>: <i>energy is transferred to the thermal store of the surroundings by friction</i>. \"Sound\" is usually ignored — it is tiny and ends up as thermal energy anyway.</p>",
        ),
        worked(
            "Explaining a wasteful transfer",
            "A ball is dropped and bounces, but each bounce is lower than the last. Explain, in terms of energy, why the ball does not return to its original height. (3 marks)",
            [
                "<b>The ball has less energy</b>: after the bounce its kinetic and gravitational stores hold <b>less</b> than before — that is the first mark (June 2019 2H Q2(b)(iv): \"(the ball) has lost energy (1)\"); the total is conserved, but the examiner is asking about the ball's share.",
                "<b>Where:</b> some of the ball's energy is transferred to the <b>thermal store of the ball and the floor</b> when it squashes and un-squashes, and to the <b>thermal store of the air</b> by air resistance.",
                "<b>So:</b> less energy is in the <b>kinetic store</b> after each bounce, so less can be transferred to the <b>gravitational store</b>, and the ball rises less. The energy has been <b>dissipated</b>.",
            ],
        ),
        practice("Dissipation", [
            written("en-n9-q1", "A toy car is given a push and rolls along the carpet until it stops. Describe the energy transfers as it slows and stops. (2)",
                    marks(["It has been transferred to the <b>thermal store</b> of the carpet, the wheels and the surroundings…",
                           "…by <b>friction</b> — work is done against friction and the energy is transferred by heating to the surroundings; it has been <b>dissipated</b>, not destroyed."]), lines=3),
            choice("en-n9-q2", "Which statement about a 40% efficient engine scores the mark?",
                   ["60% of the energy disappears", "60% of the energy is transferred to the thermal store of the surroundings", "60% of the energy is destroyed", "The engine makes 40% of its energy"], 1,
                   "Name the store the wasted energy goes to. \"Disappears\" and \"destroyed\" are wrong — energy is conserved — and a bare \"lost\" is ignored unless you say where to (the surroundings, as thermal energy)."),
            written("en-n9-q3", "Explain why a mechanical process such as a drill cutting wood is wasteful. (2)",
                    marks(["Friction between the drill and the wood <b>raises the temperature</b> of both.",
                           "Energy is <b>dissipated</b> — transferred by heating to the <b>thermal store of the surroundings</b> — so it is no longer useful."]), lines=3),
            written("en-n9-q4", "A student's experiment shows that a trolley rolling down a ramp arrives with less kinetic energy than the gravitational potential energy it lost. Give the reason. (1)",
                    marks(["Some energy is transferred to the <b>thermal store of the surroundings</b> (ramp, wheels, air) by <b>friction</b> and <b>air resistance</b>."]), lines=2,
                    hint="One store and one pathway. \"It was lost\" does not score."),
            choice("en-n9-q5", "An electric motor runs for an hour and becomes warm. Which pathway transfers energy to the surroundings?",
                   ["By radiation only", "By heating", "Electrically", "Mechanically, to the load"], 1,
                   "The warm motor transfers energy to the cooler air around it by heating — that is the dissipated part. The energy to the load is the useful part."),
        ]),
    ],
)
section_n9["subtopic"] = ["3", "8"]

# ---------------------------------------------------------------------
# N10 · Reducing unwanted transfers: lubrication, insulation, walls
# ---------------------------------------------------------------------

section_n10 = section(
    "insulation", "nn", "Reducing unwanted transfers: lubrication and insulation", "3.9, 3.10",
    equations=[r"\text{lubrication} \rightarrow \text{less friction}", r"\text{thick walls, low conductivity} \rightarrow \text{slower cooling}"],
    blurb="Unwanted transfers can be cut down but never removed. Lubrication deals with friction; thermal insulation deals with heating; a building cools more slowly through thicker walls of lower thermal conductivity.",
    checklist=[
        "Explain how lubrication reduces unwanted energy transfer",
        "Explain how thermal insulation reduces unwanted energy transfer",
        "Describe how wall thickness and thermal conductivity affect a building's rate of cooling",
    ],
    parts=[
        explain(
            "Three things to be able to say",
            "<p><b>Lubrication.</b> Oil or grease between two moving surfaces <b>reduces the friction</b> between them, so less work is done against friction and <b>less energy is transferred to the thermal store</b> of the surroundings. More of the input energy stays useful: the efficiency goes up.</p>"
            "<p><b>Thermal insulation.</b> An insulator is a material with a <b>low thermal conductivity</b> — energy is transferred through it by heating only slowly. Wrapping a hot object (or a house) in insulation reduces the <b>rate</b> at which energy is transferred to the surroundings. It does not stop it; it slows it.</p>"
            "<p><b>Walls of a building.</b> The rate at which a building cools depends on two things:</p><ul>"
            "<li><b>Thickness</b> of the walls — thicker walls, slower cooling (energy has further to travel).</li>"
            "<li><b>Thermal conductivity</b> of the material — the lower the conductivity, the slower the cooling. Brick with a cavity, or foam, conducts less than solid stone.</li></ul>"
            "<p>The spec word is <b>rate</b>: say \"reduces the rate of energy transfer\" or \"cools more slowly\", not \"keeps the heat in\".</p>",
            tone=None,
        ),
        explain(
            "Thermal conductivity",
            "<p><b>Thermal conductivity</b> is a property of a material: how quickly energy is transferred through it by heating when there is a temperature difference across it. Metals have high conductivity (a metal spoon in tea feels hot fast); air, foam, wool and fibreglass have low conductivity, which is why insulation is usually full of trapped air.</p>"
            "<p>A question may give a graph or table of conductivity against something else (density, say) and ask you to <b>describe</b> it. The June 2022 report: \"the change in the graph has to be described — is it non-linear, gradient decreases or levels off\". Numbers at two points are not a description of a trend.</p>",
        ),
        worked(
            "Why insulation works",
            "Explain how wrapping a hot water tank in a foam jacket reduces the energy transferred to the surroundings. (2 marks)",
            [
                "<b>Property:</b> The foam has a <b>low thermal conductivity</b> (it contains trapped air, which is a poor conductor).",
                "<b>Effect:</b> So the <b>rate</b> at which energy is transferred by heating from the hot water to the surroundings is <b>reduced</b> — the water stays hot for longer and less energy is wasted.",
            ],
        ),
        practice("Lubrication and insulation", [
            written("en-n10-q1", "Explain how oiling the axle of a bicycle wheel reduces the energy wasted. (2)",
                    marks(["The oil <b>reduces the friction</b> between the axle and the wheel.",
                           "So less work is done against friction and <b>less energy is transferred to the thermal store</b> of the surroundings; more of the cyclist's energy stays in the kinetic store."]), lines=3),
            written("en-n10-q2", "Describe how the thickness of the walls of a house affects its rate of cooling. (1)",
                    marks(["The <b>thicker</b> the walls, the <b>slower</b> the rate of cooling (the lower the rate of energy transfer to the outside)."]), lines=2),
            written("en-n10-q3", "Two houses have walls of the same thickness. One is built of stone, the other of a material with a lower thermal conductivity. Explain which house cools more slowly. (2)",
                    marks(["The house with the <b>lower thermal conductivity</b> walls cools more slowly…",
                           "…because energy is transferred through its walls by heating at a <b>lower rate</b>."]), lines=3),
            choice("en-n10-q4", "Why does a wool jumper keep you warm?",
                   ["Wool is a good conductor", "Wool produces heat", "Wool and the air trapped in it have a low thermal conductivity, so energy is transferred from your body more slowly", "Wool reflects light"], 2,
                   "Insulators do not make heat. They reduce the rate of energy transfer from you to the surroundings."),
            written("en-n10-q5", "A student investigates which of three materials is the best insulator by wrapping each round a beaker of hot water. State two variables that must be kept the same, and where the thermometer must be. (3)",
                    mark_scheme([
                        ("Control 1", "Same <b>volume (mass) of water</b> in each beaker."),
                        ("Control 2", "Same <b>starting temperature</b> of the water (or same <b>thickness</b> of insulation; same <b>time interval</b> between readings or same <b>temperature change</b> — June 2022 1H Q2(b)(ii): \"unqualified 'same time' is insufficient\")."),
                        ("Thermometer", "<b>In the water</b> — so the temperature of the water, not the air, is measured (the June 2022 scheme, Q2(b)(i), gave a separate mark for \"thermometer in the water\"; a thermometer drawn in the air lost it)."),
                    ]), lines=4),
            choice("en-n10-q6", "A graph of thermal conductivity against density for a foam curves downwards and then levels off. Which is the description the examiner wants?",
                   ["Conductivity goes down", "Conductivity is 0.04 at 20 kg/m³ and 0.03 at 40 kg/m³", "Conductivity decreases as density increases, but the decrease gets smaller and the graph levels off (non-linear)", "Conductivity is inversely proportional to density"], 2,
                   "Describe the shape of the change: decreasing, non-linear, levelling off. Quoting two points is not a description (\"unqualified quoted values are insufficient\"), and \"negative correlation\" is ignored. \"Inversely proportional\" was allowed for the non-linear mark in 2022, but it does not state the direction of change — write both: <i>decreases as density increases, and non-linear / levels off</i>."),
        ]),
    ],
)
section_n10["subtopic"] = ["3"]

# ---------------------------------------------------------------------
# N11 · Energy resources
# ---------------------------------------------------------------------

RESOURCES_TABLE = (
    "<table class='tbl'><tr><th>Source</th><th>Renewable?</th><th>How it is used</th><th>One point for, one against</th></tr>"
    "<tr><td><b>Fossil fuels</b> (coal, oil, gas)</td><td>No</td><td>Burned to heat water → steam → turbine → generator; transport fuel; heating</td><td>reliable, available on demand / carbon dioxide (climate change), will run out</td></tr>"
    "<tr><td><b>Nuclear fuel</b> (uranium)</td><td>No</td><td>Fission heats water → steam → turbine → generator</td><td>no carbon dioxide, huge energy per kg / radioactive waste, expensive to build and decommission</td></tr>"
    "<tr><td><b>Bio-fuel</b> (wood, crops, waste)</td><td>Yes</td><td>Burned like a fossil fuel, or made into liquid fuel</td><td>carbon-neutral if regrown / land needed for growing it</td></tr>"
    "<tr><td><b>Wind</b></td><td>Yes</td><td>Wind turns turbine blades connected to a generator</td><td>no fuel, no carbon dioxide / unreliable (no wind, no power), visual impact</td></tr>"
    "<tr><td><b>Hydroelectricity</b></td><td>Yes</td><td>Water from a dam falls through turbines</td><td>reliable, quick to start / floods valleys, few suitable sites</td></tr>"
    "<tr><td><b>Tides</b></td><td>Yes</td><td>Tidal water flows through turbines in a barrage</td><td>predictable / few sites, disturbs habitats</td></tr>"
    "<tr><td><b>The Sun</b> (solar)</td><td>Yes</td><td>Solar cells make electricity; solar panels heat water</td><td>no fuel, works anywhere sunny / nothing at night, weather-dependent</td></tr></table>"
)

section_n11 = section(
    "resources", "nn", "Energy resources", "3.13",
    equations=[r"\text{renewable: will not run out}", r"\text{non-renewable: will run out}"],
    blurb="The seven energy sources named in the spec, whether each is renewable, and how each is used. You need the facts and the ways each is used; comparing sources on cost or reliability is not on the spec — the one 6-mark \"discuss the arguments for and against\" set (nuclear power, Nov 2020 1H Q8(c)) is on the Topic 6 page, and its scheme wanted each point with its consequence: <i>no carbon emissions <b>so</b> does not contribute to global warming</i>.",
    checklist=[
        "State what renewable and non-renewable mean",
        "Name the seven sources on the spec and say which are renewable",
        "Describe how each source is used to generate electricity or for heating / transport",
    ],
    parts=[
        explain(
            "The seven sources",
            "<p>A <b>renewable</b> energy source is one that is <b>replaced as fast as it is used</b>, so it will not run out. A <b>non-renewable</b> source is being used faster than it forms, so one day it will run out.</p>" + RESOURCES_TABLE +
            "<p>Most power stations work the same way: <b>something heats water → steam → spins a turbine → turns a generator</b>. Wind, hydro and tidal skip the steam and turn the turbine directly. Solar cells skip the turbine altogether.</p>",
        ),
        worked(
            "Describing how a source is used",
            "Describe how a fossil fuel is used to generate electricity. (3 marks)",
            [
                "<b>Burn:</b> the fuel (coal, oil or gas) is <b>burned</b>, transferring energy from its chemical store by heating…",
                "<b>Steam:</b> …to <b>heat water into steam</b>…",
                "<b>Turbine and generator:</b> …which <b>turns a turbine</b> connected to a <b>generator</b>, which produces electricity (energy transferred electrically).",
            ],
        ),
        practice("Energy resources", [
            choice("en-n11-q1", "Which of these is a non-renewable energy source?",
                   ["Wind", "Bio-fuel", "Nuclear fuel", "The tides"], 2,
                   "Uranium is not replaced as it is used. Bio-fuel is renewable because the crops can be regrown."),
            written("en-n11-q2", "State what is meant by a renewable energy source. (1)",
                    marks(["A source that is <b>replaced as fast as it is used</b> (will not run out)."]), lines=2),
            written("en-n11-q3", "Describe how a wind turbine generates electricity. (2)",
                    marks(["The wind <b>turns the blades</b> (energy transferred mechanically from the kinetic store of the air).",
                           "The blades turn a <b>generator</b>, which transfers energy electrically."]), lines=3),
            choice("en-n11-q4", "Which source is renewable AND predictable (available at known times)?",
                   ["Wind", "Tides", "Solar", "Gas"], 1,
                   "Tides happen twice a day at times known years in advance. Wind and solar depend on the weather; gas is non-renewable."),
            written("en-n11-q5", "Give one advantage and one disadvantage of using nuclear fuel to generate electricity. (2)",
                    marks(["Advantage: <b>no carbon dioxide</b> emitted during generation (<b>so</b> does not contribute to global warming) / <b>large power output</b> compared with wind or solar / <b>low running costs</b> / reliable.",
                           "Disadvantage: produces <b>radioactive waste</b> that must be stored for a very long time / expensive to build and decommission / a nuclear accident is possible, <b>so</b> loss of life or contamination of an area (Nov 2020 1H Q8(c): each point with its consequence)."]), lines=3),
            written("en-n11-q6", "Describe how a hydroelectric power station generates electricity. (2)",
                    marks(["Water stored behind a <b>dam</b> (gravitational potential store) <b>falls</b> through pipes…",
                           "…and <b>turns a turbine</b> connected to a <b>generator</b>."]), lines=3),
        ]),
    ],
)
section_n11["subtopic"] = ["3"]

SECTIONS = [section_n7, section_n8, section_n9, section_n10, section_n11]
