#!/usr/bin/env python3
"""Compute every answer and every plotted coordinate for the graph type
"force-graph" (Reading graphs of forces and motion) in data/forces.json.

Each answer is printed rounded to 3 s.f. with its question id, followed by
the graph spec (as JSON) for every question so the coordinates pasted into
the topic file are exactly the ones the answers were computed from.

Run: python3 tools/calc_forces_graph.py
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


def tidy(value):
    """Round a sampled coordinate to 4 d.p. so the JSON stays readable."""
    return round(value, 4)


# ---------------------------------------------------------------
# w: lander on the Moon, W–m straight line; g = gradient.
# ---------------------------------------------------------------

w_points = [[0, 0], [10, 16]]
w_g = gradient(w_points[0], w_points[1])
record("force-graph-w", w_g, "N kg⁻¹")
GRAPHS["force-graph-w"] = {
    "x": {"label": "m / kg", "min": 0, "max": 10, "step": 1},
    "y": {"label": "W / N", "min": 0, "max": 16, "step": 2},
    "series": [{"kind": "line", "points": w_points}],
    "marks": [{"x": 10, "y": 16, "label": "X", "drop": True, "dx": -16, "dy": -8}],
    "alt": "Weight–mass graph: a straight line from the origin to X (10 kg, 16 N)",
}

# ---------------------------------------------------------------
# p1: model rocket motor thrust–time curve F = A t e^(−2t), with A
#     chosen so that F = 8.0 N exactly at t = 1.0 s (the marked point X).
# ---------------------------------------------------------------

p1_amplitude = 8.0 * math.exp(2.0)        # so that A × 1 × e^(−2) = 8.0


def p1_thrust(t):
    """Thrust in newtons at time t in seconds."""
    return p1_amplitude * t * math.exp(-2.0 * t)


p1_sample_times = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.25, 2.5, 2.75, 3.0]
p1_curve = []
for t in p1_sample_times:
    p1_curve.append([tidy(t), tidy(p1_thrust(t))])
p1_thrust_at_x = p1_thrust(1.0)
assert abs(p1_thrust_at_x - 8.0) < 1e-9
record("force-graph-p1", p1_thrust_at_x, "N")
GRAPHS["force-graph-p1"] = {
    "x": {"label": "t / s", "min": 0, "max": 3, "step": 0.5},
    "y": {"label": "F / N", "min": 0, "max": 12, "step": 2},
    "series": [{"kind": "curve", "points": p1_curve}],
    "marks": [{"x": 1.0, "y": 8.0, "label": "X", "drop": True}],
    "alt": "Thrust–time graph rising steeply from the origin to a peak near 11 N at 0.5 s then decaying towards zero by 3 s; X is marked at (1.0 s, 8.0 N)",
}

# ---------------------------------------------------------------
# p2: steel ball bearing falling through glycerol, v–t curve
#     v = v_t (1 − e^(−t/τ)); terminal velocity read from the plateau.
# ---------------------------------------------------------------

p2_terminal = 0.25
p2_tau = 0.3


def p2_velocity(t):
    """Velocity of the ball bearing at time t."""
    return p2_terminal * (1 - math.exp(-t / p2_tau))


p2_sample_times = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
p2_curve = []
for t in p2_sample_times:
    p2_curve.append([tidy(t), tidy(p2_velocity(t))])
# The curve is within 0.2 % of the plateau by the right-hand edge
assert p2_curve[-1][1] >= 0.998 * p2_terminal
record("force-graph-p2", p2_terminal, "m s⁻¹")
GRAPHS["force-graph-p2"] = {
    "x": {"label": "t / s", "min": 0, "max": 2.0, "step": 0.2},
    "y": {"label": "v / m s⁻¹", "min": 0, "max": 0.3, "step": 0.05},
    "series": [
        {"kind": "curve", "points": p2_curve},
        {"kind": "dashed", "points": [[0, p2_terminal], [2.0, p2_terminal]]},
    ],
    "alt": "Velocity–time graph for a ball bearing in glycerol rising from the origin and flattening onto a dashed line at 0.25 m/s by about 1.5 s",
}

# ---------------------------------------------------------------
# p3: wooden block on a bench, friction F against normal reaction R;
#     coefficient of friction μ = gradient.
# ---------------------------------------------------------------

p3_points = [[0, 0], [50, 20]]
p3_mu = gradient(p3_points[0], p3_points[1])
record("force-graph-p3", p3_mu, "")
GRAPHS["force-graph-p3"] = {
    "x": {"label": "R / N", "min": 0, "max": 50, "step": 10},
    "y": {"label": "F / N", "min": 0, "max": 25, "step": 5},
    "series": [{"kind": "line", "points": p3_points}],
    "marks": [{"x": 50, "y": 20, "label": "X", "drop": True, "dx": -16, "dy": -8}],
    "alt": "Friction force against normal reaction: a straight line from the origin to X (50 N, 20 N)",
}

# ---------------------------------------------------------------
# p4: skydiver v–t curve v = v_t (1 − e^(−t/τ)); initial acceleration
#     = gradient of the tangent at t = 0, which is v_t / τ.
# ---------------------------------------------------------------

p4_terminal = 50.0
p4_tau = 5.0


def p4_velocity(t):
    """Velocity of the skydiver at time t."""
    return p4_terminal * (1 - math.exp(-t / p4_tau))


p4_sample_times = [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
p4_curve = []
for t in p4_sample_times:
    p4_curve.append([tidy(t), tidy(p4_velocity(t))])
p4_true_initial_gradient = p4_terminal / p4_tau
# Tangent at the origin: v = (v_t / τ) t; end points on gridlines
p4_tangent = [[0, 0], [5, 50]]
p4_tangent_gradient = gradient(p4_tangent[0], p4_tangent[1])
assert abs(p4_tangent_gradient - p4_true_initial_gradient) < 1e-9
record("force-graph-p4", p4_tangent_gradient, "m s⁻²")
GRAPHS["force-graph-p4"] = {
    "x": {"label": "t / s", "min": 0, "max": 10, "step": 1},
    "y": {"label": "v / m s⁻¹", "min": 0, "max": 50, "step": 5},
    "series": [
        {"kind": "curve", "points": p4_curve},
        {"kind": "tangent", "points": p4_tangent},
    ],
    "marks": [
        {"x": 0, "y": 0},
        {"x": 5, "y": 50, "label": "T", "drop": True, "dx": 8, "dy": 14},
    ],
    "labels": [{"x": 5.3, "y": 44, "text": "tangent at t = 0"}],
    "alt": "Velocity–time graph for a skydiver curving from the origin towards 50 m/s with decreasing gradient, reaching about 43 m/s at 10 s; the tangent at the origin is drawn through T (5 s, 50 m/s)",
}

# ---------------------------------------------------------------
# p5: loaded laboratory trolley, a–F straight line through the origin;
#     gradient = 1/m, so m = 1 / gradient.
# ---------------------------------------------------------------

p5_points = [[0, 0], [8, 2.0]]
p5_gradient = gradient(p5_points[0], p5_points[1])
p5_mass = 1 / p5_gradient
record("force-graph-p5", p5_mass, "kg")
GRAPHS["force-graph-p5"] = {
    "x": {"label": "F / N", "min": 0, "max": 8, "step": 1},
    "y": {"label": "a / m s⁻²", "min": 0, "max": 2.5, "step": 0.5},
    "series": [{"kind": "line", "points": p5_points}],
    "marks": [{"x": 8, "y": 2.0, "label": "X", "drop": True, "dx": -16, "dy": -8}],
    "alt": "Acceleration against applied force: a straight line from the origin to X (8 N, 2.0 m/s²)",
}

# ---------------------------------------------------------------
# p6: trolley with friction, a–F straight line that cuts the F axis at
#     P (2 N, 0); gradient from P to X = 1/m.
# ---------------------------------------------------------------

p6_points = [[2, 0], [10, 4.0]]
p6_gradient = gradient(p6_points[0], p6_points[1])
p6_mass = 1 / p6_gradient
record("force-graph-p6", p6_mass, "kg")
GRAPHS["force-graph-p6"] = {
    "x": {"label": "F / N", "min": 0, "max": 10, "step": 1},
    "y": {"label": "a / m s⁻²", "min": 0, "max": 4, "step": 0.5},
    "series": [{"kind": "line", "points": p6_points}],
    "marks": [
        {"x": 2, "y": 0, "label": "P", "dx": -14, "dy": -6},
        {"x": 10, "y": 4.0, "label": "X", "drop": True, "dx": -16, "dy": -8},
    ],
    "alt": "Acceleration against applied force: a straight line from P (2 N, 0) to X (10 N, 4.0 m/s²), cutting the force axis at 2 N",
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
