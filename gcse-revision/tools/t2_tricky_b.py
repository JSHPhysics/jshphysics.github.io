"""
t2_tricky_b.py — The tricky bits, sections T8–T13, plus the key facts.

Conservation of momentum; F = Δp/t and safety features; braking distance
∝ v²; core practical analysis; measuring reaction time; estimation.
"""

from math import sqrt

from t2lib import (
    axis, choice, ewau, graph, group, label, line, mark, marks, numeric,
    sf, written,
)

G = 10

P_EQ = r"p = m \times v"
COM_EQ = r"\text{total momentum before} = \text{total momentum after}"
FP_EQ = r"F = \dfrac{mv - mu}{t}"
FP_WORDS = r"\text{force} = \dfrac{\text{change in momentum}}{\text{time}}"
KE_EQ = r"KE = \tfrac{1}{2} \times m \times v^2"
WD_EQ = r"\text{work done} = F \times d"
BRAKE_EQ = r"\tfrac{1}{2} m v^2 = F \times d"
D_EQ = r"d = \dfrac{\tfrac{1}{2} m v^2}{F}"
LIGHT_EQ = r"\text{speed} = \dfrac{\text{length of card}}{\text{time}}"
ACC_EQ = r"a = \dfrac{v - u}{t}"
GRAD_EQ = r"\text{gradient} = \dfrac{\text{change in } y}{\text{change in } x}"
DROP_EQ = r"x = \tfrac{1}{2} g t^2"
TREACT_EQ = r"t = \sqrt{\dfrac{2x}{g}}"
F_EQ = r"F = m \times a"
THINK_EQ = r"\text{thinking distance} = \text{speed} \times \text{reaction time}"


# =====================================================================
# T8 · Conservation of momentum (2.23–2.25)
# =====================================================================

t8_w = (2 * 3 + 1 * 0) / (2 + 1)
t8_1 = (1500 * 10 + 1000 * 0) / (1500 + 1000)
t8_2 = (0.02 * 300) / 4
t8_3 = (2 * 4 + 3 * (-1)) / (2 + 3)
t8_4 = (0.5 * 6 - 0.5 * 2) / 0.5
t8_7 = (5 * 4) / 50

section_t8 = {
    "id": "conservation-momentum",
    "band": "tricky",
    "lessons": "2.23–2.25",
    "title": "Conservation of momentum",
    "blurb": "Total momentum before = total momentum after, as long as no outside force acts. The method is always the same; the directions are where it goes wrong.",
    "equations": [COM_EQ, P_EQ],
    "checklist": [
        "Apply conservation of momentum to objects that stick together",
        "Use a sign convention so that opposite directions have opposite signs",
        "Handle explosions and recoil, where the total momentum is zero",
        "Find the velocity of one object after a collision when the other's is known",
    ],
    "parts": [
        {
            "kind": "explain",
            "title": "Before equals after",
            "html": (
                "<p>In any collision or explosion where no external force acts (a <b>closed system</b>), the <b>total momentum is conserved</b>: "
                "the total before equals the total after. This follows from Newton's third law (see the pairs section).</p>"
                "$$" + COM_EQ + "$$"
                "<p><b>Method, every time:</b></p>"
                "<ol class='list'><li>Choose a positive direction (usually the direction the first object moves). Anything moving the other way gets a <b>minus sign</b>.</li>"
                "<li>Write the momentum of each object <b>before</b>: $m \\times v$ each, with signs. Add them.</li>"
                "<li>Write the momentum of each object <b>after</b>, using a symbol for the unknown velocity. Add them.</li>"
                "<li>Set before = after and solve. A negative answer means that object moves in the negative direction.</li></ol>"
                "<table class='tbl'><tr><th>Type</th><th>What to watch</th></tr>"
                "<tr><td>Objects stick together</td><td>After the collision there is one object with the <b>combined mass</b> and one velocity</td></tr>"
                "<tr><td>Head-on collision</td><td>The two velocities before have <b>opposite signs</b></td></tr>"
                "<tr><td>Explosion / recoil (gun, rocket, skater throwing something)</td><td>Total momentum before is <b>zero</b>, so afterwards the two momenta are equal and opposite</td></tr>"
                "<tr><td>One object's final velocity given</td><td>Put it in; the other final velocity is the unknown</td></tr></table>"
            ),
        },
        {
            "kind": "worked",
            "title": "Sticking together",
            "question": "A 2 kg trolley moving at 3 m/s collides with a stationary 1 kg trolley. They stick together. Calculate their velocity after the collision.",
            "steps": [
                r"Positive direction: the direction of the moving trolley.",
                r"Before: $p = (2 \times 3) + (1 \times 0) = 6$ kg m/s.",
                r"After: one object of mass $2 + 1 = 3$ kg at velocity $v$: $p = 3v$.",
                r"Conservation: $3v = 6$, so $v = 2$ m/s, in the original direction of the 2 kg trolley.",
            ],
        },
        {
            "kind": "practice",
            "title": "Collisions and explosions",
            "questions": [
                numeric("t2-t8-q1", "A 1500 kg car travelling at 10 m/s runs into the back of a stationary 1000 kg car. The two cars lock together. Calculate their velocity immediately after the collision.", sf(t8_1), "m/s",
                        "Momentum before is all in the moving car. After, the combined mass is 2500 kg.",
                        [r"Before: $1500 \times 10 + 1000 \times 0 = 15\,000$ kg m/s.", r"After: $2500 \times v$.",
                         r"$2500v = 15\,000$, so $v = 6$ m/s."]),
                numeric("t2-t8-q2", "A 4 kg rifle fires a 20 g bullet at 300 m/s. Calculate the recoil speed of the rifle (just the size).", sf(t8_2), "m/s",
                        "Before firing the total momentum is zero, so afterwards the rifle's momentum is equal and opposite to the bullet's. 20 g = 0.02 kg.",
                        [r"Before: $0$ (nothing moving).", r"After: $(0.02 \times 300) + (4 \times v) = 0$.",
                         r"$6 + 4v = 0$, so $v = -1.5$ m/s. The rifle recoils at 1.5 m/s in the opposite direction to the bullet."]),
                numeric("t2-t8-q3", "A 2 kg trolley moving to the right at 4 m/s collides head-on with a 3 kg trolley moving to the left at 1 m/s. They stick together. Calculate their velocity after the collision (take right as positive).", sf(t8_3), "m/s",
                        "The 3 kg trolley's velocity is −1 m/s.",
                        [r"Before: $(2 \times 4) + (3 \times (-1)) = 8 - 3 = 5$ kg m/s.", r"After: $(2 + 3) \times v = 5v$.",
                         r"$5v = 5$, so $v = 1$ m/s to the right (positive)."]),
                numeric("t2-t8-q4", "A 0.5 kg snooker ball moving at 6 m/s hits an identical stationary ball. After the collision the first ball continues in the same direction at 2 m/s. Calculate the velocity of the second ball.", sf(t8_4), "m/s",
                        "The balls do not stick. Put in the first ball's final velocity; the second ball's is the unknown.",
                        [r"Before: $(0.5 \times 6) + (0.5 \times 0) = 3$ kg m/s.", r"After: $(0.5 \times 2) + (0.5 \times v) = 1 + 0.5v$.",
                         r"$1 + 0.5v = 3$, so $v = 4$ m/s in the original direction."]),
                written("t2-t8-q5", "State what is meant by \"momentum is conserved\" in a collision, and give the condition for it to be true.",
                        marks(["The total momentum of the objects before the collision equals the total momentum after it.",
                               "This is true provided no external (outside) forces act on the system — it is a closed system."]), lines=2),
                numeric("t2-t8-q6", "A 50 kg skater standing still on ice throws a 5 kg bag horizontally at 4 m/s. Calculate the skater's recoil speed (just the size).", sf(t8_7), "m/s",
                        "Total momentum before is zero.",
                        [r"After: $(5 \times 4) + (50 \times v) = 0$.", r"$20 + 50v = 0$, so $v = -0.4$ m/s: the skater moves at 0.4 m/s the opposite way to the bag."]),
            ],
        },
    ],
}


