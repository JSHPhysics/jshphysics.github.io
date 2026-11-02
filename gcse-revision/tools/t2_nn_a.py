"""
t2_nn_a.py — The non-negotiables, sections N1–N8.

Scalars and vectors; speed; acceleration; v² − u² = 2ax; distance–time
graphs; velocity–time graphs; typical speeds and g; measuring speed.
"""

from math import sqrt

from t2lib import (
    axis, choice, curve, dashed, ewau, graph, group, line, mark, marks,
    numeric, sf, shade, written,
)

# ---------------------------------------------------------------------
# Equations used across these sections
# ---------------------------------------------------------------------

SPEED_EQ = r"\text{speed} = \dfrac{\text{distance}}{\text{time}}"
SPEED_SYM = r"v = \dfrac{x}{t}"
DIST_EQ = r"\text{distance} = \text{speed} \times \text{time}"
TIME_EQ = r"\text{time} = \dfrac{\text{distance}}{\text{speed}}"
AVG_EQ = r"\text{average speed} = \dfrac{\text{total distance}}{\text{total time}}"
ACC_EQ = r"a = \dfrac{v - u}{t}"
ACC_WORDS = r"\text{acceleration} = \dfrac{\text{change in velocity}}{\text{time taken}}"
V_EQ = r"v = u + a \times t"
T_EQ = r"t = \dfrac{v - u}{a}"
SUVAT_EQ = r"v^2 - u^2 = 2 \times a \times x"
GRAD_EQ = r"\text{gradient} = \dfrac{\text{change in } y}{\text{change in } x}"
DT_EQ = r"\text{speed} = \text{gradient of distance–time graph}"
VT_GRAD_EQ = r"\text{acceleration} = \text{gradient of velocity–time graph}"
VT_AREA_EQ = r"\text{distance} = \text{area under velocity–time graph}"
TRI_EQ = r"\text{area of triangle} = \tfrac{1}{2} \times \text{base} \times \text{height}"
LIGHT_EQ = r"\text{speed} = \dfrac{\text{length of card}}{\text{time to pass through gate}}"

G = 10  # N/kg, the Edexcel GCSE value


# =====================================================================
# N1 · Scalars and vectors (2.1–2.5)
# =====================================================================

section_n1 = {
    "id": "scalars-vectors",
    "band": "nn",
    "lessons": "2.1–2.5",
    "title": "Scalars and vectors",
    "blurb": "Every quantity in this topic is either a scalar or a vector. You must be able to say which is which, and why.",
    "equations": [],
    "checklist": [
        "Define a scalar and a vector",
        "Sort the spec's list of quantities into scalars and vectors",
        "Explain that velocity is speed in a stated direction",
        "Tell the difference between distance and displacement",
    ],
    "parts": [
        {
            "kind": "explain",
            "title": "What makes a quantity a vector?",
            "html": (
                "<p>A <b>scalar</b> quantity has <b>magnitude (size) only</b>. "
                "A <b>vector</b> quantity has <b>magnitude <i>and</i> a specific direction</b>.</p>"
                "<p>The exam expects you to know this list. The pairs are the ones that catch people out:</p>"
                "<table class='tbl'><tr><th>Scalar (size only)</th><th>Vector (size and direction)</th></tr>"
                "<tr><td>distance</td><td>displacement</td></tr>"
                "<tr><td>speed</td><td>velocity</td></tr>"
                "<tr><td>mass</td><td>weight</td></tr>"
                "<tr><td>energy</td><td>force</td></tr>"
                "<tr><td>time, temperature</td><td>acceleration, momentum</td></tr></table>"
                "<p><b>Velocity is speed in a stated direction.</b> \"20 m/s\" is a speed; \"20 m/s due north\" is a velocity. "
                "Two cars doing 20 m/s in opposite directions have the <i>same speed</i> but <i>different velocities</i>.</p>"
                "<p><b>Displacement</b> is the straight-line distance from start to finish, in a stated direction. "
                "Walk once round a running track and your distance is 400 m but your displacement is zero — you are back where you started.</p>"
            ),
        },
        {
            "kind": "worked",
            "title": "Distance, displacement, speed and velocity",
            "question": "A ball is thrown and lands 12 m away from the thrower. Along its curved path it travels 15 m, taking 1.5 s. State the distance, the displacement, the average speed and the size of the average velocity.",
            "steps": [
                r"<b>Distance</b> is the length of the path actually travelled: 15 m.",
                r"<b>Displacement</b> is the straight line from start to finish: 12 m, in the direction of the throw.",
                r"<b>Average speed</b> uses the distance: $\text{speed} = \dfrac{15}{1.5} = 10$ m/s.",
                r"<b>Average velocity</b> uses the displacement: $\text{velocity} = \dfrac{12}{1.5} = 8$ m/s in the direction of the throw.",
                r"Speed and velocity are different here because the path was not a straight line.",
            ],
        },
        {
            "kind": "practice",
            "title": "Scalars and vectors",
            "questions": [
                choice("t2-n1-q1", "Which of these is a <b>vector</b> quantity?", ["Speed", "Distance", "Velocity", "Energy"], 2,
                       "Velocity has a direction (it is speed in a stated direction). Speed, distance and energy have size only."),
                choice("t2-n1-q2", "Which of these is a <b>scalar</b> quantity?", ["Force", "Weight", "Momentum", "Mass"], 3,
                       "Mass has no direction — 5 kg is 5 kg whichever way you turn it. Force, weight and momentum all act in a direction."),
                choice("t2-n1-q3", "A car travels at 20 m/s due north. Which statement is correct?",
                       ["20 m/s is its velocity and 20 m/s due north is its speed",
                        "20 m/s is its speed and 20 m/s due north is its velocity",
                        "Both are vectors",
                        "Both are scalars"], 1,
                       "Velocity is speed in a stated direction, so adding \"due north\" turns the speed into a velocity."),
                group("t2-n1-q4", "A student walks 30 m east along a corridor, then turns round and walks 10 m west.", [
                    numeric("t2-n1-q4a", "What distance has the student walked?", 40, "m",
                            "Distance is the total path length — add the two legs.",
                            [r"Distance $= 30 + 10 = 40$ m. Direction does not matter for a scalar."], label="a"),
                    numeric("t2-n1-q4b", "What is the student's displacement from the start? (Give the size; the direction is east.)", 20, "m",
                            "Displacement is the straight line from start to finish. Walking back cancels some of it.",
                            [r"Take east as positive: $+30 + (-10) = +20$ m.", "Displacement $= 20$ m east."], label="b"),
                ]),
                group("t2-n1-q5", "A runner completes one lap of a 400 m track in 50 s.", [
                    numeric("t2-n1-q5a", "Calculate the runner's average speed.", 8, "m/s",
                            "Average speed uses the distance run.",
                            ewau(SPEED_EQ, r"\text{speed} = \dfrac{400}{50}", "8", "m/s"), label="a"),
                    numeric("t2-n1-q5b", "State the runner's average velocity for the lap.", 0, "m/s",
                            "Where does the runner finish compared with where they started?",
                            ["After one complete lap the runner is back at the start, so the displacement is 0 m.",
                             r"Average velocity $= \dfrac{0}{50} = 0$ m/s."], label="b"),
                ]),
                written("t2-n1-q6", "Explain the difference between distance and displacement.",
                        marks(["Distance is the total length of the path travelled; it is a scalar.",
                               "Displacement is the straight-line distance from the start point to the finish point, in a stated direction; it is a vector.",
                               "A journey that returns to its start has a large distance but zero displacement."]), lines=3),
            ],
        },
    ],
}


