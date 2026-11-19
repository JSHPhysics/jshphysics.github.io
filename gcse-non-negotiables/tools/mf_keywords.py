"""
mf_keywords.py — Topic 2 Motion and forces: key words, and the Newton's
third law explanation of momentum conservation.

Definitions are written to the wording Edexcel mark schemes credit; the
words that score are in bold in each model answer.
"""

from revlib import choice, explain, fact, group, marks, practice, section, worked, written


# =====================================================================
# Key words — the definitions that score
# =====================================================================

DEFINITIONS = [
    # (term, mark-scheme definition with scoring words bolded, common wrong answer)
    ("Scalar", "A quantity with <b>magnitude (size) only</b>", "\"a number\" / \"a quantity without direction\" on its own — say magnitude only"),
    ("Vector", "A quantity with <b>magnitude and direction</b>", "\"a quantity with direction\" — the magnitude must be mentioned too"),
    ("Displacement", "The <b>distance</b> from a start point <b>in a stated direction</b>", "\"how far you have gone\" — that is distance"),
    ("Velocity", "<b>Speed in a stated direction</b> (the rate of change of displacement)", "\"how fast\" / \"speed\" — the direction is the mark"),
    ("Acceleration", "The <b>rate of change of velocity</b> (change in velocity per second)", "\"speeding up\" — acceleration includes slowing down and changing direction"),
    ("Deceleration", "A <b>negative acceleration</b>: velocity decreasing", "\"stopping\""),
    ("Resultant force", "The <b>single force</b> that has the <b>same effect</b> as all the forces acting on an object together", "\"the total force\" — needs the idea of one force with the same effect"),
    ("Equilibrium", "The <b>resultant force is zero</b> (forces balanced), so the object stays at rest or at constant velocity", "\"nothing is moving\" — a moving object can be in equilibrium"),
    ("Newton's first law", "An object stays <b>at rest</b> or moves at <b>constant velocity</b> unless a <b>resultant force</b> acts on it", "\"objects keep moving\" — all three parts are needed"),
    ("Newton's second law", "Acceleration is <b>proportional to the resultant force</b> and <b>inversely proportional to the mass</b>; $F = m \\times a$", "\"force makes things accelerate\""),
    ("Newton's third law", "When two objects interact, the forces on each are <b>equal in size</b> and <b>opposite in direction</b> (and of the same type)", "\"every action has an equal and opposite reaction\" — credited only if you then say what the two forces are"),
    ("Mass", "The <b>amount of matter</b> in an object (also: a measure of its inertia)", "\"how heavy it is\" — that is weight"),
    ("Weight", "The <b>force</b> of <b>gravity</b> on an object; $W = m \\times g$", "\"mass × gravity\" — weight is a force, in newtons"),
    ("Gravitational field strength", "The <b>force</b> of gravity <b>per kilogram</b> (per unit mass), in N/kg", "\"gravity\" / \"10\""),
    ("Inertial mass", "A measure of <b>how difficult it is to change the velocity</b> of an object; the ratio of <b>force to acceleration</b>", "\"how heavy it is\""),
    ("Momentum", "<b>Mass × velocity</b>; a <b>vector</b> quantity, in kg m/s", "\"how hard something is to stop\" (fine as an idea, not as the definition)"),
    ("Conservation of momentum", "In a closed system (no external forces) the <b>total momentum before</b> an event equals the <b>total momentum after</b>", "\"momentum stays the same\" — whose momentum? the total"),
    ("Terminal velocity", "The <b>constant</b> (maximum) velocity of a falling object reached when <b>air resistance equals the weight</b>, so the <b>resultant force is zero</b>", "\"the fastest it can go\""),
    ("Centripetal force", "The <b>resultant force</b> acting <b>towards the centre</b> of the circle that keeps an object moving in a circle", "\"the force that pulls you outwards\" — that is not a force"),
    ("Thinking distance", "The distance a vehicle travels <b>during the driver's reaction time</b> (before the brakes are applied)", "\"the distance it takes to think\""),
    ("Braking distance", "The distance a vehicle travels <b>while the braking force acts</b>, from the brakes being applied until it stops", "\"how far it takes to stop\" — that is stopping distance"),
    ("Stopping distance", "<b>Thinking distance + braking distance</b>", "\"braking distance\""),
    ("Reaction time", "The <b>time between</b> a driver <b>seeing a hazard</b> and <b>responding</b> (applying the brakes)", "\"how fast you react\" — it is a time"),
]


