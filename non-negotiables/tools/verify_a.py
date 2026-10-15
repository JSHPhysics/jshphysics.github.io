#!/usr/bin/env python3
"""
Independent check of practice questions p2, p5 and p6 for:
measurements, kinematics, forces, momentum-energy, materials.

Every value below was worked out from the question text alone, using the
standard constants in SCHEMA.md, BEFORE looking at the stored answer.
The stored answers are only loaded at the very end, for comparison.

Run:  python3 tools/verify_a.py
"""

import json
import math
import os

# ---------------------------------------------------------------------------
# Standard constants (SCHEMA.md)
# ---------------------------------------------------------------------------
g = 9.81          # m s^-2

# Where the data lives (relative to this script)
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")

# My independently computed values, collected here: {question id: value}
mine = {}


def record(question_id, value):
    """Store my own computed value for a question id."""
    mine[question_id] = value


# ===========================================================================
# MEASUREMENTS
# ===========================================================================

# --- si-prefixes -----------------------------------------------------------
# p2: 3.2 kN in newtons
record("si-prefixes-p2", 3.2 * 1e3)

# p5: 35.8 Mm in kilometres
distance_m = 35.8 * 1e6
record("si-prefixes-p5", distance_m / 1e3)

# p6: 0.062 mA in microamps
current_a = 0.062 * 1e-3
record("si-prefixes-p6", current_a / 1e-6)

# --- derived-units ---------------------------------------------------------
# p2: 55 litres to m^3 (1 litre = 1e-3 m^3)
record("derived-units-p2", 55 * 1e-3)

# p5: 100 m in 9.86 s, speed in km/h
speed_ms = 100 / 9.86
record("derived-units-p5", speed_ms * 3.6)

# p6: 12.4 kg, 642 cm^3 -> kg m^-3
volume_m3 = 642 * 1e-6
record("derived-units-p6", 12.4 / volume_m3)

# --- single-uncertainty ----------------------------------------------------
# p2: 2.46 mm +/- 0.005 mm -> % uncertainty
record("single-uncertainty-p2", 0.005 / 2.46 * 100)

# p5: 10 oscillations in 18.4 s +/- 0.2 s; % uncertainty in T is the same as in 10T
record("single-uncertainty-p5", 0.2 / 18.4 * 100)

# p6: five readings; uncertainty = half the range; % of the mean
readings = [0.244, 0.251, 0.247, 0.249, 0.254]
mean_current = sum(readings) / len(readings)
half_range = (max(readings) - min(readings)) / 2
record("single-uncertainty-p6", half_range / mean_current * 100)

# --- sums-differences ------------------------------------------------------
# p2: temperature rise, two readings each +/- 0.5 -> add absolute uncertainties
record("sums-differences-p2", 0.5 + 0.5)

# p5: mass of water = 0.428 - 0.176; each reading 0.5 %; convert to absolute, add
abs_full = 0.005 * 0.428
abs_empty = 0.005 * 0.176
mass_water = 0.428 - 0.176
record("sums-differences-p5", (abs_full + abs_empty) / mass_water * 100)

# p6: terminal pd = 9.0 - 2.4; absolute uncertainties add
terminal_pd = 9.0 - 2.4
record("sums-differences-p6", (0.1 + 0.1) / terminal_pd * 100)

# --- products-quotients ----------------------------------------------------
# p2: P = IV -> add % uncertainties
record("products-quotients-p2", (0.01 / 0.42 + 0.1 / 11.8) * 100)

# p5: p = F/(l w) -> add all three % uncertainties
record("products-quotients-p5", (2 / 120 + 0.005 / 0.250 + 0.005 / 0.120) * 100)

# p6: W = F s; absolute uncertainty in joules
work = 45 * 2.4
percent_w = (1 / 45 + 0.1 / 2.4)
record("products-quotients-p6", work * percent_w)

# --- powers ----------------------------------------------------------------
# p2: g = 4 pi^2 L / T^2 -> %L + 2 %T
record("powers-p2", 0.5 + 2 * 1.5)

# p5: P = V^2 / R -> 2 %V + %R
record("powers-p5", (2 * 0.2 / 12.0 + 1 / 36) * 100)

# p6: V = 4/3 pi r^3; % uncertainty = 3 x (0.05/2.50); absolute in cm^3
volume_ball = (4 / 3) * math.pi * 2.50 ** 3
record("powers-p6", volume_ball * 3 * (0.05 / 2.50))