# =====================================================================
# N2 · Speed, distance and time (2.6)
# =====================================================================

q2_3 = 2400 / 240
q2_4 = 1700 / 340
q2_5 = 108000 / 3600
q2_6 = (600 + 300) / (60 + 30 + 60)

section_n2 = {
    "id": "speed",
    "band": "nn",
    "lessons": "2.6",
    "title": "Speed, distance and time",
    "blurb": "The speed equation, its two rearrangements, and the unit conversions that come with it (minutes, kilometres, km/h).",
    "equations": [SPEED_SYM, AVG_EQ],
    "checklist": [
        "Use speed = distance ÷ time and rearrange it for distance or time",
        "Convert minutes to seconds and kilometres to metres before calculating",
        "Convert km/h to m/s",
        "Find an average speed over a whole journey, including stops",
    ],
    "parts": [
        {
            "kind": "explain",
            "title": "The equation and its rearrangements",
            "html": (
                "$$" + SPEED_EQ + r"\qquad v = \dfrac{x}{t}$$"
                "<p>Edexcel writes distance as $x$. Learn all three forms:</p>"
                "<table class='tbl'><tr><th>To find…</th><th>Use…</th></tr>"
                "<tr><td>speed</td><td>$" + SPEED_EQ + "$</td></tr>"
                "<tr><td>distance</td><td>$" + DIST_EQ + "$</td></tr>"
                "<tr><td>time</td><td>$" + TIME_EQ + "$</td></tr></table>"
                "<p><b>Units must match.</b> In physics, work in metres and seconds so the speed comes out in m/s. "
                "Convert <i>before</i> you substitute: 1 minute = 60 s, 1 hour = 3600 s, 1 km = 1000 m.</p>"
                "<p><b>km/h → m/s:</b> multiply by 1000 (km → m) and divide by 3600 (h → s). That is the same as dividing by 3.6. "
                "So 36 km/h = 10 m/s, and 72 km/h = 20 m/s.</p>"
                "<p><b>Average speed</b> over a journey is total distance ÷ total time — and the total time includes any time spent stopped.</p>"
            ),
        },
        {
            "kind": "worked",
            "title": "Converting km/h to m/s",
            "question": "A train travels at 90 km/h. Calculate its speed in m/s.",
            "steps": [
                r"Convert the distance: $90 \text{ km} = 90 \times 1000 = 90\,000$ m.",
                r"Convert the time: $1 \text{ h} = 60 \times 60 = 3600$ s.",
            ] + ewau(SPEED_EQ, r"\text{speed} = \dfrac{90\,000}{3600}", "25", "m/s")
            + [r"Check: $90 \div 3.6 = 25$. ✓"],
        },
        {
            "kind": "practice",
            "title": "Speed, distance and time",
            "intro": "Lay out every calculation in EWAU. Convert units first where you need to.",
            "questions": [
                numeric("t2-n2-q1", "A sprinter runs 150 m in 12 s. Calculate her average speed.", 12.5, "m/s",
                        "Distance divided by time.",
                        ewau(SPEED_EQ, r"\text{speed} = \dfrac{150}{12}", "12.5", "m/s")),
                numeric("t2-n2-q2", "A cyclist rides at 8 m/s for 45 s. How far does he travel?", 360, "m",
                        "You want a distance, so multiply speed by time.",
                        ewau(DIST_EQ, r"\text{distance} = 8 \times 45", "360", "m")),
                numeric("t2-n2-q3", "A bus travels 2.4 km in 4 minutes. Calculate its average speed in m/s.", sf(q2_3), "m/s",
                        "Convert 2.4 km to metres and 4 minutes to seconds first.",
                        [r"$2.4 \text{ km} = 2400$ m and $4 \text{ min} = 4 \times 60 = 240$ s."]
                        + ewau(SPEED_EQ, r"\text{speed} = \dfrac{2400}{240}", "10", "m/s")),
                numeric("t2-n2-q4", "Sound travels through air at 340 m/s. How long does thunder take to reach you from a lightning strike 1.7 km away?", sf(q2_4), "s",
                        "Convert 1.7 km to metres, then divide the distance by the speed.",
                        [r"$1.7 \text{ km} = 1700$ m."]
                        + ewau(TIME_EQ, r"\text{time} = \dfrac{1700}{340}", "5", "s")),
                numeric("t2-n2-q5", "A car travels at 108 km/h on a motorway. Calculate its speed in m/s.", sf(q2_5), "m/s",
                        "108 km is 108 000 m, and 1 hour is 3600 s.",
                        ewau(SPEED_EQ, r"\text{speed} = \dfrac{108\,000}{3600}", "30", "m/s")
                        + [r"Or: $108 \div 3.6 = 30$ m/s."]),
                numeric("t2-n2-q6", "A delivery rider covers 600 m in 60 s, waits 30 s at a crossing, then covers another 300 m in 60 s. Calculate the average speed for the whole journey.", sf(q2_6), "m/s",
                        "Total distance over total time — and the 30 s wait counts in the total time.",
                        [r"Total distance $= 600 + 300 = 900$ m. Total time $= 60 + 30 + 60 = 150$ s."]
                        + ewau(AVG_EQ, r"\text{average speed} = \dfrac{900}{150}", "6", "m/s")),
            ],
        },
    ],
}