# =====================================================================
# T9 · F = Δp / t and safety features (2.26, 2.31)
# =====================================================================

t9_w_dp = 60 * 15 - 60 * 0
t9_w_f1 = t9_w_dp / 0.05
t9_w_f2 = t9_w_dp / 0.3
t9_1 = (0.16 * 30 - 0) / 0.02
t9_2 = (1200 * 20 - 0) / 0.5
t9_3 = (70 * 12 - 0) / 0.1
t9_4 = (60 * 10) / 2000

section_t9 = {
    "id": "force-momentum",
    "band": "tricky",
    "lessons": "2.26, 2.31",
    "title": "Force = change in momentum ÷ time, and safety features",
    "blurb": "Why airbags, crumple zones, seatbelts and helmets work: the momentum change is fixed, so make the time longer and the force gets smaller.",
    "equations": [FP_EQ],
    "checklist": [
        "Use F = (mv − mu) ÷ t to find a force, a time or a change in momentum",
        "Explain how a safety feature reduces injury, using momentum, time and force in the right order",
        "Explain why large decelerations are dangerous",
    ],
    "parts": [
        {
            "kind": "explain",
            "title": "Newton's second law, momentum version",
            "html": (
                "$$" + FP_WORDS + r"\qquad F = \dfrac{mv - mu}{t}$$"
                "<p>The change in momentum is $mv - mu$: final momentum minus initial momentum. For something stopping, $v = 0$, so the change is just $-mu$ "
                "(the size of the force is $mu \\div t$; the minus sign says it acts against the motion).</p>"
                "<p><b>The key idea:</b> in a collision the change in momentum is fixed — the car <i>is</i> going to stop. The only thing a safety feature can change is "
                "<b>how long the stopping takes</b>. A longer time means a smaller force, and it is the force that does the damage.</p>"
                "<table class='tbl'><tr><th>Feature</th><th>How it increases the time</th></tr>"
                "<tr><td>Crumple zone</td><td>The front of the car crushes progressively instead of stopping dead</td></tr>"
                "<tr><td>Airbag</td><td>Cushions the head: it stops over the depth of the bag, not against the hard dashboard</td></tr>"
                "<tr><td>Seatbelt</td><td>Stretches slightly, and stops the person over the same time as the car rather than when they hit the windscreen</td></tr>"
                "<tr><td>Cycle helmet</td><td>Foam compresses on impact</td></tr>"
                "<tr><td>Crash mat, bending your knees on landing</td><td>Same idea: longer stopping time</td></tr></table>"
                "<p><b>The 4-mark answer, in order:</b> (1) the momentum change is the same with or without the feature; (2) the feature increases the time taken to stop; "
                "(3) force = change in momentum ÷ time, so (4) the force on the person is smaller, so less injury. Students who write \"it absorbs the impact\" get nothing.</p>"
                "<p><b>Large decelerations are dangerous</b> because a large deceleration means a large force on the body ($F = ma$). Forces of many times a person's weight can break bones, "
                "tear organs and injure the brain against the skull — even without hitting anything, because the body's own tissues have to supply the stopping force.</p>"
            ),
        },
        {
            "kind": "worked",
            "title": "With and without an airbag",
            "question": "A 60 kg driver is travelling at 15 m/s when the car crashes and stops. (a) Calculate the force on the driver if she stops in 0.05 s against the steering wheel. (b) Calculate the force if an airbag increases her stopping time to 0.3 s.",
            "steps": [
                r"Change in momentum $= mv - mu = (60 \times 0) - (60 \times 15) = -900$ kg m/s (the size is 900 kg m/s, acting against her motion).",
                r"<b>(a)</b> $F = \dfrac{900}{0.05} = 18\,000$ N — about 30 times her weight.",
                r"<b>(b)</b> $F = \dfrac{900}{0.3} = 3000$ N.",
                r"Same change in momentum, six times the time, one sixth of the force.",
            ],
        },
        {
            "kind": "practice",
            "title": "Force and momentum",
            "questions": [
                numeric("t2-t9-q1", "A 0.16 kg cricket ball travelling at 30 m/s is caught and brought to rest in 0.02 s. Calculate the size of the average force on the ball.", sf(t9_1), "N",
                        "Change in momentum is 0.16 × 30, then divide by the time.",
                        [r"Change in momentum $= (0.16 \times 0) - (0.16 \times 30) = -4.8$ kg m/s: a size of 4.8 kg m/s, against the ball's motion."] + ewau(FP_EQ, r"F = \dfrac{4.8}{0.02}", "240", "N (acting against the ball's motion)")),
                numeric("t2-t9-q2", "A 1200 kg car travelling at 20 m/s hits a wall and stops in 0.5 s. Calculate the size of the average force on the car.", sf(t9_2), "N",
                        "mu = 1200 × 20.",
                        [r"Change in momentum $= 0 - (1200 \times 20) = -24\,000$ kg m/s: a size of 24 000 kg m/s."] + ewau(FP_EQ, r"F = \dfrac{24\,000}{0.5}", "48\\,000", "N (48 kN, acting against the motion)")),
                numeric("t2-t9-q3", "A 70 kg passenger without a seatbelt is moving at 12 m/s when the car stops suddenly. He hits the dashboard and stops in 0.1 s. Calculate the size of the force on him.", sf(t9_3), "N",
                        "Momentum change 70 × 12, time 0.1 s.",
                        [r"Change in momentum $= 0 - (70 \times 12) = -840$ kg m/s: a size of 840 kg m/s."] + ewau(FP_EQ, r"F = \dfrac{840}{0.1}", "8400", "N — about 12 times his weight")),
                numeric("t2-t9-q4", "A 60 kg gymnast lands from a vault at 10 m/s. The maximum safe force on her legs is 2000 N. Calculate the minimum time she must take to stop.", sf(t9_4), "s",
                        "Rearrange: t = change in momentum ÷ force.",
                        [r"Change in momentum $= 60 \times 10 = 600$ kg m/s.", r"$t = \dfrac{600}{2000} = 0.3$ s.",
                         "She bends her knees so that the stop takes at least 0.3 s."]),
                written("t2-t9-q5", "Explain how an airbag reduces the injury to a driver in a crash.",
                        marks(["The driver's change in momentum is the same whether or not the airbag is there (she goes from her speed to rest).",
                               "The airbag increases the time taken for her head to stop.",
                               "Force = change in momentum ÷ time, so a longer time means a smaller force on her.",
                               "A smaller force means less injury."]), lines=4),
                choice("t2-t9-q6", "Which of these is the reason a crumple zone reduces the force on passengers?",
                       ["It reduces the change in momentum of the car", "It increases the time over which the car's momentum changes",
                        "It increases the mass of the car", "It makes the car stop more quickly"], 1,
                       "The momentum change is fixed by the car's speed. A crumple zone makes the stop take longer, and F = Δp ÷ t gets smaller."),
                written("t2-t9-q7", "Explain why a large deceleration is dangerous for a person in a vehicle.",
                        marks(["A large deceleration means a large resultant force on the person (F = ma).",
                               "The force on the body can be many times the person's weight.",
                               "Such forces can break bones, damage internal organs, or injure the brain as it strikes the inside of the skull."]), lines=3),
            ],
        },
    ],
}


