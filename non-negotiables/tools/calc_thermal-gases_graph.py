#!/usr/bin/env python3
"""Compute every answer and every plotted coordinate for the "Reading
thermal and gas graphs" type (thermal-graph) in data/thermal-gases.json.

Every line is defined by gridline end points and each answer is computed
from those same points (gradient, flat-section length, intercept or
trapezium area), so graph and answer agree.
Run: python3 tools/calc_thermal-gases_graph.py [out.json]
"""

import json
import math
import sys

# Standard constants from SCHEMA.md
R = 8.31          # J mol^-1 K^-1
k = 1.38e-23      # J K^-1

results = []
graphs = {}


def round_sf(value, sf=3):
    """Round a value to a given number of significant figures."""
    if value == 0:
        return 0.0
    magnitude = math.floor(math.log10(abs(value)))
    places = sf - 1 - magnitude
    return round(value, places)


def record(question_id, value, unit, notes=""):
    """Store one answer rounded to 3 significant figures."""
    rounded = round_sf(value)
    results.append((question_id, rounded, unit, value, notes))


def gradient(p, q):
    """Gradient of the straight line through two points."""
    return (q[1] - p[1]) / (q[0] - p[0])


# ---------------------------------------------------------------------
# Worked example: temperature–time graph of water heated in a kettle at
# constant power. Line from A (0 s, 20 °C) to B (100 s, 80 °C), drawn on
# to 120 s. c = P / (m × gradient).
# ---------------------------------------------------------------------
P_w = 2000.0       # W
m_w = 0.80         # kg
A_w = [0, 20]
B_w = [100, 80]
grad_w = gradient(A_w, B_w)                 # K s^-1
end_w = [120, A_w[1] + grad_w * 120]
c_w = P_w / (m_w * grad_w)
record("thermal-graph-w", c_w, "J kg⁻¹ K⁻¹", "gradient = %.2f K/s" % grad_w)
graphs["thermal-graph-w"] = {
    "x": {"label": "t / s", "min": 0, "max": 120, "step": 20},
    "y": {"label": "θ / °C", "min": 0, "max": 100, "step": 10},
    "series": [{"kind": "line", "points": [A_w, [end_w[0], round(end_w[1], 4)]]}],
    "marks": [
        {"x": A_w[0], "y": A_w[1], "label": "A", "dx": 10, "dy": 14},
        {"x": B_w[0], "y": B_w[1], "label": "B", "drop": True, "dx": 8, "dy": 16},
    ],
    "alt": "Temperature–time graph: a straight line rising from A at 20 °C at time zero through B at 80 °C at 100 s",
}

# ---------------------------------------------------------------------
# p1: pressure against Celsius temperature for a fixed mass of gas at
# constant volume. Measured crosses from 0 to 100 °C, best-fit line,
# dashed extension to the temperature axis at absolute zero (−273 °C).
# p(θ) = p0 (θ + 273) / 273 with p0 = 100 kPa.
# ---------------------------------------------------------------------
abs_zero_1 = -273.0
p0_1 = 100.0       # kPa at 0 °C


def pressure_1(theta):
    """Pressure in kPa at Celsius temperature theta on the p1 line."""
    return p0_1 * (theta - abs_zero_1) / (-abs_zero_1)


data_1 = [[theta, round(pressure_1(theta), 2)] for theta in [0, 20, 40, 60, 80, 100]]
record("thermal-graph-p1", abs_zero_1, "°C", "intercept of the extended line")
graphs["thermal-graph-p1"] = {
    "x": {"label": "θ / °C", "min": -300, "max": 100, "step": 50},
    "y": {"label": "p / kPa", "min": 0, "max": 150, "step": 25},
    "series": [
        {"kind": "data", "points": data_1, "fit": [[0, p0_1], [100, round(pressure_1(100), 2)]]},
        {"kind": "dashed", "points": [[abs_zero_1, 0], [0, p0_1]]},
    ],
    "marks": [{"x": abs_zero_1, "y": 0, "label": "X", "dx": -22, "dy": -8}],
    "alt": "Pressure against Celsius temperature: data points from 0 to 100 °C on a straight line rising from 100 kPa, extended as a dashed line down to the temperature axis at X near −273 °C",
}

