#!/usr/bin/env python3
"""Compute every answer in data/energy.json from the question data.

Usage: python3 tools/calc_energy.py

Prints each answer (3 s.f.) with its question id, prints the plotted
coordinates for every graph question, and, when the topic file exists,
reports any stored answer that disagrees with the computed one.
"""

import json
import math
import os
import sys

# Standard value from SCHEMA.md
G = 10  # N/kg


def sig3(value):
    """Round a number to three significant figures (exact values pass through)."""
    if value == 0:
        return 0
    magnitude = math.floor(math.log10(abs(value)))
    factor = 10 ** (2 - magnitude)
    rounded = round(value * factor) / factor
    # Return an int when the value is a whole number, so JSON stays tidy
    if abs(rounded - round(rounded)) < 1e-9:
        return int(round(rounded))
    return rounded


answers = {}
graphs = {}


def record(question_id, value, unit):
    """Store one computed answer."""
    answers[question_id] = (sig3(value), unit)


# ---------------------------------------------------------------------------
# Type 1: kinetic-energy   KE = ½ × m × v²
# ---------------------------------------------------------------------------

# w: 60 kg runner at 8 m/s
record("kinetic-energy-w", 0.5 * 60 * 8 ** 2, "J")

# p1: 1000 kg car at 20 m/s
record("kinetic-energy-p1", 0.5 * 1000 * 20 ** 2, "J")

# p2: 0.16 kg cricket ball at 30 m/s
record("kinetic-energy-p2", 0.5 * 0.16 * 30 ** 2, "J")

# p3: 1500 kg van at 72 km/h; answer in kJ
speed_van = 72 * 1000 / 3600
ke_van_j = 0.5 * 1500 * speed_van ** 2
record("kinetic-energy-p3", ke_van_j / 1000, "kJ")

# p4: 250 g ball at 12 m/s
mass_ball = 250 / 1000
record("kinetic-energy-p4", 0.5 * mass_ball * 12 ** 2, "J")

# p5 (Higher): 80 kg cyclist with KE 2560 J; find v
v_squared_p5 = 2 * 2560 / 80
record("kinetic-energy-p5", math.sqrt(v_squared_p5), "m/s")

# p6 (Higher): 20000 kg lorry with KE 2500 kJ; find v
ke_lorry_j = 2500 * 1000
v_squared_p6 = 2 * ke_lorry_j / 20000
record("kinetic-energy-p6", math.sqrt(v_squared_p6), "m/s")

# ---------------------------------------------------------------------------
# Type 2: gravitational-potential-energy   GPE = m × g × h
# ---------------------------------------------------------------------------

# w: 50 kg climber up 12 m
record("gravitational-potential-energy-w", 50 * G * 12, "J")

# p1: 2 kg book lifted 1.5 m
record("gravitational-potential-energy-p1", 2 * G * 1.5, "J")

# p2: 800 kg lift car rises 20 m
record("gravitational-potential-energy-p2", 800 * G * 20, "J")

# p3: 60 kg person gains 9000 J; find h
record("gravitational-potential-energy-p3", 9000 / (60 * G), "m")

# p4: crane load gains 45 kJ over 15 m; find m
gpe_crane_j = 45 * 1000
record("gravitational-potential-energy-p4", gpe_crane_j / (G * 15), "kg")

# p5: box weighing 150 N lifted 2.4 m
mass_box = 150 / G
record("gravitational-potential-energy-p5", mass_box * G * 2.4, "J")

# p6: 70 kg hiker climbs 500 steps each 20 cm; answer in kJ
height_steps = 500 * 20 / 100
gpe_hiker_j = 70 * G * height_steps
record("gravitational-potential-energy-p6", gpe_hiker_j / 1000, "kJ")

# ---------------------------------------------------------------------------
# Type 3: work-done   W = F × d
# ---------------------------------------------------------------------------

# w: 40 N push over 5 m
record("work-done-w", 40 * 5, "J")

# p1: horse pulls cart with 600 N for 50 m
record("work-done-p1", 600 * 50, "J")

# p2: suitcase lifted with 120 N through 3 m
record("work-done-p2", 120 * 3, "J")

# p3: 4500 J of work over 30 m; find F
record("work-done-p3", 4500 / 30, "N")

