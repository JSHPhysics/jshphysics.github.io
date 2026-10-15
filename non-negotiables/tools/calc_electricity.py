#!/usr/bin/env python3
"""Compute every answer in data/electricity.json.

Each answer is printed rounded to 3 s.f. with its question id.
Run: python3 tools/calc_electricity.py
"""

import math

# Standard constants from SCHEMA.md
e = 1.60e-19      # C, elementary charge

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


def area_from_diameter(diameter_m):
    """Cross-sectional area of a circular wire from its diameter in metres."""
    radius = diameter_m / 2
    return math.pi * radius ** 2


def parallel(*resistances):
    """Combined resistance of resistors in parallel."""
    total_reciprocal = 0.0
    for resistance in resistances:
        total_reciprocal = total_reciprocal + 1 / resistance
    return 1 / total_reciprocal


# ---------------------------------------------------------------
# Type 1: charge-current-time   Q = It, Q = Ne
# ---------------------------------------------------------------

# w: torch bulb 0.25 A for 2.0 minutes -> charge
record("charge-current-time-w", 0.25 * (2.0 * 60), "C")

# p1: kettle 9.5 A for 180 s -> charge
record("charge-current-time-p1", 9.5 * 180, "C")

# p2: 540 C through a motor in 45 s -> current
record("charge-current-time-p2", 540 / 45, "A")

# p3: LED 18 mA for 5.0 minutes -> charge
record("charge-current-time-p3", 18e-3 * (5.0 * 60), "C")

# p4: 2.4e4 C over 3.0 hours -> mean current
record("charge-current-time-p4", 2.4e4 / (3.0 * 3600), "A")

# p5: 2.5 uA for 4.0 s -> number of electrons (two steps)
charge_p5 = 2.5e-6 * 4.0
record("charge-current-time-p5", charge_p5 / e, "")

# p6: 3.0e20 electrons in 8.0 s -> current (two steps)
charge_p6 = 3.0e20 * e
record("charge-current-time-p6", charge_p6 / 8.0, "A")


# ---------------------------------------------------------------
# Type 2: pd-energy-charge   V = W/Q
# ---------------------------------------------------------------

# w: 54 J transferred by 6.0 C -> p.d.
record("pd-energy-charge-w", 54 / 6.0, "V")

# p1: 230 V heater, 50 C -> energy
record("pd-energy-charge-p1", 230 * 50, "J")

# p2: starter motor 2.4e3 J by 200 C -> p.d.
record("pd-energy-charge-p2", 2.4e3 / 200, "V")

# p3: electron through 2.5 kV -> energy in J
record("pd-energy-charge-p3", e * 2.5e3, "J")

# p4: defibrillator 360 J at 2.0 kV -> charge
record("pd-energy-charge-p4", 360 / 2.0e3, "C")

# p5: desk fan 230 V, 0.50 A for 3.0 minutes -> energy (two steps)
charge_fan = 0.50 * (3.0 * 60)
record("pd-energy-charge-p5", 230 * charge_fan, "J")

# p6: bicycle lamp 360 J in 40 s at 1.5 A -> p.d. (two steps)
charge_lamp = 1.5 * 40
record("pd-energy-charge-p6", 360 / charge_lamp, "V")


# ---------------------------------------------------------------
# Type 3: resistance-v-i   R = V/I
# ---------------------------------------------------------------

# w: 6.0 V, 0.40 A -> R
record("resistance-v-i-w", 6.0 / 0.40, "Ω")

# p1: filament lamp 12 V, 2.5 A -> R
record("resistance-v-i-p1", 12 / 2.5, "Ω")

# p2: immersion heater 230 V, 20 Ω -> current
record("resistance-v-i-p2", 230 / 20, "A")

# p3: 9.0 V across 4.7 kOhm -> current in mA
current_p3 = 9.0 / 4.7e3
record("resistance-v-i-p3", current_p3 * 1e3, "mA")

