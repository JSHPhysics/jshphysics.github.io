#!/usr/bin/env python3
"""
build_p3_motion.py — the source of truth for data/p3-motion.json.

The booklet content is authored here as Python (so that the KaTeX in it
can be written as raw strings without JSON backslash-doubling) and then
dumped to JSON for the app to fetch. Run from the ks3-revision folder:

    python3 tools/build_p3_motion.py

Maths is written between $...$ (inline) or $$...$$ (display) and is
typeset by KaTeX in the browser. Everything else in a text field is HTML.
See SCHEMA.md for the shape of each block.
"""

import json
import os

# ---------------------------------------------------------------------
# Small helpers for the recurring shapes
# ---------------------------------------------------------------------


def ewau(equation, working, answer, units):
    """The four lines of an EWAU calculation, as walkthrough steps."""
    return [
        r"<b>Equation:</b> $" + equation + "$",
        r"<b>Working:</b> $" + working + "$",
        r"<b>Answer:</b> $= " + answer + "$",
        r"<b>Units:</b> " + units,
    ]


def numeric(qid, text, value, unit, hint, walkthrough, label=None, graph=None, tolerance=None):
    question = {
        "id": qid,
        "type": "numeric",
        "text": text,
        "answer": {"value": value, "unit": unit},
        "hint": hint,
        "walkthrough": walkthrough,
    }
    if tolerance is not None:
        question["answer"]["tolerance"] = tolerance
    if label is not None:
        question["label"] = label
    if graph is not None:
        question["graph"] = graph
    return question


def choice(qid, text, options, correct, explain, hint=None, label=None, graph=None):
    question = {
        "id": qid,
        "type": "choice",
        "text": text,
        "options": options,
        "correct": correct,
        "explain": explain,
    }
    if hint is not None:
        question["hint"] = hint
    if label is not None:
        question["label"] = label
    if graph is not None:
        question["graph"] = graph
    return question


def written(qid, text, model, lines=3, hint=None, label=None, graph=None):
    question = {
        "id": qid,
        "type": "written",
        "text": text,
        "model": model,
        "lines": lines,
    }
    if hint is not None:
        question["hint"] = hint
    if label is not None:
        question["label"] = label
    if graph is not None:
        question["graph"] = graph
    return question


def draw(qid, text, grid, answer_graph, model, hint=None, label=None, check=True):
    """A graph-drawing task. With check=True the student taps points onto the
    grid and the app compares them with the first series of answer_graph."""
    question = {
        "id": qid,
        "type": "draw",
        "text": text,
        "grid": grid,
        "answerGraph": answer_graph,
        "model": model,
        "check": check,
    }
    if hint is not None:
        question["hint"] = hint
    if label is not None:
        question["label"] = label
    return question


def group(qid, text, parts, graph=None):
    question = {"id": qid, "type": "group", "text": text, "parts": parts}
    if graph is not None:
        question["graph"] = graph
    return question


def axis(label, mx, step, mn=0, minor=None):
    result = {"label": label, "min": mn, "max": mx, "step": step}
    if minor is not None:
        result["minor"] = minor
    return result


def line(points):
    return {"kind": "line", "points": points}


def curve(points):
    return {"kind": "curve", "points": points}


def dashed(points):
    return {"kind": "dashed", "points": points}


def vline(x, ymax):
    """A dashed vertical divider between stages of a journey."""
    return dashed([[x, 0], [x, ymax]])


def label(x, y, text, anchor="middle"):
    return {"x": x, "y": y, "text": text, "anchor": anchor}


def sample(fn, start, end, count=9):
    """Sample a function for a smooth curve."""
    points = []
    for index in range(count):
        x = start + (end - start) * index / (count - 1)
        points.append([round(x, 3), round(fn(x), 3)])
    return points


# ---------------------------------------------------------------------
# Section 1 · Speed
# ---------------------------------------------------------------------

SPEED_EQ = r"\text{speed} = \dfrac{\text{distance}}{\text{time}}"
DIST_EQ = r"\text{distance} = \text{speed} \times \text{time}"
TIME_EQ = r"\text{time} = \dfrac{\text{distance}}{\text{speed}}"
AVG_EQ = r"\text{average speed} = \dfrac{\text{total distance}}{\text{total time}}"

