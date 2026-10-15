#!/usr/bin/env python3
"""Compute every answer and every plotted coordinate for the graph-reading
type "flux-emf-graph" (Reading flux and induced e.m.f. graphs) in
data/magnetic-fields-induction.json.

    python3 tools/calc_magnetic-fields-induction_graph.py            # print answers + graph specs
    python3 tools/calc_magnetic-fields-induction_graph.py --write    # append / replace the type

Every number in the JSON type comes from this script: the answers, the
line and tangent end points, the sampled curve points and the marked points.
"""

import json
import math
import os
import sys

TOPIC_ID = "magnetic-fields-induction"
TYPE_ID = "flux-emf-graph"
ALL_BOARDS = ["AQA", "OCR A", "OCR B", "Edexcel", "WJEC"]
RMS_BOARDS = ["AQA", "OCR A", "OCR B", "WJEC"]     # r.m.s. values are not on the Edexcel specification

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DATA_PATH = os.path.join(ROOT, "data", f"{TOPIC_ID}.json")


# ----------------------------------------------------------------------
# Small helpers
# ----------------------------------------------------------------------

def sig(value, figures=3):
    """Round a number to the given significant figures (as a float)."""
    if value == 0:
        return 0.0
    magnitude = math.floor(math.log10(abs(value)))
    factor = 10 ** (figures - 1 - magnitude)
    return round(value * factor) / factor


def tidy(value, decimals=3):
    """Round a plotted coordinate and drop a needless .0 for integers."""
    rounded = round(value, decimals)
    if rounded == int(rounded):
        return int(rounded)
    return rounded


def dumps_type(obj, indent=0):
    """JSON with all-number arrays kept on one line (points, [x, y])."""
    pad = "  " * indent
    inner = "  " * (indent + 1)
    if isinstance(obj, dict):
        if not obj:
            return "{}"
        parts = []
        for key, value in obj.items():
            parts.append(f'{inner}{json.dumps(key)}: {dumps_type(value, indent + 1)}')
        return "{\n" + ",\n".join(parts) + "\n" + pad + "}"
    if isinstance(obj, list):
        if not obj:
            return "[]"
        all_numbers = all(isinstance(v, (int, float)) and not isinstance(v, bool) for v in obj)
        if all_numbers:
            return "[" + ", ".join(json.dumps(v) for v in obj) + "]"
        parts = [inner + dumps_type(value, indent + 1) for value in obj]
        return "[\n" + ",\n".join(parts) + "\n" + pad + "]"
    return json.dumps(obj, ensure_ascii=False)


def splice_type(path, type_obj):
    """Append the type to the data file's types list, replacing an earlier
    copy of the same type id if it is already the last type. Existing text
    is left byte-for-byte unchanged."""
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    ending = "\n  ]\n}\n"
    if not text.endswith(ending):
        raise SystemExit(f"{path}: unexpected file ending; refusing to splice")
    body = text[: -len(ending)]
    marker = f'    {{\n      "id": {json.dumps(type_obj["id"])},\n'
    position = body.rfind(marker)
    if position != -1:
        body = body[:position].rstrip()
        if body.endswith(","):
            body = body[:-1]
    rendered = dumps_type(type_obj, indent=2)
    new_text = body + ",\n    " + rendered + ending
    parsed = json.loads(new_text)
    assert parsed["types"][-1]["id"] == type_obj["id"]
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(new_text)


# ----------------------------------------------------------------------
# Worked example: e.m.f. from the gradient of a straight flux-linkage section
# ----------------------------------------------------------------------

W_A = (4.0, 0.60)              # end of the rising section: (t / s, NΦ / Wb turns)
W_T_END = 6.0                  # s, flat section runs to here
W_GRADIENT = (W_A[1] - 0) / (W_A[0] - 0)      # Wb turns s⁻¹
W_ANSWER = W_GRADIENT                         # V

