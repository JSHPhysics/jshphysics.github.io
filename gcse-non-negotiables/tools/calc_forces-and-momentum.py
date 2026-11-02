#!/usr/bin/env python3
"""Compute every answer in data/forces-and-momentum.json from the question data.

Usage: python3 tools/calc_forces-and-momentum.py

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
# Type 1: weight-and-mass   W = m × g
# ---------------------------------------------------------------------------

# w: 65 kg student on Earth
record("weight-and-mass-w", 65 * G, "N")

# p1: 1200 kg car
record("weight-and-mass-p1", 1200 * G, "N")

# p2: 2.5 kg bag of flour
record("weight-and-mass-p2", 2.5 * G, "N")

# p3: chair weighs 48 N, find mass
record("weight-and-mass-p3", 48 / G, "kg")

# p4: 400 g tin of beans, weight in N
mass_tin = 400 / 1000
record("weight-and-mass-p4", mass_tin * G, "N")

# p5: astronaut weighs 800 N on Earth; weight on the Moon where g = 1.6 N/kg
mass_astronaut = 800 / G
record("weight-and-mass-p5", mass_astronaut * 1.6, "N")

# p6: lander weighs 1500 N on Earth and 555 N on Mars; find g on Mars
mass_lander = 1500 / G
record("weight-and-mass-p6", 555 / mass_lander, "N/kg")

# ---------------------------------------------------------------------------
# Type 2: resultant-force   forces along a line
# ---------------------------------------------------------------------------

# w: tug of war 850 N left, 920 N right
record("resultant-force-w", 920 - 850, "N")

# p1: car 3000 N forward, 1200 N resistive
record("resultant-force-p1", 3000 - 1200, "N")

# p2: two people push same direction, 150 N and 220 N
record("resultant-force-p2", 150 + 220, "N")

# p3: boat thrust 4500 N, resultant 1700 N forward; find drag
record("resultant-force-p3", 4500 - 1700, "N")

# p4: rocket thrust 2.4 kN up, weight 1800 N; resultant
thrust_rocket = 2.4 * 1000
record("resultant-force-p4", thrust_rocket - 1800, "N")

# p5: 70 kg skydiver, air resistance 560 N; resultant downward
weight_skydiver = 70 * G
record("resultant-force-p5", weight_skydiver - 560, "N")

# p6: 500 kg lift, cable tension 6200 N; resultant upward
weight_lift = 500 * G
record("resultant-force-p6", 6200 - weight_lift, "N")

# ---------------------------------------------------------------------------
# Type 3: newtons-second-law   F = m × a
# ---------------------------------------------------------------------------

# w: 1500 kg car, a = 2 m/s²
record("newtons-second-law-w", 1500 * 2, "N")

# p1: 2 kg trolley, a = 1.5 m/s²
record("newtons-second-law-p1", 2 * 1.5, "N")

# p2: 80 kg cyclist and bike, a = 0.75 m/s²
record("newtons-second-law-p2", 80 * 0.75, "N")

# p3: lorry, resultant 18 kN gives 1.2 m/s²; find mass
force_lorry = 18 * 1000
record("newtons-second-law-p3", force_lorry / 1.2, "kg")

# p4: 300 g toy car, resultant 0.6 N; find a
mass_toy = 300 / 1000
record("newtons-second-law-p4", 0.6 / mass_toy, "m/s²")

# p5: 1200 kg car, engine 2500 N, resistive 700 N; find a
resultant_car = 2500 - 700
record("newtons-second-law-p5", resultant_car / 1200, "m/s²")

# p6: 500 kg rocket, thrust 8000 N upward; find a
weight_rocket = 500 * G
resultant_rocket = 8000 - weight_rocket
record("newtons-second-law-p6", resultant_rocket / 500, "m/s²")

# ---------------------------------------------------------------------------
# Type 4: stopping-distance
# ---------------------------------------------------------------------------

# w: 15 m/s, reaction 0.6 s, braking 14 m; stopping distance
thinking_w = 15 * 0.6
record("stopping-distance-w", thinking_w + 14, "m")

# p1: 20 m/s, reaction 0.7 s; thinking distance
record("stopping-distance-p1", 20 * 0.7, "m")

# p2: thinking 12 m, braking 24 m; stopping distance
record("stopping-distance-p2", 12 + 24, "m")

# p3: thinking distance 18 m at 24 m/s; find reaction time
record("stopping-distance-p3", 18 / 24, "s")

# p4: 54 km/h, reaction 0.8 s; thinking distance
speed_p4 = 54 * 1000 / 3600
record("stopping-distance-p4", speed_p4 * 0.8, "m")

# p5: 30 m/s, reaction 0.5 s, braking 75 m; stopping distance
thinking_p5 = 30 * 0.5
record("stopping-distance-p5", thinking_p5 + 75, "m")

# p6: stopping 60 m, speed 25 m/s, reaction 0.8 s; braking distance
thinking_p6 = 25 * 0.8
record("stopping-distance-p6", 60 - thinking_p6, "m")

# ---------------------------------------------------------------------------
# Type 5: momentum   p = m × v   (Higher)
# ---------------------------------------------------------------------------

# w: 1200 kg car at 15 m/s
record("momentum-w", 1200 * 15, "kg m/s")

# p1: 70 kg runner at 8 m/s
record("momentum-p1", 70 * 8, "kg m/s")

# p2: 0.16 kg cricket ball at 35 m/s
record("momentum-p2", 0.16 * 35, "kg m/s")

# p3: lorry momentum 240000 kg m/s at 16 m/s; find mass
record("momentum-p3", 240000 / 16, "kg")

# p4: 450 g ball, momentum 9 kg m/s; find v
mass_ball = 450 / 1000
record("momentum-p4", 9 / mass_ball, "m/s")

# p5: 75 kg cyclist covers 100 m in 12.5 s; momentum
speed_cyclist = 100 / 12.5
record("momentum-p5", 75 * speed_cyclist, "kg m/s")

# p6: trolley weighs 150 N, pushed at 1.2 m/s; momentum
mass_trolley = 150 / G
record("momentum-p6", mass_trolley * 1.2, "kg m/s")

# ---------------------------------------------------------------------------
# Type 6: conservation-of-momentum   (Higher)
# ---------------------------------------------------------------------------

# w: 2 kg at 3 m/s hits stationary 1 kg, stick
record("conservation-of-momentum-w", (2 * 3) / (2 + 1), "m/s")

# p1: 1200 kg car at 10 m/s hits stationary 800 kg car, lock together
record("conservation-of-momentum-p1", (1200 * 10) / (1200 + 800), "m/s")

# p2: 8000 kg truck at 4 m/s couples to stationary 12000 kg truck
record("conservation-of-momentum-p2", (8000 * 4) / (8000 + 12000), "m/s")

# p3: skaters push apart from rest; 60 kg moves at 2 m/s; speed of 40 kg skater
record("conservation-of-momentum-p3", (60 * 2) / 40, "m/s")

# p4: 4 kg rifle fires 10 g bullet at 400 m/s; recoil speed
mass_bullet = 10 / 1000
record("conservation-of-momentum-p4", (mass_bullet * 400) / 4, "m/s")

# p5: 0.5 kg ball at 6 m/s hits stationary 0.3 kg ball; first continues at 1.5 m/s
momentum_before_p5 = 0.5 * 6
momentum_first_after = 0.5 * 1.5
record("conservation-of-momentum-p5", (momentum_before_p5 - momentum_first_after) / 0.3, "m/s")

# p6: 3 kg trolley at 4 m/s catches 2 kg trolley at 1.5 m/s, stick
momentum_before_p6 = 3 * 4 + 2 * 1.5
record("conservation-of-momentum-p6", momentum_before_p6 / (3 + 2), "m/s")

# ---------------------------------------------------------------------------
# Type 7: force-from-momentum-change   F = (mv − mu) / t   (Higher)
# ---------------------------------------------------------------------------

# w: 0.4 kg football from rest to 20 m/s in 0.05 s
record("force-from-momentum-change-w", (0.4 * 20 - 0) / 0.05, "N")

# p1: 1000 kg car from 15 m/s to rest in 3 s; size of force
record("force-from-momentum-change-p1", (1000 * 15 - 0) / 3, "N")

# p2: 0.06 kg tennis ball from rest to 50 m/s in 0.004 s
record("force-from-momentum-change-p2", (0.06 * 50) / 0.004, "N")

# p3: 1200 kg car at 12 m/s stopped by 72000 N; find time
record("force-from-momentum-change-p3", (1200 * 12) / 72000, "s")

# p4: 160 g puck from rest to 30 m/s in 0.02 s
mass_puck = 160 / 1000
record("force-from-momentum-change-p4", (mass_puck * 30) / 0.02, "N")

# p5: climber weighing 800 N stopped from 6 m/s in 0.4 s
mass_climber = 800 / G
record("force-from-momentum-change-p5", (mass_climber * 6) / 0.4, "N")

# p6: 0.2 kg ball at 8 m/s, 60 N for 0.05 s in direction of motion; final speed
momentum_initial = 0.2 * 8
momentum_change = 60 * 0.05
record("force-from-momentum-change-p6", (momentum_initial + momentum_change) / 0.2, "m/s")

# ---------------------------------------------------------------------------
# Type 8: force-graph   (graph questions)
# ---------------------------------------------------------------------------

# w: a–F line (0,0) to (10,5); X at (8,4); gradient = 1/m
gradient_w = (4 - 0) / (8 - 0)
record("force-graph-w", 1 / gradient_w, "kg")
graphs["force-graph-w"] = {
    "line": [[0, 0], [10, 5]],
    "mark": [8, 4],
}

# p1: skydiver v–t curve, terminal velocity 50 m/s; v = 50(1 − e^(−t/8))
terminal_p1 = 50
curve_p1 = []
for index in range(0, 17):
    t = index * 2.5
    v = terminal_p1 * (1 - math.exp(-t / 8))
    curve_p1.append([round(t, 2), round(v, 2)])
record("force-graph-p1", terminal_p1, "m/s")
graphs["force-graph-p1"] = {"curve": curve_p1}

# p2: a–F line (0,0) to (8,2); P at (6,1.5); read the force
record("force-graph-p2", 6, "N")
graphs["force-graph-p2"] = {
    "line": [[0, 0], [8, 2]],
    "mark": [6, 1.5],
}

# p3: skydiver v–t: straight (0,0)→(2,20), then v = 60 − 40 e^(−0.25(t−2))
gradient_p3 = (20 - 0) / (2 - 0)
record("force-graph-p3", gradient_p3, "m/s²")
curve_p3 = []
for index in range(0, 19):
    t = 2 + index * 1.0
    v = 60 - 40 * math.exp(-0.25 * (t - 2))
    curve_p3.append([round(t, 2), round(v, 2)])
graphs["force-graph-p3"] = {
    "line": [[0, 0], [2, 20]],
    "curve": curve_p3,
}

# p4: a–F line with friction (2,0) to (10,2); intercept on F axis = friction
record("force-graph-p4", 2, "N")
graphs["force-graph-p4"] = {
    "line": [[2, 0], [10, 2]],
    "mark": [2, 0],
}

# p5: F–t graph (ms): (0,0),(2,400),(6,400),(8,0); area = impulse
area_triangle_1 = 0.5 * (2 - 0) * 400
area_rectangle = (6 - 2) * 400
area_triangle_2 = 0.5 * (8 - 6) * 400
area_n_ms = area_triangle_1 + area_rectangle + area_triangle_2
impulse_p5 = area_n_ms / 1000
record("force-graph-p5", impulse_p5, "kg m/s")
graphs["force-graph-p5"] = {
    "line": [[0, 0], [2, 400], [6, 400], [8, 0]],
    "area_n_ms": area_n_ms,
}

# p6: a–F line with friction (3,0) to (12,3); gradient = 1/m
gradient_p6 = (3 - 0) / (12 - 3)
record("force-graph-p6", 1 / gradient_p6, "kg")
graphs["force-graph-p6"] = {
    "line": [[3, 0], [12, 3]],
    "mark_a": [3, 0],
    "mark_b": [12, 3],
}

# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

print("Computed answers (3 s.f.):")
for question_id, (value, unit) in answers.items():
    print(f"  {question_id:32s} {value} {unit}")

print()
print("Graph coordinates:")
for question_id, data in graphs.items():
    print(f"  {question_id}: {json.dumps(data)}")

# Cross-check against the topic file when it exists
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
topic_path = os.path.join(root, "data", "forces-and-momentum.json")
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