section_speed = {
    "id": "speed",
    "lessons": "Lessons 1–2",
    "title": "Speed",
    "blurb": "What speed means, the speed equation and its rearrangements, laying out calculations with EWAU, and the difference between instantaneous and average speed.",
    "equations": [SPEED_EQ, AVG_EQ],
    "checklist": [
        "Know what is meant by the term 'speed'",
        "Calculate the speed of an object",
        "Rearrange the speed equation to calculate distance or time",
        "Use EWAU to lay out calculations",
        "Understand the difference between instantaneous speed and average speed",
        "Know how to calculate average speed",
    ],
    "parts": [
        {
            "kind": "explain",
            "title": "What is speed?",
            "html": (
                "<p><b>Speed</b> tells you <b>how far an object travels every second</b> (or every hour). "
                "A faster object covers more distance in the same time.</p>"
                "<p>The equation is:</p>"
                "$$" + SPEED_EQ + "$$"
                "<p>The units must match up:</p>"
                "<table class=\"tbl\"><tr><th>Distance in…</th><th>Time in…</th><th>Speed in…</th></tr>"
                "<tr><td>metres (m)</td><td>seconds (s)</td><td>metres per second (m/s)</td></tr>"
                "<tr><td>kilometres (km)</td><td>hours (h)</td><td>kilometres per hour (km/h)</td></tr>"
                "<tr><td>miles</td><td>hours (h)</td><td>miles per hour (mph)</td></tr></table>"
                "<p>In physics we normally use <b>m/s</b>. If a question gives you minutes or kilometres, "
                "<b>convert first</b>: 1 minute = 60 s and 1 km = 1000 m.</p>"
            ),
        },
        {
            "kind": "explain",
            "title": "EWAU — how to lay out every calculation",
            "html": (
                "<p>Every calculation in physics should be written out in four lines. This earns marks even if "
                "you make a slip with the arithmetic, and it makes your working easy to check.</p>"
                "<table class=\"tbl\"><tr><th>Letter</th><th>What you write</th></tr>"
                "<tr><td><b>E</b>quation</td><td>The equation in words or symbols, <i>before</i> you put any numbers in.</td></tr>"
                "<tr><td><b>W</b>orking</td><td>The numbers substituted into the equation.</td></tr>"
                "<tr><td><b>A</b>nswer</td><td>The number you get out.</td></tr>"
                "<tr><td><b>U</b>nits</td><td>The correct unit written after the answer.</td></tr></table>"
                "<p>Every worked example and walkthrough on this page is written in EWAU. Copy the layout.</p>"
            ),
        },
        {
            "kind": "worked",
            "title": "Calculating speed",
            "question": "A cyclist travels 240 m in 30 s. Calculate her speed.",
            "steps": ewau(SPEED_EQ, r"\text{speed} = \dfrac{240}{30}", "8", "m/s")
            + [r"Check it makes sense: 8 m every second for 30 seconds is $8 \times 30 = 240$ m. ✓"],
        },
        {
            "kind": "explain",
            "title": "Rearranging the speed equation",
            "html": (
                "<p>Sometimes you are given the speed and need to find the distance or the time. "
                "Here are all three versions of the equation — learn them:</p>"
                "<table class=\"tbl\"><tr><th>To find…</th><th>Use…</th><th>Why it works</th></tr>"
                "<tr><td>speed</td><td>$" + SPEED_EQ + "$</td><td>This is the original equation.</td></tr>"
                "<tr><td>distance</td><td>$" + DIST_EQ + "$</td><td>Distance was being divided by time, so multiply both sides by time to undo it.</td></tr>"
                "<tr><td>time</td><td>$" + TIME_EQ + "$</td><td>Swap speed and time — they are both \"underneath\" the distance.</td></tr></table>"
                "<p><b>Quick check:</b> if you are finding a distance, you <i>multiply</i>. If you are finding a speed "
                "or a time, you always <i>divide the distance</i> by something.</p>"
            ),
        },
        {
            "kind": "worked",
            "title": "Calculating distance",
            "question": "A car travels at 25 m/s for 40 s. How far does it travel?",
            "steps": ewau(DIST_EQ, r"\text{distance} = 25 \times 40", "1000", "m"),
        },
        {
            "kind": "worked",
            "title": "Calculating time",
            "question": "A runner moves at 5 m/s. How long does it take him to run 200 m?",
            "steps": ewau(TIME_EQ, r"\text{time} = \dfrac{200}{5}", "40", "s"),
        },
        {
            "kind": "practice",
            "title": "Speed, distance and time",
            "intro": "Use EWAU for every question. Convert units first where needed.",
            "questions": [
                numeric(
                    "p3-s1-q1", "A dog runs 50 m in 10 s. Calculate its speed.", 5, "m/s",
                    "You have a distance and a time, so use the original speed equation.",
                    ewau(SPEED_EQ, r"\text{speed} = \dfrac{50}{10}", "5", "m/s"),
                ),
                numeric(
                    "p3-s1-q2", "A train travels 3600 m in 120 s. Calculate its speed.", 30, "m/s",
                    "Distance divided by time.",
                    ewau(SPEED_EQ, r"\text{speed} = \dfrac{3600}{120}", "30", "m/s"),
                ),
                numeric(
                    "p3-s1-q3", "A walker moves at 1.5 m/s for 600 s. How far does she walk?", 900, "m",
                    "You want a distance, so multiply speed by time.",
                    ewau(DIST_EQ, r"\text{distance} = 1.5 \times 600", "900", "m"),
                ),
                numeric(
                    "p3-s1-q4", "A ball rolls at 12 m/s. How long does it take to travel 36 m?", 3, "s",
                    "You want a time, so divide the distance by the speed.",
                    ewau(TIME_EQ, r"\text{time} = \dfrac{36}{12}", "3", "s"),
                ),
                numeric(
                    "p3-s1-q5", "A bus travels 18 km in 0.5 hours. Calculate its speed in km/h.", 36, "km/h",
                    "The distance is already in km and the time in hours, so no conversion is needed.",
                    ewau(SPEED_EQ, r"\text{speed} = \dfrac{18}{0.5}", "36", "km/h"),
                ),
                numeric(
                    "p3-s1-q6", "A jet flies at 250 m/s. How far does it travel in 2 minutes? Give your answer in metres.", 30000, "m",
                    "The speed is in m/s, so the time must be in seconds. How many seconds are in 2 minutes?",
                    [r"Convert the time first: $2 \text{ minutes} = 2 \times 60 = 120$ s."]
                    + ewau(DIST_EQ, r"\text{distance} = 250 \times 120", "30\\,000", "m")
                    + [r"That is $30\,000 \div 1000 = 30$ km."],
                ),
            ],
        },
        {
            "kind": "explain",
            "title": "Instantaneous speed vs average speed",
            "html": (
                "<p>Real journeys are not at one steady speed — you speed up, slow down and stop. "
                "So there are two kinds of speed:</p>"
                "<table class=\"tbl\"><tr><th>Type</th><th>Meaning</th><th>Example</th></tr>"
                "<tr><td><b>Instantaneous speed</b></td><td>The speed at <b>one particular moment</b>.</td>"
                "<td>The reading on a car's speedometer right now; a speed-camera reading.</td></tr>"
                "<tr><td><b>Average speed</b></td><td>The <b>total distance</b> travelled divided by the <b>total time</b> "
                "taken for the <b>whole journey</b> — including any stops.</td>"
                "<td>\"The coach averaged 60 km/h on the motorway.\"</td></tr></table>"
                "$$" + AVG_EQ + "$$"
                "<p><b>Common mistake:</b> leaving out the time spent stopped. If you stop for lunch, that time still "
                "counts in the total time — it lowers your average speed.</p>"
            ),
        },
        {
            "kind": "worked",
            "title": "Average speed",
            "question": "A cyclist rides 1200 m in 100 s, stops for 50 s at a junction, then rides a further 600 m in 50 s. Calculate her average speed for the whole journey.",
            "steps": [
                r"Add up the totals first. Total distance $= 1200 + 600 = 1800$ m.",
                r"Total time $= 100 + 50 + 50 = 200$ s — the 50 s stop counts.",
            ]
            + ewau(AVG_EQ, r"\text{average speed} = \dfrac{1800}{200}", "9", "m/s")
            + [r"Notice: during the first part her speed was $1200 \div 100 = 12$ m/s, and at the junction it was 0 m/s. The average, 9 m/s, is in between."],
        },
        {
            "kind": "practice",
            "title": "Instantaneous and average speed",
            "questions": [
                written(
                    "p3-s1-q7",
                    "In your own words, explain the difference between instantaneous speed and average speed.",
                    "<p><b>Instantaneous speed</b> is the speed at one moment in time (for example, a speedometer reading). "
                    "<b>Average speed</b> is the total distance divided by the total time for a whole journey, including any stops.</p>",
                    lines=3,
                ),
                numeric(
                    "p3-s1-q8", "A car travels 30 km in 0.5 h and then 60 km in 1 h. Calculate its average speed in km/h.", 60, "km/h",
                    "Add up the total distance and the total time before you divide.",
                    [r"Total distance $= 30 + 60 = 90$ km. Total time $= 0.5 + 1 = 1.5$ h."]
                    + ewau(AVG_EQ, r"\text{average speed} = \dfrac{90}{1.5}", "60", "km/h"),
                ),
                numeric(
                    "p3-s1-q9", "An athlete runs 100 m in 12 s, rests for 18 s, then runs another 100 m in 10 s. Calculate her average speed over the whole 40 s.", 5, "m/s",
                    "The rest counts in the total time. Total distance is 200 m.",
                    [r"Total distance $= 100 + 100 = 200$ m. Total time $= 12 + 18 + 10 = 40$ s."]
                    + ewau(AVG_EQ, r"\text{average speed} = \dfrac{200}{40}", "5", "m/s"),
                ),
                choice(
                    "p3-s1-q10",
                    "A speedometer in a car reads 70 mph. Is this an instantaneous speed or an average speed?",
                    ["Instantaneous speed", "Average speed"],
                    0,
                    "A speedometer shows the speed at that exact moment, not over a whole journey — so it is an instantaneous speed.",
                ),
                group(
                    "p3-s1-q11",
                    "A cyclist's average speed over 300 s is 6 m/s.",
                    [
                        numeric(
                            "p3-s1-q11a", "Calculate the distance he travelled.", 1800, "m",
                            "Rearrange: distance = speed × time.",
                            ewau(DIST_EQ, r"\text{distance} = 6 \times 300", "1800", "m"),
                            label="a",
                        ),
                        written(
                            "p3-s1-q11b",
                            "Does this mean he was travelling at 6 m/s the whole time? Explain your answer.",
                            "<p>No. An average speed only tells you the overall speed for the whole journey. He could have gone "
                            "faster at some times and slower (or stopped) at others.</p>",
                            lines=2,
                            label="b",
                        ),
                    ],
                ),
            ],
        },
    ],
}

# ---------------------------------------------------------------------
# Section 2 · Graph skills
# ---------------------------------------------------------------------

GRAD_EQ = r"\text{gradient} = \dfrac{\text{change in } y}{\text{change in } x}"

graph_gradient_example = {
    "x": axis("x", 10, 1, minor=1),
    "y": axis("y", 50, 10, minor=2),
    "series": [
        line([[0, 0], [10, 50]]),
        dashed([[2, 10], [8, 10], [8, 40]]),
    ],
    "marks": [
        {"x": 2, "y": 10, "label": "(2, 10)", "dx": -58, "dy": -8},
        {"x": 8, "y": 40, "label": "(8, 40)", "dx": -62, "dy": 4},
    ],
    "labels": [label(5, 6, "change in x = 6"), label(8.3, 24, "change in y = 30", "start")],
    "alt": "A straight line through the origin, with a triangle drawn between (2, 10) and (8, 40)",
}

graph_three_lines = {
    "x": axis("x", 10, 1, minor=1),
    "y": axis("y", 40, 5, minor=1),
    "series": [
        line([[0, 0], [10, 40]]),
        line([[0, 0], [10, 10]]),
        line([[0, 30], [10, 0]]),
    ],
    "labels": [label(9.2, 38.5, "A"), label(9.2, 11.8, "B"), label(0.5, 32, "C")],
    "alt": "Three straight lines: A rising steeply, B rising gently, C falling",
}

grid_toy_car = {
    "x": axis("Time (s)", 50, 10, minor=5),
    "y": axis("Distance (m)", 100, 20, minor=4),
    "series": [],
    "alt": "A blank grid for plotting",
}

graph_toy_car_answer = {
    "x": axis("Time (s)", 50, 10, minor=5),
    "y": axis("Distance (m)", 100, 20, minor=4),
    "series": [
        {"kind": "data", "points": [[0, 0], [10, 21], [20, 39], [30, 62], [40, 80], [50, 99]], "fit": [[0, 0], [50, 100]]},
        dashed([[10, 20], [50, 20], [50, 100]]),
    ],
    "labels": [label(30, 14, "change in x = 40"), label(45, 60, "change in y = 80", "end")],
    "alt": "The toy-car data plotted with a straight line of best fit through the origin",
}

