"""
kc_nn.py — Topic 1 Key concepts: the non-negotiables, N1–N9.

SI units; prefixes; converting; significant figures; standard form; the
equation sheet; rearranging; percentages, ratios and proportion; EWAU.
Edexcel GCSE Physics 1PH0 spec points 1.1–1.4 plus the maths skills the
whole course leans on.
"""

from revlib import (
    choice, diagram, explain, ewau, group, marks, numeric, practice, section,
    sf, types, worked, written,
)

G = 10

# =====================================================================
# N1 · SI units (1.1)
# =====================================================================

q1_4 = 2.5 * 1000
q1_5 = 45 / 1000

section_n1 = section(
    "si-units", "nn", "SI units and the quantities they measure", "1.1",
    equations=[r"\text{metre, m}", r"\text{kilogram, kg}", r"\text{second, s}", r"\text{ampere, A}", r"\text{kelvin, K}"],
    blurb="Every quantity in physics has one standard unit. Exam answers need the right one every time: a number without a unit, or with the wrong one, loses the mark.",
    checklist=[
        "Give the SI unit for every quantity met at GCSE",
        "Tell a base unit (m, kg, s, A, K, mol) from a derived unit (N, J, W …)",
        "Write a unit with the correct symbol and capital letters (N not n, Hz not hz)",
    ],
    parts=[
        explain(
            "The units you must know",
            "<p><b>SI units</b> are the standard set of units that all scientists use. The equations on the Edexcel sheet only work when every quantity is in its SI unit — that is why so much of physics is converting first.</p>"
            "<table class='tbl'><tr><th>Quantity</th><th>SI unit</th><th>Symbol</th><th>Notes</th></tr>"
            "<tr><td>length, distance, displacement</td><td>metre</td><td>m</td><td>base unit</td></tr>"
            "<tr><td>mass</td><td>kilogram</td><td>kg</td><td>base unit — not the gram</td></tr>"
            "<tr><td>time</td><td>second</td><td>s</td><td>base unit</td></tr>"
            "<tr><td>current</td><td>ampere (amp)</td><td>A</td><td>base unit</td></tr>"
            "<tr><td>temperature</td><td>kelvin</td><td>K</td><td>base unit; °C is accepted where the question uses it</td></tr>"
            "<tr><td>force, weight</td><td>newton</td><td>N</td><td>$1\\ \\text{N} = 1\\ \\text{kg m/s}^2$</td></tr>"
            "<tr><td>energy, work done</td><td>joule</td><td>J</td><td>$1\\ \\text{J} = 1\\ \\text{N m}$</td></tr>"
            "<tr><td>power</td><td>watt</td><td>W</td><td>$1\\ \\text{W} = 1\\ \\text{J/s}$</td></tr>"
            "<tr><td>pressure</td><td>pascal</td><td>Pa</td><td>$1\\ \\text{Pa} = 1\\ \\text{N/m}^2$</td></tr>"
            "<tr><td>frequency</td><td>hertz</td><td>Hz</td><td>$1\\ \\text{Hz} = 1$ per second</td></tr>"
            "<tr><td>potential difference</td><td>volt</td><td>V</td><td>$1\\ \\text{V} = 1\\ \\text{J/C}$</td></tr>"
            "<tr><td>resistance</td><td>ohm</td><td>Ω</td><td></td></tr>"
            "<tr><td>charge</td><td>coulomb</td><td>C</td><td>$1\\ \\text{C} = 1\\ \\text{A s}$</td></tr>"
            "<tr><td>speed, velocity</td><td>metre per second</td><td>m/s</td><td></td></tr>"
            "<tr><td>acceleration</td><td>metre per second squared</td><td>m/s²</td><td></td></tr>"
            "<tr><td>density</td><td>kilogram per cubic metre</td><td>kg/m³</td><td></td></tr>"
            "<tr><td>momentum</td><td>kilogram metre per second</td><td>kg m/s</td><td></td></tr>"
            "<tr><td>specific heat capacity</td><td>joule per kilogram per degree</td><td>J/kg °C</td><td></td></tr>"
            "<tr><td>gravitational field strength</td><td>newton per kilogram</td><td>N/kg</td><td>same size as m/s²</td></tr></table>"
            "<p><b>Base</b> units are the seven the system is built from (you meet six: m, kg, s, A, K and the mole). Every other unit is <b>derived</b> — built by multiplying or dividing base units, which is why $\\text{m/s}$ is \"metres divided by seconds\".</p>",
        ),
        explain(
            "Capitals and symbols",
            "<p>A unit named after a person gets a <b>capital symbol</b> but a lower-case name: newton, N; joule, J; watt, W; hertz, Hz; pascal, Pa. Units not named after people are lower case: m, kg, s. "
            "Writing <i>n</i> for newtons or <i>hz</i> for hertz is marked wrong. The exception is the litre, L, which is capitalised to avoid confusion with 1.</p>"
            "<p>Write compound units with a slash, as the exam papers do: $\\text{m/s}$, $\\text{kg/m}^3$, $\\text{J/kg °C}$.</p>",
            tone="warn",
        ),
        worked(
            "Choosing the unit from the equation",
            "A student calculates $P = I \\times V = 2 \\times 12$. State the answer with its unit, and explain how the unit can be checked from the equation.",
            [
                r"$P = 2 \times 12 = 24$. Power is measured in <b>watts</b>, so $P = 24$ W.",
                r"Check from the equation: current in amps × potential difference in volts gives $\text{A} \times \text{V}$, and $1\ \text{A V} = 1\ \text{W}$. The unit of the answer follows from the units going in.",
                r"If the current had been in milliamps the answer would have come out in milliwatts — which is why everything is converted to SI units <i>before</i> substituting.",
            ],
        ),
        types(["si-conversions"], "Calculation: converting to SI units"),
        practice("SI units", [
            choice("kc-n1-q1", "What is the SI unit of mass?", ["gram", "kilogram", "newton", "tonne"], 1,
                   "The kilogram is the base unit of mass. Newtons measure weight (a force); grams and tonnes have to be converted."),
            choice("kc-n1-q2", "Which of these is a <b>base</b> unit?", ["newton", "joule", "second", "watt"], 2,
                   "The second is one of the base units. Newtons, joules and watts are derived from base units (a newton is a kg m/s²)."),
            choice("kc-n1-q3", "A student writes an answer as \"50 hz\". What is wrong with it?",
                   ["Nothing", "Frequency is measured in watts", "The symbol should be Hz, with a capital H", "Frequency has no unit"], 2,
                   "Hertz is named after Heinrich Hertz, so its symbol takes a capital letter: Hz. The name stays lower case."),
            numeric("kc-n1-q4", "A rope is 2.5 km long. Give its length in the SI unit.", q1_4, "m",
                    "The SI unit of length is the metre; 1 km = 1000 m.",
                    [r"$2.5 \times 1000 = 2500$ m."]),
            numeric("kc-n1-q5", "A battery supplies a current of 45 mA. Give the current in the SI unit.", q1_5, "A",
                    "The SI unit of current is the ampere; 1 mA = 0.001 A.",
                    [r"$45 \div 1000 = 0.045$ A."]),
            written("kc-n1-q6", "A student measures a pressure and writes the unit as N/m². Another student writes Pa. Explain why both are correct.",
                    marks(["Pressure = force ÷ area, so its unit is newtons per square metre, N/m².",
                           "The pascal is defined as 1 N/m² — it is the same unit with a special name.",
                           "Either is accepted; Pa is the SI name."]), lines=3),
        ]),
    ],
)