worked_graph = {
    "x": {"label": "t / s", "min": 0, "max": 6, "step": 1},
    "y": {"label": "NΦ / Wb turns", "min": 0, "max": 0.8, "step": 0.1},
    "series": [{"kind": "line", "points": [[0, 0], [tidy(W_A[0]), tidy(W_A[1])], [tidy(W_T_END), tidy(W_A[1])]]}],
    "marks": [{"x": tidy(W_A[0]), "y": tidy(W_A[1]), "label": "A", "drop": True}],
    "alt": "Flux linkage against time rising in a straight line from zero to 0.60 weber turns at A (4.0 s), then constant until 6.0 s",
}

# ----------------------------------------------------------------------
# p1: e.m.f. during a marked straight section with ms and mWb scales
# ----------------------------------------------------------------------

P1_A = (0.0, 8.0)              # (t / ms, NΦ / 10⁻³ Wb turns)
P1_B = (20.0, 8.0)
P1_C = (40.0, 0.0)
P1_D = (50.0, 0.0)
P1_GRADIENT = ((P1_C[1] - P1_B[1]) * 1e-3) / ((P1_C[0] - P1_B[0]) * 1e-3)    # Wb turns s⁻¹
P1_ANSWER = abs(P1_GRADIENT)

p1_graph = {
    "x": {"label": "t / ms", "min": 0, "max": 50, "step": 5},
    "y": {"label": "NΦ / 10⁻³ Wb turns", "min": 0, "max": 10, "step": 1},
    "series": [{"kind": "line", "points": [[tidy(P1_A[0]), tidy(P1_A[1])], [tidy(P1_B[0]), tidy(P1_B[1])], [tidy(P1_C[0]), tidy(P1_C[1])], [tidy(P1_D[0]), tidy(P1_D[1])]]}],
    "marks": [
        {"x": tidy(P1_A[0]), "y": tidy(P1_A[1]), "label": "A", "dx": 9, "dy": 16},
        {"x": tidy(P1_B[0]), "y": tidy(P1_B[1]), "label": "B"},
        {"x": tidy(P1_C[0]), "y": tidy(P1_C[1]), "label": "C"},
        {"x": tidy(P1_D[0]), "y": tidy(P1_D[1]), "label": "D", "dx": -16, "dy": -10},
    ],
    "alt": "Flux linkage against time: constant at 8 milliweber turns from A to B (0 to 20 ms), falling in a straight line to zero at C (40 ms), then zero to D (50 ms)",
}

# ----------------------------------------------------------------------
# p2: change in flux linkage from the area under an e.m.f.–time graph
# ----------------------------------------------------------------------

P2_POINTS = [(0.0, 0.0), (2.0, 6.0), (6.0, 6.0), (8.0, 0.0)]    # (t / ms, ε / V): a trapezium
P2_AREA_V_MS = 0.5 * ((P2_POINTS[2][0] - P2_POINTS[1][0]) + (P2_POINTS[3][0] - P2_POINTS[0][0])) * P2_POINTS[1][1]
P2_ANSWER = P2_AREA_V_MS * 1e-3      # V s = Wb turns (= 0.036)

p2_graph = {
    "x": {"label": "t / ms", "min": 0, "max": 8, "step": 1},
    "y": {"label": "ε / V", "min": 0, "max": 8, "step": 1},
    "series": [{"kind": "line", "points": [[tidy(t), tidy(e)] for t, e in P2_POINTS]}],
    "shade": [{"series": 0, "from": 0, "to": 8}],
    "alt": "Induced e.m.f. against time forming a trapezium: rising from zero to 6.0 V at 2 ms, constant to 6 ms, falling to zero at 8 ms, with the whole area shaded",
}

# ----------------------------------------------------------------------
# p3: maximum e.m.f. from the steepest tangent on an S-shaped NΦ–t curve
# ----------------------------------------------------------------------