# =====================================================================
# N3 · Acceleration (2.8)
# =====================================================================

q3_w = (20 - 5) / 6
q3_1 = (12 - 0) / 4
q3_2 = (10 - 30) / 5
q3_3 = 4 + 2 * 5
q3_4 = (25 - 10) / 1.5
q3_5 = 24 + (-6) * 3
q3_6 = (1.2 - 0) / 0.8

section_n3 = {
    "id": "acceleration",
    "band": "nn",
    "lessons": "2.8",
    "title": "Acceleration",
    "blurb": "Acceleration is how quickly velocity changes. The sign matters: slowing down is a negative acceleration.",
    "equations": [ACC_EQ],
    "checklist": [
        "Use a = (v − u) ÷ t, with u the initial and v the final velocity",
        "Give a deceleration as a negative acceleration",
        "Rearrange to find a final velocity or a time",
    ],
    "parts": [
        {
            "kind": "explain",
            "title": "Change in velocity ÷ time",
            "html": (
                "$$" + ACC_WORDS + r"\qquad a = \dfrac{v - u}{t}$$"
                "<p>Here $u$ is the <b>initial</b> velocity (\"<i>u</i> comes before <i>v</i> in the alphabet\") and $v$ is the <b>final</b> velocity. "
                "The unit of acceleration is <b>m/s²</b>: metres per second, <i>every second</i>.</p>"
                "<p>An acceleration of 3 m/s² means the velocity increases by 3 m/s each second: 0, 3, 6, 9, 12 …</p>"
                "<p><b>Slowing down</b> gives a <b>negative</b> answer, because $v$ is smaller than $u$. That is called a <b>deceleration</b>. "
                "If a question says \"include the sign\" or \"calculate the acceleration\" of something slowing down, write the minus sign.</p>"
                "<table class='tbl'><tr><th>To find…</th><th>Use…</th></tr>"
                "<tr><td>acceleration</td><td>$" + ACC_EQ + "$</td></tr>"
                "<tr><td>final velocity</td><td>$" + V_EQ + "$</td></tr>"
                "<tr><td>time</td><td>$" + T_EQ + "$</td></tr></table>"
            ),
        },
        {
            "kind": "worked",
            "title": "Calculating an acceleration",
            "question": "A car speeds up from 5 m/s to 20 m/s in 6 s. Calculate its acceleration.",
            "steps": [r"$u = 5$ m/s, $v = 20$ m/s, $t = 6$ s."]
            + ewau(ACC_EQ, r"a = \dfrac{20 - 5}{6} = \dfrac{15}{6}", "2.5", "m/s²"),
        },
        {
            "kind": "practice",
            "title": "Acceleration",
            "questions": [
                numeric("t2-n3-q1", "A motorbike accelerates from rest to 12 m/s in 4 s. Calculate its acceleration.", sf(q3_1), "m/s²",
                        "\"From rest\" means u = 0.",
                        ewau(ACC_EQ, r"a = \dfrac{12 - 0}{4}", "3", "m/s²")),
                numeric("t2-n3-q2", "A lorry slows from 30 m/s to 10 m/s in 5 s. Calculate its acceleration. Include the sign.", sf(q3_2), "m/s²",
                        "v is smaller than u, so the top of the fraction is negative.",
                        ewau(ACC_EQ, r"a = \dfrac{10 - 30}{5} = \dfrac{-20}{5}", "-4", "m/s²")
                        + ["A deceleration of 4 m/s²."]),
                numeric("t2-n3-q3", "A boat moving at 4 m/s accelerates at 2 m/s² for 5 s. Calculate its final velocity.", sf(q3_3), "m/s",
                        "Rearrange for v: the velocity gained is a × t, added on to u.",
                        ewau(V_EQ, r"v = 4 + 2 \times 5", "14", "m/s")),
                numeric("t2-n3-q4", "A train accelerates at 1.5 m/s² from 10 m/s to 25 m/s. How long does this take?", sf(q3_4), "s",
                        "Find the change in velocity first, then divide by the acceleration.",
                        ewau(T_EQ, r"t = \dfrac{25 - 10}{1.5} = \dfrac{15}{1.5}", "10", "s")),
                numeric("t2-n3-q5", "A car travelling at 24 m/s decelerates at 6 m/s² for 3 s. Calculate its velocity at the end of the 3 s.", sf(q3_5), "m/s",
                        "A deceleration of 6 m/s² is an acceleration of −6 m/s².",
                        ewau(V_EQ, r"v = 24 + (-6) \times 3 = 24 - 18", "6", "m/s")),
                numeric("t2-n3-q6", "A trolley released from rest on a ramp reaches 1.2 m/s after 0.8 s. Calculate its acceleration.", sf(q3_6), "m/s²",
                        "u = 0 because it starts from rest.",
                        ewau(ACC_EQ, r"a = \dfrac{1.2 - 0}{0.8}", "1.5", "m/s²")),
            ],
        },
    ],
}


