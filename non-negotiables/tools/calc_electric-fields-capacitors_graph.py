#!/usr/bin/env python3
"""Compute every answer and every plotted coordinate for the graph-reading
type "field-capacitor-graph" (Reading field, potential and capacitor graphs)
in data/electric-fields-capacitors.json.

    python3 tools/calc_electric-fields-capacitors_graph.py            # print answers + graph specs
    python3 tools/calc_electric-fields-capacitors_graph.py --write    # append / replace the type

Every number in the JSON type comes from this script: the answers, the
tangent end points, the sampled curve points and the marked points.
"""

import json
import math
import os
import sys

TOPIC_ID = "electric-fields-capacitors"
TYPE_ID = "field-capacitor-graph"
ALL_BOARDS = ["AQA", "OCR A", "OCR B", "Edexcel", "WJEC"]

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
# Worked example: E from the tangent to a V–r curve (charged sphere)
# ----------------------------------------------------------------------

W_KQ = 36.0                    # kQ = Q / 4πε₀ in V m, so V = 36 / r (r in m)
W_R_MIN_CM = 2.0               # the sphere's radius: the curve starts here
W_X_R_CM = 3.0                 # marked point X: r / cm
W_X_V = W_KQ / (W_X_R_CM / 100)             # V at X (= 1200 V)
W_SLOPE_V_PER_CM = -W_KQ / ((W_X_R_CM / 100) ** 2) / 100   # dV/dr at X in V cm⁻¹ (= −400)
# Tangent end points, chosen on gridline intersections
W_T1 = (1.0, W_X_V + W_SLOPE_V_PER_CM * (1.0 - W_X_R_CM))   # (1, 2000)
W_T2 = (6.0, W_X_V + W_SLOPE_V_PER_CM * (6.0 - W_X_R_CM))   # (6, 0)
W_GRADIENT_V_PER_M = (W_T2[1] - W_T1[1]) / ((W_T2[0] - W_T1[0]) / 100)
W_ANSWER = abs(W_GRADIENT_V_PER_M)


def sphere_potential(r_cm):
    """Potential in V at r cm from the centre of the sphere."""
    return W_KQ / (r_cm / 100)


w_points = []
for step in range(0, 17):
    r_cm = W_R_MIN_CM + 0.5 * step
    w_points.append([tidy(r_cm), tidy(sphere_potential(r_cm))])
assert [tidy(W_X_R_CM), tidy(W_X_V)] in w_points
assert tidy(W_T1[1]) == 2000 and tidy(W_T2[1]) == 0

worked_graph = {
    "x": {"label": "r / cm", "min": 0, "max": 10, "step": 1},
    "y": {"label": "V / V", "min": 0, "max": 2000, "step": 200},
    "series": [
        {"kind": "curve", "points": w_points},
        {"kind": "tangent", "points": [[tidy(W_T1[0]), tidy(W_T1[1])], [tidy(W_T2[0]), tidy(W_T2[1])]]},
    ],
    "marks": [{"x": tidy(W_X_R_CM), "y": tidy(W_X_V), "label": "X", "drop": True}],
    "labels": [{"x": 4.2, "y": 1300, "text": "tangent at X"}],
    "alt": "Potential against distance from a charged sphere, falling as 1 over r from 1800 V at 2 cm to 360 V at 10 cm, with the tangent at X (3 cm, 1200 V) drawn from (1 cm, 2000 V) to (6 cm, 0)",
}

# ----------------------------------------------------------------------
# p1: capacitance from the gradient of a Q–V graph
# ----------------------------------------------------------------------

P1_C = 150e-6                  # F
P1_V_MAX = 12                  # V
P1_X_V = 10.0                  # V
P1_X_Q_MC = P1_C * P1_X_V * 1e3          # mC (= 1.5)
P1_Q_END_MC = P1_C * P1_V_MAX * 1e3      # mC (= 1.8)
P1_GRADIENT_F = (P1_X_Q_MC * 1e-3) / P1_X_V
P1_ANSWER_UF = P1_GRADIENT_F * 1e6

p1_graph = {
    "x": {"label": "V / V", "min": 0, "max": P1_V_MAX, "step": 2},
    "y": {"label": "Q / mC", "min": 0, "max": 2.0, "step": 0.5},
    "series": [{"kind": "line", "points": [[0, 0], [P1_V_MAX, tidy(P1_Q_END_MC)]]}],
    "marks": [{"x": tidy(P1_X_V), "y": tidy(P1_X_Q_MC), "label": "X", "drop": True}],
    "alt": "Straight line through the origin of charge in mC against p.d., with point X marked at 10 V and 1.5 mC",
}

