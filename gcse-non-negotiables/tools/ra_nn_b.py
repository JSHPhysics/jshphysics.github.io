"""
ra_nn_b.py — Topic 6 (Radioactivity): the non-negotiables N6–N10.

N6 Decay equations              N9 Uses of radioactivity
N7 Activity and half-life       N10 Key words
N8 Dangers and precautions
"""

from revlib import (
    choice, explain, fact, mark_scheme, marks, numeric, practice, section,
    worked, written,
)

# ---------------------------------------------------------------------
# N6 · Decay equations
# ---------------------------------------------------------------------

DECAY_TABLE = (
    "<table class='tbl'><tr><th>Decay</th><th>What happens in the nucleus</th><th>Mass number A</th><th>Atomic number Z</th><th>Equation pattern</th></tr>"
    "<tr><td><b>Alpha α</b></td><td>2 protons + 2 neutrons leave as a helium nucleus</td><td><b>−4</b></td><td><b>−2</b></td><td>${}^{A}_{Z}\\mathrm{X} \\rightarrow {}^{A-4}_{Z-2}\\mathrm{Y} + {}^{4}_{2}\\mathrm{He}$</td></tr>"
    "<tr><td><b>Beta-minus β⁻</b></td><td>a <b>neutron turns into a proton</b> and an electron; the electron is emitted</td><td><b>0</b></td><td><b>+1</b></td><td>${}^{A}_{Z}\\mathrm{X} \\rightarrow {}^{A}_{Z+1}\\mathrm{Y} + {}^{\\;0}_{-1}\\mathrm{e}$</td></tr>"
    "<tr><td><b>Beta-plus β⁺</b></td><td>a <b>proton turns into a neutron</b> and a positron; the positron is emitted</td><td><b>0</b></td><td><b>−1</b></td><td>${}^{A}_{Z}\\mathrm{X} \\rightarrow {}^{A}_{Z-1}\\mathrm{Y} + {}^{0}_{+1}\\mathrm{e}$</td></tr>"
    "<tr><td><b>Gamma γ</b></td><td>the nucleus <b>rearranges</b> and loses energy as an EM wave, often just after another decay</td><td><b>0</b></td><td><b>0</b></td><td>${}^{A}_{Z}\\mathrm{X}^{*} \\rightarrow {}^{A}_{Z}\\mathrm{X} + \\gamma$</td></tr>"
    "<tr><td><b>Neutron emission</b></td><td>a neutron leaves</td><td><b>−1</b></td><td><b>0</b></td><td>${}^{A}_{Z}\\mathrm{X} \\rightarrow {}^{A-1}_{Z}\\mathrm{X} + {}^{1}_{0}\\mathrm{n}$</td></tr></table>"
)