# =====================================================================
# N2 · Prefixes (1.2)
# =====================================================================

q2_2 = 2.5e6
q2_4 = 500e-9

section_n2 = section(
    "prefixes-nn", "nn", "Prefixes: giga to nano", "1.2",
    equations=[r"\text{G} = 10^{9}", r"\text{M} = 10^{6}", r"\text{k} = 10^{3}", r"\text{c} = 10^{-2}", r"\text{m} = 10^{-3}", r"\mu = 10^{-6}", r"\text{n} = 10^{-9}"],
    blurb="A prefix in front of a unit is a multiplier. Strip it off and apply the multiplier before any equation sees the number.",
    checklist=[
        "Recall what G, M, k, c, m, μ and n multiply by",
        "Convert a value with a prefix into the base unit, and back again",
        "Spot a prefix hidden in a question (a 2 kW kettle, a 250 nm wavelength)",
    ],
    parts=[
        explain(
            "The seven prefixes",
            "<table class='tbl'><tr><th>Prefix</th><th>Symbol</th><th>Multiply by</th><th>In words</th><th>Example</th></tr>"
            "<tr><td>giga</td><td>G</td><td>$10^{9}$ = 1 000 000 000</td><td>a thousand million</td><td>a 2 GW power station</td></tr>"
            "<tr><td>mega</td><td>M</td><td>$10^{6}$ = 1 000 000</td><td>a million</td><td>a 3 MJ meal</td></tr>"
            "<tr><td>kilo</td><td>k</td><td>$10^{3}$ = 1000</td><td>a thousand</td><td>a 2 kW kettle</td></tr>"
            "<tr><td>centi</td><td>c</td><td>$10^{-2}$ = 0.01</td><td>a hundredth</td><td>30 cm ruler</td></tr>"
            "<tr><td>milli</td><td>m</td><td>$10^{-3}$ = 0.001</td><td>a thousandth</td><td>a 20 mA current</td></tr>"
            "<tr><td>micro</td><td>μ</td><td>$10^{-6}$ = 0.000 001</td><td>a millionth</td><td>a 50 μs pulse</td></tr>"
            "<tr><td>nano</td><td>n</td><td>$10^{-9}$ = 0.000 000 001</td><td>a thousand-millionth</td><td>500 nm light</td></tr></table>"
            "<p>Each step down the table from giga to kilo, and from milli to nano, is a factor of 1000. Centi is the odd one out (a factor of 100) and only really appears with metres.</p>"
            "<p><b>Into the base unit:</b> multiply by the prefix's value. $2.5\\ \\text{kW} = 2.5 \\times 1000 = 2500$ W. "
            "<b>Out of the base unit:</b> divide. $0.004\\ \\text{A} = 0.004 \\div 0.001 = 4$ mA.</p>",
        ),
        explain(
            "m means two things",
            "<p>Lower-case m is both the <i>metre</i> and the prefix <i>milli</i>. Read $\\text{mm}$ as \"milli-metre\" and $\\text{ms}$ as \"milli-second\" — the prefix always comes first. And capital M (mega) is a million times bigger than small m (milli): $1\\ \\text{MW}$ is a million watts, $1\\ \\text{mW}$ is a thousandth of one.</p>",
            tone="warn",
        ),
        worked(
            "Stripping a prefix",
            "A laser emits light of wavelength 650 nm. Write the wavelength in metres.",
            [
                r"nano means $\times 10^{-9}$, so $650\ \text{nm} = 650 \times 10^{-9}$ m.",
                r"$650 \times 10^{-9} = 6.5 \times 10^{-7}$ m (or 0.000 000 65 m).",
                r"Keep it in standard form: it goes straight into $v = f \times \lambda$ without a counting-the-zeros mistake.",
            ],
        ),
        types(["prefixes"], "Calculation: using prefixes"),
        practice("Prefixes", [
            choice("kc-n2-q1", "What does the prefix <b>mega</b> mean?", ["× 1000", "× 1 000 000", "× 1 000 000 000", "÷ 1 000 000"], 1,
                   "Mega (M) means a million, 10⁶. Kilo is a thousand, giga a thousand million."),
            numeric("kc-n2-q2", "A power station has an output of 2.5 MW. Give this in watts.", q2_2, "W",
                    "Mega = × 1 000 000.",
                    [r"$2.5 \times 1\,000\,000 = 2\,500\,000$ W, or $2.5 \times 10^{6}$ W."]),
            choice("kc-n2-q3", "Which is the largest current?", ["250 μA", "25 mA", "0.02 A", "2500 nA"], 1,
                   "Convert all to amps: $250 \\muA = 0.000 25$ A; 25 mA = 0.025 A; 0.02 A; 2500 nA = 0.000 0025 A. 25 mA is largest."),
            numeric("kc-n2-q4", "Write 500 nm in metres.", q2_4, "m",
                    "Nano = × 10⁻⁹.",
                    [r"$500 \times 10^{-9} = 5 \times 10^{-7}$ m. Type it as 5e-7."]),
            choice("kc-n2-q5", "A kettle is labelled 3 kW. How many watts is that?", ["0.003 W", "30 W", "300 W", "3000 W"], 3,
                   "Kilo = × 1000, so 3 kW = 3000 W."),
            written("kc-n2-q6", "Explain the difference between 5 mW and 5 MW.",
                    marks(["m (milli) means a thousandth: 5 mW = 0.005 W.",
                           "M (mega) means a million: 5 MW = 5 000 000 W.",
                           "They differ by a factor of a thousand million (10⁹)."]), lines=2),
        ]),
    ],
)


# =====================================================================
# N3 · Converting units (1.3)
# =====================================================================

q3_1 = 90 * 60
q3_2 = 0.5 * 1000 * 1000
q3_3 = 2.5 * 24 * 3600
q3_4 = 54 / 3.6
q3_5 = 1.5 * 3_600_000