# p4: table readings (0.50 V, 25 mA), (1.00 V, 50 mA), (1.50 V, 75 mA) -> R
record("resistance-v-i-p4", 1.50 / 75e-3, "Ω")

# p5: heating element 230 V, 2400 C in 2.0 minutes -> R (two steps)
current_p5 = 2400 / (2.0 * 60)
record("resistance-v-i-p5", 230 / current_p5, "Ω")

# p6: graph point (0.35 A, 4.2 V) -> R, then current at 9.0 V (two steps)
resistance_p6 = 4.2 / 0.35
record("resistance-v-i-p6", 9.0 / resistance_p6, "A")


# ---------------------------------------------------------------
# Type 4: resistivity   R = rho L / A
# ---------------------------------------------------------------

# w: constantan rho = 4.9e-7, L = 2.0 m, d = 0.50 mm -> R
area_w = area_from_diameter(0.50e-3)
record("resistivity-w", 4.9e-7 * 2.0 / area_w, "Ω")

# p1: nichrome rho = 1.1e-6, L = 1.5 m, A = 2.0e-7 -> R
record("resistivity-p1", 1.1e-6 * 1.5 / 2.0e-7, "Ω")

# p2: copper rho = 1.7e-8, L = 25 m, A = 1.0e-6 -> R
record("resistivity-p2", 1.7e-8 * 25 / 1.0e-6, "Ω")

# p3: L = 1.2 m, A = 0.25 mm^2, R = 2.3 ohm -> rho
area_p3 = 0.25e-6
record("resistivity-p3", 2.3 * area_p3 / 1.2, "Ω m")

# p4: aluminium rho = 2.8e-8, A = 120 mm^2, R = 0.35 ohm -> L in km
area_p4 = 120e-6
length_p4 = 0.35 * area_p4 / 2.8e-8
record("resistivity-p4", length_p4 / 1e3, "km")

# p5: copper rho = 1.7e-8, L = 4.0 m, R = 0.50 ohm -> diameter in mm (two steps)
area_p5 = 1.7e-8 * 4.0 / 0.50
diameter_p5 = 2 * math.sqrt(area_p5 / math.pi)
record("resistivity-p5", diameter_p5 * 1e3, "mm")

# p6: 2.5 V, 0.80 A, L = 0.60 m, A = 1.3e-7 -> rho (two steps)
resistance_p6 = 2.5 / 0.80
record("resistivity-p6", resistance_p6 * 1.3e-7 / 0.60, "Ω m")


# ---------------------------------------------------------------
# Type 5: resistor-combinations
# ---------------------------------------------------------------

# w: 6.0 || 3.0, in series with 4.0
record("resistor-combinations-w", parallel(6.0, 3.0) + 4.0, "Ω")

# p1: 12 + 18 + 30 in series
record("resistor-combinations-p1", 12 + 18 + 30, "Ω")

# p2: 20 || 30
record("resistor-combinations-p2", parallel(20, 30), "Ω")

# p3: 10 || 15 || 30
record("resistor-combinations-p3", parallel(10, 15, 30), "Ω")

# p4: 4.7 kOhm || 2.2 kOhm -> answer in kOhm
record("resistor-combinations-p4", parallel(4.7e3, 2.2e3) / 1e3, "kΩ")

# p5: (10 + 30) || 60 (two steps)
series_p5 = 10 + 30
record("resistor-combinations-p5", parallel(series_p5, 60), "Ω")

# p6: (12 || 6.0) + 5.0, then || 18 (two steps)
inner_p6 = parallel(12, 6.0) + 5.0
record("resistor-combinations-p6", parallel(inner_p6, 18), "Ω")


# ---------------------------------------------------------------
# Type 6: current-pd-circuits
# ---------------------------------------------------------------

# w: 12 V across 4.0 + 8.0 in series -> p.d. across 8.0
current_w6 = 12 / (4.0 + 8.0)
record("current-pd-circuits-w", current_w6 * 8.0, "V")

