#!/usr/bin/env python3
"""Compute every answer and every plotted coordinate for the graph-reading
type "iv-graph" (Reading I–V and V–I graphs) in data/electricity.json.

    python3 tools/calc_electricity_graph.py            # print answers + graph specs
    python3 tools/calc_electricity_graph.py --write    # append / replace the type in the data file

Every number in the JSON type comes from this script: the answers, the
line end points, the sampled curve points and the marked points.
"""

import json
import math
import os
import sys

TOPIC_ID = "electricity"
TYPE_ID = "iv-graph"
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
        # Our type is already present; it must be the last type in the list
        body = body[:position].rstrip()
        if body.endswith(","):
            body = body[:-1]
    rendered = dumps_type(type_obj, indent=2)
    new_text = body + ",\n    " + rendered + ending
    # Round-trip check: the result must parse and the type must be last
    parsed = json.loads(new_text)
    assert parsed["types"][-1]["id"] == type_obj["id"]
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(new_text)


# ----------------------------------------------------------------------
# Worked example: ohmic conductor, I–V graph, R = 1 / gradient
# ----------------------------------------------------------------------

W_R = 2.5                      # resistance of the constantan wire / Ω
W_V_MAX = 6                    # p.d. axis maximum / V
W_X_V = 5.0                    # marked point X: p.d. / V
W_X_I = W_X_V / W_R            # marked point X: current / A  (= 2.0)
W_I_END = W_V_MAX / W_R        # current at the right-hand end of the line (= 2.4)
W_GRADIENT = (W_X_I - 0) / (W_X_V - 0)
W_ANSWER = 1 / W_GRADIENT

worked_graph = {
    "x": {"label": "V / V", "min": 0, "max": W_V_MAX, "step": 1},
    "y": {"label": "I / A", "min": 0, "max": 3.0, "step": 0.5},
    "series": [
        {"kind": "line", "points": [[0, 0], [W_V_MAX, tidy(W_I_END)]]}
    ],
    "marks": [{"x": tidy(W_X_V), "y": tidy(W_X_I), "label": "X", "drop": True}],
    "alt": "Straight line through the origin on axes of current against p.d., with point X marked at 5.0 V and 2.0 A",
}

# ----------------------------------------------------------------------
# p1: ohmic conductor on a V–I graph, gradient = R
# ----------------------------------------------------------------------

P1_R = 20                      # Ω
P1_I_MAX = 0.5                 # A
P1_X_I = 0.40                  # A
P1_X_V = P1_R * P1_X_I         # V (= 8.0)
P1_V_END = P1_R * P1_I_MAX     # V (= 10)
P1_ANSWER = (P1_X_V - 0) / (P1_X_I - 0)

p1_graph = {
    "x": {"label": "I / A", "min": 0, "max": P1_I_MAX, "step": 0.1},
    "y": {"label": "V / V", "min": 0, "max": 12, "step": 2},
    "series": [
        {"kind": "line", "points": [[0, 0], [P1_I_MAX, tidy(P1_V_END)]]}
    ],
    "marks": [{"x": tidy(P1_X_I), "y": tidy(P1_X_V), "label": "X", "drop": True}],
    "alt": "Straight line through the origin on axes of p.d. against current, with point X marked at 0.40 A and 8.0 V",
}

# ----------------------------------------------------------------------
# p2: filament lamp, I–V curve, R = V / I at the marked point
# ----------------------------------------------------------------------

P2_X_V = 8.0                   # marked point X: p.d. / V
P2_X_I = 0.50                  # marked point X: current / A
# Lamp model: ohmic (linear) near the origin while the filament is cold,
# flattening towards V^0.6 as it heats: I = k V / (1 + V)^0.4, fixed through X
P2_K = P2_X_I * ((1 + P2_X_V) ** 0.4) / P2_X_V
P2_ANSWER = P2_X_V / P2_X_I


def lamp_current(v):
    """Current in the lamp at p.d. v (model curve through X)."""
    return P2_K * v / ((1 + v) ** 0.4)


p2_points = []
# Denser samples at low p.d. where the curve bends most
for v in [0, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]:
    p2_points.append([tidy(v), tidy(lamp_current(v))])
# Make sure the marked point is exactly on the plotted curve
assert [tidy(P2_X_V), tidy(P2_X_I)] in p2_points

