#!/usr/bin/env python3
"""Compute every answer and every plotted coordinate for the "Reading
photoelectric graphs" type (photoelectric-graph) in data/quantum.json.

Every graph is stopping potential V_s (V) against frequency f (10^14 Hz):
V_s = (h/e) f − φ/e. Each line is defined by its threshold frequency
(x-intercept) and a gradient of 5/12 V per 10^14 Hz = 4.17 × 10^-15 V s,
which is h/e to 0.6% and lands on gridlines. Answers are computed from the
same intercepts and gradients the graphs use.
Run: python3 tools/calc_quantum_graph.py [out.json]
"""

import json
import math
import sys

# Standard constants from SCHEMA.md
h = 6.63e-34      # J s
e = 1.60e-19      # C
c = 3.00e8        # m s^-1

X_UNIT = 1e14     # the f axis is in units of 10^14 Hz
GRADIENT = 5.0 / 12.0   # V per 10^14 Hz, used for every line

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


def line_at(f0, f):
    """Stopping potential on a line with threshold f0 at frequency f (axis units)."""
    return GRADIENT * (f - f0)


def photo_series(f0, x_max, y_max, with_extension=True):
    """Series for one photoelectric line: dashed below the axis, solid above.

    The solid part runs from the threshold to whichever comes first, the
    right-hand edge or the top of the plot.
    """
    f_top = f0 + y_max / GRADIENT
    f_end = min(x_max, f_top)
    y_end = line_at(f0, f_end)
    series = []
    if with_extension:
        y_intercept = line_at(f0, 0)
        series.append({"kind": "dashed", "points": [[0, round(y_intercept, 4)], [f0, 0]]})
    series.append({"kind": "line", "points": [[f0, 0], [round(f_end, 4), round(y_end, 4)]]})
    return series


# ---------------------------------------------------------------------
# Worked example: threshold frequency from the x-intercept.
# Line: f0 = 6.0 (×10^14 Hz), y-intercept −2.5 V.
# ---------------------------------------------------------------------
f0_w = 6.0
f0_w_Hz = f0_w * X_UNIT
record("photoelectric-graph-w", f0_w_Hz, "Hz", "x-intercept 6.0; y-intercept %.2f V" % line_at(f0_w, 0))
graphs["photoelectric-graph-w"] = {
    "x": {"label": "f / 10¹⁴ Hz", "min": 0, "max": 12, "step": 1},
    "y": {"label": "V_s / V", "min": -3, "max": 3, "step": 0.5},
    "series": photo_series(f0_w, 12, 3),
    "marks": [{"x": f0_w, "y": 0, "label": "X", "dx": 8, "dy": 18}],
    "alt": "Stopping potential against frequency: a straight line crossing the frequency axis at 6.0 × 10¹⁴ Hz (marked X) and extended as a dashed line to the stopping-potential axis at −2.5 V",
}

# ---------------------------------------------------------------------
# p1: work function in eV from the y-intercept. y-intercept −2.0 V.
# ---------------------------------------------------------------------
Vint_1 = -2.0
f0_1 = -Vint_1 / GRADIENT          # 4.8 (not needed by the student)
phi_1_eV = -Vint_1
record("photoelectric-graph-p1", phi_1_eV, "eV", "y-intercept %.1f V; x-intercept %.2f" % (Vint_1, f0_1))
graphs["photoelectric-graph-p1"] = {
    "x": {"label": "f / 10¹⁴ Hz", "min": 0, "max": 12, "step": 1},
    "y": {"label": "V_s / V", "min": -3, "max": 3, "step": 0.5},
    "series": photo_series(f0_1, 12, 3),
    "marks": [{"x": 0, "y": Vint_1, "label": "Y", "dx": 10, "dy": 14}],
    "alt": "Stopping potential against frequency: a straight line rising from the frequency axis at about 4.8 × 10¹⁴ Hz, extended as a dashed line to the stopping-potential axis at −2.0 V (marked Y)",
}

# ---------------------------------------------------------------------
# p2: maximum kinetic energy in eV at a marked frequency.
# Line f0 = 4.0; X at f = 10.0 where V_s = 2.5 V.
# ---------------------------------------------------------------------
f0_2 = 4.0
fX_2 = 10.0
VX_2 = line_at(f0_2, fX_2)
assert abs(VX_2 - 2.5) < 1e-9
KE_2_eV = VX_2
record("photoelectric-graph-p2", KE_2_eV, "eV", "V_s at f = 10.0 is %.2f V" % VX_2)
graphs["photoelectric-graph-p2"] = {
    "x": {"label": "f / 10¹⁴ Hz", "min": 0, "max": 12, "step": 1},
    "y": {"label": "V_s / V", "min": -2, "max": 3, "step": 0.5},
    "series": photo_series(f0_2, 12, 3),
    "marks": [{"x": fX_2, "y": round(VX_2, 4), "label": "X", "drop": True, "dx": -20, "dy": -4}],
    "alt": "Stopping potential against frequency: a straight line from the frequency axis at 4.0 × 10¹⁴ Hz rising to the right; the point X at 10.0 × 10¹⁴ Hz and 2.5 V is marked with dotted lines to both axes",
}