# =====================================================================
# N4 · v² − u² = 2ax (2.9)
# =====================================================================

q4_w = sqrt(0 ** 2 + 2 * 3 * 24)
q4_1 = sqrt(0 ** 2 + 2 * 2 * 16)
q4_2 = sqrt(5 ** 2 + 2 * 1.5 * 20)
q4_3 = (0 ** 2 - 20 ** 2) / (2 * 50)
q4_4 = (0 ** 2 - 30 ** 2) / (2 * -6)
q4_5 = sqrt(0 ** 2 + 2 * G * 20)
q4_6 = sqrt(25 ** 2 - 2 * 2 * 100)

section_n4 = {
    "id": "suvat",
    "band": "nn",
    "lessons": "2.9",
    "title": "v² − u² = 2ax",
    "blurb": "The equation for when you know a distance but not a time. Substitute, then rearrange — and remember the square root at the end.",
    "equations": [SUVAT_EQ],
    "checklist": [
        "Recognise when to use v² − u² = 2ax (no time given, or no time wanted)",
        "Substitute into it and solve for v, u, a or x",
        "Remember to square-root when the unknown is a velocity",
    ],
    "parts": [
        {
            "kind": "explain",
            "title": "When there is no time in the question",
            "html": (
                "$$" + SUVAT_EQ + "$$"
                "<p>$u$ = initial velocity, $v$ = final velocity, $a$ = acceleration, $x$ = distance travelled. "
                "<b>There is no $t$</b> in this equation, so use it whenever the question gives you (or asks for) a distance and says nothing about time.</p>"
                "<p>Safest method: <b>substitute the numbers first, then rearrange</b>. Square the velocities before you do anything else.</p>"
                "<table class='tbl'><tr><th>Finding…</th><th>Do this</th></tr>"
                "<tr><td>$v$</td><td>$v^2 = u^2 + 2ax$, then <b>square-root</b></td></tr>"
                "<tr><td>$a$</td><td>$a = \\dfrac{v^2 - u^2}{2x}$</td></tr>"
                "<tr><td>$x$</td><td>$x = \\dfrac{v^2 - u^2}{2a}$</td></tr></table>"
                "<p>For an object <b>falling freely</b>, $a = g = 10$ m/s². For something <b>stopping</b>, $v = 0$ and $a$ is negative.</p>"
            ),
        },
        {
            "kind": "worked",
            "title": "Finding a final velocity",
            "question": "A cyclist starts from rest and accelerates at 3 m/s² over a distance of 24 m. Calculate her final velocity.",
            "steps": [r"$u = 0$, $a = 3$ m/s², $x = 24$ m. No time is mentioned, so use $v^2 - u^2 = 2ax$."]
            + ewau(SUVAT_EQ, r"v^2 - 0^2 = 2 \times 3 \times 24 = 144 \quad\Rightarrow\quad v = \sqrt{144}", "12", "m/s"),
        },
        {
            "kind": "practice",
            "title": "Using v² − u² = 2ax",
            "questions": [
                numeric("t2-n4-q1", "A car starts from rest and accelerates at 2 m/s² for 16 m. Calculate its final velocity.", sf(q4_1), "m/s",
                        "u = 0. Work out v² first, then square-root.",
                        ewau(SUVAT_EQ, r"v^2 = 0 + 2 \times 2 \times 16 = 64 \quad\Rightarrow\quad v = \sqrt{64}", "8", "m/s")),
                numeric("t2-n4-q2", "A runner moving at 5 m/s accelerates at 1.5 m/s² for 20 m. Calculate her final velocity.", sf(q4_2), "m/s",
                        "Square u (5² = 25) before adding 2ax.",
                        ewau(SUVAT_EQ, r"v^2 = 5^2 + 2 \times 1.5 \times 20 = 25 + 60 = 85 \quad\Rightarrow\quad v = \sqrt{85}", "9.2", "m/s")),
                numeric("t2-n4-q3", "A car travelling at 20 m/s brakes and stops in 50 m. Calculate its acceleration. Include the sign.", sf(q4_3), "m/s²",
                        "Stopping means v = 0. The answer is negative.",
                        ewau(SUVAT_EQ, r"0^2 - 20^2 = 2 \times a \times 50 \quad\Rightarrow\quad a = \dfrac{-400}{100}", "-4", "m/s²")),
                numeric("t2-n4-q4", "A lorry travelling at 30 m/s decelerates at 6 m/s² until it stops. Calculate the distance it travels while stopping.", sf(q4_4), "m",
                        "v = 0 and a = −6 m/s². Two negatives on the fraction give a positive distance.",
                        ewau(SUVAT_EQ, r"0^2 - 30^2 = 2 \times (-6) \times x \quad\Rightarrow\quad x = \dfrac{-900}{-12}", "75", "m")),
                numeric("t2-n4-q5", "A stone is dropped from a bridge 20 m above a river. Calculate its speed as it hits the water. (Ignore air resistance; g = 10 m/s².)", sf(q4_5), "m/s",
                        "Dropped means u = 0, and the acceleration is g = 10 m/s².",
                        ewau(SUVAT_EQ, r"v^2 = 0 + 2 \times 10 \times 20 = 400 \quad\Rightarrow\quad v = \sqrt{400}", "20", "m/s")),
                numeric("t2-n4-q6", "A car accelerates at 2 m/s² over 100 m and reaches 25 m/s. Calculate its initial velocity.", sf(q4_6), "m/s",
                        "This time v is known and u is the unknown: u² = v² − 2ax.",
                        ewau(SUVAT_EQ, r"25^2 - u^2 = 2 \times 2 \times 100 \quad\Rightarrow\quad u^2 = 625 - 400 = 225 \quad\Rightarrow\quad u = \sqrt{225}", "15", "m/s")),
            ],
        },
    ],
}