# ---------------------------------------------------------------------
# p2: heating curve of 0.20 kg of paraffin wax with a 250 W heater.
# Solid from (0, 20) to (80, 60); flat section A (80 s) to B (200 s) at
# the melting point 60 °C; liquid from (200, 60) to (240, 80). L = P Δt / m.
# ---------------------------------------------------------------------
P_2 = 250.0
m_2 = 0.20
solid_start_2 = [0, 20]
A_2 = [80, 60]
B_2 = [200, 60]
liquid_end_2 = [240, 80]
dt_2 = B_2[0] - A_2[0]
L_2 = P_2 * dt_2 / m_2
record("thermal-graph-p2", L_2, "J kg⁻¹", "flat section %.0f s; solid gradient %.2f K/s, liquid gradient %.2f K/s" %
       (dt_2, gradient(solid_start_2, A_2), gradient(B_2, liquid_end_2)))
graphs["thermal-graph-p2"] = {
    "x": {"label": "t / s", "min": 0, "max": 240, "step": 20},
    "y": {"label": "θ / °C", "min": 0, "max": 100, "step": 10},
    "series": [{"kind": "line", "points": [solid_start_2, A_2, B_2, liquid_end_2]}],
    "marks": [
        {"x": A_2[0], "y": A_2[1], "label": "A", "dx": -4, "dy": -10},
        {"x": B_2[0], "y": B_2[1], "label": "B", "dx": -4, "dy": -10},
    ],
    "alt": "Temperature–time heating curve: rising from 20 °C to 60 °C in the first 80 s, flat at 60 °C from A at 80 s to B at 200 s, then rising again to 80 °C at 240 s",
}

# ---------------------------------------------------------------------
# p3: work done by a gas from the area under a p–V graph. Straight line
# from A (1.0 × 10⁻³ m³, 3.0 × 10⁵ Pa) to B (4.0 × 10⁻³ m³, 1.0 × 10⁵ Pa).
# Trapezium area. Boards: Edexcel, OCR A, OCR B, WJEC only.
# ---------------------------------------------------------------------
A_3 = [1.0, 3.0]   # V / 10^-3 m^3, p / 10^5 Pa
B_3 = [4.0, 1.0]
W_3 = 0.5 * (A_3[1] + B_3[1]) * 1e5 * (B_3[0] - A_3[0]) * 1e-3
record("thermal-graph-p3", W_3, "J", "trapezium ½(3.0 + 1.0) × 10⁵ × 3.0 × 10⁻³")
graphs["thermal-graph-p3"] = {
    "x": {"label": "V / 10⁻³ m³", "min": 0, "max": 5, "step": 1},
    "y": {"label": "p / 10⁵ Pa", "min": 0, "max": 4, "step": 1},
    "series": [{"kind": "line", "points": [A_3, B_3]}],
    "marks": [
        {"x": A_3[0], "y": A_3[1], "label": "A", "drop": True},
        {"x": B_3[0], "y": B_3[1], "label": "B", "drop": True},
    ],
    "shade": [{"series": 0, "from": A_3[0], "to": B_3[0]}],
    "alt": "Pressure–volume graph: a straight line falling from A at 3.0 × 10⁵ Pa and 1.0 × 10⁻³ m³ to B at 1.0 × 10⁵ Pa and 4.0 × 10⁻³ m³, with the area beneath it shaded",
}

# ---------------------------------------------------------------------
# p4: pressure against kelvin temperature at fixed volume V = 2.0 × 10⁻³ m³.
# Solid line from (200 K, 100 kPa) to (400 K, 200 kPa), dashed back to
# the origin. gradient = Nk/V → N.
# ---------------------------------------------------------------------
V_4 = 2.0e-3
P1_4 = [200, 100]
P2_4 = [400, 200]
grad_4_kPa = gradient(P1_4, P2_4)           # kPa K^-1
grad_4 = grad_4_kPa * 1e3                   # Pa K^-1
N_4 = grad_4 * V_4 / k
record("thermal-graph-p4", N_4, "", "gradient = %.2f kPa/K = %.0f Pa/K" % (grad_4_kPa, grad_4))
graphs["thermal-graph-p4"] = {
    "x": {"label": "T / K", "min": 0, "max": 400, "step": 50},
    "y": {"label": "p / kPa", "min": 0, "max": 250, "step": 50},
    "series": [
        {"kind": "dashed", "points": [[0, 0], P1_4]},
        {"kind": "line", "points": [P1_4, P2_4]},
    ],
    "marks": [
        {"x": P1_4[0], "y": P1_4[1], "label": "A", "drop": True, "dx": -18, "dy": -6},
        {"x": P2_4[0], "y": P2_4[1], "label": "B", "drop": True, "dx": -18, "dy": -6},
    ],
    "alt": "Pressure against kelvin temperature: a straight line through the origin, dashed up to A at 200 K and 100 kPa, then solid to B at 400 K and 200 kPa",
}