p2_graph = {
    "x": {"label": "V / V", "min": 0, "max": 12, "step": 2},
    "y": {"label": "I / A", "min": 0, "max": 0.7, "step": 0.1},
    "series": [{"kind": "curve", "points": p2_points}],
    "marks": [{"x": tidy(P2_X_V), "y": tidy(P2_X_I), "label": "X", "drop": True}],
    "alt": "Curve of current against p.d. for a filament lamp, steep at first and flattening, with point X marked at 8.0 V and 0.50 A",
}

# ----------------------------------------------------------------------
# p3: terminal p.d.–current graph, e.m.f. from the intercept
# ----------------------------------------------------------------------

P3_EMF = 9.0                   # V
P3_R_INT = 1.5                 # Ω
P3_I_MAX = 6                   # A
P3_V_END = P3_EMF - P3_I_MAX * P3_R_INT    # (= 0)
P3_ANSWER = P3_EMF

p3_graph = {
    "x": {"label": "I / A", "min": 0, "max": P3_I_MAX, "step": 1},
    "y": {"label": "V / V", "min": 0, "max": 10, "step": 1},
    "series": [
        {"kind": "line", "points": [[0, tidy(P3_EMF)], [P3_I_MAX, tidy(P3_V_END)]]}
    ],
    "alt": "Straight line of terminal p.d. against current, falling from 9.0 V at zero current to zero at 6.0 A",
}

# ----------------------------------------------------------------------
# p4: terminal p.d.–current graph, internal resistance from the gradient
# ----------------------------------------------------------------------

P4_EMF = 7.0                   # V
P4_R_INT = 0.75                # Ω
P4_A = (0, P4_EMF)             # point A (I / A, V / V)
P4_B = (8.0, P4_EMF - 8.0 * P4_R_INT)    # point B (= (8.0, 1.0))
P4_GRADIENT = (P4_B[1] - P4_A[1]) / (P4_B[0] - P4_A[0])
P4_ANSWER = abs(P4_GRADIENT)

p4_graph = {
    "x": {"label": "I / A", "min": 0, "max": 8, "step": 1},
    "y": {"label": "V / V", "min": 0, "max": 8, "step": 1},
    "series": [
        {"kind": "line", "points": [[tidy(P4_A[0]), tidy(P4_A[1])], [tidy(P4_B[0]), tidy(P4_B[1])]]}
    ],
    "marks": [
        {"x": tidy(P4_A[0]), "y": tidy(P4_A[1]), "label": "A"},
        {"x": tidy(P4_B[0]), "y": tidy(P4_B[1]), "label": "B", "drop": True, "dx": -16, "dy": -10},
    ],
    "alt": "Straight line of terminal p.d. against current from A at 0 A and 7.0 V down to B at 8.0 A and 1.0 V",
}

# ----------------------------------------------------------------------
# p5: power delivered at a marked point, P = IV
# ----------------------------------------------------------------------

P5_EMF = 12.0                  # V
P5_R_INT = 1.5                 # Ω
P5_I_MAX = 6                   # A
P5_V_END = P5_EMF - P5_I_MAX * P5_R_INT   # (= 3.0)
P5_P_I = 4.0                   # marked point P: current / A
P5_P_V = P5_EMF - P5_P_I * P5_R_INT       # (= 6.0)
P5_ANSWER = P5_P_I * P5_P_V

p5_graph = {
    "x": {"label": "I / A", "min": 0, "max": P5_I_MAX, "step": 1},
    "y": {"label": "V / V", "min": 0, "max": 12, "step": 2},
    "series": [
        {"kind": "line", "points": [[0, tidy(P5_EMF)], [P5_I_MAX, tidy(P5_V_END)]]}
    ],
    "marks": [{"x": tidy(P5_P_I), "y": tidy(P5_P_V), "label": "P", "drop": True}],
    "alt": "Straight line of terminal p.d. against current falling from 12 V to 3.0 V at 6.0 A, with point P marked at 4.0 A and 6.0 V",
}

# ----------------------------------------------------------------------
# p6: silicon diode, current read at a marked p.d.
# ----------------------------------------------------------------------