def keyword_rows():
    html = "<table class='tbl'><tr><th>Term</th><th>Definition that scores</th><th>Common answer that does not</th></tr>"
    for term, definition, wrong in DEFINITIONS:
        html += "<tr><td><b>" + term + "</b></td><td>" + definition + "</td><td>" + wrong + "</td></tr>"
    html += "</table>"
    return html


section_keywords = section(
    "keywords", "nn", "Key words: the definitions that score", "2.1–2.33",
    blurb="\"State what is meant by…\" is a mark for a specific form of words. Near enough is not enough: the bold words below are the ones the mark scheme is looking for.",
    checklist=[
        "Define every bold term in this topic using the words the mark scheme credits",
        "Tell a definition from an example (\"a vector has magnitude and direction\", not \"velocity is a vector\")",
        "Spot the common wrong definitions and say what is missing from them",
    ],
    parts=[
        explain(
            "The definitions",
            "<p>Learn these as forms of words. When a question says <i>state what is meant by</i> or <i>define</i>, write the definition, not an example and not an equation (unless the equation is asked for).</p>"
            + keyword_rows(),
        ),
        explain(
            "Where the mark goes",
            "<p>Markers look for the <b>key idea</b>, and in a one-mark definition there is usually exactly one: <i>direction</i> for velocity, <i>rate of change</i> for acceleration, <i>force</i> for weight, <i>resultant force is zero</i> for terminal velocity. "
            "An answer that is true but leaves the key idea out — \"velocity is how fast something moves\" — scores nothing, however long it is.</p>"
            "<p>A definition is not an example. \"A vector is something like velocity\" names a vector but does not define one.</p>",
            tone="warn",
        ),
        worked(
            "Two marks for a definition",
            "State what is meant by <i>terminal velocity</i>. (2)",
            [
                r"Find the key ideas: it is a <b>constant velocity</b> (1), reached when the <b>resultant force is zero</b> because air resistance equals the weight (1).",
                r"Answer: \"The constant velocity a falling object reaches when the air resistance has grown to equal its weight, so the resultant force on it is zero.\"",
                r"\"The maximum speed it can fall at\" would score one mark at most — it has the constant/maximum idea but not the forces.",
            ],
        ),
        practice("Key words", [
            written("t2-kw-q1", "State what is meant by a <i>vector</i> quantity. (1)",
                    marks(["A quantity that has <b>magnitude (size) and direction</b>."]), lines=1),
            written("t2-kw-q2", "State what is meant by <i>acceleration</i>. (1)",
                    marks(["The <b>rate of change of velocity</b> (the change in velocity per second)."]), lines=1),
            choice("t2-kw-q3", "Which of these is the definition of <i>velocity</i> that scores the mark?",
                   ["How fast an object is moving", "Speed in a stated direction", "Distance divided by time", "A vector"], 1,
                   "Velocity is speed in a stated (given) direction. \"How fast\" and distance ÷ time define speed; \"a vector\" says what kind of quantity it is, not what it is."),
            choice("t2-kw-q4", "Which statement of <i>Newton's first law</i> is complete?",
                   ["Objects keep moving unless a force acts", "An object stays at rest or at constant velocity unless a resultant force acts on it", "Force equals mass times acceleration", "Every force has an equal and opposite force"], 1,
                   "All three parts are needed: at rest or constant velocity, unless, resultant force. The first option misses the resultant and the at-rest case; the others are the second and third laws."),
            written("t2-kw-q5", "State what is meant by the <i>resultant force</i> on an object. (1)",
                    marks(["The <b>single force</b> that would have the <b>same effect</b> as all the forces acting on the object together."]), lines=2),
            written("t2-kw-q6", "State the difference between <i>mass</i> and <i>weight</i>. (2)",
                    marks(["Mass is the <b>amount of matter</b> in an object (a scalar, in kg).",
                           "Weight is the <b>force of gravity</b> on the object (a vector, in N)."]), lines=2),
            choice("t2-kw-q7", "A student writes: \"Weight is mass times gravity.\" Why does this not score the mark for defining weight?",
                   ["It should say mass divided by gravity", "It does not say that weight is a force", "Weight has nothing to do with mass", "It is correct and would score"], 1,
                   "The key idea for weight is that it is a force — the force of gravity on an object. An equation with no mention of force misses it."),
            written("t2-kw-q8", "State what is meant by <i>inertial mass</i>. (2)",
                    marks(["A measure of <b>how difficult it is to change the velocity</b> of an object.",
                           "Defined as the ratio of <b>force to acceleration</b>, $m = F \\div a$."]), lines=2),
            written("t2-kw-q9", "State what is meant by <i>thinking distance</i> and <i>braking distance</i>. (2)",
                    marks(["Thinking distance: the distance travelled <b>during the driver's reaction time</b>, before the brakes are applied.",
                           "Braking distance: the distance travelled <b>while the braking force acts</b>, until the vehicle stops."]), lines=2),
            choice("t2-kw-q10", "Which is the definition of <i>centripetal force</i>?",
                   ["The force that throws you outwards on a roundabout", "The resultant force towards the centre of the circle that keeps an object moving in a circle", "The speed of an object moving in a circle", "A new force created by circular motion"], 1,
                   "Centripetal force is the name for the resultant force towards the centre; it is provided by a real force such as tension, friction or gravity. There is no outward force."),
            written("t2-kw-q11", "State the <i>principle of conservation of momentum</i>. (2)",
                    marks(["In a <b>closed system</b> (no external forces),",
                           "the <b>total momentum before</b> an event (collision or explosion) is <b>equal to the total momentum after</b> it."]), lines=2, tags=["H"]),
            written("t2-kw-q12", "State Newton's third law. (2)",
                    marks(["When two objects interact, each exerts a force on the other;",
                           "the two forces are <b>equal in size and opposite in direction</b> (and of the same type)."]), lines=2),
        ], intro="Write each answer on paper first. Mark yourself strictly: if the bold words (or their equivalent) are missing, it is not a mark."),
    ],
)