section_graphs = {
    "id": "graphs",
    "lessons": "Lessons 3–5",
    "title": "Graph skills",
    "blurb": "Line graphs and scatter graphs, when to draw a line of best fit and when to join dot-to-dot, drawing graphs correctly, and calculating a gradient.",
    "equations": [GRAD_EQ],
    "checklist": [
        "Understand the difference between line and scatter graphs",
        "Understand when to draw a line of best fit and when to connect points dot-to-dot",
        "Correctly draw line and scatter graphs",
        "Calculate the gradient of a line",
        "Understand that a gradient can be positive or negative and what this tells you about the slope",
    ],
    "parts": [
        {
            "kind": "explain",
            "title": "Line graphs vs scatter graphs",
            "html": (
                "<p>Both graphs plot one number against another, but they are used for different jobs.</p>"
                "<table class=\"tbl\"><tr><th></th><th>Line graph</th><th>Scatter graph</th></tr>"
                "<tr><td><b>When you use it</b></td><td>You <b>chose</b> the values of the variable on the x-axis "
                "(the <i>independent variable</i>) and measured what happened to the other one.</td>"
                "<td>You <b>measured both</b> variables and want to see if there is a <i>correlation</i> (a link) between them.</td></tr>"
                "<tr><td><b>Example</b></td><td>Distance travelled every 10 s; extension of a spring for different forces; "
                "temperature of water each minute.</td><td>Height vs arm span of 30 pupils; hours of sleep vs test score.</td></tr>"
                "<tr><td><b>The line</b></td><td>Points are joined — either with a line of best fit or dot-to-dot (see below).</td>"
                "<td>Points are <b>not</b> joined dot-to-dot. A line of best fit can be added if there is a clear correlation.</td></tr></table>"
            ),
        },
        {
            "kind": "explain",
            "title": "Line of best fit or dot-to-dot?",
            "html": (
                "<table class=\"tbl\"><tr><th>Draw a…</th><th>When…</th><th>How</th></tr>"
                "<tr><td><b>Line of best fit</b></td><td>You expect a <b>smooth pattern</b> and the points are slightly "
                "scattered because of small measurement errors. Most science experiments are like this.</td>"
                "<td>One straight line (ruler!) or one smooth curve that passes through the <i>middle</i> of the points, "
                "with roughly as many above as below. <b>Ignore anomalous points</b> (ones clearly off the pattern) and circle them.</td></tr>"
                "<tr><td><b>Dot-to-dot</b></td><td>There is <b>no reason to expect a smooth pattern</b> between readings — "
                "the thing being measured can change suddenly. Journey graphs (distance–time and speed–time) are usually drawn "
                "like this, because a car can stop at lights or suddenly accelerate.</td>"
                "<td>Join each point to the next with a straight ruled line.</td></tr></table>"
            ),
        },
        {
            "kind": "explain",
            "title": "Drawing a graph correctly — the checklist",
            "html": (
                "<ol class=\"list\">"
                "<li><b>Axes:</b> independent variable (the one you changed or chose, usually time) on the <b>x-axis</b>; "
                "dependent variable (the one you measured) on the <b>y-axis</b>.</li>"
                "<li><b>Labels:</b> each axis labelled with the quantity <b>and its unit</b>, e.g. \"Distance (m)\".</li>"
                "<li><b>Scale:</b> goes up in equal steps (1, 2, 5, 10, 20, 50…) and the plotted points fill <b>more than half</b> "
                "of the grid in both directions.</li>"
                "<li><b>Plot:</b> small, neat crosses (×) with a sharp pencil.</li>"
                "<li><b>Line:</b> best fit (ruler or smooth curve) or dot-to-dot — decide which <i>before</i> you draw.</li>"
                "<li><b>Title</b> if asked, e.g. \"Distance–time graph for a cyclist\".</li></ol>"
            ),
        },
        {
            "kind": "explain",
            "title": "Gradient",
            "html": (
                "<p>The <b>gradient</b> is a number that tells you <b>how steep</b> a line is. It is \"how much the line "
                "goes up for every 1 it goes across\":</p>"
                "$$" + GRAD_EQ + r" = \dfrac{\text{rise}}{\text{run}}$$"
                "<p><b>Method:</b></p><ol class=\"list\">"
                "<li>Choose two points <b>on the line</b>, as far apart as possible (big triangles give more accurate answers).</li>"
                "<li>Draw a right-angled triangle between them.</li>"
                "<li>Read off the change in $y$ (the vertical side) and the change in $x$ (the horizontal side).</li>"
                "<li>Divide: change in $y$ ÷ change in $x$.</li></ol>"
                "<p><b>Positive or negative?</b></p><ul class=\"list\">"
                "<li>A line that slopes <b>up to the right</b> has a <b>positive</b> gradient — $y$ gets bigger as $x$ gets bigger.</li>"
                "<li>A line that slopes <b>down to the right</b> has a <b>negative</b> gradient — $y$ gets smaller as $x$ gets bigger.</li>"
                "<li>A <b>horizontal</b> line has a gradient of <b>zero</b> — $y$ doesn't change at all.</li>"
                "<li>The <b>bigger</b> the number (ignoring the sign), the <b>steeper</b> the line.</li></ul>"
            ),
        },
        {
            "kind": "worked",
            "title": "Finding a gradient",
            "question": "Find the gradient of the line shown.",
            "graph": graph_gradient_example,
            "steps": [
                r"Choose two points on the line, far apart: $(2,\ 10)$ and $(8,\ 40)$.",
            ]
            + ewau(GRAD_EQ, r"\text{gradient} = \dfrac{40 - 10}{8 - 2} = \dfrac{30}{6}", "5", "(units of $y$ ÷ units of $x$)")
            + [
                r"The gradient is $+5$: the line goes up 5 for every 1 it goes across.",
                r"A line from $(0,\ 20)$ to $(10,\ 0)$ would have gradient $\dfrac{0 - 20}{10 - 0} = \dfrac{-20}{10} = -2$ — negative, because it slopes downwards.",
            ],
        },
        {
            "kind": "practice",
            "title": "Graph skills",
            "questions": [
                group(
                    "p3-s2-q1",
                    "For each investigation, decide whether you would draw a <b>line graph</b> or a <b>scatter graph</b>.",
                    [
                        choice("p3-s2-q1a", "Extension of a spring when you hang different masses on it.", ["Line graph", "Scatter graph"], 0,
                               "You chose the masses (the independent variable), so this is a line graph.", label="a"),
                        choice("p3-s2-q1b", "Height and hand span of every pupil in your class.", ["Line graph", "Scatter graph"], 1,
                               "Both variables were measured and you are looking for a correlation, so this is a scatter graph.", label="b"),
                        choice("p3-s2-q1c", "Temperature of a cup of tea measured every minute as it cools.", ["Line graph", "Scatter graph"], 0,
                               "You chose when to take each reading, so this is a line graph.", label="c"),
                        choice("p3-s2-q1d", "Hours of sleep and test score for 30 pupils.", ["Line graph", "Scatter graph"], 1,
                               "Both were measured, so this is a scatter graph looking for a correlation.", label="d"),
                    ],
                ),
                group(
                    "p3-s2-q2",
                    "For each graph, decide whether you would draw a <b>line of best fit</b> or join the points <b>dot-to-dot</b>.",
                    [
                        choice("p3-s2-q2a", "Extension of a spring against the force applied.", ["Line of best fit", "Dot-to-dot"], 0,
                               "A smooth pattern is expected and small measurement errors scatter the points — line of best fit.", label="a"),
                        choice("p3-s2-q2b", "Distance a car has travelled, recorded every 10 s on a journey that includes a stop at traffic lights.",
                               ["Line of best fit", "Dot-to-dot"], 1,
                               "The motion changes suddenly at the lights, so there is no smooth pattern to expect — dot-to-dot.", label="b"),
                        choice("p3-s2-q2c", "Temperature of water heated by a steady flame, recorded every 30 s.", ["Line of best fit", "Dot-to-dot"], 0,
                               "Steady heating gives a smooth pattern — line of best fit.", label="c"),
                    ],
                ),
                group(
                    "p3-s2-q3",
                    "Calculate the gradient of the straight line passing through each pair of points.",
                    [
                        numeric("p3-s2-q3a", "$(0,\\ 0)$ and $(4,\\ 12)$", 3, "", "Change in y over change in x.",
                                ewau(GRAD_EQ, r"\text{gradient} = \dfrac{12 - 0}{4 - 0} = \dfrac{12}{4}", "3", "none"), label="a"),
                        numeric("p3-s2-q3b", "$(1,\\ 5)$ and $(5,\\ 25)$", 5, "", "Subtract the first point from the second, top and bottom.",
                                ewau(GRAD_EQ, r"\text{gradient} = \dfrac{25 - 5}{5 - 1} = \dfrac{20}{4}", "5", "none"), label="b"),
                        numeric("p3-s2-q3c", "$(0,\\ 30)$ and $(6,\\ 0)$", -5, "", "The line goes down as x increases, so expect a negative answer.",
                                ewau(GRAD_EQ, r"\text{gradient} = \dfrac{0 - 30}{6 - 0} = \dfrac{-30}{6}", "-5", "none")
                                + ["Negative — the line slopes downwards."], label="c"),
                    ],
                ),
                group(
                    "p3-s2-q4",
                    "Look at the three lines on the graph.",
                    [
                        choice("p3-s2-q4a", "Which line has a negative gradient?", ["A", "B", "C"], 2,
                               "C slopes down to the right, so its gradient is negative.", label="a"),
                        choice("p3-s2-q4b", "Which line is the steepest?", ["A", "B", "C"], 0,
                               "A rises 40 for every 10 across — the biggest gradient, ignoring sign.", label="b"),
                        numeric("p3-s2-q4c", "Calculate the gradient of line A.", 4, "", "A goes from (0, 0) to (10, 40).",
                                ewau(GRAD_EQ, r"\text{gradient} = \dfrac{40 - 0}{10 - 0}", "4", "none"), label="c"),
                        numeric("p3-s2-q4d", "Calculate the gradient of line B.", 1, "", "B goes from (0, 0) to (10, 10).",
                                ewau(GRAD_EQ, r"\text{gradient} = \dfrac{10 - 0}{10 - 0}", "1", "none"), label="d"),
                        numeric("p3-s2-q4e", "Calculate the gradient of line C.", -3, "", "C goes from (0, 30) to (10, 0). Watch the sign.",
                                ewau(GRAD_EQ, r"\text{gradient} = \dfrac{0 - 30}{10 - 0}", "-3", "none"), label="e"),
                    ],
                    graph=graph_three_lines,
                ),
                group(
                    "p3-s2-q5",
                    "A pupil measures how far a toy car has travelled along a corridor every 10 s:"
                    "<table class=\"tbl data\"><tr><th>Time (s)</th><td>0</td><td>10</td><td>20</td><td>30</td><td>40</td><td>50</td></tr>"
                    "<tr><th>Distance (m)</th><td>0</td><td>21</td><td>39</td><td>62</td><td>80</td><td>99</td></tr></table>",
                    [
                        draw(
                            "p3-s2-q5a",
                            "Plot the data on the grid (tap to place the crosses, or draw on paper). Label both axes with units. The car was travelling at a steady speed, so on paper draw a <b>line of best fit</b>.",
                            grid_toy_car,
                            graph_toy_car_answer,
                            "<p>Time (s) on the x-axis and Distance (m) on the y-axis, both labelled with units. Points plotted as small "
                            "crosses, and a single straight ruled line of best fit through the middle of the points (it passes very close to the origin).</p>",
                            label="a", check=False,
                        ),
                        numeric("p3-s2-q5b", "Use a large triangle on your line to calculate its gradient.", 2, "m/s",
                                "Pick two points far apart on your line, for example at 10 s and 50 s.",
                                [r"Read two points far apart on the line of best fit, e.g. $(10,\ 20)$ and $(50,\ 100)$."]
                                + ewau(GRAD_EQ, r"\text{gradient} = \dfrac{100 - 20}{50 - 10} = \dfrac{80}{40}", "2", "m/s")
                                + ["Anything from 1.9 to 2.1 m/s is fine — it depends on your line."],
                                label="b", tolerance=0.08),
                        choice("p3-s2-q5c", "What does the gradient of this graph tell you?", ["The car's speed", "The distance the car travelled", "The time taken"], 0,
                               "Distance ÷ time is speed, so the gradient of a distance–time graph is the speed: about 2 m/s.", label="c"),
                    ],
                ),
            ],
        },
    ],
}

