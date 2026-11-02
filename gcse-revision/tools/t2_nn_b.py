"""
t2_nn_b.py — The non-negotiables, sections N9–N15.

Newton's first law and resultant force; F = ma; weight; the core
practical (method); Newton's third law; momentum; stopping distances.
"""

from t2lib import choice, ewau, group, marks, numeric, sf, written

# ---------------------------------------------------------------------
# Equations
# ---------------------------------------------------------------------

F_EQ = r"F = m \times a"
A_EQ = r"a = \dfrac{F}{m}"
M_EQ = r"m = \dfrac{F}{a}"
ACC_EQ = r"a = \dfrac{v - u}{t}"
W_EQ = r"W = m \times g"
MW_EQ = r"m = \dfrac{W}{g}"
GW_EQ = r"g = \dfrac{W}{m}"
P_EQ = r"p = m \times v"
V_EQ = r"v = \dfrac{p}{m}"
MP_EQ = r"m = \dfrac{p}{v}"
STOP_EQ = r"\text{stopping distance} = \text{thinking distance} + \text{braking distance}"
THINK_EQ = r"\text{thinking distance} = \text{speed} \times \text{reaction time}"
RES_EQ = r"\text{resultant force} = \text{forces one way} - \text{forces the other way}"

G = 10


# =====================================================================
# N9 · Newton's first law and resultant force (2.14)
# =====================================================================

q9_1 = 450 - 300
q9_3 = 2000 - 1500

section_n9 = {
    "id": "newton-first",
    "band": "nn",
    "lessons": "2.14",
    "title": "Newton's first law and resultant force",
    "blurb": "Find the resultant of forces along a line, then say what it does: zero resultant keeps the motion as it is; a non-zero resultant changes it.",
    "equations": [RES_EQ],
    "checklist": [
        "State Newton's first law",
        "Calculate a resultant force from two forces along a line",
        "Say what happens when the resultant force is zero, and when it is not",
    ],
    "parts": [
        {
            "kind": "explain",
            "title": "Resultant force and what it does",
            "html": (
                "<p>The <b>resultant force</b> is the single force that would have the same effect as all the forces acting together. "
                "For forces along one line: add the ones pointing the same way, subtract the ones pointing the opposite way.</p>"
                "<p><b>Newton's first law:</b> an object stays at rest, or keeps moving at a <b>constant velocity</b> (same speed, same direction), "
                "unless a <b>resultant force</b> acts on it.</p>"
                "<table class='tbl'><tr><th>Resultant force</th><th>What happens</th></tr>"
                "<tr><td>Zero (forces balanced)</td><td>Stationary object stays still; moving object keeps the same velocity</td></tr>"
                "<tr><td>Not zero, same direction as motion</td><td>Speeds up</td></tr>"
                "<tr><td>Not zero, opposite to motion</td><td>Slows down</td></tr>"
                "<tr><td>Not zero, at an angle to motion</td><td>Changes direction (see circular motion)</td></tr></table>"
                "<p><b>The common mistake:</b> thinking a moving object needs a force to keep it moving. It does not. "
                "A car at a steady 20 m/s has a driving force exactly balanced by friction and air resistance — the resultant is zero.</p>"
            ),
        },
        {
            "kind": "worked",
            "title": "Resultant force on a car",
            "question": "A car's engine provides a forward force of 3000 N. Friction and air resistance total 2200 N. (a) Calculate the resultant force. (b) Describe the car's motion. (c) Air resistance increases until the backward forces total 3000 N. Describe the motion now.",
            "steps": [
                r"<b>(a)</b> $\text{resultant} = 3000 - 2200 = 800$ N, forwards.",
                r"<b>(b)</b> The resultant is not zero and is in the direction of motion, so the car accelerates (speeds up).",
                r"<b>(c)</b> Now $\text{resultant} = 3000 - 3000 = 0$ N. The forces are balanced, so by Newton's first law the car continues at a constant velocity.",
                r"It does <i>not</i> stop — a zero resultant force means no <i>change</i> in motion.",
            ],
        },
        {
            "kind": "practice",
            "title": "Resultant forces",
            "questions": [
                numeric("t2-n9-q1", "A sledge is pulled forwards with a force of 450 N while friction of 300 N acts backwards. Calculate the resultant force.", q9_1, "N",
                        "Subtract the backward force from the forward force.",
                        ewau(RES_EQ, r"\text{resultant} = 450 - 300", "150", "N forwards")),
                choice("t2-n9-q2", "A parachutist is falling at a constant velocity. What can you say about the forces on her?",
                       ["Her weight is bigger than the air resistance", "The air resistance is bigger than her weight",
                        "Her weight and the air resistance are equal in size", "There is no air resistance"], 2,
                       "Constant velocity means zero resultant force (Newton's first law), so the upward air resistance exactly balances her weight."),
                numeric("t2-n9-q3", "A helicopter's rotor provides 2000 N of lift. The helicopter weighs 1500 N. Calculate the resultant force.", q9_3, "N",
                        "Up minus down.",
                        ewau(RES_EQ, r"\text{resultant} = 2000 - 1500", "500", "N upwards")
                        + ["The helicopter accelerates upwards."]),
                numeric("t2-n9-q4", "A boat's engine pushes it forwards with 5000 N. The water resistance is also 5000 N. State the resultant force on the boat.", 0, "N",
                        "The forces are equal and opposite.",
                        [r"$\text{resultant} = 5000 - 5000 = 0$ N.", "The boat continues at a constant velocity."]),
                written("t2-n9-q5", "State Newton's first law of motion.",
                        marks(["An object at rest stays at rest, and a moving object continues at a constant velocity (constant speed in a straight line),",
                               "unless a resultant force acts on it."]), lines=2),
                choice("t2-n9-q6", "An ice puck slides at 8 m/s across perfectly smooth ice with no resultant force on it. What happens to it?",
                       ["It slows down and stops", "It keeps moving at 8 m/s in a straight line", "It speeds up", "It changes direction"], 1,
                       "No resultant force means no change in velocity. It carries on at 8 m/s until something pushes on it."),
            ],
        },
    ],
}