section_n3 = section(
    "converting", "nn", "Converting between units", "1.3",
    equations=[r"1\ \text{h} = 3600\ \text{s}", r"1\ \text{km/h} = \dfrac{1000}{3600}\ \text{m/s}", r"1\ \text{kWh} = 3.6 \times 10^{6}\ \text{J}"],
    blurb="Minutes and hours into seconds, kilometres into metres, cubic centimetres into cubic metres. Convert first; the equation comes second.",
    checklist=[
        "Convert minutes, hours and days into seconds",
        "Convert km/h into m/s (and back)",
        "Convert areas and volumes, remembering to square or cube the length conversion",
        "Convert kWh into joules",
    ],
    parts=[
        explain(
            "The conversions that come up",
            "<table class='tbl'><tr><th>From</th><th>To</th><th>Do this</th><th>Example</th></tr>"
            "<tr><td>minutes</td><td>seconds</td><td>× 60</td><td>4 min = 240 s</td></tr>"
            "<tr><td>hours</td><td>seconds</td><td>× 3600</td><td>2 h = 7200 s</td></tr>"
            "<tr><td>days</td><td>seconds</td><td>× $24 \\times 3600 = \\times 86\\,400$</td><td>1 day = 86 400 s</td></tr>"
            "<tr><td>km</td><td>m</td><td>× 1000</td><td>1.2 km = 1200 m</td></tr>"
            "<tr><td>cm</td><td>m</td><td>÷ 100</td><td>35 cm = 0.35 m</td></tr>"
            "<tr><td>g</td><td>kg</td><td>÷ 1000</td><td>250 g = 0.25 kg</td></tr>"
            "<tr><td>km/h</td><td>m/s</td><td>÷ 3.6 (× 1000 ÷ 3600)</td><td>72 km/$h = 20$ m/s</td></tr>"
            "<tr><td>cm²</td><td>m²</td><td>÷ 10 000</td><td>50 cm² = 0.005 m²</td></tr>"
            "<tr><td>cm³</td><td>m³</td><td>÷ 1 000 000</td><td>250 cm³ = 0.000 25 m³</td></tr>"
            "<tr><td>g/cm³</td><td>kg/m³</td><td>× 1000</td><td>2.7 g/cm³ = 2700 kg/m³</td></tr>"
            "<tr><td>kWh</td><td>J</td><td>× 3 600 000</td><td>2 kWh = 7.2 × 10⁶ J</td></tr></table>"
            "<p><b>Areas and volumes:</b> if 1 m = 100 cm, then 1 $m^2 = 100 \\times 100 = 10\\,000$ cm² and 1 $m^3 = 100 \\times 100 \\times 100 = 1\\,000\\,000$ cm³. Square or cube the length factor — the most common slip in Topic 14 density questions.</p>"
            "<p><b>Sense check:</b> converting to a <i>bigger</i> unit gives a <i>smaller</i> number (3500 m = 3.5 km). If the number gets bigger when the unit gets bigger, the conversion went the wrong way.</p>",
        ),
        worked(
            "km/h to m/s",
            "A car travels at 108 km/h. Convert this speed to m/s.",
            [
                r"Convert the distance: $108\ \text{km} = 108 \times 1000 = 108\,000$ m.",
                r"Convert the time: $1\ \text{h} = 60 \times 60 = 3600$ s.",
                r"$\text{speed} = \dfrac{108\,000}{3600} = 30$ m/s.",
                r"Shortcut: $108 \div 3.6 = 30$ m/s. ✓",
            ],
        ),
        types(["compound-units"], "Calculation: compound units"),
        practice("Converting", [
            numeric("kc-n3-q1", "A film lasts 90 minutes. How many seconds is that?", q3_1, "s",
                    "× 60.", [r"$90 \times 60 = 5400$ s."]),
            numeric("kc-n3-q2", "A tank holds 0.5 m³ of water. Give the volume in cm³.", q3_2, "cm³",
                    "1 $m^3 = 1\\,000\\,000$ cm³ (100 cubed).",
                    [r"$0.5 \times 1\,000\,000 = 500\,000$ cm³."]),
            numeric("kc-n3-q3", "A satellite takes 2.5 days to complete an orbit. Give this time in seconds.", q3_3, "s",
                    "Days → hours → seconds: × 24 × 3600.",
                    [r"$2.5 \times 24 = 60$ hours. $60 \times 3600 = 216\,000$ s."]),
            numeric("kc-n3-q4", "A cyclist's speed is 54 km/h. Convert this to m/s.", q3_4, "m/s",
                    "Divide by 3.6.",
                    [r"$54 \times 1000 = 54\,000$ m per $3600$ s.", r"$\dfrac{54\,000}{3600} = 15$ m/s."]),
            numeric("kc-n3-q5", "An electric heater uses 1.5 kWh of energy. Give this in joules.", q3_5, "J",
                    "1 kWh = 1000 W × 3600 s = 3 600 000 J.",
                    [r"$1.5 \times 3\,600\,000 = 5\,400\,000$ J, or $5.4 \times 10^{6}$ J."]),
            choice("kc-n3-q6", "A student converts 20 cm² to m² and gets 0.2 m². What has gone wrong?",
                   ["Nothing, it is correct", "They divided by 100 instead of 10 000", "They should have multiplied by 100", "cm² cannot be converted to m²"], 1,
                   "1 $m^2 = 100$ cm × 100 cm = 10 000 cm², so 20 cm² = $20 \\div 10\\,000 = 0.002$ m². Dividing by 100 only converts a length."),
        ]),
    ],
)


# =====================================================================
# N4 · Significant figures and rounding (1.4)
# =====================================================================

section_n4 = section(
    "sig-figs", "nn", "Significant figures and rounding", "1.4",
    blurb="Give an answer to a sensible number of significant figures, round only at the end, and never give more figures than the data had.",
    checklist=[
        "Count the significant figures in a number (including ones with leading zeros)",
        "Round an answer to a stated number of significant figures",
        "Choose a sensible number of significant figures when the question does not say",
        "Keep full precision in the working and round only the final answer",
    ],
    parts=[
        explain(
            "Counting and rounding",
            "<p><b>Significant figures</b> (s.f.) are the digits that carry information. Counting them:</p>"
            "<ul><li>All non-zero digits are significant: 3.52 has 3 s.f.</li>"
            "<li>Zeros <i>between</i> non-zero digits are significant: 2.05 has 3 s.f.</li>"
            "<li>Leading zeros are <b>not</b>: 0.0047 has 2 s.f. (the 4 and the 7).</li>"
            "<li>Trailing zeros after a decimal point are significant: 2.50 has 3 s.f. — it says the value is known to the hundredths.</li>"
            "<li>Trailing zeros in a whole number are ambiguous: 1500 might be 2, 3 or 4 s.f. Standard form removes the doubt: $1.5 \\times 10^3$ is 2 s.f.</li></ul>"
            "<p><b>Rounding to n s.f.:</b> count n digits from the first non-zero digit; look at the next digit; 5 or more rounds up. Then keep the size of the number the same with zeros if needed: 48 367 to 2 s.f. is 48 000, not 48.</p>"
            "<table class='tbl data'><tr><th>Value</th><th>s.f.</th><th>To 2 s.f.</th><th>To 3 s.f.</th></tr>"
            "<tr><td>3.14159</td><td>6</td><td>3.1</td><td>3.14</td></tr>"
            "<tr><td>0.004 762</td><td>4</td><td>0.0048</td><td>0.004 76</td></tr>"
            "<tr><td>27 850</td><td>4</td><td>28 000</td><td>27 900</td></tr>"
            "<tr><td>2.996</td><td>4</td><td>3.0</td><td>3.00</td></tr></table>",
        ),
        explain(
            "How many to give",
            "<p>If the question says \"to 2 significant figures\", give exactly two. If it does not say, give <b>the same number of significant figures as the least precise piece of data</b> in the question — usually 2 or 3. "
            "An answer of 2.857 142 857 m/s from data given to 2 s.f. is marked as 2.9 m/s (and the extra digits may cost a mark for \"inappropriate precision\").</p>"
            "<p><b>Round only at the end.</b> If you round part-way through a two-step calculation, the error grows. Keep the full calculator value (or at least one more figure than you will give) until the final line.</p>",
            tone="warn",
        ),
        worked(
            "Rounding a calculated answer",
            "A student calculates a density: $\\rho = \\dfrac{m}{V} = \\dfrac{47}{18} = 2.611\\,111\\ldots$ g/cm³. The mass was measured to 2 s.f. and the volume to 2 s.f. Give the answer to an appropriate number of significant figures.",
            [
                r"The data has 2 significant figures, so the answer should too.",
                r"Count two digits from the first non-zero digit: 2.6|11… The next digit is 1, which is less than 5, so round down.",
                r"$\rho = 2.6$ g/cm³ (to 2 s.f.).",
                r"The answer line in the exam: \"2.6 g/cm³\". The full value stays in the working above it.",
            ],
        ),
        practice("Significant figures", [
            choice("kc-n4-q1", "How many significant figures does 0.0305 have?", ["2", "3", "4", "5"], 1,
                   "Leading zeros do not count; the zero between the 3 and the 5 does. Three significant figures: 3, 0, 5."),
            choice("kc-n4-q2", "Round 0.047 83 to 2 significant figures.", ["0.05", "0.048", "0.0478", "0.04"], 1,
                   "The first significant figure is the 4. Two figures: 4, 7; the next digit (8) rounds the 7 up to 8: 0.048."),
            choice("kc-n4-q3", "Round 364 920 to 3 significant figures.", ["364", "365", "365 000", "364 900"], 2,
                   "Three figures: 3, 6, 4; the next digit (9) rounds the 4 up to 5. Keep the size of the number with zeros: 365 000."),
            choice("kc-n4-q4", "A speed is calculated as 12.4873 m/s from a distance given to 2 s.f. and a time given to 3 s.f. How should the answer be given?",
                   ["12.4873 m/s", "12.49 m/s", "12 m/s", "10 m/s"], 2,
                   "Match the least precise data: 2 significant figures. 12.4873 to 2 s.f. is 12 m/s."),
            choice("kc-n4-q5", "Which value is written to 3 significant figures?", ["0.5", "2.50", "1500", "3.1416"], 1,
                   "2.50 has three: the trailing zero after the decimal point is significant. 0.5 has one; 1500 is ambiguous; 3.1416 has five."),
            written("kc-n4-q6", "A student finds a wave speed in two steps. She rounds the frequency to 1 s.f. after the first step, then uses it in the second. Explain why her final answer may be wrong, and what she should do instead.",
                    marks(["Rounding part-way through throws away information, so the error is carried into the second calculation and can grow.",
                           "She should keep the full (unrounded) value from the first step — or at least one extra figure — in the working.",
                           "Round only the final answer, to the same number of significant figures as the least precise data."]), lines=3),
        ]),
    ],
)


