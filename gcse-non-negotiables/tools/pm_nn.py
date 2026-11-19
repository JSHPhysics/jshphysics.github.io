"""
pm_nn.py — Topic 14 (Particle model): the non-negotiables N1–N12.
Tiers from the Pearson spec: everything is both tiers except 14.20P
(doing work on a gas), which is Higher only; 14.16P–14.20P are Physics
only.

N1 The three states            N7 The two thermal equations
N2 Density                     N8 Reducing unwanted transfer
N3 The density practical       N9 Gas pressure and temperature
N4 Why densities differ        N10 Absolute zero and kelvin
N5 Changes of state            N11 Compressing a gas [P]
N6 Heating: SHC and SLH        N12 Key words
"""

from revlib import (
    choice, diagram, ewau, explain, fact, group, mark_scheme, marks, numeric,
    practice, section, worked, written,
)
import pm_diagrams as dg

# ---------------------------------------------------------------------
# N1 · The three states
# ---------------------------------------------------------------------

section_n1 = section(
    "three-states", "nn", "The three states in the kinetic model: arrangement and movement", "14.1",
    equations=[r"\text{solid: vibrate about fixed positions}", r"\text{liquid: move around, flow over each other}", r"\text{gas: fast, random, straight lines}"],
    blurb="Every state-of-matter answer has two halves — how the particles are arranged and how they move — and the marks are usually on the movement. Solids vibrate about fixed positions; liquid particles are still touching but move around and flow over each other; gas particles are far apart and move fast in straight lines in all directions.",
    checklist=[
        "Describe the arrangement of particles in a solid, a liquid and a gas",
        "Describe the movement of particles in each state in the words that score",
        "Explain a bulk property (fixed shape, flows, fills its container) from the particle picture",
    ],
    parts=[
        explain(
            "Arrangement and movement",
            diagram(dg.states_svg(), 660, 250, "The three states: arrangement (how they are packed) and movement (what they do).") +
            "<table class='tbl'><tr><th></th><th>Solid</th><th>Liquid</th><th>Gas</th></tr>"
            "<tr><td><b>Arrangement</b></td><td>regular pattern (lattice), <b>touching</b>, <b>fixed positions</b></td><td>irregular, <b>touching</b>, <b>no fixed positions</b></td><td>random, <b>far apart</b> (about ten times the particle size), no pattern</td></tr>"
            "<tr><td><b>Movement</b></td><td><b>vibrate about fixed positions</b></td><td><b>move around</b> each other, <b>flow over each other</b>, in random directions</td><td>move <b>fast</b>, in <b>straight lines</b>, in <b>random directions</b>, colliding with each other and the walls</td></tr>"
            "<tr><td><b>Energy</b></td><td>least kinetic energy; strong forces hold them</td><td>more energy: enough to leave fixed positions but not to separate</td><td>most energy; forces between particles negligible</td></tr>"
            "<tr><td><b>Bulk properties</b></td><td>fixed shape and volume</td><td>fixed volume, takes the shape of its container, flows</td><td>fills its container, easily compressed, flows</td></tr></table>"
            "<p>The June 2023 report (Q3(c)(ii), the motion of particles in a liquid): \"<b>the particles flow over each other</b>\" scored; \"move freely\" earned one mark but \"added nothing further about the motion\"; imprecise phrases such as \"with lots of energy\", bulk properties (\"they take the shape of the container\") and descriptions of <b>melting</b> scored nothing — the question was about the motion, not the change. The June 2025 report (Q5(b), liquid wax freezing): \"<b>now only vibrate in fixed positions</b>\" was full marks; \"no longer move past each other\" and \"<b>slow down</b> / lose energy\" scored; \"<b>become closer together</b>\" is arrangement, not motion, and \"is not enough for a mark\".</p>",
        ),
        worked(
            "Liquid to solid",
            "Liquid wax cools and becomes solid. Describe the change in the motion of the wax particles. (2 marks)",
            [
                "In the liquid the particles <b>move around</b>, flowing over each other; as the wax cools they <b>slow down</b> (lose kinetic energy).",
                "In the solid they <b>no longer move past each other</b>: they only <b>vibrate about fixed positions</b>.",
            ],
        ),
        practice("The three states", [
            written("pm-n1-q1", "Describe the arrangement and movement of the particles in a gas. (2)",
                    marks(["Arrangement: <b>far apart</b>, in <b>random</b> positions with no pattern.", "Movement: moving <b>fast</b> in <b>straight lines</b> in <b>random directions</b> (colliding with each other and the container)."]), lines=2),
            choice("pm-n1-q2", "Which statement about particles in a liquid would score for 'describe the motion'?",
                   ["They take the shape of the container", "They have lots of energy", "They move around and flow over each other", "They are close together"], 2,
                   "2023: 'flow over each other' scored; the others are bulk properties, vague energy or arrangement."),
            written("pm-n1-q3", "Explain, using the particle model, why a solid has a fixed shape but a liquid does not. (2)",
                    marks(["In a solid the particles are held in <b>fixed positions</b> (only vibrating), so the solid keeps its shape.", "In a liquid the particles are still touching but <b>can move around / flow over each other</b>, so the liquid takes the shape of its container."]), lines=2),
            choice("pm-n1-q4", "Why can a gas be compressed easily but a liquid cannot?",
                   ["Gas particles are smaller", "Gas particles are far apart with empty space between them; liquid particles are already touching", "Liquids are heavier", "Gas particles move faster"], 1,
                   "Compression closes up the gaps; a liquid has none to close."),
            written("pm-n1-q5", "Ice is heated until it melts. Describe the change in the motion of the particles. (2)",
                    marks(["In the ice the particles <b>vibrate about fixed positions</b>; as it is heated they vibrate more (gain energy).", "At melting they <b>leave their fixed positions</b> and can <b>move around / flow over each other</b> (still touching)."]), lines=2),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N2 · Density
# ---------------------------------------------------------------------

section_n2 = section(
    "density-nn", "nn", "Density: mass per unit volume, in SI units", "14.2",
    equations=[r"\rho = \dfrac{m}{V}", r"\text{kg/m}^3 \text{ (or g/cm}^3\text{)}"],
    blurb="Density is mass divided by volume: how much mass is packed into each cubic metre. The equation is on the list; the marks are for the units — work in kilograms and cubic metres unless the question says otherwise — and for sensible rounding.",
    checklist=[
        "Use $\\rho = m/V$ to find density, mass or volume",
        "Work in SI units (kg, m³) and convert g/cm³ ↔ kg/m³ when asked",
        "Round to the significant figures of the data, not to one figure",
    ],
    parts=[
        explain(
            "The equation and its units",
            "<p><b>Density</b> is the <b>mass per unit volume</b>: $\\rho = m \\div V$, in kg/m³ when the mass is in kg and the volume in m³. The same substance has the same density whatever the size of the sample — half a brick has half the mass and half the volume, so the same density. Water is about <b>1000 kg/m³</b> (1 g/cm³), air about 1.2 kg/m³, steel about 7900 kg/m³.</p>"
            "<p><b>Units</b>: the June 2023 report (Q3(b)) — candidates converted the given kg and m³ into g and cm³ \"and often used incorrect powers of ten\"; \"candidates are advised to use <b>SI units</b> in all calculations unless instructed specifically to convert\". When you must convert: 1 g/cm³ = <b>1000</b> kg/m³ (because $1 \\text{ m}^3 = 1\\,000\\,000 \\text{ cm}^3$ and $1 \\text{ kg} = 1000 \\text{ g}$), so multiply g/cm³ by 1000 to get kg/m³. 1 cm³ = 1 × 10⁻⁶ m³; 1 litre = 1000 cm³ = 0.001 m³.</p>"
            "<p><b>Rounding</b>: the June 2025 report (Q5(c)(i)) — many rounded a volume of 0.0047 m³ to 0.005 m³, which was \"unnecessary and actually poor practice\"; give the answer to the <b>same number of significant figures as the data</b> (two, there). A volume is also a check on sense: a small block of metal is a few cm³, i.e. a few ×10⁻⁶ m³.</p>",
        ),
        worked(
            "Volume from density",
            "A piece of wax has a mass of 4.2 kg and a density of 900 kg/m³. Calculate its volume. (2 marks)",
            [
                "$\\rho = m \\div V$, so $V = m \\div \\rho = 4.2 \\div 900$.",
                "$V = 0.0047$ m³ (2 s.f., matching the data — not 0.005).",
            ],
        ),
        practice("Density", [
            numeric("pm-n2-q1", "A copper block has a mass of 445 g and a volume of 50 cm³. Calculate its density in g/cm³.", 8.9, "g/cm³",
                    "$\\rho = m \\div V$ in the units given.",
                    ewau(r"\rho = m \div V", r"\rho = 445 \div 50", "8.9", "g/cm³")),
            numeric("pm-n2-q2", "Convert 8.9 g/cm³ into kg/m³.", 8900, "kg/m³",
                    "× 1000.",
                    [r"$8.9 \text{ g/cm}^3 = 8.9 \times 1000 = 8900 \text{ kg/m}^3$ (1 g/cm³ = 1000 kg/m³)"]),
            numeric("pm-n2-q3", "A cylinder of volume 0.0080 m³ has a density of 7900 kg/m³. Calculate its mass.", 63, "kg",
                    "$m = \\rho \\times V$.",
                    ewau(r"m = \rho V", r"m = 7900 \times 0.0080", "63", "kg (63.2 to 2 s.f., matching the data)")),
            numeric("pm-n2-q4", "A bottle holds 0.75 litres of oil of density 920 kg/m³. Calculate the mass of the oil.", 0.69, "kg",
                    "0.75 litres = 0.75 × 0.001 m³.",
                    [r"$V = 0.75 \times 0.001 = 7.5 \times 10^{-4}$ m³"] + ewau(r"m = \rho V", r"m = 920 \times 7.5 \times 10^{-4}", "0.69", "kg")),
            choice("pm-n2-q5", "A question gives a mass in kg and a volume in m³. The best plan is…",
                   ["convert both to g and cm³ first", "use them as they are: SI units in, kg/m³ out", "convert only the mass", "convert only the volume"], 1,
                   "2023 report: use SI units unless told to convert."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N3 · The density practical
# ---------------------------------------------------------------------

section_n3 = section(
    "density-practical", "nn", "The density core practical: regular solid, irregular solid, liquid", "14.3",
    equations=[r"\text{mass: balance}", r"\text{volume: ruler, or displacement, or the cylinder scale}"],
    blurb="Three objects, three ways to find the volume, one balance for the mass. A regular block: measure its sides and multiply. An irregular solid: the rise in water level in a measuring cylinder. A liquid: pour a measured volume into a cylinder on a balance. When the question gives you a measuring cylinder, describe that method: in 2023 a displacement can scored nothing.",
    checklist=[
        "Describe how to find the density of a regular solid, an irregular solid and a liquid",
        "Describe the measuring-cylinder method for an irregular solid in the words that score",
        "State one accuracy point for each method",
    ],
    parts=[
        explain(
            "The three methods",
            diagram(dg.density_svg(), 660, 295, "The density practical: a regular block, an irregular solid by displacement in a measuring cylinder, and a liquid on a balance.") +
            "<table class='tbl'><tr><th>Object</th><th>Mass</th><th>Volume</th><th>Accuracy</th></tr>"
            "<tr><td><b>Regular solid</b> (block, cylinder)</td><td>balance</td><td>measure length, width and height with a ruler (or vernier callipers); $V = l \\times w \\times h$</td><td>measure each side in several places and average; zero the balance first</td></tr>"
            "<tr><td><b>Irregular solid</b> (stone, key)</td><td>balance</td><td>pour water into a <b>measuring cylinder</b> and <b>read the volume</b>; lower the object in so it is <b>completely under the water</b>; read the new volume; <b>volume = after − before</b></td><td>read the bottom of the meniscus at eye level; lower gently (no splashing); dry the object before weighing it, or weigh it first</td></tr>"
            "<tr><td><b>Liquid</b></td><td>put an empty measuring cylinder on the balance and <b>zero it</b> (or record its mass); pour in the liquid; the reading is the liquid's mass (or subtract)</td><td>read the volume from the cylinder's scale</td><td>use a large volume (a small percentage error); read the meniscus at eye level</td></tr></table>"
            "<p>Then $\\rho = m \\div V$ for each. The June 2023 report (Q3(d), volume of an irregular piece of metal, 2 marks): any two of <b>measure the water volume before</b> adding the metal, make sure <b>all the metal is immersed</b>, <b>subtract</b> the initial from the final volume — \"many candidates scored full marks\". But \"describing a <b>displacement (Eureka) can</b> … scored nothing\" — the question had given a measuring cylinder, and the can is a different method (collect the overflow and measure that; useful for an object too big for a cylinder, but not the one asked for); and \"suggesting measurements not relevant to volume, such as the metal's mass\" earned nothing either. The June 2024 scheme (Q3(d)) had students <b>read a volume off a scale</b> before and after (1350 and 1750 cm³, each accepted within a range) and subtract: 400 cm³.</p>",
        ),
        worked(
            "The irregular solid",
            "Describe how to find the volume of a small irregular piece of metal using a measuring cylinder. (3 marks)",
            [
                "Pour water into the measuring cylinder and <b>read the volume</b> (bottom of the meniscus, at eye level).",
                "<b>Lower the metal gently into the water</b> so that it is <b>completely submerged</b>, and read the new volume.",
                "The volume of the metal is the <b>difference</b>: final reading − initial reading.",
            ],
        ),
        practice("The density practical", [
            written("pm-n3-q1", "Describe how to find the density of a small stone. (4)",
                    marks(["Measure the stone's <b>mass</b> on a balance.", "Pour water into a <b>measuring cylinder</b> and <b>read the volume</b>.", "Lower the stone in so it is <b>fully under the water</b>; read the new volume; <b>volume = new − old</b>.", "Density = mass ÷ volume ($\\rho = m / V$)."]), lines=4),
            choice("pm-n3-q2", "Which measurement is NOT needed to find the volume of an irregular solid by the measuring-cylinder method?",
                   ["The water volume before the object goes in", "The water volume after the object goes in", "The mass of the object", "That the object is fully under the water"], 2,
                   "2023 report: the metal's mass is 'not relevant to volume' — it earned nothing in a volume question."),
            written("pm-n3-q3", "Describe how to find the density of a liquid. (3)",
                    marks(["Put an empty measuring cylinder on a <b>balance</b> and zero it (or record its mass).", "Pour in the liquid: the balance gives the liquid's <b>mass</b> (subtracting the empty cylinder if needed); read the <b>volume</b> from the cylinder scale.", "Density = mass ÷ volume."]), lines=3),
            numeric("pm-n3-q4", "A measuring cylinder reads 45 cm³. A stone of mass 52 g is lowered in and the reading becomes 65 cm³. Calculate the density of the stone.", 2.6, "g/cm³",
                    "Volume = 65 − 45.",
                    [r"$V = 65 - 45 = 20$ cm³"] + ewau(r"\rho = m \div V", r"\rho = 52 \div 20", "2.6", "g/cm³")),
            choice("pm-n3-q5", "Which is an accuracy improvement for the regular-block method?",
                   ["Use a bigger balance", "Measure each dimension several times and average", "Use less water", "Weigh the block in water"], 1,
                   "Repeat each length and average; read the meniscus at eye level for the cylinder methods."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N4 · Why densities differ
# ---------------------------------------------------------------------

section_n4 = section(
    "density-states", "nn", "Why solids are denser than liquids than gases: particle spacing", "14.4",
    equations=[r"\text{closer particles} \Rightarrow \text{more mass in each m}^3"],
    blurb="The same particles, packed differently. In a solid and a liquid they are touching, so the densities are similar (the solid usually a little higher); in a gas they are far apart, so a gas is about a thousand times less dense. The mark is for the spacing — the number of particles per unit volume — not for the particles being heavier.",
    checklist=[
        "Explain why a gas is much less dense than the same substance as a liquid or solid",
        "Explain why a solid is usually slightly denser than its liquid",
        "State the exception: ice is less dense than water",
    ],
    parts=[
        explain(
            "The spacing argument",
            "<p>Density is mass per unit volume, and the particles of one substance all have the same mass, so density depends only on <b>how closely the particles are packed</b> — how many there are in each cubic metre. In a <b>gas</b> the particles are <b>far apart</b> (most of the volume is empty space), so there are far fewer in each m³: a gas is roughly a <b>thousand times less dense</b> than the liquid (steam about 0.6 kg/m³, water 1000 kg/m³). In a <b>liquid</b> and a <b>solid</b> the particles are <b>touching</b>, so the densities are similar; in most substances the solid's regular packing is slightly <b>closer</b> than the liquid's irregular packing, so the solid is a little denser and <b>sinks in its own liquid</b>. The June 2024 scheme (Q3(b), 2 marks): \"density of solid is greater than liquid\"; \"because the <b>particle spacing</b> in a solid is <b>less</b> than in a liquid\" — \"more tightly packed\" and \"<b>more particles per unit volume</b>\" accepted. The June 2025 question (Q5(c)(ii)) did it with data: the same mass of wax had a <b>smaller volume as a solid</b> than as a liquid.</p>"
            "<p>The famous exception: <b>ice is less dense than water</b> (920 against 1000 kg/m³), because water molecules in ice are held in an open lattice with more space between them than in the liquid — which is why ice floats and pipes burst. The spec wants the general rule; the exception is worth knowing because questions use it.</p>",
        ),
        worked(
            "Solid and liquid wax",
            "Explain why solid wax is denser than liquid wax. (2 marks)",
            [
                "In the solid the particles are packed in a regular pattern with the <b>particle spacing smaller</b> than in the liquid — <b>more particles in each unit of volume</b>.",
                "Density is mass per unit volume and the particles have the same mass, so the solid, with more particles per m³, is denser (the same mass of wax takes up a smaller volume as a solid).",
            ],
        ),
        practice("Why densities differ", [
            written("pm-n4-q1", "Explain, in terms of particles, why steam is much less dense than water. (2)",
                    marks(["In steam (a gas) the particles are <b>far apart</b>, with mostly empty space between them; in water they are touching.", "So there are <b>far fewer particles per unit volume</b> in steam, and density is mass per unit volume."]), lines=2),
            choice("pm-n4-q2", "A solid is usually denser than its liquid because…",
                   ["its particles are heavier", "its particles are closer together (more particles per unit volume)", "it is colder", "its particles are bigger"], 1,
                   "Same particles, closer packing."),
            choice("pm-n4-q3", "Roughly how do the densities of a substance as a gas and as a liquid compare?",
                   ["The gas is about a thousand times less dense", "They are about the same", "The gas is twice as dense", "The gas is ten times less dense"], 0,
                   "Particles about ten times further apart in each direction: a thousand times fewer per m³."),
            written("pm-n4-q4", "A table shows 0.050 kg of a substance has a volume of 60 cm³ as a solid and 65 cm³ as a liquid. Use the data to compare the two densities. (1)",
                    marks(["The <b>same mass</b> occupies a <b>smaller volume as a solid</b> (60 cm³ against 65 cm³), so the solid is <b>denser</b> (0.83 against 0.77 g/cm³)."]), lines=2),
            choice("pm-n4-q5", "Ice floats on water because…",
                   ["ice is a gas", "ice is less dense than water — its molecules are held further apart in the solid lattice", "ice is warmer", "water is a solid"], 1,
                   "The exception to the rule, and why pipes burst."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N5 · Changes of state
# ---------------------------------------------------------------------

section_n5 = section(
    "changes-of-state", "nn", "Changes of state: the six names, mass conserved, physical not chemical", "14.5",
    equations=[r"\text{melt, freeze, boil, evaporate, condense, sublimate}", r"\text{mass before} = \text{mass after}"],
    blurb="Melting, freezing, boiling (and evaporating), condensing and sublimating are physical changes: the particles are the same particles, so mass is conserved, and the substance gets its original properties back if the change is reversed — unlike many chemical changes, which make new substances.",
    checklist=[
        "Name the six changes of state and which way each goes",
        "State that mass is conserved in a change of state, and why",
        "Explain the difference between a physical change and a chemical change",
    ],
    parts=[
        explain(
            "The six changes, and why they are physical",
            "<table class='tbl'><tr><th>Change</th><th>From → to</th><th>Energy</th></tr>"
            "<tr><td><b>Melting</b></td><td>solid → liquid</td><td>taken in (at the melting point)</td></tr>"
            "<tr><td><b>Freezing</b> (solidifying)</td><td>liquid → solid</td><td>given out (at the same temperature, the freezing point)</td></tr>"
            "<tr><td><b>Boiling</b></td><td>liquid → gas, throughout the liquid, at the boiling point</td><td>taken in</td></tr>"
            "<tr><td><b>Evaporating</b></td><td>liquid → gas, from the surface only, at any temperature</td><td>taken in (which is why evaporation cools)</td></tr>"
            "<tr><td><b>Condensing</b></td><td>gas → liquid</td><td>given out</td></tr>"
            "<tr><td><b>Sublimating</b></td><td>solid → gas directly (dry ice, iodine); gas → solid is deposition</td><td>taken in</td></tr></table>"
            "<p><b>Mass is conserved</b>: the particles are not created, destroyed or changed — the same number of the same particles, just arranged and moving differently — so the mass after a change of state equals the mass before (a sealed flask of ice weighs the same once it has melted). These are <b>physical changes</b>: reverse the change (freeze the water again) and the substance <b>recovers its original properties</b>. Many <b>chemical changes</b> make <b>new substances</b> (burning wood, rusting iron) and cannot be reversed by reversing the conditions. The June 2024 paper (Q9(a)) asked which change is solid → gas: <b>sublimation</b> (not melting, freezing or condensation).</p>",
        ),
        worked(
            "Physical or chemical?",
            "Explain why melting ice is a physical change but burning wood is a chemical change. (3 marks)",
            [
                "Melting ice: the water particles are <b>unchanged</b> — only their arrangement and movement change — so the <b>mass is conserved</b>…",
                "…and the change is <b>reversible</b>: freeze the water and you get ice with its original properties back.",
                "Burning wood makes <b>new substances</b> (ash, carbon dioxide, water vapour) with different properties; the wood cannot be recovered by reversing the conditions, so it is a chemical change.",
            ],
        ),
        practice("Changes of state", [
            choice("pm-n5-q1", "The change from a solid directly to a gas is called…",
                   ["melting", "evaporation", "sublimation", "condensation"], 2,
                   "2024 Q9(a). Dry ice (solid CO₂) does it at room temperature."),
            written("pm-n5-q2", "A sealed container holds 50 g of ice. The ice melts. State the mass of the water and explain your answer. (2)",
                    marks(["<b>50 g</b>: mass is conserved.", "The <b>same particles</b> are present before and after — none are created or destroyed, they are only arranged and moving differently."]), lines=2),
            choice("pm-n5-q3", "Which is the difference between boiling and evaporating?",
                   ["Boiling needs energy, evaporating does not", "Boiling happens throughout the liquid at the boiling point; evaporating happens only at the surface, at any temperature", "Evaporating makes a solid", "There is no difference"], 1,
                   "Both liquid → gas; boiling is at one temperature, through the bulk."),
            written("pm-n5-q4", "State what is meant by a physical change, and give one way it differs from a chemical change. (2)",
                    marks(["A change in which the substance is <b>not changed into a new substance</b> (only its state, arrangement or movement of particles) — e.g. melting, boiling.", "It is <b>reversible</b>: the material <b>recovers its original properties</b> when the change is reversed; a chemical change makes new substances."]), lines=2),
            choice("pm-n5-q5", "Which change gives energy OUT to the surroundings?",
                   ["Melting", "Boiling", "Condensing", "Sublimating"], 2,
                   "Condensing and freezing release the energy that boiling and melting took in."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N6 · Heating: SHC and SLH
# ---------------------------------------------------------------------

section_n6 = section(
    "shc-slh-defined", "nn", "Heating a system: temperature rise or change of state; specific heat capacity and specific latent heat", "14.6, 14.7",
    equations=[r"\text{SHC: energy per kg per }°\text{C}", r"\text{SLH: energy per kg to change state, no temperature change}"],
    blurb="Heating a system increases the energy stored in it. That energy either raises the temperature (the particles move faster — more kinetic energy) or changes the state at a constant temperature (the particles' bonds are loosened or broken — more potential energy). Specific heat capacity measures the first per kilogram per degree; specific latent heat measures the second per kilogram.",
    checklist=[
        "Explain what heating does to the energy stored in a system, and the two things it can do",
        "Define specific heat capacity and specific latent heat in the mark-scheme words",
        "Explain the difference between them: temperature change vs change of state",
    ],
    parts=[
        explain(
            "Two things heating can do",
            "<p>Heating transfers energy into the <b>thermal store</b> of a system — its <b>internal energy</b>, the total kinetic and potential energy of its particles. That energy does one of two things:</p>"
            "<table class='tbl'><tr><th></th><th>Raising the temperature</th><th>Changing the state</th></tr>"
            "<tr><td>What the particles do</td><td>move <b>faster</b> (vibrate more in a solid): their <b>kinetic energy</b> increases</td><td>break away from their neighbours / separate: their <b>potential energy</b> increases, the <b>kinetic energy does not</b></td></tr>"
            "<tr><td>Temperature</td><td><b>rises</b></td><td><b>stays constant</b> at the melting or boiling point while the change happens</td></tr>"
            "<tr><td>Quantity</td><td><b>specific heat capacity</b>, $c$</td><td><b>specific latent heat</b>, $L$</td></tr>"
            "<tr><td>Definition (learn the sentence)</td><td>the energy needed to raise the temperature of <b>1 kg</b> of the substance by <b>1 °C</b> (unit J/kg °C)</td><td>the energy needed to change the state of <b>1 kg</b> of the substance <b>without a change in temperature</b> (unit J/kg)</td></tr>"
            "<tr><td>Water</td><td>4200 J/kg °C (large — water is slow to heat and slow to cool)</td><td>fusion (melting) 334 000 J/kg; vaporisation (boiling) 2 260 000 J/kg</td></tr></table>"
            "<p><b>The difference</b> (14.7): specific heat capacity is about a <b>temperature change</b> with no change of state; specific latent heat is about a <b>change of state</b> with no temperature change. \"Latent\" means hidden — the energy goes in but the thermometer does not move. Each change has its own latent heat: <b>fusion</b> for melting/freezing, <b>vaporisation</b> for boiling/condensing, and the energy comes back out when the change reverses.</p>",
        ),
        worked(
            "The two definitions",
            "Define specific heat capacity and specific latent heat, and state the difference between them. (3 marks)",
            [
                "<b>Specific heat capacity</b>: the energy needed to raise the temperature of <b>1 kg</b> of a substance by <b>1 °C</b>.",
                "<b>Specific latent heat</b>: the energy needed to change the state of <b>1 kg</b> of a substance <b>with no change in temperature</b>.",
                "The difference: one is for a <b>temperature change</b> (the particles speed up), the other for a <b>change of state</b> at constant temperature (the particles separate, potential energy rises).",
            ],
        ),
        practice("SHC and SLH", [
            written("pm-n6-q1", "State what is meant by the specific heat capacity of a substance. (1)",
                    marks(["The energy needed to raise the temperature of <b>1 kg</b> of the substance by <b>1 °C</b>."]), lines=1),
            written("pm-n6-q2", "State what is meant by the specific latent heat of vaporisation of water. (1)",
                    marks(["The energy needed to change <b>1 kg</b> of water from liquid to gas (boil it) <b>without a change in temperature</b>."]), lines=1),
            choice("pm-n6-q3", "While a substance is melting, the energy supplied…",
                   ["raises its temperature", "increases the kinetic energy of the particles", "increases the potential energy of the particles as they break from their fixed positions, with no temperature change", "is lost"], 2,
                   "Latent: the thermometer does not move."),
            written("pm-n6-q4", "Explain the difference between specific heat capacity and specific latent heat. (2)",
                    marks(["Specific heat capacity is the energy per kg to <b>change the temperature</b> by 1 °C, with no change of state.", "Specific latent heat is the energy per kg to <b>change the state</b>, with <b>no change in temperature</b>."]), lines=2),
            choice("pm-n6-q5", "Water has a large specific heat capacity (4200 J/kg °C). This means that…",
                   ["water boils easily", "a lot of energy is needed to raise its temperature, so it heats up and cools down slowly", "water is a good conductor", "water has a high melting point"], 1,
                   "Why the sea moderates the climate and why central heating uses water."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N7 · The two thermal equations
# ---------------------------------------------------------------------

section_n7 = section(
    "thermal-equations", "nn", "The two thermal equations, and when each applies", "14.8, 14.9",
    equations=[r"\Delta Q = m\,c\,\Delta\theta", r"Q = m\,L"],
    blurb="Temperature change: $\\Delta Q = m c \\Delta \\theta$. Change of state: $Q = m L$. A problem that does both — ice at −10 °C to water at 20 °C — is three steps added together. Both equations are on the list; the marks are for choosing the right one for each stage, using Δθ (a change, the same in °C or K) and keeping the mass in kilograms.",
    checklist=[
        "Use $\\Delta Q = m c \\Delta \\theta$ for a temperature change and $Q = m L$ for a change of state",
        "Split a mixed problem into stages and add the energies",
        "Use the temperature change, not the temperature, and the mass in kg",
    ],
    parts=[
        explain(
            "Choosing the equation",
            "<table class='tbl'><tr><th>The question says…</th><th>Equation</th><th>Watch</th></tr>"
            "<tr><td>temperature rises / falls from … to …</td><td>$\\Delta Q = m c \\Delta\\theta$</td><td>$\\Delta\\theta$ is the <b>change</b> (final − initial); the same number in °C or K</td></tr>"
            "<tr><td>melts / freezes / boils / condenses, at a constant temperature</td><td>$Q = m L$</td><td>no $\\Delta\\theta$ at all; use the latent heat for the <b>right change</b> (fusion or vaporisation)</td></tr>"
            "<tr><td>ice at −10 °C becomes water at 20 °C</td><td>three stages: warm the ice to 0 °C ($m c_{ice} \\Delta\\theta$), melt it ($m L_f$), warm the water to 20 °C ($m c_{water} \\Delta\\theta$); <b>add</b></td><td>different $c$ for ice (2100) and water (4200)</td></tr>"
            "<tr><td>energy supplied by a heater for a time</td><td>$E = P t$ first (Topic 10), then one of the above</td><td>the heater energy equals $\\Delta Q$ only if none is wasted</td></tr></table>"
            "<p>The June 2024 scheme: Q3(c), $Q = m L$ for a change of state — substitution (1), evaluation (1), $1.36 \\times 10^5$ J; Q9(c)(i), $\\Delta\\theta = \\Delta Q \\div (m c)$ — rearrangement and substitution (1), evaluation (1), 42 °C. Grams must become kilograms before substituting (250 g = 0.25 kg), and a latent heat of 334 000 J/kg is often written 334 kJ/kg — convert, or keep the kJ and remember the answer is in kJ.</p>",
        ),
        worked(
            "Ice to warm water",
            "0.20 kg of ice at 0 °C is turned into water at 30 °C. Specific latent heat of fusion of ice = 334 000 J/kg; specific heat capacity of water = 4200 J/kg °C. Calculate the total energy needed. (4 marks)",
            [
                "Melt the ice (no temperature change): $Q = m L = 0.20 \\times 334\\,000 = 66\\,800$ J.",
                "Warm the water from 0 °C to 30 °C: $\\Delta\\theta = 30$ °C.",
                "$\\Delta Q = m c \\Delta\\theta = 0.20 \\times 4200 \\times 30 = 25\\,200$ J.",
                "Total $= 66\\,800 + 25\\,200 = 92\\,000$ J (92 kJ).",
            ],
        ),
        practice("The two equations", [
            numeric("pm-n7-q1", "Calculate the energy needed to raise the temperature of 1.5 kg of water from 20 °C to 60 °C. ($c = 4200$ J/kg °C)", 252000, "J",
                    "$\\Delta \\theta = 60 - 20$.",
                    ewau(r"\Delta Q = m c \Delta\theta", r"\Delta Q = 1.5 \times 4200 \times 40", "252\\,000", "J")),
            numeric("pm-n7-q2", "Calculate the energy needed to boil 0.50 kg of water that is already at 100 °C. ($L = 2\\,260\\,000$ J/kg)", 1130000, "J",
                    "A change of state at constant temperature: $Q = m L$.",
                    ewau(r"Q = m L", r"Q = 0.50 \times 2\,260\,000", "1\\,130\\,000", "J")),
            numeric("pm-n7-q3", "A 2.0 kg aluminium block ($c = 900$ J/kg °C) receives 36 000 J. Calculate its temperature rise.", 20, "°C",
                    "$\\Delta \\theta = \\Delta Q \\div (m c)$.",
                    ewau(r"\Delta\theta = \Delta Q \div (m c)", r"\Delta\theta = 36\,000 \div (2.0 \times 900)", "20", "°C")),
            numeric("pm-n7-q4", "250 g of ice at 0 °C melts and the water warms to 10 °C. Calculate the total energy needed. ($L = 334\\,000$ J/kg, $c = 4200$ J/kg °C)", 94000, "J",
                    "250 g = 0.25 kg; melt, then warm; add.",
                    [r"$Q = m L = 0.25 \times 334\,000 = 83\,500$ J", r"$\Delta Q = m c \Delta\theta = 0.25 \times 4200 \times 10 = 10\,500$ J", r"total $= 83\,500 + 10\,500 = 94\,000$ J"]),
            choice("pm-n7-q5", "Steam at 100 °C condenses to water at 100 °C. Which equation gives the energy released?",
                   ["$\\Delta Q = m c \\Delta \\theta$ with $\\Delta \\theta = 100$", "$Q = m L$ with the latent heat of vaporisation", "$Q = m L$ with the latent heat of fusion", "$E = P t$"], 1,
                   "Change of state at constant temperature; vaporisation for gas ↔ liquid."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N8 · Reducing unwanted transfer
# ---------------------------------------------------------------------

section_n8 = section(
    "insulation", "nn", "Reducing unwanted energy transfer: thermal insulation", "14.10",
    equations=[r"\text{insulator: low thermal conductivity}", r"\text{trapped air}"],
    blurb="Unwanted transfer by heating is reduced with insulation: a material of low thermal conductivity, usually one that traps air (foam, fibreglass, feathers, double glazing) so that conduction and convection are both cut down. The 2025 examiners saw students apply the word to a cable's plastic coating — that insulation is electrical, not thermal.",
    checklist=[
        "Explain how insulation reduces unwanted energy transfer",
        "Give examples: lagging, loft insulation, double glazing, a vacuum flask",
        "Distinguish thermal insulation from electrical insulation",
    ],
    parts=[
        explain(
            "How insulation works",
            "<p>Energy is transferred from a hot object to its cooler surroundings by heating — conduction through solids, convection in fluids, radiation. <b>Thermal insulation</b> slows this down: an <b>insulator</b> has a <b>low thermal conductivity</b>, and most good insulators work by <b>trapping air</b> in small pockets (foam, fibreglass, wool, feathers, bubble wrap), because still air is a poor conductor and the pockets stop it convecting. Thicker insulation, more layers and a smaller surface area all reduce the rate of transfer. The <b>vacuum flask</b> removes the air altogether between its double walls (no conduction or convection) and silvers the surfaces (less radiation).</p>"
            "<p>The spec's examples: <b>lagging</b> a hot-water tank or pipes, <b>loft insulation</b>, <b>cavity-wall</b> insulation, <b>double glazing</b> (a trapped layer of air or gas between the panes), a lid on a beaker, a cup sleeve. In the SHC practical (T6) the beaker is <b>lagged</b> so that nearly all the heater's energy goes into the water. The June 2025 report (Q3(d)): students explained a thick cable's plastic coating as \"thermal insulation to prevent energy loss\" — wrong: \"wasted heat can only be reduced by lowering resistance, and insulation at best only reduces transfer of that heat to the air\". The plastic is <b>electrical</b> insulation (Topic 10); thermal insulation is about reducing transfer by heating.</p>",
        ),
        worked(
            "The hot drink",
            "A cafe serves hot drinks in cups with a cardboard sleeve and a lid. Explain how these reduce the rate at which the drink cools. (3 marks)",
            [
                "The sleeve is a <b>thermal insulator</b> with a <b>low thermal conductivity</b> (corrugated card traps <b>air</b>), so less energy is conducted through the side of the cup each second.",
                "The lid stops the hot vapour and air above the drink escaping — it reduces transfer by <b>convection</b> and by <b>evaporation</b> from the surface.",
                "With less energy transferred to the surroundings each second, the drink's temperature falls more slowly.",
            ],
        ),
        practice("Insulation", [
            written("pm-n8-q1", "Explain how loft insulation reduces the rate of energy transfer out of a house. (2)",
                    marks(["The fibreglass or wool has a <b>low thermal conductivity</b> and <b>traps air</b> in small pockets (air is a poor conductor and cannot convect in the pockets).", "So energy is <b>conducted</b> through the roof space more slowly: less energy transferred to the outside each second."]), lines=2),
            choice("pm-n8-q2", "A thick plastic coating on an electrical cable is…",
                   ["thermal insulation that stops the cable wasting energy", "electrical insulation; wasted energy in the cable is reduced by lowering its resistance, not by the coating", "a conductor", "lagging"], 1,
                   "2025 report: the coating does not reduce the heating; a lower resistance does."),
            written("pm-n8-q3", "A vacuum flask keeps a drink hot. Explain how the vacuum between its double walls helps. (2)",
                    marks(["There are <b>no particles</b> in a vacuum, so energy cannot be transferred across the gap by <b>conduction or convection</b>.", "Only radiation can cross it, and the silvered surfaces reduce that — so the drink loses energy very slowly."]), lines=2),
            choice("pm-n8-q4", "Which change would increase the rate at which a beaker of hot water cools?",
                   ["Adding a lid", "Wrapping it in foam", "Pouring the water into a wide shallow dish", "Standing it on a cork mat"], 2,
                   "A larger surface area in contact with the air: faster transfer."),
            choice("pm-n8-q5", "Why does double glazing use two panes with a gap rather than one thick pane?",
                   ["Glass is a good conductor, so thicker glass helps little; the trapped air (or gas) between the panes has a low thermal conductivity", "Two panes are stronger", "The gap lets light through", "It is cheaper"], 0,
                   "The gap is the insulator."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N9 · Gas pressure and temperature
# ---------------------------------------------------------------------

section_n9 = section(
    "gas-pressure", "nn", "Gas pressure from particle collisions, and what heating does to it", "14.12, 14.13",
    equations=[r"\text{collisions with the walls} \rightarrow \text{force} \rightarrow \text{pressure}", r"\text{hotter} \rightarrow \text{faster} \rightarrow \text{more frequent, harder collisions}"],
    blurb="Gas particles move fast and randomly and collide with the walls of their container; each collision exerts a small force on the wall, and the total force per unit area is the pressure. Heat the gas (at constant volume) and the particles move faster, so they hit the walls more often and harder, and the pressure rises.",
    checklist=[
        "Explain the pressure of a gas in terms of particle collisions",
        "Explain why heating a fixed mass of gas at constant volume increases its pressure",
        "Write the chain in the mark-scheme words: faster → more frequent and harder collisions → greater force → greater pressure",
    ],
    parts=[
        explain(
            "The collision chain",
            diagram(dg.pressure_svg(), 670, 275, "A cold and a hot gas in the same volume: the faster particles hit the walls more often and harder.") +
            "<p><b>Why a gas has a pressure</b> (14.12): the particles move <b>fast</b> and <b>randomly</b>; they <b>collide with the walls</b> of the container; each collision exerts a <b>force on the wall</b> (the particle's momentum is changed, so the wall pushes it and it pushes the wall — Topic 2); with billions of collisions each second the total force on each unit of area is steady — that is the <b>pressure</b>.</p>"
            "<p><b>Heating a fixed mass of gas at constant volume</b> (14.13): the particles gain kinetic energy and move <b>faster</b> (the average speed rises); so they <b>collide with the walls more often</b> (more collisions per second) <b>and harder</b> (each collision exerts a larger force); so the <b>total force</b> on the walls increases; so the <b>pressure increases</b>. Cool it and everything reverses. The chain needs <b>both</b> \"more frequent\" and \"harder\" (greater force per collision) for full marks, and it must say the <b>walls</b> — \"the particles bump into each other more\" earns nothing, because collisions between particles do not push on the container.</p>",
        ),
        worked(
            "A sealed can in the sun",
            "A sealed can of gas is left in the sun and warms up. Explain why the pressure inside the can increases. (3 marks)",
            [
                "The gas particles gain energy and move <b>faster</b> (their average speed increases).",
                "So they <b>collide with the walls</b> of the can <b>more frequently</b> and with <b>more force</b> each time (harder).",
                "The volume is fixed, so the total force on each unit of area of the walls increases: the <b>pressure increases</b>.",
            ],
        ),
        practice("Gas pressure", [
            written("pm-n9-q1", "Explain how the particles of a gas produce a pressure on the walls of their container. (3)",
                    marks(["The particles move <b>fast and randomly</b> and <b>collide with the walls</b>.", "Each collision exerts a <b>force on the wall</b>.", "The total force of all the collisions per unit area of wall is the <b>pressure</b>."]), lines=3),
            choice("pm-n9-q2", "A fixed mass of gas at constant volume is cooled. Its pressure…",
                   ["increases", "decreases, because the particles move more slowly and hit the walls less often and less hard", "stays the same", "becomes zero"], 1,
                   "The chain in reverse."),
            choice("pm-n9-q3", "Which statement earns nothing in a gas-pressure explanation?",
                   ["The particles collide with the walls", "The particles collide with each other more often", "Each collision exerts a force on the wall", "The particles move faster when heated"], 1,
                   "Particle–particle collisions do not push on the container."),
            written("pm-n9-q4", "A sealed rigid container of gas is heated from 20 °C to 80 °C. Explain the effect on the pressure. (3)",
                    marks(["The particles move <b>faster</b> (greater average speed / kinetic energy).", "So they hit the walls <b>more often</b> and <b>harder</b> (greater force per collision).", "The volume is constant, so the total force per unit area — the <b>pressure</b> — <b>increases</b>."]), lines=3),
            choice("pm-n9-q5", "In a sealed can heated in the sun (2024 Q9(b)), which quantity does NOT increase?",
                   ["The average speed of the particles", "The pressure", "The mean distance between the particles", "The energy of the particles"], 2,
                   "Constant volume and the same number of particles: the spacing cannot change."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N10 · Absolute zero and kelvin
# ---------------------------------------------------------------------

section_n10 = section(
    "kelvin-nn", "nn", "Absolute zero and the kelvin scale", "14.14, 14.15",
    equations=[r"T(\text{K}) = \theta(°\text{C}) + 273", r"\theta(°\text{C}) = T(\text{K}) - 273"],
    blurb="Cool a gas and its particles slow down; at −273 °C they would have the least possible energy and the pressure would be zero — absolute zero, the bottom of the kelvin scale. Kelvin and Celsius degrees are the same size, so converting is adding or subtracting 273, and a temperature change is the same number on both scales.",
    checklist=[
        "Describe absolute zero in terms of particle movement",
        "Convert between kelvin and degrees Celsius",
        "State that a temperature change is the same in K and °C, and that 0 K is the lowest possible temperature",
    ],
    parts=[
        explain(
            "The scale that starts at the bottom",
            diagram(dg.kelvin_svg(), 660, 270, "The Celsius and kelvin scales: the same size of degree, zero in different places.") +
            "<p>As a gas is cooled its particles move more and more slowly and its pressure falls. Extrapolating, at <b>−273 °C</b> the particles would have the <b>least possible movement</b> (the lowest possible energy) and the pressure would be zero: this is <b>absolute zero</b>, the lowest temperature there can be — nothing can be colder, because there is no movement left to take away. The spec's words (14.14): absolute zero, −273 °C, \"in terms of the <b>lack of movement</b> of particles\".</p>"
            "<p>The <b>kelvin scale</b> starts there: 0 K = −273 °C, so <b>$T(\\text{K}) = \\theta(°\\text{C}) + 273$</b> and <b>$\\theta(°\\text{C}) = T(\\text{K}) - 273$</b>. The degree is the same size on both scales, so a <b>change</b> of temperature is the same number in K as in °C (a rise of 20 °C is a rise of 20 K) — and there are <b>no negative kelvin temperatures</b>. Ice melts at 273 K, water boils at 373 K, room temperature is about 293 K. The kelvin is the SI unit of temperature, and the scale scientists use for gases, because its zero is a real zero: at 0 K the particles have the least possible energy and a gas would exert no pressure.</p>",
        ),
        worked(
            "Both ways",
            "(a) Convert 25 °C to kelvin. (b) Convert 200 K to degrees Celsius. (c) A gas is heated from 300 K to 350 K; state the temperature change in °C. (3 marks)",
            [
                "(a) $25 + 273 = 298$ K.",
                "(b) $200 - 273 = -73$ °C.",
                "(c) A change of 50 K is a change of <b>50 °C</b> — the degree is the same size on both scales.",
            ],
        ),
        practice("Absolute zero and kelvin", [
            numeric("pm-n10-q1", "Convert 37 °C to kelvin.", 310, "K",
                    "Add 273.",
                    [r"$37 + 273 = 310$ K"]),
            numeric("pm-n10-q2", "Convert 77 K (liquid nitrogen) to degrees Celsius.", -196, "°C",
                    "Subtract 273.",
                    [r"$77 - 273 = -196$ °C"]),
            written("pm-n10-q3", "Describe what is meant by absolute zero. (2)",
                    marks(["The <b>lowest possible temperature</b>, <b>−273 °C</b> (0 K)…", "…at which the particles have the <b>least possible movement</b> (lowest possible energy) — a gas would exert no pressure."]), lines=2),
            choice("pm-n10-q4", "A temperature rise of 15 °C is a rise of…",
                   ["288 K", "15 K", "−258 K", "15 ÷ 273 K"], 1,
                   "Changes are the same on both scales; only the zero differs."),
            choice("pm-n10-q5", "Which temperature is impossible?",
                   ["−100 °C", "0 K", "−10 K", "1000 K"], 2,
                   "Nothing is below absolute zero."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N11 · Compressing a gas [P]
# ---------------------------------------------------------------------

section_n11 = section(
    "compressing-gas", "nn", "Compressing a gas: the force on the walls, and P₁V₁ = P₂V₂ at constant temperature", "14.16P–14.19P",
    equations=[r"P_1 V_1 = P_2 V_2", r"\text{smaller volume} \rightarrow \text{more frequent collisions} \rightarrow \text{higher pressure}"],
    blurb="A gas can be squeezed into a smaller volume or allowed to expand; its pressure exerts a net force at right angles to every surface it touches. Halve the volume of a fixed mass of gas at constant temperature and each particle hits the walls twice as often, so the pressure doubles: pressure × volume stays constant.",
    tags=["P"],
    checklist=[
        "Explain that a gas can be compressed or expanded by changing the pressure, and that its pressure produces a net force at right angles to any surface",
        "Explain why reducing the volume at constant temperature increases the pressure",
        "Use $P_1 V_1 = P_2 V_2$ for a fixed mass of gas at constant temperature",
    ],
    parts=[
        explain(
            "Volume down, pressure up",
            diagram(dg.boyle_svg(), 670, 265, "The same gas at the same temperature in half the volume: twice as many collisions with the walls each second, twice the pressure.") +
            "<p><b>Compressing and expanding</b> (14.16P, 14.17P): a gas has no fixed volume — push a piston in and the same particles fit into a smaller space; let it out and they spread into the larger one. Because the particles collide with every wall, the gas pressure produces a <b>net force at right angles to any surface</b> (the piston, the walls, your eardrum); the force on a surface is pressure × area (Topic 15), which is why a small pressure on a large area is a large force.</p>"
            "<p><b>The volume chain</b> (14.18P), at constant temperature so the particles' <b>speed is unchanged</b>: a smaller volume means the particles have <b>less distance to travel between the walls</b>, so each particle <b>hits the walls more often</b> (more collisions per second); the collisions are <b>no harder</b> than before (same speed); but there are more of them on a smaller area, so the <b>force per unit area</b> — the pressure — <b>increases</b>. The relationship is exact: $P_1 V_1 = P_2 V_2$ (14.19P), pressure inversely proportional to volume for a <b>fixed mass</b> of gas at <b>constant temperature</b>. Pressure can be in any unit as long as both pressures are in the same one (Pa, kPa, atmospheres), and the same for the volumes.</p>",
        ),
        worked(
            "The syringe",
            "A sealed syringe holds 80 cm³ of air at a pressure of 100 kPa. The plunger is pushed in slowly until the volume is 25 cm³. Calculate the new pressure, and state the assumption you made. (3 marks)",
            [
                "$P_1 V_1 = P_2 V_2$, so $P_2 = P_1 V_1 \\div V_2 = 100 \\times 80 \\div 25$.",
                "$P_2 = 320$ kPa — the volume is 3.2 times smaller, so the pressure is 3.2 times larger.",
                "Assumption: the <b>temperature stays constant</b> (pushed in slowly, so the gas does not warm up) and no air escapes (fixed mass).",
            ],
        ),
        practice("Compressing a gas", [
            numeric("pm-n11-q1", "A gas occupies 2.0 m³ at 150 kPa. Calculate its volume when the pressure is increased to 300 kPa at constant temperature.", 1.0, "m³",
                    "$V_2 = P_1 V_1 \\div P_2$.",
                    ewau(r"V_2 = P_1 V_1 \div P_2", r"V_2 = 150 \times 2.0 \div 300", "1.0", "m³")),
            numeric("pm-n11-q2", "A diver's air bubble has a volume of 5.0 cm³ at a depth where the pressure is 400 kPa. Calculate its volume at the surface, where the pressure is 100 kPa (same temperature).", 20, "cm³",
                    "Pressure ÷ 4, so volume × 4.",
                    ewau(r"V_2 = P_1 V_1 \div P_2", r"V_2 = 400 \times 5.0 \div 100", "20", "cm³")),
            written("pm-n11-q3", "A fixed mass of gas is compressed to half its volume at constant temperature. Explain, in terms of particles, why its pressure doubles. (3)",
                    marks(["The particles' <b>speed is unchanged</b> (same temperature), but they have <b>less distance to travel between the walls</b>…", "…so each particle <b>collides with the walls more often</b> — twice as many collisions per second in half the volume (the collisions are not harder).", "More collisions per second on a smaller wall area means a greater <b>force per unit area</b>: the pressure doubles ($P_1 V_1 = P_2 V_2$)."]), lines=3),
            choice("pm-n11-q4", "The pressure of a gas produces a force on a surface that is…",
                   ["parallel to the surface", "at right angles to the surface", "only on the bottom of the container", "zero on a vertical wall"], 1,
                   "14.17P: a net force at right angles to any surface."),
            choice("pm-n11-q5", "$P_1 V_1 = P_2 V_2$ applies only when…",
                   ["the gas is heated", "the mass of gas is fixed and the temperature is constant", "the volume is constant", "the pressure is atmospheric"], 1,
                   "Change the temperature and the speeds change too — the equation no longer holds."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N12 · Key words
# ---------------------------------------------------------------------

DEFINITIONS = [
    ("Density", "<b>Mass per unit volume</b>: $\\rho = m / V$, in kg/m³.", "\"how heavy it is\""),
    ("Internal energy", "The <b>total energy stored in a system by its particles</b>: their kinetic energy (movement) plus their potential energy (positions / bonds).", "\"heat\""),
    ("Specific heat capacity", "The energy needed to raise the temperature of <b>1 kg</b> of a substance by <b>1 °C</b> (J/kg °C).", "missing the 1 kg or the 1 °C"),
    ("Specific latent heat", "The energy needed to change the state of <b>1 kg</b> of a substance <b>without a change in temperature</b> (J/kg); fusion for melting, vaporisation for boiling.", "missing \"no change in temperature\""),
    ("Melting point / boiling point", "The temperature at which a substance <b>changes state</b> (solid ↔ liquid; liquid ↔ gas) — the temperature stays constant while it does.", "\"when it gets hot\""),
    ("Sublimation", "A change <b>directly from solid to gas</b> (dry ice, iodine).", "confusing with evaporation"),
    ("Physical change", "A change in which <b>no new substance is formed</b> (e.g. a change of state); mass is conserved and the original properties return when it is reversed.", "\"a change you can see\""),
    ("Pressure (of a gas)", "The <b>force per unit area</b> exerted on a surface by the <b>collisions</b> of the gas particles with it.", "\"how squashed the gas is\""),
    ("Absolute zero", "The <b>lowest possible temperature</b>, <b>−273 °C</b> (0 K), at which the particles have the <b>least possible movement</b> (energy).", "\"when everything freezes\""),
    ("Kelvin scale", "The temperature scale that starts at <b>absolute zero</b>: $T(\\text{K}) = \\theta(°\\text{C}) + 273$; the same size of degree as Celsius.", "a scale with a different degree size"),
    ("Thermal insulator", "A material with a <b>low thermal conductivity</b> (usually trapping air) that <b>reduces the rate of energy transfer</b> by heating.", "\"stops heat\""),
    ("Conservation of mass (in a change of state)", "The <b>mass is the same before and after</b> a change of state, because the same particles are present — only their arrangement and movement change.", "\"nothing changes\""),
]


def definitions_table():
    html = "<table class='tbl'><tr><th>Term</th><th>What to write (mark-scheme form)</th><th>Not this</th></tr>"
    for term, definition, wrong in DEFINITIONS:
        html += "<tr><td><b>" + term + "</b></td><td>" + definition + "</td><td>" + wrong + "</td></tr>"
    html += "</table>"
    return html


section_keywords = section(
    "keywords-particle", "nn", "Key words: state what is meant by…", "14.1–14.20P",
    equations=[r"\text{definition, word for word}"],
    blurb="One-mark definitions in the form of words the mark schemes credit. The two that lose marks most are specific heat capacity without the 1 kg and 1 °C, and specific latent heat without \"no change in temperature\".",
    checklist=[
        "Define density, internal energy, specific heat capacity and specific latent heat",
        "Define melting and boiling point, sublimation and physical change",
        "Define gas pressure, absolute zero, the kelvin scale and a thermal insulator",
    ],
    parts=[
        explain("The definitions", "<p>\"<b>State what is meant by</b>\" asks for the definition. Learn these as sentences.</p>" + definitions_table()),
        practice("Key words", [
            written("pm-kw-q1", "State what is meant by density. (1)",
                    marks(["<b>Mass per unit volume</b> (mass ÷ volume)."]), lines=1),
            written("pm-kw-q2", "State what is meant by the specific latent heat of fusion of a substance. (1)",
                    marks(["The energy needed to change <b>1 kg</b> of the substance from solid to liquid (melt it) <b>without a change in temperature</b>."]), lines=1),
            choice("pm-kw-q3", "Which is the best definition of absolute zero?",
                   ["The temperature at which water freezes", "The lowest possible temperature, −273 °C, at which particles have the least possible movement", "The temperature of space", "0 °C"], 1,
                   "$-273\\ °\\text{C} = 0\\ \\text{K}$; least possible movement."),
            written("pm-kw-q4", "State what is meant by the internal energy of a system. (1)",
                    marks(["The <b>total</b> energy stored by its particles: their <b>kinetic energy</b> plus their <b>potential energy</b>."]), lines=1),
            choice("pm-kw-q5", "The pressure of a gas on a surface is…",
                   ["the number of particles", "the force per unit area from the particles' collisions with the surface", "the weight of the gas", "the temperature of the gas"], 1,
                   "Force per unit area, from the particles' collisions with the surface."),
        ]),
    ],
)

FACTS_KW = [fact("State what is meant by: " + term[0].lower() + term[1:] + ".", definition, "keywords-particle") for term, definition, wrong in DEFINITIONS]

SECTIONS = [section_n1, section_n2, section_n3, section_n4, section_n5, section_n6, section_n7, section_n8, section_n9, section_n10, section_n11, section_keywords]