# =====================================================================
# N10 · F = ma (2.15)
# =====================================================================

q10_w = 3000 / 1200
q10_1 = 10 / 2
q10_2 = 800 * 2
q10_3 = 60 / 4
q10_4 = 2 / 0.5
q10_5 = 2500 / 1000
q10_6a = (8 - 0) / 2
q10_6b = 70 * q10_6a

section_n10 = {
    "id": "f-ma",
    "band": "nn",
    "lessons": "2.15",
    "title": "Newton's second law: F = ma",
    "blurb": "Resultant force, mass and acceleration — with the unit conversions (grams, kilonewtons) and one two-step question.",
    "equations": [F_EQ],
    "checklist": [
        "Use F = ma and rearrange it for m or a",
        "Convert grams to kilograms and kN to N before substituting",
        "Remember that F is the resultant force",
    ],
    "parts": [
        {
            "kind": "explain",
            "title": "Force, mass and acceleration",
            "html": (
                "$$" + F_EQ + "$$"
                "<p>$F$ is the <b>resultant</b> force in newtons, $m$ the mass in <b>kilograms</b>, $a$ the acceleration in m/s². "
                "A bigger force gives a bigger acceleration; a bigger mass gives a smaller acceleration for the same force.</p>"
                "<table class='tbl'><tr><th>To find…</th><th>Use…</th></tr>"
                "<tr><td>force</td><td>$" + F_EQ + "$</td></tr>"
                "<tr><td>acceleration</td><td>$" + A_EQ + "$</td></tr>"
                "<tr><td>mass</td><td>$" + M_EQ + "$</td></tr></table>"
                "<p><b>Units:</b> 500 g = 0.5 kg; 2.5 kN = 2500 N; 1 tonne = 1000 kg. Convert before you substitute.</p>"
                "<p>If a question gives two forces, find the resultant first (the tricky bits cover this), then use $F = ma$ with the resultant.</p>"
            ),
        },
        {
            "kind": "worked",
            "title": "Finding an acceleration",
            "question": "A car of mass 1200 kg experiences a resultant force of 3000 N. Calculate its acceleration.",
            "steps": ewau(A_EQ, r"a = \dfrac{3000}{1200}", "2.5", "m/s²"),
        },
        {
            "kind": "practice",
            "title": "F = ma",
            "questions": [
                numeric("t2-n10-q1", "A resultant force of 10 N acts on a 2 kg trolley. Calculate its acceleration.", sf(q10_1), "m/s²",
                        "a = F ÷ m.",
                        ewau(A_EQ, r"a = \dfrac{10}{2}", "5", "m/s²")),
                numeric("t2-n10-q2", "A car of mass 800 kg accelerates at 2 m/s². Calculate the resultant force on it.", sf(q10_2), "N",
                        "Multiply mass by acceleration.",
                        ewau(F_EQ, r"F = 800 \times 2", "1600", "N")),
                numeric("t2-n10-q3", "A resultant force of 60 N gives a box an acceleration of 4 m/s². Calculate the mass of the box.", sf(q10_3), "kg",
                        "m = F ÷ a.",
                        ewau(M_EQ, r"m = \dfrac{60}{4}", "15", "kg")),
                numeric("t2-n10-q4", "A resultant force of 2 N acts on a 500 g model car. Calculate its acceleration.", sf(q10_4), "m/s²",
                        "Convert 500 g to kilograms first.",
                        [r"$500 \text{ g} = 0.5$ kg."] + ewau(A_EQ, r"a = \dfrac{2}{0.5}", "4", "m/s²")),
                numeric("t2-n10-q5", "A resultant force of 2.5 kN acts on a 1000 kg van. Calculate its acceleration.", sf(q10_5), "m/s²",
                        "2.5 kN = 2500 N.",
                        [r"$2.5 \text{ kN} = 2500$ N."] + ewau(A_EQ, r"a = \dfrac{2500}{1000}", "2.5", "m/s²")),
                group("t2-n10-q6", "A 70 kg sprinter accelerates from rest to 8 m/s in 2 s.", [
                    numeric("t2-n10-q6a", "Calculate the sprinter's acceleration.", sf(q10_6a), "m/s²",
                            "Change in velocity ÷ time.",
                            ewau(ACC_EQ, r"a = \dfrac{8 - 0}{2}", "4", "m/s²"), label="a"),
                    numeric("t2-n10-q6b", "Calculate the resultant force on the sprinter.", sf(q10_6b), "N",
                            "Use the acceleration you just found in F = ma.",
                            ewau(F_EQ, r"F = 70 \times 4", "280", "N"), label="b"),
                ]),
            ],
        },
    ],
}