# ----------------------------------------------------------------------
# p2: energy stored from the area under a V–Q graph
# ----------------------------------------------------------------------

P2_C = 5e-6                    # F (V = Q / C gives the line)
P2_Q_MAX_UC = 60               # μC axis maximum
P2_P_Q_UC = 50.0               # marked point P: charge / μC
P2_P_V = (P2_P_Q_UC * 1e-6) / P2_C       # p.d. at P (= 10 V)
P2_V_END = (P2_Q_MAX_UC * 1e-6) / P2_C   # (= 12 V)
P2_ANSWER = 0.5 * (P2_P_Q_UC * 1e-6) * P2_P_V   # triangle area = ½QV

p2_graph = {
    "x": {"label": "Q / μC", "min": 0, "max": P2_Q_MAX_UC, "step": 10},
    "y": {"label": "V / V", "min": 0, "max": 12, "step": 2},
    "series": [{"kind": "line", "points": [[0, 0], [P2_Q_MAX_UC, tidy(P2_V_END)]]}],
    "marks": [{"x": tidy(P2_P_Q_UC), "y": tidy(P2_P_V), "label": "P", "drop": True}],
    "shade": [{"series": 0, "from": 0, "to": tidy(P2_P_Q_UC)}],
    "alt": "Straight line through the origin of p.d. against charge in μC, with the triangle under the line up to P (50 μC, 10 V) shaded",
}

# ----------------------------------------------------------------------
# p3: p.d. between two radii from the area under an E–r graph
# ----------------------------------------------------------------------

P3_KQ = 90.0                   # V m, so E = 90 / r² (V m⁻¹)
P3_R_MIN = 0.10                # m, the dome's radius: the curve starts here
P3_R_A = 0.20                  # m
P3_R_B = 0.40                  # m
P3_ANSWER = P3_KQ * (1 / P3_R_A - 1 / P3_R_B)          # exact ΔV (= 225 V)
P3_SQUARE_V = 0.05 * 1000.0                           # one large square: 0.05 m × 1 kV m⁻¹ = 50 V
P3_SQUARES = P3_ANSWER / P3_SQUARE_V                  # (= 4.5)
assert abs(P3_SQUARES - 4.5) < 1e-9


def dome_field_kv(r):
    """Field strength in kV m⁻¹ at distance r (m) from the dome's centre."""
    return P3_KQ / (r ** 2) / 1000.0


p3_points = []
for step in range(0, 17):
    r = P3_R_MIN + 0.025 * step
    p3_points.append([tidy(r, 3), tidy(dome_field_kv(r), 3)])
assert p3_points[0] == [0.1, 9] and p3_points[-1][0] == 0.5

p3_graph = {
    "x": {"label": "r / m", "min": 0, "max": 0.5, "step": 0.05},
    "y": {"label": "E / kV m⁻¹", "min": 0, "max": 10, "step": 1},
    "series": [{"kind": "curve", "points": p3_points}],
    "marks": [
        {"x": tidy(P3_R_A), "y": tidy(dome_field_kv(P3_R_A), 3), "label": "A"},
        {"x": tidy(P3_R_B), "y": tidy(dome_field_kv(P3_R_B), 3), "label": "B"},
    ],
    "shade": [{"series": 0, "from": tidy(P3_R_A), "to": tidy(P3_R_B)}],
    "alt": "Field strength in kV per metre against distance from a charged dome, falling as 1 over r squared from 9 kV per metre at 0.10 m, with the area between r = 0.20 m and r = 0.40 m shaded",
}

# ----------------------------------------------------------------------
# p4: time constant from a V–t discharge curve (V = 0.37 V₀)
# ----------------------------------------------------------------------

P4_V0 = 2.7                    # V (a 2.7 V supercapacitor)
P4_TAU = 20.0                  # s
P4_V_AT_TAU = P4_V0 * math.exp(-1)        # (= 0.993 V, read as 1.0 V = 0.37 V₀)
P4_READ_V = 1.0                # the gridline value the question quotes for 0.37 V₀
P4_ANSWER = P4_TAU
assert abs(0.37 * P4_V0 - P4_READ_V) < 0.01


def supercap_voltage(t):
    """P.d. across the supercapacitor at time t."""
    return P4_V0 * math.exp(-t / P4_TAU)


p4_points = []
for step in range(0, 16):
    t = 4.0 * step
    p4_points.append([tidy(t), tidy(supercap_voltage(t), 3)])
