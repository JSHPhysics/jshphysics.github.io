#!/usr/bin/env python3
"""Compute every answer and every plotted coordinate for the graph type
"experiment-graph" in data/measurements.json.

Run: python3 tools/calc_measurements_graph.py [out.json]

Prints each answer rounded to 3 s.f. with its question id. If an output
path is given, writes the complete type object (with graphs) there so it
can be appended to the topic file.
"""

import json
import math
import sys

FOUR_PI_SQUARED = 4 * math.pi ** 2

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
    # pick up binary noise, so those stay as floats.
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


def gradient(point_a, point_b):
    """Gradient of the straight line through two points."""
    return (point_b[1] - point_a[1]) / (point_b[0] - point_a[0])


def scattered_data(x_values, function, offsets):
    """Plotted 'measurements': the true line value nudged by an absolute offset."""
    points = []
    for x, offset in zip(x_values, offsets):
        points.append([tidy(x), tidy(function(x) + offset, 2)])
    return points


# ---------------------------------------------------------------
# Worked example: resistivity from the gradient of R against L
# ---------------------------------------------------------------
# R = 0.5 + 4.0 L (small contact resistance), A = 4.0 × 10^-7 m².
# P (0, 0.5) and Q (1.0, 4.5) lie on gridlines.
AREA_w = 4.0e-7         # m²


def resistance_w(length):
    return 0.5 + 4.0 * length


line_w = [[0, tidy(resistance_w(0))], [1.0, tidy(resistance_w(1.0))]]
P_w = (0, resistance_w(0))
Q_w = (1.0, resistance_w(1.0))
gradient_w = gradient(P_w, Q_w)                 # Ω m^-1
rho_w = gradient_w * AREA_w
answer_w = record("experiment-graph-w", rho_w, "Ω m")

# ---------------------------------------------------------------
# p1: gradient of a best-fit line through plotted data
# ---------------------------------------------------------------
# Water heated by an immersion heater: θ = 20 + 5.0 t (t in minutes).
# Best-fit line from (0, 20) to (10, 70).


def temperature_p1(t):
    return 20 + 5.0 * t


data_p1 = scattered_data(
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    temperature_p1,
    [1.2, -0.9, 1.5, -1.3, 0.6, 1.4, -1.1, 0.8, -0.7])
fit_p1 = [[0, tidy(temperature_p1(0))], [10, tidy(temperature_p1(10))]]
gradient_p1 = gradient(fit_p1[0], fit_p1[1])
answer_p1 = record("experiment-graph-p1", gradient_p1, "°C min⁻¹")

# ---------------------------------------------------------------
# p2: g from the gradient of T² against L for a pendulum
# ---------------------------------------------------------------
# T² = (4π² / g) L. Best-fit line from (0, 0) to (1.0, 4.0): gradient 4.0.


def t_squared_p2(length):
    return 4.0 * length


