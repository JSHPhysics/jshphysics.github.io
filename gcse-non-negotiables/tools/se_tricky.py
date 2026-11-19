"""
se_tricky.py — Topic 11 (Static electricity): the tricky bits T1–T7 and
the flashcards. Every section is Physics-only.

T1 The electron chain and the force chain   T5 Sprayers: each advantage with its reason
T2 Induction without contact                T6 Drawing and reading field diagrams
T3 Sparks and shocks explained              T7 Explaining with fields
T4 Fuelling: the danger-and-precaution question
"""

from revlib import (
    choice, diagram, explain, fact, group, mark_scheme, marks, numeric,
    practice, section, worked, written,
)
import se_diagrams as dg

# ---------------------------------------------------------------------
# T1 · The electron chain and the force chain
# ---------------------------------------------------------------------

section_t1 = section(
    "electron-force-chains", "tricky", "Two chains the marks are on: electrons, and force → acceleration", "11.1P, 11.2P, 11.3P",
    equations=[r"\text{friction} \rightarrow \text{electrons move} \rightarrow \text{charge}", r"\text{like charges repel} \rightarrow \text{force on X away from Y} \rightarrow \text{X accelerates away}"],
    blurb="Every 'explain' in this topic is one of two chains. The charging chain is about electrons moving. The moving-apart chain is about a force: 'they repel' on its own is not an explanation — the examiners want the force named, its direction given, and the acceleration that follows.",
    tags=["P"],
    checklist=[
        "Write the charging chain: friction → electrons transferred from A to B → B negative, A positive",
        "Write the force chain: like charges → repel → force on X away from Y → X accelerates away",
        "Avoid the traps: protons moving, charge being made, 'it moves' without a force, 'the charge pushes it'",
    ],
    parts=[
        explain(
            "The two chains",
            "<table class='tbl'><tr><th>Question</th><th>The chain (one mark a link)</th></tr>"
            "<tr><td>Explain how the rod becomes charged</td><td><b>friction</b> (rubbing) → <b>electrons are transferred</b> from the cloth to the rod → the rod has <b>gained electrons</b> so it is <b>negative</b> → the cloth has <b>lost</b> them so it is <b>positive</b>, by the same amount</td></tr>"
            "<tr><td>Explain why the two balloons move apart</td><td>both balloons are charged the <b>same sign</b> → <b>like charges repel</b> → so there is a <b>force on each balloon</b>, directed <b>away from the other</b> → a resultant force causes an <b>acceleration</b>, so each balloon <b>accelerates away</b> from the other</td></tr>"
            "<tr><td>Explain why the ball moves towards the rod</td><td>the charges are <b>unlike</b> (or the ball is neutral and is <b>induced</b>, T2) → <b>attract</b> → a <b>force on the ball towards the rod</b> → the ball <b>accelerates towards</b> the rod</td></tr></table>"
            "<p><b>The force → acceleration link.</b> Examiners are strict here, because it is Topic 2's rule in a new setting: a <b>resultant force</b> changes an object's motion — it makes it <b>accelerate</b>. So \"they repel, so the ball moves away\" skips a link. The full sentence is: \"<i>the charges are alike, so they repel: a force acts on the ball, directed away from the rod, so the ball accelerates away from the rod</i>\". Name the force, give its direction, say it causes an acceleration. If the question says the ball ends up hanging at an angle, add that it moves until the <b>thread's pull balances</b> the repulsion.</p>"
            "<p><b>Losses:</b> \"the <b>charge</b> pushes it\" (a charge is not a force — say the force <i>between</i> the charges); \"<b>positive charge moves</b> to the cloth\" (only electrons move); \"the rod <b>makes</b> charge\" (charge is transferred); \"it <b>repels</b>\" with no force or direction; \"the force makes it <b>move</b>\" where the question wants <b>accelerate</b>.</p>",
        ),
        worked(
            "Both chains in one question",
            "Two identical balloons are rubbed on the same jumper and hung side by side on threads. They hang apart from each other. (a) Explain how the balloons became charged. (b) Explain why they hang apart. (5 marks)",
            [
                "<b>(a)</b> <b>Friction</b> between each balloon and the jumper <b>transferred electrons</b> from the jumper to the balloon…",
                "…so each balloon <b>gained electrons</b> and is <b>negatively charged</b> (the jumper is left positive).",
                "<b>(b)</b> Both balloons have the <b>same (negative) charge</b>, and <b>like charges repel</b>.",
                "So there is a <b>force on each balloon directed away from the other</b> — an equal and opposite pair.",
                "A force causes an <b>acceleration</b>: each balloon <b>accelerates away</b> from the other, until the pull of its thread balances the repulsion and it hangs at an angle.",
            ],
        ),
        practice("The two chains", [
            written("se-t1-q1", "A negatively charged rod is brought near a small negatively charged ball hanging on a thread. Explain why the ball moves. (3)",
                    mark_scheme([
                        ("Rule", "The rod and the ball have the <b>same charge</b>, and <b>like charges repel</b>."),
                        ("Force", "So a <b>force acts on the ball</b>, directed <b>away from the rod</b>."),
                        ("Motion", "A (resultant) force causes an <b>acceleration</b>: the ball <b>accelerates away</b> from the rod."),
                    ]), lines=4),
            choice("se-t1-q2", "Which answer gains all the marks for \"explain why the two charged balls move apart\"?",
                   ["\"They have the same charge so they repel.\"", "\"Like charges repel, so each ball has a force on it directed away from the other, so each ball accelerates away.\"", "\"The charge pushes them apart.\"", "\"They are both negative so they move.\""], 1,
                   "Rule, force with direction, acceleration."),
            written("se-t1-q3", "A positively charged rod is held near a negatively charged ball. Explain the motion of the ball. (3)",
                    mark_scheme([
                        ("Rule", "The charges are <b>unlike</b>, and unlike charges <b>attract</b>."),
                        ("Force", "A <b>force acts on the ball towards the rod</b>."),
                        ("Motion", "The force causes the ball to <b>accelerate towards</b> the rod."),
                    ]), lines=4),
            written("se-t1-q4", "A student writes: \"When the rod is rubbed, positive charge moves from the rod to the cloth, so the rod becomes negative.\" Correct the student's explanation. (2)",
                    marks(["Positive charge (protons) <b>cannot move</b>; it is <b>electrons</b> that are transferred.", "Electrons move <b>from the cloth to the rod</b>: the rod gains electrons and becomes negative, the cloth loses them and becomes positive."]), lines=2),
            choice("se-t1-q5", "Why is \"the force makes the ball move\" marked down when the question asks to explain the ball's motion?",
                   ["Forces do not cause motion", "The mark is for linking the resultant force to the ball's acceleration (a change in its motion), not just to movement", "Balls cannot accelerate", "The word 'force' should not be used"], 1,
                   "Resultant force → acceleration is the link they want."),
            written("se-t1-q6", "Two charged objects attract each other. One is much heavier than the other. Compare the forces on them and their accelerations. (2)",
                    marks(["The forces are <b>equal in size and opposite</b> in direction (an interaction pair).", "The <b>lighter</b> object has the <b>larger acceleration</b> ($a = F/m$), so it is the one seen to move."]), lines=2),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T2 · Induction without contact
# ---------------------------------------------------------------------

section_t2 = section(
    "induction-explain", "tricky", "Induction: why a neutral object is attracted", "11.4P",
    equations=[r"\text{electrons in the neutral object move} \rightarrow \text{near side opposite} \rightarrow \text{nearer force wins}"],
    blurb="The comb and the paper, the balloon and the wall, the charged rod and the tap water: the thing being attracted is neutral. The explanation is that its electrons move, the near side gets the opposite charge, and the attraction on the nearer side beats the repulsion on the far side.",
    tags=["P"],
    checklist=[
        "Explain attraction of a neutral object by induction, step by step",
        "Draw the induced charges on both sides of the object",
        "Explain why the net force is attractive, and why the object stays neutral overall",
    ],
    parts=[
        explain(
            "The four steps",
            "<ol><li>The neutral object has <b>equal numbers of positive and negative charges</b>, spread evenly.</li>"
            "<li>The charged object's field acts on them. A <b>negative</b> rod <b>repels the electrons</b> to the far side; a <b>positive</b> rod <b>attracts them</b> to the near side. Either way the <b>electrons move</b> — the positive charges (nuclei) do not.</li>"
            "<li>So the <b>near side has the opposite charge</b> to the rod and the <b>far side the same charge</b>. The object is <b>still neutral overall</b>: the charges have been <b>separated</b>, not changed.</li>"
            "<li>The near side is <b>attracted</b> and the far side is <b>repelled</b>, but the near side is <b>closer</b>, and the force is larger at a smaller distance — so the <b>attraction is the larger force</b> and there is a <b>resultant force towards the rod</b>.</li></ol>"
            "<p>That is why a neutral object is <b>always attracted</b>, whatever the sign of the rod, and never repelled. In a <b>metal</b> the free electrons move through the whole object; in <b>water</b> the charged particles in it (ions) and the water molecules themselves shift; in an <b>insulator</b> (paper) the electrons shift slightly within each molecule — the effect is the same, just weaker.</p>"
            "<p>The June 2023 report (Q1(c), a dust particle near a positive base): a diagram with the induced <b>negative</b> charge on the near side scored, but the fully correct one also showed the induced <b>positive</b> charge on the far side — \"the total numbers of positive and negative charges still balance\". Draw both sides. The 2025 scheme (Q4(b)(ii)) gave full marks for \"a positive charge would be <b>induced</b> on the surface of the metal tube\".</p>",
        ),
        worked(
            "Water bends towards a comb",
            "A charged plastic comb held near a thin stream of water from a tap makes the stream bend towards the comb. Explain why. (3 marks)",
            [
                "The water is <b>neutral</b>, but the comb's charge <b>moves the electrons</b> in the water: with a negative comb they are pushed to the far side of the stream, leaving the <b>near side positive</b>.",
                "The near (positive) side is <b>attracted</b> to the comb and the far (negative) side is <b>repelled</b>.",
                "The attraction acts at a <b>shorter distance</b>, so it is the <b>larger</b> force: there is a resultant force on the water <b>towards the comb</b>, so the water <b>accelerates towards the comb</b> and the stream bends.",
            ],
        ),
        practice("Induction", [
            written("se-t2-q1", "A negatively charged balloon is held near a wall. Draw (describe) the charges on the wall's surface and explain why the balloon sticks. (3)",
                    mark_scheme([
                        ("Electrons move", "The balloon's charge <b>repels electrons</b> in the wall's surface <b>away</b> from the balloon."),
                        ("Induced charges", "The surface <b>nearest the balloon is left positive</b>; further in, the surface is negative (the wall stays neutral overall)."),
                        ("Force", "The near positive surface <b>attracts</b> the balloon more strongly than the further negative charge repels it, so there is a resultant attractive force holding it on."),
                    ]), lines=4),
            choice("se-t2-q2", "A positively charged rod is held near a neutral metal can. Which is correct?",
                   ["Electrons move to the far side of the can", "Electrons move to the near side, so the near side is negative and the far side positive", "Protons move to the near side", "The can becomes positively charged overall"], 1,
                   "Electrons are attracted towards the positive rod; the can stays neutral."),
            written("se-t2-q3", "Explain why a neutral piece of paper is attracted to a charged comb but is never repelled by it. (2)",
                    marks(["Induction always puts the <b>opposite charge on the near side</b> (electrons move towards a positive comb, away from a negative one).", "The attraction on the <b>nearer</b> side is always <b>larger</b> than the repulsion on the far side, so the resultant force is towards the comb."]), lines=3),
            written("se-t2-q4", "A student's diagram shows induced negative charge on the near side of a neutral sphere and nothing on the far side. Explain what is missing. (2)",
                    marks(["The sphere is <b>neutral overall</b>, so the electrons that moved to the near side have left an <b>equal positive charge on the far side</b>.", "The diagram must show both: negative near, positive far, with the total charges balancing."]), lines=2),
            choice("se-t2-q5", "Why does the attraction on the near side of an induced object beat the repulsion on the far side?",
                   ["There are more charges on the near side", "The near side is closer to the charged object, and the force is larger at a smaller distance", "The far side is positive", "Repulsion is always weaker than attraction"], 1,
                   "Same size charges; different distances."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T3 · Sparks and shocks explained
# ---------------------------------------------------------------------

section_t3 = section(
    "sparks", "tricky", "Sparks and shocks: from a build-up of charge to a flow through the air", "11.4P, 11.5P",
    equations=[r"\text{charge builds} \rightarrow \text{pd grows} \rightarrow \text{air conducts} \rightarrow \text{electrons jump}"],
    blurb="A spark is electrons crossing a gap that normally insulates. The chain is always: charge builds up, the pd between the object and something earthed grows, the field becomes strong enough to make the air conduct, and the electrons jump across all at once.",
    tags=["P"],
    checklist=[
        "Explain a spark as the chain: charge build-up → large pd → air breaks down → electrons flow",
        "Apply it to a shock from a car door and to lightning",
        "Explain why touching an earthed conductor discharges you, and why dry conditions make static worse",
    ],
    parts=[
        explain(
            "The chain, and where it comes up",
            "<p><b>1 Charge builds up.</b> Friction (walking on a carpet, sliding off a car seat, fuel in a hose, ice in a cloud) transfers electrons, and because the object is <b>insulated</b> from the ground the charge cannot leak away.</p>"
            "<p><b>2 The pd grows.</b> More charge means a larger <b>potential difference</b> between the object and the earth (or an earthed conductor nearby) — thousands of volts from a carpet, hundreds of millions in a storm.</p>"
            "<p><b>3 The air breaks down.</b> Air is an insulator, but a strong enough <b>electric field</b> pulls electrons off air molecules; the air becomes a conductor for an instant.</p>"
            "<p><b>4 Electrons flow.</b> The excess electrons rush across the gap (or electrons rush in to a positive object) — a <b>spark</b>: you see light, hear a crack, and feel the current if it passes through you. The object is left <b>discharged</b>.</p>"
            "<table class='tbl'><tr><th>Situation</th><th>How it fits the chain</th></tr>"
            "<tr><td>shock from a car door</td><td>you charge up sliding across the seat; the door is a conductor at a different potential from you; the spark jumps as your finger approaches, before you touch</td></tr>"
            "<tr><td>lightning</td><td>the cloud base charges by friction between ice and water; the pd between cloud and ground becomes enormous; the air along a path breaks down and a vast current flows</td></tr>"
            "<tr><td>crackles taking off a jumper</td><td>friction between the layers charges them; many tiny sparks as they separate</td></tr></table>"
            "<p><b>Dry days are worse</b> because moist air lets charge leak away slowly (water conducts a little), so it never builds up; dry air lets it accumulate. <b>Touching the earthed metal first with a key</b> moves the spark to the key, not your fingertip.</p>",
        ),
        worked(
            "The car-door shock",
            "A passenger slides across a car seat, steps out and gets a shock as she touches the metal door. Explain why. (4 marks)",
            [
                "<b>Friction</b> between her clothes and the seat <b>transfers electrons</b>, so she becomes <b>charged</b>; her shoes insulate her from the ground, so the charge <b>builds up</b>.",
                "This gives a large <b>pd between her and the car body</b>, which is a large conductor at a different potential from her.",
                "As her hand nears the door the electric field across the small gap is strong enough for the <b>air to conduct</b>…",
                "…and <b>electrons flow</b> across the gap in a sudden <b>spark</b>: the current through her hand is the shock, and she is left discharged.",
            ],
        ),
        practice("Sparks and shocks", [
            written("se-t3-q1", "Explain what a spark is, in terms of electrons. (2)",
                    marks(["A large pd across a gap makes the electric field strong enough for the <b>air to conduct</b>…", "…so <b>electrons flow suddenly across the gap</b> (through the air), discharging the object."]), lines=2),
            choice("se-t3-q2", "Why can static charge build up on a person walking on a carpet, but not on one walking barefoot on wet grass?",
                   ["Grass makes no friction", "Wet grass and skin conduct, so the charge leaks away to earth as fast as it forms", "Carpets are positively charged", "Shoes are conductors"], 1,
                   "A conducting path to earth stops the build-up."),
            written("se-t3-q3", "Explain why static shocks are more common in dry weather. (2)",
                    marks(["In humid air, moisture lets charge <b>leak away slowly</b>, so a large charge never builds up.", "Dry air is a better <b>insulator</b>, so charge <b>accumulates</b> until the pd is large enough for a spark."]), lines=2),
            written("se-t3-q4", "Explain why lightning is far more powerful than a shock from a door handle, using the same chain of ideas. (2)",
                    marks(["The <b>amount of charge</b> separated in a storm cloud is vastly greater, so the <b>pd</b> between cloud and ground is enormous.", "When the air breaks down, a correspondingly <b>huge flow of electrons</b> passes along the path — a much larger current, over a much larger gap."]), lines=2),
            choice("se-t3-q5", "A person about to touch a metal railing holds a key out and touches the railing with the key first. Why?",
                   ["Keys stop the charge forming", "The spark jumps between the key and the railing instead of from the fingertip, so it is not felt", "Metal keys are insulators", "It increases the charge"], 1,
                   "The discharge still happens, but through the key."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T4 · Fuelling: the danger-and-precaution question
# ---------------------------------------------------------------------

section_t4 = section(
    "fuelling-question", "tricky", "Fuelling: the 6-mark danger-and-precaution question", "11.7P, 11.8P",
    equations=[r"\text{danger chain (3)} + \text{precautions with reasons (3)}"],
    blurb="The long question on this topic: explain why refuelling is dangerous and how the danger is reduced. Half the marks are the danger chain, half are the precautions — and each precaution scores only with its reason.",
    tags=["P"],
    checklist=[
        "Write the danger chain: friction → electrons transferred → charge builds up → pd → spark → ignites vapour",
        "Write each precaution with what it does: bonding keeps the same potential; earthing lets charge flow away",
        "Avoid naming a precaution without its reason",
    ],
    parts=[
        explain(
            "The structure that reaches Level 3",
            "<table class='tbl'><tr><th>Part</th><th>Points</th></tr>"
            "<tr><td><b>Danger</b></td><td>fuel moving through the hose rubs against it: <b>friction transfers electrons</b> → the fuel / aircraft becomes <b>charged</b> → the aircraft is <b>insulated</b> by its tyres, so the charge <b>builds up</b> → a large <b>pd</b> between the aircraft and the tanker or ground → the air can break down and a <b>spark</b> jumps → fuel <b>vapour</b> is flammable, so the spark can cause a <b>fire or explosion</b></td></tr>"
            "<tr><td><b>Precaution 1: bonding</b></td><td>a <b>conducting cable</b> is clipped between the aircraft and the tanker <b>before</b> the hose is connected → charge can <b>flow between them</b> → they stay at the <b>same potential</b> → <b>no pd</b>, so <b>no spark</b> between them</td></tr>"
            "<tr><td><b>Precaution 2: earthing</b></td><td>both are connected to <b>earth</b> by a conductor → any charge <b>flows away to the ground</b> as it is produced → it <b>cannot build up</b> to a dangerous pd</td></tr>"
            "<tr><td>Also accepted</td><td>pumping the fuel <b>slowly</b> (less friction, less charge per second); <b>conducting hoses</b>; no other sources of sparks nearby</td></tr></table>"
            "<p>The usual losses: naming earthing without saying <b>what it does</b>; saying the fuel \"is static\" or \"has electricity\" instead of \"becomes charged by friction\"; forgetting the <b>vapour</b> — it is the vapour that ignites; and writing \"the spark causes a shock\" when the danger here is <b>fire</b>. Say <b>electrons</b> are transferred, say <b>pd</b>, say <b>conductor</b>.</p>",
        ),
        worked(
            "The 6-mark answer",
            "An aircraft is refuelled from a tanker. Explain why static electricity is a danger during refuelling and how the danger is reduced. (6 marks)",
            [
                "As the fuel flows through the hose, <b>friction</b> between the fuel and the hose <b>transfers electrons</b>, so the fuel and the aircraft become <b>charged</b>.",
                "The aircraft stands on <b>insulating</b> tyres, so the charge <b>cannot flow away</b> and <b>builds up</b>, producing a large <b>pd</b> between the aircraft and the tanker.",
                "If the pd becomes large enough a <b>spark</b> can jump across the gap; fuel <b>vapour</b> is flammable, so the spark could cause a <b>fire or explosion</b>.",
                "Before refuelling, a <b>bonding cable</b> (a conductor) is connected between the aircraft and the tanker, so charge <b>flows between them</b> and they stay at the <b>same potential</b> — no pd, so no spark between them.",
                "The aircraft and tanker are also <b>earthed</b>: a conductor to the ground lets the charge <b>flow away to earth</b> as fast as it is made, so it cannot build up.",
                "Pumping the fuel more slowly reduces the friction and the rate at which charge is produced.",
            ],
        ),
        practice("The fuelling question", [
            written("se-t4-q1", "Explain why a bonding cable is connected between a tanker and an aircraft before the fuel hose is attached. (3)",
                    mark_scheme([
                        ("Conductor", "The cable is a <b>conductor</b> joining the two vehicles."),
                        ("Same potential", "Charge can <b>flow between them</b>, so they are at the <b>same potential</b> — there is no pd between them."),
                        ("No spark", "With no pd there can be <b>no spark</b> when the hose is connected, so fuel vapour cannot be ignited."),
                    ]), lines=4),
            choice("se-t4-q2", "What ignites in a refuelling fire caused by a spark?",
                   ["The metal of the aircraft", "The fuel vapour in the air", "The tyres", "The bonding cable"], 1,
                   "Vapour is what a spark can ignite."),
            written("se-t4-q3", "A student answers: \"The tanker is earthed, which makes it safe.\" Rewrite the point so it scores. (2)",
                    marks(["The tanker is connected to earth by a <b>conductor</b>, so any charge produced <b>flows away to the ground</b>…", "…and <b>cannot build up</b> to a pd large enough for a spark that could ignite the fuel vapour."]), lines=2),
            written("se-t4-q4", "Explain why the danger is reduced if the fuel is pumped more slowly. (1)",
                    marks(["Less <b>friction</b> per second between fuel and hose, so charge is produced <b>more slowly</b> and has time to flow away — less build-up."]), lines=1),
            choice("se-t4-q5", "Why does charge build up on an aircraft but not on an earthed metal tank?",
                   ["Aircraft fuel is special", "The aircraft is insulated from the ground by its tyres, so the charge has no path to earth; the earthed tank lets it flow away", "Metal tanks cannot be charged", "The aircraft is positively charged"], 1,
                   "Build-up needs insulation; a conductor to earth prevents it."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T5 · Sprayers
# ---------------------------------------------------------------------

section_t5 = section(
    "sprayers-explain", "tricky", "Sprayers: each advantage with its reason", "11.6P",
    equations=[r"\text{same charge} \rightarrow \text{repel} \rightarrow \text{spread}", r"\text{earthed target} \rightarrow \text{induced opposite charge} \rightarrow \text{attract}"],
    blurb="The sprayer question is marked advantage-plus-reason. Students lose marks by giving the advantage ('even coat') without the physics ('the droplets repel each other'), or by saying the paint is attracted without saying what it is attracted to and why.",
    tags=["P"],
    checklist=[
        "Give each advantage of an electrostatic sprayer with its reason",
        "Explain which charge is where: the droplets, the nozzle, the target",
        "Explain why the target is earthed",
    ],
    parts=[
        explain(
            "Advantage, reason; advantage, reason",
            "<table class='tbl'><tr><th>Advantage</th><th>Reason (the physics the mark is on)</th></tr>"
            "<tr><td>the spray is a <b>fine, even mist</b></td><td>every droplet leaves the nozzle with the <b>same charge</b>; <b>like charges repel</b>, so the droplets push apart and spread out instead of clumping</td></tr>"
            "<tr><td>the paint / insecticide <b>reaches all sides</b> of the target, including the back</td><td>the target is <b>earthed</b> (or oppositely charged); the charged mist <b>induces the opposite charge</b> on its surface, so the droplets are <b>attracted</b> to the whole surface — a non-contact force, not just the air carrying them</td></tr>"
            "<tr><td><b>less is wasted</b>; less drifts into the air</td><td>the droplets are <b>pulled to the target</b> by the attraction rather than passing it; so less chemical is needed and less pollution</td></tr>"
            "<tr><td>an <b>even thickness</b> of coat</td><td>once a patch is coated it carries the droplets' charge, so further droplets are <b>repelled from it</b> towards bare patches</td></tr></table>"
            "<p>Which charge: the nozzle is held at a high potential (a large pd relative to earth), so the droplets all carry <b>one sign</b> (either will do — what matters is that they are all the same). The target is <b>earthed</b>, so it is at 0 V: the approaching charged mist induces the <b>opposite</b> charge on its surface, and electrons flow to or from earth to supply it. Some systems give the target the opposite charge directly instead; the explanation is the same.</p>",
        ),
        worked(
            "Four marks",
            "Explain how an electrostatic sprayer gives a car an even coat of paint using less paint than an ordinary sprayer. (4 marks)",
            [
                "The nozzle gives every paint droplet the <b>same charge</b>.",
                "<b>Like charges repel</b>, so the droplets spread out into a <b>fine, even mist</b> rather than large drops.",
                "The car body is <b>earthed</b>, so the charged mist <b>induces the opposite charge</b> on its surface and the droplets are <b>attracted</b> to it — onto every part of the surface, including the sides and underneath.",
                "Because the droplets are drawn onto the car rather than drifting past, <b>less paint is wasted</b>; and droplets are repelled from already-coated patches towards bare ones, evening the thickness.",
            ],
        ),
        practice("Sprayers", [
            written("se-t5-q1", "State one advantage of charging the droplets in an insecticide sprayer and explain the physics behind it. (2)",
                    marks(["Advantage: an <b>even spray</b> / reaches the <b>undersides of leaves</b> / <b>less wasted</b>.", "Reason: like-charged droplets <b>repel each other</b> (even spread); or the droplets are <b>attracted to the earthed plant</b> by induced opposite charge (coverage, less waste)."]), lines=2),
            choice("se-t5-q2", "In an electrostatic sprayer, why must all the droplets have the same charge?",
                   ["So they attract each other into big drops", "So they repel each other and spread into a fine mist", "So they fall faster", "So they stay in the nozzle"], 1,
                   "Repulsion between droplets is the spreading mechanism."),
            written("se-t5-q3", "Explain why the paint droplets are attracted to an earthed car body. (2)",
                    marks(["The charged droplets <b>induce the opposite charge</b> on the car's surface (electrons flow to or from earth to supply it).", "<b>Unlike charges attract</b>, so there is a force on the droplets towards the surface — on every side of the car."]), lines=2),
            written("se-t5-q4", "A student writes: \"The paint is charged so it sticks to the car.\" Explain why this answer is incomplete. (2)",
                    marks(["It does not say <b>what</b> the paint is attracted to or <b>why</b>: the car must be <b>earthed / oppositely charged</b> so that the droplets' charge induces the opposite charge and unlike charges attract.", "It also misses the other advantage: the droplets <b>repel one another</b>, giving an even mist."]), lines=3),
            choice("se-t5-q5", "Why does an electrostatic sprayer give an even thickness of coat?",
                   ["Paint is thicker when charged", "Once a patch is coated it carries the droplets' charge and repels further droplets towards bare patches", "The air blows it evenly", "The car is spinning"], 1,
                   "Self-levelling by repulsion."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T6 · Drawing and reading field diagrams
# ---------------------------------------------------------------------

section_t6 = section(
    "field-diagrams", "tricky", "Drawing and reading electric field diagrams", "11.10P",
    equations=[r"\text{arrows + to −; evenly spaced; never cross; closer = stronger}"],
    blurb="Field diagrams are drawn for marks: the right shape, arrows the right way, even spacing, and no lines crossing. Reading one is the reverse: direction from the arrows, strength from the spacing.",
    tags=["P"],
    checklist=[
        "Draw the field of a positive and of a negative point charge",
        "Draw the field between two oppositely charged parallel plates",
        "Read direction and relative strength from a field diagram, and spot drawing errors",
    ],
    parts=[
        explain(
            "The rules for drawing, and the errors that lose marks",
            "<table class='tbl'><tr><th>Rule</th><th>Why</th><th>The error</th></tr>"
            "<tr><td>arrows <b>from + to −</b> (away from a positive charge, towards a negative one)</td><td>a line shows the direction of the force on a <b>positive</b> charge</td><td>arrows the wrong way — the 2025 scheme (Q4(a)) gave 1 of 2 marks for correct lines with reversed arrows; no arrows at all scores the same</td></tr>"
            "<tr><td>lines <b>never cross</b> or touch</td><td>at any point the force has one direction</td><td>crossing lines near a charge</td></tr>"
            "<tr><td>a point charge: lines <b>radial</b>, <b>evenly spaced</b> round it, starting (or ending) on the charge</td><td>the field is the same in every direction at the same distance</td><td>lines that curve, or stop in empty space</td></tr>"
            "<tr><td>parallel plates: lines <b>straight, parallel, equally spaced</b>, at right angles to the plates, from the + plate to the − plate</td><td>the field is <b>uniform</b></td><td>lines fanning out, unequal gaps, lines not reaching the plates</td></tr>"
            "<tr><td>spacing shows <b>strength</b></td><td>closer lines = stronger field</td><td>drawing a point charge's lines evenly spaced all the way out (they must spread)</td></tr></table>"
            "<p><b>Reading a diagram:</b> the direction of the force on a positive charge is <b>along the arrow</b>; on a negative charge it is <b>against the arrow</b>. The field is strongest where the lines are <b>closest</b> — next to a point charge, or between the plates rather than at their edges. Two like charges side by side: the lines curve away from each other and there is one point midway between them where the field is zero; a positive and a negative: the lines run from one to the other.</p>",
        ),
        worked(
            "Mark the drawing",
            "A student draws the field between two parallel plates (+ on the left, − on the right) as five straight lines from left to right, bunched towards the middle, with arrows pointing left. Mark the drawing out of 2 and say what would gain full marks.",
            [
                "<b>Shape:</b> straight, parallel lines from plate to plate — correct in kind, but they must be <b>equally spaced</b> (a uniform field), not bunched. Bunching says the field is stronger in the middle, which it is not.",
                "<b>Direction:</b> the arrows should point from the <b>+ plate to the − plate</b>, i.e. left to right here. Pointing left loses the direction mark.",
                "<b>Verdict: 1 of 2.</b> The lines are straight and reach both plates, so the line mark scores; the arrows are reversed, so the direction mark is lost. Bunched lines would cost the line mark with a strict examiner — for 2: four or five equally spaced straight lines, arrows left → right.",
            ],
        ),
        practice("Field diagrams", [
            written("se-t6-q1", "Describe how to draw the electric field around a single negative point charge. (3)",
                    mark_scheme([
                        ("Shape", "Straight <b>radial</b> lines ending on the charge, <b>evenly spaced</b> around it."),
                        ("Direction", "Arrows pointing <b>inwards, towards</b> the charge (the direction of the force on a positive charge)."),
                        ("Spacing", "The lines get <b>further apart</b> away from the charge, showing the field weakening with distance; no lines cross."),
                    ]), lines=4),
            choice("se-t6-q2", "Where is the electric field strongest in a diagram?",
                   ["Where the lines are furthest apart", "Where the lines are closest together", "Where there are no lines", "At the arrowheads"], 1,
                   "Spacing shows strength."),
            choice("se-t6-q3", "A diagram shows the field between parallel plates with arrows pointing from the lower plate to the upper plate. Which plate is positive?",
                   ["The upper plate", "The lower plate", "Neither", "Both"], 1,
                   "Arrows leave the positive plate."),
            written("se-t6-q4", "A negative charge is placed in a uniform field whose lines point to the right. State the direction of the force on it and explain. (2)",
                    marks(["To the <b>left</b>.", "Field lines show the force on a <b>positive</b> charge; a negative charge is pushed the <b>opposite way</b> to the arrows."]), lines=2),
            written("se-t6-q5", "Give two features of a drawing of the field between parallel plates that show the field is uniform. (2)",
                    marks(["The lines are <b>parallel</b> (same direction everywhere).", "The lines are <b>equally spaced</b> (same strength everywhere)."]), lines=2),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T7 · Explaining with fields
# ---------------------------------------------------------------------

section_t7 = section(
    "fields-explain", "tricky", "Explaining static with the field idea", "11.10P",
    equations=[r"\text{a charge has a field} \rightarrow \text{any charge in it feels a force} \rightarrow \text{attraction, induction, sparks}"],
    blurb="The spec's last statement asks you to explain static phenomena with the idea of a field: a charged object has a field around it, a charge placed in that field experiences a force, and a field that becomes strong enough makes the air itself conduct.",
    tags=["P"],
    checklist=[
        "Explain non-contact attraction and repulsion in terms of a field",
        "Explain induction as the field acting on the electrons in a neutral object",
        "Explain a spark as the field becoming strong enough to make air conduct",
    ],
    parts=[
        explain(
            "The same phenomena, in field language",
            "<table class='tbl'><tr><th>Phenomenon</th><th>Field explanation</th></tr>"
            "<tr><td>two charged balloons push apart without touching</td><td>each balloon has an <b>electric field</b> around it; the other balloon's charge is <b>in that field</b>, so it <b>experiences a force</b> — along the field lines for a positive charge, against them for a negative one</td></tr>"
            "<tr><td>a charged comb lifts paper</td><td>the comb's field reaches into the paper and <b>acts on the electrons</b> there, moving them (induction); the near side, now oppositely charged, is in the <b>stronger</b> part of the field (closer lines), so the attraction on it is larger than the repulsion on the far side</td></tr>"
            "<tr><td>a spark jumps</td><td>as charge builds up, the field between the object and earth gets <b>stronger</b> (lines closer); when it is strong enough it pulls <b>electrons off air molecules</b>, the air <b>conducts</b> and electrons flow across — a spark</td></tr>"
            "<tr><td>a lightning conductor's point</td><td>the field is <b>strongest at a sharp point</b> (lines bunched), so the air breaks down there first and the strike is led to the conductor rather than the building</td></tr>"
            "<tr><td>the force weakens with distance</td><td>the lines of a point charge's field <b>spread out</b>, so the field — and the force on a charge in it — is weaker further away</td></tr></table>"
            "<p>The shape of a field answer: (1) the charged object has a field; (2) the other charge is in the field so it feels a force; (3) the direction and strength follow from the lines. The 2024 scheme's definition marks (Q1(b)) and direction mark (Q1(c)(i)) are the same ideas: a region where a charge experiences a force; lines showing the direction of the force on a positive charge.</p>",
        ),
        worked(
            "Field explanation of repulsion",
            "Use the idea of an electric field to explain why a negatively charged ball moves away from a negatively charged rod that is brought near it. (3 marks)",
            [
                "The rod has an <b>electric field</b> around it — a region in which a charge experiences a force.",
                "The ball's (negative) charge is <b>in that field</b>, so a force acts on it; the field lines point towards the negative rod, and a negative charge feels a force <b>against</b> the lines — <b>away from the rod</b>.",
                "The force causes the ball to <b>accelerate away</b> from the rod (it is larger when the rod is closer, where the lines are closer together).",
            ],
        ),
        practice("Explaining with fields", [
            written("se-t7-q1", "Use the idea of an electric field to explain why two positively charged objects repel without touching. (2)",
                    marks(["Each object has an <b>electric field</b> around it.", "The other object's charge is <b>in that field</b> and so <b>experiences a force</b>, directed along the lines — away from the positive charge — so they repel."]), lines=2),
            written("se-t7-q2", "Explain, in terms of electric fields, how a spark occurs between a charged object and an earthed conductor. (3)",
                    mark_scheme([
                        ("Field", "The charged object has an electric field; as more charge builds up the field between it and the conductor gets <b>stronger</b>."),
                        ("Breakdown", "When the field is strong enough it <b>pulls electrons off the air molecules</b>, so the air becomes a <b>conductor</b>."),
                        ("Flow", "Electrons then <b>flow across the gap</b> — the spark — and the object discharges."),
                    ]), lines=4),
            choice("se-t7-q3", "Why does the force between two charged objects get smaller as they are moved apart?",
                   ["The charges leak away", "The field lines spread out with distance, so the field — and the force on a charge in it — is weaker", "Fields only exist close to a charge", "Air absorbs the force"], 1,
                   "Line spacing = strength."),
            written("se-t7-q4", "Explain, using a field, why the near side of a neutral object becomes oppositely charged when a charged rod approaches. (2)",
                    marks(["The rod's <b>field reaches into the object</b> and exerts a force on the <b>electrons</b> in it.", "The electrons move (towards a positive rod, away from a negative one) until the near side carries the <b>opposite charge</b> to the rod."]), lines=2),
            choice("se-t7-q5", "Why does a lightning conductor have a sharp point at the top?",
                   ["To look tall", "The field is strongest at a sharp point, so the air breaks down there first and the strike is led to the conductor", "Points repel lightning", "It is cheaper to make"], 1,
                   "Field lines bunch at a point."),
        ]),
    ],
)

SECTIONS = [section_t1, section_t2, section_t3, section_t4, section_t5, section_t6, section_t7]

# ---------------------------------------------------------------------
# Flashcards (the key-word definitions are added by se_nn.FACTS_KW)
# ---------------------------------------------------------------------

FACTS = [
    # N1
    fact("How does an insulator become charged by friction?", "Rubbing transfers electrons from one material to the other; the one that gains electrons is negative, the one that loses them is positive by the same amount.", "charging-friction"),
    fact("Which particle moves when something is charged?", "Electrons only. Protons are fixed in the nucleus.", "charging-friction"),
    fact("Why can't a metal rod held in the hand be charged by rubbing?", "It is a conductor: the electrons flow through the metal and the hand to earth.", "charging-friction"),
    fact("Is charge created when a rod is rubbed?", "No — transferred. The rod's negative charge equals the cloth's positive charge.", "charging-friction"),
    fact("Two marks for 'explain how the cloth becomes charged'?", "Electrons transferred (from the other object to the cloth) and friction as the cause (June 2023, a plastic base rubbed with a cloth: many omitted friction).", "charging-friction"),
    # N2
    fact("Rule for forces between charges?", "Like charges repel; unlike charges attract. Both objects feel an equal and opposite force.", "charge-forces"),
    fact("How do you prove an object is charged with a known rod?", "Repulsion proves the same charge. Attraction proves nothing, because a neutral object is also attracted (induction).", "charge-forces"),
    fact("What happens to the force as two charges get closer?", "It increases.", "charge-forces"),
    # N3
    fact("Why do you get a shock from a car door?", "Friction with the seat charges you; the door is a conductor at a different potential; as you touch it electrons flow suddenly between you and the metal — a spark.", "static-phenomena"),
    fact("How does lightning happen?", "Friction between ice and water in the cloud separates charge; the pd between cloud and ground grows until the air conducts and a huge flow of electrons discharges it.", "static-phenomena"),
    fact("Why does a charged comb pick up paper?", "The comb's charge moves the paper's electrons: the near side gets the opposite charge and is attracted; the far side is repelled, but more weakly because it is further away.", "static-phenomena"),
    fact("Is the paper charged overall after induction?", "No — neutral. Its charges have been separated, not changed.", "static-phenomena"),
    # N4
    fact("What is earthing?", "Connecting a charged object to the ground with a conductor so that electrons flow to or from earth and the excess charge is removed.", "earthing"),
    fact("Earthing a negative object: which way do the electrons go?", "Down the conductor to earth.", "earthing"),
    fact("Earthing a positive object: which way do the electrons go?", "Up from earth into the object.", "earthing"),
    fact("Why must the earth path be a conductor?", "Electrons cannot move through an insulator; without a conducting path the charge has nowhere to go.", "earthing"),
    # N5
    fact("Why do charged spray droplets spread into a fine mist?", "They all have the same charge, and like charges repel.", "static-uses"),
    fact("Why are charged droplets attracted to the car or plant?", "The target is earthed (or oppositely charged); the droplets induce the opposite charge on its surface, and unlike charges attract — even round the back.", "static-uses"),
    fact("Advantages of an electrostatic sprayer?", "Even coat (droplets repel each other), reaches all sides (attracted to the target), less wasted (drawn to the target rather than drifting), even thickness (repelled from patches already coated).", "static-uses"),
    # N6
    fact("Why is refuelling dangerous?", "Friction between fuel and hose transfers electrons; charge builds up on the insulated aircraft; a large pd forms; a spark could ignite the fuel vapour.", "static-dangers"),
    fact("What does the bonding line do?", "A conductor joining tanker and aircraft so charge flows between them: same potential, no pd, no spark.", "static-dangers"),
    fact("What does earthing do during refuelling?", "Lets the charge flow away to the ground as it is produced, so it cannot build up.", "static-dangers"),
    fact("How does a lightning conductor work?", "A thick conductor from a point above the building to a plate in the ground: a low-resistance path to earth, so the current bypasses the building.", "static-dangers"),
    # N7
    fact("Define an electric field.", "A region in which an electric charge experiences a force.", "electric-fields"),
    fact("Which way do field lines point?", "From positive to negative — the direction of the force on a positive charge.", "electric-fields"),
    fact("Field of a point charge?", "Radial straight lines, evenly spaced round the charge, outwards for +, inwards for −; spreading out, so weaker with distance.", "electric-fields"),
    fact("Field between parallel plates?", "Uniform: straight, parallel, equally spaced lines from the + plate to the − plate; the same strength everywhere between them.", "electric-fields"),
    fact("What does the spacing of field lines show?", "Strength: closer lines, stronger field.", "electric-fields"),
    fact("Can field lines cross?", "Never — the force at a point has only one direction.", "electric-fields"),
    # T1
    fact("The charging chain (word for word)?", "Friction → electrons transferred from A to B → B has gained electrons so is negative → A has lost electrons so is positive (equal amount).", "electron-force-chains"),
    fact("The moving-apart chain (word for word)?", "Same charge → like charges repel → a force on X directed away from Y → the force causes X to accelerate away from Y.", "electron-force-chains"),
    fact("Why is 'they repel so it moves away' not enough?", "It skips the force: name the force on the object, give its direction, and say the force causes an acceleration.", "electron-force-chains"),
    fact("Two charged objects attract; one is much lighter. What is the same and what differs?", "The forces are equal and opposite; the lighter one has the larger acceleration ($a = F/m$).", "electron-force-chains"),
    # T2
    fact("Four steps of induction?", "Neutral object, equal charges → the rod's field moves its electrons → near side opposite, far side same, still neutral overall → attraction on the nearer side wins.", "induction-explain"),
    fact("What must an induction diagram show?", "Both the induced charge on the near side AND the equal opposite charge on the far side.", "induction-explain"),
    fact("Why is a neutral object never repelled?", "Induction always puts the opposite charge on the near side, and the nearer force is the larger.", "induction-explain"),
    # T3
    fact("The spark chain?", "Charge builds up (object insulated) → pd grows → field strong enough for the air to conduct → electrons flow across the gap.", "sparks"),
    fact("Why is static worse on dry days?", "Moist air lets charge leak away; dry air is a better insulator so charge accumulates.", "sparks"),
    fact("Why touch a railing with a key first?", "The spark jumps between the key and the railing, not from your fingertip.", "sparks"),
    # T4
    fact("The fuelling 6-marker: the danger half?", "Friction transfers electrons → charge builds up on the insulated aircraft → large pd → spark → ignites fuel vapour → fire/explosion.", "fuelling-question"),
    fact("The fuelling 6-marker: the precaution half?", "Bonding cable (conductor): same potential, no pd, no spark. Earthing: charge flows to the ground, cannot build up. (Pump slowly: less charge per second.)", "fuelling-question"),
    fact("What is wrong with 'it is earthed so it is safe'?", "It gives the precaution without what it does: the charge flows away to earth and cannot build up to a pd that sparks.", "fuelling-question"),
    # T5
    fact("Sprayer: advantage + reason, pair 1?", "Fine even mist — the droplets all have the same charge and repel each other.", "sprayers-explain"),
    fact("Sprayer: advantage + reason, pair 2?", "Reaches all sides and less is wasted — the droplets are attracted to the earthed target, which has an induced opposite charge.", "sprayers-explain"),
    fact("Why is the target earthed?", "So it is at 0 V and the charged mist induces the opposite charge on its surface; electrons flow to or from earth to supply it.", "sprayers-explain"),
    # T6
    fact("Rules for drawing a field diagram?", "Arrows from + to −; lines never cross; point charge: radial and evenly spaced; plates: straight, parallel, equally spaced; closer lines = stronger.", "field-diagrams"),
    fact("What did the 2025 scheme give for plate field lines with the arrows reversed?", "1 of 2 marks: lines right, direction wrong.", "field-diagrams"),
    fact("Force on a negative charge in a field?", "Against the arrows (the lines show the force on a positive charge).", "field-diagrams"),
    # T7
    fact("Field explanation of repulsion?", "The rod has a field; the ball's charge is in it and experiences a force (away, for like charges); the force makes the ball accelerate away.", "fields-explain"),
    fact("Field explanation of a spark?", "As charge builds, the field gets stronger until it pulls electrons off air molecules; the air conducts and electrons flow across the gap.", "fields-explain"),
    fact("Why is the field strongest at a sharp point?", "The field lines bunch together at a point, so the air breaks down there first — the lightning conductor's tip.", "fields-explain"),
]
