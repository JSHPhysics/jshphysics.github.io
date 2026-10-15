#!/usr/bin/env python3
"""Compute every answer and every plotted coordinate for the "Reading
oscillation graphs" type (shm-graph) in data/circular-shm.json.

Sinusoids are sampled here (24 points per cycle, or a fixed fine step for
the tangent questions) and each answer is computed from the same
parameters. For the two tangent questions the curve's angular frequency is
derived from the tangent's gridline end points, so the drawn tangent is
exactly the tangent of the drawn curve; the period is stated in the
question rather than read off.
Run: python3 tools/calc_circular-shm_graph.py [out.json]
"""

import json
import math
import sys

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


def sinusoid(amplitude, period, start, stop, shape="sin", per_cycle=24):
    """Sample A sin(2πt/T) or A cos(2πt/T) from start to stop inclusive."""
    spacing = period / per_cycle
    count = int(round((stop - start) / spacing))
    points = []
    for index in range(count + 1):
        t = start + index * spacing
        angle = 2 * math.pi * t / period
        if shape == "sin":
            y = amplitude * math.sin(angle)
        else:
            y = amplitude * math.cos(angle)
        points.append([round(t, 4), round(y, 4)])
    return points


def shifted_sine(amplitude, omega, t_zero, start, stop, spacing):
    """Sample A sin(ω(t − t_zero)) from start to stop with a fixed spacing.

    The curve crosses zero going upwards at t_zero, where its gradient is
    exactly ωA.
    """
    count = int(round((stop - start) / spacing))
    points = []
    for index in range(count + 1):
        t = start + index * spacing
        y = amplitude * math.sin(omega * (t - t_zero))
        points.append([round(t, 4), round(y, 4)])
    return points


# ---------------------------------------------------------------------
# Worked example: displacement–time graph of a mass on a spring.
# Sine, T = 1.2 s, A = 5.0 cm. Read T and A, then v_max = ωA.
# ---------------------------------------------------------------------
T_w = 1.2          # s
A_w_cm = 5.0       # cm
A_w = A_w_cm * 1e-2
omega_w = 2 * math.pi / T_w
vmax_w = omega_w * A_w
record("shm-graph-w", vmax_w, "m s⁻¹", "ω = %.3f rad/s, A = %.3f m" % (omega_w, A_w))
graphs["shm-graph-w"] = {
    "x": {"label": "t / s", "min": 0, "max": 2.4, "step": 0.3},
    "y": {"label": "x / cm", "min": -6, "max": 6, "step": 1},
    "series": [{"kind": "curve", "points": sinusoid(A_w_cm, T_w, 0, 2.4, "sin")}],
    "marks": [
        {"x": 0.3, "y": A_w_cm, "label": "P", "drop": True},
        {"x": 1.5, "y": A_w_cm, "label": "Q", "drop": True},
    ],
    "alt": "Displacement–time graph: a sine curve of amplitude 5 cm with peaks at 0.3 s and 1.5 s marked P and Q",
}

# ---------------------------------------------------------------------
# p1: displacement–time graph of a short pendulum. Sine, T = 0.80 s,
# A = 3.0 cm. Read the period.
# ---------------------------------------------------------------------
T_1 = 0.80
A_1_cm = 3.0
record("shm-graph-p1", T_1, "s", "peaks at 0.2 s and 1.0 s")
graphs["shm-graph-p1"] = {
    "x": {"label": "t / s", "min": 0, "max": 2.0, "step": 0.2},
    "y": {"label": "x / cm", "min": -4, "max": 4, "step": 1},
    "series": [{"kind": "curve", "points": sinusoid(A_1_cm, T_1, 0, 2.0, "sin")}],
    "marks": [
        {"x": 0.2, "y": A_1_cm, "label": "A", "drop": True},
        {"x": 1.0, "y": A_1_cm, "label": "B", "drop": True},
    ],
    "alt": "Displacement–time graph: a sine curve of amplitude 3 cm with peaks at 0.2, 1.0 and 1.8 s; the first two peaks are marked A and B",
}

