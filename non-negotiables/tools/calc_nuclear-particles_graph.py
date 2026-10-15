#!/usr/bin/env python3
"""Compute every answer and every plotted coordinate for the graph type
"decay-graph" in data/nuclear-particles.json.

Run: python3 tools/calc_nuclear-particles_graph.py [out.json]

Prints each answer rounded to 3 s.f. with its question id. If an output
path is given, writes the complete type object (with graphs) there so it
can be appended to the topic file.
"""

import json
import math
import sys

LN2 = math.log(2)

results = []


def round_sf(value, sf=3):
    """Round a value to the given number of significant figures."""
    if value == 0:
        return 0.0
    magnitude = math.floor(math.log10(abs(value)))
    places = sf - 1 - magnitude
    rounded = round(value, places)
    # Large round numbers are stored as integers so the validator does not
    # mistake 9360000.0 for an unrounded float. Beyond 10^15 an int would
    # pick up binary noise, so those stay as floats (repr 1.01e+27 is fine).
    if places <= 0 and abs(rounded) < 1e15:
        rounded = int(rounded)
    return rounded


def record(question_id, value, unit):
    """Store one answer, rounded to 3 s.f."""
    results.append((question_id, round_sf(value), unit, value))
    return round_sf(value)


def tidy(value, places=4):
    """Round a plotted coordinate so the JSON stays readable."""
    rounded = round(value, places)
    if rounded == int(rounded):
        return int(rounded)
    return rounded


def sample(function, x_values):
    """Sample a function at the given x values; returns [x, y] pairs."""
    points = []
    for x in x_values:
        points.append([tidy(x), tidy(function(x))])
    return points


def frange(start, stop, step):
    """Inclusive range of floats."""
    values = []
    count = int(round((stop - start) / step))
    for index in range(count + 1):
        values.append(start + index * step)
    return values


# ---------------------------------------------------------------
# Worked example: half-life read from an activity–time curve
# ---------------------------------------------------------------
# A0 = 1200 Bq, t_half = 40 s. At t = 40 s, A = 600 Bq: both on gridlines.
A0_w = 1200.0
T_HALF_w = 40.0


def activity_w(t):
    return A0_w * math.exp(-LN2 * t / T_HALF_w)


points_w = sample(activity_w, frange(0, 120, 8))
assert abs(activity_w(40) - 600) < 1e-9
answer_w = record("decay-graph-w", T_HALF_w, "s")

# ---------------------------------------------------------------
# p1: number of undecayed nuclei at a marked time on an N–t curve
# ---------------------------------------------------------------
# N0 = 8.0 × 10^20, t_half = 3.0 h. At t = 6.0 h, N = 2.0 × 10^20.
N0_p1 = 8.0            # in units of 10^20
T_HALF_p1 = 3.0        # hours


def nuclei_p1(t):
    return N0_p1 * math.exp(-LN2 * t / T_HALF_p1)


points_p1 = sample(nuclei_p1, frange(0, 12, 0.75))
N_at_X = nuclei_p1(6.0)
assert abs(N_at_X - 2.0) < 1e-9
answer_p1 = record("decay-graph-p1", N_at_X * 1e20, "")

# ---------------------------------------------------------------
# p2: decay constant from the gradient of ln A against t (seconds)
# ---------------------------------------------------------------
# ln A = 9.0 − 0.020 t. Points P (50, 8.0) and Q (250, 4.0) on gridlines.
INTERCEPT_p2 = 9.0
LAMBDA_p2 = 0.020      # s^-1


def ln_activity_p2(t):
    return INTERCEPT_p2 - LAMBDA_p2 * t


line_p2 = [[0, tidy(ln_activity_p2(0))], [300, tidy(ln_activity_p2(300))]]
P_p2 = (50, ln_activity_p2(50))
Q_p2 = (250, ln_activity_p2(250))
gradient_p2 = (Q_p2[1] - P_p2[1]) / (Q_p2[0] - P_p2[0])
answer_p2 = record("decay-graph-p2", -gradient_p2, "s⁻¹")

# ---------------------------------------------------------------
# p3: initial activity from the y-intercept of ln A against t
# ---------------------------------------------------------------
# ln A = 6.0 − 0.125 t (t in minutes). Intercept 6.0 → A0 = e^6.0.
INTERCEPT_p3 = 6.0
SLOPE_p3 = 0.125       # min^-1


def ln_activity_p3(t):
    return INTERCEPT_p3 - SLOPE_p3 * t


line_p3 = [[0, tidy(ln_activity_p3(0))], [40, tidy(ln_activity_p3(40))]]
answer_p3 = record("decay-graph-p3", math.exp(INTERCEPT_p3), "Bq")