# p1: 9.0 V across 10 + 20 + 15 in series -> current
record("current-pd-circuits-p1", 9.0 / (10 + 20 + 15), "A")

# p2: 6.0 V across 12 || 4.0 -> current through 12 ohm branch
record("current-pd-circuits-p2", 6.0 / 12, "A")

# p3: 5.0 V across 2.2 kOhm + 3.3 kOhm in series -> current in mA
current_p3c = 5.0 / (2.2e3 + 3.3e3)
record("current-pd-circuits-p3", current_p3c * 1e3, "mA")

# p4: 12 V across 60 || 40 -> total current from supply
record("current-pd-circuits-p4", 12 / parallel(60, 40), "A")

# p5: 9.0 V, 2.0 in series with (6.0 || 3.0) -> supply current (two steps)
total_p5 = 2.0 + parallel(6.0, 3.0)
record("current-pd-circuits-p5", 9.0 / total_p5, "A")

# p6: 12 V, 3.0 in series with (12 || 6.0) -> p.d. across parallel pair (two steps)
pair_p6 = parallel(12, 6.0)
current_p6c = 12 / (3.0 + pair_p6)
record("current-pd-circuits-p6", current_p6c * pair_p6, "V")


# ---------------------------------------------------------------
# Type 7: power-energy   P = IV = I^2 R = V^2 / R, E = Pt
# ---------------------------------------------------------------

# w: kettle 230 V, 9.0 A -> power
record("power-energy-w", 230 * 9.0, "W")

# p1: toaster element 3.4 A, 66 ohm -> power
record("power-energy-p1", 3.4 ** 2 * 66, "W")

# p2: 12 V across 4.0 ohm lamp -> power
record("power-energy-p2", 12 ** 2 / 4.0, "W")

# p3: 2.4 kW dryer for 1.25 h at 28 p per kWh -> cost in pence
energy_kwh_p3 = 2.4 * 1.25
record("power-energy-p3", energy_kwh_p3 * 28, "p")

# p4: 1.2 W LED at 3.4 V -> current in mA
record("power-energy-p4", 1.2 / 3.4 * 1e3, "mA")

# p5: 1.8 kW heater on 230 V -> resistance (two steps: I then R)
current_p5p = 1.8e3 / 230
record("power-energy-p5", 230 / current_p5p, "Ω")

# p6: motor 4.0 A from 24 V for 5.0 minutes -> energy in J (two steps)
power_p6 = 4.0 * 24
record("power-energy-p6", power_p6 * (5.0 * 60), "J")


# ---------------------------------------------------------------
# Type 8: emf-internal-resistance   emf = I(R + r)
# ---------------------------------------------------------------

# w: emf 12 V, r = 0.50, R = 5.5 -> current
record("emf-internal-resistance-w", 12 / (5.5 + 0.50), "A")

# p1: emf 1.5 V, r = 0.80, I = 0.50 A -> terminal p.d.
record("emf-internal-resistance-p1", 1.5 - 0.50 * 0.80, "V")

# p2: emf 9.0 V, r = 2.0, R = 16 -> current
record("emf-internal-resistance-p2", 9.0 / (16 + 2.0), "A")

# p3: emf 6.0 V, terminal 5.4 V at 1.5 A -> r
record("emf-internal-resistance-p3", (6.0 - 5.4) / 1.5, "Ω")

# p4: open-circuit 12.6 V, terminal 10.8 V at 30 A -> r
record("emf-internal-resistance-p4", (12.6 - 10.8) / 30, "Ω")

# p5: emf 4.5 V, r = 0.40, R = 2.6 -> power in load (two steps)
current_p5e = 4.5 / (2.6 + 0.40)
record("emf-internal-resistance-p5", current_p5e ** 2 * 2.6, "W")

# p6: 0.20 A through 6.0 ohm, 0.30 A through 3.8 ohm -> r (two steps)
terminal_1 = 0.20 * 6.0
terminal_2 = 0.30 * 3.8
record("emf-internal-resistance-p6", (terminal_1 - terminal_2) / (0.30 - 0.20), "Ω")