# =====================================================================
# N11 · Weight, mass and gravitational field strength (2.16–2.18)
# =====================================================================

G_MOON = 1.6
G_MARS = 3.7
q11_w1 = 60 * G
q11_w2 = 60 * G_MOON
q11_1 = 12 * G
q11_2 = 350 / G
q11_3 = 50 * G_MARS
q11_4 = 125 / 5

section_n11 = {
    "id": "weight",
    "band": "nn",
    "lessons": "2.16–2.18",
    "title": "Weight, mass and g",
    "blurb": "Weight is a force; mass is not. W = mg links them through the gravitational field strength, which is different on different planets.",
    "equations": [W_EQ],
    "checklist": [
        "Define weight and use W = mg",
        "Explain the difference between mass and weight",
        "Describe how weight is measured",
        "Describe how weight depends on gravitational field strength",
    ],
    "parts": [
        {
            "kind": "explain",
            "title": "Mass is not weight",
            "html": (
                "<table class='tbl'><tr><th></th><th>Mass</th><th>Weight</th></tr>"
                "<tr><td>What it is</td><td>The amount of matter in an object</td><td>The <b>force</b> of gravity pulling the object towards the Earth (or planet)</td></tr>"
                "<tr><td>Unit</td><td>kilograms, kg</td><td>newtons, N</td></tr>"
                "<tr><td>Scalar or vector?</td><td>Scalar</td><td>Vector — it acts downwards, towards the centre of the planet</td></tr>"
                "<tr><td>On the Moon…</td><td>Same as on Earth</td><td>About one sixth of the Earth value</td></tr>"
                "<tr><td>Measured with</td><td>A balance (compares against known masses)</td><td>A newtonmeter (a calibrated spring balance)</td></tr></table>"
                "$$" + W_EQ + "$$"
                "<p>$g$ is the <b>gravitational field strength</b>, in N/kg: the force of gravity on each kilogram. "
                "On Earth $g = 10$ N/kg. (The same number as the acceleration of free fall, 10 m/s² — not a coincidence.)</p>"
                "<table class='tbl'><tr><th>Place</th><th>$g$ / N/kg</th></tr>"
                "<tr><td>Earth</td><td>10</td></tr><tr><td>Moon</td><td>1.6</td></tr><tr><td>Mars</td><td>3.7</td></tr><tr><td>Jupiter</td><td>25</td></tr></table>"
                "<p><b>Weight is directly proportional to $g$.</b> Take the same mass somewhere with twice the field strength and it weighs twice as much.</p>"
            ),
        },
        {
            "kind": "worked",
            "title": "Weight on Earth and on the Moon",
            "question": "An astronaut has a mass of 60 kg. Calculate her weight (a) on Earth (g = 10 N/kg) and (b) on the Moon (g = 1.6 N/kg).",
            "steps": [
                r"<b>(a)</b> $W = m \times g = 60 \times 10 = 600$ N.",
                r"<b>(b)</b> Her mass is still 60 kg on the Moon. $W = 60 \times 1.6 = 96$ N.",
                r"Her weight on the Moon is 96 N, about one sixth of 600 N, because $g$ is about one sixth as big.",
            ],
        },
        {
            "kind": "practice",
            "title": "Weight and mass",
            "questions": [
                numeric("t2-n11-q1", "Calculate the weight of a 12 kg suitcase on Earth.", sf(q11_1), "N",
                        "W = mg with g = 10 N/kg.",
                        ewau(W_EQ, r"W = 12 \times 10", "120", "N")),
                numeric("t2-n11-q2", "A person weighs 350 N on Earth. Calculate their mass.", sf(q11_2), "kg",
                        "Rearrange: m = W ÷ g.",
                        ewau(MW_EQ, r"m = \dfrac{350}{10}", "35", "kg")),
                numeric("t2-n11-q3", "A 50 kg rover lands on Mars, where g = 3.7 N/kg. Calculate its weight on Mars.", sf(q11_3), "N",
                        "Use the Mars value of g, not 10.",
                        ewau(W_EQ, r"W = 50 \times 3.7", "185", "N")),
                numeric("t2-n11-q4", "A 5 kg mass weighs 125 N on a certain planet. Calculate the planet's gravitational field strength.", sf(q11_4), "N/kg",
                        "g = W ÷ m.",
                        ewau(GW_EQ, r"g = \dfrac{125}{5}", "25", "N/kg")
                        + ["That is Jupiter's value."]),
                choice("t2-n11-q5", "An astronaut travels from the Earth to the Moon. What happens to her mass?",
                       ["It decreases to about one sixth", "It stays the same", "It increases", "It becomes zero"], 1,
                       "Mass is the amount of matter in her body — it does not depend on where she is. Her <i>weight</i> falls to about one sixth."),
                written("t2-n11-q6", "Describe how the weight of an object can be measured.",
                        marks(["Hang the object from a newtonmeter (a calibrated spring balance) and read the force in newtons directly.",
                               "Or: measure the mass on a balance, then calculate W = m × g."]), lines=2),
            ],
        },
    ],
}