# =====================================================================
# T10 · Braking distance ∝ v² (2.32P, 2.33P)
# =====================================================================

t10_w = 0.5 * 1200 * 20 ** 2 / 6000
t10_1 = 0.5 * 1200 * 30 ** 2 / 6000
t10_2 = 0.5 * 1000 * 15 ** 2 / 25
# Highway Code style estimate: 30 mph ≈ 13 m/s, 60 mph ≈ 26 m/s; reaction time 0.7 s;
# braking 14 m at 30 mph scales with v²
t10_4_think = 26 * 0.7
t10_4_brake = 14 * (26 / 13) ** 2
t10_4 = t10_4_think + t10_4_brake

section_t10 = {
    "id": "braking-v-squared",
    "band": "tricky",
    "lessons": "2.32P, 2.33P",
    "title": "Braking distance and speed squared",
    "blurb": "The brakes do work to remove the car's kinetic energy. Because KE depends on v², doubling the speed quadruples the braking distance.",
    "equations": [BRAKE_EQ],
    "checklist": [
        "Use work done = kinetic energy to calculate a braking distance or a braking force",
        "Explain why braking distance is proportional to speed squared",
        "Estimate how stopping distance changes across typical speeds (thinking ∝ v, braking ∝ v²)",
    ],
    "parts": [
        {
            "kind": "explain",
            "title": "Work done by the brakes = kinetic energy lost",
            "html": (
                "<p>To stop a car, the brakes must remove all of its kinetic energy. The braking force does work over the braking distance:</p>"
                "$$" + WD_EQ + r"\qquad\qquad " + KE_EQ + "$$"
                "<p>Setting them equal:</p>"
                "$$" + BRAKE_EQ + r"\qquad\Rightarrow\qquad " + D_EQ + "$$"
                "<p>The braking force $F$ is roughly constant for a given car and road (it depends on the brakes, tyres and surface). So:</p>"
                "<ul><li><b>Braking distance ∝ $v^2$.</b> Double the speed → four times the braking distance. Treble it → nine times.</li>"
                "<li><b>Thinking distance ∝ $v$</b>, because it is speed × reaction time. Double the speed → double the thinking distance.</li>"
                "<li>A heavier car (more $m$) or a wet road (less $F$) also increases the braking distance.</li></ul>"
                "<table class='tbl'><tr><th>Speed</th><th>Thinking distance</th><th>Braking distance</th><th>Stopping distance</th></tr>"
                "<tr><td>20 mph (9 m/s)</td><td>6 m</td><td>6 m</td><td>12 m</td></tr>"
                "<tr><td>30 mph (13 m/s)</td><td>9 m</td><td>14 m</td><td>23 m</td></tr>"
                "<tr><td>40 mph (18 m/s)</td><td>12 m</td><td>24 m</td><td>36 m</td></tr>"
                "<tr><td>50 mph (22 m/s)</td><td>15 m</td><td>38 m</td><td>53 m</td></tr>"
                "<tr><td>60 mph (27 m/s)</td><td>18 m</td><td>55 m</td><td>73 m</td></tr>"
                "<tr><td>70 mph (31 m/s)</td><td>21 m</td><td>75 m</td><td>96 m</td></tr></table>"
                "<p>(Highway Code figures, for a dry road and an alert driver.) Notice the thinking column goes up in equal steps; the braking column grows faster and faster.</p>"
            ),
        },
        {
            "kind": "worked",
            "title": "Braking distance from work done",
            "question": "A 1200 kg car travelling at 20 m/s brakes with a constant braking force of 6000 N. Calculate its braking distance.",
            "steps": [
                r"Kinetic energy to remove: $KE = \tfrac{1}{2} \times 1200 \times 20^2 = \tfrac{1}{2} \times 1200 \times 400 = 240\,000$ J.",
                r"The brakes do this much work: $F \times d = 240\,000$.",
                r"$d = \dfrac{240\,000}{6000} = 40$ m.",
            ],
        },
        {
            "kind": "practice",
            "title": "Braking and speed",
            "questions": [
                numeric("t2-t10-q1", "The same 1200 kg car with the same 6000 N braking force is now travelling at 30 m/s. Calculate its braking distance.", sf(t10_1), "m",
                        "KE = ½ × 1200 × 30². Then divide by 6000 N.",
                        [r"$KE = \tfrac{1}{2} \times 1200 \times 30^2 = 540\,000$ J.", r"$d = \dfrac{540\,000}{6000} = 90$ m.",
                         r"1.5 times the speed gives $1.5^2 = 2.25$ times the braking distance ($2.25 \times 40 = 90$ m). ✓"]),
                numeric("t2-t10-q2", "A 1000 kg car travelling at 15 m/s stops in a braking distance of 25 m. Calculate the average braking force.", sf(t10_2), "N",
                        "Find the KE, then F = KE ÷ d.",
                        [r"$KE = \tfrac{1}{2} \times 1000 \times 15^2 = 112\,500$ J.", r"$F = \dfrac{112\,500}{25} = 4500$ N."]),
                choice("t2-t10-q3", "A driver doubles her speed. What happens to the braking distance?",
                       ["It doubles", "It stays the same", "It quadruples (×4)", "It halves"], 2,
                       "Braking distance ∝ v². Doubling v multiplies v² by 4, so the braking distance is four times as long. (Thinking distance only doubles.)"),
                numeric("t2-t10-q4", "At 30 mph (13 m/s) a car's thinking distance is 9 m and its braking distance is 14 m. Estimate its stopping distance at 60 mph (26 m/s).", sf(t10_4), "m",
                        "Thinking distance doubles; braking distance goes up by 2² = 4.",
                        [r"Thinking distance $\propto v$: $9 \times 2 = 18$ m.", r"Braking distance $\propto v^2$: $14 \times 2^2 = 56$ m.",
                         r"Stopping distance $\approx 18 + 56 = 74$ m — roughly three times the 23 m at 30 mph, not twice."], tolerance=0.06),
                written("t2-t10-q5", "Explain why the braking distance of a car is proportional to the square of its speed.",
                        marks(["The brakes must do work equal to the car's kinetic energy to stop it: F × d = ½mv².",
                               "The braking force F is roughly constant (it depends on the brakes, tyres and road, not on speed).",
                               "So d = ½mv² ÷ F, and d is proportional to v²: doubling the speed quadruples the braking distance."]), lines=3),
                choice("t2-t10-q6", "Which factor increases the braking distance by reducing the braking force?",
                       ["A heavier load in the car", "A higher speed", "A wet or icy road", "A faster reaction time"], 2,
                       "Water or ice reduces the friction between the tyres and the road, so the braking force is smaller and the same KE takes a longer distance to remove. A heavier load increases the KE instead."),
            ],
        },
    ],
}