# ---------------------------------------------------------------------
# Section 3 · Distance–time graphs
# ---------------------------------------------------------------------

DT_SPEED_EQ = r"\text{speed} = \text{gradient} = \dfrac{\text{change in distance}}{\text{change in time}}"

graph_dt_shapes = {
    "x": axis("Time (s)", 50, 10, minor=2),
    "y": axis("Distance (m)", 100, 20, minor=2),
    "series": [
        line([[0, 0], [10, 50]]),
        line([[10, 50], [20, 50]]),
        line([[20, 50], [30, 0]]),
        curve(sample(lambda x: 0.4 * (x - 30) ** 2, 30, 40, 7)),
        curve(sample(lambda x: 80 - 0.4 * (50 - x) ** 2, 40, 50, 7)),
        vline(10, 100), vline(20, 100), vline(30, 100), vline(40, 100),
    ],
    "labels": [
        label(5, 70, "constant speed"), label(15, 70, "stationary"), label(25, 70, "constant speed,"), label(25, 62, "heading home"),
        label(35, 70, "speeding up"), label(45, 36, "slowing down"),
    ],
    "alt": "The five shapes on a distance–time graph: rising line, flat line, falling line, curve getting steeper, curve getting flatter",
}

graph_dt_example = {
    "x": axis("Time (s)", 60, 10, minor=2),
    "y": axis("Distance from home (m)", 120, 20, minor=2),
    "series": [
        line([[0, 0], [20, 100], [40, 100], [60, 0]]),
        vline(20, 120), vline(40, 120),
    ],
    "marks": [{"x": 0, "y": 0}, {"x": 20, "y": 100}, {"x": 40, "y": 100}, {"x": 60, "y": 0}],
    "labels": [label(10, 110, "A"), label(30, 110, "B"), label(50, 110, "C")],
    "alt": "Distance–time graph: up to 100 m in 20 s, flat for 20 s, back to 0 in 20 s",
}

graph_dt_practice = {
    "x": axis("Time (s)", 60, 10, minor=2),
    "y": axis("Distance from start (m)", 150, 30, minor=3),
    "series": [
        line([[0, 0], [10, 60], [20, 60], [30, 150], [60, 0]]),
        vline(10, 150), vline(20, 150), vline(30, 150),
    ],
    "marks": [{"x": 10, "y": 60}, {"x": 20, "y": 60}, {"x": 30, "y": 150}, {"x": 60, "y": 0}],
    "labels": [label(5, 140, "A"), label(15, 140, "B"), label(25, 140, "C"), label(45, 140, "D")],
    "alt": "Distance–time graph for a delivery robot with four stages A to D",
}

graph_dt_curves = {
    "x": axis("Time (s)", 30, 5, minor=1),
    "y": axis("Distance (m)", 100, 20, minor=2),
    "series": [
        curve(sample(lambda x: (100 / 900) * x * x, 0, 30, 9)),
        curve(sample(lambda x: 100 * (x / 30) ** 0.5, 0, 30, 11)),
    ],
    "labels": [label(24, 48, "P"), label(10, 66, "Q")],
    "alt": "Two curves: P gets steeper, Q gets flatter",
}

grid_sam = {
    "x": axis("Time (s)", 250, 50, minor=5),
    "y": axis("Distance from home (m)", 250, 50, minor=5),
    "series": [],
    "alt": "A blank grid for drawing a distance–time graph",
}

graph_sam_answer = {
    "x": axis("Time (s)", 250, 50, minor=5),
    "y": axis("Distance from home (m)", 250, 50, minor=5),
    "series": [line([[0, 0], [100, 200], [150, 200], [200, 0]])],
    "marks": [{"x": 100, "y": 200}, {"x": 150, "y": 200}, {"x": 200, "y": 0}],
    "alt": "Sam's journey: up to 200 m in 100 s, flat for 50 s, back to 0 in 50 s",
}

