"""
en_keywords.py — Topics 3 and 8 (Energy): the key-words section (N12)
and the flashcards that go with it.

Definitions are in the form of words the Edexcel mark schemes credit;
the words in bold are the ones the marks are attached to.
"""

from revlib import choice, explain, fact, marks, practice, section, written

# (term, mark-scheme definition, the wrong answer students give)
DEFINITIONS = [
    ("Energy store", "A way energy is <b>held</b> in a system: kinetic, gravitational potential, elastic potential, thermal, chemical, nuclear, electrostatic, magnetic.", "\"a type of energy\" — the exam wants the word store"),
    ("Pathway", "A way energy is <b>transferred</b> between stores: <b>mechanically</b>, <b>electrically</b>, <b>by heating</b>, <b>by radiation</b>.", "calling light, sound or electricity a store"),
    ("Conservation of energy", "Energy <b>cannot be created or destroyed</b>; it can only be <b>transferred</b> from one store to another.", "\"energy is always saved\""),
    ("Closed system", "A system where <b>no energy can enter or leave</b>, so the <b>total energy stays the same</b>.", "\"a system with a lid\""),
    ("Work done", "The <b>energy transferred</b> when a <b>force moves</b> an object: work done = force × distance moved <b>in the direction of the force</b>.", "\"effort\" or \"how hard you push\""),
    ("Joule", "The unit of energy and of work: the work done when a force of <b>one newton</b> moves something <b>one metre</b> (1 J = 1 N m).", "\"a unit of power\""),
    ("Power", "The <b>rate</b> at which energy is transferred (or work is done): energy transferred <b>per second</b>.", "\"how strong something is\""),
    ("Watt", "<b>One joule per second</b> (1 W = 1 J/s).", "\"a unit of energy\""),
    ("Efficiency", "The <b>fraction</b> (or percentage) of the <b>total energy supplied</b> that is transferred <b>usefully</b>: useful out ÷ total in.", "quoting a percentage above 100%"),
    ("Dissipated", "Energy that has been <b>spread out</b> into the <b>thermal store of the surroundings</b>, where it is <b>no longer useful</b>.", "\"lost\" or \"used up\""),
    ("Kinetic energy", "The energy an object has <b>because it is moving</b>: $\\text{KE} = \\tfrac{1}{2} m v^2$.", "\"movement energy\""),
    ("Gravitational potential energy", "The energy an object has <b>because of its height</b> in a gravitational field: $\\Delta \\text{GPE} = m g \\Delta h$.", "\"height energy\""),
    ("Elastic potential energy", "The energy stored in an object that has been <b>stretched, squashed or bent</b>.", "\"spring energy\""),
    ("Thermal conductivity", "A measure of how <b>quickly energy is transferred through a material</b> by heating; low conductivity = good insulator.", "\"how hot it gets\""),
    ("Thermal insulation", "Material of <b>low thermal conductivity</b> used to <b>reduce the rate</b> of energy transfer to the surroundings.", "\"something that keeps heat in\" (it slows it, it cannot stop it)"),
    ("Lubrication", "Adding oil or grease between moving surfaces to <b>reduce friction</b>, so less energy is transferred to the thermal store.", "\"makes it slippery\" with no link to friction and energy"),
    ("Renewable energy source", "A source that is <b>replaced as fast as it is used</b>, so it <b>will not run out</b>.", "\"can be used again\""),
    ("Non-renewable energy source", "A source that is being <b>used faster than it is replaced</b>, so it <b>will run out</b>.", "\"bad for the environment\" (that is a different point)"),
]


def definitions_table():
    html = "<table class='tbl'><tr><th>Term</th><th>What to write (mark-scheme form)</th><th>Not this</th></tr>"
    for term, definition, wrong in DEFINITIONS:
        html += "<tr><td><b>" + term + "</b></td><td>" + definition + "</td><td>" + wrong + "</td></tr>"
    html += "</table>"
    return html


section_keywords = section(
    "keywords-energy", "nn", "Key words: state what is meant by…", "3, 8",
    equations=[r"\text{\"state what is meant by\" = the definition, word for word}"],
    blurb="One-mark definitions come up on every paper. These are the forms of words the mark schemes credit; the bold words are the ones that carry the mark.",
    checklist=[
        "Define power, efficiency, work done and dissipated in the mark-scheme form",
        "Define renewable and non-renewable, closed system and conservation of energy",
        "Use \"store\" and \"pathway\" correctly and never say energy is lost or used up",
    ],
    parts=[
        explain(
            "The definitions",
            "<p>\"<b>State what is meant by</b>\" asks for the definition. Learn these as sentences, not ideas: the examiner is checking for particular words.</p>" + definitions_table(),
        ),
        practice("Key words", [
            written("en-kw-q1", "State what is meant by the power of a motor. (1)",
                    marks(["The <b>rate</b> at which it transfers energy — the energy transferred (or work done) <b>per second</b>."]), lines=2),
            written("en-kw-q2", "State what is meant by work done. (1)",
                    marks(["The <b>energy transferred</b> when a <b>force moves</b> an object (force × distance moved in the direction of the force)."]), lines=2),
            written("en-kw-q3", "State what is meant by the term dissipated. (1)",
                    marks(["Energy <b>spread out</b> into the <b>thermal store of the surroundings</b> so that it is <b>no longer useful</b>."]), lines=2),
            choice("en-kw-q4", "Which is the correct definition of a watt?",
                   ["One newton per metre", "One joule per second", "One joule per metre", "One newton per second"], 1,
                   "Power is energy per time: 1 W = 1 J/s."),
            written("en-kw-q5", "State what is meant by a non-renewable energy source. (1)",
                    marks(["A source that is being <b>used faster than it is replaced</b>, so it <b>will run out</b>."]), lines=2),
            written("en-kw-q6", "State the law of conservation of energy. (1)",
                    marks(["Energy <b>cannot be created or destroyed</b>, only <b>transferred</b> between stores."]), lines=2),
            choice("en-kw-q7", "A student writes: \"The lamp changes electrical energy into light energy and heat energy.\" What is wrong with this?",
                   ["Nothing", "Light and electricity are pathways, not stores; the answer should name the store the energy ends in (thermal store of the surroundings — \"heat\" is accepted for thermal) rather than \"light energy\", which is not a store", "It should say \"heat\" first", "Lamps do not get hot"], 1,
                   "Edexcel wants stores and pathways. \"Electrical energy\" and \"light energy\" are not stores; every scheme allows \"heat\" for \"thermal\", but write thermal store."),
            written("en-kw-q8", "State what is meant by the efficiency of a kettle. (1)",
                    marks(["The <b>fraction</b> of the <b>energy supplied</b> to the kettle that is <b>transferred usefully</b> (to the thermal store of the water)."]), lines=2),
            written("en-kw-q9", "State what is meant by thermal conductivity. (1)",
                    marks(["How <b>quickly energy is transferred through a material</b> by heating (a high value means a good conductor)."]), lines=2),
            choice("en-kw-q10", "\"Energy is transferred mechanically.\" What does this mean?",
                   ["A machine is involved", "A force does work on an object", "Energy is transferred by heating", "A current flows"], 1,
                   "Mechanical transfer is work done by a force. Electrical transfer is a current; heating is a temperature difference; radiation is waves."),
        ]),
    ],
)
section_keywords["subtopic"] = ["3", "8"]

FACTS = [fact("State what is meant by: " + term.lower() + ".", definition, "keywords-energy") for term, definition, wrong in DEFINITIONS]
