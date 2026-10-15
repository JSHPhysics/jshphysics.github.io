#!/usr/bin/env python3
"""Compute every answer in data/forces.json.

Each answer is printed rounded to 3 s.f. with its question id.
Run: python3 tools/calc_forces.py
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


def tan_deg(angle):
    """Tangent of an angle given in degrees."""
    return math.tan(math.radians(angle))


def atan_deg(ratio):
    """Inverse tangent, returned in degrees."""
    return math.degrees(math.atan(ratio))


def asin_deg(ratio):
    """Inverse sine, returned in degrees."""
    return math.degrees(math.asin(ratio))


# ---------------------------------------------------------------
# Type 1: weight-and-mass   W = mg
# ---------------------------------------------------------------

# w: astronaut of mass 85 kg on Earth
record("weight-and-mass-w", 85 * g, "N")

# p1: textbook of mass 1.2 kg on Earth
record("weight-and-mass-p1", 1.2 * g, "N")

# p2: Mars rover of mass 899 kg, g_Mars = 3.71 N/kg
record("weight-and-mass-p2", 899 * 3.71, "N")

# p3: weight 540 N on Earth -> mass
record("weight-and-mass-p3", 540 / g, "kg")

# p4: crate of weight 2.4 kN on Earth -> mass (convert kN to N first)
weight_p4 = 2.4 * 1000
record("weight-and-mass-p4", weight_p4 / g, "kg")

# p5: weight 73.6 N on the Moon (g = 1.62) -> mass -> weight on Earth
mass_p5 = 73.6 / 1.62
record("weight-and-mass-p5", mass_p5 * g, "N")

# p6: weight 1570 N on Earth -> mass -> weight on Jupiter (g = 24.8)
mass_p6 = 1570 / g
record("weight-and-mass-p6", mass_p6 * 24.8, "N")


# ---------------------------------------------------------------
# Type 2: resolving-forces   F_x = F cos θ, F_y = F sin θ
# ---------------------------------------------------------------

# w: sledge rope 40 N at 30° above horizontal -> horizontal component
record("resolving-forces-w", 40 * cos_deg(30), "N")

# p1: kite string 25 N at 55° to horizontal -> vertical component
record("resolving-forces-p1", 25 * sin_deg(55), "N")

# p2: lawnmower push 120 N at 35° below horizontal -> horizontal component
record("resolving-forces-p2", 120 * cos_deg(35), "N")

# p3: horizontal component 180 N at 20° to horizontal -> full force
record("resolving-forces-p3", 180 / cos_deg(20), "N")

# p4: cable tension 3.5 kN at 65° to the vertical -> vertical component in N
tension_p4 = 3.5 * 1000
record("resolving-forces-p4", tension_p4 * cos_deg(65), "N")

# p5: roller handle at 28° to horizontal, vertical component 32 N -> horizontal component
force_p5 = 32 / sin_deg(28)
record("resolving-forces-p5", force_p5 * cos_deg(28), "N")

# p6: 250 N force, horizontal component 150 N -> angle -> vertical component
angle_p6 = math.degrees(math.acos(150 / 250))
record("resolving-forces-p6", 250 * sin_deg(angle_p6), "N")


# ---------------------------------------------------------------
# Type 3: resultant-perpendicular   R = √(F₁² + F₂²), tan θ = F₂/F₁
# ---------------------------------------------------------------

# w: boat 300 N forward, 400 N sideways -> magnitude
record("resultant-perpendicular-w", math.sqrt(300 ** 2 + 400 ** 2), "N")

# p1: puck 2.5 N and 6.0 N -> magnitude
record("resultant-perpendicular-p1", math.sqrt(2.5 ** 2 + 6.0 ** 2), "N")

# p2: 35 N horizontal, 60 N vertical -> angle above horizontal
record("resultant-perpendicular-p2", atan_deg(60 / 35), "°")

# p3: 1.2 kN and 900 N -> magnitude in kN
force_a_p3 = 1.2 * 1000
force_b_p3 = 900
resultant_p3 = math.sqrt(force_a_p3 ** 2 + force_b_p3 ** 2)
record("resultant-perpendicular-p3", resultant_p3 / 1000, "kN")

# p4: resultant 25 N, one force 15 N -> other force
record("resultant-perpendicular-p4", math.sqrt(25 ** 2 - 15 ** 2), "N")

# p5: 48 N horizontal pull on a 3.2 kg object; weight first, then magnitude
weight_p5 = 3.2 * g
record("resultant-perpendicular-p5", math.sqrt(48 ** 2 + weight_p5 ** 2), "N")

# p6: resultant 5.0 kN, one force 3.0 kN -> other force -> angle with the 3.0 kN force
other_p6 = math.sqrt(5.0 ** 2 - 3.0 ** 2)
record("resultant-perpendicular-p6", atan_deg(other_p6 / 3.0), "°")


# ---------------------------------------------------------------
# Type 4: newton-second-law   F = ma
# ---------------------------------------------------------------

# w: car 1200 kg, driving 3000 N, resistive 1200 N -> acceleration
record("newton-second-law-w", (3000 - 1200) / 1200, "m s⁻²")

# p1: trolley 2.5 kg, 6.0 N, no friction -> acceleration
record("newton-second-law-p1", 6.0 / 2.5, "m s⁻²")

# p2: sprinter 70 kg at 4.2 m/s^2 -> resultant force
record("newton-second-law-p2", 70 * 4.2, "N")

# p3: lorry 16 tonnes, driving 40 kN, resistance 12 kN -> acceleration
mass_p3 = 16 * 1000
resultant_p3_force = (40 - 12) * 1000
record("newton-second-law-p3", resultant_p3_force / mass_p3, "m s⁻²")

# p4: cyclist + bike 92 kg, a = 1.4, air resistance 35 N -> forward force
record("newton-second-law-p4", 92 * 1.4 + 35, "N")

# p5: sled 450 kg, 0 to 30 m/s in 4.0 s, friction 600 N -> thrust
accel_p5 = 30 / 4.0
record("newton-second-law-p5", 450 * accel_p5 + 600, "N")

# p6: car 1500 kg, 25 m/s to rest in 50 m -> deceleration -> braking force
decel_p6 = 25 ** 2 / (2 * 50)
record("newton-second-law-p6", 1500 * decel_p6, "N")


# ---------------------------------------------------------------
# Type 5: connected-bodies
# ---------------------------------------------------------------

# w: 3.0 kg and 5.0 kg over a pulley -> acceleration
record("connected-bodies-w", (5.0 - 3.0) * g / (5.0 + 3.0), "m s⁻²")

# p1: car 1200 kg tows trailer 400 kg, driving force 3200 N -> acceleration
record("connected-bodies-p1", 3200 / (1200 + 400), "m s⁻²")

# p2: tractor 2500 kg tows trailer 1500 kg at 0.80 m/s^2 -> tow bar tension
record("connected-bodies-p2", 1500 * 0.80, "N")

# p3: trolley 800 g, hanging mass 200 g -> acceleration (convert to kg)
trolley_p3 = 800 / 1000
hanging_p3 = 200 / 1000
record("connected-bodies-p3", hanging_p3 * g / (trolley_p3 + hanging_p3), "m s⁻²")

# p4: caravan 900 kg, tension 1350 N, resistance 270 N -> acceleration
record("connected-bodies-p4", (1350 - 270) / 900, "m s⁻²")

# p5: 4.0 kg and 6.0 kg over a pulley -> acceleration -> tension
accel_p5_cb = (6.0 - 4.0) * g / (6.0 + 4.0)
record("connected-bodies-p5", 4.0 * (g + accel_p5_cb), "N")

# p6: 2.0 kg block on smooth table, 1.5 kg hanging -> acceleration -> tension
accel_p6_cb = 1.5 * g / (2.0 + 1.5)
record("connected-bodies-p6", 2.0 * accel_p6_cb, "N")


# ---------------------------------------------------------------
# Type 6: inclines
# ---------------------------------------------------------------

# w: 12 kg box, 25° slope, friction 20 N -> acceleration
along_w = 12 * g * sin_deg(25)
record("inclines-w", (along_w - 20) / 12, "m s⁻²")

# p1: 65 kg skier on 15° slope -> component of weight along slope
record("inclines-p1", 65 * g * sin_deg(15), "N")

# p2: toy car on smooth 20° slope -> acceleration
record("inclines-p2", g * sin_deg(20), "m s⁻²")

# p3: 850 kg car on 12° hill -> normal reaction in kN
reaction_p3 = 850 * g * cos_deg(12)
record("inclines-p3", reaction_p3 / 1000, "kN")

# p4: smooth slope, acceleration 2.5 m/s^2 -> angle
record("inclines-p4", asin_deg(2.5 / g), "°")

# p5: 30 kg crate pulled up 20° slope at constant speed, friction 45 N -> pull
along_p5 = 30 * g * sin_deg(20)
record("inclines-p5", along_p5 + 45, "N")

# p6: 1400 kg car up 6.0° hill at 1.2 m/s^2, resistance 500 N -> driving force in kN
along_p6 = 1400 * g * sin_deg(6.0)
driving_p6 = 1400 * 1.2 + along_p6 + 500
record("inclines-p6", driving_p6 / 1000, "kN")


# ---------------------------------------------------------------
# Type 7: lifts   R − mg = ma
# ---------------------------------------------------------------

# w: 60 kg person, lift accelerating up at 1.5 -> reaction
record("lifts-w", 60 * (g + 1.5), "N")

# p1: 75 kg person, lift accelerating down at 2.0 -> reaction
record("lifts-p1", 75 * (g - 2.0), "N")

# p2: 120 kg crate, lift at constant speed -> reaction
record("lifts-p2", 120 * g, "N")

# p3: scales read 58.0 kg for a 50.0 kg person -> reaction -> acceleration
reaction_p3_lift = 58.0 * g
record("lifts-p3", reaction_p3_lift / 50.0 - g, "m s⁻²")

# p4: reaction 450 N on 55 kg person -> magnitude of (downward) acceleration
accel_p4_lift = 450 / 55 - g
record("lifts-p4", abs(accel_p4_lift), "m s⁻²")

# p5: lift 800 kg + passengers 250 kg, up at 1.2 -> cable tension in kN
total_p5 = 800 + 250
record("lifts-p5", total_p5 * (g + 1.2) / 1000, "kN")

# p6: lift moving up at 3.0 m/s stops in 2.5 s; 68 kg passenger -> reaction
accel_p6_lift = (0 - 3.0) / 2.5
record("lifts-p6", 68 * (g + accel_p6_lift), "N")


# ---------------------------------------------------------------
# Type 8: moments   moment = F × d; Σ clockwise = Σ anticlockwise
# ---------------------------------------------------------------

# w: 30 kg child at 1.6 m balanced by a force at 0.80 m -> force
child_w = 30 * g
record("moments-w", child_w * 1.6 / 0.80, "N")

# p1: spanner 40 N at 0.25 m -> moment
record("moments-p1", 40 * 0.25, "N m")

# p2: 400 N at 1.5 m balances child at 2.0 m -> child's weight
record("moments-p2", 400 * 1.5 / 2.0, "N")

# p3: nut needs 36 N m, spanner 180 mm -> force
arm_p3 = 180 / 1000
record("moments-p3", 36 / arm_p3, "N")

# p4: 1.5 N at 40 cm balances 2.0 N -> distance in cm
record("moments-p4", 1.5 * 40 / 2.0, "cm")

# p5: beam 200 N, 4.0 m, 600 N load 1.0 m from left; moments about left -> right reaction
moment_weight_p5 = 200 * 2.0
moment_load_p5 = 600 * 1.0
record("moments-p5", (moment_weight_p5 + moment_load_p5) / 4.0, "N")

# p6: plank 12 kg, 3.0 m, pivot 0.90 m from one end -> force at short end
plank_weight_p6 = 12 * g
arm_weight_p6 = 1.5 - 0.90
record("moments-p6", plank_weight_p6 * arm_weight_p6 / 0.90, "N")


# ---------------------------------------------------------------
# Print
# ---------------------------------------------------------------

for question_id, rounded, unit, raw in results:
    print(f"{question_id:30s} {rounded!r:>14}  {unit:8s} (raw {raw!r})")