section_dt = {
    "id": "distance-time",
    "lessons": "Lessons 6–7",
    "title": "Distance–time graphs",
    "blurb": "Reading the shape of a distance–time graph, finding the speed from its gradient, and drawing one from a description of a journey.",
    "equations": [DT_SPEED_EQ],
    "checklist": [
        "Know how constant speed, stationary, constant speed towards home, speeding up and slowing down are shown on a distance–time graph",
        "Use the gradient to work out the speed from a distance–time graph",
        "Draw a distance–time graph to represent a journey",
    ],
    "parts": [
        {
            "kind": "explain",
            "title": "Reading a distance–time graph",
            "html": (
                "<p>A <b>distance–time graph</b> has <b>distance from the start on the y-axis</b> and <b>time on the x-axis</b>. "
                "The <b>shape</b> of the line tells you what the object is doing:</p>"
                "<table class=\"tbl\"><tr><th>Shape of line</th><th>What the object is doing</th></tr>"
                "<tr><td>Straight line sloping <b>upwards</b></td><td><b>Constant speed</b>, moving away from the start. The steeper the line, the faster it is going.</td></tr>"
                "<tr><td><b>Horizontal</b> line</td><td><b>Stationary</b> (not moving). Distance stays the same as time passes.</td></tr>"
                "<tr><td>Straight line sloping <b>downwards</b></td><td><b>Constant speed back towards the start</b> (heading home). The distance from the start is getting smaller.</td></tr>"
                "<tr><td>Curve getting <b>steeper</b></td><td><b>Speeding up</b> (accelerating) — covering more distance each second.</td></tr>"
                "<tr><td>Curve getting <b>flatter</b></td><td><b>Slowing down</b> (decelerating) — covering less distance each second.</td></tr></table>"
            ),
            "graph": graph_dt_shapes,
            "after": (
                "<p><b>The gradient of a distance–time graph is the speed.</b> That is because gradient "
                "$= \\dfrac{\\text{change in } y}{\\text{change in } x} = \\dfrac{\\text{change in distance}}{\\text{change in time}}$ "
                "— which is exactly the speed equation.</p>"
                "<p>A <b>negative</b> gradient just means the object is moving <b>back towards the start</b>. "
                "Its speed is still a positive number (the size of the gradient).</p>"
            ),
        },
        {
            "kind": "worked",
            "title": "Finding speeds from a distance–time graph",
            "question": "The graph shows a pupil walking to a post box and back. Describe each stage and find the speed in each.",
            "graph": graph_dt_example,
            "steps": [
                "<b>A (0–20 s):</b> straight sloping line — constant speed away from home.",
                "<b>B (20–40 s):</b> horizontal — stationary (posting the letter).",
                "<b>C (40–60 s):</b> straight line sloping down — constant speed back towards home.",
                r"<b>Speed in A</b> — gradient between $(0,\ 0)$ and $(20,\ 100)$:",
            ]
            + ewau(DT_SPEED_EQ, r"\text{speed} = \dfrac{100 - 0}{20 - 0} = \dfrac{100}{20}", "5", "m/s")
            + [
                r"<b>Speed in B:</b> the line is horizontal, so the gradient is 0 and the speed is <b>0 m/s</b>.",
                r"<b>Speed in C</b> — between $(40,\ 100)$ and $(60,\ 0)$: gradient $= \dfrac{0 - 100}{60 - 40} = \dfrac{-100}{20} = -5$. The gradient is negative because she is heading home; her <b>speed is 5 m/s</b>.",
            ],
        },
        {
            "kind": "explain",
            "title": "Drawing a distance–time graph for a journey",
            "html": (
                "<ol class=\"list\">"
                "<li>Read the journey carefully and split it into stages. Write down the <b>time at the end of each stage</b> "
                "(add the times up as you go) and the <b>distance from the start</b> at that moment.</li>"
                "<li>Plot each of these as a point.</li>"
                "<li>Join the points <b>dot-to-dot</b> with a ruler (a journey can change suddenly, so no line of best fit).</li>"
                "<li>Check: stationary stages must be horizontal; returning home must slope back down to zero.</li></ol>"
            ),
        },
        {
            "kind": "practice",
            "title": "Distance–time graphs",
            "questions": [
                group(
                    "p3-s3-q1",
                    "The graph shows a delivery robot's journey.",
                    [
                        written("p3-s3-q1a", "Describe what the robot is doing in each stage, A to D.",
                                "<p><b>A (0–10 s):</b> constant speed away from the start. <b>B (10–20 s):</b> stationary. "
                                "<b>C (20–30 s):</b> constant speed away from the start, faster than in A (steeper). "
                                "<b>D (30–60 s):</b> constant speed back towards the start, arriving back at 60 s.</p>", lines=4, label="a"),
                        numeric("p3-s3-q1b", "Calculate the robot's speed in stage A.", 6, "m/s", "Gradient of stage A: it goes from (0, 0) to (10, 60).",
                                ewau(DT_SPEED_EQ, r"\text{speed} = \dfrac{60 - 0}{10 - 0}", "6", "m/s"), label="b"),
                        numeric("p3-s3-q1c", "Calculate the robot's speed in stage C.", 9, "m/s", "Stage C goes from (20, 60) to (30, 150).",
                                ewau(DT_SPEED_EQ, r"\text{speed} = \dfrac{150 - 60}{30 - 20} = \dfrac{90}{10}", "9", "m/s"), label="c"),
                        numeric("p3-s3-q1d", "Calculate the robot's speed in stage D.", 5, "m/s", "Stage D goes from (30, 150) down to (60, 0). Speed is the size of the gradient.",
                                ewau(DT_SPEED_EQ, r"\text{gradient} = \dfrac{0 - 150}{60 - 30} = \dfrac{-150}{30}", "-5", "m/s")
                                + ["The gradient is −5, so the <b>speed is 5 m/s</b>, heading back towards the start. (An answer of −5 is marked right here too.)"],
                                label="d", tolerance=0.02),
                        choice("p3-s3-q1e", "In which stage is the robot moving fastest?", ["A", "B", "C", "D"], 2,
                               "Stage C has the steepest line, so the biggest gradient and the greatest speed.", label="e"),
                        numeric("p3-s3-q1f", "Calculate the robot's <b>average speed</b> for the whole journey. (Careful: total <i>distance travelled</i>, not final distance from the start!)",
                                5, "m/s", "Add up the distance covered in every stage: 60 + 0 + 90 + 150. The whole journey takes 60 s.",
                                [r"Total distance travelled $= 60 + 0 + 90 + 150 = 300$ m. Total time $= 60$ s."]
                                + ewau(AVG_EQ, r"\text{average speed} = \dfrac{300}{60}", "5", "m/s"), label="f"),
                    ],
                    graph=graph_dt_practice,
                ),
                group(
                    "p3-s3-q2",
                    "Two distance–time graphs are shown.",
                    [
                        choice("p3-s3-q2a", "Which graph shows an object <b>speeding up</b>?", ["P", "Q"], 0,
                               "P gets steeper as time goes on, so more distance is covered each second — speeding up. Q gets flatter — slowing down.", label="a"),
                        written("p3-s3-q2b", "Explain how you can tell from the shape of the lines.",
                                "<p>On P the curve gets <b>steeper</b>, so the gradient (the speed) is increasing — the object covers more distance "
                                "each second. On Q the curve gets <b>flatter</b>, so the gradient is decreasing — less distance each second, slowing down.</p>",
                                lines=3, label="b"),
                    ],
                    graph=graph_dt_curves,
                ),
                group(
                    "p3-s3-q3",
                    "Sam walks 200 m to the shop at a constant speed, taking 100 s. He spends 50 s inside the shop. He then jogs home at a constant speed, taking 50 s.",
                    [
                        draw("p3-s3-q3a", "Draw a distance–time graph for Sam's journey: tap the grid to place the points in order, or draw it on paper (and label the axes with units).",
                             grid_sam, graph_sam_answer,
                             "<p>Points at (0 s, 0 m), (100 s, 200 m), (150 s, 200 m) and (200 s, 0 m), joined dot-to-dot with a ruler: "
                             "a line up to 200 m, a horizontal line for 50 s, then a line back down to 0 m.</p>",
                             hint="Work out the time at the end of each stage: 100 s, then 150 s, then 200 s.", label="a"),
                        numeric("p3-s3-q3b", "Calculate Sam's jogging speed on the way home.", 4, "m/s", "He covers 200 m in 50 s.",
                                ewau(SPEED_EQ, r"\text{speed} = \dfrac{200}{50}", "4", "m/s")
                                + ["(The gradient of that part of the graph is −4, because he is heading home, but his speed is 4 m/s.)"], label="b"),
                    ],
                ),
            ],
        },
    ],
}

# ---------------------------------------------------------------------
# Section 4 · Acceleration
# ---------------------------------------------------------------------

ACC_EQ = r"a = \dfrac{v - u}{t}"
ACC_WORDS = r"\text{acceleration} = \dfrac{\text{change in speed}}{\text{time taken}}"

