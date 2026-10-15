#!/usr/bin/env python3
"""Compute every answer and every plotted coordinate for the graph type
"fx-stress-strain-graph" (Reading force–extension and stress–strain graphs)
in data/materials.json.

Each answer is printed rounded to 3 s.f. with its question id, followed by
the graph spec (as JSON) for every question so the coordinates pasted into
the topic file are exactly the ones the answers were computed from.

Run: python3 tools/calc_materials_graph.py
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
# w: laboratory spring, F–x straight line (x in mm).
#    Spring constant = gradient with x converted to metres.
# ---------------------------------------------------------------

w_points = [[0, 0], [80, 20]]
w_x_m = 80 * 1e-3
w_k = 20 / w_x_m
record("fx-stress-strain-graph-w", w_k, "N m⁻¹")
GRAPHS["fx-stress-strain-graph-w"] = {
    "x": {"label": "x / mm", "min": 0, "max": 80, "step": 10},
    "y": {"label": "F / N", "min": 0, "max": 20, "step": 5},
    "series": [{"kind": "line", "points": w_points}],
    "marks": [{"x": 80, "y": 20, "label": "X", "drop": True, "dx": -16, "dy": -8}],
    "alt": "Force–extension graph: a straight line from the origin to 20 N at an extension of 80 mm, with X marked at the end",
}

# ---------------------------------------------------------------
# p1: toy catapult spring, F–x straight line; strain energy up to P
#     = triangle area (x in mm).
# ---------------------------------------------------------------

p1_points = [[0, 0], [60, 30]]
p1_x_m = 40 * 1e-3
p1_energy = triangle_area(p1_x_m, 20)
record("fx-stress-strain-graph-p1", p1_energy, "J")
GRAPHS["fx-stress-strain-graph-p1"] = {
    "x": {"label": "x / mm", "min": 0, "max": 60, "step": 10},
    "y": {"label": "F / N", "min": 0, "max": 30, "step": 5},
    "series": [{"kind": "line", "points": p1_points}],
    "marks": [{"x": 40, "y": 20, "label": "P", "drop": True, "dx": -16, "dy": -6}],
    "shade": [{"series": 0, "from": 0, "to": 40}],
    "alt": "Force–extension graph: a straight line from the origin to 30 N at 60 mm; the triangle under the line up to P (40 mm, 20 N) is shaded",
}

# ---------------------------------------------------------------
# p2: ductile alloy stress–strain curve; breaking stress read at B.
#     Linear to (2, 300) MPa, then a parabola peaking at ε = 8 ×10⁻³
#     (480 MPa) and breaking at B = (12, 400) MPa, on a major gridline.
# ---------------------------------------------------------------


def p2_stress(strain_milli):
    """Stress in MPa beyond the linear region (strain in units of 10⁻³)."""
    return 300 + 180 * (1 - ((strain_milli - 8) / 6) ** 2)


p2_line = [[0, 0], [2, 300]]
p2_curve = []
for index in range(0, 11):
    strain_milli = 2 + index * 1.0
    p2_curve.append([tidy(strain_milli), tidy(p2_stress(strain_milli))])
assert p2_curve[0] == [2.0, 300.0]
assert p2_curve[-1] == [12.0, 400.0]
p2_breaking_stress = 400 * 1e6
record("fx-stress-strain-graph-p2", p2_breaking_stress, "Pa")
GRAPHS["fx-stress-strain-graph-p2"] = {
    "x": {"label": "ε / 10⁻³", "min": 0, "max": 12, "step": 1},
    "y": {"label": "σ / MPa", "min": 0, "max": 500, "step": 50},
    "series": [
        {"kind": "line", "points": p2_line},
        {"kind": "curve", "points": p2_curve},
    ],
    "marks": [{"x": 12, "y": 400, "label": "B", "drop": True, "dx": -16, "dy": -8}],
    "alt": "Stress–strain graph rising linearly to 300 MPa at a strain of 0.002, curving over a maximum near 480 MPa, and ending at the breaking point B (0.012, 400 MPa)",
}

# ---------------------------------------------------------------
# p3: brass wire stress–strain; Young modulus = gradient of the linear
#     region OP (stress in MPa, strain in 10⁻³).
# ---------------------------------------------------------------


def p3_stress(strain_milli):
    """Stress in MPa beyond the limit of proportionality."""
    return 250 + 40 * (1 - ((5 - strain_milli) / 2.5) ** 2)


p3_line = [[0, 0], [2.5, 250]]
p3_curve = []
for index in range(0, 11):
    strain_milli = 2.5 + index * 0.25
    p3_curve.append([tidy(strain_milli), tidy(p3_stress(strain_milli))])
assert p3_curve[0] == [2.5, 250.0]
p3_stress_pa = 250 * 1e6
p3_strain = 2.5 * 1e-3
p3_young = p3_stress_pa / p3_strain
record("fx-stress-strain-graph-p3", p3_young, "Pa")
GRAPHS["fx-stress-strain-graph-p3"] = {
    "x": {"label": "ε / 10⁻³", "min": 0, "max": 5, "step": 0.5},
    "y": {"label": "σ / MPa", "min": 0, "max": 300, "step": 50},
    "series": [
        {"kind": "line", "points": p3_line},
        {"kind": "curve", "points": p3_curve},
    ],
    "marks": [{"x": 2.5, "y": 250, "label": "P", "drop": True, "dx": 8, "dy": 14}],
    "alt": "Stress–strain graph: straight from the origin to P (strain 0.0025, stress 250 MPa), then curving with decreasing gradient to 290 MPa at a strain of 0.005",
}

# ---------------------------------------------------------------
# p4: aluminium alloy strut, stress–strain straight line (σ in 10⁸ Pa);
#     strain energy per unit volume up to P = triangle area.
# ---------------------------------------------------------------

p4_points = [[0, 0], [5, 3.75]]
p4_stress_pa = 3 * 1e8
p4_strain = 4 * 1e-3
p4_energy_density = triangle_area(p4_strain, p4_stress_pa)
record("fx-stress-strain-graph-p4", p4_energy_density, "J m⁻³")
GRAPHS["fx-stress-strain-graph-p4"] = {
    "x": {"label": "ε / 10⁻³", "min": 0, "max": 5, "step": 1},
    "y": {"label": "σ / 10⁸ Pa", "min": 0, "max": 4, "step": 1},
    "series": [{"kind": "line", "points": p4_points}],
    "marks": [{"x": 4, "y": 3, "label": "P", "drop": True, "dx": 8, "dy": 14}],
    "shade": [{"series": 0, "from": 0, "to": 4}],
    "alt": "Stress–strain graph: a straight line from the origin through P (strain 0.004, stress 3 × 10⁸ Pa); the triangle under the line up to P is shaded",
}

# ---------------------------------------------------------------
# p5: steel wire, F–x straight line (x in mm); k from gradient, then
#     E = kL / A with L = 2.0 m and A = 0.50 mm².
# ---------------------------------------------------------------

p5_points = [[0, 0], [2.0, 100]]
p5_x_m = 2.0 * 1e-3
p5_k = 100 / p5_x_m
p5_length = 2.0
p5_area = 0.50 * 1e-6
p5_young = p5_k * p5_length / p5_area
record("fx-stress-strain-graph-p5", p5_young, "Pa")
GRAPHS["fx-stress-strain-graph-p5"] = {
    "x": {"label": "x / mm", "min": 0, "max": 2.5, "step": 0.5},
    "y": {"label": "F / N", "min": 0, "max": 120, "step": 20},
    "series": [{"kind": "line", "points": p5_points}],
    "marks": [{"x": 2.0, "y": 100, "label": "X", "drop": True, "dx": -16, "dy": -8}],
    "alt": "Force–extension graph for a steel wire: a straight line from the origin to X (2.0 mm, 100 N)",
}

# ---------------------------------------------------------------
# p6: car suspension spring, F–x straight line (F in kN, x in cm);
#     work done stretching from A to B = trapezium area.
# ---------------------------------------------------------------

p6_points = [[0, 0], [12, 6]]
p6_f_a = 2 * 1e3
p6_f_b = 5 * 1e3
p6_width_m = (10 - 4) * 1e-2
p6_work = trapezium_area(p6_f_a, p6_f_b, p6_width_m)
record("fx-stress-strain-graph-p6", p6_work, "J")
GRAPHS["fx-stress-strain-graph-p6"] = {
    "x": {"label": "x / cm", "min": 0, "max": 12, "step": 2},
    "y": {"label": "F / kN", "min": 0, "max": 6, "step": 1},
    "series": [{"kind": "line", "points": p6_points}],
    "marks": [
        {"x": 4, "y": 2, "label": "A", "drop": True, "dx": -16, "dy": -6},
        {"x": 10, "y": 5, "label": "B", "drop": True, "dx": -16, "dy": -6},
    ],
    "shade": [{"series": 0, "from": 4, "to": 10}],
    "alt": "Force–extension graph for a car spring: a straight line from the origin to 6 kN at 12 cm; the trapezium under the line between A (4 cm, 2 kN) and B (10 cm, 5 kN) is shaded",
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