# =====================================================================
# N5 · Standard form (1.4, Higher)
# =====================================================================

q5_1 = 3e8
q5_2 = 4.5e-5
q5_4 = 6.4e6 / 1000

section_n5 = section(
    "standard-form-nn", "nn", "Standard form", "1.4",
    tags=["H"],
    equations=[r"a \times 10^{n},\quad 1 \le a < 10"],
    blurb="Very large and very small numbers written as a number between 1 and 10 times a power of ten. The calculator does the arithmetic; your job is to enter it correctly and read it back.",
    checklist=[
        "Write a large or small number in standard form",
        "Convert from standard form to an ordinary number",
        "Enter standard form on a calculator with the ×10ˣ (EXP) key, not by typing × 10 ^",
        "Read a calculator display such as 3.2E-5 and write it correctly",
    ],
    parts=[
        explain(
            "Reading and writing standard form",
            "<p>A number in <b>standard form</b> is written $a \\times 10^{n}$, where $a$ is between 1 and 10 (it can be 1, but not 10) and $n$ is a whole number.</p>"
            "<ul><li>A <b>positive</b> power means a big number: $3 \\times 10^{8}$ m/s is 300 000 000 m/s — the point moves 8 places to the right.</li>"
            "<li>A <b>negative</b> power means a small number: $5 \\times 10^{-7}$ m is 0.000 000 5 m — the point moves 7 places to the left.</li></ul>"
            "<p><b>Writing a number in standard form:</b> move the decimal point until there is one non-zero digit in front of it; the number of places moved is $n$ (positive if the original number was 10 or more, negative if it was less than 1).</p>"
            "<table class='tbl data'><tr><th>Ordinary</th><th>Standard form</th><th>Calculator shows</th></tr>"
            "<tr><td>340 000 000</td><td>$3.4 \\times 10^{8}$</td><td>3.4E8</td></tr>"
            "<tr><td>0.000 025</td><td>$2.5 \\times 10^{-5}$</td><td>2.5E-5</td></tr>"
            "<tr><td>6 400 000</td><td>$6.4 \\times 10^{6}$</td><td>6.4E6</td></tr>"
            "<tr><td>0.0016</td><td>$1.6 \\times 10^{-3}$</td><td>1.6E-3</td></tr></table>"
            "<p>On the calculator use the <b>×10ˣ</b> key (sometimes marked EXP or EE): type 3.4, press ×10ˣ, type 8. Typing \"3.4 × 10 ^ 8\" also works but is where the brackets go wrong when you then divide by something.</p>",
        ),
        explain(
            "The E on the screen is not a unit",
            "<p>A display of <i>2.5E-5</i> means $2.5 \\times 10^{-5}$. Write it in the exam as $2.5 \\times 10^{-5}$, never as \"2.5E-5\" or \"2.5⁻⁵\". And $12 \\times 10^{4}$ is not standard form — the front number must be below 10: $1.2 \\times 10^{5}$.</p>",
            tone="warn",
        ),
        worked(
            "A calculation with standard form",
            "Red light has a wavelength of $7 \\times 10^{-7}$ m and travels at $3 \\times 10^{8}$ m/s. Calculate its frequency using $v = f \\times \\lambda$.",
            [
                r"Rearrange: $f = \dfrac{v}{\lambda}$.",
                r"Enter on the calculator: 3 ×10ˣ 8 ÷ 7 ×10ˣ −7. The display shows 4.2857E14.",
                r"$f = 4.3 \times 10^{14}$ Hz (to 2 s.f.).",
                r"Sense check: the power is 8 − (−7) = 15 before the division by 7 brings it down to 14. Visible light is around $10^{14}$ Hz. ✓",
            ],
        ),
        types(["standard-form"], "Calculation: standard form"),
        practice("Standard form", [
            numeric("kc-n5-q1", "Write 300 000 000 in standard form. (Type it as 3e8.)", q5_1, "",
                    "One non-zero digit in front of the point; count the places.",
                    [r"$300\,000\,000 = 3 \times 10^{8}$: the point moves 8 places."]),
            numeric("kc-n5-q2", "Write 0.000 045 in standard form.", q5_2, "",
                    "Small number, so the power is negative.",
                    [r"$0.000\,045 = 4.5 \times 10^{-5}$: the point moves 5 places to the right to get 4.5."]),
            choice("kc-n5-q3", "Which of these is correctly written in standard form?",
                   ["$12 \\times 10^{3}$", "$0.8 \\times 10^{-4}$", "$1.2 \\times 10^{4}$", "$10 \\times 10^{2}$"], 2,
                   "The number in front must be at least 1 and less than 10. Only 1.2 × 10⁴ qualifies."),
            numeric("kc-n5-q4", "The radius of the Earth is $6.4 \\times 10^{6}$ m. Give this in kilometres.", q5_4, "km",
                    "Divide by 1000, which lowers the power by 3.",
                    [r"$6.4 \times 10^{6} \div 10^{3} = 6.4 \times 10^{3}$ km $= 6400$ km."]),
            choice("kc-n5-q5", "A calculator shows 1.6E-19 after a calculation. How should this be written on the answer line?",
                   ["1.6E-19", "$1.6 \\times 10^{-19}$", "$1.6^{-19}$", "0.000 16"], 1,
                   "E on the display stands for × 10 to the power. Write the power of ten out in full."),
            choice("kc-n5-q6", "Which is the larger number: $2 \\times 10^{-3}$ or $5 \\times 10^{-4}$?",
                   ["$2 \\times 10^{-3}$", "$5 \\times 10^{-4}$", "They are equal"], 0,
                   "$2 \\times 10^{-3} = 0.002$ and $5 \\times 10^{-4} = 0.0005$. The less negative power wins, whatever the front number."),
        ]),
    ],
)


