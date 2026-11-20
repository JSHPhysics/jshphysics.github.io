"""
mx_p2.py — Mixed-topic questions: the Paper 2 blends (band "p2",
P2-1 … P2-8) and the flashcards for the whole page.

P2-1 One object, four topics: density, change of state, latent heat (14 + 15 + 3)
P2-2 Pressure, force and particles (15 + 9 + 14) [P]
P2-3 Springs with forces and energy (15 + 9 + 8)
P2-4 Upthrust into density into moments (15 + 14 + 9) [P]
P2-5 Work, efficiency, GPE and power (8 + 3)
P2-6 Electrical energy as a store (10 + 3 + 8)
P2-7 Induction with its neighbours (13 + 12 + 10)
P2-8 Electricity into heat (10 + 14)
"""

from revlib import (
    axis, choice, curve, dashed, ewau, explain, fact, graph, group, line,
    mark_scheme, marks, numeric, practice, section, worked, written,
)

# ---------------------------------------------------------------------
# P2-1 · One object, four topics
# ---------------------------------------------------------------------

cooling_points = [[0, 90], [2, 70], [8, 70], [10, 40]]
graph_wax = graph(
    axis("time in min", 10, 1), axis("temperature in °C", 100, 10),
    [line(cooling_points)],
    "Cooling curve for wax: 90 degrees at the start, falling to 70 degrees at 2 minutes, flat at 70 degrees until 8 minutes, then falling to 40 degrees at 10 minutes.",
)

section_b1 = section(
    "one-object", "p2", "One object, four stages: density, change of state, latent heat and specific heat capacity in the same question", "14.2–14.9",
    equations=[r"V = \dfrac{m}{\rho} \ \rightarrow\ Q = mL \ \rightarrow\ \Delta Q = mc\Delta\theta", r"\text{one mass, carried through}"],
    blurb="A lump of wax, a coil of copper, a block of aluminium: the question gives its mass once and then walks through density (a volume), a change of state (the particle picture and the cooling curve) and the thermal equations (latent heat, specific heat capacity). The join is the mass — the same number in every stage — and the trap is a unit that changes between stages (g/cm³ in one line, kg in the next).",
    checklist=[
        "Carry one mass through $\\rho = m/V$, $Q = mL$ and $\\Delta Q = mc\\Delta\\theta$ with the units matched",
        "Explain the solid/liquid density difference and the cooling curve's flat section with the particle model",
        "Compare the energies in a cooling curve using the latent heat and specific heat capacity values",
    ],
    parts=[
        explain(
            "The chain",
            "<table class='tbl'><tr><th>Stage</th><th>Equation</th><th>Hands over</th><th>Watch</th></tr>"
            "<tr><td>mass and density → volume</td><td>$V = m \\div \\rho$ (Topic 14 / 15)</td><td>$V$ in m³ or cm³</td><td>keep the units the data use (kg and kg/m³, or g and g/cm³); do not round 0.0047 m³ to 0.005</td></tr>"
            "<tr><td>solid vs liquid density</td><td>particle spacing</td><td>—</td><td>the solid is usually denser: particles closer, more per unit volume; the same mass has a smaller volume</td></tr>"
            "<tr><td>cooling curve → change of state</td><td>flat section = freezing at constant temperature</td><td>the melting point</td><td>on a cooling curve the flat part is <b>freezing</b>, not melting; energy is transferred <b>from</b> the wax</td></tr>"
            "<tr><td>mass → energies</td><td>$Q = mL$ for the flat part; $\\Delta Q = mc\\Delta\\theta$ for the slopes</td><td>energies in J</td><td>same mass in both; $L$ in J/kg (190 kJ/kg = 190 000 J/kg); $\\Delta\\theta$ is the temperature change</td></tr></table>"
            "<p>June 2025 2H Q5: all the wax liquid between which points (1), the particles' motion as it freezes (2), the volume of 3.9 kg of liquid wax at 830 kg/m³ (2), how the volume changes on solidifying at 930 kg/m³ (1), and why the flat section R–S is much longer than the cooling Q–R with $L = 190$ kJ/kg and $c = 2.1$ kJ/kg °C given (3). June 2024 2H Q3: the volume of 14.1 g of copper at 8.96 g/cm³ (3), why the solid is denser (2), the energy to vaporise 60.0 g of water with $L = 2.26 \\times 10^{6}$ J/kg (2), and a volume read off a jug (2). Every stage is on the Topic 14 page; the exam asks them in one go.</p>",
        ),
        worked(
            "A block of wax",
            "3.0 kg of liquid wax (density 800 kg/m³) is left to cool; the graph shows its temperature. Specific latent heat of fusion of wax = 180 000 J/kg; specific heat capacity of solid wax = 2100 J/kg °C. (a) Calculate the volume of the liquid wax. (b) State how the volume changes as the wax solidifies (solid density 920 kg/m³). (c) Calculate the energy transferred to the surroundings while the wax freezes. (d) Calculate the energy transferred as the solid cools from 70 °C to 40 °C, and use the two values to explain the shape of the graph. (9 marks)",
            [
                "(a) $V = m \\div \\rho = 3.0 \\div 800 = 3.75 \\times 10^{-3}$ m³ (0.00375 m³ — keep the figures).",
                "(b) The solid is denser, so the same 3.0 kg occupies a <b>smaller volume</b> ($3.0 \\div 920 = 3.26 \\times 10^{-3}$ m³): the particles pack closer in the solid.",
                "(c) Join: the same 3.0 kg. Freezing at 70 °C (the flat section): $Q = mL = 3.0 \\times 180\\,000 = 540\\,000$ J, transferred <b>from the wax to the surroundings</b>.",
                "(d) Cooling the solid: $\\Delta Q = mc\\Delta\\theta = 3.0 \\times 2100 \\times 30 = 189\\,000$ J.",
                "The freezing section (6 min) is about three times as long as the cooling to 40 °C (2 min) because <b>far more energy</b> (540 kJ against 189 kJ, the same ratio) must leave the wax during the change of state than during 30 °C of cooling, and energy leaves at roughly the same rate throughout — so it takes longer.",
            ],
            graph=graph_wax,
        ),
        practice("One object, four stages", [
            group("mx-b1-q1", "A 0.250 kg block of ice at 0 °C is heated until it is water at 20 °C. Density of ice = 920 kg/m³; $L = 334\\,000$ J/kg; $c$ (water) $= 4200$ J/kg °C.", [
                numeric("mx-b1-q1a", "Calculate the volume of the ice.", 2.72e-4, "m³",
                        "$V = m \\div \\rho$.",
                        ewau(r"V = m \div \rho", r"V = 0.250 \div 920", r"2.7 \times 10^{-4}", "m³ (2.72)"), label="a"),
                numeric("mx-b1-q1b", "Calculate the energy needed to melt the ice.", 83500, "J",
                        "$Q = m L$ with the same mass.",
                        ewau(r"Q = m L", r"Q = 0.250 \times 334\,000", "83\\,500", "J"), label="b"),
                numeric("mx-b1-q1c", "Calculate the energy needed to warm the water to 20 °C.", 21000, "J",
                        "$\\Delta Q = m c \\Delta \\theta$.",
                        ewau(r"\Delta Q = m c \Delta\theta", r"\Delta Q = 0.250 \times 4200 \times 20", "21\\,000", "J"), label="c"),
                written("mx-b1-q1d", "Ice is less dense than water. Explain what this means for the volume of the water compared with the ice. (2)",
                        marks(["Density = mass ÷ volume and the <b>mass is the same</b> (conserved in the change of state).", "A <b>larger density</b> (water, 1000 kg/m³) means the same mass has a <b>smaller volume</b>: the water occupies less space than the ice did ($0.250 \\div 1000 = 2.5 \\times 10^{-4}$ m³)."]), lines=2, label="d"),
            ]),
            numeric("mx-b1-q2", "A copper wire has a mass of 22.4 g. Copper has a density of 8.96 g/cm³. Calculate the volume of the wire.", 2.5, "cm³",
                    "Keep g and g/cm³ together.",
                    ewau(r"V = m \div \rho", r"V = 22.4 \div 8.96", "2.5", "cm³")),
            written("mx-b1-q3", "On a cooling curve the flat section is much longer than the sloping section before it. Explain why, using the words latent heat and specific heat capacity. (3)",
                    marks(["The flat section is the <b>change of state</b> (freezing), where the energy transferred per kilogram is the <b>specific latent heat</b>, which is <b>much larger</b> than the specific heat capacity × the temperature fall in the sloping section (quote the values if given).", "Energy is transferred <b>from the substance to the surroundings</b> at about the <b>same rate</b> throughout…", "…so transferring the larger amount of energy takes a <b>longer time</b>."]), lines=3),
        ]),
    ],
)