P3_AMPLITUDE = 6.0             # final flux linkage / 10⁻³ Wb turns
P3_T_RISE = 12.0               # ms over which the flux linkage rises (smoothstep)
P3_T_END = 16.0                # ms, flat afterwards
P3_P = (P3_T_RISE / 2, P3_AMPLITUDE / 2)              # steepest point P (6, 3)
P3_MAX_SLOPE = 1.5 * P3_AMPLITUDE / P3_T_RISE         # 10⁻³ Wb turns per ms at P (= 0.75)
# Tangent at P reaches 0 at T/6 and the full amplitude at 5T/6: gridline points
P3_T1 = (P3_T_RISE / 6, 0.0)                          # (2, 0)
P3_T2 = (5 * P3_T_RISE / 6, P3_AMPLITUDE)             # (10, 6)
P3_GRADIENT = ((P3_T2[1] - P3_T1[1]) * 1e-3) / ((P3_T2[0] - P3_T1[0]) * 1e-3)   # Wb turns s⁻¹
P3_ANSWER = P3_GRADIENT
assert abs(P3_GRADIENT - P3_MAX_SLOPE) < 1e-9


def s_curve(t_ms):
    """Flux linkage (10⁻³ Wb turns) as the magnet enters: smoothstep then flat."""
    if t_ms >= P3_T_RISE:
        return P3_AMPLITUDE
    u = t_ms / P3_T_RISE
    return P3_AMPLITUDE * (3 * u ** 2 - 2 * u ** 3)


p3_points = []
for t_ms in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16]:
    p3_points.append([tidy(t_ms), tidy(s_curve(t_ms))])
assert [6, 3] in p3_points

p3_graph = {
    "x": {"label": "t / ms", "min": 0, "max": 16, "step": 2},
    "y": {"label": "NΦ / 10⁻³ Wb turns", "min": 0, "max": 8, "step": 1},
    "series": [
        {"kind": "curve", "points": p3_points},
        {"kind": "tangent", "points": [[tidy(P3_T1[0]), tidy(P3_T1[1])], [tidy(P3_T2[0]), tidy(P3_T2[1])]]},
    ],
    "marks": [{"x": tidy(P3_P[0]), "y": tidy(P3_P[1]), "label": "P", "dx": 10, "dy": 4}],
    "labels": [{"x": 10.4, "y": 6.6, "text": "tangent at P"}],
    "alt": "S-shaped curve of flux linkage against time rising from zero to 6 milliweber turns over 12 ms then constant, with the tangent at the steepest point P drawn from (2 ms, 0) to (10 ms, 6)",
}

# ----------------------------------------------------------------------
# p4: frequency from the period of a sinusoidal current
# ----------------------------------------------------------------------

P4_I0 = 20.0                   # mA
P4_T_MS = 8.0                  # ms
P4_ANSWER = 1 / (P4_T_MS * 1e-3)         # Hz (= 125)


def p4_current(t_ms):
    return P4_I0 * math.sin(2 * math.pi * t_ms / P4_T_MS)


p4_points = []
for t_ms in range(0, 17):
    p4_points.append([tidy(t_ms), tidy(p4_current(t_ms), 2)])
assert [2, 20] in p4_points and [10, 20] in p4_points

p4_graph = {
    "x": {"label": "t / ms", "min": 0, "max": 16, "step": 2},
    "y": {"label": "I / mA", "min": -30, "max": 30, "step": 10},
    "series": [{"kind": "curve", "points": p4_points}],
    "marks": [
        {"x": 2, "y": tidy(P4_I0), "label": "P"},
        {"x": 10, "y": tidy(P4_I0), "label": "Q"},
    ],
    "alt": "Sinusoidal current of amplitude 20 mA against time, with successive positive peaks P at 2 ms and Q at 10 ms",
}

# ----------------------------------------------------------------------
# p5: e.m.f. from a flux-per-turn graph: N × gradient (two-step)
# ----------------------------------------------------------------------

P5_N = 400
P5_P = (0.10, 2.0)             # (t / s, Φ / 10⁻⁴ Wb)
P5_Q = (0.40, 8.0)
P5_GRADIENT = ((P5_Q[1] - P5_P[1]) * 1e-4) / (P5_Q[0] - P5_P[0])    # Wb s⁻¹ (= 2.0 × 10⁻³)
P5_ANSWER = P5_N * P5_GRADIENT                                     # V (= 0.80)

