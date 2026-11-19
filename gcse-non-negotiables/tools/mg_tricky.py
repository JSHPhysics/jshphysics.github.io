"""
mg_tricky.py — Topic 12 (Magnetism and the motor effect): the tricky
bits T1–T8 and the flashcards.

T1 Explaining attraction and repulsion     T5 Fleming's rule on diagrams [H]
T2 Is it a magnet?                         T6 F = BIl the hard way [H]
T3 Drawing and marking field diagrams      T7 The d.c. motor [H, P]
T4 The Earth as a magnet                   T8 The electromagnet investigation
"""

from revlib import (
    choice, diagram, ewau, explain, fact, group, mark_scheme, marks, numeric,
    practice, section, worked, written,
)
import mg_diagrams as dg
from mg_nn import WIRE_CHAIN, chain_list

# The author's standard chain for the motor effect in a motor, word for
# word from simple-motor/src/build.mjs (EXAM.motor). Keep identical.
MOTOR_CHAIN = [
    "There is a current in the coil.",
    "This creates a magnetic field around the coil.",
    "This interacts with the permanent magnetic field.",
    "This causes a resultant force on the coil.",
    "The direction of the force is opposite on either side of the coil.",
    "So the coil rotates.",
]

# ---------------------------------------------------------------------
# T1 · Explaining attraction and repulsion
# ---------------------------------------------------------------------