# =====================================================================
# N5 · Distance–time graphs (2.7)
# =====================================================================

dt_points = [[0, 0], [20, 200], [40, 200], [60, 300]]
graph_dt_1 = graph(
    axis("t / s", 60, 10), axis("x / m", 300, 50),
    [line(dt_points)],
    "Distance–time graph: rises to 200 m at 20 s, flat until 40 s, then rises to 300 m at 60 s.",
    marks_list=[mark(20, 200, "A", drop=True), mark(40, 200, "B"), mark(60, 300, "C", drop=True)],
)

dt_cyclist = [[0, 0], [30, 150], [50, 150], [70, 0]]
graph_dt_2 = graph(
    axis("t / s", 80, 10), axis("x / m", 200, 50),
    [line(dt_cyclist)],
    "Distance-from-start against time for a cyclist: rises to 150 m at 30 s, flat until 50 s, then falls back to 0 at 70 s.",
)

q5_w = (200 - 0) / (20 - 0)
q5_1a = (300 - 200) / (60 - 40)
q5_1d = 300 / 60
q5_2a = (150 - 0) / (30 - 0)
q5_2c = (150 - 0) / (70 - 50)

section_n5 = {
    "id": "dt-graphs",
    "band": "nn",
    "lessons": "2.7",
    "title": "Distance–time graphs",
    "blurb": "The gradient of a distance–time graph is the speed. Flat means stationary; steeper means faster.",
    "equations": [DT_EQ, GRAD_EQ],
    "checklist": [
        "Read the speed from the gradient of a straight section",
        "Recognise a stationary section (horizontal line)",
        "Compare speeds from steepness",
        "Find an average speed for a whole journey from the graph",
    ],
    "parts": [
        {
            "kind": "explain",
            "title": "Gradient means speed",
            "html": (
                "<p>On a distance–time graph, <b>gradient = speed</b>. Draw a big triangle on the straight section, then:</p>"
                "$$\\text{speed} = \\dfrac{\\text{change in distance}}{\\text{change in time}}$$"
                "<table class='tbl'><tr><th>Shape of line</th><th>Motion</th></tr>"
                "<tr><td>Straight, sloping up</td><td>Constant speed</td></tr>"
                "<tr><td>Horizontal (flat)</td><td>Stationary — distance is not changing</td></tr>"
                "<tr><td>Steeper straight line</td><td>Faster constant speed</td></tr>"
                "<tr><td>Straight, sloping down</td><td>Constant speed back towards the start (if the axis is distance <i>from the start</i>)</td></tr>"
                "<tr><td>Curved</td><td>Changing speed — see the tricky bits</td></tr></table>"
                "<p>Use the <b>whole</b> straight section for your triangle: bigger triangles give more accurate gradients.</p>"
            ),
        },
        {
            "kind": "worked",
            "title": "Speed from a gradient",
            "question": "The graph shows a walker's journey. Calculate the walker's speed between 0 and 20 s.",
            "graph": graph_dt_1,
            "steps": [
                r"Between $t = 0$ and $t = 20$ s the line is straight, so the speed is constant. Draw a triangle from the origin to point A.",
                r"Change in distance $= 200 - 0 = 200$ m. Change in time $= 20 - 0 = 20$ s.",
            ] + ewau(GRAD_EQ, r"\text{speed} = \dfrac{200}{20}", "10", "m/s"),
        },
        {
            "kind": "practice",
            "title": "Reading distance–time graphs",
            "questions": [
                group("t2-n5-q1", "Use the walker's graph from the worked example.", [
                    numeric("t2-n5-q1a", "Calculate the walker's speed between B and C (40 s to 60 s).", sf(q5_1a), "m/s",
                            "Distance goes from 200 m to 300 m while time goes from 40 s to 60 s.",
                            ewau(GRAD_EQ, r"\text{speed} = \dfrac{300 - 200}{60 - 40} = \dfrac{100}{20}", "5", "m/s"), label="a"),
                    choice("t2-n5-q1b", "What is the walker doing between A and B (20 s to 40 s)?",
                           ["Walking at a constant speed", "Stationary", "Speeding up", "Walking back towards the start"], 1,
                           "The line is horizontal: the distance stays at 200 m, so the walker is not moving.", label="b"),
                    numeric("t2-n5-q1c", "What total distance did the walker travel in the 60 s?", 300, "m",
                            "Read the final distance off the graph.",
                            ["At 60 s the distance from the start is 300 m, and the walker never came back, so the total distance is 300 m."], label="c"),
                    numeric("t2-n5-q1d", "Calculate the walker's average speed for the whole 60 s.", sf(q5_1d), "m/s",
                            "Total distance ÷ total time, including the 20 s stop.",
                            ewau(AVG_EQ, r"\text{average speed} = \dfrac{300}{60}", "5", "m/s"), label="d"),
                ], graph=graph_dt_1),
                group("t2-n5-q2", "The graph shows the distance of a cyclist from her front door.", [
                    numeric("t2-n5-q2a", "Calculate the cyclist's speed during the first 30 s.", sf(q5_2a), "m/s",
                            "Gradient of the first straight section.",
                            ewau(GRAD_EQ, r"\text{speed} = \dfrac{150 - 0}{30 - 0}", "5", "m/s"), label="a"),
                    choice("t2-n5-q2b", "Which section of the journey was the fastest?",
                           ["0–30 s", "30–50 s", "50–70 s", "They were all the same speed"], 2,
                           "The steepest line is the fastest. The return leg covers 150 m in only 20 s; the outward leg took 30 s for the same distance.", label="b"),
                    numeric("t2-n5-q2c", "Calculate her speed on the way back (50 s to 70 s).", sf(q5_2c), "m/s",
                            "Ignore the minus sign on the gradient: a downward slope still has a speed.",
                            [r"Distance from the door changes from 150 m to 0 in $70 - 50 = 20$ s."]
                            + ewau(GRAD_EQ, r"\text{speed} = \dfrac{150}{20}", "7.5", "m/s")
                            + ["The gradient is negative because she is coming back towards the door; the steepness gives the speed and the sign gives the direction."], label="c"),
                ], graph=graph_dt_2),
            ],
        },
    ],
}


