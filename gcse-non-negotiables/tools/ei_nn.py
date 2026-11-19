"""
ei_nn.py — Topic 13 (Electromagnetic induction): the non-negotiables
N1–N10. Tiers from the Pearson spec: 13.1P, 13.2, 13.3P, 13.5, 13.6,
13.7P and 13.11P are Higher only; 13.4P, 13.8, 13.9 and 13.10 are both
tiers; the P statements are Physics only.

N1 Inducing a pd [H, P]          N6 The turns ratio [H, P]
N2 Size and direction [H]        N7 The national grid
N3 Alternator and dynamo [H, P]  N8 Power in a transformer
N4 Loudspeaker and microphone [P] N9 Why high voltage [H, P]
N5 The transformer [H]           N10 Key words
"""

from revlib import (
    choice, diagram, ewau, explain, fact, group, mark_scheme, marks, numeric,
    practice, section, worked, written,
)
import ei_diagrams as dg
from mg_nn import chain_list

# The author's standard chains, word for word from induction/src/build.mjs
# (EXAM.induction) and simple-motor/src/build.mjs (EXAM.speaker). Keep
# identical. INDUCTION_LEAD is the one line added, with the author's
# approval, for the case where the magnet moves and the coil stays still.
INDUCTION_LEAD = "The magnet moves relative to the coil (either may move)."
INDUCTION_CHAIN = [
    "The wire or coil moves through the magnetic field of the permanent magnet.",
    "So the wire or coil experiences a changing magnetic field.",
    "This induces a potential difference across the wire or coil.",
    "If the wire or coil is in a closed circuit, a current flows.",
]
SPEAKER_CHAIN = [
    "There is a current in the coil.",
    "This creates a magnetic field around the coil.",
    "This interacts with the permanent magnetic field.",
    "This causes a resultant force on the coil.",
    "The direction of the force is the same on either side of the coil.",
    "So the coil moves forwards or backwards. You can find the direction using Fleming's left-hand rule.",
    "With an alternating current, the force alternates back and forth at the same frequency as the current.",
]

# ---------------------------------------------------------------------
# N1 · Inducing a pd [H, P]
# ---------------------------------------------------------------------