# =====================================================================
# N12 · Core practical: force, mass and acceleration (2.19)
# =====================================================================

q12_w_f = 0.1 * G
q12_w_a = q12_w_f / 1.2
q12_1 = 0.2 * G
q12_2 = q12_1 / 0.8

section_n12 = {
    "id": "core-practical",
    "band": "nn",
    "lessons": "2.19",
    "title": "Core practical: force, mass and acceleration",
    "blurb": "The method you must be able to describe: a trolley, a string over a pulley, hanging masses, light gates. The analysis is in the tricky bits.",
    "equations": [F_EQ],
    "checklist": [
        "Describe the equipment and method of the trolley core practical",
        "Name the independent, dependent and control variables",
        "Calculate the accelerating force from the hanging mass",
    ],
    "parts": [
        {
            "kind": "explain",
            "title": "The method",
            "html": (
                "<p><b>Aim:</b> investigate how the acceleration of a trolley depends on the force applied and on its mass.</p>"
                "<p><b>Set-up:</b> a trolley on a runway (bench or ramp); a string from the trolley over a pulley at the end of the bench to a <b>mass hanger</b>; "
                "a card on the trolley and two <b>light gates</b> connected to a data logger; a set of slotted masses.</p>"
                "<table class='tbl'><tr><th>Step</th><th>Detail</th></tr>"
                "<tr><td>1</td><td>Measure the length of the card. Measure the distance between the light gates.</td></tr>"
                "<tr><td>2</td><td>Hang a mass on the hanger. The weight of the hanging mass is the force pulling the trolley: $F = m \\times g$.</td></tr>"
                "<tr><td>3</td><td>Release the trolley from the same starting point each time. The data logger records the speed at each gate and the time between them, and calculates the acceleration.</td></tr>"
                "<tr><td>4 (force)</td><td>Move one slotted mass <b>from the trolley to the hanger</b> and repeat, so the force changes but the <b>total mass</b> being accelerated stays the same.</td></tr>"
                "<tr><td>4 (mass)</td><td>Or: keep the hanging mass the same and add masses to the trolley, so the mass changes but the force stays the same.</td></tr>"
                "<tr><td>5</td><td>Repeat each reading three times and take a mean. Plot acceleration against force (or against mass).</td></tr></table>"
                "<table class='tbl'><tr><th>Investigating force</th><th>Investigating mass</th></tr>"
                "<tr><td><b>Independent:</b> force (hanging weight)</td><td><b>Independent:</b> total mass</td></tr>"
                "<tr><td><b>Dependent:</b> acceleration</td><td><b>Dependent:</b> acceleration</td></tr>"
                "<tr><td><b>Control:</b> total mass of trolley + hanger, same runway, same starting point</td><td><b>Control:</b> force (hanging mass), same runway, same starting point</td></tr></table>"
            ),
        },
        {
            "kind": "worked",
            "title": "The force from a hanging mass",
            "question": "In the experiment a 100 g mass hangs from the string. The trolley, card and hanging mass have a total mass of 1.2 kg. Calculate (a) the force accelerating the trolley and (b) the expected acceleration.",
            "steps": [
                r"<b>(a)</b> The force is the weight of the hanging mass. $100 \text{ g} = 0.1$ kg, so $F = 0.1 \times 10 = 1.0$ N.",
                r"<b>(b)</b> This force accelerates <i>everything</i> attached to the string: the trolley <i>and</i> the hanging mass, 1.2 kg in total.",
                r"$a = \dfrac{F}{m} = \dfrac{1.0}{1.2} = 0.83$ m/s² (to 2 s.f.).",
            ],
        },
        {
            "kind": "practice",
            "title": "The core practical",
            "questions": [
                numeric("t2-n12-q1", "A 200 g mass is hung from the string. Calculate the force pulling the trolley.", sf(q12_1), "N",
                        "Weight of the hanging mass: convert to kg, multiply by 10.",
                        [r"$200 \text{ g} = 0.2$ kg."] + ewau(W_EQ, r"F = 0.2 \times 10", "2", "N")),
                numeric("t2-n12-q2", "The total mass of the trolley and the hanging mass is 0.8 kg. Using the force from question 1, calculate the expected acceleration.", sf(q12_2), "m/s²",
                        "a = F ÷ (total mass).",
                        ewau(A_EQ, r"a = \dfrac{2}{0.8}", "2.5", "m/s²")),
                choice("t2-n12-q3", "A student investigates how acceleration depends on force. What is the <b>independent</b> variable?",
                       ["Acceleration", "Force", "Mass of the trolley", "Length of the card"], 1,
                       "The independent variable is the one the student deliberately changes — the force, by moving masses onto the hanger. Acceleration is the dependent variable."),
                choice("t2-n12-q4", "When investigating force, where should the extra masses come from when you increase the hanging mass?",
                       ["A separate box of masses", "The trolley", "Nowhere — just add them", "The pulley"], 1,
                       "Moving a mass from the trolley to the hanger increases the force while keeping the total accelerated mass constant. Adding masses from elsewhere would change two variables at once."),
                written("t2-n12-q5", "Describe how you would investigate the effect of force on the acceleration of a trolley.",
                        marks(["Trolley on a bench, string over a pulley to a mass hanger; card on the trolley; two light gates and a data logger.",
                               "The hanging weight provides the force (F = mg); the data logger measures the speed at each gate and the time between them, giving the acceleration.",
                               "Change the force by moving a slotted mass from the trolley to the hanger, so the total mass stays constant.",
                               "Repeat each force three times, take a mean, and plot acceleration against force."]), lines=5),
                choice("t2-n12-q6", "Which graph would you expect for acceleration against force (with the mass constant)?",
                       ["A straight line through the origin", "A curve that levels off", "A horizontal line", "A straight line with a negative gradient"], 0,
                       "F = ma means a is directly proportional to F: doubling the force doubles the acceleration, so the graph is a straight line through the origin. Its gradient is 1/m."),
            ],
        },
    ],
}


