"""
t2_tricky_a.py — The tricky bits, sections T1–T7.

Motion graphs the hard way; curved graphs and tangents; choosing the
kinematics route; resultant force and terminal velocity; Newton's third
law vs balanced forces; circular motion; inertial mass.
"""

from math import exp, sqrt

from t2lib import (
    axis, choice, curve, dashed, ewau, graph, group, label, line, mark,
    marks, numeric, sample, sf, shade, tangent, written,
)

G = 10

ACC_EQ = r"a = \dfrac{v - u}{t}"
V_EQ = r"v = u + a \times t"
T_EQ = r"t = \dfrac{v - u}{a}"
SUVAT_EQ = r"v^2 - u^2 = 2 \times a \times x"
F_EQ = r"F = m \times a"
A_EQ = r"a = \dfrac{F}{m}"
W_EQ = r"W = m \times g"
GRAD_EQ = r"\text{gradient} = \dfrac{\text{change in } y}{\text{change in } x}"
TRAP_EQ = r"\text{area of trapezium} = \tfrac{1}{2}(a + b) \times h"
VT_AREA_EQ = r"\text{distance} = \text{area under velocity–time graph}"
INERTIAL_EQ = r"\text{inertial mass} = \dfrac{F}{a}"


# =====================================================================
# T1 · Motion graphs the hard way (2.7, 2.10)
# =====================================================================

vt_trap = [[0, 10], [10, 20], [20, 20], [30, 0]]
graph_t1_a = graph(
    axis("t / s", 30, 5), axis("v / m/s", 20, 5),
    [line(vt_trap)],
    "Velocity–time graph starting at 10 m/s, rising to 20 m/s at 10 s, constant to 20 s, falling to zero at 30 s.",
    marks_list=[mark(10, 20, "A", drop=True), mark(20, 20, "B", drop=True)],
    shade_list=[shade(0, 0, 10)],
)
t1_w = 0.5 * (10 + 20) * 10
t1_a_total = t1_w + 10 * 20 + 0.5 * 10 * 20

vt_return = [[0, 0], [2, 10], [4, 10], [6, 0], [7, -10], [8, 0]]
graph_t1_b = graph(
    axis("t / s", 8, 1), axis("v / m/s", 10, 5, mn=-10),
    [line(vt_return), dashed([[0, 0], [8, 0]])],
    "Velocity–time graph: rises to 10 m/s at 2 s, constant until 4 s, falls through zero at 6 s to −10 m/s at 7 s, back to zero at 8 s.",
)
t1_b_forward = 0.5 * 2 * 10 + 2 * 10 + 0.5 * 2 * 10
t1_b_back = 0.5 * 2 * 10
t1_b_disp = t1_b_forward - t1_b_back
t1_b_dist = t1_b_forward + t1_b_back

section_t1 = {
    "id": "graphs-hard",
    "band": "tricky",
    "lessons": "2.7, 2.10",
    "title": "Motion graphs the hard way",
    "blurb": "Areas that are not simple triangles, graphs that go below the axis, and turning a shape into a sentence (or a sentence into a shape).",
    "equations": [VT_AREA_EQ, TRAP_EQ],
    "checklist": [
        "Find the area under a sloping section that does not start at zero (trapezium, or rectangle + triangle)",
        "Interpret a negative velocity on a velocity–time graph",
        "Tell displacement from distance when the graph goes below the axis",
        "Describe the motion shown by a graph in words, and sketch a graph from a description",
    ],
    "parts": [
        {
            "kind": "explain",
            "title": "Three things that catch people out",
            "html": (
                "<p><b>1. A sloping section that does not start at zero.</b> The area under it is a trapezium. Either use "
                "$\\tfrac{1}{2}(a + b) \\times h$ with $a$ and $b$ the two parallel sides (the velocities at each end) and $h$ the time, "
                "or split it into a rectangle (the lower velocity × time) plus a triangle on top.</p>"
                "<p><b>2. Velocity below the axis.</b> A negative velocity means the object is moving <b>in the opposite direction</b> — not slowing down. "
                "The line passing through zero is the moment it changes direction. Area <i>below</i> the axis is distance travelled backwards: "
                "add it for total <b>distance</b>, subtract it for <b>displacement</b>.</p>"
                "<p><b>3. Converting between the two graphs.</b></p>"
                "<table class='tbl'><tr><th>Motion</th><th>Distance–time graph</th><th>Velocity–time graph</th></tr>"
                "<tr><td>Stationary</td><td>Horizontal line</td><td>Line along the time axis (v = 0)</td></tr>"
                "<tr><td>Constant velocity</td><td>Straight line, sloping</td><td>Horizontal line above the axis</td></tr>"
                "<tr><td>Constant acceleration from rest</td><td>Curve getting steeper</td><td>Straight line sloping up from the origin</td></tr>"
                "<tr><td>Constant deceleration to rest</td><td>Curve flattening out</td><td>Straight line sloping down to the axis</td></tr>"
                "<tr><td>Returning to the start</td><td>Line sloping back down to zero</td><td>Line below the axis</td></tr></table>"
                "<p>To <b>describe</b> motion from a graph, go section by section: name the motion, give the numbers (how fast, how long, how far), and say when it changes.</p>"
            ),
        },
        {
            "kind": "worked",
            "title": "Area of a trapezium",
            "question": "The graph shows a van's velocity. Calculate the distance travelled in the first 10 s (the shaded region).",
            "graph": graph_t1_a,
            "steps": [
                r"The shaded region is a trapezium: parallel sides 10 m/s (at $t = 0$) and 20 m/s (at $t = 10$ s), width 10 s.",
                r"<b>Method 1:</b> $\text{area} = \tfrac{1}{2}(10 + 20) \times 10 = \tfrac{1}{2} \times 30 \times 10 = 150$ m.",
                r"<b>Method 2:</b> rectangle $10 \times 10 = 100$ m, plus triangle $\tfrac{1}{2} \times 10 \times 10 = 50$ m, total $150$ m.",
                r"Distance in the first 10 s $= 150$ m. (Forgetting the rectangle underneath and answering 50 m is the classic error.)",
            ],
        },
        {
            "kind": "practice",
            "title": "Harder graph reading",
            "questions": [
                group("t2-t1-q1", "Use the van's graph from the worked example.", [
                    numeric("t2-t1-q1a", "Calculate the total distance the van travels in the 30 s.", sf(t1_a_total), "m",
                            "Trapezium + rectangle + triangle.",
                            [r"0–10 s: trapezium $= 150$ m (worked example).",
                             r"10–20 s: rectangle $= 10 \times 20 = 200$ m.",
                             r"20–30 s: triangle $= \tfrac{1}{2} \times 10 \times 20 = 100$ m."]
                            + ewau(VT_AREA_EQ, r"\text{distance} = 150 + 200 + 100", "450", "m"), label="a"),
                    written("t2-t1-q1b", "Describe the motion of the van during the 30 s. Use numbers from the graph.",
                            marks(["0–10 s: the van is already moving at 10 m/s and accelerates uniformly to 20 m/s (acceleration 1 m/s²).",
                                   "10–20 s: constant velocity of 20 m/s (zero acceleration, zero resultant force).",
                                   "20–30 s: decelerates uniformly from 20 m/s to rest (acceleration −2 m/s²), stopping at 30 s."]), lines=4, label="b"),
                ], graph=graph_t1_a),
                group("t2-t1-q2", "The graph shows the velocity of a remote-controlled car along a straight track. Forwards is positive.", [
                    numeric("t2-t1-q2a", "Calculate the distance the car travels forwards in the first 6 s.", sf(t1_b_forward), "m",
                            "Triangle + rectangle + triangle, all above the axis.",
                            [r"Triangle $\tfrac{1}{2} \times 2 \times 10 = 10$ m; rectangle $2 \times 10 = 20$ m; triangle $\tfrac{1}{2} \times 2 \times 10 = 10$ m.",
                             r"Forward distance $= 10 + 20 + 10 = 40$ m."], label="a"),
                    choice("t2-t1-q2b", "What is the car doing between 6 s and 8 s?",
                           ["Slowing down while still moving forwards", "Moving backwards (reversing)", "Stationary", "Speeding up forwards"], 1,
                           "The velocity is negative, so the car is moving in the opposite direction. It reverses, fastest at 7 s, and comes to rest at 8 s.", label="b"),
                    numeric("t2-t1-q2c", "Calculate the car's displacement from its starting point at 8 s.", sf(t1_b_disp), "m",
                            "Area above the axis minus area below it.",
                            [r"Area below the axis (6–8 s): triangle $\tfrac{1}{2} \times 2 \times 10 = 10$ m backwards.",
                             r"Displacement $= 40 - 10 = 30$ m forwards of the start."], label="c"),
                    numeric("t2-t1-q2d", "Calculate the total distance the car travels in the 8 s.", sf(t1_b_dist), "m",
                            "For distance, every bit of area counts, whichever side of the axis.",
                            [r"Total distance $= 40 + 10 = 50$ m."], label="d"),
                ], graph=graph_t1_b),
                choice("t2-t1-q3", "An object's velocity–time graph is a horizontal line above the time axis. What does its distance–time graph look like?",
                       ["A horizontal line", "A straight line sloping upwards", "A curve getting steeper", "A curve flattening out"], 1,
                       "Constant velocity means the distance increases by the same amount every second — a straight sloping line on a distance–time graph."),
                choice("t2-t1-q4", "A distance–time graph is a curve that gets steeper and steeper. What does the velocity–time graph look like?",
                       ["A horizontal line", "A straight line sloping upwards", "A line along the time axis", "A straight line sloping downwards"], 1,
                       "Getting steeper means the speed is increasing. If it increases steadily, the velocity–time graph is a straight line sloping up."),
            ],
        },
    ],
}


