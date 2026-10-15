#!/usr/bin/env python3
"""Compute every answer in data/circular-shm.json.

Each answer is printed rounded to 3 s.f. with its question id.
Run: python3 tools/calc_circular-shm.py
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


# ---------------------------------------------------------------
# Type 1: angular-velocity
# ---------------------------------------------------------------

# w: record turntable at 45 rpm -> omega in rad/s
f_w = 45 / 60
record("angular-velocity-w", 2 * math.pi * f_w, "rad s⁻¹")

# p1: wind turbine, one revolution every 4.0 s
record("angular-velocity-p1", 2 * math.pi / 4.0, "rad s⁻¹")

# p2: ceiling fan at 2.5 Hz
record("angular-velocity-p2", 2 * math.pi * 2.5, "rad s⁻¹")

# p3: Earth rotating once in 24 hours (convert to seconds)
T_earth = 24 * 60 * 60
record("angular-velocity-p3", 2 * math.pi / T_earth, "rad s⁻¹")

# p4: radar aerial turns 135 degrees in 0.75 s
theta_p4 = 135 * math.pi / 180
record("angular-velocity-p4", theta_p4 / 0.75, "rad s⁻¹")

# p5: bicycle wheel r = 0.34 m at 180 rpm -> rim speed
omega_p5 = 2 * math.pi * 180 / 60
record("angular-velocity-p5", omega_p5 * 0.34, "m s⁻¹")

# p6: satellite v = 7.6e3 m/s at r = 6.9e6 m -> period
omega_p6 = 7.6e3 / 6.9e6
record("angular-velocity-p6", 2 * math.pi / omega_p6, "s")


# ---------------------------------------------------------------
# Type 2: centripetal-acceleration
# ---------------------------------------------------------------

# w: car at 15 m/s round a bend of radius 50 m
record("centripetal-acceleration-w", 15 ** 2 / 50, "m s⁻²")

# p1: hammer at 25 m/s on radius 2.1 m
record("centripetal-acceleration-p1", 25 ** 2 / 2.1, "m s⁻²")

# p2: washing machine drum r = 0.25 m at omega = 120 rad/s
record("centripetal-acceleration-p2", 120 ** 2 * 0.25, "m s⁻²")

# p3: centrifuge, a = 2.5e4 m/s^2 at r = 12 cm -> omega
r_p3 = 12 / 100
record("centripetal-acceleration-p3", math.sqrt(2.5e4 / r_p3), "rad s⁻¹")

# p4: train at 90 km/h, a must not exceed 0.80 m/s^2 -> minimum radius
v_p4 = 90 * 1000 / 3600
record("centripetal-acceleration-p4", v_p4 ** 2 / 0.80, "m")

# p5: Earth orbit, T = 3.16e7 s, r = 1.50e11 m -> a
omega_p5 = 2 * math.pi / 3.16e7
record("centripetal-acceleration-p5", omega_p5 ** 2 * 1.50e11, "m s⁻²")

# p6: fairground ride r = 6.0 m at 24 rpm -> a
omega_p6 = 2 * math.pi * 24 / 60
record("centripetal-acceleration-p6", omega_p6 ** 2 * 6.0, "m s⁻²")


# ---------------------------------------------------------------
# Type 3: centripetal-force
# ---------------------------------------------------------------

# w: 0.20 kg ball, string 0.80 m, speed 6.0 m/s -> tension
record("centripetal-force-w", 0.20 * 6.0 ** 2 / 0.80, "N")

# p1: 1200 kg car, radius 40 m, speed 12 m/s -> friction needed
record("centripetal-force-p1", 1200 * 12 ** 2 / 40, "N")

# p2: 65 kg rider, omega = 1.5 rad/s, r = 5.0 m
record("centripetal-force-p2", 65 * 1.5 ** 2 * 5.0, "N")

# p3: 850 g model plane, line 12 m, tension 48 N -> speed
m_p3 = 850 / 1000
record("centripetal-force-p3", math.sqrt(48 * 12 / m_p3), "m s⁻¹")

# p4: max friction 6.4 kN on 950 kg car, radius 60 m -> max speed
F_p4 = 6.4 * 1000
record("centripetal-force-p4", math.sqrt(F_p4 * 60 / 950), "m s⁻¹")

# p5: 2.5 kg mass, rope 1.6 m, 40 rpm -> tension
omega_p5 = 2 * math.pi * 40 / 60
record("centripetal-force-p5", 2.5 * omega_p5 ** 2 * 1.6, "N")

# p6: 450 kg satellite, r = 7.0e6 m, T = 5.8e3 s -> centripetal force
omega_p6 = 2 * math.pi / 5.8e3
record("centripetal-force-p6", 450 * omega_p6 ** 2 * 7.0e6, "N")


# ---------------------------------------------------------------
# Type 4: vertical-circle
# ---------------------------------------------------------------

# w: 0.50 kg bucket, rope 1.2 m, speed 5.0 m/s at the top -> tension
record("vertical-circle-w", 0.50 * 5.0 ** 2 / 1.2 - 0.50 * g, "N")

# p1: minimum speed at the top of a loop of radius 6.0 m
record("vertical-circle-p1", math.sqrt(g * 6.0), "m s⁻¹")

# p2: 0.30 kg ball, string 0.90 m, speed 4.0 m/s at the bottom -> tension
record("vertical-circle-p2", 0.30 * 4.0 ** 2 / 0.90 + 0.30 * g, "N")

# p3: 1100 kg car over a hump of radius 25 m at 36 km/h -> reaction
v_p3 = 36 * 1000 / 3600
record("vertical-circle-p3", 1100 * g - 1100 * v_p3 ** 2 / 25, "N")

# p4: 0.15 kg conker, string 0.60 m, tension 3.8 N at the bottom -> speed
v_squared_p4 = (3.8 - 0.15 * g) * 0.60 / 0.15
record("vertical-circle-p4", math.sqrt(v_squared_p4), "m s⁻¹")

# p5: 70 kg pilot at the bottom of a loop r = 500 m at 150 m/s -> seat force
a_p5 = 150 ** 2 / 500
record("vertical-circle-p5", 70 * (g + a_p5), "N")

# p6: 25 g toy car at the top of a loop r = 0.20 m, track pushes 0.30 N -> speed
m_p6 = 25 / 1000
v_squared_p6 = (0.30 + m_p6 * g) * 0.20 / m_p6
record("vertical-circle-p6", math.sqrt(v_squared_p6), "m s⁻¹")


# ---------------------------------------------------------------
# Type 5: shm-kinematics
# ---------------------------------------------------------------

# w: A = 0.050 m, f = 2.0 Hz -> maximum speed
omega_w = 2 * math.pi * 2.0
record("shm-kinematics-w", omega_w * 0.050, "m s⁻¹")

# p1: piston A = 0.040 m, omega = 150 rad/s -> maximum acceleration
record("shm-kinematics-p1", 150 ** 2 * 0.040, "m s⁻²")

# p2: omega = 8.0 rad/s, x = 0.030 m -> magnitude of acceleration
record("shm-kinematics-p2", 8.0 ** 2 * 0.030, "m s⁻²")

# p3: A = 60 mm, omega = 3.5 rad/s, x = 25 mm -> speed in m/s
A_p3 = 60 / 1000
x_p3 = 25 / 1000
record("shm-kinematics-p3", 3.5 * math.sqrt(A_p3 ** 2 - x_p3 ** 2), "m s⁻¹")

# p4: a_max = 15 m/s^2, A = 0.12 m -> omega
record("shm-kinematics-p4", math.sqrt(15 / 0.12), "rad s⁻¹")

# p5: tuning fork f = 440 Hz, A = 0.60 mm, t = 0.50 ms -> displacement in mm
omega_p5 = 2 * math.pi * 440
t_p5 = 0.50 / 1000
record("shm-kinematics-p5", 0.60 * math.cos(omega_p5 * t_p5), "mm")

# p6: f = 1.5 Hz, A = 8.0 cm, x = 5.0 cm -> speed in m/s
omega_p6 = 2 * math.pi * 1.5
A_p6 = 8.0 / 100
x_p6 = 5.0 / 100
record("shm-kinematics-p6", omega_p6 * math.sqrt(A_p6 ** 2 - x_p6 ** 2), "m s⁻¹")


# ---------------------------------------------------------------
# Type 6: mass-spring
# ---------------------------------------------------------------

# w: 0.40 kg on k = 25 N/m -> period
record("mass-spring-w", 2 * math.pi * math.sqrt(0.40 / 25), "s")

# p1: 0.25 kg on k = 40 N/m -> period
record("mass-spring-p1", 2 * math.pi * math.sqrt(0.25 / 40), "s")

# p2: 350 kg on k = 2.2e4 N/m -> frequency
T_p2 = 2 * math.pi * math.sqrt(350 / 2.2e4)
record("mass-spring-p2", 1 / T_p2, "Hz")

# p3: 150 g mass, T = 0.80 s -> k
m_p3 = 150 / 1000
record("mass-spring-p3", 4 * math.pi ** 2 * m_p3 / 0.80 ** 2, "N m⁻¹")

# p4: k = 1.5 kN/m, T = 0.12 s -> mass
k_p4 = 1.5 * 1000
record("mass-spring-p4", k_p4 * 0.12 ** 2 / (4 * math.pi ** 2), "kg")

# p5: spring extends 45 mm under 0.30 kg -> k, then T
x_p5 = 45 / 1000
k_p5 = 0.30 * g / x_p5
record("mass-spring-p5", 2 * math.pi * math.sqrt(0.30 / k_p5), "s")

# p6: 0.60 kg trolley, 20 oscillations in 15 s -> T, then k
T_p6 = 15 / 20
record("mass-spring-p6", 4 * math.pi ** 2 * 0.60 / T_p6 ** 2, "N m⁻¹")


# ---------------------------------------------------------------
# Type 7: pendulum
# ---------------------------------------------------------------

# w: L = 0.80 m -> period
record("pendulum-w", 2 * math.pi * math.sqrt(0.80 / g), "s")

# p1: L = 2.5 m -> period
record("pendulum-p1", 2 * math.pi * math.sqrt(2.5 / g), "s")

# p2: L = 0.25 m -> frequency
T_p2 = 2 * math.pi * math.sqrt(0.25 / g)
record("pendulum-p2", 1 / T_p2, "Hz")

# p3: T = 2.00 s -> L
record("pendulum-p3", g * 2.00 ** 2 / (4 * math.pi ** 2), "m")

# p4: L = 45 cm, T = 2.19 s on Mars -> g
L_p4 = 45 / 100
record("pendulum-p4", 4 * math.pi ** 2 * L_p4 / 2.19 ** 2, "m s⁻²")

# p5: L = 1.2 m -> T, then complete oscillations in 2.0 minutes
T_p5 = 2 * math.pi * math.sqrt(1.2 / g)
count_p5 = math.floor(2.0 * 60 / T_p5)
record("pendulum-p5", count_p5, "")

# p6: 25 oscillations in 38.0 s -> T, then L
T_p6 = 38.0 / 25
record("pendulum-p6", g * T_p6 ** 2 / (4 * math.pi ** 2), "m")


# ---------------------------------------------------------------
# Type 8: shm-energy
# ---------------------------------------------------------------

# w: 0.50 kg, omega = 6.0 rad/s, A = 0.080 m -> total energy
record("shm-energy-w", 0.5 * 0.50 * 6.0 ** 2 * 0.080 ** 2, "J")

# p1: k = 80 N/m, A = 0.050 m -> total energy
record("shm-energy-p1", 0.5 * 80 * 0.050 ** 2, "J")

# p2: 0.20 kg, omega = 12 rad/s, A = 0.040 m -> total energy
record("shm-energy-p2", 0.5 * 0.20 * 12 ** 2 * 0.040 ** 2, "J")

# p3: k = 2.5 kN/m, A = 30 mm -> total energy
k_p3 = 2.5 * 1000
A_p3 = 30 / 1000
record("shm-energy-p3", 0.5 * k_p3 * A_p3 ** 2, "J")

# p4: E = 0.045 J, k = 36 N/m -> amplitude
record("shm-energy-p4", math.sqrt(2 * 0.045 / 36), "m")

# p5: 0.30 kg, omega = 8.0 rad/s, A = 0.10 m, x = 0.060 m -> KE
record("shm-energy-p5", 0.5 * 0.30 * 8.0 ** 2 * (0.10 ** 2 - 0.060 ** 2), "J")

# p6: k = 50 N/m, A = 0.12 m, m = 0.40 kg -> E, then v_max
E_p6 = 0.5 * 50 * 0.12 ** 2
record("shm-energy-p6", math.sqrt(2 * E_p6 / 0.40), "m s⁻¹")


# ---------------------------------------------------------------
# Print
# ---------------------------------------------------------------

for question_id, rounded, unit, raw in results:
    print(f"{question_id:30s} {rounded!r:>14}  {unit:10s} (raw {raw!r})")