assert p4_points[5][0] == 20

p4_graph = {
    "x": {"label": "t / s", "min": 0, "max": 60, "step": 10},
    "y": {"label": "V / V", "min": 0, "max": 3.0, "step": 0.5},
    "series": [{"kind": "curve", "points": p4_points}],
    "marks": [{"x": tidy(P4_TAU), "y": tidy(P4_READ_V), "label": "X", "drop": True}],
    "alt": "Exponential decay of p.d. from 2.7 V towards zero over 60 s, with point X marked where the p.d. has fallen to 1.0 V at 20 s",
}

# ----------------------------------------------------------------------
# p5: initial discharge current from the tangent at t = 0 on a Q–t graph
# ----------------------------------------------------------------------

P5_Q0_UC = 600.0               # μC
P5_TAU = 30.0                  # s
# The tangent at t = 0 has gradient −Q₀/τ and so reaches Q = 0 at t = τ
P5_T1 = (0.0, P5_Q0_UC)
P5_T2 = (P5_TAU, 0.0)
P5_GRADIENT_UC_PER_S = (P5_T2[1] - P5_T1[1]) / (P5_T2[0] - P5_T1[0])
P5_ANSWER_UA = abs(P5_GRADIENT_UC_PER_S)   # μC s⁻¹ = μA


def discharge_charge(t):
    """Charge in μC on the capacitor at time t."""
    return P5_Q0_UC * math.exp(-t / P5_TAU)


p5_points = []
for step in range(0, 16):
    t = 4.0 * step
    p5_points.append([tidy(t), tidy(discharge_charge(t), 1)])

p5_graph = {
    "x": {"label": "t / s", "min": 0, "max": 60, "step": 10},
    "y": {"label": "Q / μC", "min": 0, "max": 600, "step": 100},
    "series": [
        {"kind": "curve", "points": p5_points},
        {"kind": "tangent", "points": [[tidy(P5_T1[0]), tidy(P5_T1[1])], [tidy(P5_T2[0]), tidy(P5_T2[1])]]},
    ],
    "marks": [{"x": 0, "y": tidy(P5_Q0_UC), "label": "X"}],
    "labels": [{"x": 16, "y": 380, "text": "tangent at X"}],
    "alt": "Exponential decay of charge in μC from 600 μC at t = 0, with the tangent at t = 0 drawn from (0, 600 μC) down to (30 s, 0)",
}

# ----------------------------------------------------------------------
# p6: ln V against t: gradient → RC, then R from C
# ----------------------------------------------------------------------

P6_C = 1000e-6                 # F
P6_A = (0.0, 2.5)              # best-fit line end points on gridlines
P6_B = (100.0, 0.5)
P6_GRADIENT = (P6_B[1] - P6_A[1]) / (P6_B[0] - P6_A[0])   # s⁻¹ (= −0.020)
P6_TAU = -1 / P6_GRADIENT                                  # s (= 50)
P6_R = P6_TAU / P6_C                                       # Ω (= 50 000)
P6_ANSWER_KOHM = P6_R / 1e3
# Small deterministic scatter so the crosses look like readings; the
# best-fit line, not the crosses, defines the answer
P6_JITTER = [0.02, -0.03, 0.01, 0.03, -0.02, 0.0, 0.02, -0.03, 0.01, -0.01, 0.02]
p6_points = []
for index, jitter in enumerate(P6_JITTER):
    t = 10.0 * index
    ln_v = P6_A[1] + P6_GRADIENT * t + jitter
    p6_points.append([tidy(t), tidy(ln_v, 2)])

p6_graph = {
    "x": {"label": "t / s", "min": 0, "max": 100, "step": 10},
    "y": {"label": "ln (V / V)", "min": 0, "max": 3.0, "step": 0.5},
    "series": [
        {"kind": "data", "points": p6_points, "fit": [[tidy(P6_A[0]), tidy(P6_A[1])], [tidy(P6_B[0]), tidy(P6_B[1])]]}
    ],
    "marks": [
        {"x": tidy(P6_A[0]), "y": tidy(P6_A[1]), "label": "A"},
        {"x": tidy(P6_B[0]), "y": tidy(P6_B[1]), "label": "B", "drop": True, "dx": -16, "dy": -10},
    ],
    "alt": "Data crosses of ln V against time with a straight best-fit line from A (0, 2.5) to B (100 s, 0.5)",
}

# ----------------------------------------------------------------------
# The type
# ----------------------------------------------------------------------