# =====================================================================
# T2 · Curved graphs and tangents (2.7, 2.10)
# =====================================================================

# d–t curve for an accelerating object: x = 0.5 t²; tangent at t = 6 has gradient 6
curve_dt_acc = sample(lambda t: 0.5 * t * t, 0, 10, 11)
graph_t2_w = graph(
    axis("t / s", 10, 1), axis("x / m", 50, 10),
    [curve(curve_dt_acc), tangent([[3, 0], [8, 30]])],
    "Distance–time graph curving upwards (accelerating), with a tangent drawn at t = 6 s from (3, 0) to (8, 30).",
    marks_list=[mark(6, 18, "P", drop=True, dx=-18, dy=-4)],
    labels=[label(8.6, 24, "tangent at P", anchor="start")],
)
t2_w = (30 - 0) / (8 - 3)

# d–t curve for a decelerating object: x = 20t − t²; tangent at t = 4 has gradient 12
curve_dt_dec = sample(lambda t: 20 * t - t * t, 0, 10, 11)
graph_t2_1 = graph(
    axis("t / s", 10, 1), axis("x / m", 100, 10),
    [curve(curve_dt_dec), tangent([[2, 40], [7, 100]])],
    "Distance–time graph curving over and flattening out at t = 10 s (decelerating), with a tangent at t = 4 s from (2, 40) to (7, 100).",
    marks_list=[mark(4, 64, "Q", drop=True, dx=-18, dy=-4)],
    labels=[label(2.2, 78, "tangent at Q", anchor="start")],
)
t2_1 = (100 - 40) / (7 - 2)

# v–t curve for a falling object with air resistance: v = 20(1 − e^(−t/5)); initial gradient 4
curve_vt_terminal = sample(lambda t: 20 * (1 - exp(-t / 5)), 0, 20, 21)
graph_t2_2 = graph(
    axis("t / s", 20, 5), axis("v / m/s", 25, 5),
    [curve(curve_vt_terminal), tangent([[0, 0], [5, 20]]), dashed([[0, 20], [20, 20]])],
    "Velocity–time graph rising steeply at first then levelling off towards 20 m/s, with a tangent at the origin from (0, 0) to (5, 20) and a dashed line at 20 m/s.",
    labels=[label(13, 22, "terminal velocity")],
)
t2_2 = (20 - 0) / (5 - 0)