# =====================================================================
# N6 · Velocity–time graphs (2.10)
# =====================================================================

vt_points = [[0, 0], [10, 20], [20, 20], [30, 0]]
graph_vt_1 = graph(
    axis("t / s", 30, 5), axis("v / m/s", 20, 5),
    [line(vt_points)],
    "Velocity–time graph: rises from 0 to 20 m/s at 10 s, flat until 20 s, falls to 0 at 30 s.",
    marks_list=[mark(10, 20, "P", drop=True), mark(20, 20, "Q", drop=True)],
)

vt_points_2 = [[0, 5], [8, 25], [12, 25]]
graph_vt_2 = graph(
    axis("t / s", 12, 2), axis("v / m/s", 30, 5),
    [line(vt_points_2)],
    "Velocity–time graph: starts at 5 m/s, rises to 25 m/s at 8 s, then constant to 12 s.",
    marks_list=[mark(8, 25, "R", drop=True)],
)

q6_w_a = (20 - 0) / (10 - 0)
q6_w_d = 0.5 * 10 * 20
q6_1a = (0 - 20) / (30 - 20)
q6_1b = 10 * 20
q6_1c = 0.5 * 10 * 20 + 10 * 20 + 0.5 * 10 * 20
q6_2a = (25 - 5) / 8
q6_2b = 4 * 25

section_n6 = {
    "id": "vt-graphs",
    "band": "nn",
    "lessons": "2.10",
    "title": "Velocity–time graphs",
    "blurb": "Gradient gives acceleration; area under the line gives distance. Rectangles and triangles — and keep the units straight.",
    "equations": [VT_GRAD_EQ, VT_AREA_EQ],
    "checklist": [
        "Find an acceleration from the gradient of a straight section",
        "Recognise constant velocity (horizontal) and deceleration (sloping down)",
        "Find a distance from the area under the line (rectangle or triangle)",
    ],
    "parts": [
        {
            "kind": "explain",
            "title": "Gradient for acceleration, area for distance",
            "html": (
                "<p>A velocity–time graph tells you two things:</p>"
                "<table class='tbl'><tr><th>Feature</th><th>Gives you</th><th>How</th></tr>"
                "<tr><td>Gradient</td><td>Acceleration</td><td>change in velocity ÷ change in time (a triangle on the line)</td></tr>"
                "<tr><td>Area under the line</td><td>Distance travelled</td><td>split into rectangles and triangles, add them up</td></tr></table>"
                "<p><b>Reading the shape:</b> a line sloping up is acceleration; horizontal is constant velocity (zero acceleration, so zero resultant force); "
                "sloping down is deceleration.</p>"
                "<p><b>Areas:</b> rectangle $= \\text{base} \\times \\text{height}$; triangle $= \\tfrac{1}{2} \\times \\text{base} \\times \\text{height}$. "
                "The base is a <i>time</i> and the height is a <i>velocity</i>, so the area comes out in metres.</p>"
                "<p>Do not mix the two graphs up: on a <b>distance</b>–time graph the gradient is speed; on a <b>velocity</b>–time graph the gradient is acceleration.</p>"
            ),
        },
        {
            "kind": "worked",
            "title": "Acceleration and distance from a v–t graph",
            "question": "The graph shows a tram's journey between two stops. Calculate (a) the acceleration in the first 10 s and (b) the distance travelled in the first 10 s.",
            "graph": graph_vt_1,
            "steps": [
                r"<b>(a)</b> Gradient from the origin to P: velocity changes by $20 - 0 = 20$ m/s in $10 - 0 = 10$ s.",
                r"$a = \dfrac{20}{10} = 2$ m/s².",
                r"<b>(b)</b> The area under the line from 0 to 10 s is a triangle with base 10 s and height 20 m/s.",
                r"$\text{distance} = \tfrac{1}{2} \times 10 \times 20 = 100$ m.",
            ],
        },
        {
            "kind": "practice",
            "title": "Reading velocity–time graphs",
            "questions": [
                group("t2-n6-q1", "Use the tram's graph from the worked example.", [
                    numeric("t2-n6-q1a", "Calculate the tram's acceleration between 20 s and 30 s. Include the sign.", sf(q6_1a), "m/s²",
                            "The velocity falls from 20 m/s to 0 in 10 s.",
                            ewau(ACC_EQ, r"a = \dfrac{0 - 20}{30 - 20} = \dfrac{-20}{10}", "-2", "m/s²"), label="a"),
                    numeric("t2-n6-q1b", "Calculate the distance travelled between P and Q (10 s to 20 s).", sf(q6_1b), "m",
                            "That part of the area is a rectangle: 10 s wide and 20 m/s tall.",
                            ewau(VT_AREA_EQ, r"\text{distance} = 10 \times 20", "200", "m"), label="b"),
                    numeric("t2-n6-q1c", "Calculate the total distance between the two stops.", sf(q6_1c), "m",
                            "Triangle + rectangle + triangle.",
                            [r"First triangle: $\tfrac{1}{2} \times 10 \times 20 = 100$ m.",
                             r"Rectangle: $10 \times 20 = 200$ m.",
                             r"Last triangle: $\tfrac{1}{2} \times 10 \times 20 = 100$ m."]
                            + ewau(VT_AREA_EQ, r"\text{distance} = 100 + 200 + 100", "400", "m"), label="c"),
                    choice("t2-n6-q1d", "During which part of the journey is the resultant force on the tram zero?",
                           ["0–10 s", "10–20 s", "20–30 s", "Never"], 1,
                           "Between P and Q the velocity is constant, so the acceleration is zero — and Newton's first law says the resultant force is zero.", label="d"),
                ], graph=graph_vt_1),
                group("t2-n6-q2", "The graph shows a car joining a dual carriageway.", [
                    numeric("t2-n6-q2a", "Calculate the car's acceleration in the first 8 s.", sf(q6_2a), "m/s²",
                            "It does not start from rest: u = 5 m/s.",
                            ewau(ACC_EQ, r"a = \dfrac{25 - 5}{8} = \dfrac{20}{8}", "2.5", "m/s²"), label="a"),
                    numeric("t2-n6-q2b", "Calculate the distance travelled between 8 s and 12 s.", sf(q6_2b), "m",
                            "A rectangle 4 s wide and 25 m/s tall.",
                            ewau(VT_AREA_EQ, r"\text{distance} = (12 - 8) \times 25 = 4 \times 25", "100", "m"), label="b"),
                ], graph=graph_vt_2),
            ],
        },
    ],
}