p5_graph = {
    "x": {"label": "t / s", "min": 0, "max": 0.5, "step": 0.05},
    "y": {"label": "Φ / 10⁻⁴ Wb", "min": 0, "max": 10, "step": 1},
    "series": [{"kind": "line", "points": [[0, tidy(P5_P[1])], [tidy(P5_P[0]), tidy(P5_P[1])], [tidy(P5_Q[0]), tidy(P5_Q[1])], [0.5, tidy(P5_Q[1])]]}],
    "marks": [
        {"x": tidy(P5_P[0]), "y": tidy(P5_P[1]), "label": "P", "drop": True},
        {"x": tidy(P5_Q[0]), "y": tidy(P5_Q[1]), "label": "Q", "drop": True},
    ],
    "alt": "Flux through one turn against time: constant at 2 times 10 to the minus 4 weber until P (0.10 s), rising in a straight line to 8 times 10 to the minus 4 weber at Q (0.40 s), then constant",
}

# ----------------------------------------------------------------------
# p6: peak voltage read from a sinusoid, then r.m.s. (two-step)
# ----------------------------------------------------------------------

P6_V0 = 6.0                    # V
P6_T_MS = 40.0                 # ms
P6_ANSWER = P6_V0 / math.sqrt(2)         # V (= 4.24)


def p6_voltage(t_ms):
    return P6_V0 * math.sin(2 * math.pi * t_ms / P6_T_MS)


p6_points = []
for step in range(0, 17):
    t_ms = 5.0 * step
    p6_points.append([tidy(t_ms), tidy(p6_voltage(t_ms), 2)])
assert [10, 6] in p6_points

p6_graph = {
    "x": {"label": "t / ms", "min": 0, "max": 80, "step": 10},
    "y": {"label": "V / V", "min": -8, "max": 8, "step": 2},
    "series": [{"kind": "curve", "points": p6_points}],
    "marks": [{"x": 10, "y": tidy(P6_V0), "label": "X", "drop": True}],
    "alt": "Sinusoidal voltage against time with period 40 ms, with the first positive peak X marked at 10 ms and 6.0 V",
}

# ----------------------------------------------------------------------
# The type
# ----------------------------------------------------------------------

answers = {
    f"{TYPE_ID}-w": (sig(W_ANSWER), "V"),
    f"{TYPE_ID}-p1": (sig(P1_ANSWER), "V"),
    f"{TYPE_ID}-p2": (sig(P2_ANSWER), "Wb turns"),
    f"{TYPE_ID}-p3": (sig(P3_ANSWER), "V"),
    f"{TYPE_ID}-p4": (sig(P4_ANSWER), "Hz"),
    f"{TYPE_ID}-p5": (sig(P5_ANSWER), "V"),
    f"{TYPE_ID}-p6": (sig(P6_ANSWER), "V"),
}


def answer(question_id):
    value, unit = answers[question_id]
    return {"value": value, "unit": unit}


