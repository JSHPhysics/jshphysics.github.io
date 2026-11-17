"""
wv_tricky.py — Topic 4 (Waves): the tricky bits T1–T7 and the flashcards.

T1 Reading wave graphs               T5 Seismic waves and the Earth (H, P)
T2 Explaining transverse/longitudinal  T6 The core practical
T3 Refraction of waves               T7 Apply the seven steps
T4 Echoes and ultrasound distances (H, P)
"""

from math import pi, sin

from revlib import (
    axis, choice, curve, ewau, explain, fact, graph, group, mark_scheme, marks,
    numeric, practice, sample, section, sf, worked, written,
)

V_SOUND = 340

# ---------------------------------------------------------------------
# T1 · Reading wave graphs
# ---------------------------------------------------------------------

graph_dd = graph(
    axis("distance in cm", 60, 10), axis("displacement in mm", 4, 2, mn=-4),
    [curve(sample(lambda x: 3 * sin(2 * pi * x / 20), 0, 60, 61))],
    "Displacement against distance: a wave with crests 20 cm apart and amplitude 3 mm.",
)
graph_dt = graph(
    axis("time in ms", 20, 5), axis("displacement in mm", 4, 2, mn=-4),
    [curve(sample(lambda t: 3 * sin(2 * pi * t / 8), 0, 20, 61))],
    "Displacement against time: the same point oscillating with a period of 8 ms and amplitude 3 mm.",
)