answers = {
    f"{TYPE_ID}-w": (int(sig(W_ANSWER)), "V m⁻¹"),
    f"{TYPE_ID}-p1": (sig(P1_ANSWER_UF), "μF"),
    f"{TYPE_ID}-p2": (sig(P2_ANSWER), "J"),
    f"{TYPE_ID}-p3": (sig(P3_ANSWER), "V"),
    f"{TYPE_ID}-p4": (sig(P4_ANSWER), "s"),
    f"{TYPE_ID}-p5": (sig(P5_ANSWER_UA), "μA"),
    f"{TYPE_ID}-p6": (sig(P6_ANSWER_KOHM), "kΩ"),
}


def answer(question_id):
    value, unit = answers[question_id]
    return {"value": value, "unit": unit}


type_obj = {
    "id": TYPE_ID,
    "name": "Reading field, potential and capacitor graphs",
    "equations": [
        "E = −ΔV / Δr (gradient of a V–r graph; tangent on a curve)",
        "ΔV = area under an E–r graph",
        "W = ½QV = area under a V–Q graph",
        "C = Q / V = gradient of a Q–V graph",
        "V = V₀e^(−t/RC): V = 0.37 V₀ when t = RC",
        "ln V = ln V₀ − t / RC (gradient = −1 / RC)",
        "I = −ΔQ / Δt (gradient of a Q–t graph)",
    ],
    "boards": ALL_BOARDS,
    "method": "Decide what the gradient and the area of the graph mean before reading anything. Potential against distance: the gradient (of a tangent, on a curve) gives the field strength. Field strength against distance: the area gives the p.d. For a capacitor, the area under a V–Q graph is the energy stored and the gradient of a Q–V graph is the capacitance. On discharge curves the time constant RC is the time for V or Q to fall to 0.37 of its starting value, the tangent at t = 0 has gradient −Q₀ / RC, and ln V against t is a straight line of gradient −1 / RC. Convert axis scales (cm, μC, kV m⁻¹) to SI before quoting the answer.",
    "commonErrors": [
        "Reading a gradient in V cm⁻¹ and forgetting to convert it to V m⁻¹",
        "Using the whole area under a V–Q graph instead of the triangle up to the final charge, or forgetting the ½",
        "Taking the time constant as the time for V to fall to half of V₀ (that is 0.69 RC, not RC)",
        "Quoting the gradient of ln V against t as RC instead of −1 / RC",
    ],
    "worked": {
        "id": f"{TYPE_ID}-w",
        "question": "The graph shows how the electric potential V varies with distance r from the centre of a charged metal sphere of radius 2.0 cm. The tangent to the curve at X is drawn. Use the graph to determine the magnitude of the electric field strength at X.",
        "steps": [
            "Field strength is the potential gradient: E = −ΔV / Δr, so E at X is the gradient of the tangent at X.",
            "The tangent passes through (1.0 cm, 2000 V) and (6.0 cm, 0 V).",
            "Gradient = (0 − 2000) / (6.0 − 1.0) = −400 V cm⁻¹",
            "Convert: 1 cm = 0.010 m, so gradient = −400 / 0.010 = −4.0 × 10⁴ V m⁻¹",
            "E = 4.0 × 10⁴ V m⁻¹ (magnitude; the field points outwards, down the potential slope)",
        ],
        "answer": answer(f"{TYPE_ID}-w"),
        "graph": worked_graph,
    },
    "practice": [
        {
            "id": f"{TYPE_ID}-p1",
            "question": "The graph shows how the charge Q stored on a capacitor varies with the p.d. V across it. Point X is marked on the line. Use the graph to determine the capacitance of the capacitor in μF.",
            "hint": "C = Q / V, so the gradient of a Q–V line through the origin is the capacitance; the charge axis is in mC.",
            "walkthrough": [
                "The line passes through the origin and X at (10 V, 1.5 mC).",
                "Gradient = Q / V = 1.5 × 10⁻³ / 10 = 1.5 × 10⁻⁴ F",
                "C = 1.5 × 10⁻⁴ F = 150 μF",
            ],
            "answer": answer(f"{TYPE_ID}-p1"),
            "graph": p1_graph,
        },
        {
            "id": f"{TYPE_ID}-p2",
            "question": "The graph shows how the p.d. V across a capacitor in a camera flash unit varies with the charge Q stored on it. Use the shaded area to determine the energy stored in the capacitor when it holds the charge at point P. Give your answer in J.",
            "hint": "The energy stored is the area under the V–Q line, which is a triangle: ½ × base × height, with the charge converted from μC to C.",
            "walkthrough": [
                "At P: Q = 50 μC = 50 × 10⁻⁶ C and V = 10 V.",
                "Energy stored = area of the shaded triangle = ½ × Q × V",
                "W = ½ × 50 × 10⁻⁶ × 10",
                "W = 2.5 × 10⁻⁴ J",
            ],
            "answer": answer(f"{TYPE_ID}-p2"),
            "graph": p2_graph,
        },
        {
            "id": f"{TYPE_ID}-p3",
            "question": "The graph shows how the electric field strength E varies with distance r from the centre of the charged dome of a Van de Graaff generator. The area under the curve between A (r = 0.20 m) and B (r = 0.40 m) is shaded and contains 4.5 large squares. Use the graph to determine the potential difference between A and B.",
            "hint": "The area under an E–r graph is the p.d.; work out what one large square represents from the axis scales, remembering the E axis is in kV m⁻¹.",
            "walkthrough": [
                "P.d. = area under the E–r graph between A and B.",
                "One large square is 0.05 m wide and 1 kV m⁻¹ = 1000 V m⁻¹ tall, so it represents 0.05 × 1000 = 50 V.",
                "Shaded area = 4.5 squares × 50 V",
                "ΔV = 225 V",
            ],
            "answer": answer(f"{TYPE_ID}-p3"),
            "graph": p3_graph,
        },
        {
            "id": f"{TYPE_ID}-p4",
            "question": "A 2.7 V supercapacitor discharges through a resistor. The graph shows how the p.d. V across it varies with time t. Point X is marked where the p.d. has fallen to 0.37 of its initial value. Use the graph to determine the time constant of the circuit.",
            "hint": "After one time constant the p.d. has fallen to V₀ / e = 0.37 V₀; read the time at which V reaches that value.",
            "walkthrough": [
                "V₀ = 2.7 V, so 0.37 V₀ = 0.37 × 2.7 = 1.0 V.",
                "Point X is where V = 1.0 V; read down to the time axis: t = 20 s.",
                "After one time constant V = V₀e⁻¹ = 0.37 V₀, so RC = 20 s",
            ],
            "answer": answer(f"{TYPE_ID}-p4"),
            "graph": p4_graph,
        },
        {
            "id": f"{TYPE_ID}-p5",
            "question": "The graph shows how the charge Q on a capacitor varies with time t as it discharges through a resistor in a timing circuit. The tangent to the curve at X, where t = 0, is drawn. Use the graph to determine the initial discharge current in μA.",
            "hint": "Current is the rate of change of charge, I = −ΔQ / Δt, so the magnitude of the gradient of the tangent at t = 0 is the initial current; μC per second is μA.",
            "walkthrough": [
                "The tangent at X passes through (0 s, 600 μC) and (30 s, 0 μC).",
                "Gradient = (0 − 600) / (30 − 0) = −20 μC s⁻¹",
                "I = −ΔQ / Δt = 20 μC s⁻¹",
                "I₀ = 20 μA",
            ],
            "answer": answer(f"{TYPE_ID}-p5"),
            "graph": p5_graph,
        },
        {
            "id": f"{TYPE_ID}-p6",
            "question": "A 1000 μF capacitor discharges through a resistor. The graph shows ln V plotted against time t, where V is the p.d. across the capacitor, with the best-fit line drawn through A and B. Use the graph to determine the resistance of the resistor in kΩ.",
            "hint": "Taking logs of V = V₀e^(−t/RC) gives ln V = ln V₀ − t / RC, so the gradient is −1 / RC; find RC, then divide by C in farads.",
            "walkthrough": [
                "ln V = ln V₀ − t / RC, so the gradient of the line is −1 / RC.",
                "Gradient = (0.5 − 2.5) / (100 − 0) = −2.0 / 100 = −0.020 s⁻¹",
                "RC = −1 / gradient = 1 / 0.020 = 50 s",
                "R = RC / C = 50 / (1000 × 10⁻⁶) = 5.0 × 10⁴ Ω",
                "R = 50 kΩ",
            ],
            "answer": answer(f"{TYPE_ID}-p6"),
            "graph": p6_graph,
        },
    ],
}


def main():
    for question_id, (value, unit) in answers.items():
        print(f"{question_id}: {value} {unit}")
    print(f"# p3 check: ΔV exact = {P3_ANSWER} V = {P3_SQUARES} squares × {P3_SQUARE_V} V")
    print(f"# p4 check: V at t = RC is {P4_V_AT_TAU:.3f} V, quoted as {P4_READ_V} V")
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