# =====================================================================
# T11 · Core practical: the analysis (2.19)
# =====================================================================

t11_w_v1 = 0.10 / 0.050
t11_w_v2 = 0.10 / 0.025
t11_w_a = (t11_w_v2 - t11_w_v1) / 0.4
t11_1_v1 = 0.08 / 0.040
t11_1_v2 = 0.08 / 0.020
t11_1_a = (t11_1_v2 - t11_1_v1) / 0.5

graph_t11 = graph(
    axis("F / N", 3, 0.5), axis("a / m/s²", 6, 1),
    [line([[0.5, 0], [3, 5]])],
    "Acceleration against force: a straight line from (0.5, 0) to (3, 5), not through the origin.",
    marks_list=[mark(0.5, 0, "X", dx=-4, dy=-12), mark(3, 5, "Y", drop=True)],
)
t11_g_grad = (5 - 0) / (3 - 0.5)
t11_g_mass = 1 / t11_g_grad

section_t11 = {
    "id": "core-practical-analysis",
    "band": "tricky",
    "lessons": "2.19",
    "title": "Core practical: the analysis",
    "blurb": "Why the masses move from trolley to hanger, how two light gates give an acceleration, what friction does to the graph, and what the gradient means.",
    "equations": [LIGHT_EQ, ACC_EQ],
    "checklist": [
        "Calculate an acceleration from two light-gate readings and the time between them",
        "Explain why the total mass must stay constant when investigating force",
        "Explain how to compensate for friction, and how friction shows up on the graph",
        "Interpret the gradient and intercept of an acceleration–force graph",
    ],
    "parts": [
        {
            "kind": "explain",
            "title": "From light-gate times to an acceleration",
            "html": (
                "<p>With two light gates the data logger (or you) does three calculations:</p>"
                "<ol class='list'><li>Speed at gate 1: $v_1 = \\text{card length} \\div \\text{time through gate 1}$.</li>"
                "<li>Speed at gate 2: $v_2 = \\text{card length} \\div \\text{time through gate 2}$.</li>"
                "<li>Acceleration: $a = (v_2 - v_1) \\div \\text{time to travel from gate 1 to gate 2}$.</li></ol>"
                "<p>Keep the units straight: card length in <b>metres</b>, times in seconds.</p>"
                "<p><b>Why the masses move from the trolley to the hanger.</b> The hanging weight accelerates the whole system — trolley <i>plus</i> hanging mass — "
                "because they are joined by the string. If you simply added more mass to the hanger you would increase the force <i>and</i> the mass at the same time, "
                "so you could not tell which caused the change in acceleration. Moving a mass from the trolley to the hanger changes only the force; the total mass is unchanged.</p>"
                "<p><b>Friction.</b> Friction on the trolley opposes the motion, so the <i>resultant</i> force is less than the hanging weight. Two ways to deal with it:</p>"
                "<ul><li><b>Compensate:</b> tilt the runway slightly, until the trolley (given a gentle push, with no hanging mass) runs at a constant speed. The component of its weight down the slope now cancels friction.</li>"
                "<li><b>Or leave it and read it off the graph:</b> uncompensated friction gives an acceleration–force graph that is still a straight line, but it cuts the force axis at a positive value. That intercept is the friction force — the force you need before the trolley accelerates at all.</li></ul>"
                "<p><b>The gradient.</b> From $F = ma$, $a = F \\times \\dfrac{1}{m}$, so the gradient of $a$ against $F$ is $\\dfrac{1}{m}$: the reciprocal of the total mass. "
                "A plot of $a$ against $m$ (force constant) is a curve, because $a = F \\div m$; to get a straight line, plot $a$ against $\\dfrac{1}{m}$.</p>"
            ),
        },
        {
            "kind": "worked",
            "title": "Acceleration from two light gates",
            "question": "A 10 cm card on a trolley takes 0.050 s to pass through the first light gate and 0.025 s to pass through the second. The trolley takes 0.4 s to travel between the gates. Calculate its acceleration.",
            "steps": [
                r"Card length $= 10 \text{ cm} = 0.10$ m.",
                r"$v_1 = \dfrac{0.10}{0.050} = 2.0$ m/s. $v_2 = \dfrac{0.10}{0.025} = 4.0$ m/s.",
                r"$a = \dfrac{v_2 - v_1}{t} = \dfrac{4.0 - 2.0}{0.4} = 5.0$ m/s².",
            ],
        },
        {
            "kind": "practice",
            "title": "Analysing the practical",
            "questions": [
                group("t2-t11-q1", "A trolley carries an 8 cm card. It takes 0.040 s to pass the first light gate and 0.020 s to pass the second, and 0.5 s to travel between the gates.", [
                    numeric("t2-t11-q1a", "Calculate the speed at the first gate.", sf(t11_1_v1), "m/s",
                            "8 cm = 0.08 m.",
                            ewau(LIGHT_EQ, r"v_1 = \dfrac{0.08}{0.040}", "2", "m/s"), label="a"),
                    numeric("t2-t11-q1b", "Calculate the speed at the second gate.", sf(t11_1_v2), "m/s",
                            "Same card, shorter time.",
                            ewau(LIGHT_EQ, r"v_2 = \dfrac{0.08}{0.020}", "4", "m/s"), label="b"),
                    numeric("t2-t11-q1c", "Calculate the acceleration of the trolley.", sf(t11_1_a), "m/s²",
                            "Change in velocity between the gates ÷ time between the gates.",
                            ewau(ACC_EQ, r"a = \dfrac{4 - 2}{0.5}", "4", "m/s²"), label="c"),
                ]),
                written("t2-t11-q2", "A student investigates how acceleration depends on force. Explain why she moves masses from the trolley onto the hanger, rather than adding new masses to the hanger.",
                        marks(["The hanging weight accelerates both the trolley and the hanging masses, because they are connected.",
                               "Adding new masses would increase the force and the total mass at the same time, so two variables would change.",
                               "Moving a mass from the trolley to the hanger increases the force but keeps the total accelerated mass constant — a fair test."]), lines=3),
                written("t2-t11-q3", "Describe how to compensate for friction before starting the experiment.",
                        marks(["Remove the hanging mass and give the trolley a gentle push.",
                               "Raise the end of the runway (tilt it) a little at a time,",
                               "until the trolley moves along it at a constant speed (the light gates can check this).",
                               "The component of the trolley's weight down the slope now balances friction, so the hanging weight is the resultant force."]), lines=4),
                group("t2-t11-q4", "The graph shows another student's results for acceleration against force, with the total mass kept constant. She did not compensate for friction.", [
                    numeric("t2-t11-q4a", "Calculate the gradient of the line.", sf(t11_g_grad), "m/s² per N",
                            "Use the points X (0.5, 0) and Y (3, 5).",
                            ewau(GRAD_EQ, r"\text{gradient} = \dfrac{5 - 0}{3 - 0.5} = \dfrac{5}{2.5}", "2", "m/s² per N (or kg⁻¹)"), label="a"),
                    numeric("t2-t11-q4b", "Use the gradient to find the total mass of the trolley and hanging masses.", sf(t11_g_mass), "kg",
                            "Gradient = 1 ÷ mass.",
                            [r"$a = \dfrac{1}{m} \times F$, so $\text{gradient} = \dfrac{1}{m}$.", r"$m = \dfrac{1}{2} = 0.5$ kg."], label="b"),
                    choice("t2-t11-q4c", "What does the intercept on the force axis (0.5 N at X) tell you?",
                           ["The mass of the trolley", "The friction force on the trolley", "The acceleration due to gravity", "A mistake in the plotting"], 1,
                           "The trolley does not accelerate until the force exceeds 0.5 N — that is the friction that has to be overcome first. A compensated runway would move the line to pass through the origin.", label="c"),
                ], graph=graph_t11),
                choice("t2-t11-q5", "A student plots acceleration against mass with the force kept constant. What shape of graph should she expect?",
                       ["A straight line through the origin", "A curve, because a = F ÷ m", "A horizontal line", "A straight line with a positive intercept"], 1,
                       "With F constant, a is inversely proportional to m — a curve that falls as m increases. Plotting a against 1/m gives a straight line through the origin."),
            ],
        },
    ],
}