section_t2 = {
    "id": "curved-graphs",
    "band": "tricky",
    "lessons": "2.7, 2.10",
    "title": "Curved graphs and tangents",
    "blurb": "A curve means the gradient is changing. To find the speed (or acceleration) at one instant, draw a tangent and take its gradient.",
    "equations": [r"\text{instantaneous speed} = \text{gradient of tangent to } x\text{–}t \text{ graph}", r"\text{acceleration} = \text{gradient of tangent to } v\text{–}t \text{ graph}"],
    "checklist": [
        "Recognise speeding up and slowing down from the shape of a curved distance–time graph",
        "Find an instantaneous speed from the gradient of a tangent to a distance–time graph",
        "Find an acceleration at an instant from the gradient of a tangent to a velocity–time graph",
        "Describe how the acceleration changes when a velocity–time graph curves",
    ],
    "parts": [
        {
            "kind": "explain",
            "title": "Reading a curve",
            "html": (
                "<p>On a straight line the gradient is the same everywhere. On a <b>curve the gradient changes</b> from point to point, so the speed (on a distance–time graph) "
                "or the acceleration (on a velocity–time graph) is changing.</p>"
                "<table class='tbl'><tr><th>Curve shape</th><th>Distance–time graph</th><th>Velocity–time graph</th></tr>"
                "<tr><td>Getting steeper</td><td>Speeding up</td><td>Acceleration increasing</td></tr>"
                "<tr><td>Flattening out (bending towards horizontal)</td><td>Slowing down</td><td>Acceleration decreasing (velocity still rising, but more slowly)</td></tr>"
                "<tr><td>Horizontal</td><td>Stationary</td><td>Constant velocity, zero acceleration</td></tr></table>"
                "<p><b>To find the value at one instant, draw a tangent</b>: a straight line that just touches the curve at that point, with the same steepness as the curve there. "
                "Then find the gradient of the tangent with a large triangle, reading its ends off gridline intersections.</p>"
                "<p>Pick the triangle's corners from the <b>tangent</b>, not from the curve — the whole point is that the curve's gradient is different everywhere else.</p>"
            ),
        },
        {
            "kind": "explain",
            "tone": "warn",
            "title": "What a tangent is not",
            "html": (
                "<p>The gradient of the line from the origin to a point on the curve is the <b>average</b> speed up to that time, not the speed at that instant. "
                "Only a tangent gives the instantaneous value. On the graph below, the chord from the origin to P would give $18 \\div 6 = 3$ m/s — the average — "
                "while the tangent gives $6$ m/s, the actual speed at $t = 6$ s.</p>"
            ),
        },
        {
            "kind": "worked",
            "title": "Instantaneous speed from a tangent",
            "question": "The graph shows the distance travelled by a sprinter leaving the blocks. The tangent at P (t = 6 s) is drawn. Calculate the sprinter's speed at 6 s.",
            "graph": graph_t2_w,
            "steps": [
                r"The tangent at P passes through $(3,\ 0)$ and $(8,\ 30)$ — read where it crosses gridline intersections.",
                r"Change in distance $= 30 - 0 = 30$ m. Change in time $= 8 - 3 = 5$ s.",
            ] + ewau(GRAD_EQ, r"\text{speed} = \dfrac{30}{5}", "6", "m/s")
            + [r"The curve gets steeper as time goes on, so the sprinter is speeding up: her speed at 6 s (6 m/s) is more than her average so far (3 m/s)."],
        },
        {
            "kind": "practice",
            "title": "Tangents and curves",
            "questions": [
                group("t2-t2-q1", "The graph shows the distance travelled by a car as it slows down for a junction. The tangent at Q (t = 4 s) is drawn.", [
                    choice("t2-t2-q1a", "How can you tell from the shape of the graph that the car is slowing down?",
                           ["The line is going up", "The curve gets flatter (less steep) as time goes on", "The curve gets steeper", "The graph is a curve"], 1,
                           "The gradient of a distance–time graph is the speed. The curve flattens out, so the gradient — and the speed — is decreasing.", label="a"),
                    numeric("t2-t2-q1b", "Use the tangent to calculate the car's speed at Q.", sf(t2_1), "m/s",
                            "The tangent passes through (2, 40) and (7, 100).",
                            [r"Gradient of tangent $= \dfrac{100 - 40}{7 - 2} = \dfrac{60}{5}$."]
                            + ["Speed at Q $= 12$ m/s."], label="b"),
                    choice("t2-t2-q1c", "At what time does the car stop?",
                           ["4 s", "7 s", "10 s", "It never stops"], 2,
                           "The car is stationary when the distance stops changing — where the curve becomes horizontal, at 10 s.", label="c"),
                ], graph=graph_t2_1),
                group("t2-t2-q2", "The graph shows the velocity of a skydiver after jumping from a plane. The tangent at t = 0 is drawn.", [
                    numeric("t2-t2-q2a", "Use the tangent to calculate the skydiver's acceleration at the moment of jumping.", sf(t2_2), "m/s²",
                            "The tangent goes from (0, 0) to (5, 20).",
                            [r"Gradient of tangent $= \dfrac{20 - 0}{5 - 0} = 4$ m/s²."]
                            + ["(With air resistance ignored this would be 10 m/s²; the skydiver's suit and the thin plane air give a smaller value in this example.)"], label="a"),
                    choice("t2-t2-q2b", "How does the skydiver's acceleration change during the 20 s?",
                           ["It stays the same", "It increases", "It decreases, reaching zero", "It becomes negative"], 2,
                           "The curve flattens: the gradient of a velocity–time graph is the acceleration, and it drops towards zero as the velocity approaches 20 m/s.", label="b"),
                    written("t2-t2-q2c", "Explain, in terms of forces, why the graph has this shape.",
                            marks(["At first air resistance is small, so there is a large resultant force (weight − air resistance) downwards and a large acceleration.",
                                   "As the velocity increases, air resistance increases, so the resultant force and the acceleration decrease.",
                                   "Eventually air resistance equals the weight; the resultant force is zero and the velocity is constant: terminal velocity (20 m/s here)."]), lines=4, label="c"),
                ], graph=graph_t2_2),
                written("t2-t2-q3", "Describe how to find the instantaneous speed of an object at a particular time from a curved distance–time graph.",
                        marks(["Draw a tangent to the curve at that time: a straight line that touches the curve there with the same steepness.",
                               "Draw a large triangle on the tangent, using points where it crosses gridlines.",
                               "Speed = gradient of the tangent = change in distance ÷ change in time."]), lines=3),
            ],
        },
    ],
}


# =====================================================================
# T3 · Choosing the kinematics route (2.8, 2.9)
# =====================================================================

