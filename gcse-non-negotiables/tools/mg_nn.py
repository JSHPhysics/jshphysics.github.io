"""
mg_nn.py — Topic 12 (Magnetism and the motor effect): the non-negotiables
N1–N10. Statements 12.1–12.9 are both tiers; 12.10–12.14P are Higher
only (N7, N8 and N9 carry H); 12.14P is also Physics only (T7 carries P).

N1 Poles and the test for a magnet     N6 The solenoid
N2 Permanent and induced magnets       N7 The motor effect [H]
N3 Field lines                         N8 Fleming's left-hand rule [H]
N4 Plotting compasses and the Earth    N9 F = BIl [H]
N5 The field around a wire             N10 Key words
"""

from revlib import (
    choice, diagram, ewau, explain, fact, group, mark_scheme, marks, numeric,
    practice, section, worked, written,
)
import mg_diagrams as dg

# The author's standard chain for the motor effect on a single wire, word
# for word from simple-motor/src/build.mjs (EXAM.wire). Keep identical.
WIRE_CHAIN = [
    "There is a current in the wire.",
    "This creates a magnetic field around the wire.",
    "This interacts with the permanent magnetic field.",
    "This causes a resultant force on the wire, so the wire accelerates.",
    "You can find the direction of the force using Fleming's left-hand rule.",
]


def chain_list(steps):
    return "<ol class='steps'>" + "".join("<li>" + step + "</li>" for step in steps) + "</ol>"


# ---------------------------------------------------------------------
# N1 · Poles
# ---------------------------------------------------------------------