section_n1 = section(
    "inducing-pd", "nn", "Inducing a pd: a conductor and a magnetic field moving relative to each other", "13.1P",
    equations=[r"\text{relative movement} \rightarrow \text{changing field} \rightarrow \text{pd induced} \rightarrow \text{current if closed}"],
    blurb="Move a wire or coil through a magnetic field, or move a magnet into a coil, and a potential difference is induced across the conductor; if the conductor is part of a closed circuit, a current flows. Nothing is induced while nothing moves. This is how every generator works, from a bicycle dynamo to a power station.",
    tags=["H", "P"],
    checklist=[
        "Write the induction chain for a wire or coil moving in a field, and for a magnet moving into a coil",
        "Describe how to show induction in the laboratory",
        "Describe how electricity is generated on a large scale",
    ],
    parts=[
        explain(
            "The chain to write every time",
            diagram(dg.induction_svg(), 660, 280, "A magnet pushed into a coil: the meter kicks one way going in, the other way coming out, and not at all while the magnet is still.") +
            "<p>A potential difference is <b>induced</b> across a conductor whenever it and a magnetic field <b>move relative to each other</b> — the wire moving through the field, or the magnet moving past the wire; what matters is that the conductor experiences a <b>changing magnetic field</b>. The standard explanation, in the steps the marks are on (the <a href='../induction/'>Electromagnetic Induction</a> page animates it):</p>"
            + chain_list(INDUCTION_CHAIN) +
            "<p>When it is the <b>magnet</b> that moves (dropped through a coil, pushed into one), put one line in front: <b>" + INDUCTION_LEAD + "</b> — and then steps 2 to 4 follow exactly as written. The June 2024 scheme (Q10(a)(i), a magnet falling through a coil) credited: the coil <b>cuts the field lines</b> / experiences a <b>changing field</b>; this <b>induces a pd</b> (or current) in the coil; the voltmeter reads it; and the induced pd <b>changes direction</b> as the magnet passes through (the far end of the magnet is the opposite pole, so the change is reversed).</p>"
            "<p>The word is <b>induces</b>. The June 2025 report (Q6(a)(i)): \"examiners would not accept 'produces' an alternating current. The correct word is 'induces'.\" A pd is induced; a current then flows <b>if the circuit is closed</b> — an open coil has an induced pd across it but no current.</p>"
            "<p><b>In the laboratory</b>: push a bar magnet into a coil connected to a centre-zero meter — the needle kicks; pull it out — it kicks the other way; hold it still inside — nothing. Or swing a straight wire between the poles of a magnet with a sensitive meter across its ends. <b>On a large scale</b>: a power-station generator turns a coil (or turns magnets past coils) continuously, driven by a turbine, so the coil experiences a continuously changing field and a pd is induced continuously — the same physics as the meter kick, just never stopping.</p>",
        ),
        worked(
            "The meter kick",
            "A student pushes a bar magnet into a coil connected to a centre-zero ammeter. The needle moves to the right and then returns to zero while the magnet is held still inside the coil. Explain these observations. (4 marks)",
            [
                INDUCTION_LEAD + " As the magnet moves into the coil, <b>the coil experiences a changing magnetic field</b> (it cuts the field lines).",
                "This <b>induces a potential difference</b> across the coil.",
                "The coil is in a <b>closed circuit</b> (through the ammeter), so a <b>current flows</b> and the needle moves.",
                "When the magnet is <b>held still</b> the field through the coil is <b>no longer changing</b>, so no pd is induced and the needle returns to zero.",
            ],
        ),
        practice("Inducing a pd", [
            written("ei-n1-q1", "A magnet is dropped through a coil connected to a voltmeter. Explain why the voltmeter shows a reading as the magnet passes through. (3)",
                    marks(["The magnet moves relative to the coil, so the coil <b>cuts the field lines</b> / experiences a <b>changing magnetic field</b>.", "This <b>induces a potential difference</b> across the coil…", "…which the voltmeter measures (the reading changes direction as the magnet passes through, because the trailing pole is the opposite pole)."]), lines=3),
            choice("ei-n1-q2", "A magnet is held stationary inside a coil connected to a meter. The meter reads…",
                   ["a steady value", "zero", "a value that slowly falls", "a.c."], 1,
                   "No relative movement, no changing field, nothing induced."),
            choice("ei-n1-q3", "Which word do the examiners require for what happens to the pd?",
                   ["produced", "made", "induced", "generated"], 2,
                   "2025 report: 'produces' was not accepted; the correct word is 'induces'."),
            written("ei-n1-q4", "Describe how to show in the laboratory that moving a magnet near a coil induces a potential difference. (3)",
                    marks(["Connect a coil to a <b>sensitive centre-zero meter</b> (voltmeter or galvanometer).", "<b>Push a magnet into the coil</b>: the needle kicks; pull it out: it kicks the <b>other way</b>.", "Hold the magnet <b>still</b> in the coil: the needle reads zero — only movement induces a pd."]), lines=3),
            written("ei-n1-q5", "State the difference between what happens in an open coil and a closed coil when a magnet is moved into each. (2)",
                    marks(["In both a <b>potential difference is induced</b> across the coil.", "Only in the <b>closed</b> circuit does a <b>current flow</b>; an open coil has the pd but no current."]), lines=2),
            choice("ei-n1-q6", "A power-station generator induces a pd continuously because…",
                   ["the coil is very large", "a turbine keeps the coil turning in the field, so the coil experiences a continuously changing field", "the magnets are electromagnets", "the wires are made of copper"], 1,
                   "Continuous relative movement, continuous change, continuous induction."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N2 · Size and direction [H]
# ---------------------------------------------------------------------

section_n2 = section(
    "induced-size-direction", "nn", "Size and direction of the induced pd — and the field that opposes the change", "13.2",
    equations=[r"\text{bigger: faster, stronger magnet, more turns}", r"\text{reversed: reverse the movement or the magnet}"],
    blurb="The induced pd is larger when the movement is faster, the magnet stronger or the coil has more turns; it reverses when the direction of movement reverses or the magnet is turned round. The induced current has its own magnetic field, and that field opposes the change that caused it — which is why a generator is harder to turn when it is supplying a current.",
    tags=["H"],
    checklist=[
        "List the factors that make the induced pd larger",
        "State what reverses the direction of the induced pd",
        "State that the induced current's field opposes the original change",
    ],
    parts=[
        explain(
            "Size, direction, and the field that opposes",
            "<table class='tbl'><tr><th>To induce a larger pd</th><th>Why</th></tr>"
            "<tr><td>move <b>faster</b> (turn the generator faster)</td><td>the field changes more quickly</td></tr>"
            "<tr><td>a <b>stronger magnet</b></td><td>more field lines to cut in the same time</td></tr>"
            "<tr><td><b>more turns</b> on the coil</td><td>each turn has a pd induced; they add</td></tr>"
            "<tr><td>(a larger coil area, an iron core)</td><td>more of the field passes through the coil</td></tr></table>"
            "<p><b>Direction</b>: the induced pd <b>reverses</b> if the <b>direction of movement</b> reverses (magnet in, then out) or if the <b>magnet is turned round</b> (N first instead of S first). Reverse both and it is unchanged.</p>"
            "<p><b>The field opposes the change</b> (13.2): when the induced current flows, it has its own magnetic field, and that field <b>opposes the change that caused it</b> — push a N pole into a coil and the coil's near end becomes a N pole, pushing back; pull it out and the near end becomes a S pole, pulling back. So <b>work has to be done</b> to keep moving the magnet (or turning the generator), and that work is where the electrical energy comes from. The June 2023 report (Q10(a)(ii), a dynamo lighting a lamp): the handle is harder to turn because the lamp needs energy, which comes from the extra work of turning; and \"an induced current in the rotating coil produces a magnetic field\" that opposes the motion — \"very few\" gave this (T2).</p>",
        ),
        worked(
            "Bigger reading",
            "A student moves a magnet into a coil and records the maximum reading on a voltmeter. State three changes that would give a larger maximum reading. (3 marks)",
            [
                "Move the magnet <b>faster</b> into the coil.",
                "Use a <b>stronger magnet</b>.",
                "Use a coil with <b>more turns</b> (or a larger coil / an iron core).",
            ],
        ),
        practice("Size and direction", [
            choice("ei-n2-q1", "Which change does NOT increase the induced pd?",
                   ["Moving the magnet faster", "Using a coil with more turns", "Using a stronger magnet", "Using thicker wire for the leads"], 3,
                   "Speed, strength and turns; the leads make no difference."),
            written("ei-n2-q2", "A magnet is pushed into a coil and the meter needle moves to the left. State two separate changes that would each make the needle move to the right instead. (2)",
                    marks(["<b>Pull the magnet out</b> (reverse the direction of movement).", "<b>Turn the magnet round</b> and push the other pole in."]), lines=2),
            written("ei-n2-q3", "Explain why a magnet being pushed into a coil connected in a closed circuit is harder to push than the same magnet pushed into an open coil. (3)",
                    marks(["In the closed circuit the induced pd drives a <b>current</b> in the coil.", "The current produces a <b>magnetic field</b> around the coil that <b>opposes the change</b> causing it — the near end of the coil becomes the same pole as the approaching pole, repelling it.", "So a larger force (more work) is needed to push the magnet in; in the open coil there is no current, so no opposing field."]), lines=4),
            choice("ei-n2-q4", "The induced current's magnetic field always…",
                   ["helps the magnet move", "opposes the change that caused it", "points north", "is zero"], 1,
                   "13.2: the induced current's field opposes the original change — energy has to come from the work done."),
            choice("ei-n2-q5", "A magnet is pushed in N pole first and the needle kicks right. It is then pulled out N pole first. The needle…",
                   ["kicks right again", "kicks left", "does not move", "stays right"], 1,
                   "Reversing the movement reverses the induced pd."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N3 · Alternator and dynamo [H, P]
# ---------------------------------------------------------------------

section_n3 = section(
    "alternator-dynamo", "nn", "Alternator and dynamo: slip rings give a.c., a split ring gives d.c.", "13.3P",
    equations=[r"\text{slip rings} \rightarrow \text{a.c.}", r"\text{split ring} \rightarrow \text{d.c.}"],
    blurb="Both turn a coil in a magnetic field, so a pd is induced that reverses every half turn. An alternator connects the coil to the circuit through two slip rings, so the circuit gets that alternating pd (a.c.). A dynamo uses a split-ring commutator, which swaps the connections every half turn, so the circuit always gets the same sign: a d.c. output that rises and falls but never reverses.",
    tags=["H", "P"],
    checklist=[
        "Explain why the pd induced in a turning coil alternates",
        "Describe the difference between slip rings and a split ring, and the output each gives",
        "Sketch the output of each against time",
    ],
    parts=[
        explain(
            "Same coil, different rings",
            diagram(dg.generator_svg(), 670, 260, "An alternator and a dynamo: the same coil turning between the same poles, with different rings.") +
            "<p>As the coil turns, each side moves <b>up</b> through the field for half a turn and <b>down</b> for the next half, so the pd induced across the coil <b>reverses every half turn</b> — and it is largest when the sides are cutting across the field fastest (coil flat), zero when they are moving along the field (coil vertical). The induced pd itself is therefore <b>alternating</b> whatever rings are used; the rings decide what the external circuit sees.</p>"
            "<table class='tbl'><tr><th></th><th>Alternator</th><th>Dynamo</th></tr>"
            "<tr><td>Connection</td><td>two <b>slip rings</b>: complete rings, one on each end of the coil, each pressed by its own brush</td><td>a <b>split-ring commutator</b>: one ring cut into two halves, one on each end of the coil, two brushes</td></tr>"
            "<tr><td>What it does</td><td>each brush stays connected to the <b>same end</b> of the coil all the time</td><td>the halves <b>swap brushes every half turn</b>, exactly when the induced pd reverses</td></tr>"
            "<tr><td>Output</td><td><b>a.c.</b>: reverses direction every half turn</td><td><b>d.c.</b>: always the same direction, but rising and falling (not steady)</td></tr>"
            "<tr><td>Graph</td><td>a sine wave through zero</td><td>the same wave with the negative halves flipped up (humps)</td></tr></table>"
            + diagram(dg.outputs_svg(), 720, 265, "The outputs: an alternator's a.c., a dynamo's d.c., and the a.c. when the coil is turned twice as fast.") +
            "<p>The split ring is the same part as in the d.c. motor (Topic 12 T7) doing the opposite job: in the motor it reverses the <b>supply</b> current into the coil every half turn; in the dynamo it reverses the <b>connection</b> so the induced pd always leaves the same way. The June 2023 report (Q8(a)(iii)) warned against describing \"split ring commutators without mentioning an electric current\" — the commutator is a detail; the point is that a current is induced and sent to the circuit.</p>",
        ),
        worked(
            "Why the dynamo gives d.c.",
            "Explain why the output of a dynamo is a direct current even though the pd induced in its coil alternates. (3 marks)",
            [
                "As the coil turns, each side moves up through the field for half a turn then down, so the pd induced in the coil <b>reverses every half turn</b>.",
                "The coil is connected through a <b>split-ring commutator</b>: the two halves of the ring <b>swap brushes every half turn</b>…",
                "…at the moment the induced pd reverses, so the external circuit is always connected the same way round and the current in it is always in the <b>same direction</b> (though it rises and falls).",
            ],
        ),
        practice("Alternator and dynamo", [
            choice("ei-n3-q1", "An alternator's coil is connected to the circuit through…",
                   ["a split ring", "two slip rings", "a diode", "a transformer"], 1,
                   "Slip rings: each brush stays on its own end of the coil, so the output alternates."),
            written("ei-n3-q2", "Explain why the pd induced in a coil turning in a magnetic field alternates. (2)",
                    marks(["Each side of the coil moves <b>up</b> through the field for half a turn and <b>down</b> for the next half.", "Reversing the direction of movement <b>reverses the induced pd</b>, so it reverses every half turn."]), lines=2),
            choice("ei-n3-q3", "The output of a dynamo is best described as…",
                   ["steady d.c.", "d.c. that rises and falls but never reverses", "a.c.", "zero"], 1,
                   "Humps above the axis: one direction, not constant."),
            written("ei-n3-q4", "A generator's coil is turned twice as fast. State two changes to its output. (2)",
                    marks(["The <b>peak pd is larger</b> (the field changes more quickly).", "The <b>frequency is doubled</b> (two cycles in the time of one)."]), lines=2),
            choice("ei-n3-q5", "In a dynamo, the split ring swaps the connections…",
                   ["every quarter turn", "every half turn, when the induced pd reverses", "once per second", "only when the coil is vertical and the pd is largest"], 1,
                   "Every half turn — at the vertical position, where the induced pd is zero and about to reverse."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N4 · Loudspeaker and microphone [P]
# ---------------------------------------------------------------------

section_n4 = section(
    "speaker-microphone", "nn", "Loudspeaker and microphone: the motor effect one way, induction the other", "13.4P",
    equations=[r"\text{speaker: current} \rightarrow \text{force} \rightarrow \text{movement} \rightarrow \text{sound}", r"\text{microphone: sound} \rightarrow \text{movement} \rightarrow \text{changing field} \rightarrow \text{pd induced}"],
    blurb="A loudspeaker is a coil on a cone in the field of a permanent magnet: an alternating current gives an alternating force, the cone moves in and out at the same frequency and makes sound. A microphone is the same parts run backwards: sound moves a diaphragm with a coil on it through the field, the coil experiences a changing field, and an alternating pd is induced that copies the sound.",
    tags=["P"],
    checklist=[
        "Write the seven-step chain for the loudspeaker",
        "Write the induction chain for the microphone",
        "State what the two devices have in common and what is reversed",
    ],
    parts=[
        explain(
            "The two chains",
            diagram(dg.speaker_mic_svg(), 690, 275, "A moving-coil loudspeaker and a moving-coil microphone: the same magnet, coil and cone or diaphragm, working in opposite directions.") +
            "<p><b>The loudspeaker</b> — the standard explanation, in the steps the marks are on (the <a href='../simple-motor/'>Simple Motor and Loudspeaker</a> page animates it):</p>"
            + chain_list(SPEAKER_CHAIN) +
            "<p>The coil is fixed to a <b>cone</b> (or diaphragm), so the cone moves with it, pushing the air in and out and making a <b>sound wave of the same frequency</b> as the current; a larger current gives a larger force, a larger movement and a louder sound. The <b>same force on both sides</b> of the coil is what makes it a loudspeaker and not a motor: the coil sits in a <b>radial</b> field (a centre pole inside the coil, a ring pole outside), so every part of the coil is pushed the same way — along the axis.</p>"
            "<p><b>The microphone</b> is the reverse, and the chain is the induction chain: the <b>sound wave</b> (pressure variations in the air) makes the <b>diaphragm vibrate</b>; the <b>coil attached to it moves</b> back and forth through the magnetic field of the permanent magnet; so the coil <b>experiences a changing magnetic field</b>; this <b>induces a pd</b> across the coil; in a closed circuit a current flows — an <b>alternating</b> current with the <b>same frequency</b> as the sound, and larger for a louder sound. The June 2023 6-marker (Q10(c), compare the two) reached Level 3 only with the <b>interaction of the coil's field and the magnet's field</b> for the speaker <b>and</b> \"electromagnetic induction as a result of a coil moving in a magnetic field\" for the microphone (the microphone-versus-loudspeaker section).</p>",
        ),
        worked(
            "The microphone in four marks",
            "Explain how a moving-coil microphone converts sound into an electrical signal. (4 marks)",
            [
                "The <b>sound wave</b> (pressure variations in the air) makes the <b>diaphragm vibrate</b>, and the coil fixed to it <b>moves with it</b>.",
                "The coil <b>moves through the magnetic field</b> of the permanent magnet, so it <b>experiences a changing magnetic field</b>.",
                "This <b>induces a potential difference</b> across the coil; in a closed circuit, a current flows.",
                "The movement is back and forth, so the induced pd is <b>alternating</b>, with the <b>same frequency</b> as the sound (and larger for a louder sound).",
            ],
        ),
        practice("Loudspeaker and microphone", [
            written("ei-n4-q1", "Explain how a loudspeaker produces sound from an alternating current. (4)",
                    marks(["There is a <b>current in the coil</b>, which <b>creates a magnetic field</b> around the coil; this <b>interacts with the permanent magnetic field</b>.", "This causes a <b>resultant force on the coil</b>, the same on either side, so the coil (and the cone fixed to it) <b>moves forwards or backwards</b>.", "With an <b>alternating current the force alternates</b> back and forth at the same frequency as the current.", "So the cone vibrates and produces a <b>sound wave of that frequency</b>."]), lines=5),
            choice("ei-n4-q2", "Which physics does a microphone use?",
                   ["The motor effect", "Electromagnetic induction", "Static electricity", "Refraction"], 1,
                   "Coil moved by sound in a field: a pd is induced."),
            choice("ei-n4-q3", "A louder sound reaches a microphone. The induced pd…",
                   ["has a higher frequency", "is larger", "is d.c.", "is unchanged"], 1,
                   "Louder: the diaphragm moves further and faster, so a larger pd; pitch sets the frequency."),
            written("ei-n4-q4", "State one similarity and one difference between a moving-coil loudspeaker and a moving-coil microphone. (2)",
                    marks(["Similarity: both have a <b>coil in the field of a permanent magnet</b>, attached to a cone/diaphragm.", "Difference: in the speaker a <b>current causes movement</b> (motor effect); in the microphone <b>movement induces a pd</b> (electromagnetic induction)."]), lines=2),
            choice("ei-n4-q5", "Why does the loudspeaker's coil move along its axis rather than rotate like a motor coil?",
                   ["It carries d.c.", "The force is the same on every part of the coil (radial field), not opposite on the two sides", "It has no commutator", "The cone is heavy"], 1,
                   "Same direction of force all round the coil: it moves forwards or backwards."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N5 · The transformer [H]
# ---------------------------------------------------------------------

section_n5 = section(
    "transformer", "nn", "The transformer: a.c. in the primary induces a.c. in the secondary", "13.5, 13.6",
    equations=[r"\text{a.c. in primary} \rightarrow \text{changing field in core} \rightarrow \text{pd induced in secondary}"],
    blurb="Two coils on one soft-iron core. An alternating current in the primary coil produces a changing magnetic field in the core; the secondary coil is in that changing field, so an alternating pd is induced across it. A transformer changes the size of an alternating pd — more turns on the secondary steps it up, fewer steps it down — and does nothing with steady d.c., because a steady current gives a steady field and no induction.",
    tags=["H"],
    checklist=[
        "Explain how an alternating current in one circuit induces a current in another",
        "State what a transformer can and cannot do (a.c. only; changes the size of the pd)",
        "Say which coil has more turns in a step-up and in a step-down transformer",
    ],
    parts=[
        explain(
            "The three marks",
            diagram(dg.transformer_svg(), 660, 280, "A transformer: primary and secondary coils on a soft-iron core, which carries the changing field from one to the other.") +
            "<p>The June 2025 scheme (Q6(a)(i), 3 marks): (1) there is an <b>alternating current in the primary coil</b>; (2) this produces a <b>changing magnetic field in the iron core</b>; (3) the secondary coil is in that changing field, so an <b>alternating pd is induced</b> across it. \"Marks were usually lost by not stating the magnetic field in the core was <b>changing</b>\" — and by writing <b>produces</b> instead of <b>induces</b>. The core is <b>soft iron</b>: it is easily magnetised and demagnetised, so it carries the changing field efficiently from one coil to the other without keeping any.</p>"
            "<p><b>Why a.c. only</b>: a steady d.c. in the primary gives a steady field in the core, and a steady field induces <b>nothing</b> in the secondary (no change, no induction). Only at the instants of switching on and off is there a brief induced pd.</p>"
            "<p><b>What it does</b> (13.6): changes the <b>size of an alternating pd</b>. A <b>step-up</b> transformer has <b>more turns on the secondary</b> than the primary and gives a larger pd out; a <b>step-down</b> has <b>fewer</b> turns on the secondary and gives a smaller pd out. The pd changes in the same ratio as the turns (N6), and because the power is (nearly) the same on both sides, the <b>current changes the other way</b> (N8): step up the pd and the current goes down.</p>",
        ),
        worked(
            "The 2025 three-marker",
            "A phone charger contains a transformer. Explain how an alternating current in the primary coil causes an alternating pd across the secondary coil. (3 marks)",
            [
                "The <b>alternating current in the primary coil</b> produces a magnetic field in the iron core that is <b>changing</b> (continuously reversing).",
                "The core carries this changing field through the <b>secondary coil</b>, so the secondary coil experiences a <b>changing magnetic field</b>.",
                "This <b>induces an alternating pd</b> across the secondary coil (and, with the charger connected, an alternating current flows).",
            ],
        ),
        practice("The transformer", [
            written("ei-n5-q1", "Explain why a transformer does not work with a steady direct current in its primary coil. (2)",
                    marks(["A steady current produces a <b>steady (unchanging) magnetic field</b> in the core.", "A pd is only induced by a <b>changing</b> field, so nothing is induced in the secondary coil."]), lines=2),
            choice("ei-n5-q2", "The mark most often lost on 'how a transformer works' (2025) was for not saying…",
                   ["the core is made of iron", "the magnetic field in the core is changing", "the coils are made of copper", "the transformer is efficient"], 1,
                   "'Changing' is the word; a steady field induces nothing."),
            choice("ei-n5-q3", "A step-up transformer has…",
                   ["more turns on the primary than the secondary", "more turns on the secondary than the primary", "equal turns", "no core"], 1,
                   "More secondary turns: larger pd out."),
            written("ei-n5-q4", "State what a transformer does, and give one reason the core is made of soft iron. (2)",
                    marks(["It <b>changes the size of an alternating pd</b> (steps it up or down).", "Soft iron is <b>easily magnetised and demagnetised</b>, so it carries the changing field from the primary to the secondary (without staying magnetised)."]), lines=2),
            choice("ei-n5-q5", "Which word is wrong in: 'the changing field in the core produces an alternating pd in the secondary'?",
                   ["changing", "core", "produces", "alternating"], 2,
                   "The pd is induced. 2025: 'produces' was not accepted."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N6 · The turns ratio [H, P]
# ---------------------------------------------------------------------

section_n6 = section(
    "turns-ratio", "nn", "The turns ratio: pd in proportion to turns", "13.7P",
    equations=[r"\dfrac{V_p}{V_s} = \dfrac{N_p}{N_s}"],
    blurb="The pd across each coil is in proportion to its number of turns: primary over secondary on both sides. The equation is on the list; the marks are for keeping primary with primary, rearranging, and checking the answer makes sense (step-down means a smaller pd out).",
    tags=["H", "P"],
    checklist=[
        "Use the turns-ratio equation to find a missing pd or number of turns",
        "Keep primary quantities together on one side of the fraction",
        "Check the direction: step-up gives more pd out, step-down less",
    ],
    parts=[
        explain(
            "Using it",
            "<p>$\\dfrac{V_p}{V_s} = \\dfrac{N_p}{N_s}$: pd across the primary over pd across the secondary equals turns on the primary over turns on the secondary. Both fractions are <b>primary on top</b>. It is quicker as a ratio: the pd changes by the <b>same factor</b> as the turns — ten times the turns, ten times the pd. The June 2024 6-marker (Q10(b)) wanted the ratio idea for a 11 000 V → 230 V step-down: $11\\,000 : 230 \\approx 48 : 1$, so the primary needs about 48 times as many turns as the secondary. The June 2025 report (Q6(a)(ii)): \"many examples of confident substitution into and rearrangement of the appropriate transformer equation\"; a few used the pd–current equation by mistake (that one needs currents — N8).</p>"
            "<p>Check every answer against the direction: a <b>step-down</b> (fewer secondary turns) must give a <b>smaller</b> secondary pd. If your answer comes out bigger, the fraction is upside down.</p>",
        ),
        worked(
            "A missing number of turns",
            "A transformer steps 230 V down to 12 V for a doorbell. The primary coil has 4600 turns. Calculate the number of turns on the secondary coil. (3 marks)",
            [
                "$\\dfrac{V_p}{V_s} = \\dfrac{N_p}{N_s}$, so $N_s = N_p \\times \\dfrac{V_s}{V_p}$.",
                "$N_s = 4600 \\times \\dfrac{12}{230}$.",
                "$N_s = 240$ turns — fewer than the primary, as a step-down must have.",
            ],
        ),
        practice("The turns ratio", [
            numeric("ei-n6-q1", "A transformer has 500 turns on the primary and 2500 turns on the secondary. The primary pd is 24 V. Calculate the secondary pd.", 120, "V",
                    "Five times the turns, five times the pd.",
                    ewau(r"V_s = V_p \times N_s \div N_p", r"V_s = 24 \times 2500 \div 500", "120", "V")),
            numeric("ei-n6-q2", "The 230 V mains is stepped down to 5.0 V for a charger. The secondary coil has 50 turns. Calculate the number of turns on the primary.", 2300, "turns",
                    "$N_p = N_s \\times V_p \\div V_s$.",
                    ewau(r"N_p = N_s \times V_p \div V_s", r"N_p = 50 \times 230 \div 5.0", "2300", "turns")),
            numeric("ei-n6-q3", "A step-up transformer with 400 primary turns and 6400 secondary turns has a primary pd of 25 kV. Calculate the secondary pd in kV.", 400, "kV",
                    "Ratio 16: multiply the pd by 16.",
                    ewau(r"V_s = V_p \times N_s \div N_p", r"V_s = 25 \times 6400 \div 400", "400", "kV")),
            choice("ei-n6-q4", "A student's answer gives a secondary pd of 920 V for a transformer stepping down from 230 V. What has gone wrong?",
                   ["Nothing", "The fraction is upside down — a step-down must give a smaller pd", "The units are wrong", "The transformer is broken"], 1,
                   "Check the direction every time."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N7 · The national grid
# ---------------------------------------------------------------------

section_n7 = section(
    "national-grid", "nn", "The national grid: step up to transmit, step down to use", "13.8, 13.9",
    equations=[r"\text{high pd} \rightarrow \text{low current} \rightarrow \text{less heating of the cables}"],
    blurb="Power stations generate at about 25 kV; step-up transformers raise this to as much as 400 kV for the transmission cables; step-down transformers near towns bring it down in stages to 230 V for homes. Transmitting at a high pd means a small current, and a small current wastes much less energy heating the cables, so the transfer is more efficient.",
    checklist=[
        "Describe where step-up and step-down transformers are used in the grid",
        "Explain why electricity is transmitted at a high pd",
        "State why it is stepped down again near homes",
    ],
    parts=[
        explain(
            "Where and why",
            diagram(dg.grid_svg(), 720, 265, "The national grid: a step-up transformer at the power station, long cables at a very high pd, and step-down transformers near the homes.") +
            "<p><b>Where</b> (13.9): a <b>step-up</b> transformer <b>at the power station</b> raises the pd from the generator's ~25 kV to 132 kV, 275 kV or 400 kV for the <b>transmission lines</b>; <b>step-down</b> transformers at substations <b>near the towns and homes</b> reduce it in stages to 230 V for domestic use.</p>"
            "<p><b>Why</b> (13.8), as a chain: for a given power, a <b>higher pd means a smaller current</b> (power = pd × current); the cables waste energy by <b>heating</b>, and the heating rises steeply with the current; so a <b>smaller current wastes much less energy</b> in the cables; so transmitting at a high pd is <b>more efficient</b> — more of the power generated reaches the user. It is stepped down again because 400 kV would be far too <b>dangerous</b> for homes and would break down insulation; 230 V is what appliances are designed for. The marks are on <b>reducing the current</b> and <b>reducing the energy wasted as heat in the cables</b> — \"it is more efficient\" alone is a conclusion, not a reason.</p>",
        ),
        worked(
            "The 3-mark why",
            "Explain why electrical energy is transmitted through the national grid at a very high potential difference. (3 marks)",
            [
                "For the same power, a higher pd means a <b>smaller current</b> in the cables.",
                "A smaller current means <b>less energy is wasted as heat</b> in the cables (heating rises steeply with current).",
                "So the transmission is <b>more efficient</b>: more of the energy generated reaches the users.",
            ],
        ),
        practice("The national grid", [
            choice("ei-n7-q1", "A step-up transformer is used…",
                   ["at the power station, before the transmission cables", "at the house", "in the middle of the cables", "nowhere in the grid"], 0,
                   "Step up at the station, step down near the user."),
            written("ei-n7-q2", "Explain why step-down transformers are needed before electricity reaches homes. (2)",
                    marks(["The transmission pd (up to 400 kV) is far too <b>high to be safe</b> in homes and for appliances.", "Step-down transformers reduce it to <b>230 V</b>, which appliances are designed for."]), lines=2),
            choice("ei-n7-q3", "Transmitting at a higher pd reduces energy losses because…",
                   ["the cables are shorter", "the current is smaller, so less energy is wasted heating the cables", "the electrons move faster", "transformers store energy"], 1,
                   "Higher pd → smaller current → less heating."),
            written("ei-n7-q4", "A student writes: 'Electricity is sent at high voltage because it is more efficient.' Explain why this would not get full marks and add what is missing. (2)",
                    marks(["'More efficient' is the <b>conclusion</b>; the reason is missing.", "Add: a high pd means a <b>small current</b>, and a small current means <b>less energy wasted as heat</b> in the cables."]), lines=2),
            choice("ei-n7-q5", "Roughly what pd do the main transmission lines of the grid operate at?",
                   ["230 V", "25 kV", "400 kV", "4 V"], 2,
                   "Up to 400 kV on the main lines; 25 kV at the generator; 230 V at home."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N8 · Power in a transformer
# ---------------------------------------------------------------------

section_n8 = section(
    "transformer-power", "nn", "Power in and out of a transformer: the pd–current equation", "13.10",
    equations=[r"V_p\,I_p = V_s\,I_s"],
    blurb="For a transformer that is 100 % efficient, the power delivered to the primary equals the power taken from the secondary: pd × current on one side equals pd × current on the other. Step the pd up and the current comes down in the same ratio. The equation is on the list; the marks are for choosing it (not the turns equation), converting mA, and rearranging.",
    checklist=[
        "Use $V_p I_p = V_s I_s$ to find a missing pd or current",
        "Explain why stepping the pd up steps the current down",
        "State the assumption (100 % efficiency) the equation relies on",
    ],
    parts=[
        explain(
            "Using it",
            "<p>Power = pd × current (Topic 10). If none is wasted, the power into the primary equals the power out of the secondary: $V_p I_p = V_s I_s$ — the spec words it \"for transformers with 100% efficiency\". So a transformer that <b>steps the pd up by a factor</b> steps the <b>current down by the same factor</b>; it cannot give more power out than in. Choose this equation when the question gives or asks for a <b>current</b>; choose the turns equation (the turns-ratio section, Higher) when it gives or asks for <b>turns</b>. The two can be chained: turns give the secondary pd, then this gives the secondary current (\"Transformer calculations the hard way\", Higher).</p>"
            "<p>Units: convert <b>mA to A</b> and <b>kV to V</b> before substituting, or keep both sides in the same units consistently. Real transformers are a little less than 100 % efficient (the core and coils warm up), so the real secondary power is slightly lower than the equation gives.</p>",
        ),
        worked(
            "Current in the secondary",
            "A transformer steps the 230 V mains down to 11.5 V. The current in the primary coil is 0.20 A. Assuming the transformer is 100 % efficient, calculate the current in the secondary coil. (3 marks)",
            [
                "$V_p I_p = V_s I_s$, so $I_s = V_p I_p \\div V_s$.",
                "$I_s = 230 \\times 0.20 \\div 11.5$.",
                "$I_s = 4.0$ A — twenty times the primary current, because the pd is stepped down by twenty.",
            ],
        ),
        practice("Power in a transformer", [
            numeric("ei-n8-q1", "A 100 % efficient transformer has a primary pd of 230 V and a primary current of 50 mA. The secondary pd is 5.0 V. Calculate the secondary current.", 2.3, "A",
                    "50 mA = 0.050 A; $I_s = V_p I_p \\div V_s$.",
                    [r"$I_p = 50$ mA $= 0.050$ A"] + ewau(r"I_s = V_p I_p \div V_s", r"I_s = 230 \times 0.050 \div 5.0", "2.3", "A")),
            numeric("ei-n8-q2", "A step-up transformer at a power station has an input of 25 kV at 8000 A. The output pd is 400 kV. Calculate the output current, assuming 100 % efficiency.", 500, "A",
                    "Keep both pds in kV; the ratio is what matters.",
                    ewau(r"I_s = V_p I_p \div V_s", r"I_s = 25 \times 8000 \div 400", "500", "A")),
            numeric("ei-n8-q3", "The secondary coil of a transformer supplies 12 V at 2.5 A. Calculate the primary current when the primary pd is 230 V, assuming 100 % efficiency. Give your answer in mA.", 130, "mA",
                    "Find $I_p$ in A, then × 1000; two significant figures.",
                    ewau(r"I_p = V_s I_s \div V_p", r"I_p = 12 \times 2.5 \div 230 = 0.1304 \text{ A}", "130", "mA (2 s.f.)")),
            choice("ei-n8-q4", "A transformer steps the pd up by a factor of 10. If it is 100 % efficient, the current…",
                   ["goes up by 10", "goes down by 10", "stays the same", "goes up by 100"], 1,
                   "Same power: pd × 10 means current ÷ 10."),
            numeric("ei-n8-q5", "A charger's transformer takes 230 V at 40 mA and delivers 9.2 V. Calculate the output current, assuming 100 % efficiency.", 1.0, "A",
                    "40 mA = 0.040 A.",
                    [r"$I_p = 40$ mA $= 0.040$ A"] + ewau(r"I_s = V_p I_p \div V_s", r"I_s = 230 \times 0.040 \div 9.2", "1.0", "A")),
            numeric("ei-n8-q6", "A transformer supplies a 48 W lamp at 12 V from the 230 V mains. Calculate the current in the primary coil, assuming 100 % efficiency. Give your answer to 2 significant figures.", 0.21, "A",
                    "Power in = power out = 48 W, so $I_p = P \\div V_p$.",
                    ewau(r"I_p = P \div V_p", r"I_p = 48 \div 230 = 0.2087", "0.21", "A (2 s.f.)")),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N9 · Why high voltage, with the equations [H, P]
# ---------------------------------------------------------------------

section_n9 = section(
    "transmission-loss", "nn", "Why high voltage, with the power equations", "13.11P",
    equations=[r"P = I\,V", r"P = I^2 R"],
    blurb="The national-grid argument made quantitative: for a fixed power, P = IV says a higher pd means a smaller current; P = I²R says the power wasted heating the cables falls with the square of the current — ten times the pd, a tenth of the current, a hundredth of the loss. The marks are for using both equations, in that order.",
    tags=["H", "P"],
    checklist=[
        "Use $P = IV$ to show that a higher transmission pd means a smaller current",
        "Use $P = I^2R$ to show the loss in the cables falls with the current squared",
        "Calculate the power wasted in a cable of given resistance",
    ],
    parts=[
        explain(
            "The argument with numbers",
            "<p>Take 100 MW to be transmitted along cables of total resistance 5 Ω. At 25 kV the current is $I = \\dfrac{P}{V} = \\dfrac{100\\,000\\,000}{25\\,000} = 4000$ A and the loss is $I^2 R = 4000^2 \\times 5 = 80$ MW — most of the power. At 400 kV the current is $250$ A and the loss is $250^2 \\times 5 = 0.31$ MW. Sixteen times the pd, a sixteenth of the current, a <b>256th</b> of the loss. That is 13.11P: the advantage of high-voltage transmission, <b>using the equations</b> — $P = IV$ for the current, then $P = I^2R$ for the loss. The transformer equations (N6, N8) supply the pd and current on each side.</p>"
            "<p>Write the chain with the equations named: (1) $P = IV$: for the same power, a higher $V$ means a smaller $I$; (2) $P = I^2R$: the power wasted in the cables is proportional to $I^2$, so a smaller current wastes <b>much</b> less; (3) so the transmission is more efficient. The common slip is to put the <b>transmission pd</b> into $P = IV$ to find the loss — that gives the power carried, not the power wasted; the loss needs the <b>current and the cable's resistance</b>.</p>",
        ),
        worked(
            "Loss at two pds",
            "A power station delivers 50 MW through cables of total resistance 4.0 Ω. Calculate the power wasted in the cables (a) at 50 kV and (b) at 250 kV. (4 marks)",
            [
                "(a) $I = \\dfrac{P}{V} = \\dfrac{50 \\times 10^6}{50 \\times 10^3} = 1000$ A.",
                "Loss $= I^2 R = 1000^2 \\times 4.0 = 4.0 \\times 10^6$ W $= 4.0$ MW.",
                "(b) $I = \\dfrac{50 \\times 10^6}{250 \\times 10^3} = 200$ A.",
                "Loss $= 200^2 \\times 4.0 = 160\\,000$ W $= 0.16$ MW — five times the pd, a fifth of the current, a twenty-fifth of the loss.",
            ],
        ),
        practice("Transmission loss", [
            numeric("ei-n9-q1", "A cable of resistance 2.0 Ω carries 300 A. Calculate the power wasted as heat in the cable.", 180000, "W",
                    "$P = I^2 R$ — square the current first.",
                    ewau(r"P = I^2 R", r"P = 300^2 \times 2.0", "180\\,000", "W")),
            numeric("ei-n9-q2", "20 MW is transmitted at 100 kV. Calculate the current in the cables.", 200, "A",
                    "$I = P \\div V$, both in base units (or MW ÷ kV × 1000).",
                    ewau(r"I = P \div V", r"I = \dfrac{20 \times 10^6}{100 \times 10^3}", "200", "A")),
            numeric("ei-n9-q3", "The same 20 MW is instead transmitted at 400 kV through cables of resistance 10 Ω. Calculate the power wasted in the cables, in kW.", 25, "kW",
                    "Current first ($P = IV$), then loss ($P = I^2R$), then ÷ 1000.",
                    [r"$I = \dfrac{20 \times 10^6}{400 \times 10^3} = 50$ A"] + ewau(r"P = I^2 R", r"P = 50^2 \times 10 = 25\,000 \text{ W}", "25", "kW")),
            written("ei-n9-q4", "Using equations, explain why transmitting at a higher pd reduces the energy wasted in the cables. (3)",
                    marks(["$P = IV$: for the same power transmitted, a <b>higher pd means a smaller current</b>.", "$P = I^2R$: the power wasted heating the cables is proportional to the <b>square of the current</b>…", "…so a smaller current wastes <b>much less</b> power (halve the current, quarter the loss), making the transmission more efficient."]), lines=3),
            choice("ei-n9-q5", "A student finds the cable loss by putting the transmission pd into P = IV. What is wrong?",
                   ["Nothing", "That gives the power carried by the cables, not the power wasted — the loss needs I²R with the cable's resistance", "P = IV is not on the equation list", "The current should be squared in P = IV"], 1,
                   "Loss = I²R (or I × the pd dropped across the cable, which is not the transmission pd)."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N10 · Key words
# ---------------------------------------------------------------------

DEFINITIONS = [
    ("Electromagnetic induction", "A <b>potential difference is induced</b> across a conductor when it experiences a <b>changing magnetic field</b> (relative movement of the conductor and a magnet, or a changing current nearby).", "\"a current is made\""),
    ("Induced pd", "The pd across a conductor <b>caused by a changing magnetic field</b>; a current flows only if the circuit is closed.", "\"produced\" pd"),
    ("Generator", "A device that <b>induces a pd by turning a coil in a magnetic field</b> (or magnets past a coil), driven by a turbine, engine or hand.", "\"makes electricity from nothing\""),
    ("Alternator", "A generator with <b>slip rings</b>, whose output is <b>a.c.</b>", "confusing with dynamo"),
    ("Dynamo", "A generator with a <b>split-ring commutator</b>, whose output is <b>d.c.</b> (one direction, rising and falling).", "\"steady d.c.\""),
    ("Slip rings", "Two <b>complete rings</b>, one on each end of the coil, each with its own brush, so the output alternates.", "\"split rings\""),
    ("Split-ring commutator", "One ring cut in two, the halves joined to the ends of the coil, <b>swapping brushes every half turn</b>: in a dynamo it makes the output d.c.; in a motor it reverses the current in the coil.", "\"the slip ring\""),
    ("Transformer", "A device of two coils on a soft-iron core which <b>changes the size of an alternating pd</b>: a.c. in the primary induces a.c. in the secondary.", "\"changes a.c. to d.c.\""),
    ("Primary / secondary coil", "The <b>primary</b> is connected to the supply; the pd is <b>induced in the secondary</b>, which is connected to the load.", "swapping them in the ratio"),
    ("Step-up / step-down transformer", "Step-up: <b>more turns on the secondary</b>, larger pd out, smaller current. Step-down: <b>fewer</b> turns on the secondary, smaller pd out, larger current.", "\"step-up increases the power\""),
    ("Turns ratio", "$V_p / V_s = N_p / N_s$: the pds are in the <b>same ratio as the numbers of turns</b>.", "primary and secondary mixed"),
    ("National grid", "The network of <b>cables and transformers</b> that carries electrical power from power stations to users, at a very high pd to reduce losses.", "\"the power station\""),
]


def definitions_table():
    html = "<table class='tbl'><tr><th>Term</th><th>What to write (mark-scheme form)</th><th>Not this</th></tr>"
    for term, definition, wrong in DEFINITIONS:
        html += "<tr><td><b>" + term + "</b></td><td>" + definition + "</td><td>" + wrong + "</td></tr>"
    html += "</table>"
    return html


section_keywords = section(
    "keywords-induction", "nn", "Key words: state what is meant by…", "13.1P–13.11P",
    equations=[r"\text{definition, word for word}"],
    blurb="One-mark definitions in the form of words the mark schemes credit. The generator, alternator, dynamo, slip-ring and transformer terms are Higher only (and the alternator/dynamo ones Physics only); the national grid is both tiers.",
    checklist=[
        "Define electromagnetic induction and induced pd",
        "Define generator, alternator, dynamo, slip rings and the split ring",
        "Define transformer, primary and secondary, step-up and step-down, turns ratio, national grid",
    ],
    parts=[
        explain("The definitions", "<p>\"<b>State what is meant by</b>\" asks for the definition. Learn these as sentences.</p>" + definitions_table()),
        practice("Key words", [
            written("ei-kw-q1", "State what is meant by electromagnetic induction. (1)",
                    marks(["A <b>potential difference is induced</b> across a conductor when it experiences a <b>changing magnetic field</b> (e.g. by moving relative to a magnet)."]), lines=1, tags=["H"]),
            choice("ei-kw-q2", "Which device has slip rings and an a.c. output?",
                   ["Dynamo", "Alternator", "Transformer", "Motor"], 1,
                   "Slip rings: alternator, a.c. Split ring: dynamo, d.c.", tags=["H"]),
            written("ei-kw-q3", "State what a transformer does. (1)",
                    marks(["It <b>changes the size of an alternating pd</b> (steps it up or down)."]), lines=1, tags=["H"]),
            choice("ei-kw-q4", "In a step-down transformer…",
                   ["the secondary has fewer turns and a smaller pd than the primary", "the secondary has more turns than the primary", "the pd is unchanged", "d.c. is produced"], 0,
                   "Fewer secondary turns: smaller pd out (and larger current).", tags=["H"]),
            written("ei-kw-q5", "State what is meant by the national grid. (1)",
                    marks(["The network of <b>cables and transformers</b> connecting power stations to users across the country."]), lines=1),
        ]),
    ],
)

FACTS_KW = [fact("State what is meant by: " + term[0].lower() + term[1:] + ".", definition, "keywords-induction") for term, definition, wrong in DEFINITIONS]

SECTIONS = [section_n1, section_n2, section_n3, section_n4, section_n5, section_n6, section_n7, section_n8, section_n9, section_keywords]