t3_w_x = (0 - 24 ** 2) / (2 * -4)
t3_w_t = (0 - 24) / -4
t3_1 = (0 - 18 ** 2) / (2 * 27)
t3_2v = sqrt(2 * 1.2 * 60)
t3_2t = t3_2v / 1.2
t3_4 = (0 - 15 ** 2) / (2 * -G)
t3_6v = 10 + 2 * 8
t3_6x = (t3_6v ** 2 - 10 ** 2) / (2 * 2)

section_t3 = {
    "id": "kinematics-route",
    "band": "tricky",
    "lessons": "2.8, 2.9",
    "title": "Choosing the equation, and the sign of a",
    "blurb": "When a question mixes velocities, accelerations, times and distances: list what you know, pick the equation that fits, and keep the minus signs honest.",
    "equations": [ACC_EQ, SUVAT_EQ],
    "checklist": [
        "List u, v, a, t and x, and pick the equation that contains the three you know and the one you want",
        "Use a negative acceleration for an object slowing down, and v = 0 for an object stopping",
        "Chain two equations: find one quantity, then use it in the next step",
    ],
    "parts": [
        {
            "kind": "explain",
            "title": "List the five, pick the equation",
            "html": (
                "<p>Every motion question involves some of five quantities. Write them down with values before you choose anything:</p>"
                "<table class='tbl'><tr><th>Symbol</th><th>Quantity</th><th>Clues in the question</th></tr>"
                "<tr><td>$u$</td><td>initial velocity</td><td>\"from rest\" → $u = 0$; \"travelling at\"</td></tr>"
                "<tr><td>$v$</td><td>final velocity</td><td>\"stops\" / \"comes to rest\" → $v = 0$; at the top of a throw → $v = 0$</td></tr>"
                "<tr><td>$a$</td><td>acceleration</td><td>\"decelerates at\" → negative; \"falls freely\" → $10$ m/s²</td></tr>"
                "<tr><td>$t$</td><td>time</td><td>seconds, minutes (convert)</td></tr>"
                "<tr><td>$x$</td><td>distance</td><td>\"over a distance of\", \"in 50 m\", height fallen</td></tr></table>"
                "<table class='tbl'><tr><th>You have / want</th><th>Equation</th></tr>"
                "<tr><td>$u, v, a, t$ (no distance)</td><td>$a = \\dfrac{v - u}{t}$</td></tr>"
                "<tr><td>$u, v, a, x$ (no time)</td><td>$v^2 - u^2 = 2ax$</td></tr>"
                "<tr><td>$t$ and $x$ both involved</td><td>Two steps: use one equation to find $v$ or $a$, then the other (or use a velocity–time graph)</td></tr></table>"
                "<p><b>Signs.</b> Choose the direction of motion as positive. Then a deceleration is a <b>negative</b> $a$, and anything pointing the other way is negative. "
                "In $v^2 - u^2 = 2ax$ the squares are always positive, so a stopping object gives a negative top line and a negative $a$ — the distance comes out positive, as it should.</p>"
            ),
        },
        {
            "kind": "worked",
            "title": "A stopping car, two questions",
            "question": "A car travelling at 24 m/s brakes with a deceleration of 4 m/s². Calculate (a) the distance it travels before stopping and (b) the time it takes to stop.",
            "steps": [
                r"List: $u = 24$ m/s, $v = 0$ (stops), $a = -4$ m/s² (decelerating). Wanted: $x$ in (a), $t$ in (b).",
                r"<b>(a)</b> No time → $v^2 - u^2 = 2ax$: $0 - 24^2 = 2 \times (-4) \times x$, so $x = \dfrac{-576}{-8} = 72$ m.",
                r"<b>(b)</b> No distance needed → $a = \dfrac{v - u}{t}$: $t = \dfrac{0 - 24}{-4} = 6$ s.",
                r"Check with the graph picture: a triangle of height 24 m/s and base 6 s has area $\tfrac{1}{2} \times 6 \times 24 = 72$ m. ✓",
            ],
        },
        {
            "kind": "practice",
            "title": "Choosing the route",
            "questions": [
                numeric("t2-t3-q1", "A lorry travelling at 18 m/s brakes and stops in a distance of 27 m. Calculate its acceleration. Include the sign.", sf(t3_1), "m/s²",
                        "You have u, v (= 0) and x, so there is no time: use v² − u² = 2ax.",
                        ewau(SUVAT_EQ, r"0 - 18^2 = 2 \times a \times 27 \quad\Rightarrow\quad a = \dfrac{-324}{54}", "-6", "m/s²")),
                group("t2-t3-q2", "A cyclist starts from rest and accelerates at 1.2 m/s² along 60 m of straight road.", [
                    numeric("t2-t3-q2a", "Calculate her velocity at the end of the 60 m.", sf(t3_2v), "m/s",
                            "No time is given: v² = u² + 2ax with u = 0.",
                            ewau(SUVAT_EQ, r"v^2 = 0 + 2 \times 1.2 \times 60 = 144 \quad\Rightarrow\quad v = \sqrt{144}", "12", "m/s"), label="a"),
                    numeric("t2-t3-q2b", "Calculate how long the 60 m takes.", sf(t3_2t), "s",
                            "Now you know v, use a = (v − u)/t rearranged for t.",
                            ewau(T_EQ, r"t = \dfrac{12 - 0}{1.2}", "10", "s"), label="b"),
                ]),
                choice("t2-t3-q3", "A question gives the initial velocity, the acceleration and the distance, and asks for the final velocity. Which equation should you use?",
                       ["a = (v − u) ÷ t", "v² − u² = 2ax", "speed = distance ÷ time", "F = ma"], 1,
                       "No time is given or wanted, so the equation without t is the one: v² − u² = 2ax."),
                numeric("t2-t3-q4", "A ball is thrown straight up at 15 m/s. Calculate the maximum height it reaches. (g = 10 m/s²; ignore air resistance.)", 11.25, "m",
                        "At the top the ball is momentarily at rest, v = 0. Taking up as positive, a = −10 m/s².",
                        ewau(SUVAT_EQ, r"0 - 15^2 = 2 \times (-10) \times x \quad\Rightarrow\quad x = \dfrac{-225}{-20}", "11.25", "m")
                        + ["Both minus signs matter: get one wrong and the height comes out negative."]),
                written("t2-t3-q5", "A student calculates the acceleration of a braking car and gets −3 m/s². Explain what the minus sign means.",
                        marks(["The acceleration is in the opposite direction to the car's velocity (the direction chosen as positive).",
                               "So the car is slowing down: it is a deceleration of 3 m/s² — its velocity decreases by 3 m/s every second."]), lines=2),
                group("t2-t3-q6", "A car travelling at 10 m/s accelerates at 2 m/s² for 8 s.", [
                    numeric("t2-t3-q6a", "Calculate its final velocity.", sf(t3_6v), "m/s",
                            "You have u, a and t: v = u + at.",
                            ewau(V_EQ, r"v = 10 + 2 \times 8", "26", "m/s"), label="a"),
                    numeric("t2-t3-q6b", "Calculate the distance it travels in the 8 s.", sf(t3_6x), "m",
                            "Now you know u, v and a; use v² − u² = 2ax (or the area under a v–t graph: a trapezium with sides 10 and 26 and width 8).",
                            ewau(SUVAT_EQ, r"26^2 - 10^2 = 2 \times 2 \times x \quad\Rightarrow\quad x = \dfrac{676 - 100}{4}", "144", "m")
                            + [r"Check: trapezium area $\tfrac{1}{2}(10 + 26) \times 8 = 144$ m. ✓"], label="b"),
                ]),
            ],
        },
    ],
}