section_n6 = section(
    "decays", "nn", "Decay equations: what each decay does to A and Z", "6.18, 6.19, 6.20, 6.21, 6.22",
    equations=[r"\alpha: A-4,\ Z-2", r"\beta^{-}: Z+1", r"\beta^{+}: Z-1", r"\gamma: \text{no change}"],
    blurb="Every decay equation balances: the mass numbers add up on both sides, and so do the atomic numbers (charges). Learn what each decay does to A and Z and the equations write themselves.",
    checklist=[
        "Describe β⁻ decay (neutron → proton + electron) and β⁺ decay (proton → neutron + positron)",
        "State the effect of α, β⁻, β⁺, γ and neutron emission on the mass number and atomic number",
        "Balance a nuclear equation for mass and charge",
    ],
    parts=[
        explain(
            "The five decays",
            DECAY_TABLE +
            "<p><b>Balancing:</b> the top numbers add up on both sides, and so do the bottom numbers. ${}^{238}_{92}\\mathrm{U} \\rightarrow {}^{234}_{90}\\mathrm{Th} + {}^{4}_{2}\\mathrm{He}$: 238 = 234 + 4 and 92 = 90 + 2. For beta-minus, ${}^{14}_{6}\\mathrm{C} \\rightarrow {}^{14}_{7}\\mathrm{N} + {}^{\\;0}_{-1}\\mathrm{e}$: 14 = 14 + 0 and 6 = 7 + (−1).</p>"
            "<p>Two things the examiners' reports pick out. <b>β⁺ is not just β⁻ in reverse — think it through</b>: in June 2025 \"a common error was to describe beta-minus emission\" when β⁺ was asked — a proton becomes a neutron and a <b>positron</b> is emitted, so Z goes <b>down</b> by one. And the beta symbol needs its charge: the June 2024 scheme gave a mark for writing β with <b>−1</b>, and a mark for numbers that balance.</p>"
            "<p><b>Gamma after a decay</b> (6.21): a nucleus that has just emitted an alpha or beta particle is often left with spare energy; it <b>rearranges</b> and gets rid of that energy as a <b>gamma ray</b>. Nothing about A or Z changes.</p>",
        ),
        worked(
            "A beta-minus equation",
            "Strontium-90 (⁹⁰₃₈Sr) decays by beta-minus emission to yttrium (Y). Write the nuclear equation and describe what happens inside the nucleus. (3 marks)",
            [
                r"<b>Rule:</b> β⁻ leaves A the same and raises Z by 1, so the product is ${}^{90}_{39}\mathrm{Y}$.",
                r"<b>Equation:</b> ${}^{90}_{38}\mathrm{Sr} \rightarrow {}^{90}_{39}\mathrm{Y} + {}^{\;0}_{-1}\mathrm{e}$ — check: 90 = 90 + 0; 38 = 39 − 1 ✓",
                "<b>Inside:</b> a <b>neutron changes into a proton</b> and an <b>electron</b>, and the electron is emitted at high speed.",
            ],
        ),
        practice("Decay equations", [
            written("ra-n6-q1", "Describe the process of beta-minus decay. (2)",
                    marks(["A <b>neutron in the nucleus changes into a proton</b>…", "…and an <b>electron</b> (the beta particle) is <b>emitted</b> from the nucleus. Mass number unchanged, atomic number up by 1."]), lines=2),
            written("ra-n6-q2", "Describe the process of beta-plus decay. (2)",
                    marks(["A <b>proton in the nucleus changes into a neutron</b>…", "…and a <b>positron</b> is <b>emitted</b>. Mass number unchanged, atomic number down by 1."]), lines=2),
            choice("ra-n6-q3", "²²⁶₈₈Ra decays by alpha emission. The product is…",
                   ["²²²₈₆Rn", "²²⁶₈₉Ac", "²²⁴₈₆Rn", "²²²₈₈Ra"], 0,
                   "Alpha: A − 4 = 222, Z − 2 = 86."),
            choice("ra-n6-q4", "¹⁸₉F decays by β⁺ emission. The product is…",
                   ["¹⁸₁₀Ne", "¹⁸₈O", "¹⁷₉F", "¹⁴₇N"], 1,
                   "β⁺: A unchanged, Z − 1 = 8 (oxygen)."),
            written("ra-n6-q5", "Explain why the mass number and atomic number of a nucleus do not change when it emits a gamma ray. (2)",
                    marks(["A gamma ray is <b>electromagnetic radiation</b>: it has <b>no mass and no charge</b>.",
                           "So no protons or neutrons leave — the nucleus just <b>loses energy</b> (rearranges into a lower-energy state)."]), lines=3),
            written("ra-n6-q6", "Complete and check this equation for the alpha decay of polonium-210: ²¹⁰₈₄Po → ? + ⁴₂He. (2)",
                    marks([r"Product: ${}^{206}_{82}\mathrm{Pb}$ (lead) — mass number $210 - 4 = 206$, atomic number $84 - 2 = 82$.",
                           "Check both lines balance: 210 = 206 + 4 and 84 = 82 + 2."]), lines=2),
            choice("ra-n6-q7", "A nucleus emits a neutron. What happens to its mass number and atomic number?",
                   ["A − 1, Z unchanged", "A − 1, Z − 1", "A unchanged, Z − 1", "A − 4, Z − 2"], 0,
                   "A neutron has mass 1 and no charge."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N7 · Activity and half-life
# ---------------------------------------------------------------------

section_n7 = section(
    "half-life-nn", "nn", "Activity and half-life", "6.23, 6.24, 6.25, 6.26, 6.27",
    equations=[r"\text{activity in Bq} = \text{decays per second}", r"\text{half-life: time for activity (or undecayed nuclei) to halve}"],
    blurb="The activity of a source falls over time because there are fewer undecayed nuclei left. The half-life is how long it takes to halve — the same however much you start with, and the one thing about a random process that can be predicted.",
    checklist=[
        "Define activity and its unit, and half-life in both forms",
        "Explain why decay is random but the half-life is predictable",
        "Carry out half-life calculations: fraction left, activity after n half-lives, time taken, and from a graph",
    ],
    parts=[
        explain(
            "Definitions, and why activity falls",
            "<p><b>Activity</b> is the <b>number of decays per second</b> of a source; its unit is the <b>becquerel (Bq)</b>: 1 Bq = 1 decay per second. A GM tube measures a <b>count rate</b>, which is a fraction of the activity (it only catches the radiation that enters the tube).</p>"
            "<p>The activity <b>decreases over time</b> because each decay uses up one unstable nucleus, so there are <b>fewer undecayed nuclei left</b> to decay; fewer nuclei → fewer decays per second.</p>"
            "<p><b>Half-life</b> is <b>the time taken for half of the undecayed nuclei to decay</b> — equivalently, <b>the time for the activity (or count rate) to fall to half</b> its value. Either form is credited; give one in full.</p>"
            "<p><b>Random but predictable:</b> it <b>cannot be predicted when a particular nucleus will decay</b> — each decay is random. But a source contains an enormous number of nuclei, and with large numbers the random behaviour averages out, so the half-life lets you <b>predict how the activity of the whole source</b> will fall. Like dice: you cannot say which die will show a six, but with a thousand dice about a sixth will.</p>"
            "<p>The calculation types below do the four standard calculations: fraction remaining after n half-lives (1/2ⁿ), activity after a time, time taken for the activity to fall to a value, and reading a half-life from a decay graph (draw the horizontal line at half the activity, drop to the time axis — the June 2024 scheme gave one mark for the line at 48–52 Bq and one for the time read off).</p>",
        ),
        worked(
            "Activity after three half-lives",
            "A source has an activity of 800 Bq and a half-life of 6 hours. Calculate its activity after 18 hours.",
            [
                r"<b>Number of half-lives:</b> $18 \div 6 = 3$.",
                r"<b>Halve three times:</b> $800 \rightarrow 400 \rightarrow 200 \rightarrow 100$ Bq.",
                r"(Or: fraction left $= \dfrac{1}{2^{3}} = \dfrac{1}{8}$; $800 \times \dfrac{1}{8} = 100$ Bq.)",
            ],
        ),
        practice("Activity and half-life", [
            written("ra-n7-q1", "State what is meant by the half-life of a radioactive isotope. (1)",
                    marks(["The <b>time taken for half the undecayed nuclei to decay</b> (or for the <b>activity to fall to half</b> its original value)."]), lines=2),
            written("ra-n7-q2", "State what is meant by the activity of a source, and give its unit. (2)",
                    marks(["The <b>number of decays per second</b> (rate of decay).", "Unit: the <b>becquerel, Bq</b> (1 Bq = 1 decay per second)."]), lines=2),
            written("ra-n7-q3", "Explain why the activity of a radioactive source decreases with time. (2)",
                    marks(["Each decay leaves <b>one fewer undecayed (unstable) nucleus</b>.",
                           "The activity depends on the <b>number of undecayed nuclei</b>, so as they are used up fewer decay each second."]), lines=2),
            written("ra-n7-q4", "Radioactive decay is random, yet half-lives can be used to make predictions. Explain. (2)",
                    marks(["It <b>cannot be predicted when any particular nucleus</b> will decay.",
                           "But a source contains a <b>very large number</b> of nuclei, so the overall behaviour averages out and the half-life predicts how the <b>activity of the whole sample</b> changes."]), lines=3),
            numeric("ra-n7-q5", "A source has an activity of 6000 Bq and a half-life of 8 days. Calculate its activity after 24 days.", 750, "Bq",
                    "24 ÷ 8 = 3 half-lives.", [r"$6000 \rightarrow 3000 \rightarrow 1500 \rightarrow 750$ Bq."]),
            numeric("ra-n7-q6", "The activity of a source falls from 1200 Bq to 150 Bq in 45 minutes. Calculate its half-life.", 15, "min",
                    "How many halvings from 1200 to 150?", [r"$1200 \rightarrow 600 \rightarrow 300 \rightarrow 150$: three half-lives in 45 min, so one half-life $= 15$ min."]),
            choice("ra-n7-q7", "After two half-lives, what fraction of the original undecayed nuclei remain?",
                   ["1/2", "1/3", "1/4", "0"], 2,
                   "½ × ½ = ¼. The source never quite reaches zero."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N8 · Dangers and precautions
# ---------------------------------------------------------------------

section_n8 = section(
    "dangers-precautions", "nn", "Dangers, precautions, contamination and irradiation", "6.29, 6.31, 6.32",
    equations=[r"\text{time} \downarrow\ \text{distance} \uparrow\ \text{shielding} \uparrow", r"\text{contamination: source on/in}\quad \text{irradiation: exposed to}"],
    blurb="Ionising radiation damages cells. The precautions all come down to less time, more distance, more shielding, and not getting the material on or in you — which is the difference between irradiation and contamination.",
    checklist=[
        "Describe the dangers of ionising radiation (tissue damage, mutation, cancer) in mark-scheme form",
        "Give precautions for people handling sources and for medical staff and patients",
        "State the difference between contamination and irradiation and compare their hazards",
    ],
    parts=[
        explain(
            "Dangers",
            "<p>Ionising radiation <b>knocks electrons out of atoms</b> in living cells. That can <b>damage or kill cells</b> (high doses: radiation burns, radiation sickness) or <b>damage the DNA</b> in a cell so that it <b>mutates</b>; a mutated cell that keeps dividing is <b>cancer</b>. Write <i>mutation</i> and <i>cancer</i> — \"it is dangerous\" or \"it makes you ill\" score nothing.</p>"
            "<p><b>Precautions when handling a source:</b> keep it in a <b>lead-lined box</b>; handle it with <b>tongs</b>, never fingers, and point it <b>away</b> from people (distance); <b>limit the time</b> of exposure; use <b>shielding</b> (lead); don't eat or drink nearby; wash hands afterwards.</p>"
            "<p><b>Medical staff and patients</b> (6.31): staff wear <b>film badges</b> to monitor their dose, stand behind <b>lead screens</b> or leave the room, wear <b>lead aprons</b>, and limit their time — they are exposed every day, so their total dose would otherwise be high. Patients have <b>dose limits</b>: use the <b>lowest dose</b> that works, a <b>short half-life</b> tracer, and only when the benefit outweighs the risk. The 2022 report: two precautions must be <b>different kinds</b> — \"gloves and masks\" are both protective clothing and scored one; protective clothing <i>and</i> shielding <i>or</i> limited time scored two. Lead was credited; aluminium ignored.</p>",
        ),
        explain(
            "Contamination and irradiation",
            "<table class='tbl'><tr><th></th><th>Irradiation</th><th>Contamination</th></tr>"
            "<tr><td>What it is</td><td>being <b>exposed to radiation</b> from a source <b>outside</b> the object or body</td><td><b>radioactive material</b> getting <b>on or inside</b> the object or body</td></tr>"
            "<tr><td>Does it make you radioactive?</td><td><b>No</b></td><td><b>Yes</b> — the source is now in or on you</td></tr>"
            "<tr><td>How long?</td><td>only while the source is there: <b>stops when the source is removed</b> or you move away</td><td><b>continues</b> until the material decays or is removed; hard to remove</td></tr>"
            "<tr><td>Protection</td><td><b>shielding</b>, distance, time</td><td>gloves, sealed sources, no eating; prevent it in the first place</td></tr>"
            "<tr><td>Most dangerous radiation</td><td><b>gamma</b> (penetrates to the organs; alpha cannot get through skin)</td><td><b>alpha</b> (strongly ionising, and now inside where it cannot be shielded)</td></tr></table>"
            "<p>The June 2024 scheme (Q4(c), 2 marks): irradiation <b>does not make the object radioactive</b>; it <b>can be stopped by shielding</b>; the <b>source is outside</b>; it <b>stops when the source is removed</b>; \"you can move away from irradiation\" accepted.</p>",
        ),
        worked(
            "Comparing the hazards",
            "Explain why an alpha source is more dangerous inside the body than outside it. (3 marks)",
            [
                "<b>Outside (irradiation):</b> alpha particles are <b>stopped by the skin</b> (or a few cm of air), so they cannot reach living cells inside — little harm.",
                "<b>Inside (contamination):</b> the source is <b>next to living cells</b>, and alpha is the <b>most strongly ionising</b> radiation, so all its energy is absorbed in a small volume of tissue.",
                "<b>Consequence:</b> many cells are <b>damaged or mutated</b> (risk of cancer), and the source <b>cannot be shielded or removed</b> once inside.",
            ],
        ),
        practice("Dangers and precautions", [
            written("ra-n8-q1", "Describe the dangers of ionising radiation to the body. (2)",
                    marks(["It <b>ionises atoms in cells</b>, which can <b>kill or damage</b> cells (tissue damage, burns).",
                           "It can damage DNA and cause <b>mutations</b>, which may lead to <b>cancer</b>."]), lines=2),
            written("ra-n8-q2", "A technician injects patients with a radioactive tracer. State two different precautions that reduce the technician's exposure. (2)",
                    marks(["<b>Shielding</b>: lead apron / lead screen / keep the source in a lead container.",
                           "<b>Limit the time</b> near the source / increase the <b>distance</b> (tongs, stand back) / <b>film badge</b> to monitor the dose. (Two different kinds of precaution.)"]), lines=2),
            written("ra-n8-q3", "State the difference between contamination and irradiation. (2)",
                    marks(["<b>Contamination</b>: radioactive material is <b>on or in</b> the object (it becomes radioactive).",
                           "<b>Irradiation</b>: the object is <b>exposed to radiation</b> from an <b>external</b> source and does <b>not</b> become radioactive; it stops when the source is removed."]), lines=3),
            choice("ra-n8-q4", "Food is irradiated with gamma rays to kill bacteria. Does the food become radioactive?",
                   ["Yes, slightly", "No — irradiation does not make the object radioactive", "Yes, for one half-life", "Only if it is contaminated"], 1,
                   "Irradiation = exposure; no radioactive material is left in the food."),
            written("ra-n8-q5", "Explain why gamma sources are more hazardous than alpha sources for irradiation, but alpha sources are more hazardous for contamination. (3)",
                    mark_scheme([
                        ("Irradiation", "Gamma <b>penetrates</b> the skin and reaches internal organs; alpha is <b>stopped by the skin</b>, so from outside it does little harm."),
                        ("Contamination", "Once inside the body, alpha is the <b>most ionising</b>, so it does the most damage to the cells around it."),
                        ("Link", "Gamma, being weakly ionising, mostly passes out of the body; and an internal source cannot be shielded."),
                    ]), lines=4),
            written("ra-n8-q6", "Give two precautions that limit the radiation dose to a patient having a tracer scan. (2)",
                    marks(["Use a tracer with a <b>short half-life</b> so the activity falls quickly after the scan / use the <b>smallest activity</b> that gives a clear image.",
                           "Only scan when the <b>benefit outweighs the risk</b>; keep a record of the patient's <b>total dose</b> (dose limits)."]), lines=2),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N9 · Uses
# ---------------------------------------------------------------------

USES_TABLE = (
    "<table class='tbl'><tr><th>Use</th><th>Radiation</th><th>Half-life</th><th>Why</th></tr>"
    "<tr><td><b>Smoke alarm</b> (americium-241)</td><td>alpha</td><td>long (hundreds of years)</td><td>alpha ionises the air between two plates so a small current flows; <b>smoke absorbs the alpha</b>, the current falls, the alarm sounds. Alpha is stopped by the casing and a few cm of air, so it is safe in the home; long half-life means it never needs replacing</td></tr>"
    "<tr><td><b>Irradiating food</b> / <b>sterilising</b> medical equipment</td><td>gamma</td><td>long</td><td>gamma <b>penetrates the packaging</b> and <b>kills microbes</b> inside it; the food/instrument is irradiated, not contaminated, so it does not become radioactive</td></tr>"
    "<tr><td><b>Medical tracer</b> (technetium-99m)</td><td>gamma</td><td>short (hours)</td><td>gamma <b>passes out of the body</b> to be detected by a gamma camera; weakly ionising, so little damage; short half-life so the patient's dose soon falls</td></tr>"
    "<tr><td><b>Industrial tracer</b> (finding a leak in a pipe)</td><td>gamma</td><td>short (days)</td><td>detected through the soil above the pipe; decays away afterwards</td></tr>"
    "<tr><td><b>Thickness gauging</b> (paper, foil)</td><td>beta</td><td>long</td><td>beta is <b>partly absorbed</b> by the sheet: thicker → fewer counts get through → rollers adjust. Alpha would all be stopped, gamma would all get through; long half-life so the reading does not drift</td></tr>"
    "<tr><td><b>Diagnosing cancer</b> (PET, tracers)</td><td>β⁺ → gamma</td><td>short</td><td>T6</td></tr>"
    "<tr><td><b>Treating cancer</b></td><td>gamma beams from outside; beta/alpha sources placed inside</td><td>—</td><td>ionising radiation <b>kills the tumour cells</b>; T5</td></tr></table>"
)

section_n9 = section(
    "uses-radioactivity", "nn", "Uses of radioactivity in the home, industry and medicine", "6.28",
    equations=[r"\text{choose by: type (penetration, ionisation) and half-life}"],
    blurb="Each use picks a radiation for its penetration and a half-life for how long the source needs to last. Learn the use, the radiation, the half-life and the reason together — the reason is where the marks are.",
    checklist=[
        "Describe the spec uses: smoke alarms, irradiating food, sterilising equipment, tracers, gauging, diagnosing and treating cancer",
        "For each, state the type of radiation and the half-life, with the reason",
        "Explain how a smoke alarm and a thickness gauge work",
    ],
    parts=[
        explain("The uses", USES_TABLE),
        worked(
            "Explaining a choice",
            "Explain why americium-241, an alpha emitter with a half-life of 432 years, is suitable for a smoke alarm. (3 marks)",
            [
                "<b>Alpha and the job:</b> alpha is <b>strongly ionising</b>, so it ionises the air in the detector and a current flows; <b>smoke absorbs</b> the alpha particles, the current drops and the alarm sounds.",
                "<b>Alpha and safety:</b> alpha is <b>stopped by a few cm of air</b> and the plastic casing, so it cannot reach people in the room.",
                "<b>Half-life:</b> a <b>long</b> half-life means the activity stays almost constant for the life of the alarm — it does not need replacing.",
            ],
        ),
        practice("Uses", [
            written("ra-n9-q1", "Explain how a smoke alarm uses an alpha source to detect smoke. (3)",
                    mark_scheme([
                        ("Ionises", "The alpha particles <b>ionise the air</b> between two charged plates, so a small <b>current flows</b>."),
                        ("Smoke", "<b>Smoke particles absorb</b> the alpha particles (or the ions), so <b>fewer ions</b> reach the plates…"),
                        ("Alarm", "…the <b>current falls</b>, and the circuit sounds the alarm."),
                    ]), lines=4),
            choice("ra-n9-q2", "Which source is best for a tracer injected into a patient?",
                   ["An alpha emitter with a long half-life", "A gamma emitter with a short half-life", "A beta emitter with a long half-life", "A gamma emitter with a very long half-life"], 1,
                   "Gamma gets out of the body to the detector; a short half-life limits the dose."),
            written("ra-n9-q3", "Explain why a beta source, not an alpha or gamma source, is used to monitor the thickness of paper in a paper mill. (3)",
                    mark_scheme([
                        ("Beta", "Beta is <b>partly absorbed</b> by paper, so the count rate reaching the detector <b>changes with thickness</b>."),
                        ("Alpha", "Alpha would be <b>completely stopped</b> by any thickness of paper — no change to detect."),
                        ("Gamma", "Gamma would <b>pass straight through</b> whatever the thickness — no change to detect."),
                    ]), lines=4),
            written("ra-n9-q4", "Explain why gamma rays are used to sterilise surgical instruments in sealed packets. (2)",
                    marks(["Gamma <b>penetrates the packaging</b> and <b>kills microbes</b> (bacteria) on the instruments inside.",
                           "The instruments are only <b>irradiated</b>, so they do not become radioactive and stay sterile in the sealed packet."]), lines=3),
            written("ra-n9-q5", "A radioactive tracer is used to find a leak in an underground water pipe. Explain the choice of radiation and half-life. (3)",
                    mark_scheme([
                        ("Gamma", "<b>Gamma</b>, because it <b>penetrates the soil</b> and can be detected at the surface (alpha and beta would be absorbed)."),
                        ("Where", "The count rate is <b>highest above the leak</b>, where the tracer collects."),
                        ("Half-life", "A <b>short</b> half-life (days), so the water is not left radioactive for long — but long enough to complete the search."),
                    ]), lines=4),
            choice("ra-n9-q6", "Why does a thickness gauge need a source with a long half-life?",
                   ["So that it is safer", "So that the activity stays constant and the reading does not drift", "So that it is more penetrating", "So that it is cheaper"], 1,
                   "If the activity fell during use, a falling count would look like thicker paper."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N10 · Key words
# ---------------------------------------------------------------------

DEFINITIONS = [
    ("Isotopes", "Atoms of the <b>same element</b> (same number of protons) with <b>different numbers of neutrons</b>.", "\"different versions of an atom\""),
    ("Atomic (proton) number", "The number of <b>protons</b> in the nucleus.", "the number of particles"),
    ("Mass (nucleon) number", "The number of <b>protons plus neutrons</b> in the nucleus.", "the mass in grams"),
    ("Ion", "An atom that has <b>lost or gained electrons</b> and so has a charge (positive if it has lost them).", "\"a charged particle\" with no cause"),
    ("Ionising radiation", "Radiation with enough energy to <b>knock electrons out of atoms</b>, forming ions.", "\"radioactive radiation\""),
    ("Alpha particle", "A <b>helium nucleus</b>: two protons and two neutrons, charge +2.", "\"a helium atom\""),
    ("Beta-minus particle", "A fast <b>electron emitted from the nucleus</b> when a neutron turns into a proton.", "\"an electron from the shell\""),
    ("Gamma ray", "High-frequency <b>electromagnetic radiation</b> emitted from the nucleus.", "\"a particle\""),
    ("Positron", "The antiparticle of the electron: same mass, charge <b>+1</b>; emitted in β⁺ decay.", "\"a positive electron in the shell\""),
    ("Background radiation", "Low-level ionising radiation that is <b>always present</b> in the environment (rocks, radon, cosmic rays, food, medical).", "\"radiation from nuclear power\""),
    ("Activity", "The <b>number of decays per second</b> of a source, in becquerels (Bq).", "\"how radioactive it is\""),
    ("Becquerel", "<b>One decay per second</b>.", "\"a unit of radiation\""),
    ("Half-life", "The <b>time for half the undecayed nuclei to decay</b> (or for the activity to halve).", "\"half the life of the source\""),
    ("Random (decay)", "It <b>cannot be predicted which nucleus will decay or when</b>.", "\"it happens by chance sometimes\""),
    ("Count rate", "The number of <b>counts per second (or minute)</b> recorded by a detector.", "confusing it with activity (it is only the radiation that reaches the detector)"),
    ("Irradiation", "<b>Exposure</b> to radiation from an <b>external</b> source; the object does <b>not</b> become radioactive.", "\"being radiated\""),
    ("Contamination", "Radioactive material getting <b>on or in</b> an object, which then <b>stays radioactive</b>.", "\"being near radiation\""),
    ("Nuclear fission", "A <b>large nucleus splits</b> into two smaller nuclei and neutrons, releasing energy (P).", "\"an atom exploding\""),
    ("Nuclear fusion", "Two <b>small nuclei join</b> to form a larger nucleus, with a loss of mass and a release of energy (P).", "\"atoms joining\" — say nuclei"),
    ("Chain reaction", "Neutrons from one fission go on to cause <b>further fissions</b> (P).", "\"a big explosion\""),
]


def definitions_table():
    html = "<table class='tbl'><tr><th>Term</th><th>What to write (mark-scheme form)</th><th>Not this</th></tr>"
    for term, definition, wrong in DEFINITIONS:
        html += "<tr><td><b>" + term + "</b></td><td>" + definition + "</td><td>" + wrong + "</td></tr>"
    html += "</table>"
    return html


section_keywords = section(
    "keywords-radioactivity", "nn", "Key words: state what is meant by…", "6",
    equations=[r"\text{definition, word for word}"],
    blurb="One-mark definitions in the form of words the mark schemes credit. The bold words are the ones the marks are attached to.",
    checklist=[
        "Define isotope, atomic number, mass number, ion and ionising",
        "Define activity, becquerel, half-life, count rate and background radiation",
        "Define irradiation and contamination (and, for Physics, fission, fusion and chain reaction)",
    ],
    parts=[
        explain("The definitions", "<p>\"<b>State what is meant by</b>\" asks for the definition. Learn these as sentences.</p>" + definitions_table()),
        practice("Key words", [
            written("ra-kw-q1", "State what is meant by the half-life of a radioactive source. (1)",
                    marks(["The <b>time taken for half of the undecayed nuclei to decay</b> (or for the activity to fall to half)."]), lines=2),
            written("ra-kw-q2", "State what is meant by an isotope. (1)",
                    marks(["Atoms of the <b>same element</b> (same proton number) with <b>different numbers of neutrons</b>."]), lines=2),
            written("ra-kw-q3", "State what is meant by irradiation. (1)",
                    marks(["Being <b>exposed to radiation</b> from an <b>external</b> source, without the object becoming radioactive."]), lines=2),
            choice("ra-kw-q4", "Which is the correct definition of activity?",
                   ["The energy of the radiation", "The number of decays per second", "The half-life", "The number of nuclei in the source"], 1,
                   "Activity = decays per second, in Bq."),
            written("ra-kw-q5", "State what is meant by background radiation. (1)",
                    marks(["Low-level ionising radiation that is <b>always present</b> in the environment, from natural (and some artificial) sources."]), lines=2),
            written("ra-kw-q6", "State what is meant by the mass number of a nucleus. (1)",
                    marks(["The total number of <b>protons and neutrons</b> (nucleons) in the nucleus."]), lines=2),
            choice("ra-kw-q7", "A student writes \"a beta particle is an electron from the outer shell of the atom\". What is wrong?",
                   ["Nothing", "A beta-minus particle is an electron emitted from the nucleus, created when a neutron turns into a proton", "Beta particles are protons", "Beta particles are waves"], 1,
                   "The electron comes from the nucleus, not the shells."),
            written("ra-kw-q8", "State what is meant by contamination. (1)",
                    marks(["Radioactive material getting <b>on or into</b> an object (or person), which then <b>emits radiation</b> itself."]), lines=2),
        ]),
    ],
)

FACTS_KW = [fact("State what is meant by: " + term.lower() + ".", definition, "keywords-radioactivity") for term, definition, wrong in DEFINITIONS]

SECTIONS = [section_n6, section_n7, section_n8, section_n9, section_keywords]