section_acc = {
    "id": "acceleration",
    "lessons": "Lessons 8–10",
    "title": "Acceleration",
    "blurb": "What acceleration means, calculating it (including deceleration), and planning a practical to measure it with good measurements.",
    "equations": [ACC_EQ],
    "checklist": [
        "Know what is meant by the term 'acceleration'",
        "Calculate the size of the acceleration of an object",
        "Devise a practical to measure the acceleration of an object",
        "Take appropriate measurements in a practical",
    ],
    "parts": [
        {
            "kind": "explain",
            "title": "What is acceleration?",
            "html": (
                "<p><b>Acceleration</b> is <b>how quickly the speed changes</b> — the change in speed every second.</p>"
                "$$" + ACC_WORDS + r" = \dfrac{\text{final speed} - \text{initial speed}}{\text{time taken}}$$"
                "<p>Using symbols, where $u$ is the <b>initial</b> (starting) speed and $v$ is the <b>final</b> speed:</p>"
                "$$" + ACC_EQ + "$$"
                "<p><b>Units:</b> speed is in m/s and time is in s, so acceleration is in (m/s) per s, written <b>m/s²</b> "
                "(\"metres per second squared\"). An acceleration of 3 m/s² means the speed increases by 3 m/s <i>every second</i>.</p>"
                "<ul class=\"list\">"
                "<li>If the object is <b>speeding up</b>, the acceleration is <b>positive</b>.</li>"
                "<li>If the object is <b>slowing down</b>, the acceleration is <b>negative</b>. This is called a <b>deceleration</b>.</li>"
                "<li>\"From rest\" or \"starts from stationary\" means $u = 0$. \"Comes to a stop\" means $v = 0$.</li></ul>"
            ),
        },
        {
            "kind": "worked",
            "title": "Calculating acceleration",
            "question": "A car accelerates from rest to 24 m/s in 8 s. Calculate its acceleration.",
            "steps": [r"From rest means the initial speed $u = 0$ m/s. Final speed $v = 24$ m/s. Time $t = 8$ s."]
            + ewau(ACC_EQ, r"a = \dfrac{24 - 0}{8} = \dfrac{24}{8}", "3", "m/s²"),
        },
        {
            "kind": "worked",
            "title": "Deceleration",
            "question": "A cyclist slows from 10 m/s to 4 m/s in 3 s. Calculate her acceleration.",
            "steps": ewau(ACC_EQ, r"a = \dfrac{4 - 10}{3} = \dfrac{-6}{3}", "-2", "m/s²")
            + ["The minus sign shows she is slowing down: a <b>deceleration of 2 m/s²</b>."],
        },
        {
            "kind": "practice",
            "title": "Acceleration",
            "questions": [
                choice("p3-s4-q1", "Acceleration is the change in … every second.", ["speed", "distance", "time"], 0,
                       "Acceleration is the change in speed every second. Its unit is m/s²."),
                numeric("p3-s4-q2", "A train starts from rest and reaches 30 m/s after 60 s. Calculate its acceleration.", 0.5, "m/s²",
                        "From rest means u = 0.", ewau(ACC_EQ, r"a = \dfrac{30 - 0}{60}", "0.5", "m/s²")),
                numeric("p3-s4-q3", "A ball speeds up from 2 m/s to 14 m/s in 4 s. Calculate its acceleration.", 3, "m/s²",
                        "Final speed minus initial speed, divided by the time.", ewau(ACC_EQ, r"a = \dfrac{14 - 2}{4} = \dfrac{12}{4}", "3", "m/s²")),
                numeric("p3-s4-q4", "A car brakes from 20 m/s to 5 m/s in 5 s. Calculate its acceleration. (Include the sign.)", -3, "m/s²",
                        "It is slowing down, so expect a negative answer.",
                        ewau(ACC_EQ, r"a = \dfrac{5 - 20}{5} = \dfrac{-15}{5}", "-3", "m/s²")
                        + ["The negative sign shows the car is slowing down — a deceleration of 3 m/s²."]),
                numeric("p3-s4-q5", "A rocket sled accelerates from rest at 2 m/s² for 6 s. What is its final speed?", 12, "m/s",
                        "Rearrange: change in speed = acceleration × time. It started from rest.",
                        ewau(r"\text{change in speed} = a \times t", r"\text{change in speed} = 2 \times 6", "12", "m/s")
                        + ["It started from rest, so final speed $= 0 + 12 = 12$ m/s."]),
                written("p3-s4-q6", "Explain why the unit of acceleration is m/s² and not m/s.",
                        "<p>Acceleration is a change in speed (m/s) divided by a time (s). (m/s) ÷ s = m/s². It tells you how many m/s "
                        "the speed changes by <i>each second</i>, which is a different kind of quantity from a speed.</p>", lines=2),
            ],
        },
        {
            "kind": "explain",
            "title": "Devising a practical to measure acceleration",
            "html": (
                "<p>To find an acceleration you need to measure <b>two things</b>: the <b>change in speed</b> and the <b>time</b> it took. "
                "Here is a method for a trolley rolling down a ramp.</p>"
                "<figure class=\"diagram\">" + open(os.path.join(os.path.dirname(__file__), "ramp.svg")).read() + "</figure>"
                "<h4>Equipment</h4><p>Trolley, ramp, two light gates connected to a timer/datalogger, a card of known length fixed to the trolley, "
                "a ruler, a stopwatch (as a back-up).</p>"
                "<h4>Method</h4><ol class=\"list\">"
                "<li><b>Measure the length of the card</b> with a ruler (in metres).</li>"
                "<li>Release the trolley from the same mark on the ramp each time (<b>don't push it</b>).</li>"
                "<li>Each light gate records how long the card takes to pass through it. <b>Speed at a gate</b> "
                "$= \\dfrac{\\text{card length}}{\\text{time to pass through}}$. This gives $u$ at gate 1 and $v$ at gate 2.</li>"
                "<li>The timer also records the <b>time taken to travel from gate 1 to gate 2</b>. This is $t$.</li>"
                "<li>Calculate $a = \\dfrac{v - u}{t}$.</li>"
                "<li><b>Repeat</b> at least three times and calculate a <b>mean</b>. Ignore any anomalous result.</li></ol>"
                "<h4>Why light gates and not a stopwatch?</h4>"
                "<p>A person's <b>reaction time</b> (about 0.2 s) makes stopwatch timings unreliable when the times are short. "
                "Light gates start and stop automatically, so the measurement is more <b>accurate</b>.</p>"
                "<h4>Variables</h4>"
                "<table class=\"tbl\"><tr><th>Type</th><th>In this experiment</th></tr>"
                "<tr><td><b>Independent</b> (the one you change)</td><td>e.g. the height (steepness) of the ramp, if you are investigating what affects the acceleration.</td></tr>"
                "<tr><td><b>Dependent</b> (the one you measure)</td><td>The acceleration of the trolley (found from the speeds and time).</td></tr>"
                "<tr><td><b>Control</b> (kept the same)</td><td>Same trolley, same mass, same release point, same distance between the light gates, same surface.</td></tr></table>"
                "<h4>Taking good measurements</h4><ul class=\"list\">"
                "<li>Use the <b>right instrument</b>: ruler for the card length, light gates for short times.</li>"
                "<li>Read scales at eye level to avoid parallax error.</li>"
                "<li>Record results in a <b>table</b> with headings and units, and repeat to spot anomalies.</li>"
                "<li>Write times to a sensible number of decimal places (what the timer actually shows).</li></ul>"
            ),
        },
        {
            "kind": "practice",
            "title": "Planning and measuring",
            "questions": [
                written("p3-s4-q7",
                        "A pupil wants to measure the acceleration of a toy car rolling down a slope. Describe a method she could use. "
                        "Include: the equipment, <b>what she would measure</b>, how she would calculate the acceleration, and <b>one</b> way to make the results more reliable.",
                        "<p>A good answer includes: equipment (slope, toy car, two light gates and timer — or a stopwatch — ruler, card); "
                        "measuring the card length with a ruler; measuring the speed at two points (card length ÷ time through each light gate); "
                        "measuring the time between the two points; calculating $a = \\dfrac{v - u}{t}$; releasing from the same point without pushing; "
                        "repeating at least three times and finding a mean, discarding anomalies; keeping the slope angle and car the same.</p>",
                        lines=7),
                group(
                    "p3-s4-q8",
                    "In the light-gate experiment, the card is 0.10 m long. It takes 0.050 s to pass through gate 1 and 0.020 s to pass through gate 2. The trolley takes 0.60 s to travel between the gates.",
                    [
                        numeric("p3-s4-q8a", "Calculate the speed at gate 1.", 2, "m/s", "Speed = card length ÷ time to pass through.",
                                ewau(SPEED_EQ, r"\text{speed} = \dfrac{0.10}{0.050}", "2", "m/s"), label="a"),
                        numeric("p3-s4-q8b", "Calculate the speed at gate 2.", 5, "m/s", "Same card, shorter time — so a faster speed.",
                                ewau(SPEED_EQ, r"\text{speed} = \dfrac{0.10}{0.020}", "5", "m/s"), label="b"),
                        numeric("p3-s4-q8c", "Calculate the acceleration of the trolley.", 5, "m/s²", "u is the speed at gate 1, v the speed at gate 2, t the time between them.",
                                ewau(ACC_EQ, r"a = \dfrac{5 - 2}{0.60} = \dfrac{3}{0.60}", "5", "m/s²"), label="c"),
                    ],
                ),
                written("p3-s4-q9", "Explain why using a stopwatch to time the card through a light gate's position would give a less accurate result than using the light gate itself.",
                        "<p>The time for a card to pass through a gate is very short (a fraction of a second). Human reaction time (about 0.2 s) is a large "
                        "fraction of that, so the stopwatch reading would be far too inaccurate. A light gate starts and stops the timer automatically.</p>", lines=2),
                written("p3-s4-q10", "A pupil's three repeat readings for the time between gates are 0.61 s, 0.59 s and 0.92 s. Which reading is anomalous, and what should the pupil do about it?",
                        "<p>0.92 s is anomalous — it is much larger than the other two. The pupil should ignore it when calculating the mean "
                        "(and repeat the reading if possible). Mean of the other two $= \\dfrac{0.61 + 0.59}{2} = 0.60$ s.</p>", lines=2),
            ],
        },
    ],
}

