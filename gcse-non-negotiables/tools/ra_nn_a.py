"""
ra_nn_a.py — Topic 6 (Radioactivity): the non-negotiables N1–N5.

N1 The atom                     N4 Alpha, beta, gamma and neutrons
N2 Isotopes and notation        N5 Background radiation and detection
N3 Electrons, energy levels and ions
"""

from revlib import (
    choice, diagram, explain, mark_scheme, marks, numeric, practice, section,
    worked, written,
)
import ra_diagrams as dg

# ---------------------------------------------------------------------
# N1 · The atom
# ---------------------------------------------------------------------

section_n1 = section(
    "atom", "nn", "The atom: nucleus, electrons, sizes, masses and charges", "6.1, 6.2, 6.5, 6.6",
    equations=[r"\text{atom} \approx 10^{-10}\ \text{m}", r"\text{nucleus} \approx 10^{-15}\ \text{m}", r"p: +1, 1 \quad n: 0, 1 \quad e^{-}: -1, \tfrac{1}{1836}"],
    blurb="A tiny, dense, positive nucleus of protons and neutrons, with electrons orbiting far outside it. Almost all the mass is in the nucleus; almost all the volume is empty space.",
    checklist=[
        "Describe the structure of the atom and state the typical size of an atom",
        "Recall the relative masses and charges of the proton, neutron, electron and positron",
        "Explain why an atom is neutral",
    ],
    parts=[
        explain(
            "Structure and numbers",
            "<p>An atom has a <b>positively charged nucleus</b> made of <b>protons and neutrons</b>, surrounded by <b>negatively charged electrons</b>. The nucleus is <b>very much smaller than the atom</b> — ten to a hundred thousand times smaller across — but contains <b>almost all of its mass</b>.</p>"
            "<p><b>Sizes:</b> an atom (and a small molecule) is about $1 \\times 10^{-10}$ m across (0.1 nm); the nucleus about $1 \\times 10^{-15}$ m. The 2022 report: converting 0.15 nm to $1.5 \\times 10^{-10}$ m \"was difficult\" — nano is $10^{-9}$.</p>"
            "<table class='tbl'><tr><th>Particle</th><th>Relative mass</th><th>Relative charge</th><th>Where</th></tr>"
            "<tr><td><b>Proton</b></td><td>1</td><td>+1</td><td>nucleus</td></tr>"
            "<tr><td><b>Neutron</b></td><td>1</td><td>0</td><td>nucleus</td></tr>"
            "<tr><td><b>Electron</b></td><td>about 1/1836 (negligible, ≈ 0.0005)</td><td>−1</td><td>orbiting the nucleus</td></tr>"
            "<tr><td><b>Positron</b></td><td>same as an electron</td><td>+1</td><td>emitted in β⁺ decay</td></tr></table>"
            "<p>In a neutral atom the <b>number of protons equals the number of electrons</b>, so the positive and negative charges cancel. The number of protons is what makes an element that element: every nucleus of a given element has the same positive charge.</p>",
        ),
        worked(
            "Why the atom is neutral",
            "A neutral atom of carbon has 6 protons. State how many electrons it has, and explain why the atom has no overall charge. (2 marks)",
            [
                "<b>Number:</b> <b>6 electrons</b> — in a neutral atom the number of electrons equals the number of protons.",
                "<b>Why neutral:</b> each proton has a charge of <b>+1</b> and each electron <b>−1</b>, so 6 of each give a <b>total charge of zero</b>.",
            ],
        ),
        practice("The atom", [
            choice("ra-n1-q1", "Which statement about the nucleus is correct?",
                   ["It contains protons and electrons", "It is about the same size as the atom", "It contains almost all the atom's mass and is positively charged", "It has no charge"], 2,
                   "Protons and neutrons; tiny; positive; almost all the mass."),
            written("ra-n1-q2", "State the relative mass and relative charge of a proton, a neutron and an electron. (3)",
                    marks(["Proton: mass <b>1</b>, charge <b>+1</b>.", "Neutron: mass <b>1</b>, charge <b>0</b>.", "Electron: mass <b>about 1/1836</b> (very small), charge <b>−1</b>."]), lines=3),
            choice("ra-n1-q3", "What is the typical size of an atom?",
                   ["1 × 10⁻¹⁵ m", "1 × 10⁻¹⁰ m", "1 × 10⁻⁶ m", "1 × 10⁻³ m"], 1,
                   "About 10⁻¹⁰ m (0.1 nm); the nucleus is about 10⁻¹⁵ m."),
            numeric("ra-n1-q4", "The diameter of an atom is 0.15 nm. Write this in metres. Type the answer as 1.5e-10.", 1.5e-10, "m",
                    "nano = 10⁻⁹.", [r"$0.15\ \text{nm} = 0.15 \times 10^{-9} = 1.5 \times 10^{-10}$ m."]),
            written("ra-n1-q5", "Compare a positron with an electron. (2)",
                    marks(["<b>Same mass</b> (about 1/1836 of a proton).", "<b>Opposite charge</b>: the positron is <b>+1</b>, the electron −1."]), lines=2),
            written("ra-n1-q6", "Explain why an atom has no overall electric charge. (2)",
                    marks(["It has <b>equal numbers of protons and electrons</b>.", "Each proton's +1 charge is cancelled by an electron's −1 charge, so the <b>total is zero</b>."]), lines=2),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N2 · Isotopes and notation
# ---------------------------------------------------------------------

section_n2 = section(
    "isotopes", "nn", "Isotopes and nuclide notation", "6.3, 6.4",
    equations=[r"{}^{A}_{Z}\mathrm{X}", r"A = \text{protons} + \text{neutrons}", r"\text{neutrons} = A - Z"],
    blurb="Every nucleus is written with its mass number on top and its atomic number below. Isotopes of an element have the same atomic number but different mass numbers — same protons, different neutrons.",
    checklist=[
        "Read A and Z from nuclide notation and find protons, neutrons and electrons",
        "Define isotope in the mark-scheme form",
        "Explain why isotopes of an element have the same chemical properties but different masses",
    ],
    parts=[
        explain(
            "A, Z and isotopes",
            "<p>$${}^{A}_{Z}\\mathrm{X} \\qquad A = \\text{mass (nucleon) number} = \\text{protons} + \\text{neutrons} \\qquad Z = \\text{atomic (proton) number} = \\text{protons}$$</p>"
            "<p>So <b>neutrons = A − Z</b>, and in a neutral atom <b>electrons = Z</b>. ${}^{14}_{6}\\mathrm{C}$: 6 protons, 8 neutrons, 6 electrons.</p>"
            "<p><b>Isotopes</b> are atoms of the <b>same element</b> (same number of protons, same atomic number) with <b>different numbers of neutrons</b> (different mass numbers). ${}^{12}_{6}\\mathrm{C}$ and ${}^{14}_{6}\\mathrm{C}$ are isotopes of carbon. Because the nucleus of every atom of an element has the same positive charge (same Z), isotopes have the same electrons and the same <b>chemical</b> properties; they differ in <b>mass</b> and, often, in stability — the heavier isotope is frequently radioactive.</p>"
            "<p>The June 2023 scheme (Q7(a)(i)) rejected every option that did not have the <b>same atomic number</b> as the given element: that is the whole test.</p>",
        ),
        worked(
            "Reading a nuclide",
            "Uranium-235 is written ²³⁵₉₂U. State the number of protons, neutrons and electrons in a neutral atom. (2 marks)",
            [
                "<b>Protons:</b> Z = <b>92</b>. <b>Electrons:</b> also 92 (neutral atom).",
                "<b>Neutrons:</b> A − Z = 235 − 92 = <b>143</b>.",
            ],
        ),
        practice("Isotopes", [
            written("ra-n2-q1", "State what is meant by isotopes. (2)",
                    marks(["Atoms of the <b>same element</b> — the <b>same number of protons</b> (atomic number)…", "…with <b>different numbers of neutrons</b> (different mass numbers)."]), lines=2),
            choice("ra-n2-q2", "Which nucleus is an isotope of ¹⁴₇N?",
                   ["¹⁴₆C", "¹⁵₇N", "¹⁴₈O", "¹³₆C"], 1,
                   "Same atomic number (7 = nitrogen), different mass number."),
            numeric("ra-n2-q3", "How many neutrons are in a nucleus of ⁶⁰₂₇Co?", 33, "", "A − Z.", [r"$60 - 27 = 33$ neutrons."]),
            written("ra-n2-q4", "Explain why ³⁵Cl and ³⁷Cl have the same chemical properties but different masses. (2)",
                    marks(["Same number of <b>protons</b> (17), so the same number of <b>electrons</b>, which decide the chemistry.",
                           "Different numbers of <b>neutrons</b> (18 and 20), so different mass numbers."]), lines=3),
            choice("ra-n2-q5", "In the notation ᴬ_Z X, what does A stand for?",
                   ["The number of protons", "The number of neutrons", "The number of protons plus neutrons (mass number)", "The number of electrons"], 2,
                   "A is the nucleon (mass) number; Z is the proton (atomic) number."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N3 · Electrons, energy levels, ions
# ---------------------------------------------------------------------

section_n3 = section(
    "electrons-ions", "nn", "Electrons: set orbits, absorbing and emitting, and ions", "6.7, 6.8, 6.9",
    equations=[r"\text{absorb EM} \rightarrow \text{higher orbit}", r"\text{emit EM} \rightarrow \text{lower orbit}", r"\text{lose an electron} \rightarrow \text{positive ion}"],
    blurb="Electrons sit in orbits at set distances from the nucleus. They move up when they absorb electromagnetic radiation and down when they emit it; knock one out altogether and you have a positive ion — which is what ionising radiation does.",
    checklist=[
        "State that electrons orbit at set distances (energy levels) from the nucleus",
        "Describe how absorbing or emitting EM radiation moves an electron between orbits",
        "Explain how an atom becomes a positive ion, and link it to ionising radiation",
    ],
    parts=[
        explain(
            "Levels and ions",
            "<p>In an atom the electrons orbit the nucleus at <b>different set distances</b> — energy levels (the Bohr model, T1). An electron can only sit in one of these levels, not in between.</p>"
            "<p>An electron moves to a <b>higher orbit</b> (further from the nucleus) when the atom <b>absorbs</b> electromagnetic radiation of the right energy. It falls back to a <b>lower orbit</b> by <b>emitting</b> electromagnetic radiation. This is why hot gases give out light of particular colours (and how fluorescence works, Topic 5).</p>"
            "<p>If an outer electron gains enough energy it <b>leaves the atom altogether</b>. The atom now has more protons than electrons: it is a <b>positive ion</b>. Anything that knocks electrons out of atoms is <b>ionising</b> — alpha, beta and gamma radiation, X-rays and ultraviolet. The June 2024 scheme (Q8(b)): ionisation is the <b>loss (or gain) of electrons</b> from atoms; \"knocking electrons out\" accepted.</p>",
        ),
        worked(
            "Ionisation by an alpha particle",
            "An alpha particle passes close to an atom and the atom becomes a positive ion. Explain how. (2 marks)",
            [
                "<b>What happens:</b> the alpha particle transfers energy to an <b>outer electron</b>, which <b>leaves the atom</b> (is knocked out).",
                "<b>Why positive:</b> the atom now has <b>more protons than electrons</b>, so it has an overall <b>positive charge</b> — a positive ion. The alpha particle loses a little energy each time, which is why it is stopped by a few cm of air.",
            ],
        ),
        practice("Electrons and ions", [
            written("ra-n3-q1", "Describe what happens to an electron in an atom when the atom absorbs electromagnetic radiation. (1)",
                    marks(["The electron moves to a <b>higher orbit / energy level</b> (further from the nucleus)."]), lines=2),
            written("ra-n3-q2", "State what is meant by ionisation. (1)",
                    marks(["An atom <b>losing (or gaining) an electron</b>, so that it becomes charged (an ion); for ionising radiation, electrons are knocked out leaving a positive ion."]), lines=2),
            choice("ra-n3-q3", "An atom emits electromagnetic radiation. Which has happened?",
                   ["An electron has moved to a higher orbit", "An electron has moved to a lower orbit", "A proton has left the nucleus", "The atom has gained an electron"], 1,
                   "Falling to a lower level releases energy as EM radiation."),
            written("ra-n3-q4", "Explain how an atom can become a positive ion. (2)",
                    marks(["An outer electron gains enough energy (e.g. from ionising radiation) to <b>leave the atom</b>.",
                           "The atom is left with <b>more protons than electrons</b>, so it is <b>positively charged</b>."]), lines=2),
            choice("ra-n3-q5", "Why are alpha, beta and gamma called ionising radiation?",
                   ["They are radioactive", "They have enough energy to knock electrons out of atoms, forming ions", "They come from the nucleus", "They travel at the speed of light"], 1,
                   "Ionising = removes electrons from atoms."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N4 · Alpha, beta, gamma, neutrons
# ---------------------------------------------------------------------

RADIATION_TABLE = (
    "<table class='tbl'><tr><th></th><th>Alpha α</th><th>Beta-minus β⁻</th><th>Beta-plus β⁺</th><th>Gamma γ</th><th>Neutron n</th></tr>"
    "<tr><td><b>What it is</b></td><td>a <b>helium nucleus</b>: 2 protons + 2 neutrons</td><td>a fast <b>electron</b> emitted from the nucleus</td><td>a <b>positron</b> emitted from the nucleus</td><td><b>electromagnetic</b> radiation (a wave, no mass, no charge)</td><td>a neutron</td></tr>"
    "<tr><td><b>Symbol</b></td><td>${}^{4}_{2}\\mathrm{He}$ or ${}^{4}_{2}\\alpha$</td><td>${}^{\\;0}_{-1}\\mathrm{e}$ or ${}^{\\;0}_{-1}\\beta$</td><td>${}^{0}_{+1}\\mathrm{e}$</td><td>${}^{0}_{0}\\gamma$</td><td>${}^{1}_{0}\\mathrm{n}$</td></tr>"
    "<tr><td><b>Charge</b></td><td>+2</td><td>−1</td><td>+1</td><td>0</td><td>0</td></tr>"
    "<tr><td><b>Ionising power</b></td><td><b>strongest</b></td><td>medium</td><td>medium</td><td><b>weakest</b></td><td>—</td></tr>"
    "<tr><td><b>Penetration</b></td><td>a few <b>cm of air</b>; stopped by <b>paper</b> or skin</td><td>about a metre of air; stopped by a few <b>mm of aluminium</b></td><td>as β⁻ (but soon annihilates)</td><td>very far in air; <b>reduced</b> by thick <b>lead</b> or metres of concrete, never fully stopped</td><td>very penetrating</td></tr>"
    "<tr><td><b>Why</b></td><td>big and doubly charged: ionises a lot, loses energy fast</td><td>small and singly charged</td><td></td><td>no charge, no mass: rarely interacts</td><td>no charge</td></tr></table>"
)

section_n4 = section(
    "radiation-types", "nn", "Alpha, beta, gamma (and neutrons)", "6.10, 6.11, 6.15, 6.16",
    equations=[r"\alpha = {}^{4}_{2}\mathrm{He}", r"\beta^{-} = {}^{\;0}_{-1}\mathrm{e}", r"\gamma = \text{EM wave}"],
    blurb="Unstable nuclei emit alpha particles, beta particles (minus or plus), gamma rays or neutrons, at random. Know what each one is, how far it gets, and how strongly it ionises — the three columns that every comparison question is marked on.",
    checklist=[
        "State what alpha, beta and gamma radiation are made of",
        "Compare their penetration (paper, aluminium, lead) and ionising power",
        "State that emission is a random process from unstable nuclei",
    ],
    parts=[
        explain(
            "The table",
            diagram(dg.penetration_svg(), 500, 270, "Penetration: alpha is stopped by paper, beta by a few millimetres of aluminium, gamma only reduced by thick lead. Ionising power runs the opposite way.") +
            RADIATION_TABLE +
            "<p>Radiation is emitted from <b>unstable nuclei</b> in a <b>random</b> process: you cannot say which nucleus will decay next or when (N7). All of alpha, β⁻, β⁺ and gamma are <b>ionising</b>.</p>"
            "<p><b>Why penetration and ionisation are opposites:</b> an alpha particle is large and carries +2, so it ionises almost every atom it passes, losing its energy within a few centimetres. A gamma ray has no charge and no mass, so it rarely interacts — it ionises little and travels far. The June 2024 scheme (Q8(a)): the charge on an alpha particle is <b>+2</b>.</p>"
            "<p>\"Alpha is stopped by paper\" scores; \"alpha is the weakest\" does not — say <b>least penetrating</b> or <b>most ionising</b>, never \"strongest\" or \"weakest\".</p>",
        ),
        worked(
            "Comparing two radiations",
            "Compare alpha and gamma radiation. (4 marks)",
            [
                "<b>Nature:</b> alpha is a <b>helium nucleus</b> (2 protons, 2 neutrons, charge +2); gamma is an <b>electromagnetic wave</b> with no mass or charge.",
                "<b>Ionising:</b> alpha is <b>strongly</b> ionising; gamma is <b>weakly</b> ionising.",
                "<b>Penetration:</b> alpha travels a few cm in air and is stopped by paper; gamma travels far and is only reduced by thick lead.",
                "<b>Effect on the nucleus</b> (what the June 2025 6-marker wanted): alpha emission reduces the mass number by 4 and the atomic number by 2 — a new element; gamma emission <b>changes neither</b> — the nucleus just loses energy.",
            ],
        ),
        practice("Types of radiation", [
            written("ra-n4-q1", "State what an alpha particle, a beta particle and a gamma ray each consist of. (3)",
                    marks(["Alpha: a <b>helium nucleus</b> — two protons and two neutrons.", "Beta(-minus): a fast-moving <b>electron</b> emitted from the nucleus.", "Gamma: <b>electromagnetic radiation</b> (a high-frequency wave)."]), lines=3),
            choice("ra-n4-q2", "A source is placed near a detector. The count falls to background when a sheet of paper is put in the way. What is the source emitting?",
                   ["Alpha only", "Beta only", "Gamma only", "Beta and gamma"], 0,
                   "Only alpha is stopped by paper."),
            choice("ra-n4-q3", "Which radiation is the most ionising?",
                   ["Alpha", "Beta", "Gamma", "They are all the same"], 0,
                   "Big, slow and doubly charged: alpha ionises most and penetrates least."),
            written("ra-n4-q4", "Explain why alpha radiation is strongly ionising but only travels a few centimetres in air. (2)",
                    marks(["It is relatively <b>large and has a +2 charge</b>, so it pulls electrons off almost every atom it passes — strongly ionising.",
                           "Each ionisation <b>transfers some of its energy</b>, so it soon loses all its energy and stops."]), lines=3),
            choice("ra-n4-q5", "What is the charge on an alpha particle?",
                   ["0", "+1", "+2", "−1"], 2,
                   "Two protons, no electrons: +2."),
            written("ra-n4-q6", "A source emits beta and gamma radiation. Describe how you could show, using absorbers and a detector, that it emits both. (3)",
                    mark_scheme([
                        ("Baseline", "Measure the <b>count rate</b> with nothing in the way (and subtract background)."),
                        ("Aluminium", "Put a few mm of <b>aluminium</b> between source and detector: the count <b>falls</b> but does not reach background — the beta has been stopped, something more penetrating remains."),
                        ("Lead", "Put thick <b>lead</b> in the way: the count falls again (towards background) — that remaining radiation is <b>gamma</b>."),
                    ]), lines=4),
            written("ra-n4-q7", "State what is meant by saying radioactive decay is a random process. (1)",
                    marks(["It <b>cannot be predicted which nucleus will decay next, or when</b> a particular nucleus will decay."]), lines=2),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N5 · Background radiation and detection
# ---------------------------------------------------------------------

section_n5 = section(
    "background", "nn", "Background radiation and how radiation is detected", "6.12, 6.13, 6.14",
    equations=[r"\text{corrected count rate} = \text{measured} - \text{background}"],
    blurb="There is always some ionising radiation around us — from rocks, the air, space, food and medicine. A Geiger–Müller tube counts it; photographic film darkens in it. Any measurement of a source must have the background taken off.",
    checklist=[
        "State what background radiation is and give sources from the Earth and from space",
        "Describe how a GM tube and photographic film detect radiation",
        "Describe how to measure the background count and use it to correct a reading",
    ],
    parts=[
        explain(
            "Where it comes from, how it is detected",
            "<p><b>Background radiation</b> is the low-level ionising radiation that is <b>always present</b> in the environment, from natural and artificial sources.</p>"
            "<table class='tbl'><tr><th>From the Earth</th><th>From space</th><th>Artificial</th></tr>"
            "<tr><td><b>radon gas</b> from rocks and soil (the largest share in the UK); <b>rocks and building materials</b> (granite); <b>food and drink</b> (potassium-40 in bananas, Brazil nuts)</td><td><b>cosmic rays</b> — high-energy particles from the Sun and beyond, more at altitude and in aircraft</td><td><b>medical</b> X-rays and scans (the largest artificial share); nuclear industry and weapons-test fallout (tiny)</td></tr></table>"
            "<p><b>Detecting it.</b> A <b>Geiger–Müller (GM) tube</b> with a counter: each ionising particle or ray entering the tube ionises the gas inside, giving a pulse of current that is counted — the reading is a <b>count rate</b> in counts per second or per minute. <b>Photographic film</b> is <b>darkened</b> (fogged) by ionising radiation, the more radiation the darker — film badges worn by radiographers show the dose they have received.</p>"
            "<p><b>Measuring the background count</b> (June 2024 Q8(c), 3 marks): use a GM tube and counter with <b>no source nearby</b>; <b>count for a measured time</b> (several minutes, because the counts are random); <b>divide counts by time</b>; <b>repeat and average</b>. Then subtract it from every reading taken with a source: <b>corrected count rate = measured count rate − background count rate</b>.</p>",
        ),
        worked(
            "Correcting a count",
            "With no source present a GM tube records 90 counts in 5 minutes. With a source in place it records 420 counts per minute. Calculate the corrected count rate of the source.",
            [
                r"<b>Background rate:</b> $90 \div 5 = 18$ counts per minute.",
                r"<b>Corrected:</b> $420 - 18 = 402$ counts per minute. (Subtracting 90 instead of 18 — mixing counts with counts per minute — is the common slip.)",
            ],
        ),
        practice("Background and detection", [
            written("ra-n5-q1", "State what is meant by background radiation, and give two natural sources. (3)",
                    marks(["Low-level ionising radiation that is <b>always present</b> in the environment.", "Source 1: <b>radon gas</b> from rocks / rocks and soil / food and drink.", "Source 2: <b>cosmic rays</b> from space."]), lines=3),
            choice("ra-n5-q2", "Which is the largest source of background radiation for most people in the UK?",
                   ["Nuclear power stations", "Radon gas from the ground", "Cosmic rays", "Mobile phones"], 1,
                   "Radon seeping from rocks and soil is about half the UK average dose; medical is the biggest artificial source."),
            written("ra-n5-q3", "Describe how to measure the background count rate in a laboratory. (3)",
                    mark_scheme([
                        ("Equipment", "Use a <b>GM tube and counter</b> with <b>no radioactive sources nearby</b>."),
                        ("Count", "Record the number of <b>counts in a measured time</b> (several minutes) and <b>divide by the time</b>."),
                        ("Repeat", "<b>Repeat</b> (in different places / times) and <b>calculate a mean</b>, because the counts arrive at random."),
                    ]), lines=4),
            numeric("ra-n5-q4", "The background count rate is 20 counts per minute. A source gives a reading of 260 counts per minute. Calculate the corrected count rate.", 240, "counts/min",
                    "Subtract the background.", [r"$260 - 20 = 240$ counts per minute."]),
            written("ra-n5-q5", "Describe how photographic film can be used to monitor the radiation dose of a hospital worker. (2)",
                    marks(["The film is worn in a <b>badge</b>; ionising radiation <b>darkens (fogs)</b> the film.",
                           "When developed, the <b>darker</b> the film the <b>greater the dose</b> received; windows of different absorbers show which type of radiation."]), lines=3),
            written("ra-n5-q6", "Explain why readings of a weak source should be taken over a long time and repeated. (2)",
                    marks(["Decay (and background) is <b>random</b>, so the count in a short time varies a lot from one measurement to the next.",
                           "A <b>long count and a mean of repeats</b> averages out the random variation and gives a more accurate count rate."]), lines=3),
        ]),
    ],
)

SECTIONS = [section_n1, section_n2, section_n3, section_n4, section_n5]
