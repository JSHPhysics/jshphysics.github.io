#!/usr/bin/env python3
"""Compute every answer in data/kinematics.json.

Each answer is printed rounded to 3 s.f. with its question id.
Run: python3 tools/calc_kinematics.py
"""

import math

# Standard constants from SCHEMA.md
g = 9.81          # m s^-2

results = []


def record(question_id, value, unit):
    """Store one answer, rounded to 3 significant figures."""
    if value == 0:
        rounded = 0.0
    else:
        # Number of decimal places that gives 3 s.f.
        magnitude = math.floor(math.log10(abs(value)))
        places = 2 - magnitude
        rounded = round(value, places)
    results.append((question_id, rounded, unit, value))


def sin_deg(angle):
    """Sine of an angle given in degrees."""
    return math.sin(math.radians(angle))


def cos_deg(angle):
    """Cosine of an angle given in degrees."""
    return math.cos(math.radians(angle))


# ---------------------------------------------------------------
# Type 1: speed-velocity-acceleration
# ---------------------------------------------------------------

# w: sprinter 200 m in 20.3 s -> average speed
record("speed-velocity-acceleration-w", 200 / 20.3, "m s⁻¹")

# p1: car 5.0 -> 23 m/s in 6.0 s -> acceleration
record("speed-velocity-acceleration-p1", (23 - 5.0) / 6.0, "m s⁻²")

# p2: lift rises 42 m in 15 s -> average velocity
record("speed-velocity-acceleration-p2", 42 / 15, "m s⁻¹")

# p3: train 54 km in 40 minutes -> average speed in m/s
distance_p3 = 54 * 1000
time_p3 = 40 * 60
record("speed-velocity-acceleration-p3", distance_p3 / time_p3, "m s⁻¹")

# p4: car 90 km/h to rest in 7.5 s -> magnitude of deceleration
u_p4 = 90 * 1000 / 3600
record("speed-velocity-acceleration-p4", u_p4 / 7.5, "m s⁻²")

# p5: van 12 km at 8.0 m/s then 6.0 km in 10 min -> overall average speed
time_1_p5 = 12000 / 8.0
time_2_p5 = 10 * 60
record("speed-velocity-acceleration-p5", (12000 + 6000) / (time_1_p5 + time_2_p5), "m s⁻¹")

# p6: car 54 km/h -> 90 km/h in 8.0 s -> acceleration
u_p6 = 54 * 1000 / 3600
v_p6 = 90 * 1000 / 3600
record("speed-velocity-acceleration-p6", (v_p6 - u_p6) / 8.0, "m s⁻²")


# ---------------------------------------------------------------
# Type 2: suvat-one-equation
# ---------------------------------------------------------------

# w: cyclist 3.0 -> 9.0 m/s over 24 m -> a
record("suvat-one-equation-w", (9.0 ** 2 - 3.0 ** 2) / (2 * 24), "m s⁻²")

# p1: train from rest, a = 0.50, t = 40 s -> v
record("suvat-one-equation-p1", 0 + 0.50 * 40, "m s⁻¹")

# p2: rocket sled from rest, a = 30, t = 4.0 s -> s
record("suvat-one-equation-p2", 0.5 * 30 * 4.0 ** 2, "m")

# p3: ball from rest reaches 6.0 m/s after 9.0 m -> a
record("suvat-one-equation-p3", (6.0 ** 2 - 0) / (2 * 9.0), "m s⁻²")

# p4: car at 72 km/h brakes to rest over 50 m -> magnitude of deceleration
u_s_p4 = 72 * 1000 / 3600
record("suvat-one-equation-p4", (u_s_p4 ** 2 - 0) / (2 * 50), "m s⁻²")

# p5: bullet from rest to 320 m/s along 0.60 m barrel -> time in ms
t_s_p5 = 2 * 0.60 / (0 + 320)
record("suvat-one-equation-p5", t_s_p5 * 1000, "ms")

# p6: electron from rest to 2.0e7 m/s over 5.0 cm -> a
s_s_p6 = 5.0 / 100
record("suvat-one-equation-p6", (2.0e7) ** 2 / (2 * s_s_p6), "m s⁻²")


# ---------------------------------------------------------------
# Type 3: suvat-two-step
# ---------------------------------------------------------------

# w: car from rest at 2.5 for 6.0 s, then decelerates to rest over 30 m -> deceleration
v_w3 = 0 + 2.5 * 6.0
record("suvat-two-step-w", v_w3 ** 2 / (2 * 30), "m s⁻²")

# p1: cyclist 4.0 m/s, a = 0.80 for 10 s, then constant for 20 s -> distance at constant velocity
v_3p1 = 4.0 + 0.80 * 10
record("suvat-two-step-p1", v_3p1 * 20, "m")