# --- graph-gradient --------------------------------------------------------
# p2: k = gradient of F-x line
record("graph-gradient-p2", (20.0 - 5.0) / (0.080 - 0.020))

# p5: V = emf - I r; gradient = -r; emf = V + I r
r_internal = -(1.08 - 1.40) / (0.60 - 0.20)
emf = 1.40 + 0.20 * r_internal
record("graph-gradient-p5", emf)

# p6: P t = m c dT -> gradient dT/dt = P/(m c) -> c = P / (m x gradient)
gradient_t = (36.0 - 24.0) / (240 - 60)
record("graph-gradient-p6", 50 / (0.50 * gradient_t))

# --- percentage-error ------------------------------------------------------
# p2: (measured - accepted)/accepted
record("percentage-error-p2", (1.80e-8 - 1.68e-8) / 1.68e-8 * 100)

# p5: g from pendulum, then % error vs 9.81 (magnitude)
g_measured = 4 * math.pi ** 2 * 0.500 / 1.45 ** 2
record("percentage-error-p5", abs(g_measured - 9.81) / 9.81 * 100)

# p6: R = V/I vs 22 ohm
r_measured = 4.80 / 0.210
record("percentage-error-p6", abs(r_measured - 22) / 22 * 100)


# ===========================================================================
# KINEMATICS
# ===========================================================================

# --- speed-velocity-acceleration -------------------------------------------
# p2: 42 m in 15 s
record("speed-velocity-acceleration-p2", 42 / 15)

# p5: 12 km at 8.0 m/s, then 6.0 km in 10 min; average speed = total d / total t
t1 = 12000 / 8.0
t2 = 10 * 60
record("speed-velocity-acceleration-p5", (12000 + 6000) / (t1 + t2))

# p6: 54 km/h -> 90 km/h in 8.0 s
u = 54 / 3.6
v = 90 / 3.6
record("speed-velocity-acceleration-p6", (v - u) / 8.0)

# --- suvat-one-equation ----------------------------------------------------
# p2: s = 1/2 a t^2 from rest
record("suvat-one-equation-p2", 0.5 * 30 * 4.0 ** 2)

# p5: s = 1/2 (u + v) t -> t = 2 s / v, in ms
t_barrel = 2 * 0.60 / 320
record("suvat-one-equation-p5", t_barrel * 1e3)

# p6: v^2 = 2 a s -> a = v^2 / 2 s
record("suvat-one-equation-p6", (2.0e7) ** 2 / (2 * 0.050))

# --- suvat-two-step --------------------------------------------------------
# p2: accelerate 0 -> 9 in 3 s (s = 1/2 (u+v) t), then constant 9 m/s for 7 s
s_accel = 0.5 * (0 + 9.0) * 3.0
s_const = 9.0 * 7.0
record("suvat-two-step-p2", s_accel + s_const)

# p5: s = 1/2 a t^2 -> a; then v = a t
a_sled = 2 * 180 / 6.0 ** 2
record("suvat-two-step-p5", a_sled * 6.0)

# p6: v^2 = 2 a s -> a from first 0.5 m; then v at 2.0 m
a_ramp = 1.2 ** 2 / (2 * 0.50)
record("suvat-two-step-p6", math.sqrt(2 * a_ramp * 2.0))

# --- vertical-motion -------------------------------------------------------
# p2: v = g t
record("vertical-motion-p2", g * 3.2)

# p5: up and back to same height: t = 2 u / g
record("vertical-motion-p5", 2 * 14 / g)

# p6: s = u t - 1/2 g t^2 with s = -30 (up positive); solve quadratic
# 1/2 g t^2 - 12 t - 30 = 0
a_q = 0.5 * g
b_q = -12
c_q = -30
t_ground = (-b_q + math.sqrt(b_q ** 2 - 4 * a_q * c_q)) / (2 * a_q)
record("vertical-motion-p6", t_ground)

# --- projectiles-horizontal ------------------------------------------------
# p2: x = u t
record("projectiles-horizontal-p2", 60 * 4.9)

# p5: t from h = 1/2 g t^2; then x = u t
t_fall = math.sqrt(2 * 40 / g)
record("projectiles-horizontal-p5", 25 * t_fall)