# =====================================================================
# N6 · The equation sheet and Edexcel's symbols
# =====================================================================

section_n6 = section(
    "equation-sheet", "nn", "The equation list: choosing the right equation", "WS",
    blurb="Every equation is printed on a list in the exam. Nothing to memorise — but the list is no use unless you can find the one equation that fits the question, fast, and know what every symbol in it means.",
    checklist=[
        "Know what is on the equation list, roughly where, so you can find an equation in seconds",
        "Pick the right equation from the quantities a question gives you and the one it asks for",
        "Recognise every symbol on the list, including the ones that mean two things",
    ],
    parts=[
        explain(
            "The list, and how to use it",
            "<p>In the exam you are given a <b>list of every equation</b> in the course. You do not have to remember any of them. The skill the exam tests is <b>selection</b>: "
            "reading a question, listing the quantities it gives you and the one it wants, and finding the equation that contains exactly those.</p>"
            "<ol class='list'>"
            "<li>Write down the symbols for what is given: $m = \\ldots$, $h = \\ldots$, and the unknown with a question mark: $E = ?$</li>"
            "<li>Scan the list for an equation with <b>those symbols and nothing else unknown</b>. Constants you are expected to know ($g = 10$ N/kg) count as given.</li>"
            "<li>If no equation has them all, it is a two-step question: find one that gets you a quantity the other needs (see the multi-step section).</li>"
            "<li>Copy the equation down exactly, symbols first — that is the E of EWAU.</li></ol>"
            "<p>Knowing the list well is still worth doing, because scanning thirty equations under time pressure is slow. Here it is, by topic:</p>"
            "<table class='tbl'><tr><th>Topic</th><th>Equations</th></tr>"
            "<tr><td>2 Motion and forces</td><td>$\\text{speed} = \\dfrac{\\text{distance}}{\\text{time}}$ &nbsp; $a = \\dfrac{v - u}{t}$ &nbsp; $v^2 - u^2 = 2 \\times a \\times x$ &nbsp; $F = m \\times a$ &nbsp; $W = m \\times g$ &nbsp; $p = m \\times v$ &nbsp; $F = \\dfrac{mv - mu}{t}$</td></tr>"
            "<tr><td>3 &amp; 8 Energy, work and power</td><td>$KE = \\tfrac{1}{2} \\times m \\times v^2$ &nbsp; $\\Delta GPE = m \\times g \\times \\Delta h$ &nbsp; $\\text{efficiency} = \\dfrac{\\text{useful energy output}}{\\text{total energy input}}$ &nbsp; $E = F \\times d$ &nbsp; $P = \\dfrac{E}{t}$ &nbsp; $P = \\dfrac{W}{t}$</td></tr>"
            "<tr><td>4 Waves</td><td>$v = f \\times \\lambda$ &nbsp; $v = \\dfrac{x}{t}$ &nbsp; $T = \\dfrac{1}{f}$</td></tr>"
            "<tr><td>5 Light</td><td>$\\text{power of a lens} = \\dfrac{1}{\\text{focal length}}$ &nbsp; (Physics only)</td></tr>"
            "<tr><td>9 Forces and their effects</td><td>$\\text{moment} = F \\times d$ &nbsp; (distance normal to the force)</td></tr>"
            "<tr><td>10 Electricity</td><td>$Q = I \\times t$ &nbsp; $V = I \\times R$ &nbsp; $E = Q \\times V$ &nbsp; $P = \\dfrac{E}{t}$ &nbsp; $P = I \\times V$ &nbsp; $P = I^2 \\times R$ &nbsp; $E = I \\times V \\times t$</td></tr>"
            "<tr><td>12 Magnetism</td><td>$F = B \\times I \\times l$</td></tr>"
            "<tr><td>13 Induction</td><td>$\\dfrac{V_p}{V_s} = \\dfrac{N_p}{N_s}$ &nbsp; $V_p \\times I_p = V_s \\times I_s$</td></tr>"
            "<tr><td>14 Particle model</td><td>$\\rho = \\dfrac{m}{V}$ &nbsp; $\\Delta Q = m \\times c \\times \\Delta\\theta$ &nbsp; $Q = m \\times L$ &nbsp; $P_1 V_1 = P_2 V_2$</td></tr>"
            "<tr><td>15 Forces and matter</td><td>$F = k \\times x$ &nbsp; $E = \\tfrac{1}{2} \\times k \\times x^2$ &nbsp; $p = \\dfrac{F}{A}$ &nbsp; $P = h \\times \\rho \\times g$</td></tr></table>"
            "<p>Check your own copy of the list before the exam — the layout on the paper is what you need to be able to navigate.</p>",
        ),
        explain(
            "Symbols that mean two things",
            "<table class='tbl'><tr><th>Symbol</th><th>Can mean</th><th>How to tell</th></tr>"
            "<tr><td>$W$</td><td>weight (N) <i>or</i> work done (J)</td><td>$W = m \\times g$ is weight; $E = F \\times d$ (work done) is often written $W = F \\times d$</td></tr>"
            "<tr><td>$Q$</td><td>charge (C) <i>or</i> thermal energy (J)</td><td>$Q = I \\times t$ is charge; $\\Delta Q = m c \\Delta\\theta$ and $Q = m L$ are energy</td></tr>"
            "<tr><td>$P$</td><td>power (W) <i>or</i> pressure (Pa)</td><td>$P = \\dfrac{E}{t}$, $P = I V$ are power; $P = \\dfrac{F}{A}$, $P = h \\rho g$ are pressure</td></tr>"
            "<tr><td>$x$</td><td>distance (m) <i>or</i> extension (m)</td><td>Edexcel uses $x$ for distance in motion equations and for extension in $F = k x$</td></tr>"
            "<tr><td>$v$</td><td>velocity (m/s) <i>or</i> wave speed (m/s)</td><td>context</td></tr>"
            "<tr><td>$V$</td><td>potential difference (V) <i>or</i> volume (m³)</td><td>capital $V$ with $I$ and $R$ is p.d.; with $m$ and $\\rho$ it is volume</td></tr>"
            "<tr><td>$E$</td><td>energy (J)</td><td>any energy — kinetic, work done, electrical</td></tr>"
            "<tr><td>$\\rho$ (rho)</td><td>density (kg/m³)</td><td>not to be confused with $p$, momentum or pressure</td></tr></table>"
            "<p>In your own working, write what each symbol stands for the first time you use it: \"$W$ = weight = …\". It costs two seconds and stops you substituting a weight into a work equation.</p>",
            tone="warn",
        ),
        worked(
            "Picking the equation",
            "A question gives a mass of 2 kg, a height of 5 m and asks for the energy transferred when the object is lifted. Which equation, and why?",
            [
                r"List what is given: mass $m$, height $h$. Wanted: energy $E$.",
                r"Scan the list for an equation with $m$, $h$ and an energy: $\Delta GPE = m \times g \times \Delta h$. ($g = 10$ N/kg is a known constant, so it does not need to be given.)",
                r"Substitute: $GPE = 2 \times 10 \times 5 = 100$ J.",
                r"The method: list the given symbols, find the equation that contains exactly those and the unknown. It also tells you which quantity you have been given but do not need.",
            ],
        ),
        practice("Choosing the equation", [
            choice("kc-n6-q1", "A question gives a force and a distance moved in the direction of the force, and asks for the energy transferred. Which equation from the list?",
                   ["$F = m \\times a$", "$E = F \\times d$", "$P = \\dfrac{E}{t}$", "$\\text{moment} = F \\times d$"], 1,
                   "Force, distance and an energy: work done, $E = F \\times d$. Moment = $F \\times d$ has the same symbols but gives a turning effect in N m, not an energy — read what the question asks for."),
            choice("kc-n6-q2", "In $W = m \\times g$, what does $W$ stand for?", ["Work done", "Weight", "Watts", "Wavelength"], 1,
                   "With mass and gravitational field strength, W is weight in newtons. Work done is $E = F \\times d$."),
            choice("kc-n6-q3", "A question gives a current, a resistance and a time, and asks for the energy transferred. Which pair of equations do you need?",
                   ["$V = I R$ then $E = Q V$", "$P = I^2 R$ then $E = P t$", "$Q = I t$ then $V = I R$", "$P = I V$ then $Q = I t$"], 1,
                   "Current and resistance give power through $P = I^2R$; power and time give energy through $E = P \\times t$. ($V = IR$ then $P = IV$ then $E = Pt$ also works — one step longer.)"),
            choice("kc-n6-q4", "In $\\Delta Q = m \\times c \\times \\Delta\\theta$, what is $Q$?", ["Charge in coulombs", "Thermal energy in joules", "Heat capacity", "Temperature"], 1,
                   "Here Q is thermal energy (J): mass × specific heat capacity × temperature change. The same letter means charge in $Q = I \\times t$."),
            written("kc-n6-q5", "A student is asked for the pressure at the bottom of a swimming pool and writes down $P = I \\times V$. Explain the mistake and state the correct equation.",
                    marks(["$P = I \\times V$ is electrical power; the symbol P means pressure in a different equation.",
                           "Pressure in a liquid: $P = h \\times \\rho \\times g$ (depth × density × gravitational field strength).",
                           "The quantities given (depth, density) point to the right equation — match the symbols you have to the equation."]), lines=3),
            choice("kc-n6-q6", "A question gives an initial velocity, a final velocity and a distance, and asks for the acceleration. Which equation from the list?",
                   ["$a = \\dfrac{v - u}{t}$", "$v^2 - u^2 = 2 \\times a \\times x$", "$F = m \\times a$", "$\\text{speed} = \\dfrac{\\text{distance}}{\\text{time}}$"], 1,
                   "No time is given, so the equation with u, v, a and x (and no t) is the one: $v^2 - u^2 = 2ax$. The first option needs a time you do not have."),
            written("kc-n6-q7", "Describe how you would use the equation list to choose an equation for a calculation question.",
                    marks(["Write down the symbols for each quantity given in the question, and the symbol for the quantity asked for.",
                           "Scan the list for the equation that contains exactly those symbols (known constants such as g count as given).",
                           "If no single equation contains them all, find one that gives a quantity the other needs — a two-step calculation.",
                           "Copy the equation down exactly before substituting."]), lines=4),
        ]),
    ],
)