# =====================================================================
# N13 · Newton's third law (2.23)
# =====================================================================

section_n13 = {
    "id": "newton-third",
    "band": "nn",

    "lessons": "2.23",
    "title": "Newton's third law",
    "blurb": "Forces come in pairs: same size, opposite direction, same type, acting on different objects.",
    "equations": [],
    "checklist": [
        "State Newton's third law",
        "Identify the pair force for a given force (what acts on what)",
        "Give the four features of a third-law pair",
    ],
    "parts": [
        {
            "kind": "explain",
            "title": "Forces come in pairs",
            "html": (
                "<p><b>Newton's third law:</b> when object A exerts a force on object B, object B exerts a force on object A that is <b>equal in size and opposite in direction</b>.</p>"
                "<p>A third-law pair always has these four features — write all four in an exam:</p>"
                "<table class='tbl'><tr><th>Feature</th><th>Example: you push a wall with 50 N</th></tr>"
                "<tr><td>Same size</td><td>The wall pushes you with 50 N</td></tr>"
                "<tr><td>Opposite direction</td><td>You push east; the wall pushes you west</td></tr>"
                "<tr><td>Same type of force</td><td>Both are contact (push) forces</td></tr>"
                "<tr><td>Act on <b>different</b> objects</td><td>Your force acts on the wall; the wall's force acts on you</td></tr></table>"
                "<p>The quick way to find the partner: swap the two objects round. \"The Earth pulls the apple down\" pairs with \"the apple pulls the Earth up\". "
                "The Earth's acceleration is tiny because its mass is enormous, but the force is the same size.</p>"
            ),
        },
        {
            "kind": "worked",
            "title": "Finding the pair force",
            "question": "A book rests on a table. The table pushes up on the book with a contact force of 20 N. State the Newton's third law pair of this force.",
            "steps": [
                r"Swap the objects: the force is <i>table on book</i>, so the partner is <i>book on table</i>.",
                r"The book pushes <b>down</b> on the table with a contact force of <b>20 N</b>.",
                r"Check the four features: 20 N and 20 N (same size); up and down (opposite); both contact forces (same type); one acts on the book, the other on the table (different objects).",
                r"Note: the book's <i>weight</i> is NOT the partner of the table's push — weight acts on the book too, so they act on the same object. The tricky bits deal with this.",
            ],
        },
        {
            "kind": "practice",
            "title": "Newton's third law",
            "questions": [
                choice("t2-n13-q1", "The Earth pulls an apple downwards with a gravitational force of 1 N. What is the Newton's third law pair of this force?",
                       ["The table pushing the apple up with 1 N", "The apple pulling the Earth upwards with 1 N",
                        "The apple's weight", "Air resistance on the apple"], 1,
                       "Swap the objects: Earth-on-apple pairs with apple-on-Earth. Same size (1 N), opposite direction, both gravitational, acting on different objects."),
                choice("t2-n13-q2", "A swimmer pushes the water backwards with her hands. Which force makes her move forwards?",
                       ["Her weight", "The water pushing her forwards", "Upthrust", "Friction with the pool floor"], 1,
                       "By Newton's third law the water pushes back on her with an equal force in the opposite direction — forwards."),
                numeric("t2-n13-q3", "A rocket engine pushes exhaust gases downwards with a force of 5000 N. What size force do the gases exert on the rocket?", 5000, "N",
                        "Third-law pairs are equal in size.",
                        ["The gases push the rocket upwards with a force of 5000 N — equal in size, opposite in direction."]),
                written("t2-n13-q4", "State Newton's third law of motion.",
                        marks(["When one object exerts a force on a second object,",
                               "the second object exerts a force on the first that is equal in size and opposite in direction."]), lines=2),
                choice("t2-n13-q5", "Which of these is NOT a feature of a Newton's third law pair?",
                       ["The two forces are the same size", "The two forces are the same type", "The two forces act on the same object", "The two forces act in opposite directions"], 2,
                       "Pair forces always act on <i>different</i> objects. Two forces on the same object can balance, but they are never a third-law pair."),
                choice("t2-n13-q6", "A person leans against a wall with a force of 80 N. The wall does not move. Which statement is correct?",
                       ["The wall pushes back with less than 80 N because it does not move", "The wall pushes back with exactly 80 N",
                        "The wall pushes back with more than 80 N", "The wall exerts no force"], 1,
                       "Third-law pairs are always equal in size, whether or not anything moves. The wall does not move because the ground holds it in place — that is a separate force."),
            ],
        },
    ],
}


