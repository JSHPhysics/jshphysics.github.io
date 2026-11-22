"""
mf_exam.py — Topic 2: additions from the examiners' reports and mark
schemes (SOP steps 2 and 5). See motion-and-forces_notes.md for the
evidence behind each one.

Each entry says which section it goes into and what it adds.
"""

from revlib import (
    axis, choice, draw, explain, ewau, fact, graph, group, line, mark_scheme,
    marks, numeric, sf, written,
)

# ---------------------------------------------------------------------
# N2 · m/s → km/h (June 2022 Q3(a)(ii): "convert one unit at a time")
# ---------------------------------------------------------------------

q_ms_to_kmh = numeric(
    "t2-n2-q7",
    "A car travels at 15 m/s. Convert this speed to km/h.",
    15 * 3600 / 1000, "km/h",
    "Convert one unit at a time: metres per second → metres per hour (× 3600) → kilometres per hour (÷ 1000).",
    [r"In one hour (3600 s) the car travels $15 \times 3600 = 54\,000$ m.",
     r"$54\,000\ \text{m} = 54$ km, so the speed is 54 km/h.",
     r"Shortcut: m/s $\times 3.6$ = km/h. Show the conversion — it is a mark on its own."],
)

# ---------------------------------------------------------------------
# N9 · acceleration at constant velocity is zero (June 2023 Q2(b)(iv))
# ---------------------------------------------------------------------

q_zero_acc = choice(
    "t2-n9-q7",
    "A paper cupcake case falls at a constant velocity. What is its acceleration?",
    ["10 m/s² downwards", "Zero", "10 m/s² upwards", "It depends on its mass"], 1,
    "Constant velocity means the velocity is not changing, so the acceleration is zero — the air resistance has grown to equal the weight and the resultant force is zero. \"Constant\" on its own is not the answer the examiner wants; say zero.",
)

# ---------------------------------------------------------------------
# N8 · describing a speed investigation (June 2023 Q2(b)(i), 4 marks)
# ---------------------------------------------------------------------

q_describe_speed = written(
    "t2-n8-q7",
    "A student has some paper cupcake cases, a metre rule and a stopwatch. Describe how the student could investigate how the speed of fall depends on the number of cupcake cases in a stack. (4)",
    mark_scheme([
        ("Distance", "Measure the <b>height</b> the stack falls from, with the metre rule (keep it the same each time)."),
        ("Time", "Measure the <b>time of fall</b> with the stopwatch."),
        ("Speed", "Calculate <b>average speed = distance ÷ time</b>."),
        ("Change", "Repeat with a <b>different number of cupcake cases</b> in the stack (several stacks)."),
        ("Repeat &amp; mean", "<b>Repeat and average</b> the time for each stack."),
        ("Use the result", "<b>Plot a graph</b> of speed of fall against number of cases."),
    ], total=4, extra=["Any four of the six rows score. \"Time it\" is accepted for measuring the time; \"keep the same height\" is accepted in place of \"measure the height\" (it is not an extra mark)."]),
    lines=5,
    hint="Two measurements, one calculation, what you change, repeats, a graph — pick four.",
)

# ---------------------------------------------------------------------
# N14 · momentum in standard form (June 2023 Q9(a): "the only issue was
# standard form with negative indices")
# ---------------------------------------------------------------------

mol_m = 6.6e-26
mol_v = 480
q_momentum_sf = numeric(
    "t2-n14-q7",
    "A gas molecule has a mass of $6.6 \\times 10^{-26}$ kg and moves at 480 m/s. Calculate its momentum. Give your answer in standard form.",
    sf(mol_m * mol_v, 2), "kg m/s",
    "Enter the mass with the ×10ˣ key: 6.6 ×10ˣ (−)26. Keep the answer in standard form; do not write out the zeros.",
    ewau(r"p = m \times v", r"p = 6.6 \times 10^{-26} \times 480", r"3.2 \times 10^{-23}", "kg m/s — type it as 3.2e-23"),
    tags=["H"],
)

# ---------------------------------------------------------------------
# N15 · stopping distances: the physics reason, and reaction time to 2 s.f.
# (June 2022 Q3(a)(i) and (iii))
# ---------------------------------------------------------------------