# =====================================================================
# N7 · Rearranging equations
# =====================================================================

TRIANGLE_SVG = (
    "<polygon points='150,20 40,150 260,150' fill='none' class='d-ink' style='fill:none;stroke:var(--line);stroke-width:2'/>"
    "<line x1='75' y1='108' x2='225' y2='108' style='stroke:var(--line);stroke-width:2'/>"
    "<line x1='150' y1='108' x2='150' y2='150' style='stroke:var(--line);stroke-width:2'/>"
    "<text x='150' y='88' text-anchor='middle' font-size='26' style='fill:var(--accent);font-weight:700'>F</text>"
    "<text x='112' y='138' text-anchor='middle' font-size='26' style='fill:var(--line)'>m</text>"
    "<text x='188' y='138' text-anchor='middle' font-size='26' style='fill:var(--line)'>a</text>"
    "<text x='300' y='70' font-size='14' style='fill:var(--ink-2)'>cover F:  $F = m \\times a$</text>"
    "<text x='300' y='100' font-size='14' style='fill:var(--ink-2)'>cover m:  $m = F \\div a$</text>"
    "<text x='300' y='130' font-size='14' style='fill:var(--ink-2)'>cover a:  $a = F \\div m$</text>"
)

q7_1 = 1200 / 400
q7_2 = 36 / (2 * 4)
q7_3 = 1500 / (10 * 25)
q7_4 = (2 * 800 / 1600) ** 0.5
q7_5 = (22.5 - 10) / 5
q7_6 = 450 / 5