# ---------------------------------------------------------------------
# Section 5 · Speed–time graphs
# ---------------------------------------------------------------------

VT_ACC_EQ = r"a = \text{gradient} = \dfrac{\text{change in speed}}{\text{change in time}}"
AREA_EQ = r"\text{distance} = \text{area under the graph}"

graph_vt_shapes = {
    "x": axis("Time (s)", 40, 10, minor=2),
    "y": axis("Speed (m/s)", 30, 5, minor=1),
    "series": [
        line([[0, 0], [10, 20]]),
        line([[10, 20], [20, 20]]),
        line([[20, 20], [30, 0]]),
        line([[30, 0], [40, 0]]),
        vline(10, 30), vline(20, 30), vline(30, 30),
    ],
    "labels": [label(5, 26, "accelerating"), label(15, 26, "constant speed"), label(25, 26, "decelerating"), label(35, 26, "stationary"), label(35, 23, "(speed = 0)")],
    "alt": "The shapes on a speed–time graph: rising line, flat line, falling line, line along the axis",
}

graph_vt_example = {
    "x": axis("Time (s)", 40, 5, minor=1),
    "y": axis("Speed (m/s)", 25, 5, minor=1),
    "series": [line([[0, 0], [10, 20], [30, 20], [40, 0]])],
    "shade": [{"series": 0, "from": 0, "to": 10}, {"series": 0, "from": 10, "to": 30}, {"series": 0, "from": 30, "to": 40}],
    "marks": [{"x": 10, "y": 20}, {"x": 30, "y": 20}, {"x": 40, "y": 0}],
    "labels": [label(7, 3, "triangle 1"), label(20, 9, "rectangle"), label(33, 3, "triangle 2")],
    "alt": "Speed–time graph: up to 20 m/s in 10 s, constant to 30 s, down to 0 at 40 s, with the area split into two triangles and a rectangle",
}

graph_vt_practice = {
    "x": axis("Time (s)", 30, 5, minor=1),
    "y": axis("Speed (m/s)", 20, 5, minor=1),
    "series": [line([[0, 0], [5, 15], [20, 15], [30, 0]]), vline(5, 20), vline(20, 20)],
    "marks": [{"x": 5, "y": 15}, {"x": 20, "y": 15}, {"x": 30, "y": 0}],
    "alt": "Speed–time graph for a motorbike: up to 15 m/s in 5 s, constant to 20 s, down to 0 at 30 s",
}

grid_bus = {
    "x": axis("Time (s)", 24, 4, minor=4),
    "y": axis("Speed (m/s)", 15, 5, minor=5),
    "series": [],
    "alt": "A blank grid for drawing a speed–time graph",
}

graph_bus_answer = {
    "x": axis("Time (s)", 24, 4, minor=4),
    "y": axis("Speed (m/s)", 15, 5, minor=5),
    "series": [line([[0, 0], [6, 12], [20, 12], [24, 0]])],
    "marks": [{"x": 6, "y": 12}, {"x": 20, "y": 12}, {"x": 24, "y": 0}],
    "alt": "The bus journey: up to 12 m/s in 6 s, constant to 20 s, down to 0 at 24 s",
}

