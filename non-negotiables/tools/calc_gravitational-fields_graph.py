#!/usr/bin/env python3
"""Compute every answer and every plotted coordinate for the graph-reading
type "gravity-graph" (Reading gravitational field and potential graphs) in
data/gravitational-fields.json.

    python3 tools/calc_gravitational-fields_graph.py            # print answers + graph specs
    python3 tools/calc_gravitational-fields_graph.py --write    # append / replace the type

Every number in the JSON type comes from this script: the answers, the
tangent end points, the sampled curve points and the marked points.
"""

import json
import math
import os
import sys

TOPIC_ID = "gravitational-fields"
TYPE_ID = "gravity-graph"
ALL_BOARDS = ["AQA", "OCR A", "OCR B", "Edexcel", "WJEC"]

G = 6.67e-11                   # N m² kg⁻² (data-sheet value)

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


def big_int(value, figures=3):
    """Round a large value to the given significant figures as an exact
    Python integer (so 1.08 × 10²⁴ is written 1080000000000000000000000)."""
    magnitude = math.floor(math.log10(abs(value)))
    shift = magnitude - (figures - 1)
    if shift < 0:
        raise ValueError("big_int is for values with at least 3 integer digits")
    mantissa = round(value / (10 ** shift))
    return int(mantissa) * (10 ** shift)


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


def sample_curve(function, starts_and_steps, x_scale=1.0, decimals=3):
    """Sample a curve at the given (start, stop, step) runs of the plotted
    x value; the function takes the x in SI (x × x_scale)."""
    points = []
    for start, stop, step in starts_and_steps:
        count = int(round((stop - start) / step))
        for index in range(count + 1):
            x_plot = start + index * step
            if points and abs(points[-1][0] - x_plot) < 1e-9:
                continue
            points.append([tidy(x_plot), tidy(function(x_plot * x_scale), decimals)])
    return points


# ----------------------------------------------------------------------
# Worked example: g at a marked altitude read from a g–r curve
# ----------------------------------------------------------------------

W_R_PLANET = 4.0e6             # m
W_GM = 1.92e14                 # N m² kg⁻¹, so surface g = 12.0 N kg⁻¹
W_ALTITUDE = 4.0e6             # m (4000 km)
W_R_X = W_R_PLANET + W_ALTITUDE          # 8.0 × 10⁶ m
W_ANSWER = W_GM / W_R_X ** 2             # (= 3.0 N kg⁻¹)


def w_field(r):
    return W_GM / r ** 2


w_points = sample_curve(w_field, [(4, 8, 0.5), (8, 16, 1.0)], x_scale=1e6)
assert [8, 3] in w_points and w_points[0] == [4, 12]

worked_graph = {
    "x": {"label": "r / 10⁶ m", "min": 0, "max": 16, "step": 2},
    "y": {"label": "g / N kg⁻¹", "min": 0, "max": 12, "step": 1},
    "series": [{"kind": "curve", "points": w_points}],
    "marks": [{"x": 8, "y": tidy(W_ANSWER), "label": "X", "drop": True}],
    "alt": "Gravitational field strength against distance from a planet's centre, falling as 1 over r squared from 12 N per kg at 4 million metres, with X marked at 8 million metres and 3.0 N per kg",
}

# ----------------------------------------------------------------------
# p1: mass of the planet from g at a marked point
# ----------------------------------------------------------------------

P1_R_PLANET = 3.0e6            # m
P1_GM = 7.2e13                 # surface g = 8.0 N kg⁻¹
P1_R_P = 6.0e6                 # m, marked point P
P1_G_P = P1_GM / P1_R_P ** 2   # (= 2.0 N kg⁻¹)
P1_ANSWER = P1_G_P * P1_R_P ** 2 / G     # kg


def p1_field(r):
    return P1_GM / r ** 2


p1_points = sample_curve(p1_field, [(3, 12, 0.5)], x_scale=1e6)
assert [6, 2] in p1_points