# ---------------------------------------------------------------------
# P2-2 · Pressure, force and particles [P]
# ---------------------------------------------------------------------

section_b2 = section(
    "pressure-force-particles", "p2", "Pressure, force and particles: one pressure question across three topics", "15.7P–15.11P, 9.x, 14.4",
    equations=[r"P = \dfrac{F}{A} \ \rightarrow\ F = PA \text{ (normal to the surface)}", r"\text{height graph} \rightarrow \text{less air above} \rightarrow \text{particles further apart}"],
    blurb="The 2023 and 2024 pressure questions each ran through three topics: an arrow for a force (Topic 9), a calculation with $P = F/A$ (Topic 15), a graph of pressure against height, and then 'explain with the particle model' (Topic 14). The joins are a pressure handed into $F = PA$ and a graph handed into an explanation.",
    tags=["P"],
    checklist=[
        "Turn a pressure into a force on a surface with $F = PA$, drawn normal to the surface",
        "Describe a pressure–height graph with numbers and explain it with less air above and lower density",
        "Explain the lower density with the particle model: particles further apart",
    ],
    parts=[
        explain(
            "The chain",
            "<table class='tbl'><tr><th>Stage</th><th>Equation or idea</th><th>Hands over</th><th>Watch</th></tr>"
            "<tr><td>force direction</td><td>fluid pressure acts <b>normal</b> to the surface, towards it (Topic 15 / 9)</td><td>an arrow</td><td>from the point, at right angles</td></tr>"
            "<tr><td>pressure and area → force</td><td>$F = PA$ (Topic 15)</td><td>$F$ in N</td><td>area in m²; a <b>difference</b> in pressure if fluid is on both sides; round as asked</td></tr>"
            "<tr><td>graph → description</td><td>pressure <b>decreases</b> as height increases; <b>non-linear</b>; quote numbers</td><td>a reading, a % change</td><td>(new − old) ÷ old × 100</td></tr>"
            "<tr><td>description → particles</td><td>less air above → smaller weight of air → lower pressure; the air is <b>less dense</b>: particles <b>further apart</b> (Topic 14)</td><td>—</td><td>do not say gravity is weaker higher up; density is about spacing, not particle size</td></tr></table>"
            "<p>June 2024 2H Q4: the direction of the water's force at X (1), the force from a skate on ice from $4.8 \\times 10^{7}$ Pa and $1.2 \\times 10^{-5}$ m² to 2 s.f. (3), describe the pressure–height graph (2), read 8850 m (1), the % change from 104 to 74 kPa (2), and explain the density change with height using the particle model (2). June 2023 2H Q4 did the aeroplane window: pressure difference, $F = PA$, the larger window, the arrow, the graph and the reason.</p>",
        ),
        worked(
            "The skate and the mountain",
            "(a) An ice skater of weight 600 N stands on one blade with an area of $2.0 \\times 10^{-5}$ m². Calculate the pressure on the ice. (b) Atmospheric pressure is 101 kPa at sea level and 70 kPa at 3000 m. Calculate the percentage decrease. (c) Explain, using the particle model, why the air at 3000 m is less dense than at sea level. (7 marks)",
            [
                "(a) $P = F \\div A = 600 \\div (2.0 \\times 10^{-5}) = 3.0 \\times 10^{7}$ Pa — a huge pressure from a small area, which is why the blade bites into the ice.",
                "(b) Change $= 70 - 101 = -31$ kPa; percentage $= -31 \\div 101 \\times 100 = -31$ % (a 31 % decrease; divide by the <i>original</i> value).",
                "(c) At 3000 m there is <b>less air above</b>, so a smaller weight of air presses down on the air there…",
                "…so it is <b>less compressed</b>: its particles are <b>further apart</b> — fewer particles in each cubic metre — which is a lower density (Topic 14: density depends on spacing).",
            ],
        ),
        practice("Pressure, force and particles", [
            group("mx-b2-q1", "A submarine hatch has an area of 0.60 m². The water outside is at a total pressure of 400 kPa and the air inside the submarine is at 100 kPa.", [
                numeric("mx-b2-q1a", "Calculate the net pressure on the hatch.", 300000, "Pa",
                        "Outside − inside.",
                        [r"net $P = 400\,000 - 100\,000 = 300\,000$ Pa"], label="a"),
                numeric("mx-b2-q1b", "Calculate the net force on the hatch.", 180000, "N",
                        "$F = P A$.",
                        ewau(r"F = P A", r"F = 300\,000 \times 0.60", "180\\,000", "N inward"), label="b"),
                choice("mx-b2-q1c", "The force of the water on the hatch acts…",
                       ["downwards, whatever the hatch's angle", "at right angles to the hatch, towards the inside", "along the hatch", "upwards"], 1,
                       "Normal to the surface, towards it.", label="c"),
                written("mx-b2-q1d", "Explain why the total pressure outside is greater at a greater depth. (2)",
                        marks(["Deeper down there is a <b>taller column of water above</b> the hatch, which has more weight.", "That weight acts over the same area, so the pressure due to the water is greater (plus the same atmospheric pressure on the surface)."]), lines=2, label="d"),
            ]),
            written("mx-b2-q2", "A graph shows atmospheric pressure falling from 100 kPa at sea level to 50 kPa at 5.5 km and 26 kPa at 10 km. Describe the relationship and explain it. (4)",
                    marks(["As height increases the pressure <b>decreases</b>.", "The relationship is <b>non-linear</b>: the pressure halves in the first 5.5 km but falls by only 24 kPa in the next 4.5 km — the fall per km gets smaller.", "Higher up there is <b>less air above</b>, so a <b>smaller weight of air</b> presses down.", "The air higher up is also <b>less dense</b> — its particles are further apart because less air presses on it — so each extra kilometre of height removes less weight."]), lines=4),
            numeric("mx-b2-q3", "A pressure of $1.5 \\times 10^{5}$ Pa acts on a window of area 0.35 m². Calculate the force on the window, to 2 significant figures.", 53000, "N",
                    "$F = PA$, then round.",
                    ewau(r"F = P A", r"F = 1.5 \times 10^{5} \times 0.35", "52\\,500 = 53\\,000", "N (2 s.f.)")),
        ]),
    ],
)

# ---------------------------------------------------------------------
# P2-3 · Springs with forces and energy
# ---------------------------------------------------------------------

spring_pts = [[0, 0], [5, 2], [10, 4], [15, 6], [20, 8]]
graph_spring = graph(
    axis("extension in cm", 25, 5), axis("weight in N", 10, 2),
    [line(spring_pts)],
    "Weight against extension for a spring: a straight line from the origin through 20 cm and 8 N.",
)