# p6: vy^2 = 2 g h; speed = sqrt(vx^2 + vy^2)
vy_sq = 2 * g * 20
record("projectiles-horizontal-p6", math.sqrt(15 ** 2 + vy_sq))

# --- projectiles-angle -----------------------------------------------------
# p2: uy = u sin(theta); time to top = uy / g
uy = 35 * math.sin(math.radians(40))
record("projectiles-angle-p2", uy / g)

# p5: range on level ground: t = 2 uy / g, x = ux t
uy = 28 * math.sin(math.radians(38))
ux = 28 * math.cos(math.radians(38))
record("projectiles-angle-p5", ux * 2 * uy / g)

# p6: same, 22 m/s at 25 deg
uy = 22 * math.sin(math.radians(25))
ux = 22 * math.cos(math.radians(25))
record("projectiles-angle-p6", ux * 2 * uy / g)

# --- velocity-time-graphs --------------------------------------------------
# p2: trapezium area
record("velocity-time-graphs-p2", 0.5 * (6.0 + 18) * 4.0)

# p5: area = 1/2 x 10 x v + 30 v = 35 v = 700
record("velocity-time-graphs-p5", 700 / (0.5 * 10 + 30))

# p6: triangle area / total time
area = 0.5 * 15 * 9.0
record("velocity-time-graphs-p6", area / 15)

# --- displacement-time-graphs ----------------------------------------------
# p2: speed = |gradient|
record("displacement-time-graphs-p2", 12 / 8.0)

# p5: total distance = 30 out + 30 back; / 15 s
record("displacement-time-graphs-p5", (30 + 30) / 15)

# p6: v1 = 150/10, v2 = (390-150)/10; difference
v1 = 150 / 10
v2 = (390 - 150) / 10
record("displacement-time-graphs-p6", v2 - v1)


# ===========================================================================
# FORCES
# ===========================================================================

# --- weight-and-mass -------------------------------------------------------
# p2: W = m g_mars
record("weight-and-mass-p2", 899 * 3.71)

# p5: m = W_moon / g_moon; W_earth = m g
m_container = 73.6 / 1.62
record("weight-and-mass-p5", m_container * g)

# p6: m = 1570 / g; W_jupiter = m x 24.8
m_probe = 1570 / g
record("weight-and-mass-p6", m_probe * 24.8)

# --- resolving-forces ------------------------------------------------------
# p2: horizontal component = F cos 35
record("resolving-forces-p2", 120 * math.cos(math.radians(35)))

# p5: handle at 28 deg to the wall; perpendicular component = F sin 28 = 32
# along the wall = F cos 28 = 32 / tan 28
record("resolving-forces-p5", 32 / math.tan(math.radians(28)))

# p6: Pythagoras: perpendicular = sqrt(T^2 - along^2)
record("resolving-forces-p6", math.sqrt(250 ** 2 - 150 ** 2))

# --- resultant-perpendicular -----------------------------------------------
# p2: angle with horizontal = atan(vertical / horizontal)
record("resultant-perpendicular-p2", math.degrees(math.atan(60 / 35)))

# p5: weight = 3.2 g; resultant = sqrt(W^2 + 48^2)
w_bucket = 3.2 * g
record("resultant-perpendicular-p5", math.sqrt(w_bucket ** 2 + 48 ** 2))

# p6: cos(theta) = 3.0 / 5.0 (3 kN is adjacent to the resultant)
record("resultant-perpendicular-p6", math.degrees(math.acos(3.0 / 5.0)))

# --- newton-second-law -----------------------------------------------------
# p2: F = m a
record("newton-second-law-p2", 70 * 4.2)

# p5: a = 30/4; thrust = m a + friction
a_sled = 30 / 4.0
record("newton-second-law-p5", 450 * a_sled + 600)

# p6: a = v^2 / (2 s); F = m a
a_brake = 25 ** 2 / (2 * 50)
record("newton-second-law-p6", 1500 * a_brake)

# --- connected-bodies ------------------------------------------------------
# p2: tension accelerates the trailer only: T = m_trailer a
record("connected-bodies-p2", 1500 * 0.80)

# p5: Atwood: a = (m2 - m1) g / (m1 + m2); T = m1 (g + a)
a_atwood = (6.0 - 4.0) * g / (6.0 + 4.0)
record("connected-bodies-p5", 4.0 * (g + a_atwood))