section_n7 = section(
    "rearranging-nn", "nn", "Rearranging an equation", "WS",
    equations=[r"\text{Do the same thing to both sides}", r"F = m \times a \;\Rightarrow\; a = \dfrac{F}{m}"],
    blurb="The subject of an equation is the thing on its own. To make a different quantity the subject, undo what is being done to it, on both sides.",
    checklist=[
        "Make any quantity the subject of a three-term equation (triangle or algebra)",
        "Rearrange an equation with a square (KE, spring energy) including the square root",
        "Rearrange an equation with a fraction ($a = (v - u) \\div t$) for the quantity on the top or the bottom",
        "Substitute first, then rearrange, when the algebra looks hard",
    ],
    parts=[
        explain(
            "Two methods",
            "<p><b>Method 1 — the formula triangle</b> works for any equation of the form <i>one thing = two things multiplied</i>, such as $F = m \\times a$, $V = I \\times R$, $v = f \\times \\lambda$, $\\rho = m \\div V$ (that is $m = \\rho \\times V$). "
            "Put the single quantity at the top; cover the one you want; what you can see is the answer.</p>"
            + diagram(TRIANGLE_SVG, 480, 170, "The $F = m \\times a$ triangle. Cover the quantity you want; the other two tell you whether to multiply (side by side) or divide (one above the other).") +
            "<p><b>Method 2 — do the same to both sides</b> works for every equation, including the ones with squares and fractions that triangles cannot handle:</p>"
            "<ol class='list'>"
            "<li>Write the equation. Circle the quantity you want.</li>"
            "<li>Ask what is being done to it: multiplied by something? divided? squared? having something subtracted?</li>"
            "<li>Undo it, on both sides: divide to undo a multiply, multiply to undo a divide, square-root to undo a square, add to undo a subtract.</li>"
            "<li>Repeat until the quantity is on its own.</li></ol>"
            "<table class='tbl'><tr><th>Equation</th><th>Make … the subject</th><th>Result</th><th>Because</th></tr>"
            "<tr><td>$KE = \\tfrac{1}{2} m v^2$</td><td>$v$</td><td>$v = \\sqrt{\\dfrac{2 \\times KE}{m}}$</td><td>× 2, ÷ m, then square-root both sides</td></tr>"
            "<tr><td>$a = \\dfrac{v - u}{t}$</td><td>$v$</td><td>$v = u + a t$</td><td>× t to clear the fraction, then + u</td></tr>"
            "<tr><td>$a = \\dfrac{v - u}{t}$</td><td>$t$</td><td>$t = \\dfrac{v - u}{a}$</td><td>× t, then ÷ a (t and a swap places)</td></tr>"
            "<tr><td>$GPE = m g h$</td><td>$h$</td><td>$h = \\dfrac{GPE}{m g}$</td><td>÷ m and ÷ g</td></tr>"
            "<tr><td>$P = \\dfrac{E}{t}$</td><td>$t$</td><td>$t = \\dfrac{E}{P}$</td><td>× t, ÷ P</td></tr></table>",
        ),
        explain(
            "Substitute first if the algebra scares you",
            "<p>Marks are for the right answer with working, not for elegant algebra. If you cannot see how to rearrange $v^2 - u^2 = 2 a x$ for $a$, put the numbers in first: $0 - 20^2 = 2 \\times a \\times 50$, so $-400 = 100a$, so $a = -4$ m/s². Numbers are easier to push around than letters.</p>",
            tone="warn",
        ),
        worked(
            "Rearranging with a square",
            "A ball has 180 J of kinetic energy and a mass of 0.4 kg. Calculate its speed.",
            [
                r"Equation: $KE = \tfrac{1}{2} \times m \times v^2$. Wanted: $v$.",
                r"Undo the × ½ and the × m: $v^2 = \dfrac{2 \times KE}{m} = \dfrac{2 \times 180}{0.4} = 900$.",
                r"Undo the square with a square root: $v = \sqrt{900} = 30$ m/s.",
                r"Forgetting the square root (answering 900 m/s) is the most common lost mark on this equation — 900 m/s is nearly three times the speed of sound, which is the clue.",
            ],
        ),
        types(["rearranging"], "Calculation: rearranging"),
        practice("Rearranging", [
            numeric("kc-n7-q1", "A resultant force of 1200 N acts on a car of mass 400 kg. Calculate the acceleration.", q7_1, "m/s²",
                    "Cover a in the triangle: $a = F \\div m$.",
                    ewau(r"a = \dfrac{F}{m}", r"a = \dfrac{1200}{400}", "3", "m/s²")),
            numeric("kc-n7-q2", "A wave has speed 36 m/s and frequency 4 Hz. Calculate its wavelength using $v = f \\times \\lambda$.", 9, "m",
                    "$\\lambda = v \\div f$.",
                    ewau(r"\lambda = \dfrac{v}{f}", r"\lambda = \dfrac{36}{4}", "9", "m")),
            numeric("kc-n7-q3", "An object gains 1500 J of gravitational potential energy when lifted 25 m. Calculate its mass. ($g = 10$ N/kg.)", q7_3, "kg",
                    "$\\text{GPE} = m g h$, so $m = \\text{GPE} \\div (g \\times h)$.",
                    ewau(r"m = \dfrac{GPE}{g \times h}", r"m = \dfrac{1500}{10 \times 25}", "6", "kg")),
            numeric("kc-n7-q4", "A 1600 kg car has 800 J of kinetic energy. Calculate its speed.", q7_4, "m/s",
                    "$v^2 = 2 \\times \\text{KE} \\div m$, then square-root.",
                    [r"$v^2 = \dfrac{2 \times 800}{1600} = 1$.", r"$v = \sqrt{1} = 1$ m/s."]),
            numeric("kc-n7-q5", "A car accelerates from 10 m/s to 22.5 m/s in 5 s. Calculate its acceleration.", q7_5, "m/s²",
                    "$a = (v - u) \\div t$.",
                    ewau(r"a = \dfrac{v - u}{t}", r"a = \dfrac{22.5 - 10}{5} = \dfrac{12.5}{5}", "2.5", "m/s²")),
            numeric("kc-n7-q6", "A motor transfers 450 J of energy in 5 s. Calculate its power.", q7_6, "W",
                    "$P = E \\div t$.",
                    ewau(r"P = \dfrac{E}{t}", r"P = \dfrac{450}{5}", "90", "W")),
        ]),
    ],
)


# =====================================================================
# N8 · Percentages, ratios and proportion
# =====================================================================

q8_1 = 60 / 200 * 100
q8_2 = 0.35 * 2000
q8_3 = (24 - 20) / 20 * 100
q8_5 = 4 * 3