P6_B = 0.08                    # V, controls how sharp the knee is
P6_X_V = 0.70                  # V
P6_X_I = 20.0                  # mA
P6_A = P6_X_I / (math.exp(P6_X_V / P6_B) - 1)
P6_ANSWER = P6_X_I


def diode_current(v):
    """Diode current in mA at p.d. v (Shockley-shaped curve through X)."""
    return P6_A * (math.exp(v / P6_B) - 1)


p6_points = []
for step in range(0, 17):
    v = step * 0.05
    p6_points.append([tidy(v, 2), tidy(diode_current(v), 2)])
assert [tidy(P6_X_V, 2), tidy(P6_X_I, 2)] in p6_points
assert max(point[1] for point in p6_points) <= 80

p6_graph = {
    "x": {"label": "V / V", "min": 0, "max": 0.8, "step": 0.1},
    "y": {"label": "I / mA", "min": 0, "max": 80, "step": 10},
    "series": [{"kind": "curve", "points": p6_points}],
    "marks": [{"x": tidy(P6_X_V, 2), "y": tidy(P6_X_I), "label": "X", "drop": True}],
    "alt": "Diode characteristic: current stays near zero until about 0.5 V then rises steeply, with point X marked at 0.70 V and 20 mA",
}

# ----------------------------------------------------------------------
# The type
# ----------------------------------------------------------------------

answers = {
    f"{TYPE_ID}-w": (sig(W_ANSWER), "Ω"),
    f"{TYPE_ID}-p1": (sig(P1_ANSWER), "Ω"),
    f"{TYPE_ID}-p2": (sig(P2_ANSWER), "Ω"),
    f"{TYPE_ID}-p3": (sig(P3_ANSWER), "V"),
    f"{TYPE_ID}-p4": (sig(P4_ANSWER), "Ω"),
    f"{TYPE_ID}-p5": (sig(P5_ANSWER), "W"),
    f"{TYPE_ID}-p6": (sig(P6_ANSWER), "mA"),
}


def answer(question_id):
    value, unit = answers[question_id]
    return {"value": value, "unit": unit}


