#!/usr/bin/env python3
"""Compute every answer in data/forces-and-matter.json (Edexcel GCSE 1PH0).

Run:  python3 tools/calc_forces-and-matter.py
Prints each question id with its answer (exact whole numbers, else 3 s.f.)
and every plotted coordinate used by the force–extension graph type,
including the sampled curved sections beyond the limit of proportionality.
"""

import json

# Standard values from SCHEMA.md
G = 10  # N/kg

# Values given in the question text
RHO_WATER = 1000      # kg/m³
RHO_SEA_WATER = 1030  # kg/m³
ATMOSPHERIC_PA = 100000  # Pa

answers = []
graphs = {}


def record(question_id, value, unit):
    """Store one answer: exact when it is a whole number, else 3 s.f."""
    if abs(value - round(value)) < 1e-9:
        stored = int(round(value))
    else:
        stored = float(f"{value:.3g}")
    answers.append((question_id, stored, unit))


# ------------------------------------------------------------ Hooke's law
# F = k × x

# w: k = 25 N/m, x = 0.2 m
record("hooke-w", 25 * 0.2, "N")

# p1: k = 40 N/m, x = 0.15 m
record("hooke-p1", 40 * 0.15, "N")

# p2: k = 500 N/m, x = 0.04 m
record("hooke-p2", 500 * 0.04, "N")

# p3: 8 N stretches a spring by 16 cm → k in N/m
p3_x_m = 16 / 100
record("hooke-p3", 8 / p3_x_m, "N/m")

# p4: k = 2000 N/m, F = 30 N → x in mm
p4_x_m = 30 / 2000
record("hooke-p4", p4_x_m * 1000, "mm")

# p5: 0.6 kg mass on a spring, k = 120 N/m → extension in cm (two-step)
p5_weight = 0.6 * G
p5_x_m = p5_weight / 120
record("hooke-p5", p5_x_m * 100, "cm")

# p6: natural length 15 cm, loaded length 21 cm under 1.8 N → k (two-step)
p6_x_m = (21 - 15) / 100
record("hooke-p6", 1.8 / p6_x_m, "N/m")


# ------------------------------------------------------ elastic energy
# E = ½ × k × x²

# w: k = 200 N/m, x = 0.1 m
record("elastic-w", 0.5 * 200 * 0.1 ** 2, "J")

# p1: k = 400 N/m, x = 0.05 m
record("elastic-p1", 0.5 * 400 * 0.05 ** 2, "J")

# p2: k = 30 N/m, x = 0.4 m
record("elastic-p2", 0.5 * 30 * 0.4 ** 2, "J")

# p3: k = 150 N/m, x = 8 cm
p3_ext_m = 8 / 100
record("elastic-p3", 0.5 * 150 * p3_ext_m ** 2, "J")

# p4: k = 6000 N/m, x = 15 mm
p4_ext_m = 15 / 1000
record("elastic-p4", 0.5 * 6000 * p4_ext_m ** 2, "J")

# p5 (Higher): E = 0.9 J, k = 20 N/m → x in m
p5_x_squared = 0.9 / (0.5 * 20)
record("elastic-p5", p5_x_squared ** 0.5, "m")

# p6 (Higher): E = 0.45 J, k = 1000 N/m → x in cm
p6_x_squared = 0.45 / (0.5 * 1000)
p6_x_m = p6_x_squared ** 0.5
record("elastic-p6", p6_x_m * 100, "cm")


# ---------------------------------------------------------------- moments
# M = F × d

# w: 20 N at 0.5 m
record("moment-w", 20 * 0.5, "N m")

# p1: spanner, 50 N at 0.3 m
record("moment-p1", 50 * 0.3, "N m")

# p2: door, 8 N at 0.75 m
record("moment-p2", 8 * 0.75, "N m")

# p3: 150 N at 40 cm → N m
record("moment-p3", 150 * (40 / 100), "N m")

# p4: moment 36 N m at 0.9 m → force
record("moment-p4", 36 / 0.9, "N")

# p5: 2 kg mass at 25 cm → moment (two-step: weight, cm → m)
p5_weight_moment = 2 * G
record("moment-p5", p5_weight_moment * (25 / 100), "N m")

# p6: moment 3 N m from a 1.5 kg mass → distance in cm (two-step)
p6_weight_moment = 1.5 * G
p6_distance_m = 3 / p6_weight_moment
record("moment-p6", p6_distance_m * 100, "cm")


# ------------------------------------------------- principle of moments
# anticlockwise moment = clockwise moment

# w: 300 N at 2 m balanced by 400 N at d
record("balance-w", 300 * 2 / 400, "m")

# p1: 20 N at 0.3 m balanced by F at 0.6 m
record("balance-p1", 20 * 0.3 / 0.6, "N")

# p2: 50 N at 0.4 m balanced by 80 N at d
record("balance-p2", 50 * 0.4 / 80, "m")

# p3: 6 N at 25 cm balanced by F at 15 cm (cm cancel)
record("balance-p3", 6 * 25 / 15, "N")

# p4: 40 kg child at 1.5 m balanced by 30 kg child at d (weights first)
p4_w1 = 40 * G
p4_w2 = 30 * G
record("balance-p4", p4_w1 * 1.5 / p4_w2, "m")

# p5: 10 N at 0.2 m and 5 N at 0.6 m on one side; F at 0.5 m on the other
p5_total_moment = 10 * 0.2 + 5 * 0.6
record("balance-p5", p5_total_moment / 0.5, "N")

# p6: 300 N at 1 m and 200 N at 2 m on the left; 350 N at d on the right
p6_total_moment = 300 * 1 + 200 * 2
record("balance-p6", p6_total_moment / 350, "m")


