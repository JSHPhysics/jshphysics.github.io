"""
kc_keywords.py — Topic 1 Key concepts: key words, the definitions that score.

Working-scientifically vocabulary, written to the wording Edexcel mark
schemes credit; the scoring words are in bold.
"""

from revlib import choice, explain, fact, marks, practice, section, worked, written

DEFINITIONS = [
    ("Independent variable", "The variable you <b>change</b> (deliberately, in steps)", "\"the one on its own\""),
    ("Dependent variable", "The variable you <b>measure</b> (that changes as a result)", "\"the one that depends\" — on what?"),
    ("Control variable", "A variable that is <b>kept the same</b> so that it does not affect the result", "\"a variable you control\" — say kept constant"),
    ("Valid", "The experiment tests what it claims to: only the independent variable is changed (a <b>fair test</b>)", "\"correct\""),
    ("Accurate", "<b>Close to the true value</b>", "\"precise\" / \"correct\""),
    ("Precise", "Repeated readings are <b>close to each other</b> (little spread)", "\"accurate\" / \"to lots of decimal places\""),
    ("Resolution", "The <b>smallest change</b> in a quantity that an instrument <b>can detect</b> (or show)", "\"how accurate the instrument is\""),
    ("Repeatable", "The <b>same person</b>, with the <b>same method and equipment</b>, gets the <b>same result</b> when the measurement is done again", "\"you can repeat it\""),
    ("Reproducible", "A <b>different person</b>, or different method or equipment, gets the <b>same result</b>", "\"you can do it again\""),
    ("Random error", "An error that makes readings <b>scatter</b> unpredictably above and below the true value; reduced by <b>repeating and averaging</b>", "\"human error\""),
    ("Systematic error", "An error that shifts <b>every reading by the same amount</b> in the same direction; not reduced by averaging", "\"a big error\""),
    ("Zero error", "A systematic error where the instrument <b>reads a non-zero value when it should read zero</b>", "\"an error of zero\""),
    ("Anomalous result", "A result that <b>does not fit the pattern</b> of the others; repeat it or leave it out of the mean", "\"a wrong result\""),
    ("Uncertainty", "The <b>range</b> within which the true value is expected to lie; half the range of repeated readings", "\"the error\""),
    ("Mean", "The <b>sum of the readings divided by the number of readings</b>, leaving out anomalies", "\"the average\" (accepted, but say how)"),
    ("Directly proportional", "Doubling one quantity <b>doubles</b> the other; the graph is a <b>straight line through the origin</b>", "\"a straight line\" — it must go through the origin"),
    ("Inversely proportional", "Doubling one quantity <b>halves</b> the other; their <b>product is constant</b>", "\"they go opposite ways\""),
    ("Significant figures", "The digits in a value that <b>carry meaning</b>, counted from the <b>first non-zero digit</b>", "\"the decimal places\""),
]


def keyword_rows():
    html = "<table class='tbl'><tr><th>Term</th><th>Definition that scores</th><th>Common answer that does not</th></tr>"
    for term, definition, wrong in DEFINITIONS:
        html += "<tr><td><b>" + term + "</b></td><td>" + definition + "</td><td>" + wrong + "</td></tr>"
    html += "</table>"
    return html


