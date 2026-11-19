"""
fe_nn.py — Topic 9 (Forces and their effects): the non-negotiables N1–N10.

N1 Contact and non-contact forces     N6  Moment of a force [P]
N2 Interaction pairs                  N7  The principle of moments [P]
N3 Vectors and scalars                N8  Levers and gears [P]
N4 Free body force diagrams           N9  Lubrication
N5 Resultant force along a line       N10 Key words
"""

from revlib import (
    choice, diagram, ewau, explain, fact, group, mark_scheme, marks, numeric,
    practice, section, worked, written,
)
import fe_diagrams as dg

# ---------------------------------------------------------------------
# N1 · Contact and non-contact forces
# ---------------------------------------------------------------------

section_n1 = section(
    "force-types", "nn", "Contact and non-contact forces", "9.1",
    equations=[r"\text{non-contact: gravitational, electrostatic, magnetic fields}", r"\text{contact: normal contact force, friction, tension, drag, upthrust}"],
    blurb="Every force is one object acting on another. Some need the objects to touch; some act across a gap through a field. Naming the right force, and the field behind it, is the first mark in most Paper 2 force questions.",
    checklist=[
        "Give examples of forces that act at a distance and name the field responsible",
        "Give examples of contact forces, including normal contact force and friction",
        "Describe what a field is",
    ],
    parts=[
        explain(
            "The two kinds",
            "<table class='tbl'><tr><th>Non-contact forces</th><th>Field</th><th>Example</th></tr>"
            "<tr><td><b>Gravitational</b> (weight)</td><td>gravitational field — a region where a <b>mass</b> experiences a force</td><td>the Earth pulls an apple down; the Sun holds the planets</td></tr>"
            "<tr><td><b>Electrostatic</b></td><td>electric field — a region where a <b>charge</b> experiences a force</td><td>a charged balloon lifts hair; like charges repel</td></tr>"
            "<tr><td><b>Magnetic</b></td><td>magnetic field — a region where a <b>magnetic material</b> (or another magnet, or a current) experiences a force</td><td>a magnet lifts a paperclip; two north poles repel</td></tr></table>"
            "<table class='tbl'><tr><th>Contact forces</th><th>What it is</th><th>Example</th></tr>"
            "<tr><td><b>Normal contact force</b> (reaction)</td><td>a surface pushing back on whatever presses on it, always at <b>right angles</b> (normal) to the surface</td><td>the table holding up a book</td></tr>"
            "<tr><td><b>Friction</b></td><td>the force between two surfaces that <b>opposes</b> their sliding; it transfers energy to the thermal store</td><td>brakes; shoes gripping the floor</td></tr>"
            "<tr><td><b>Tension</b></td><td>the pull along a stretched rope, string or cable</td><td>a crane cable</td></tr>"
            "<tr><td><b>Drag</b> (air resistance, water resistance)</td><td>friction with a fluid, opposing motion through it</td><td>a parachute</td></tr>"
            "<tr><td><b>Upthrust</b></td><td>the upward push of a fluid on an object in it</td><td>a boat floating</td></tr></table>"
            "<p>The June 2024 scheme (Q1(b)) credited \"a region where a charge experiences a force\" for an electric field; the same shape of sentence does for the other two fields. The June 2023 report (Q5(b), a magnet floating above another): \"many answers had the words <i>magnetic fields</i> but usually in terms of repelling\" — say that the <b>fields interact</b> to produce the force, then that the repulsion <b>balances the weight</b>. The 2024 scheme (Q4(a)) and 2023 report (Q4(a)(iv)): a normal contact force arrow is drawn <b>at right angles to the surface</b> and must <b>start or end at the point</b> where it acts.</p>",
        ),
        worked(
            "Naming the forces",
            "A magnet is held above a second magnet so that it floats. Explain how the forces on the upper magnet keep it at rest. (3 marks)",
            [
                "The <b>magnetic fields</b> of the two magnets <b>interact</b> (like poles facing), producing a <b>repulsive</b> force upwards on the upper magnet — a <b>non-contact</b> force.",
                "The Earth's gravitational field pulls the upper magnet down: its <b>weight</b>, also non-contact.",
                "The repulsion is <b>equal in size and opposite</b> to the weight, so the <b>resultant force is zero</b> and the magnet stays at rest.",
            ],
        ),
        practice("Contact and non-contact", [
            choice("fe-n1-q1", "Which of these is a non-contact force?",
                   ["Friction", "Tension", "Weight", "Normal contact force"], 2,
                   "Weight is the gravitational force — it acts through the gravitational field without touching."),
            written("fe-n1-q2", "A book rests on a table. Name the two forces acting on the book and state whether each is a contact or non-contact force. (2)",
                    marks(["Its <b>weight</b> (gravitational force, downwards) — <b>non-contact</b>.", "The <b>normal contact force</b> from the table (upwards) — <b>contact</b>."]), lines=2),
            written("fe-n1-q3", "State what is meant by a gravitational field. (1)",
                    marks(["A <b>region</b> in which a <b>mass experiences a force</b>."]), lines=1),
            choice("fe-n1-q4", "Two charged balloons push each other apart. Which field is responsible?",
                   ["Gravitational", "Magnetic", "Electrostatic (electric)", "None — they are touching"], 2,
                   "Charges interact through electric fields."),
            written("fe-n1-q5", "A box is pushed along a floor at constant speed. Name the contact force that opposes the motion and describe what it does to the energy of the box. (2)",
                    marks(["<b>Friction</b> between the box and the floor.", "It transfers energy from the box's kinetic store to the <b>thermal store</b> of the surfaces (they warm up), so the push is needed just to keep the speed constant."]), lines=2),
            written("fe-n1-q6", "A block rests on a slope. Describe the direction of the normal contact force on the block. (1)",
                    marks(["At <b>right angles to the surface of the slope</b> (not vertically upwards), pushing away from the slope."]), lines=1),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N2 · Interaction pairs
# ---------------------------------------------------------------------

section_n2 = section(
    "force-pairs", "nn", "Interaction pairs: forces come in twos", "9.1",
    equations=[r"\text{A on B} = -\,\text{B on A}"],
    blurb="Whenever two objects interact, each exerts a force on the other: equal in size, opposite in direction, the same type, one on each object. These pairs are not the same thing as two balanced forces on one object — the exam trap of the topic.",
    checklist=[
        "State the four properties of an interaction pair",
        "Identify both forces of a pair in a situation",
        "Distinguish an interaction pair from balanced forces on one object",
    ],
    parts=[
        explain(
            "Pairs and how to spot them",
            diagram(dg.pair_svg(), 640, 275, "Left: an interaction pair — one force on each object. Right: two balanced forces on the same object, which is not a pair.") +
            "<p>An <b>interaction pair</b> (Newton's third law pair) is two forces that are <b>equal in size</b>, <b>opposite in direction</b>, of the <b>same type</b> (both gravitational, or both contact…), and act on <b>different objects</b>. Written as a sentence: \"<i>the Earth pulls the book down with 5 N; the book pulls the Earth up with 5 N</i>\". Swap the two nouns and the force is its partner.</p>"
            "<p>The <b>weight of the book and the normal contact force from the table</b> are <b>not</b> a pair: they act on the <b>same</b> object (the book) and are <b>different types</b> (gravity and contact). They happen to be equal because the book is in equilibrium; tip the table and they are no longer equal, while the real pairs stay equal always.</p>"
            "<p>Both forces of a pair are <b>vectors</b> — they can be drawn as arrows of the same length pointing opposite ways, one on each object (9.1c).</p>",
        ),
        worked(
            "The pair to the weight",
            "A student says: \"The weight of a cup on a table and the normal contact force from the table are an interaction pair because they are equal and opposite.\" Explain why the student is wrong and identify the correct partner force to the cup's weight. (3 marks)",
            [
                "The two forces the student names both act on the <b>same object</b> (the cup) and are <b>different types</b> (gravitational and contact), so they cannot be an interaction pair — pairs act on <b>different</b> objects and are the same type.",
                "They are equal only because the cup is <b>in equilibrium</b> (balanced forces), not because they are a pair.",
                "The partner to the weight (the Earth pulling the cup down) is the <b>cup pulling the Earth up</b> with an equal gravitational force.",
            ],
        ),
        practice("Interaction pairs", [
            written("fe-n2-q1", "State the four features of an interaction pair of forces. (2)",
                    marks(["<b>Equal</b> in size and <b>opposite</b> in direction…", "…of the <b>same type</b>, acting on <b>different objects</b>. (Two features per mark.)"]), lines=2),
            choice("fe-n2-q2", "A footballer kicks a ball with a force of 200 N. What is the partner force?",
                   ["The ball's weight, 200 N", "The ball pushing on the boot with 200 N", "Friction on the ball, 200 N", "The ground pushing up on the footballer"], 1,
                   "Swap the nouns: boot on ball ↔ ball on boot, same size, opposite direction."),
            written("fe-n2-q3", "A rocket pushes exhaust gas downwards. Identify the partner force and explain how it makes the rocket accelerate upwards. (2)",
                    marks(["The <b>gas pushes the rocket upwards</b> with an equal and opposite force.",
                           "If that upward force is larger than the rocket's weight there is a <b>resultant upward force</b>, so it accelerates upwards."]), lines=2),
            choice("fe-n2-q4", "A book rests on a table. Which pair of forces is an interaction pair?",
                   ["The book's weight and the normal contact force on the book", "The normal contact force on the book and the book's push on the table", "The book's weight and friction", "The table's weight and the book's weight"], 1,
                   "Table pushes book up / book pushes table down: same type (contact), different objects."),
            written("fe-n2-q5", "A swimmer pushes backwards on the water with her hands. Explain how this moves her forwards. (2)",
                    marks(["The water pushes <b>forwards on her hands</b> with an <b>equal and opposite</b> force (the interaction pair).",
                           "This forward force on the swimmer is greater than the drag, giving a resultant force forwards, so she accelerates."]), lines=2),
            written("fe-n2-q6", "An apple of weight 1 N hangs from a tree. State the size and direction of the gravitational force the apple exerts on the Earth. (1)",
                    marks(["<b>1 N</b>, <b>upwards</b> (towards the apple) on the Earth."]), lines=1),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N3 · Vectors and scalars
# ---------------------------------------------------------------------

section_n3 = section(
    "vectors-scalars-nn", "nn", "Vectors and scalars", "9.2",
    equations=[r"\text{vector: size and direction}", r"\text{scalar: size only}"],
    blurb="A vector has a size and a direction; a scalar has size only. Force is a vector, which is why it is drawn as an arrow and why two forces can add to less than their sum.",
    checklist=[
        "Define vector and scalar quantities",
        "Sort force, velocity, displacement, acceleration, momentum, speed, distance, mass, energy, time, temperature",
        "Explain how an arrow represents a vector",
    ],
    parts=[
        explain(
            "The lists and the arrow",
            "<table class='tbl'><tr><th>Vectors (size <b>and</b> direction)</th><th>Scalars (size only)</th></tr>"
            "<tr><td>force, weight, velocity, displacement, acceleration, momentum</td><td>speed, distance, mass, energy, work done, power, time, temperature, density, pressure*</td></tr></table>"
            "<p>*Pressure acts in all directions at a point, so it is a scalar; the <i>force</i> it produces on a surface is a vector.</p>"
            "<p>A vector is drawn as an <b>arrow</b>: the <b>length</b> shows the size (to a stated scale) and the <b>arrowhead</b> shows the direction. Two vectors are only equal if both size and direction match — which is why a car going round a bend at a steady 30 mph has a constant <b>speed</b> but a changing <b>velocity</b> (Topic 2).</p>"
            "<p>Explain-the-difference questions want an <b>example pair</b>: \"speed is a scalar — 5 m/s; velocity is a vector — 5 m/s north\", or \"mass is a scalar — 2 kg; weight is a vector — 20 N downwards\".</p>",
        ),
        worked(
            "The 2-mark explanation",
            "Explain the difference between a vector quantity and a scalar quantity, giving an example of each. (2 marks)",
            [
                "A <b>vector</b> has both a <b>size (magnitude) and a direction</b>; a <b>scalar</b> has <b>size only</b>.",
                "Example: <b>force</b> (10 N to the left) is a vector; <b>mass</b> (2 kg) is a scalar. Any correct pair scores.",
            ],
        ),
        practice("Vectors and scalars", [
            choice("fe-n3-q1", "Which row is all vectors?",
                   ["Speed, mass, time", "Force, velocity, displacement", "Energy, force, distance", "Momentum, temperature, acceleration"], 1,
                   "Speed, mass, time, energy, distance and temperature are scalars."),
            written("fe-n3-q2", "State what is meant by a vector quantity. (1)",
                    marks(["A quantity that has both <b>size (magnitude) and direction</b>."]), lines=1),
            choice("fe-n3-q3", "Which quantity is a scalar?",
                   ["Weight", "Acceleration", "Work done", "Momentum"], 2,
                   "Work done (energy transferred) has no direction."),
            written("fe-n3-q4", "A diagram shows a force as an arrow. State what the length and the direction of the arrow represent. (2)",
                    marks(["The <b>length</b> represents the <b>size</b> of the force (to a scale).", "The <b>direction</b> of the arrow is the <b>direction</b> of the force."]), lines=2),
            written("fe-n3-q5", "Two forces of 6 N act on an object. Explain why the resultant force could be anything from 0 N to 12 N. (2)",
                    marks(["Force is a <b>vector</b>, so the resultant depends on the <b>directions</b> as well as the sizes.",
                           "In the same direction they add to 12 N; in opposite directions they cancel to 0 N; at an angle, somewhere between."]), lines=2),
            choice("fe-n3-q6", "A car travels at a steady 20 m/s round a roundabout. Which statement is correct?",
                   ["Its speed and velocity are both constant", "Its speed is constant but its velocity changes because its direction changes", "Its velocity is constant but its speed changes", "Neither is constant"], 1,
                   "Velocity is a vector: changing direction is a changing velocity."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N4 · Free body force diagrams
# ---------------------------------------------------------------------

section_n4 = section(
    "free-body", "nn", "Free body force diagrams", "9.4",
    equations=[r"\text{one object, arrows from its centre, labelled, to scale}"],
    blurb="A free body diagram shows all the forces on one object and nothing else. The marks are for arrows that start at (or point through) the centre, point the right way, are labelled with their sizes, and have lengths in proportion.",
    checklist=[
        "Draw a free body diagram for an object at rest, moving steadily, and accelerating",
        "Label each arrow with the name and size of the force",
        "Read the resultant force off a free body diagram",
    ],
    parts=[
        explain(
            "The rules",
            diagram(dg.free_body_svg(), 700, 270, "A block on a table, its free body diagram, and the version that loses the marks.") +
            "<ol><li><b>One object only.</b> Draw it as a box or a dot; leave out the table, the ground, the rope — only the <b>forces they exert on the object</b> appear.</li>"
            "<li><b>Every arrow starts at the centre</b> of the object (or its line passes through the centre). On a <i>picture of the situation</i> a force is drawn where it acts — a contact force at the point of contact (N1); on a <i>free body diagram</i> the object is a box or a dot and every force is drawn from its centre. The June 2025 report (Q8(b)(iii)): \"examiners were looking for correctly labelled vectors that would both pass through the centre of the block\"; arrows near the edges were penalised because the block would spin.</li>"
            "<li><b>Direction</b>: weight straight down; normal contact force at right angles to the surface; friction and drag against the motion; tension along the rope.</li>"
            "<li><b>Label</b> each arrow with the force's <b>name and size</b>. \"Force vectors must have a size as well as a direction\" — unlabelled arrows scored 1 of 2.</li>"
            "<li><b>Lengths in proportion</b>: equal forces, equal arrows; a 10 N arrow twice as long as a 5 N one.</li></ol>"
            "<p>Reading one: if the arrows balance (equal and opposite in every direction) the resultant is zero and the object is at rest or moving at constant velocity; a longer arrow one way means a resultant that way and an acceleration that way (N5).</p>",
        ),
        worked(
            "Three situations",
            "Describe the free body diagrams for (a) a book at rest on a table, (b) a car moving at constant velocity along a flat road, (c) a skydiver just after jumping. (3 marks)",
            [
                "<b>(a)</b> Two arrows from the centre: <b>weight</b> down and <b>normal contact force</b> up, <b>equal lengths</b>.",
                "<b>(b)</b> Four arrows: weight down and normal contact force up, equal; <b>driving force</b> forwards and <b>drag + friction</b> backwards, <b>equal</b> — constant velocity means zero resultant.",
                "<b>(c)</b> Weight down, <b>long</b>; air resistance up, <b>short</b> — the resultant is downwards, so the skydiver accelerates downwards.",
            ],
        ),
        practice("Free body diagrams", [
            written("fe-n4-q1", "A 5 N block rests on a table. Describe the free body diagram for the block. (2)",
                    marks(["A <b>5 N weight</b> arrow straight <b>down</b> from the centre, and a <b>5 N normal contact force</b> arrow straight <b>up</b> through the centre.",
                           "The two arrows are the <b>same length</b> and both labelled with 5 N."]), lines=2),
            choice("fe-n4-q2", "A student draws the weight arrow of a block starting at its bottom-left corner. Why does this lose a mark?",
                   ["Weight acts upwards", "Force arrows must pass through the centre of the object — drawn at a corner, the force would make the block rotate", "The arrow is too long", "Weight is not a force"], 1,
                   "The 2025 report's exact point."),
            written("fe-n4-q3", "A sledge is pulled along flat snow by a rope at constant speed. Name the four forces on the sledge's free body diagram and state which pairs are equal. (3)",
                    mark_scheme([
                        ("Vertical", "<b>Weight</b> down and <b>normal contact force</b> up — equal."),
                        ("Horizontal", "<b>Tension</b> in the rope forwards and <b>friction</b> backwards — equal (constant speed, zero resultant)."),
                        ("Drawing", "All four from the centre, labelled, equal pairs the same length."),
                    ]), lines=3),
            choice("fe-n4-q4", "A free body diagram of a car shows a 2000 N driving force forwards and 1500 N of drag backwards. What is the resultant force?",
                   ["3500 N forwards", "500 N forwards", "500 N backwards", "0 N"], 1,
                   "$2000 - 1500 = 500$ N in the direction of the larger force."),
            written("fe-n4-q5", "Explain what the free body diagram of a ball thrown upwards looks like at the top of its flight (ignore air resistance). (2)",
                    marks(["<b>One arrow only</b>: the <b>weight</b>, straight down from the centre.",
                           "There is no upward force — the hand stopped pushing when the ball left it; the weight gives a downward resultant, so the ball accelerates downwards even while momentarily at rest."]), lines=2),
            written("fe-n4-q6", "A block hangs at rest from a string. State the two forces on the block, their directions and how their sizes compare. (2)",
                    marks(["<b>Weight</b> downwards and <b>tension</b> in the string upwards.", "They are <b>equal</b> in size (the block is at rest, so the resultant is zero)."]), lines=2),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N5 · Resultant force along a line
# ---------------------------------------------------------------------

section_n5 = section(
    "resultant-line", "nn", "Resultant force along a line, and balanced forces", "9.4, 9.5 (the basics; Topic 2)",
    equations=[r"\text{same direction: add}", r"\text{opposite: subtract}", r"\text{resultant } 0 \Rightarrow \text{at rest or constant velocity}"],
    blurb="The resultant force is the single force that would have the same effect as all the forces together. Along a line it is add-and-subtract. Zero resultant does not mean 'stopped' — it means the velocity is not changing.",
    checklist=[
        "Calculate the resultant of forces along a line",
        "State what a zero resultant means for the motion",
        "Link the direction of the resultant to the direction of the acceleration",
    ],
    parts=[
        explain(
            "Resultant and what it does",
            "<p>The <b>resultant force</b> is one force that has the <b>same effect</b> as all the forces acting together. Along a line: forces in the <b>same direction add</b>; forces in <b>opposite directions subtract</b>, and the resultant is in the direction of the larger. 700 N forwards and 400 N backwards → 300 N forwards.</p>"
            "<table class='tbl'><tr><th>Resultant</th><th>Motion</th><th>Name</th></tr>"
            "<tr><td><b>zero</b></td><td><b>at rest</b>, or moving at <b>constant velocity</b> (steady speed in a straight line)</td><td>balanced forces, equilibrium</td></tr>"
            "<tr><td><b>not zero</b></td><td><b>accelerates</b> in the direction of the resultant: speeds up, slows down or changes direction ($F = m \\times a$, Topic 2)</td><td>unbalanced forces</td></tr></table>"
            "<p>Two traps. \"Balanced forces\" is not the same as \"no forces\": a car at 70 mph on the motorway has four forces on it, all balanced. And a zero resultant does not mean the object is <b>stationary</b> — a parachutist at terminal velocity has balanced forces and is falling fast.</p>"
            "<p>The spec's phrase (9.5): an <b>isolated object or system</b> — treat the object (or a group of objects moving together, like a car and its trailer) as one thing and add up only the <b>external</b> forces on it; forces between the parts of the system cancel in pairs.</p>",
        ),
        worked(
            "A tug of war",
            "Team A pulls a rope with 1500 N to the left; team B pulls with 1200 N to the right. (a) Calculate the resultant force on the rope. (b) Describe the motion of the rope. (c) Later the teams pull with equal forces. State the resultant and describe the motion. (4 marks)",
            [
                "<b>(a)</b> Opposite directions, so subtract: $1500 - 1200 = 300$ N <b>to the left</b> (the direction of the larger force).",
                "<b>(b)</b> There is a resultant force, so the rope <b>accelerates to the left</b> — it starts moving, speeding up towards team A.",
                "<b>(c)</b> Resultant <b>zero</b>. The forces are <b>balanced</b>: the rope stays at rest if it was at rest, or keeps moving at a <b>constant velocity</b> if it was already moving — it does not have to stop.",
            ],
        ),
        practice("Resultant force", [
            numeric("fe-n5-q1", "A boat's engine pushes it forwards with 3000 N; water resistance is 1800 N. Calculate the resultant force.", 1200, "N", "Opposite directions: subtract.",
                    [r"$3000 - 1800 = 1200$ N forwards."]),
            choice("fe-n5-q2", "The resultant force on a moving object is zero. Which must be true?",
                   ["It is stationary", "It is slowing down", "It moves at constant velocity (or is at rest)", "It is accelerating"], 2,
                   "Zero resultant → velocity does not change."),
            numeric("fe-n5-q3", "Two people push a car in the same direction with 250 N and 300 N; friction is 400 N. Calculate the resultant force.", 150, "N", "Add the two pushes, subtract the friction.",
                    [r"$250 + 300 = 550$ N forwards; $550 - 400 = 150$ N forwards."]),
            written("fe-n5-q4", "A skydiver falls at a constant speed of 50 m/s. A student says the forces on him must be unbalanced because he is moving so fast. Explain why the student is wrong. (2)",
                    marks(["Constant speed in a straight line means the <b>velocity is not changing</b>, so there is <b>no acceleration</b>.",
                           "No acceleration means the <b>resultant force is zero</b>: air resistance <b>equals</b> his weight. Speed itself does not need a resultant force."]), lines=3),
            written("fe-n5-q5", "A lift accelerates upwards. Compare the tension in its cable with the weight of the lift and explain your answer. (2)",
                    marks(["The tension is <b>greater than</b> the weight.", "An acceleration upwards needs a <b>resultant force upwards</b>, so the upward force (tension) must exceed the downward force (weight)."]), lines=2),
            choice("fe-n5-q6", "A car and its trailer are treated as one system. Which force is NOT counted when finding the resultant force on the system?",
                   ["Air resistance on the trailer", "The driving force on the car's tyres", "The pull of the car on the trailer through the tow bar", "Friction on the trailer's wheels"], 2,
                   "The tow-bar forces are internal to the system and cancel as an interaction pair.", tags=["H"]),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N6 · Moment of a force
# ---------------------------------------------------------------------

section_n6 = section(
    "moment-nn", "nn", "Moment of a force: the turning effect", "9.6P, 9.7P",
    equations=[r"M = F \times d", r"\text{N m} = \text{N} \times \text{m}"],
    blurb="A force on something that can pivot makes it turn. The size of the turning effect is the moment: force × the perpendicular distance from the pivot to the line of the force. Longer spanner, bigger moment.",
    tags=["P"],
    checklist=[
        "Describe situations where a force causes rotation",
        "Use moment = force × distance normal to the direction of the force",
        "Use the unit N m, and explain why d must be the perpendicular distance",
    ],
    parts=[
        explain(
            "Moments",
            diagram(dg.moment_svg(), 640, 290, "The same 20 N on the same spanner: at right angles the distance is the full 0.30 m; at an angle the perpendicular distance — and the moment — is smaller.") +
            "<p><b>Situations with rotation</b> (9.6P): a door on its hinges, a spanner on a nut, a see-saw, a wheelbarrow, a crowbar, a bicycle pedal, a steering wheel, scissors, a tap. In each there is a <b>pivot</b> (hinge, nut, fulcrum, axle) and a force applied some distance from it.</p>"
            "<p><b>Moment of a force</b> (9.7P) $= $ force $\\times$ <b>distance normal to the direction of the force</b> (the perpendicular distance from the pivot to the force's line of action). Unit: <b>newton metre, N m</b> (the June 2024 scheme's one-mark question). It is not a joule even though both are $\\text{N} \\times \\text{m}$: in a moment the distance is <i>across</i> the force, in work it is <i>along</i> it.</p>"
            "<p>Why perpendicular: only the part of the force at right angles to the lever turns it. Pushing straight along a spanner towards the nut does nothing; pushing at right angles at the far end does the most. So: <b>bigger force</b> or <b>longer perpendicular distance</b> → bigger moment. That is why door handles are far from the hinges and why a long spanner loosens a stiff nut.</p>"
            "<p>Units trap (June 2022 report, Q6): \"the most common detracting mistake was not converting cm to m\" — a 30 cm spanner is 0.30 m, or the moment comes out 100 times too big.</p>",
        ),
        worked(
            "A door",
            "A door handle is 0.80 m from the hinges. A person pushes the handle with a force of 15 N at right angles to the door. (a) Calculate the moment. (b) Explain why pushing with the same force 0.20 m from the hinges is much harder to open the door with.",
            ewau(r"M = F \times d", r"M = 15 \times 0.80", "12", "N m") + [
                r"<b>(b)</b> At 0.20 m the moment is only $15 \times 0.20 = 3$ N m — a quarter of the turning effect for the same force, so <b>four times the force</b> would be needed for the same moment.",
            ],
        ),
        practice("Moments", [
            numeric("fe-n6-q1", "A spanner is 25 cm long. A mechanic pushes on its end with 60 N at right angles. Calculate the moment about the nut.", 15, "N m", "Convert 25 cm to m first.",
                    ewau(r"M = F \times d", r"M = 60 \times 0.25", "15", "N m")),
            choice("fe-n6-q2", "What is the unit of the moment of a force?",
                   ["N", "J", "N m", "N/m"], 2,
                   "Newton metre. Not the joule, even though $J = N m$ dimensionally, because the distance is perpendicular to the force, not along it."),
            numeric("fe-n6-q3", "A moment of 24 N m is needed to turn a stiff tap. The tap handle is 0.08 m long. Calculate the force needed at its end.", 300, "N", "$F = M \\div d$.",
                    [r"$F = \dfrac{M}{d} = \dfrac{24}{0.08} = 300$ N."]),
            written("fe-n6-q4", "Explain why it is easier to loosen a wheel nut with a long wheel brace than with a short one. (2)",
                    marks(["Moment = force × perpendicular distance; the long brace puts the hand at a <b>greater distance</b> from the nut.",
                           "So the <b>same force produces a bigger moment</b> — or the moment needed to loosen the nut is produced with a <b>smaller force</b>."]), lines=2),
            choice("fe-n6-q5", "A force of 10 N acts on a lever 0.5 m from the pivot, but at 30° to the lever instead of at right angles. The moment is…",
                   ["exactly 5 N m", "more than 5 N m", "less than 5 N m", "zero"], 2,
                   "The perpendicular distance from the pivot to the line of the force is less than 0.5 m, so the moment is less than 10 × 0.5."),
            written("fe-n6-q6", "State what is meant by the moment of a force. (2)",
                    marks(["The <b>turning effect</b> of a force about a pivot.", "Moment = <b>force × perpendicular distance</b> from the pivot to the line of action of the force (N m)."]), lines=2),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N7 · The principle of moments
# ---------------------------------------------------------------------

section_n7 = section(
    "balance-nn", "nn", "The principle of moments", "9.8P",
    equations=[r"\sum M_{\text{clockwise}} = \sum M_{\text{anticlockwise}}", r"F_1 d_1 = F_2 d_2"],
    blurb="If something pivoted is balanced — not turning — the total clockwise moment equals the total anticlockwise moment about the pivot. Say 'sum of', say 'in equilibrium', and show the moment calculations.",
    tags=["P"],
    checklist=[
        "State the principle of moments in full",
        "Use it to find an unknown force or distance",
        "Show the working the examiners expect: both moments calculated as force × distance",
    ],
    parts=[
        explain(
            "The principle and how it is marked",
            diagram(dg.beam_svg(), 600, 230, "A balanced beam: the anticlockwise moment of the 200 N equals the clockwise moment of the 300 N.") +
            "<p><b>The principle of moments:</b> for an object <b>in equilibrium</b> (balanced, not rotating), the <b>sum of the clockwise moments</b> about a pivot <b>equals the sum of the anticlockwise moments</b> about the same pivot.</p>"
            "<p>The June 2024 scheme (Q6(b)(i), 2 marks) gave one mark for \"sum of the clockwise moments = sum of anticlockwise moments (about the same point)\" and a separate mark for \"<b>for a system in equilibrium</b>\". The June 2022 report: \"just saying clockwise moments = anticlockwise moments would not score\" — the <b>totals</b> must be stated. Both halves, every time.</p>"
            "<p><b>Calculations:</b> decide which side turns which way, write each moment as force × distance, set the totals equal, solve. The June 2023 report: \"questions asking for the principle of moments will expect you to show a <b>calculation of moments using force × distance</b>\" — students who used ratios of forces and distances without calculating a moment lost marks, even with the right answer. Keep the distances all in m (or all in cm — consistent units were accepted) and measure every distance <b>from the pivot</b>, not from the end of the beam.</p>",
        ),
        worked(
            "An unknown distance",
            "A uniform beam is pivoted at its centre. A 200 N box sits 1.5 m to the left of the pivot. Calculate how far to the right of the pivot a 300 N box must be placed to balance the beam.",
            [
                r"Anticlockwise moment (left box) $= 200 \times 1.5 = 300$ N m.",
                r"Clockwise moment (right box) $= 300 \times d$.",
                r"In equilibrium, sum of clockwise moments = sum of anticlockwise moments: $300 \times d = 300$, so $d = 1.0$ m.",
            ],
        ),
        practice("The principle of moments", [
            written("fe-n7-q1", "State the principle of moments. (2)",
                    marks(["The <b>sum of the clockwise moments</b> about a point equals the <b>sum of the anticlockwise moments</b> about that point…", "…when the object is <b>in equilibrium</b> (balanced)."]), lines=2),
            numeric("fe-n7-q2", "A see-saw is pivoted at its centre. A 450 N child sits 1.2 m from the pivot. Calculate the force needed 1.8 m from the pivot on the other side to balance it.", 300, "N", "Set the two moments equal.",
                    [r"$450 \times 1.2 = F \times 1.8$", r"$540 = 1.8F$, so $F = 300$ N."]),
            numeric("fe-n7-q3", "A metre rule balances on a pivot at its centre. A 4 N weight hangs 20 cm left of the pivot. Calculate how far right of the pivot a 5 N weight must hang.", 16, "cm", "Work in cm throughout.",
                    [r"$4 \times 20 = 5 \times d$", r"$80 = 5d$, so $d = 16$ cm."]),
            choice("fe-n7-q4", "A student answers a principle-of-moments question by writing \"$300 \\div 200 = 1.5$, so the distance is $1.5 \\times 1 = 1.5$ m\" and gets the right number. Why might this lose marks?",
                   ["The answer is wrong", "No moment was calculated as force × distance, which is what the question asks to be shown", "Units should be cm", "Ratios are not allowed in physics"], 1,
                   "The 2023 report's exact point: show the moments."),
            group("fe-n7-q5", "A uniform plank is pivoted at its centre. A 60 N weight hangs 0.5 m to the left and a 20 N weight hangs 1.0 m to the left. A single weight W hangs 1.6 m to the right.", [
                numeric("fe-n7-q5a", "Calculate the total anticlockwise moment.", 50, "N m", "Two moments to add.",
                        [r"$60 \times 0.5 + 20 \times 1.0 = 30 + 20 = 50$ N m."]),
                numeric("fe-n7-q5b", "Calculate W.", 31.25, "N", "Clockwise moment = 50 N m.",
                        [r"$W \times 1.6 = 50$, so $W = 31.25$ N (31 N to 2 s.f.)."], tolerance=0.02),
            ]),
            written("fe-n7-q6", "Explain why a person can lift a heavy load in a wheelbarrow with a force much smaller than the load's weight. (2)",
                    marks(["The wheel is the <b>pivot</b>; the load is <b>close</b> to it and the handles are <b>far</b> from it.",
                           "By the principle of moments, effort × long distance = load × short distance, so the <b>effort is smaller than the load</b> by the ratio of the distances."]), lines=3),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N8 · Levers and gears
# ---------------------------------------------------------------------

section_n8 = section(
    "levers-gears", "nn", "Levers and gears: passing a turning effect on", "9.9P",
    equations=[r"\text{lever: } E \times d_E = L \times d_L", r"\text{gears: same tooth force, moment} \propto \text{radius}"],
    blurb="A lever and a pair of gears both transmit the rotational effect of a force — and both can multiply it. A lever trades distance for force about one pivot; gears pass a force from one wheel to another, and the bigger wheel gets the bigger moment.",
    tags=["P"],
    checklist=[
        "Explain how a lever transmits and multiplies a turning effect",
        "Explain how gears transmit a turning effect, including direction, speed and moment",
        "State the link between numbers of teeth and the numbers of turns",
    ],
    parts=[
        explain(
            "Levers",
            diagram(dg.lever_svg(), 640, 280, "A crowbar: a 100 N effort 1.2 m from the pivot balances a 600 N load 0.2 m from it.") +
            "<p>A <b>lever</b> is a rigid bar that turns about a <b>pivot</b>. The <b>effort</b> is the force you apply; the <b>load</b> is the force the lever applies to the thing being moved. By the principle of moments, just as it starts to move: <b>effort × distance of effort from pivot = load × distance of load from pivot</b>. Put the effort <b>far</b> from the pivot and the load <b>near</b> it and the lever is a <b>force multiplier</b>: the crowbar above turns 100 N into 600 N. The price is distance — the effort end moves six times as far as the load end (see <i>Levers: force multipliers</i> in the tricky bits).</p>",
        ),
        explain(
            "Gears",
            diagram(dg.gears_svg(), 720, 250, "A 10-tooth gear driving a 20-tooth gear: the same force between the teeth, twice the moment on the larger wheel, half the turns, opposite direction.") +
            "<p>Two <b>gears</b> mesh tooth to tooth. The force one tooth pushes on the other with is the <b>same on both wheels</b> (an interaction pair), but it acts at each wheel's <b>own radius</b>, so the <b>moment on each wheel is proportional to its radius</b> (and so to its number of teeth).</p>"
            "<ul><li><b>Small driving large</b>: the large wheel gets a <b>bigger moment</b> but turns <b>fewer times</b> (slower) — a force multiplier, used for climbing hills on a bike, in a winch, in a car's low gear.</li>"
            "<li><b>Large driving small</b>: the small wheel gets a <b>smaller moment</b> but turns <b>more times</b> (faster) — a speed multiplier, a bike's top gear.</li>"
            "<li>Meshed gears turn in <b>opposite directions</b>; a chain or belt between two wheels keeps them turning the same way.</li>"
            "<li><b>Turns × teeth is the same for both wheels</b> (turns of A : turns of B = teeth of B : teeth of A): a 10-tooth wheel must turn twice to turn a 20-tooth wheel once, because the same number of teeth pass the contact point on each.</li></ul>"
            "<p>The June 2024 scheme (Q6(c)): a gear with three times the teeth turns at a third of the rate; to make an output turn <b>twice as fast</b>, add a wheel with <b>half the teeth</b> meshing with it.</p>",
        ),
        worked(
            "A bicycle",
            "A cyclist's pedal wheel has 48 teeth and drives, through a chain, a rear wheel gear with 16 teeth. (a) How many times does the rear gear turn for one turn of the pedals? (b) Compare the moment on the rear gear with the moment on the pedal wheel. (c) Explain why the cyclist changes to a 32-tooth rear gear for a hill. (4 marks)",
            [
                "<b>(a)</b> Turns × teeth is the same for both: $48 \\div 16 = 3$ turns of the rear gear per pedal turn.",
                "<b>(b)</b> The chain pulls both wheels with the <b>same force</b>; the rear gear has <b>one third of the radius</b>, so it gets <b>one third of the moment</b> — a speed multiplier.",
                "<b>(c)</b> With 32 teeth the rear gear's radius is larger, so the <b>same chain force gives a bigger moment</b> on the wheel — more turning force to climb — while the wheel turns only 1.5 times per pedal turn, so the bike goes slower.",
            ],
        ),
        practice("Levers and gears", [
            numeric("fe-n8-q1", "A crowbar has its pivot 0.1 m from a rock and the effort is applied 0.9 m from the pivot. The rock needs a force of 450 N to move. Calculate the effort needed.", 50, "N", "Effort × $0.9 = 450 \\times 0.1$.",
                    [r"$E \times 0.9 = 450 \times 0.1 = 45$", r"$E = 50$ N."]),
            choice("fe-n8-q2", "A 12-tooth gear drives a 36-tooth gear. For one turn of the 36-tooth gear, the 12-tooth gear turns…",
                   ["once", "three times", "a third of a turn", "twelve times"], 1,
                   "36 teeth must pass the contact point; the small wheel has 12, so three turns."),
            written("fe-n8-q3", "Explain how a small gear driving a larger gear increases the turning effect. (3)",
                    mark_scheme([
                        ("Same force", "The force between the meshing teeth is the <b>same</b> on both gears."),
                        ("Bigger radius", "On the larger gear that force acts at a <b>greater distance</b> from the axle (larger radius)."),
                        ("Moment", "Moment = force × distance, so the larger gear has the <b>greater moment</b> (it turns more slowly in exchange)."),
                    ]), lines=4),
            choice("fe-n8-q4", "Two meshed gears: A turns clockwise. B turns…",
                   ["clockwise", "anticlockwise", "it does not turn", "clockwise, then anticlockwise"], 1,
                   "Meshed gears turn opposite ways."),
            written("fe-n8-q5", "A motor turns a 40-tooth gear at 60 turns per minute. Describe how to add a gear so that an output turns at 120 turns per minute, and explain your choice. (2)",
                    marks(["Mesh a gear with <b>20 teeth</b> (half as many) with the 40-tooth gear.",
                           "The same number of teeth pass the contact point on each, so the 20-tooth gear makes <b>two turns for every one</b> of the 40-tooth gear: 120 per minute."]), lines=3),
            written("fe-n8-q6", "Explain why a lever with the effort far from the pivot and the load near it is called a force multiplier, and what the user gives up in return. (2)",
                    marks(["Effort × its distance = load × its distance, so with a longer effort distance the <b>load force is larger than the effort</b>.",
                           "The effort has to <b>move further</b> than the load does (the work done is the same, ignoring friction)."]), lines=2),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N9 · Lubrication
# ---------------------------------------------------------------------

section_n9 = section(
    "lubrication", "nn", "Lubrication: reducing unwanted energy transfer", "9.10",
    equations=[r"\text{friction} \rightarrow \text{thermal store (dissipated)}"],
    blurb="Friction between moving parts transfers energy to the thermal store of the surroundings — wasted. A lubricant keeps the surfaces apart so there is less friction and less waste. Say how, not just why.",
    checklist=[
        "Explain how friction wastes energy in a machine",
        "Explain how lubrication reduces the waste",
        "Give a method, not a reason, when asked how to reduce friction",
    ],
    parts=[
        explain(
            "Friction, lubrication and the 'how' mark",
            "<p>When two surfaces slide over each other, <b>friction</b> acts and <b>work is done against it</b>; the energy is transferred to the <b>thermal store</b> of the surfaces and the air — it heats them up and spreads out (<b>dissipates</b>), so it is no longer useful. In a machine that lowers the <b>efficiency</b> (Topic 3): more of the input energy ends up as heat and less as useful output.</p>"
            "<p>A <b>lubricant</b> (oil, grease, graphite) is a thin layer that <b>separates the surfaces</b> so they slide on the fluid instead of rubbing directly; the frictional force is <b>smaller</b>, so <b>less work is done against friction</b>, less energy is dissipated as heat, and more is transferred usefully.</p>"
            "<p>Where friction is wanted — brakes, tyres, shoes, a match — you do not lubricate; you increase the grip (rougher surface, larger normal force).</p>"
            "<p>The June 2025 report (Q2(a)(iii)): asked for a <b>way</b> to reduce the effect of friction on a trolley, \"many candidates answered in general terms of reducing friction rather than how this could be achieved\" — \"reduce friction\" scored nothing; \"<b>oil the wheel axles</b>\" scored. The June 2023 report said the same for practical improvements: \"you need to say <b>how</b> it will improve, not why\".</p>",
        ),
        worked(
            "Say how",
            "A pupil's trolley rolls more slowly down a ramp than the calculation predicts. (a) Explain why. (b) Suggest one way to reduce the difference. (3 marks)",
            [
                "<b>(a)</b> <b>Friction</b> at the axles and bearings (and air resistance) does work against the motion, transferring some of the trolley's energy to the <b>thermal store</b> instead of its kinetic store — so it ends up slower than predicted.",
                "<b>(b)</b> <b>Lubricate the axles with oil</b> (a method)…",
                "…which <b>separates the moving surfaces</b>, reducing the frictional force and the energy dissipated. (\"Reduce friction\" alone is a reason, not a method, and scores nothing.)",
            ],
        ),
        practice("Lubrication", [
            written("fe-n9-q1", "Explain how lubricating the moving parts of a machine increases its efficiency. (3)",
                    mark_scheme([
                        ("Friction", "Without lubricant the surfaces rub; work is done against <b>friction</b> and energy is transferred to the <b>thermal store</b> (dissipated / wasted)."),
                        ("Lubricant", "The lubricant forms a layer that <b>separates the surfaces</b>, so the frictional force is <b>smaller</b>."),
                        ("Efficiency", "Less energy is wasted as heat, so a <b>larger fraction</b> of the input is transferred usefully — higher efficiency."),
                    ]), lines=4),
            choice("fe-n9-q2", "A question asks: \"Suggest one way to reduce the effect of friction on the trolley.\" Which answer scores?",
                   ["Reduce the friction", "Make it more efficient", "Oil the wheel axles", "Friction wastes energy"], 2,
                   "A method, not a reason."),
            written("fe-n9-q3", "Describe what happens to the energy when work is done against friction. (2)",
                    marks(["It is transferred to the <b>thermal store</b> of the surfaces and surroundings (they get warmer).", "It <b>spreads out / dissipates</b> and is no longer useful."]), lines=2),
            choice("fe-n9-q4", "Where should friction NOT be reduced?",
                   ["A door hinge", "A bicycle chain", "The brake pads of a car", "A sliding drawer"], 2,
                   "Brakes work by friction."),
            written("fe-n9-q5", "A bicycle chain squeaks and the cyclist has to pedal harder. Explain what has happened and what to do. (2)",
                    marks(["The chain has lost its lubricant, so there is <b>more friction</b> between the links and the gear teeth; more of the pedalling energy is dissipated as heat (and sound).",
                           "<b>Oil the chain</b>: the oil separates the metal surfaces and reduces the frictional force."]), lines=2),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N10 · Key words
# ---------------------------------------------------------------------

DEFINITIONS = [
    ("Contact force", "A force between objects that are <b>touching</b> (normal contact force, friction, tension, drag).", "\"a push\""),
    ("Non-contact force", "A force that acts <b>at a distance</b>, through a field (gravitational, electrostatic, magnetic).", "\"a force that does not touch\""),
    ("Field", "A <b>region</b> in which a mass / charge / magnetic material <b>experiences a force</b>.", "\"where the force is\""),
    ("Normal contact force", "The force from a surface on an object pressing on it, <b>at right angles</b> to the surface.", "\"the reaction\" alone"),
    ("Friction", "The force between two surfaces that <b>opposes</b> their relative motion.", "\"stickiness\""),
    ("Interaction pair", "Two forces, <b>equal and opposite</b>, of the <b>same type</b>, on <b>different objects</b>.", "\"balanced forces\""),
    ("Vector", "A quantity with <b>size and direction</b> (force, velocity, displacement, acceleration, momentum).", "\"a quantity with direction\" alone"),
    ("Scalar", "A quantity with <b>size only</b> (speed, distance, mass, energy, time).", "\"a quantity with no size\""),
    ("Resultant force", "The <b>single force</b> that has the <b>same effect</b> as all the forces acting together.", "\"the total force\" alone"),
    ("Equilibrium", "The state in which the <b>resultant force is zero</b> (and, for rotation, the moments balance): at rest or constant velocity.", "\"stationary\""),
    ("Free body force diagram", "A diagram of <b>one object</b> showing <b>all the forces acting on it</b> as labelled arrows from its centre.", "\"a force diagram\""),
    ("Moment of a force", "The <b>turning effect</b> of a force: force × <b>perpendicular distance</b> from the pivot to its line of action, in N m.", "\"force × distance\" with no 'perpendicular'"),
    ("Pivot", "The point about which an object <b>turns</b> (hinge, fulcrum, axle).", "\"the middle\""),
    ("Principle of moments", "In equilibrium, the <b>sum of the clockwise moments</b> about a point = the <b>sum of the anticlockwise moments</b> about that point.", "\"clockwise = anticlockwise\""),
    ("Lever", "A rigid bar that turns about a pivot, <b>transmitting and usually multiplying</b> the turning effect of a force.", "\"a stick\""),
    ("Effort and load", "The <b>effort</b> is the force applied to a machine; the <b>load</b> is the force it exerts on the object being moved.", "swapping them"),
    ("Gear", "A toothed wheel that <b>transmits a turning effect</b> to another by meshing; the moment on each is proportional to its radius.", "\"a cog that makes things go faster\""),
    ("Lubricant", "A substance (oil, grease) that <b>separates sliding surfaces</b> to reduce friction and the energy dissipated.", "\"something slippery\""),
]


def definitions_table():
    html = "<table class='tbl'><tr><th>Term</th><th>What to write (mark-scheme form)</th><th>Not this</th></tr>"
    for term, definition, wrong in DEFINITIONS:
        html += "<tr><td><b>" + term + "</b></td><td>" + definition + "</td><td>" + wrong + "</td></tr>"
    html += "</table>"
    return html


section_keywords = section(
    "keywords-forces-effects", "nn", "Key words: state what is meant by…", "9",
    equations=[r"\text{definition, word for word}"],
    blurb="One-mark definitions in the form of words the mark schemes credit. The bold words are the ones the marks are attached to.",
    checklist=[
        "Define the force words: contact, non-contact, field, normal contact force, friction, interaction pair",
        "Define vector, scalar, resultant force, equilibrium, free body diagram",
        "Define moment, pivot, principle of moments, lever, effort, load, gear, lubricant",
    ],
    parts=[
        explain("The definitions", "<p>\"<b>State what is meant by</b>\" asks for the definition. Learn these as sentences.</p>" + definitions_table()),
        practice("Key words", [
            written("fe-kw-q1", "State what is meant by the moment of a force. (1)",
                    marks(["The <b>turning effect</b> of a force: force × <b>perpendicular distance</b> from the pivot."]), lines=1, tags=["P"]),
            written("fe-kw-q2", "State what is meant by a resultant force. (1)",
                    marks(["The <b>single force</b> that would have the <b>same effect</b> as all the forces acting on the object."]), lines=1),
            choice("fe-kw-q3", "Which is the correct statement of the principle of moments?",
                   ["Clockwise moments equal anticlockwise moments", "For an object in equilibrium, the sum of the clockwise moments about a point equals the sum of the anticlockwise moments about that point", "Force × distance is constant", "Moments cancel out"], 1,
                   "\"Sum of\" and \"in equilibrium\" are both needed.", tags=["P"]),
            written("fe-kw-q4", "State what is meant by a vector quantity and give one example. (1)",
                    marks(["A quantity with <b>size and direction</b>, e.g. force / velocity / displacement / acceleration / momentum."]), lines=1),
            written("fe-kw-q5", "State what is meant by a magnetic field. (1)",
                    marks(["A <b>region</b> in which a <b>magnetic material</b> (or magnet, or current) <b>experiences a force</b>."]), lines=1),
            written("fe-kw-q6", "State what is meant by equilibrium. (1)",
                    marks(["The <b>resultant force</b> (and resultant moment) on the object is <b>zero</b> — it is at rest or moving at constant velocity."]), lines=1),
            choice("fe-kw-q7", "A student defines friction as \"the force that stops things\". What is the mark-scheme form?",
                   ["The force that makes things hot", "The force between two surfaces that opposes their relative motion", "A contact force", "The force of the ground"], 1,
                   "Opposes relative motion of surfaces in contact."),
            written("fe-kw-q8", "State what is meant by a free body force diagram. (1)",
                    marks(["A diagram showing <b>one object</b> and <b>all the forces acting on it</b>, as labelled arrows from its centre."]), lines=1),
        ]),
    ],
)

FACTS_KW = [fact("State what is meant by: " + term.lower() + ".", definition, "keywords-forces-effects") for term, definition, wrong in DEFINITIONS]

SECTIONS = [section_n1, section_n2, section_n3, section_n4, section_n5, section_n6, section_n7, section_n8, section_n9, section_keywords]