q_wet_road = written(
    "t2-n15-q8",
    "Explain why it is safer to drive more slowly when the road is wet. (2)",
    marks(["On a wet road there is <b>less friction</b> between the tyres and the road, so the braking force is smaller and the <b>braking distance is longer</b> for the same speed.",
           "Driving more slowly <b>reduces both the thinking distance and the braking distance</b>, so the car can stop in a shorter distance (before reaching a hazard)."]),
    lines=3,
    hint="It is a physics exam: give a reason, then a \"because\" that uses friction and braking distance.",
)

q_reaction_time = numeric(
    "t2-n15-q9",
    "A car travelling at 13 m/s has a thinking distance of 12 m. Calculate the driver's reaction time. Give your answer to 2 significant figures.",
    sf(12 / 13, 2), "s",
    "Thinking distance = speed × reaction time; substitute, then rearrange. The answer line must show 2 significant figures.",
    [r"$\text{thinking distance} = \text{speed} \times \text{reaction time}$, so $12 = 13 \times t$.",
     r"$t = \dfrac{12}{13} = 0.923\ldots$ s.",
     r"To 2 significant figures: $t = 0.92$ s. Writing 0.923 on the answer line loses the mark the question asked for."],
)

# ---------------------------------------------------------------------
# T1 · continuing a v–t graph below the axis (June 2023 Q5(e): "do not
# accept vertical line; do not accept line extending to the left")
# ---------------------------------------------------------------------

grid_bounce = graph(
    axis("time in s", 2, 0.5), axis("velocity in m/s", 10, 5, mn=-10),
    [line([[0, 10], [1, 0]])],
    "A velocity–time graph with a straight line from (0, 10) down to (1, 0); the grid continues to 2 s and down to −10 m/s.",
)
answer_bounce = graph(
    axis("time in s", 2, 0.5), axis("velocity in m/s", 10, 5, mn=-10),
    [line([[1, 0], [2, -10]])],
    "The line continues from (1, 0) down to (2, −10): the same gradient, below the axis.",
)
q_draw_fall = draw(
    "t2-t1-q5",
    "A ball is thrown straight up at 10 m/s; taking up as positive, the graph shows its velocity until it stops at the top after 1 s. It then falls for 1 s. Draw the line for the fall on the grid (tap the grid to place the points in order, or draw it on paper).",
    grid_bounce,
    "A straight line from (1, 0) to (2, −10): the ball's velocity is now downwards (negative) and growing at the same rate, 10 m/s each second. The line must start where the first one ended, slope at the same gradient, and go below the time axis — not vertical, and not to the left of 1 s.",
    answer_graph=answer_bounce, check=True,
    hint="Gravity does not switch off at the top: the acceleration is still 10 m/s² downwards, so the velocity keeps falling by 10 m/s every second — through zero and into negative values.",
)

# ---------------------------------------------------------------------
# T5 · Newton's third law in a specific collision: name both forces
# (June 2022 Q7(c)(ii); June 2025 Q8(a)(iii) "a deceptively difficult
# concept")
# ---------------------------------------------------------------------

q_racket_ball = written(
    "t2-t5-q7",
    "A tennis racket hits a ball. Explain the forces involved in terms of Newton's third law. (2)",
    marks(["The racket exerts a force on the ball, <b>and the ball exerts a force on the racket</b> — name both forces.",
           "The two forces are <b>equal in size and opposite in direction</b> (and both are contact forces, acting on different objects)."]),
    lines=3,
    hint="Quoting the law scores one mark at most. Say what the two forces are in this collision — \"the force of the racket on the ball\" and \"the force of the ball on the racket\".",
)

# ---------------------------------------------------------------------
# T9 · change in momentum when the direction reverses, with the time in
# milliseconds (June 2022 Q7(c)(i), June 2023 Q9(b): the two named errors)
# ---------------------------------------------------------------------