# p4: 2.5 kJ of work with 20 N; find d
work_p4_j = 2.5 * 1000
record("work-done-p4", work_p4_j / 20, "m")

# p5: tug pulls barge with 3000 N at 2 m/s for 60 s; answer in kJ
distance_barge = 2 * 60
work_barge_j = 3000 * distance_barge
record("work-done-p5", work_barge_j / 1000, "kJ")

# p6: 1200 kg car accelerates at 2 m/s² over 50 m; work by resultant force in kJ
force_car = 1200 * 2
work_car_j = force_car * 50
record("work-done-p6", work_car_j / 1000, "kJ")

# ---------------------------------------------------------------------------
# Type 4: power   P = E / t,  P = W / t
# ---------------------------------------------------------------------------

# w: motor does 3000 J in 20 s
record("power-w", 3000 / 20, "W")

# p1: kettle transfers 180000 J in 90 s
record("power-p1", 180000 / 90, "W")

# p2: weightlifter does 1500 J in 2.5 s
record("power-p2", 1500 / 2.5, "W")

# p3: 2 kW heater for 5 minutes; energy in kJ
power_heater = 2 * 1000
time_heater = 5 * 60
record("power-p3", power_heater * time_heater / 1000, "kJ")

# p4: 60 W bulb transfers 9000 J; find t
record("power-p4", 9000 / 60, "s")

# p5: motor lifts 50 kg load 8 m in 20 s
gpe_load = 50 * G * 8
record("power-p5", gpe_load / 20, "W")

# p6: winch pulls with 1500 N over 12 m in 30 s
work_winch = 1500 * 12
record("power-p6", work_winch / 30, "W")

# ---------------------------------------------------------------------------
# Type 5: efficiency
# ---------------------------------------------------------------------------

# w: motor input 500 J, useful 350 J; decimal
record("efficiency-w", 350 / 500, "")

# p1: kettle input 120 kJ, useful 108 kJ; percentage
record("efficiency-p1", 108 / 120 * 100, "%")

# p2: lamp input 60 W, light output 6 W; decimal
record("efficiency-p2", 6 / 60, "")

# p3: motor 80 % efficient, input 2500 J; useful output
record("efficiency-p3", 0.80 * 2500, "J")

# p4: petrol engine 30 % efficient, useful 45 kJ; input in kJ
record("efficiency-p4", 45 / 0.30, "kJ")

# p5: crane input 20000 J lifts 50 kg by 24 m; decimal
gpe_crane_load = 50 * G * 24
record("efficiency-p5", gpe_crane_load / 20000, "")

# p6: 400 W motor for 30 s, useful output 9000 J; percentage
input_motor = 400 * 30
record("efficiency-p6", 9000 / input_motor * 100, "%")

# ---------------------------------------------------------------------------
# Type 6: energy-transfers   GPE lost = KE gained
# ---------------------------------------------------------------------------

# w: ball dropped from 5 m; speed at the ground
record("energy-transfers-w", math.sqrt(2 * G * 5), "m/s")

# p1: 500 kg roller-coaster car drops 20 m; KE at the bottom
record("energy-transfers-p1", 500 * G * 20, "J")

# p2: diver from 7.2 m; speed on entry
record("energy-transfers-p2", math.sqrt(2 * G * 7.2), "m/s")

# p3: ball thrown up at 14 m/s; height reached
record("energy-transfers-p3", 14 ** 2 / (2 * G), "m")

# p4: phone dropped 180 cm; speed at the floor
height_phone = 180 / 100
record("energy-transfers-p4", math.sqrt(2 * G * height_phone), "m/s")

# p5 (Higher): 60 kg skier drops 30 m, 6000 J wasted; speed at the bottom
gpe_skier = 60 * G * 30
ke_skier = gpe_skier - 6000
record("energy-transfers-p5", math.sqrt(2 * ke_skier / 60), "m/s")

# p6 (Higher): 2 kg block slides from 4 m height, reaches 6 m/s; energy wasted
gpe_block = 2 * G * 4
ke_block = 0.5 * 2 * 6 ** 2
record("energy-transfers-p6", gpe_block - ke_block, "J")