# p6: a = m_hang g / (m_total); T = m_table a
a_table = 1.5 * g / (2.0 + 1.5)
record("connected-bodies-p6", 2.0 * a_table)

# --- inclines --------------------------------------------------------------
# p2: a = g sin 20
record("inclines-p2", g * math.sin(math.radians(20)))

# p5: constant speed: T = m g sin 20 + friction
record("inclines-p5", 30 * g * math.sin(math.radians(20)) + 45)

# p6: F = m a + m g sin 6 + resistive; in kN
f_drive = 1400 * 1.2 + 1400 * g * math.sin(math.radians(6.0)) + 500
record("inclines-p6", f_drive / 1e3)

# --- lifts -----------------------------------------------------------------
# p2: constant speed -> R = m g
record("lifts-p2", 120 * g)

# p5: T = (m) (g + a) in kN
record("lifts-p5", (800 + 250) * (g + 1.2) / 1e3)

# p6: slowing while moving up: a = -3.0/2.5 (downward); R = m (g + a)
a_lift = -3.0 / 2.5
record("lifts-p6", 68 * (g + a_lift))

# --- moments ---------------------------------------------------------------
# p2: 400 x 1.5 = W x 2.0
record("moments-p2", 400 * 1.5 / 2.0)

# p5: moments about the left support: R_right x 4.0 = 600 x 1.0 + 200 x 2.0
record("moments-p5", (600 * 1.0 + 200 * 2.0) / 4.0)

# p6: pivot 0.90 m from end A; plank centre at 1.5 m from A, i.e. 0.60 m beyond pivot
# F x 0.90 = W x 0.60
w_plank = 12 * g
record("moments-p6", w_plank * 0.60 / 0.90)


# ===========================================================================
# MOMENTUM AND ENERGY
# ===========================================================================

# --- momentum-conservation-1d ----------------------------------------------
# p2: recoil speed = m_shell v_shell / m_cannon
record("momentum-conservation-1d-p2", 8.0 * 150 / 1200)

# p5: east positive; (60 x 3 - 45 x 2) / 105
p_total = 60 * 3.0 - 45 * 2.0
record("momentum-conservation-1d-p5", abs(p_total) / (60 + 45))

# p6: 250 x 1.5 = 250 x (-0.30) + 300 v
record("momentum-conservation-1d-p6", (250 * 1.5 - 250 * (-0.30)) / 300)

# --- impulse-and-force -----------------------------------------------------
# p2: F = m v / t
record("impulse-and-force-p2", 0.50 * 8.0 / 0.0025)

# p5: change in velocity = 35 - (-25) = 60; F = m dv / t
record("impulse-and-force-p5", 0.16 * (35 + 25) / 1.2e-3)

# p6: v on impact = sqrt(2 g h); F = m v / t
v_impact = math.sqrt(2 * g * 1.8)
record("impulse-and-force-p6", 0.20 * v_impact / 0.040)

# --- kinetic-energy-in-collisions ------------------------------------------
# p2: KE lost = 1/2 m (u^2 - v^2)
record("kinetic-energy-in-collisions-p2", 0.5 * 0.40 * (5.0 ** 2 - 3.0 ** 2))

# p5: v after = 0.5 x 6 / 2.0; KE before - after
v_after = 0.50 * 6.0 / (0.50 + 1.5)
ke_before = 0.5 * 0.50 * 6.0 ** 2
ke_after = 0.5 * 2.0 * v_after ** 2
record("kinetic-energy-in-collisions-p5", ke_before - ke_after)

# p6: north positive; v after = (95 x 4 - 80 x 1.5) / 175
v_after = (95 * 4.0 - 80 * 1.5) / (95 + 80)
ke_before = 0.5 * 95 * 4.0 ** 2 + 0.5 * 80 * 1.5 ** 2
ke_after = 0.5 * 175 * v_after ** 2
record("kinetic-energy-in-collisions-p6", ke_before - ke_after)

# --- momentum-conservation-2d ----------------------------------------------
# p2: third piece momentum balances the other two (perpendicular)
px = 0.50 * 20
py = 0.30 * 25
p3 = math.sqrt(px ** 2 + py ** 2)
record("momentum-conservation-2d-p2", p3 / 0.50)

# p5: red ball momentum = vector (p_initial, -p_cue_perp)
p_init = 0.17 * 2.0
p_cue = 0.17 * 1.2
p_red = math.sqrt(p_init ** 2 + p_cue ** 2)
record("momentum-conservation-2d-p5", p_red / 0.17)