type_obj = {
    "id": TYPE_ID,
    "name": "Reading I–V and V–I graphs",
    "equations": [
        "R = V / I (the ratio at a point)",
        "gradient of I–V line = 1 / R (ohmic conductor)",
        "gradient of V–I line = R (ohmic conductor)",
        "V = ε − Ir (intercept on V axis = ε, gradient = −r)",
        "P = IV",
    ],
    "boards": ALL_BOARDS,
    "method": "First check which quantity is on which axis. For an ohmic conductor the straight line through the origin has gradient 1 / R on an I–V graph and gradient R on a V–I graph. For a non-ohmic component such as a lamp or a diode, the resistance at a point is V / I using that point's coordinates — never the gradient of the curve. On a terminal p.d.–current graph the intercept on the V axis is the e.m.f. and the magnitude of the gradient is the internal resistance.",
    "commonErrors": [
        "Taking the gradient of an I–V graph as R when it is 1 / R",
        "Finding the resistance of a lamp from the gradient of a tangent instead of V / I at the point",
        "Reading the e.m.f. from the current-axis intercept instead of the p.d.-axis intercept",
        "Ignoring an axis scale in mA or kΩ",
    ],
    "worked": {
        "id": f"{TYPE_ID}-w",
        "question": "The graph shows the I–V characteristic of a length of constantan wire. Point X is marked on the line. Use the graph to determine the resistance of the wire.",
        "steps": [
            "Check the axes: current I is on the vertical axis and p.d. V on the horizontal axis, so the gradient of the line is I / V = 1 / R, not R.",
            "The line passes through the origin and through X at (5.0 V, 2.0 A).",
            "Gradient = (2.0 − 0) / (5.0 − 0) = 0.40 A V⁻¹",
            "R = 1 / gradient = 1 / 0.40",
            "R = 2.5 Ω (check: R = V / I at X = 5.0 / 2.0 = 2.5 Ω)",
        ],
        "answer": answer(f"{TYPE_ID}-w"),
        "graph": worked_graph,
    },
    "practice": [
        {
            "id": f"{TYPE_ID}-p1",
            "question": "The graph shows how the p.d. V across a carbon resistor varies with the current I in it. Point X is marked on the line. Use the graph to determine the resistance of the resistor.",
            "hint": "This time V is on the vertical axis, so the gradient of the line is V / I, which is R directly.",
            "walkthrough": [
                "V is on the vertical axis and I on the horizontal axis, so gradient = V / I = R.",
                "The line passes through the origin and X at (0.40 A, 8.0 V).",
                "R = gradient = (8.0 − 0) / (0.40 − 0)",
                "R = 20 Ω",
            ],
            "answer": answer(f"{TYPE_ID}-p1"),
            "graph": p1_graph,
        },
        {
            "id": f"{TYPE_ID}-p2",
            "question": "The graph shows the I–V characteristic of a filament lamp. Use the graph to determine the resistance of the lamp at the point marked X.",
            "hint": "For a non-ohmic component the resistance at a point is V / I using that point's coordinates, not the gradient of the curve.",
            "walkthrough": [
                "Read both coordinates of X along the dotted lines: V = 8.0 V, I = 0.50 A.",
                "The lamp is non-ohmic, so do not take a gradient: resistance is defined as R = V / I at the point.",
                "R = 8.0 / 0.50",
                "R = 16 Ω",
            ],
            "answer": answer(f"{TYPE_ID}-p2"),
            "graph": p2_graph,
        },
        {
            "id": f"{TYPE_ID}-p3",
            "question": "The graph shows how the terminal p.d. V of a battery varies with the current I it delivers. Use the graph to determine the e.m.f. of the battery.",
            "hint": "V = ε − Ir, so when I = 0 the terminal p.d. equals the e.m.f.: read the intercept on the V axis.",
            "walkthrough": [
                "V = ε − Ir. At I = 0 there are no lost volts, so V = ε.",
                "The line meets the V axis (where I = 0) at V = 9.0 V.",
                "ε = 9.0 V",
            ],
            "answer": answer(f"{TYPE_ID}-p3"),
            "graph": p3_graph,
        },
        {
            "id": f"{TYPE_ID}-p4",
            "question": "The graph shows how the terminal p.d. V across a laboratory power supply varies with the current I drawn from it. Points A and B are marked on the line. Use the graph to determine the internal resistance of the supply.",
            "hint": "Compare V = ε − Ir with y = mx + c: the gradient of the line is −r, so find the gradient between A and B and take its magnitude.",
            "walkthrough": [
                "A is at (0 A, 7.0 V) and B is at (8.0 A, 1.0 V).",
                "Gradient = (1.0 − 7.0) / (8.0 − 0) = −6.0 / 8.0 = −0.75 V A⁻¹",
                "V = ε − Ir, so gradient = −r.",
                "r = 0.75 Ω",
            ],
            "answer": answer(f"{TYPE_ID}-p4"),
            "graph": p4_graph,
        },
        {
            "id": f"{TYPE_ID}-p5",
            "question": "The graph shows how the terminal p.d. V of a battery pack varies with the current I in an external resistor connected across it. Point P is marked on the line. Use the graph to determine the power delivered to the external resistor at P.",
            "hint": "Read both the current and the terminal p.d. at P, then use P = IV.",
            "walkthrough": [
                "At P the dotted lines give I = 4.0 A and V = 6.0 V.",
                "The terminal p.d. is the p.d. across the external resistor, so P = IV.",
                "P = 4.0 × 6.0",
                "P = 24 W",
            ],
            "answer": answer(f"{TYPE_ID}-p5"),
            "graph": p5_graph,
        },
        {
            "id": f"{TYPE_ID}-p6",
            "question": "The graph shows the I–V characteristic of a silicon diode in forward bias. Point X is marked on the curve where the p.d. is 0.70 V. Use the graph to determine the current in the diode, in mA, at this p.d.",
            "hint": "Find 0.70 V on the horizontal axis, go up to the curve and read across to the current axis; note the axis is in mA.",
            "walkthrough": [
                "Locate V = 0.70 V on the horizontal axis and go up to the curve at X.",
                "Read across to the vertical axis: I = 20 mA.",
                "The current axis is scaled in mA, so I = 20 mA (= 0.020 A).",
            ],
            "answer": answer(f"{TYPE_ID}-p6"),
            "graph": p6_graph,
        },
    ],
}


def main():
    for question_id, (value, unit) in answers.items():
        print(f"{question_id}: {value} {unit}")
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