# ---------------------------------------------------------------
# p4: decay constant in s^-1 from ln A against t in minutes
# ---------------------------------------------------------------
# ln A = 10.0 − 0.10 t (t in minutes). P (10, 9.0), Q (50, 5.0).
INTERCEPT_p4 = 10.0
SLOPE_p4 = 0.10        # min^-1


def ln_activity_p4(t):
    return INTERCEPT_p4 - SLOPE_p4 * t


line_p4 = [[0, tidy(ln_activity_p4(0))], [60, tidy(ln_activity_p4(60))]]
P_p4 = (10, ln_activity_p4(10))
Q_p4 = (50, ln_activity_p4(50))
gradient_p4_per_min = (Q_p4[1] - P_p4[1]) / (Q_p4[0] - P_p4[0])
lambda_p4 = -gradient_p4_per_min / 60.0
answer_p4 = record("decay-graph-p4", lambda_p4, "s⁻¹")

# ---------------------------------------------------------------
# p5: half-life from an A–t curve, then the decay constant (two-step)
# ---------------------------------------------------------------
# A0 = 600 kBq, t_half = 8.0 days. At t = 8.0 days, A = 300 kBq.
A0_p5 = 600.0          # kBq
T_HALF_p5 = 8.0        # days


def activity_p5(t):
    return A0_p5 * math.exp(-LN2 * t / T_HALF_p5)


points_p5 = sample(activity_p5, frange(0, 24, 1.5))
assert abs(activity_p5(8.0) - 300) < 1e-9
lambda_p5 = LN2 / T_HALF_p5
answer_p5 = record("decay-graph-p5", lambda_p5, "day⁻¹")

# ---------------------------------------------------------------
# p6: corrected half-life from a count-rate graph with background
# ---------------------------------------------------------------
# Background 50 counts min^-1. Corrected initial rate 400 → observed 450.
# Corrected half of 400 is 200 → observed 250, reached at t = 4.0 min.
BACKGROUND_p6 = 50.0   # counts per minute
C0_p6 = 400.0          # corrected initial count rate
T_HALF_p6 = 4.0        # minutes


def observed_rate_p6(t):
    return BACKGROUND_p6 + C0_p6 * math.exp(-LN2 * t / T_HALF_p6)


points_p6 = sample(observed_rate_p6, frange(0, 10, 0.625))
assert abs(observed_rate_p6(0) - 450) < 1e-9
assert abs(observed_rate_p6(4.0) - 250) < 1e-9
answer_p6 = record("decay-graph-p6", T_HALF_p6, "min")

# ---------------------------------------------------------------
# Print the answers
# ---------------------------------------------------------------
for question_id, rounded, unit, raw in results:
    print(f"{question_id:18s} {rounded!r:>14} {unit:8s} (raw {raw:.6g})")

# ---------------------------------------------------------------
# The type object
# ---------------------------------------------------------------
BOARDS = ["AQA", "OCR A", "OCR B", "Edexcel", "WJEC"]