section_t1 = section(
    "magnet-force-chains", "tricky", "Explaining why magnets move: fields interact → force on X → X accelerates", "12.1, 12.11",
    equations=[r"\text{fields interact} \rightarrow \text{force on X} \rightarrow \text{X accelerates (or is held)}"],
    blurb="\"Explain why the magnet moves away\" is not answered by \"like poles repel\". The marks are on the chain: the two magnetic fields interact (the Higher-only link, 12.11), so there is a force on the magnet (say which one, and which way), so it accelerates — or, if it floats or is held, the force balances another force. Same shape as the Topic 11 chain for charges.",
    checklist=[
        "Write the chain for a magnet moving away from (or towards) another",
        "Write the chain for a magnet held still: the magnetic force balances the weight",
        "Say which object the force acts on, and which way",
    ],
    parts=[
        explain(
            "The chain, and where the marks are",
            "<table class='tbl'><tr><th>Situation</th><th>Chain (each link a mark)</th></tr>"
            "<tr><td>Magnet X placed near magnet Y, like poles facing, X free to move</td><td>the magnetic field of X <b>interacts with</b> the field of Y → like poles repel, so there is a <b>force on X directed away from Y</b> → the force is unbalanced, so <b>X accelerates away</b> from Y</td></tr>"
            "<tr><td>Unlike poles facing</td><td>fields interact → unlike poles attract, so a <b>force on X towards Y</b> → X <b>accelerates towards</b> Y</td></tr>"
            "<tr><td>A magnet floating above another (like poles facing) — June 2023 Q5(b)</td><td>the fields <b>interact</b> → like poles repel, so there is an <b>upward (repulsive) force on the upper magnet</b> → this force is <b>equal to its weight</b> (the downward force of gravity), so the forces are <b>balanced</b> and the magnet stays still (equilibrium)</td></tr>"
            "<tr><td>A piece of iron near a magnet</td><td>the magnet's field <b>induces</b> the opposite pole in the near end of the iron → unlike poles attract, so a <b>force on the iron towards the magnet</b> → the iron <b>accelerates towards</b> the magnet (so iron is always attracted, never repelled)</td></tr></table>"
            "<p>The June 2023 report on the floating magnet: answers that mentioned fields only to say \"repulsion\" \"can score one mark for repulsion but not another mark for the <b>interaction between fields</b>\". Full marks: the interaction of the two magnetic fields, an upward repulsive force, and that it <b>balances gravity</b>. One answer with interaction and repulsion but no gravity and no equilibrium lost marks. The link between the force and what happens — <b>accelerates</b>, or <b>balanced</b> so it stays — is the same link the examiners look for with charges (Topic 11 T1) and with forces generally (Topic 2).</p>",
        ),
        worked(
            "The floating magnet",
            "Two ring magnets are threaded on a wooden rod with like poles facing. The upper magnet floats above the lower one. Explain why it floats. (3 marks)",
            [
                "The magnetic field of the upper magnet <b>interacts with</b> the magnetic field of the lower magnet.",
                "Like poles are facing, so they <b>repel</b>: there is an <b>upward force on the upper magnet</b>.",
                "This upward force is <b>equal to the weight</b> of the upper magnet, so the forces on it are <b>balanced</b> and it stays still.",
            ],
        ),
        practice("Force chains", [
            written("mg-t1-q1", "A bar magnet is placed on a smooth table with its N pole facing the N pole of a fixed magnet. It moves away. Explain why. (2)",
                    marks(["Like poles repel, so there is a <b>force on the free magnet directed away from</b> the fixed one.", "The force is unbalanced, so the magnet <b>accelerates away</b>. (Higher: add that the force arises because the two magnets' <b>fields interact</b>.)"]), lines=3),
            written("mg-t1-q2", "A student explains the floating magnet by writing \"like poles repel so it floats\". State two things the answer is missing. (2)",
                    marks(["That the force comes from the <b>interaction between the two magnetic fields</b>.", "That the upward repulsive force <b>balances the weight</b> (gravity) of the upper magnet, so it is in equilibrium."]), lines=2, tags=["H"]),
            choice("mg-t1-q3", "A magnet X is released near a fixed magnet Y with unlike poles facing. Which is the best description of what happens?",
                   ["X and Y repel", "There is a force on X towards Y, so X accelerates towards Y", "X moves at a steady speed towards Y", "Y moves towards X"], 1,
                   "Force on X, towards Y, so X accelerates — name the object, the direction and the acceleration."),
            written("mg-t1-q4", "An unmagnetised iron nail is placed near a magnet and moves towards it. Explain why the nail is attracted whichever pole of the magnet faces it. (3)",
                    marks(["The magnet's field <b>induces</b> magnetism in the nail, with the <b>opposite pole</b> at the end nearest the magnet.", "Unlike poles attract, so there is a <b>force on the nail towards the magnet</b>…", "…so the nail <b>accelerates towards</b> the magnet. Either pole of the magnet induces the opposite pole, so it is attraction every time."]), lines=4),
            choice("mg-t1-q5", "Why does a floating magnet stay at a fixed height rather than keep rising?",
                   ["The repulsive force switches off", "The upward magnetic force equals its weight, so the resultant force is zero", "Gravity is stronger than magnetism", "The rod stops it"], 1,
                   "Balanced forces: it stays at the height where repulsion equals weight."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T2 · Is it a magnet?
# ---------------------------------------------------------------------

section_t2 = section(
    "magnet-test", "tricky", "Is it a magnet? Designing the test and stating the result", "12.1, 12.3",
    equations=[r"\text{attracted both ways round} \Rightarrow \text{magnetic material}", r"\text{repelled one way} \Rightarrow \text{magnet}"],
    blurb="Three kinds of object look the same: a permanent magnet, an unmagnetised magnetic material, and a non-magnetic material. One compass or one known magnet tells them apart — if you test both ends and say what each result means. The 2025 examiners gave one mark for the test and one for the expected result.",
    checklist=[
        "Design a test that distinguishes a magnet from a magnetic material",
        "State the expected result for each possibility",
        "Explain why picking up a paper clip is not enough",
    ],
    parts=[
        explain(
            "The three possibilities",
            "<table class='tbl'><tr><th>Object</th><th>Bring one pole of a known magnet to each end in turn</th><th>Why</th></tr>"
            "<tr><td><b>Permanent magnet</b></td><td>one end is <b>attracted</b>, the other is <b>repelled</b></td><td>it has its own poles; like poles repel</td></tr>"
            "<tr><td><b>Magnetic material</b> (unmagnetised iron, steel)</td><td><b>attracted at both ends</b>, never repelled</td><td>the known magnet induces the opposite pole whichever end is nearer</td></tr>"
            "<tr><td><b>Non-magnetic material</b> (copper, plastic)</td><td><b>no force</b> either way</td><td>it cannot be magnetised</td></tr></table>"
            "<p>So the test is: approach <b>both ends</b> with the <b>same pole</b> of a known magnet (or a compass needle — its N end is a known pole), and look for <b>repulsion</b>. The June 2025 report (Q7(b)(iv)): \"one mark for a suitable test and one for a clear statement of the expected result\"; \"trying to pick up a paper clip … earned 1 of 2, since it did not show what the result would mean\" — an induced magnet also picks up paper clips while the field is there. The full-mark answer <b>reversed one nail</b> and looked for <b>no repulsion in either orientation</b> (any force was attraction both ways, or there was none). Why a paper-clip test fails for a nail that has just been in a field: it may be a weak <b>induced</b> magnet for a while; only <b>repulsion</b> is proof of a <b>permanent</b> magnet.</p>",
        ),
        worked(
            "Nails after the electromagnet",
            "Nails were picked up by an electromagnet. A student claims the nails have become permanent magnets. Describe a test to check this and state the result expected if she is wrong. (2 marks)",
            [
                "Hold one nail by its middle and bring one end of a second nail (or one pole of a known magnet) to <b>each end</b> of it in turn, i.e. test both orientations.",
                "If the nails are <b>not</b> permanent magnets there is <b>no repulsion in either orientation</b> (any attraction is the same at both ends, or there is none); a permanent magnet would be repelled at one end.",
            ],
        ),
        practice("Is it a magnet?", [
            choice("mg-t2-q1", "A bar is attracted to both poles of a magnet. It is…",
                   ["a permanent magnet", "an unmagnetised magnetic material", "a non-magnetic material", "a solenoid"], 1,
                   "Attraction at both ends, no repulsion: magnetic material, not a magnet."),
            written("mg-t2-q2", "Explain why a bar that picks up a paper clip is not necessarily a permanent magnet. (2)",
                    marks(["The bar might be an <b>induced (temporary) magnet</b> — a magnetic material still in, or just out of, a magnetic field.", "Only <b>repulsion</b> by a known magnet proves it is a permanent magnet, because only two magnets can repel."]), lines=2),
            written("mg-t2-q3", "Describe how a compass could be used to find out whether a steel rod is a permanent magnet. State the expected results. (3)",
                    marks(["Bring the <b>N end</b> of the compass needle to <b>one end</b> of the rod, then to the <b>other end</b>.", "If the rod is a permanent magnet the needle's N end is <b>attracted to one end and repelled by the other</b>.", "If it is not, the needle's N end is <b>attracted to both ends</b> (induced magnetism) — no repulsion."]), lines=4),
            choice("mg-t2-q4", "A student's answer to 'test whether the nail is a magnet' is: \"Hold it near some iron filings and see if they stick.\" What is wrong?",
                   ["Iron filings are not magnetic", "Filings would also stick to an induced magnet, so sticking does not show it is permanent — and no expected result is stated", "Filings are too heavy", "Nothing — it scores full marks"], 1,
                   "Test needs repulsion, and the expected result must be stated."),
            choice("mg-t2-q5", "Two bars look identical. One is a magnet, one is unmagnetised iron. Bringing the END of bar A to the MIDDLE of bar B gives strong attraction; bringing the end of B to the middle of A gives almost none. Which is the magnet?",
                   ["A", "B", "Both", "Cannot tell"], 0,
                   "A magnet's poles are at its ends, and its middle is weak: A's end attracts B's middle strongly, so A is the magnet (B's end at A's weak middle does little)."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T3 · Drawing and marking field diagrams
# ---------------------------------------------------------------------

section_t3 = section(
    "field-diagrams-mag", "tricky", "Drawing and marking field diagrams", "12.4, 12.7, 12.9",
    equations=[r"\text{shape mark} + \text{direction mark}"],
    blurb="A field-diagram question is usually two marks: one for the shape, one for the direction. The shapes to know are the bar magnet, two magnets facing (N–S and N–N), the straight wire, and the solenoid. What loses the mark: lines that cross or touch, no arrows, arrows into N, lines that stop in mid-air.",
    checklist=[
        "Draw the five standard field patterns",
        "Mark a field diagram: say what scores and what loses the mark",
        "Describe the field between two like poles",
    ],
    parts=[
        explain(
            "The five patterns and the marking",
            "<table class='tbl'><tr><th>Field</th><th>Shape</th><th>Direction</th><th>See</th></tr>"
            "<tr><td><b>Bar magnet</b></td><td>loops from one pole round to the other; straight line out of each end; closest at the poles</td><td>out of N, into S</td><td>N3</td></tr>"
            "<tr><td><b>N facing S</b></td><td>nearly straight, parallel lines across the gap (uniform between the poles), curving outward at the edges</td><td>N → S across the gap</td><td>N3</td></tr>"
            "<tr><td><b>N facing N</b> (or S facing S)</td><td>lines <b>curve away</b> from each other; a <b>neutral point</b> midway where the field is zero (no lines)</td><td>out of both N poles</td><td>—</td></tr>"
            "<tr><td><b>Straight wire</b></td><td>concentric circles centred on the wire, further apart with distance</td><td>right-hand grip rule</td><td>N5</td></tr>"
            "<tr><td><b>Solenoid</b></td><td>straight, parallel, equally spaced inside; bar-magnet loops outside</td><td>through the inside and out of the N end</td><td>N6</td></tr></table>"
            "<p><b>Marking</b> (June 2023 Q5(a) and the general schemes): the <b>shape mark</b> needs lines that <b>do not cross, touch or overlap</b>, that start and end on poles (or form closed circles round a wire), and that are <b>closer near the poles</b>; several lines from the same point on a pole lost it. The <b>direction mark</b> needs <b>arrows</b> on the lines, <b>out of N and into S</b> — at least one arrow on each line, all consistent. No arrows at all: no direction mark. Arrows the wrong way: no direction mark, even with a perfect shape. Field lines inside the magnet are not needed at GCSE and are ignored if drawn.</p>",
        ),
        worked(
            "Two N poles",
            "Two bar magnets are placed in a line with their N poles 3 cm apart. Draw the magnetic field between them, and describe it. (3 marks)",
            [
                "Lines leave <b>each N pole</b> and <b>curve away</b> from the other magnet — none joins the two N poles, because like poles repel.",
                "Midway between the poles there is a <b>neutral point</b> where the two fields cancel: the field is zero there, so no line passes through it.",
                "<b>Arrows out of both N poles</b> (and, if the S poles are shown, round to them). Description: the field is weak between the poles and zero at the neutral point; the lines are furthest apart there.",
            ],
        ),
        practice("Field diagrams", [
            choice("mg-t3-q1", "A diagram of the field around a bar magnet has no arrows on any line. The shape is perfect. Marks out of 2?",
                   ["2", "1 — shape only", "0", "Depends on the examiner"], 1,
                   "No arrows, no direction mark."),
            written("mg-t3-q2", "Describe the magnetic field pattern between the S pole of one magnet and the S pole of another placed facing it. (2)",
                    marks(["The lines <b>curve away</b> from each other: they <b>enter each S pole</b> from the sides and do not run straight across the gap.", "There is a <b>neutral point</b> midway between the poles where the field is <b>zero</b>."]), lines=2),
            choice("mg-t3-q3", "Which is NOT a reason for losing the shape mark on a bar-magnet field diagram?",
                   ["Two lines cross", "Lines are closer together near the poles", "Several lines leave the same point on the pole", "A line stops in mid-air"], 1,
                   "Closer near the poles is correct — it shows the stronger field."),
            written("mg-t3-q4", "A student draws the field around a straight wire as straight lines pointing away from the wire. Explain what is wrong and what she should draw. (2)",
                    marks(["The field of a straight wire is <b>circles centred on the wire</b>, not radial lines — the radial pattern is an <b>electric</b> field (Topic 11).", "Draw <b>concentric circles</b>, further apart with distance, with arrows given by the <b>right-hand grip rule</b> (clockwise for current into the page)."]), lines=3),
            choice("mg-t3-q5", "Inside a solenoid the field lines should be drawn…",
                   ["as circles", "straight, parallel and equally spaced", "curving outwards", "there is no field inside"], 1,
                   "Uniform inside: straight, parallel, equally spaced."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T4 · The Earth as a magnet
# ---------------------------------------------------------------------

section_t4 = section(
    "earth-magnet", "tricky", "The Earth as a magnet: reading the field and the evidence", "12.5, 12.6",
    equations=[r"\text{compass points north} \Rightarrow \text{Earth has a field} \Rightarrow \text{core is magnetic}"],
    blurb="The 2024 paper drew the Earth with its field and asked for the field direction at marked points, then for the evidence that the Earth has a magnetic field. The direction at any point follows the bar-magnet picture: out of the magnetic N pole (near geographic south), round, into the magnetic S pole (near geographic north); parallel to the surface at the equator.",
    checklist=[
        "Give the field direction at points around the Earth from the bar-magnet picture",
        "List the evidence that the Earth has a magnetic field and a magnetic core",
        "Explain why the pole near geographic north is a magnetic S pole",
    ],
    parts=[
        explain(
            "Reading the Earth's field",
            "<p>Treat the Earth as a bar magnet with its <b>S pole near geographic north</b> and its N pole near geographic south (N4 figure). Then at any point: lines <b>come out</b> of the Earth near geographic <b>south</b>, run <b>parallel to the surface, pointing north</b>, at the <b>equator</b>, and <b>go into</b> the Earth near geographic <b>north</b>. A compass at any point lines up with the field there: on the surface its N end points north; a compass free to tilt dips downwards in the northern hemisphere.</p>"
            "<p>The June 2024 scheme (Q5(a)): at the point on the surface near the equator the arrow pointed <b>up the page</b> (along the surface towards north); at the other marked point the arrow pointed the other way, <b>down the page</b> — read each one from the loop it lies on: outside the Earth the lines run from the magnetic N pole (geographic south) round to the magnetic S pole (geographic north), and inside the Earth they run back the other way. Judged by eye, within 10°. For the evidence (3 marks, any three): the <b>Earth has a magnetic field</b>; a <b>compass needle points along the field</b>; the field <b>goes into the Earth</b> at the north pole / <b>comes out</b> at the south; it <b>runs parallel to the surface at the equator</b>; the <b>core is magnetic</b> — \"as if there were a magnet inside the Earth\".</p>"
            "<p>The naming twist: the end of a compass needle that points north is its <b>north-seeking pole</b>, a magnetic N pole. It is attracted north, and unlike poles attract, so the thing attracting it — the Earth's pole near geographic north — is a <b>magnetic S pole</b>. Students lose this mark by writing \"the Earth's north pole is a north pole\".</p>",
        ),
        worked(
            "The 3-mark evidence",
            "Explain how the behaviour of a magnetic compass provides evidence that the core of the Earth is magnetic. (3 marks)",
            [
                "A compass needle is a small magnet that <b>lines up with a magnetic field</b>; it points north everywhere, so the <b>Earth has a magnetic field</b>.",
                "The shape of that field — parallel to the ground at the equator, dipping into the ground near the poles — is the shape of a <b>bar magnet's field</b>.",
                "So the field must come from <b>inside the Earth</b>: the <b>core must be magnetic</b>, as if there were a bar magnet in it.",
            ],
        ),
        practice("The Earth as a magnet", [
            choice("mg-t4-q1", "At a point just above the equator, the Earth's magnetic field points…",
                   ["straight down into the ground", "parallel to the surface, towards geographic north", "parallel to the surface, towards geographic south", "straight up"], 1,
                   "Along the surface, from the magnetic N pole (south) to the magnetic S pole (north)."),
            written("mg-t4-q2", "Explain why the magnetic pole of the Earth near the geographic north pole is a magnetic south pole. (2)",
                    marks(["The N (north-seeking) pole of a compass needle <b>points towards</b> geographic north — it is <b>attracted</b> there.", "<b>Unlike poles attract</b>, so the pole it is attracted to must be a magnetic <b>S</b> pole."]), lines=2),
            choice("mg-t4-q3", "Near the geographic north pole, the Earth's field lines…",
                   ["come out of the Earth", "go into the Earth", "run parallel to the surface", "stop"], 1,
                   "Into the magnetic S pole, which is near geographic north."),
            written("mg-t4-q4", "Give three pieces of evidence, from the behaviour of compasses, that the Earth has a magnetic field like that of a bar magnet. (3)",
                    marks(["A compass <b>points north</b> everywhere (it only points when in a field).", "The field is <b>parallel to the surface at the equator</b> and <b>dips into the ground</b> near the poles (goes in at one pole, out at the other).", "The naming: a compass's N end is attracted towards geographic north, consistent with a <b>magnetic S pole</b> there — the pattern of a bar magnet inside the Earth."]), lines=4),
            choice("mg-t4-q5", "Why is a compass used in navigation?",
                   ["It points towards the Sun", "Its needle lines up with the Earth's magnetic field, so it always shows the direction of north", "It measures distance", "It detects metal"], 1,
                   "Lines up with the Earth's field: a fixed reference direction."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T5 · Fleming's rule on diagrams [H]
# ---------------------------------------------------------------------

section_t5 = section(
    "flhr-diagrams", "tricky", "Using Fleming's left-hand rule on diagrams: dots, crosses and the missing direction", "12.12",
    equations=[r"\text{dot: out of the page}", r"\text{cross: into the page}", r"\text{parallel: no force}"],
    blurb="The exam gives two of the three directions and asks for the third, usually with the wire end on. The method is the same every time: set the first finger along the field, the second along the current, read the thumb; and check first that the current and field are at right angles.",
    tags=["H"],
    checklist=[
        "Find the force direction from a dot-or-cross diagram",
        "Find the current direction given the field and the force",
        "Recognise the no-force case and the two ways of reversing the force",
    ],
    parts=[
        explain(
            "The three cases",
            diagram(dg.cases_svg(), 720, 245, "A wire end on between the poles: current out of the page is pushed up, current into the page is pushed down, and a wire along the field feels no force.") +
            "<p><b>Method</b>: (1) check the current and field are at <b>right angles</b> — if the wire runs along the field, the answer is <b>no force</b> and you stop; (2) point the <b>first finger</b> along the field, <b>N to S</b>; (3) point the <b>second finger</b> along the current — <b>towards you</b> for a dot, <b>away from you</b> for a cross; (4) the <b>thumb</b> gives the force. To find the <b>current</b> instead, set the first finger (field) and thumb (force) and read the second finger. To find the <b>field</b>, set thumb and second finger and read the first.</p>"
            "<p><b>Reversing</b>: reversing the current reverses the force; reversing the field reverses the force; reversing both leaves it as it was. The June 2024 scheme (Q5(b)(ii)): \"swap the battery connections around\" <b>or</b> \"turn the magnet around\". A common slip is to use the <b>right</b> hand (which gives the opposite answer) or to point the second finger along the <b>electron</b> flow — the rule uses <b>conventional current</b>, + to −.</p>",
        ),
        worked(
            "Finding the current",
            "A wire between the poles of a magnet experiences a force up the page. The field points from right to left. Find the direction of the current. (2 marks)",
            [
                "First finger along the field: pointing <b>left</b>. Thumb along the force: pointing <b>up</b>.",
                "The second finger then points <b>into the page</b>, away from you — the current is <b>into the page</b> (a cross). Check against the reference case: field right with current out gives force up; reversing the field alone would give force down, so to keep the force up the current must be reversed too — into the page.",
            ],
        ),
        practice("Diagrams", [
            choice("mg-t5-q1", "Field from left to right; current out of the page (dot). Force on the wire?",
                   ["Up the page", "Down the page", "Left", "Right"], 0,
                   "First finger right, second finger towards you, thumb up."),
            choice("mg-t5-q2", "Field from left to right; current into the page (cross). Force?",
                   ["Up the page", "Down the page", "Left", "Right"], 1,
                   "Reversing the current reverses the force: down."),
            choice("mg-t5-q3", "Field from right to left; current into the page (cross). Force?",
                   ["Up the page", "Down the page", "Left", "Right"], 0,
                   "Reversing both the field and the current (compared with q1) leaves the force as it was: up."),
            choice("mg-t5-q4", "Field down the page; force on the wire to the right. The current is…",
                   ["out of the page", "into the page", "up the page", "to the left"], 0,
                   "First finger down, thumb right: the second finger points towards you — out of the page. (Check: field down, current out, force right.)"),
            choice("mg-t5-q5", "Field from left to right; the wire runs from left to right too, carrying a current. Force?",
                   ["Up", "Down", "Zero", "Into the page"], 2,
                   "Current parallel to the field: no force."),
            written("mg-t5-q6", "A wire between two magnets is pushed upwards when the current is switched on. State and explain two separate changes that would each make it move downwards instead. (4)",
                    marks(["<b>Reverse the current</b> (swap the connections to the supply)…", "…because the force reverses when the current reverses (the second finger reverses, so the thumb reverses).", "<b>Reverse the field</b> (turn the magnet round / swap the poles)…", "…because the force reverses when the field reverses (the first finger reverses, so the thumb reverses). Doing both would leave it moving up."]), lines=4),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T6 · F = BIl the hard way [H]
# ---------------------------------------------------------------------

section_t6 = section(
    "motor-force-hard", "tricky", "F = BIl the hard way: rearranging, the length in the field, and unfamiliar equations", "12.13",
    equations=[r"B = \dfrac{F}{I\,l}", r"I = \dfrac{F}{B\,l}", r"l = \dfrac{F}{B\,I}"],
    blurb="The harder $F = BIl$ questions hide one of three things: the length is only the part of the wire inside the field; the current comes from another equation first ($V = IR$); or the equation is an unfamiliar one you are given and simply have to use. In 2024 the answer was 0.58 T; in 2025 an inverse-square equation gave 160 μT.",
    tags=["H"],
    checklist=[
        "Rearrange $F = BIl$ for any quantity and convert units first",
        "Use only the length of wire inside the field",
        "Use an unfamiliar given equation with the same care as a familiar one",
    ],
    parts=[
        explain(
            "Where the extra marks hide",
            "<table class='tbl'><tr><th>Twist</th><th>What to do</th></tr>"
            "<tr><td>Length given in <b>cm</b>, current in <b>mA</b>, force in <b>mN</b></td><td>convert to m, A and N <b>before</b> substituting; write the conversion as a line of working</td></tr>"
            "<tr><td>A long wire, only part of it <b>between the poles</b></td><td>$l$ is the length <b>inside the field</b> — usually the width of the magnet or the pole pieces, not the whole wire</td></tr>"
            "<tr><td>A coil of <b>N turns</b> with one side in the field</td><td>the force on that side is $N$ times the force on one wire: $F = B I l N$ — the question will say so, or ask for the force on one wire</td></tr>"
            "<tr><td>Current <b>not given</b>, but pd and resistance are</td><td>find $I = V / R$ first (Topic 10), then $F = B I l$</td></tr>"
            "<tr><td>An <b>unfamiliar equation</b> is given</td><td>June 2025 Q7(c): an equation linking $B$ and distance $d$ — substitute and rearrange exactly as you would for $F = B I l$; finding the constant and stopping scored 1 of 3</td></tr>"
            "<tr><td>Wire <b>parallel</b> to the field</td><td>$F = 0$ — the equation only applies at right angles</td></tr></table>"
            "<p>The June 2024 scheme (Q5(b)(iii), 2 marks): \"rearrangement and substitution\" (1), \"evaluation\" (1) — 0.58 T, or anything rounding to 0.6 T; full marks for the correct answer alone. Show the rearranged equation with numbers in it: that line is a mark on its own if the arithmetic goes wrong.</p>",
        ),
        worked(
            "The 2024-style flux density",
            "A wire carries a current of 1.2 A. A 5.0 cm length of it lies at right angles to a magnetic field, and the force on the wire is 0.035 N. Calculate the magnetic flux density. (2 marks)",
            [
                "Convert: $l = 5.0$ cm $= 0.050$ m. Rearrange and substitute: $B = F \\div (I l) = 0.035 \\div (1.2 \\times 0.050)$.",
                "$B = 0.035 \\div 0.060 = 0.58$ T (anything rounding to 0.6 T).",
            ],
        ),
        practice("The hard way", [
            numeric("mg-t6-q1", "A wire 60 cm long is held across a magnet whose poles are 4.0 cm wide. The current is 3.0 A and the flux density 0.20 T. Calculate the force on the wire.", 0.024, "N",
                    "Only the length between the poles is in the field.",
                    [r"$l = 4.0$ cm $= 0.040$ m — the length <b>in the field</b>, not the 0.60 m of wire."] + ewau(r"F = B I l", r"F = 0.20 \times 3.0 \times 0.040", "0.024", "N")),
            numeric("mg-t6-q2", "A 0.10 m length of wire in a 0.30 T field feels a force of 45 mN. Calculate the current.", 1.5, "A",
                    "45 mN = 0.045 N; $I = F \\div (B l)$.",
                    [r"$F = 45$ mN $= 0.045$ N"] + ewau(r"I = F \div (B l)", r"I = 0.045 \div (0.30 \times 0.10) = 0.045 \div 0.030", "1.5", "A")),
            numeric("mg-t6-q3", "A wire of resistance 4.0 Ω is connected to a 6.0 V supply. 0.25 m of it is at right angles to a field of 0.080 T. Calculate the force on that length.", 0.03, "N",
                    "Find $I$ from $V = IR$ first.",
                    [r"$I = V \div R = 6.0 \div 4.0 = 1.5$ A"] + ewau(r"F = B I l", r"F = 0.080 \times 1.5 \times 0.25", "0.030", "N")),
            numeric("mg-t6-q4", "One side of a coil of 50 turns lies in a field of 0.12 T; the side is 8.0 cm long and carries 2.0 A. Calculate the force on that side of the coil (all 50 wires).", 0.96, "N",
                    "Force on one wire × 50.",
                    ewau(r"F = B I l N", r"F = 0.12 \times 2.0 \times 0.080 \times 50", "0.96", "N") + [r"(one wire: $0.0192$ N; fifty of them: $0.96$ N)"]),
            numeric("mg-t6-q5", "The magnetic flux density at a distance d from a small magnet is given by B = K ÷ d², where K is a constant. At d = 0.10 m, B = 640 μT. Calculate B at d = 0.20 m, in μT.", 160, "μT",
                    "Find K first, then use it again — or notice doubling d divides B by 4.",
                    [r"<b>Find K:</b> $K = B d^2 = 640 \times 0.10^2 = 6.4$ (μT m²)", r"<b>Use it:</b> $B = K \div d^2 = 6.4 \div 0.20^2 = 6.4 \div 0.040$", r"<b>Answer:</b> $= 160$ μT — inverse square: twice the distance, a quarter of the field"]),
            choice("mg-t6-q6", "A student finds the constant K in the 2025-style question and stops. Out of 3 marks she scores…",
                   ["3", "2", "1", "0"], 2,
                   "The report: finding K 'earning 1 of 3, but made no further progress'."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T7 · The d.c. motor [H, P]
# ---------------------------------------------------------------------

section_t7 = section(
    "dc-motor", "tricky", "The d.c. motor: why the coil turns, and why it keeps turning", "12.14P",
    equations=[r"\text{opposite forces on the two sides} \Rightarrow \text{rotation}", r"\text{commutator: reverse every half turn}"],
    blurb="A motor is the motor effect applied to a coil: the current goes one way along one side and the other way along the opposite side, so the forces are opposite and the coil turns. The split-ring commutator reverses the current in the coil every half turn so that it keeps turning the same way. In 2025 the commutator was 'poorly explained' and many students described a generator instead.",
    tags=["H", "P"],
    checklist=[
        "Write the six-step chain for the motor effect in a motor",
        "Explain what the split-ring commutator does and why the motor needs it",
        "State what makes the motor turn faster, and what reverses it",
    ],
    parts=[
        explain(
            "The chain, then the commutator",
            diagram(dg.motor_svg(), 700, 280, "The coil end on, with opposite forces on its two sides; and the split-ring commutator, whose halves swap brushes every half turn.") +
            "<p>The standard explanation of the motor effect in a motor, in the steps the marks are on (the <a href='../simple-motor/'>Simple Motor</a> page animates it):</p>"
            + chain_list(MOTOR_CHAIN) +
            "<p>Why the forces are opposite: the current goes <b>one way along one side of the coil and the opposite way along the other</b>, and Fleming's left-hand rule gives opposite forces for opposite currents in the same field. The two forces make a <b>turning effect</b> about the axle.</p>"
            "<p><b>The split-ring commutator</b>: two half-rings on the axle, each joined to one end of the coil, turning with it; two fixed <b>brushes</b> press on them and connect to the supply. Every <b>half turn</b> the halves swap brushes, so the <b>current in the coil reverses</b>. Without it, once the coil passed the vertical the force on each side would be the same way as before but that side is now on the other side of the axle, so it would be turned <b>back</b> — the coil would rock to the vertical and stop. With it, the side that is now on the left always carries the current the left side needs, so the force on it is always the same way and the coil <b>keeps turning in the same direction</b>. The June 2025 report (Q6(c)): credit was given for \"<b>reversing the current every half turn</b>\" and for explaining that this \"lets the motor <b>spin continuously</b>\" (keeps rotating in the same direction); many gave the first without the second, some said it stops the wires tangling, and \"a surprisingly large number\" described a <b>dynamo</b> — one scored 1 of 3 because \"the motor does not produce a current\".</p>"
            "<p><b>Faster</b> (larger force): more <b>current</b>, a <b>stronger magnet</b>, <b>more turns</b> on the coil, an iron core in the coil. <b>Reverse</b>: reverse the current (swap the supply connections) or reverse the field (swap the magnets). The force on each side is the <b>same size at every angle</b> (the long sides are always at right angles to the field), but its <b>turning effect</b> is largest when the coil is <b>flat</b> and falls to zero as the coil reaches the vertical — real motors use several coils at different angles so there is never a dead spot.</p>",
        ),
        worked(
            "The 6-mark motor",
            "Explain how a simple d.c. motor produces continuous rotation. (6 marks)",
            [
                "There is a <b>current in the coil</b>. This <b>creates a magnetic field around the coil</b>.",
                "This <b>interacts with the permanent magnetic field</b>. This causes a <b>resultant force on the coil</b>.",
                "<b>The direction of the force is opposite on either side of the coil</b> (the current goes opposite ways along the two sides — Fleming's left-hand rule). <b>So the coil rotates.</b>",
                "The <b>split-ring commutator</b> turns with the coil; its two halves are connected to the ends of the coil and press against fixed brushes.",
                "Every <b>half turn</b> the halves swap brushes, so the <b>current in the coil reverses</b>…",
                "…so the force on whichever side is on the left is always in the same direction, and the coil <b>keeps rotating in the same direction</b> instead of rocking back.",
            ],
        ),
        practice("The d.c. motor", [
            written("mg-t7-q1", "Explain why the coil of a d.c. motor starts to turn when the current is switched on. (4)",
                    marks(["There is a <b>current in the coil</b>. This <b>creates a magnetic field around the coil</b>.", "This <b>interacts with the permanent magnetic field</b>. This causes a <b>resultant force on the coil</b>.", "<b>The direction of the force is opposite on either side of the coil</b> (the current goes opposite ways along the two sides).", "<b>So the coil rotates</b> (the two forces give a turning effect about the axle)."]), lines=4),
            written("mg-t7-q2", "Explain the purpose of the split-ring commutator in a d.c. motor. (3)",
                    marks(["It <b>reverses the current in the coil every half turn</b> (the halves of the ring swap brushes as the coil turns).", "So the force on each side of the coil is always in the direction needed on that side of the axle…", "…and the coil <b>keeps rotating in the same direction</b> (continuously) instead of turning back and stopping."]), lines=3),
            choice("mg-t7-q3", "Which statement about a d.c. motor is WRONG?",
                   ["The forces on the two sides of the coil are in opposite directions", "The commutator reverses the current every half turn", "The motor produces a current", "Reversing the supply reverses the rotation"], 2,
                   "2025 report: 'the motor does not produce a current' — that is a generator (Topic 13)."),
            written("mg-t7-q4", "State two changes that would make the coil of a d.c. motor turn faster. (2)",
                    marks(["<b>Increase the current</b> (higher pd) — or use <b>stronger magnets</b>.", "<b>More turns</b> on the coil (or an iron core) — each gives a larger force and so a larger turning effect."]), lines=2),
            choice("mg-t7-q5", "What would happen to a motor's coil if the split ring were replaced by a complete ring (the same connection all the time)?",
                   ["It would turn faster", "It would turn to the vertical, then be pushed back — rocking about the vertical and stopping", "It would turn the other way", "Nothing would change"], 1,
                   "Without reversal the force turns the coil back once it passes vertical."),
            written("mg-t7-q6", "A student describes a d.c. motor by writing: \"As the coil turns in the field, a current is induced in it, which makes it spin.\" Explain the error. (2)",
                    marks(["That describes a <b>generator/dynamo</b> (electromagnetic induction): a motor does <b>not produce</b> a current.", "In a motor the current comes from the <b>supply</b>; the force on the current-carrying coil in the field (the <b>motor effect</b>) makes it turn."]), lines=2),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T8 · The electromagnet investigation
# ---------------------------------------------------------------------

section_t8 = section(
    "electromagnet-practical", "tricky", "Investigating an electromagnet: the seven steps, and describing the trend", "12.8, 12.9",
    equations=[r"\text{variables} \rightarrow \text{relationship} \rightarrow \text{change} \rightarrow \text{measure} \rightarrow \text{use} \rightarrow \text{accuracy} \rightarrow \text{repeat}"],
    blurb="The 2025 paper used nails picked up by an electromagnet as the measure of its strength, against the number of turns. The seven-step recipe from Topic 1 (T6 there) plans it; the data question wants a trend described in plain words — not 'inversely proportional', which the examiners said to avoid unless it is true.",
    checklist=[
        "Plan an investigation into how the strength of an electromagnet depends on the current or the number of turns",
        "Describe a trend from a bar chart or graph in the words that score",
        "Explain why the nails must be tested for permanent magnetism afterwards",
    ],
    parts=[
        explain(
            "The recipe applied",
            "<table class='tbl'><tr><th>Step</th><th>Strength against number of turns</th><th>Strength against current</th></tr>"
            "<tr><td><b>1 Variables</b></td><td>independent: number of turns on the core; dependent: strength, measured as the number of nails (or paper clips) picked up, or the mass held; control: current, the core, the nails</td><td>independent: current (set with a variable resistor, read on an ammeter); dependent: number of nails held; control: turns, core, nails</td></tr>"
            "<tr><td><b>2 Equation / relationship</b></td><td>no equation; state the relationship you expect — the strength (nails held) should rise with the number of turns</td><td>no equation; expected to rise with the current</td></tr>"
            "<tr><td><b>3 Change</b></td><td>wind 10, 20, 30 … turns on the same core, keeping the current the same</td><td>change the current in equal steps with the variable resistor</td></tr>"
            "<tr><td><b>4 Measure</b></td><td>dip the core into a tray of nails, lift, count the nails held</td><td>same</td></tr>"
            "<tr><td><b>5 Use the result</b></td><td>plot nails against turns; describe the trend</td><td>plot nails against current</td></tr>"
            "<tr><td><b>6 Accuracy detail</b></td><td>use the same nails each time; switch off between readings so the coil does not heat up (its resistance would rise and change the current) and the nails do not become magnetised; lift from the same depth</td><td>switch off between readings; wait for the ammeter to settle</td></tr>"
            "<tr><td><b>7 Repeat</b></td><td>repeat each number of turns three times and take a mean</td><td>same</td></tr></table>"
            "<p><b>Describing the trend</b> (June 2025 Q7(b)(iii)): \"as the number of turns increases the number of nails held increases\" scores; better answers added that the increase is <b>not linear</b> (not proportional — the graph is not a straight line through the origin). The examiners: candidates \"should be discouraged from using the term '<b>inversely proportional</b>'\" as a synonym for \"one goes down as the other goes up\" — it only means that one variable is proportional to the reciprocal of the other. Say <b>what happens to the dependent variable as the independent variable increases</b>, and whether the change is steady, speeding up or levelling off.</p>"
            "<p>Afterwards the nails may have become weak permanent magnets (steel), which would change later counts — hence the 2025 test for permanent magnetism (T2).</p>",
        ),
        worked(
            "The 6-mark plan",
            "Plan an investigation to find how the strength of an electromagnet depends on the number of turns of wire on its core. (6 marks)",
            [
                "<b>Variables:</b> change the number of turns (independent); measure the strength as the number of nails the electromagnet can hold (dependent); keep the current, the core and the nails the same (control).",
                "<b>Relationship expected:</b> more turns, a stronger electromagnet, so more nails held (no equation needed). Circuit: the coil in series with a cell, a switch, an ammeter and a variable resistor, set so the current is the same for every number of turns.",
                "<b>Change:</b> wind 10 turns on the iron core; then 20, 30, 40, 50 — five values at least.",
                "<b>Measure:</b> switch on, lower the core into a tray of nails, lift it out and count the nails held; switch off between readings.",
                "<b>Use:</b> plot number of nails against number of turns and describe the trend.",
                "<b>Accuracy and repeats:</b> use the same tray of nails and lift from the same depth each time; repeat each number of turns three times and take a mean.",
            ],
        ),
        practice("The investigation", [
            written("mg-t8-q1", "Plan an investigation into how the strength of an electromagnet depends on the current in its coil. (6)",
                    mark_scheme([
                        ("Variables", "Independent: current; dependent: strength (number of nails or paper clips held, or mass lifted); control: number of turns, the core, the nails."),
                        ("Relationship", "No equation; expect the strength (nails held) to rise with the current."),
                        ("Change", "Coil in series with a supply, a <b>variable resistor</b> and an <b>ammeter</b>; set the current to at least five values in equal steps."),
                        ("Measure", "Count the nails held (or mass lifted) at each current; switch off between readings."),
                        ("Use", "Plot nails against current and describe the trend."),
                        ("Accuracy", "Same nails and same depth each time; switch off between readings so the coil does not heat up."),
                        ("Repeat", "Repeat each current three times and take a mean."),
                    ], total=6, extra=["Any six of the seven points."]), lines=7),
            choice("mg-t8-q2", "In the turns investigation, which is the control variable?",
                   ["The number of turns", "The number of nails held", "The current", "The trend"], 2,
                   "Keep the current (and core and nails) the same."),
            written("mg-t8-q3", "A bar chart shows 4, 7, 9, 10 and 10 nails held for 10, 20, 30, 40 and 50 turns. Describe the relationship. (2)",
                    marks(["As the number of turns <b>increases</b>, the number of nails held <b>increases</b>…", "…but <b>not in proportion</b>: the increase gets smaller and <b>levels off</b> (no change from 40 to 50 turns)."]), lines=2),
            choice("mg-t8-q4", "Fewer nails are held as a variable is increased. The examiners said NOT to describe this as…",
                   ["a negative correlation", "a decrease", "inversely proportional", "a downward trend"], 2,
                   "2025 report: 'inversely proportional' only when one variable is proportional to the reciprocal of the other."),
            written("mg-t8-q5", "Explain why the student switches the electromagnet off between readings. (2)",
                    marks(["So the coil does not <b>heat up</b> (its resistance would rise and change the current)…", "…and so the steel nails are not left in the field long enough to become <b>permanent magnets</b>, which would change later counts."]), lines=2),
        ]),
    ],
)

SECTIONS = [section_t1, section_t2, section_t3, section_t4, section_t5, section_t6, section_t7, section_t8]

# ---------------------------------------------------------------------
# Flashcards (the key-word definitions are added by mg_nn.FACTS_KW)
# ---------------------------------------------------------------------

FACTS = [
    # N1
    fact("Rule for poles?", "Like poles repel; unlike poles attract.", "poles"),
    fact("Why is attraction not a test for a magnet?", "A magnet attracts any magnetic material (it induces the opposite pole), whichever way round. Only repulsion proves an object is a magnet.", "poles"),
    fact("The 2-mark 'is it a magnet' test?", "Bring the same pole of a known magnet to each end in turn (test both orientations) AND state the result: a magnet is repelled at one end; a magnetic material is attracted at both.", "poles"),
    fact("The four magnetic materials?", "Iron, steel, cobalt, nickel.", "poles"),
    # N2
    fact("Permanent magnet?", "Produces its own magnetic field all the time (steel).", "permanent-induced"),
    fact("Induced (temporary) magnet?", "A magnetic material that is a magnet only while in a field; loses it when the field is removed (soft iron).", "permanent-induced"),
    fact("Which pole is induced nearest a magnet's N pole?", "A S pole — so induced magnetism always attracts.", "permanent-induced"),
    fact("Why iron, not steel, for an electromagnet core?", "Iron loses its magnetism when the current is off, so the electromagnet can be switched off; steel would stay magnetised.", "permanent-induced"),
    fact("Use of a permanent magnet? Of a temporary one?", "Permanent: compass needle, motor, loudspeaker, fridge magnet. Temporary: electromagnet core, relay, electric bell, transformer core.", "permanent-induced"),
    # N3
    fact("What is a magnetic field?", "The region around a magnet (or current) where a magnetic material or another magnet experiences a force.", "field-lines"),
    fact("Which way do field lines point?", "Out of N, into S (outside the magnet).", "field-lines"),
    fact("How does a diagram show field strength?", "Closer lines = stronger field; closest at the poles.", "field-lines"),
    fact("Field between N and S poles facing each other?", "Uniform: straight, parallel, equally spaced lines from N to S.", "field-lines"),
    fact("Three ways to lose the field-diagram marks?", "Lines that cross or touch; no arrows; arrows into N.", "field-lines"),
    # N4
    fact("How to plot a field line with a compass?", "Mark dots at each end of the needle; move the compass so its tail is on the head's dot; repeat; join the dots; arrow the way the N end pointed.", "compass-earth"),
    fact("What does a compass pointing north show?", "The Earth has a magnetic field, so its core must be magnetic (like a bar magnet inside the Earth).", "compass-earth"),
    fact("Which magnetic pole is near geographic north?", "A magnetic S pole — the compass's N pole is attracted to it.", "compass-earth"),
    # N5
    fact("Shape of the field around a straight wire?", "Concentric circles centred on the wire, further apart with distance.", "wire-field"),
    fact("Right-hand grip rule?", "Thumb along the (conventional) current; fingers curl the way the field goes.", "wire-field"),
    fact("Current out of the page: field direction?", "Anticlockwise (into the page: clockwise).", "wire-field"),
    fact("What does the strength of a wire's field depend on?", "The size of the current (more = stronger) and the distance from the wire (further = weaker).", "wire-field"),
    fact("How to show a current has a magnetic effect?", "Wire through a card with plotting compasses: they line up in circles when the current is on and reverse when it is reversed.", "wire-field"),
    # N6
    fact("Field inside a solenoid?", "Strong and almost uniform: the fields of the turns add together along the centre.", "solenoid"),
    fact("Field outside a solenoid?", "Weaker: the fields of the turns largely cancel; the shape is a bar magnet's.", "solenoid"),
    fact("Three ways to make an electromagnet stronger?", "More current, more turns, an iron core.", "solenoid"),
    fact("What does reversing the current in a solenoid do?", "Swaps its N and S poles.", "solenoid"),
    # N7
    fact("The motor effect?", "A current-carrying conductor in a magnetic field experiences a force, due to the interaction between the two magnetic fields.", "motor-effect"),
    fact("The five-step chain for a wire?", "Current in the wire → magnetic field around the wire → interacts with the permanent field → resultant force, so the wire accelerates → direction from Fleming's left-hand rule.", "motor-effect"),
    fact("What force acts on the magnet?", "An equal and opposite force (Newton's third law).", "motor-effect"),
    fact("When is the motor-effect force zero? Largest?", "Zero when the wire is parallel to the field; largest at right angles.", "motor-effect"),
    fact("The 'interaction' mark (2023 Q5(b))?", "'Repulsion' alone scored 1; the second mark was 'the interaction between the two magnetic fields'.", "motor-effect"),
    # N8
    fact("Fleming's left-hand rule: the three digits?", "First finger: Field (N → S). Second finger: Current (+ → −). Thumb: Motion (force).", "flhr"),
    fact("Dot and cross?", "Dot: current out of the page (towards you). Cross: into the page.", "flhr"),
    fact("Two ways to reverse the force on a wire?", "Reverse the current, or reverse the field (turn the magnet round). Both together: no change.", "flhr"),
    fact("Which current direction does the second finger use?", "Conventional current, + to − (not electron flow).", "flhr"),
    # N9
    fact("Equation for the force on a wire at right angles to a field?", "$F = B I l$: force (N) = flux density (T) × current (A) × length in the field (m).", "motor-force-nn"),
    fact("Unit of magnetic flux density?", "Tesla, T (= N/A m).", "motor-force-nn"),
    fact("Three F = BIl traps?", "cm not converted to m; using the whole wire instead of the length in the field; forgetting F = 0 for a wire parallel to the field.", "motor-force-nn"),
    # T1
    fact("Chain for a magnet moving away from another?", "The two fields interact → like poles repel, so a force on X away from Y → X accelerates away.", "magnet-force-chains"),
    fact("Chain for a floating magnet?", "Fields interact → repulsive (upward) force on the upper magnet → equal to its weight, so the forces are balanced and it stays still.", "magnet-force-chains"),
    fact("Why is iron always attracted, never repelled?", "The magnet induces the opposite pole in the near end of the iron, whichever pole faces it.", "magnet-force-chains"),
    # T2
    fact("What does 'picks up a paper clip' prove?", "Only that it is magnetised now — possibly induced. Repulsion by a known magnet is the proof of a permanent magnet.", "magnet-test"),
    fact("Result that shows a nail is NOT a permanent magnet?", "No repulsion in either orientation (attraction the same at both ends, or none).", "magnet-test"),
    # T3
    fact("Field between two like poles facing?", "Lines curve away from each other; a neutral point midway where the field is zero.", "field-diagrams-mag"),
    fact("What earns the two marks on a field diagram?", "Shape: separate, non-crossing lines, pole to pole, closer at the poles. Direction: arrows out of N into S.", "field-diagrams-mag"),
    # T4
    fact("Direction of the Earth's field at the equator?", "Parallel to the surface, pointing (geographic) north.", "earth-magnet"),
    fact("Where do the Earth's field lines go into the Earth?", "Near the geographic north pole (the magnetic S pole); out near geographic south.", "earth-magnet"),
    fact("The 2024 three marks of evidence?", "Earth has a magnetic field; the compass points along the field; the core is magnetic / as if a magnet were inside the Earth (or a point read from the diagram).", "earth-magnet"),
    # T5
    fact("Field left → right, current out of the page: force?", "Up the page.", "flhr-diagrams"),
    fact("Field left → right, current into the page: force?", "Down the page.", "flhr-diagrams"),
    fact("Wire along the field lines: force?", "Zero.", "flhr-diagrams"),
    # T6
    fact("How much of a long wire counts in F = BIl?", "Only the length inside the field (e.g. the width of the poles).", "motor-force-hard"),
    fact("Force on a coil side with N turns?", "$N$ × the force on one wire: $F = B I l N$.", "motor-force-hard"),
    fact("The 2025 unfamiliar equation?", "B against distance, inverse square (B ∝ 1/d²); use it like any other — finding the constant alone was 1 of 3.", "motor-force-hard"),
    # T7
    fact("The six-step chain for a motor?", "Current in the coil → field around the coil → interacts with the permanent field → resultant force on the coil → force opposite on either side → so the coil rotates.", "dc-motor"),
    fact("What does the split-ring commutator do?", "Reverses the current in the coil every half turn, so the coil keeps rotating in the same direction.", "dc-motor"),
    fact("What happens with no commutator?", "The coil turns to the vertical, is pushed back, and rocks to a stop.", "dc-motor"),
    fact("Three ways to make a motor turn faster?", "More current, stronger magnets, more turns (or an iron core).", "dc-motor"),
    fact("The 2025 motor trap?", "Describing a dynamo: 'the motor does not produce a current' — the current comes from the supply.", "dc-motor"),
    # T8
    fact("Dependent variable in the electromagnet investigation?", "Its strength, measured as the number of nails (or clips) held, or the mass lifted.", "electromagnet-practical"),
    fact("Why not say 'inversely proportional' for a falling trend?", "It only means proportional to the reciprocal; say 'as X increases, Y decreases' and whether it is linear.", "electromagnet-practical"),
    fact("Why switch the electromagnet off between readings?", "So the coil does not heat up (changing the current) and the nails do not become permanent magnets.", "electromagnet-practical"),
]