# =====================================================================
# T4 · Resultant force, acceleration and terminal velocity (2.14, 2.15)
# =====================================================================

t4_w_W = 70 * G
t4_w_R = t4_w_W - 300
t4_w_a = t4_w_R / 70
t4_1 = (4500 - 1500) / 1500
t4_4 = (1500 - 100 * G) / 100
t4_5 = (7200 - 600 * G) / 600

section_t4 = {
    "id": "resultant-acceleration",
    "band": "tricky",
    "lessons": "2.14–2.15",
    "title": "Resultant force → acceleration, and terminal velocity",
    "blurb": "Two forces, one resultant, then F = ma. And the story of a falling object: the acceleration shrinks while the speed keeps growing.",
    "equations": [r"\text{resultant} = F_1 - F_2", A_EQ],
    "checklist": [
        "Find the resultant of two opposing forces, then use it in F = ma (not one of the forces on its own)",
        "Work out the weight first when one of the forces is gravity",
        "Describe and explain the motion of a falling object up to terminal velocity",
        "Say which way the acceleration points at the top of a throw",
    ],
    "parts": [
        {
            "kind": "explain",
            "title": "Resultant first, then F = ma",
            "html": (
                "<p>$F = ma$ only works with the <b>resultant</b> force. If a question gives a driving force and a friction force, or a weight and an air resistance, "
                "subtract to find the resultant <i>before</i> dividing by the mass. The acceleration is in the direction of the resultant.</p>"
                "<p>If one of the forces is gravity and the question gives a mass, you must calculate the weight yourself: $W = m \\times g$ with $g = 10$ N/kg.</p>"
                "<p><b>The falling object (skydiver, raindrop, feather in air):</b></p>"
                "<table class='tbl'><tr><th>Stage</th><th>Forces</th><th>Resultant</th><th>Motion</th></tr>"
                "<tr><td>Just released</td><td>Weight down; air resistance zero (not yet moving)</td><td>= weight, downwards</td><td>Accelerates at 10 m/s²</td></tr>"
                "<tr><td>Speeding up</td><td>Air resistance grows as speed grows, but is still less than weight</td><td>Smaller, still downwards</td><td>Still speeding up, but with a <b>decreasing acceleration</b></td></tr>"
                "<tr><td>Terminal velocity</td><td>Air resistance = weight</td><td>Zero</td><td>Constant velocity (Newton's first law)</td></tr></table>"
                "<p>Students lose the mark by writing \"the object slows down\" in the second stage. It does not: as long as the resultant force points down, the speed is still increasing. "
                "It is the <i>acceleration</i> that gets smaller.</p>"
                "<p><b>At the top of a throw</b> the velocity is zero for an instant, but the acceleration is still $10$ m/s² downwards — gravity has not switched off.</p>"
            ),
        },
        {
            "kind": "worked",
            "title": "A skydiver part-way down",
            "question": "A skydiver has a mass of 70 kg. At one moment the air resistance on him is 300 N. Calculate his acceleration at that moment. (g = 10 N/kg.)",
            "steps": [
                r"Weight first: $W = m \times g = 70 \times 10 = 700$ N, downwards.",
                r"Resultant force $= 700 - 300 = 400$ N, downwards (weight is bigger, so he is still speeding up).",
            ] + ewau(A_EQ, r"a = \dfrac{400}{70}", "5.7", "m/s² downwards")
            + ["Less than 10 m/s² because air resistance is already taking some of the weight; as he speeds up further this acceleration will shrink to zero."],
        },
        {
            "kind": "practice",
            "title": "Resultant force and acceleration",
            "questions": [
                numeric("t2-t4-q1", "A 1500 kg car has a driving force of 4500 N. Friction and air resistance total 1500 N. Calculate the car's acceleration.", sf(t4_1), "m/s²",
                        "Resultant = 4500 − 1500, then divide by the mass.",
                        [r"Resultant $= 4500 - 1500 = 3000$ N."] + ewau(A_EQ, r"a = \dfrac{3000}{1500}", "2", "m/s²")),
                choice("t2-t4-q2", "An 80 kg skydiver experiences 800 N of air resistance. Which statement is correct?",
                       ["She is accelerating downwards at 10 m/s²", "She is slowing down", "She is falling at a constant velocity", "She is moving upwards"], 2,
                       "Her weight is 80 × 10 = 800 N, equal to the air resistance. Resultant force zero → constant velocity. This is terminal velocity."),
                written("t2-t4-q3", "A skydiver jumps from a plane. Describe and explain how her velocity changes from the moment she jumps until she reaches terminal velocity. (Do not consider the parachute.)",
                        marks(["At first only her weight acts (air resistance is zero because she is not yet moving), so the resultant force is large and she accelerates at 10 m/s².",
                               "As her velocity increases, air resistance increases, so the resultant force (weight − air resistance) decreases.",
                               "Her acceleration therefore decreases — but she is still speeding up, because the resultant still acts downwards.",
                               "Eventually air resistance equals her weight. The resultant force is zero, so her velocity stops changing: she falls at a constant (terminal) velocity."]), lines=5),
                numeric("t2-t4-q4", "A model rocket of mass 100 kg produces a thrust of 1.5 kN upwards. Calculate its acceleration at launch. (g = 10 N/kg.)", sf(t4_4), "m/s²",
                        "Thrust up, weight down. Find the weight, then the resultant.",
                        [r"Weight $= 100 \times 10 = 1000$ N. Thrust $= 1500$ N.", r"Resultant $= 1500 - 1000 = 500$ N upwards."]
                        + ewau(A_EQ, r"a = \dfrac{500}{100}", "5", "m/s² upwards")),
                numeric("t2-t4-q5", "A lift of mass 600 kg is pulled upwards by a cable with a tension of 7200 N. Calculate the lift's acceleration.", sf(t4_5), "m/s²",
                        "Weight = 600 × 10 = 6000 N.",
                        [r"Resultant $= 7200 - 6000 = 1200$ N upwards."] + ewau(A_EQ, r"a = \dfrac{1200}{600}", "2", "m/s² upwards")),
                choice("t2-t4-q6", "A ball is thrown straight up. At the very top of its flight, what is its acceleration? (Ignore air resistance.)",
                       ["Zero, because it is momentarily at rest", "10 m/s² downwards", "10 m/s² upwards", "It depends on how hard it was thrown"], 1,
                       "Gravity acts all the time. The velocity is zero for an instant, but the resultant force (the weight) is still there, so the acceleration is still 10 m/s² downwards."),
            ],
        },
    ],
}