# ---------------------------------------------------------------------
# p3: work function in joules from the y-intercept −3.0 V.
# ---------------------------------------------------------------------
Vint_3 = -3.0
f0_3 = -Vint_3 / GRADIENT          # 7.2
phi_3_J = e * (-Vint_3)
record("photoelectric-graph-p3", phi_3_J, "J", "y-intercept %.1f V; x-intercept %.2f" % (Vint_3, f0_3))
graphs["photoelectric-graph-p3"] = {
    "x": {"label": "f / 10¹⁴ Hz", "min": 0, "max": 16, "step": 2},
    "y": {"label": "V_s / V", "min": -4, "max": 4, "step": 1},
    "series": photo_series(f0_3, 16, 4),
    "marks": [{"x": 0, "y": Vint_3, "label": "Y", "dx": 10, "dy": 14}],
    "alt": "Stopping potential against frequency: a straight line rising from the frequency axis at about 7.2 × 10¹⁴ Hz, extended as a dashed line to the stopping-potential axis at −3.0 V (marked Y)",
}

# ---------------------------------------------------------------------
# p4: Planck constant from the gradient. Line from A (4.0, 0) to
# B (16.0, 5.0): gradient = 5.0 V / (12 × 10^14 Hz).
# ---------------------------------------------------------------------
fA_4, VA_4 = 4.0, 0.0
fB_4, VB_4 = 16.0, line_at(4.0, 16.0)
assert abs(VB_4 - 5.0) < 1e-9
gradient_4 = (VB_4 - VA_4) / ((fB_4 - fA_4) * X_UNIT)   # V s
h_4 = e * gradient_4
record("photoelectric-graph-p4", h_4, "J s", "gradient = %.4g V s" % gradient_4)
graphs["photoelectric-graph-p4"] = {
    "x": {"label": "f / 10¹⁴ Hz", "min": 0, "max": 18, "step": 2},
    "y": {"label": "V_s / V", "min": 0, "max": 6, "step": 0.5},
    "series": [{"kind": "line", "points": [[fA_4, VA_4], [18, round(line_at(fA_4, 18), 4)]]}],
    "marks": [
        {"x": fA_4, "y": VA_4, "label": "A", "dx": -18, "dy": -6},
        {"x": fB_4, "y": round(VB_4, 4), "label": "B", "drop": True, "dx": 8, "dy": 16},
    ],
    "alt": "Stopping potential against frequency: a straight line from A at 4.0 × 10¹⁴ Hz on the frequency axis to B at 16.0 × 10¹⁴ Hz and 5.0 V",
}

# ---------------------------------------------------------------------
# p5: threshold wavelength from the x-intercept f0 = 8.0 (×10^14 Hz).
# ---------------------------------------------------------------------
f0_5 = 8.0
f0_5_Hz = f0_5 * X_UNIT
lambda0_5 = c / f0_5_Hz
lambda0_5_nm = lambda0_5 * 1e9
record("photoelectric-graph-p5", lambda0_5_nm, "nm", "f0 = %.3g Hz; λ0 = %.4g m" % (f0_5_Hz, lambda0_5))
graphs["photoelectric-graph-p5"] = {
    "x": {"label": "f / 10¹⁴ Hz", "min": 0, "max": 14, "step": 2},
    "y": {"label": "V_s / V", "min": -4, "max": 3, "step": 1},
    "series": photo_series(f0_5, 14, 3),
    "marks": [{"x": f0_5, "y": 0, "label": "X", "dx": 8, "dy": 18}],
    "alt": "Stopping potential against frequency: a straight line crossing the frequency axis at 8.0 × 10¹⁴ Hz (marked X), extended as a dashed line below the axis",
}

# ---------------------------------------------------------------------
# p6: two parallel lines for metals A (f0 = 5.0) and B (f0 = 7.0).
# Work function of metal B from its threshold: φ = h f0.
# ---------------------------------------------------------------------
f0_A6 = 5.0
f0_B6 = 7.0
f0_B6_Hz = f0_B6 * X_UNIT
phi_B6_J = h * f0_B6_Hz
phi_B6_eV = phi_B6_J / e
record("photoelectric-graph-p6", phi_B6_eV, "eV", "f0(B) = %.3g Hz; φ = %.4g J" % (f0_B6_Hz, phi_B6_J))
graphs["photoelectric-graph-p6"] = {
    "x": {"label": "f / 10¹⁴ Hz", "min": 0, "max": 14, "step": 1},
    "y": {"label": "V_s / V", "min": 0, "max": 3, "step": 0.5},
    "series": photo_series(f0_A6, 14, 3, with_extension=False) + photo_series(f0_B6, 14, 3, with_extension=False),
    "labels": [
        {"x": 10.2, "y": 2.7, "text": "metal A", "anchor": "end"},
        {"x": 12.6, "y": 1.9, "text": "metal B"},
    ],
    "alt": "Stopping potential against frequency: two parallel straight lines, metal A starting from the frequency axis at 5.0 × 10¹⁴ Hz and metal B from 7.0 × 10¹⁴ Hz",
}


# ---------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------
for question_id, rounded, unit, raw, notes in results:
    print("%-24s %-14r %-6s raw=%.6g  %s" % (question_id, rounded, unit, raw, notes))

if len(sys.argv) > 1:
    dump = {}
    for question_id, rounded, unit, raw, notes in results:
        value = rounded
        # Large round answers are stored as integers so they do not look unrounded
        if isinstance(value, float) and value.is_integer() and 1e5 <= abs(value) < 1e15:
            value = int(value)
        dump[question_id] = {"answer": value, "unit": unit, "graph": graphs[question_id]}
    with open(sys.argv[1], "w", encoding="utf-8") as handle:
        json.dump(dump, handle, ensure_ascii=False, indent=1)
    print("wrote", sys.argv[1])
