#!/usr/bin/env python3
"""Compute every answer and every plotted coordinate for the "Reading wave
graphs" type (wave-graph) in data/waves.json.

Each sinusoid is sampled here (24 points per cycle) and the answer is
computed from the same parameters, so graph and answer agree.
Run: python3 tools/calc_waves_graph.py [out.json]
With an output path, the graph specs and answers are dumped as JSON so the
topic file can be assembled from them.
"""

import json
import math
import sys

# Standard constants from SCHEMA.md
c = 3.00e8  # m s^-1

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
    """Sample y = A sin(2πt/T) or A cos(2πt/T) from start to stop inclusive.

    The spacing is period / per_cycle so every peak and zero crossing is
    one of the sampled points exactly.
    """
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
        # Tidy the coordinates so the JSON stays readable
        points.append([round(t, 4), round(y, 4)])
    return points


# ---------------------------------------------------------------------
# Worked example: displacement–time graph of a point on a guitar string.
# Cosine, T = 4.0 ms, A = 3.0 mm; read T peak to peak, then f = 1/T.
# ---------------------------------------------------------------------
T_w = 4.0          # ms
A_w = 3.0          # mm
f_w = 1 / (T_w * 1e-3)
record("wave-graph-w", f_w, "Hz", "T = %.1f ms read from peaks at 4 and 8 ms" % T_w)
graphs["wave-graph-w"] = {
    "x": {"label": "t / ms", "min": 0, "max": 12, "step": 1},
    "y": {"label": "y / mm", "min": -4, "max": 4, "step": 1},
    "series": [{"kind": "curve", "points": sinusoid(A_w, T_w, 0, 12, "cos")}],
    "marks": [
        {"x": 4, "y": A_w, "label": "A", "drop": True},
        {"x": 8, "y": A_w, "label": "B", "drop": True},
    ],
    "alt": "Displacement–time graph: a cosine wave of amplitude 3 mm with peaks at 0, 4, 8 and 12 ms; the peaks at 4 ms and 8 ms are marked A and B",
}

# ---------------------------------------------------------------------
# p1: displacement–time graph of a buoy. Sine, T = 2.0 s, A = 20 cm.
# Read the period from successive peaks.
# ---------------------------------------------------------------------
T_1 = 2.0          # s
A_1 = 20.0         # cm
record("wave-graph-p1", T_1, "s", "peaks at 0.5 s and 2.5 s")
graphs["wave-graph-p1"] = {
    "x": {"label": "t / s", "min": 0, "max": 6, "step": 0.5},
    "y": {"label": "y / cm", "min": -25, "max": 25, "step": 5},
    "series": [{"kind": "curve", "points": sinusoid(A_1, T_1, 0, 6, "sin")}],
    "marks": [
        {"x": 0.5, "y": A_1, "label": "P", "drop": True},
        {"x": 2.5, "y": A_1, "label": "Q", "drop": True},
    ],
    "alt": "Displacement–time graph: a sine wave of amplitude 20 cm with peaks at 0.5, 2.5 and 4.5 s; the first two peaks are marked P and Q",
}

# ---------------------------------------------------------------------
# p2: displacement–distance graph of a wave on a rope. Sine, λ = 1.2 m,
# A = 4.0 cm. Read the wavelength from successive peaks.
# ---------------------------------------------------------------------
lam_2 = 1.2        # m
A_2 = 4.0          # cm
record("wave-graph-p2", lam_2, "m", "peaks at 0.3 m and 1.5 m")
graphs["wave-graph-p2"] = {
    "x": {"label": "x / m", "min": 0, "max": 3.0, "step": 0.3},
    "y": {"label": "y / cm", "min": -5, "max": 5, "step": 1},
    "series": [{"kind": "curve", "points": sinusoid(A_2, lam_2, 0, 3.0, "sin")}],
    "marks": [
        {"x": 0.3, "y": A_2, "label": "P", "drop": True},
        {"x": 1.5, "y": A_2, "label": "Q", "drop": True},
    ],
    "alt": "Displacement–distance graph: a sine wave of amplitude 4 cm with peaks at 0.3, 1.5 and 2.7 m; the first two peaks are marked P and Q",
}

# ---------------------------------------------------------------------
# p3: displacement–time graph of a loudspeaker cone. Cosine, T = 8.0 ms,
# A = 0.80 mm. Read the amplitude and give it in metres.
# ---------------------------------------------------------------------
T_3 = 8.0          # ms
A_3 = 0.80         # mm
A_3_m = A_3 * 1e-3
record("wave-graph-p3", A_3_m, "m", "amplitude 0.80 mm read at the peak")
graphs["wave-graph-p3"] = {
    "x": {"label": "t / ms", "min": 0, "max": 16, "step": 2},
    "y": {"label": "y / mm", "min": -1.0, "max": 1.0, "step": 0.2},
    "series": [{"kind": "curve", "points": sinusoid(A_3, T_3, 0, 16, "cos")}],
    "marks": [{"x": 8, "y": A_3, "label": "X", "drop": True}],
    "alt": "Displacement–time graph: a cosine wave of amplitude 0.8 mm with peaks at 0, 8 and 16 ms; the peak at 8 ms is marked X",
}

