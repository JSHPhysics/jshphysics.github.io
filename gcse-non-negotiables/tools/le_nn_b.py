"""
le_nn_b.py — Topic 5 (Light and the EM spectrum): the non-negotiables N7–N11.

N7  The EM spectrum            N10 Radiation and temperature
N8  Uses                       N11 Key words
N9  Dangers
"""

from revlib import (
    choice, diagram, explain, fact, mark_scheme, marks, practice, section,
    worked, written,
)
import le_diagrams as dg

# ---------------------------------------------------------------------
# N7 · The spectrum
# ---------------------------------------------------------------------

section_n7 = section(
    "spectrum", "nn", "The electromagnetic spectrum", "5.10, 5.11, 5.12",
    equations=[r"\text{radio, micro, IR, visible, UV, X, gamma}", r"f \uparrow\ \lambda \downarrow\ \text{left to right}"],
    blurb="One continuous family of waves, grouped by wavelength. Learn the order both ways, and which way frequency, wavelength, energy and danger run.",
    checklist=[
        "Recall the seven groups in order of increasing frequency (and the reverse)",
        "State that the spectrum is continuous and that the groups overlap at their edges",
        "State the order of the colours of visible light and that our eyes detect only this narrow range",
    ],
    parts=[
        explain(
            "The order and the trends",
            diagram(dg.spectrum_svg(), 460, 225, "The electromagnetic spectrum in order of increasing frequency: radio, microwaves, infrared, visible, ultraviolet, X-rays, gamma rays. Wavelength runs the other way.") +
            "<p>A mnemonic for increasing frequency: <b>R</b>aging <b>M</b>artians <b>I</b>nvaded <b>V</b>enus <b>U</b>sing <b>X</b>-ray <b>G</b>uns. Radio waves have the longest wavelength (metres to kilometres) and lowest frequency; gamma rays the shortest wavelength (smaller than an atom) and highest frequency.</p>"
            "<p>The spectrum is <b>continuous</b>: there are no gaps, and the groups <b>overlap</b> at their boundaries — a wave at the edge of the microwave region could equally be called a short radio wave. The names are groupings by wavelength, nothing more.</p>"
            "<p><b>Visible light</b> is the narrow band our eyes can detect, from <b>red</b> (longest wavelength, about 700 nm, lowest frequency) through orange, yellow, green, blue, indigo to <b>violet</b> (shortest, about 400 nm). Everything else in the spectrum is invisible to us, which is why we need detectors (aerials, thermal cameras, film) for the rest.</p>",
        ),
        worked(
            "Placing a wave",
            "Infrared, X-rays and radio waves are three parts of the spectrum. Put them in order of increasing wavelength and say which has the highest frequency. (2 marks)",
            [
                "<b>Increasing wavelength</b> is right-to-left on the spectrum: <b>X-rays, infrared, radio waves</b>.",
                "<b>Highest frequency</b> = shortest wavelength = <b>X-rays</b> (frequency and wavelength run opposite ways, since $v = f\\lambda$ with $v$ fixed).",
            ],
        ),
        practice("The spectrum", [
            choice("le-n7-q1", "Which list is in order of increasing frequency?",
                   ["gamma, X-rays, UV, visible, IR, microwaves, radio", "radio, microwaves, IR, visible, UV, X-rays, gamma", "radio, IR, microwaves, visible, X-rays, UV, gamma", "visible, UV, IR, X-rays, gamma, radio, microwaves"], 1,
                   "Radio has the lowest frequency, gamma the highest."),
            written("le-n7-q2", "State which part of the electromagnetic spectrum has the longest wavelength, and which has the highest frequency. (2)",
                    marks(["Longest wavelength: <b>radio waves</b>.", "Highest frequency: <b>gamma rays</b>."]), lines=2),
            choice("le-n7-q3", "Which colour of visible light has the shortest wavelength?",
                   ["Red", "Green", "Violet", "Yellow"], 2,
                   "Red is about 700 nm, violet about 400 nm."),
            written("le-n7-q4", "Explain what is meant by saying the electromagnetic spectrum is continuous. (1)",
                    marks(["There are <b>no gaps</b> between the groups — every wavelength from radio to gamma exists, and the named groups <b>overlap</b> at their edges."]), lines=2),
            choice("le-n7-q5", "Why can we not see infrared or ultraviolet?",
                   ["They are not electromagnetic waves", "Our eyes can only detect a limited range of frequencies (visible light)", "They travel too fast", "They have no energy"], 1,
                   "The eye detects only roughly 400–700 nm; IR and UV lie just outside that range."),
            choice("le-n7-q6", "Microwaves and infrared are next to each other on the spectrum. Which has the higher frequency?",
                   ["Microwaves", "Infrared", "They are equal", "It depends on the source"], 1,
                   "Infrared is further towards the gamma end, so higher frequency and shorter wavelength."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N8 · Uses
# ---------------------------------------------------------------------

USES_TABLE = (
    "<table class='tbl'><tr><th>Wave</th><th>Uses on the spec (5.22)</th><th>Why that wave</th></tr>"
    "<tr><td><b>Radio</b></td><td>broadcasting (TV, radio), communications, satellite transmissions</td><td>long wavelength: travels far, passes through walls, diffracts round hills; easy to produce with an aerial</td></tr>"
    "<tr><td><b>Microwaves</b></td><td>cooking, communications (mobile phones, Wi-Fi), satellite transmissions</td><td>absorbed by water molecules (cooking); pass through the atmosphere to satellites</td></tr>"
    "<tr><td><b>Infrared</b></td><td>cooking (grills, toasters), thermal imaging, short-range communications, optical fibres, TV remote controls, security systems</td><td>emitted by all warm objects (imaging); absorbed by surfaces and heats them</td></tr>"
    "<tr><td><b>Visible</b></td><td>vision, photography, illumination</td><td>the range our eyes detect</td></tr>"
    "<tr><td><b>Ultraviolet</b></td><td>security marking, fluorescent lamps, detecting forged bank notes, disinfecting water</td><td>makes some substances fluoresce (glow visibly); enough energy to kill microbes</td></tr>"
    "<tr><td><b>X-rays</b></td><td>observing the internal structure of objects, airport security scanners, medical X-rays</td><td>pass through soft material but are absorbed by bone and metal</td></tr>"
    "<tr><td><b>Gamma</b></td><td>sterilising food and medical equipment, detecting and treating cancer</td><td>very penetrating and ionising: kills cells and microbes; a tracer's gamma rays get out of the body to a detector</td></tr></table>"
)

section_n8 = section(
    "uses", "nn", "Uses of each part of the spectrum", "5.22",
    equations=[r"\text{one use per region, in the spec's words}"],
    blurb="The spec lists the uses it will ask about. A question usually wants the wave <b>and</b> a reason it suits the job, or the wave and the energy transfer that makes the use work.",
    checklist=[
        "Give at least one spec use for each of the seven regions",
        "Match a use to its wave when given the use",
        "Give the energy-transfer reason behind a use (absorbed by water, passes through skin, makes a current in an aerial…)",
    ],
    parts=[
        explain(
            "The list",
            USES_TABLE +
            "<p>June 2023 Q6(c) (4 marks) asked for two EM waves and, for each, a use or effect that showed energy being transferred: one mark for the wave, one for the result. Credited pairs included microwaves — cooking (water molecules gain energy); infrared — thermal imaging; ultraviolet — fluorescent lamps; X-rays — seeing inside the body; gamma — sterilising equipment; radio — communication (oscillations of electrons in wires).</p>",
        ),
        worked(
            "A use with a reason",
            "Explain why infrared is used in TV remote controls rather than visible light or radio waves. (2 marks)",
            [
                "<b>Use:</b> the remote sends a coded pulse of <b>infrared</b> to the TV's detector — short-range communication.",
                "<b>Reason:</b> infrared is <b>invisible</b> (so it does not distract, unlike visible light) and is easily produced and detected over a short range with a cheap LED and sensor; radio would need an aerial and a licence and is not needed for a few metres.",
            ],
        ),
        practice("Uses", [
            choice("le-n8-q1", "Which wave is used to detect forged bank notes?",
                   ["Infrared", "Ultraviolet", "X-rays", "Microwaves"], 1,
                   "Security markings fluoresce — glow visibly — under ultraviolet."),
            written("le-n8-q2", "State one use of gamma rays and one use of X-rays. (2)",
                    marks(["Gamma: <b>sterilising</b> food / medical equipment, or <b>detecting and treating cancer</b>.",
                           "X-rays: <b>medical X-rays</b> (seeing bones), <b>airport security scanners</b>, observing the internal structure of objects."]), lines=3),
            choice("le-n8-q3", "Which use goes with microwaves?",
                   ["Thermal imaging", "Satellite communications and cooking", "Sterilising surgical instruments", "Photography"], 1,
                   "Microwaves pass through the atmosphere to satellites and are absorbed by water in food."),
            written("le-n8-q4", "Name two electromagnetic waves and, for each, give a use that involves energy being transferred to something. (4)",
                    mark_scheme([
                        ("Wave 1", "A named wave, e.g. <b>microwaves</b>…"),
                        ("Result 1", "…<b>cooking</b>: absorbed by water molecules in the food, which gain energy (heat up)."),
                        ("Wave 2", "A second named wave, e.g. <b>infrared</b>…"),
                        ("Result 2", "…<b>cooking / heating</b>: absorbed by the surface of food or skin, which warms (or thermal imaging: detected after being emitted by warm objects)."),
                    ], extra=["Any correct pair scores: UV — fluorescent lamp / disinfecting water; X-rays — image of bones (absorbed by bone); gamma — sterilising (kills microbes); radio — communication (makes electrons oscillate in the aerial)."]), lines=5),
            written("le-n8-q5", "Explain why X-rays are useful for finding a broken bone. (2)",
                    marks(["X-rays <b>pass through soft tissue</b> (skin, muscle) but are <b>absorbed by bone</b>.",
                           "So the bone leaves a <b>shadow</b> on the detector / film, showing its shape and any break."]), lines=3),
            choice("le-n8-q6", "Optical fibres carry signals using which waves?",
                   ["Radio waves", "Infrared (and visible light)", "Gamma rays", "Microwaves"], 1,
                   "Infrared and visible light are totally internally reflected along the glass fibre."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N9 · Dangers
# ---------------------------------------------------------------------

section_n9 = section(
    "dangers", "nn", "Dangers of electromagnetic radiation", "5.20, 5.21",
    equations=[r"\text{danger increases with frequency}"],
    blurb="The higher the frequency, the more energy each wave carries and the more harm it can do. The spec names one harm each for microwaves, infrared, ultraviolet and X-rays / gamma rays.",
    checklist=[
        "State that the potential danger increases with increasing frequency",
        "Give the named harm for microwaves, infrared, ultraviolet and X-rays/gamma",
        "Explain a danger in terms of the wave being absorbed and transferring energy",
    ],
    parts=[
        explain(
            "The four harms",
            "<table class='tbl'><tr><th>Wave</th><th>Harm from excessive exposure (5.21)</th><th>Why</th></tr>"
            "<tr><td><b>Microwaves</b></td><td><b>internal heating of body cells</b></td><td>absorbed by water in cells, which heats up</td></tr>"
            "<tr><td><b>Infrared</b></td><td><b>skin burns</b></td><td>absorbed at the surface of the skin, heating it</td></tr>"
            "<tr><td><b>Ultraviolet</b></td><td><b>damage to surface cells and eyes</b>, leading to <b>skin cancer</b> and eye conditions (cataracts)</td><td>enough energy to damage cells and their DNA</td></tr>"
            "<tr><td><b>X-rays and gamma rays</b></td><td><b>mutation or damage to cells</b> in the body, which can cause <b>cancer</b></td><td>ionising: enough energy to knock electrons off atoms and break molecules such as DNA</td></tr></table>"
            "<p><b>The rule:</b> the potential danger <b>increases with frequency</b>. Radio waves and microwaves at everyday intensities do little; ultraviolet and beyond carry enough energy per wave to damage cells. That is why we wear sunscreen for UV but not for radio.</p>"
            "<p>June 2024 Q5(a)(i): UVC has the <b>highest frequency</b> (most energy, most ionising) of the UV types, but it does not harm us because it is <b>completely absorbed by the atmosphere</b> and none reaches the ground — two marks, one for each half.</p>",
        ),
        worked(
            "Explaining a danger",
            "Explain why excessive exposure to ultraviolet radiation is dangerous. (2 marks)",
            [
                "<b>Harm:</b> UV is absorbed by the <b>surface cells</b> of the skin and the eyes and <b>damages</b> them (and their DNA).",
                "<b>Consequence:</b> this can lead to <b>skin cancer</b> and eye conditions such as cataracts; UV has a high frequency, so each wave carries enough energy to do this.",
            ],
        ),
        practice("Dangers", [
            choice("le-n9-q1", "Which statement about the dangers of EM waves is correct?",
                   ["Danger increases with wavelength", "Danger increases with frequency", "All EM waves are equally dangerous", "Only visible light is safe"], 1,
                   "Higher frequency means more energy per wave: gamma most dangerous, radio least."),
            written("le-n9-q2", "State the harmful effect on the body of excessive exposure to microwaves, and to infrared. (2)",
                    marks(["Microwaves: <b>internal heating of body cells</b>.", "Infrared: <b>skin burns</b>."]), lines=2),
            written("le-n9-q3", "Explain why X-rays and gamma rays can cause cancer. (2)",
                    marks(["They have very <b>high frequency</b> (high energy) and are <b>ionising</b>: they can damage or <b>mutate cells</b> (their DNA).",
                           "A mutated cell can divide uncontrollably — <b>cancer</b>."]), lines=3),
            choice("le-n9-q4", "Which wave causes skin cancer with excessive exposure?",
                   ["Infrared", "Microwaves", "Ultraviolet", "Radio"], 2,
                   "UV damages surface cells; IR burns, microwaves heat internally."),
            written("le-n9-q5", "UVC has a higher frequency than the UVA and UVB that reach the ground. Explain why UVC is not a danger to people outdoors. (2)",
                    marks(["UVC has the <b>highest frequency / most energy</b> of the three, so it would be the most harmful…",
                           "…but it is <b>completely absorbed by the atmosphere</b> (ozone), so <b>none reaches the surface</b>."]), lines=3),
            written("le-n9-q6", "A radiographer leaves the room while an X-ray is taken. Explain why. (2)",
                    marks(["The radiographer takes many X-rays a day, so without protection their <b>exposure would be excessive</b>.",
                           "X-rays can <b>damage or mutate cells</b>, leading to cancer; leaving the room (or standing behind a lead screen) keeps their dose low."]), lines=3),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N10 · Radiation and temperature
# ---------------------------------------------------------------------

section_n10 = section(
    "thermal-radiation", "nn", "Every body radiates: intensity and wavelength", "5.15P",
    equations=[r"\text{hotter} \Rightarrow \text{more intense, shorter peak wavelength}"],
    blurb="Everything with a temperature gives out electromagnetic radiation — mostly infrared for things around room temperature. The hotter the object, the more it radiates and the shorter the wavelength at which it radiates most.",
    tags=["P"],
    checklist=[
        "State that all bodies emit radiation, whatever their temperature",
        "Describe how the intensity and the peak wavelength change with temperature",
        "Explain why a heated metal glows red, then yellow, then white",
    ],
    parts=[
        explain(
            "Intensity and wavelength distribution",
            "<p><b>All bodies emit radiation.</b> You, the desk, an ice cube — anything above absolute zero gives out electromagnetic waves, spread over a range of wavelengths. At room temperature almost all of it is <b>infrared</b>, which is what a thermal camera sees.</p>"
            "<p>Two things change as an object gets hotter:</p><ul>"
            "<li>The <b>intensity</b> (power radiated per square metre) <b>increases</b> — at every wavelength, and so in total.</li>"
            "<li>The <b>peak wavelength</b> — the wavelength at which most is emitted — gets <b>shorter</b> (the distribution shifts towards higher frequency).</li></ul>"
            "<p>So a poker in a fire first radiates only infrared (invisible), then as it heats the peak moves into the visible: dull <b>red</b>, then orange, <b>yellow</b>, and finally <b>white</b> when it emits across the whole visible range. The Sun's surface (about 5800 K) peaks in the visible; a cooler red star peaks at longer wavelengths.</p>",
        ),
        worked(
            "Describing the change",
            "A lamp filament is slowly heated from cold to white-hot. Describe how the radiation it emits changes. (3 marks)",
            [
                "<b>Cold:</b> it already <b>emits radiation</b> — infrared only, invisible.",
                "<b>Intensity:</b> as it heats, the <b>intensity increases</b> at every wavelength (it radiates more power).",
                "<b>Wavelength:</b> the <b>peak wavelength gets shorter</b> — the emission moves into the visible, so the filament glows red, then yellow, then white.",
            ],
        ),
        practice("Thermal radiation", [
            choice("le-n10-q1", "A cup of tea at 60 °C emits…",
                   ["no radiation until it boils", "mostly infrared radiation", "mostly visible light", "ultraviolet"], 1,
                   "Every body radiates; at everyday temperatures the emission is almost all infrared."),
            written("le-n10-q2", "Describe two ways in which the radiation emitted by an object changes when its temperature increases. (2)",
                    marks(["The <b>intensity</b> (power radiated) <b>increases</b>.", "The <b>peak wavelength becomes shorter</b> (shifts towards higher frequency / the visible)."]), lines=3),
            written("le-n10-q3", "Explain why a piece of iron glows red when heated but white when heated much more. (2)",
                    marks(["As the temperature rises the <b>peak wavelength gets shorter</b>: at first only the red (longest-wavelength) end of the visible is emitted strongly.",
                           "Much hotter, it emits strongly <b>across the whole visible range</b>, and all the colours together look <b>white</b>."]), lines=3),
            choice("le-n10-q4", "Two stars: one looks red, one looks blue-white. Which is hotter?",
                   ["The red one", "The blue-white one", "They are the same", "Colour does not depend on temperature"], 1,
                   "Shorter peak wavelength (blue) means higher temperature."),
            written("le-n10-q5", "A thermal-imaging camera can see a person in a dark room. Explain how. (2)",
                    marks(["The person's body <b>emits infrared</b> radiation because of its temperature (all bodies emit).",
                           "The camera <b>detects the infrared</b>; the person is warmer than the surroundings so emits more intensely and shows up brighter."]), lines=3),
        ]),
    ],
)

# ---------------------------------------------------------------------
# N11 · Key words
# ---------------------------------------------------------------------

DEFINITIONS = [
    ("Normal", "A line at <b>90° to the surface</b> at the point where the ray meets it; angles are measured from it.", "measuring angles from the surface"),
    ("Angle of incidence", "The angle between the <b>incident ray and the normal</b>.", "the angle to the mirror"),
    ("Angle of refraction", "The angle between the <b>refracted ray and the normal</b> (inside the second material).", "the angle to the surface"),
    ("Reflection", "Light <b>bouncing off</b> a surface; angle of incidence = angle of reflection.", "\"light going back\""),
    ("Refraction", "The <b>change of direction</b> of a wave when it crosses a boundary, caused by a <b>change of speed</b>.", "\"light bending\" with no reason"),
    ("Specular reflection", "Reflection from a <b>smooth</b> surface: parallel rays stay parallel, forming an image.", "\"shiny reflection\""),
    ("Diffuse reflection", "Reflection from a <b>rough</b> surface: rays are <b>scattered</b> in many directions because the normal varies.", "\"the law of reflection does not apply\""),
    ("Critical angle", "The <b>angle of incidence</b> (in the denser medium) at which the <b>angle of refraction is 90°</b>.", "\"the angle where it reflects\""),
    ("Total internal reflection", "<b>All</b> the light is reflected back inside the denser medium, when the angle of incidence is <b>greater than the critical angle</b>.", "\"the light stays in\""),
    ("Converging lens", "A lens (convex, fatter in the middle) that brings parallel rays <b>together to a focus</b>.", "\"a lens that makes things bigger\""),
    ("Diverging lens", "A lens (concave, thinner in the middle) that <b>spreads</b> parallel rays apart, as if from a focus on the near side.", "\"a lens that makes things smaller\""),
    ("Focal length", "The distance from the <b>centre of the lens to the principal focus</b>.", "the width of the lens"),
    ("Power of a lens", "<b>1 ÷ focal length</b> (in metres), in dioptres; higher power = more curved = shorter focal length.", "\"how strong it is\""),
    ("Real image", "An image formed where rays <b>actually meet</b>; it can be <b>projected onto a screen</b>; usually inverted.", "\"an image you can see\""),
    ("Virtual image", "An image formed where rays <b>appear to come from</b>; it <b>cannot be projected</b> onto a screen; upright.", "\"not real\" on its own (ignored by the mark scheme)"),
    ("Transverse wave", "A wave whose oscillations are at <b>right angles</b> to the direction of energy transfer (all EM waves).", "\"a wave that goes up and down\" with no direction stated"),
    ("Frequency", "The number of <b>waves per second</b>, in hertz (Hz).", "\"how fast the wave is\""),
    ("Wavelength", "The distance from one point on a wave to the <b>same point on the next wave</b> (e.g. crest to crest), in metres.", "\"the length of the wave\""),
    ("Ionising radiation", "Radiation with enough energy to <b>remove electrons from atoms</b> (ionise them): UV, X-rays, gamma.", "\"radioactive\""),
]


def definitions_table():
    html = "<table class='tbl'><tr><th>Term</th><th>What to write (mark-scheme form)</th><th>Not this</th></tr>"
    for term, definition, wrong in DEFINITIONS:
        html += "<tr><td><b>" + term + "</b></td><td>" + definition + "</td><td>" + wrong + "</td></tr>"
    html += "</table>"
    return html


section_keywords = section(
    "keywords-light", "nn", "Key words: state what is meant by…", "5",
    equations=[r"\text{definition, word for word}"],
    blurb="One-mark definitions in the form of words the mark schemes credit. The bold words are the ones the marks are attached to.",
    checklist=[
        "Define normal, angle of incidence, angle of refraction, critical angle and total internal reflection",
        "Define focal length, power, real image and virtual image",
        "Define transverse, frequency, wavelength and ionising",
    ],
    parts=[
        explain("The definitions", "<p>\"<b>State what is meant by</b>\" asks for the definition. Learn these as sentences.</p>" + definitions_table()),
        practice("Key words", [
            written("le-kw-q1", "State what is meant by the normal. (1)",
                    marks(["A line at <b>right angles (90°) to the surface</b> at the point where the ray strikes it."]), lines=2),
            written("le-kw-q2", "State what is meant by a virtual image. (1)",
                    marks(["An image formed where the rays <b>appear to come from</b> — it <b>cannot be projected onto a screen</b> (the rays do not actually pass through it)."]), lines=2),
            written("le-kw-q3", "State what is meant by the focal length of a lens. (1)",
                    marks(["The distance from the <b>centre of the lens to the principal focus</b>."]), lines=2),
            choice("le-kw-q4", "Which is the correct definition of refraction?",
                   ["Light bouncing off a surface", "A wave changing direction as it crosses a boundary, because its speed changes", "Light splitting into colours", "A wave spreading out through a gap"], 1,
                   "Refraction = change of direction caused by a change of speed at a boundary."),
            written("le-kw-q5", "State what is meant by total internal reflection. (1)",
                    marks(["<b>All</b> the light is <b>reflected back</b> inside the denser material (none refracts out), which happens when the angle of incidence is <b>greater than the critical angle</b>."]), lines=2),
            written("le-kw-q6", "State what is meant by a transverse wave. (1)",
                    marks(["A wave in which the <b>oscillations are at right angles</b> to the direction the wave travels (direction of energy transfer)."]), lines=2),
            choice("le-kw-q7", "A student writes \"the critical angle is the angle at which total internal reflection happens\". What is wrong with this?",
                   ["Nothing", "At the critical angle the refracted ray runs along the surface (angle of refraction 90°); TIR happens above it", "It should say reflection, not refraction", "Critical angle only applies to lenses"], 1,
                   "The critical angle is where r = 90°; TIR needs i greater than the critical angle."),
            written("le-kw-q8", "State what is meant by the power of a lens. (1)",
                    marks(["<b>1 ÷ the focal length</b> (in metres), measured in dioptres; a measure of how strongly the lens refracts light."]), lines=2),
        ]),
    ],
)

FACTS_KW = [fact("State what is meant by: " + term.lower() + ".", definition, "keywords-light") for term, definition, wrong in DEFINITIONS]

SECTIONS = [section_n7, section_n8, section_n9, section_n10, section_keywords]