ball_m = 0.16
ball_u = 20
ball_v = 25
contact_ms = 70
dp = ball_m * (ball_v + ball_u)
force_ball = dp / (contact_ms / 1000)
q_bounce_group = group(
    "t2-t9-q8",
    "A tennis ball of mass 0.16 kg travels towards a racket at 20 m/s. The racket hits it and it leaves in the opposite direction at 25 m/s. The ball is in contact with the racket for 70 ms.",
    [
        numeric("t2-t9-q8a", "Calculate the change in momentum of the ball. (Give the size.)", sf(dp, 2), "kg m/s",
                "Velocity is a vector. Take the direction towards the racket as positive: $u = +20$ m/s, $v = -25$ m/s. The change is $v - u$, not the difference of the two sizes.",
                [r"Take towards the racket as positive: $u = +20$ m/s, $v = -25$ m/s.",
                 r"$\Delta p = m v - m u = 0.16 \times (-25) - 0.16 \times 20 = -4 - 3.2 = -7.2$ kg m/s.",
                 r"Size of the change: 7.2 kg m/s (the minus sign says it is directed away from the racket). Subtracting $4 - 3.2 = 0.8$ ignores the change of direction and loses the <b>final mark only</b> — the schemes still give the substitution mark (June 2022 Q7(c)(i): \"42.5 N scores 2 marks maximum\"; June 2023 Q9(b): \"allow Δp = ±0.2\"). Get the direction right and you keep all three."], label="a", tags=["H"]),
        numeric("t2-t9-q8b", "Calculate the average force the racket exerts on the ball.", sf(force_ball, 3), "N",
                "70 ms is 0.070 s — ms means milliseconds.",
                [r"$t = 70\ \text{ms} = 0.070$ s.",
                 r"$F = \dfrac{\Delta p}{t} = \dfrac{7.2}{0.070} = 103$ N (to 3 s.f.).",
                 r"Using 70 instead of 0.070 gives 0.1 N — a force smaller than the weight of a feather, which is the sense check that catches it."], label="b", tags=["H"]),
    ],
)

# ---------------------------------------------------------------------
# T3 · free fall: a = g, and the equation has to be chosen (June 2023
# Q3(b): "the majority scored 0 — not recognising which equation to use
# or that the acceleration is g")
# ---------------------------------------------------------------------

drop_h = 20
drop_v = (2 * 10 * drop_h) ** 0.5
q_free_fall = group(
    "t2-t3-q7",
    "A stone is dropped from rest from a bridge 20 m above a river. Ignore air resistance and take $g = 10$ m/s².",
    [
        choice("t2-t3-q7a", "Which equation from the list should you use to find the speed of the stone as it hits the water?",
               [r"$v^2 - u^2 = 2 \times a \times x$", r"$a = \dfrac{v - u}{t}$", r"$\text{speed} = \dfrac{\text{distance}}{\text{time}}$", r"$W = m \times g$"], 0,
               "You know u (0, dropped from rest), a (= $g = 10$ m/s², because the only force is gravity) and x (20 m), and you want v. No time is given, so the equation without t is the one. Many candidates left this blank or used speed = distance ÷ time, which only works for constant speed.",
               label="a"),
        numeric("t2-t3-q7b", "Calculate the speed of the stone as it hits the water.", sf(drop_v, 2), "m/s",
                "Write down what you know first: $u = 0$, $a = 10$ m/s², $x = 20$ m. The acceleration of anything in free fall is g.",
                [r"$u = 0$ (dropped from rest), $a = g = 10$ m/s², $x = 20$ m.",
                 r"$v^2 - u^2 = 2 a x$ so $v^2 = 0 + 2 \times 10 \times 20 = 400$.",
                 r"$v = \sqrt{400} = 20$ m/s."], label="b"),
    ],
)

# ---------------------------------------------------------------------
# N10 · the force in F = ma is the resultant force (June 2025 Q2(a)(i):
# candidates used the weight instead of the resultant)
# ---------------------------------------------------------------------

box_m = 4.0
box_pull = 30
box_fric = 6
q_resultant_not_weight = numeric(
    "t2-n10-q7",
    "A 4.0 kg box is pulled along the floor by a horizontal force of 30 N. Friction on the box is 6 N. Calculate the acceleration of the box.",
    (box_pull - box_fric) / box_m, "m/s²",
    "F in $F = ma$ is the resultant force: 30 − 6, not 30, and definitely not the weight (40 N), which is balanced by the floor and does nothing to the horizontal motion.",
    [r"Resultant force $= 30 - 6 = 24$ N (horizontal forces only; the weight and the floor's push cancel).",
     r"$F = m \times a$ so $a = \dfrac{F}{m} = \dfrac{24}{4.0}$.",
     r"$a = 6.0$ m/s². Using the weight (40 N) gives 10 m/s², which is a mark of 0: the box is not falling."],
)

# ---------------------------------------------------------------------
# T12 · how the 6-mark practical question is marked (June 2023 Q9(c)
# levels and indicative content)
# ---------------------------------------------------------------------