# =====================================================================
# N14 · Momentum (2.24)
# =====================================================================

q14_w = 1200 * 15
q14_1 = 0.5 * 20
q14_2 = 80 * 5
q14_3 = 4500 / 900
q14_4 = 60 / 4
q14_5 = 0.16 * 25
q14_6v = 72000 / 3600
q14_6 = 2000 * q14_6v

section_n14 = {
    "id": "momentum",
    "band": "nn",
    "lessons": "2.24",
    "title": "Momentum: p = mv",
    "blurb": "Mass times velocity, in kg m/s. A vector — so its direction matters, which is what makes collisions work in the tricky bits.",
    "equations": [P_EQ],
    "checklist": [
        "Define momentum and use p = mv",
        "Give the unit of momentum, kg m/s",
        "Rearrange to find a mass or a velocity",
    ],
    "parts": [
        {
            "kind": "explain",
            "title": "Momentum",
            "html": (
                "$$" + P_EQ + "$$"
                "<p><b>Momentum</b> $=$ mass $\\times$ velocity. The unit is <b>kg m/s</b> (kilogram metres per second). "
                "Momentum is a <b>vector</b>: it has the same direction as the velocity, so a car going north and an identical car going south have opposite momentum.</p>"
                "<p>Roughly, momentum measures how hard something is to stop: a slow lorry and a fast cricket ball can have similar momentum.</p>"
                "<table class='tbl'><tr><th>To find…</th><th>Use…</th></tr>"
                "<tr><td>momentum</td><td>$" + P_EQ + "$</td></tr>"
                "<tr><td>velocity</td><td>$" + V_EQ + "$</td></tr>"
                "<tr><td>mass</td><td>$" + MP_EQ + "$</td></tr></table>"
                "<p>Mass in <b>kg</b>, velocity in <b>m/s</b>. A stationary object has zero momentum.</p>"
            ),
        },
        {
            "kind": "worked",
            "title": "Calculating momentum",
            "question": "A car of mass 1200 kg travels at 15 m/s. Calculate its momentum.",
            "steps": ewau(P_EQ, r"p = 1200 \times 15", "18\\,000", "kg m/s"),
        },
        {
            "kind": "practice",
            "title": "Momentum",
            "questions": [
                numeric("t2-n14-q1", "Calculate the momentum of a 0.5 kg football kicked at 20 m/s.", sf(q14_1), "kg m/s",
                        "Mass times velocity.",
                        ewau(P_EQ, r"p = 0.5 \times 20", "10", "kg m/s")),
                numeric("t2-n14-q2", "An 80 kg rugby player runs at 5 m/s. Calculate his momentum.", sf(q14_2), "kg m/s",
                        "p = mv.",
                        ewau(P_EQ, r"p = 80 \times 5", "400", "kg m/s")),
                numeric("t2-n14-q3", "A 900 kg car has a momentum of 4500 kg m/s. Calculate its velocity.", sf(q14_3), "m/s",
                        "v = p ÷ m.",
                        ewau(V_EQ, r"v = \dfrac{4500}{900}", "5", "m/s")),
                numeric("t2-n14-q4", "An object moving at 4 m/s has a momentum of 60 kg m/s. Calculate its mass.", sf(q14_4), "kg",
                        "m = p ÷ v.",
                        ewau(MP_EQ, r"m = \dfrac{60}{4}", "15", "kg")),
                numeric("t2-n14-q5", "A 160 g cricket ball is bowled at 25 m/s. Calculate its momentum.", sf(q14_5), "kg m/s",
                        "160 g = 0.16 kg.",
                        [r"$160 \text{ g} = 0.16$ kg."] + ewau(P_EQ, r"p = 0.16 \times 25", "4", "kg m/s")),
                numeric("t2-n14-q6", "A 2000 kg van travels at 72 km/h. Calculate its momentum in kg m/s.", sf(q14_6), "kg m/s",
                        "Convert 72 km/h to m/s first (divide by 3.6).",
                        [r"$72 \text{ km/h} = \dfrac{72\,000}{3600} = 20$ m/s."] + ewau(P_EQ, r"p = 2000 \times 20", "40\\,000", "kg m/s")),
            ],
        },
    ],
}