p1_graph = {
    "x": {"label": "r / 10⁶ m", "min": 0, "max": 12, "step": 1},
    "y": {"label": "g / N kg⁻¹", "min": 0, "max": 8, "step": 1},
    "series": [{"kind": "curve", "points": p1_points}],
    "marks": [{"x": 6, "y": tidy(P1_G_P), "label": "P", "drop": True}],
    "alt": "Gravitational field strength against distance from a planet's centre, falling from 8.0 N per kg at 3 million metres, with P marked at 6 million metres and 2.0 N per kg",
}

# ----------------------------------------------------------------------
# p2: change in potential from the area under a g–r graph
# ----------------------------------------------------------------------

P2_R_PLANET = 6.0e6            # m
P2_GM = 3.6e14                 # surface g = 10.0 N kg⁻¹
P2_R_A = 8.0e6                 # m
P2_R_B = 12.0e6                # m
P2_ANSWER = P2_GM * (1 / P2_R_A - 1 / P2_R_B)     # exact ΔV (= 1.5 × 10⁷ J kg⁻¹)
P2_SQUARE = 2.0e6 * 1.0                           # one large square: 2 × 10⁶ m × 1 N kg⁻¹
P2_SQUARES = P2_ANSWER / P2_SQUARE                # (= 7.5)
assert abs(P2_SQUARES - 7.5) < 1e-9


def p2_field(r):
    return P2_GM / r ** 2


p2_points = sample_curve(p2_field, [(6, 10, 0.5), (10, 20, 1.0)], x_scale=1e6)

p2_graph = {
    "x": {"label": "r / 10⁶ m", "min": 0, "max": 20, "step": 2},
    "y": {"label": "g / N kg⁻¹", "min": 0, "max": 10, "step": 1},
    "series": [{"kind": "curve", "points": p2_points}],
    "marks": [
        {"x": 8, "y": tidy(p2_field(P2_R_A)), "label": "A"},
        {"x": 12, "y": tidy(p2_field(P2_R_B)), "label": "B"},
    ],
    "shade": [{"series": 0, "from": 8, "to": 12}],
    "alt": "Gravitational field strength against distance from a planet's centre, falling from 10 N per kg at 6 million metres, with the area under the curve between A at 8 million metres and B at 12 million metres shaded",
}

# ----------------------------------------------------------------------
# p3: g from the gradient of a tangent to a V–r graph
# ----------------------------------------------------------------------

P3_R_PLANET = 6.0e6            # m
P3_GM = 4.8e14                 # surface V = −8.0 × 10⁷ J kg⁻¹
P3_R_X = 12.0e6                # m
P3_V_X = -P3_GM / P3_R_X       # (= −4.0 × 10⁷ J kg⁻¹)
P3_SLOPE = P3_GM / P3_R_X ** 2           # dV/dr at X in J kg⁻¹ m⁻¹ (= 3.33)
# Tangent end points on gridlines, in plotted units (x: 10⁶ m, y: 10⁷ J kg⁻¹)
P3_T1 = (0.0, (P3_V_X + P3_SLOPE * (0 - P3_R_X)) / 1e7)       # (0, −8)
P3_T2 = (18.0, (P3_V_X + P3_SLOPE * (18e6 - P3_R_X)) / 1e7)   # (18, −2)
P3_GRADIENT = ((P3_T2[1] - P3_T1[1]) * 1e7) / ((P3_T2[0] - P3_T1[0]) * 1e6)
P3_ANSWER = abs(P3_GRADIENT)
assert abs(P3_T1[1] + 8) < 1e-9 and abs(P3_T2[1] + 2) < 1e-9


def p3_potential(r):
    return -P3_GM / r / 1e7


p3_points = sample_curve(p3_potential, [(6, 10, 0.5), (10, 20, 1.0)], x_scale=1e6)
assert [12, -4] in p3_points