explain_levels = explain(
    "How the 6-mark question is marked",
    "<p>Edexcel marks the 6-mark \"describe how you would investigate\" question in <b>levels</b>, not point by point. For the force–mass–acceleration practical the mark scheme separates <i>isolated statements</i> from <i>details of the procedure</i>:</p>"
    "<table class='tbl'><tr><th>Isolated statements (naming things)</th><th>Details of the procedure (saying what is done with them)</th></tr>"
    "<tr><td>weights on hanger; weights added to trolley; light gates / ticker timer; data logger; card on trolley; sloping runway; weigh the trolley; use $a = (v - u) \\div t$; plot a graph of $F$ against $a$</td>"
    "<td>suspend weights from the hanger <i>to produce the force</i>; change the force <i>by changing the weights on the hanger</i>; keep the mass constant <i>by moving weights between hanger and trolley</i>; light gates <i>used to measure velocity / time</i>; runway sloped <i>so the trolley rolls at constant speed with no force (friction compensated)</i>; interrupter card <i>for the time through the gate</i></td></tr></table>"
    "<table class='tbl'><tr><th>Level</th><th>Marks</th><th>Needs</th></tr>"
    "<tr><td>1</td><td>1–2</td><td>at least two isolated statements (\"add weights\", \"use light gates\")</td></tr>"
    "<tr><td>2</td><td>3–4</td><td>one detail of procedure plus one other statement</td></tr>"
    "<tr><td>3</td><td>5–6</td><td><b>two details of procedure</b> plus one other statement, in a clear, logical order</td></tr></table>"
    "<p>So the difference between 2 marks and 6 is <b>saying what each piece of equipment is for</b>. \"Use light gates\" is a statement; \"use light gates to measure the velocity at two points\" is a procedure. The seven steps produce procedure details automatically — steps 3, 4 and 6 are each one.</p>",
)


FACTS = [
    fact("An object falls at constant velocity. What is its acceleration?", "Zero. Constant velocity means no change in velocity, so the resultant force is zero and the acceleration is zero.", "newton-first"),
    fact("What is the acceleration of anything in free fall (ignoring air resistance)?", "$g = 10$ m/s² downwards, whatever its mass. Use it as a in the equations of motion.", "kinematics-route"),
    fact("Which force goes into $F = ma$?", "The resultant force — all the forces on the object added with their directions. Not the weight, unless the object is falling freely.", "f-ma"),
    fact("Convert 15 m/s to km/h.", "$15 \\times 3600 = 54\\,000$ m per hour = 54 km/h. ($m/s \\times 3.6$ = km/h.)", "speed-nn"),
    fact("A ball hits a wall at 5 m/s and bounces back at 4 m/s. What is the change in its velocity?", "9 m/s (from +5 to −4): velocity is a vector, so a change of direction counts. Not 1 m/s.", "force-momentum"),
    fact("Convert 50 ms to seconds.", "0.050 s. ms is milliseconds — divide by 1000 before using $F = \\Delta p \\div t$.", "force-momentum"),
    fact("What is needed for a Newton's-third-law answer about a collision?", "Name both forces (A on B and B on A), say they are equal in size and opposite in direction, and that they are the same type of force acting on different objects.", "third-law-trap"),
    fact("How does a v–t graph continue when a ball thrown upwards starts to fall?", "The same straight line carries on below the time axis: the velocity becomes negative and keeps changing at the same rate. Not a vertical drop.", "graphs-hard"),
    fact("In the 6-mark practical question, what moves an answer from Level 2 to Level 3?", "Two details of procedure — saying what each piece of equipment is used for — plus one other statement, in a logical order.", "planning-practical"),
]

# Where each addition goes: section id → (list of questions to append, extra explain parts)
ADDITIONS = {
    "speed-nn": ([q_ms_to_kmh], []),
    "newton-first": ([q_zero_acc], []),
    "f-ma": ([q_resultant_not_weight], []),
    "kinematics-route": ([q_free_fall], []),
    "measuring-speed": ([q_describe_speed], []),
    "momentum-nn": ([q_momentum_sf], []),
    "stopping-distance-nn": ([q_wet_road, q_reaction_time], []),
    "graphs-hard": ([q_draw_fall], []),
    "third-law-trap": ([q_racket_ball], []),
    "force-momentum": ([q_bounce_group], []),
    "planning-practical": ([], [explain_levels]),
}