# =====================================================================
# N15 · Stopping distances and reaction time (2.27–2.30)
# =====================================================================

q15_w_think = 20 * 0.7
q15_w_stop = q15_w_think + 30
q15_1 = 15 * 0.6
q15_2 = q15_1 + 21
q15_6 = 60 - 18

section_n15 = {
    "id": "stopping-distance",
    "band": "nn",
    "lessons": "2.27–2.30",
    "title": "Stopping distances and reaction time",
    "blurb": "Stopping = thinking + braking. Which factors change which part, and the typical human reaction time.",
    "equations": [STOP_EQ, THINK_EQ],
    "checklist": [
        "Recall that stopping distance = thinking distance + braking distance",
        "List the factors that affect thinking distance and those that affect braking distance",
        "Recall a typical human reaction time (0.2–0.9 s)",
        "Calculate a thinking distance from speed and reaction time",
    ],
    "parts": [
        {
            "kind": "explain",
            "title": "Thinking distance and braking distance",
            "html": (
                "$$" + STOP_EQ + "$$"
                "<table class='tbl'><tr><th></th><th>Thinking distance</th><th>Braking distance</th></tr>"
                "<tr><td>What it is</td><td>Distance travelled <b>during the driver's reaction time</b>, before the brakes are touched</td>"
                "<td>Distance travelled <b>while the brakes are on</b>, until the car stops</td></tr>"
                "<tr><td>Depends on the car's speed?</td><td>Yes — doubling the speed doubles it</td><td>Yes — doubling the speed <i>quadruples</i> it (see the tricky bits)</td></tr>"
                "<tr><td>Other factors</td><td><b>Driver's reaction time:</b> tiredness, alcohol, drugs, distractions (phones, passengers)</td>"
                "<td><b>Mass of the vehicle</b> (loaded lorry), <b>condition of the brakes</b>, <b>condition of the tyres</b>, <b>state of the road</b> (wet, icy, gravel) — anything that changes the friction</td></tr></table>"
                "$$" + THINK_EQ + "$$"
                "<p>A typical human <b>reaction time</b> is <b>0.2 s to 0.9 s</b>. The Highway Code assumes about 0.7 s. "
                "Tiredness, alcohol, drugs and distractions all make it <i>longer</i>, which makes the thinking distance longer.</p>"
                "<p>The exam loves asking which part a factor affects. Ice does not change how fast you <i>react</i>; a phone does not change how well the <i>brakes</i> grip.</p>"
            ),
        },
        {
            "kind": "worked",
            "title": "Stopping distance",
            "question": "A car travels at 20 m/s. The driver's reaction time is 0.7 s and the braking distance is 30 m. Calculate (a) the thinking distance and (b) the stopping distance.",
            "steps": [
                r"<b>(a)</b> During the reaction time the car keeps going at 20 m/s.",
                r"$\text{thinking distance} = 20 \times 0.7 = 14$ m.",
                r"<b>(b)</b> $\text{stopping distance} = 14 + 30 = 44$ m.",
            ],
        },
        {
            "kind": "practice",
            "title": "Stopping distances",
            "questions": [
                numeric("t2-n15-q1", "A car travels at 15 m/s and the driver's reaction time is 0.6 s. Calculate the thinking distance.", sf(q15_1), "m",
                        "Speed × reaction time.",
                        ewau(THINK_EQ, r"\text{thinking distance} = 15 \times 0.6", "9", "m")),
                numeric("t2-n15-q2", "The braking distance of the car in question 1 is 21 m. Calculate its stopping distance.", sf(q15_2), "m",
                        "Thinking distance + braking distance.",
                        ewau(STOP_EQ, r"\text{stopping distance} = 9 + 21", "30", "m")),
                choice("t2-n15-q3", "Which of these increases the <b>thinking</b> distance but not the braking distance?",
                       ["A wet road", "A tired driver", "Worn brake pads", "A heavily loaded car"], 1,
                       "Tiredness lengthens the reaction time, so the car travels further before braking starts. The other three all affect the braking distance."),
                choice("t2-n15-q4", "Which of these increases the <b>braking</b> distance but not the thinking distance?",
                       ["Alcohol", "An icy road", "Using a mobile phone", "Tiredness"], 1,
                       "Ice reduces friction between the tyres and the road, so the brakes take longer to stop the car. The other three affect the driver's reaction time."),
                choice("t2-n15-q5", "Which is a typical reaction time for a human driver?", ["0.02 s", "0.5 s", "2 s", "5 s"], 1,
                       "Typical reaction times are 0.2–0.9 s. 2 s would be dangerously slow; 0.02 s is faster than any human nerve signal."),
                numeric("t2-n15-q6", "A lorry's stopping distance is 60 m and its thinking distance is 18 m. Calculate its braking distance.", sf(q15_6), "m",
                        "Rearrange: braking = stopping − thinking.",
                        [r"$\text{braking distance} = 60 - 18 = 42$ m."]),
                written("t2-n15-q7", "Give three factors that affect a driver's reaction time.",
                        marks(["Tiredness", "Alcohol", "Drugs (including some medicines)", "Distractions, e.g. mobile phones or passengers",
                               "(Any three.)"]), lines=2),
            ],
        },
    ],
}


SECTIONS = [section_n9, section_n10, section_n11, section_n12, section_n13, section_n14, section_n15]