p3_graph = {
    "x": {"label": "r / 10⁶ m", "min": 0, "max": 20, "step": 2},
    "y": {"label": "V / 10⁷ J kg⁻¹", "min": -8, "max": 0, "step": 1},
    "series": [
        {"kind": "curve", "points": p3_points},
        {"kind": "tangent", "points": [[tidy(P3_T1[0]), tidy(P3_T1[1])], [tidy(P3_T2[0]), tidy(P3_T2[1])]]},
    ],
    "marks": [{"x": 12, "y": tidy(P3_V_X / 1e7), "label": "X", "drop": True}],
    "labels": [{"x": 3.6, "y": -6.0, "text": "tangent at X"}],
    "alt": "Gravitational potential against distance from a planet's centre, rising from minus 8 times 10 to the 7 joules per kilogram at 6 million metres towards zero, with the tangent at X (12 million metres) drawn from (0, minus 8) to (18 million metres, minus 2)",
}

# ----------------------------------------------------------------------
# p4: work done between two marked radii on a V–r graph
# ----------------------------------------------------------------------

P4_R_PLANET = 2.0e6            # m
P4_GM = 1.2e13                 # surface V = −6.0 × 10⁶ J kg⁻¹
P4_R_A = 3.0e6
P4_R_B = 6.0e6
P4_V_A = -P4_GM / P4_R_A       # (= −4.0 × 10⁶)
P4_V_B = -P4_GM / P4_R_B       # (= −2.0 × 10⁶)
P4_MASS = 500.0                # kg
P4_ANSWER = P4_MASS * (P4_V_B - P4_V_A)  # J (= 1.0 × 10⁹)


def p4_potential(r):
    return -P4_GM / r / 1e6


p4_points = sample_curve(p4_potential, [(2, 10, 0.5)], x_scale=1e6)
assert [3, -4] in p4_points and [6, -2] in p4_points

p4_graph = {
    "x": {"label": "r / 10⁶ m", "min": 0, "max": 10, "step": 1},
    "y": {"label": "V / 10⁶ J kg⁻¹", "min": -6, "max": 0, "step": 1},
    "series": [{"kind": "curve", "points": p4_points}],
    "marks": [
        {"x": 3, "y": tidy(P4_V_A / 1e6), "label": "A", "drop": True},
        {"x": 6, "y": tidy(P4_V_B / 1e6), "label": "B", "drop": True},
    ],
    "alt": "Gravitational potential against distance from a moon's centre, rising from minus 6 million joules per kilogram at 2 million metres towards zero, with A marked at 3 million metres and B at 6 million metres",
}

# ----------------------------------------------------------------------
# p5: escape speed from the surface potential read off a V–r graph
# ----------------------------------------------------------------------

P5_R_MOON = 1.0e6              # m
P5_GM = 3.0e12                 # surface V = −3.0 × 10⁶ J kg⁻¹
P5_V_S = -P5_GM / P5_R_MOON
P5_ANSWER = math.sqrt(2 * abs(P5_V_S))   # m s⁻¹ (= 2449)


def p5_potential(r):
    return -P5_GM / r / 1e6


p5_points = sample_curve(p5_potential, [(1, 4, 0.25), (4, 8, 1.0)], x_scale=1e6)
assert [1, -3] in p5_points

p5_graph = {
    "x": {"label": "r / 10⁶ m", "min": 0, "max": 8, "step": 1},
    "y": {"label": "V / 10⁶ J kg⁻¹", "min": -3, "max": 0, "step": 0.5},
    "series": [{"kind": "curve", "points": p5_points}],
    "marks": [{"x": 1, "y": tidy(P5_V_S / 1e6), "label": "S", "drop": True}],
    "alt": "Gravitational potential against distance from a small moon's centre, rising from minus 3 million joules per kilogram at the surface S (1 million metres) towards zero at large distances",
}