# =====================================================================
# N7 · Typical speeds and g (2.12, 2.13)
# =====================================================================

q7_4 = G * 3
q7_5 = G * 1.5

section_n7 = {
    "id": "typical-speeds",
    "band": "nn",
    "lessons": "2.12–2.13",
    "title": "Typical speeds and g",
    "blurb": "Numbers you must simply know: everyday speeds, the acceleration of free fall, and the size of everyday accelerations.",
    "equations": [r"g = 10\ \text{m/s}^2"],
    "checklist": [
        "Recall typical speeds for walking, running, cycling, cars, trains, wind and sound",
        "Recall that g = 10 m/s² in free fall",
        "Estimate the size of everyday accelerations",
    ],
    "parts": [
        {
            "kind": "explain",
            "title": "Speeds and accelerations to memorise",
            "html": (
                "<p>Exam questions ask you to <i>recall</i> these, or to spot a silly answer (a cyclist at 60 m/s is not plausible). "
                "Learn the rough values:</p>"
                "<table class='tbl'><tr><th>Moving thing</th><th>Typical speed</th></tr>"
                "<tr><td>Walking</td><td>about 1.5 m/s</td></tr>"
                "<tr><td>Running</td><td>about 3 m/s (a sprinter: 10 m/s)</td></tr>"
                "<tr><td>Cycling</td><td>about 6 m/s</td></tr>"
                "<tr><td>Car in town (30 mph)</td><td>about 13 m/s</td></tr>"
                "<tr><td>Car on a motorway (70 mph)</td><td>about 30 m/s</td></tr>"
                "<tr><td>Fast train</td><td>about 55 m/s</td></tr>"
                "<tr><td>Airliner</td><td>about 250 m/s</td></tr>"
                "<tr><td>Wind</td><td>light breeze 5 m/s; gale 20 m/s</td></tr>"
                "<tr><td>Sound in air</td><td>about 340 m/s</td></tr></table>"
                "<p><b>Free fall:</b> near the Earth's surface, anything falling freely accelerates at $g = 10$ m/s² (ignoring air resistance). "
                "Its speed increases by 10 m/s every second.</p>"
                "<table class='tbl'><tr><th>Everyday acceleration</th><th>Rough size</th></tr>"
                "<tr><td>Lift starting to move</td><td>about 1 m/s²</td></tr>"
                "<tr><td>Family car pulling away</td><td>2–3 m/s²</td></tr>"
                "<tr><td>Sprinter off the blocks</td><td>about 5 m/s²</td></tr>"
                "<tr><td>Free fall</td><td>10 m/s²</td></tr>"
                "<tr><td>Car in a crash</td><td>hundreds of m/s²</td></tr></table>"
            ),
        },
        {
            "kind": "worked",
            "title": "Using g",
            "question": "A coin is dropped down a well. Calculate its speed after 2 s of free fall.",
            "steps": [r"Dropped means $u = 0$. In free fall $a = g = 10$ m/s², $t = 2$ s."]
            + ewau(V_EQ, r"v = 0 + 10 \times 2", "20", "m/s")
            + ["Sense check: 20 m/s is about 45 mph — fast, but plausible for 2 s of falling."],
        },
        {
            "kind": "practice",
            "title": "Typical values",
            "questions": [
                choice("t2-n7-q1", "Which is the best estimate of walking speed?", ["0.15 m/s", "1.5 m/s", "15 m/s", "150 m/s"], 1,
                       "About 1.5 m/s — roughly 5 km/h. 15 m/s would be faster than an Olympic sprinter."),
                choice("t2-n7-q2", "What is the approximate speed of sound in air?", ["34 m/s", "340 m/s", "3400 m/s", "300 000 000 m/s"], 1,
                       "About 340 m/s. The last option is the speed of light."),
                choice("t2-n7-q3", "A car is driving along a motorway. Which is the best estimate of its speed?", ["3 m/s", "13 m/s", "30 m/s", "300 m/s"], 2,
                       "70 mph is about 30 m/s. 13 m/s is the 30 mph town limit."),
                numeric("t2-n7-q4", "A ball is dropped from a tall building. Calculate its speed after 3 s. (Ignore air resistance.)", sf(q7_4), "m/s",
                        "It gains 10 m/s every second.",
                        ewau(V_EQ, r"v = 0 + 10 \times 3", "30", "m/s")),
                numeric("t2-n7-q5", "A stone is dropped from a cliff. Calculate its speed after 1.5 s.", sf(q7_5), "m/s",
                        "v = u + at with u = 0 and a = 10 m/s².",
                        ewau(V_EQ, r"v = 0 + 10 \times 1.5", "15", "m/s")),
                choice("t2-n7-q6", "Which is the best estimate of the acceleration of a family car pulling away from traffic lights?",
                       ["0.02 m/s²", "2 m/s²", "20 m/s²", "200 m/s²"], 1,
                       "About 2 m/s²: 0 to 13 m/s (30 mph) in roughly 6 s. 20 m/s² is twice the acceleration of free fall — you would be pinned to your seat."),
            ],
        },
    ],
}