# ---------------------------------------------------------------
# Type 9: potential-divider   V_out = V_in R2 / (R1 + R2)
# ---------------------------------------------------------------

# w: 12 V across 4.0 kOhm + 2.0 kOhm -> p.d. across 2.0 kOhm
record("potential-divider-w", 12 * 2.0 / (4.0 + 2.0), "V")

# p1: 9.0 V across 100 + 200 -> p.d. across 200
record("potential-divider-p1", 9.0 * 200 / (100 + 200), "V")

# p2: 5.0 V across 1.5 kOhm + 3.5 kOhm -> p.d. across 1.5 kOhm
record("potential-divider-p2", 5.0 * 1.5 / (1.5 + 3.5), "V")

# p3: 6.0 V, R1 = 470 ohm, want 2.0 V across R2 -> R2
# 2.0 = 6.0 R2 / (470 + R2)  ->  R2 = 2.0 * 470 / (6.0 - 2.0)
record("potential-divider-p3", 2.0 * 470 / (6.0 - 2.0), "Ω")

# p4: LDR 400 ohm in series with 1.2 kOhm across 9.0 V -> p.d. across LDR
record("potential-divider-p4", 9.0 * 400 / (400 + 1.2e3), "V")

# p5: thermistor 5.0 kOhm at 20 C, 9.0 V, want 3.0 V across fixed R -> R in kOhm
# 3.0 = 9.0 R / (5.0 + R)  ->  R = 3.0 * 5.0 / (9.0 - 3.0)
record("potential-divider-p5", 3.0 * 5.0 / (9.0 - 3.0), "kΩ")

# p6: 6.0 V, R1 = 1.8 kOhm, 2.4 V across R2 -> R2 in kOhm (two steps: I then R2)
pd_across_r1 = 6.0 - 2.4
current_p6d = pd_across_r1 / 1.8e3
record("potential-divider-p6", 2.4 / current_p6d / 1e3, "kΩ")


# ---------------------------------------------------------------
# Type 10: drift-velocity   I = nAve
# ---------------------------------------------------------------

# w: copper A = 1.0e-6, n = 8.5e28, I = 3.0 A -> v
record("drift-velocity-w", 3.0 / (8.5e28 * 1.0e-6 * e), "m s⁻¹")

# p1: I = 0.50 A, n = 8.5e28, A = 2.5e-7 -> v
record("drift-velocity-p1", 0.50 / (8.5e28 * 2.5e-7 * e), "m s⁻¹")

# p2: silver n = 5.8e28, A = 4.0e-7, v = 1.2e-4 -> I
record("drift-velocity-p2", 5.8e28 * 4.0e-7 * e * 1.2e-4, "A")

# p3: I = 2.0 A, A = 1.5e-6, v = 1.5e-4 -> n
record("drift-velocity-p3", 2.0 / (1.5e-6 * e * 1.5e-4), "m⁻³")

# p4: I = 1.5 A, d = 0.80 mm, n = 8.5e28 -> v
area_p4d = area_from_diameter(0.80e-3)
record("drift-velocity-p4", 1.5 / (8.5e28 * area_p4d * e), "m s⁻¹")

# p5: R = 2.0 ohm across 3.0 V, n = 8.5e28, A = 2.0e-7 -> v (two steps)
current_p5d = 3.0 / 2.0
record("drift-velocity-p5", current_p5d / (8.5e28 * 2.0e-7 * e), "m s⁻¹")

# p6: tungsten d = 0.030 mm, I = 250 mA, n = 3.4e28 -> v (two steps)
area_p6d = area_from_diameter(0.030e-3)
record("drift-velocity-p6", 250e-3 / (3.4e28 * area_p6d * e), "m s⁻¹")


# ---------------------------------------------------------------
# Print
# ---------------------------------------------------------------

for question_id, rounded, unit, raw in results:
    print(f"{question_id:32s} {rounded!r:>14}  {unit:8s} (raw {raw!r})")
