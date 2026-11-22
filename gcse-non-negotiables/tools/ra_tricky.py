"""
ra_tricky.py — Topic 6 (Radioactivity): the tricky bits T1–T9 and the
flashcards.

T1 How the model of the atom changed    T6 PET scanners and tracers (P)
T2 Choosing a source                     T7 Fission and the reactor (P)
T3 Half-life the hard way                T8 Fusion (P)
T4 Contamination, irradiation, precautions  T9 Nuclear power: evaluate (P)
T5 Treating tumours (P)
"""

from revlib import (
    axis, choice, curve, data, diagram, explain, fact, graph, group, line,
    mark_scheme, marks, numeric, practice, sample, section, sf, worked, written,
)
import ra_diagrams as dg

# ---------------------------------------------------------------------
# T1 · The model of the atom
# ---------------------------------------------------------------------

section_t1 = section(
    "atomic-model", "tricky", "How and why the model of the atom changed", "6.17",
    equations=[r"\text{plum pudding} \rightarrow \text{Rutherford (nucleus)} \rightarrow \text{Bohr (orbits)}"],
    blurb="Three models, and the evidence that forced each change. The marks are for linking each observation in the alpha-scattering experiment to the conclusion drawn from it, and for saying why the model had to change.",
    checklist=[
        "Describe the plum pudding model and the Bohr model",
        "Describe the alpha-scattering experiment: the three observations and the conclusion from each",
        "Explain why each new piece of evidence changed the model",
    ],
    parts=[
        explain(
            "Three models and the evidence",
            "<p><b>1. Plum pudding (Thomson, after discovering the electron):</b> the atom is a <b>ball of positive charge</b> with <b>negative electrons dotted through it</b> like plums in a pudding. Mass and charge spread evenly.</p>"
            + diagram(dg.rutherford_svg(), 600, 260, "Rutherford's alpha-scattering experiment: alpha particles fired at thin gold foil in a vacuum. Most go straight through, a few are deflected, and very few bounce back.") +
            "<p><b>2. Rutherford's nuclear model (from Geiger and Marsden's experiment):</b></p>"
            "<table class='tbl'><tr><th>Observation</th><th>Conclusion</th></tr>"
            "<tr><td><b>most</b> alpha particles passed <b>straight through</b> the foil undeflected</td><td>the atom is <b>mostly empty space</b></td></tr>"
            "<tr><td><b>some</b> were <b>deflected</b> through small angles</td><td>the centre of the atom is <b>positively charged</b> (repels the positive alpha particles)</td></tr>"
            "<tr><td><b>very few</b> (about 1 in 8000) were <b>deflected back</b> through more than 90°</td><td>the positive charge and <b>most of the mass</b> are concentrated in a <b>tiny, dense nucleus</b></td></tr></table>"
            "<p>The plum pudding model could not explain this: if the positive charge were spread out thinly, nothing could turn an alpha particle round. So the model changed to a <b>small positive nucleus with electrons orbiting far outside it</b>. (The June 2022 scheme, Q8(b)(ii), gave a mark each for three observations — <b>most pass straight through</b>, <b>some deflected through small angles</b> (less than 90°), <b>very few through large angles</b> (more than 90°) — and three conclusions — <b>mostly empty space</b>, <b>there must be a nucleus</b>, which is <b>small / dense / positive</b>. \"Bounce back\" and \"repelled\" were allowed; \"refracted\" and anything about electrons ignored.)</p>"
            "<p><b>3. Bohr:</b> electrons orbiting freely would spiral into the nucleus, and hot gases emit light only at particular frequencies. Bohr proposed that electrons can only occupy <b>certain fixed orbits (energy levels)</b> at set distances, and move between them by absorbing or emitting fixed amounts of EM radiation. This agreed with experiment, so it replaced the free-orbit picture. Later, the nucleus was found to contain <b>protons</b> and (Chadwick, 1932) <b>neutrons</b>.</p>"
            "<p><b>The pattern for the 6-marker:</b> for each step say the <b>model</b>, the <b>evidence</b>, and <b>why</b> the evidence could not be explained by the old model.</p>",
        ),
        worked(
            "Observation to conclusion",
            "In the alpha-scattering experiment, a very small number of alpha particles were deflected straight back. Explain what this showed about the atom. (2 marks)",
            [
                "<b>Mass and charge concentrated:</b> to turn a fast, heavy alpha particle round, it must have met something with a <b>large positive charge and a large mass concentrated in a very small volume</b> — a <b>nucleus</b>.",
                "<b>Tiny:</b> because so <b>few</b> were deflected back, that nucleus must be <b>very small</b> compared with the atom — most alpha particles never came near it.",
            ],
        ),
        practice("The atomic model", [
            written("ra-t1-q1", "Describe the plum pudding model of the atom. (2)",
                    marks(["A <b>ball (sphere) of positive charge</b>…", "…with <b>negative electrons embedded</b> throughout it."]), lines=2),
            written("ra-t1-q2", "In the alpha-scattering experiment, most alpha particles passed straight through the gold foil. Explain what this showed. (1)",
                    marks(["The atom is <b>mostly empty space</b>."]), lines=2),
            written("ra-t1-q3", "Explain why the results of the alpha-scattering experiment meant the plum pudding model had to be replaced. (3)",
                    mark_scheme([
                        ("Prediction", "In the plum pudding model the positive charge is <b>spread out</b>, so alpha particles should all pass through with <b>little or no deflection</b>."),
                        ("Observation", "But <b>some were deflected through large angles</b> and a few came <b>straight back</b>."),
                        ("New model", "That needs the positive charge and most of the mass to be <b>concentrated in a tiny nucleus</b> — the nuclear model."),
                    ]), lines=4),
            written("ra-t1-q4", "Describe how the Bohr model changed the nuclear model, and why. (2)",
                    marks(["Electrons are in <b>fixed orbits (energy levels) at set distances</b> from the nucleus, and move between them by absorbing or emitting EM radiation.",
                           "Because this <b>agreed with experimental observations</b> (e.g. atoms emit light only at particular frequencies) that free orbits could not explain."]), lines=3),
            choice("ra-t1-q5", "Which observation showed that the nucleus is positively charged?",
                   ["Most alpha particles passed straight through", "Some alpha particles were deflected away from the nucleus", "The foil glowed", "Alpha particles were absorbed"], 1,
                   "Positive alpha particles repelled by a positive nucleus are deflected."),
            written("ra-t1-q6", "A student models alpha scattering by rolling marbles at a heavy weight hidden under a sheet of paper. Give two limitations of this model. (2)",
                    marks(["The marble and weight have <b>no charge</b>, so the deflection is by contact rather than electrostatic repulsion; the model is <b>not to scale</b> (the weight is far too big compared with the atom).",
                           "It is <b>two-dimensional</b> (not 3D) / there is <b>only one</b> marble and one weight / <b>all the marbles have the same speed</b>, whereas alpha particles do not (June 2022 Q8(c)(ii))."]), lines=3),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T2 · Choosing a source
# ---------------------------------------------------------------------

section_t2 = section(
    "choosing-source", "tricky", "Choosing a source: type and half-life, with reasons", "6.28, 6.30",
    equations=[r"\text{type} \leftarrow \text{penetration needed}", r"\text{half-life} \leftarrow \text{how long it must last / how soon it must be gone}"],
    blurb="\"Explain why this source is suitable\" is marked on reasons, not on naming the right source. Two reasons every time: one for the type of radiation (penetration, ionisation) and one for the half-life (long enough, short enough), each linked to the job.",
    checklist=[
        "Choose the type of radiation for a use from its penetration and ionising power, and say why",
        "Choose a half-life for a use and say why, linked to the use",
        "Explain why the danger of a source depends on its half-life",
    ],
    parts=[
        explain(
            "The two-reason answer, and the half-life trap",
            "<p><b>Type:</b> does the radiation need to get <b>out</b> of something (gamma: out of the body, through packaging, through soil)? Be <b>partly stopped</b> (beta: thickness gauge)? Stay <b>inside</b> a small space and ionise strongly (alpha: smoke alarm, internal cancer treatment)?</p>"
            "<p><b>Half-life</b> — and link it to the job, every time. The June 2022 report (kidney scan, 6-hour tracer): \"too fast / too slow\" scored nothing on its own; the credited answers were <b>\"with a 6-minute half-life the technician would not be able to take a reading (in 30 minutes)\"</b> and <b>\"with a 6-day half-life the patient would be exposed for a long time\"</b>. The June 2023 scheme (RTG on a Mars rover): \"long half-life\" + a reason — the mission lasts years, the source cannot be replaced.</p>"
            "<table class='tbl'><tr><th>Half-life</th><th>Activity behaviour</th><th>Danger (6.30)</th><th>Suits</th></tr>"
            "<tr><td><b>short</b> (minutes–days)</td><td>very active now, gone soon</td><td>high dose rate while it lasts, but it <b>does not stay</b> radioactive</td><td>medical tracers, PET, leak detection</td></tr>"
            "<tr><td><b>long</b> (years–millennia)</td><td>steady low activity for a long time</td><td>low dose rate but the hazard <b>lasts</b> — waste must be stored for thousands of years</td><td>smoke alarms, gauges, RTGs, dating</td></tr></table>"
            "<p><b>Precautions follow the half-life:</b> a short half-life source needs <b>heavy shielding and distance now</b>; a long half-life source needs <b>secure, long-term storage</b> and keeping out of the environment (contamination).</p>",
        ),
        worked(
            "A tracer",
            "Technetium-99m emits gamma rays and has a half-life of 6 hours. Explain why it is suitable as a medical tracer. (4 marks)",
            [
                "<b>Type — gets out:</b> gamma <b>penetrates</b> body tissue, so it can be <b>detected outside the body</b> by a gamma camera.",
                "<b>Type — low damage:</b> gamma is <b>weakly ionising</b>, so it does little damage to cells on its way out.",
                "<b>Half-life — long enough:</b> 6 hours gives time to <b>inject it, let it reach the organ and take the scan</b>.",
                "<b>Half-life — short enough:</b> the activity has <b>fallen to a safe level within a day or two</b>, so the patient's dose is limited.",
            ],
        ),
        practice("Choosing a source", [
            written("ra-t2-q1", "A hospital has tracers with half-lives of 6 minutes, 6 hours and 6 days. Explain why the 6-minute and 6-day sources are unsuitable for a scan that takes 30 minutes. (2)",
                    marks(["6 minutes: the activity would have <b>fallen too far for a reading to be taken</b> (five half-lives in 30 min — 1/32 left) by the time the scan is done.",
                           "6 days: the patient would be left <b>radioactive / exposed for days</b> after the scan — an unnecessarily large dose."]), lines=3),
            written("ra-t2-q2", "A radioactive source powers a space probe for a 20-year mission. Explain two properties the source should have. (2)",
                    marks(["A <b>long half-life</b>, so its activity (and power output) stays high for the whole mission — it cannot be replaced in space.",
                           "An <b>alpha</b> emitter (or one with high energy per decay), because alpha is easily absorbed to produce heating and needs little shielding; also high melting point / not chemically reactive."]), lines=3),
            choice("ra-t2-q3", "Which source would you choose to check the thickness of aluminium sheet (a few mm thick)?",
                   ["Alpha, short half-life", "Beta, long half-life", "Gamma, long half-life", "Gamma, short half-life"], 2,
                   "Beta is fully stopped by a few mm of aluminium, so gamma (partly absorbed by metal) is needed; a long half-life keeps the reading steady. For paper it would be beta."),
            written("ra-t2-q4", "Explain why a source with a short half-life can be more dangerous in the short term but less dangerous in the long term than one with a long half-life. (2)",
                    marks(["Short half-life: a <b>high activity</b> (many decays per second) at first, so a <b>high dose rate</b> now — but it soon decays away.",
                           "Long half-life: a <b>lower activity</b> now, but it <b>stays radioactive for years</b>, so the hazard (and the need to store it securely) lasts."]), lines=3),
            written("ra-t2-q5", "Explain why alpha sources are not used as medical tracers. (2)",
                    marks(["Alpha is <b>stopped by a few cm of tissue</b>, so it <b>could not be detected outside the body</b>.",
                           "It is <b>strongly ionising</b>, so inside the body it would <b>damage cells</b> near the source."]), lines=2),
            written("ra-t2-q6", "Explain the precautions needed for storing waste with a very long half-life. (2)",
                    marks(["It stays radioactive for <b>thousands of years</b>, so it must be <b>stored securely for a very long time</b> (sealed, deep underground, in stable rock).",
                           "It must be kept from <b>contaminating</b> water and soil, and shielded so it does not irradiate people."]), lines=3),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T3 · Half-life the hard way
# ---------------------------------------------------------------------

# decay graph with background: measured count = 160 e^{-t ln2 / 20} + 20 (background 20)
import math
graph_decay_bg = graph(
    axis("time in minutes", 80, 10), axis("count rate in counts per minute", 200, 20),
    [curve(sample(lambda t: 160 * math.exp(-t * math.log(2) / 20) + 20, 0, 80, 41))],
    "A measured count rate falling from 180 towards 20 counts per minute (the background) over 80 minutes.",
)

section_t3 = section(
    "half-life-hard", "tricky", "Half-life the hard way: background, graphs and working backwards", "6.27",
    equations=[r"\text{corrected count} = \text{measured} - \text{background}", r"\text{fraction left} = \dfrac{1}{2^{n}}", r"\text{ratio} = 2^{n}"],
    blurb="The harder half-life questions read a value off a graph and turn it into a percentage, ask for the original activity from a later one, count half-lives in years, or want a fraction, percentage or ratio rather than a number. (A background hidden in the graph has not been set in a Physics paper since 2018, but it is the method behind the core practical.) Each one is the same halving, with one extra step first.",
    checklist=[
        "Subtract the background before finding a half-life from a graph",
        "Work backwards from a later activity to the original",
        "Give answers as fractions, percentages or ratios of the original",
        "Read a half-life from a graph correctly (half of the corrected count, then the time)",
    ],
    parts=[
        explain(
            "The extra steps",
            "<p><b>Background in a graph.</b> A measured count rate never falls to zero — it levels off at the background. Find the background from the flat tail, <b>subtract it</b> from the starting count to get the corrected count, halve <i>that</i>, add the background back, and read the time at which the measured curve reaches it. For the graph below: measured 180, background 20, corrected 160 → half is 80 → measured 100 → at $t = 20$ min. Halving 180 to 90 gives the wrong half-life (about 24 min).</p>"
            "<p><b>Working backwards.</b> If the activity is 50 Bq after 3 half-lives, the original was $50 \\times 2^{3} = 400$ Bq. The June 2025 report (fluorine-18 curve): the common error was \"using the original mass as 60.0 mg\" — read the actual starting value off the graph.</p>"
            "<p><b>Fractions and percentages.</b> After $n$ half-lives the fraction left is $\\dfrac{1}{2^{n}}$: 1/2, 1/4, 1/8, 1/16 → 50%, 25%, 12.5%, 6.25%. The fraction that has <b>decayed</b> is 1 minus that. \"After how many half-lives is the activity below 10%?\" → 4 (6.25%). A ratio question (\"activity of A to B\") is $2^{n}$ to 1.</p>"
            "<p><b>Reading the graph in the exam:</b> draw the horizontal line at half the (corrected) value, drop a vertical to the axis, label it. The June 2024 scheme gave a mark for the horizontal line and a mark for the time — show both.</p>",
            graph=graph_decay_bg,
        ),
        worked(
            "Half-life with background",
            "The graph shows the count rate measured near a source. The background count rate is 20 counts per minute. Find the half-life of the source.",
            [
                r"<b>Corrected start:</b> measured 180 − background 20 = <b>160</b> counts/min from the source.",
                r"<b>Half of that:</b> 80 counts/min from the source, which is a <b>measured</b> count of $80 + 20 = 100$ counts/min.",
                r"<b>Read the time:</b> the curve reaches 100 counts/min at <b>$t = 20$ minutes</b>. Half-life = 20 min.",
                r"<b>Check:</b> next halving: source 40 → measured 60 at $t = 40$ min ✓",
            ],
            graph=graph_decay_bg,
        ),
        practice("Half-life the hard way", [
            numeric("ra-t3-q1", "Using the graph above (background 20 counts per minute), find the half-life of the source.", 20, "min",
                    "Subtract the background before halving.", [r"Source count 160 → 80 means measured 100, at $t = 20$ min."], graph=graph_decay_bg, tolerance=0.1),
            numeric("ra-t3-q2", "A source has a half-life of 15 years. Its activity now is 300 Bq. Calculate its activity 60 years ago.", 4800, "Bq",
                    "Four half-lives back: double four times.", [r"$60 \div 15 = 4$ half-lives; $300 \times 2^{4} = 300 \times 16 = 4800$ Bq."]),
            numeric("ra-t3-q3", "What percentage of the original undecayed nuclei remain after 4 half-lives?", 6.25, "%",
                    "1/2⁴.", [r"$\dfrac{1}{2^{4}} = \dfrac{1}{16} = 6.25\%$."]),
            numeric("ra-t3-q4", "Fluorine-18 has a half-life of 110 minutes. A sample has a mass of 48 mg at the start. Calculate the percentage remaining after 220 minutes.", 25, "%",
                    "$220 \\div 110 = 2$ half-lives → ¼.", [r"$48 \rightarrow 24 \rightarrow 12$ mg; $\dfrac{12}{48} = 25\%$."]),
            group("ra-t3-q5", "Two sources, A and B, start with the same activity. A has a half-life of 2 days, B a half-life of 8 days.", [
                numeric("ra-t3-q5a", "After 8 days, what fraction of A's original activity remains? Give it as a decimal.", 0.0625, "", "$8 \\div 2 = 4$ half-lives.", [r"$\dfrac{1}{2^{4}} = \dfrac{1}{16} = 0.0625$."], label="a", tolerance=0.02),
                numeric("ra-t3-q5b", "After 8 days, how many times greater is B's activity than A's?", 8, "", "B has had one half-life (½ left); A has 1/16 left.", [r"$\dfrac{1/2}{1/16} = 8$ times."], label="b"),
            ]),
            written("ra-t3-q6", "A student finds the half-life from a graph of measured count rate against time by halving the first reading. The graph levels off at 30 counts per minute. Explain the mistake. (2)",
                    marks(["The measured count includes the <b>background</b> (the 30 counts/min the graph levels off at), which does not decay.",
                           "The student should <b>subtract 30</b> from the readings (or halve the <b>corrected</b> count) first; halving the raw count gives a half-life that is too long."]), lines=3),
            choice("ra-t3-q7", "A source's activity falls to 1/8 of its original value in 36 hours. Its half-life is…",
                   ["4.5 hours", "12 hours", "18 hours", "36 hours"], 1,
                   "1/8 = three halvings; $36 \\div 3 = 12$ h."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T4 · Contamination, irradiation and precautions — the explain marks
# ---------------------------------------------------------------------

section_t4 = section(
    "contamination-explain", "tricky", "Contamination, irradiation and precautions: the explain marks", "6.29, 6.31, 6.32",
    equations=[r"\text{which? why? for how long? which radiation is worst?}"],
    blurb="The comparison and precaution questions are marked on specific phrases: \"does not become radioactive\", \"stops when the source is removed\", \"different kinds of precaution\". Here they are, with the reasoning behind each.",
    checklist=[
        "Compare the hazards of contamination and irradiation, saying which radiation is worst for each",
        "Explain the precautions for a named situation (lab, hospital, nuclear worker), giving different kinds",
        "Explain why patients' doses are limited and how",
    ],
    parts=[
        explain(
            "The answers that score",
            "<p><b>Irradiation vs contamination</b> — the June 2024 marks: irradiation <b>does not make the object radioactive</b>; it <b>stops when the source is removed</b> (you can move away); the <b>source is outside</b>; it <b>can be shielded</b>. Contamination: the source is <b>on or in</b> the object, which <b>keeps emitting</b> radiation, it is <b>hard to remove</b>, and it <b>cannot be shielded</b> from the inside.</p>"
            "<p><b>Which radiation is worst?</b> For irradiation from outside, <b>gamma</b> (and beta) — they penetrate to living tissue; alpha is stopped by skin. For contamination inside the body, <b>alpha</b> — all of its strongly ionising energy is absorbed by the surrounding cells. Dust and gas (radon) are the usual contaminants because they are breathed in.</p>"
            "<p><b>Precautions, by situation</b> (give <i>different kinds</i>):</p>"
            "<table class='tbl'><tr><th>Who</th><th>Precautions</th></tr>"
            "<tr><td>School lab</td><td>tongs, point the source away, lead-lined box, short exposure, no eating, wash hands</td></tr>"
            "<tr><td>Radiographer / technician</td><td>lead apron or lead screen, leave the room, limit time, film badge (dose monitored), keep distance, rotate duties</td></tr>"
            "<tr><td>Nuclear-industry worker</td><td>full protective suit and breathing apparatus against contamination, remote handling, dose monitoring, shielding</td></tr>"
            "<tr><td>Patient</td><td>lowest activity that works, short half-life, benefit outweighs risk, dose limits recorded</td></tr></table>"
            "<p><b>Why staff but not the patient?</b> The patient has one scan; the technician does many every day, so their <b>total dose</b> would otherwise be far higher. That sentence is usually a mark.</p>",
        ),
        worked(
            "Contamination from radon",
            "Radon is a radioactive gas that seeps from the ground into some houses. Explain why breathing radon is more hazardous than being near a sealed gamma source of the same activity. (3 marks)",
            [
                "<b>Contamination:</b> breathing radon puts the radioactive material <b>inside the lungs</b> — the body is contaminated, and the source stays there emitting.",
                "<b>Alpha inside:</b> radon decays by <b>alpha</b> emission, which is <b>strongly ionising</b>, so all its energy is absorbed by the lung tissue around it, damaging and mutating cells.",
                "<b>Irradiation outside:</b> the sealed gamma source only <b>irradiates</b>: gamma is weakly ionising, much passes straight through, and the exposure <b>stops when you move away</b> or shield it.",
            ],
        ),
        practice("Explain questions", [
            written("ra-t4-q1", "Explain why a radiographer leaves the room while a patient is X-rayed, but the patient does not need protecting from the same exposure. (2)",
                    marks(["The radiographer would be exposed to <b>many X-rays every day</b>, so their <b>total dose</b> (and risk of cell damage / cancer) would be high.",
                           "The patient has <b>one</b> exposure, kept to the lowest useful dose, and the <b>benefit</b> of the diagnosis outweighs the small risk."]), lines=3),
            written("ra-t4-q2", "A worker's overalls become contaminated with radioactive dust. Explain why this is more serious than the worker having been irradiated by the same source. (3)",
                    mark_scheme([
                        ("Continues", "The dust <b>keeps emitting</b> radiation, so the exposure <b>continues</b> after the worker leaves the area — irradiation would have stopped."),
                        ("Spread / inside", "The dust can be <b>breathed in or swallowed</b>, putting the source inside the body where it cannot be shielded."),
                        ("Alpha", "Inside the body even <b>alpha</b> (harmless from outside) does serious damage, as it is strongly ionising."),
                    ]), lines=4),
            choice("ra-t4-q3", "Which is the best way to protect someone from a gamma source across a room?",
                   ["Wear gloves", "A sheet of paper", "Move further away and put a lead screen between", "Hold your breath"], 2,
                   "Gamma: distance and dense shielding. Gloves protect against contamination, not irradiation."),
            written("ra-t4-q4", "Give three precautions a teacher should take when demonstrating a radioactive source in class, and say which hazard each reduces. (3)",
                    mark_scheme([
                        ("Distance", "Handle with <b>tongs</b> / keep the source at arm's length and pointed away — reduces the <b>dose from irradiation</b> (intensity falls with distance)."),
                        ("Time / shielding", "Keep it out of the <b>lead-lined box</b> for as short a time as possible — less exposure; the box <b>shields</b> it when stored."),
                        ("Contamination", "Do not <b>touch</b> the source, eat or drink; wash hands — prevents <b>contamination</b>."),
                    ]), lines=4),
            written("ra-t4-q5", "Explain why a patient given a radioactive tracer is advised to keep away from young children for a day. (2)",
                    marks(["The patient is <b>contaminated</b> — the tracer inside them keeps emitting gamma rays, so they <b>irradiate</b> people nearby.",
                           "Children's dividing cells are more at risk from radiation; after a day the short-half-life tracer has largely <b>decayed away</b>."]), lines=3),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T5 · Treating tumours (P)
# ---------------------------------------------------------------------

section_t5 = section(
    "tumours", "tricky", "Treating tumours: internal and external radiation", "6.33P",
    equations=[r"\text{external: gamma / X beams from several directions}", r"\text{internal: a source placed in the tumour (short-range, or sealed gamma)}"],
    blurb="Ionising radiation kills cells, so it can kill a tumour. From outside, beams of gamma or X-rays are aimed through the body; from inside, a small source is put into or next to the tumour. Each has a cost.",
    tags=["P"],
    checklist=[
        "Describe external treatment (gamma or X-ray beams, rotated or from several angles)",
        "Describe internal treatment (a short-range beta or alpha source, or a sealed gamma source, implanted or injected)",
        "Compare the two: targeting, damage to healthy tissue, the need for surgery, radiation type and half-life",
    ],
    parts=[
        explain(
            "The comparison",
            "<table class='tbl'><tr><th></th><th>External (radiotherapy)</th><th>Internal (brachytherapy, radioactive implants, injected isotopes)</th></tr>"
            "<tr><td>How</td><td><b>beams of gamma or X-rays</b> from a machine outside the body, aimed at the tumour; the beam (or the patient) is <b>rotated</b> so the beams cross at the tumour</td><td>a small sealed source is <b>implanted in or next to</b> the tumour — usually a <b>beta or alpha</b> emitter for its short range, sometimes a low-energy <b>gamma</b> emitter — or an isotope that collects in the organ is injected (iodine-131 for the thyroid)</td></tr>"
            "<tr><td>Why that radiation</td><td>gamma / X <b>penetrate</b> to a tumour deep in the body</td><td>a <b>short-range</b> emitter keeps the dose <b>in the tumour</b>; an implanted gamma source sits where the tumour is, so it too irradiates mainly the tumour</td></tr>"
            "<tr><td>Rotation</td><td>healthy tissue along any one path gets only a <b>fraction</b> of the dose; the tumour, where all the beams meet, gets it all</td><td>—</td></tr>"
            "<tr><td>Healthy tissue</td><td><b>some damage</b> to tissue the beams pass through (side effects)</td><td><b>less</b> damage to surrounding tissue; very targeted</td></tr>"
            "<tr><td>Downsides</td><td>many sessions; not all of the dose reaches the tumour</td><td>needs <b>surgery or injection</b>; the patient is <b>contaminated</b> (radioactive) for a time; source must have a suitable <b>half-life</b></td></tr></table>"
            "<p>The June 2024 scheme (Q4(a)): of gamma, X-rays, radio waves and microwaves, <b>gamma</b> is the one that can be applied <b>internally</b> (from an implanted source); the others are applied externally.</p>",
        ),
        worked(
            "Why rotate the beam",
            "In external radiotherapy the gamma beam is rotated around the patient, always pointing at the tumour. Explain why. (2 marks)",
            [
                "<b>Tumour:</b> the tumour is at the <b>centre of rotation</b>, so it is in the beam <b>all the time</b> and receives the <b>full dose</b>, enough to kill its cells.",
                "<b>Healthy tissue:</b> each part of the healthy tissue is in the beam only <b>briefly</b> as it passes, so each gets a <b>small dose</b> and is less damaged.",
            ],
        ),
        practice("Treating tumours", [
            written("ra-t5-q1", "Compare the treatment of a tumour using an external gamma source with treatment using an implanted beta source. (4)",
                    mark_scheme([
                        ("External how", "Gamma <b>beams from outside</b>, penetrating to the tumour, rotated so they cross at it."),
                        ("External cost", "The beams pass through <b>healthy tissue</b>, which is damaged (less so with rotation); no surgery."),
                        ("Internal how", "A <b>beta source placed in the tumour</b>; beta's <b>short range</b> keeps the dose in the tumour."),
                        ("Internal cost", "Needs <b>surgery / injection</b>; the patient is radioactive for a time; less damage to surrounding tissue."),
                    ]), lines=5),
            choice("ra-t5-q2", "Why is a short-range emitter (beta or alpha) a good choice for a source implanted in a tumour?",
                   ["It is cheaper", "Its short range keeps the radiation within the tumour, sparing healthy tissue", "It is not ionising", "It lasts longer"], 1,
                   "Short range = dose stays local. (Sealed gamma sources are also implanted — gamma is the spec's answer for a radiation that can be applied internally.)"),
            written("ra-t5-q3", "Explain why gamma rays or X-rays, not alpha particles, are used for external radiotherapy. (2)",
                    marks(["Alpha is <b>stopped by the skin</b> (a few cm of air), so from outside it could never reach a tumour inside the body.",
                           "Gamma and X-rays <b>penetrate</b> deep into the body to reach the tumour."]), lines=2),
            written("ra-t5-q4", "Iodine-131 (a beta emitter, half-life 8 days) is swallowed to treat thyroid cancer. Explain why this works and why the half-life is suitable. (3)",
                    mark_scheme([
                        ("Targeting", "The thyroid <b>absorbs iodine</b>, so the source collects <b>in the tumour</b>."),
                        ("Beta", "Beta has a <b>short range</b> in tissue, so it <b>kills the thyroid cells</b> while sparing the rest of the body."),
                        ("Half-life", "8 days is <b>long enough to deliver the dose</b> but short enough that the patient is not radioactive for months."),
                    ]), lines=4),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T6 · PET and tracers (P)
# ---------------------------------------------------------------------

section_t6 = section(
    "pet-scanners", "tricky", "PET scanners and tracers", "6.34P, 6.35P",
    equations=[r"e^{+} + e^{-} \rightarrow 2\gamma \text{ (opposite directions)}", r"\text{short half-life} \Rightarrow \text{made nearby}"],
    blurb="A PET scan injects a positron emitter. Each positron meets an electron and the pair annihilates into two gamma rays flying off in opposite directions; detecting both pins down where the decay happened. The isotope's half-life is so short it has to be made next door.",
    tags=["P"],
    checklist=[
        "Describe how a PET scan works: positron emitter, annihilation, two gamma rays, detector ring, image",
        "Explain why PET isotopes must be produced close to the scanner",
        "Explain how a tracer is chosen (where it collects, radiation, half-life)",
    ],
    parts=[
        explain(
            "How PET works, and the half-life problem",
            "<ol><li>The patient is injected with a <b>tracer</b> containing a <b>positron (β⁺) emitter</b> — usually fluorine-18 attached to glucose (FDG), half-life about 110 minutes.</li>"
            "<li>The tracer <b>collects where the body uses most glucose</b>: active tissue such as a tumour or a working part of the brain.</li>"
            "<li>Each emitted <b>positron meets an electron</b> within a millimetre and the two <b>annihilate</b>: their mass becomes energy as <b>two gamma rays</b> travelling in <b>opposite directions</b> (180° apart).</li>"
            "<li>A <b>ring of gamma detectors</b> around the patient records the two gamma rays arriving at <b>almost the same time</b> on opposite sides; the decay happened on the line between them, and the small <b>time difference</b> says where along the line.</li>"
            "<li>Millions of such lines are combined by a computer into a <b>3-D image</b> of where the tracer is concentrated.</li></ol>"
            "<p>These are the June 2024 marks (Q4(b)(i)): annihilate; two gamma rays; opposite directions; detected (gamma camera); at almost the same time; time difference gives the position. The June 2025 scheme for \"positron meets electron\" (Q4(b)(ii), 2 marks): any two of <b>collide</b>, <b>annihilate</b>, <b>release (a pair of) gamma rays</b>; \"meet\", \"combine\", \"interact\", \"attract\" and \"light\" were <b>ignored</b>.</p>"
            "<p><b>Why made nearby</b> (6.35P): positron emitters have <b>short half-lives</b> (F-18 110 min, others minutes), so the activity <b>decays rapidly</b>; if it were transported far it would be <b>too weak to use</b> by the time it arrived. So they are made in a <b>cyclotron</b> at or near the hospital and used within hours.</p>",
        ),
        worked(
            "The two gamma rays",
            "Explain how a PET scanner locates where a positron was emitted. (3 marks)",
            [
                "<b>Annihilation:</b> the positron meets an electron and they <b>annihilate</b>, producing <b>two gamma rays in opposite directions</b>.",
                "<b>Detection:</b> the two gamma rays reach <b>detectors on opposite sides</b> of the ring at almost the same time, so the emission was somewhere on the <b>straight line</b> joining those two detectors.",
                "<b>Position:</b> the <b>difference in arrival times</b> gives where along the line; many lines crossing build the image.",
            ],
        ),
        practice("PET", [
            written("ra-t6-q1", "Describe what happens when a positron meets an electron. (2)",
                    marks(["They <b>collide</b> and <b>annihilate</b> (both are destroyed; their mass becomes energy)…", "…producing <b>two gamma rays</b> travelling in <b>opposite directions</b>."]), lines=2),
            written("ra-t6-q2", "Explain why isotopes used in PET scanners have to be produced close to the hospital. (2)",
                    marks(["They have <b>very short half-lives</b>, so their activity <b>decays rapidly</b>.",
                           "If transported a long way they would be <b>too weak to use</b> (have decayed) on arrival, so they are made in a nearby cyclotron and used within hours."]), lines=3),
            choice("ra-t6-q3", "Why are the gamma rays from annihilation detected in pairs on opposite sides of the patient?",
                   ["The scanner has two detectors", "Momentum is conserved: the two gamma rays leave in opposite directions", "Gamma rays always come in pairs", "The patient reflects them"], 1,
                   "Opposite directions from a near-stationary pair; detecting both fixes a line through the source."),
            written("ra-t6-q4", "Explain why a positron emitter is used for PET rather than a gamma-emitting tracer such as technetium-99m. (2)",
                    marks(["Annihilation gives <b>two gamma rays in opposite directions</b>, so the source can be located <b>on a line</b> between two detectors — far more precise than a single gamma ray of unknown direction.",
                           "Positron emitters can be attached to <b>glucose</b>, so the image shows <b>how active</b> tissue is (metabolism), not just where it is."]), lines=3),
            written("ra-t6-q5", "A hospital 300 km from the nearest cyclotron wants to use fluorine-18 (half-life 110 minutes). A delivery takes 5.5 hours. Calculate the fraction of the activity that would remain, and comment. (3)",
                    marks([r"$5.5\ \text{h} = 330$ min $= 3$ half-lives.", r"Fraction remaining $= \dfrac{1}{2^{3}} = \dfrac{1}{8}$ (12.5%).",
                           "So seven-eighths has decayed before use: the dose injected would have to be eight times larger, or the hospital needs its own cyclotron."]), lines=4),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T7 · Fission and the reactor (P)
# ---------------------------------------------------------------------

section_t7 = section(
    "fission-reactor", "tricky", "Fission, the chain reaction and the reactor", "6.37P, 6.38P, 6.39P, 6.40P, 6.41P, 6.42P",
    equations=[r"{}^{235}\mathrm{U} + n \rightarrow \text{2 daughters} + \text{2–3 } n + \text{energy}", r"\text{moderator slows; control rods absorb}"],
    blurb="A slow neutron splits a uranium-235 nucleus into two smaller nuclei and two or three more neutrons, releasing energy. Those neutrons can split more nuclei: a chain reaction. A reactor keeps it going at a steady rate and turns the energy into electricity.",
    tags=["P"],
    checklist=[
        "Describe the fission of U-235: absorbs a neutron, splits into two daughter nuclei and two or more neutrons, releases energy",
        "Explain a chain reaction and what \"controlled\" means",
        "Explain the jobs of the moderator and the control rods — and keep them apart",
        "Describe the energy chain from fission to electricity, and state that the products are radioactive",
    ],
    parts=[
        explain(
            "Fission and the chain",
            diagram(dg.chain_svg(), 560, 262, "A chain reaction: each fission releases two or three neutrons, which can cause further fissions.") +
            "<p><b>Fission</b> (6.38P): a <b>U-235 nucleus absorbs a slow neutron</b>, becomes unstable (U-236), and <b>splits into two smaller daughter nuclei</b> plus <b>two or three neutrons</b>, <b>releasing energy</b> — mostly as kinetic energy of the fragments. Nuclear reactions (fission, fusion and radioactive decay) are all energy sources (6.37P).</p>"
            "<p><b>Chain reaction</b> (6.39P): the neutrons released can be absorbed by <b>other U-235 nuclei</b>, causing further fissions, which release more neutrons, and so on. <b>Uncontrolled</b> (every neutron causes another fission): the rate grows exponentially — a bomb. <b>Controlled</b> (on average exactly <b>one</b> neutron from each fission causes another): a steady rate of energy release — a reactor.</p>"
            "<p>The June 2025 report (Q4(c)) wanted a \"well-structured explanation\" of what happens when one neutron meets one uranium nucleus: absorbed → unstable → splits into two daughter nuclei → releases neutrons → releases energy.</p>",
        ),
        explain(
            "Inside the reactor",
            "<table class='tbl'><tr><th>Part</th><th>Job</th><th>Why</th></tr>"
            "<tr><td><b>Fuel rods</b></td><td>contain the uranium (enriched in U-235)</td><td></td></tr>"
            "<tr><td><b>Moderator</b> (graphite or water)</td><td><b>slows down</b> the fast neutrons released by fission</td><td><b>slow neutrons are far more likely to be absorbed</b> by U-235 and cause fission; fast ones mostly bounce off</td></tr>"
            "<tr><td><b>Control rods</b> (boron or cadmium)</td><td><b>absorb neutrons</b>; raised or lowered to change how many are absorbed</td><td>fewer neutrons → fewer fissions: this <b>controls the rate</b> of the chain reaction (and can shut it down)</td></tr>"
            "<tr><td><b>Coolant</b> (water or gas)</td><td>carries the thermal energy out of the core</td><td>the kinetic energy of the fission fragments heats the fuel; the coolant transfers it to the boiler</td></tr>"
            "<tr><td><b>Boiler, turbine, generator</b></td><td>heat makes <b>steam</b>, steam turns a <b>turbine</b>, the turbine turns a <b>generator</b></td><td>the same as any thermal power station from here on</td></tr>"
            "<tr><td><b>Concrete and steel shielding</b></td><td>absorbs the radiation from the core</td><td>the <b>fission products are radioactive</b> (6.42P), with long half-lives</td></tr></table>"
            "<p><b>Moderator vs control rods</b> is the examiner's recurring complaint: in 2022 \"most candidates did not recognise that control rods absorb neutrons\" and confused them with the moderator. <b>Moderator slows; control rods absorb.</b> The June 2023 6-marker on this (Q10(c)): the indicative content has three strands — chain reaction, control rods, moderator — so cover all three: \"neutrons hit other U-235 nuclei; control rods absorb neutrons to reduce the number of fissions; the moderator slows neutrons so they are more likely to cause fission\".</p>"
            "<p><b>The energy chain</b> (2022 Q4(b)(iii), \"few gained both marks\"): nuclear store of the fuel → <b>kinetic energy of the fission fragments</b> → <b>thermal store of the fuel and coolant</b> (by heating) → <b>steam</b> → <b>kinetic energy of the turbine</b> → generator (electrically). Start with the fragments, not the coolant.</p>",
        ),
        worked(
            "The 6-marker, in order",
            "Explain how a chain reaction in a nuclear reactor is controlled, including the roles of the moderator and the control rods. (6 marks)",
            [
                "<b>Fission:</b> a U-235 nucleus absorbs a neutron and splits into two daughter nuclei, releasing <b>two or three neutrons</b> and energy.",
                "<b>Chain reaction:</b> those neutrons can be absorbed by <b>other U-235 nuclei</b>, causing further fissions; left alone the number of fissions would grow rapidly.",
                "<b>Moderator:</b> the neutrons are released fast; the moderator (graphite / water) <b>slows them down</b>, because <b>slow neutrons are much more likely to be absorbed</b> by U-235 and cause fission.",
                "<b>Control rods:</b> made of boron, they <b>absorb neutrons</b>; lowering them further into the core absorbs more neutrons, so <b>fewer fissions</b> happen.",
                "<b>Controlled:</b> the rods are set so that, on average, <b>exactly one neutron from each fission</b> goes on to cause another — a steady rate of energy release; pushing them fully in <b>stops</b> the reaction.",
                "<b>Energy out:</b> the energy heats the coolant, which makes steam for the turbine and generator.",
            ],
        ),
        practice("Fission and the reactor", [
            written("ra-t7-q1", "Describe what happens when a neutron is absorbed by a uranium-235 nucleus. (3)",
                    mark_scheme([
                        ("Unstable", "The nucleus becomes <b>unstable</b> (uranium-236)…"),
                        ("Splits", "…and <b>splits into two smaller (daughter) nuclei</b>…"),
                        ("Neutrons + energy", "…releasing <b>two or three neutrons</b> and <b>energy</b> (mostly kinetic energy of the fragments)."),
                    ]), lines=4),
            written("ra-t7-q2", "Explain the difference between the moderator and the control rods in a nuclear reactor. (2)",
                    marks(["The <b>moderator slows down</b> the neutrons so they are <b>more likely to cause fission</b>.",
                           "The <b>control rods absorb</b> neutrons, so <b>fewer fissions</b> occur — they set the rate of the chain reaction."]), lines=2),
            choice("ra-t7-q3", "What does \"controlled chain reaction\" mean?",
                   ["No neutrons are released", "On average one neutron from each fission goes on to cause another fission", "All the neutrons cause fissions", "The reaction has stopped"], 1,
                   "Exactly one on average → steady rate; more than one → runaway; less than one → dies out."),
            written("ra-t7-q4", "Describe how the energy released by fission in a reactor is used to generate electricity. (3)",
                    mark_scheme([
                        ("Fragments → heat", "The <b>kinetic energy of the fission fragments</b> heats the fuel; the <b>coolant</b> carries this thermal energy out of the core."),
                        ("Steam", "The hot coolant <b>heats water to make steam</b>…"),
                        ("Turbine", "…which <b>turns a turbine</b> connected to a <b>generator</b>."),
                    ]), lines=4),
            written("ra-t7-q5", "Explain why the waste from a nuclear reactor must be stored securely for a very long time. (2)",
                    marks(["The <b>fission products are radioactive</b>, many with <b>long half-lives</b>.",
                           "So they stay dangerous (ionising, causing cell damage and cancer) for thousands of years and must be kept from contaminating the environment."]), lines=2),
            choice("ra-t7-q6", "What would happen if the control rods were pulled fully out of the core?",
                   ["The reaction would stop", "More than one neutron per fission would cause further fissions and the rate would rise out of control", "The moderator would melt", "Nothing"], 1,
                   "Nothing absorbing neutrons → an uncontrolled chain reaction."),
            written("ra-t7-q7", "Explain why fast neutrons must be slowed down in a reactor. (2)",
                    marks(["A U-235 nucleus is <b>much more likely to absorb a slow neutron</b> than a fast one (fast ones tend to pass by or bounce off).",
                           "So without a <b>moderator</b> too few neutrons would cause fission and the chain reaction would die out."]), lines=2),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T8 · Fusion (P)
# ---------------------------------------------------------------------

section_t8 = section(
    "fusion", "tricky", "Fusion: stars, conditions, and why it is hard on Earth", "6.43P, 6.44P, 6.45P, 6.46P",
    equations=[r"\text{small nuclei join} \rightarrow \text{larger nucleus} + \text{energy}", r"\text{needs very high temperature and pressure}"],
    blurb="Fusion is small nuclei joining into a larger one, losing a little mass that becomes a lot of energy. It powers stars. It needs enormous temperatures and pressures because the nuclei repel each other, which is why nobody has yet built a fusion power station that pays.",
    tags=["P"],
    checklist=[
        "Describe fusion (nuclei, not atoms) and state that it is the energy source of stars",
        "Explain why fusion needs high temperature and pressure (electrostatic repulsion between protons)",
        "Compare fusion and fission",
        "Relate the conditions for fusion to the difficulty of a practical fusion power station",
    ],
    parts=[
        explain(
            "Fusion, fission, and the obstacle",
            "<p><b>Fusion</b> (6.43P): <b>two small nuclei</b> (e.g. hydrogen isotopes) <b>join to form a larger nucleus</b> (helium). The product has slightly <b>less mass</b> than the parts; the <b>lost mass is released as energy</b>. This is the <b>energy source of stars</b>, including the Sun. The June 2025 report: \"the most common errors were to use the words <b>'atoms' or 'particles' instead of 'nuclei'</b>\". Say nuclei.</p>"
            "<table class='tbl'><tr><th></th><th>Fission</th><th>Fusion</th></tr>"
            "<tr><td>What</td><td>a <b>large</b> nucleus <b>splits</b> into two smaller ones</td><td>two <b>small</b> nuclei <b>join</b> into a larger one</td></tr>"
            "<tr><td>Started by</td><td>absorbing a neutron</td><td>extreme temperature and pressure</td></tr>"
            "<tr><td>Fuel</td><td>uranium-235, plutonium</td><td>hydrogen isotopes (deuterium, tritium)</td></tr>"
            "<tr><td>Products</td><td><b>radioactive</b> daughter nuclei, neutrons</td><td>helium (not radioactive), neutrons</td></tr>"
            "<tr><td>Where</td><td>reactors, bombs</td><td>stars; experimental reactors</td></tr>"
            "<tr><td>Energy per kg of fuel</td><td>very large</td><td>even larger</td></tr></table>"
            "<p><b>Why it needs high temperature and pressure</b> (6.45P): nuclei are <b>positively charged</b>, so they <b>repel</b> each other electrostatically. To get close enough to fuse they need enough <b>kinetic energy to overcome that repulsion</b> — moving extremely <b>fast</b> (very <b>high temperature</b>, millions of kelvin) — and must be crowded <b>close together</b> (very <b>high pressure / density</b>). At low temperature and pressure they never get near enough. The schemes mark \"high energy\" and \"to overcome the (force of) repulsion\" as separate points (June 2018 Q10(a)(i), Nov 2020 Q4(c)).</p>"
            "<p><b>$E = mc^2$</b> is not on the equation list but has been <b>supplied</b> in five of the nine series (2018, 2019, 2023, 2024, 2025): the mass lost in fusion becomes energy. Rearrange to $m = E \\div c^2$ with $c = 3.0 \\times 10^8$ m/s. June 2025 Q10(b)(ii): the Sun radiates $3.9 \\times 10^{26}$ J each second, so $m = 3.9 \\times 10^{26} \\div (3.0 \\times 10^8)^2 = 4.3 \\times 10^9$ <b>kg</b> each second — the <b>unit</b> was part of the evaluation mark (\"$4.3 \\times 10^9$ with no unit or the wrong unit scores 1 mark\"), and every year's guidance says a power-of-ten slip costs the last mark only.</p>"
            "<p><b>Why no fusion power station yet</b> (6.46P): those conditions are <b>very hard to create and contain</b> on Earth — no material can hold a gas at millions of degrees, so it is confined by magnetic fields; so far the energy put in to reach the conditions is <b>about as much as</b> the energy got out, so it is not yet <b>practical or economic</b>.</p>",
        ),
        worked(
            "Why stars fuse and we struggle",
            "Explain why fusion happens in the core of the Sun but is difficult to achieve on Earth. (4 marks)",
            [
                "<b>Repulsion:</b> nuclei are <b>positively charged</b> and <b>repel</b> each other, so they only fuse if they have enough <b>energy to overcome that repulsion</b> (collide at very high speed) and are packed close together.",
                "<b>In the Sun:</b> gravity compresses the core to an enormous <b>pressure</b> and <b>temperature</b> (about 15 million K), so hydrogen nuclei move fast enough and are close enough to fuse.",
                "<b>On Earth:</b> reaching those temperatures takes a huge energy input, and the hot plasma must be <b>contained</b> without touching any material (magnetic confinement).",
                "<b>Economics:</b> so far the energy needed to create the conditions is about the same as the energy released, so it is not yet a <b>practical, economic</b> power source.",
            ],
        ),
        practice("Fusion", [
            written("ra-t8-q1", "Describe what is meant by nuclear fusion. (2)",
                    marks(["Two <b>small nuclei join</b> (fuse) to form a <b>larger nucleus</b>…", "…with a <b>loss of mass</b> that is released as <b>energy</b>."]), lines=2),
            written("ra-t8-q2", "Explain why nuclear fusion does not happen at low temperatures and pressures. (2)",
                    marks(["Nuclei are <b>positively charged</b> and <b>repel</b> each other (electrostatic repulsion between the protons).",
                           "A very <b>high temperature</b> gives the nuclei enough <b>kinetic energy to overcome the repulsion</b>, and a <b>high pressure</b> keeps them close together, so they get near enough to fuse (June 2018 Q10(a)(i): \"high energy (1) to overcome (force of) repulsion (1)\")."]), lines=3),
            choice("ra-t8-q3", "Which statement about fusion and fission is correct?",
                   ["Both split large nuclei", "Fission splits a large nucleus; fusion joins small nuclei", "Fusion is the energy source of nuclear power stations today", "Fission is the energy source of stars"], 1,
                   "Stars fuse; power stations (so far) fission."),
            written("ra-t8-q4", "Give two differences between nuclear fusion and nuclear fission. (2)",
                    marks(["Fusion <b>joins small nuclei</b>; fission <b>splits a large nucleus</b>.",
                           "Fusion needs <b>very high temperature and pressure</b> to start; fission is started by a nucleus <b>absorbing a neutron</b>. (Or: fission products are radioactive; fusion's helium is not.)"]), lines=2),
            written("ra-t8-q5", "Explain why a fusion power station has not yet been built as a practical source of electricity. (2)",
                    marks(["The <b>temperature and pressure needed are extremely hard to produce and contain</b> on Earth (no container can touch plasma at millions of degrees; magnetic confinement is needed).",
                           "The energy required to reach those conditions has so far been <b>about as much as the energy released</b>, so it is not yet economic."]), lines=3),
            written("ra-t8-q6", "A student writes: \"In fusion, two hydrogen atoms join to make a helium atom.\" Correct the statement. (1)",
                    marks(["It is the <b>nuclei</b> that fuse: two hydrogen <b>nuclei</b> join to form a helium <b>nucleus</b>, releasing energy."]), lines=2),
        ]),
    ],
)

# ---------------------------------------------------------------------
# T9 · Nuclear power: evaluate (P)
# ---------------------------------------------------------------------

section_t9 = section(
    "nuclear-power", "tricky", "Nuclear power: the for-and-against question", "6.36P",
    equations=[r"\text{advantages} + \text{disadvantages} + \text{a judgement}"],
    blurb="The papers say \"Discuss the arguments for and against\" (Nov 2020 Q8(c)), \"Compare\" fission and fusion as sources (Nov 2021) or give you a FOR / AGAINST list to add to (June 2026). Every point is a fact plus a <b>so</b>: \"no carbon emissions, <b>so</b> it does not add to global warming\". Add a conclusion when the command word is discuss or evaluate; the marks are in the reasoned points.",
    tags=["P"],
    checklist=[
        "Give the advantages of nuclear power (no CO₂ in generation, reliable, energy density, small fuel volume)",
        "Give the disadvantages (radioactive waste with long half-lives, cost of building and decommissioning, accident risk, non-renewable)",
        "Finish an evaluate answer with a justified conclusion",
    ],
    parts=[
        explain(
            "For, against, decide",
            "<table class='tbl'><tr><th>Advantages</th><th>Disadvantages</th></tr>"
            "<tr><td><b>No carbon dioxide</b> (or other greenhouse gas) produced while generating — does not add to climate change</td><td>The <b>waste is radioactive</b>, with <b>long half-lives</b>: it must be stored securely for thousands of years, and nobody has a permanent solution agreed</td></tr>"
            "<tr><td><b>Reliable</b>: generates continuously regardless of weather, unlike wind and solar</td><td>Very <b>expensive to build</b> and to <b>decommission</b> (dismantle safely) at the end of its life</td></tr>"
            "<tr><td>Enormous <b>energy per kilogram of fuel</b>: a small volume of fuel for a huge output, so little mining and transport</td><td>Risk of <b>accidents</b> releasing radioactive material over a wide area (contamination lasting decades)</td></tr>"
            "<tr><td>Fuel is relatively <b>plentiful</b> and not concentrated in a few countries</td><td>Uranium is <b>non-renewable</b>; mining and enrichment have their own impacts and energy cost</td></tr>"
            "<tr><td>Small land area compared with wind or solar farms</td><td>Security concerns: fuel and waste could be misused; public opposition</td></tr></table>"
            "<p><b>The shape of a Level-3 evaluate answer:</b> at least two advantages and two disadvantages, each with the physics reason (\"no CO₂ <i>because</i> the energy comes from fission, not combustion\"; \"waste is dangerous <i>because</i> the fission products are radioactive with long half-lives\"), then a <b>conclusion that follows</b>: e.g. \"nuclear is a good way to supply reliable low-carbon electricity while renewables are built up, provided the waste is stored securely\". The Nov 2020 indicative content also credits: running out of fossil fuels; <b>low running costs</b>; <b>large power output</b> compared with wind or solar; fuel lasts hundreds of years with reprocessing; against — contamination of ground water, loss of life in an accident, terrorism.</p>",
        ),
        worked(
            "A compact evaluation",
            "Discuss the arguments for and against using nuclear power to meet the increasing demand for electricity. (6 marks)",
            [
                "<b>For 1:</b> fission releases energy without burning fuel, so <b>no carbon dioxide</b> is produced during generation — it does not contribute to climate change as fossil fuels do.",
                "<b>For 2:</b> a nuclear station runs <b>continuously</b> whatever the weather, so it provides a reliable baseload that wind and solar cannot; and a tiny mass of fuel gives a huge energy output.",
                "<b>Against 1:</b> the <b>fission products are radioactive with long half-lives</b>, so the waste must be stored safely for thousands of years and there is no agreed permanent solution.",
                "<b>Against 2:</b> stations are <b>very expensive to build and decommission</b>, and an accident could contaminate a large area for decades.",
                "<b>Judgement:</b> because the climate problem is urgent and renewables are intermittent, nuclear power is a <b>reasonable part of a low-carbon mix</b> — provided the waste is dealt with properly and the high costs are accepted; it is not a complete answer on its own because the fuel is non-renewable.",
            ],
        ),
        practice("Nuclear power", [
            written("ra-t9-q1", "Give two advantages and two disadvantages of generating electricity from nuclear power. (4)",
                    mark_scheme([
                        ("Advantage 1", "<b>No carbon dioxide</b> emitted during generation."),
                        ("Advantage 2", "<b>Reliable</b> / huge energy per kg of fuel / small volume of fuel."),
                        ("Disadvantage 1", "<b>Radioactive waste</b> with long half-lives that must be stored for thousands of years."),
                        ("Disadvantage 2", "<b>Expensive</b> to build and decommission / risk of <b>accident</b> and contamination / non-renewable fuel."),
                    ]), lines=5),
            choice("ra-t9-q2", "Why is nuclear waste a long-term problem?",
                   ["It explodes", "The fission products are radioactive with long half-lives, so they stay hazardous for thousands of years", "It is very hot", "It is radioactive for a few days"], 1,
                   "Long half-life = hazard that lasts."),
            written("ra-t9-q3", "A country is deciding between building a nuclear power station and a gas-fired power station. Use physics to give one argument for each choice. (2)",
                    marks(["Nuclear: no <b>carbon dioxide</b> in generation (gas releases CO₂ when burned) and far more energy per kilogram of fuel.",
                           "Gas: much <b>cheaper and quicker to build</b>, no radioactive waste, can be started and stopped quickly to meet demand."]), lines=3),
            written("ra-t9-q4", "Explain why nuclear power is described as low-carbon but not renewable. (2)",
                    marks(["Low-carbon: the energy comes from <b>fission</b>, not combustion, so <b>no carbon dioxide</b> is released during generation.",
                           "Not renewable: the fuel (<b>uranium</b>) is a finite resource that is <b>not replaced</b> as it is used."]), lines=2),
        ]),
    ],
)

SECTIONS = [section_t1, section_t2, section_t3, section_t4, section_t5, section_t6, section_t7, section_t8, section_t9]

# ---------------------------------------------------------------------
# Flashcards
# ---------------------------------------------------------------------

FACTS = [
    fact("Structure of the atom?", "A tiny, dense, positive nucleus of protons and neutrons, with electrons orbiting at set distances. Almost all the mass is in the nucleus; most of the atom is empty space.", "atom"),
    fact("Size of an atom? Of the nucleus?", "Atom about 10⁻¹⁰ m; nucleus about 10⁻¹⁵ m (1/10 000 of the atom).", "atom"),
    fact("Relative masses and charges: p, n, e, e⁺?", "Proton 1, +1. Neutron 1, 0. Electron 1/1836, −1. Positron 1/1836, +1.", "atom"),
    fact("Why is an atom neutral?", "Equal numbers of protons (+1) and electrons (−1).", "atom"),
    fact("A and Z?", "A = mass (nucleon) number = protons + neutrons; Z = atomic (proton) number = protons. Neutrons = A − Z.", "isotopes"),
    fact("Isotopes?", "Same element (same protons), different numbers of neutrons (different mass number).", "isotopes"),
    fact("How does an electron move to a higher orbit?", "By absorbing electromagnetic radiation; it emits EM radiation when it falls back.", "electrons-ions"),
    fact("How does an atom become a positive ion?", "It loses an outer electron (e.g. knocked out by ionising radiation), leaving more protons than electrons.", "electrons-ions"),
    fact("Alpha particle?", "A helium nucleus: 2 protons + 2 neutrons, charge +2. Most ionising; stopped by paper or a few cm of air.", "radiation-types"),
    fact("Beta-minus particle?", "A fast electron from the nucleus (a neutron became a proton), charge −1. Stopped by a few mm of aluminium.", "radiation-types"),
    fact("Gamma ray?", "Electromagnetic radiation from the nucleus: no mass, no charge. Least ionising; reduced by thick lead or concrete.", "radiation-types"),
    fact("Penetration order? Ionising order?", "Penetration: alpha < beta < gamma. Ionising: alpha > beta > gamma.", "radiation-types"),
    fact("Sources of background radiation?", "Radon gas from rocks (largest), rocks and buildings, food and drink, cosmic rays, medical X-rays, nuclear industry (tiny).", "background"),
    fact("Two detectors of radiation?", "Geiger–Müller tube with a counter (count rate); photographic film, which darkens (film badges).", "background"),
    fact("Corrected count rate?", "Measured count rate − background count rate. Measure background with no source, over several minutes, repeat and average.", "background"),
    fact("Alpha decay: effect on A and Z?", "A − 4, $Z - 2$.", "decays"),
    fact("Beta-minus decay: what happens, effect on A and Z?", "Neutron → proton + electron (emitted). A same, $Z + 1$.", "decays"),
    fact("Beta-plus decay: what happens, effect on A and Z?", "Proton → neutron + positron (emitted). A same, $Z - 1$.", "decays"),
    fact("Gamma emission: effect on A and Z?", "None — same element. The nucleus rearranges, loses energy and becomes more stable, often just after an alpha or beta decay.", "decays"),
    fact("Neutron emission: effect on A and Z?", "A − 1, Z same.", "decays"),
    fact("How do you check a nuclear equation?", "Top numbers (mass) add up on both sides; bottom numbers (charge) add up on both sides.", "decays"),
    fact("Activity and its unit?", "Number of decays per second; becquerel (Bq) = 1 decay per second.", "half-life-nn"),
    fact("Half-life (two forms)?", "Time for half the undecayed nuclei to decay; time for the activity to fall to half.", "half-life-nn"),
    fact("Random but predictable?", "Cannot predict which nucleus decays or when; but with huge numbers of nuclei the half-life predicts the activity of the sample.", "half-life-nn"),
    fact("Fraction left after n half-lives?", "1/2ⁿ: ½, ¼, ⅛, 1/16 (50%, 25%, 12.5%, 6.25%).", "half-life-nn"),
    fact("Dangers of ionising radiation?", "Ionises atoms in cells: kills or damages cells (tissue damage, burns); damages DNA → mutations → cancer.", "dangers-precautions"),
    fact("Precautions for handling a source?", "Tongs, point away, lead-lined box, limit time, keep distance, no eating, wash hands.", "dangers-precautions"),
    fact("Precautions for radiographers?", "Lead apron / lead screen, leave the room, limit time, film badge to monitor dose.", "dangers-precautions"),
    fact("Irradiation?", "Exposure to radiation from an external source: does not make you radioactive; stops when the source is removed; can be shielded.", "dangers-precautions"),
    fact("Contamination?", "Radioactive material on or in the object: it stays radioactive, keeps emitting, hard to remove, cannot be shielded from inside.", "dangers-precautions"),
    fact("Worst radiation for irradiation? For contamination?", "Irradiation: gamma (penetrates). Contamination: alpha (most ionising, now inside).", "dangers-precautions"),
    fact("Smoke alarm: source and why?", "Americium-241, alpha, long half-life. Alpha ionises air so a current flows; smoke absorbs alpha, current falls, alarm. Alpha cannot escape the casing.", "uses-radioactivity"),
    fact("Sterilising / irradiating food: source and why?", "Gamma, long half-life: penetrates packaging and kills microbes; the food is irradiated, not contaminated.", "uses-radioactivity"),
    fact("Medical tracer: source and why?", "Gamma emitter (technetium-99m), short half-life (6 h): gamma escapes the body to the camera; weakly ionising; dose falls quickly.", "uses-radioactivity"),
    fact("Thickness gauge: source and why?", "Beta, long half-life: partly absorbed by paper so the count changes with thickness; alpha all stopped, gamma all through; steady activity.", "uses-radioactivity"),
    fact("Two-reason answer for choosing a source?", "One reason for the type (penetration / ionisation) and one for the half-life — each linked to the job.", "choosing-source"),
    fact("Short vs long half-life: danger?", "Short: high activity now, soon gone. Long: lower activity but the hazard lasts — long-term storage.", "choosing-source"),
    fact("Plum pudding model?", "A ball of positive charge with electrons embedded in it.", "atomic-model"),
    fact("Alpha scattering: three observations and conclusions?", "Most straight through → mostly empty space. Some deflected → positive nucleus. Very few bounced back → tiny, dense nucleus with most of the mass.", "atomic-model"),
    fact("Bohr's change to the model?", "Electrons in fixed orbits (energy levels) at set distances; they move between levels by absorbing or emitting EM radiation — which matched observations.", "atomic-model"),
    fact("Half-life from a graph with background?", "Subtract the background from the start value, halve the corrected count, add the background back, read the time.", "half-life-hard"),
    fact("Working backwards?", "Original activity = later activity × 2ⁿ.", "half-life-hard"),
    fact("Why is the radiographer protected but not the patient?", "The radiographer is exposed many times a day (large total dose); the patient has one exposure where the benefit outweighs the risk.", "contamination-explain"),
    fact("External vs internal tumour treatment?", "External: gamma/X beams rotated to cross at the tumour; no surgery; some healthy tissue damaged. Internal: a source (short-range beta/alpha, or a sealed gamma source) placed in the tumour; targeted; needs surgery; patient radioactive for a while.", "tumours"),
    fact("PET scan in four steps?", "Positron-emitting tracer injected → positron meets electron and they annihilate → two gamma rays in opposite directions → ring of detectors locates the line; many lines make the image.", "pet-scanners"),
    fact("Why are PET isotopes made nearby?", "Very short half-lives: the activity decays rapidly, so they would be too weak after a long journey.", "pet-scanners"),
    fact("Fission of U-235?", "Absorbs a slow neutron → unstable → splits into two daughter nuclei + 2 or 3 neutrons + energy.", "fission-reactor"),
    fact("Chain reaction? Controlled?", "Neutrons from one fission cause further fissions. Controlled: on average one neutron per fission goes on to cause another.", "fission-reactor"),
    fact("Moderator vs control rods?", "Moderator (graphite/water) SLOWS neutrons so they are absorbed and cause fission. Control rods (boron) ABSORB neutrons to set the rate.", "fission-reactor"),
    fact("Energy chain in a reactor?", "Kinetic energy of fission fragments → thermal store of fuel and coolant → steam → kinetic energy of turbine → generator.", "fission-reactor"),
    fact("Fission products?", "Radioactive, with long half-lives — the waste problem.", "fission-reactor"),
    fact("Fusion?", "Two small NUCLEI join to form a larger nucleus; mass is lost and released as energy. The energy source of stars.", "fusion"),
    fact("Why does fusion need high temperature and pressure?", "Nuclei are positive and repel; they need enough kinetic energy (high T) to overcome the repulsion and must be close together (high P).", "fusion"),
    fact("Why no fusion power station yet?", "The conditions are extremely hard to create and contain; so far the energy in is about equal to the energy out — not practical or economic.", "fusion"),
    fact("Fission vs fusion in one line each?", "Fission: large nucleus splits, started by a neutron, radioactive products. Fusion: small nuclei join, needs extreme T and P, powers stars.", "fusion"),
    fact("Nuclear power: two for, two against?", "For: no CO₂ in generation; reliable, huge energy per kg. Against: long-lived radioactive waste; expensive to build and decommission, accident risk.", "nuclear-power"),
]