# -------------------------------------------------- pressure on a surface
# P = F / A

# w: 600 N on 0.5 m²
record("pressure-w", 600 / 0.5, "Pa")

# p1: 200 N box on 0.4 m²
record("pressure-p1", 200 / 0.4, "Pa")

# p2: 900 N on 0.03 m²
record("pressure-p2", 900 / 0.03, "Pa")

# p3: 50 N on 20 cm² → Pa
p3_area_m2 = 20 / 10000
record("pressure-p3", 50 / p3_area_m2, "Pa")

# p4: tyre at 200 kPa on 0.015 m² → force
record("pressure-p4", 200000 * 0.015, "N")

# p5: 60 kg person on 0.04 m² → Pa (two-step: weight)
p5_person_weight = 60 * G
record("pressure-p5", p5_person_weight / 0.04, "Pa")

# p6: 4000 kg elephant on 2000 cm² → kPa (two-step: weight, cm² → m²)
p6_elephant_weight = 4000 * G
p6_area_m2 = 2000 / 10000
p6_pressure_pa = p6_elephant_weight / p6_area_m2
record("pressure-p6", p6_pressure_pa / 1000, "kPa")


# ---------------------------------------------------- pressure in a liquid
# P = h × ρ × g

# w: 3 m of water
record("liquid-w", 3 * RHO_WATER * G, "Pa")

# p1: 2 m deep pool
record("liquid-p1", 2 * RHO_WATER * G, "Pa")

# p2: 50 m of sea water
record("liquid-p2", 50 * RHO_SEA_WATER * G, "Pa")

# p3: 0.5 m of a liquid gives 4500 Pa → ρ
record("liquid-p3", 4500 / (0.5 * G), "kg/m³")

# p4: 120 kPa due to water → depth
record("liquid-p4", 120000 / (RHO_WATER * G), "m")

# p5: diver at 15 m in water, plus atmospheric 100 kPa → total in kPa
p5_water_pa = 15 * RHO_WATER * G
record("liquid-p5", (p5_water_pa + ATMOSPHERIC_PA) / 1000, "kPa")

# p6: hatch 0.5 m² at 40 m in sea water → force (two-step)
p6_hatch_pa = 40 * RHO_SEA_WATER * G
record("liquid-p6", p6_hatch_pa * 0.5, "N")


# ------------------------------------------- reading force–extension graphs
# Extension axes in cm (or mm); force in N. Points on gridline intersections.

def sample_curve(x_start, f_start, slope, bend, x_end, count):
    """Sample a gently bending curve beyond the limit of proportionality.

    F = f_start + slope × u − bend × u² where u = x − x_start, so it leaves
    the straight line smoothly and then bends toward the extension axis.
    Returns points rounded to 2 d.p.
    """
    points = []
    for index in range(count + 1):
        u = (x_end - x_start) * index / count
        force = f_start + slope * u - bend * u * u
        points.append([round(x_start + u, 2), round(force, 2)])
    return points


# w: straight to P(8 cm, 16 N), then curves; k from gradient
w_line = [[0, 0], [8, 16]]
w_curve = sample_curve(8, 16, 2, 0.4, 10, 8)
graphs["fx-graph-w"] = {"line": w_line, "curve": w_curve}
w_k = 16 / (8 / 100)
record("fx-graph-w", w_k, "N/m")

# p1: straight line, read extension at A where force = 3 N
p1_line = [[0, 0], [12, 6]]
p1_gradient = 6 / 12
p1_extension = 3 / p1_gradient
graphs["fx-graph-p1"] = {"line": p1_line, "mark": [p1_extension, 3]}
record("fx-graph-p1", p1_extension, "cm")

# p2: straight to L(6 cm, 12 N), then curves; force at the limit
p2_line = [[0, 0], [6, 12]]
p2_curve = sample_curve(6, 12, 2, 0.2, 10, 8)
graphs["fx-graph-p2"] = {"line": p2_line, "curve": p2_curve}
record("fx-graph-p2", 12, "N")

# p3: straight (0,0)→(10 cm, 8 N); energy = area of triangle
p3_line = [[0, 0], [10, 8]]
p3_energy = 0.5 * (10 / 100) * 8
graphs["fx-graph-p3"] = {"line": p3_line}
record("fx-graph-p3", p3_energy, "J")

# p4: straight (0,0)→(40 mm, 10 N); k from gradient with mm → m
p4_line = [[0, 0], [40, 10]]
p4_k = 10 / (40 / 1000)
graphs["fx-graph-p4"] = {"line": p4_line}
record("fx-graph-p4", p4_k, "N/m")

# p5: straight (0,0)→(8 cm, 12 N), X at (6 cm, 9 N); energy up to X
p5_line = [[0, 0], [8, 12]]
p5_x_cm = 6
p5_force = (12 / 8) * p5_x_cm
p5_energy = 0.5 * (p5_x_cm / 100) * p5_force
graphs["fx-graph-p5"] = {"line": p5_line, "mark": [p5_x_cm, p5_force]}
record("fx-graph-p5", p5_energy, "J")

# p6: straight (0,0)→(10 cm, 5 N); B at 8 cm; force then mass (two-step)
p6_line = [[0, 0], [10, 5]]
p6_force = (5 / 10) * 8
p6_mass = p6_force / G
graphs["fx-graph-p6"] = {"line": p6_line, "mark": [8, p6_force]}
record("fx-graph-p6", p6_mass, "kg")


# ------------------------------------------------------------------ output
for question_id, value, unit in answers:
    print(f"{question_id:16s} {value!r:>10}  {unit}")

print()
print("Graph points:")
for question_id, parts in graphs.items():
    print(f"{question_id:16s} {json.dumps(parts)}")
