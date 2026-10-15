#!/usr/bin/env python3
"""Compute every answer and every plotted coordinate for the graph type
"ft-fs-graph" (Reading force–time and force–displacement graphs) in
data/momentum-energy.json.

Each answer is printed rounded to 3 s.f. with its question id, followed by
the graph spec (as JSON) for every question so the coordinates pasted into
the topic file are exactly the ones the answers were computed from.

Run: python3 tools/calc_momentum-energy_graph.py
"""

import json
import math

results = []

# Graph specs keyed by question id; the topic file copies these verbatim
GRAPHS = {}


def record(question_id, value, unit):
    """Store one answer, rounded to 3 significant figures."""
    if value == 0:
        rounded = 0.0
    else:
        # Number of decimal places that gives 3 s.f.
        magnitude = math.floor(math.log10(abs(value)))
        places = 2 - magnitude
        rounded = round(value, places)
    results.append((question_id, rounded, unit, value))


def gradient(point_a, point_b):
    """Gradient of the straight line through two points."""
    return (point_b[1] - point_a[1]) / (point_b[0] - point_a[0])


def triangle_area(base, height):
    """Area of a triangle."""
    return 0.5 * base * height


def trapezium_area(side_a, side_b, width):
    """Area of a trapezium with parallel sides a and b."""
    return 0.5 * (side_a + side_b) * width


# ---------------------------------------------------------------
# w: tennis racket on ball, F–t triangle; time axis in ms.
#    Impulse = area = ½ × base × height.
# ---------------------------------------------------------------

w_points = [[0, 0], [4, 600], [10, 0]]
w_base_s = 10 * 1e-3                      # 10 ms in seconds
w_impulse = triangle_area(w_base_s, 600)
record("ft-fs-graph-w", w_impulse, "N s")
GRAPHS["ft-fs-graph-w"] = {
    "x": {"label": "t / ms", "min": 0, "max": 10, "step": 1},
    "y": {"label": "F / N", "min": 0, "max": 600, "step": 100},
    "series": [{"kind": "line", "points": w_points}],
    "marks": [{"x": 4, "y": 600, "label": "P", "drop": True}],
    "shade": [{"series": 0, "from": 0, "to": 10}],
    "alt": "Force–time graph: a triangle rising from the origin to 600 N at 4 ms and falling back to zero at 10 ms; the whole triangle is shaded",
}

# ---------------------------------------------------------------
# p1: satellite thruster, F–t rectangle + triangle.
#     Impulse = rectangle area + triangle area.
# ---------------------------------------------------------------

p1_points = [[0, 200], [6, 200], [10, 0]]
p1_rectangle = 6 * 200
p1_triangle = triangle_area(10 - 6, 200)
p1_impulse = p1_rectangle + p1_triangle
record("ft-fs-graph-p1", p1_impulse, "N s")
GRAPHS["ft-fs-graph-p1"] = {
    "x": {"label": "t / s", "min": 0, "max": 10, "step": 1},
    "y": {"label": "F / N", "min": 0, "max": 250, "step": 50},
    "series": [{"kind": "line", "points": p1_points}],
    "marks": [
        {"x": 6, "y": 200, "label": "A", "drop": True},
        {"x": 10, "y": 0, "label": "B", "dx": 6, "dy": -6},
    ],
    "shade": [{"series": 0, "from": 0, "to": 10}],
    "alt": "Force–time graph level at 200 N from 0 to 6 s then falling in a straight line to zero at 10 s; the area under the whole graph is shaded",
}

# ---------------------------------------------------------------
# p2: sledge pulled across snow, F–s trapezium.
#     Work done = area under the F–s graph.
# ---------------------------------------------------------------

p2_points = [[0, 100], [16, 40]]
p2_work = trapezium_area(100, 40, 16)
record("ft-fs-graph-p2", p2_work, "J")
GRAPHS["ft-fs-graph-p2"] = {
    "x": {"label": "s / m", "min": 0, "max": 16, "step": 2},
    "y": {"label": "F / N", "min": 0, "max": 120, "step": 20},
    "series": [{"kind": "line", "points": p2_points}],
    "marks": [
        {"x": 0, "y": 100, "label": "A", "dx": 8, "dy": -8},
        {"x": 16, "y": 40, "label": "B", "drop": True, "dx": -14, "dy": -10},
    ],
    "shade": [{"series": 0, "from": 0, "to": 16}],
    "alt": "Force–displacement graph: a straight line falling from 100 N at 0 m to 40 N at 16 m; the trapezium under the line is shaded",
}

# ---------------------------------------------------------------
# p3: golf club on ball, F–t triangle with F in kN and t in ms.
#     Average force = impulse / contact time.
# ---------------------------------------------------------------