section_t1 = section(
    "wave-graphs-hard", "tricky", "Reading wave graphs: distance axis or time axis?", "4.3, 4.4",
    equations=[r"\text{displacement–distance: read } \lambda", r"\text{displacement–time: read } T \text{, then } f = 1/T"],
    blurb="Two graphs look identical — a wave shape — but one has distance along the bottom and the other has time. One gives the wavelength, the other the period. Read the axis before you read anything else.",
    checklist=[
        "Read amplitude and wavelength from a displacement–distance graph",
        "Read the period from a displacement–time graph and turn it into a frequency",
        "Combine the two to find the wave speed",
    ],
    parts=[
        explain(
            "Which graph is which",
            "<table class='tbl'><tr><th>Graph</th><th>It shows</th><th>Crest-to-crest gap is…</th><th>Height of a crest is…</th></tr>"
            "<tr><td>displacement against <b>distance</b></td><td>a snapshot of the whole wave at one instant</td><td>the <b>wavelength</b> λ</td><td>the amplitude</td></tr>"
            "<tr><td>displacement against <b>time</b></td><td>one point on the wave, oscillating as time passes</td><td>the <b>period</b> T (then $f = 1/T$)</td><td>the amplitude</td></tr></table>"
            "<p>Traps: reading crest-to-trough as the amplitude (it is twice the amplitude); reading crest-to-trough as the wavelength (it is half); forgetting to convert cm, mm and ms; and reading a wavelength off a time graph. Using <b>several</b> wavelengths and dividing is more accurate than one.</p>",
        ),
        worked(
            "Speed from two graphs",
            "The graph shows displacement against distance for a wave (crests 20 cm apart). A displacement–time graph for the same wave (in the practice below) shows a period of 8 ms. Find the wavelength, the frequency and the speed.",
            [
                r"<b>From the distance graph:</b> $\lambda = 20$ cm $= 0.20$ m; amplitude 3 mm.",
                r"<b>From the time graph (given):</b> $T = 8$ ms $= 0.008$ s, so $f = \dfrac{1}{T} = \dfrac{1}{0.008} = 125$ Hz.",
                r"<b>Speed:</b> $v = f \lambda = 125 \times 0.20 = 25$ m/s.",
            ],
            graph=graph_dd,
        ),
        practice("Wave graphs", [
            group("wv-t1-q1", "The graph shows displacement against distance for a wave.", [
                numeric("wv-t1-q1a", "State the amplitude of the wave in mm.", 3, "mm", "Rest position to crest.", [r"Crest at $+3$ mm, so amplitude $= 3$ mm (not 6 mm)."], label="a"),
                numeric("wv-t1-q1b", "State the wavelength of the wave in cm.", 20, "cm", "Crest to next crest.", [r"Crests at 5, 25, 45 cm: $\lambda = 20$ cm."], label="b"),
            ], graph=graph_dd),
            group("wv-t1-q2", "The graph shows displacement against time for one point on a wave.", [
                numeric("wv-t1-q2a", "State the period of the wave in ms.", 8, "ms", "Crest to next crest along the time axis.", [r"Crests at 2, 10, 18 ms: $T = 8$ ms."], label="a"),
                numeric("wv-t1-q2b", "Calculate the frequency of the wave.", 125, "Hz", "f = 1 ÷ T with T in seconds.", [r"$T = 0.008$ s; $f = \dfrac{1}{0.008} = 125$ Hz."], label="b"),
            ], graph=graph_dt),
            numeric("wv-t1-q3", "Using the two graphs above (wavelength 20 cm, period 8 ms), calculate the speed of the wave.", 25, "m/s",
                    "v = f λ with λ in metres.", [r"$v = f \lambda = 125 \times 0.20 = 25$ m/s."]),
            choice("wv-t1-q4", "A displacement–time graph shows crests 0.5 s apart. What is the frequency?",
                   ["0.5 Hz", "2 Hz", "5 Hz", "It cannot be found from a time graph"], 1,
                   "T = 0.5 s, so f = 1/0.5 = 2 Hz."),
            choice("wv-t1-q5", "On a displacement–distance graph the distance from a crest to the next trough is 15 cm. The wavelength is…",
                   ["15 cm", "7.5 cm", "30 cm", "60 cm"], 2,
                   "Crest to trough is half a wavelength."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T2 · Explaining transverse and longitudinal
# ---------------------------------------------------------------------

section_t2 = section(
    "explain-wave-types", "tricky", "Explaining wave types and the evidence", "4.2, 4.5",
    equations=[r"\text{say: oscillations, and which direction compared with travel}"],
    blurb="The explain marks need the word <b>oscillations</b> (or vibrations) and a comparison with the <b>direction of energy transfer</b>. \"Up and down\" and \"side to side\" score nothing on their own.",
    checklist=[
        "Explain, with the correct phrase, why sound is longitudinal and light is transverse",
        "Explain the evidence that it is the wave that travels, not the medium",
        "Describe a slinky or rope demonstration of each wave type",
    ],
    parts=[
        explain(
            "The phrases that score",
            "<p><b>Transverse:</b> \"the oscillations are <b>perpendicular (at right angles) to the direction of energy transfer</b>\". <b>Longitudinal:</b> \"the oscillations are <b>parallel to the direction of energy transfer</b>, producing compressions and rarefactions\".</p>"
            "<p>\"Up and down\" only works if you also say the wave travels along — the comparison is the mark. The June 2025 scheme for rock in an S wave wanted \"oscillations or vibrations perpendicular to the direction of travel of the wave\".</p>"
            "<p><b>Demonstrations:</b> on a slinky, push the end back and forth along its length for a longitudinal wave (compressions travel along; each coil moves to and fro along the slinky); flick the end sideways for a transverse wave (the hump travels along; each coil moves across). A marked coil shows the medium <b>oscillates about a fixed point and does not travel</b> — the evidence for 4.2.</p>"
            "<p><b>Sound is longitudinal</b> because the loudspeaker cone moves <b>forward and back</b>, pushing the air into a compression and then leaving a rarefaction, and these travel outwards in the <b>same direction</b> as the cone's movement.</p>",
        ),
        worked(
            "Why sound is longitudinal",
            "Explain why sound is described as a longitudinal wave. (2 marks)",
            [
                "<b>What oscillates:</b> the air particles <b>oscillate back and forth</b> about fixed positions, making <b>compressions and rarefactions</b>.",
                "<b>Direction:</b> these oscillations are <b>parallel to the direction in which the sound travels</b> (the direction of energy transfer) — which is the definition of longitudinal.",
            ],
        ),
        practice("Explaining wave types", [
            written("wv-t2-q1", "Light is a transverse wave. Explain what this means. (1)",
                    marks(["The <b>oscillations are at right angles (perpendicular) to the direction the wave travels</b> (direction of energy transfer)."]), lines=2),
            written("wv-t2-q2", "A student says \"a transverse wave goes up and down and a longitudinal wave goes side to side\". Explain why this would not score full marks. (2)",
                    marks(["Both must be compared with the <b>direction of energy transfer</b>: transverse oscillations are <b>perpendicular</b> to it, longitudinal oscillations are <b>parallel</b> to it.",
                           "\"Up and down\" and \"side to side\" are both perpendicular to a wave travelling along — the answer does not say what the oscillation is compared with, and it does not use the word oscillation."]), lines=3),
            written("wv-t2-q3", "Describe how a slinky can be used to show a longitudinal wave, and how it shows that the coils do not travel with the wave. (3)",
                    mark_scheme([
                        ("Make it", "Push and pull one end of the slinky <b>back and forth along its length</b>."),
                        ("See it", "<b>Compressions</b> (bunched coils) and rarefactions travel along the slinky."),
                        ("Evidence", "A marked coil <b>oscillates back and forth about the same place</b> and does not move along with the compression — the wave travels, the coils do not."),
                    ]), lines=4),
            choice("wv-t2-q4", "A loudspeaker cone moves forward and back. Why does this produce a longitudinal wave in the air?",
                   ["Because the cone is round", "Because the air is pushed into compressions and rarefactions that travel in the same direction as the cone moves", "Because sound is fast", "Because the air moves across the room"], 1,
                   "Oscillation direction = travel direction → longitudinal."),
            written("wv-t2-q5", "Explain how a floating object on a water wave shows that the wave is transverse and that the water does not travel with it. (2)",
                    marks(["The object <b>oscillates up and down</b> — at right angles to the direction the wave travels across the surface — so the wave is <b>transverse</b>.",
                           "It <b>stays in the same place</b> rather than moving along with the wave, so the water (the medium) does not travel; only the energy does."]), lines=3),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T3 · Refraction of waves
# ---------------------------------------------------------------------

section_t3 = section(
    "wave-refraction", "tricky", "Refraction of waves: direction, speed, wavelength, frequency", "4.10, 4.16P",
    equations=[r"f \text{ unchanged}", r"\lambda \propto v \text{ (at fixed } f)", r"\text{slows} \Rightarrow \text{towards the normal}"],
    blurb="Every refraction answer comes down to one fact: the <b>speed changes</b> at the boundary and the <b>frequency does not</b>. From that follow the direction change and the wavelength change.",
    checklist=[
        "Explain refraction of a wave at a boundary in terms of the change of speed turning the wavefronts",
        "State what happens to speed, wavelength and frequency when sound passes into another medium",
        "Use the ripple-tank example: shallow water slows the waves and shortens the wavelength",
    ],
    parts=[
        explain(
            "Wavefronts turning",
            "<p>Think in <b>wavefronts</b> (the lines of crests). When a wavefront meets a boundary <b>at an angle</b>, one end reaches the new medium before the other. If the wave is <b>slower</b> there, that end lags, the wavefront <b>swings round</b>, and the wave now travels <b>closer to the normal</b>. If the new medium is faster, the opposite: away from the normal. If the wavefront meets the boundary square on (along the normal) every part changes speed together and the direction does not change — only the speed and wavelength.</p>"
            "<p><b>Frequency is fixed by the source</b>: the number of wavefronts arriving at the boundary each second equals the number leaving. So with $v = f\\lambda$, the <b>wavelength changes in proportion to the speed</b>: slower → shorter wavelength (the wavefronts bunch up), faster → longer.</p>"
            "<table class='tbl'><tr><th>Wave crossing into…</th><th>Speed</th><th>Wavelength</th><th>Frequency</th><th>Direction</th></tr>"
            "<tr><td>ripples into <b>shallow</b> water</td><td>slower</td><td>shorter</td><td>same</td><td>towards the normal</td></tr>"
            "<tr><td>sound from air into <b>water</b></td><td>faster (≈1500 m/s from 340)</td><td>longer</td><td>same</td><td>away from the normal</td></tr>"
            "<tr><td>light from air into <b>glass</b></td><td>slower</td><td>shorter</td><td>same</td><td>towards the normal</td></tr></table>"
            "<p>June 2023 Q6(b) (3 marks): \"refraction is caused by a change in speed\"; \"sound speeds up entering water\"; \"light slows down entering water\". Mentioning only that the wavelength changes was worth one mark at most.</p>",
        ),
        worked(
            "Ripples into shallow water",
            "Water waves in a ripple tank pass from deep water into shallow water, where they travel more slowly. Explain what happens to their wavelength and frequency, and to their direction if they meet the boundary at an angle. (3 marks)",
            [
                "<b>Frequency:</b> <b>unchanged</b> — it is set by the dipper; the same number of waves arrive at the boundary each second as leave it.",
                r"<b>Wavelength:</b> <b>shorter</b> — $v = f\lambda$ with $f$ constant and $v$ smaller, so the wavefronts bunch closer together.",
                "<b>Direction:</b> the end of each wavefront that reaches the shallow water first slows first, so the wavefronts turn and the wave bends <b>towards the normal</b>.",
            ],
        ),
        practice("Refraction of waves", [
            written("wv-t3-q1", "Sound passes from air into a brick wall, where it travels faster. State what happens to its speed, wavelength and frequency. (3)",
                    marks(["Speed <b>increases</b>.", "Wavelength <b>increases</b> (in proportion).", "Frequency <b>stays the same</b>."]), lines=3),
            written("wv-t3-q2", "Explain why the frequency of a wave does not change when it is refracted. (1)",
                    marks(["The frequency is set by the <b>source</b>: waves arrive at the boundary and leave it at the <b>same rate</b> (they cannot pile up or vanish)."]), lines=2),
            written("wv-t3-q3", "Explain, in terms of wavefronts, why water waves change direction when they cross at an angle into shallower water. (3)",
                    mark_scheme([
                        ("Speed", "The waves travel <b>more slowly</b> in the shallow water."),
                        ("One end first", "The end of each wavefront that reaches the shallow water <b>first slows down first</b>, while the rest is still moving fast."),
                        ("Turn", "So the wavefront <b>turns</b> (pivots) and the wave travels in a new direction — <b>towards the normal</b>."),
                    ]), lines=4),
            choice("wv-t3-q4", "Sound travels at 340 m/s in air and 1500 m/s in water. A 1000 Hz sound passes into water. Its wavelength in the water is…",
                   ["0.34 m", "1.5 m", "0.23 m", "unchanged"], 1,
                   "f unchanged: λ = v/f = 1500/1000 = 1.5 m (0.34 m in air)."),
            numeric("wv-t3-q5", "Ripples of wavelength 2.0 cm travel at 10 cm/s in deep water. In shallow water they slow to 6 cm/s. Calculate the wavelength in the shallow water.", 2.0 * 6 / 10, "cm",
                    "f is the same in both: f = v/λ = 10/2 = 5 Hz; then λ = v/f.",
                    [r"$f = \dfrac{v}{\lambda} = \dfrac{10}{2.0} = 5$ Hz (unchanged across the boundary).", r"In shallow water $\lambda = \dfrac{v}{f} = \dfrac{6}{5} = 1.2$ cm."]),
            written("wv-t3-q6", "Explain why a wave that crosses a boundary along the normal changes speed but not direction. (2)",
                    marks(["The whole wavefront reaches the boundary <b>at the same time</b>, so every part changes speed <b>together</b>.",
                           "No part lags behind another, so the wavefront does not turn — the wave keeps its direction (its wavelength still changes)."]), lines=3),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T4 · Echoes and ultrasound distances (H, P)
# ---------------------------------------------------------------------

q4_1 = 330 * 0.018 / 2
q4_2 = 1500 * 0.4 / 2
q4_3 = 2 * 85 / 340
q4_4_v = 2 * 0.030 / (40e-6)

section_t4 = section(
    "echo-distances", "tricky", "Echoes and ultrasound: the distance is half", "4.8P, 4.15P",
    equations=[r"\text{distance there and back} = v \times t", r"\text{distance to the surface} = \dfrac{v \times t}{2}"],
    blurb="A pulse goes out, reflects, and comes back: the time measured is for <b>twice</b> the distance. Halve the time (or halve the distance) — forgetting to is the standard lost mark, and so is leaving the time in milliseconds.",
    tags=["H", "P"],
    checklist=[
        "Calculate a depth or distance from an echo time, halving correctly",
        "Convert ms and μs before calculating",
        "Describe how sonar / a scanner / crack detection uses reflected pulses, in the 6-mark form",
    ],
    parts=[
        explain(
            "Halve it, and watch the units",
            "<p>The pulse travels <b>to the surface and back</b>, so $v \\times t$ is the <b>round-trip</b> distance. Either halve the time first or halve the distance at the end — the June 2023 scheme (Q1(b), 4 marks) credited both routes and gave 3 of 4 for 5.94 m (forgot to halve) and the June 2025 report notes a candidate who \"rearranged correctly but did not double the distance in the diagram\". Write the halving as its own line.</p>"
            "<p>Units: echo times come in <b>ms</b> ($\\times 10^{-3}$ s) and ultrasound times in <b>μs</b> ($\\times 10^{-6}$ s). Speeds: sound in air 330–340 m/s, in water about 1500 m/s, in body tissue about 1500 m/s, in steel about 6000 m/s.</p>"
            "<p>Embedded calculation practice (the <i>Echoes and ultrasound</i> type) sits below the worked example.</p>",
        ),
        explain(
            "The 6-mark sonar answer",
            "<p>June 2024 Q10(d) asked how ultrasound is used to measure the depth of the sea. Level 3 (5–6) needed, in a logical order: a pulse of <b>ultrasound</b> (above 20 kHz; \"sonar\" accepted) is <b>emitted</b> from a device on the boat; it travels through the water and is <b>reflected</b> by the sea bed; it returns to a <b>detector</b> on the boat; the <b>time</b> between emission and return is measured; the <b>speed of sound in water is known</b>; <b>distance = speed × time</b>; and the distance (or the time) is <b>halved</b> because the pulse went down and back. \"Two or more of ultrasound, pulse, halving and the calculation step\" separated Level 3 from Level 2.</p>"
            "<p><b>Crack detection</b> (2022 Q10(b)): a pulse into a metal bar reflects from the far end; if there is a crack, part of the pulse reflects from the crack <b>earlier</b> (shorter distance), and the pulse from the far end is <b>smaller</b> because some of the energy has already been reflected — the amplitude of a wave shows the energy it carries. <b>Foetal scan:</b> pulses reflect at the <b>boundaries between tissues</b>; the times give the depths and the echoes build an image; no ionising radiation.</p>",
        ),
        worked(
            "Bat and prey",
            "A bat's call travels at 330 m/s. It hears the echo from an insect 18 ms after calling. Calculate the distance from the bat to the insect.",
            [
                r"<b>Convert:</b> $t = 18\ \text{ms} = 0.018$ s.",
                r"<b>Round trip:</b> $x = v \times t = 330 \times 0.018 = 5.94$ m (there and back).",
                r"<b>Halve:</b> distance to the insect $= \dfrac{5.94}{2} = 2.97 \approx 3.0$ m.",
            ],
        ),
        practice("Echo distances", [
            numeric("wv-t4-q1", "A bat hears the echo of its call 18 ms after making it. Sound travels at 330 m/s. Calculate the distance to the object.", sf(q4_1, 2), "m",
                    "Round trip = v × t; then halve.",
                    [r"$x = 330 \times 0.018 = 5.94$ m round trip; distance $= 5.94 \div 2 = 2.97 \approx 3.0$ m."]),
            numeric("wv-t4-q2", "A ship's sonar pulse returns from the sea bed after 0.40 s. Sound travels at 1500 m/s in sea water. Calculate the depth of the sea.", q4_2, "m",
                    "Halve the time first: 0.20 s each way.",
                    [r"Time to the sea bed $= 0.40 \div 2 = 0.20$ s.", r"Depth $= v \times t = 1500 \times 0.20 = 300$ m."]),
            numeric("wv-t4-q3", "A student claps 85 m from a wall and hears the echo. Sound travels at 340 m/s. Calculate the time between the clap and the echo.", q4_3, "s",
                    "The sound travels 2 × 85 m.",
                    [r"Round-trip distance $= 2 \times 85 = 170$ m.", r"$t = \dfrac{x}{v} = \dfrac{170}{340} = 0.5$ s."]),
            numeric("wv-t4-q4", "An ultrasound pulse sent into a steel bar 3.0 cm thick returns from the far end after 10 μs. Calculate the speed of ultrasound in the steel. Type the answer as 6000.", round(2 * 0.030 / 10e-6), "m/s",
                    "Round-trip distance 0.060 m; t = 10 × 10⁻⁶ s.",
                    [r"Round trip $= 2 \times 0.030 = 0.060$ m; $t = 10 \times 10^{-6}$ s.", r"$v = \dfrac{0.060}{10 \times 10^{-6}} = 6000$ m/s."]),
            written("wv-t4-q5", "Explain how a ship uses ultrasound to measure the depth of the water beneath it. (6)",
                    mark_scheme([
                        ("Emit", "A device on the ship <b>emits a pulse of ultrasound</b> (frequency above 20 kHz) downwards."),
                        ("Travel", "The pulse travels through the water…"),
                        ("Reflect", "…and is <b>reflected by the sea bed</b> back up to the ship."),
                        ("Time", "A detector on the ship records the <b>time between emitting the pulse and receiving the echo</b>."),
                        ("Speed", "The <b>speed of sound in water is known</b> (about 1500 m/s)."),
                        ("Calculate", "<b>Distance = speed × time</b>, and the distance (or time) is <b>halved</b> because the pulse went down and back."),
                    ], extra=["June 2024 Q10(d): Level 3 needs the detailed, ordered description including ultrasound/pulse, the reflection, the timing, the calculation and the halving."]), lines=8),
            written("wv-t4-q6", "An ultrasound pulse is sent into a metal bar. When the bar has a crack, an extra reflected pulse appears earlier than the pulse from the far end, and the far-end pulse is smaller. Explain both observations. (3)",
                    mark_scheme([
                        ("Earlier", "Part of the pulse is <b>reflected at the crack</b>, which is <b>closer</b> than the far end, so that echo travels a shorter distance and <b>returns sooner</b>."),
                        ("Smaller", "Some of the pulse's energy has <b>already been reflected</b> at the crack, so less reaches the far end and less is reflected back from it."),
                        ("Amplitude", "The <b>amplitude</b> of a wave shows the <b>energy</b> it carries, so the far-end echo has a smaller amplitude."),
                    ]), lines=4),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T5 · Seismic waves and the Earth (H, P)
# ---------------------------------------------------------------------

section_t5 = section(
    "seismic", "tricky", "Seismic waves and what they tell us about the Earth", "4.5, 4.15P",
    equations=[r"\text{P: longitudinal, through solids and liquids}", r"\text{S: transverse, solids only}"],
    blurb="Earthquakes send P and S waves through the Earth. Where each kind is detected — and where it is not — tells us the outer core is liquid and the Earth's density changes with depth. The 6-mark version is marked on the <b>conclusions</b>, not the observations.",
    tags=["H", "P"],
    checklist=[
        "Describe P and S waves: wave type, speed, and which materials they pass through",
        "Explain the shadow zones and what they show about the core",
        "Explain how the curved paths show the density (and speed) changes with depth",
    ],
    parts=[
        explain(
            "P, S and the shadow zones",
            "<table class='tbl'><tr><th></th><th>P waves (primary)</th><th>S waves (secondary)</th></tr>"
            "<tr><td>Type</td><td><b>longitudinal</b></td><td><b>transverse</b></td></tr>"
            "<tr><td>Speed</td><td>faster — arrive first</td><td>slower — arrive second</td></tr>"
            "<tr><td>Travel through</td><td><b>solids and liquids</b></td><td><b>solids only</b> (a liquid cannot be sheared sideways)</td></tr>"
            "<tr><td>Detected</td><td>almost everywhere, but with a <b>shadow zone</b> where they are refracted by the core</td><td>only within about 103° of the earthquake — <b>not on the far side</b> of the Earth</td></tr></table>"
            "<p><b>Conclusions</b> (what the examiners mark): S waves are not detected on the far side of the Earth → S waves cannot pass through the core → the <b>outer core is liquid</b>. P waves are <b>refracted</b> (their paths curve, and they bend sharply at the core boundary, leaving a P-wave shadow zone) → their <b>speed changes</b> with depth → the <b>density of the Earth changes</b> with depth, and the core is denser. Both wave types curve gradually through the mantle because the density, and so the speed, increases with depth.</p>"
            "<p>The 2022 report on the 6-mark version: stating observations (\"no S waves are detected on the other side\") without conclusions \"scores only Level 1\"; Level 3 \"combined both observations and conclusions\" — \"remember to draw conclusions from your analysis of information\".</p>",
        ),
        worked(
            "Observation → conclusion",
            "Seismometers on the opposite side of the Earth from an earthquake detect P waves but no S waves. Explain what this shows about the Earth's core. (3 marks)",
            [
                "<b>Observation:</b> S waves are <b>not detected</b> on the far side; P waves are.",
                "<b>Physics:</b> S waves are <b>transverse</b> and can only travel through <b>solids</b>; P waves are longitudinal and travel through solids and liquids.",
                "<b>Conclusion:</b> the S waves must have been <b>stopped by a liquid</b> on the way — the <b>outer core is liquid</b>.",
            ],
        ),
        practice("Seismic waves", [
            choice("wv-t5-q1", "Why are S waves not detected on the opposite side of the Earth from an earthquake?",
                   ["They are too slow", "They are transverse and cannot travel through the liquid outer core", "They are absorbed by the crust", "They are infrasound"], 1,
                   "Transverse waves need a solid; the liquid outer core stops them."),
            written("wv-t5-q2", "Explain how the curved paths of P waves through the Earth show that the Earth's density changes with depth. (2)",
                    marks(["The paths curve because the waves are <b>refracted</b> — their <b>speed changes</b> as they go deeper.",
                           "The speed of a seismic wave depends on the <b>density</b> of the rock, so the density must change (increase) with depth."]), lines=3),
            written("wv-t5-q3", "Describe two differences between P waves and S waves. (2)",
                    marks(["P waves are <b>longitudinal</b>, S waves are <b>transverse</b>.", "P waves travel <b>faster</b> (arrive first) and can pass through <b>liquids</b>; S waves cannot."]), lines=3),
            written("wv-t5-q4", "A student writes: \"P waves have a shadow zone.\" Add the conclusion that would turn this observation into a full answer. (2)",
                    marks(["The P-wave shadow zone exists because the P waves are <b>sharply refracted</b> at the boundary with the core…",
                           "…which shows there is a <b>sudden change in density / speed</b> at the core boundary — the core is a different material (denser) from the mantle."]), lines=3),
            choice("wv-t5-q5", "Which statement is a conclusion, not an observation?",
                   ["No S waves arrive on the far side of the Earth", "P waves arrive before S waves", "The outer core must be liquid", "P waves have a shadow zone"], 2,
                   "The others are what the seismometers record; the liquid core is what we deduce from them."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T6 · The core practical
# ---------------------------------------------------------------------

section_t6 = section(
    "core-practical-waves", "tricky", "Core practical: speed, frequency and wavelength in a fluid and a solid", "4.17",
    equations=[r"v = f \lambda", r"v = \dfrac{x}{t}"],
    blurb="The core practical measures the speed, frequency and wavelength of waves in a <b>fluid</b> (ripples in a tank) and in a <b>solid</b> (a stretched string driven by a vibration generator), and asks which equipment is suitable for each.",
    checklist=[
        "Describe the ripple-tank method: frequency from the generator or counting, wavelength from several wavelengths, speed from v = fλ or timing a crest",
        "Describe the string method: vibration generator, standing wave, wavelength from the loops, speed from v = fλ",
        "Say why each piece of equipment is suitable and what limits the accuracy",
    ],
    parts=[
        explain(
            "Fluid: the ripple tank",
            "<ol><li>Set up the ripple tank with a <b>dipper</b> driven by a <b>signal generator</b>; a <b>lamp</b> above projects the pattern onto a screen below.</li>"
            "<li><b>Frequency:</b> read it from the signal generator, or count the waves passing a point in 10 s and divide by 10.</li>"
            "<li><b>Wavelength:</b> freeze the pattern with a <b>stroboscope</b> (or photograph it with a ruler in shot); measure across <b>10 wavelengths</b> with a ruler and divide by 10.</li>"
            "<li><b>Speed:</b> $v = f \\lambda$. Check by timing a crest over a measured distance ($v = x/t$).</li></ol>"
            "<p><b>Suitability:</b> the ruler on the screen is fine for a wavelength of a few cm but the image may be magnified — measure the tank itself, or calibrate the screen; a stopwatch is too slow for one wave, which is why you count ten or use the generator's frequency.</p>",
        ),
        explain(
            "Solid: waves on a string",
            "<ol><li>Attach a <b>string</b> to a <b>vibration generator</b> driven by a signal generator; pass the string over a <b>pulley</b> with a <b>mass hanging</b> on the end to keep the tension constant.</li>"
            "<li>Adjust the frequency until a clear <b>standing wave</b> forms — a fixed pattern of loops.</li>"
            "<li><b>Wavelength:</b> each loop is <b>half a wavelength</b>; measure the length of several loops with a metre rule and work out $\\lambda$.</li>"
            "<li><b>Frequency:</b> from the signal generator.</li>"
            "<li><b>Speed:</b> $v = f \\lambda$. Repeat at other frequencies; the speed should be the same (it depends on the tension and the string, not on $f$).</li></ol>"
            "<p><b>Suitability:</b> the loops are static so a metre rule works; the string's vibration is far too fast to time directly, which is why $v = f\\lambda$ is used instead of $x/t$.</p>",
        ),
        worked(
            "Speed on a string",
            "A string vibrates at 40 Hz and shows a standing wave of three loops over a length of 0.90 m. Calculate the speed of the waves on the string.",
            [
                r"<b>Wavelength:</b> three loops $= 1.5$ wavelengths, so $\lambda = \dfrac{0.90}{1.5} = 0.60$ m (one loop is half a wavelength).",
            ] + ewau(r"v = f \times \lambda", r"v = 40 \times 0.60", "24", "m/s"),
        ),
        practice("The core practical", [
            numeric("wv-t6-q1", "A string vibrating at 40 Hz shows three loops over 0.90 m. Calculate the wave speed.", 40 * 0.60, "m/s",
                    "Three loops = 1.5 λ.", [r"$\lambda = 0.90 \div 1.5 = 0.60$ m; $v = 40 \times 0.60 = 24$ m/s."]),
            numeric("wv-t6-q2", "In a ripple tank, 10 wavelengths measure 25 cm and the generator is set to 8 Hz. Calculate the wave speed.", 8 * 0.025, "m/s",
                    "λ = 2.5 cm = 0.025 m.", [r"$\lambda = 25 \div 10 = 2.5$ cm $= 0.025$ m; $v = 8 \times 0.025 = 0.2$ m/s."]),
            written("wv-t6-q3", "Explain why measuring across ten wavelengths and dividing by ten gives a more accurate wavelength than measuring one. (2)",
                    marks(["The <b>uncertainty</b> in reading the ruler (about ± 1 mm) is the same whether one or ten wavelengths are measured…",
                           "…so it is a <b>smaller fraction</b> of a longer measurement; dividing by ten also divides the error by ten."]), lines=3),
            written("wv-t6-q4", "Explain why the speed of waves on a string is found using v = fλ rather than by timing the wave over a distance. (2)",
                    marks(["The waves on the string travel far too <b>fast</b> (and the pattern repeats too quickly) to <b>time with a stopwatch</b>.",
                           "The standing-wave loops are <b>stationary</b>, so the wavelength can be measured with a rule, and the frequency is read from the generator — so $v = f\\lambda$ works."]), lines=3),
            written("wv-t6-q5", "Describe how a student could use a stroboscope to measure the wavelength of ripples in a tank. (2)",
                    marks(["Adjust the stroboscope's flash rate until it <b>matches the wave frequency</b>, so the pattern appears to <b>stand still</b> (frozen).",
                           "Then <b>measure the distance across several wavelengths</b> with a ruler and divide by the number."]), lines=3),
            choice("wv-t6-q6", "Why is a mass hung over a pulley in the string experiment?",
                   ["To make the string vibrate", "To keep the tension in the string constant", "To measure the frequency", "To stop the string breaking"], 1,
                   "The wave speed depends on the tension, so it must stay fixed."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T7 · Apply the seven steps
# ---------------------------------------------------------------------

section_t7 = section(
    "planning-waves", "tricky", "Apply the seven steps: the wave practicals", "4.7, 4.17",
    equations=[r"\text{7 steps: variables, equation, change, measure, use, accuracy, repeat + mean}"],
    blurb="The seven-step recipe from Topic 1 applied to the wave practicals: the speed of sound in air, the ripple tank, and waves on a string.",
    checklist=[
        "Write a full method for measuring the speed of sound in air",
        "Write a full method for finding the speed of ripples in a tank",
        "Write a full method for finding the speed of waves on a string",
    ],
    parts=[
        explain(
            "The seven steps, applied here",
            "<p>From <a href='#key-concepts/planning-practical'>Topic 1, T6</a>: (1) the two variables; (2) the equation; (3) what you change and how, what you keep the same; (4) what you measure, how, with what; (5) what you do with the results; (6) one accuracy detail; (7) repeat <b>and calculate a mean</b>.</p>"
            "<table class='tbl'><tr><th>Step</th><th>Ripple tank</th><th>String</th></tr>"
            "<tr><td>1 Variables</td><td>frequency (change); wavelength (measure); speed (calculate)</td><td>frequency (change); wavelength from the loops (measure)</td></tr>"
            "<tr><td>2 Equation</td><td>$v = f\\lambda$ (check with $v = x/t$)</td><td>$v = f\\lambda$</td></tr>"
            "<tr><td>3 Change</td><td>frequency on the signal generator; same water depth</td><td>frequency on the signal generator; same tension (same hanging mass) and same string</td></tr>"
            "<tr><td>4 Measure</td><td>f from the generator (or count in 10 s); λ across 10 wavelengths with a ruler, pattern frozen by a stroboscope</td><td>f from the generator; length of several loops with a metre rule (each loop = ½λ)</td></tr>"
            "<tr><td>5 Use</td><td>calculate v for each f; plot v against f (should be constant) or λ against 1/f (straight line)</td><td>calculate v for each f; compare — it should be the same</td></tr>"
            "<tr><td>6 Accuracy</td><td>measure 10 wavelengths not one; darken the room</td><td>adjust f until the loops are sharp; measure from node to node</td></tr>"
            "<tr><td>7 Repeat</td><td>repeat each f and average λ</td><td>repeat each f and average</td></tr></table>",
        ),
        worked(
            "Speed of sound in air, in full",
            "Describe how a student could measure the speed of sound in air. (6 marks)",
            [
                "<b>Step 1 — variables.</b> I will measure the <b>distance</b> the sound travels and the <b>time</b> it takes; the speed is calculated from them.",
                r"<b>Step 2 — equation.</b> $v = \dfrac{x}{t}$.",
                "<b>Step 3 — set-up.</b> Two microphones a measured distance apart (e.g. 2.0 m with a tape measure), both connected to a data logger / oscilloscope, in a line with the sound source.",
                "<b>Step 4 — measure.</b> Make a sharp sound (clap) in line with the microphones; the logger records the <b>time delay</b> between the sound reaching the first and the second microphone.",
                "<b>Step 5 — use the results.</b> Speed = separation ÷ time delay. (Or: repeat for several separations and plot distance against time delay; the gradient is the speed.)",
                "<b>Step 6 — accuracy.</b> Use the data logger rather than a stopwatch so there is no reaction time; use a large separation so the delay is long compared with the logger's resolution.",
                "<b>Step 7 — repeat.</b> Repeat several times <b>and calculate a mean</b> time delay.",
            ],
        ),
        practice("Planning", [
            written("wv-t7-q1", "Describe how a student could investigate how the speed of water waves in a ripple tank depends on the depth of the water. (6)",
                    mark_scheme([
                        ("Variables", "Change the <b>depth of water</b>; measure the <b>wave speed</b> (from f and λ, or by timing a crest)."),
                        ("Equation", "$v = f\\lambda$ (or $v = x/t$)."),
                        ("Change", "Set the depth with a ruler (e.g. 0.5 cm to 2.5 cm); keep the <b>frequency</b> of the dipper the same."),
                        ("Measure", "Frequency from the signal generator; <b>wavelength</b> across 10 wavelengths on the screen with a ruler (stroboscope to freeze the pattern), ÷ 10."),
                        ("Use", "Calculate $v = f\\lambda$ for each depth and <b>plot speed against depth</b>."),
                        ("Accuracy", "Measure several wavelengths not one; keep the tank level so the depth is uniform."),
                        ("Repeat", "<b>Repeat and calculate a mean</b> wavelength at each depth."),
                    ], total=6), lines=8, hint="Seven steps; any six score."),
            written("wv-t7-q2", "Describe how a student could find the speed of waves on a stretched string using a vibration generator. (6)",
                    mark_scheme([
                        ("Variables", "Change the <b>frequency</b>; measure the <b>wavelength</b> of the standing wave; calculate the speed."),
                        ("Equation", "$v = f\\lambda$; each loop of the standing wave is half a wavelength."),
                        ("Change", "Frequency on the signal generator; keep the <b>tension</b> constant with the same mass hanging over the pulley, and the same string length."),
                        ("Measure", "Adjust f until a clear standing wave forms; measure the <b>length of several loops</b> with a metre rule and work out λ; read f from the generator."),
                        ("Use", "Calculate $v = f\\lambda$ for each frequency; the values should agree — take the mean, or plot λ against 1/f."),
                        ("Accuracy", "Measure from node to node across several loops; make sure the loops are sharply defined before measuring."),
                        ("Repeat", "<b>Repeat and calculate a mean</b> for each frequency."),
                    ], total=6), lines=8),
        ]),
    ],
)

SECTIONS = [section_t1, section_t2, section_t3, section_t4, section_t5, section_t6, section_t7]

# ---------------------------------------------------------------------
# Flashcards
# ---------------------------------------------------------------------

FACTS = [
    fact("What do waves transfer, and not transfer?", "Energy and information — without transferring matter.", "what-is-a-wave"),
    fact("Evidence that it is the wave, not the water, that travels?", "A floating cork bobs up and down as ripples pass but stays in the same place.", "what-is-a-wave"),
    fact("Evidence that it is the wave, not the air, that travels (sound)?", "Dust or a candle flame in front of a speaker vibrates in place; the air does not rush across the room, but the sound arrives.", "what-is-a-wave"),
    fact("Amplitude?", "Maximum displacement from the undisturbed position (rest to crest, not crest to trough).", "wave-words"),
    fact("Wavelength?", "Distance from a point on one wave to the same point on the next (crest to crest). Unit m.", "wave-words"),
    fact("Frequency?", "Number of waves passing a point per second. Unit Hz.", "wave-words"),
    fact("Period?", "Time for one complete wave to pass a point. Unit s.", "wave-words"),
    fact("Wavefront?", "A line joining points at the same stage of the wave (all the crests); the wave travels at right angles to it.", "wave-words"),
    fact("Loudness and pitch of a sound depend on…", "Loudness: amplitude. Pitch: frequency.", "wave-words"),
    fact("Transverse wave?", "Oscillations perpendicular to the direction of energy transfer: light and all EM waves, water surface waves, S waves.", "transverse-longitudinal"),
    fact("Longitudinal wave?", "Oscillations parallel to the direction of energy transfer, with compressions and rarefactions: sound, P waves.", "transverse-longitudinal"),
    fact("Which waves need a medium?", "All mechanical waves (sound, water, seismic, string) need particles; electromagnetic waves do not and cross a vacuum.", "transverse-longitudinal"),
    fact("The two wave equations?", "v = f × λ and v = x ÷ t, for every kind of wave.", "wave-equations"),
    fact("Speed of sound in air, in water; speed of light?", "About 340 m/s (330 also used); about 1500 m/s; 3 × 10⁸ m/s.", "wave-equations"),
    fact("Why does v = fλ work?", "f waves pass each second, each λ long, so the wave advances f × λ metres per second.", "wave-equations"),
    fact("11 mm, 1.5 MHz, 20 kHz in base units?", "0.011 m; 1.5 × 10⁶ Hz; 20 000 Hz.", "wave-equations"),
    fact("T and f?", "T = 1/f and f = 1/T. 50 Hz → 0.02 s.", "period-nn"),
    fact("Frequency by counting?", "f = number of waves ÷ time taken. Count for longer for more accuracy.", "period-nn"),
    fact("Speed of sound with a stopwatch: the method?", "Large measured distance; see the bang, start; hear it, stop; speed = distance ÷ time; repeat and average.", "measuring-wave-speed"),
    fact("Why stand further apart in the stopwatch method?", "The travel time is longer, so the reaction time is a smaller fraction of it.", "measuring-wave-speed"),
    fact("Speed of sound with two microphones?", "Measured separation; data logger records the delay between the sound reaching each; v = separation ÷ delay. No reaction time.", "measuring-wave-speed"),
    fact("Speed of ripples, two ways?", "Time a crest over a measured distance (v = x/t); or frequency from the generator and wavelength from 10 wavelengths ÷ 10, then v = fλ.", "measuring-wave-speed"),
    fact("Four things that can happen at a boundary?", "Reflection, refraction, transmission, absorption.", "boundaries"),
    fact("Which way does a wave refract when it slows down?", "Towards the normal. Speeding up: away from the normal.", "boundaries"),
    fact("Why do carpets make a room less echoey?", "They absorb more of the sound, so less is reflected back into the room.", "boundaries"),
    fact("Range of human hearing? Ultrasound? Infrasound?", "20 Hz to 20 000 Hz. Above 20 000 Hz. Below 20 Hz.", "sound-ear"),
    fact("How does the ear detect sound?", "Sound makes the eardrum vibrate at the same frequency; the vibration passes through the small bones to the cochlea, which sends nerve signals.", "sound-ear"),
    fact("Why does the ear detect only a limited range of frequencies?", "The eardrum (a solid) only vibrates efficiently over a limited range of frequencies — too low or too high and it does not respond enough.", "sound-ear"),
    fact("Uses of ultrasound on the spec?", "Sonar (depth), foetal scanning (echoes from tissue boundaries). Infrasound/seismic waves: exploring the Earth's core.", "sound-ear"),
    fact("Displacement–distance vs displacement–time graph?", "Distance axis: the gap between crests is the wavelength. Time axis: the gap is the period (f = 1/T).", "wave-graphs-hard"),
    fact("Crest-to-trough on a graph is…", "Twice the amplitude (vertically) or half a wavelength (horizontally). Not the amplitude; not the wavelength.", "wave-graphs-hard"),
    fact("The phrase for transverse?", "\"Oscillations perpendicular to the direction of energy transfer.\" Say oscillations, and say what they are compared with.", "explain-wave-types"),
    fact("On refraction, what happens to f, v and λ?", "Frequency unchanged (set by the source); speed changes; wavelength changes in proportion to the speed.", "wave-refraction"),
    fact("Ripples into shallow water?", "Slower, shorter wavelength, same frequency, bend towards the normal.", "wave-refraction"),
    fact("Sound into water?", "Faster (≈1500 m/s), longer wavelength, same frequency, bends away from the normal.", "wave-refraction"),
    fact("Echo distance?", "Distance to the surface = v × t ÷ 2 — the pulse goes there and back. Halve it, as its own line.", "echo-distances"),
    fact("ms and μs?", "× 10⁻³ s and × 10⁻⁶ s.", "echo-distances"),
    fact("Sonar in six points?", "Ultrasound pulse emitted; travels through water; reflected by the sea bed; time to return measured; speed in water known; distance = v × t, halved.", "echo-distances"),
    fact("Crack in a bar: why is the echo earlier and the far-end echo smaller?", "Part of the pulse reflects at the crack (closer, so sooner); less energy reaches the far end, so its echo has a smaller amplitude.", "echo-distances"),
    fact("P waves vs S waves?", "P: longitudinal, faster, through solids and liquids. S: transverse, slower, solids only.", "seismic"),
    fact("What do the S-wave shadow and the P-wave shadow show?", "No S waves on the far side → the outer core is liquid. P waves refracted sharply at the core → a sudden change in density; curved paths → density changes with depth.", "seismic"),
    fact("Observation vs conclusion in the seismic 6-marker?", "Observations alone are Level 1; the marks are for the conclusions drawn from them.", "seismic"),
    fact("Core practical: fluid?", "Ripple tank: f from the generator or counting; λ from 10 wavelengths ÷ 10 (stroboscope to freeze); v = fλ or time a crest.", "core-practical-waves"),
    fact("Core practical: solid?", "String with a vibration generator and a hanging mass; standing wave; each loop = ½λ; f from the generator; v = fλ.", "core-practical-waves"),
    fact("Why measure 10 wavelengths?", "The ruler's uncertainty is the same, so it is a smaller fraction of a longer length; dividing by 10 divides the error by 10.", "core-practical-waves"),
]