# =====================================================================
# Conservation of momentum from Newton's third law (added to T8)
# =====================================================================

explain_n3_momentum = explain(
    "Why momentum is conserved: Newton's third law",
    "<p>Conservation of momentum is not a separate rule to memorise — it follows from Newton's third law. The chain of reasoning the exam wants, in order:</p>"
    "<ol class='list'>"
    "<li>When the two bodies collide, each exerts a force on the other. By Newton's third law the forces are the <b>same size</b> on each body and in <b>opposite directions</b>.</li>"
    "<li>The two forces act for the <b>same time</b> — the time the bodies are in contact.</li>"
    "<li>Force × time is the change in momentum ($F = \\dfrac{\\Delta p}{t}$, so $\\Delta p = F \\times t$). Equal forces for equal times give changes in momentum that are <b>equal in size and opposite in direction</b>.</li>"
    "<li>So the <b>total change in momentum is zero</b>: whatever momentum one body gains, the other loses. The total momentum after equals the total before.</li></ol>"
    "<p>Four steps, four marks. Leave out \"for the same time\" and the argument does not work — equal forces for different times would give different changes in momentum.</p>",
)

worked_n3_momentum = worked(
    "The explanation as an exam answer",
    "Two trolleys collide on a frictionless track. Explain, using Newton's third law, why the total momentum of the trolleys is the same after the collision as before. (4)",
    [
        r"<b>1.</b> During the collision trolley A exerts a force on trolley B, and trolley B exerts a force on trolley A that is <b>equal in size and opposite in direction</b> (Newton's third law).",
        r"<b>2.</b> The two forces act for the <b>same time</b>, because the trolleys are in contact for the same time.",
        r"<b>3.</b> Change in momentum = force × time, so the trolleys receive changes in momentum that are <b>equal in size and opposite in direction</b>.",
        r"<b>4.</b> The changes cancel: the <b>total change in momentum is zero</b>, so the total momentum is unchanged by the collision.",
        r"Each numbered line is one mark. The same answer, with \"the ball and the bat\" or \"the gun and the bullet\" substituted, answers every version of the question.",
    ],
)