section_keywords = section(
    "keywords-ws", "nn", "Key words: the definitions that score", "WS",
    blurb="The working-scientifically words are examined directly (\"state what is meant by…\") and indirectly (an evaluation that uses them correctly scores; one that uses them loosely does not).",
    checklist=[
        "Define every bold term using the words the mark scheme credits",
        "Tell accurate from precise, repeatable from reproducible, and random from systematic",
        "Name the independent, dependent and control variables of any experiment",
    ],
    parts=[
        explain("The definitions", "<p>Learn these as forms of words. In an evaluation, use the right word for the right idea — \"the readings were precise but not accurate\" is a mark; \"the readings were good\" is not.</p>" + keyword_rows()),
        explain(
            "The pairs that get swapped",
            "<p><b>Accurate / precise:</b> accurate is about the true value; precise is about the spread. <b>Repeatable / reproducible:</b> repeatable is the same person again; reproducible is someone else. "
            "<b>Random / systematic:</b> random scatters, systematic shifts. If you are writing one of these words, check you have not written its partner.</p>",
            tone="warn",
        ),
        worked(
            "Using the words in an evaluation",
            "A student measures the period of a pendulum five times with a stopwatch: 1.58, 1.62, 1.60, 1.59, 1.61 s. The accepted value is 1.80 s. Describe the quality of her results using the correct terms. (3)",
            [
                r"The readings are all within 0.04 s of each other: they are <b>precise</b> (small spread) and <b>repeatable</b>.",
                r"They are all about 0.2 s below the accepted value: they are <b>not accurate</b>.",
                r"Every reading is shifted the same way, so there is a <b>systematic error</b> — perhaps she timed from the wrong point of the swing, or the stopwatch was started late every time. Repeating more would not fix it.",
            ],
        ),
        practice("Key words", [
            written("kc-kw-q1", "State what is meant by a <i>precise</i> set of measurements. (1)",
                    marks(["Measurements that are <b>close to each other</b> (little spread) when repeated."]), lines=1),
            written("kc-kw-q2", "State what is meant by an <i>accurate</i> measurement. (1)",
                    marks(["A measurement that is <b>close to the true value</b>."]), lines=1),
            choice("kc-kw-q3", "Which is the definition of <i>resolution</i>?",
                   ["How accurate an instrument is", "The smallest change in a quantity an instrument can detect", "The number of readings taken", "The range of an instrument"], 1,
                   "Resolution is the smallest change the instrument can show — 1 mm on a rule, 0.01 s on a stopwatch. It is not the same as accuracy."),
            written("kc-kw-q4", "State the difference between a <i>repeatable</i> and a <i>reproducible</i> result. (2)",
                    marks(["Repeatable: the <b>same person</b> using the <b>same method and equipment</b> gets the same result again.",
                           "Reproducible: a <b>different person</b>, or a different method or equipment, gets the same result."]), lines=2),
            choice("kc-kw-q5", "A thermometer always reads 1 °C too high. This is:",
                   ["A random error", "A systematic error", "An anomalous result", "Poor resolution"], 1,
                   "Every reading is shifted by the same amount in the same direction: systematic (in fact a zero error). Averaging would not remove it."),
            written("kc-kw-q6", "A student investigates how the extension of a spring depends on the force applied. Name the independent, dependent and one control variable. (3)",
                    marks(["Independent: the <b>force</b> applied (changed by adding masses).",
                           "Dependent: the <b>extension</b> (measured).",
                           "Control: the <b>same spring</b> (or the same original length / temperature) throughout."]), lines=3),
            choice("kc-kw-q7", "Which statement defines <i>directly proportional</i>?",
                   ["Both quantities increase", "The graph is a straight line", "Doubling one quantity doubles the other; the graph is a straight line through the origin", "One quantity depends on the other"], 2,
                   "Proportional needs the straight line through the origin (or the constant ratio). A straight line with an intercept is linear, not proportional."),
            written("kc-kw-q8", "State what is meant by a <i>random error</i> and give one way of reducing its effect. (2)",
                    marks(["An error that makes readings <b>vary unpredictably</b> (scatter) above and below the true value.",
                           "Reduce its effect by <b>repeating the readings and calculating a mean</b>."]), lines=2),
        ], intro="Write each answer on paper first. Mark yourself strictly: if the bold words (or their equivalent) are missing, it is not a mark."),
    ],
)

FACTS = [
    fact("Define the independent variable", "The one you change", "keywords-ws"),
    fact("Define the dependent variable", "The one you measure", "keywords-ws"),
    fact("Define a control variable", "One kept the same so it does not affect the result", "keywords-ws"),
    fact("Define uncertainty", "The range within which the true value is expected to lie", "keywords-ws"),
    fact("Define a zero error", "The instrument reads a non-zero value when it should read zero", "keywords-ws"),
]