section_vt = {
    "id": "speed-time",
    "lessons": "Lessons 11 onwards",
    "title": "Speed–time graphs",
    "blurb": "Reading the shape of a speed–time graph, finding acceleration from the gradient, finding distance from the area under the line, and drawing one from a description.",
    "equations": [VT_ACC_EQ, AREA_EQ],
    "checklist": [
        "Know how constant speed, stationary, acceleration and deceleration are shown on a speed–time graph",
        "Use the gradient to work out the acceleration from a speed–time graph",
        "Use the area under a slope or horizontal line to work out the distance travelled in that time",
        "Draw a speed–time graph to represent a journey",
    ],
    "parts": [
        {
            "kind": "explain",
            "title": "Watch out!",
            "tone": "warn",
            "html": (
                "<p>A speed–time graph looks similar to a distance–time graph but means something completely different. "
                "<b>Always read the y-axis label first.</b> A horizontal line on a distance–time graph means <i>stationary</i>; "
                "a horizontal line on a speed–time graph means <i>constant speed</i>.</p>"
            ),
        },
        {
            "kind": "explain",
            "title": "Reading a speed–time graph",
            "html": (
                "<p>A <b>speed–time graph</b> has <b>speed on the y-axis</b> and <b>time on the x-axis</b>.</p>"
                "<table class=\"tbl\"><tr><th>Shape of line</th><th>What the object is doing</th></tr>"
                "<tr><td><b>Horizontal</b> line above the x-axis</td><td><b>Constant speed</b>. Speed is not changing.</td></tr>"
                "<tr><td>Horizontal line <b>along the x-axis</b> (speed = 0)</td><td><b>Stationary</b>.</td></tr>"
                "<tr><td>Straight line sloping <b>upwards</b></td><td><b>Constant acceleration</b> — speeding up steadily. Steeper = bigger acceleration.</td></tr>"
                "<tr><td>Straight line sloping <b>downwards</b></td><td><b>Constant deceleration</b> — slowing down steadily.</td></tr></table>"
            ),
            "graph": graph_vt_shapes,
            "after": (
                "<p><b>The gradient of a speed–time graph is the acceleration</b>, because gradient "
                "$= \\dfrac{\\text{change in speed}}{\\text{change in time}}$, which is the acceleration equation. "
                "A negative gradient is a deceleration.</p>"
            ),
        },
        {
            "kind": "explain",
            "title": "Area under a speed–time graph = distance travelled",
            "html": (
                "<p>Because distance $=$ speed $\\times$ time, the <b>area between the line and the x-axis</b> gives the distance travelled.</p>"
                "<ul class=\"list\">"
                "<li>Under a <b>horizontal line</b> (constant speed) the shape is a <b>rectangle</b>: area $= \\text{speed} \\times \\text{time}$.</li>"
                "<li>Under a <b>sloping line</b> (accelerating from rest, or decelerating to rest) the shape is a <b>triangle</b>: "
                "area $= \\tfrac{1}{2} \\times \\text{base} \\times \\text{height} = \\tfrac{1}{2} \\times \\text{time} \\times \\text{speed}$.</li></ul>"
                "<p><b>Method:</b> split the area into rectangles and triangles, work out each one, then <b>add them up</b>. "
                "Use the <i>numbers on the axes</i>, not centimetres on the paper.</p>"
            ),
        },
        {
            "kind": "worked",
            "title": "Acceleration and distance from a speed–time graph",
            "question": "The graph shows a tram journey between two stops. Describe the journey, find the acceleration in the first 10 s, and find the total distance travelled.",
            "graph": graph_vt_example,
            "steps": [
                "<b>Describe:</b> 0–10 s constant acceleration from rest; 10–30 s constant speed of 20 m/s; 30–40 s constant deceleration to rest.",
                r"<b>Acceleration in the first 10 s</b> — gradient from $(0,\ 0)$ to $(10,\ 20)$:",
            ]
            + ewau(VT_ACC_EQ, r"a = \dfrac{20 - 0}{10 - 0} = \dfrac{20}{10}", "2", "m/s²")
            + [
                r"<b>Deceleration in the last 10 s:</b> $\dfrac{0 - 20}{40 - 30} = \dfrac{-20}{10} = -2$ m/s², a deceleration of 2 m/s².",
                "<b>Total distance</b> — add the three areas:",
            ]
            + ewau(
                r"\text{distance} = \text{triangle 1} + \text{rectangle} + \text{triangle 2}",
                r"= \left(\tfrac{1}{2} \times 10 \times 20\right) + (20 \times 20) + \left(\tfrac{1}{2} \times 10 \times 20\right) = 100 + 400 + 100",
                "600", "m",
            ),
        },
        {
            "kind": "explain",
            "title": "Drawing a speed–time graph for a journey",
            "html": (
                "<ol class=\"list\">"
                "<li>Split the journey into stages and write down the <b>time at the end of each stage</b> and the <b>speed</b> at that moment.</li>"
                "<li>Plot each point and join them <b>dot-to-dot</b> with a ruler.</li>"
                "<li>Check: \"constant speed\" must be horizontal; \"accelerates from rest\" starts at speed 0; \"comes to a stop\" finishes at speed 0.</li></ol>"
            ),
        },
        {
            "kind": "practice",
            "title": "Speed–time graphs",
            "questions": [
                group(
                    "p3-s5-q1",
                    "The graph shows a motorbike's journey.",
                    [
                        written("p3-s5-q1a", "Describe the motion in each of the three stages.",
                                "<p>0–5 s: constant acceleration from rest to 15 m/s. 5–20 s: constant speed of 15 m/s. 20–30 s: constant deceleration to a stop.</p>",
                                lines=3, label="a"),
                        numeric("p3-s5-q1b", "Calculate the acceleration during the first 5 s.", 3, "m/s²", "Gradient: the speed goes from 0 to 15 m/s in 5 s.",
                                ewau(VT_ACC_EQ, r"a = \dfrac{15 - 0}{5 - 0}", "3", "m/s²"), label="b"),
                        numeric("p3-s5-q1c", "Calculate the acceleration between 20 s and 30 s. (Include the sign.)", -1.5, "m/s²",
                                "The speed falls from 15 m/s to 0 in 10 s, so the gradient is negative.",
                                ewau(VT_ACC_EQ, r"a = \dfrac{0 - 15}{30 - 20} = \dfrac{-15}{10}", "-1.5", "m/s²")
                                + ["A deceleration of 1.5 m/s²."], label="c"),
                        numeric("p3-s5-q1d", "Calculate the total distance travelled. Show each area separately.", 337.5, "m",
                                "Split the area into a triangle (0–5 s), a rectangle (5–20 s) and a triangle (20–30 s).",
                                [
                                    r"Triangle (0–5 s): $\tfrac{1}{2} \times 5 \times 15 = 37.5$ m.",
                                    r"Rectangle (5–20 s): $15 \times 15 = 225$ m.",
                                    r"Triangle (20–30 s): $\tfrac{1}{2} \times 10 \times 15 = 75$ m.",
                                ]
                                + ewau(AREA_EQ, r"\text{distance} = 37.5 + 225 + 75", "337.5", "m"), label="d"),
                    ],
                    graph=graph_vt_practice,
                ),
                group(
                    "p3-s5-q2",
                    "A horizontal line appears on two different graphs.",
                    [
                        choice("p3-s5-q2a", "On a <b>distance–time</b> graph, a horizontal line means the object is…",
                               ["stationary", "moving at constant speed", "accelerating"], 0,
                               "Distance is not changing as time passes, so the object is stationary.", label="a"),
                        choice("p3-s5-q2b", "On a <b>speed–time</b> graph, a horizontal line above the axis means the object is…",
                               ["stationary", "moving at constant speed", "accelerating"], 1,
                               "Speed is not changing — but it is not zero, so the object is moving at a constant speed.", label="b"),
                    ],
                ),
                group(
                    "p3-s5-q3",
                    "A bus accelerates from rest to 12 m/s in 6 s. It travels at 12 m/s for 14 s, then decelerates to a stop in 4 s.",
                    [
                        draw("p3-s5-q3a", "Draw a speed–time graph of the journey: tap the grid to place the points in order, or draw it on paper (and label the axes with units).",
                             grid_bus, graph_bus_answer,
                             "<p>Points at (0 s, 0 m/s), (6 s, 12 m/s), (20 s, 12 m/s) and (24 s, 0 m/s), joined with ruled straight lines. "
                             "Axes: Time (s) and Speed (m/s).</p>",
                             hint="The constant-speed stage ends at 6 + 14 = 20 s, and the bus stops at 24 s.", label="a"),
                        numeric("p3-s5-q3b", "Calculate the acceleration in the first 6 s.", 2, "m/s²", "Speed goes from 0 to 12 m/s in 6 s.",
                                ewau(VT_ACC_EQ, r"a = \dfrac{12 - 0}{6}", "2", "m/s²"), label="b"),
                        numeric("p3-s5-q3c", "Calculate the acceleration in the last 4 s. (Include the sign.)", -3, "m/s²", "Speed falls from 12 m/s to 0 in 4 s.",
                                ewau(VT_ACC_EQ, r"a = \dfrac{0 - 12}{4}", "-3", "m/s²") + ["A deceleration of 3 m/s²."], label="c"),
                        numeric("p3-s5-q3d", "Use your graph to calculate the total distance the bus travels.", 228, "m",
                                "Triangle + rectangle + triangle.",
                                [
                                    r"Triangle (0–6 s): $\tfrac{1}{2} \times 6 \times 12 = 36$ m.",
                                    r"Rectangle (6–20 s): $14 \times 12 = 168$ m.",
                                    r"Triangle (20–24 s): $\tfrac{1}{2} \times 4 \times 12 = 24$ m.",
                                ]
                                + ewau(AREA_EQ, r"\text{distance} = 36 + 168 + 24", "228", "m"), label="d"),
                    ],
                ),
            ],
        },
    ],
}

# ---------------------------------------------------------------------
# Key facts
# ---------------------------------------------------------------------

key_facts = [
    ("What is the speed equation?", "$" + SPEED_EQ + "$"),
    ("Unit of speed (in physics)?", "m/s"),
    ("How do you find distance from speed and time?", "$" + DIST_EQ + "$"),
    ("What does EWAU stand for?", "Equation, Working, Answer, Units"),
    ("Average speed equation?", "$" + AVG_EQ + "$ (including stops)"),
    ("What is instantaneous speed?", "The speed at one particular moment"),
    ("Gradient equation?", "$" + GRAD_EQ + "$"),
    ("What does a negative gradient look like?", "A line sloping down to the right"),
    ("Horizontal line on a distance–time graph means…", "Stationary"),
    ("Gradient of a distance–time graph gives…", "Speed"),
    ("Curve getting steeper on a distance–time graph means…", "Speeding up (accelerating)"),
    ("Acceleration equation?", "$" + ACC_EQ + "$ (change in speed ÷ time)"),
    ("Unit of acceleration?", "m/s²"),
    ("A negative acceleration is called…", "A deceleration"),
    ("Horizontal line on a speed–time graph means…", "Constant speed"),
    ("Gradient of a speed–time graph gives…", "Acceleration"),
    ("Area under a speed–time graph gives…", "Distance travelled"),
    ("Area of a triangle?", r"$\tfrac{1}{2} \times \text{base} \times \text{height}$"),
    ("Why use light gates rather than a stopwatch?", "They remove human reaction time, so timings are more accurate"),
]

section_facts = {
    "id": "key-facts",
    "lessons": "Whole topic",
    "title": "Key facts",
    "blurb": "Cover and test yourself: tap a card to flip it, or cover the right-hand column on the printout.",
    "equations": [],
    "checklist": [],
    "parts": [
        {
            "kind": "facts",
            "title": "Cover and test yourself",
            "items": [{"q": question, "a": answer} for question, answer in key_facts],
        }
    ],
}

# ---------------------------------------------------------------------
# The topic
# ---------------------------------------------------------------------

topic = {
    "id": "p3-motion",
    "order": 1,
    "title": "P3 Motion",
    "subtitle": "Speed, graph skills, distance–time graphs, acceleration and speed–time graphs",
    "stage": "Key Stage 3",
    "lede": (
        "Everything on the P3 revision checklist, in order. Each lesson's ideas are explained, shown in a worked example, "
        "then practised straight away — with answers checked as you go."
    ),
    "howto": [
        "Read the explanation. Cover it up and try to say it back to yourself in your own words.",
        "Study the worked example. Reveal the steps one at a time and notice <i>how</i> the answer is laid out, not just what it is.",
        "Do the practice questions <b>before</b> opening the hint or walkthrough. Write every calculation in EWAU layout on paper first, then type the answer to check it.",
        "If you got something wrong, go back to the explanation, then try the question again.",
        "Fill in the traffic-light self-check at the end of each section. Anything red or amber is what to revise next.",
    ],
    "sections": [section_speed, section_graphs, section_dt, section_acc, section_vt, section_facts],
}


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, "..", "data", "p3-motion.json")
    with open(out, "w", encoding="utf-8") as handle:
        json.dump(topic, handle, ensure_ascii=False, indent=1)
    # Count the questions for the summary line
    count = 0
    for section in topic["sections"]:
        for part in section["parts"]:
            if part["kind"] != "practice":
                continue
            for question in part["questions"]:
                if question["type"] == "group":
                    count += len(question["parts"])
                else:
                    count += 1
    print("wrote", os.path.normpath(out), "-", len(topic["sections"]), "sections,", count, "questions")


if __name__ == "__main__":
    main()