# =====================================================================
# T12 · Measuring reaction time (2.27)
# =====================================================================

t12_w = sqrt(2 * 0.20 / G)
t12_1 = sqrt(2 * 0.45 / G)
t12_2 = 0.5 * G * 0.25 ** 2 * 100  # in cm

section_t12 = {
    "id": "reaction-time",
    "band": "tricky",
    "lessons": "2.27",
    "title": "Measuring reaction time",
    "blurb": "The ruler-drop test and the computer test: how each works, the maths that turns a drop distance into a time, and why neither is quite the same as reacting while driving.",
    "equations": [DROP_EQ, TREACT_EQ],
    "checklist": [
        "Describe the ruler-drop and computer-click methods of measuring reaction time",
        "Convert a ruler-drop distance into a reaction time using x = ½gt²",
        "Evaluate the methods: repeats, anticipation, and the difference from a real driving situation",
    ],
    "parts": [
        {
            "kind": "explain",
            "title": "Two methods",
            "html": (
                "<table class='tbl'><tr><th>Ruler drop</th><th>Computer test</th></tr>"
                "<tr><td>A partner holds a ruler vertically with the zero level with your open thumb and finger. Without warning they let go; you catch it as quickly as you can. "
                "Read the distance it fell. Repeat several times and take a mean.</td>"
                "<td>A program shows a signal (a colour change, a sound) at a random moment; you click or press a key as fast as you can. The computer records the time directly, in milliseconds. "
                "Repeat and take a mean.</td></tr>"
                "<tr><td>Gives a <b>distance</b>; you convert it to a time.</td><td>Gives the <b>time</b> directly, more precisely.</td></tr></table>"
                "<p><b>Converting the drop distance.</b> The ruler falls freely from rest, so with $u = 0$ and $a = g$:</p>"
                "$$" + DROP_EQ + r"\qquad\Rightarrow\qquad " + TREACT_EQ + "$$"
                "<p>Use the distance in <b>metres</b>. A 20 cm drop gives $t = \\sqrt{2 \\times 0.2 \\div 10} = 0.2$ s. (Edexcel do not require you to derive this; they do expect you to use it.)</p>"
                "<p><b>Evaluating.</b> Repeating and averaging reduces random error. Problems: the catcher may <b>anticipate</b> the drop (so the partner must vary the timing); "
                "the catching reaction uses the hand, whereas a driver's foot has further to move to the brake, so <b>real braking reaction times are longer</b>; "
                "and a test done when alert does not show the effect of tiredness, alcohol or distraction. Typical results: 0.2–0.3 s for a hand catch; 0.5–0.9 s for a driver.</p>"
            ),
        },
        {
            "kind": "worked",
            "title": "Reaction time from a ruler drop",
            "question": "A student catches a dropped ruler after it has fallen 20 cm. Calculate her reaction time. (g = 10 m/s².)",
            "steps": [
                r"Convert: $20 \text{ cm} = 0.20$ m.",
                r"$x = \tfrac{1}{2} g t^2$, so $t^2 = \dfrac{2x}{g} = \dfrac{2 \times 0.20}{10} = 0.04$.",
                r"$t = \sqrt{0.04} = 0.2$ s.",
            ],
        },
        {
            "kind": "practice",
            "title": "Reaction time",
            "questions": [
                numeric("t2-t12-q1", "A ruler falls 45 cm before it is caught. Calculate the reaction time.", sf(t12_1), "s",
                        "45 cm = 0.45 m; t = √(2x ÷ g).",
                        [r"$t^2 = \dfrac{2 \times 0.45}{10} = 0.09$.", r"$t = \sqrt{0.09} = 0.3$ s."]),
                numeric("t2-t12-q2", "A student's reaction time is 0.25 s. How far, in cm, will a ruler fall before she catches it?", 31.25, "cm",
                        "x = ½gt², then convert metres to centimetres.",
                        [r"$x = \tfrac{1}{2} \times 10 \times 0.25^2 = 5 \times 0.0625 = 0.3125$ m.", r"$0.3125 \text{ m} = 31$ cm (to 2 s.f.)."]),
                written("t2-t12-q3", "Explain why the ruler-drop test should be repeated several times and a mean taken.",
                        marks(["Reaction time varies from one attempt to the next (random variation).",
                               "Repeating and averaging reduces the effect of this random error and makes the result more reliable.",
                               "Any anomalous result (e.g. an anticipated catch) can be spotted and left out."]), lines=3),
                choice("t2-t12-q4", "Which is an advantage of the computer test over the ruler drop?",
                       ["It measures the time directly and more precisely", "It uses a longer reaction time", "It does not need repeating", "It measures the driver's braking time exactly"], 0,
                       "The computer times the response in milliseconds with no conversion needed. It still needs repeats, and it is still a hand response, not a foot-on-brake response."),
                choice("t2-t12-q5", "In a ruler-drop test, student A catches the ruler at 15 cm and student B at 30 cm. Which statement is correct?",
                       ["A has the slower reaction time", "B has the slower reaction time", "They have the same reaction time", "B's reaction time is exactly twice A's"], 1,
                       "A longer drop means the ruler fell for longer before it was caught — a slower reaction. Because x ∝ t², doubling the distance makes the time √2 ≈ 1.4 times longer, not twice."),
                written("t2-t12-q6", "Give two reasons why a reaction time measured by the ruler-drop test may not be the same as a driver's reaction time on the road.",
                        marks(["The catcher may anticipate the drop, giving an unrealistically short time.",
                               "A driver must move a foot to the brake pedal, which takes longer than closing a hand.",
                               "The test is done while alert and expecting a signal; a real driver may be tired, distracted or not expecting a hazard.",
                               "(Any two.)"]), lines=3),
            ],
        },
    ],
}