# p6: same structure
p_init = 1200 * 5.0
p_sat = 1200 * 2.0
p_debris = math.sqrt(p_init ** 2 + p_sat ** 2)
record("momentum-conservation-2d-p6", p_debris / 800)

# --- work-done -------------------------------------------------------------
# p2: W = F s cos 40
record("work-done-p2", 60 * 15 * math.cos(math.radians(40)))

# p5: friction = 0.30 m g; W = f s
friction = 0.30 * 12 * g
record("work-done-p5", friction * 6.0)

# p6: cos(theta) = W / (F s)
record("work-done-p6", math.degrees(math.acos(1440 / (120 * 16))))

# --- kinetic-and-potential-energy ------------------------------------------
# p2: GPE = m g h
record("kinetic-and-potential-energy-p2", 65 * g * 420)

# p5: v = 100 / 10; KE = 1/2 m v^2
v_sprint = 100 / 10.0
record("kinetic-and-potential-energy-p5", 0.5 * 70 * v_sprint ** 2)

# p6: m = rho V; GPE = m g h
m_water = 1000 * 2.4
record("kinetic-and-potential-energy-p6", m_water * g * 15)

# --- energy-conservation ---------------------------------------------------
# p2: h = u^2 / (2 g)
record("energy-conservation-p2", 14 ** 2 / (2 * g))

# p5: v^2 = u^2 + 2 g h
record("energy-conservation-p5", math.sqrt(3.5 ** 2 + 2 * g * 10))

# p6: 1/2 m v^2 = m g h - 250
ke_bottom = 60 * g * 3.2 - 250
record("energy-conservation-p6", math.sqrt(2 * ke_bottom / 60))

# --- power -----------------------------------------------------------------
# p2: P = F v
record("power-p2", 650 * 30)

# p5: v = P / (m g)
record("power-p5", 15e3 / (900 * g))

# p6: mass per second = 1500 / 60; P = (m/t) g h
mass_per_s = 1000 * 1.5 / 60
record("power-p6", mass_per_s * g * 8.0)

# --- efficiency ------------------------------------------------------------
# p2: 4.8 / 12 as decimal
record("efficiency-p2", 4.8 / 12)

# p5: useful = m g h; / 120 kJ, as %
useful = 800 * g * 12
record("efficiency-p5", useful / 120e3 * 100)

# p6: useful power = m g v; / 2.0 kW, as %
useful_p = 150 * g * 0.90
record("efficiency-p6", useful_p / 2.0e3 * 100)


# ===========================================================================
# MATERIALS
# ===========================================================================

# --- density ---------------------------------------------------------------
# p2: rho = m / V
record("density-p2", 12.4 / 6.42e-4)

# p5: V = m / rho; L = V / A (A = 0.50 mm^2 = 0.50e-6 m^2)
v_wire = 0.0250 / 8960
record("density-p5", v_wire / 0.50e-6)

# p6: V = 4/3 pi R^3; rho = M / V
v_mars = (4 / 3) * math.pi * (3.39e6) ** 3
record("density-p6", 6.42e23 / v_mars)

# --- hookes-law ------------------------------------------------------------
# p2: F = k x
record("hookes-law-p2", 3500 * 0.020)

# p5: x = m g / k
record("hookes-law-p5", 0.350 * g / 70)

# p6: k = F / (L - L0)
record("hookes-law-p6", 48 / (0.410 - 0.250))

# --- springs-combined ------------------------------------------------------
# p2: series: 1/k = 1/40 + 1/60
record("springs-combined-p2", 1 / (1 / 40 + 1 / 60))

# p5: parallel: k = 3 x 45; x = m g / k
k_par = 3 * 45
record("springs-combined-p5", 0.60 * g / k_par)

# p6: series: k = 1/(1/120 + 1/180); F = k x
k_ser = 1 / (1 / 120 + 1 / 180)
record("springs-combined-p6", k_ser * 0.090)

# --- young-modulus ---------------------------------------------------------
# p2: E = stress / strain
record("young-modulus-p2", 1.2e8 / 8.0e-4)

# p5: E = F L / (A x), A = pi (d/2)^2
a_wire = math.pi * (0.60e-3 / 2) ** 2
record("young-modulus-p5", 40 * 1.80 / (a_wire * 2.1e-3))