section_n1 = section(
    "poles", "nn", "Poles: like repel, unlike attract — and repulsion is the only test", "12.1",
    equations=[r"\text{N–N or S–S: repel}", r"\text{N–S: attract}", r"\text{magnet–iron: attract either way}"],
    blurb="Unlike poles attract and like poles repel. A magnet attracts a piece of iron whichever way round it is, so attraction proves nothing — only repulsion shows that an object is itself a magnet.",
    checklist=[
        "State that like poles repel and unlike poles attract",
        "Explain why repulsion is the only test for a magnet",
        "Describe a test to show whether an object is a permanent magnet, with the expected result",
    ],
    parts=[
        explain(
            "The rule and the test",
            "<p>Every magnet has a <b>north-seeking (N) pole</b> and a <b>south-seeking (S) pole</b>; you cannot have one without the other. <b>Like poles repel</b> (N–N, S–S); <b>unlike poles attract</b> (N–S). Magnets also attract <b>magnetic materials</b> — iron, steel, cobalt, nickel — and they attract them <b>whichever pole</b> is nearer, because the magnet induces the opposite pole in the material (N2).</p>"
            "<p>So <b>attraction is not a test</b>: a magnet and a piece of unmagnetised iron attract, and so do two magnets with unlike poles facing. <b>Repulsion is</b>: only two magnets can repel. The June 2025 report (Q7(b)(iv), nails that may or may not be permanently magnetised): one mark for a <b>suitable test</b>, one for a <b>clear statement of the expected result</b>. \"Try to pick up a paper clip\" scored 1 of 2 — it did not say what the result would mean. The full-mark answer brought one end of a nail up to one end of another, then <b>turned one nail round</b>: if they are not magnets there is <b>attraction in both orientations</b> (or none at all), and never repulsion; if they are magnets, one orientation <b>repels</b>.</p>",
        ),
        worked(
            "Is the nail a magnet?",
            "A student thinks an iron nail has become a permanent magnet. Describe how she could test this, and state the result she would expect if she is right. (2 marks)",
            [
                "Bring one end of the nail close to one pole of a <b>known magnet</b> (or a compass needle), then <b>reverse the nail</b> and bring the other end to the same pole.",
                "If the nail is a magnet, one end is <b>attracted</b> and the other is <b>repelled</b>. If it is not, <b>both ends are attracted</b> — attraction alone proves nothing, because the magnet would attract any iron.",
            ],
        ),
        practice("Poles", [
            choice("mg-n1-q1", "Two bar magnets are placed end to end and they push apart. Which is true?",
                   ["N is facing S", "Like poles are facing each other", "One of them is not a magnet", "They are both unmagnetised iron"], 1,
                   "Only like poles repel, and only magnets can repel."),
            written("mg-n1-q2", "A steel bar is attracted to the N pole of a magnet. Explain why this does not show that the bar is a magnet. (2)",
                    marks(["A magnet attracts any <b>magnetic material</b> (steel), because it <b>induces</b> the opposite pole in it — so an unmagnetised bar would also be attracted.", "Only <b>repulsion</b> shows the bar is a magnet, because only two magnets (like poles) can repel."]), lines=3),
            choice("mg-n1-q3", "Which observation proves that an object is a permanent magnet?",
                   ["It is attracted to a magnet", "It picks up a paper clip", "It is repelled by one pole of a magnet", "It is heavier than a non-magnet"], 2,
                   "Repulsion is the only test."),
            written("mg-n1-q4", "Describe a test to show that a bar is not a permanent magnet, and state the expected result. (2)",
                    marks(["Bring each end of the bar in turn to the <b>same pole</b> of a magnet (or a compass needle) — i.e. test both orientations.", "Expected result if it is not a magnet: <b>attraction in both orientations</b> (no repulsion either way)."]), lines=3),
            choice("mg-n1-q5", "Which of these is NOT a magnetic material?",
                   ["Iron", "Nickel", "Copper", "Cobalt"], 2,
                   "Iron, steel, cobalt and nickel are magnetic; copper, aluminium and brass are not."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N2 · Permanent and induced magnets
# ---------------------------------------------------------------------

section_n2 = section(
    "permanent-induced", "nn", "Permanent and induced magnets, and what each is used for", "12.2, 12.3",
    equations=[r"\text{permanent: its own field, always}", r"\text{induced: a magnet only while in a field}"],
    blurb="A permanent magnet produces its own magnetic field all the time. An induced (temporary) magnet becomes a magnet only when it is in another magnetic field, and loses most of its magnetism when the field is removed. Steel keeps its magnetism; iron does not.",
    checklist=[
        "Explain the difference between a permanent and an induced magnet",
        "Name the four magnetic materials and say which make permanent and which temporary magnets",
        "Give a use of each kind of material",
    ],
    parts=[
        explain(
            "Permanent versus induced",
            "<p>A <b>permanent magnet</b> produces its <b>own magnetic field</b> and keeps it. An <b>induced magnet</b> is a magnetic material that <b>becomes a magnet when it is placed in a magnetic field</b>: the pole nearest the permanent magnet is the <b>opposite</b> pole, so induced magnetism always causes <b>attraction</b>. Take the field away and an induced magnet <b>loses most or all</b> of its magnetism — that is why it is also called a <b>temporary</b> magnet.</p>"
            "<table class='tbl'><tr><th>Material</th><th>Behaviour</th><th>Used for</th></tr>"
            "<tr><td><b>Steel</b> (and alloys with cobalt or nickel)</td><td><b>hard</b> magnetic material: hard to magnetise, but <b>keeps</b> its magnetism</td><td><b>permanent magnets</b>: compass needles, fridge magnets, the magnets in motors, loudspeakers and generators</td></tr>"
            "<tr><td><b>Iron</b> (soft iron)</td><td><b>soft</b> magnetic material: easy to magnetise, <b>loses</b> its magnetism as soon as the field is removed</td><td><b>temporary magnets</b>: the core of an electromagnet, transformer cores, relays and electric bells — anything that must switch off</td></tr>"
            "<tr><td>Cobalt, nickel</td><td>magnetic materials; used mainly in alloys for strong permanent magnets</td><td>permanent magnets in headphones, small motors</td></tr></table>"
            "<p>The exam phrasing: \"<b>explain why a steel core would not be suitable</b> for an electromagnet\" — because steel <b>keeps its magnetism</b> when the current is switched off, so the electromagnet could not be switched off; iron loses its magnetism, so it can.</p>",
        ),
        worked(
            "The 2-mark difference",
            "Explain the difference between a permanent magnet and an induced magnet. (2 marks)",
            [
                "A <b>permanent magnet</b> produces its <b>own magnetic field</b> all the time (it does not need another field to be a magnet).",
                "An <b>induced magnet</b> only becomes a magnet <b>while it is in a magnetic field</b> (of a permanent magnet or an electromagnet), and <b>loses its magnetism</b> when that field is removed.",
            ],
        ),
        practice("Permanent and induced magnets", [
            written("mg-n2-q1", "An iron nail is held close to a bar magnet and picks up some paper clips. When the magnet is taken away the clips fall off. Explain these observations. (3)",
                    marks(["In the magnet's field the nail becomes an <b>induced magnet</b>…", "…so it has poles of its own and <b>attracts</b> the clips (which are themselves induced magnets).", "Iron is a <b>soft</b> magnetic material, so when the field is removed the nail <b>loses its magnetism</b> and no longer attracts the clips."]), lines=4),
            choice("mg-n2-q2", "Why is iron, not steel, used for the core of an electromagnet?",
                   ["Iron is a stronger magnet", "Iron loses its magnetism when the current is switched off, so the electromagnet can be switched off", "Steel is not magnetic", "Iron is cheaper"], 1,
                   "Steel would stay magnetised: the electromagnet could not be switched off."),
            choice("mg-n2-q3", "Which pole is induced in the end of an iron bar nearest the N pole of a magnet?",
                   ["N", "S", "Both", "Neither — iron has no poles"], 1,
                   "The opposite pole is induced, which is why induced magnetism always attracts."),
            written("mg-n2-q4", "Give one use of a permanent magnet and one use of a temporary magnet. (2)",
                    marks(["Permanent: e.g. a <b>compass needle</b>, the magnets in a <b>motor</b>, <b>loudspeaker</b> or generator, a fridge magnet.", "Temporary: the <b>core of an electromagnet</b> (scrapyard crane, electric bell, relay, circuit breaker), a transformer core."]), lines=2),
            choice("mg-n2-q5", "A magnetic material that is easy to magnetise and easy to demagnetise is described as…",
                   ["hard", "soft", "permanent", "induced-proof"], 1,
                   "Soft iron: easy both ways. Steel is 'hard': difficult to magnetise and keeps it."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N3 · Field lines
# ---------------------------------------------------------------------

section_n3 = section(
    "field-lines", "nn", "Magnetic field lines: N to S, never crossing, closer means stronger", "12.4",
    equations=[r"\text{direction: N} \rightarrow \text{S outside the magnet}", r"\text{closer lines} = \text{stronger field}"],
    blurb="A magnetic field is the region around a magnet where a magnetic material or another magnet experiences a force. Field lines show its direction (the way a free N pole would move: from N to S outside the magnet) and its strength (the closer the lines, the stronger the field). Between two facing unlike poles the field is uniform: parallel, equally spaced lines.",
    checklist=[
        "Draw the field around a bar magnet with arrows from N to S",
        "Draw the uniform field between two facing unlike poles",
        "Relate the strength of the field to how close the lines are",
    ],
    parts=[
        explain(
            "Reading and drawing field lines",
            diagram(dg.bar_magnet_svg(), 720, 270, "The field of a bar magnet, and the uniform field between an N and an S pole.") +
            "<p>A <b>magnetic field</b> is the region around a magnet in which a <b>magnetic material</b> (or another magnet, or a current) <b>experiences a force</b>. The field is drawn as <b>field lines</b> with arrows showing the direction of the force on a <b>N pole</b> placed there: lines <b>leave the N pole</b>, curve round and <b>enter the S pole</b>. The <b>strength</b> of the field is shown by how close the lines are: they are <b>closest at the poles</b>, where the field is strongest, and further apart as you move away.</p>"
            "<p>Between two <b>unlike poles facing each other</b> the lines are <b>straight, parallel and equally spaced</b> from N to S: a <b>uniform field</b>, the same strength and direction everywhere — the field a wire sits in for the motor effect (the motor-effect section, Higher).</p>"
            "<p>The June 2023 report (Q5(a), two magnets): lines drawn <b>overlapping or crossing</b>, or several from the same point on a pole, scored 1 of 2 — \"the lines never touch each other and never overlap or cross\". Both marks: arrows <b>away from N</b>, lines <b>clean and separate</b>, more of them near the poles.</p>",
        ),
        worked(
            "Marking a field diagram",
            "A student draws the field around a bar magnet. Her lines leave the N pole, curve round to the S pole, do not cross, and carry arrows — but the arrows point into the N pole. How many of the 2 marks does she get? (2 marks)",
            [
                "<b>Shape</b>: lines from pole to pole, separate, not crossing — the shape mark is earned.",
                "<b>Direction</b>: the arrows must point <b>out of N and into S</b>; hers point the wrong way, so the direction mark is lost. <b>1 of 2.</b>",
            ],
        ),
        practice("Field lines", [
            choice("mg-n3-q1", "Field lines around a bar magnet point…",
                   ["from S to N outside the magnet", "from N to S outside the magnet", "towards the middle of the magnet", "in no particular direction"], 1,
                   "Out of N, into S (outside the magnet)."),
            written("mg-n3-q2", "State two things the field-line diagram of a magnet tells you, and how. (2)",
                    marks(["The <b>direction</b> of the field: the arrows (the direction a N pole would be pushed, N → S).", "The <b>strength</b> of the field: how <b>close together</b> the lines are — closer means stronger."]), lines=2),
            choice("mg-n3-q3", "Where is the field of a bar magnet strongest?",
                   ["In the middle of the magnet's side", "At the poles, where the lines are closest", "Far from the magnet", "Between the two poles on the outside"], 1,
                   "Lines are closest at the poles."),
            written("mg-n3-q4", "Describe the magnetic field between the N pole of one magnet and the S pole of another, placed facing each other a few centimetres apart. (2)",
                    marks(["A <b>uniform</b> field: the lines are <b>straight, parallel and equally spaced</b>…", "…pointing <b>from the N pole to the S pole</b>; the strength and direction are the same everywhere between them."]), lines=2),
            choice("mg-n3-q5", "A student's field diagram has two lines that cross. Why is this wrong?",
                   ["Field lines must be straight", "At a crossing point the field would have two directions at once, which is impossible", "There should only be one line", "Crossing lines mean the magnet is broken"], 1,
                   "One direction per point: lines never cross or touch."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N4 · Plotting compasses and the Earth
# ---------------------------------------------------------------------

section_n4 = section(
    "compass-earth", "nn", "Plotting compasses and the Earth's magnetic field", "12.5, 12.6",
    equations=[r"\text{compass N pole} \rightarrow \text{points along the field}", r"\text{geographic north} = \text{a magnetic S pole}"],
    blurb="A plotting compass is a small magnet on a pivot: its N pole points along the field at that spot, so moving it step by step traces a field line. Away from any magnet it points north, because the Earth has a magnetic field — evidence that the Earth's core is magnetic, with a magnetic S pole near geographic north.",
    checklist=[
        "Describe how to plot a field line with a plotting compass",
        "Explain how a compass shows that the Earth has a magnetic field and that its core must be magnetic",
        "State which magnetic pole is near geographic north, and why a compass points north",
    ],
    parts=[
        explain(
            "The compass and the Earth",
            diagram(dg.earth_svg(), 720, 280, "The Earth's field is like that of a bar magnet inside it, with its S pole near geographic north. A compass needle's N pole is attracted towards it.") +
            "<p><b>Plotting a field</b>: put the magnet on paper, place a plotting compass near one pole and mark a dot at each end of the needle; move the compass so its tail sits on the dot its head made; repeat until you reach the other pole, then join the dots and add an arrow in the direction the <b>N end</b> pointed. Repeat from other starting points for more lines. The compass needle is itself a <b>small magnet</b>, so its N pole points along the field, <b>towards the S pole</b> of the magnet.</p>"
            "<p><b>The Earth</b>: away from any magnet a compass still points <b>north</b>. A compass only points when there is a magnetic field, so the <b>Earth has a magnetic field</b>; its shape (traced by compasses, with the field running parallel to the ground at the equator and dipping into the ground near the poles) is the shape of a <b>bar magnet's</b> field, so <b>the core of the Earth must be magnetic</b>. Because a compass's <b>N pole</b> is attracted to it, the pole near <b>geographic north is a magnetic S pole</b>. The June 2024 scheme (Q5(a)(ii), 3 marks): \"the Earth has a magnetic field\"; \"the compass needle points in the direction of the field\"; \"the core is magnetic / as if there were a magnet inside the Earth\"; or a point read from the diagram such as \"the field goes into the Earth at the north pole\".</p>",
        ),
        worked(
            "Why a compass points north",
            "Explain why a magnetic compass points north, and what this tells us about the Earth. (3 marks)",
            [
                "The compass needle is a <b>small permanent magnet</b> free to turn, so it lines up with any magnetic field it is in, its N pole pointing along the field.",
                "It points north everywhere on Earth, so the <b>Earth has a magnetic field</b> — the Earth's <b>core must be magnetic</b>, acting like a bar magnet inside the Earth.",
                "The needle's N pole is attracted to an <b>unlike pole</b>, so the magnetic pole near geographic north is a <b>magnetic S pole</b>.",
            ],
        ),
        practice("Compasses and the Earth", [
            written("mg-n4-q1", "Describe how to use a plotting compass to show the shape and direction of the field around a bar magnet. (3)",
                    marks(["Place the compass near one <b>pole</b>; mark a <b>dot at each end</b> of the needle.", "<b>Move the compass</b> so the tail of the needle is on the dot the head made; mark again; repeat to the other pole and <b>join the dots</b>.", "Add an <b>arrow</b> in the direction the N end pointed; repeat from other starting points to get more lines."]), lines=4),
            choice("mg-n4-q2", "The magnetic pole of the Earth near geographic north is…",
                   ["a magnetic N pole", "a magnetic S pole", "not a pole", "both poles"], 1,
                   "The compass N pole is attracted to it, and unlike poles attract."),
            written("mg-n4-q3", "A compass needle points north wherever it is taken on the Earth's surface. Explain what this is evidence for. (2)",
                    marks(["A compass only points when it is in a <b>magnetic field</b>, so the <b>Earth has a magnetic field</b>.", "The field is like a bar magnet's, so the <b>core of the Earth must be magnetic</b>."]), lines=2),
            choice("mg-n4-q4", "A plotting compass is placed near the N pole of a bar magnet. Its needle's N end points…",
                   ["towards the magnet's N pole", "away from the magnet's N pole, along the field line", "at right angles to the field", "always north"], 1,
                   "Like poles repel: the needle's N end points away from the magnet's N pole, along the field line towards S."),
            choice("mg-n4-q5", "At the equator the Earth's field is parallel to the ground; near the poles it dips steeply into the ground. This matches the field of…",
                   ["a solenoid with no core", "a bar magnet inside the Earth", "a straight wire", "a flat sheet"], 1,
                   "The 2024 scheme: 'as if there were a magnet inside the Earth'."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N5 · The field around a straight wire
# ---------------------------------------------------------------------

section_n5 = section(
    "wire-field", "nn", "A current makes a magnetic field: the straight wire", "12.7, 12.8",
    equations=[r"\text{circles centred on the wire}", r"\text{stronger: more current, closer to the wire}"],
    blurb="A wire carrying a current has a magnetic field around it: concentric circles centred on the wire. The direction comes from the right-hand grip rule (thumb along the current, fingers curl with the field) and reverses when the current reverses. The field is stronger with a larger current and closer to the wire.",
    checklist=[
        "Describe how to show that a current produces a magnetic field",
        "Draw the field around a straight wire and give its direction from the current direction",
        "State the two things the strength of the field depends on",
    ],
    parts=[
        explain(
            "Showing it, and its shape",
            diagram(dg.wire_field_svg(), 670, 295, "The field around a straight wire seen end on: circles, anticlockwise for current out of the page, clockwise for current into it.") +
            "<p><b>Showing that a current has a magnetic effect</b>: pass a straight wire vertically through a horizontal card, place plotting compasses (or sprinkle iron filings) on the card around it, and switch on a large current. The compasses line up in <b>circles</b> round the wire; switch off and they return to pointing north; <b>reverse the current</b> and every compass <b>turns round</b>. The field is a set of <b>concentric circles</b> centred on the wire, in a plane at right angles to it.</p>"
            "<p><b>Direction — the right-hand grip rule</b>: grip the wire with your <b>right</b> hand, <b>thumb along the current</b> (conventional, + to −); your <b>fingers curl the way the field goes</b>. Seen end on, current <b>out of the page</b> (dot) gives an <b>anticlockwise</b> field; current <b>into the page</b> (cross) gives <b>clockwise</b>.</p>"
            "<p><b>Strength</b>: the field is stronger with a <b>larger current</b>, and <b>weaker further from the wire</b> — the circles are drawn further apart as the distance increases. The June 2025 paper (Q7(c)) gave an unfamiliar equation for B against distance d and expected it to be used like any other; only a few noticed it was an <b>inverse square</b>. You will not be asked to recall any equation for this — just that <b>more current and less distance mean a stronger field</b>.</p>",
        ),
        worked(
            "Describing the field",
            "A long straight wire carries a current. Describe the magnetic field around it, including how its direction and strength can be changed. (4 marks)",
            [
                "The field lines are <b>concentric circles</b> centred on the wire, in planes at right angles to it.",
                "Their direction is given by the <b>right-hand grip rule</b>: thumb along the current, fingers show the field.",
                "<b>Reversing the current reverses</b> the direction of the field.",
                "The field is <b>stronger for a larger current</b> and <b>weaker further from the wire</b> (the circles are further apart).",
            ],
        ),
        practice("The field around a wire", [
            choice("mg-n5-q1", "Seen end on, a wire carries current into the page (cross). Its magnetic field is…",
                   ["straight lines pointing away from the wire", "clockwise circles", "anticlockwise circles", "parallel lines"], 1,
                   "Right-hand grip: thumb into the page, fingers curl clockwise."),
            written("mg-n5-q2", "Describe how you could show that a current in a wire produces a magnetic field. (3)",
                    marks(["Pass the wire <b>vertically through a card</b> with <b>plotting compasses</b> (or iron filings) on it.", "With the current on, the compasses line up in <b>circles</b> around the wire; with it off, they point north.", "<b>Reversing the current reverses</b> the compasses, showing the field direction depends on the current direction."]), lines=4),
            choice("mg-n5-q3", "Which change makes the field around a straight wire weaker at a given point?",
                   ["Increasing the current", "Moving the point closer to the wire", "Moving the point further from the wire", "Reversing the current"], 2,
                   "Strength falls with distance; reversing only changes direction."),
            written("mg-n5-q4", "State two factors that affect the strength of the magnetic field around a long straight wire. (2)",
                    marks(["The <b>size of the current</b> (larger current, stronger field).", "The <b>distance from the wire</b> (further away, weaker field)."]), lines=2),
            choice("mg-n5-q5", "A plotting compass next to a wire turns round when the current is reversed. This shows that…",
                   ["the current has stopped", "the direction of the field depends on the direction of the current", "the compass is broken", "the wire has become a permanent magnet"], 1,
                   "Field direction follows the current direction."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N6 · The solenoid
# ---------------------------------------------------------------------

section_n6 = section(
    "solenoid", "nn", "The solenoid: fields add inside, cancel outside", "12.9",
    equations=[r"\text{inside: strong, almost uniform}", r"\text{outside: weak, bar-magnet shape}"],
    blurb="A solenoid is a long coil of wire. Inside it, the fields of all the turns point the same way and add up to a strong, almost uniform field along the axis; outside, they largely cancel, leaving a weaker field with the shape of a bar magnet's. An iron core makes it an electromagnet.",
    checklist=[
        "Explain why the field inside a solenoid is strong and almost uniform",
        "Explain why the field outside is weaker, and describe its shape",
        "State three ways to make an electromagnet stronger",
    ],
    parts=[
        explain(
            "Why a coil beats a wire",
            diagram(dg.solenoid_svg(), 640, 305, "The field of a solenoid: straight and close together inside, a bar magnet's shape outside.") +
            "<p>A <b>solenoid</b> is a wire wound into a long coil. Each turn has the circular field of N5. <b>Inside</b> the coil the fields of all the turns point <b>the same way along the axis</b>, so they <b>add together</b> to give a <b>very strong, almost uniform</b> field (straight, parallel, equally spaced lines along the centre). <b>Outside</b> the coil the fields of neighbouring turns point in <b>opposite directions</b> and largely <b>cancel</b>, so the field there is <b>weaker</b>; what is left has the <b>same shape as a bar magnet's field</b>, with a N pole at one end and a S pole at the other. The spec's own words (12.9): the fields from individual coils \"<b>add together</b> to form a very strong almost uniform field along the centre\" and \"<b>cancel</b> to give a weaker field outside\".</p>"
            "<p>An <b>electromagnet</b> is a solenoid with a <b>soft iron core</b>, which becomes an induced magnet and makes the field far stronger — and switches off with the current (N2). <b>Stronger electromagnet</b>: more <b>current</b>, more <b>turns</b> (per unit length), an <b>iron core</b>. <b>Reverse the current</b> and the poles swap.</p>",
        ),
        worked(
            "The 3-mark explanation",
            "Explain why the magnetic field inside a solenoid is much stronger than the field around a single straight wire carrying the same current. (3 marks)",
            [
                "Each turn of the solenoid produces its own magnetic field (circles around the wire).",
                "Inside the coil the fields of <b>all the turns point the same way</b>, so they <b>add together</b>…",
                "…giving a strong, almost <b>uniform</b> field along the centre — many turns' worth of field in the same place.",
            ],
        ),
        practice("The solenoid", [
            choice("mg-n6-q1", "The field outside a solenoid is weak because…",
                   ["the wire is too thin", "the fields of neighbouring turns point in opposite directions there and cancel", "there is no current outside", "field lines cannot leave a coil"], 1,
                   "Cancel outside, add inside."),
            written("mg-n6-q2", "Describe the magnetic field inside and outside a solenoid. (3)",
                    marks(["Inside: <b>strong</b> and <b>almost uniform</b> — straight, parallel, equally spaced lines along the axis.", "Outside: <b>weaker</b>…", "…with the <b>shape of a bar magnet's field</b>: a N pole at one end, a S pole at the other."]), lines=3),
            choice("mg-n6-q3", "Which does NOT increase the strength of an electromagnet?",
                   ["More turns on the coil", "A larger current", "An iron core", "Using thinner card for the coil to sit on"], 3,
                   "Turns, current and core are the three."),
            written("mg-n6-q4", "An electromagnet is used in a scrapyard crane to lift and drop cars. Explain why it has a soft iron core and not a steel one. (2)",
                    marks(["Soft iron becomes an induced magnet in the coil's field, making the electromagnet <b>much stronger</b>, and <b>loses its magnetism</b> as soon as the current is switched off — so the car can be dropped.", "Steel would <b>keep its magnetism</b> when the current is off, so the car could not be released."]), lines=3),
            choice("mg-n6-q5", "Reversing the current in a solenoid…",
                   ["switches the field off", "swaps its N and S poles", "makes the field stronger", "has no effect on the field"], 1,
                   "Field direction follows current direction, so the poles swap."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N7 · The motor effect [H]
# ---------------------------------------------------------------------

section_n7 = section(
    "motor-effect", "nn", "The motor effect: two fields interact, so there is a force on the wire", "12.10, 12.11",
    equations=[r"\text{current} \rightarrow \text{field} \rightarrow \text{fields interact} \rightarrow \text{force} \rightarrow \text{accelerates}"],
    blurb="A wire carrying a current in a magnetic field experiences a force, and an equal and opposite force acts on the magnet. The force is the interaction between the wire's own magnetic field and the magnet's field. The standard five-step chain below is the one to write every time.",
    tags=["H"],
    checklist=[
        "Write the five-step chain for the motor effect on a wire",
        "State that an equal and opposite force acts on the magnet",
        "Explain that the force is due to the interaction between two magnetic fields",
    ],
    parts=[
        explain(
            "The chain to write every time",
            diagram(dg.motor_effect_svg(), 720, 255, "A wire between the poles of a magnet: the wire's own circular field adds to the magnet's field on one side and cancels it on the other, so there is a resultant force on the wire.") +
            "<p>A current-carrying wire placed in a magnetic field <b>experiences a force</b> — the <b>motor effect</b>. Why: the current creates a <b>magnetic field around the wire</b>; this <b>interacts with the permanent magnet's field</b>; where the two point the same way the field is stronger, where they oppose it is weaker, and the result is a <b>resultant force on the wire</b> from the strong side towards the weak side. By Newton's third law an <b>equal and opposite force acts on the magnet</b>. The standard explanation, in the steps the marks are on:</p>"
            + chain_list(WIRE_CHAIN) +
            "<p>Two things the examiners want and students leave out: the force is <b>due to the interaction between the two magnetic fields</b> (12.11) — not \"the magnet pushes the wire\"; and the chain ends with <b>what happens</b>: a resultant force, so the wire <b>accelerates</b> (or, if it is held, is pushed against what holds it). The June 2023 report (Q5(b), one magnet floating above another): \"repulsion\" alone scored one mark; the second mark needed \"<b>the interaction between the two magnetic fields</b>\" — the same idea.</p>"
            "<p>The force is <b>at right angles</b> to both the current and the field (direction from Fleming's left-hand rule, N8). It is <b>largest when the wire is at right angles to the field</b> and <b>zero when the wire is parallel</b> to it. It reverses if <b>either</b> the current or the field is reversed, and grows with more current, a stronger field or more wire in the field (N9).</p>",
        ),
        worked(
            "Why the wire jumps",
            "A straight wire is placed between the poles of a horseshoe magnet. When the current is switched on the wire jumps out of the magnet. Explain why. (4 marks)",
            [
                "There is a <b>current in the wire</b>. This <b>creates a magnetic field around the wire</b>.",
                "This <b>interacts with the permanent magnetic field</b>.",
                "This causes a <b>resultant force on the wire</b>, so the wire <b>accelerates</b> — out of the magnet.",
                "You can find the direction of the force using <b>Fleming's left-hand rule</b> (it is at right angles to both the current and the field).",
            ],
        ),
        practice("The motor effect", [
            written("mg-n7-q1", "A wire carrying a current is placed at right angles to the field between two magnets. Explain why there is a force on the wire. (3)",
                    marks(["The current in the wire <b>creates a magnetic field</b> around the wire.", "This field <b>interacts with the permanent magnetic field</b> of the magnets.", "The interaction causes a <b>resultant force on the wire</b>, so the wire accelerates."]), lines=3),
            choice("mg-n7-q2", "A wire carrying a current experiences a force from a magnet. What force acts on the magnet?",
                   ["None — magnets do not feel forces", "An equal and opposite force", "A force in the same direction as the force on the wire", "A smaller force"], 1,
                   "Newton's third law: the magnet feels an equal and opposite force."),
            choice("mg-n7-q3", "When is the force on a current-carrying wire in a magnetic field zero?",
                   ["When the wire is at right angles to the field", "When the wire is parallel to the field", "When the current is large", "It is never zero"], 1,
                   "Parallel: no force. At right angles: maximum."),
            written("mg-n7-q4", "A student writes: \"The magnet pushes the wire.\" Rewrite the explanation so that it earns the 'interaction' mark. (2)",
                    marks(["The current in the wire produces its own <b>magnetic field</b>…", "…which <b>interacts with the magnet's field</b>; the force on the wire is due to this <b>interaction between the two magnetic fields</b>."]), lines=2),
            choice("mg-n7-q5", "Which change makes the force on the wire larger without changing its direction?",
                   ["Reversing the current", "Reversing the magnetic field (turning the magnet round)", "Doubling the current", "Turning the wire so it lies along the field"], 2,
                   "Doubling the current doubles the force and keeps its direction. Reversing either reverses it; a wire along the field feels no force at all."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N8 · Fleming's left-hand rule [H]
# ---------------------------------------------------------------------

section_n8 = section(
    "flhr", "nn", "Fleming's left-hand rule: thumb force, first finger field, second finger current", "12.12",
    equations=[r"\text{thuMb: Motion (force)}", r"\text{First finger: Field (N} \rightarrow \text{S)}", r"\text{seCond finger: Current (+} \rightarrow \text{−)}"],
    blurb="Hold the left hand with thumb, first finger and second finger at right angles to each other. First finger along the field (N to S), second finger along the conventional current (+ to −), and the thumb gives the direction of the force (the motion). It only applies when the current and field are at right angles.",
    tags=["H"],
    checklist=[
        "State what each of the three digits represents",
        "Use the rule to find the missing one of force, field and current on a diagram",
        "State that the rule applies when the three directions are mutually perpendicular",
    ],
    parts=[
        explain(
            "The rule",
            diagram(dg.flhr_svg(), 660, 285, "Fleming's left-hand rule: three directions at right angles to each other.") +
            "<p>Use the <b>left</b> hand. Hold the <b>thumb</b>, <b>first finger</b> and <b>second finger</b> so that each is at right angles to the other two. Then: <b>First finger = Field</b>, pointing the way the field lines go (<b>N to S</b>); <b>seCond finger = Current</b>, pointing the way the <b>conventional current</b> goes (<b>+ to −</b>, not the electron flow); <b>thuMb = Motion</b>, the direction of the <b>force</b> on the wire (and so the way it moves). The three are <b>mutually perpendicular</b>: the rule represents \"the relative directions of the force, the current and the magnetic field for cases where they are mutually perpendicular\" (12.12). If the current is <b>parallel</b> to the field there is <b>no force</b> and the rule does not apply.</p>"
            "<p>In the exam the picture is usually <b>end on</b>: a dot is current <b>out of the page</b>, a cross is current <b>into the page</b>. Point the second finger at yourself for a dot, away for a cross, line the first finger up with the field arrows, and read the thumb. Reversing the current <b>or</b> the field reverses the force; reversing <b>both</b> leaves it unchanged. The June 2024 scheme (Q5(b)(ii)): to reverse the force on a coil, \"any clear action that will reverse the current\" (swap the battery connections) <b>or</b> \"any clear action that will reverse the poles\" (turn the magnet round).</p>",
        ),
        worked(
            "Reading a diagram",
            "A wire between the poles of a magnet carries a current out of the page. The magnetic field points from left to right. Find the direction of the force on the wire. (2 marks)",
            [
                "First finger along the <b>field</b>: pointing to the <b>right</b>. Second finger along the <b>current</b>: pointing <b>out of the page</b>, towards you.",
                "With both in place the thumb points <b>upwards</b> — the force on the wire is <b>up the page</b>.",
            ],
        ),
        practice("Fleming's left-hand rule", [
            choice("mg-n8-q1", "In Fleming's left-hand rule the first finger represents…",
                   ["the force", "the current", "the magnetic field", "the motion of the magnet"], 2,
                   "First finger: Field. Second: Current. Thumb: Motion (force)."),
            choice("mg-n8-q2", "A wire carries current into the page; the field points from left to right. The force on the wire is…",
                   ["up the page", "down the page", "to the left", "zero"], 1,
                   "Second finger away from you, first finger right: thumb points down."),
            written("mg-n8-q3", "State two ways of reversing the direction of the force on a current-carrying wire in a magnetic field. (2)",
                    marks(["<b>Reverse the current</b> (e.g. swap the connections to the battery).", "<b>Reverse the magnetic field</b> (e.g. turn the magnet round so the poles swap)."]), lines=2),
            choice("mg-n8-q4", "A wire lies parallel to the field lines between two magnets and carries a current. The force on it is…",
                   ["maximum", "zero", "upwards", "towards the N pole"], 1,
                   "The rule needs the current and field at right angles; parallel means no force."),
            choice("mg-n8-q5", "The second finger must point in the direction of…",
                   ["electron flow, − to +", "conventional current, + to −", "the field, N to S", "the force"], 1,
                   "Conventional current. Using electron flow gives the opposite answer."),
            choice("mg-n8-q6", "The field points up the page and the force on a wire is out of the page (towards you). The current in the wire is…",
                   ["to the right", "to the left", "up the page", "into the page"], 0,
                   "Set first finger up, thumb towards you: the second finger points right. (Check: field up, current right, force out of the page.)"),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N9 · F = BIl [H]
# ---------------------------------------------------------------------

section_n9 = section(
    "motor-force-nn", "nn", "The size of the force: F = B I l", "12.13",
    equations=[r"F = B\,I\,l", r"B \text{ in tesla (T)} = \text{N/A m}"],
    blurb="For a wire at right angles to the field, the force is magnetic flux density × current × length of wire in the field: $F = BIl$, with $B$ in tesla; the equation is on the list, so the skill is choosing it, converting cm to m, and rearranging for B, I or l.",
    tags=["H"],
    checklist=[
        "Use $F = BIl$ for a wire at right angles to the field",
        "Give the unit of magnetic flux density and convert cm and mA before substituting",
        "Rearrange for B, I or l",
    ],
    parts=[
        explain(
            "The equation and its units",
            "<p>For a conductor <b>at right angles</b> to a magnetic field: <b>force (N) = magnetic flux density (T) × current (A) × length (m)</b>, $F = B I l$. <b>Magnetic flux density</b> $B$ is the strength of the field, in <b>tesla</b> (T); 1 T = 1 N/A m, i.e. the field in which 1 m of wire carrying 1 A feels 1 N — a large unit, so exam fields are usually tenths of a tesla or millitesla. $l$ is the length of wire <b>in the field</b>, in metres. The equation is on the equation list, so the marks are for choosing it, <b>converting cm to m</b> and mA to A, substituting and rearranging. The June 2023 report (Q5(c)(ii)): almost every candidate selected and used it correctly; the June 2024 scheme (Q5(b)(iii)) gave one mark for \"rearrangement and substitution\" and one for the evaluation, 0.58 T, with full marks for a correct answer without working.</p>"
            "<p>Three traps: leaving the length in centimetres (force 100 times too big); using the <b>whole</b> length of a wire when only part of it is in the field; and forgetting the force is <b>zero</b> for a wire parallel to the field, whatever $B$, $I$ and $l$ are.</p>",
        ),
        worked(
            "Finding B",
            "A wire of length 5.0 cm carries a current of 2.5 A at right angles to a magnetic field. The force on it is 0.030 N. Calculate the magnetic flux density. (3 marks)",
            [
                "$l = 5.0$ cm $= 0.050$ m. Known: $F = 0.030$ N, $I = 2.5$ A.",
                "Rearrange $F = B I l$: $B = F \\div (I \\times l) = 0.030 \\div (2.5 \\times 0.050)$.",
                "$B = 0.030 \\div 0.125 = 0.24$ T.",
            ],
        ),
        practice("F = BIl", [
            numeric("mg-n9-q1", "A wire 0.20 m long carries 4.0 A at right angles to a field of flux density 0.15 T. Calculate the force on it.", 0.12, "N",
                    "$F = B \\times I \\times l$ — all three already in base units.",
                    ewau(r"$F = B I l$", r"F = 0.15 \times 4.0 \times 0.20", "0.12", "N")),
            numeric("mg-n9-q2", "A 12 cm length of wire carries a current of 0.50 A across a field of 0.80 T. Calculate the force.", 0.048, "N",
                    "Convert 12 cm to metres first.",
                    [r"$l = 12$ cm $= 0.12$ m"] + ewau(r"$F = B I l$", r"F = 0.80 \times 0.50 \times 0.12", "0.048", "N")),
            numeric("mg-n9-q3", "The force on a 0.40 m wire in a field of 0.25 T is 0.30 N. Calculate the current.", 3.0, "A",
                    "$I = F \\div (B \\times l)$.",
                    ewau(r"I = F \div (B l)", r"I = 0.30 \div (0.25 \times 0.40) = 0.30 \div 0.10", "3.0", "A")),
            numeric("mg-n9-q4", "A wire carries 1.5 A. A 25 cm length of it lies in a field of 0.040 T at right angles. Calculate the force in millinewtons.", 15, "mN",
                    "Work in N, then × 1000.",
                    ewau(r"$F = B I l$", r"F = 0.040 \times 1.5 \times 0.25 = 0.015 \text{ N}", "15", "mN (× 1000)")),
            choice("mg-n9-q5", "Which is a correct unit for magnetic flux density?",
                   ["N/A", "N/A m", "T/m", "A m/N"], 1,
                   "1 T = 1 N/A m, from $B = F \\div (I l)$."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N10 · Key words
# ---------------------------------------------------------------------

DEFINITIONS = [
    ("Magnetic material", "A material that is <b>attracted by a magnet</b> and can be magnetised: <b>iron, steel, cobalt, nickel</b>.", "\"metal\" — copper and aluminium are not magnetic"),
    ("Permanent magnet", "A magnet that produces its <b>own magnetic field</b> all the time (steel, or alloys of cobalt and nickel).", "\"a strong magnet\""),
    ("Induced (temporary) magnet", "A magnetic material that becomes a magnet <b>only while it is in a magnetic field</b>, and loses its magnetism when the field is removed (soft iron).", "\"a weak magnet\""),
    ("Magnetic field", "The <b>region around a magnet</b> (or a current) in which a <b>magnetic material</b> or another magnet <b>experiences a force</b>.", "\"the magnetism\""),
    ("Field line", "A line showing the <b>direction of the field</b> (the direction of the force on a N pole: <b>N to S</b>); closer lines mean a <b>stronger</b> field; lines never cross.", "\"the path of the magnet\""),
    ("Uniform field", "A field with the <b>same strength and direction everywhere</b>: parallel, equally spaced lines (between unlike poles; inside a solenoid).", "\"a straight field\""),
    ("Solenoid", "A <b>long coil of wire</b>; with a current it has a field like a bar magnet's, strong and uniform inside.", "\"an electromagnet\" (only with a core)"),
    ("Electromagnet", "A <b>solenoid with a soft iron core</b>: a magnet that can be <b>switched on and off</b> with the current.", "\"a magnet with wire\""),
    ("Right-hand grip rule", "Grip the wire with the right hand, <b>thumb along the current</b>: the <b>fingers curl the way the field goes</b>.", "mixing it up with the left-hand rule"),
    ("Motor effect", "A <b>current-carrying conductor in a magnetic field experiences a force</b>, due to the interaction between the two magnetic fields.", "\"a motor spins\""),
    ("Fleming's left-hand rule", "First finger <b>Field</b> (N → S), second finger <b>Current</b> (+ → −), thumb <b>Motion</b> (force), all at right angles.", "right hand; electron flow"),
    ("Magnetic flux density, B", "The <b>strength of a magnetic field</b>: the force per unit current per unit length on a wire at right angles to it; unit <b>tesla</b>, T (= N/A m).", "\"the amount of magnetism\""),
    ("Split-ring commutator", "The two half-rings on a d.c. motor's axle that <b>reverse the current in the coil every half turn</b>, so the coil keeps turning the same way.", "\"the thing that connects the wires\""),
]


def definitions_table():
    html = "<table class='tbl'><tr><th>Term</th><th>What to write (mark-scheme form)</th><th>Not this</th></tr>"
    for term, definition, wrong in DEFINITIONS:
        html += "<tr><td><b>" + term + "</b></td><td>" + definition + "</td><td>" + wrong + "</td></tr>"
    html += "</table>"
    return html


section_keywords = section(
    "keywords-magnetism", "nn", "Key words: state what is meant by…", "12.1–12.14P",
    equations=[r"\text{definition, word for word}"],
    blurb="One-mark definitions in the form of words the mark schemes credit. The bold words are the ones the marks are attached to. The last four terms (motor effect onwards) are Higher only, and the commutator is Physics only as well.",
    checklist=[
        "Define magnetic material, permanent and induced magnet",
        "Define magnetic field, field line, uniform field, solenoid and electromagnet",
        "Define the motor effect, magnetic flux density and the commutator",
    ],
    parts=[
        explain("The definitions", "<p>\"<b>State what is meant by</b>\" asks for the definition. Learn these as sentences.</p>" + definitions_table()),
        practice("Key words", [
            written("mg-kw-q1", "State what is meant by a magnetic field. (1)",
                    marks(["The <b>region around a magnet</b> (or current) in which a <b>magnetic material</b> (or another magnet) <b>experiences a force</b>."]), lines=1),
            written("mg-kw-q2", "State what is meant by an induced magnet. (1)",
                    marks(["A magnetic material that becomes a magnet <b>only while it is in a magnetic field</b> (and loses its magnetism when the field is removed)."]), lines=1),
            choice("mg-kw-q3", "Which is the best definition of a permanent magnet?",
                   ["A magnet that is very strong", "A magnet that produces its own magnetic field all the time", "A magnet made of iron", "A magnet that never moves"], 1,
                   "Its own field, always."),
            written("mg-kw-q4", "State what is meant by a uniform magnetic field, and where one is found. (2)",
                    marks(["A field with the <b>same strength and direction at every point</b> (parallel, equally spaced lines).", "Between two <b>unlike poles facing each other</b>, or inside a <b>solenoid</b>."]), lines=2),
            written("mg-kw-q5", "State what is meant by the motor effect. (1)",
                    marks(["A <b>current-carrying conductor in a magnetic field experiences a force</b> (due to the interaction of the two fields)."]), lines=1, tags=["H"]),
            choice("mg-kw-q6", "Magnetic flux density is measured in…",
                   ["newtons", "amperes", "tesla", "webers per second"], 2,
                   "Tesla, T (= N/A m).", tags=["H"]),
        ]),
    ],
)

FACTS_KW = [fact("State what is meant by: " + (term if term.split()[0].isupper() or term.startswith("Fleming") else term[0].lower() + term[1:]) + ".", definition, "keywords-magnetism") for term, definition, wrong in DEFINITIONS]

SECTIONS = [section_n1, section_n2, section_n3, section_n4, section_n5, section_n6, section_n7, section_n8, section_n9, section_keywords]