# =====================================================================
# T5 · Newton's third law vs balanced forces (2.23)
# =====================================================================

section_t5 = {
    "id": "third-law-trap",
    "band": "tricky",
    "lessons": "2.23",
    "title": "Third-law pairs vs balanced forces",
    "blurb": "Two equal and opposite forces on the same object are balanced forces, not a third-law pair. Sorting the two ideas out is worth several marks a year.",
    "equations": [],
    "checklist": [
        "Explain why the weight of an object and the surface's push on it are not a third-law pair",
        "Identify the two third-law pairs in a book-on-table situation",
        "Use Newton's third law to explain why momentum is conserved in a collision",
    ],
    "parts": [
        {
            "kind": "explain",
            "title": "The book on the table",
            "html": (
                "<p>A book rests on a table. Two forces act <b>on the book</b>: its weight (10 N, down) and the table's upward push (10 N, up). "
                "They are equal and opposite — and they are <b>not</b> a Newton's third law pair. Here is why:</p>"
                "<table class='tbl'><tr><th>Test</th><th>Weight and table's push</th><th>A real third-law pair</th></tr>"
                "<tr><td>Act on different objects?</td><td>No — both act on the book</td><td>Yes — always</td></tr>"
                "<tr><td>Same type of force?</td><td>No — one gravitational, one contact</td><td>Yes — always</td></tr>"
                "<tr><td>Why equal?</td><td>Because the book is in equilibrium (Newton's <b>first</b> law). Put the book in an accelerating lift and they are no longer equal.</td><td>Because of Newton's <b>third</b> law — always equal, whatever is happening</td></tr></table>"
                "<p>The book-on-table situation actually contains <b>two</b> third-law pairs:</p>"
                "<ul><li>The Earth pulls the book down (gravity) ↔ the book pulls the Earth up (gravity).</li>"
                "<li>The table pushes the book up (contact) ↔ the book pushes the table down (contact).</li></ul>"
                "<p><b>Collisions.</b> When object A hits object B, A pushes B and B pushes A with equal and opposite forces, for the same contact time. "
                "Equal and opposite forces for the same time produce equal and opposite <i>changes in momentum</i> — one gains exactly what the other loses. "
                "That is why the total momentum is conserved: Newton's third law is the reason behind the rule you use in the momentum section.</p>"
            ),
        },
        {
            "kind": "worked",
            "title": "Sorting the forces out",
            "question": "A 2 kg bag sits on a shelf. (a) Name the two forces acting on the bag and explain why they are equal. (b) State the third-law partner of each.",
            "steps": [
                r"<b>(a)</b> Weight, $W = 2 \times 10 = 20$ N, acting downwards on the bag (the Earth's gravitational pull). The shelf's contact force, 20 N, acting upwards on the bag.",
                r"They are equal because the bag is at rest, so the resultant force on it must be zero — Newton's <b>first</b> law, not the third.",
                r"<b>(b)</b> Partner of the weight: the bag pulls the Earth upwards with a gravitational force of 20 N (acts on the Earth).",
                r"Partner of the shelf's push: the bag pushes the shelf downwards with a contact force of 20 N (acts on the shelf).",
                r"Each partner is the same type of force, the same size, opposite in direction, and acts on the <i>other</i> object.",
            ],
        },
        {
            "kind": "practice",
            "title": "Pairs and balance",
            "questions": [
                choice("t2-t5-q1", "A cup rests on a desk. Its weight is 3 N and the desk pushes up on it with 3 N. Are these two forces a Newton's third law pair?",
                       ["Yes — they are equal and opposite", "No — they both act on the cup, and they are different types of force",
                        "Yes — they are the same size", "No — third-law pairs are never equal"], 1,
                       "Equal and opposite is not enough. A third-law pair acts on two different objects and is the same type of force. These are balanced forces on one object (Newton's first law)."),
                written("t2-t5-q2", "A student says: \"The weight of a book and the table pushing up on it are a Newton's third law pair because they are equal and opposite.\" Explain why the student is wrong.",
                        marks(["Both forces act on the same object (the book); third-law pair forces act on different objects.",
                               "They are different types of force (gravitational and contact); a third-law pair is always the same type.",
                               "They are equal because the book is in equilibrium (Newton's first law) — if the table were accelerating upwards in a lift, the push would be bigger than the weight, but a third-law pair is always equal."]), lines=4),
                choice("t2-t5-q3", "A cannon fires a cannonball. Which statement is correct?",
                       ["The cannon exerts a bigger force on the ball than the ball exerts on the cannon, because the ball moves faster",
                        "The forces are equal; the ball accelerates more because its mass is much smaller",
                        "Only the ball experiences a force", "The cannon exerts no force because it is heavy"], 1,
                       "Third-law forces are always equal. The ball's acceleration is large because a = F/m with a small m; the cannon's recoil acceleration is small for the same F and a large m."),
                written("t2-t5-q4", "Use Newton's third law to explain why momentum is conserved when two trolleys collide.",
                        marks(["During the collision trolley A exerts a force on trolley B, and B exerts an equal and opposite force on A (Newton's third law).",
                               "The two forces act for the same time (the time they are in contact).",
                               "Force × time is the change in momentum, so A and B receive equal and opposite changes in momentum.",
                               "Whatever momentum one gains, the other loses, so the total momentum is unchanged."]), lines=4),
                choice("t2-t5-q5", "A car accelerates forwards. Its tyres push backwards on the road. Which force makes the car accelerate?",
                       ["The engine pushing the car", "The road pushing forwards on the tyres", "The car's weight", "Air resistance"], 1,
                       "The tyres push the road backwards; by Newton's third law the road pushes the tyres (and so the car) forwards. The engine turns the wheels, but the forward force on the car comes from the road."),
                choice("t2-t5-q6", "A drone hovers at a constant height. Which pair of forces is a Newton's third law pair?",
                       ["The drone's weight and the upward force from the air", "The drone pushing air downwards and the air pushing the drone upwards",
                        "The drone's weight and the drone's thrust", "The air pushing the drone up and the Earth pulling the drone down"], 1,
                       "Drone-on-air and air-on-drone: same type, equal, opposite, on different objects. Weight and the air's lift both act on the drone — they balance, but they are not a pair."),
            ],
        },
    ],
}