data_p2 = scattered_data(
    [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
    t_squared_p2,
    [0.08, -0.06, 0.05, -0.09, 0.07, -0.04, 0.06, -0.05])
fit_p2 = [[0, 0], [1.0, tidy(t_squared_p2(1.0))]]
gradient_p2 = gradient(fit_p2[0], fit_p2[1])     # s² m^-1
g_p2 = FOUR_PI_SQUARED / gradient_p2
answer_p2 = record("experiment-graph-p2", g_p2, "m s⁻²")

# ---------------------------------------------------------------
# p3: zero error from the intercept of an extension–load graph
# ---------------------------------------------------------------
# Recorded extension x = 0.5 + 0.5 F (cm). Intercept 0.5 cm = 5.0 mm.


def extension_p3(load):
    return 0.5 + 0.5 * load


line_p3 = [[0, tidy(extension_p3(0))], [8, tidy(extension_p3(8))]]
intercept_cm_p3 = extension_p3(0)
answer_p3 = record("experiment-graph-p3", intercept_cm_p3 * 10, "mm")

# ---------------------------------------------------------------
# p4: spring constant from the gradient of T² against m
# ---------------------------------------------------------------
# T² = (4π² / k) m. Line through (0, 0) and P (0.5, 1.0): gradient 2.0.


def t_squared_p4(mass):
    return 2.0 * mass


line_p4 = [[0, 0], [0.6, tidy(t_squared_p4(0.6))]]
P_p4 = (0.5, t_squared_p4(0.5))
gradient_p4 = gradient((0, 0), P_p4)             # s² kg^-1
k_p4 = FOUR_PI_SQUARED / gradient_p4
answer_p4 = record("experiment-graph-p4", k_p4, "N m⁻¹")

# ---------------------------------------------------------------
# p5: percentage uncertainty in a gradient from a worst-fit line
# ---------------------------------------------------------------
# Best fit: x = 2.0 F through (0, 0) and (20, 40).
# Worst fit (dashed): through A (0, 2) and B (20, 38).
best_p5 = [[0, 0], [20, 40]]
worst_p5 = [[0, 2], [20, 38]]
gradient_best_p5 = gradient(best_p5[0], best_p5[1])
gradient_worst_p5 = gradient(worst_p5[0], worst_p5[1])
percent_p5 = abs(gradient_best_p5 - gradient_worst_p5) / gradient_best_p5 * 100
answer_p5 = record("experiment-graph-p5", percent_p5, "%")

# ---------------------------------------------------------------
# p6: density from the gradient of mass against volume, in kg m^-3
# ---------------------------------------------------------------
# m = 80 + 0.80 V (g, cm³): the intercept is the empty cylinder's mass.
# Best-fit line from (0, 80) to (100, 160).


def mass_p6(volume):
    return 80 + 0.80 * volume


data_p6 = scattered_data(
    [10, 20, 30, 40, 50, 60, 70, 80, 90],
    mass_p6,
    [1.5, -1.2, 0.9, -1.6, 1.1, -0.8, 1.4, -1.0, 0.7])
fit_p6 = [[0, tidy(mass_p6(0))], [100, tidy(mass_p6(100))]]
gradient_p6 = gradient(fit_p6[0], fit_p6[1])     # g cm^-3
density_p6 = gradient_p6 * 1000                  # kg m^-3
answer_p6 = record("experiment-graph-p6", density_p6, "kg m⁻³")

# ---------------------------------------------------------------
# Print the answers
# ---------------------------------------------------------------
for question_id, rounded, unit, raw in results:
    print(f"{question_id:22s} {rounded!r:>10} {unit:10s} (raw {raw:.6g})")
print(f"(w gradient {gradient_w} Ω m⁻¹; p2 gradient {gradient_p2}; p4 gradient {gradient_p4}; "
      f"p5 gradients {gradient_best_p5} and {gradient_worst_p5}; p6 gradient {gradient_p6} g cm⁻³)")

# ---------------------------------------------------------------
# The type object
# ---------------------------------------------------------------
BOARDS = ["AQA", "OCR A", "OCR B", "Edexcel", "WJEC"]

type_object = {
    "id": "experiment-graph",
    "name": "Reading experimental graphs",
    "equations": [
        "gradient = (y₂ − y₁) / (x₂ − x₁), using two points far apart on the line",
        "y = mx + c: match the physics equation to find what the gradient and intercept mean",
        "percentage uncertainty in gradient = |best − worst| / best × 100%"
    ],
    "boards": BOARDS,
    "method": "Pick two points on the drawn line (not data points) at gridline intersections as far apart as possible, and find the gradient with its unit, converting any scaled axis units first. Then compare the plotted equation with y = mx + c to turn the gradient or intercept into the quantity asked for. For an uncertainty, find the gradient of the worst-fit line the same way and quote the percentage difference from the best-fit gradient.",
    "commonErrors": [
        "Taking the gradient between two data points instead of two points on the best-fit line",
        "Reading the gradient triangle too small, so the gradient is poorly determined",
        "Forgetting that an axis in cm, mm or 10⁻²³ m⁻² must be converted before the gradient is used in an equation",
        "Reporting the gradient when the question asks for the quantity it represents (e.g. g = 4π² / gradient)"
    ],
    "worked": {
        "id": "experiment-graph-w",
        "question": "A student measures the resistance R of a wire of cross-sectional area 4.0 × 10⁻⁷ m² for different lengths L. The best-fit line through the results is shown; points P and Q lie on the line. Use the gradient of the line to determine the resistivity of the wire.",
        "steps": [
            "Known: A = 4.0 × 10⁻⁷ m². R = ρL / A, so the gradient of R against L is ρ / A.",
            "P is at (0, 0.5 Ω) and Q is at (1.0 m, 4.5 Ω).",
            "Gradient = (4.5 − 0.5) / (1.0 − 0) = 4.0 Ω m⁻¹",
            "ρ = gradient × A = 4.0 × 4.0 × 10⁻⁷",
            "ρ = 1.6 × 10⁻⁶ Ω m"
        ],
        "answer": {"value": answer_w, "unit": "Ω m"},
        "graph": {
            "x": {"label": "L / m", "min": 0, "max": 1.0, "step": 0.1},
            "y": {"label": "R / Ω", "min": 0, "max": 5, "step": 0.5},
            "series": [
                {"kind": "line", "points": line_w}
            ],
            "marks": [
                {"x": 0, "y": 0.5, "label": "P", "dx": 10, "dy": 4},
                {"x": 1.0, "y": 4.5, "label": "Q", "dx": -18, "dy": -8}
            ],
            "alt": "Straight line of resistance against length from point P at (0, 0.5 Ω) to point Q at (1.0 m, 4.5 Ω)"
        }
    },
    "practice": [
        {
            "id": "experiment-graph-p1",
            "question": "A beaker of water is heated by an immersion heater and its temperature θ is recorded every minute. The graph shows the results with a best-fit line drawn. Determine the gradient of the best-fit line.",
            "hint": "Use two points on the line far apart, such as where it meets the left and right edges of the grid: (0, 20 °C) and (10 min, 70 °C).",
            "walkthrough": [
                "Choose two points on the best-fit line, not data points: (0, 20 °C) and (10 min, 70 °C).",
                "Gradient = (70 − 20) / (10 − 0) = 50 / 10",
                "Gradient = 5.0 °C min⁻¹"
            ],
            "answer": {"value": answer_p1, "unit": "°C min⁻¹"},
            "graph": {
                "x": {"label": "t / min", "min": 0, "max": 10, "step": 1},
                "y": {"label": "θ / °C", "min": 20, "max": 80, "step": 10},
                "series": [
                    {"kind": "data", "points": data_p1, "fit": fit_p1}
                ],
                "alt": "Temperature against time for nine readings scattered about a best-fit line rising from 20 °C at t = 0 to 70 °C at 10 minutes"
            }
        },
        {
            "id": "experiment-graph-p2",
            "question": "A student times a simple pendulum for several lengths L and plots T² against L, where T is the period. The best-fit line is drawn through the origin. Use T = 2π√(L / g) and the gradient of the line to determine a value for g.",
            "hint": "Squaring the equation gives T² = (4π² / g) L, so g = 4π² / gradient; read the gradient from (0, 0) and (1.0 m, 4.0 s²).",
            "walkthrough": [
                "T² = (4π² / g) L, so the gradient of T² against L is 4π² / g.",
                "Points on the line: (0, 0) and (1.0 m, 4.0 s²).",
                "Gradient = (4.0 − 0) / (1.0 − 0) = 4.0 s² m⁻¹",
                "g = 4π² / gradient = 39.5 / 4.0",
                "g = 9.87 m s⁻²"
            ],
            "answer": {"value": answer_p2, "unit": "m s⁻²"},
            "graph": {
                "x": {"label": "L / m", "min": 0, "max": 1.0, "step": 0.1},
                "y": {"label": "T² / s²", "min": 0, "max": 4, "step": 0.5},
                "series": [
                    {"kind": "data", "points": data_p2, "fit": fit_p2}
                ],
                "alt": "Period squared against length for eight pendulum readings scattered about a best-fit line through the origin reaching 4.0 s² at 1.0 m"
            }
        },
        {
            "id": "experiment-graph-p3",
            "question": "A student loads a spring and records its extension x with a ruler, plotting x against the load F. The best-fit line is shown. The line should pass through the origin, but the student made the same zero error in every ruler reading. Use the intercept of the graph to determine the zero error, in mm.",
            "hint": "Read where the line crosses the x axis of the graph at F = 0; that is the extension recorded when there should have been none, in cm.",
            "walkthrough": [
                "With no load the true extension is zero, so the intercept on the extension axis is the zero error.",
                "Intercept: at F = 0 the line reads x = 0.5 cm.",
                "Zero error = 0.5 cm = 5.0 mm"
            ],
            "answer": {"value": answer_p3, "unit": "mm"},
            "graph": {
                "x": {"label": "F / N", "min": 0, "max": 8, "step": 1},
                "y": {"label": "x / cm", "min": 0, "max": 5, "step": 0.5},
                "series": [
                    {"kind": "line", "points": line_p3}
                ],
                "marks": [{"x": 0, "y": 0.5, "label": "intercept", "dx": 10, "dy": 4}],
                "alt": "Straight line of recorded extension against load starting at an intercept of 0.5 cm when F = 0 and rising to 4.5 cm at 8 N"
            }
        },
        {
            "id": "experiment-graph-p4",
            "question": "A mass m hanging from a spring is set oscillating and its period T is measured for several masses. The graph shows T² against m with a straight line drawn through the origin; point P lies on the line. Use T = 2π√(m / k) and the gradient of the line to determine the spring constant k.",
            "hint": "T² = (4π² / k) m, so gradient = 4π² / k; find the gradient from the origin and P, then rearrange for k.",
            "walkthrough": [
                "T² = (4π² / k) m, so the gradient of T² against m is 4π² / k.",
                "P is at (0.50 kg, 1.0 s²) and the line passes through (0, 0).",
                "Gradient = (1.0 − 0) / (0.50 − 0) = 2.0 s² kg⁻¹",
                "k = 4π² / gradient = 39.5 / 2.0",
                "k = 19.7 N m⁻¹"
            ],
            "answer": {"value": answer_p4, "unit": "N m⁻¹"},
            "graph": {
                "x": {"label": "m / kg", "min": 0, "max": 0.6, "step": 0.1},
                "y": {"label": "T² / s²", "min": 0, "max": 1.2, "step": 0.2},
                "series": [
                    {"kind": "line", "points": line_p4}
                ],
                "marks": [{"x": 0.5, "y": 1.0, "label": "P"}],
                "alt": "Straight line of period squared against mass through the origin and point P at (0.50 kg, 1.0 s²), reaching 1.2 s² at 0.6 kg"
            }
        },
        {
            "id": "experiment-graph-p5",
            "question": "A student plots the extension x of a spring against the load F. The solid line is the best-fit line, which passes through the origin, and the dashed line is the worst-fit line; points A and B lie on the worst-fit line. Determine the percentage uncertainty in the gradient of the best-fit line.",
            "hint": "Find both gradients from points far apart on each line, then percentage uncertainty = |best − worst| / best × 100%.",
            "walkthrough": [
                "Best-fit line through (0, 0) and (20 N, 40 mm): gradient = 40 / 20 = 2.0 mm N⁻¹",
                "Worst-fit line through A (0, 2 mm) and B (20 N, 38 mm): gradient = (38 − 2) / (20 − 0) = 1.8 mm N⁻¹",
                "Difference = 2.0 − 1.8 = 0.2 mm N⁻¹",
                "Percentage uncertainty = 0.2 / 2.0 × 100% = 10%"
            ],
            "answer": {"value": answer_p5, "unit": "%"},
            "graph": {
                "x": {"label": "F / N", "min": 0, "max": 20, "step": 2},
                "y": {"label": "x / mm", "min": 0, "max": 40, "step": 2},
                "series": [
                    {"kind": "line", "points": best_p5},
                    {"kind": "dashed", "points": worst_p5}
                ],
                "marks": [
                    {"x": 0, "y": 2, "label": "A", "dx": 10, "dy": 4},
                    {"x": 20, "y": 38, "label": "B", "dx": 6, "dy": 16}
                ],
                "alt": "Extension against load with a solid best-fit line from the origin to (20 N, 40 mm) and a dashed worst-fit line from point A at (0, 2 mm) to point B at (20 N, 38 mm)"
            }
        },
        {
            "id": "experiment-graph-p6",
            "question": "A student pours ethanol into a measuring cylinder on a balance and records the total mass m for several volumes V. The graph shows m against V with a best-fit line drawn. Use the gradient of the line to determine the density of the ethanol in kg m⁻³.",
            "hint": "The gradient is the density in g cm⁻³ (the intercept is the mass of the empty cylinder); read it from (0, 80 g) and (100 cm³, 160 g), then convert using 1 g cm⁻³ = 1000 kg m⁻³.",
            "walkthrough": [
                "m = (mass of cylinder) + ρV, so the gradient of m against V is ρ.",
                "Points on the line: (0, 80 g) and (100 cm³, 160 g).",
                "Gradient = (160 − 80) / (100 − 0) = 0.80 g cm⁻³",
                "ρ = 0.80 g cm⁻³ = 0.80 × 1000 kg m⁻³",
                "ρ = 800 kg m⁻³"
            ],
            "answer": {"value": answer_p6, "unit": "kg m⁻³"},
            "graph": {
                "x": {"label": "V / cm³", "min": 0, "max": 100, "step": 10},
                "y": {"label": "m / g", "min": 60, "max": 160, "step": 10},
                "series": [
                    {"kind": "data", "points": data_p6, "fit": fit_p6}
                ],
                "alt": "Total mass against volume for nine readings scattered about a best-fit line from 80 g at zero volume to 160 g at 100 cm³"
            }
        }
    ]
}

if len(sys.argv) > 1:
    with open(sys.argv[1], "w", encoding="utf-8") as handle:
        json.dump(type_object, handle, ensure_ascii=False, indent=2)
    print(f"wrote {sys.argv[1]}")