type_obj = {
    "id": TYPE_ID,
    "name": "Reading flux and induced e.m.f. graphs",
    "equations": [
        "ε = N ΔΦ / Δt = gradient of a flux linkage–time graph (magnitude)",
        "ε_max = gradient of the steepest tangent",
        "ΔNΦ = area under an ε–t graph",
        "f = 1 / T",
        "V_rms = V₀ / √2",
    ],
    "boards": ALL_BOARDS,
    "method": "On a flux linkage–time graph the induced e.m.f. is the magnitude of the gradient: a straight section gives a constant e.m.f., a flat section gives zero, and a curve needs a tangent, drawn at the steepest point for the maximum e.m.f. The area under an e.m.f.–time graph is the change in flux linkage. If the graph shows the flux through one turn, multiply the gradient by the number of turns. On a sinusoidal trace read the peak where it sits on a gridline and the period between two matching points, then use f = 1 / T and V_rms = V₀ / √2.",
    "commonErrors": [
        "Leaving a time in ms or a flux in 10⁻³ Wb unconverted, so the e.m.f. is out by a factor of 10³",
        "Giving a non-zero e.m.f. for a flat section of a flux-linkage graph",
        "Reading the peak-to-peak value of a trace and using it as the peak",
        "Taking the period as the time from a positive peak to the next negative peak, which is half a period",
    ],
    "worked": {
        "id": f"{TYPE_ID}-w",
        "question": "A coil is pushed steadily into a magnetic field. The graph shows how the flux linkage NΦ of the coil varies with time t. Use the graph to determine the magnitude of the e.m.f. induced in the coil during the first 4.0 s.",
        "steps": [
            "Faraday's law: the induced e.m.f. equals the rate of change of flux linkage, which is the gradient of the NΦ–t graph.",
            "From 0 to 4.0 s the graph is a straight line from (0, 0) to A at (4.0 s, 0.60 Wb turns), so the e.m.f. is constant.",
            "Gradient = (0.60 − 0) / (4.0 − 0) = 0.15 Wb turns s⁻¹",
            "ε = 0.15 V (after 4.0 s the graph is flat, so the e.m.f. is zero)",
        ],
        "answer": answer(f"{TYPE_ID}-w"),
        "graph": worked_graph,
    },
    "practice": [
        {
            "id": f"{TYPE_ID}-p1",
            "question": "A magnet is held near a search coil and then moved away. The graph shows how the flux linkage of the coil varies with time; points A, B, C and D are marked. Use the graph to determine the magnitude of the e.m.f. induced in the coil during the section BC.",
            "hint": "The e.m.f. is the gradient of the straight section BC; convert ms to s and 10⁻³ Wb turns to Wb turns before dividing.",
            "walkthrough": [
                "B is at (20 ms, 8.0 × 10⁻³ Wb turns) and C is at (40 ms, 0).",
                "ΔNΦ = 0 − 8.0 × 10⁻³ = −8.0 × 10⁻³ Wb turns; Δt = 40 − 20 = 20 ms = 0.020 s",
                "ε = |ΔNΦ / Δt| = 8.0 × 10⁻³ / 0.020",
                "ε = 0.40 V (zero during AB and CD, where the flux linkage is constant)",
            ],
            "answer": answer(f"{TYPE_ID}-p1"),
            "graph": p1_graph,
        },
        {
            "id": f"{TYPE_ID}-p2",
            "question": "The graph shows how the e.m.f. ε induced in a coil varies with time t as the coil passes through a magnetic field. Use the shaded area to determine the total change in flux linkage of the coil during the 8.0 ms. Give your answer in Wb turns.",
            "hint": "ε = ΔNΦ / Δt, so the change in flux linkage is the area under the ε–t graph; the shape is a trapezium and the time axis is in ms.",
            "walkthrough": [
                "ΔNΦ = ε × Δt summed over the motion = area under the ε–t graph.",
                "The shaded trapezium has parallel sides of 4.0 ms (2 to 6 ms) and 8.0 ms (0 to 8 ms) and height 6.0 V.",
                "Area = ½ × (4.0 + 8.0) × 10⁻³ × 6.0 = ½ × 12 × 10⁻³ × 6.0",
                "ΔNΦ = 0.036 Wb turns",
            ],
            "answer": answer(f"{TYPE_ID}-p2"),
            "graph": p2_graph,
        },
        {
            "id": f"{TYPE_ID}-p3",
            "question": "A bar magnet is pushed into a coil and held there. The graph shows how the flux linkage of the coil varies with time. The tangent to the curve at P, where the curve is steepest, is drawn. Use the graph to determine the maximum e.m.f. induced in the coil.",
            "hint": "The e.m.f. is greatest where the flux linkage changes fastest, so find the gradient of the tangent at P from its two end points, converting ms and 10⁻³ Wb turns.",
            "walkthrough": [
                "The maximum e.m.f. is the maximum gradient, which is the gradient of the tangent at P.",
                "The tangent passes through (2.0 ms, 0) and (10.0 ms, 6.0 × 10⁻³ Wb turns).",
                "Gradient = (6.0 × 10⁻³ − 0) / ((10.0 − 2.0) × 10⁻³) = 6.0 × 10⁻³ / 8.0 × 10⁻³",
                "ε_max = 0.75 V",
            ],
            "answer": answer(f"{TYPE_ID}-p3"),
            "graph": p3_graph,
        },
        {
            "id": f"{TYPE_ID}-p4",
            "question": "The graph shows how the alternating current I in a loudspeaker coil varies with time t. Successive positive peaks P and Q are marked. Use the graph to determine the frequency of the current.",
            "hint": "The period is the time between two matching points such as P and Q (not half a cycle); convert ms to s, then f = 1 / T.",
            "walkthrough": [
                "P is at t = 2.0 ms and Q is at t = 10.0 ms, so one full cycle takes T = 10.0 − 2.0 = 8.0 ms.",
                "T = 8.0 × 10⁻³ s",
                "f = 1 / T = 1 / 8.0 × 10⁻³",
                "f = 125 Hz",
            ],
            "answer": answer(f"{TYPE_ID}-p4"),
            "graph": p4_graph,
        },
        {
            "id": f"{TYPE_ID}-p5",
            "question": "The graph shows how the magnetic flux Φ through one turn of a 400-turn coil varies with time t as the coil is moved steadily into a field. Points P and Q are marked. Use the graph to determine the e.m.f. induced in the coil between P and Q.",
            "hint": "The graph gives flux through one turn, so the e.m.f. is N times the gradient of PQ; the Φ axis is in 10⁻⁴ Wb.",
            "walkthrough": [
                "P is at (0.10 s, 2.0 × 10⁻⁴ Wb) and Q is at (0.40 s, 8.0 × 10⁻⁴ Wb).",
                "ΔΦ / Δt = (8.0 − 2.0) × 10⁻⁴ / (0.40 − 0.10) = 6.0 × 10⁻⁴ / 0.30 = 2.0 × 10⁻³ Wb s⁻¹",
                "ε = N ΔΦ / Δt = 400 × 2.0 × 10⁻³",
                "ε = 0.80 V",
            ],
            "answer": answer(f"{TYPE_ID}-p5"),
            "graph": p5_graph,
        },
        {
            "id": f"{TYPE_ID}-p6",
            "question": "The graph shows the output voltage V of a bicycle dynamo against time t. The first positive peak X is marked. Use the graph to determine the r.m.s. value of the output voltage.",
            "hint": "Read the peak voltage at X (not the peak-to-peak value), then V_rms = V₀ / √2.",
            "walkthrough": [
                "The peak voltage is read at X: V₀ = 6.0 V (the trace swings from +6.0 V to −6.0 V, so the peak is 6.0 V, not 12 V).",
                "V_rms = V₀ / √2 = 6.0 / 1.414",
                "V_rms = 4.24 V",
            ],
            "answer": answer(f"{TYPE_ID}-p6"),
            "graph": p6_graph,
            "boards": RMS_BOARDS,
        },
    ],
}


def main():
    for question_id, (value, unit) in answers.items():
        print(f"{question_id}: {value} {unit}")
    print(f"# p2 check: trapezium area = {P2_AREA_V_MS} V ms; p3 check: max slope = {P3_MAX_SLOPE} (10⁻³ Wb turns per ms)")
    if "--write" in sys.argv:
        splice_type(DATA_PATH, type_obj)
        print(f"wrote type {TYPE_ID} into {os.path.relpath(DATA_PATH, ROOT)}")
    else:
        print()
        print("graph specs:")
        for question in [type_obj["worked"]] + type_obj["practice"]:
            print(question["id"], json.dumps(question["graph"], ensure_ascii=False))


if __name__ == "__main__":
    main()