# =====================================================================
# T13 · Estimation (2.13, 2.31)
# =====================================================================

t13_w_a = 13 / 0.1
t13_w_f = 70 * t13_w_a
t13_1 = 13 / 5
t13_2 = 60 * (10 / 0.5)
t13_5 = 10 / 2
t13_6 = 13 * 0.7

section_t13 = {
    "id": "estimation",
    "band": "tricky",
    "lessons": "2.13, 2.31",
    "title": "Estimation questions",
    "blurb": "\"Estimate the force on…\" means: choose sensible values, say what you chose, calculate, and round. The method earns most of the marks.",
    "equations": [F_EQ, ACC_EQ],
    "checklist": [
        "Estimate the size of an everyday acceleration",
        "Estimate the force in a typical road situation, stating the values you assume",
        "Give an estimate to one or two significant figures with a unit",
    ],
    "parts": [
        {
            "kind": "explain",
            "title": "How to answer an estimation question",
            "html": (
                "<p>An estimation question is marked on your <b>method and sensible values</b>, not on hitting one exact number. The examiner wants to see:</p>"
                "<ol class='list'><li><b>Assumed values</b>, written down with units — a mass, a speed, a time or distance. Use the typical values from the non-negotiables.</li>"
                "<li>The <b>equations</b> you are using.</li>"
                "<li>The <b>calculation</b>, to 1 or 2 significant figures.</li>"
                "<li>A <b>sense check</b>: compare the force with a weight, or the acceleration with $g$.</li></ol>"
                "<table class='tbl'><tr><th>Useful assumed values</th><th></th></tr>"
                "<tr><td>Mass of an adult</td><td>70 kg</td></tr>"
                "<tr><td>Mass of a car</td><td>1000–1500 kg</td></tr>"
                "<tr><td>Town speed (30 mph)</td><td>13 m/s</td></tr>"
                "<tr><td>Motorway speed (70 mph)</td><td>30 m/s</td></tr>"
                "<tr><td>Time for a car to pull away to 30 mph</td><td>about 5 s</td></tr>"
                "<tr><td>Time to stop in a crash</td><td>about 0.1 s (0.5 s with a crumple zone)</td></tr>"
                "<tr><td>Driver's reaction time</td><td>0.7 s</td></tr></table>"
                "<p>Any answer within a factor of two or so of the examiner's will be accepted <i>if your assumptions are stated and sensible</i>. An unexplained number on its own is not.</p>"
            ),
        },
        {
            "kind": "worked",
            "title": "Estimating a crash force",
            "question": "Estimate the force on a driver when a car travelling in town crashes into a wall.",
            "steps": [
                r"<b>Assume:</b> driver's mass $\approx 70$ kg; town speed $\approx 13$ m/s (30 mph); the driver stops in about $0.1$ s.",
                r"Deceleration: $a = \dfrac{13 - 0}{0.1} = 130$ m/s² (13 times $g$).",
                r"Force: $F = m \times a = 70 \times 130 \approx 9000$ N.",
                r"<b>Sense check:</b> about 13 times the driver's weight (700 N) — easily enough to cause serious injury, which is why cars have crumple zones and airbags.",
            ],
        },
        {
            "kind": "practice",
            "title": "Estimation",
            "intro": "Answers within about 20% of the model values are accepted — the method matters more than the exact number.",
            "questions": [
                numeric("t2-t13-q1", "Estimate the acceleration of a car pulling away from traffic lights and reaching the 30 mph limit.", sf(t13_1, 2), "m/s²",
                        "30 mph is about 13 m/s; a car takes roughly 5 s to get there.",
                        [r"Assume $v = 13$ m/s reached in $t = 5$ s from rest.", r"$a = \dfrac{13}{5} \approx 2.6$ m/s² — a few m/s², well under $g$."], tolerance=0.3),
                numeric("t2-t13-q2", "Estimate the force on a 60 kg bus passenger when the bus brakes sharply from 10 m/s to rest in 0.5 s.", sf(t13_2, 2), "N",
                        "Deceleration first, then F = ma.",
                        [r"$a = \dfrac{10}{0.5} = 20$ m/s².", r"$F = 60 \times 20 = 1200$ N — about twice her weight, which is why standing passengers get thrown forwards."], tolerance=0.2),
                choice("t2-t13-q3", "Which is the best estimate of the force on a 1000 kg car during a motorway crash lasting 0.1 s?",
                       ["300 N", "3000 N", "300 000 N", "30 000 000 N"], 2,
                       "a ≈ 30 ÷ 0.1 = 300 m/s², so F ≈ 1000 × 300 = 300 000 N. Thirty times the weight of the car."),
                written("t2-t13-q4", "Describe how you would estimate the force on a cyclist who rides into a wall.",
                        marks(["Assume sensible values: the cyclist's mass (about 70 kg) and a typical cycling speed (about 6 m/s).",
                               "Assume a stopping time (around 0.1 s) or a stopping distance.",
                               "Calculate the deceleration from a = (v − u) ÷ t (or v² = 2ax), then the force from F = ma.",
                               "State the answer to 1 or 2 significant figures and compare it with the cyclist's weight."]), lines=4),
                numeric("t2-t13-q5", "A sprinter crosses the finish line at 10 m/s and comes to a stop in about 2 s. Estimate her deceleration.", sf(t13_5, 2), "m/s²",
                        "Change in speed ÷ time.",
                        [r"$a = \dfrac{10 - 0}{2} = 5$ m/s² — about half of $g$."], tolerance=0.3),
                numeric("t2-t13-q6", "Estimate the thinking distance of a car travelling at 30 mph in town.", sf(t13_6, 2), "m",
                        "30 mph ≈ 13 m/s; a typical reaction time is about 0.7 s.",
                        [r"Thinking distance $= 13 \times 0.7 \approx 9$ m — matching the Highway Code's 9 m."], tolerance=0.3),
            ],
        },
    ],
}