# ----------------------------------------------------------------------
# p6: mass of a planet from the gradient of T² against r³
# ----------------------------------------------------------------------

P6_GRADIENT_PLOT = 2.0         # T² (10⁷ s²) per r³ (10²¹ m³)
P6_GRADIENT = P6_GRADIENT_PLOT * 1e7 / 1e21       # s² m⁻³ (= 2.0 × 10⁻¹⁴)
P6_X = (8.0, 16.0)             # marked point X on the line (plot units)
P6_ANSWER = 4 * math.pi ** 2 / (G * P6_GRADIENT)   # kg
P6_R3_VALUES = [1.0, 2.0, 3.5, 5.0, 7.0, 9.0]
P6_JITTER = [0.15, -0.2, 0.1, -0.15, 0.2, -0.1]
p6_points = []
for r3, jitter in zip(P6_R3_VALUES, P6_JITTER):
    p6_points.append([tidy(r3), tidy(P6_GRADIENT_PLOT * r3 + jitter, 2)])

p6_graph = {
    "x": {"label": "r³ / 10²¹ m³", "min": 0, "max": 10, "step": 1},
    "y": {"label": "T² / 10⁷ s²", "min": 0, "max": 20, "step": 2},
    "series": [{"kind": "data", "points": p6_points, "fit": [[0, 0], [10, 20]]}],
    "marks": [{"x": tidy(P6_X[0]), "y": tidy(P6_X[1]), "label": "X", "drop": True}],
    "alt": "Data crosses of orbital period squared against orbital radius cubed for six moons, with a best-fit straight line through the origin and point X marked on it at 8 times 10 to the 21 cubic metres and 16 times 10 to the 7 seconds squared",
}

# ----------------------------------------------------------------------
# The type
# ----------------------------------------------------------------------

answers = {
    f"{TYPE_ID}-w": (sig(W_ANSWER), "N kg⁻¹"),
    f"{TYPE_ID}-p1": (big_int(P1_ANSWER), "kg"),
    f"{TYPE_ID}-p2": (big_int(P2_ANSWER), "J kg⁻¹"),
    f"{TYPE_ID}-p3": (sig(P3_ANSWER), "N kg⁻¹"),
    f"{TYPE_ID}-p4": (big_int(P4_ANSWER), "J"),
    f"{TYPE_ID}-p5": (big_int(P5_ANSWER), "m s⁻¹"),
    f"{TYPE_ID}-p6": (big_int(P6_ANSWER), "kg"),
}


def answer(question_id):
    value, unit = answers[question_id]
    return {"value": value, "unit": unit}


