#!/usr/bin/env python3
"""Compute every answer in data/momentum-energy.json.

Each answer is printed rounded to 3 s.f. with its question id.
Run: python3 tools/calc_momentum-energy.py
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
# Type 1: momentum-conservation-1d
# ---------------------------------------------------------------

# w: 0.80 kg glider at 3.0 m/s sticks to stationary 1.2 kg glider
record("momentum-conservation-1d-w", 0.80 * 3.0 / (0.80 + 1.2), "m s⁻¹")

# p1: 12 000 kg truck at 2.5 m/s couples with stationary 8000 kg truck
record("momentum-conservation-1d-p1", 12000 * 2.5 / (12000 + 8000), "m s⁻¹")

# p2: 1200 kg cannon fires 8.0 kg shell at 150 m/s; recoil speed
record("momentum-conservation-1d-p2", 8.0 * 150 / 1200, "m s⁻¹")

# p3: 1400 kg car at 54 km/h hits stationary 2200 kg van, stick together
car_speed_p3 = 54 * 1000 / 3600
record("momentum-conservation-1d-p3", 1400 * car_speed_p3 / (1400 + 2200), "m s⁻¹")

# p4: cue ball 0.17 kg at 1.8 m/s hits stationary 0.16 kg red; cue ball continues at 0.40 m/s
record("momentum-conservation-1d-p4", (0.17 * 1.8 - 0.17 * 0.40) / 0.16, "m s⁻¹")

# p5: 60 kg skater at 3.0 m/s east meets 45 kg skater at 2.0 m/s west; hold together
total_p_p5 = 60 * 3.0 - 45 * 2.0
record("momentum-conservation-1d-p5", total_p_p5 / (60 + 45), "m s⁻¹")

# p6: 250 kg bumper car at 1.5 m/s hits stationary 300 kg car; first car rebounds at 0.30 m/s
p_before_p6 = 250 * 1.5
p_car1_after_p6 = 250 * (-0.30)
record("momentum-conservation-1d-p6", (p_before_p6 - p_car1_after_p6) / 300, "m s⁻¹")


# ---------------------------------------------------------------
# Type 2: impulse-and-force
# ---------------------------------------------------------------

# w: 0.45 kg football from rest to 25 m/s in 0.050 s
record("impulse-and-force-w", 0.45 * 25 / 0.050, "N")

# p1: model rocket motor, 12 N for 1.6 s; impulse
record("impulse-and-force-p1", 12 * 1.6, "N s")

# p2: 0.50 kg hammer at 8.0 m/s stops in 0.0025 s
record("impulse-and-force-p2", 0.50 * 8.0 / 0.0025, "N")

# p3: 1500 kg car from 20 m/s to rest in 0.12 s; force in kN
force_p3 = 1500 * 20 / 0.12
record("impulse-and-force-p3", force_p3 / 1000, "kN")

# p4: 0.046 kg golf ball from rest to 70 m/s, average force 6.4 kN; contact time in ms
time_p4 = 0.046 * 70 / 6400
record("impulse-and-force-p4", time_p4 * 1000, "ms")

# p5: 0.16 kg cricket ball arrives at 35 m/s, leaves at 25 m/s opposite way, contact 1.2 ms
delta_p_p5 = 0.16 * (25 - (-35))
record("impulse-and-force-p5", delta_p_p5 / 1.2e-3, "N")

# p6: 0.20 kg ball dropped from 1.8 m, stops in 0.040 s; average resultant force
v_impact_p6 = math.sqrt(2 * g * 1.8)
record("impulse-and-force-p6", 0.20 * v_impact_p6 / 0.040, "N")


# ---------------------------------------------------------------
# Type 3: kinetic-energy-in-collisions
# ---------------------------------------------------------------

def ke(mass, speed):
    """Kinetic energy, ½mv²."""
    return 0.5 * mass * speed ** 2


# w: 2.0 kg trolley at 3.0 m/s sticks to stationary 1.0 kg trolley, move at 2.0 m/s
record("kinetic-energy-in-collisions-w", ke(2.0, 3.0) - ke(3.0, 2.0), "J")

# p1: 1200 kg car at 15 m/s hits stationary 1800 kg car; together at 6.0 m/s
record("kinetic-energy-in-collisions-p1", ke(1200, 15) - ke(3000, 6.0), "J")

# p2: 0.40 kg ball hits wall at 5.0 m/s, rebounds at 3.0 m/s
record("kinetic-energy-in-collisions-p2", ke(0.40, 5.0) - ke(0.40, 3.0), "J")

# p3: 150 g plasticine at 4.0 m/s sticks to 350 g block at rest; move at 1.2 m/s
m_clay_p3 = 150 / 1000
m_block_p3 = 350 / 1000
record("kinetic-energy-in-collisions-p3", ke(m_clay_p3, 4.0) - ke(m_clay_p3 + m_block_p3, 1.2), "J")

# p4: 40 000 kg wagon at 18 km/h couples with stationary 60 000 kg wagon; together at 2.0 m/s; kJ
speed_p4 = 18 * 1000 / 3600
lost_p4 = ke(40000, speed_p4) - ke(100000, 2.0)
record("kinetic-energy-in-collisions-p4", lost_p4 / 1000, "kJ")

# p5: 0.50 kg puck at 6.0 m/s sticks to stationary 1.5 kg puck (find v first)
v_after_p5 = 0.50 * 6.0 / (0.50 + 1.5)
record("kinetic-energy-in-collisions-p5", ke(0.50, 6.0) - ke(2.0, v_after_p5), "J")

# p6: 95 kg player at 4.0 m/s north meets 80 kg player at 1.5 m/s south; hold together
v_after_p6 = (95 * 4.0 - 80 * 1.5) / (95 + 80)
ke_before_p6 = ke(95, 4.0) + ke(80, 1.5)
record("kinetic-energy-in-collisions-p6", ke_before_p6 - ke(175, v_after_p6), "J")


# ---------------------------------------------------------------
# Type 4: momentum-conservation-2d
# ---------------------------------------------------------------

# w: 1000 kg car at 12 m/s east, 1500 kg car at 8.0 m/s north; stick
px_w = 1000 * 12
py_w = 1500 * 8.0
record("momentum-conservation-2d-w", math.hypot(px_w, py_w) / 2500, "m s⁻¹")

# p1: 0.20 kg puck at 3.0 m/s east, 0.20 kg puck at 4.0 m/s north; stick
px_p1 = 0.20 * 3.0
py_p1 = 0.20 * 4.0
record("momentum-conservation-2d-p1", math.hypot(px_p1, py_p1) / 0.40, "m s⁻¹")

# p2: shell at rest explodes: 0.50 kg at 20 m/s east, 0.30 kg at 25 m/s north, 0.50 kg third piece
px_p2 = 0.50 * 20
py_p2 = 0.30 * 25
record("momentum-conservation-2d-p2", math.hypot(px_p2, py_p2) / 0.50, "m s⁻¹")

# p3: 2400 kg motor boat at 36 km/h east, 1200 kg yacht at 54 km/h north; lock together
v_boat_p3 = 36 * 1000 / 3600
v_yacht_p3 = 54 * 1000 / 3600
px_p3 = 2400 * v_boat_p3
py_p3 = 1200 * v_yacht_p3
record("momentum-conservation-2d-p3", math.hypot(px_p3, py_p3) / 3600, "m s⁻¹")

# p4: 250 g clay at 3.2 m/s east, 400 g clay at 1.5 m/s north; stick
m1_p4 = 250 / 1000
m2_p4 = 400 / 1000
px_p4 = m1_p4 * 3.2
py_p4 = m2_p4 * 1.5
record("momentum-conservation-2d-p4", math.hypot(px_p4, py_p4) / (m1_p4 + m2_p4), "m s⁻¹")

# p5: 0.17 kg cue ball at 2.0 m/s hits stationary 0.17 kg red; cue ball leaves at 1.2 m/s at 90°
vx_red_p5 = 0.17 * 2.0 / 0.17
vy_red_p5 = -(0.17 * 1.2) / 0.17
record("momentum-conservation-2d-p5", math.hypot(vx_red_p5, vy_red_p5), "m s⁻¹")

# p6: 1200 kg satellite at 5.0 m/s hits stationary 800 kg debris; satellite leaves at 2.0 m/s at 90°
vx_debris_p6 = 1200 * 5.0 / 800
vy_debris_p6 = -(1200 * 2.0) / 800
record("momentum-conservation-2d-p6", math.hypot(vx_debris_p6, vy_debris_p6), "m s⁻¹")


# ---------------------------------------------------------------
# Type 5: work-done
# ---------------------------------------------------------------

# w: sledge, 80 N rope at 30°, 25 m
record("work-done-w", 80 * 25 * math.cos(math.radians(30)), "J")

# p1: crane lifts 1500 N load 12 m vertically
record("work-done-p1", 1500 * 12, "J")

# p2: lawnmower, 60 N at 40°, 15 m
record("work-done-p2", 60 * 15 * math.cos(math.radians(40)), "J")

# p3: tow truck 2.5 kN over 1.2 km
record("work-done-p3", 2.5e3 * 1.2e3, "J")

# p4: 1800 J pushing wheelbarrow 24 m, handles at 20°; find F
record("work-done-p4", 1800 / (24 * math.cos(math.radians(20))), "N")

# p5: 12 kg crate, friction = 0.30 of weight, dragged 6.0 m at constant speed
friction_p5 = 0.30 * 12 * g
record("work-done-p5", friction_p5 * 6.0, "J")

# p6: 120 N does 1440 J over 16 m; angle
cos_theta_p6 = 1440 / (120 * 16)
record("work-done-p6", math.degrees(math.acos(cos_theta_p6)), "°")


# ---------------------------------------------------------------
# Type 6: kinetic-and-potential-energy
# ---------------------------------------------------------------

# w: 85 kg cyclist + bike with KE 3400 J; speed
record("kinetic-and-potential-energy-w", math.sqrt(2 * 3400 / 85), "m s⁻¹")

# p1: KE of 1200 kg car at 25 m/s
record("kinetic-and-potential-energy-p1", ke(1200, 25), "J")

# p2: GPE gained by 65 kg climber rising 420 m
record("kinetic-and-potential-energy-p2", 65 * g * 420, "J")

# p3: bullet at 400 m/s with KE 1600 J; mass in grams
mass_p3 = 2 * 1600 / 400 ** 2
record("kinetic-and-potential-energy-p3", mass_p3 * 1000, "g")

# p4: 750 kg lift car gains 66 kJ GPE; height
record("kinetic-and-potential-energy-p4", 66e3 / (750 * g), "m")

# p5: 70 kg sprinter, 100 m in 10.0 s; KE at that average speed
v_p5 = 100 / 10.0
record("kinetic-and-potential-energy-p5", ke(70, v_p5), "J")

# p6: 2.4 m³ water (1000 kg/m³) pumped up 15 m; GPE gained
mass_p6 = 2.4 * 1000
record("kinetic-and-potential-energy-p6", mass_p6 * g * 15, "J")


# ---------------------------------------------------------------
# Type 7: energy-conservation
# ---------------------------------------------------------------

# w: roller coaster drops 42 m from rest
record("energy-conservation-w", math.sqrt(2 * g * 42), "m s⁻¹")

# p1: pendulum bob released 0.12 m above lowest point
record("energy-conservation-p1", math.sqrt(2 * g * 0.12), "m s⁻¹")

# p2: ball thrown up at 14 m/s; max height
record("energy-conservation-p2", 14 ** 2 / (2 * g), "m")

# p3: skier descends 120 m from rest; speed in km/h
v_p3 = math.sqrt(2 * g * 120)
record("energy-conservation-p3", v_p3 * 3600 / 1000, "km h⁻¹")

# p4: toy popper launched at 4.2 m/s; height in cm
h_p4 = 4.2 ** 2 / (2 * g)
record("energy-conservation-p4", h_p4 * 100, "cm")

# p5: diver leaves 10 m board at 3.5 m/s upwards; speed at water
v_squared_p5 = 3.5 ** 2 + 2 * g * 10
record("energy-conservation-p5", math.sqrt(v_squared_p5), "m s⁻¹")

# p6: 60 kg skateboarder from rest at 3.2 m; 250 J lost to friction
gpe_p6 = 60 * g * 3.2
ke_bottom_p6 = gpe_p6 - 250
record("energy-conservation-p6", math.sqrt(2 * ke_bottom_p6 / 60), "m s⁻¹")


# ---------------------------------------------------------------
# Type 8: power
# ---------------------------------------------------------------

# w: motor lifts 250 kg load 12 m in 20 s
record("power-w", 250 * g * 12 / 20, "W")

# p1: kettle transfers 540 000 J in 180 s
record("power-p1", 540000 / 180, "W")

# p2: car at 30 m/s against 650 N drag
record("power-p2", 650 * 30, "W")

# p3: cyclist 320 W at 12 m/s; resistive force
record("power-p3", 320 / 12, "N")

# p4: wind turbine 2.4 MW for 5.0 minutes; energy in J
record("power-p4", 2.4e6 * 5.0 * 60, "J")

# p5: 15 kW lift motor raises 900 kg; steady speed
weight_p5 = 900 * g
record("power-p5", 15e3 / weight_p5, "m s⁻¹")

# p6: pump raises 1.5 m³ water through 8.0 m every minute
mass_p6_pump = 1.5 * 1000
energy_p6 = mass_p6_pump * g * 8.0
record("power-p6", energy_p6 / 60, "W")


# ---------------------------------------------------------------
# Type 9: efficiency
# ---------------------------------------------------------------

# w: drill, 85 J in, 68 J useful out; percentage
record("efficiency-w", 68 / 85 * 100, "%")

# p1: kettle 420 kJ in, 360 kJ useful; percentage
record("efficiency-p1", 360 / 420 * 100, "%")

# p2: LED 12 W in, 4.8 W light out; decimal
record("efficiency-p2", 4.8 / 12, "")

# p3: wind turbine 1.8 MW out at 45%; input power in MW
record("efficiency-p3", 1.8 / 0.45, "MW")

# p4: crane uses 4.5 kWh, useful work 1.08e7 J; percentage
input_p4 = 4.5 * 3.6e6
record("efficiency-p4", 1.08e7 / input_p4 * 100, "%")

# p5: pump raises 800 kg water 12 m using 120 kJ; percentage
useful_p5 = 800 * g * 12
record("efficiency-p5", useful_p5 / 120e3 * 100, "%")

# p6: motor draws 2.0 kW, lifts 150 kg at 0.90 m/s; percentage
useful_power_p6 = 150 * g * 0.90
record("efficiency-p6", useful_power_p6 / 2000 * 100, "%")


# ---------------------------------------------------------------
# Print
# ---------------------------------------------------------------

for question_id, rounded, unit, raw in results:
    print(f"{question_id:34s} {rounded!r:>14}  {unit:8s} (raw {raw!r})")
