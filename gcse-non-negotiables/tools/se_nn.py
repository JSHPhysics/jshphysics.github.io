"""
se_nn.py — Topic 11 (Static electricity): the non-negotiables N1–N8.
The whole topic is Physics-only (11.1P–11.10P), so every section carries P.

N1 Charging by friction        N5 Uses: sprayers
N2 Like and unlike charges     N6 Dangers and how they are reduced
N3 Explaining the phenomena    N7 Electric fields
N4 Earthing                    N8 Key words
"""

from revlib import (
    choice, diagram, explain, fact, group, mark_scheme, marks, numeric,
    practice, section, worked, written,
)
import se_diagrams as dg

# ---------------------------------------------------------------------
# N1 · Charging by friction
# ---------------------------------------------------------------------

section_n1 = section(
    "charging-friction", "nn", "Charging by friction: electrons move, nothing else", "11.1P, 11.2P",
    equations=[r"\text{gains electrons} \Rightarrow \text{negative}", r"\text{loses electrons} \Rightarrow \text{positive, equal size}"],
    blurb="Rub two insulators together and electrons are transferred from one to the other. The one that gains electrons is negative; the one that loses them is left positive by exactly the same amount. Protons never move and charge is never created.",
    tags=["P"],
    checklist=[
        "Explain how an insulator is charged by friction through the transfer of electrons",
        "State which object becomes negative and which positive, and that the charges are equal",
        "Explain why only insulators can be charged this way",
    ],
    parts=[
        explain(
            "What happens when you rub",
            diagram(dg.rubbing_svg(), 700, 250, "A polythene rod rubbed with a cloth: electrons move from the cloth to the rod.") +
            "<p>Every atom has positive protons in its nucleus and negative electrons around it. When two <b>insulators</b> are rubbed together, <b>friction</b> transfers <b>electrons</b> from one surface to the other. The material that <b>gains electrons</b> has more negative than positive charge: it is <b>negatively charged</b>. The material that <b>loses electrons</b> is left with more positive than negative: it is <b>positively charged</b>, by an <b>equal amount</b>, because every electron that left it arrived on the other.</p>"
            "<p>Three things the marks depend on: it is <b>electrons</b> that move (never protons, which are locked in the nucleus); charge is <b>transferred, not created</b>; and the cause is <b>friction</b> (rubbing). The June 2023 report (Q1(a)(ii)): \"many omitted friction\" — the two marks were electrons transferred from the base to the cloth, <i>and</i> friction as the cause.</p>"
            "<p><b>Why insulators:</b> the transferred electrons <b>stay where they land</b> because an insulator has no free electrons to carry charge away. Rub a metal rod held in your hand and the electrons flow straight through you to earth. The June 2023 scheme (Q1(b), 2 marks, any two): a person holds a metal star and rubs it with the charged cloth, and the cloth loses its charge because <b>electrons are transferred from the cloth to the metal</b>, <b>the metal is a conductor</b>, and <b>the electrons travel through the person to earth</b>. The star does not stay charged: it is earthed through the hand — \"friction charges insulators, not conductors\".</p>",
        ),
        worked(
            "The 2-mark explanation",
            "A student rubs a balloon on her jumper. The balloon becomes negatively charged. Explain how. (2 marks)",
            [
                "<b>Friction</b> between the balloon and the jumper transfers <b>electrons from the jumper to the balloon</b>.",
                "The balloon has <b>gained electrons</b>, so it has an excess of negative charge; the jumper has <b>lost</b> the same number and is left <b>positively charged</b>.",
            ],
        ),
        practice("Charging by friction", [
            written("se-n1-q1", "A polythene rod is rubbed with a cloth and becomes negatively charged. Explain what has happened. (2)",
                    marks(["<b>Friction</b> has transferred <b>electrons from the cloth to the rod</b>.", "The rod has <b>gained electrons</b> (negative); the cloth has <b>lost</b> the same number and is <b>positive</b>."]), lines=2),
            choice("se-n1-q2", "An acetate rod is rubbed and becomes positively charged. Which is correct?",
                   ["It gained protons", "It lost electrons to the cloth", "It gained electrons", "It lost protons"], 1,
                   "Only electrons move; positive means electrons have been lost."),
            written("se-n1-q3", "Explain why a metal rod held in the hand cannot be charged by rubbing. (2)",
                    marks(["A metal is a <b>conductor</b> with free electrons…", "…so any electrons transferred <b>flow through the metal and the hand to earth</b> at once instead of staying on the rod."]), lines=2),
            choice("se-n1-q4", "A cloth loses 10¹⁰ electrons to a rod. The charge on the cloth is…",
                   ["negative, 10¹⁰ electrons' worth", "positive, equal in size to the rod's negative charge", "zero", "positive, but smaller than the rod's charge"], 1,
                   "Transferred, not created: equal and opposite."),
            written("se-n1-q5", "State what is transferred when an insulator is charged by friction, and what is never transferred. (2)",
                    marks(["<b>Electrons</b> are transferred (from one material to the other).", "<b>Protons</b> are never transferred — they are fixed in the nuclei."]), lines=2),
            written("se-n1-q6", "A metal ball on an insulating stand is touched with a negatively charged rod. Explain how the ball becomes charged. (2)",
                    marks(["Electrons move <b>from the rod into the ball</b> on contact (charging by conduction, not friction).", "The metal is a <b>conductor</b>, so the electrons spread over the whole ball, which is left negatively charged."]), lines=2),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N2 · Like and unlike charges
# ---------------------------------------------------------------------

section_n2 = section(
    "charge-forces", "nn", "Like charges repel, unlike charges attract", "11.3P",
    equations=[r"+\,+ \text{ or } -\,- \text{: repel}", r"+\,- \text{: attract}"],
    blurb="Two charged objects exert a force on each other without touching. Same sign: they push apart. Opposite signs: they pull together. Each object feels the force, and a force is what makes it accelerate.",
    tags=["P"],
    checklist=[
        "State the rule for forces between like and unlike charges",
        "Describe how to test the charge on an object with a known charged rod",
        "Say that both objects feel an equal and opposite force (an interaction pair)",
    ],
    parts=[
        explain(
            "The rule and the test",
            diagram(dg.forces_svg(), 650, 250, "Two hanging charged balls: like charges push apart, unlike charges pull together. Both balls feel the force.") +
            "<p><b>Like charges repel; unlike charges attract.</b> The force is a <b>non-contact</b> force acting through the <b>electric field</b> around each charge (N7). It gets <b>stronger as the charges get closer</b> and as the charges get larger. Both objects feel it — equal in size, opposite in direction, an interaction pair (Topic 9) — so a light object accelerates more than a heavy one ($a = F/m$), but both are pushed.</p>"
            "<p><b>Testing a charge</b> (3 marks in Nov 2020 2H Q4(a)(iii)): <b>hang the object by its thread / hold it by an insulating handle so it is not discharged</b>; <b>bring a rod of known charge near</b> it; <b>repulsion</b> proves the object has the <b>same</b> charge as the rod. If the question asks whether it is positive, negative or uncharged (June 2026 Q1(c)), test with both a positive and a negative rod: repelled by one → that sign; attracted by both → uncharged. Attraction does not prove the opposite charge — an <b>uncharged</b> object is also attracted (by induction, N3). The June 2024 scheme (Q1(a)) used exactly this: three objects <b>all stated to be charged</b>, with X attracted to Y and Z repelled from Y — the repulsion fixes Z's sign, and because X is known to be charged its attraction fixes X's.</p>"
            "<p>A force on an object makes it <b>accelerate</b> (Topic 2). Write the whole chain, because each link has been a mark somewhere: <b>the ball is in the rod's electric field</b> (the mark in 2018 Q4(c)(i) and 2025 Q4(b)(ii)); <b>the charges are alike, so they repel</b> — a <b>force</b> on the ball <b>away from</b> the rod; so the ball <b>accelerates away</b> (T1). Saying it accelerates is the physics and never loses a mark; beyond \"they repel\" the schemes also credit the <b>result the question asks about</b> — 2019 Q1(a)(ii): \"like charged drops repel (1) so the spray is wider (1)\".</p>",
        ),
        worked(
            "Identify the charge",
            "A rod known to be negative is brought near a light ball hanging on a thread. The ball moves away. State the charge on the ball and explain your answer. (2 marks)",
            [
                "The ball is <b>negatively charged</b>.",
                "It is <b>repelled</b>, and only <b>like</b> charges repel — if it had been positive or uncharged it would have been attracted.",
            ],
        ),
        practice("Forces between charges", [
            choice("se-n2-q1", "Two positively charged balloons are brought together. They…",
                   ["attract", "repel", "neither — they are not touching", "become neutral"], 1,
                   "Like charges repel."),
            written("se-n2-q2", "A charged rod attracts a hanging ball. A student says this proves the ball has the opposite charge. Explain why the student may be wrong. (2)",
                    marks(["An <b>uncharged</b> object is also attracted to a charged rod (by induction).", "Only <b>repulsion</b> proves a charge, because only like charges repel."]), lines=2),
            choice("se-n2-q3", "As two charged objects are moved closer together, the force between them…",
                   ["decreases", "increases", "stays the same", "becomes zero"], 1,
                   "Closer → stronger field → larger force."),
            written("se-n2-q4", "Two hanging balls, each negatively charged, hang apart from each other. Explain why. (2)",
                    marks(["Like charges <b>repel</b>, so there is a <b>force on each ball</b> directed away from the other.", "Each ball <b>accelerates away</b> from the other until the pull of its thread balances the repulsion, so they hang at an angle."]), lines=2),
            choice("se-n2-q5", "Ball A has a large positive charge and ball B a small negative charge. Which is true about the forces?",
                   ["A pushes B harder than B pushes A", "The forces on A and B are equal in size and opposite (attractive)", "Only B feels a force", "They repel"], 1,
                   "An interaction pair: equal and opposite."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N3 · Explaining the phenomena
# ---------------------------------------------------------------------

section_n3 = section(
    "static-phenomena", "nn", "Explaining shocks, lightning and attraction by induction", "11.4P",
    equations=[r"\text{every explanation: where the electrons move, and why}"],
    blurb="Three things the spec names — shocks from everyday objects, lightning, and a charged comb picking up paper or a balloon sticking to a wall. Each is explained the same way: say where electrons move and what charge that leaves.",
    tags=["P"],
    checklist=[
        "Explain a shock from a car door or a jumper in terms of electron movement",
        "Explain lightning as charge build-up and a huge discharge",
        "Explain attraction by induction: the near side of a neutral object gets the opposite charge",
    ],
    parts=[
        explain(
            "Three phenomena, one method",
            diagram(dg.induction_svg(), 660, 240, "A negatively charged comb held over a scrap of paper: electrons in the paper are pushed to the far side, the near side is left positive, and the paper is attracted.") +
            "<p><b>Shocks:</b> walking on a carpet (or sliding off a car seat) rubs insulators together: <b>friction transfers electrons</b> and your body builds up a charge. When you touch a door handle (a <b>conductor connected to earth</b>) the excess <b>electrons flow</b> between you and the metal in a sudden rush — a small <b>spark</b> that you feel as a shock. Which way they flow depends on the sign of your charge; either way the charge is <b>discharged</b>.</p>"
            "<p><b>Lightning:</b> inside a storm cloud, ice and water droplets rub against each other and <b>friction separates charge</b>; the bottom of the cloud usually becomes <b>negative</b>. The charge builds until the <b>pd between the cloud and the ground</b> (or another cloud) is so large that the <b>air conducts</b>: a huge flow of electrons — lightning — discharges it (T3).</p>"
            "<p><b>Attraction by induction</b> (the comb and the paper, the balloon on the wall): the paper is <b>neutral</b>, but the negative comb <b>repels the electrons</b> in the paper to the <b>far side</b>, leaving the <b>near side positive</b>. The near, positive side is <b>attracted</b> to the comb and the far, negative side is <b>repelled</b> — but the attraction is on the <b>nearer</b> charges, so it is the <b>larger</b> force, and the paper is pulled towards the comb. The paper stays neutral overall: the charges have moved, not changed. The 2023 report (Q1(c)): the fully correct diagram shows <b>both</b> the induced negative near a positive object <b>and</b> the induced positive on the far side — \"the total numbers of positive and negative charges still balance\".</p>",
        ),
        worked(
            "Balloon on a wall",
            "A balloon is rubbed on a jumper and then sticks to a wall. Explain why. (3 marks)",
            [
                "Rubbing transfers <b>electrons</b> from the jumper to the balloon, so the balloon is <b>negatively charged</b>.",
                "Near the wall, the balloon's charge <b>repels electrons</b> in the wall's surface away, leaving the surface nearest the balloon <b>positively charged</b> (induced charge).",
                "Unlike charges <b>attract</b>: there is a force <b>on the balloon</b> towards the induced positive surface, which holds it on the wall.",
            ],
        ),
        practice("Explaining the phenomena", [
            written("se-n3-q1", "Explain why a person sometimes gets a shock when touching a metal door handle after walking across a carpet. (3)",
                    mark_scheme([
                        ("Charging", "<b>Friction</b> between shoes and carpet transfers <b>electrons</b>, so the person builds up a charge."),
                        ("Discharge", "The handle is a <b>conductor</b> (connected to earth); when touched, <b>electrons flow</b> suddenly between the person and the handle."),
                        ("Shock", "The sudden flow of charge — a small <b>spark</b> — is felt as the shock, and the person is left neutral."),
                    ]), lines=4),
            written("se-n3-q2", "Explain how lightning occurs. (3)",
                    mark_scheme([
                        ("Charging", "Ice and water particles in the cloud rub together: <b>friction</b> separates charge (electrons transferred), and the base of the cloud becomes (usually) <b>negative</b>."),
                        ("Build-up", "The charge builds until there is a very large <b>pd between the cloud and the ground</b>."),
                        ("Discharge", "The electric field becomes strong enough for the <b>air to conduct</b>: a huge flow of <b>electrons</b> — the lightning — discharges the cloud."),
                    ]), lines=4),
            choice("se-n3-q3", "A negatively charged comb is held above small pieces of paper. Which is correct about the paper?",
                   ["It is negatively charged, so it is repelled", "Electrons in it are pushed to the far side, so the near side is positive and it is attracted", "It becomes positively charged overall", "Protons move to the near side"], 1,
                   "Induction: electrons move within the neutral paper; protons never move."),
            written("se-n3-q4", "A positively charged rod is held near a neutral metal sphere on an insulating stand. Describe the charge distribution on the sphere and explain why the sphere is attracted to the rod. (3)",
                    mark_scheme([
                        ("Induced charge", "<b>Electrons</b> in the sphere are <b>attracted towards the rod</b>, so a <b>negative charge is induced</b> on the sphere…"),
                        ("Where", "…on the side <b>closest to the rod</b>; the far side is left positive and the sphere is still neutral overall."),
                        ("Force", "<b>Opposite charges attract</b>: a force on the sphere towards the rod (June 2018 2H Q4(a)(ii): \"induced (1) on the part closest (1) opposite charges attract (1)\"). The attraction wins because the negative side is closer than the positive side."),
                    ]), lines=4),
            choice("se-n3-q5", "Why is a neutral object attracted to a charged object but never repelled?",
                   ["Neutral objects have no electrons", "The charges in it separate so the opposite charge is always on the nearer side, and the nearer force is the larger", "Only positive objects can be repelled", "Neutral objects are always lighter"], 1,
                   "Induction always puts the opposite charge nearest."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N4 · Earthing
# ---------------------------------------------------------------------

section_n4 = section(
    "earthing", "nn", "Earthing: removing the excess charge", "11.5P",
    equations=[r"\text{negative object: electrons flow to earth}", r"\text{positive object: electrons flow from earth}"],
    blurb="Earthing connects a charged object to the ground by a conductor. Electrons flow until the excess charge is gone — down to earth from a negative object, up from earth to a positive one. It is always the electrons that move.",
    tags=["P"],
    checklist=[
        "Explain how earthing removes excess charge by the movement of electrons",
        "State the direction electrons flow for a negatively and a positively charged object",
        "Explain why the path must be a conductor",
    ],
    parts=[
        explain(
            "Which way the electrons go",
            diagram(dg.earthing_svg(), 670, 255, "Earthing a negative object and a positive object: the electrons move in opposite directions, and both objects end up neutral.") +
            "<p>The Earth is so large that it can take or give <b>any number of electrons</b> without being noticeably charged. Connect a charged object to it with a <b>conductor</b> (a wire, a metal pipe, a damp hand) and:</p>"
            "<ul><li>a <b>negatively</b> charged object has excess electrons; they <b>repel each other</b> and flow <b>down the conductor to earth</b> until none are in excess;</li>"
            "<li>a <b>positively</b> charged object is short of electrons; electrons are <b>attracted up from earth</b> through the conductor until the shortage is made up.</li></ul>"
            "<p>Either way the object is left <b>neutral</b>: it has been <b>discharged</b>. Say which way the <b>electrons</b> move — never \"the positive charge flows to earth\". The path must be a conductor: through an insulator the electrons cannot move, which is why charge stays on a plastic rod. The June 2025 scheme (Q4(b)(iv), \"explain why the metal tube does not become charged\", 2 marks): <b>the metal is a conductor</b> (1) and it is <b>connected to earth</b> (1) — \"charge moves through the metal / tube / wire\". Both words, conductor and earth, are needed for both marks.</p>",
        ),
        worked(
            "Earthing a positive object",
            "A metal sphere is positively charged. A wire is connected from the sphere to earth. Explain what happens. (2 marks)",
            [
                "The sphere is short of electrons, so <b>electrons flow up the wire from the earth</b> into the sphere (attracted by the positive charge).",
                "They flow until the sphere has <b>equal numbers of positive and negative charges</b>: it is discharged / neutral.",
            ],
        ),
        practice("Earthing", [
            written("se-n4-q1", "A negatively charged metal plate is connected to earth. Explain what happens to its charge. (2)",
                    marks(["The excess <b>electrons flow through the conductor to earth</b> (they repel each other and the earth can accept them).", "The plate is left with no excess charge — it is <b>neutral / discharged</b>."]), lines=2),
            choice("se-n4-q2", "A positively charged object is earthed. Which is correct?",
                   ["Positive charge flows to earth", "Protons flow to earth", "Electrons flow from earth to the object", "Nothing happens"], 2,
                   "Only electrons move; they come up from earth to cancel the positive charge."),
            written("se-n4-q3", "Explain why a charged plastic ruler cannot be discharged by touching it with a plastic wire. (1)",
                    marks(["Plastic is an <b>insulator</b>: electrons cannot flow through it, so there is no path for the charge to reach earth."]), lines=1),
            written("se-n4-q4", "Explain why charge flows from an earthed metal tube to the ground, but not from an identical tube on an insulating stand. (2)",
                    marks(["The earthed tube is a <b>conductor connected to earth</b>, so electrons have a path and <b>flow along the wire</b> — to earth if the tube is negative, up from earth if it is positive.", "On an insulating stand there is <b>nowhere for the charge to go</b>, so it stays on the tube."]), lines=2),
            choice("se-n4-q5", "Why does charge flow to earth rather than building up on the wire?",
                   ["The wire is an insulator", "The Earth is so large it can take or give electrons without becoming noticeably charged", "Earth is positively charged", "Wires repel electrons"], 1,
                   "Earth acts as an unlimited reservoir of charge."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N5 · Uses
# ---------------------------------------------------------------------

section_n5 = section(
    "static-uses", "nn", "Uses: insecticide and paint sprayers", "11.6P",
    equations=[r"\text{droplets repel one another} \Rightarrow \text{fine, even spray}", r"\text{droplets attracted to the target} \Rightarrow \text{even coat, less waste}"],
    blurb="Give the spray a charge and two things happen: the droplets repel each other into a fine, even mist, and they are attracted to the (earthed or oppositely charged) target — even its back. Three advantages, each with its reason.",
    tags=["P"],
    checklist=[
        "Explain how an electrostatic sprayer works",
        "Give the advantages of charging the droplets, each with the reason",
        "Say why the target is earthed or given the opposite charge",
    ],
    parts=[
        explain(
            "How a sprayer works",
            diagram(dg.sprayer_svg(), 760, 260, "An electrostatic paint sprayer: the charged droplets spread out and are drawn onto the earthed car body.") +
            "<ol><li>The nozzle is connected to a high pd, so every droplet leaving it carries the <b>same charge</b>.</li>"
            "<li><b>Like charges repel</b>: the droplets push one another apart and <b>spread out into a fine, even mist</b> — no clumps, no drips.</li>"
            "<li>The target (car body, plant) is <b>earthed</b>, or given the <b>opposite charge</b>. The charged mist <b>induces the opposite charge</b> on the target's surface, so the droplets are <b>attracted</b> to it — including the <b>sides and back</b>, where the spray would not otherwise reach.</li></ol>"
            "<table class='tbl'><tr><th>Advantage</th><th>Because</th></tr>"
            "<tr><td><b>even coat</b></td><td>the droplets repel each other into a fine, evenly spread mist</td></tr>"
            "<tr><td><b>reaches all round</b> (the back of the leaf, the underside of the car)</td><td>the droplets are attracted to the oppositely charged surface, not just carried by the air</td></tr>"
            "<tr><td><b>less paint / insecticide wasted</b></td><td>the droplets are pulled to the target instead of drifting past it (less chemical in the air, cheaper)</td></tr></table>"
            "<p>Say both halves — the repulsion <i>between droplets</i> and the attraction <i>to the target</i>. \"The paint is charged so it sticks\" is not an explanation.</p>",
        ),
        worked(
            "The 3-mark explanation",
            "Explain how giving the droplets a charge improves a crop sprayer. (3 marks)",
            [
                "All the droplets have the <b>same charge</b>, so they <b>repel one another</b> and spread into a <b>fine, even mist</b>.",
                "The droplets are <b>attracted</b> to the plants, which are earthed and gain an <b>induced opposite charge</b>, so the insecticide reaches <b>all sides</b> of the leaves.",
                "<b>Electrons move between the earth and the leaf</b> to give it this induced charge; <b>opposite charges attract</b>, so the droplets are pulled onto <b>the back of the leaf</b> as well as the front (the June 2022 2H Q1(c) points — \"less is wasted\" is a sensible advantage but is not one of its seven).",
            ],
        ),
        practice("Uses", [
            written("se-n5-q1", "Explain why the droplets from an electrostatic paint sprayer spread out into a fine mist. (2)",
                    marks(["All the droplets carry the <b>same charge</b>.", "<b>Like charges repel</b>, so the droplets push one another apart and spread evenly."]), lines=2),
            choice("se-n5-q2", "Why is the car body earthed when it is spray-painted with charged paint?",
                   ["To make the paint dry faster", "So the wire conducts electrons to or from earth: charge cannot accumulate on the car (which would repel the next droplets), and the car gains an induced opposite charge that attracts them", "To stop the car moving", "So the paint loses its charge in the air"], 1,
                   "The June 2019 2H scheme (Q1(a)(iii)): \"the metal wire can conduct electrons (from earth) (1) so prevent charge accumulating on the object (1)\" — plus the induced opposite charge that attracts the droplets to every side."),
            written("se-n5-q3", "Give two advantages of using charged droplets in an insecticide sprayer, with a reason for each. (4)",
                    mark_scheme([
                        ("Advantage 1", "An <b>even</b> spray / fine mist…"),
                        ("Reason 1", "…because the droplets all have the same charge and <b>repel each other</b>."),
                        ("Advantage 2", "Reaches <b>all sides</b> of the plant, and <b>less is wasted</b>…"),
                        ("Reason 2", "…because the droplets are <b>attracted</b> to the earthed (oppositely charged) plant rather than drifting past."),
                    ]), lines=4),
            choice("se-n5-q4", "Charged paint droplets reach the back of a metal panel. Why?",
                   ["The air carries them round", "They are attracted to the induced opposite charge on the whole surface, including the back", "Paint is magnetic", "They are heavier when charged"], 1,
                   "Attraction works all round the earthed object."),
            written("se-n5-q5", "A gardener uses a sprayer without charging the droplets. State two disadvantages compared with an electrostatic sprayer. (2)",
                    marks(["Uneven coverage — the droplets do not spread out evenly and the <b>undersides of leaves are missed</b>.", "More insecticide <b>wasted</b> (drifts away in the air) — more chemical needed and more pollution."]), lines=2),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N6 · Dangers and earthing
# ---------------------------------------------------------------------

section_n6 = section(
    "static-dangers", "nn", "Dangers of static, and how earthing removes them", "11.7P, 11.8P",
    equations=[r"\text{charge builds} \rightarrow \text{pd grows} \rightarrow \text{spark} \rightarrow \text{fire}", r"\text{bonding + earthing: no pd, no spark}"],
    blurb="Fuel rushing through a hose charges it by friction. Let the charge build and a spark can jump — into fuel vapour. The cure is a conducting path: bond the two vehicles together so they stay at the same potential, and earth them so the charge drains away.",
    tags=["P"],
    checklist=[
        "Explain why refuelling an aircraft or tanker is dangerous because of static",
        "Explain how bonding and earthing remove the danger",
        "Describe how a lightning conductor protects a building",
    ],
    parts=[
        explain(
            "The danger and the cure",
            diagram(dg.fuelling_svg(), 680, 240, "Refuelling an aircraft: the bonding line keeps tanker and aircraft at the same potential; the earth wire lets the charge drain away.") +
            "<p><b>The danger:</b> as fuel <b>flows through the hose</b> there is <b>friction</b> between the fuel and the pipe, which <b>transfers electrons</b> — the fuel (and the aircraft) becomes charged. The charge <b>builds up</b> because the aircraft stands on insulating tyres. A large charge means a large <b>pd</b> between the aircraft and the tanker (or the ground). If the pd gets high enough, the air breaks down and a <b>spark</b> jumps across the gap. Fuel <b>vapour</b> is explosive, so a spark can cause a <b>fire or explosion</b>.</p>"
            "<p><b>The cure (11.8P):</b> before the hose is connected, a <b>bonding line</b> — a conducting cable — is clipped between the tanker and the aircraft, and both are connected to <b>earth</b>. Now any charge that builds up <b>flows through the conductor</b> instead of building up: the two vehicles stay at the <b>same potential</b>, so there is <b>no pd</b> between them and <b>no spark</b>; and the earth connection drains the charge away. The same idea protects fuel tankers at petrol stations (the pump nozzle is earthed through the hose) and operating theatres (conducting floors).</p>"
            "<p><b>Lightning conductors:</b> a thick copper strip from a spike above the building down to a metal plate in the ground. If lightning strikes it provides a <b>low-resistance path to earth</b>, so the huge current goes through the conductor rather than through the building; the field is strongest at the sharp point, so the air breaks down there first and the strike is led to the conductor rather than the roof.</p>"
            "<p>Give the reason with each step: \"it is earthed\" alone is a precaution without an explanation; \"it is earthed <b>so the charge flows away and cannot build up to produce a spark</b>\" is the answer. (The danger-and-precaution statements have not yet been examined on a 2H paper, 2018–2025.)</p>",
        ),
        worked(
            "The 4-mark fuelling question",
            "Explain why static electricity can be dangerous when an aircraft is refuelled, and how the danger is reduced. (4 marks)",
            [
                "<b>Friction</b> between the fuel and the hose <b>transfers electrons</b>, so charge <b>builds up</b> on the aircraft (which is insulated from the ground by its tyres).",
                "The charge produces a large <b>pd</b> between the aircraft and the tanker; a <b>spark</b> can jump across, which could <b>ignite the fuel vapour</b>.",
                "A <b>bonding line</b> (conductor) connects the aircraft to the tanker, so charge flows between them and they stay at the <b>same potential</b> — no pd, no spark.",
                "Both are also <b>earthed</b>, so the charge <b>flows away to the ground</b> as fast as it is made and cannot build up.",
            ],
        ),
        practice("Dangers and earthing", [
            written("se-n6-q1", "Explain why fuel flowing through a hose can cause a spark. (3)",
                    mark_scheme([
                        ("Friction", "<b>Friction</b> between the moving fuel and the hose <b>transfers electrons</b>."),
                        ("Build-up", "Charge <b>builds up</b> (the vehicle is insulated from the ground), creating a large <b>pd</b> between the vehicle and nearby objects."),
                        ("Spark", "When the pd is large enough the air conducts and a <b>spark</b> jumps across — which can ignite fuel vapour."),
                    ]), lines=4),
            written("se-n6-q2", "Explain how connecting a tanker to the aircraft with a conducting cable before refuelling reduces the danger. (2)",
                    marks(["Charge can <b>flow between them through the conductor</b> instead of building up, so they stay at the <b>same potential</b>.", "With <b>no pd</b> between them there is <b>no spark</b>."]), lines=2),
            choice("se-n6-q3", "Why does charge build up on an aircraft during refuelling rather than flowing away?",
                   ["Aircraft are made of plastic", "Its rubber tyres insulate it from the ground, so the charge has nowhere to go", "Fuel is an excellent conductor", "The air is a conductor"], 1,
                   "No conducting path to earth until one is provided."),
            written("se-n6-q4", "Describe how a lightning conductor protects a tall building. (2)",
                    marks(["A thick copper conductor runs from a <b>point above the building to a plate in the ground</b>.", "It provides a <b>low-resistance path to earth</b>, so a strike's current flows through it rather than through the building (the point is where the field is strongest, so the strike is led there)."]), lines=2),
            written("se-n6-q5", "A student writes: \"The tanker is earthed, so it is safe.\" Explain what is missing from this answer. (2)",
                    marks(["It does not say <b>what earthing does</b>: the earth wire lets the <b>charge flow away to the ground</b>…", "…so charge <b>cannot build up</b> to give a pd large enough for a <b>spark</b> that could ignite the fuel vapour."]), lines=2),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N7 · Electric fields
# ---------------------------------------------------------------------

section_n7 = section(
    "electric-fields", "nn", "Electric fields: the definition and the two diagrams", "11.9P, 11.10P",
    equations=[r"\text{field: a region where a charge experiences a force}", r"\text{lines from + to −; closer lines = stronger field}"],
    blurb="An electric field is a region where an electric charge experiences a force. Draw it with field lines: radial around a point charge, parallel and evenly spaced between two plates, arrows from positive to negative. The field is the reason charged objects affect each other without touching.",
    tags=["P"],
    checklist=[
        "Define an electric field",
        "Draw the field around a point charge and between parallel plates, with directions",
        "Use the spacing of field lines to compare field strength",
        "Explain static phenomena in terms of fields",
    ],
    parts=[
        explain(
            "Definition, diagrams and rules",
            diagram(dg.fields_svg(), 660, 270, "The two field patterns the spec asks for.") +
            "<p><b>Definition</b> (11.9P): an electric field is <b>a region in which an electric charge experiences a force</b>. The June 2024 scheme (Q1(b), 1 mark): \"<b>a region where (electric) charge experiences a force</b>\"; also accepted: \"where a charge experiences attraction / repulsion\", \"where the direction of the force on a positive charge is shown\"; \"electricity\" ignored.</p>"
            "<p><b>Field lines</b> show the <b>direction of the force on a positive charge</b>: they point <b>away from positive</b> and <b>towards negative</b> (the 2024 scheme's mark for Q1(c)(i)). Where the lines are <b>closer together</b> the field is <b>stronger</b> — near a point charge; where they <b>spread out</b> (diverge) the field is weaker (Q1(c)(ii): \"field lines get further apart as x increases\"). Lines <b>never cross</b> or touch.</p>"
            "<table class='tbl'><tr><th>Point charge</th><th>Parallel plates</th></tr>"
            "<tr><td><b>radial</b>: straight lines out from (or in to) the charge, evenly spaced round it; arrows outwards for +, inwards for −; the field gets <b>weaker with distance</b> as the lines spread</td><td><b>uniform</b>: straight, <b>parallel</b>, <b>equally spaced</b> lines from the + plate to the − plate, at right angles to the plates; the <b>same strength</b> everywhere between them (the lines bulge only at the edges)</td></tr></table>"
            "<p>The June 2025 scheme (Q4(a)): straight lines with arrows <b>from the positive plate to the negative plate</b> — 2 marks; correct lines with the arrows the wrong way — 1. The schemes ask for <b>at least three</b> straight lines (2025: two); draw four or five, equally spaced, straight (June 2022 Q1(a): \"do not allow curved lines\"), with an arrowhead on each.</p>"
            "<p><b>Why fields explain static</b> (11.10P): a charged object has a field around it; any other charge in that region feels a force — attraction or repulsion — without contact. The field of a charged comb acts on the electrons in a piece of paper and moves them (induction); if a field becomes strong enough it pulls electrons off air molecules, the air conducts, and a spark jumps (T7).</p>",
        ),
        worked(
            "Describe the field",
            "Describe the electric field around a negatively charged sphere. (3 marks)",
            [
                "The field lines are <b>radial</b>: straight lines pointing <b>towards the centre</b> of the sphere (the direction of the force on a positive charge).",
                "They are <b>evenly spaced</b> round the sphere, so the field has the same strength at the same distance in every direction.",
                "The lines get <b>further apart</b> with distance, so the field is <b>strongest near the surface</b> and weakens further away.",
            ],
        ),
        practice("Electric fields", [
            written("se-n7-q1", "State what is meant by an electric field, and what the direction of a field line shows. (2)",
                    marks(["A <b>region</b> in which an <b>electric charge experiences a force</b>.", "The line shows the <b>direction of the force on a positive charge</b>."]), lines=2),
            choice("se-n7-q2", "In which direction do electric field lines point?",
                   ["From negative to positive", "From positive to negative (the direction of the force on a positive charge)", "Clockwise", "It depends on the current"], 1,
                   "Away from +, towards −."),
            written("se-n7-q3", "Describe the electric field between two oppositely charged parallel plates. (3)",
                    mark_scheme([
                        ("Shape", "Straight, <b>parallel</b> lines at right angles to the plates."),
                        ("Direction", "From the <b>positive plate to the negative plate</b>."),
                        ("Strength", "<b>Equally spaced</b>, so the field is <b>uniform</b> — the same strength everywhere between the plates."),
                    ]), lines=4),
            choice("se-n7-q4", "Field lines around a point charge get further apart with distance. This shows that…",
                   ["the field gets stronger", "the field gets weaker", "the charge is negative", "the field is uniform"], 1,
                   "Line spacing shows strength: spread out = weaker."),
            written("se-n7-q5", "A student draws field lines between parallel plates that cross each other. Explain why this is wrong. (1)",
                    marks(["A field line shows the direction of the force on a charge at that point; it can only have <b>one direction</b>, so lines <b>never cross</b>."]), lines=1),
            written("se-n7-q6", "Use the idea of an electric field to explain why a charged balloon can attract a piece of paper without touching it. (2)",
                    marks(["The balloon's charge produces an <b>electric field</b> in the region around it.", "The paper is in that region, so the charges in it <b>experience a force</b>: the electrons in it are moved (pushed away by a negative balloon, pulled nearer by a positive one), so the near side has the opposite charge and is attracted."]), lines=2),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N8 · Key words
# ---------------------------------------------------------------------

DEFINITIONS = [
    ("Static electricity", "Charge that <b>stays on an insulator</b> (or an insulated conductor) rather than flowing.", "\"electricity that does not move\""),
    ("Charging by friction", "Rubbing two <b>insulators</b> together <b>transfers electrons</b> from one to the other; one is left negative, the other equally positive.", "\"rubbing makes charge\""),
    ("Negatively charged", "Has <b>gained electrons</b> (more electrons than protons).", "\"has negative protons\""),
    ("Positively charged", "Has <b>lost electrons</b> (fewer electrons than protons).", "\"has gained protons\""),
    ("Induction", "A charged object <b>moves the electrons</b> within a nearby neutral object, so the <b>near side gets the opposite charge</b> and is attracted.", "\"the charge jumps across\""),
    ("Earthing", "Connecting a charged object to the ground with a <b>conductor</b> so <b>electrons flow</b> to or from earth and the excess charge is removed.", "\"touching the ground\""),
    ("Discharge", "The <b>removal</b> of excess charge — by earthing or by a spark.", "\"losing electricity\""),
    ("Spark", "A sudden <b>flow of electrons through the air</b> when the pd across a gap is large enough for the air to conduct.", "\"a bit of lightning\""),
    ("Bonding (bonding line)", "A <b>conductor connecting</b> two objects so that they stay at the <b>same potential</b> and no spark can jump between them.", "\"a safety wire\""),
    ("Electric field", "A <b>region</b> in which an <b>electric charge experiences a force</b>.", "\"where the electricity is\""),
    ("Field line", "A line showing the <b>direction of the force on a positive charge</b>; from + to −; closer lines mean a stronger field; lines never cross.", "\"the path the charge takes\""),
    ("Uniform field", "A field with the <b>same strength and direction everywhere</b>: parallel, equally spaced lines (between parallel plates).", "\"a straight field\""),
    ("Radial field", "The field of a <b>point charge</b>: lines straight out from (or in to) the charge, weakening with distance.", "\"a round field\""),
]


def definitions_table():
    html = "<table class='tbl'><tr><th>Term</th><th>What to write (mark-scheme form)</th><th>Not this</th></tr>"
    for term, definition, wrong in DEFINITIONS:
        html += "<tr><td><b>" + term + "</b></td><td>" + definition + "</td><td>" + wrong + "</td></tr>"
    html += "</table>"
    return html


section_keywords = section(
    "keywords-static", "nn", "Key words: state what is meant by…", "11.1P–11.10P",
    equations=[r"\text{definition, word for word}"],
    blurb="One-mark definitions in the form of words the mark schemes credit. The bold words are the ones the marks are attached to.",
    tags=["P"],
    checklist=[
        "Define charging by friction, negative and positive charge, induction",
        "Define earthing, discharge, spark and bonding",
        "Define electric field, field line, uniform and radial fields",
    ],
    parts=[
        explain("The definitions", "<p>\"<b>State what is meant by</b>\" asks for the definition. Learn these as sentences.</p>" + definitions_table()),
        practice("Key words", [
            written("se-kw-q1", "State what is meant by an electric field. (1)",
                    marks(["A <b>region</b> in which an <b>electric charge experiences a force</b>."]), lines=1),
            written("se-kw-q2", "State what is meant by earthing a charged object. (1)",
                    marks(["Connecting it to the ground by a <b>conductor</b> so that <b>electrons flow</b> to or from earth and the excess charge is removed."]), lines=1),
            choice("se-kw-q3", "Which statement defines a negatively charged object?",
                   ["It has gained protons", "It has gained electrons", "It has lost electrons", "It has no electrons"], 1,
                   "Negative = extra electrons."),
            written("se-kw-q4", "State what is meant by attraction by induction. (1)",
                    marks(["A charged object <b>moves the electrons within a nearby neutral object</b> (without touching), so the near side gets the <b>opposite charge</b>."]), lines=1),
            written("se-kw-q5", "State what a field line shows. (1)",
                    marks(["The <b>direction of the force on a positive charge</b> at that point (and, by its spacing, the strength of the field)."]), lines=1),
            choice("se-kw-q6", "What is a bonding line used for during refuelling?",
                   ["To hold the hose in place", "To connect the two vehicles with a conductor so they stay at the same potential and no spark can jump", "To charge the fuel", "To measure the fuel"], 1,
                   "Same potential, no pd, no spark."),
        ]),
    ],
)

FACTS_KW = [fact("State what is meant by: " + term[0].lower() + term[1:] + ".", definition, "keywords-static") for term, definition, wrong in DEFINITIONS]

SECTIONS = [section_n1, section_n2, section_n3, section_n4, section_n5, section_n6, section_n7, section_keywords]