section_n8 = section(
    "proportion", "nn", "Percentages, ratios and proportion", "WS",
    equations=[r"\text{percentage} = \dfrac{\text{part}}{\text{whole}} \times 100", r"y \propto x \;\Rightarrow\; \text{double } x,\ \text{double } y"],
    blurb="Efficiency, percentage change, scaling a recipe up: the same three skills behind a quarter of the marks on every paper.",
    checklist=[
        "Find a percentage of a quantity, and a quantity as a percentage of another",
        "Calculate a percentage change",
        "Use \"directly proportional\" and \"inversely proportional\" correctly in a sentence and in a calculation",
        "Answer a \"what happens if x is doubled\" question without a calculator",
    ],
    parts=[
        explain(
            "Percentages and ratios",
            "<p>A <b>percentage</b> is a fraction with 100 on the bottom. Three jobs:</p>"
            "<table class='tbl'><tr><th>Job</th><th>Do this</th><th>Example</th></tr>"
            "<tr><td>Part as a percentage of a whole</td><td>$\\dfrac{\\text{part}}{\\text{whole}} \\times 100$</td><td>useful 30 J of 120 J in: $\\dfrac{30}{120} \\times 100 = 25\\%$</td></tr>"
            "<tr><td>A percentage of a quantity</td><td>$\\dfrac{\\%}{100} \\times \\text{quantity}$</td><td>40% of 500 J: $0.4 \\times 500 = 200$ J</td></tr>"
            "<tr><td>Percentage change</td><td>$\\dfrac{\\text{new} - \\text{old}}{\\text{old}} \\times 100$</td><td>20 m/s to 25 m/s: $\\dfrac{5}{20} \\times 100 = 25\\%$ increase</td></tr></table>"
            "<p><b>Efficiency</b> is the percentage job in disguise: $\\text{efficiency} = \\dfrac{\\text{useful energy output}}{\\text{total energy input}}$, as a decimal or × 100 as a percentage. It can never be more than 1 (100%).</p>"
            "<p>A <b>ratio</b> compares two quantities: a transformer with 200 turns on the primary and 50 on the secondary has a turns ratio of 4 : 1, so the voltage is divided by 4.</p>",
        ),
        explain(
            "Proportion",
            "<p><b>Directly proportional</b> ($y \\propto x$): double one, the other doubles; halve one, the other halves; the graph is a straight line <b>through the origin</b>. Force and extension of a spring (up to the limit), current and p.d. for a fixed resistor, distance and time at constant speed.</p>"
            "<p><b>Inversely proportional</b> ($y \\propto \\dfrac{1}{x}$): double one, the other halves. Pressure and volume of a gas at constant temperature; acceleration and mass for a fixed force.</p>"
            "<p><b>Proportional to the square</b> ($y \\propto x^2$): double one, the other goes up by $2^2 = 4$. Kinetic energy and speed; braking distance and speed.</p>"
            "<p>The <b>doubling test</b> answers most \"what happens if…\" questions without a calculator. Look at the equation: if the quantity is on the top, the answer scales the same way; on the bottom, the opposite way; squared, by the square of the factor.</p>",
        ),
        worked(
            "A doubling question",
            "The kinetic energy of a car is 200 kJ. State the kinetic energy if its speed is trebled, and explain your answer.",
            [
                r"$KE = \tfrac{1}{2} m v^2$: kinetic energy is proportional to the <b>square</b> of the speed.",
                r"Trebling $v$ multiplies $v^2$ by $3^2 = 9$.",
                r"$KE = 9 \times 200 = 1800$ kJ.",
                r"The sentence the examiner wants: \"KE is proportional to $v^2$, so trebling the speed makes the KE nine times bigger.\"",
            ],
        ),
        types(["percentages-ratios"], "Calculation: percentages and ratios"),
        practice("Proportion", [
            numeric("kc-n8-q1", "A lamp transfers 200 J of energy, of which 60 J is useful light. Calculate its efficiency as a percentage.", q8_1, "%",
                    "Useful ÷ total × 100.",
                    [r"$\dfrac{60}{200} \times 100 = 30\%$."]),
            numeric("kc-n8-q2", "A motor is 35% efficient. It is supplied with 2000 J. Calculate the useful energy output.", q8_2, "J",
                    "35% of 2000.",
                    [r"$0.35 \times 2000 = 700$ J."]),
            numeric("kc-n8-q3", "A car's speed increases from 20 m/s to 24 m/s. Calculate the percentage increase.", q8_3, "%",
                    "Change ÷ original × 100.",
                    [r"$\dfrac{24 - 20}{20} \times 100 = 20\%$."]),
            choice("kc-n8-q4", "The pressure of a fixed mass of gas at constant temperature is inversely proportional to its volume. The volume is halved. What happens to the pressure?",
                   ["It halves", "It stays the same", "It doubles", "It goes up by 4"], 2,
                   "Inversely proportional: when one halves the other doubles."),
            numeric("kc-n8-q5", "A spring extends by 3 cm with a 2 N load. The load is increased to 8 N. Calculate the new extension (Hooke's law applies).", q8_5, "cm",
                    "Extension is directly proportional to force: the force is 4 times bigger.",
                    [r"$8 \div 2 = 4$ times the force, so $4 \times 3 = 12$ cm."]),
            written("kc-n8-q6", "The braking distance of a car is proportional to the square of its speed. A driver doubles her speed. Explain what happens to the braking distance.",
                    marks(["Braking distance ∝ speed², so the distance scales with the square of the factor the speed changes by.",
                           "Doubling the speed multiplies speed² by 2² = 4.",
                           "The braking distance becomes four times as long."]), lines=3),
        ]),
    ],
)


# =====================================================================
# N9 · EWAU: how a calculation is marked
# =====================================================================

section_n9 = section(
    "ewau", "nn", "EWAU: how a calculation is marked", "WS",
    blurb="Equation, Working, Answer, Units. Four lines, in that order, every time — because that is how the marks are given out.",
    checklist=[
        "Lay out every calculation as Equation, Working, Answer, Units",
        "Show the substituted numbers, not just the equation and the answer",
        "Earn the working marks even when the final answer is wrong",
    ],
    parts=[
        explain(
            "Where the marks are",
            "<p>A 3-mark calculation is usually marked like this:</p>"
            "<table class='tbl'><tr><th>Line</th><th>What you write</th><th>Mark for</th></tr>"
            "<tr><td><b>E</b>quation</td><td>$a = \\dfrac{v - u}{t}$</td><td>choosing the right equation from the list</td></tr>"
            "<tr><td><b>W</b>orking</td><td>$a = \\dfrac{20 - 5}{6}$</td><td>substituting the right numbers (after any conversion)</td></tr>"
            "<tr><td><b>A</b>nswer</td><td>$= 2.5$</td><td>evaluating correctly</td></tr>"
            "<tr><td><b>U</b>nits</td><td>m/s²</td><td>the unit (sometimes part of the answer mark)</td></tr></table>"
            "<p><b>Why it matters:</b> if you make a slip on the calculator but have written the equation and the substitution, you still get 2 of the 3 marks. If you write only \"2.6 m/s²\", you get nothing. The working is not for you — it is for the examiner.</p>"
            "<p><b>Rearranging</b> goes between E and W: write the equation as given, then the rearranged form, then substitute. Or substitute into the original and rearrange the numbers — both score.</p>"
            "<p><b>Two-step questions</b> get EWAU twice: finish the first quantity with its unit, then start the second equation on a new line.</p>",
        ),
        worked(
            "A full EWAU answer",
            "A kettle transfers 180 kJ of energy in 2 minutes. Calculate its power.",
            [
                r"<b>Convert first:</b> $180\ \text{kJ} = 180\,000$ J; $2\ \text{min} = 120$ s. (Conversions sit above the E line.)",
                r"<b>E:</b> $P = \dfrac{E}{t}$",
                r"<b>W:</b> $P = \dfrac{180\,000}{120}$",
                r"<b>A:</b> $= 1500$",
                r"<b>U:</b> W",
                r"Final answer line: $P = 1500$ W (or 1.5 kW). Every mark is visible on its own line.",
            ],
        ),
        practice("EWAU", [
            written("kc-n9-q1", "A student answers \"calculate the weight of a 12 kg box\" by writing only \"120 N\". She gets 1 mark out of 2. Explain why, and write the answer that earns both marks.",
                    marks(["No equation and no working are shown, so only the answer mark is available.",
                           "Full answer: $W = m \\times g$; $W = 12 \\times 10$; $= 120$; N.",
                           "With the working shown, a slip on the calculator would still earn the equation and substitution marks."]), lines=4),
            choice("kc-n9-q2", "In a 3-mark calculation, which line usually earns the first mark?",
                   ["The final number", "The unit", "The correct equation", "Underlining the answer"], 2,
                   "The first mark is for choosing the right equation from the list; the second for the substitution; the third for the evaluated answer with its unit."),
            written("kc-n9-q3", "Write out, in EWAU layout, the calculation of the acceleration of a car that speeds up from 8 m/s to 20 m/s in 4 s.",
                    marks(["E: $a = \\dfrac{v - u}{t}$",
                           "W: $a = \\dfrac{20 - 8}{4} = \\dfrac{12}{4}$",
                           "A: $= 3$",
                           "U: m/s²"]), lines=4),
            choice("kc-n9-q4", "A question gives a time of 5 minutes. Where in an EWAU answer should the conversion to seconds appear?",
                   ["It is not needed", "Above the equation line, before substituting", "In the units line", "After the answer"], 1,
                   "Convert before you substitute: write 5 min = 300 s above the E line, so the W line uses 300."),
        ]),
    ],
)


SECTIONS = [section_n1, section_n2, section_n3, section_n4, section_n5, section_n6, section_n7, section_n8, section_n9]
