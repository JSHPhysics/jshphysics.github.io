"""
ei_tricky.py — Topic 13 (Electromagnetic induction): the tricky bits
T1–T8 and the flashcards.

T1 The induction chain in the exam [H]      T5 The transformer 6-marker [H]
T2 Why the dynamo gets harder to turn [H]   T6 Transformer calculations the hard way [H, P]
T3 Generator output graphs [H, P]           T7 The national grid as a chain
T4 Microphone versus loudspeaker [P]        T8 Investigating induction [H]
"""

from revlib import (
    choice, diagram, ewau, explain, fact, group, mark_scheme, marks, numeric,
    practice, section, worked, written,
)
import ei_diagrams as dg
from mg_nn import chain_list
from ei_nn import INDUCTION_CHAIN, INDUCTION_LEAD, SPEAKER_CHAIN

# ---------------------------------------------------------------------
# T1 · The induction chain in the exam [H]
# ---------------------------------------------------------------------

section_t1 = section(
    "induction-chain-exam", "tricky", "The induction chain in the exam: the falling magnet, and \"induces\"", "13.1P, 13.2",
    equations=[r"\text{relative movement} \rightarrow \text{changing field} \rightarrow \text{pd induced} \rightarrow \text{current if closed}"],
    blurb="The exam's favourite induction question drops a magnet through a coil or waves one near it and asks why the meter reads. The marks are on the chain — changing field, induced pd, current if the circuit is closed — plus one detail students miss: the reading reverses as the magnet passes through. And the word is induces.",
    tags=["H", "P"],
    checklist=[
        "Write the chain for a magnet moving past a coil, with the lead line",
        "Explain why the reading reverses as a magnet passes through a coil",
        "Use 'induces' and never 'produces' for the pd",
    ],
    parts=[
        explain(
            "The 2024 falling magnet",
            "<p>The June 2024 scheme (Q10(a)(i), 3 marks, any three): the coil <b>cuts the field lines</b> (or experiences a <b>changing field</b>); this <b>induces a voltage or current</b> in the coil; the <b>voltmeter measures</b> the induced pd (the scheme lets that statement count for two of the three); <b>electrons in the wire experience a force</b> / move in response to the changing field; the induced pd <b>changes in size and direction</b> as the magnet passes through. The chain, with the lead line for a moving magnet:</p>"
            "<ol class='steps'><li>" + INDUCTION_LEAD + "</li>" + "".join("<li>" + step + "</li>" for step in INDUCTION_CHAIN[1:]) + "</ol>"
            "<p><b>Why the reading reverses</b>: as the magnet's leading pole enters, the field through the coil <b>increases</b>; as its trailing pole (the opposite pole) leaves, the field through the coil <b>decreases</b> — the change is the opposite way, so the induced pd is the opposite way. A magnet dropped through a coil gives one kick in each direction, the second one sharper because the magnet is moving faster by then.</p>"
            "<p><b>The vocabulary</b>: a pd is <b>induced</b>; a current <b>flows</b> if the circuit is closed; a generator <b>induces</b> a pd. The June 2025 report: \"There still seems to be a confusion between a p.d. being induced and a p.d. being produced\" — and \"produces\" was not accepted. The June 2023 report (Q8(a)(iii), regenerative braking) wanted the dynamo \"to cause an electric current\" that recharges the battery, not a description of split rings.</p>",
        ),
        worked(
            "Dropped through a coil",
            "A bar magnet is dropped through a vertical coil connected to a voltmeter. Explain why the voltmeter reading rises, falls to zero, reverses and returns to zero as the magnet falls through. (4 marks)",
            [
                INDUCTION_LEAD + " As the magnet enters the coil, the coil <b>cuts the field lines</b> — it experiences a <b>changing magnetic field</b>.",
                "This <b>induces a pd</b> across the coil, which the voltmeter reads; it rises as the magnet speeds up and the field through the coil grows.",
                "When the magnet is centred in the coil the field through it is momentarily <b>not changing</b>, so the pd falls to <b>zero</b>.",
                "As the magnet leaves, the field through the coil <b>decreases</b> — the opposite change — so the induced pd is <b>reversed</b>; once the magnet is clear, no change, so zero again.",
            ],
        ),
        practice("The chain in the exam", [
            written("ei-t1-q1", "A student waves a magnet near a coil connected to a sensitive voltmeter. Explain why the voltmeter reading keeps changing. (3)",
                    marks(["The magnet moves relative to the coil, so the coil experiences a <b>changing magnetic field</b> (cuts field lines).", "This <b>induces a pd</b> across the coil, which the voltmeter reads.", "As the magnet moves <b>towards and away</b>, the change reverses, so the induced pd <b>changes size and direction</b>."]), lines=3),
            choice("ei-t1-q2", "A magnet falls through a coil. The second kick on the meter is larger than the first because…",
                   ["the magnet is heavier", "the magnet is moving faster when it leaves, so the field changes more quickly", "the coil has heated up", "the second pole is stronger"], 1,
                   "Faster movement, faster change, larger induced pd."),
            choice("ei-t1-q3", "Which sentence would NOT be credited?",
                   ["The coil cuts the field lines", "A pd is induced across the coil", "The magnet produces a current in the coil", "A current flows because the circuit is closed"], 2,
                   "'Produces' is the rejected word, and the magnet does not make the current — the changing field induces a pd."),
            written("ei-t1-q4", "An electric car charges its battery when it slows down. Explain how. (3)",
                    marks(["As the car slows, the wheels turn the motor, which acts as a <b>generator (dynamo)</b>: a coil turns in a magnetic field.", "The coil experiences a changing magnetic field, so a <b>pd is induced</b> and a <b>current flows</b> to the battery…", "…transferring energy from the car's <b>kinetic</b> store to the battery's <b>chemical</b> store (which is also what slows the car)."]), lines=3),
            choice("ei-t1-q5", "The voltmeter reads zero at the instant the magnet is exactly centred in the coil because…",
                   ["the magnet has stopped", "the field through the coil is momentarily not changing", "the coil is too short", "the voltmeter is on the wrong setting"], 1,
                   "Maximum field through the coil, but zero rate of change at that instant."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T2 · Why the dynamo gets harder to turn [H]
# ---------------------------------------------------------------------

section_t2 = section(
    "dynamo-harder", "tricky", "Why the dynamo gets harder to turn when it lights a lamp", "13.2",
    equations=[r"\text{induced current} \rightarrow \text{its own field} \rightarrow \text{opposes the motion} \rightarrow \text{more work}"],
    blurb="A bicycle dynamo turning a voltmeter turns freely; connect a lamp and the handle stiffens. Two ideas earn the marks: the lamp needs energy, which has to come from extra work turning the handle; and the induced current's own magnetic field opposes the motion of the coil. In 2023 very few students gave the second.",
    tags=["H"],
    checklist=[
        "Explain the extra effort by conservation of energy",
        "Explain it by the induced current's field opposing the motion",
        "Explain why there is no extra effort with a voltmeter alone",
    ],
    parts=[
        explain(
            "Two explanations, both wanted",
            "<p>The June 2023 report (Q10(a)(ii)): many said the lamp \"would increase resistance in the circuit\" — wrong, a lamp has <b>far less</b> resistance than a voltmeter, which is exactly why a current now flows. Examiners wanted that \"the lamp required an energy transfer to produce light\", supplied by extra work turning the dynamo; credit was also available for \"an induced current in the rotating coil in the dynamo produces a magnetic field\" that opposes the coil's motion — \"very few examples of this\". \"The handle needs to be turned more\" was \"too vague\".</p>"
            "<table class='tbl'><tr><th>Idea</th><th>What to write</th></tr>"
            "<tr><td><b>Energy</b></td><td>with the lamp connected a <b>current flows</b> and the lamp transfers energy (to light and heat); by conservation of energy this must come from the <b>work done turning the handle</b>, so more force (more work per turn) is needed</td></tr>"
            "<tr><td><b>Field</b></td><td>the induced current in the coil produces its own <b>magnetic field</b>, which <b>interacts with the magnet's field</b> and gives a force on the coil that <b>opposes its rotation</b> (the induced current's field opposes the change causing it, 13.2) — the turning has to overcome this force</td></tr>"
            "<tr><td><b>Voltmeter only</b></td><td>a voltmeter has a <b>very high resistance</b>, so almost <b>no current</b> flows: a pd is induced but there is no induced current's field to oppose the motion and almost no energy transferred, so the handle turns freely</td></tr></table>"
            "<p>The same idea is why a motor draws a large current when it starts and less once it is turning (its turning coil induces a pd that opposes the supply), and why an electric car's regenerative braking slows the car: the opposing force on the generator's coil is the braking force.</p>",
        ),
        worked(
            "The 2023 question",
            "A hand-turned dynamo is connected to a voltmeter and turns easily. When a lamp is connected instead, the handle becomes harder to turn. Explain why. (3 marks)",
            [
                "With the lamp connected, the circuit has a low resistance, so the induced pd drives a <b>current</b>; the lamp <b>transfers energy</b> (lights up). By conservation of energy this energy must come from the <b>work done turning the handle</b>, so more effort is needed.",
                "Also, the induced current in the coil produces its own <b>magnetic field</b>, which interacts with the magnet's field to give a force on the coil that <b>opposes its rotation</b>.",
                "With only the voltmeter (very high resistance) almost <b>no current</b> flows, so there is no opposing force and no energy to supply — the handle turns freely.",
            ],
        ),
        practice("Harder to turn", [
            choice("ei-t2-q1", "Why does connecting a lamp to a hand-turned generator make it harder to turn?",
                   ["The lamp increases the resistance of the circuit", "A current now flows: the lamp needs energy, which comes from extra work turning the handle, and the current's field opposes the motion", "The lamp heats the coil", "The magnet gets weaker"], 1,
                   "Not resistance — a lamp has less resistance than a voltmeter, which is why current flows."),
            written("ei-t2-q2", "Explain, in terms of magnetic fields, why a generator supplying a current needs more force to turn it than the same generator on open circuit. (3)",
                    marks(["When a current flows in the coil it produces its own <b>magnetic field</b>.", "This <b>interacts with the permanent magnet's field</b>, giving a force on the coil that <b>opposes its motion</b> (the induced field opposes the change causing it).", "On open circuit no current flows, so there is no induced field and no opposing force."]), lines=3),
            choice("ei-t2-q3", "A student writes: 'the handle has to be turned more'. The examiners judged this…",
                   ["full marks", "too vague — it does not say why", "wrong physics", "a Level 3 answer"], 1,
                   "Say where the energy goes or what opposes the motion."),
            written("ei-t2-q4", "Explain how a generator's behaviour when it supplies a current illustrates conservation of energy. (2)",
                    marks(["The energy transferred by the current (to the lamp) does not appear from nowhere: it equals the <b>extra work done turning</b> the handle against the opposing force.", "More current drawn → more energy transferred → <b>more work needed</b>; the opposing force is what makes the work necessary."]), lines=2),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T3 · Generator output graphs [H, P]
# ---------------------------------------------------------------------

section_t3 = section(
    "output-graphs", "tricky", "Reading and sketching generator output graphs", "13.3P",
    equations=[r"\text{a.c.: through zero}", r"\text{dynamo: humps above zero}", r"\text{faster: taller and more frequent}"],
    blurb="The output of a generator against time is a graph question: recognise a.c. from d.c., read the peak pd and the period, and sketch what changes when the coil turns faster (both the peak and the frequency), when the magnet is stronger (the peak only) or when the coil is turned the other way (the graph is inverted).",
    tags=["H", "P"],
    checklist=[
        "Tell an alternator's output from a dynamo's on a graph",
        "Sketch the change when the coil is turned faster, or with a stronger magnet",
        "Read the peak pd, the period and the frequency from a graph",
    ],
    parts=[
        explain(
            "What each change does to the graph",
            "<table class='tbl'><tr><th>Change</th><th>Peak pd</th><th>Frequency / period</th><th>Shape</th></tr>"
            "<tr><td>turn the coil <b>faster</b></td><td><b>larger</b> (field cut more quickly)</td><td>frequency <b>higher</b>, period <b>shorter</b></td><td>taller and squashed sideways</td></tr>"
            "<tr><td><b>stronger magnet</b> or <b>more turns</b></td><td><b>larger</b></td><td>unchanged</td><td>taller only</td></tr>"
            "<tr><td>turn the coil the <b>other way</b></td><td>same</td><td>same</td><td><b>inverted</b> (starts negative where it started positive)</td></tr>"
            "<tr><td>swap slip rings for a <b>split ring</b></td><td>same</td><td>twice as many humps per second (each half-cycle flipped up)</td><td>all above the axis — d.c.</td></tr></table>"
            "<p>Reading: the <b>peak pd</b> is the height of the crest above zero; the <b>period</b> is the time for one full cycle (crest to crest for a.c.; for a dynamo, two humps make one turn of the coil); <b>frequency = 1 / period</b> (Topic 4). Mains a.c. has a frequency of 50 Hz, period 0.02 s. Note the a.c. pd is <b>zero twice per cycle</b> — when the coil is vertical and its sides are moving along the field, not cutting it — and <b>largest when the coil is flat</b>, cutting across the field fastest.</p>",
        ),
        worked(
            "Sketching the change",
            "The graph shows the a.c. output of an alternator: peak 6 V, period 0.04 s. The coil is now turned twice as fast. Describe the new graph. (3 marks)",
            [
                "The <b>peak pd doubles</b> to about 12 V, because the coil cuts the field twice as quickly.",
                "The <b>period halves</b> to 0.02 s (frequency doubles from 25 Hz to 50 Hz): twice as many cycles in the same time.",
                "It is still a.c. — the same shape through zero — just taller and squashed along the time axis.",
            ],
        ),
        practice("Output graphs", [
            choice("ei-t3-q1", "A graph of pd against time shows humps that are all above the axis. The generator is…",
                   ["an alternator", "a dynamo", "a transformer", "a motor"], 1,
                   "Never reverses: d.c., so a split-ring dynamo."),
            numeric("ei-t3-q2", "An alternator's output has a period of 0.025 s. Calculate its frequency.", 40, "Hz",
                    "$f = 1 \\div T$.",
                    ewau(r"f = 1 \div T", r"f = 1 \div 0.025", "40", "Hz")),
            written("ei-t3-q3", "Describe two changes to an alternator's output graph when a stronger magnet is used, the coil turning at the same rate. (2)",
                    marks(["The <b>peak pd is larger</b>.", "The <b>frequency (period) is unchanged</b> — the coil still turns at the same rate."]), lines=2),
            choice("ei-t3-q4", "At the instants when an alternator's output pd is zero, the coil is…",
                   ["flat, with its sides cutting across the field fastest", "vertical, with its sides moving along the field lines", "stationary", "at 45° to the field"], 1,
                   "Moving along the field: no lines cut, no pd."),
            written("ei-t3-q5", "A dynamo's output graph has 100 humps per second. State the rate at which the coil turns, and explain your answer. (2)",
                    marks(["<b>50 turns per second</b>.", "Each turn of the coil gives <b>two humps</b> (the induced pd reverses every half turn and the split ring flips the second half up)."]), lines=2),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T4 · Microphone versus loudspeaker [P]
# ---------------------------------------------------------------------

section_t4 = section(
    "mic-vs-speaker", "tricky", "Microphone versus loudspeaker: the 6-mark comparison", "13.4P",
    equations=[r"\text{speaker: fields interact} \rightarrow \text{force} \rightarrow \text{moves}", r"\text{microphone: moves} \rightarrow \text{changing field} \rightarrow \text{pd induced}"],
    blurb="The 2023 6-marker asked for a comparison of the two devices. Level 2 answers described the loudspeaker well and the microphone thinly; Level 3 needed the interaction of the coil's field and the magnet's field for the speaker, and electromagnetic induction from a coil moving in a magnetic field for the microphone — both chains, both devices.",
    tags=["P"],
    checklist=[
        "Write both chains side by side",
        "Say what the devices share and what is reversed",
        "Know what Level 3 needs for each device",
    ],
    parts=[
        explain(
            "The levels, and the two chains side by side",
            "<p>The June 2023 report (Q10(c)): Level 1 gave basic facts; Level 2 described how the cone's motion relates to the electrical signal; Level 3 discussed \"the interaction between the coil's magnetic field and the magnet's field\" for the speaker and, for the microphone, \"how electromagnetic induction is a result of a coil moving in a magnetic field\". \"It was acceptable for the details of one device to be less complete than the other provided they were both referenced\" — but Level 2 answers \"tended to describe the principles of operation of the loudspeaker more fully\". The microphone is the one to practise.</p>"
            "<table class='tbl'><tr><th>Loudspeaker (motor effect)</th><th>Microphone (induction)</th></tr>"
            "<tr><td>an <b>alternating current</b> from the amplifier flows in the coil</td><td>a <b>sound wave</b> (pressure variations) makes the diaphragm, and the coil fixed to it, <b>vibrate</b></td></tr>"
            "<tr><td>the current creates a <b>magnetic field around the coil</b>, which <b>interacts with the permanent magnet's field</b></td><td>the coil <b>moves through the permanent magnet's field</b>, so it experiences a <b>changing magnetic field</b></td></tr>"
            "<tr><td>this causes a <b>resultant force on the coil</b>, the same on either side, so the coil and cone <b>move forwards or backwards</b></td><td>this <b>induces a pd</b> across the coil; in the closed circuit a <b>current flows</b></td></tr>"
            "<tr><td>with a.c. the force <b>alternates</b> at the frequency of the current, so the cone vibrates and makes a <b>sound wave of that frequency</b></td><td>the vibration is back and forth, so the induced current is <b>alternating</b>, with the <b>frequency of the sound</b>; louder sound, larger current</td></tr>"
            "<tr><td colspan='2'><b>Shared</b>: a coil in the field of a permanent magnet, fixed to a cone or diaphragm. <b>Reversed</b>: current → movement in the speaker; movement → current in the microphone. A loudspeaker can be used as a microphone and vice versa.</td></tr></table>",
        ),
        worked(
            "The Level 3 answer",
            "Compare the way a moving-coil loudspeaker and a moving-coil microphone work. (6 marks)",
            [
                "<b>Both</b> have a coil in the magnetic field of a permanent magnet, attached to a cone (speaker) or diaphragm (microphone); the speaker turns a current into sound, the microphone turns sound into a current.",
                "<b>Speaker:</b> there is an alternating current in the coil; this creates a magnetic field around the coil, which interacts with the permanent magnetic field.",
                "This causes a resultant force on the coil, the same on either side, so the coil and cone move forwards or backwards; with a.c. the force alternates at the same frequency as the current, so the cone vibrates and produces a sound wave of that frequency.",
                "<b>Microphone:</b> the sound wave makes the diaphragm and the coil fixed to it vibrate, so the coil moves through the magnetic field of the permanent magnet.",
                "The coil therefore experiences a changing magnetic field, which induces a pd across the coil; in the closed circuit a current flows.",
                "Because the coil moves back and forth, the induced current is alternating, with the same frequency as the sound and a size that depends on its loudness — the reverse of the speaker.",
            ],
        ),
        practice("Microphone versus loudspeaker", [
            written("ei-t4-q1", "Explain how a moving-coil microphone produces an electrical signal from a sound wave, and how this differs from what happens in a moving-coil loudspeaker. (6)",
                    mark_scheme([
                        ("Shared", "Both: a coil in a permanent magnet's field, fixed to a cone/diaphragm; speaker converts current to sound, microphone sound to current."),
                        ("Speaker 1", "Current in the coil creates a magnetic field around the coil, which <b>interacts with the permanent magnetic field</b>."),
                        ("Speaker 2", "Resultant force on the coil, the same on either side, so the cone moves; with a.c. the force alternates at the current's frequency and the cone vibrates, producing sound of that frequency."),
                        ("Microphone 1", "Sound makes the diaphragm and coil vibrate, so the coil <b>moves through the magnetic field</b>."),
                        ("Microphone 2", "The coil experiences a changing magnetic field, so a <b>pd is induced</b> (electromagnetic induction); a current flows in the closed circuit."),
                        ("Microphone 3", "The current alternates at the frequency of the sound, larger for a louder sound."),
                    ], total=6, extra=["Level 3 (5–6) needs the field interaction for the speaker AND induction from a coil moving in a field for the microphone; one device may be thinner than the other if both are there."]), lines=8),
            choice("ei-t4-q2", "Which statement about the microphone would lift an answer to Level 3?",
                   ["The microphone has a diaphragm", "Sound makes the coil move", "The coil moving through the magnetic field experiences a changing field, so a pd is induced", "The microphone is connected to an amplifier"], 2,
                   "Induction as the result of a coil moving in a field."),
            choice("ei-t4-q3", "A loudspeaker is connected to a sensitive voltmeter and someone speaks into it. The voltmeter…",
                   ["reads nothing — speakers cannot do that", "shows a changing reading: the speaker is working as a microphone", "reads a steady pd", "reads 230 V"], 1,
                   "Same parts: sound moves the coil in the field, so a pd is induced."),
            written("ei-t4-q4", "State what is reversed between a loudspeaker and a microphone, and what is the same. (2)",
                    marks(["Reversed: speaker — <b>current causes movement</b> (motor effect); microphone — <b>movement induces a pd/current</b> (induction).", "Same: a <b>coil in a permanent magnet's field</b> fixed to a cone or diaphragm."]), lines=2),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T5 · The transformer 6-marker [H]
# ---------------------------------------------------------------------

section_t5 = section(
    "transformer-six", "tricky", "The transformer 6-marker: construction, operation, ratio", "13.5, 13.6, 13.7P",
    equations=[r"\text{construction} + \text{operation} + \text{ratio}"],
    blurb="The 2024 6-marker asked how a transformer steps 11 000 V down to 230 V. Level 3 needed all three parts: the construction (two coils on a closed iron core, many more turns on the primary), the operation (a.c. in the primary → changing field in the core → a.c. induced in the secondary) and the ratio (11 000 : 230, about 48 : 1). One part may be thin, but all three must be there.",
    tags=["H"],
    checklist=[
        "Describe the construction of a transformer",
        "Explain its operation with 'changing' and 'induces'",
        "Give the turns ratio for a stated pair of pds",
    ],
    parts=[
        explain(
            "The three parts and the levels",
            "<p>The June 2024 scheme (Q10(b), indicative content): <b>construction</b> — a closed iron core with a primary and a secondary coil, the primary having considerably more turns than the secondary; <b>operation</b> — a.c. in the primary causes a changing magnetic field in the core, which induces an a.c. pd in the secondary; <b>step-down</b> — more turns on the primary than the secondary; <b>ratio</b> — $V_p / V_s = N_p / N_s$, giving 11 000 : 230, i.e. about 48 : 1. Level 1 (1–2): basic ideas about construction or operation, or use of the ratio. Level 2 (3–4): more developed ideas about construction and operation, or the ratio. <b>Level 3 (5–6)</b>: detail on construction, how it works, and the ratio idea — \"one of the three aspects may be treated weakly and still be tolerated\". Within a level, coherence decides top or bottom.</p>"
            "<p>The 2025 three-marker (N5) is the operation part on its own, and the mark lost there — <b>the field in the core is changing</b> — is the one to check in the 6-marker too. Also \"<b>induces</b>\", not \"produces\".</p>",
        ),
        worked(
            "The 2024 answer",
            "A transformer at a substation reduces the pd from 11 000 V to 230 V. Explain how the transformer is constructed and how it does this. (6 marks)",
            [
                "<b>Construction:</b> two coils of insulated wire wound on a closed <b>soft-iron core</b> — the <b>primary</b> coil connected to the 11 000 V supply and the <b>secondary</b> coil to the 230 V output.",
                "It is a <b>step-down</b> transformer, so the primary has <b>many more turns</b> than the secondary.",
                "<b>Operation:</b> the <b>alternating current</b> in the primary coil produces a <b>changing magnetic field</b> in the iron core.",
                "The core carries this changing field through the secondary coil, so a <b>pd is induced</b> across the secondary — an alternating pd, because the field keeps reversing.",
                "<b>Ratio:</b> $V_p / V_s = N_p / N_s$, so $N_p / N_s = 11\\,000 / 230 \\approx 48$: the primary needs about 48 times as many turns as the secondary.",
                "For example 4800 turns on the primary and 100 on the secondary would give 230 V from 11 000 V.",
            ],
        ),
        practice("The transformer 6-marker", [
            written("ei-t5-q1", "A transformer in a laptop charger reduces the 230 V mains to 20 V. Explain how the transformer is constructed and how it works. (6)",
                    mark_scheme([
                        ("Construction 1", "Two coils (primary, secondary) on a closed <b>soft-iron core</b>."),
                        ("Construction 2", "Step-down: the <b>primary has more turns</b> than the secondary."),
                        ("Operation 1", "<b>Alternating current</b> in the primary produces a <b>changing magnetic field</b> in the core."),
                        ("Operation 2", "The secondary is in this changing field, so an alternating <b>pd is induced</b> across it."),
                        ("Ratio 1", "$V_p / V_s = N_p / N_s$ = $230 / 20 = 11.5$ : 1."),
                        ("Ratio 2", "e.g. 2300 primary turns to 200 secondary turns."),
                    ], total=6, extra=["Level 3 needs construction, operation and the ratio idea; one may be thin."]), lines=8),
            choice("ei-t5-q2", "An answer describes the construction and operation fully but says nothing about turns or ratio. Its best level is…",
                   ["Level 3, 6 marks", "Level 3, 5 marks — one aspect may be missing", "Level 2", "Level 1"], 2,
                   "All three aspects must be present for Level 3; one of them may be thin."),
            choice("ei-t5-q3", "Why does a transformer have a closed iron core rather than two separate coils in air?",
                   ["To make it heavier", "To carry almost all of the changing magnetic field from the primary through the secondary", "To conduct the current between the coils", "To store charge"], 1,
                   "The core links the coils magnetically; the coils are not connected electrically."),
            written("ei-t5-q4", "A step-up transformer raises 25 kV to 400 kV. State the turns ratio and which coil has more turns. (2)",
                    marks(["$N_s / N_p = V_s / V_p = 400 / 25 = 16$: ratio 1 : 16 (primary : secondary).", "The <b>secondary</b> has 16 times as many turns (step-up)."]), lines=2, tags=["P"]),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T6 · Transformer calculations the hard way [H, P]
# ---------------------------------------------------------------------

section_t6 = section(
    "transformer-hard", "tricky", "Transformer calculations the hard way: which equation, and both together", "13.7P, 13.10",
    equations=[r"\dfrac{V_p}{V_s} = \dfrac{N_p}{N_s}", r"V_p I_p = V_s I_s"],
    blurb="Two transformer equations are on the list. Turns in the question means the ratio equation; a current means the power equation; and some questions need both — turns to get the secondary pd, then the power equation for the current. Watch for mA, kV and the 100 % efficiency assumption.",
    tags=["H", "P"],
    checklist=[
        "Choose the right transformer equation from what the question gives",
        "Chain the two equations when a question needs both",
        "Convert mA and kV and state the efficiency assumption",
    ],
    parts=[
        explain(
            "Choosing, chaining, checking",
            "<table class='tbl'><tr><th>Question gives / asks</th><th>Equation</th></tr>"
            "<tr><td>turns and pds (any three of $N_p, N_s, V_p, V_s$)</td><td>$V_p / V_s = N_p / N_s$</td></tr>"
            "<tr><td>pds and currents (any three of $V_p, I_p, V_s, I_s$)</td><td>$V_p I_p = V_s I_s$ (100 % efficient)</td></tr>"
            "<tr><td>turns, the primary pd and a current — asks for the other current</td><td><b>both</b>: ratio first for $V_s$, then power for $I_s$</td></tr>"
            "<tr><td>power out, pd out, and asks for the current in</td><td>$P = IV$ for $I_s$ (or straight to $V_p I_p = P$)</td></tr></table>"
            "<p>The June 2025 report (Q6(a)(ii)): most substituted and rearranged confidently; the few who lost marks used the pd–current equation where turns were given. <b>Checks</b>: a step-down must give a smaller $V_s$ and a <b>larger</b> $I_s$; the power out can never exceed the power in; convert mA → A and kV → V (or keep the same prefix on both sides of the same equation).</p>",
        ),
        worked(
            "Both equations",
            "A transformer has 2000 turns on the primary and 100 turns on the secondary. The primary is connected to the 230 V mains and the secondary supplies a 5.0 A current to a heater. Assuming 100 % efficiency, calculate the current in the primary coil. (4 marks)",
            [
                "Secondary pd from the turns: $V_s = V_p \\times N_s / N_p = 230 \\times 100 / 2000 = 11.5$ V.",
                "Power equation: $V_p I_p = V_s I_s$, so $I_p = V_s I_s / V_p$.",
                "$I_p = 11.5 \\times 5.0 / 230$.",
                "$I_p = 0.25$ A — twenty times smaller than the secondary current, because the pd is twenty times larger.",
            ],
        ),
        practice("The hard way", [
            numeric("ei-t6-q1", "A transformer has 1200 primary turns and 60 secondary turns, with 240 V across the primary. The secondary supplies 3.0 A. Calculate the primary current, assuming 100 % efficiency.", 0.15, "A",
                    "$V_s$ from the turns first, then $V_p I_p = V_s I_s$.",
                    [r"$V_s = 240 \times 60 \div 1200 = 12$ V"] + ewau(r"I_p = V_s I_s \div V_p", r"I_p = 12 \times 3.0 \div 240", "0.15", "A")),
            numeric("ei-t6-q2", "A step-up transformer at a power station has 500 primary turns and 8000 secondary turns. The generator supplies 25 kV at 6000 A. Calculate the current in the transmission lines, assuming 100 % efficiency.", 375, "A",
                    "Ratio 16: $V_s = 400$ kV; then the power equation (keep kV on both sides).",
                    [r"$V_s = 25 \times 8000 \div 500 = 400$ kV"] + ewau(r"I_s = V_p I_p \div V_s", r"I_s = 25 \times 6000 \div 400", "375", "A")),
            choice("ei-t6-q3", "A question gives the number of turns on both coils and the primary pd, and asks for the secondary pd. A student uses $V_p I_p = V_s I_s$. What happens?",
                   ["It works", "It cannot work — no currents are given; the turns-ratio equation is needed", "It gives half the answer", "It gives the current instead"], 1,
                   "Turns → ratio equation; currents → power equation."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T7 · The national grid as a chain
# ---------------------------------------------------------------------

section_t7 = section(
    "grid-chain", "tricky", "The national grid explained as a chain, with and without the equations", "13.8, 13.9, 13.11P",
    equations=[r"\text{high pd} \rightarrow \text{low } I \rightarrow \text{low } I^2 R \rightarrow \text{efficient}"],
    blurb="Every grid question — why step up, why step down, why not transmit at 230 V — is the same chain: for a given power, a higher pd means a lower current; a lower current wastes less energy heating the cables; so the transfer is more efficient. The Foundation version says it in words; the Higher Physics version (13.11P) names $P = IV$ and $P = I^2R$ and can put numbers in.",
    checklist=[
        "Write the chain in words for any grid question",
        "Answer 'why not transmit at 230 V' and 'why step down' with the same chain",
        "Add the equations for the Higher Physics version",
    ],
    parts=[
        explain(
            "One chain, several questions",
            "<table class='tbl'><tr><th>Question</th><th>Answer (the same chain each time)</th></tr>"
            "<tr><td>why is the pd <b>stepped up</b> at the power station?</td><td>a higher pd means a <b>smaller current</b> for the same power → less energy <b>wasted as heat</b> in the cables → <b>more efficient</b> transmission</td></tr>"
            "<tr><td>why not transmit at <b>230 V</b>?</td><td>at 230 V the current would be <b>enormous</b> → huge heating losses in the cables (and far thicker cables needed) → most of the energy wasted</td></tr>"
            "<tr><td>why is it <b>stepped down</b> again?</td><td>400 kV is far too <b>dangerous</b> for homes and appliances → stepped down in stages to <b>230 V</b>, which appliances are designed for</td></tr>"
            "<tr><td>why use <b>a.c.</b> in the grid?</td><td>transformers only work with a.c. (a changing field is needed to induce a pd) → a.c. lets the pd be stepped up and down</td></tr></table>"
            "<p><b>With the equations</b> (13.11P, Higher Physics): $P = IV$ — for a fixed power, $I = P/V$, so ten times the pd gives a tenth of the current; $P = I^2 R$ — the power wasted in cables of resistance $R$ falls to a <b>hundredth</b>. The equations are named in the answer and, if numbers are given, used (the transmission-loss section, Higher Physics).</p>",
        ),
        worked(
            "Why not 230 V?",
            "Explain why the national grid does not transmit electricity from power stations at 230 V. (3 marks)",
            [
                "At 230 V, delivering the same power would need an <b>enormous current</b> in the cables (power = pd × current).",
                "A large current wastes a great deal of energy <b>heating the cables</b> (the heating rises steeply with current).",
                "So the transmission would be very <b>inefficient</b>; stepping up to a high pd keeps the current, and the losses, small.",
            ],
        ),
        practice("The grid chain", [
            written("ei-t7-q1", "Explain why transformers are used at both ends of the national grid's transmission lines. (4)",
                    marks(["At the power station a <b>step-up</b> transformer raises the pd (to e.g. 400 kV)…", "…so that the <b>current is small</b> and <b>little energy is wasted heating</b> the cables (efficient).", "Near the users a <b>step-down</b> transformer reduces the pd to 230 V…", "…because the transmission pd is far too <b>dangerous</b> for homes and appliances are designed for 230 V."]), lines=4),
            choice("ei-t7-q2", "Why must the grid use a.c. rather than d.c.?",
                   ["a.c. travels faster", "transformers only work with a.c., so only a.c. can be stepped up and down", "d.c. cannot flow in long cables", "a.c. is safer"], 1,
                   "No changing field, no induction, no transformer."),
            written("ei-t7-q3", "Using the equations $P = IV$ and $P = I^2R$, explain the advantage of transmitting at 400 kV rather than 40 kV for the same power. (3)",
                    marks(["$P = IV$: ten times the pd means <b>one tenth of the current</b> for the same power.", "$P = I^2R$: the power wasted in the cables depends on the <b>square of the current</b>…", "…so the loss falls to <b>one hundredth</b>: far more of the power reaches the users."]), lines=3, tags=["H", "P"]),
            numeric("ei-t7-q4", "A 10 MW supply is sent through cables of resistance 8.0 Ω. Calculate the power wasted when it is transmitted at 20 kV.", 2000000, "W",
                    "$I = P \\div V = 500$ A, then $I^2R$.",
                    [r"$I = \dfrac{10 \times 10^6}{20 \times 10^3} = 500$ A"] + ewau(r"P = I^2 R", r"P = 500^2 \times 8.0", "2\\,000\\,000", "W"), tags=["H", "P"]),
            choice("ei-t7-q5", "Which is the reason, not just the conclusion, in 'why transmit at high pd'?",
                   ["It is more efficient", "It is cheaper", "The current is smaller, so less energy is wasted as heat in the cables", "The cables are longer"], 2,
                   "'More efficient' is where the chain ends; the smaller current and less heating is why."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T8 · Investigating induction [H]
# ---------------------------------------------------------------------

section_t8 = section(
    "induction-practical", "tricky", "Investigating induction: the falling-magnet practical and the seven steps", "13.1P, 13.2",
    equations=[r"\text{variables} \rightarrow \text{relationship} \rightarrow \text{change} \rightarrow \text{measure} \rightarrow \text{use} \rightarrow \text{accuracy} \rightarrow \text{repeat}"],
    blurb="The 2024 paper dropped a magnet through a coil and asked for the practical steps to investigate the induced pd: drop from different heights, measured with a metre rule, in equal steps; record the maximum reading; set the voltmeter to a.c.; repeat and average; plot reading against height. The seven-step recipe from Topic 1 covers it.",
    tags=["H", "P"],
    checklist=[
        "Plan an investigation of induced pd against drop height (or speed, turns, magnet strength)",
        "Say why the voltmeter is set to a.c. and why the maximum is recorded",
        "Describe the expected result in words",
    ],
    parts=[
        explain(
            "The 2024 marks, step by step",
            diagram(dg.drop_svg(), 660, 280, "The falling-magnet investigation: a magnet dropped down a tube through a coil, the height measured with a metre rule, the maximum voltmeter reading recorded.") +
            "<p>The June 2024 scheme (Q10(a)(ii), 4 marks, any four): drop the magnet from <b>different heights</b>; use a <b>metre rule</b> (ruler, tape measure allowed); change the height <b>in steps</b> (e.g. 5 cm); record the <b>maximum</b> meter reading; <b>repeat</b> for each drop and average; set the digital voltmeter on <b>a.c.</b>; plot a <b>graph</b> of reading against height; or move the coil / use tubes of different lengths.</p>"
            "<table class='tbl'><tr><th>Step</th><th>Induced pd against drop height</th></tr>"
            "<tr><td><b>1 Variables</b></td><td>independent: height of the magnet above the coil (which sets its speed through the coil); dependent: the maximum voltmeter reading; control: the same magnet, the same coil, the same tube, the voltmeter setting</td></tr>"
            "<tr><td><b>2 Relationship</b></td><td>no equation; expect a greater height → faster magnet → a larger maximum pd</td></tr>"
            "<tr><td><b>3 Change</b></td><td>drop from heights of 10, 20, 30, 40, 50 cm, measured with a metre rule from the top of the coil</td></tr>"
            "<tr><td><b>4 Measure</b></td><td>record the <b>maximum</b> reading on the voltmeter (set to a.c., or use a data logger — the pd lasts a fraction of a second and reverses)</td></tr>"
            "<tr><td><b>5 Use</b></td><td>plot maximum pd against height; describe the trend</td></tr>"
            "<tr><td><b>6 Accuracy</b></td><td>drop the magnet the same way up each time, down a tube so it falls straight through the centre of the coil; measure height from the same point</td></tr>"
            "<tr><td><b>7 Repeat</b></td><td>three drops at each height, take a mean</td></tr></table>"
            "<p>Why <b>a.c.</b> and why the <b>maximum</b>: the induced pd rises, falls, reverses and falls again in well under a second; a d.c. meter averages it to nearly zero, and only the peak is a fair measure of \"how much pd\". Other versions of the practical change the <b>number of turns</b> or the <b>magnet</b> (strength) with the drop height fixed.</p>",
        ),
        worked(
            "The 6-mark plan",
            "Plan an investigation to find how the pd induced in a coil depends on the speed at which a magnet falls through it. (6 marks)",
            [
                "<b>Variables:</b> change the drop height (independent — a greater height gives a faster magnet); measure the maximum induced pd (dependent); keep the same magnet, coil, tube and voltmeter setting (control).",
                "<b>Relationship expected:</b> a faster-moving magnet gives a larger induced pd (no equation needed).",
                "<b>Change:</b> drop the magnet down the tube from 10, 20, 30, 40 and 50 cm above the coil, measured with a metre rule from the top of the coil.",
                "<b>Measure:</b> record the maximum reading on a voltmeter set to a.c. (or a data logger) for each drop.",
                "<b>Use:</b> plot maximum pd against drop height and describe the trend.",
                "<b>Accuracy and repeats:</b> drop the magnet the same way up through the centre of the coil each time; repeat each height three times and take a mean.",
            ],
        ),
        practice("The practical", [
            written("ei-t8-q1", "Plan an investigation into how the pd induced in a coil depends on the number of turns on the coil, using a magnet dropped through the coil. (6)",
                    mark_scheme([
                        ("Variables", "Independent: number of turns; dependent: maximum induced pd; control: drop height, the magnet, the tube, the voltmeter setting."),
                        ("Relationship", "No equation; expect more turns → larger maximum pd."),
                        ("Change", "Use coils of 10, 20, 30, 40, 50 turns (or add turns to one coil), same wire."),
                        ("Measure", "Drop the magnet from the same height each time; record the maximum reading on a voltmeter set to a.c. (or a data logger)."),
                        ("Use", "Plot maximum pd against number of turns; describe the trend."),
                        ("Accuracy", "Same height, measured with a metre rule; same way up; down a tube through the centre of the coil."),
                        ("Repeat", "Three drops per coil; take a mean."),
                    ], total=6, extra=["Any six of the seven points."]), lines=7),
            choice("ei-t8-q2", "Why is the voltmeter set to a.c. in the falling-magnet investigation?",
                   ["The magnet is an a.c. source", "The induced pd reverses as the magnet passes through, so a d.c. meter would average it to nearly zero", "a.c. meters are more sensitive", "The coil is connected to the mains"], 1,
                   "Reversing pd: a.c. setting (or a data logger) to catch it."),
            choice("ei-t8-q3", "Which reading is recorded for each drop?",
                   ["The reading after the magnet has landed", "The maximum reading", "The reading at the start", "The average of the readings over a minute"], 1,
                   "The pd lasts a fraction of a second: the maximum is the measure."),
            written("ei-t8-q4", "State the independent, dependent and one control variable when investigating how the induced pd depends on drop height. (3)",
                    marks(["Independent: the <b>height</b> the magnet is dropped from.", "Dependent: the <b>maximum pd</b> induced (voltmeter reading).", "Control: the same <b>magnet</b> / <b>coil</b> (number of turns) / tube / meter setting."]), lines=3),
            written("ei-t8-q5", "In the drop-height investigation, describe the result you would expect, and explain it. (2)",
                    marks(["The maximum pd <b>increases</b> with drop height (not in proportion — the speed goes as the square root of the height).", "A greater height means the magnet is moving <b>faster</b> through the coil, so the field through the coil <b>changes more quickly</b> and a larger pd is induced."]), lines=2),
        ]),
    ],
)

SECTIONS = [section_t1, section_t2, section_t3, section_t4, section_t5, section_t6, section_t7, section_t8]

# ---------------------------------------------------------------------
# Flashcards (the key-word definitions are added by ei_nn.FACTS_KW)
# ---------------------------------------------------------------------

FACTS = [
    # N1
    fact("The induction chain?", "The wire or coil moves through the magnetic field of the permanent magnet → so it experiences a changing magnetic field → this induces a pd across it → if it is in a closed circuit, a current flows.", "inducing-pd"),
    fact("The lead line when the magnet moves?", "The magnet moves relative to the coil (either may move) — then the chain follows.", "inducing-pd"),
    fact("Which word for the pd: 'induced' or 'produced'?", "Induced — 'produces' was not accepted (2025).", "inducing-pd"),
    fact("Magnet held still in a coil: reading?", "Zero — no relative movement, no changing field, nothing induced.", "inducing-pd"),
    fact("Open coil vs closed coil?", "Both have a pd induced; only the closed circuit has a current.", "inducing-pd"),
    fact("How does a power station generate continuously?", "A turbine keeps turning the coil (or magnets) so the coil experiences a continuously changing field.", "inducing-pd"),
    # N2
    fact("Three ways to induce a larger pd?", "Move faster; stronger magnet; more turns on the coil.", "induced-size-direction"),
    fact("Two ways to reverse the induced pd?", "Reverse the direction of movement; turn the magnet round.", "induced-size-direction"),
    fact("What does the induced current's field do?", "It opposes the change that produced it — so work has to be done to keep moving the magnet or turning the generator.", "induced-size-direction"),
    # N3
    fact("Why does the pd in a turning coil alternate?", "Each side moves up through the field for half a turn, then down: reversing the movement reverses the pd every half turn.", "alternator-dynamo"),
    fact("Slip rings vs split ring?", "Slip rings (two complete rings): alternator, a.c. Split ring (one ring in two halves, swapping brushes every half turn): dynamo, d.c.", "alternator-dynamo"),
    fact("Shape of a dynamo's output graph?", "Humps all above the axis: one direction, rising and falling, not steady.", "alternator-dynamo"),
    fact("Turn the coil twice as fast: output?", "Peak pd doubles AND frequency doubles.", "alternator-dynamo"),
    # N4
    fact("The loudspeaker chain?", "Current in the coil → field around the coil → interacts with the permanent field → resultant force on the coil → same direction on either side → coil moves forwards or backwards (left-hand rule) → with a.c. the force alternates at the current's frequency.", "speaker-microphone"),
    fact("The microphone chain?", "Sound makes the diaphragm and coil vibrate → the coil moves through the magnet's field → changing field → pd induced → alternating current at the sound's frequency.", "speaker-microphone"),
    fact("Why does a speaker coil move along its axis, not rotate?", "The force is the same on every part of the coil (radial field), not opposite on the two sides.", "speaker-microphone"),
    # N5
    fact("How a transformer works, in three marks?", "Alternating current in the primary → changing magnetic field in the iron core → alternating pd induced in the secondary.", "transformer"),
    fact("The mark most often lost on the transformer (2025)?", "That the field in the core is CHANGING.", "transformer"),
    fact("Why no transformer with d.c.?", "A steady current gives a steady field; only a changing field induces a pd.", "transformer"),
    fact("Step-up vs step-down: turns?", "Step-up: more turns on the secondary (larger pd, smaller current). Step-down: fewer on the secondary.", "transformer"),
    fact("Why a soft-iron core?", "Easily magnetised and demagnetised, so it carries the changing field from one coil to the other.", "transformer"),
    # N6
    fact("The turns-ratio equation?", "$V_p / V_s = N_p / N_s$ — primary on top on both sides; the pd changes by the same factor as the turns.", "turns-ratio"),
    fact("The 2024 ratio for 11 000 V → 230 V?", "11 000 : 230 ≈ 48 : 1 — the primary has about 48 times as many turns.", "turns-ratio"),
    fact("Check on a turns-ratio answer?", "Step-down must give a smaller secondary pd; if not, the fraction is upside down.", "turns-ratio"),
    # N7
    fact("Where are step-up and step-down transformers?", "Step-up at the power station (to ~400 kV); step-down at substations near towns and homes (to 230 V).", "national-grid"),
    fact("Why transmit at a high pd?", "Higher pd → smaller current for the same power → less energy wasted heating the cables → more efficient.", "national-grid"),
    fact("Why step down near homes?", "400 kV is far too dangerous; appliances are designed for 230 V.", "national-grid"),
    # N8
    fact("The transformer power equation?", "$V_p I_p = V_s I_s$ (100 % efficient): step the pd up by a factor and the current comes down by the same factor.", "transformer-power"),
    fact("Which transformer equation when?", "Turns given or asked → ratio equation; currents → power equation; both → ratio first, then power.", "transformer-power"),
    # N9
    fact("The two equations for high-voltage transmission?", "$P = IV$: higher $V$, smaller $I$ for the same $P$. $P = I^2R$: loss in the cables falls with $I^2$.", "transmission-loss"),
    fact("Ten times the pd: what happens to the cable loss?", "A tenth of the current, a hundredth of the loss.", "transmission-loss"),
    fact("Common slip finding the cable loss?", "Putting the transmission pd into $P = IV$ — that is the power carried; the loss is $I^2R$ with the cable's resistance.", "transmission-loss"),
    # T1
    fact("The 2024 falling-magnet marks?", "Coil cuts the field lines / changing field; pd (or current) induced; voltmeter reads it; electrons in the wire experience a force; the pd changes size and direction as the magnet passes.", "induction-chain-exam"),
    fact("Why does the reading reverse as the magnet passes through?", "Entering: field through the coil increases. Leaving: it decreases — the opposite change, so the opposite pd.", "induction-chain-exam"),
    fact("Why is the second kick larger?", "The magnet is moving faster when it leaves, so the field changes more quickly.", "induction-chain-exam"),
    # T2
    fact("Why is a dynamo harder to turn with a lamp connected?", "A current flows: the lamp needs energy, which comes from extra work turning the handle; and the induced current's field opposes the coil's motion.", "dynamo-harder"),
    fact("Why does a voltmeter alone not make it harder?", "Very high resistance, so almost no current — no opposing field, almost no energy transferred.", "dynamo-harder"),
    fact("The wrong answer in 2023?", "'The lamp increases the resistance' — a lamp has far LESS resistance than a voltmeter, which is why current flows.", "dynamo-harder"),
    # T3
    fact("Stronger magnet, same speed: graph change?", "Taller peak; same frequency.", "output-graphs"),
    fact("When is an alternator's pd zero?", "When the coil is vertical: its sides move along the field lines and cut none.", "output-graphs"),
    fact("Humps per turn on a dynamo graph?", "Two — one per half turn.", "output-graphs"),
    # T4
    fact("Level 3 in the microphone/speaker comparison (2023)?", "Speaker: the coil's field interacts with the magnet's field. Microphone: induction as a result of a coil moving in a magnetic field. Both devices referenced.", "mic-vs-speaker"),
    fact("What do speaker and microphone share? What is reversed?", "Share: coil in a permanent magnet's field, fixed to a cone/diaphragm. Reversed: current → movement vs movement → current.", "mic-vs-speaker"),
    # T5
    fact("The three parts of the transformer 6-marker (2024)?", "Construction (two coils on a closed iron core, more turns on the primary for step-down); operation (a.c. → changing field in the core → pd induced in the secondary); ratio (11 000 : 230 ≈ 48 : 1).", "transformer-six"),
    fact("Why a closed iron core?", "It carries almost all the changing field from the primary through the secondary; the coils are not connected electrically.", "transformer-six"),
    # T6
    fact("Turns, primary pd and secondary current given, primary current asked?", "Ratio equation for $V_s$, then $V_p I_p = V_s I_s$ for $I_p$.", "transformer-hard"),
    fact("Checks on a transformer calculation?", "Step-down: smaller $V_s$, LARGER $I_s$; power out never exceeds power in; mA → A, kV → V.", "transformer-hard"),
    # T7
    fact("Why not transmit at 230 V?", "The current would be enormous → huge heating losses in the cables → most energy wasted.", "grid-chain"),
    fact("Why must the grid use a.c.?", "Transformers need a changing field, so only a.c. can be stepped up and down.", "grid-chain"),
    fact("Reason vs conclusion in a grid answer?", "'Smaller current, less heating in the cables' is the reason; 'more efficient' is the conclusion.", "grid-chain"),
    # T8
    fact("The 2024 practical marks?", "Different heights; metre rule; equal steps; record the maximum reading; repeat and average; voltmeter on a.c.; plot reading against height.", "induction-practical"),
    fact("Why record the maximum, on a.c.?", "The induced pd lasts a fraction of a second and reverses; a d.c. meter would average it to nearly zero.", "induction-practical"),
    fact("Expected result for pd against drop height?", "Larger pd from a greater height (faster magnet, quicker change) — increasing, not in proportion.", "induction-practical"),
]