# =====================================================================
# Key facts — flip cards: (question, answer, section id)
# =====================================================================

key_facts = [
    ("Scalar or vector: velocity?", "Vector (speed in a stated direction)", "scalars-vectors"),
    ("Scalar or vector: mass? weight?", "Mass is a scalar; weight is a vector", "scalars-vectors"),
    ("Scalar or vector: momentum? energy?", "Momentum is a vector; energy is a scalar", "scalars-vectors"),
    ("Speed equation (symbols)?", r"$v = \dfrac{x}{t}$", "speed"),
    ("Convert km/h to m/s?", "Divide by 3.6 (×1000 ÷ 3600)", "speed"),
    ("Acceleration equation?", r"$a = \dfrac{v - u}{t}$", "acceleration"),
    ("Equation with no time in it?", r"$v^2 - u^2 = 2ax$", "suvat"),
    ("Gradient of a distance–time graph gives…", "Speed", "dt-graphs"),
    ("Gradient of a velocity–time graph gives…", "Acceleration", "vt-graphs"),
    ("Area under a velocity–time graph gives…", "Distance travelled", "vt-graphs"),
    ("Instantaneous speed on a curved graph?", "Gradient of the tangent at that point", "curved-graphs"),
    ("Value of g?", "10 m/s² (or 10 N/kg)", "typical-speeds"),
    ("Typical speeds: walking, cycling, sound?", "1.5 m/s, 6 m/s, 340 m/s", "typical-speeds"),
    ("Newton's first law?", "Zero resultant force → stays at rest or at constant velocity", "newton-first"),
    ("Newton's second law?", r"$F = m \times a$ (F is the resultant force)", "f-ma"),
    ("Newton's third law?", "A on B is equal and opposite to B on A — same type, different objects", "newton-third"),
    ("Weight equation?", r"$W = m \times g$", "weight"),
    ("How is weight measured?", "With a newtonmeter (calibrated spring balance)", "weight"),
    ("Why does an object in a circle at constant speed accelerate?", "Its direction, and so its velocity, is changing", "circular-motion"),
    ("Direction of the centripetal force?", "Towards the centre of the circle", "circular-motion"),
    ("Inertial mass is defined as…", r"The ratio $F \div a$: how hard it is to change velocity", "inertial-mass"),
    ("Momentum equation and unit?", r"$p = m \times v$, kg m/s", "momentum"),
    ("Conservation of momentum?", "Total momentum before = total after, if no external force", "conservation-momentum"),
    ("Force from momentum?", r"$F = \dfrac{mv - mu}{t}$", "force-momentum"),
    ("How do airbags reduce injury?", "Same momentum change, longer time, smaller force", "force-momentum"),
    ("Stopping distance =", "Thinking distance + braking distance", "stopping-distance"),
    ("Factors affecting thinking distance?", "Speed, and reaction time (tiredness, alcohol, drugs, distractions)", "stopping-distance"),
    ("Factors affecting braking distance?", "Speed, mass, brakes, tyres, road surface (friction)", "stopping-distance"),
    ("Typical human reaction time?", "0.2–0.9 s", "reaction-time"),
    ("Double the speed: thinking and braking distances?", "Thinking ×2, braking ×4", "braking-v-squared"),
    ("Why is braking distance ∝ v²?", r"Work done by brakes $F d$ = KE $\tfrac{1}{2}mv^2$", "braking-v-squared"),
    ("Core practical: why move masses from trolley to hanger?", "To change the force while keeping the total mass constant", "core-practical-analysis"),
    ("Ruler drop: distance to time?", r"$t = \sqrt{2x \div g}$", "reaction-time"),
]

section_facts = {
    "id": "key-facts",
    "band": "tricky",
    "lessons": "Whole topic",
    "title": "Key facts",
    "blurb": "Cover and test yourself: tap a card to flip it, or cover the right-hand column on the printout.",
    "equations": [],
    "checklist": [],
    "parts": [
        {
            "kind": "facts",
            "title": "Cover and test yourself",
            # Each card carries the id of the section it belongs to, so that a hidden
    # section (see the build script) also hides its cards
    "items": [{"q": question, "a": answer, "section": section_id} for question, answer, section_id in key_facts],
        }
    ],
}


SECTIONS = [section_t8, section_t9, section_t10, section_t11, section_t12, section_t13]