type_obj = {
    "id": TYPE_ID,
    "name": "Reading gravitational field and potential graphs",
    "equations": [
        "g = GM / r² (value read at a point → M = gr² / G)",
        "ΔV = area under a g–r graph",
        "g = −ΔV / Δr (gradient of a V–r graph; tangent on a curve)",
        "ΔW = mΔV",
        "v_esc = √(2GM / r) = √(2|V_surface|)",
        "T² = (4π² / GM) r³ (gradient of T² against r³ = 4π² / GM)",
    ],
    "boards": ALL_BOARDS,
    "method": "Check what is plotted and where the surface is: the curves start at the planet's radius, so add any altitude to the radius before reading r. On a g–r graph a value read at a point gives g (and M = gr² / G), and the area between two radii is the change in potential. On a V–r graph the gradient of a tangent gives g, and the difference between two readings gives ΔV for ΔW = mΔV or the escape speed. A linearised plot such as T² against r³ has gradient 4π² / GM. Multiply by the axis scales (× 10⁶ m, × 10⁷ J kg⁻¹) before calculating.",
    "commonErrors": [
        "Reading r as the altitude instead of the distance from the planet's centre",
        "Ignoring the power of ten in an axis label such as r / 10⁶ m",
        "Mishandling the minus signs on a potential axis so that ΔV comes out as a sum instead of a difference",
        "Counting squares under a curve without first working out what one square represents",
    ],
    "worked": {
        "id": f"{TYPE_ID}-w",
        "question": "The graph shows how the gravitational field strength g varies with distance r from the centre of a planet of radius 4.0 × 10⁶ m. A probe is at an altitude of 4000 km above the surface. Point X is marked. Use the graph to determine the gravitational field strength at the probe.",
        "steps": [
            "The r axis is distance from the centre, not altitude: r = R + h = 4.0 × 10⁶ + 4.0 × 10⁶ = 8.0 × 10⁶ m.",
            "The r axis is scaled in 10⁶ m, so find r = 8 on the axis and go up to the curve: this is point X.",
            "Read across to the g axis: g = 3.0 N kg⁻¹",
            "Check: g has fallen to a quarter of the surface value (12 → 3.0) when r has doubled, as expected for an inverse-square field.",
            "g = 3.0 N kg⁻¹",
        ],
        "answer": answer(f"{TYPE_ID}-w"),
        "graph": worked_graph,
    },
    "practice": [
        {
            "id": f"{TYPE_ID}-p1",
            "question": "The graph shows how the gravitational field strength g varies with distance r from the centre of a planet. Point P is marked on the curve. Use the value of g at P to determine the mass of the planet.",
            "hint": "Read r and g at P (the r axis is in 10⁶ m), then rearrange g = GM / r² to M = gr² / G.",
            "walkthrough": [
                "At P: r = 6.0 × 10⁶ m and g = 2.0 N kg⁻¹.",
                "g = GM / r², so M = gr² / G",
                "M = 2.0 × (6.0 × 10⁶)² / 6.67 × 10⁻¹¹ = 7.2 × 10¹³ / 6.67 × 10⁻¹¹",
                "M = 1.08 × 10²⁴ kg",
            ],
            "answer": answer(f"{TYPE_ID}-p1"),
            "graph": p1_graph,
        },
        {
            "id": f"{TYPE_ID}-p2",
            "question": "The graph shows how the gravitational field strength g varies with distance r from the centre of a planet. The area under the curve between A (r = 8.0 × 10⁶ m) and B (r = 12.0 × 10⁶ m) is shaded and contains 7.5 large squares. Use the graph to determine the magnitude of the change in gravitational potential between A and B.",
            "hint": "The area under a g–r graph is the change in potential; work out what one large square represents from the axis scales, remembering the r axis is in 10⁶ m.",
            "walkthrough": [
                "ΔV = area under the g–r graph between A and B.",
                "One large square is 2 × 10⁶ m wide and 1 N kg⁻¹ tall, so it represents 2 × 10⁶ × 1 = 2.0 × 10⁶ J kg⁻¹.",
                "Shaded area = 7.5 squares × 2.0 × 10⁶ J kg⁻¹",
                "ΔV = 1.5 × 10⁷ J kg⁻¹",
            ],
            "answer": answer(f"{TYPE_ID}-p2"),
            "graph": p2_graph,
        },
        {
            "id": f"{TYPE_ID}-p3",
            "question": "The graph shows how the gravitational potential V varies with distance r from the centre of a planet. The tangent to the curve at X is drawn. Use the graph to determine the gravitational field strength at X.",
            "hint": "g = −ΔV / Δr, so g at X is the magnitude of the gradient of the tangent; use its end points and include both axis scales.",
            "walkthrough": [
                "Field strength is the potential gradient: g = −ΔV / Δr, found from the tangent at X.",
                "The tangent passes through (0, −8.0 × 10⁷ J kg⁻¹) and (18 × 10⁶ m, −2.0 × 10⁷ J kg⁻¹).",
                "Gradient = (−2.0 × 10⁷ − (−8.0 × 10⁷)) / (18 × 10⁶ − 0) = 6.0 × 10⁷ / 1.8 × 10⁷",
                "g = 3.33 N kg⁻¹ (magnitude; the field points towards the planet)",
            ],
            "answer": answer(f"{TYPE_ID}-p3"),
            "graph": p3_graph,
        },
        {
            "id": f"{TYPE_ID}-p4",
            "question": "The graph shows how the gravitational potential V varies with distance r from the centre of a moon. A lander of mass 500 kg is raised from point A to point B. Use the graph to determine the work done on the lander against gravity.",
            "hint": "Read V at A and at B (the V axis is in 10⁶ J kg⁻¹), subtract to get ΔV, then ΔW = mΔV.",
            "walkthrough": [
                "V_A = −4.0 × 10⁶ J kg⁻¹ and V_B = −2.0 × 10⁶ J kg⁻¹ (read along the dotted lines).",
                "ΔV = V_B − V_A = −2.0 × 10⁶ − (−4.0 × 10⁶) = 2.0 × 10⁶ J kg⁻¹",
                "ΔW = mΔV = 500 × 2.0 × 10⁶",
                "ΔW = 1.0 × 10⁹ J",
            ],
            "answer": answer(f"{TYPE_ID}-p4"),
            "graph": p4_graph,
        },
        {
            "id": f"{TYPE_ID}-p5",
            "question": "The graph shows how the gravitational potential V varies with distance r from the centre of a small moon. Point S marks the moon's surface. Use the graph to determine the minimum speed at which an object must be launched from the surface to escape the moon's gravitational field.",
            "hint": "Read the potential at S (the axis is in 10⁶ J kg⁻¹); escaping means gaining enough kinetic energy per unit mass to reach V = 0, so ½v² = |V_S|.",
            "walkthrough": [
                "At S: V = −3.0 × 10⁶ J kg⁻¹.",
                "To escape, the kinetic energy per kilogram must equal the rise in potential to zero: ½v² = 0 − V_S = 3.0 × 10⁶ J kg⁻¹",
                "v = √(2 × 3.0 × 10⁶) = √(6.0 × 10⁶)",
                "v = 2.45 × 10³ m s⁻¹",
            ],
            "answer": answer(f"{TYPE_ID}-p5"),
            "graph": p5_graph,
        },
        {
            "id": f"{TYPE_ID}-p6",
            "question": "For six moons of a planet, the square of the orbital period T² is plotted against the cube of the orbital radius r³, and a best-fit line is drawn through the origin. Point X is marked on the line. Use the gradient of the line to determine the mass of the planet.",
            "hint": "From T² = (4π² / GM) r³ the gradient is 4π² / GM; find the gradient using X and the origin, including both axis scales, then M = 4π² / (G × gradient).",
            "walkthrough": [
                "T² = (4π² / GM) r³, so the gradient of T² against r³ is 4π² / GM.",
                "X is at r³ = 8.0 × 10²¹ m³, T² = 16 × 10⁷ s²; the line passes through the origin.",
                "Gradient = 16 × 10⁷ / 8.0 × 10²¹ = 2.0 × 10⁻¹⁴ s² m⁻³",
                "M = 4π² / (G × gradient) = 39.5 / (6.67 × 10⁻¹¹ × 2.0 × 10⁻¹⁴) = 39.5 / 1.33 × 10⁻²⁴",
                "M = 2.96 × 10²⁵ kg",
            ],
            "answer": answer(f"{TYPE_ID}-p6"),
            "graph": p6_graph,
        },
    ],
}


def main():
    for question_id, (value, unit) in answers.items():
        print(f"{question_id}: {value} {unit}")
    print(f"# p2 check: ΔV exact = {P2_ANSWER:.4g} J/kg = {P2_SQUARES} squares × {P2_SQUARE:.3g}")
    print(f"# p5 check: v_esc = {P5_ANSWER:.5g} m/s; p6 check: M = {P6_ANSWER:.5g} kg")
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