# =====================================================================
# T6 · Circular motion (2.20–2.21)
# =====================================================================

section_t6 = {
    "id": "circular-motion",
    "band": "tricky",
    "lessons": "2.20–2.21",
    "title": "Circular motion",
    "blurb": "Constant speed, changing velocity, a resultant force towards the centre — and the word \"centripetal\" is a job description, not a new force.",
    "equations": [],
    "checklist": [
        "Explain why an object moving in a circle at constant speed has a changing velocity",
        "State that a resultant (centripetal) force acts towards the centre of the circle",
        "Say which real force provides the centripetal force in a given situation",
        "Predict what happens when the centripetal force is removed",
    ],
    "parts": [
        {
            "kind": "explain",
            "title": "Constant speed but changing velocity",
            "html": (
                "<p>A satellite orbiting at a steady 7500 m/s, a car going round a roundabout at 10 m/s, a hammer being swung round a thrower's head: each has a "
                "<b>constant speed</b>. But velocity is a vector, and the <b>direction</b> is changing all the time — so the <b>velocity is changing</b>.</p>"
                "<p>A changing velocity is an acceleration. By Newton's first law, an accelerating object must have a <b>resultant force</b> on it. "
                "For circular motion that resultant force acts <b>towards the centre of the circle</b> — at right angles to the velocity, which is why it changes the direction and not the speed. "
                "We call it the <b>centripetal force</b> (\"centre-seeking\").</p>"
                "<p><b>Centripetal force is not an extra force.</b> It is the name for whichever real force happens to be doing the job of pulling the object towards the centre:</p>"
                "<table class='tbl'><tr><th>Situation</th><th>What provides the centripetal force</th></tr>"
                "<tr><td>Satellite or planet in orbit</td><td>Gravity</td></tr>"
                "<tr><td>Car going round a bend or roundabout</td><td>Friction between the tyres and the road</td></tr>"
                "<tr><td>Ball on a string, hammer throw</td><td>Tension in the string / wire</td></tr>"
                "<tr><td>Clothes in a spinning washing machine drum</td><td>The contact (normal) force from the drum</td></tr>"
                "<tr><td>Electron orbiting a nucleus (old model)</td><td>Electrostatic attraction</td></tr></table>"
                "<p><b>Remove the force</b> (the string breaks, the road is icy) and the object no longer accelerates: it carries on in a straight line at a tangent to the circle, at the speed it had — Newton's first law again.</p>"
            ),
        },
        {
            "kind": "worked",
            "title": "A satellite in orbit",
            "question": "A satellite moves in a circular orbit around the Earth at a constant speed. Explain why it is accelerating, and state what provides the force.",
            "steps": [
                r"Velocity is a vector: speed <i>and</i> direction.",
                r"The satellite's speed is constant, but its direction of motion is continually changing as it goes round the circle.",
                r"So its velocity is changing, and a changing velocity means it is accelerating.",
                r"An acceleration needs a resultant force. Here it is the Earth's gravitational pull on the satellite, which acts towards the centre of the Earth — the centre of the orbit.",
                r"Gravity is the centripetal force. It acts at right angles to the velocity, so it changes the direction of motion without changing the speed.",
            ],
        },
        {
            "kind": "practice",
            "title": "Circular motion",
            "questions": [
                written("t2-t6-q1", "A car drives round a roundabout at a steady 8 m/s. Explain why the car's velocity is changing even though its speed is not.",
                        marks(["Velocity is a vector quantity — it has a direction as well as a size.",
                               "The car's direction of motion is continually changing as it goes round the roundabout.",
                               "So its velocity is changing (and it is accelerating) even though its speed stays at 8 m/s."]), lines=3),
                choice("t2-t6-q2", "Which force provides the centripetal force on a car going round a roundabout?",
                       ["The engine's driving force", "Friction between the tyres and the road", "The car's weight", "Air resistance"], 1,
                       "Friction from the road acts sideways on the tyres, towards the centre of the roundabout. On ice there is little friction, which is why cars slide straight on."),
                choice("t2-t6-q3", "In which direction does the resultant force act on an object moving in a circle at constant speed?",
                       ["In the direction of motion", "Opposite to the direction of motion", "Towards the centre of the circle", "Away from the centre of the circle"], 2,
                       "Towards the centre. If it had a component along the motion the speed would change; a force at right angles only changes the direction."),
                choice("t2-t6-q4", "A hammer thrower swings the hammer in a circle on a wire. What provides the centripetal force?",
                       ["Gravity", "The tension in the wire", "Air resistance", "The hammer's momentum"], 1,
                       "The wire pulls the hammer inwards towards the thrower: tension. Momentum is not a force."),
                written("t2-t6-q5", "A ball is whirled round on a string. Describe and explain what happens to the ball if the string snaps.",
                        marks(["The ball moves off in a straight line, along a tangent to the circle (not outwards along the radius).",
                               "It keeps the speed it had at that moment.",
                               "Because the tension — the centripetal force — has gone, there is no resultant force, so by Newton's first law the ball continues at constant velocity."]), lines=3),
                choice("t2-t6-q6", "Which statement about centripetal force is correct?",
                       ["It is an extra force that appears whenever something moves in a circle",
                        "It is the name given to whichever force acts towards the centre, such as gravity or tension",
                        "It acts outwards, which is why you feel pushed to the outside on a roundabout",
                        "It is only present for objects moving at high speed"], 1,
                       "Centripetal is a role, not a new force. The outward feeling on a roundabout is your body trying to go straight on (Newton's first law) while the car turns under you."),
            ],
        },
    ],
}