type_object = {
    "id": "decay-graph",
    "name": "Reading decay graphs",
    "equations": [
        "t½: the time for A (or N, or the corrected count rate) to halve",
        "λ = ln 2 / t½",
        "ln A = ln A₀ − λt: gradient = −λ, intercept = ln A₀"
    ],
    "boards": BOARDS,
    "method": "On an activity–time or N–t curve, read the starting value, halve it, and read across and down to find the half-life (do this from the graph, not from memory). On a graph of ln A against t the line is straight: its gradient is −λ and its y-intercept is ln A₀, so A₀ = e^(intercept). With a count-rate graph, subtract the stated background from every reading before you halve anything.",
    "commonErrors": [
        "Halving the time axis instead of the activity axis",
        "Quoting the gradient of a ln A graph as λ with the minus sign still attached",
        "Reading the y-intercept of ln A against t as A₀ instead of ln A₀",
        "Finding the half-life of a count-rate curve without subtracting the background first"
    ],
    "worked": {
        "id": "decay-graph-w",
        "question": "The graph shows how the activity A of a short-lived source in a school laboratory varies with time t. Point X is marked. Use the graph to determine the half-life of the source.",
        "steps": [
            "Known: the curve starts at A₀ = 1200 Bq when t = 0. Unknown: t½, the time for the activity to fall to A₀ / 2.",
            "A₀ / 2 = 1200 / 2 = 600 Bq",
            "Read across from A = 600 Bq to the curve (point X) and down to the time axis.",
            "X is at (40 s, 600 Bq), so the activity halves in 40 s.",
            "t½ = 40 s"
        ],
        "answer": {"value": answer_w, "unit": "s"},
        "graph": {
            "x": {"label": "t / s", "min": 0, "max": 120, "step": 20},
            "y": {"label": "A / Bq", "min": 0, "max": 1200, "step": 200},
            "series": [
                {"kind": "curve", "points": points_w}
            ],
            "marks": [{"x": 40, "y": 600, "label": "X", "drop": True}],
            "alt": "Activity–time curve falling exponentially from 1200 Bq at t = 0, passing through point X at 600 Bq when t = 40 s, with dotted lines from X to both axes"
        }
    },
    "practice": [
        {
            "id": "decay-graph-p1",
            "question": "A hospital generator produces a short-lived isotope. The graph shows how the number N of undecayed nuclei in a sample varies with time t. Point X is marked at t = 6.0 hours. Use the graph to determine the number of undecayed nuclei at X.",
            "hint": "Read straight across from X to the N axis, and remember the axis is in units of 10²⁰.",
            "walkthrough": [
                "X is on the curve at t = 6.0 hours; follow the dotted line across to the N axis.",
                "The reading is 2.0 on an axis labelled N / 10²⁰.",
                "Check: N₀ = 8.0 × 10²⁰ and 6.0 hours is two half-lives of 3.0 hours, so N should be 8.0 × 10²⁰ / 4.",
                "N = 2.0 × 10²⁰"
            ],
            "answer": {"value": answer_p1, "unit": ""},
            "graph": {
                "x": {"label": "t / hours", "min": 0, "max": 12, "step": 2},
                "y": {"label": "N / 10²⁰", "min": 0, "max": 8, "step": 1},
                "series": [
                    {"kind": "curve", "points": points_p1}
                ],
                "marks": [{"x": 6, "y": 2, "label": "X", "drop": True}],
                "alt": "Curve of number of undecayed nuclei against time falling exponentially from 8.0 × 10²⁰ at t = 0 to 0.5 × 10²⁰ at 12 hours, with point X marked at 6.0 hours and 2.0 × 10²⁰"
            }
        },
        {
            "id": "decay-graph-p2",
            "question": "A radioactive gas is sealed in a chamber and its activity A is measured for 300 s. The graph shows ln A plotted against time t; points P and Q lie on the line. Use the graph to determine the decay constant of the gas.",
            "hint": "ln A = ln A₀ − λt, so the gradient of the line is −λ; use P and Q to find the gradient.",
            "walkthrough": [
                "P is at (50 s, 8.0) and Q is at (250 s, 4.0).",
                "Gradient = (4.0 − 8.0) / (250 − 50) = −4.0 / 200 = −0.020 s⁻¹",
                "Gradient = −λ, so λ = 0.020 s⁻¹",
                "λ = 2.0 × 10⁻² s⁻¹"
            ],
            "answer": {"value": answer_p2, "unit": "s⁻¹"},
            "graph": {
                "x": {"label": "t / s", "min": 0, "max": 300, "step": 50},
                "y": {"label": "ln (A / Bq)", "min": 3, "max": 9, "step": 1},
                "series": [
                    {"kind": "line", "points": line_p2}
                ],
                "marks": [
                    {"x": 50, "y": 8.0, "label": "P"},
                    {"x": 250, "y": 4.0, "label": "Q"}
                ],
                "alt": "Straight line of ln A against t falling from 9.0 at t = 0 through point P at (50 s, 8.0) and point Q at (250 s, 4.0) to 3.0 at 300 s"
            }
        },
        {
            "id": "decay-graph-p3",
            "question": "A radioactive tracer is injected into a pipeline to find a leak. The graph shows ln A against time t for the tracer, where A is its activity in Bq. Use the y-intercept of the graph to determine the initial activity A₀ of the tracer.",
            "hint": "The intercept is ln A₀, not A₀; undo the natural log with A₀ = e^(intercept).",
            "walkthrough": [
                "ln A = ln A₀ − λt, so the y-intercept is ln A₀.",
                "Read the intercept: ln A₀ = 6.0",
                "A₀ = e^6.0",
                "A₀ = 403 Bq"
            ],
            "answer": {"value": answer_p3, "unit": "Bq"},
            "graph": {
                "x": {"label": "t / min", "min": 0, "max": 40, "step": 5},
                "y": {"label": "ln (A / Bq)", "min": 0, "max": 7, "step": 1},
                "series": [
                    {"kind": "line", "points": line_p3}
                ],
                "marks": [{"x": 0, "y": 6.0, "label": "intercept", "dx": 10, "dy": 4}],
                "alt": "Straight line of ln A against t in minutes starting at an intercept of 6.0 on the ln A axis and falling to 1.0 at 40 minutes"
            }
        },
        {
            "id": "decay-graph-p4",
            "question": "A nuclear medicine department measures the activity A of a freshly prepared isotope. The graph shows ln A against time t in minutes; points P and Q lie on the line. Use the graph to determine the decay constant of the isotope in s⁻¹.",
            "hint": "The gradient from P and Q is −λ in min⁻¹; divide by 60 to convert λ to s⁻¹.",
            "walkthrough": [
                "P is at (10 min, 9.0) and Q is at (50 min, 5.0).",
                "Gradient = (5.0 − 9.0) / (50 − 10) = −4.0 / 40 = −0.10 min⁻¹",
                "λ = 0.10 min⁻¹ = 0.10 / 60 s⁻¹",
                "λ = 1.67 × 10⁻³ s⁻¹"
            ],
            "answer": {"value": answer_p4, "unit": "s⁻¹"},
            "graph": {
                "x": {"label": "t / min", "min": 0, "max": 60, "step": 10},
                "y": {"label": "ln (A / Bq)", "min": 4, "max": 10, "step": 1},
                "series": [
                    {"kind": "line", "points": line_p4}
                ],
                "marks": [
                    {"x": 10, "y": 9.0, "label": "P"},
                    {"x": 50, "y": 5.0, "label": "Q"}
                ],
                "alt": "Straight line of ln A against t in minutes falling from 10.0 at t = 0 through point P at (10, 9.0) and point Q at (50, 5.0) to 4.0 at 60 minutes"
            }
        },
        {
            "id": "decay-graph-p5",
            "question": "An iodine-131 source is delivered to a hospital. The graph shows how its activity A, in kBq, varies with time t in days. Point X is marked. Use the graph to determine the half-life of iodine-131 and hence its decay constant in day⁻¹.",
            "hint": "Halve the activity at t = 0, read off the time at X, then use λ = ln 2 / t½ with t½ in days.",
            "walkthrough": [
                "A₀ = 600 kBq, so A₀ / 2 = 300 kBq.",
                "X is at (8.0 days, 300 kBq), so t½ = 8.0 days.",
                "λ = ln 2 / t½ = 0.693 / 8.0",
                "λ = 0.0866 day⁻¹"
            ],
            "answer": {"value": answer_p5, "unit": "day⁻¹"},
            "graph": {
                "x": {"label": "t / days", "min": 0, "max": 24, "step": 4},
                "y": {"label": "A / kBq", "min": 0, "max": 600, "step": 100},
                "series": [
                    {"kind": "curve", "points": points_p5}
                ],
                "marks": [{"x": 8, "y": 300, "label": "X", "drop": True}],
                "alt": "Activity–time curve falling exponentially from 600 kBq at t = 0 through point X at 300 kBq when t = 8.0 days to 75 kBq at 24 days"
            }
        },
        {
            "id": "decay-graph-p6",
            "question": "A student measures the count rate from a radioactive sample with a Geiger–Müller tube. The graph shows the measured count rate C against time t. The background count rate in the laboratory is 50 counts per minute and is shown as the dashed line. Point X is marked. Use the graph to determine the half-life of the sample.",
            "hint": "Subtract the background from the count rate at t = 0, halve the corrected value, then add the background back to find which measured count rate to read across from.",
            "walkthrough": [
                "Measured count rate at t = 0 is 450 min⁻¹; corrected rate = 450 − 50 = 400 min⁻¹.",
                "Half the corrected rate is 200 min⁻¹, which is a measured rate of 200 + 50 = 250 min⁻¹.",
                "Read across from C = 250 min⁻¹ to the curve (point X) and down: t = 4.0 min.",
                "t½ = 4.0 min"
            ],
            "answer": {"value": answer_p6, "unit": "min"},
            "graph": {
                "x": {"label": "t / min", "min": 0, "max": 10, "step": 1},
                "y": {"label": "C / counts min⁻¹", "min": 0, "max": 500, "step": 50},
                "series": [
                    {"kind": "curve", "points": points_p6},
                    {"kind": "dashed", "points": [[0, 50], [10, 50]]}
                ],
                "marks": [{"x": 4, "y": 250, "label": "X", "drop": True}],
                "labels": [{"x": 6.2, "y": 80, "text": "background"}],
                "alt": "Measured count rate against time falling from 450 counts per minute at t = 0 through point X at 250 counts per minute when t = 4.0 minutes towards a dashed background level of 50 counts per minute"
            }
        }
    ]
}

if len(sys.argv) > 1:
    with open(sys.argv[1], "w", encoding="utf-8") as handle:
        json.dump(type_object, handle, ensure_ascii=False, indent=2)
    print(f"wrote {sys.argv[1]}")