# ---------------------------------------------------------------------
# p4: displacement–time graph of an ultrasound transducer face. Sine,
# T = 20 μs, A = 1.5 μm. Read T, convert μs, find f in kHz.
# ---------------------------------------------------------------------
T_4 = 20.0         # μs
A_4 = 1.5          # μm
f_4 = 1 / (T_4 * 1e-6)
f_4_kHz = f_4 / 1e3
record("wave-graph-p4", f_4_kHz, "kHz", "T = 20 μs from peaks at 5 and 25 μs; f = %.0f Hz" % f_4)
graphs["wave-graph-p4"] = {
    "x": {"label": "t / μs", "min": 0, "max": 60, "step": 5},
    "y": {"label": "y / μm", "min": -2.0, "max": 2.0, "step": 0.5},
    "series": [{"kind": "curve", "points": sinusoid(A_4, T_4, 0, 60, "sin")}],
    "marks": [
        {"x": 5, "y": A_4, "label": "A", "drop": True},
        {"x": 25, "y": A_4, "label": "B", "drop": True},
    ],
    "alt": "Displacement–time graph: a sine wave of amplitude 1.5 micrometres with peaks at 5, 25 and 45 microseconds; the first two peaks are marked A and B",
}

# ---------------------------------------------------------------------
# p5: displacement–distance graph of a ripple-tank wave. Sine, λ = 2.0 cm,
# A = 2.0 mm. Period T = 0.25 s given. v = λ / T.
# ---------------------------------------------------------------------
lam_5_cm = 2.0     # cm
lam_5 = lam_5_cm * 1e-2
A_5 = 2.0          # mm
T_5 = 0.25         # s
f_5 = 1 / T_5
v_5 = f_5 * lam_5
record("wave-graph-p5", v_5, "m s⁻¹", "λ = 2.0 cm from peaks at 0.5 and 2.5 cm; f = %.1f Hz" % f_5)
graphs["wave-graph-p5"] = {
    "x": {"label": "x / cm", "min": 0, "max": 6, "step": 0.5},
    "y": {"label": "y / mm", "min": -3, "max": 3, "step": 1},
    "series": [{"kind": "curve", "points": sinusoid(A_5, lam_5_cm, 0, 6, "sin")}],
    "marks": [
        {"x": 0.5, "y": A_5, "label": "P", "drop": True},
        {"x": 2.5, "y": A_5, "label": "Q", "drop": True},
    ],
    "alt": "Displacement–distance graph: a sine wave of amplitude 2 mm with peaks at 0.5, 2.5 and 4.5 cm; the first two peaks are marked P and Q",
}

# ---------------------------------------------------------------------
# p6: displacement–distance graph of a sea wave. Sine, λ = 8.0 m,
# A = 0.60 m. P is the peak at x = 2.0 m, Q the zero crossing at
# x = 8.0 m. Phase difference in radians.
# ---------------------------------------------------------------------
lam_6 = 8.0        # m
A_6 = 0.60         # m
x_P = 2.0
x_Q = 8.0
dx_6 = x_Q - x_P
phase_6 = (dx_6 / lam_6) * 2 * math.pi
record("wave-graph-p6", phase_6, "rad", "Δx = %.1f m = %.2f λ" % (dx_6, dx_6 / lam_6))
graphs["wave-graph-p6"] = {
    "x": {"label": "x / m", "min": 0, "max": 16, "step": 2},
    "y": {"label": "y / m", "min": -0.8, "max": 0.8, "step": 0.2},
    "series": [{"kind": "curve", "points": sinusoid(A_6, lam_6, 0, 16, "sin")}],
    "marks": [
        {"x": x_P, "y": A_6, "label": "P", "drop": True},
        {"x": x_Q, "y": 0, "label": "Q", "drop": True},
    ],
    "alt": "Displacement–distance graph: a sine wave of amplitude 0.6 m and wavelength 8 m; P marks the peak at 2 m and Q the zero crossing at 8 m",
}


# ---------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------
for question_id, rounded, unit, raw, notes in results:
    print("%-16s %-14r %-8s raw=%.6g  %s" % (question_id, rounded, unit, raw, notes))

if len(sys.argv) > 1:
    dump = {}
    for question_id, rounded, unit, raw, notes in results:
        dump[question_id] = {"answer": rounded, "unit": unit, "graph": graphs[question_id]}
    with open(sys.argv[1], "w", encoding="utf-8") as handle:
        json.dump(dump, handle, ensure_ascii=False, indent=1)
    print("wrote", sys.argv[1])