# =====================================================================
# T7 · Inertial mass (2.22)
# =====================================================================

t7_w = 12 / 3
t7_1 = 50 / 2.5
t7_2 = 20 / 8
t7_5 = 50 / 25

section_t7 = {
    "id": "inertial-mass",
    "band": "tricky",
    "lessons": "2.22",
    "title": "Inertial mass",
    "blurb": "Mass as a measure of how hard it is to change an object's velocity — defined as force ÷ acceleration — and why it is not the same idea as weight.",
    "equations": [INERTIAL_EQ],
    "checklist": [
        "Explain what inertial mass measures",
        "State that inertial mass is defined as the ratio of force to acceleration",
        "Explain why inertial mass does not change on the Moon even though weight does",
    ],
    "parts": [
        {
            "kind": "explain",
            "title": "Mass as resistance to changing velocity",
            "html": (
                "<p><b>Inertia</b> is the tendency of an object to keep doing what it is doing — to stay at rest, or to keep moving at constant velocity (Newton's first law).</p>"
                "<p><b>Inertial mass</b> is a measure of <b>how difficult it is to change the velocity</b> of an object — to get it moving from rest, to speed it up, slow it down, or change its direction. "
                "It is <b>defined as the ratio of force to acceleration</b>:</p>"
                "$$" + INERTIAL_EQ + "$$"
                "<p>So if the same force gives one object half the acceleration of another, the first object has twice the inertial mass. This is just $F = ma$ rearranged, "
                "but the exam wants the <i>idea</i>: mass is what makes velocity hard to change.</p>"
                "<table class='tbl'><tr><th></th><th>Inertial mass</th><th>Weight</th></tr>"
                "<tr><td>Measures</td><td>Resistance to acceleration</td><td>The pull of gravity</td></tr>"
                "<tr><td>Found from</td><td>$F \\div a$</td><td>$m \\times g$</td></tr>"
                "<tr><td>On the Moon</td><td>Unchanged — a 1000 kg buggy is just as hard to push into motion</td><td>About one sixth</td></tr>"
                "<tr><td>In deep space (no gravity)</td><td>Unchanged</td><td>Zero</td></tr></table>"
                "<p>An astronaut floating in orbit is \"weightless\", but a loaded cargo pallet is still hard to push: its inertial mass is the same as on Earth.</p>"
            ),
        },
        {
            "kind": "worked",
            "title": "Comparing inertial masses",
            "question": "A resultant force of 12 N gives trolley A an acceleration of 3 m/s². The same force gives trolley B an acceleration of 1.5 m/s². Calculate the inertial mass of each trolley and say which is harder to get moving.",
            "steps": [
                r"Trolley A: $m = \dfrac{F}{a} = \dfrac{12}{3} = 4$ kg.",
                r"Trolley B: $m = \dfrac{12}{1.5} = 8$ kg.",
                r"Trolley B has twice the inertial mass: for the same force it accelerates half as much, so it is harder to change its velocity.",
            ],
        },
        {
            "kind": "practice",
            "title": "Inertial mass",
            "questions": [
                numeric("t2-t7-q1", "A resultant force of 50 N gives a crate an acceleration of 2.5 m/s². Calculate the inertial mass of the crate.", sf(t7_1), "kg",
                        "Force divided by acceleration.",
                        ewau(INERTIAL_EQ, r"m = \dfrac{50}{2.5}", "20", "kg")),
                numeric("t2-t7-q2", "A 20 N push gives a loaded trolley an acceleration of 8 m/s². Calculate its inertial mass.", sf(t7_2), "kg",
                        "m = F ÷ a.",
                        ewau(INERTIAL_EQ, r"m = \dfrac{20}{8}", "2.5", "kg")),
                written("t2-t7-q3", "Explain what is meant by the inertial mass of an object.",
                        marks(["A measure of how difficult it is to change the velocity of the object (including starting it from rest).",
                               "It is defined as the ratio of the force applied to the acceleration produced: m = F ÷ a."]), lines=2),
                choice("t2-t7-q4", "The same resultant force is applied to a tennis ball and to a bowling ball. Which statement is correct?",
                       ["They have the same acceleration", "The bowling ball accelerates less because it has more inertial mass",
                        "The bowling ball accelerates more because it is heavier", "The tennis ball accelerates less because it is lighter"], 1,
                       "a = F ÷ m: with the same F, the larger mass gets the smaller acceleration. The bowling ball's velocity is harder to change."),
                numeric("t2-t7-q5", "On Earth a shopping trolley needs a resultant force of 50 N to accelerate at 2 m/s². On the Moon, what resultant force would give the same trolley the same acceleration?", 50, "N",
                        "Inertial mass does not depend on gravity.",
                        [r"Inertial mass $= \dfrac{50}{2} = 25$ kg — the same on the Moon.", r"$F = m \times a = 25 \times 2 = 50$ N, exactly as on Earth.",
                         "Its weight on the Moon is smaller (about 40 N instead of 250 N), but its resistance to acceleration is unchanged."]),
                choice("t2-t7-q6", "An astronaut in orbit is \"weightless\". Which statement about a 500 kg satellite she is trying to push is correct?",
                       ["It is easy to push because it has no weight", "It is just as hard to accelerate as on Earth because its inertial mass is unchanged",
                        "It cannot be moved at all", "It has no mass in orbit"], 1,
                       "Weight depends on gravity; inertial mass does not. Changing the satellite's velocity needs the same force in orbit as it would on Earth."),
            ],
        },
    ],
}


SECTIONS = [section_t1, section_t2, section_t3, section_t4, section_t5, section_t6, section_t7]
