#!/usr/bin/env python3
"""Compute every answer and every plotted coordinate for the graph type
"motion-graph" (Reading motion graphs) in data/kinematics.json.

Each answer is printed rounded to 3 s.f. with its question id, followed by
the graph spec (as JSON) for every question so the coordinates pasted into
the topic file are exactly the ones the answers were computed from.

Run: python3 tools/calc_kinematics_graph.py
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


def tidy(value):
    """Round a sampled coordinate to 4 d.p. so the JSON stays readable."""
    return round(value, 4)


# ---------------------------------------------------------------
# w: underground train v–t graph, three straight sections.
#    Acceleration during the first 6.0 s = gradient of OB.
# ---------------------------------------------------------------

w_points = [[0, 5], [6, 20], [12, 20], [16, 0]]
w_accel = gradient(w_points[0], w_points[1])
record("motion-graph-w", w_accel, "m s⁻²")
GRAPHS["motion-graph-w"] = {
    "x": {"label": "t / s", "min": 0, "max": 16, "step": 2},
    "y": {"label": "v / m s⁻¹", "min": 0, "max": 25, "step": 5},
    "series": [{"kind": "line", "points": w_points}],
    "marks": [
        {"x": 0, "y": 5, "label": "A", "dx": 6, "dy": 16},
        {"x": 6, "y": 20, "label": "B", "drop": True},
    ],
    "alt": "Velocity–time graph rising in a straight line from 5 m/s at 0 s to 20 m/s at 6 s, level at 20 m/s until 12 s, then falling in a straight line to zero at 16 s",
}

# ---------------------------------------------------------------
# p1: cyclist v–t graph; displacement in the first 8.0 s = triangle area.
# ---------------------------------------------------------------

p1_points = [[0, 0], [8, 12], [12, 12]]
p1_displacement = triangle_area(8, 12)
record("motion-graph-p1", p1_displacement, "m")
GRAPHS["motion-graph-p1"] = {
    "x": {"label": "t / s", "min": 0, "max": 12, "step": 2},
    "y": {"label": "v / m s⁻¹", "min": 0, "max": 16, "step": 2},
    "series": [{"kind": "line", "points": p1_points}],
    "marks": [{"x": 8, "y": 12, "label": "X", "drop": True}],
    "shade": [{"series": 0, "from": 0, "to": 8}],
    "alt": "Velocity–time graph rising in a straight line from the origin to 12 m/s at 8 s, then level at 12 m/s to 12 s; the triangle under the rising section is shaded",
}

# ---------------------------------------------------------------
# p2: lorry v–t graph; deceleration = magnitude of gradient of AB.
# ---------------------------------------------------------------

p2_points = [[0, 20], [10, 20], [35, 0]]
p2_decel = abs(gradient(p2_points[1], p2_points[2]))
record("motion-graph-p2", p2_decel, "m s⁻²")
GRAPHS["motion-graph-p2"] = {
    "x": {"label": "t / s", "min": 0, "max": 40, "step": 5},
    "y": {"label": "v / m s⁻¹", "min": 0, "max": 25, "step": 5},
    "series": [{"kind": "line", "points": p2_points}],
    "marks": [
        {"x": 10, "y": 20, "label": "A", "drop": True},
        {"x": 35, "y": 0, "label": "B", "dx": 6, "dy": -8},
    ],
    "alt": "Velocity–time graph level at 20 m/s from 0 to 10 s, then falling in a straight line to zero at 35 s",
}

# ---------------------------------------------------------------
# p3: train s–t graph in km and minutes; velocity in first 4.0 min.
# ---------------------------------------------------------------

p3_points = [[0, 0], [4, 6], [8, 6], [12, 15]]
p3_delta_s_m = 6 * 1000          # 6 km in metres
p3_delta_t_s = 4 * 60            # 4 min in seconds
p3_velocity = p3_delta_s_m / p3_delta_t_s
record("motion-graph-p3", p3_velocity, "m s⁻¹")
GRAPHS["motion-graph-p3"] = {
    "x": {"label": "t / min", "min": 0, "max": 12, "step": 2},
    "y": {"label": "s / km", "min": 0, "max": 15, "step": 3},
    "series": [{"kind": "line", "points": p3_points}],
    "marks": [{"x": 4, "y": 6, "label": "A", "drop": True}],
    "alt": "Displacement–time graph rising in a straight line from the origin to 6 km at 4 min, level until 8 min, then rising to 15 km at 12 min",
}

# ---------------------------------------------------------------
# p4: motorboat v–t graph; displacement between A (4 s) and B (10 s)
#     = trapezium area.
# ---------------------------------------------------------------

p4_points = [[0, 4], [10, 14]]
p4_v_at_4 = 4 + gradient(p4_points[0], p4_points[1]) * 4   # should be 8
p4_displacement = trapezium_area(p4_v_at_4, 14, 10 - 4)
record("motion-graph-p4", p4_displacement, "m")
GRAPHS["motion-graph-p4"] = {
    "x": {"label": "t / s", "min": 0, "max": 10, "step": 1},
    "y": {"label": "v / m s⁻¹", "min": 0, "max": 16, "step": 2},
    "series": [{"kind": "line", "points": p4_points}],
    "marks": [
        {"x": 4, "y": p4_v_at_4, "label": "A", "drop": True},
        {"x": 10, "y": 14, "label": "B", "drop": True, "dx": -14, "dy": -10},
    ],
    "shade": [{"series": 0, "from": 4, "to": 10}],
    "alt": "Velocity–time graph, a straight line from 4 m/s at 0 s to 14 m/s at 10 s; the trapezium under the line between 4 s and 10 s is shaded",
}

# ---------------------------------------------------------------
# p5: model rocket, curved v–t graph v = 0.5 t²; tangent at X (t = 4 s).
#     Instantaneous acceleration = gradient of the tangent.
# ---------------------------------------------------------------


def p5_velocity(t):
    """Velocity of the rocket at time t (non-uniform acceleration)."""
    return 0.5 * t * t


p5_curve = []
for index in range(0, 17):
    t = index * 0.5
    p5_curve.append([tidy(t), tidy(p5_velocity(t))])

p5_tx = 4.0
p5_tv = p5_velocity(p5_tx)                    # 8.0
p5_true_gradient = 1.0 * p5_tx                # dv/dt = t
# Tangent line v = 8 + 4 (t − 4) = 4t − 8; end points on gridlines:
p5_tangent = [[2, 0], [8, 24]]
p5_tangent_gradient = gradient(p5_tangent[0], p5_tangent[1])
assert abs(p5_tangent_gradient - p5_true_gradient) < 1e-9
assert abs((p5_tangent[0][1] + p5_tangent_gradient * (p5_tx - p5_tangent[0][0])) - p5_tv) < 1e-9
record("motion-graph-p5", p5_tangent_gradient, "m s⁻²")
GRAPHS["motion-graph-p5"] = {
    "x": {"label": "t / s", "min": 0, "max": 8, "step": 1},
    "y": {"label": "v / m s⁻¹", "min": 0, "max": 32, "step": 4},
    "series": [
        {"kind": "curve", "points": p5_curve},
        {"kind": "tangent", "points": p5_tangent},
    ],
    "marks": [{"x": p5_tx, "y": p5_tv, "label": "X", "drop": True, "dx": -16, "dy": -8}],
    "labels": [{"x": 5.6, "y": 10, "text": "tangent at X"}],
    "alt": "Velocity–time graph curving upwards with increasing gradient from the origin to 32 m/s at 8 s; a tangent at X (4 s, 8 m/s) passes through (2 s, 0) and (8 s, 24 m/s)",
}

# ---------------------------------------------------------------
# p6: tram braking, curved s–t graph s = 20t − t²; tangent at X (t = 4 s).
#     Instantaneous velocity = gradient of the tangent.
# ---------------------------------------------------------------


def p6_displacement(t):
    """Displacement of the tram at time t while braking uniformly."""
    return 20 * t - t * t


p6_curve = []
for index in range(0, 11):
    t = index * 1.0
    p6_curve.append([tidy(t), tidy(p6_displacement(t))])

p6_tx = 4.0
p6_ts = p6_displacement(p6_tx)                 # 64
p6_true_gradient = 20 - 2 * p6_tx              # ds/dt = 20 − 2t = 12
# Tangent line s = 64 + 12 (t − 4) = 12t + 16; end points on gridlines:
p6_tangent = [[2, 40], [7, 100]]
p6_tangent_gradient = gradient(p6_tangent[0], p6_tangent[1])
assert abs(p6_tangent_gradient - p6_true_gradient) < 1e-9
assert abs((p6_tangent[0][1] + p6_tangent_gradient * (p6_tx - p6_tangent[0][0])) - p6_ts) < 1e-9
record("motion-graph-p6", p6_tangent_gradient, "m s⁻¹")
GRAPHS["motion-graph-p6"] = {
    "x": {"label": "t / s", "min": 0, "max": 10, "step": 1},
    "y": {"label": "s / m", "min": 0, "max": 100, "step": 10},
    "series": [
        {"kind": "curve", "points": p6_curve},
        {"kind": "tangent", "points": p6_tangent},
    ],
    "marks": [{"x": p6_tx, "y": p6_ts, "label": "X", "dx": 8, "dy": 14}],
    "labels": [{"x": 5.2, "y": 55, "text": "tangent at X"}],
    "alt": "Displacement–time graph curving from the origin to 100 m at 10 s with decreasing gradient; a tangent at X (4 s, 64 m) passes through (2 s, 40 m) and (7 s, 100 m)",
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