# ---------------------------------------------------------------------
# p2: displacement–time graph of a vibrating hacksaw blade. Sine,
# T = 40 ms, A = 4.0 mm. Read T, convert ms, f = 1/T.
# ---------------------------------------------------------------------
T_2_ms = 40.0
A_2_mm = 4.0
f_2 = 1 / (T_2_ms * 1e-3)
record("shm-graph-p2", f_2, "Hz", "T = 40 ms from peaks at 10 and 50 ms")
graphs["shm-graph-p2"] = {
    "x": {"label": "t / ms", "min": 0, "max": 120, "step": 10},
    "y": {"label": "x / mm", "min": -6, "max": 6, "step": 2},
    "series": [{"kind": "curve", "points": sinusoid(A_2_mm, T_2_ms, 0, 120, "sin")}],
    "marks": [
        {"x": 10, "y": A_2_mm, "label": "A", "drop": True},
        {"x": 50, "y": A_2_mm, "label": "B", "drop": True},
    ],
    "alt": "Displacement–time graph: a sine curve of amplitude 4 mm with peaks at 10, 50 and 90 ms; the first two peaks are marked A and B",
}

# ---------------------------------------------------------------------
# p3: velocity–time graph of a moored boat. Maximum acceleration from
# the gradient of the tangent at the zero crossing X (t = 3.0 s).
# Tangent end points on gridlines: (1.0, −0.5) and (5.0, 0.5).
# v_max = 0.40 m/s; ω is derived so the tangent is exact.
# ---------------------------------------------------------------------
vmax_3 = 0.40
tX_3 = 3.0
tan_3 = [[1.0, -0.5], [5.0, 0.5]]
amax_3 = (tan_3[1][1] - tan_3[0][1]) / (tan_3[1][0] - tan_3[0][0])
omega_3 = amax_3 / vmax_3
T_3 = 2 * math.pi / omega_3
record("shm-graph-p3", amax_3, "m s⁻²", "ω = %.4f rad/s, T = %.2f s (curve only)" % (omega_3, T_3))
graphs["shm-graph-p3"] = {
    "x": {"label": "t / s", "min": 0, "max": 8, "step": 1},
    "y": {"label": "v / m s⁻¹", "min": -0.5, "max": 0.5, "step": 0.1},
    "series": [
        {"kind": "curve", "points": shifted_sine(vmax_3, omega_3, tX_3, 0, 8, 0.2)},
        {"kind": "tangent", "points": tan_3},
    ],
    "marks": [{"x": tX_3, "y": 0, "label": "X", "dx": 8, "dy": 18}],
    "labels": [{"x": 5.2, "y": 0.46, "text": "tangent at X"}],
    "alt": "Velocity–time graph: a sinusoidal curve of amplitude 0.4 m/s crossing zero upwards at 3 s (marked X), with the tangent at X drawn from (1.0 s, −0.5 m/s) to (5.0 s, 0.5 m/s)",
}

# ---------------------------------------------------------------------
# p4: displacement–time graph of a long museum pendulum. Maximum speed
# from the gradient of the tangent at the zero crossing X (t = 4.0 s).
# Tangent end points: (2.0, −1.0) and (6.0, 1.0). A = 0.60 m.
# The question states the period (7.5 s) for the ωA check.
# ---------------------------------------------------------------------
A_4 = 0.60
tX_4 = 4.0
tan_4 = [[2.0, -1.0], [6.0, 1.0]]
vmax_4 = (tan_4[1][1] - tan_4[0][1]) / (tan_4[1][0] - tan_4[0][0])
omega_4 = vmax_4 / A_4
T_4 = 2 * math.pi / omega_4
T_4_stated = 7.5
check_4 = 2 * math.pi / T_4_stated * A_4
record("shm-graph-p4", vmax_4, "m s⁻¹", "ω = %.4f rad/s, T = %.2f s; ωA with T = 7.5 s gives %.3f" % (omega_4, T_4, check_4))
graphs["shm-graph-p4"] = {
    "x": {"label": "t / s", "min": 0, "max": 8, "step": 1},
    "y": {"label": "x / m", "min": -1.0, "max": 1.0, "step": 0.2},
    "series": [
        {"kind": "curve", "points": shifted_sine(A_4, omega_4, tX_4, 0, 8, 0.2)},
        {"kind": "tangent", "points": tan_4},
    ],
    "marks": [{"x": tX_4, "y": 0, "label": "X", "dx": 8, "dy": 18}],
    "labels": [{"x": 6.2, "y": 0.92, "text": "tangent at X"}],
    "alt": "Displacement–time graph: a sinusoidal curve of amplitude 0.6 m crossing zero upwards at 4 s (marked X), with the tangent at X drawn from (2.0 s, −1.0 m) to (6.0 s, 1.0 m)",
}