# p2: sprinter from rest to 9.0 m/s in 3.0 s, then 7.0 s at that speed -> total distance
s_1_3p2 = 0.5 * (0 + 9.0) * 3.0
s_2_3p2 = 9.0 * 7.0
record("suvat-two-step-p2", s_1_3p2 + s_2_3p2, "m")

# p3: lorry 20 -> 8.0 m/s over 84 m; -> total time to come to rest from 20 m/s
a_3p3 = (8.0 ** 2 - 20 ** 2) / (2 * 84)
record("suvat-two-step-p3", (0 - 20) / a_3p3, "s")

# p4: tram from rest at 1.2 for 25 s, then brakes to rest in 15 s -> total distance in km
v_3p4 = 1.2 * 25
s_1_3p4 = 0.5 * 1.2 * 25 ** 2
s_2_3p4 = 0.5 * (v_3p4 + 0) * 15
record("suvat-two-step-p4", (s_1_3p4 + s_2_3p4) / 1000, "km")

# p5: rocket sled from rest covers 180 m in 6.0 s -> final velocity
a_3p5 = 2 * 180 / 6.0 ** 2
record("suvat-two-step-p5", 0 + a_3p5 * 6.0, "m s⁻¹")

# p6: ball from rest, 1.2 m/s after 0.50 m -> velocity after 2.0 m
a_3p6 = 1.2 ** 2 / (2 * 0.50)
record("suvat-two-step-p6", math.sqrt(2 * a_3p6 * 2.0), "m s⁻¹")


# ---------------------------------------------------------------
# Type 4: vertical-motion
# ---------------------------------------------------------------

# w: ball thrown up at 15 m/s -> max height
record("vertical-motion-w", 15 ** 2 / (2 * g), "m")

# p1: coin dropped from 20 m -> time to hit water
record("vertical-motion-p1", math.sqrt(2 * 20 / g), "s")

# p2: stone dropped, hits sea after 3.2 s -> speed on impact
record("vertical-motion-p2", g * 3.2, "m s⁻¹")

# p3: dropped from 45 m -> speed on impact in km/h
v_4p3 = math.sqrt(2 * g * 45)
record("vertical-motion-p3", v_4p3 * 3600 / 1000, "km h⁻¹")

# p4: flea reaches 20 cm -> take-off speed
h_4p4 = 20 / 100
record("vertical-motion-p4", math.sqrt(2 * g * h_4p4), "m s⁻¹")

# p5: ball thrown up at 14 m/s, caught at same height -> total time in air
t_up_4p5 = 14 / g
record("vertical-motion-p5", 2 * t_up_4p5, "s")

# p6: thrown up at 12 m/s from balcony 30 m up -> time to reach ground
# up positive: u = 12, a = -g, s = -30
v_4p6 = -math.sqrt(12 ** 2 + 2 * (-g) * (-30))
record("vertical-motion-p6", (v_4p6 - 12) / (-g), "s")


# ---------------------------------------------------------------
# Type 5: projectiles-horizontal
# ---------------------------------------------------------------

# w: ball rolls off 0.80 m table at 2.5 m/s -> horizontal distance
t_5w = math.sqrt(2 * 0.80 / g)
record("projectiles-horizontal-w", 2.5 * t_5w, "m")

# p1: stone thrown horizontally from 45 m cliff -> time to hit water
record("projectiles-horizontal-p1", math.sqrt(2 * 45 / g), "s")

# p2: package from plane at 60 m/s, falls for 4.9 s -> horizontal distance
record("projectiles-horizontal-p2", 60 * 4.9, "m")

# p3: dart at 12 m/s, board 2.4 m away -> drop in cm
t_5p3 = 2.4 / 12
drop_5p3 = 0.5 * g * t_5p3 ** 2
record("projectiles-horizontal-p3", drop_5p3 * 100, "cm")

# p4: hose 1.2 m up, water lands 3.0 m away -> speed of water
t_5p4 = math.sqrt(2 * 1.2 / g)
record("projectiles-horizontal-p4", 3.0 / t_5p4, "m s⁻¹")

# p5: ski jumper 25 m/s, lands 40 m below -> horizontal distance
t_5p5 = math.sqrt(2 * 40 / g)
record("projectiles-horizontal-p5", 25 * t_5p5, "m")

# p6: stone 15 m/s horizontal from 20 m cliff -> speed on landing
vy_5p6 = math.sqrt(2 * g * 20)
record("projectiles-horizontal-p6", math.sqrt(15 ** 2 + vy_5p6 ** 2), "m s⁻¹")


# ---------------------------------------------------------------
# Type 6: projectiles-angle
# ---------------------------------------------------------------

# w: football 20 m/s at 30 deg -> max height
uy_6w = 20 * sin_deg(30)
record("projectiles-angle-w", uy_6w ** 2 / (2 * g), "m")

# p1: arrow 40 m/s at 25 deg -> initial vertical component
record("projectiles-angle-p1", 40 * sin_deg(25), "m s⁻¹")