section_b3 = section(
    "springs-forces-energy", "p2", "Springs with forces and energy: graph, spring constant, free-body diagram, resultant", "15.3–15.5, 9.3–9.7, 8.x",
    equations=[r"E = \text{area} \ \rightarrow\ k = \dfrac{F}{x}", r"\text{free-body diagram: weight} = \text{spring force}"],
    blurb="The 2023 and 2025 spring questions moved from Topic 15 into Topic 9 half-way through: the energy from the area under the graph and the spring constant, then a free-body diagram of the hanging block, then the resultant of two forces by scale drawing. The joins are an extension in metres and a weight that appears in both the spring equation and the force diagram.",
    checklist=[
        "Find the energy stored from the area under a weight–extension graph and the spring constant from its gradient",
        "Draw the free-body diagram of a block hanging in equilibrium: two vectors, equal, through the centre",
        "Carry the block's weight from the spring equation into the force diagram",
    ],
    parts=[
        explain(
            "The chain",
            "<table class='tbl'><tr><th>Stage</th><th>Equation or method</th><th>Hands over</th><th>Watch</th></tr>"
            "<tr><td>graph → energy</td><td>area under the weight–extension line: $\\tfrac{1}{2} F x$ (Topic 15)</td><td>$E$ in J</td><td>$x$ in metres (2025: cm left in, 100 times too large)</td></tr>"
            "<tr><td>graph → spring constant</td><td>gradient, or $k = F \\div x$ from a point on the line</td><td>$k$ in N/m</td><td>$x$ in metres (2025: 100 times too small); the unit is often a separate mark</td></tr>"
            "<tr><td>block in equilibrium → free-body diagram</td><td>weight down, tension (spring force) up, <b>equal length</b>, through the <b>centre</b> (Topic 9)</td><td>a diagram</td><td>2025: vectors \"must have a size as well as a direction\"; arrows near the edge of the box would make it spin</td></tr>"
            "<tr><td>two forces at an angle → resultant</td><td>scale drawing, tip to tail, measure the closing side (Topic 9) [H]</td><td>$R$ in N</td><td>state the scale; measure the length and convert</td></tr></table>"
            "<p>June 2025 2H Q8: why the vertical spring is longer than the horizontal one (its own weight stretches it) (1), what the extension equals (the added weight ÷ $k$) (1), energy from 0 to 8 cm from the area (3), the spring constant with its unit (2), two vectors on the 5 N block (2), the resultant of 4 N and 5 N at X by scale drawing (2). June 2023 2H Q7: the pen spring's force, the change in length, the accuracy point, the hook's force (6 N up) and the resultant of 30 N and 40 N.</p>",
        ),
        worked(
            "The spring and the block",
            "The graph shows the weight hung on a spring against its extension. (a) Calculate the energy stored at an extension of 20 cm. (b) Calculate the spring constant and give its unit. (c) A 4.0 N block hangs at rest from the spring; describe the free-body diagram. (7 marks)",
            [
                "(a) Area of the triangle to 20 cm: $E = \\tfrac{1}{2} F x = \\tfrac{1}{2} \\times 8.0 \\times 0.20 = 0.80$ J (extension in metres).",
                "(b) $k = F \\div x = 8.0 \\div 0.20 = 40$ N/m (or $E = \\tfrac{1}{2} k x^2$: $0.80 = \\tfrac{1}{2} \\times k \\times 0.20^2$ gives the same).",
                "(c) Two vectors through the <b>centre</b> of the block: <b>weight 4.0 N downwards</b> and the <b>force of the spring 4.0 N upwards</b> — the same length, because the block is in equilibrium (resultant zero).",
            ],
            graph=graph_spring,
        ),
        practice("Springs with forces", [
            group("mx-b3-q1", "Use the weight–extension graph for the spring.", [
                numeric("mx-b3-q1a", "Calculate the energy stored when the extension is 10 cm.", 0.20, "J",
                        "Area of the triangle to 10 cm (weight 4 N), x in metres.",
                        ewau(r"E = \tfrac{1}{2} F x", r"E = \tfrac{1}{2} \times 4.0 \times 0.10", "0.20", "J"), label="a"),
                numeric("mx-b3-q1b", "Calculate the extension when a 6.0 N block hangs from the spring, in cm.", 15, "cm",
                        "$k = 40$ N/m; $x = F \\div k$.",
                        ewau(r"x = F \div k", r"x = 6.0 \div 40 = 0.15 \text{ m}", "15", "cm"), label="b"),
                written("mx-b3-q1c", "The 6.0 N block hangs at rest. Describe the two force vectors that a free-body diagram of the block must show. (2)",
                        marks(["The <b>weight</b>, 6.0 N, drawn <b>vertically downwards</b> from the centre of the block.", "The <b>force of the spring</b> on the block (tension), 6.0 N <b>upwards</b> from the centre — the <b>same length</b> as the weight, because the block is in equilibrium."]), lines=2, label="c"),
                numeric("mx-b3-q1d", "The block is now pulled along a table by one string with 6.0 N and a second string at right angles with 8.0 N. Find the resultant of the two pulls (by scale drawing or otherwise).", 10, "N",
                        "Scale drawing, or the 6-8-10 triangle.",
                        [r"tip to tail at right angles: $R = \sqrt{6.0^2 + 8.0^2} = 10$ N (a scale drawing gives the same)"], label="d", tags=["H"]),
            ], graph=graph_spring),
            choice("mx-b3-q2", "A 2025 free-body diagram of a block on a spring scored one mark of two because…",
                   ["the arrows were the wrong colour", "the arrows had no size shown — force vectors must have a size as well as a direction", "it showed only the weight", "the block was too small"], 1,
                   "Two vectors, equal length, through the centre."),
            choice("mx-b3-q3", "A vertical spring is longer than an identical horizontal one with nothing hanging on either. Why?",
                   ["Gravity is stronger vertically", "The vertical spring is stretched by its own weight", "The horizontal spring is compressed", "They are not really identical"], 1,
                   "2025 Q8(a)(i)."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# P2-4 · Upthrust into density into moments [P]
# ---------------------------------------------------------------------

section_b4 = section(
    "upthrust-density-moments", "p2", "Upthrust into density into moments: two chains in one question", "15.15P–15.17P, 14.2, 9.8P–9.13P",
    equations=[r"\text{loss in weight} \rightarrow V \rightarrow \rho", r"\text{then: moments, levers, gears}"],
    blurb="The 2025 paper's last question was two chains back to back: a block weighed in air and in a liquid became a density (Topic 15 into 14), then a lifting machine became a 6-mark moments-and-gears explanation (Topic 9). The 2023 paper paired moments on an arm with a ball floating in two liquids. The joins are a volume, and a weight that reappears as the load.",
    tags=["P"],
    checklist=[
        "Run the four-stage chain from loss in weight to density, carrying each stage forward",
        "Use the object's weight as the load in a moments calculation",
        "Explain why the upthrust on a floating object is the same in two liquids and what changes",
    ],
    parts=[
        explain(
            "The chains",
            "<table class='tbl'><tr><th>Stage</th><th>Equation</th><th>Hands over</th><th>Watch</th></tr>"
            "<tr><td>two weights → upthrust</td><td>upthrust $= W_{\\text{air}} - W_{\\text{liquid}}$ (Topic 15)</td><td>a force in N</td><td>the <b>loss</b> in weight, not the reading in the liquid</td></tr>"
            "<tr><td>upthrust → volume</td><td>upthrust = weight of liquid displaced; $V = \\text{upthrust} \\div (\\rho_{\\text{liquid}} g)$</td><td>$V$ in m³</td><td>the liquid's density, not the block's</td></tr>"
            "<tr><td>weight in air → mass; mass and volume → density</td><td>$m = W \\div g$; $\\rho = m \\div V$ (Topic 14)</td><td>$\\rho$ in kg/m³</td><td>sense check: metals 2000–20 000 kg/m³</td></tr>"
            "<tr><td>the weight → a load on a lever</td><td>moment $= F d$; sum of clockwise = sum of anticlockwise in equilibrium (Topic 9)</td><td>an effort in N</td><td>distances from the pivot, in the same unit</td></tr></table>"
            "<p>June 2025 2H Q9: why the newton-meter reading differs in liquid and air (2: upthrust, equal to the weight of liquid displaced, the liquid denser than air); the block's density from a liquid of $1.4 \\times 10^{3}$ kg/m³ (4, one mark per stage, error carried forward); then the winch 6-marker (Topic 9 T7). June 2023 2H Q6: a push-up pivot, moments on an arm holding a ball (equilibrium shown, then the muscle force with 15 N added), and the same ball floating in fresh and sea water.</p>",
        ),
        worked(
            "A block, a liquid and a lever",
            "A metal block weighs 8.0 N in air and 6.0 N when fully submerged in a liquid of density 1250 kg/m³ ($g = 10$ N/kg). (a) Calculate the density of the block. (b) The block is then hung 0.10 m from the pivot of a lever; calculate the effort needed 0.40 m from the pivot on the other side to balance it. (6 marks)",
            [
                "(a) Upthrust $= 8.0 - 6.0 = 2.0$ N = weight of liquid displaced; mass of liquid displaced $= 0.20$ kg; $V = 0.20 \\div 1250 = 1.6 \\times 10^{-4}$ m³ — the block's volume.",
                "Mass of the block $= 8.0 \\div 10 = 0.80$ kg; $\\rho = m \\div V = 0.80 \\div (1.6 \\times 10^{-4}) = 5000$ kg/m³.",
                "(b) Join: the block's weight in air, 8.0 N, is the load. Moment of the load $= 8.0 \\times 0.10 = 0.80$ N m.",
                "In equilibrium the effort's moment equals it: effort $\\times 0.40 = 0.80$, so effort $= 2.0$ N — a lever that quarters the force.",
            ],
        ),
        practice("Upthrust, density, moments", [
            group("mx-b4-q1", "A stone weighs 12.0 N in air and 9.0 N when fully under water (density 1000 kg/m³). $g = 10$ N/kg.", [
                numeric("mx-b4-q1a", "State the upthrust on the stone.", 3.0, "N",
                        "Loss in weight.",
                        [r"upthrust $= 12.0 - 9.0 = 3.0$ N"], label="a"),
                numeric("mx-b4-q1b", "Calculate the volume of the stone.", 3e-4, "m³",
                        "Weight of water displaced = 3.0 N → mass 0.30 kg → volume.",
                        [r"mass of water displaced $= 3.0 \div 10 = 0.30$ kg", r"$V = 0.30 \div 1000 = 3.0 \times 10^{-4}$ m³"], label="b"),
                numeric("mx-b4-q1c", "Calculate the density of the stone.", 4000, "kg/m³",
                        "$m = 12.0 \\div 10$; $\\rho = m \\div V$.",
                        [r"$m = 12.0 \div 10 = 1.2$ kg"] + ewau(r"\rho = m \div V", r"\rho = 1.2 \div (3.0 \times 10^{-4})", "4000", "kg/m³"), label="c"),
                numeric("mx-b4-q1d", "The stone is hung 0.25 m from the pivot of a uniform beam balanced at its centre. Calculate the force needed 0.75 m from the pivot on the other side to keep the beam level.", 4.0, "N",
                        "Clockwise moment = anticlockwise moment with the stone's weight in air.",
                        [r"moment of the stone $= 12.0 \times 0.25 = 3.0$ N m", r"$F \times 0.75 = 3.0$, so $F = 4.0$ N"], label="d"),
            ]),
            written("mx-b4-q2", "Explain why the newton-meter reading is smaller when the stone is in water than in air. (3)",
                    marks(["In the water there is an <b>upthrust</b> on the stone, supporting part of its weight.", "The upthrust equals the <b>weight of water displaced</b> by the stone.", "Water is <b>much more dense than air</b>, so the water displaced weighs far more than the air displaced did — the upthrust in air is negligible."]), lines=3),
            choice("mx-b4-q3", "In the worked example's chain a student uses the reading in the liquid (6.0 N) as the upthrust instead of the loss in weight (2.0 N). On the 2025 marking, this…",
                   ["gave zero", "took one mark off and carried the error forward through the other three stages", "gave full marks", "took two marks off"], 1,
                   "Each stage is marked; errors carry forward."),
            written("mx-b4-q4", "A ball floats in fresh water and then in sea water. Compare the upthrust on the ball in the two liquids, and explain why less of the ball is under the surface in the sea water. (3)",
                    marks(["The upthrust is the <b>same</b> in both: the ball floats, so in each liquid the upthrust <b>equals the ball's weight</b> (= the weight of liquid displaced).", "Sea water is <b>more dense</b> than fresh water…", "…so a <b>smaller volume</b> of sea water has the same weight as the ball: less needs to be displaced, so less of the ball is below the surface (June 2023 Q6(c))."]), lines=3),
        ]),
    ],
)

# ---------------------------------------------------------------------
# P2-5 · Work, efficiency, GPE and power
# ---------------------------------------------------------------------

section_b5 = section(
    "work-efficiency-power", "p2", "Work, efficiency, GPE and power: the lifting questions", "8.1–8.5, 3.1–3.10",
    equations=[r"W = F d \ \rightarrow\ \text{efficiency} = \dfrac{\text{useful}}{\text{total}}", r"\Delta GPE = m g \Delta h,\quad P = \dfrac{E}{t}"],
    blurb="A pulley lifting a barrel, a motor lifting a mass, a student running upstairs: work done becomes useful energy, efficiency divides it by the total, and power divides it by time. Three joins — an energy, a fraction, a time — and a 6-mark plan to investigate efficiency that the seven steps answer.",
    checklist=[
        "Find the useful work from a force and distance, then the total energy from the efficiency",
        "Plan the pulley-efficiency investigation with the seven steps, including how the measurements are used",
        "Find a height from a GPE and a power from an energy and a time, to the figures asked",
    ],
    parts=[
        explain(
            "The chain",
            "<table class='tbl'><tr><th>Stage</th><th>Equation</th><th>Hands over</th><th>Watch</th></tr>"
            "<tr><td>force and distance → work</td><td>$W = F d$ (Topic 8): the load's weight × the height lifted = useful work</td><td>an energy in J</td><td>distance in the direction of the force</td></tr>"
            "<tr><td>useful → total</td><td>efficiency $=$ useful ÷ total, so total $=$ useful ÷ efficiency (Topic 3)</td><td>an energy in J</td><td>divide by the efficiency, do not multiply; as a decimal</td></tr>"
            "<tr><td>wasted</td><td>total − useful</td><td>—</td><td>say where: friction in the pulley bearings, lifting the pulley's own moving parts, the rope stretching</td></tr>"
            "<tr><td>energy → height, or → power</td><td>$\\Delta h = \\Delta GPE \\div (mg)$; $P = E \\div t$</td><td>$h$ in m, $P$ in W</td><td>mass in kg (320 g = 0.32 kg); time in s</td></tr></table>"
            "<p>June 2023 2H Q9: the barrel's weight from 3000 J of work over 2.0 m (2), the total work at 64 % efficiency (2), another reason for wasted energy (1), and the 6-mark plan \"investigate how the efficiency of the pulley system varies with the weight being lifted\" with a spring balance, metre rule, pulley and metal cubes — \"include how you will use your measurements\". June 2024 2H Q7: distance from $W = Fd$, an experiment to find the GPE gained by a lifted mass naming the measuring devices (4), the height from 5.8 J and 320 g, and one reason a motor is under 100 % efficient. June 2025 2H Q2(b): a student's power climbing stairs to 2 s.f.</p>",
        ),
        worked(
            "The pulley",
            "A pulley system lifts a crate 2.5 m. The useful work done on the crate is 4000 J. The system is 60 % efficient. (a) Calculate the weight of the crate. (b) Calculate the total work done by the person pulling the rope. (c) The person pulls 10 m of rope; calculate the force they pull with. (d) The lift takes 16 s; calculate the useful power. (7 marks)",
            [
                "(a) $W = F d$, so $F = W \\div d = 4000 \\div 2.5 = 1600$ N.",
                "(b) Join: 4000 J is the useful energy. Total $=$ useful ÷ efficiency $= 4000 \\div 0.60 = 6700$ J (6667; about 2700 J wasted against friction in the pulleys and lifting the lower pulley block).",
                "(c) The person's work is the total: $6667 = F \\times 10$, so $F = 670$ N — less than the crate's weight, over four times the distance.",
                "(d) Useful power $= E \\div t = 4000 \\div 16 = 250$ W.",
            ],
        ),
        practice("Work, efficiency and power", [
            group("mx-b5-q1", "An electric motor lifts a 0.450 kg mass through 1.6 m in 2.5 s. The motor transfers 9.0 J of electrical energy during the lift. $g = 10$ N/kg.", [
                numeric("mx-b5-q1a", "Calculate the gravitational potential energy gained by the mass.", 7.2, "J",
                        "$m g \\Delta h$ with the mass in kg.",
                        ewau(r"\Delta GPE = m g \Delta h", r"\Delta GPE = 0.450 \times 10 \times 1.6", "7.2", "J"), label="a"),
                numeric("mx-b5-q1b", "Calculate the efficiency of the motor as a percentage.", 80, "%",
                        "Useful ÷ total × 100.",
                        ewau(r"\text{efficiency} = \text{useful} \div \text{total}", r"\text{efficiency} = 7.2 \div 9.0", "0.80 = 80", "%"), label="b"),
                numeric("mx-b5-q1c", "Calculate the useful power output of the motor.", 2.88, "W",
                        "$P = E \\div t$ with the useful energy.",
                        ewau(r"P = E \div t", r"P = 7.2 \div 2.5", "2.9", "W (2.88)"), label="c"),
                written("mx-b5-q1d", "Give two reasons why the motor is less than 100 % efficient. (2)",
                        marks(["Energy is transferred to the <b>thermal store</b> of the motor's wires and bearings by <b>friction</b> and by the current's heating effect.", "Some energy is transferred by <b>sound</b>, and some lifts the string or hook as well as the mass (not useful)."]), lines=2, label="d"),
            ]),
            written("mx-b5-q2", "Devise an experiment to investigate how the efficiency of a pulley system depends on the weight being lifted. You have a spring balance, a metre rule, the pulley system and metal cubes. Include how you will use your measurements. (6)",
                    mark_scheme([
                        ("Variables", "Independent: the weight lifted (number of cubes); dependent: the efficiency; control: the same pulley, the same height lifted, pulling steadily."),
                        ("Relationship", "Efficiency = useful work ÷ total work = (weight × height) ÷ (pulling force × rope pulled)."),
                        ("Change", "Lift one cube, then two, three … (weigh each load with the spring balance)."),
                        ("Measure", "Height the load rises and length of rope pulled, with the metre rule; the pulling force, with the spring balance in the rope; the load's weight."),
                        ("Use", "Calculate useful work = weight × height and total work = force × rope length for each load; efficiency = useful ÷ total; plot efficiency against weight."),
                        ("Accuracy", "Pull slowly and steadily (constant speed, so the balance reads the force); read the balance at eye level; measure heights from the same reference point."),
                        ("Repeat", "Repeat each load three times and take a mean efficiency."),
                    ], total=6, extra=["Any six of the seven points; the 2023 question asked for how the measurements are used, so the Use row is essential."]), lines=7),
            numeric("mx-b5-q3", "A student of mass 55 kg climbs a flight of stairs 4.2 m high in 6.0 s. Calculate her power, to 2 significant figures. ($g = 10$ N/kg)", 390, "W",
                    "Work $= m g h$; power = work ÷ time.",
                    [r"$W = m g h = 55 \times 10 \times 4.2 = 2310$ J"] + ewau(r"P = E \div t", r"P = 2310 \div 6.0", "385 = 390", "W (2 s.f.)"), tolerance=0.03),
        ]),
    ],
)

# ---------------------------------------------------------------------
# P2-6 · Electrical energy as a store
# ---------------------------------------------------------------------

section_b6 = section(
    "electrical-energy-store", "p2", "Electrical energy as a store: the electric car", "10.16–10.19, 3.3, 2.x",
    equations=[r"E = IVt,\quad Q = It", r"KE = \tfrac{1}{2}mv^2,\quad t = \dfrac{E}{P}"],
    blurb="An electric car's question joins Topic 10 to Topic 3 through energy: the kinetic energy comes from the battery, the battery's energy divided by the motor's power gives a running time, and charging it back is $E = IVt$ with a charge $Q = It$. Watch the units at every join — kWh to J, hours to seconds.",
    checklist=[
        "Find a kinetic energy and compare it with a battery's energy to get a time",
        "Use $E = IVt$ (or $P = IV$ and $E = Pt$) to check a charging-time claim",
        "Find the charge moved with $Q = It$, in coulombs",
    ],
    parts=[
        explain(
            "The chain",
            "<table class='tbl'><tr><th>Stage</th><th>Equation</th><th>Hands over</th><th>Watch</th></tr>"
            "<tr><td>mass and speed → KE</td><td>$KE = \\tfrac{1}{2} m v^2$ (Topic 3)</td><td>$E$ in J</td><td>a car's KE is $10^5$ J; a battery stores $10^8$ J</td></tr>"
            "<tr><td>battery energy and motor power → time</td><td>$t = E \\div P$ (Topic 8)</td><td>$t$ in s → hours</td><td>1 kWh $= 3.6 \\times 10^{6}$ J; convert before dividing</td></tr>"
            "<tr><td>charging → energy</td><td>$E = I V t$, or $P = IV$ then $E = Pt$ (Topic 10)</td><td>$E$ in J, $t$ in s</td><td>\"evaluate the claim\": calculate the time and compare it with the claim in a sentence</td></tr>"
            "<tr><td>current and time → charge</td><td>$Q = I t$ (Topic 10)</td><td>$Q$ in C</td><td>hours into seconds first</td></tr>"
            "<tr><td>regenerative braking</td><td>KE → electrical (the motor runs as a generator, Topic 13) → chemical store of the battery</td><td>—</td><td>instead of the thermal store of the brakes: less energy wasted, longer range</td></tr></table>"
            "<p>June 2023 2H Q8: the car's KE (2), how long the battery lasts (2), how regenerative braking extends the range (2), whether a charging-time claim is right using $t = E \\div (IV)$ (3), and the charge moved (2). The evaluate mark is for the <b>comparison</b> and a <b>conclusion</b>, not just the number.</p>",
        ),
        worked(
            "The electric car",
            "An electric car of mass 1200 kg travels at 16 m/s. Its battery stores 36 kWh ($1.3 \\times 10^{8}$ J) and its motor has an average power of 18 kW. The charger supplies 32 A at 230 V and the maker claims a full charge takes 'under 5 hours'. (a) Calculate the car's kinetic energy. (b) Calculate how long the battery can run the motor, in hours. (c) Evaluate the charging claim. (d) Calculate the charge that flows during the charge. (9 marks)",
            [
                "(a) $KE = \\tfrac{1}{2} m v^2 = \\tfrac{1}{2} \\times 1200 \\times 16^2 = 153\\,600$ J (about 0.1 % of the battery).",
                "(b) $t = E \\div P = 1.3 \\times 10^{8} \\div 18\\,000 = 7200$ s $= 2.0$ hours.",
                "(c) Charging power $P = IV = 32 \\times 230 = 7360$ W; $t = E \\div P = 1.3 \\times 10^{8} \\div 7360 = 17\\,700$ s $= 4.9$ hours — so the claim of under 5 hours is <b>just</b> right, but only if nothing is wasted in the charger and battery; in practice it would take a little longer.",
                "(d) $Q = I t = 32 \\times 17\\,700 = 5.7 \\times 10^{5}$ C.",
            ],
        ),
        practice("Electrical energy as a store", [
            group("mx-b6-q1", "An electric scooter of mass 90 kg (with rider) travels at 8.0 m/s. Its battery stores $1.8 \\times 10^{6}$ J and its motor's average power is 250 W. It is charged at 2.0 A from a 230 V supply.", [
                numeric("mx-b6-q1a", "Calculate the kinetic energy of the scooter and rider.", 2880, "J",
                        "$\\tfrac{1}{2} m v^2$.",
                        ewau(r"KE = \tfrac{1}{2} m v^2", r"KE = \tfrac{1}{2} \times 90 \times 8.0^2", "2880", "J"), label="a"),
                numeric("mx-b6-q1b", "Calculate how long the battery can run the motor, in minutes.", 120, "min",
                        "$t = E \\div P$ in seconds, then ÷ 60.",
                        [r"$t = E \div P = 1.8 \times 10^{6} \div 250 = 7200$ s $= 120$ min"], label="b"),
                numeric("mx-b6-q1c", "Calculate the time to recharge the battery fully, in hours.", 1.09, "h",
                        "$E = IVt$ → $t = E \\div (IV)$.",
                        ewau(r"t = E \div (I V)", r"t = 1.8 \times 10^{6} \div (2.0 \times 230)", "3900 \\text{ s} = 1.1", "h (1.09)"), label="c"),
                numeric("mx-b6-q1d", "Calculate the charge that flows during the recharge.", 7800, "C",
                        "$Q = I t$ with t in seconds.",
                        ewau(r"Q = I t", r"Q = 2.0 \times 3900", "7800", "C"), label="d"),
            ]),
            written("mx-b6-q2", "Explain how regenerative braking increases the distance an electric car can travel on one charge. (3)",
                    marks(["When the car brakes, its <b>kinetic energy</b> is transferred to the motor, which runs as a <b>generator</b> (induction)…", "…so the energy is transferred <b>electrically to the chemical store of the battery</b> instead of to the thermal store of the brakes.", "The battery therefore has <b>more energy</b> after braking than it would with friction brakes, so the car can travel further before it needs charging."]), lines=3),
            choice("mx-b6-q3", "A charging calculation gives $t = 3.6 \\times 10^4$ s. The claim says '8 hours'. The evaluation should say…",
                   ["the claim is wrong", "$3.6 \\times 10^{4}$ s is 10 hours, so the claim is too optimistic — and real charging wastes some energy, making it longer still", "the claim is right", "the units are wrong"], 1,
                   "Convert, compare, conclude."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# P2-7 · Induction with its neighbours
# ---------------------------------------------------------------------

section_b7 = section(
    "induction-neighbours", "p2", "Induction with its neighbours: dynamo, transformer, diode, motor, grid, loudspeaker", "13.1P–13.11P, 12.10–12.14P, 10.x",
    tags=["H"],
    equations=[r"\dfrac{V_p}{V_s} = \dfrac{N_p}{N_s},\quad V_p I_p = V_s I_s", r"\text{induced pd} \leftrightarrow \text{motor effect}"],
    blurb="The induction questions never stay in Topic 13: a dynamo's output goes to a lamp (Topic 10), the transformer's output through a diode to a battery, a motor's commutator sits next to the transformer, and the loudspeaker is compared with the microphone (Topic 12 beside 13). The join is a pd — induced in one place, used in the next.",
    checklist=[
        "Explain the dynamo (harder to turn with a lamp) and the transformer (why a current flows in the secondary) in the standard chains",
        "Use the turns-ratio and pd–current equations and carry the output into the circuit that follows",
        "Compare the loudspeaker with the microphone, and explain the diode and the commutator in the same question",
    ],
    parts=[
        explain(
            "The chain",
            "<table class='tbl'><tr><th>Stage</th><th>Idea or equation</th><th>Hands over</th><th>Watch</th></tr>"
            "<tr><td>turning → induced pd</td><td>the coil cuts field lines, a pd is <b>induced</b>; with a lamp connected a current flows and the induced current's field <b>opposes</b> the motion, so it is harder to turn (Topic 13) [H]</td><td>a pd, then a current</td><td>\"induced\", never \"produced\"</td></tr>"
            "<tr><td>primary → secondary</td><td>alternating current → changing field in the core → changing field through the secondary → pd induced (Topic 13) [H]</td><td>$V_s$</td><td>d.c. would give no changing field</td></tr>"
            "<tr><td>turns → pd; pd → current</td><td>$V_p \\div V_s = N_p \\div N_s$ [H, P]; $V_p I_p = V_s I_s$</td><td>$V_s$, $I_s$</td><td>step-down: fewer turns on the secondary, larger current</td></tr>"
            "<tr><td>a.c. → charging a battery</td><td>a <b>diode</b> lets current flow one way only, so the battery is charged, not discharged on the reverse half-cycles (Topic 10)</td><td>d.c.</td><td>a battery needs d.c.</td></tr>"
            "<tr><td>motor beside generator</td><td>the <b>commutator</b> reverses the current every half turn so the force on each side of the coil keeps it turning the same way (Topic 12) [H, P]</td><td>—</td><td>the loudspeaker is the motor effect; the microphone is induction — the same parts, opposite direction of transfer (Topic 13 T4) [P]</td></tr></table>"
            "<p>June 2025 2H Q6: how a current is produced in the secondary (3), the secondary turns from 230 V, 1.5 V and 1840 turns (2), why a diode is needed in series with the battery (2), the commutator (3). June 2023 2H Q10: how the dynamo was turned between readings, why it gets harder to turn with a lamp (2), the secondary pd (3), loudspeaker versus microphone (6). June 2024 2H Q10: the falling magnet and its investigation, then the grid transformer 11 000 V → 230 V (6). The standard chains are on the Topic 13 page word for word; this is where they are asked side by side.</p>",
        ),
        worked(
            "The toothbrush charger",
            "An electric toothbrush is charged through a transformer with 1150 turns on its primary, connected to 230 V a.c.; its secondary gives 12 V. A diode connects the secondary to the rechargeable battery. (a) Explain how a pd is induced in the secondary coil. (b) Calculate the number of turns on the secondary. (c) Explain why the diode is needed. (d) The primary current is 0.050 A; calculate the secondary current, assuming no energy is wasted. (9 marks)",
            [
                "(a) The <b>alternating</b> current in the primary produces a <b>changing magnetic field</b> in the iron core; the changing field passes through the secondary coil; a <b>changing field through a coil induces a pd</b> across it [H].",
                "(b) $V_p \\div V_s = N_p \\div N_s$: $230 \\div 12 = 1150 \\div N_s$, so $N_s = 1150 \\times 12 \\div 230 = 60$ turns [H, P].",
                "(c) The secondary pd is <b>alternating</b>, but a battery must be charged with current in <b>one direction</b> (d.c.); the diode conducts only one way, so it blocks the half-cycles that would drive current the wrong way through the battery.",
                "(d) Join: the transformer's output. $V_p I_p = V_s I_s$: $230 \\times 0.050 = 12 \\times I_s$, so $I_s = 0.96$ A — stepping the pd down steps the current up.",
            ],
        ),
        practice("Induction and its neighbours", [
            group("mx-b7-q1", "A bicycle dynamo is turned by the wheel and lights a lamp.", [
                written("mx-b7-q1a", "Explain why a pd is induced in the dynamo. (3)",
                        marks(["The coil (or magnet) <b>moves relative to</b> the magnetic field, so the coil <b>cuts magnetic field lines</b>.", "A <b>pd is induced</b> across the coil (the field through the coil is changing).", "Because the coil is in a complete circuit with the lamp, the induced pd drives a <b>current</b>."]), lines=3, label="a", tags=["H"]),
                written("mx-b7-q1b", "Explain why the wheel is harder to turn when the lamp is switched on. (2)",
                        marks(["With the lamp connected a <b>current flows</b> in the coil, and the current has its own <b>magnetic field</b>.", "That field <b>opposes the motion</b> that induced it (a force against the turning), so more work must be done to keep the dynamo turning — the extra work is the energy transferred to the lamp."]), lines=2, label="b", tags=["H"]),
                numeric("mx-b7-q1c", "The dynamo supplies the lamp with 6.0 V at 0.50 A. Calculate the power transferred to the lamp.", 3.0, "W",
                        "$P = IV$.",
                        ewau(r"P = I V", r"P = 0.50 \times 6.0", "3.0", "W"), label="c"),
            ]),
            group("mx-b7-q2", "A step-down transformer in the grid takes 11 000 V and gives 230 V. It supplies a street with 150 A at 230 V.", [
                numeric("mx-b7-q2a", "The primary has 9600 turns. Calculate the number of turns on the secondary.", 200, "turns",
                        "$N_p \\div N_s = V_p \\div V_s$.",
                        ewau(r"N_s = N_p V_s \div V_p", r"N_s = 9600 \times 230 \div 11\,000", "200", "turns"), label="a", tags=["H", "P"]),
                numeric("mx-b7-q2b", "Calculate the current in the primary, assuming the transformer is 100 % efficient.", 3.14, "A",
                        "$V_p I_p = V_s I_s$.",
                        ewau(r"I_p = V_s I_s \div V_p", r"I_p = 230 \times 150 \div 11\,000", "3.1", "A (3.14)"), label="b"),
                written("mx-b7-q2c", "Explain why electricity is transmitted at 11 000 V rather than at 230 V. (3)",
                        marks(["For the same power, a higher pd means a <b>smaller current</b> ($P = IV$).", "The energy wasted by heating in the cables depends on the current ($P = I^2 R$), so a smaller current wastes <b>much less</b> energy.", "Transformers step the pd up for transmission and down again to 230 V for homes, so the saving comes at no cost in usable energy."]), lines=3, label="c", tags=["H", "P"]),
            ]),
            written("mx-b7-q3", "A coil of wire attached to a cone sits in a magnetic field. Compare how it works as a loudspeaker with how it works as a microphone. (4)",
                    marks(["<b>Loudspeaker</b>: an alternating <b>current</b> in the coil → a <b>force</b> on the coil in the magnetic field (motor effect) → the coil and cone <b>move</b> back and forth → the cone pushes the air: <b>sound</b>.", "<b>Microphone</b>: <b>sound</b> makes the cone and coil <b>move</b> in the field → the coil cuts field lines → a <b>pd is induced</b> → an alternating <b>current</b> with the same frequency as the sound.", "Both use the same parts — a coil, a magnet, a cone — and in both the current and the movement have the frequency of the sound.", "The direction of transfer is opposite: electrical → sound in the loudspeaker (motor effect), sound → electrical in the microphone (induction)."]), lines=4, tags=["P"]),
        ]),
    ],
)

# ---------------------------------------------------------------------
# P2-8 · Electricity into heat
# ---------------------------------------------------------------------

section_b8 = section(
    "electricity-into-heat", "p2", "Electricity into heat: a heater's energy into a temperature rise", "10.16–10.19, 14.8, 14.11",
    equations=[r"E = IVt \ \rightarrow\ \Delta Q = mc\Delta\theta", r"\Delta\theta = \dfrac{IVt}{mc}"],
    blurb="The specific-heat-capacity practical is an electricity question for its first half: the energy supplied is current × pd × time, and only then does it become $mc\\Delta\\theta$. The 2024 storage-heater question handed 210 kJ from the heater into a brick; the 6-marker asked for the whole practical with electrical measurements. The join is the energy in joules, and the trap is minutes.",
    checklist=[
        "Find the energy supplied by a heater from I, V and t (or P and t) with t in seconds",
        "Hand that energy into $\\Delta Q = mc\\Delta\\theta$ to predict a temperature rise, or into $c = \\Delta Q \\div (m\\Delta \\theta)$",
        "Explain why the measured rise is smaller, naming where the energy went",
    ],
    parts=[
        explain(
            "The chain",
            "<table class='tbl'><tr><th>Stage</th><th>Equation</th><th>Hands over</th><th>Watch</th></tr>"
            "<tr><td>current, pd, time → energy</td><td>$E = IVt$, or $P = IV$ then $E = Pt$ (Topic 10)</td><td>$E$ in J</td><td>$t$ in <b>seconds</b>; a joulemeter reads $E$ directly</td></tr>"
            "<tr><td>energy → temperature rise</td><td>$\\Delta\\theta = \\Delta Q \\div (mc)$ (Topic 14)</td><td>$\\Delta\\theta$ in °C</td><td>mass in kg; this assumes all the energy went into the substance</td></tr>"
            "<tr><td>measured rise → c</td><td>$c = \\Delta Q \\div (m \\Delta\\theta)$</td><td>$c$ in J/kg °C</td><td>comes out too high if energy went elsewhere</td></tr>"
            "<tr><td>why smaller</td><td>energy transferred to the <b>surroundings</b> and to the <b>container / heater parts</b></td><td>—</td><td>2024: ignore \"energy is lost\" and \"not 100 % efficient\"</td></tr></table>"
            "<p>June 2024 2H Q9: the temperature rise of a 5.8 kg storage-heater brick given 210 kJ with $c = 860$ J/kg °C (2 — the kJ must become J), why the actual rise is smaller (2), and the 6-mark SHC-of-water practical (Topic 14 T6: immersion heater, joulemeter or ammeter and voltmeter with a stopwatch, balance, thermometer; Level 3 needs $\\Delta\\theta$, the energy and how $c$ is found). The Topic 10 heating-effect explanation sits underneath: the current's electrons collide with the ions of the heater wire and transfer energy to them.</p>",
        ),
        worked(
            "The heater in the water",
            "A 12 V immersion heater draws 4.0 A for 5.0 minutes in 0.40 kg of water ($c = 4200$ J/kg °C). (a) Calculate the energy supplied. (b) Calculate the expected temperature rise. (c) The measured rise is 7.5 °C; calculate the value of c this gives and explain why it differs from 4200. (7 marks)",
            [
                "(a) $t = 5.0 \\times 60 = 300$ s; $E = IVt = 4.0 \\times 12 \\times 300 = 14\\,400$ J.",
                "(b) Join: 14 400 J into the water. $\\Delta\\theta = \\Delta Q \\div (mc) = 14\\,400 \\div (0.40 \\times 4200) = 8.6$ °C (8.57).",
                "(c) $c = \\Delta Q \\div (m\\Delta\\theta) = 14\\,400 \\div (0.40 \\times 7.5) = 4800$ J/kg °C.",
                "It is too high because some of the heater's energy was transferred to the <b>surroundings</b> and to the <b>beaker, heater and thermometer</b>, so the water received less than 14 400 J and its rise was smaller than expected; dividing the full energy by the smaller rise overestimates $c$.",
            ],
        ),
        practice("Electricity into heat", [
            group("mx-b8-q1", "A 230 V kettle element carries 8.0 A and is switched on for 2.0 minutes with 0.80 kg of water in it ($c = 4200$ J/kg °C).", [
                numeric("mx-b8-q1a", "Calculate the energy supplied by the element.", 220800, "J",
                        "$E = IVt$ with t in seconds.",
                        [r"$t = 2.0 \times 60 = 120$ s"] + ewau(r"E = I V t", r"E = 8.0 \times 230 \times 120", "220\\,800", "J"), label="a"),
                numeric("mx-b8-q1b", "Calculate the temperature rise of the water if all this energy goes into it.", 65.7, "°C",
                        "$\\Delta \\theta = E \\div (m c)$.",
                        ewau(r"\Delta\theta = \Delta Q \div (m c)", r"\Delta\theta = 220\,800 \div (0.80 \times 4200)", "66", "°C (65.7)"), label="b"),
                written("mx-b8-q1c", "The measured rise is 60 °C. Explain the difference. (2)",
                        marks(["Some of the energy is transferred to the <b>surroundings</b> (the air, by heating from the kettle's outside).", "Some heats the <b>kettle itself</b> (the element, the body) rather than the water — so the water receives less than 220 800 J. (Name where it went, not \"lost\".)"]), lines=2, label="c"),
            ]),
            numeric("mx-b8-q2", "A storage-heater brick of mass 6.0 kg ($c = 850$ J/kg °C) receives 255 kJ from its heating element overnight. Calculate its temperature rise.", 50, "°C",
                    "kJ to J first.",
                    [r"$\Delta Q = 255\,000$ J"] + ewau(r"\Delta\theta = \Delta Q \div (m c)", r"\Delta\theta = 255\,000 \div (6.0 \times 850)", "50", "°C")),
            written("mx-b8-q3", "Describe how to find the specific heat capacity of a metal block using an electric heater, a joulemeter, a balance, a thermometer and a stopwatch. (6)",
                    mark_scheme([
                        ("Mass", "Measure the mass of the block with the balance."),
                        ("Set-up", "Put the immersion heater in one hole of the block and the thermometer in the other (a drop of oil for contact); lag the block."),
                        ("Energy", "Connect the heater through the joulemeter; record the initial temperature; switch on and time the heating; read the energy supplied from the joulemeter (or $E = IVt$ with an ammeter and voltmeter)."),
                        ("Temperature", "Record the final temperature; $\\Delta\\theta$ = final − initial."),
                        ("Calculate", "$c = \\Delta Q \\div (m \\Delta\\theta)$ — or plot temperature against energy and use the gradient."),
                        ("Accuracy", "Lag the block to reduce energy transferred to the surroundings; wait for the highest reading after switching off; repeat."),
                    ], total=6, extra=["Marked by levels: Level 3 needs the temperature change, the energy supplied and how $c$ is found from them."]), lines=8),
        ]),
    ],
)

SECTIONS_P2 = [section_b1, section_b2, section_b3, section_b4, section_b5, section_b6, section_b7, section_b8]

# ---------------------------------------------------------------------
# Flashcards: the joins
# ---------------------------------------------------------------------

FACTS = [
    fact("What is 'the join' in a blended question?", "The quantity one stage hands to the next — an energy, a force, a volume, a pd. Name it before the arithmetic.", "join"),
    fact("Four habits at the join?", "Find it; match units there; carry forward and label each stage; check the number makes sense.", "join"),
    fact("Stage 1 wrong — what about stages 2 and 3?", "Use the wrong value, show the working, label the stage: error carried forward still scores.", "join"),
    fact("GPE → KE → speed: the join?", "The energy: $KE = \\Delta GPE$, then $v = \\sqrt{2KE/m}$.", "gpe-ke-speed"),
    fact("Energy dissipated on a slope?", "$\\Delta GPE - \\tfrac{1}{2}mv_{\\text{measured}}^2$, transferred to the surroundings by friction and air resistance.", "gpe-ke-speed"),
    fact("$\\Delta h$ in $mg\\Delta h$ is…", "The vertical height, not the slope length.", "gpe-ke-speed"),
    fact("Same mass and speed: momentum and KE?", "$p = mv$ (kg m/s); $KE = \\tfrac{1}{2}mv^2$ (J) — different equations, different answers.", "momentum-force-ke"),
    fact("Force from momentum?", "$F = \\Delta(mv) \\div t$; from rest the change is the full $mv$ (Higher).", "momentum-force-ke"),
    fact("Why do stuck-together trolleys move more slowly?", "Momentum is conserved and shared by a larger mass, so $v$ is smaller.", "momentum-force-ke"),
    fact("Braking: the join?", "The KE: braking force × braking distance $= \\tfrac{1}{2}mv^2$.", "stopping-energy"),
    fact("Double the speed: braking and thinking distances?", "Braking ×4 ($\\propto v^2$); thinking ×2 ($\\propto v$).", "stopping-energy"),
    fact("Where does a braking car's KE go?", "Work done by the brakes → thermal store of the brakes → surroundings.", "stopping-energy"),
    fact("Light into glass: what changes?", "Speed and wavelength decrease together; frequency stays the same (set by the source).", "wave-equation-light"),
    fact("The join in a light $v = f\\lambda$ question?", "The frequency — the same on both sides of the boundary.", "wave-equation-light"),
    fact("470 nm in metres?", "$470 \\times 10^{-9}$ m.", "wave-equation-light"),
    fact("Fraction left after n half-lives?", "100 % → 50 → 25 → 12.5 …; between whole half-lives, read the graph.", "nuclear-energy"),
    fact("Mass lost in fusion?", "$m = E \\div c^2$ (the equation is supplied); $c^2 = 9.0 \\times 10^{16}$; unit kg.", "nuclear-energy"),
    fact("Where does fusion's energy come from?", "The products have less mass than the nuclei that fused; the lost mass becomes energy.", "nuclear-energy"),
    fact("Why is a planet's temperature constant?", "It absorbs radiation from its star and emits infrared at the same rate.", "thermal-balance"),
    fact("Planet warms up — then what?", "It emits more, until emission equals absorption again at a higher temperature.", "thermal-balance"),
    fact("A stable star's balance?", "Inward gravity equals the outward pressure from fusion.", "thermal-balance"),
    fact("One object, four stages: the join?", "The mass — the same number in $V = m/\\rho$, $Q = mL$ and $\\Delta Q = mc\\Delta\\theta$.", "one-object"),
    fact("Cooling-curve flat section?", "Freezing at constant temperature; $Q = mL$; energy from the substance to the surroundings.", "one-object"),
    fact("Pressure → force on a surface?", "$F = PA$, normal to the surface; use the pressure difference with fluid on both sides.", "pressure-force-particles"),
    fact("Less dense air higher up, in particles?", "Less air above presses on it, so the particles are further apart: fewer per m³.", "pressure-force-particles"),
    fact("Spring graph → energy and k?", "Area $\\tfrac{1}{2}Fx$ (x in m) and gradient $F \\div x$ (N/m).", "springs-forces-energy"),
    fact("Free-body diagram of a hanging block at rest?", "Weight down and spring force up, equal lengths, through the centre.", "springs-forces-energy"),
    fact("The 2025 upthrust-to-density chain in one line?", "Loss in weight = upthrust = weight of liquid displaced → volume → mass from weight in air → density.", "upthrust-density-moments"),
    fact("The block's weight after the density stage?", "It becomes the load in the moments stage: moment = weight × distance from the pivot.", "upthrust-density-moments"),
    fact("Total energy from useful and efficiency?", "Total = useful ÷ efficiency (divide, as a decimal).", "work-efficiency-power"),
    fact("Pulley efficiency from measurements?", "Useful = weight × height; total = pulling force × rope pulled; efficiency = useful ÷ total.", "work-efficiency-power"),
    fact("Power from a climb?", "$W = mgh$, then $P = W \\div t$, to the figures asked.", "work-efficiency-power"),
    fact("1 kWh in joules?", "$3.6 \\times 10^{6}$ J — convert before dividing by a power in W.", "electrical-energy-store"),
    fact("Charging time from a supply?", "$t = E \\div (IV)$; then compare with the claim and conclude.", "electrical-energy-store"),
    fact("Regenerative braking in one line?", "KE → generator → electrical → battery's chemical store, instead of the brakes' thermal store.", "electrical-energy-store"),
    fact("Why a diode after a transformer charging a battery?", "The secondary pd is a.c.; the diode passes current one way so the battery is charged, not discharged.", "induction-neighbours"),
    fact("Loudspeaker vs microphone?", "Same parts; loudspeaker is current → force → movement → sound (motor effect), microphone is sound → movement → induced pd → current (induction).", "induction-neighbours"),
    fact("Step-down transformer: turns and current?", "Fewer turns on the secondary, smaller pd, larger current ($V_pI_p = V_sI_s$).", "induction-neighbours"),
    fact("Heater energy into water: the join?", "$E = IVt$ (t in seconds) hands the energy to $\\Delta Q = mc\\Delta\\theta$.", "electricity-into-heat"),
    fact("Why is the measured rise smaller?", "Energy transferred to the surroundings and to the container / heater parts — name where, not \"lost\".", "electricity-into-heat"),
    fact("Calculated c too high — why?", "The water got less than the heater's energy, so the rise was smaller; the full energy ÷ the smaller rise overestimates c.", "electricity-into-heat"),
]