# p6: F = E A x / L
a_line = math.pi * (0.40e-3 / 2) ** 2
record("young-modulus-p6", 3.0e9 * a_line * 12e-3 / 1.5)

# --- wire-extension --------------------------------------------------------
# p2: x = F L / (E A)
record("wire-extension-p2", 9000 * 40 / (2.0e11 * 3.0e-4))

# p5: F = m g; A = pi (3.0 mm)^2; x in mm
a_rope = math.pi * (6.0e-3 / 2) ** 2
x_rope = 12 * g * 10 / (3.0e9 * a_rope)
record("wire-extension-p5", x_rope * 1e3)

# p6: L = x E A / F
a_string = math.pi * (0.25e-3 / 2) ** 2
record("wire-extension-p6", 2.0e-3 * 2.0e11 * a_string / 70)

# --- elastic-energy --------------------------------------------------------
# p2: E = 1/2 k x^2
record("elastic-energy-p2", 0.5 * 800 * 0.050 ** 2)

# p5: x = m g / k; E = 1/2 k x^2
x_spring = 0.50 * g / 60
record("elastic-energy-p5", 0.5 * 60 * x_spring ** 2)

# p6: x = F / k; E = 1/2 k x^2  (= F^2 / 2k)
x_pen = 32 / 400
record("elastic-energy-p6", 0.5 * 400 * x_pen ** 2)

# --- pressure --------------------------------------------------------------
# p2: p = rho g h
record("pressure-p2", 1000 * g * 1.8)

# p5: total = atmospheric + rho g h
record("pressure-p5", 1.01e5 + 850 * g * 3.2)

# p6: F = rho g h A
record("pressure-p6", 1030 * g * 60 * 0.80)

# --- upthrust --------------------------------------------------------------
# p2: U = rho_air g V
record("upthrust-p2", 1.2 * g * 0.50)

# p5: V = m / rho_al; reading = W - U
v_block = 0.540 / 2700
upthrust = 1000 * g * v_block
record("upthrust-p5", 0.540 * g - upthrust)

# p6: floating: m g = rho g A d -> d = m / (rho A)
record("upthrust-p6", 1.6 / (1000 * 0.020))

# --- stokes-terminal -------------------------------------------------------
# p2: F = 6 pi eta r v
record("stokes-terminal-p2", 6 * math.pi * 1.8e-5 * 0.50e-3 * 4.0)

# p5: ignoring upthrust: v = 2 r^2 rho g / (9 eta)
r_fog = 10e-6
record("stokes-terminal-p5", 2 * r_fog ** 2 * 1000 * g / (9 * 1.8e-5))

# p6: with upthrust: v = 2 r^2 (rho_s - rho_f) g / (9 eta)
r_bead = 0.80e-3
record("stokes-terminal-p6", 2 * r_bead ** 2 * (2500 - 900) * g / (9 * 0.25))


# ===========================================================================
# Comparison with stored answers (loaded only now)
# ===========================================================================

def load_stored():
    """Return {question id: (value, unit)} for every practice question in my five files."""
    stored = {}
    files = ["measurements", "kinematics", "forces", "momentum-energy", "materials"]
    for name in files:
        path = os.path.join(DATA_DIR, name + ".json")
        with open(path) as handle:
            topic = json.load(handle)
        for calc_type in topic["types"]:
            for question in calc_type["practice"]:
                stored[question["id"]] = (question["answer"]["value"], question["answer"]["unit"])
    return stored


def main():
    stored = load_stored()
    checked = 0
    matches = 0
    mismatches = []

    for question_id in mine:
        my_value = mine[question_id]
        stored_value, unit = stored[question_id]
        checked = checked + 1

        # Relative difference against the stored value
        if stored_value == 0:
            rel = abs(my_value - stored_value)
        else:
            rel = abs(my_value - stored_value) / abs(stored_value)

        if rel <= 0.01:
            status = "OK"
            matches = matches + 1
        else:
            status = "MISMATCH"
            mismatches.append(question_id)

        print(f"{status:9s} {question_id:38s} mine={my_value:<14.6g} stored={stored_value:<14.6g} {unit}")

    print()
    print(f"checked: {checked}   matches: {matches}   mismatches: {len(mismatches)}")
    for question_id in mismatches:
        print("  MISMATCH:", question_id)


if __name__ == "__main__":
    main()