# ---------------------------------------------------------------------------
# Type 7: energy-graph   (graph questions)
# ---------------------------------------------------------------------------

# w: F–d constant 150 N, shaded 0–8 m; area = work
record("energy-graph-w", 150 * (8 - 0), "J")
graphs["energy-graph-w"] = {"line": [[0, 150], [10, 150]]}

# p1: bow F–d (0,0) to (0.5, 120); triangle area
record("energy-graph-p1", 0.5 * (0.5 - 0) * 120, "J")
graphs["energy-graph-p1"] = {"line": [[0, 0], [0.5, 120]]}

# p2: GPE–height (0,0) to (5,400); gradient = m × g
gradient_p2 = (400 - 0) / (5 - 0)
record("energy-graph-p2", gradient_p2 / G, "kg")
graphs["energy-graph-p2"] = {"line": [[0, 0], [5, 400]], "mark": [5, 400]}

# p3: E–t (0,0) to (20,3000); gradient = power
gradient_p3 = (3000 - 0) / (20 - 0)
record("energy-graph-p3", gradient_p3, "W")
graphs["energy-graph-p3"] = {"line": [[0, 0], [20, 3000]], "mark": [20, 3000]}

# p4: sledge F–d (0,100),(6,100),(10,0); rectangle + triangle
area_rectangle = (6 - 0) * 100
area_triangle = 0.5 * (10 - 6) * 100
record("energy-graph-p4", area_rectangle + area_triangle, "J")
graphs["energy-graph-p4"] = {"line": [[0, 100], [6, 100], [10, 0]]}

# p5 (Higher): KE–v² (0,0) to (100,250); gradient = ½ m
gradient_p5 = (250 - 0) / (100 - 0)
record("energy-graph-p5", 2 * gradient_p5, "kg")
graphs["energy-graph-p5"] = {"line": [[0, 0], [100, 250]], "mark": [100, 250]}

# p6: motor useful E–t (0,0) to (20,6000); gradient = useful power; input 500 W
gradient_p6 = (6000 - 0) / (20 - 0)
record("energy-graph-p6", gradient_p6 / 500 * 100, "%")
graphs["energy-graph-p6"] = {"line": [[0, 0], [20, 6000]], "mark": [20, 6000]}

# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

print("Computed answers (3 s.f.):")
for question_id, (value, unit) in answers.items():
    print(f"  {question_id:36s} {value} {unit}")

print()
print("Graph coordinates:")
for question_id, data in graphs.items():
    print(f"  {question_id}: {json.dumps(data)}")

# Cross-check against the topic file when it exists
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
topic_path = os.path.join(root, "data", "energy.json")
if os.path.exists(topic_path):
    with open(topic_path, encoding="utf-8") as handle:
        topic = json.load(handle)
    mismatches = 0
    seen = 0
    for ctype in topic["types"]:
        questions = [ctype["worked"]] + ctype["practice"]
        for question in questions:
            seen += 1
            question_id = question["id"]
            if question_id not in answers:
                print(f"NOT COMPUTED: {question_id}")
                mismatches += 1
                continue
            expected_value, expected_unit = answers[question_id]
            stored_value = question["answer"]["value"]
            stored_unit = question["answer"]["unit"]
            if abs(stored_value - expected_value) > 1e-9 * max(1, abs(expected_value)):
                print(f"MISMATCH {question_id}: stored {stored_value}, computed {expected_value}")
                mismatches += 1
            if stored_unit != expected_unit:
                print(f"UNIT MISMATCH {question_id}: stored {stored_unit!r}, computed {expected_unit!r}")
                mismatches += 1
            # Check that every plotted point in a graph matches the script's data
            if question_id in graphs and "graph" in question:
                script_points = []
                for key, value in graphs[question_id].items():
                    if key in ("line", "curve"):
                        script_points.append(value)
                stored_points = [series["points"] for series in question["graph"]["series"]
                                 if series.get("kind") in ("line", "curve")]
                if script_points != stored_points:
                    print(f"GRAPH POINTS DIFFER {question_id}")
                    mismatches += 1
    print()
    print(f"Cross-check: {seen} questions in file, {len(answers)} computed, {mismatches} problem(s)")
    if mismatches:
        sys.exit(1)