# =====================================================================
# N8 · Measuring speed in the lab (2.11)
# =====================================================================

q8_w = 0.05 / 0.025
q8_1 = 0.10 / 0.040
q8_2 = 0.80 / 0.32
q8_5 = 1.5 / 2.5

section_n8 = {
    "id": "measuring-speed",
    "band": "nn",
    "lessons": "2.11",
    "title": "Measuring speed in the lab",
    "blurb": "Light gates, stopwatches, ticker timers and video: what each one actually measures, and the calculation that turns it into a speed.",
    "equations": [LIGHT_EQ],
    "checklist": [
        "Describe how to measure a speed with a light gate and an interrupt card",
        "Describe how to measure a speed with a stopwatch and a metre rule",
        "Explain why light gates give more accurate timings than a stopwatch",
    ],
    "parts": [
        {
            "kind": "explain",
            "title": "Every method measures a distance and a time",
            "html": (
                "<p>No instrument measures speed directly. Each method measures a <b>distance</b> and a <b>time</b>, and you calculate speed = distance ÷ time.</p>"
                "<table class='tbl'><tr><th>Method</th><th>Distance</th><th>Time</th><th>Notes</th></tr>"
                "<tr><td><b>Stopwatch + metre rule / tape</b></td><td>Marked out on the floor or bench</td><td>Stopwatch, started and stopped by hand</td>"
                "<td>Simple, but human <b>reaction time</b> (about 0.2 s) adds error. Fine for long times; poor for anything under a few seconds.</td></tr>"
                "<tr><td><b>One light gate + interrupt card</b></td><td>Length of the card on the trolley</td><td>How long the card blocks the beam</td>"
                "<td>Gives the speed <i>at that point</i>. The timer starts and stops automatically, so no reaction time.</td></tr>"
                "<tr><td><b>Two light gates</b></td><td>Distance between the gates</td><td>Time for the trolley to go from one gate to the other</td>"
                "<td>Gives the <i>average</i> speed between the gates.</td></tr>"
                "<tr><td><b>Ticker timer</b></td><td>Measured between dots on the tape</td><td>50 dots per second, so 0.02 s between dots</td>"
                "<td>Older method; dots spreading out shows acceleration.</td></tr>"
                "<tr><td><b>Video / motion sensor</b></td><td>Scale in the frame, or ultrasound pulses</td><td>Frame rate, or the sensor's clock</td>"
                "<td>Records the whole motion, not just one moment.</td></tr></table>"
                "<p>For a light gate: $$" + LIGHT_EQ + "$$ Convert the card length to <b>metres</b>.</p>"
            ),
        },
        {
            "kind": "worked",
            "title": "Speed from a light gate",
            "question": "A trolley carries a card 5.0 cm long. The card takes 0.025 s to pass through a light gate. Calculate the trolley's speed.",
            "steps": [r"Convert the card length: $5.0 \text{ cm} = 0.050$ m."]
            + ewau(LIGHT_EQ, r"\text{speed} = \dfrac{0.050}{0.025}", "2.0", "m/s"),
        },
        {
            "kind": "practice",
            "title": "Measuring speed",
            "questions": [
                numeric("t2-n8-q1", "A 10 cm card on a trolley blocks a light gate for 0.040 s. Calculate the speed of the trolley.", sf(q8_1), "m/s",
                        "10 cm = 0.10 m.",
                        ewau(LIGHT_EQ, r"\text{speed} = \dfrac{0.10}{0.040}", "2.5", "m/s")),
                numeric("t2-n8-q2", "Two light gates are placed 0.80 m apart. A trolley takes 0.32 s to travel from the first gate to the second. Calculate its average speed between the gates.", sf(q8_2), "m/s",
                        "Distance between the gates ÷ time between the gates.",
                        ewau(SPEED_EQ, r"\text{speed} = \dfrac{0.80}{0.32}", "2.5", "m/s")),
                written("t2-n8-q3", "Explain why a light gate gives a more accurate speed than a student with a stopwatch.",
                        marks(["The light gate's timer starts and stops automatically when the beam is broken.",
                               "So there is no human reaction time (about 0.2 s) adding to the measured time.",
                               "This matters most when the time being measured is short — the error from reaction time would be a large fraction of it."]), lines=3),
                choice("t2-n8-q4", "What does a light gate connected to a timer measure directly?", ["Speed", "Time", "Distance", "Acceleration"], 1,
                       "It measures a time: how long the beam is broken. You have to divide a distance (the card length) by that time to get a speed."),
                numeric("t2-n8-q5", "A student uses a stopwatch to time a toy car travelling 1.5 m along a bench. The time is 2.5 s. Calculate the average speed.", sf(q8_5), "m/s",
                        "Distance over time, nothing to convert.",
                        ewau(SPEED_EQ, r"\text{speed} = \dfrac{1.5}{2.5}", "0.6", "m/s")),
                written("t2-n8-q6", "Describe how you would measure the speed of a trolley at one point on a bench using a light gate.",
                        marks(["Fix a card of known length to the trolley and measure the card's length with a ruler.",
                               "Set up the light gate at the point of interest, connected to a timer, so the card breaks the beam as the trolley passes.",
                               "Read the time the beam is blocked from the timer.",
                               "Calculate speed = length of card ÷ time. Repeat and take a mean."]), lines=4),
            ],
        },
    ],
}


SECTIONS = [section_n1, section_n2, section_n3, section_n4, section_n5, section_n6, section_n7, section_n8]