p3_points = [[0, 0], [0.2, 1.8], [0.6, 0]]
p3_contact_s = 0.6 * 1e-3                 # 0.6 ms in seconds
p3_peak_n = 1.8 * 1e3                     # 1.8 kN in newtons
p3_impulse = triangle_area(p3_contact_s, p3_peak_n)
p3_average_force = p3_impulse / p3_contact_s
record("ft-fs-graph-p3", p3_average_force, "N")
GRAPHS["ft-fs-graph-p3"] = {
    "x": {"label": "t / ms", "min": 0, "max": 0.6, "step": 0.1},
    "y": {"label": "F / kN", "min": 0, "max": 2.0, "step": 0.2},
    "series": [{"kind": "line", "points": p3_points}],
    "marks": [{"x": 0.2, "y": 1.8, "label": "P", "drop": True}],
    "shade": [{"series": 0, "from": 0, "to": 0.6}],
    "alt": "Force–time graph: a triangle rising from the origin to 1.8 kN at 0.2 ms and falling to zero at 0.6 ms; the triangle is shaded",
}

# ---------------------------------------------------------------
# p4: crane motor, work done against time (W in kJ).
#     Power = gradient of the W–t graph.
# ---------------------------------------------------------------

p4_points = [[0, 0], [20, 30]]
p4_work_j = 30 * 1e3                      # 30 kJ in joules
p4_power = p4_work_j / 20
record("ft-fs-graph-p4", p4_power, "W")
GRAPHS["ft-fs-graph-p4"] = {
    "x": {"label": "t / s", "min": 0, "max": 20, "step": 2},
    "y": {"label": "W / kJ", "min": 0, "max": 30, "step": 5},
    "series": [{"kind": "line", "points": p4_points}],
    "marks": [{"x": 20, "y": 30, "label": "X", "drop": True, "dx": -16, "dy": -8}],
    "alt": "Work done–time graph: a straight line from the origin to 30 kJ at 20 s, with X marked at the end",
}

# ---------------------------------------------------------------
# p5: hockey ball push, F–t trapezium (t in ms); then Δv = impulse / m.
# ---------------------------------------------------------------

p5_points = [[0, 0], [2, 300], [6, 300], [8, 0]]
p5_top_s = (6 - 2) * 1e-3                 # top side of trapezium in s
p5_bottom_s = 8 * 1e-3                    # bottom side in s
p5_impulse = trapezium_area(p5_top_s, p5_bottom_s, 300)
p5_mass = 0.18
p5_delta_v = p5_impulse / p5_mass
record("ft-fs-graph-p5", p5_delta_v, "m s⁻¹")
GRAPHS["ft-fs-graph-p5"] = {
    "x": {"label": "t / ms", "min": 0, "max": 8, "step": 1},
    "y": {"label": "F / N", "min": 0, "max": 300, "step": 50},
    "series": [{"kind": "line", "points": p5_points}],
    "marks": [
        {"x": 2, "y": 300, "label": "A", "drop": True, "dx": -14, "dy": -8},
        {"x": 6, "y": 300, "label": "B", "drop": True},
    ],
    "shade": [{"series": 0, "from": 0, "to": 8}],
    "alt": "Force–time graph: a trapezium rising from the origin to 300 N at 2 ms, level to 6 ms, then falling to zero at 8 ms; the whole area is shaded",
}

# ---------------------------------------------------------------
# p6: model car from rest, resultant F–s trapezium; W = area, then
#     ½mv² = W gives the speed.
# ---------------------------------------------------------------

p6_points = [[0, 50], [8, 30]]
p6_work = trapezium_area(50, 30, 8)
p6_mass = 2.5
p6_speed = math.sqrt(2 * p6_work / p6_mass)
record("ft-fs-graph-p6", p6_speed, "m s⁻¹")
GRAPHS["ft-fs-graph-p6"] = {
    "x": {"label": "s / m", "min": 0, "max": 8, "step": 1},
    "y": {"label": "F / N", "min": 0, "max": 60, "step": 10},
    "series": [{"kind": "line", "points": p6_points}],
    "marks": [
        {"x": 0, "y": 50, "label": "A", "dx": 8, "dy": -8},
        {"x": 8, "y": 30, "label": "B", "drop": True, "dx": -14, "dy": -10},
    ],
    "shade": [{"series": 0, "from": 0, "to": 8}],
    "alt": "Resultant force–displacement graph: a straight line falling from 50 N at 0 m to 30 N at 8 m; the trapezium under the line is shaded",
}


# ---------------------------------------------------------------
# Print
# ---------------------------------------------------------------

if __name__ == "__main__":
    for question_id, rounded, unit, raw in results:
        print(f"{question_id:32s} {rounded!r:>14}  {unit:14s} (raw {raw!r})")
    print()
    for question_id, graph in GRAPHS.items():
        print(question_id)
        print(json.dumps(graph, ensure_ascii=False))