# ---------------------------------------------------------------------
# p5: velocity–time graph of a 0.20 kg pendulum bob. Sine, T = 2.0 s,
# v_max = 1.5 m/s read at P. KE_max = ½ m v_max².
# ---------------------------------------------------------------------
T_5 = 2.0
vmax_5 = 1.5
m_5 = 0.20
KE_5 = 0.5 * m_5 * vmax_5 ** 2
record("shm-graph-p5", KE_5, "J", "v_max = %.1f m/s read at P" % vmax_5)
graphs["shm-graph-p5"] = {
    "x": {"label": "t / s", "min": 0, "max": 4, "step": 0.5},
    "y": {"label": "v / m s⁻¹", "min": -2, "max": 2, "step": 0.5},
    "series": [{"kind": "curve", "points": sinusoid(vmax_5, T_5, 0, 4, "sin")}],
    "marks": [{"x": 0.5, "y": vmax_5, "label": "P", "drop": True}],
    "alt": "Velocity–time graph: a sine curve of amplitude 1.5 m/s and period 2 s; the first peak at 0.5 s is marked P",
}

# ---------------------------------------------------------------------
# p6: acceleration–displacement graph: straight line through the origin
# from A (−0.10 m, 2.5 m s⁻²) to B (0.10 m, −2.5 m s⁻²).
# gradient = −ω², then T = 2π/ω.
# ---------------------------------------------------------------------
pA_6 = [-0.10, 2.5]
pB_6 = [0.10, -2.5]
gradient_6 = (pB_6[1] - pA_6[1]) / (pB_6[0] - pA_6[0])
omega_sq_6 = -gradient_6
omega_6 = math.sqrt(omega_sq_6)
T_6 = 2 * math.pi / omega_6
record("shm-graph-p6", T_6, "s", "gradient = %.1f s⁻², ω = %.2f rad/s" % (gradient_6, omega_6))
graphs["shm-graph-p6"] = {
    "x": {"label": "x / m", "min": -0.1, "max": 0.1, "step": 0.05},
    "y": {"label": "a / m s⁻²", "min": -3, "max": 3, "step": 0.5},
    "series": [{"kind": "line", "points": [pA_6, pB_6]}],
    "marks": [
        {"x": pA_6[0], "y": pA_6[1], "label": "A", "drop": True},
        {"x": pB_6[0], "y": pB_6[1], "label": "B", "drop": True, "dx": -18, "dy": 16},
    ],
    "alt": "Acceleration–displacement graph: a straight line through the origin from A at (−0.10 m, 2.5 m/s²) to B at (0.10 m, −2.5 m/s²)",
}


# ---------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------
for question_id, rounded, unit, raw, notes in results:
    print("%-14s %-10r %-8s raw=%.6g  %s" % (question_id, rounded, unit, raw, notes))

if len(sys.argv) > 1:
    dump = {}
    for question_id, rounded, unit, raw, notes in results:
        dump[question_id] = {"answer": rounded, "unit": unit, "graph": graphs[question_id]}
    with open(sys.argv[1], "w", encoding="utf-8") as handle:
        json.dump(dump, handle, ensure_ascii=False, indent=1)
    print("wrote", sys.argv[1])