# p2: golf ball 35 m/s at 40 deg -> time to max height
uy_6p2 = 35 * sin_deg(40)
record("projectiles-angle-p2", uy_6p2 / g, "s")

# p3: long jumper 9.0 m/s at 20 deg -> max height in cm
uy_6p3 = 9.0 * sin_deg(20)
record("projectiles-angle-p3", uy_6p3 ** 2 / (2 * g) * 100, "cm")

# p4: shell 150 m/s at 35 deg -> time of flight
uy_6p4 = 150 * sin_deg(35)
record("projectiles-angle-p4", 2 * uy_6p4 / g, "s")

# p5: javelin 28 m/s at 38 deg -> range
uy_6p5 = 28 * sin_deg(38)
ux_6p5 = 28 * cos_deg(38)
t_6p5 = 2 * uy_6p5 / g
record("projectiles-angle-p5", ux_6p5 * t_6p5, "m")

# p6: motorcyclist 22 m/s at 25 deg -> range
uy_6p6 = 22 * sin_deg(25)
ux_6p6 = 22 * cos_deg(25)
t_6p6 = 2 * uy_6p6 / g
record("projectiles-angle-p6", ux_6p6 * t_6p6, "m")


# ---------------------------------------------------------------
# Type 7: velocity-time-graphs
# ---------------------------------------------------------------

# w: 0 -> 12 in 8 s, 12 for 20 s, 12 -> 0 in 4 s -> total displacement
area_1_7w = 0.5 * 8 * 12
area_2_7w = 20 * 12
area_3_7w = 0.5 * 4 * 12
record("velocity-time-graphs-w", area_1_7w + area_2_7w + area_3_7w, "m")

# p1: 0 -> 15 m/s in 6.0 s -> acceleration
record("velocity-time-graphs-p1", (15 - 0) / 6.0, "m s⁻²")

# p2: 6.0 -> 18 m/s between t = 0 and 4.0 s -> displacement (trapezium)
record("velocity-time-graphs-p2", 0.5 * (6.0 + 18) * 4.0, "m")

# p3: lorry 54 km/h to rest in 12 s -> magnitude of deceleration
u_7p3 = 54 * 1000 / 3600
record("velocity-time-graphs-p3", u_7p3 / 12, "m s⁻²")

# p4: triangle 0 -> v in 5.0 s, area 60 m -> v
record("velocity-time-graphs-p4", 2 * 60 / 5.0, "m s⁻¹")

# p5: 0 -> v in 10 s, then v for 30 s; total 700 m -> v
record("velocity-time-graphs-p5", 700 / (0.5 * 10 + 30), "m s⁻¹")

# p6: 0 -> 9.0 in 3.0 s, 9.0 -> 0 in 12 s -> average velocity
area_7p6 = 0.5 * 3.0 * 9.0 + 0.5 * 12 * 9.0
record("velocity-time-graphs-p6", area_7p6 / 15, "m s⁻¹")


# ---------------------------------------------------------------
# Type 8: displacement-time-graphs
# ---------------------------------------------------------------

# w: s = 40 m at 5.0 s, s = 160 m at 20 s -> velocity
record("displacement-time-graphs-w", (160 - 40) / (20 - 5.0), "m s⁻¹")

# p1: straight line (0, 0) to (12 s, 54 m) -> velocity
record("displacement-time-graphs-p1", 54 / 12, "m s⁻¹")

# p2: toy boat from (0, 12 m) to (8.0 s, 0) -> speed
record("displacement-time-graphs-p2", abs(0 - 12) / 8.0, "m s⁻¹")

# p3: snail 0 -> 36 cm in 2.0 minutes -> velocity in m/s
record("displacement-time-graphs-p3", (36 / 100) / (2.0 * 60), "m s⁻¹")

# p4: tram 0.60 km at 20 s to 1.5 km at 80 s -> velocity in m/s
record("displacement-time-graphs-p4", (1.5 - 0.60) * 1000 / (80 - 20), "m s⁻¹")

# p5: RC car 0 -> 30 m in 5.0 s, stationary to 12 s, back to 0 at 15 s -> average speed
distance_8p5 = 30 + 30
record("displacement-time-graphs-p5", distance_8p5 / 15, "m s⁻¹")

# p6: car 0 -> 150 m in first 10 s, 150 -> 390 m in next 10 s -> increase in velocity
v_1_8p6 = 150 / 10
v_2_8p6 = (390 - 150) / 10
record("displacement-time-graphs-p6", v_2_8p6 - v_1_8p6, "m s⁻¹")


# ---------------------------------------------------------------
# Print
# ---------------------------------------------------------------

for question_id, rounded, unit, raw in results:
    print(f"{question_id:32s} {rounded!r:>14}  {unit:14s} (raw {raw!r})")
