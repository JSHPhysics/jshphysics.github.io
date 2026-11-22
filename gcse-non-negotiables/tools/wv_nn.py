"""
wv_nn.py — Topic 4 (Waves): the non-negotiables N1–N9.

N1 What a wave is              N6 Measuring wave speed
N2 Wave words                  N7 Waves at a boundary
N3 Transverse and longitudinal N8 Sound, the ear, ultrasound and infrasound (H, P)
N4 The wave equations          N9 Key words
N5 Period and frequency
"""

from revlib import (
    choice, diagram, ewau, explain, fact, mark_scheme, marks, numeric,
    practice, section, sf, worked, written,
)
import wv_diagrams as dg

V_SOUND = 340

# ---------------------------------------------------------------------
# N1 · What a wave is
# ---------------------------------------------------------------------

section_n1 = section(
    "what-is-a-wave", "nn", "What a wave is", "4.1, 4.2",
    equations=[r"\text{waves transfer energy and information, not matter}"],
    blurb="A wave carries energy (and information) from one place to another without carrying the material along with it. The evidence is that the water or the air only oscillates; it does not travel.",
    checklist=[
        "State that waves transfer energy and information without transferring matter",
        "Describe the evidence for this with water waves and with sound",
    ],
    parts=[
        explain(
            "The statement and the evidence",
            "<p><b>Waves transfer energy and information without transferring matter.</b> Drop a stone in a pond and the ripples spread out, but the water does not flow outwards; shout across a room and the sound arrives, but no wind blows from your mouth.</p>"
            "<p><b>Evidence with water waves:</b> a cork or a duck on the water <b>bobs up and down</b> (oscillates) as the ripples pass, but it <b>stays in the same place</b> — it is not carried along. So the wave travels, the water does not.</p>"
            "<p><b>Evidence with sound:</b> a loudspeaker cone <b>vibrates back and forth</b> and the sound reaches you across the room, but the air does not rush from the speaker to you (a candle flame in front of it flickers but is not blown out; dust in front of a speaker vibrates in place). The air particles oscillate about fixed positions; the wave passes through them.</p>"
            "<p>The energy is real: sea waves move boats and erode cliffs; sound waves make your eardrum move.</p>",
        ),
        worked(
            "Evidence question",
            "A student watches a leaf floating on a pond as ripples pass. Explain how the leaf's movement shows that the wave, and not the water, travels across the pond. (2 marks)",
            [
                "<b>Observation:</b> the leaf <b>moves up and down</b> (oscillates) as each ripple passes…",
                "<b>Conclusion:</b> …but it <b>does not move along</b> with the ripples — it stays in the same place. So the water only oscillates; it is the <b>wave</b> (the energy) that travels across the pond.",
            ],
        ),
        practice("Waves carry energy", [
            written("wv-n1-q1", "State what a wave transfers, and what it does not transfer. (2)",
                    marks(["Transfers <b>energy</b> (and information)…", "…<b>without transferring matter</b> (the medium does not travel)."]), lines=2),
            choice("wv-n1-q2", "A cork on a pond bobs up and down as ripples pass but stays where it is. What does this show?",
                   ["The water travels across the pond", "The wave travels but the water does not", "The cork is too heavy to move", "Waves do not carry energy"], 1,
                   "The water only oscillates; the wave (energy) travels."),
            written("wv-n1-q3", "Describe evidence that it is the sound wave and not the air that travels from a loudspeaker to a listener. (2)",
                    marks(["Dust (or a candle flame) in front of the speaker <b>vibrates in place</b> but is not blown across the room — the air particles <b>oscillate about fixed positions</b>.",
                           "The sound still arrives at the listener, so the <b>wave</b> has travelled through the air without the air moving across the room."]), lines=3),
            written("wv-n1-q4", "Give one example that shows waves carry energy. (1)",
                    marks(["Sea waves <b>move boats</b> / erode cliffs; sound waves make the <b>eardrum vibrate</b>; light from the Sun warms the ground; a loud sound can rattle a window."]), lines=2),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N2 · Wave words
# ---------------------------------------------------------------------

section_n2 = section(
    "wave-words", "nn", "Amplitude, wavelength, frequency, period, wavefront", "4.3, 4.4",
    equations=[r"\lambda\ \text{(m)},\ f\ \text{(Hz)},\ T\ \text{(s)},\ A\ \text{(m)}"],
    blurb="Five words, each with a precise definition and a unit. Most one-mark losses in this topic are a definition that is nearly right.",
    checklist=[
        "Define amplitude, wavelength, frequency and period with units",
        "Read amplitude and wavelength off a wave diagram",
        "Use the words wavefront and wave velocity correctly",
    ],
    parts=[
        explain(
            "The definitions",
            diagram(dg.transverse_svg(), 480, 270, "A transverse wave drawn as displacement against distance. The amplitude is measured from the undisturbed (middle) position to a crest, not from trough to crest; the wavelength is crest to crest.") +
            "<table class='tbl'><tr><th>Term</th><th>Definition</th><th>Unit</th></tr>"
            "<tr><td><b>Amplitude</b></td><td>the <b>maximum displacement</b> of a point on the wave from its <b>undisturbed (rest) position</b></td><td>m</td></tr>"
            "<tr><td><b>Wavelength λ</b></td><td>the distance from a point on one wave to the <b>same point on the next wave</b> (crest to crest, compression to compression)</td><td>m</td></tr>"
            "<tr><td><b>Frequency f</b></td><td>the <b>number of waves passing a point per second</b> (or produced per second)</td><td>Hz (hertz, = per second)</td></tr>"
            "<tr><td><b>Period T</b></td><td>the <b>time for one complete wave</b> to pass a point (one full oscillation)</td><td>s</td></tr>"
            "<tr><td><b>Wave velocity</b></td><td>the speed (and direction) at which the <b>wave (energy) travels</b> — not the speed of the oscillating particles</td><td>m/s</td></tr>"
            "<tr><td><b>Wavefront</b></td><td>a line joining points that are at the <b>same stage</b> of the wave (e.g. all the crests) — the lines you see in a ripple tank; the wave travels at right angles to its wavefronts</td><td>—</td></tr></table>"
            "<p><b>Traps:</b> amplitude is <i>not</i> crest-to-trough (that is twice the amplitude). Frequency is not \"how fast the wave goes\" — that is wave speed. A louder sound has a bigger <b>amplitude</b>; a higher-pitched sound has a higher <b>frequency</b>. The 2022 report: \"learn the difference between frequency and loudness of a sound.\"</p>",
        ),
        worked(
            "Reading the diagram",
            "On the diagram above, a crest is 6 cm above the undisturbed position and the crests are 24 cm apart. State the amplitude and the wavelength. (2 marks)",
            [
                "<b>Amplitude:</b> rest position to crest = <b>6 cm</b> (0.06 m). Not 12 cm, which is crest to trough.",
                "<b>Wavelength:</b> crest to next crest = <b>24 cm</b> (0.24 m).",
            ],
        ),
        practice("Wave words", [
            written("wv-n2-q1", "State what is meant by the amplitude of a wave. (1)",
                    marks(["The <b>maximum displacement</b> of a point on the wave from its <b>undisturbed (rest) position</b>."]), lines=2),
            written("wv-n2-q2", "State what is meant by the frequency of a wave, and give its unit. (2)",
                    marks(["The <b>number of waves passing a point each second</b>.", "Unit: <b>hertz, Hz</b>."]), lines=2),
            choice("wv-n2-q3", "On a wave diagram the distance from a crest to the next trough is 10 cm. What is the wavelength?",
                   ["10 cm", "20 cm", "5 cm", "40 cm"], 1,
                   "Crest to trough is half a wavelength; crest to the next crest is 20 cm."),
            choice("wv-n2-q4", "A sound is made louder without changing its pitch. What has changed?",
                   ["The frequency", "The amplitude", "The wavelength", "The speed"], 1,
                   "Loudness goes with amplitude; pitch goes with frequency."),
            written("wv-n2-q5", "State what is meant by the period of a wave. (1)",
                    marks(["The <b>time taken for one complete wave</b> (one full oscillation) to pass a point."]), lines=2),
            written("wv-n2-q6", "State what is meant by a wavefront. (1)",
                    marks(["A line joining all the points (across the wave) that are at the <b>same stage</b> of their oscillation — e.g. along one crest; the wave travels at right angles to it."]), lines=2),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N3 · Transverse and longitudinal
# ---------------------------------------------------------------------

section_n3 = section(
    "transverse-longitudinal", "nn", "Transverse and longitudinal waves", "4.5",
    equations=[r"\text{transverse: oscillations} \perp \text{direction of travel}", r"\text{longitudinal: oscillations} \parallel \text{direction of travel}"],
    blurb="Two kinds of wave, told apart by the direction of the oscillations compared with the direction the wave travels. Sound is longitudinal; light and all EM waves are transverse; water-surface waves are transverse; earthquakes send out both.",
    checklist=[
        "Define transverse and longitudinal waves in terms of the direction of oscillation",
        "Give the examples: sound (L), electromagnetic (T), water surface (T), seismic P (L) and S (T)",
        "Use the words compression and rarefaction for a longitudinal wave",
    ],
    parts=[
        explain(
            "The two kinds",
            diagram(dg.longitudinal_svg(), 480, 250, "A longitudinal wave on a slinky: the coils oscillate back and forth along the direction of travel, making compressions (bunched) and rarefactions (spread out). The wavelength is compression to compression.") +
            "<p><b>Transverse:</b> the oscillations (vibrations) are <b>at right angles (perpendicular) to the direction of energy transfer</b>. Examples: <b>all electromagnetic waves</b> (light, radio…), <b>water surface waves</b> (ripples), waves on a string, seismic <b>S</b> waves.</p>"
            "<p><b>Longitudinal:</b> the oscillations are <b>parallel to the direction of energy transfer</b>. The medium is squashed into <b>compressions</b> and stretched into <b>rarefactions</b>. Examples: <b>sound</b> (and ultrasound and infrasound), seismic <b>P</b> waves. A slinky is a demonstration, not an exam example — June 2025 Q3(b)(i) ignored \"waves on a spring\", and ignored \"seismic\" when the question was already about an earthquake wave; for a transverse example give an <b>electromagnetic wave</b>, <b>water ripples</b> or <b>waves on a string</b>.</p>"
            "<p>The mark-scheme words (June 2025 Q3(b)(ii)): \"vibrate/oscillate (1) <b>perpendicular / at right angles to (the direction of travel of) the wave</b> (1)\". Say <i>oscillates</i> or <i>vibrates</i> (\"up and down\" or \"back and forth\" is accepted for that mark), and always say which direction that is compared with — the <b>second mark is the comparison</b>, and it is the one students drop.</p>"
            "<p>All <b>mechanical</b> waves — sound, water, seismic, waves on a string, whichever kind — need a <b>medium</b> to travel through; sound cannot cross a vacuum. Electromagnetic waves are the exception: they need no medium.</p>",
        ),
        worked(
            "Explaining the difference",
            "Explain the difference between a transverse wave and a longitudinal wave, giving an example of each. (3 marks)",
            [
                "<b>Transverse:</b> the oscillations are <b>at right angles to the direction the wave travels</b> — e.g. light / water surface waves.",
                "<b>Longitudinal:</b> the oscillations are <b>parallel to the direction the wave travels</b>, producing compressions and rarefactions — e.g. sound.",
                "<b>Examples named</b> correctly for both (third mark).",
            ],
        ),
        practice("Transverse and longitudinal", [
            choice("wv-n3-q1", "Which of these is a longitudinal wave?",
                   ["Light", "Sound", "A water ripple", "A radio wave"], 1,
                   "Sound is longitudinal; the others are transverse."),
            written("wv-n3-q2", "Describe how the particles of air move as a sound wave passes. (2)",
                    marks(["They <b>oscillate (vibrate) back and forth</b> about a fixed position…", "…<b>parallel to the direction</b> the sound travels, forming compressions and rarefactions."]), lines=3),
            written("wv-n3-q3", "An earthquake produces P waves and S waves. State which is longitudinal and which is transverse. (2)",
                    marks(["P waves: <b>longitudinal</b>.", "S waves: <b>transverse</b>."]), lines=2),
            written("wv-n3-q4", "A rock is in the path of a seismic S wave. Describe how the rock moves. (2)",
                    marks(["It <b>oscillates (vibrates)</b>…", "…<b>perpendicular (at right angles) to the direction the wave travels</b> (S waves are transverse)."]), lines=3),
            choice("wv-n3-q5", "What is a compression in a sound wave?",
                   ["A region where the air particles are closer together (higher pressure)", "A region where the air particles are further apart", "The top of the wave", "The speed of the wave"], 0,
                   "Compression = particles bunched; rarefaction = particles spread out."),
            written("wv-n3-q6", "Explain why sound cannot travel through a vacuum but light can. (2)",
                    marks(["Sound is a <b>longitudinal</b> wave that needs <b>particles to oscillate</b> (a medium to compress); a vacuum has none.",
                           "Light is an <b>electromagnetic</b> wave that <b>does not need a medium</b>."]), lines=3),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N4 · The wave equations
# ---------------------------------------------------------------------

q4_1 = 330 / 0.011

section_n4 = section(
    "wave-equations", "nn", "The wave equations: v = fλ and v = x/t", "4.6",
    equations=[r"v = f \times \lambda", r"v = \dfrac{x}{t}"],
    blurb="Two equations, both on the list, both for every kind of wave. The first links speed to how often and how long; the second is just speed = distance ÷ time.",
    checklist=[
        "Select $v = f\\lambda$ and $v = x/t$ and say what each symbol is, with units",
        "Convert kHz, MHz, mm and cm before substituting",
        "Rearrange both equations",
    ],
    parts=[
        explain(
            "Two equations for all waves",
            "<p>$$v = f \\times \\lambda \\qquad\\qquad v = \\dfrac{x}{t}$$</p>"
            "<table class='tbl'><tr><th>Symbol</th><th>Quantity</th><th>Unit</th></tr>"
            "<tr><td>$v$</td><td>wave speed (velocity)</td><td>m/s</td></tr>"
            "<tr><td>$f$</td><td>frequency</td><td>Hz</td></tr>"
            "<tr><td>$\\lambda$</td><td>wavelength</td><td>m</td></tr>"
            "<tr><td>$x$</td><td>distance travelled</td><td>m</td></tr>"
            "<tr><td>$t$</td><td>time taken</td><td>s</td></tr></table>"
            "<p>Why $v = f\\lambda$ works: $f$ waves pass each second and each is $\\lambda$ long, so the front of the wave moves $f \\times \\lambda$ metres every second.</p>"
            "<p><b>Typical speeds:</b> sound in air about <b>340 m/s</b> (330 is also used), sound in water about 1500 m/s, light and all EM waves <b>3 × 10⁸ m/s</b>, ripples in a tank a few tens of cm/s.</p>"
            "<p>The June 2023 scheme (Q1(a)): $f = 330 \\div 0.011 = 30\\,000$ Hz; 30, 300 or 3000 (a power-of-ten slip from the 11 mm) got one mark of two. Convert first, substitute into the original equation, then rearrange — the 2022 report: \"substitute in the original equation to be sure of getting a mark for this\".</p>",
        ),
        worked(
            "Frequency from wavelength",
            "A bat's call travels at 330 m/s and has a wavelength of 11 mm. Calculate its frequency.",
            [r"<b>Convert:</b> $11\ \text{mm} = 0.011$ m."] + ewau(r"v = f \times \lambda \;\Rightarrow\; f = \dfrac{v}{\lambda}", r"f = \dfrac{330}{0.011}", "30\\,000", "Hz"),
        ),
        practice("Wave equations", [
            numeric("wv-n4-q1", "A bat's call has speed 330 m/s and wavelength 11 mm. Calculate its frequency.", q4_1, "Hz",
                    "11 mm = 0.011 m; $f = v \\div \\lambda$.",
                    ewau(r"f = \dfrac{v}{\lambda}", r"f = \dfrac{330}{0.011}", "30\\,000", "Hz")),
            numeric("wv-n4-q2", "Ultrasound of frequency 1.5 MHz travels through water at 1500 m/s. Calculate its wavelength.", 1500 / 1.5e6, "m",
                    "1.5 MHz = 1.5 × 10⁶ Hz; $\\lambda = v \\div f$. Type 0.001.",
                    ewau(r"\lambda = \dfrac{v}{f}", r"\lambda = \dfrac{1500}{1.5 \times 10^{6}}", "0.001", "m (1 mm)")),
            numeric("wv-n4-q3", "Thunder is heard 4.0 s after the lightning. Sound travels at 340 m/s. Calculate the distance to the storm.", 340 * 4.0, "m",
                    "$x = v \\times t$.",
                    ewau(r"v = \dfrac{x}{t} \;\Rightarrow\; x = v \times t", r"x = 340 \times 4.0", "1360", "m")),
            numeric("wv-n4-q4", "Water waves in a tank have a frequency of 5 Hz and a wavelength of 4 cm. Calculate their speed.", 5 * 0.04, "m/s",
                    "4 cm = 0.04 m.",
                    ewau(r"v = f \times \lambda", r"v = 5 \times 0.04", "0.2", "m/s")),
            numeric("wv-n4-q5", "A sound wave travels 1700 m across a lake in 5.0 s. Calculate its speed.", 1700 / 5, "m/s",
                    "$v = x \\div t$.",
                    ewau(r"v = \dfrac{x}{t}", r"v = \dfrac{1700}{5.0}", "340", "m/s")),
            numeric("wv-n4-q6", "A radio wave has a frequency of 200 kHz. Calculate its wavelength. ($v = 3 \\times 10^8$ m/s)", 3e8 / 200e3, "m",
                    "200 kHz = 2 × 10⁵ Hz.",
                    ewau(r"\lambda = \dfrac{v}{f}", r"\lambda = \dfrac{3 \times 10^{8}}{2 \times 10^{5}}", "1500", "m")),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N5 · Period and frequency
# ---------------------------------------------------------------------

section_n5 = section(
    "period-nn", "nn", "Period and frequency", "4.4",
    equations=[r"T = \dfrac{1}{f}", r"f = \dfrac{1}{T}", r"f = \dfrac{\text{number of waves}}{\text{time}}"],
    blurb="Period is the time for one wave; frequency is waves per second. Each is one divided by the other — a 50 Hz wave has a period of 0.02 s.",
    checklist=[
        "Use $T = 1/f$ and $f = 1/T$",
        "Find a frequency by counting waves in a measured time",
        "Read the period from a displacement–time graph",
    ],
    parts=[
        explain(
            "One over the other",
            "<p>$$T = \\dfrac{1}{f} \\qquad f = \\dfrac{1}{T}$$</p>"
            "<p>If 50 waves pass each second ($f = 50$ Hz), each one takes $1/50 = 0.02$ s: that is the <b>period</b>. If a pendulum takes 2 s per swing ($T = 2$ s), its frequency is $1/2 = 0.5$ Hz.</p>"
            "<p><b>Counting method:</b> $f = \\dfrac{\\text{number of waves}}{\\text{time taken}}$ — count the ripples passing a point in 10 s (or the oscillations of a vibrating ruler) and divide. Counting for a longer time makes the frequency more accurate.</p>"
            "<p>On a <b>displacement–time</b> graph the period is the time from one crest to the next; on a <b>displacement–distance</b> graph the same gap is the wavelength. Check which axis is which before you read anything off (T1).</p>",
        ),
        worked(
            "Period from frequency",
            "A loudspeaker vibrates at 250 Hz. Calculate the period of the sound wave.",
            ewau(r"T = \dfrac{1}{f}", r"T = \dfrac{1}{250}", "0.004", "s (4 ms)"),
        ),
        practice("Period and frequency", [
            numeric("wv-n5-q1", "A wave has a frequency of 250 Hz. Calculate its period.", 1 / 250, "s", "$T = 1 \\div f$.",
                    ewau(r"T = \dfrac{1}{f}", r"T = \dfrac{1}{250}", "0.004", "s")),
            numeric("wv-n5-q2", "A pendulum takes 0.8 s for one complete swing. Calculate its frequency.", 1 / 0.8, "Hz", "$f = 1 \\div T$.",
                    ewau(r"f = \dfrac{1}{T}", r"f = \dfrac{1}{0.8}", "1.25", "Hz")),
            numeric("wv-n5-q3", "A student counts 24 ripples passing a mark in 8.0 s. Calculate the frequency of the ripples.", 24 / 8, "Hz", "Waves ÷ time.",
                    ewau(r"f = \dfrac{\text{number of waves}}{\text{time}}", r"f = \dfrac{24}{8.0}", "3", "Hz")),
            numeric("wv-n5-q4", "The UK mains supply has a frequency of 50 Hz. Calculate its period in milliseconds.", 1000 / 50, "ms", "$T = 1/50$ s, then × 1000.",
                    [r"$T = \dfrac{1}{50} = 0.02$ s $= 20$ ms."]),
            choice("wv-n5-q5", "A wave's period is doubled. What happens to its frequency?",
                   ["It doubles", "It halves", "It stays the same", "It quadruples"], 1,
                   "$f = 1/T$: doubling T halves f."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N6 · Measuring wave speed
# ---------------------------------------------------------------------

section_n6 = section(
    "measuring-wave-speed", "nn", "Measuring the speed of sound and of ripples", "4.7",
    equations=[r"v = \dfrac{x}{t}", r"v = f \times \lambda"],
    blurb="Two methods the spec names: the speed of sound in air, and the speed of ripples on water. Each is either \"time it over a known distance\" or \"measure f and λ, multiply\".",
    checklist=[
        "Describe a method for measuring the speed of sound in air",
        "Describe how to find the speed of ripples in a tank (two ways)",
        "Give an improvement <b>and its effect</b> — \"more accurate\" alone is not accepted",
    ],
    parts=[
        explain(
            "Sound in air",
            "<p><b>Method A — a long distance and a stopwatch.</b> Two people stand a measured distance apart (100 m or more, by trundle wheel). One bangs cymbals (or fires a starting pistol); the other starts the stopwatch when they <b>see</b> the bang and stops it when they <b>hear</b> it. Speed = distance ÷ time. Light arrives almost instantly, so the time measured is the sound's travel time.</p>"
            "<p>The problem is <b>reaction time</b> (about 0.2 s) compared with a travel time of about 0.3 s over 100 m. The June 2023 scheme (Q6(a)) had candidates work out that 0.23 s of reaction time was 63% of the 0.364 s travel time over 120 m, and the improvement asked for was <b>increase the distance</b> — a longer time makes the reaction time a smaller fraction. Repeating and averaging helps too.</p>"
            "<p><b>Method B — two microphones.</b> Connect two microphones, a measured distance apart, to a data logger or oscilloscope; make a sharp sound in line with them; the logger records the <b>time between</b> the sound reaching the first and the second microphone. Speed = separation ÷ time delay. No reaction time, so the timing is far better — but in an exam always write the improvement <b>with its effect</b>: \"use microphones and a data logger <b>to remove reaction time</b>\" or \"use a longer distance <b>so the time is longer and reaction time is a smaller fraction of it</b>\". June 2019 Q6(a): \"do not accept 'more accurate' without qualification\"; Nov 2020 Q6(a)(iii) gave the second mark only \"with effect\".</p>"
            "<p><b>Method C — echoes:</b> stand a measured distance from a large wall and clap in time with the echoes; time 20 claps, divide for the time of one round trip, and speed = 2 × distance ÷ time.</p>",
        ),
        explain(
            "Ripples in a tank",
            "<p>A <b>ripple tank</b>: a shallow tray of water, a <b>vibrating bar (dipper)</b> driven by a motor or signal generator makes straight ripples, and a <b>lamp above</b> casts the wave pattern as light and dark lines on a screen or paper below (the crests focus the light into bright lines).</p>"
            "<p><b>Way 1 — time a crest:</b> mark two points a measured distance apart on the screen and <b>time a crest</b> travelling between them (or time it crossing the whole tank); $v = x/t$. Better: time it over a longer distance, or film it and use the frame rate.</p>"
            "<p><b>Way 2 — f and λ:</b> read the <b>frequency</b> off the signal generator (or count waves passing a point in 10 s and divide); measure the <b>wavelength</b> by photographing the pattern with a ruler beside it, or by measuring the distance across <b>ten</b> wavelengths and dividing by ten (one gap is too small to measure accurately); then $v = f \\lambda$. A <b>stroboscope</b> flashing at the wave's frequency \"freezes\" the pattern so the wavelength can be measured.</p>"
            "<p>June 2025 Q3(a)(iii) gave two marks for either way: \"time a wave crest over a known distance, then speed = distance ÷ time\" or \"count the number of waves in a specified time (to calculate frequency) then use $v = f \\times \\lambda$\".</p>",
        ),
        worked(
            "Speed of ripples",
            "In a ripple tank the dipper vibrates at 6 Hz. A student measures the distance across 10 wavelengths on the screen as 30 cm. Calculate the speed of the ripples.",
            [r"<b>Wavelength:</b> $\lambda = \dfrac{30}{10} = 3$ cm $= 0.03$ m (ten gaps measured, then divided — more accurate than one)."] + ewau(r"v = f \times \lambda", r"v = 6 \times 0.03", "0.18", "m/s"),
        ),
        practice("Measuring wave speed", [
            written("wv-n6-q1", "Describe how two students could measure the speed of sound in air using a stopwatch. (4)",
                    mark_scheme([
                        ("Distance", "Stand a <b>large measured distance</b> apart (e.g. 100 m, measured with a trundle wheel / tape)."),
                        ("Signal", "One makes a loud sharp sound (cymbals / starting pistol) that the other can <b>see</b> being made."),
                        ("Time", "The other <b>starts the stopwatch on seeing it and stops on hearing it</b>."),
                        ("Calculate", "<b>Speed = distance ÷ time</b>; repeat and calculate a mean."),
                    ]), lines=5),
            choice("wv-n6-q2", "Why does standing further apart improve the stopwatch method for the speed of sound?",
                   ["Sound travels faster over long distances", "The travel time is longer, so the reaction time is a smaller fraction of it", "The sound is louder", "The stopwatch is more accurate"], 1,
                   "Reaction time is fixed (~0.2 s); a longer travel time makes its percentage effect smaller."),
            written("wv-n6-q3", "Describe how a student could measure the wavelength of ripples in a ripple tank accurately. (2)",
                    marks(["Measure the distance across <b>several wavelengths</b> (e.g. 10) on the screen (or a photo with a ruler in it)…",
                           "…and <b>divide by the number</b> of wavelengths — or freeze the pattern with a <b>stroboscope</b> first."]), lines=3),
            written("wv-n6-q4", "Describe two different methods of finding the speed of water waves in a ripple tank. (4)",
                    mark_scheme([
                        ("Method 1", "<b>Time a crest</b> travelling a <b>measured distance</b> (two marks on the screen / across the tank)…"),
                        ("…", "…and use <b>speed = distance ÷ time</b>."),
                        ("Method 2", "Find the <b>frequency</b> by <b>counting the waves passing a point in a measured time</b> (say 10 s — not \"one second\") and dividing; find the <b>wavelength</b> (several wavelengths ÷ number)… \"Measure the frequency\" on its own scores nothing (June 2025 Q3(a)(iii)); read it from the signal generator only if the question gives you one."),
                        ("…", "…and use <b>$v = f \\times \\lambda$</b>."),
                    ]), lines=5),
            numeric("wv-n6-q5", "Two microphones 1.7 m apart are connected to a data logger. A clap reaches the second microphone 5.0 ms after the first. Calculate the speed of sound.", 1.7 / 0.005, "m/s",
                    "5.0 ms = 0.005 s; $v = x \\div t$.",
                    ewau(r"v = \dfrac{x}{t}", r"v = \dfrac{1.7}{0.0050}", "340", "m/s")),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N7 · Waves at a boundary
# ---------------------------------------------------------------------

section_n7 = section(
    "boundaries", "nn", "Waves at a boundary: reflected, refracted, transmitted, absorbed", "4.9P, 4.10, 4.11",
    equations=[r"\text{reflected / refracted / transmitted / absorbed}", r"\text{refraction: direction changes because speed changes}"],
    blurb="When a wave meets the boundary between two materials, four things can happen, usually more than one at once. Which dominates depends on the materials and on the wavelength.",
    checklist=[
        "Describe the four effects at an interface and give an example of each",
        "State which way a wave refracts when it slows down or speeds up",
        "Give an example of absorption or reflection that depends on wavelength",
    ],
    parts=[
        explain(
            "The four effects",
            "<table class='tbl'><tr><th>Effect</th><th>What happens</th><th>Example</th></tr>"
            "<tr><td><b>Reflection</b></td><td>the wave bounces back off the boundary (angle of incidence = angle of reflection)</td><td>echoes; a mirror; sonar</td></tr>"
            "<tr><td><b>Refraction</b></td><td>the wave crosses the boundary and <b>changes direction</b> because its <b>speed changes</b></td><td>light into glass; ripples into shallow water; sound into warmer air</td></tr>"
            "<tr><td><b>Transmission</b></td><td>the wave passes through the material</td><td>light through a window; radio through walls</td></tr>"
            "<tr><td><b>Absorption</b></td><td>the wave's energy is taken in by the material (usually warming it)</td><td>microwaves by water in food; sound by curtains and carpet</td></tr></table>"
            "<p><b>Refraction direction:</b> a wave that <b>slows down</b> on crossing a boundary bends <b>towards the normal</b>; one that <b>speeds up</b> bends <b>away</b> from it. Light slows in glass and water; sound <i>speeds up</i> in water; ripples slow in shallow water. The frequency never changes (T3).</p>"
            "<p><b>It depends on wavelength:</b> glass transmits visible light but absorbs most ultraviolet; carpet absorbs high-frequency sound better than low; a thick wall reflects or absorbs high frequencies but lets the bass through. June 2024 Q10(c): carpets and curtains <b>absorb</b> more of the sound, so <b>less is reflected</b> back into the room; wooden floors and painted walls <b>reflect</b> it — \"echoes / bounces around\" was accepted for reflection.</p>",
        ),
        worked(
            "Which effect?",
            "A room with wooden floors and bare walls sounds echoey; adding carpets and curtains makes it quieter. Explain why. (2 marks)",
            [
                "<b>Carpets and curtains:</b> they <b>absorb</b> a larger fraction of the sound that hits them (soft, fibrous materials).",
                "<b>So:</b> <b>less sound is reflected</b> back into the room; the bare wood and paint <b>reflect</b> most of it, which is what you hear as echoes.",
            ],
        ),
        practice("Boundaries", [
            choice("wv-n7-q1", "Sound travels from air into water, where it moves faster. Which way does it refract?",
                   ["Towards the normal", "Away from the normal", "It does not change direction", "It reflects back"], 1,
                   "Speeding up → away from the normal (opposite to light into water)."),
            written("wv-n7-q2", "State the four things that can happen to a wave when it reaches the boundary between two materials. (2)",
                    marks(["<b>Reflection</b> and <b>refraction</b>…", "…<b>transmission</b> and <b>absorption</b>."]), lines=2),
            written("wv-n7-q3", "Explain why a wave changes direction when it is refracted. (1)",
                    marks(["Its <b>speed changes</b> as it crosses the boundary (and it meets the boundary at an angle), so the wavefront turns."]), lines=2),
            written("wv-n7-q4", "A studio wall is covered in foam. Explain why. (2)",
                    marks(["The foam <b>absorbs</b> sound (its energy is transferred to the foam's thermal store)…", "…so <b>less is reflected</b> and there are fewer echoes in the recording."]), lines=3),
            choice("wv-n7-q5", "Which is an example of transmission?",
                   ["An echo from a cliff", "Light passing through a window", "A black surface warming in sunlight", "A ripple bending in shallow water"], 1,
                   "Through = transmission; echo = reflection; warming = absorption; bending = refraction."),
            written("wv-n7-q6", "Give one example of a material that transmits one wavelength of electromagnetic wave but absorbs another. (1)",
                    marks(["<b>Glass</b> transmits visible light but absorbs most <b>ultraviolet</b> (or: the atmosphere transmits visible and radio but absorbs X-rays; water transmits light but absorbs microwaves)."]), lines=2),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N8 · Sound, the ear, ultrasound, infrasound (H, P)
# ---------------------------------------------------------------------

section_n8 = section(
    "sound-ear", "nn", "Sound, the ear, ultrasound and infrasound", "4.12P, 4.13P, 4.14P, 4.15P",
    equations=[r"\text{hearing: } 20\ \text{Hz} \text{ to } 20\,000\ \text{Hz}", r"\text{ultrasound} > 20\,000\ \text{Hz}", r"\text{infrasound} < 20\ \text{Hz}"],
    blurb="Sound is a vibration passed from the air to a solid — the eardrum — and the ear only works for a limited range of frequencies. Above that range is ultrasound; below it, infrasound.",
    tags=["H", "P"],
    checklist=[
        "Recall the range of human hearing and the definitions of ultrasound and infrasound",
        "Describe how a sound wave is converted to vibrations in a solid (the eardrum) and why it only works over a limited frequency range",
        "Give the spec uses of ultrasound and infrasound",
    ],
    parts=[
        explain(
            "Numbers and the ear",
            "<p><b>Human hearing:</b> about <b>20 Hz to 20 000 Hz</b> (20 kHz). <b>Ultrasound</b> is sound with a frequency <b>above 20 000 Hz</b>; <b>infrasound</b> is sound with a frequency <b>below 20 Hz</b>. Both are longitudinal, like all sound; we just cannot hear them.</p>"
            "<p><b>Sound → vibrations in a solid:</b> the compressions and rarefactions of a sound wave push and pull on a solid surface, making it <b>vibrate at the same frequency</b>. In the ear: the sound makes the <b>eardrum</b> vibrate; the eardrum passes the vibration to the <b>small bones</b> (ossicles), which pass it to the fluid in the <b>cochlea</b>, where hair cells turn it into nerve signals. A microphone's diaphragm works the same way; a loudspeaker does it in reverse.</p>"
            "<p><b>Why only a limited range:</b> a solid (the eardrum, a diaphragm) can only be made to vibrate efficiently over a <b>limited range of frequencies</b> — its size, mass and stiffness set what it responds to. Very low frequencies do not make the eardrum move enough to be detected; very high frequencies it cannot follow. So we hear nothing below 20 Hz or above 20 kHz (and the upper limit falls with age). June 2025 Q1(c): why infrasound is not heard — either \"the <b>frequency is too low</b>\" or \"the <b>eardrum</b> (named part) does not vibrate / respond at that frequency\" — scored; describing ultrasound by mistake did not. \"<b>Below 20 Hz</b>\" on its own was worth both marks, and the named-part route needs the <b>effect</b> (\"the eardrum cannot vibrate / is too stiff at that frequency\").</p>",
        ),
        explain(
            "Uses of ultrasound and infrasound",
            "<table class='tbl'><tr><th>Use</th><th>How it works</th></tr>"
            "<tr><td><b>Sonar</b> (ships, fishing boats)</td><td>a pulse of ultrasound is sent down; it <b>reflects</b> off the sea bed (or a shoal); the <b>time</b> for the echo is measured; distance = speed × time ÷ 2 (T4)</td></tr>"
            "<tr><td><b>Foetal (pre-natal) scanning</b></td><td>ultrasound pulses from a probe reflect at the <b>boundaries between tissues</b> (different densities); the times and strengths of the echoes build an image; no ionising radiation, so safe for the baby</td></tr>"
            "<tr><td><b>Exploring the Earth's core</b> (infrasound / seismic waves)</td><td>earthquakes produce low-frequency P and S waves; detecting where each type arrives shows the core is partly liquid and the Earth's density changes with depth (T5)</td></tr>"
            "<tr><td>Also: industrial cleaning, detecting cracks in metal (an echo returns early from the crack — 2022 Q10(b))</td><td></td></tr></table>",
        ),
        worked(
            "Why we cannot hear infrasound",
            "Elephants communicate with infrasound. Explain why a person standing nearby cannot hear it. (2 marks)",
            [
                "<b>Frequency:</b> infrasound has a frequency <b>below 20 Hz</b>, which is below the range the human ear detects (20 Hz – 20 kHz).",
                "<b>The ear:</b> the <b>eardrum does not vibrate</b> enough at such a low frequency to pass the vibration on, so no signal reaches the brain.",
            ],
        ),
        practice("Sound and the ear", [
            written("wv-n8-q1", "State what is meant by ultrasound, and give the range of frequencies humans can hear. (2)",
                    marks(["Sound with a frequency <b>greater than 20 000 Hz</b>.", "Human hearing: about <b>20 Hz to 20 000 Hz</b>."]), lines=2),
            written("wv-n8-q2", "Describe how a sound wave in the air makes the eardrum vibrate. (2)",
                    marks(["The <b>compressions and rarefactions</b> of the sound wave reach the eardrum and push and pull on it (pressure changes)…",
                           "…so the eardrum <b>vibrates at the same frequency</b> as the sound; the vibration is passed on to the small bones and then the cochlea."]), lines=3),
            written("wv-n8-q3", "Explain why the human ear can only detect a limited range of frequencies. (2)",
                    marks(["The eardrum (a solid) can only be made to <b>vibrate efficiently over a limited range of frequencies</b> — its size and stiffness set what it responds to.",
                           "At very low or very high frequencies it <b>does not vibrate enough</b> to pass on a signal, so those sounds are not detected."]), lines=3),
            choice("wv-n8-q4", "Which is a use of infrasound?",
                   ["Foetal scanning", "Sonar", "Studying the Earth's core with seismic waves", "Cleaning jewellery"], 2,
                   "Seismic waves are low-frequency; the others use ultrasound."),
            written("wv-n8-q5", "Explain why ultrasound rather than X-rays is used to scan an unborn baby. (2)",
                    marks(["Ultrasound is <b>not ionising</b>, so it does not damage the baby's cells; X-rays could cause mutations.",
                           "Ultrasound is <b>reflected at the boundaries between different tissues</b>, so the echoes can build an image of the soft tissue of the baby."]), lines=3),
            choice("wv-n8-q6", "A whistle produces a sound of 25 kHz. Why can a dog hear it but a person cannot?",
                   ["It is too quiet for people", "25 kHz is above the human hearing range (ultrasound) but within the dog's", "Dogs have bigger ears", "It is infrasound"], 1,
                   "25 000 Hz > 20 000 Hz: ultrasound to us, audible to a dog."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N9 · Key words
# ---------------------------------------------------------------------

DEFINITIONS = [
    ("Amplitude", "The <b>maximum displacement</b> of a point on the wave from its <b>undisturbed position</b>.", "crest to trough"),
    ("Wavelength", "The distance from a point on one wave to the <b>same point on the next wave</b> (crest to crest).", "\"the length of a wave\""),
    ("Frequency", "The <b>number of waves passing a point per second</b>; unit hertz (Hz).", "\"how fast the wave is\""),
    ("Period", "The <b>time for one complete wave</b> (one oscillation) to pass a point; unit s.", "\"how long the wave lasts\""),
    ("Wave speed (velocity)", "The speed at which the <b>wave (the energy) travels</b> through the medium.", "the speed of the particles"),
    ("Wavefront", "A line joining points on the wave that are at the <b>same stage</b> of oscillation (e.g. all crests).", "\"the front of the wave\""),
    ("Transverse wave", "Oscillations <b>perpendicular</b> to the direction of energy transfer (light, water surface, S waves).", "\"a wave that goes up and down\" with no direction compared"),
    ("Longitudinal wave", "Oscillations <b>parallel</b> to the direction of energy transfer, with compressions and rarefactions (sound, P waves).", "\"a wave that goes along\""),
    ("Compression", "A region of a longitudinal wave where the particles are <b>closer together</b> (higher pressure).", "\"the crest\""),
    ("Rarefaction", "A region of a longitudinal wave where the particles are <b>further apart</b> (lower pressure).", "\"the trough\""),
    ("Reflection", "A wave <b>bouncing back</b> from a boundary.", "\"the wave stops\""),
    ("Refraction", "A wave <b>changing direction</b> at a boundary because its <b>speed changes</b>.", "\"the wave bends\" with no cause"),
    ("Transmission", "A wave <b>passing through</b> a material.", "\"sending a signal\""),
    ("Absorption", "A wave's <b>energy being taken in</b> by a material (transferred to its thermal store).", "\"the wave disappears\""),
    ("Ultrasound", "Sound with a frequency <b>above 20 000 Hz</b> (above the range of human hearing).", "\"very loud sound\""),
    ("Infrasound", "Sound with a frequency <b>below 20 Hz</b>.", "\"very quiet sound\""),
    ("Echo", "A <b>reflected</b> sound wave heard after the original.", "\"a repeated sound\""),
]


def definitions_table():
    html = "<table class='tbl'><tr><th>Term</th><th>What to write (mark-scheme form)</th><th>Not this</th></tr>"
    for term, definition, wrong in DEFINITIONS:
        html += "<tr><td><b>" + term + "</b></td><td>" + definition + "</td><td>" + wrong + "</td></tr>"
    html += "</table>"
    return html


section_keywords = section(
    "keywords-waves", "nn", "Key words: state what is meant by…", "4",
    equations=[r"\text{definition, word for word}"],
    blurb="One-mark definitions in the form of words the mark schemes credit. The bold words are the ones the marks are attached to.",
    checklist=[
        "Define amplitude, wavelength, frequency, period and wavefront",
        "Define transverse and longitudinal, compression and rarefaction",
        "Define reflection, refraction, transmission, absorption, ultrasound and infrasound",
    ],
    parts=[
        explain("The definitions", "<p>\"<b>State what is meant by</b>\" asks for the definition. Learn these as sentences.</p>" + definitions_table()),
        practice("Key words", [
            written("wv-kw-q1", "State what is meant by the wavelength of a wave. (1)",
                    marks(["The distance from a point on one wave to the <b>same point on the next wave</b> (e.g. crest to crest)."]), lines=2),
            written("wv-kw-q2", "State what is meant by a longitudinal wave. (1)",
                    marks(["A wave in which the <b>oscillations are parallel to the direction of energy transfer</b>."]), lines=2),
            written("wv-kw-q3", "State what is meant by infrasound. (1)",
                    marks(["Sound with a frequency <b>below 20 Hz</b>."]), lines=2, tags=["H", "P"]),
            choice("wv-kw-q4", "Which is the correct definition of amplitude?",
                   ["The distance from a crest to a trough", "The maximum displacement from the undisturbed position", "The height of the wave", "The distance between two crests"], 1,
                   "Amplitude is rest position to crest (or trough), half of crest-to-trough."),
            written("wv-kw-q5", "State what is meant by the period of a wave, and give its unit. (2)",
                    marks(["The <b>time for one complete wave</b> to pass a point.", "Unit: <b>seconds, s</b>."]), lines=2),
            written("wv-kw-q6", "State what is meant by refraction. (1)",
                    marks(["A wave <b>changing direction</b> as it crosses a boundary, because its <b>speed changes</b>."]), lines=2),
            choice("wv-kw-q7", "\"The frequency is how fast the wave moves.\" What is wrong with this?",
                   ["Nothing", "Frequency is the number of waves per second; how fast the wave moves is the wave speed", "Frequency is measured in metres", "Frequency is the same as wavelength"], 1,
                   "Frequency (Hz) counts waves per second; speed (m/s) is how far the wave travels per second."),
            written("wv-kw-q8", "State what is meant by a compression in a sound wave. (1)",
                    marks(["A region where the air particles are <b>closer together</b> (squashed, higher pressure)."]), lines=2),
        ]),
    ],
)

FACTS_KW = [fact("State what is meant by: " + term.lower() + ".", definition, "sound-ear" if term in ("Ultrasound", "Infrasound") else "keywords-waves") for term, definition, wrong in DEFINITIONS]

SECTIONS = [section_n1, section_n2, section_n3, section_n4, section_n5, section_n6, section_n7, section_n8, section_keywords]
