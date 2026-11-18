"""
fe_tricky.py — Topic 9 (Forces and their effects): the tricky bits T1–T8
and the flashcards.

T1 Scale drawing for a resultant [H]      T5 Moments the hard way [P]
T2 Resolving a force [H]                  T6 Levers as force multipliers [P]
T3 Equilibrium: the closed triangle [H]   T7 Gears, force and work: the winch 6-marker [P]
T4 Explaining motion from the resultant [H]   T8 Friction and lubrication explained
"""

from revlib import (
    choice, diagram, explain, fact, group, mark_scheme, marks, numeric,
    practice, section, worked, written,
)
import fe_diagrams as dg

# ---------------------------------------------------------------------
# T1 · Scale drawing for a resultant
# ---------------------------------------------------------------------

section_t1 = section(
    "scale-resultant", "tricky", "Finding a resultant by scale drawing", "9.3",
    equations=[r"\text{tip to tail; measure the closing line}", r"3^2 + 4^2 = 5^2"],
    blurb="Two forces at an angle do not add like numbers. Draw them to scale, tip to tail, and the resultant is the line from the start of the first to the tip of the second — measure its length and its angle. For a right angle, Pythagoras is the check.",
    tags=["H"],
    checklist=[
        "Choose a scale and draw two forces tip to tail",
        "Measure the resultant's size and direction",
        "Check a right-angled case with Pythagoras",
    ],
    parts=[
        explain(
            "The method",
            diagram(dg.resultant_svg(), 600, 280, "3 N and 4 N at right angles: tip to tail the closing line measures 5 N at 53° above the 3 N.") +
            "<ol><li><b>Choose a scale</b> and write it down: \"1 cm = 1 N\" (or 1 cm = 10 N for big forces). Pick one that makes the drawing 5–10 cm across.</li>"
            "<li><b>Draw the first force</b> as an arrow of the right length in the right direction, with a ruler.</li>"
            "<li><b>Draw the second force starting from the tip of the first</b> (tip to tail), at its correct angle — use a protractor.</li>"
            "<li><b>The resultant</b> is the arrow from the <b>start of the first</b> to the <b>tip of the second</b>. Measure its <b>length</b> and convert with the scale; measure its <b>angle</b> from a stated direction.</li></ol>"
            "<p>The <b>parallelogram</b> method gives the same answer: draw both forces from the same point, complete the parallelogram, and the diagonal from that point is the resultant. The June 2025 scheme (Q8(c)) accepted either, or \"a right-angled triangle and Pythagoras\". The marks were for the <b>direction</b> (judged by eye) and the <b>size</b> (within a tolerance — 2.5 to 3.5 for a 3 N answer), so the arrow must be drawn, labelled, and measurably right.</p>"
            "<p><b>Pythagoras check</b> for forces at right angles: $R^2 = F_1^2 + F_2^2$; $3^2 + 4^2 = 25$, $R = 5$ N. If the drawing says 5.4, redraw. Trig is not required (\"scale drawings only\" in the spec) but is accepted if correct.</p>",
        ),
        worked(
            "Two ropes on a boat",
            "A boat is pulled by two ropes: 60 N due east and 80 N due north. Find the resultant force by scale drawing. (3 marks)",
            [
                "<b>Scale:</b> 1 cm = 10 N. Draw 6.0 cm due east, then from its tip 8.0 cm due north.",
                "<b>Resultant:</b> the line from the start to the tip measures <b>10.0 cm → 100 N</b>.",
                "<b>Direction:</b> the angle between the resultant and the east arrow measures <b>53°</b> — 100 N at 53° north of east. Check: $60^2 + 80^2 = 10\\,000 = 100^2$. ✓",
            ],
        ),
        practice("Scale drawings", [
            numeric("fe-t1-q1", "Forces of 5 N east and 12 N north act on an object. Calculate the size of the resultant (or find it by scale drawing).", 13, "N", "Right angle: Pythagoras.",
                    [r"$R = \sqrt{5^2 + 12^2} = \sqrt{169} = 13$ N."]),
            written("fe-t1-q2", "Describe how to find the resultant of two forces at an angle using a scale drawing. (3)",
                    mark_scheme([
                        ("Scale", "Choose and state a <b>scale</b> (e.g. 1 cm = 1 N); draw the first force as an arrow of the correct length and direction."),
                        ("Tip to tail", "Draw the second force <b>from the tip of the first</b>, at the correct angle (protractor)."),
                        ("Measure", "Draw the resultant from the <b>start of the first to the tip of the second</b>; measure its <b>length</b> (convert with the scale) and its <b>angle</b>."),
                    ]), lines=4),
            choice("fe-t1-q3", "Two forces of 6 N and 8 N act at right angles. A student's scale drawing gives a resultant of 12 N. What should they conclude?",
                   ["Correct — 6 + 8 is about 12", "The drawing is wrong — Pythagoras gives 10 N", "Resultants cannot be found for right angles", "The scale was too small"], 1,
                   "√(36 + 64) = 10 N. Always check a right angle with Pythagoras."),
            numeric("fe-t1-q4", "A scale drawing uses 1 cm = 20 N. The resultant measures 6.5 cm. Calculate the resultant force.", 130, "N", "Multiply by the scale.",
                    [r"$6.5 \times 20 = 130$ N."]),
            written("fe-t1-q5", "Two 10 N forces act on a ring at 60° to each other. Explain, without a full drawing, why the resultant is less than 20 N but more than 10 N. (2)",
                    marks(["Force is a vector: the two forces are <b>not in the same direction</b>, so they do not add to the full 20 N.",
                           "At 60° apart they partly reinforce each other, so the tip-to-tail closing line is longer than either force alone — the resultant lies between 10 N and 20 N (it is about 17 N)."]), lines=3),
            choice("fe-t1-q6", "In a scale drawing of two forces, where is the resultant drawn?",
                   ["Between the tips of the two force arrows", "From the start of the first force to the tip of the second", "From the tip of the second back to the start", "Along the longer force"], 1,
                   "Start of the first to tip of the last; the arrowhead points at the tip."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T2 · Resolving a force
# ---------------------------------------------------------------------

section_t2 = section(
    "resolving", "tricky", "Resolving a force into two components", "9.3",
    equations=[r"\text{one force} \rightarrow \text{two at right angles with the same effect}"],
    blurb="Resolving is adding in reverse: replacing one force at an angle with two forces at right angles that together have exactly the same effect. By scale drawing: draw the force, drop perpendiculars, measure.",
    tags=["H"],
    checklist=[
        "Explain what it means to resolve a force",
        "Find the components of a force by scale drawing",
        "Use components to explain a sledge on the flat and an object on a slope",
    ],
    parts=[
        explain(
            "Components by drawing",
            diagram(dg.resolve_svg(), 640, 250, "A 10 N pull at 30° above the horizontal: 8.7 N along the ground and 5 N upwards.") +
            "<p>To <b>resolve</b> a force is to split it into two <b>components</b> at right angles — usually horizontal and vertical, or along and perpendicular to a slope — whose combined effect is the same as the original. The components are the two sides of the rectangle whose diagonal is the force.</p>"
            "<ol><li>Draw the force to scale at its correct angle.</li>"
            "<li>From its tip, drop a <b>perpendicular</b> to each of the two directions you want.</li>"
            "<li>Measure the two sides from the start point: those are the components.</li></ol>"
            "<p><b>Why it matters:</b> only the <b>horizontal</b> component of the rope's pull moves the sledge along; the vertical component just lightens it on the snow (reducing the normal contact force and so the friction). On a <b>slope</b>, the weight resolves into a component <b>along the slope</b> (which tends to make the object slide, and friction must match) and a component <b>into the slope</b> (which the normal contact force matches). The steeper the slope, the bigger the along-slope component.</p>"
            "<p>Check with trig if you know it: the component along a direction at angle $\\theta$ to the force is $F\\cos\\theta$; $10\\cos 30° = 8.7$ N and $10\\sin 30° = 5$ N. The spec asks for scale drawings only, so the drawing is what is marked.</p>",
        ),
        worked(
            "A sledge on the flat",
            "A child pulls a sledge with a 40 N force on a rope at 30° above the horizontal. (a) Find the horizontal and vertical components by scale drawing. (b) The friction on the sledge is 30 N. Calculate the resultant horizontal force. (4 marks)",
            [
                "<b>(a)</b> Scale 1 cm = 5 N: draw 8.0 cm at 30° above horizontal. Drop perpendiculars: the horizontal side measures <b>6.9 cm → 35 N</b> (34.6), the vertical side <b>4.0 cm → 20 N</b>.",
                "The horizontal component pulls the sledge along; the vertical component (20 N upwards) partly supports its weight.",
                "<b>(b)</b> Horizontal resultant $= 34.6 - 30 = 4.6$ N forwards (about 5 N), so the sledge accelerates forwards gently.",
            ],
        ),
        practice("Resolving", [
            written("fe-t2-q1", "State what is meant by resolving a force. (1)",
                    marks(["Splitting one force into <b>two components at right angles</b> to each other that together have the <b>same effect</b> as the original force."]), lines=1),
            numeric("fe-t2-q2", "A 20 N force acts at 60° above the horizontal. A scale drawing (1 cm = 2 N) gives a horizontal side of 5.0 cm. State the horizontal component.", 10, "N", "Convert with the scale.",
                    [r"$5.0 \times 2 = 10$ N (check: $20 \cos 60° = 10$ N)."]),
            numeric("fe-t2-q3", "The same 20 N force at 60° above the horizontal: the vertical side of the drawing measures 8.7 cm. State the vertical component.", 17.4, "N", "Scale 1 cm = 2 N.",
                    [r"$8.7 \times 2 = 17.4$ N (check: $20 \sin 60° = 17.3$ N)."], tolerance=0.03),
            written("fe-t2-q4", "A box rests on a slope. Describe how to find the component of its weight acting along the slope, and explain why this component matters. (3)",
                    mark_scheme([
                        ("Draw", "Draw the weight to scale, <b>vertically downwards</b> from the box's centre."),
                        ("Perpendiculars", "From its tip drop perpendiculars to the <b>along-slope</b> and <b>into-slope</b> directions; measure the along-slope side and convert with the scale."),
                        ("Why", "The along-slope component is the force tending to make the box <b>slide down</b>; friction must at least equal it for the box to stay at rest (the into-slope component is balanced by the normal contact force)."),
                    ]), lines=4),
            choice("fe-t2-q5", "A rope pulls a sledge at an angle above the horizontal. Which component moves the sledge along the ground?",
                   ["The vertical component", "The horizontal component", "Both equally", "Neither — the whole force does"], 1,
                   "Only the horizontal component acts along the direction of travel."),
            choice("fe-t2-q6", "As a slope is made steeper, the component of an object's weight along the slope…",
                   ["decreases", "increases", "stays the same", "becomes zero"], 1,
                   "At 0° it is zero; at 90° it is the whole weight."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T3 · Equilibrium: the closed triangle
# ---------------------------------------------------------------------

section_t3 = section(
    "equilibrium-triangle", "tricky", "Equilibrium: three forces that close into a triangle", "9.3, 9.5",
    equations=[r"\text{resultant } = 0 \Leftrightarrow \text{the vectors close}"],
    blurb="If an object is in equilibrium under three forces, drawing them tip to tail brings you back to where you started: a closed triangle. That is the scale-drawing test for equilibrium, and the way to find an unknown tension.",
    tags=["H"],
    checklist=[
        "Explain why forces in equilibrium form a closed vector triangle",
        "Find an unknown force from a closed triangle by scale drawing",
        "Describe the forces on a hanging object and an object on a slope in equilibrium",
    ],
    parts=[
        explain(
            "Closing the triangle",
            diagram(dg.triangle_svg(), 600, 280, "A 10 N sign on two strings at right angles: the three forces on the knot drawn tip to tail close into a right-angled triangle, so each tension is 7.1 N.") +
            "<p><b>Equilibrium</b> means the resultant force is <b>zero</b>. Draw the forces tip to tail and the resultant is the line from the start to the finish — if that is zero, the finish <b>is</b> the start: the arrows form a <b>closed shape</b>. For three forces, a <b>triangle</b>.</p>"
            "<p><b>To find an unknown:</b> draw the known force(s) to scale; draw the <b>directions</b> of the unknown ones as lines from the right ends; where they meet closes the triangle; measure. Two tensions at known angles holding a known weight is the standard case.</p>"
            "<p><b>The 'explain' version</b>: for an object at rest the forces are balanced — in the vertical direction the upward components add up to the weight; in the horizontal direction the sideways components cancel. A picture hanging from two strings: each string's <b>vertical component</b> is half the weight; the <b>horizontal components</b> are equal and opposite. The wider the angle between the strings, the bigger the tensions needed for the same vertical component — which is why a washing line sags.</p>"
            "<p>The spec's 'isolated object or system' (9.5): the triangle is drawn for the forces on <b>one</b> body (the knot, the sign, the box) — not mixing in forces on other things.</p>",
        ),
        worked(
            "A hanging sign",
            "A 10 N sign hangs from a knot held by two strings, each at 45° to the vertical. Use a scale drawing to find the tension in each string. (3 marks)",
            [
                "<b>Scale</b> 1 cm = 1 N. Draw the weight: 10 cm straight down.",
                "From the bottom draw a line at 45° to the vertical (the direction of $T_1$); from the top draw a line at 45° the other way ($T_2$). They meet, closing the triangle.",
                "Measure: each side is <b>7.1 cm → 7.1 N</b>. (Check: each vertical component is $7.1 \\times \\cos 45° = 5$ N; two of them hold the 10 N.)",
            ],
        ),
        practice("Equilibrium", [
            written("fe-t3-q1", "Explain why, for an object in equilibrium, the force vectors drawn tip to tail form a closed shape. (2)",
                    marks(["In equilibrium the <b>resultant force is zero</b>.", "The resultant is the line from the start of the first vector to the tip of the last; if it is zero the tip of the last is <b>back at the start</b> — the shape closes."]), lines=2),
            choice("fe-t3-q2", "A 20 N lamp hangs from two identical chains at 30° to the vertical. Each chain's vertical component must be…",
                   ["20 N", "10 N", "40 N", "0 N"], 1,
                   "The two vertical components together support the 20 N."),
            numeric("fe-t3-q3", "The lamp above: a scale drawing (1 cm = 2 N) of the closed triangle gives each chain tension as a side of 5.8 cm. State the tension.", 11.6, "N", "Multiply by the scale.",
                    [r"$5.8 \times 2 = 11.6$ N (check: $10 \div \cos 30° = 11.5$ N)."], tolerance=0.03),
            written("fe-t3-q4", "A picture hangs from a single cord looped over a hook. Explain why the tension in the cord is greater when the cord is nearly horizontal than when it is nearly vertical. (2)",
                    marks(["The <b>vertical components</b> of the two parts of the cord must always add up to the picture's <b>weight</b>.",
                           "When the cord is nearly horizontal only a <b>small fraction</b> of each tension acts vertically, so the tension itself must be much <b>larger</b> to supply the same vertical component."]), lines=3),
            written("fe-t3-q5", "A box rests on a rough slope. Name the three forces on it and explain how they can be in equilibrium. (3)",
                    mark_scheme([
                        ("Forces", "<b>Weight</b> (vertically down), <b>normal contact force</b> (at right angles to the slope), <b>friction</b> (up the slope)."),
                        ("Balance", "The normal force balances the component of the weight <b>into</b> the slope; friction balances the component of the weight <b>along</b> the slope."),
                        ("Triangle", "Drawn tip to tail the three forces <b>close into a triangle</b> — the resultant is zero, so the box stays at rest."),
                    ]), lines=4),
            choice("fe-t3-q6", "Three forces act on an object. Drawn tip to tail to scale, there is a gap of 2 cm (scale 1 cm = 5 N) between the tip of the last and the start of the first. What is the resultant?",
                   ["0 N — it is in equilibrium", "2 N", "10 N", "Cannot tell"], 2,
                   "The gap is the resultant: 2 cm × 5 N/cm = 10 N."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T4 · Explaining motion from the resultant
# ---------------------------------------------------------------------

section_t4 = section(
    "resultant-motion", "tricky", "Explaining motion from the resultant force", "9.5",
    equations=[r"F_{\text{resultant}} = m \times a", r"\text{direction of } a = \text{direction of } F_{\text{resultant}}"],
    blurb="'Explain the motion' questions are marked on a chain: which forces act, which is bigger, so which way the resultant points, so what the acceleration does. Topic 2 has the full treatment; this is the Paper 2 phrasing.",
    tags=["H"],
    checklist=[
        "Explain the motion of a falling object as drag grows to equal weight",
        "Explain why a vehicle at constant velocity has balanced forces, and what happens when one force changes",
        "Explain the forces on a system of connected objects",
    ],
    parts=[
        explain(
            "The chain of reasoning",
            "<table class='tbl'><tr><th>Situation</th><th>Forces</th><th>Resultant</th><th>Motion</th></tr>"
            "<tr><td>skydiver just after jumping</td><td>weight large, air resistance small</td><td>downwards, large</td><td>accelerates downwards quickly</td></tr>"
            "<tr><td>skydiver speeding up</td><td>air resistance <b>grows with speed</b></td><td>downwards, shrinking</td><td>still accelerates, but less and less</td></tr>"
            "<tr><td>terminal velocity</td><td>air resistance <b>equals</b> weight</td><td><b>zero</b></td><td><b>constant velocity</b> (not stopped)</td></tr>"
            "<tr><td>parachute opens</td><td>air resistance jumps to more than weight</td><td><b>upwards</b></td><td>decelerates (slows while still falling) until a new, lower terminal velocity</td></tr>"
            "<tr><td>car at steady 30 m/s</td><td>driving force = drag + friction</td><td>zero</td><td>constant velocity</td></tr>"
            "<tr><td>driver presses the accelerator</td><td>driving force &gt; resistive forces</td><td>forwards</td><td>accelerates until drag has grown to match again</td></tr>"
            "<tr><td>lift starting to go up</td><td>tension &gt; weight</td><td>upwards</td><td>accelerates upwards; at steady speed tension = weight again</td></tr></table>"
            "<p>The sentence pattern that scores: \"<b>[force A] is greater than [force B]</b>, so there is a <b>resultant force [direction]</b>, so the object <b>accelerates [direction]</b>\" — then, if the forces change with speed, \"as the speed increases [force B] increases, the resultant decreases, until the forces are <b>balanced</b> and the velocity is <b>constant</b>\". Four links; each is a mark.</p>"
            "<p><b>Systems</b> (9.5): a car towing a trailer is one system — the engine's driving force must overcome the drag and friction on <b>both</b>, and the tow-bar forces are internal. To find the tension in the tow bar, look at the <b>trailer alone</b>: tension − trailer's resistive forces = trailer's mass × acceleration.</p>",
        ),
        worked(
            "Parachute opens",
            "A skydiver is falling at terminal velocity when her parachute opens. Explain, in terms of the forces, what happens to her motion. (4 marks)",
            [
                "At terminal velocity <b>air resistance equals weight</b>: resultant zero, constant velocity.",
                "When the parachute opens the <b>area increases</b>, so <b>air resistance increases</b> and becomes <b>greater than the weight</b>.",
                "There is now a <b>resultant force upwards</b>, so she <b>decelerates</b> — she slows down while still moving downwards (she does not move upwards).",
                "As she slows, air resistance <b>decreases</b> until it <b>equals the weight again</b>: resultant zero, a new <b>lower terminal velocity</b>.",
            ],
        ),
        practice("Explaining motion", [
            written("fe-t4-q1", "A ball is dropped from a tall building. Explain why its acceleration decreases as it falls, and why it eventually falls at a constant speed. (4)",
                    mark_scheme([
                        ("Start", "At first only the <b>weight</b> is significant: resultant = weight, acceleration = g."),
                        ("Drag grows", "As the speed increases, <b>air resistance increases</b>."),
                        ("Resultant shrinks", "Resultant = weight − air resistance <b>decreases</b>, so the acceleration decreases ($F = ma$)."),
                        ("Terminal", "When air resistance <b>equals</b> the weight the resultant is <b>zero</b>: no acceleration, <b>constant (terminal) velocity</b>."),
                    ]), lines=5),
            choice("fe-t4-q2", "A car travels at constant velocity. The driver presses the brake. Which is true just after?",
                   ["The resultant force is zero", "The resultant force is backwards and the car decelerates", "The resultant force is forwards", "There is no friction"], 1,
                   "Resistive forces now exceed the driving force."),
            written("fe-t4-q3", "A car pulls a trailer. Explain why the tension in the tow bar is less than the driving force on the car. (2)",
                    marks(["The <b>driving force</b> has to overcome the resistive forces on the car <b>and</b> the trailer and accelerate <b>both</b>.",
                           "The <b>tension</b> only has to overcome the trailer's resistive forces and accelerate the <b>trailer</b> — a smaller job, so a smaller force."]), lines=3),
            group("fe-t4-q4", "A lift of mass 500 kg hangs from a cable. (g = 10 N/kg)", [
                numeric("fe-t4-q4a", "Calculate the tension in the cable when the lift moves upwards at constant velocity.", 5000, "N", "Constant velocity: tension = weight.",
                        [r"$W = 500 \times 10 = 5000$ N; resultant zero, so $T = 5000$ N."]),
                numeric("fe-t4-q4b", "Calculate the tension when the lift accelerates upwards at 2 m/s².", 6000, "N", "Resultant = m × a upwards.",
                        [r"Resultant $= 500 \times 2 = 1000$ N upwards.", r"$T - 5000 = 1000$, so $T = 6000$ N."]),
            ]),
            written("fe-t4-q5", "A cyclist stops pedalling on a flat road. Explain why she slows down and eventually stops. (2)",
                    marks(["With no driving force, the only horizontal forces are <b>friction and air resistance</b>, acting <b>backwards</b>.",
                           "The resultant force is backwards, so she <b>decelerates</b>; the resultant stays backwards until her velocity is zero."]), lines=2),
            choice("fe-t4-q6", "Which statement about an object at terminal velocity is correct?",
                   ["It has stopped moving", "Its weight is greater than the drag", "The drag equals its weight and it falls at constant velocity", "It is accelerating slowly"], 2,
                   "Balanced forces, constant velocity."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T5 · Moments the hard way
# ---------------------------------------------------------------------

section_t5 = section(
    "moments-hard", "tricky", "Moments the hard way: angles, several forces, the beam's own weight", "9.7P, 9.8P",
    equations=[r"\sum F \times d_{\perp}\ \text{each side}", r"\text{weight of a uniform beam acts at its centre}"],
    blurb="The 3- and 4-mark moments questions add one twist: a force at an angle, more than one load a side, a beam that weighs something, a pivot not at the centre, or the question of when a plank tips. The method does not change — only the bookkeeping.",
    tags=["P"],
    checklist=[
        "Use the perpendicular distance when a force is not at right angles",
        "Add up several moments on each side",
        "Include the weight of a uniform beam at its centre",
        "Work out when a plank or crane will tip",
    ],
    parts=[
        explain(
            "Four twists",
            "<p><b>1 — A force at an angle.</b> Use the <b>perpendicular distance</b> from the pivot to the <b>line of action</b> (extend the force's line and drop a perpendicular from the pivot), not the distance along the lever. It is always <b>less</b> than the lever length, so the moment is less than F × length (N6's diagram). If a question gives the angle, scale-draw the perpendicular distance or use the component of the force at right angles to the lever.</p>"
            "<p><b>2 — Several forces.</b> Decide the turning sense of <b>each</b> force about the pivot, calculate each moment, <b>add the clockwise ones and add the anticlockwise ones</b> separately, then set the totals equal. The June 2022 report praised answers that \"set out separate moment calculations for S and P, then summed them\".</p>"
            "<p><b>3 — The beam's own weight.</b> A <b>uniform</b> beam's weight acts at its <b>centre</b> (its centre of mass). If the pivot is at the centre that weight has <b>no moment</b> and can be ignored; if the pivot is anywhere else, the weight is one more force at distance (centre − pivot). This is the usual reason a see-saw problem \"doesn't balance\".</p>"
            "<p><b>4 — Tipping.</b> A plank on two supports, or a crane, tips about the <b>edge support</b> when the moment of the load about that edge <b>exceeds</b> the moment of everything on the other side. At the point of tipping the <b>other support carries no force</b> — set its force to zero and apply the principle of moments about the edge. A crane's <b>counterweight</b> is placed to make its anticlockwise moment match the load's clockwise moment; a heavier load must be carried <b>closer</b> to the tower.</p>"
            "<p><b>The pivot force</b> (reaction) is not found from moments but from the forces: in equilibrium the upward forces equal the downward forces, so pivot force = total weight on the beam.</p>",
        ),
        worked(
            "A non-uniform load and the beam's weight",
            "A uniform plank of weight 100 N and length 4.0 m rests on a pivot 1.0 m from its left end. A 300 N box sits on the left end. Calculate the force F that must be applied downwards at the right end to balance the plank. (4 marks)",
            [
                r"<b>Distances from the pivot:</b> box 1.0 m (left); plank's weight at its centre, 2.0 m from the left end, so $2.0 - 1.0 = 1.0$ m (right); F at the right end, $4.0 - 1.0 = 3.0$ m (right).",
                r"<b>Anticlockwise:</b> $300 \times 1.0 = 300$ N m.",
                r"<b>Clockwise:</b> $100 \times 1.0 + F \times 3.0 = 100 + 3F$.",
                r"<b>Equilibrium:</b> $100 + 3F = 300$, so $3F = 200$, $F = 67$ N (66.7). The pivot then pushes up with $300 + 100 + 67 = 467$ N.",
            ],
        ),
        practice("Moments the hard way", [
            numeric("fe-t5-q1", "A uniform beam of weight 60 N and length 3.0 m is pivoted 0.5 m from its left end. Calculate the downward force needed at the left end to keep it horizontal.", 120, "N", "The beam's weight acts at 1.5 m from the left end: 1.0 m from the pivot.",
                    [r"Weight's moment (clockwise): $60 \times 1.0 = 60$ N m.", r"$F \times 0.5 = 60$, so $F = 120$ N."]),
            group("fe-t5-q2", "A metre rule is pivoted at its 50 cm mark. A 2 N weight hangs at 10 cm and a 3 N weight at 30 cm. A single weight W hangs at 80 cm.", [
                numeric("fe-t5-q2a", "Calculate the total anticlockwise moment about the pivot, in N cm.", 140, "N cm", "Distances from the pivot: 40 cm and 20 cm.",
                        [r"$2 \times 40 + 3 \times 20 = 80 + 60 = 140$ N cm."]),
                numeric("fe-t5-q2b", "Calculate W.", 4.67, "N", "W × 30 = 140.",
                        [r"$W = \dfrac{140}{30} = 4.67$ N (4.7 N)."], tolerance=0.02),
            ]),
            choice("fe-t5-q3", "A force of 40 N is applied to the end of a 0.5 m lever at 60° to the lever. The moment is…",
                   ["40 × 0.5 = 20 N m", "less than 20 N m, because the perpendicular distance is less than 0.5 m", "more than 20 N m", "zero"], 1,
                   "Perpendicular distance = 0.5 × sin 60° = 0.43 m, moment 17 N m."),
            written("fe-t5-q4", "A plank rests on two supports, A at its left end and B 1.0 m from its right end. A person walks towards the right end. Explain why the plank tips when the person passes a certain point, and what is true about support A at that moment. (3)",
                    mark_scheme([
                        ("Moments about B", "Beyond B the person's weight has a <b>clockwise moment about B</b> that <b>increases</b> as they move further out."),
                        ("Tipping", "The plank tips when that moment <b>exceeds the anticlockwise moment</b> of the plank's own weight (acting at its centre) about B."),
                        ("Support A", "At the point of tipping the plank is just lifting off A, so the <b>force from A is zero</b>."),
                    ]), lines=4),
            numeric("fe-t5-q5", "A tower crane carries a 20 000 N load 15 m from the tower. Its counterweight is 5 m from the tower on the other side. Calculate the counterweight needed to balance the load (ignore the arm's weight).", 60000, "N", "Moments about the tower.",
                    [r"$W \times 5 = 20\,000 \times 15 = 300\,000$", r"$W = 60\,000$ N."]),
            numeric("fe-t5-q6", "A 500 N uniform beam is pivoted at its centre and balanced: a 200 N load sits 3 m to the left and a 300 N load 2 m to the right. Calculate the upward force from the pivot.", 1000, "N", "Forces, not moments: up = down.",
                    [r"Check it balances: $200 \times 3 = 600 = 300 \times 2$. ✓", r"In equilibrium the pivot supports everything: $500 + 200 + 300 = 1000$ N upwards."]),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T6 · Levers as force multipliers
# ---------------------------------------------------------------------

section_t6 = section(
    "levers-hard", "tricky", "Levers: force multipliers, distance multipliers, and the work done", "9.9P",
    equations=[r"E \times d_E = L \times d_L", r"E \times s_E = L \times s_L\ \text{(work in = work out)}"],
    blurb="A lever can make a force bigger or a movement bigger, never both at once: effort × its distance from the pivot = load × its distance, and effort × distance it moves = load × distance it moves. The second equation is the one students miss, and it is the key to the winch question.",
    tags=["P"],
    checklist=[
        "Classify a lever by where the pivot, effort and load are",
        "Calculate effort or load from the two distances",
        "Explain why a force multiplier is also a distance divider: the work done is the same",
    ],
    parts=[
        explain(
            "Two equations, one idea",
            "<table class='tbl'><tr><th>Lever</th><th>Pivot between?</th><th>Effort distance vs load distance</th><th>Effect</th></tr>"
            "<tr><td>crowbar, see-saw, scissors, pliers</td><td>pivot <b>between</b> effort and load</td><td>effort further out</td><td><b>force multiplier</b></td></tr>"
            "<tr><td>wheelbarrow, nutcracker, bottle opener</td><td>load between pivot and effort</td><td>effort further out</td><td><b>force multiplier</b></td></tr>"
            "<tr><td>tweezers, fishing rod, your forearm</td><td>effort between pivot and load</td><td>effort <b>closer</b> than load</td><td><b>distance / speed multiplier</b>: a small movement of the effort moves the load a long way, but the effort must be <b>bigger</b> than the load</td></tr></table>"
            "<p><b>Equation 1 (moments):</b> at balance, $E \\times d_E = L \\times d_L$. Effort four times as far from the pivot as the load → effort a quarter of the load.</p>"
            "<p><b>Equation 2 (work):</b> when the lever turns, both ends move along arcs, and the distance each moves is <b>proportional to its distance from the pivot</b>. The effort end moves four times as far as the load end. Work done = force × distance moved, so work by the effort $= \\frac{L}{4} \\times 4s = L \\times s =$ work done on the load. <b>A lever multiplies force by dividing distance; it never multiplies work.</b> (With friction, the work by the effort is a bit more than the work on the load — efficiency below 100 %.)</p>"
            "<p>The June 2023 scheme (Q6(b)(ii), the forearm): the biceps is a distance multiplier — attached close to the elbow, it had to pull with <b>212 N</b> to hold the forearm and a ball whose own moment about the elbow was only 4.8 N m; the scheme accepted either adding up the total moment or adding the extra force the ball needed to the force already there.</p>",
        ),
        worked(
            "A wheelbarrow",
            "A wheelbarrow carries a 600 N load whose weight acts 0.4 m from the wheel axle. The handles are 1.6 m from the axle. (a) Calculate the effort needed to lift the handles. (b) The handles are lifted 0.2 m. Calculate the distance the load rises and the work done by the effort and on the load. (4 marks)",
            [
                r"<b>(a)</b> Moments about the axle: $E \times 1.6 = 600 \times 0.4 = 240$, so $E = 150$ N — a quarter of the load.",
                r"<b>(b)</b> Distances moved are in the ratio of the distances from the pivot: the load rises $0.2 \times \dfrac{0.4}{1.6} = 0.05$ m.",
                r"Work by the effort $= 150 \times 0.2 = 30$ J; work on the load $= 600 \times 0.05 = 30$ J. The same: the lever quartered the force and quartered the distance.",
            ],
        ),
        practice("Levers", [
            numeric("fe-t6-q1", "A bottle opener's pivot is 1.5 cm from the cap and the hand pushes 12 cm from the pivot with 20 N. Calculate the force on the cap.", 160, "N", "20 × 12 = L × 1.5.",
                    [r"$L = \dfrac{20 \times 12}{1.5} = 160$ N."]),
            choice("fe-t6-q2", "In a pair of tweezers the effort is applied closer to the pivot than the load. Which is true?",
                   ["The force on the object is bigger than the effort", "The force on the object is smaller than the effort but it moves further", "The force and distance are both multiplied", "Tweezers are not levers"], 1,
                   "A distance multiplier: more movement, less force."),
            written("fe-t6-q3", "A crowbar lets a person lift a 900 N rock with an effort of 150 N. Explain why the person does not get 'something for nothing'. (2)",
                    marks(["The effort end moves <b>six times as far</b> as the rock (distances moved are proportional to the distances from the pivot).",
                           "Work done = force × distance: $150 \\times 6s = 900 \\times s$ — the <b>work done by the effort equals the work done on the rock</b> (more, with friction); only the force is multiplied."]), lines=3),
            group("fe-t6-q4", "A see-saw lever lifts a 400 N load that is 0.5 m from the pivot. The effort is applied 2.0 m from the pivot.", [
                numeric("fe-t6-q4a", "Calculate the effort needed.", 100, "N", "Moments.", [r"$E \times 2.0 = 400 \times 0.5 = 200$, so $E = 100$ N."]),
                numeric("fe-t6-q4b", "The effort end moves down 0.8 m. Calculate how far the load rises.", 0.2, "m", "Ratio of distances from the pivot: 0.5 : 2.0.",
                        [r"$0.8 \times \dfrac{0.5}{2.0} = 0.2$ m."]),
                numeric("fe-t6-q4c", "Calculate the work done on the load.", 80, "J", "W = F × s.", [r"$400 \times 0.2 = 80$ J (the same as $100 \times 0.8$ by the effort)."]),
            ]),
            written("fe-t6-q5", "The biceps muscle attaches to the forearm 4 cm from the elbow; a weight is held in the hand 36 cm from the elbow. Explain why the muscle force is much larger than the weight held. (2)",
                    marks(["Taking moments about the elbow, muscle force × 4 cm = weight × 36 cm, so the muscle force is <b>nine times</b> the weight.",
                           "The forearm is a <b>distance multiplier</b>: the hand moves nine times as far as the muscle shortens, at the cost of a larger force."]), lines=3),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T7 · Gears, force and work: the winch 6-marker
# ---------------------------------------------------------------------

LEVELS_TABLE = (
    "<table class='tbl'><tr><th>Equation (Level 2 if left like this)</th><th>The same equation in the parts of the winch (Level 3)</th><th>Said in words (also Level 3)</th></tr>"
    "<tr><td>moment = force × perpendicular distance</td><td><b>moment of the handle = effort × length of the handle</b></td><td>the longer the handle, the smaller the effort needed for the same moment</td></tr>"
    "<tr><td>moment = force × perpendicular distance</td><td><b>moment on gear X = force between the teeth × radius of X</b> (and on Y: the same tooth force × radius of Y)</td><td>the bigger gear X is compared with Y, the more the moment is multiplied</td></tr>"
    "<tr><td>moment = force × perpendicular distance</td><td><b>moment of the load on the drum = load × radius of the drum</b></td><td>the smaller the drum, the smaller the moment the load produces, so the smaller the effort</td></tr>"
    "<tr><td>work done = force × distance moved</td><td><b>work done by the effort = effort × distance the end of the handle moves</b> (2π × handle length per turn)</td><td>a longer handle means the effort moves further each turn</td></tr>"
    "<tr><td>work done = force × distance moved</td><td><b>work done on the load = load × height the load rises</b> (2π × drum radius per turn of the drum)</td><td>a smaller drum lifts the load less far per turn</td></tr>"
    "<tr><td>gear ratio = turns of one ÷ turns of the other</td><td><b>turns of the handle for one turn of the drum = teeth on X ÷ teeth on Y</b></td><td>the more teeth X has compared with Y, the more turns of the handle per turn of the drum, so the further the effort moves for each metre the load rises</td></tr>"
    "<tr><td>efficiency = useful energy out ÷ total energy in</td><td><b>efficiency = work done on the load ÷ work done by the effort</b></td><td>friction in the gears and bearings means the effort does a little more work than the load gains</td></tr></table>"
)

section_t7 = section(
    "winch", "tricky", "Gears, force and work: the hand-winch 6-marker", "9.9P",
    equations=[r"E \times L_{\text{handle}} = F_{\text{teeth}} \times r_Y", r"F_{\text{teeth}} \times r_X = W \times r_{\text{drum}}", r"E \times s_{\text{effort}} = W \times h"],
    blurb="June 2025 Paper 2H Q9(b) asked how the sizes of a winch's parts decide the effort needed to lift a load. Students found it very hard. The difference between Level 2 and Level 3 was not more physics — it was writing each equation in the names of the parts.",
    tags=["P"],
    checklist=[
        "Follow the force through a winch: handle → small gear → large gear → drum → load",
        "Write moment, work and gear-ratio equations in the names of the parts (Level 3), not just in general (Level 2)",
        "Explain the effect of changing each size on the effort, in both the moment and the work pictures",
        "Avoid the three errors the examiners listed",
    ],
    parts=[
        explain(
            "The winch and how the question was marked",
            diagram(dg.winch_svg(), 700, 370, "The winch as modelled here: the handle turns small gear Y, which drives large gear X; X is fixed to the drum; the rope round the drum lifts the load.") +
            "<p><b>Following the force.</b> The effort $E$ on the handle makes a <b>moment about Y's axle</b> of $E \\times$ (length of handle). That moment is passed to gear Y, whose teeth push on gear X's teeth with a force $F_{\\text{teeth}}$ such that $F_{\\text{teeth}} \\times r_Y = E \\times L$. The <b>same tooth force</b> pushes on X at X's bigger radius, so the moment on X is $F_{\\text{teeth}} \\times r_X$ — bigger by the ratio $r_X / r_Y$. X and the drum turn together, and that moment must at least match the <b>moment of the load on the drum</b>, $W \\times r_{\\text{drum}}$. Put together: $$E = W \\times \\frac{r_{\\text{drum}}}{L} \\times \\frac{r_Y}{r_X}$$ — a long handle, a small drum and a big X compared with Y all make the effort smaller.</p>"
            "<p><b>Following the distance.</b> One turn of the handle moves the effort $2\\pi L$ and turns Y once; X turns $\\frac{\\text{teeth}_Y}{\\text{teeth}_X}$ of a turn, and so does the drum, raising the load $\\frac{\\text{teeth}_Y}{\\text{teeth}_X} \\times 2\\pi r_{\\text{drum}}$. The effort moves <b>much further</b> than the load rises. Work done by the effort = work done on the load (ignoring friction), so $E \\times s_{\\text{effort}} = W \\times h$, and the effort is smaller than the load by exactly the ratio of the distances. <b>Both pictures give the same answer</b> — the moment picture explains the force, the work picture explains why it is not something for nothing.</p>"
            "<p><b>How it was marked.</b> The mark scheme listed the sizes (length of bar, number of teeth / radius of each gear, radius of drum), the equations (moment, work done, gear ratio, efficiency), and the <b>links between them</b>: \"moment of effort = effort × length of handle\", \"moment of load on drum = load × radius of drum\", \"work done by effort = force × distance moved by the end of the handle\", \"work done on load = load × distance raised\". What separated the levels: writing an equation in its <b>general</b> form (\"moment = force × distance\") reached Level 2; writing it <b>in the parts of the winch</b> (\"moment of the handle = effort × length of the handle\") — or saying the same thing in words — got into Level 3. Any of the equations would do.</p>"
            + LEVELS_TABLE +
            "<p><b>The three errors the examiners reported.</b> (1) <b>Confusing work done with moment</b> — both are force × distance, but in a moment the distance is the perpendicular distance <i>from the pivot</i> (N m), in work it is the distance <i>moved along the force</i> (J); mixing them capped answers at Level 2. (2) Saying <b>the force of gear Y on gear X is increased</b> — the force between the teeth is the <b>same</b> on both (an interaction pair); it is the <b>moment</b> that is bigger on X, because X's radius is bigger. (3) <b>Describing the sizes without their effect</b> — \"the handle is long and X is bigger than Y\" is Level 1; every size must be followed by what changing it does to the effort.</p>",
        ),
        worked(
            "The numbers",
            "In the winch drawn above, the handle is 0.30 m long, gear Y has radius 0.05 m (8 teeth), gear X has radius 0.15 m (24 teeth), the drum has radius 0.05 m and the load weighs 600 N. Ignore friction. (a) Calculate the moment of the load on the drum. (b) Calculate the force between the gear teeth. (c) Calculate the effort. (d) Check the answer using work done for one turn of the handle.",
            [
                r"<b>(a)</b> Moment of the load on the drum $= W \times r_{\text{drum}} = 600 \times 0.05 = 30$ N m. Gear X must supply this.",
                r"<b>(b)</b> Moment on X = tooth force × radius of X: $F_{\text{teeth}} \times 0.15 = 30$, so $F_{\text{teeth}} = 200$ N.",
                r"<b>(c)</b> The same 200 N acts on Y at 0.05 m: moment on Y $= 200 \times 0.05 = 10$ N m. Moment of the handle = effort × length of handle: $E \times 0.30 = 10$, so $E = 33$ N (33.3) — an 18 times smaller force than the load ($6 \times 3$).",
                r"<b>(d)</b> One turn of the handle: the effort moves $2\pi \times 0.30 = 1.88$ m, work by the effort $= 33.3 \times 1.88 = 63$ J. Y turns once, X and the drum turn $8/24 = \tfrac13$ of a turn, the load rises $\tfrac13 \times 2\pi \times 0.05 = 0.105$ m, work on the load $= 600 \times 0.105 = 63$ J. ✓",
            ],
        ),
        worked(
            "A Level 3 answer",
            "Using physics principles, explain how the sizes of the handle, the gears and the drum determine the effort needed to lift the load. (6 marks)",
            [
                "<b>Handle:</b> the moment of the handle = effort × length of the handle. For the moment the winch needs, a <b>longer handle means a smaller effort</b>; in the work picture, a longer handle means the end of the handle <b>moves further each turn</b>, so for the same work done the effort is smaller.",
                "<b>Gears:</b> the force between the teeth is the same on both gears, but moment on gear X = tooth force × radius of X, and moment on Y = tooth force × radius of Y; because <b>X has the larger radius (more teeth) the moment is multiplied</b> by the ratio of the radii.",
                "Equally, the turns of the handle for one turn of the drum = teeth on X ÷ teeth on Y, so the <b>more teeth X has compared with Y, the more turns of the handle</b> — the effort moves further for each metre the load rises, and work done by the effort = effort × distance the handle end moves must equal work done on the load = load × height raised, so the effort is smaller.",
                "<b>Drum:</b> the moment of the load on the drum = load × radius of the drum, so a <b>smaller drum means a smaller moment to overcome</b> and a smaller effort (but the load rises less per turn, so more turns are needed).",
                "<b>Overall:</b> effort = load × (drum radius ÷ handle length) × (radius of Y ÷ radius of X): long handle, small drum, X much bigger than Y → small effort. The <b>work done is not reduced</b> — the effort just moves much further than the load.",
                "<b>Efficiency:</b> friction in the gears and bearings means the work done by the effort is a little more than the work done on the load, so the real effort is slightly larger than calculated.",
            ],
        ),
        practice("The winch", [
            choice("fe-t7-q1", "Two answers: A — \"moment = force × distance, so the handle should be long\"; B — \"the moment of the handle = effort × length of the handle, so for the same moment a longer handle needs a smaller effort\". Which reaches Level 3 and why?",
                   ["A — it is shorter", "B — the equation is written in the parts of the winch and its effect on the effort is stated", "Both — they say the same thing", "Neither — a calculation is needed"], 1,
                   "The general equation is Level 2; the equation in the parts, with the effect, is Level 3."),
            written("fe-t7-q2", "A student writes: \"The large gear X increases the force from gear Y.\" Explain what is wrong and write a correct sentence. (2)",
                    marks(["The <b>force between the teeth is the same</b> on both gears (an interaction pair); a gear cannot increase a force on itself.",
                           "Correct: \"the same tooth force acts at the <b>larger radius of X</b>, so the <b>moment</b> on X (tooth force × radius of X) is larger than the moment on Y.\""]), lines=3),
            group("fe-t7-q3", "A winch has a handle 0.40 m long on the axle of a 10-tooth gear (radius 0.04 m), which drives a 40-tooth gear (radius 0.16 m) fixed to a drum of radius 0.08 m. The load is 800 N. Ignore friction.", [
                numeric("fe-t7-q3a", "Calculate the moment of the load on the drum.", 64, "N m", "Load × radius of drum.", [r"$800 \times 0.08 = 64$ N m."]),
                numeric("fe-t7-q3b", "Calculate the force between the gear teeth.", 400, "N", "Moment on the 40-tooth gear = tooth force × 0.16.", [r"$F \times 0.16 = 64$, so $F = 400$ N."]),
                numeric("fe-t7-q3c", "Calculate the effort on the handle.", 40, "N", "Moment on the 10-tooth gear = 400 × 0.04; handle moment = effort × 0.40.",
                        [r"Moment on the small gear $= 400 \times 0.04 = 16$ N m.", r"$E \times 0.40 = 16$, so $E = 40$ N."]),
                numeric("fe-t7-q3d", "Calculate how far the load rises for one turn of the handle.", 0.126, "m", "The drum turns 10/40 of a turn; one turn lifts 2π × 0.08.",
                        [r"$\tfrac{10}{40} \times 2\pi \times 0.08 = 0.126$ m (0.13 m to 2 s.f.)."], tolerance=0.05),
                numeric("fe-t7-q3e", "Show that the work done by the effort in one turn equals the work done on the load. Give the work done by the effort.", 100.5, "J", "Effort × 2π × 0.40.",
                        [r"Effort: $40 \times 2\pi \times 0.40 = 100.5$ J.", r"Load: $800 \times 0.126 = 100.5$ J. ✓"], tolerance=0.03),
            ]),
            written("fe-t7-q4", "Explain, using work done, why the effort on a winch handle is much smaller than the load it lifts. (3)",
                    mark_scheme([
                        ("Distances", "In one turn the effort moves <b>2π × the handle length</b>, while the load rises only a fraction of 2π × the drum radius (the drum turns fewer times than the handle because of the gear ratio)."),
                        ("Equal work", "Work done by the effort (effort × distance the handle end moves) = work done on the load (load × height raised), ignoring friction."),
                        ("Conclusion", "Since the effort's distance is <b>much larger</b>, the effort is <b>smaller</b> than the load in the same ratio."),
                    ]), lines=4),
            choice("fe-t7-q5", "A student writes \"work done = force × distance, so a longer handle means more moment\". Why did the examiners cap this at Level 2?",
                   ["Handles do not matter", "It confuses work done with moment — the distance in a moment is the perpendicular distance from the pivot, not the distance moved", "Work done is not on the specification", "It should say energy"], 1,
                   "The first of the three reported errors."),
            written("fe-t7-q6", "The drum of a winch is replaced by one with twice the radius. Explain the effect on (a) the effort needed and (b) the number of turns of the handle to lift the load 1 m. (3)",
                    mark_scheme([
                        ("Effort", "The moment of the load on the drum = load × radius of the drum <b>doubles</b>, so the moment needed at the handle doubles and the <b>effort doubles</b>."),
                        ("Turns", "Each turn of the drum lifts the load 2π × radius, now <b>twice as far</b>, so <b>half as many turns</b> of the handle are needed."),
                        ("Work", "Twice the force for half the distance: the work done by the effort is <b>unchanged</b> (= load × 1 m)."),
                    ]), lines=4),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T8 · Friction and lubrication explained
# ---------------------------------------------------------------------

section_t8 = section(
    "friction-explain", "tricky", "Friction: explaining it, using it, reducing it", "9.1, 9.10",
    equations=[r"\text{work against friction} \rightarrow \text{thermal store}"],
    blurb="Friction questions are marked on specifics: name the surfaces, say which way the force acts, say where the energy goes, and when asked for a way to reduce it, give a method.",
    checklist=[
        "Describe the direction of friction and what decides its size",
        "Explain the energy transfer when work is done against friction",
        "Give methods, not reasons, for reducing friction — and say when friction is wanted",
    ],
    parts=[
        explain(
            "What the marks are on",
            "<p><b>Direction:</b> friction acts <b>along the surfaces</b>, <b>opposite to the motion</b> (or the attempted motion) of one surface over the other. On a car's driving wheels it acts <b>forwards</b> — the tyre pushes back on the road, the road pushes forwards on the tyre — which is how a car moves at all.</p>"
            "<p><b>Size:</b> larger with rougher surfaces and with a larger <b>normal contact force</b> pressing them together (a heavier box is harder to push); it does <b>not</b> depend on the area of contact at GCSE level. Air resistance grows with <b>speed</b> and with <b>area</b>.</p>"
            "<p><b>Energy:</b> work is done against friction, $W = F \\times d$, and that energy is transferred to the <b>thermal store</b> of the surfaces and the air — <b>dissipated</b>. In a machine it is why efficiency is below 100 %. (The June 2023 report, Q9(a)(iii): asked for a reason <i>other than friction</i> for wasted work in a pulley, most students still wrote \"heat\" or \"squeaky wheels\", which <b>are</b> friction; lifting the rope and pulley themselves, or stretching the rope, were the credited answers.)</p>"
            "<p><b>Reducing it:</b> <b>lubricate</b> (oil separates the surfaces), use <b>ball bearings</b> or wheels (rolling instead of sliding), <b>polish</b> the surfaces, <b>streamline</b> for air resistance. Each is a method; \"reduce friction\" is not.</p>"
            "<p><b>Wanting it:</b> brakes, tyres on a wet road (tread channels water away), shoes, climbing holds, a nail in wood, striking a match. There the answer is to <b>increase</b> friction: rougher surface, larger normal force, drier contact.</p>",
        ),
        worked(
            "Three marks on a box",
            "A 30 N box is pushed across a floor at constant speed with a force of 12 N. (a) State the size and direction of the friction. (b) Explain what happens to the energy transferred by the push. (c) Suggest one way to reduce the force needed. (4 marks)",
            [
                "<b>(a)</b> <b>12 N, backwards</b> (opposite to the motion): constant speed means balanced horizontal forces.",
                "<b>(b)</b> Work is done against friction ($12$ J for every metre); the energy goes to the <b>thermal store</b> of the box's base and the floor — they warm slightly — and spreads to the surroundings, so it is <b>dissipated</b>.",
                "<b>(c)</b> <b>Put it on a trolley with wheels</b> (rolling friction is much smaller than sliding) or <b>polish / wax the floor</b> — a specific method.",
                "Not: \"reduce the friction\" — that is the aim, not a method.",
            ],
        ),
        practice("Friction", [
            written("fe-t8-q1", "A car's engine turns the wheels. Explain how friction makes the car move forwards. (2)",
                    marks(["The turning tyre pushes <b>backwards on the road</b> (friction between tyre and road).",
                           "By the interaction pair the road pushes <b>forwards on the tyre</b> with an equal force — this is the driving force on the car."]), lines=2),
            choice("fe-t8-q2", "A question asks for a reason, other than friction, why the work done by the effort on a pulley is more than the work done on the load. Which answer scores?",
                   ["The pulley wheels squeak", "Heat is produced", "Work is done lifting the rope and the lower pulley block as well as the load", "Energy is wasted"], 2,
                   "Squeaks and heat are friction; \"energy is wasted\" is the question restated."),
            written("fe-t8-q3", "Explain why a bicycle slows down and stops when the rider stops pedalling, in terms of forces and energy. (3)",
                    mark_scheme([
                        ("Forces", "<b>Friction</b> (bearings, tyres on the road) and <b>air resistance</b> act <b>against the motion</b>; with no driving force the resultant is backwards."),
                        ("Deceleration", "A backward resultant force means the bicycle <b>decelerates</b> until its velocity is zero."),
                        ("Energy", "The bicycle's <b>kinetic store</b> is transferred, by work done against the resistive forces, to the <b>thermal store</b> of the parts and the air — dissipated."),
                    ]), lines=4),
            choice("fe-t8-q4", "Which change increases the friction between a crate and the floor?",
                   ["Polishing the floor", "Putting the crate on rollers", "Adding more weight to the crate", "Oiling the floor"], 2,
                   "A larger normal contact force → larger friction."),
            written("fe-t8-q5", "Give two different methods of reducing the friction in a machine's moving parts, and explain how one of them works. (3)",
                    marks(["Method 1: <b>lubricate</b> with oil or grease. Method 2: use <b>ball bearings</b> (or wheels) so parts roll rather than slide.",
                           "Lubrication works because the oil forms a <b>layer that separates the two surfaces</b>…", "…so they no longer rub directly and the frictional force (and the energy dissipated as heat) is smaller."]), lines=3),
            written("fe-t8-q6", "Explain why car tyres have tread patterns rather than being smooth. (2)",
                    marks(["On a wet road the grooves <b>channel water away</b> from the contact between rubber and road.",
                           "This keeps the rubber in contact with the road, maintaining the <b>friction</b> needed for grip when braking and steering (a smooth tyre would slide on a film of water)."]), lines=2),
        ]),
    ],
)

SECTIONS = [section_t1, section_t2, section_t3, section_t4, section_t5, section_t6, section_t7, section_t8]

# ---------------------------------------------------------------------
# Flashcards (the key-word definitions are added by fe_nn.FACTS_KW)
# ---------------------------------------------------------------------

FACTS = [
    # N1
    fact("Name the three non-contact forces and their fields.", "Gravitational (gravitational field), electrostatic (electric field), magnetic (magnetic field).", "force-types"),
    fact("Name five contact forces.", "Normal contact force, friction, tension, drag (air / water resistance), upthrust.", "force-types"),
    fact("In which direction does the normal contact force act?", "At right angles (normal) to the surface, pushing away from it.", "force-types"),
    fact("What is a field, in one sentence?", "A region in which a mass / charge / magnetic material experiences a force.", "force-types"),
    fact("How should a force arrow be drawn on a surface?", "Starting or ending at the point where the force acts, at right angles to the surface for a normal contact force.", "force-types"),
    # N2
    fact("Four features of an interaction pair?", "Equal in size, opposite in direction, same type of force, acting on different objects.", "force-pairs"),
    fact("Are the weight of a book and the normal contact force from the table an interaction pair?", "No — both act on the book and they are different types. They are balanced forces. The pair to the weight is the book pulling the Earth up.", "force-pairs"),
    fact("How do you find the partner of a force?", "Swap the two objects: 'A pushes B' ↔ 'B pushes A', same size, opposite direction.", "force-pairs"),
    # N3
    fact("Vector or scalar: force, speed, velocity, mass, displacement, energy, acceleration, time, momentum, distance?", "Vectors: force, velocity, displacement, acceleration, momentum. Scalars: speed, mass, energy, time, distance.", "vectors-scalars-nn"),
    fact("What do the length and direction of a force arrow show?", "Length: the size of the force (to scale). Direction: the direction of the force.", "vectors-scalars-nn"),
    fact("Why can two 6 N forces have a resultant anywhere from 0 to 12 N?", "Force is a vector: the resultant depends on the directions — same direction 12 N, opposite 0 N, at an angle in between.", "vectors-scalars-nn"),
    # N4
    fact("Five rules of a free body force diagram?", "One object only; every arrow from (or through) its centre; correct directions; labelled with name and size; lengths in proportion.", "free-body"),
    fact("Why are force arrows drawn from the centre of the object?", "A force drawn at an edge would make the object rotate; through the centre it only changes its motion. The 2025 examiners penalised edge arrows.", "free-body"),
    fact("Free body diagram of a car at constant velocity?", "Weight down = normal contact force up; driving force forwards = drag + friction backwards. Four arrows, two equal pairs.", "free-body"),
    fact("Free body diagram of a ball at the top of its flight (no air resistance)?", "One arrow: weight, downwards. Nothing pushes up once it has left the hand.", "free-body"),
    # N5
    fact("What is a resultant force?", "The single force that has the same effect as all the forces acting together.", "resultant-line"),
    fact("How do forces along a line combine?", "Same direction: add. Opposite directions: subtract; the resultant is in the direction of the larger.", "resultant-line"),
    fact("What does a zero resultant force mean for the motion?", "The velocity does not change: the object is at rest or moves at constant velocity (steady speed in a straight line).", "resultant-line"),
    fact("What does a non-zero resultant force do?", "Accelerates the object in the direction of the resultant: speeds up, slows down or changes direction (F = m a).", "resultant-line"),
    fact("Does 'balanced forces' mean 'stationary'?", "No. A skydiver at terminal velocity has balanced forces and is falling fast.", "resultant-line"),
    # N6
    fact("Equation for the moment of a force, with unit?", "Moment = force × distance normal (perpendicular) to the direction of the force, from the pivot. Unit N m.", "moment-nn"),
    fact("Why must the distance in a moment be the perpendicular distance?", "Only the part of the force at right angles to the lever turns it; pushing along the lever towards the pivot has no turning effect.", "moment-nn"),
    fact("Two ways to increase a moment?", "Increase the force, or increase the perpendicular distance from the pivot (longer spanner, handle far from the hinge).", "moment-nn"),
    fact("Why is the moment unit N m and not J?", "In a moment the distance is across the force (from the pivot); in work it is along the force. Different quantities.", "moment-nn"),
    fact("The commonest moments calculation error?", "Not converting cm to m — a 30 cm spanner is 0.30 m.", "moment-nn"),
    # N7
    fact("State the principle of moments (both marks).", "For an object in equilibrium, the sum of the clockwise moments about a point = the sum of the anticlockwise moments about that point.", "balance-nn"),
    fact("What working do examiners expect in a principle-of-moments question?", "Each moment calculated as force × distance, the totals set equal — not just ratios of forces and distances.", "balance-nn"),
    fact("From where are the distances in a moments question measured?", "From the pivot — not from the end of the beam.", "balance-nn"),
    fact("Why can a wheelbarrow lift a load with a small effort?", "The wheel is the pivot; the load is close to it, the handles far from it: effort × long distance = load × short distance.", "balance-nn"),
    # N8
    fact("Lever equation at balance?", "Effort × distance of effort from pivot = load × distance of load from pivot.", "levers-gears"),
    fact("How do gears transmit a turning effect?", "Teeth mesh; the force between the teeth is the same on both wheels; the moment on each wheel = that force × its own radius.", "levers-gears"),
    fact("Small gear driving a large gear: effect?", "Larger moment on the large gear, but it turns fewer times (slower) — a force multiplier.", "levers-gears"),
    fact("Large gear driving a small gear: effect?", "Smaller moment on the small gear, but it turns more times (faster) — a speed multiplier.", "levers-gears"),
    fact("How are numbers of teeth and numbers of turns related?", "Turns are in inverse ratio to teeth: a 10-tooth gear turns twice for one turn of a 20-tooth gear.", "levers-gears"),
    fact("Which way do meshed gears turn?", "Opposite directions. (A chain or belt keeps two wheels turning the same way.)", "levers-gears"),
    fact("To double the speed of an output gear, what do you add?", "A gear with half as many teeth meshing with it (June 2024).", "levers-gears"),
    # N9
    fact("Where does energy go when work is done against friction?", "To the thermal store of the surfaces and surroundings — dissipated, no longer useful.", "lubrication"),
    fact("How does a lubricant reduce friction?", "It forms a layer that separates the sliding surfaces so they do not rub directly; the frictional force is smaller, less energy is dissipated.", "lubrication"),
    fact("\"Suggest a way to reduce friction\" — what kind of answer scores?", "A method: oil the axles, use ball bearings, polish the surface. 'Reduce friction' alone is a reason, not a method, and scores nothing (2025).", "lubrication"),
    fact("Where should friction not be reduced?", "Brakes, tyres, shoes, matches — anywhere grip is the point.", "lubrication"),
    # T1
    fact("Steps to find a resultant by scale drawing?", "State a scale; draw the first force; draw the second from its tip (tip to tail); draw the resultant from the start of the first to the tip of the second; measure length and angle.", "scale-resultant"),
    fact("Resultant of 3 N and 4 N at right angles?", "5 N (Pythagoras: 9 + 16 = 25), at 53° to the 3 N.", "scale-resultant"),
    fact("Resultant of 6 N and 8 N at right angles? And 5 N and 12 N?", "10 N; 13 N.", "scale-resultant"),
    fact("What did the 2025 scheme mark in a resultant-by-drawing question?", "The direction (judged by eye) and the size (within a tolerance) — the arrow must be drawn and labelled.", "scale-resultant"),
    # T2
    fact("What does it mean to resolve a force?", "To split it into two components at right angles that together have the same effect as the original force.", "resolving"),
    fact("How do you resolve a force by scale drawing?", "Draw the force to scale at its angle; drop perpendiculars from its tip to the two directions; measure the two sides.", "resolving"),
    fact("Which component of an angled rope pull moves a sledge along the ground?", "The horizontal component. The vertical component only reduces the normal contact force.", "resolving"),
    fact("Components of weight on a slope?", "One along the slope (tends to make it slide; friction opposes) and one into the slope (balanced by the normal contact force). Steeper → bigger along-slope component.", "resolving"),
    # T3
    fact("What do forces in equilibrium look like drawn tip to tail?", "A closed shape (a triangle for three forces): the resultant is zero, so the last tip returns to the start.", "equilibrium-triangle"),
    fact("A 10 N sign on two strings at 45° to the vertical: each tension?", "About 7.1 N (each vertical component is 5 N).", "equilibrium-triangle"),
    fact("Why does a nearly horizontal washing line have a large tension?", "Only a small fraction of each tension acts vertically, but the vertical components must still add up to the weight, so the tensions are large.", "equilibrium-triangle"),
    # T4
    fact("The sentence pattern for 'explain the motion'?", "[Force A] is greater than [force B], so there is a resultant force [direction], so the object accelerates [direction]; as speed changes, [force B] changes until the forces balance and the velocity is constant.", "resultant-motion"),
    fact("What happens when a parachute opens at terminal velocity?", "Air resistance becomes greater than weight → resultant upwards → decelerates (still falling) → air resistance falls until it equals weight → new lower terminal velocity.", "resultant-motion"),
    fact("Tension in a lift cable: constant velocity vs accelerating upwards?", "Constant velocity: tension = weight. Accelerating upwards: tension = weight + m a (greater than weight).", "resultant-motion"),
    # T5
    fact("Where does the weight of a uniform beam act?", "At its centre (centre of mass). No moment if the pivot is at the centre; otherwise include it as a force.", "moments-hard"),
    fact("How do you handle several forces in a moments problem?", "Find the turning sense of each about the pivot, calculate each moment, add the clockwise ones and the anticlockwise ones separately, set the totals equal.", "moments-hard"),
    fact("At the moment a plank tips off a support, what is true?", "The force from the other support is zero; take moments about the edge support.", "moments-hard"),
    fact("How do you find the force at the pivot?", "From the forces, not the moments: in equilibrium, upward forces = downward forces, so pivot force = total weight on the beam.", "moments-hard"),
    # T6
    fact("A lever multiplies force by…?", "…dividing distance: the effort moves further than the load in the same ratio, so work by the effort = work on the load (ignoring friction).", "levers-hard"),
    fact("Example of a distance multiplier lever?", "Tweezers, a fishing rod, the forearm: effort closer to the pivot than the load — more movement, bigger effort than load.", "levers-hard"),
    fact("Biceps holding a weight in the hand: why is the muscle force so large?", "The muscle attaches close to the elbow; muscle force × short distance = weight × long distance, so the force is many times the weight (212 N in June 2023).", "levers-hard"),
    # T7
    fact("Level 2 vs Level 3 in the 2025 winch question?", "Level 2: the equation in general ('moment = force × distance'). Level 3: the equation in the parts ('moment of the handle = effort × length of handle') or the same in words, with its effect on the effort.", "winch"),
    fact("Moment equation in the parts of a winch (three versions)?", "Moment of the handle = effort × length of handle; moment on gear X = tooth force × radius of X; moment of the load on the drum = load × radius of drum.", "winch"),
    fact("Work equation in the parts of a winch?", "Work done by the effort = effort × distance the end of the handle moves; work done on the load = load × height the load rises; the two are equal ignoring friction.", "winch"),
    fact("Why is the effort on a winch much smaller than the load?", "Moment picture: long handle, small drum and big X over small Y multiply the moment. Work picture: the effort moves much further than the load rises, so for equal work it is a smaller force.", "winch"),
    fact("Three errors in the 2025 winch answers?", "Confusing work done with moment; saying gear Y's force on X is 'increased' (the tooth force is the same, the moment is bigger); describing sizes without their effect.", "winch"),
    fact("What does the gear ratio tell you in a winch?", "How many turns of the handle for one turn of the drum (teeth on X ÷ teeth on Y) — so how much further the effort moves than the load rises.", "winch"),
    fact("Effect of a bigger drum on a winch?", "Larger load moment (load × radius) so a larger effort — but fewer turns, since each turn lifts the load further. Work unchanged.", "winch"),
    # T8
    fact("In which direction does friction act?", "Along the surfaces, opposite to the (attempted) motion of one over the other. On a driving wheel it acts forwards on the car.", "friction-explain"),
    fact("What increases sliding friction?", "Rougher surfaces and a larger normal contact force; not the area of contact.", "friction-explain"),
    fact("Reasons other than friction for wasted work in a pulley?", "Lifting the rope and the pulley block themselves; stretching the rope (June 2023). 'Heat' and 'squeaks' are friction.", "friction-explain"),
    fact("Four methods of reducing friction?", "Lubricate; ball bearings or wheels (rolling); polish the surfaces; streamline (for drag).", "friction-explain"),
]