practice_n3_momentum = [
    written("t2-t8-q7", "A cannon fires a cannonball. Explain, using Newton's third law, why the cannon recoils with the same size of momentum as the cannonball. (4)",
            marks(["The cannon exerts a force on the ball and the ball exerts a force on the cannon that is <b>equal in size and opposite in direction</b> (Newton's third law).",
                   "The two forces act for the <b>same time</b> (while the ball is being pushed along the barrel).",
                   "Change in momentum = force × time, so the ball and the cannon gain changes in momentum that are <b>equal in size and opposite in direction</b>.",
                   "The total momentum was zero before firing, so it is zero after: the cannon's momentum backwards equals the ball's momentum forwards."]), lines=5, tags=["H"]),
    choice("t2-t8-q8", "In the Newton's-third-law explanation of momentum conservation, why does it matter that the two forces act for the same time?",
           ["It does not matter", "Because change in momentum = force × time, so equal forces for equal times give equal and opposite changes in momentum", "Because the forces are only equal while the objects are moving", "Because momentum is measured in seconds"], 1,
           "Equal forces alone are not enough: the change in momentum each body receives is $F \\times t$, so the times must be equal too for the changes to cancel."),
]

facts_extra = [
    fact("Define a scalar", "A quantity with magnitude (size) only", "keywords"),
    fact("Define a vector", "A quantity with magnitude and direction", "keywords"),
    fact("Define velocity", "Speed in a stated direction", "keywords"),
    fact("Define acceleration", "Rate of change of velocity", "keywords"),
    fact("Define resultant force", "The single force with the same effect as all the forces together", "keywords"),
    fact("Define weight", "The force of gravity on an object ($W = m \\times g$)", "keywords"),
    fact("Define gravitational field strength", "Force of gravity per kilogram, N/kg", "keywords"),
    fact("Define inertial mass", "How difficult it is to change an object's velocity; $F \\div a$", "keywords"),
    fact("Define terminal velocity", "Constant velocity reached when air resistance = weight, so resultant force = 0", "keywords"),
    fact("Define centripetal force", "The resultant force towards the centre keeping an object in a circle", "keywords"),
    fact("Define thinking distance", "Distance travelled during the driver's reaction time", "keywords"),
    fact("Define braking distance", "Distance travelled while the braking force acts", "keywords"),
    fact("Define reaction time", "Time between seeing a hazard and responding", "keywords"),
    fact("State the principle of conservation of momentum", "Total momentum before = total momentum after, if no external forces", "keywords"),
    fact("Why is momentum conserved (4 steps)?", "N3: equal and opposite forces → same time → equal and opposite Δp → total $\\Delta p = 0$", "conservation-momentum"),
    fact("What provides the centripetal force for a car on a roundabout?", "Friction between the tyres and the road", "circular-motion"),
    fact("What provides the centripetal force for a satellite?", "Gravity", "circular-motion"),
    fact("Doubling speed does what to KE and braking distance?", "Both ×4 ($\\propto v^2$)", "braking-v-squared"),
    fact("Unit of acceleration? of momentum?", "m/s²; kg m/s", "acceleration-nn"),
    fact("Equation linking force, momentum change and time?", "$F = \\dfrac{mv - mu}{t}$", "force-momentum"),
    fact("Equation for weight, and the unit of each symbol?", "$W = m \\times g$: W in N, m in kg, g in N/kg (10 N/kg on Earth).", "weight"),
]