# ---------------------------------------------------------------------
# p5: pV against T for a sample of gas. Solid line from (150 K, 600 J)
# to (400 K, 1600 J), dashed back to the origin. gradient = nR → n.
# ---------------------------------------------------------------------
P1_5 = [150, 600]
P2_5 = [400, 1600]
grad_5 = gradient(P1_5, P2_5)               # J K^-1
n_5 = grad_5 / R
record("thermal-graph-p5", n_5, "mol", "gradient = %.2f J/K" % grad_5)
graphs["thermal-graph-p5"] = {
    "x": {"label": "T / K", "min": 0, "max": 400, "step": 50},
    "y": {"label": "pV / J", "min": 0, "max": 2000, "step": 200},
    "series": [
        {"kind": "dashed", "points": [[0, 0], P1_5]},
        {"kind": "line", "points": [P1_5, P2_5]},
    ],
    "marks": [
        {"x": P1_5[0], "y": P1_5[1], "label": "A", "drop": True, "dx": -18, "dy": -6},
        {"x": P2_5[0], "y": P2_5[1], "label": "B", "drop": True, "dx": -18, "dy": -6},
    ],
    "alt": "pV against kelvin temperature: a straight line through the origin, dashed up to A at 150 K and 600 J, then solid to B at 400 K and 1600 J",
}

# ---------------------------------------------------------------------
# p6: temperature–time graph of 0.60 kg of cooking oil (c = 2000 J kg⁻¹ K⁻¹)
# heated on a hob. Line from A (0 min, 20 °C) to B (4 min, 140 °C),
# drawn on to 5 min. P = m c × gradient (gradient converted to K/s).
# ---------------------------------------------------------------------
m_6 = 0.60
c_6 = 2000.0
A_6 = [0, 20]
B_6 = [4, 140]
grad_6_per_min = gradient(A_6, B_6)         # K min^-1
grad_6 = grad_6_per_min / 60.0              # K s^-1
end_6 = [5, A_6[1] + grad_6_per_min * 5]
P_6 = m_6 * c_6 * grad_6
record("thermal-graph-p6", P_6, "W", "gradient = %.0f K/min = %.2f K/s" % (grad_6_per_min, grad_6))
graphs["thermal-graph-p6"] = {
    "x": {"label": "t / min", "min": 0, "max": 5, "step": 1},
    "y": {"label": "θ / °C", "min": 0, "max": 180, "step": 20},
    "series": [{"kind": "line", "points": [A_6, end_6]}],
    "marks": [
        {"x": A_6[0], "y": A_6[1], "label": "A", "dx": 10, "dy": 14},
        {"x": B_6[0], "y": B_6[1], "label": "B", "drop": True, "dx": 8, "dy": 16},
    ],
    "alt": "Temperature–time graph: a straight line rising from A at 20 °C at time zero through B at 140 °C at 4 minutes",
}


# ---------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------
for question_id, rounded, unit, raw, notes in results:
    print("%-18s %-12r %-14s raw=%.6g  %s" % (question_id, rounded, unit, raw, notes))

if len(sys.argv) > 1:
    dump = {}
    for question_id, rounded, unit, raw, notes in results:
        value = rounded
        # Large round answers are stored as integers so they do not look unrounded
        if isinstance(value, float) and value.is_integer() and 1e3 <= abs(value) < 1e15:
            value = int(value)
        dump[question_id] = {"answer": value, "unit": unit, "graph": graphs[question_id]}
    with open(sys.argv[1], "w", encoding="utf-8") as handle:
        json.dump(dump, handle, ensure_ascii=False, indent=1)
    print("wrote", sys.argv[1])
