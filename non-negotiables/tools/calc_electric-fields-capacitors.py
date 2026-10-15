#!/usr/bin/env python3
"""Compute every answer in data/electric-fields-capacitors.json.

Each answer is printed rounded to 3 s.f. with its question id.
Run: python3 tools/calc_electric-fields-capacitors.py
"""

import math

# Standard constants from SCHEMA.md
e = 1.60e-19          # C
eps0 = 8.85e-12       # F m^-1
m_e = 9.11e-31        # kg
m_p = 1.67e-27        # kg
u = 1.66e-27          # kg
eV = 1.60e-19         # J

# Coulomb constant derived from the standard eps0
k = 1 / (4 * math.pi * eps0)

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
# Type 1: coulombs-law
# ---------------------------------------------------------------

# w: +3.0 uC and +5.0 uC, 0.20 m apart
record("coulombs-law-w", k * 3.0e-6 * 5.0e-6 / 0.20 ** 2, "N")

# p1: +40 nC and -25 nC, 0.15 m apart (magnitude)
record("coulombs-law-p1", k * 40e-9 * 25e-9 / 0.15 ** 2, "N")

# p2: electron and proton, 5.3e-11 m apart
record("coulombs-law-p2", k * e * e / (5.3e-11) ** 2, "N")

# p3: two toner particles 2.0 nC each, 3.0 mm apart
separation_p3 = 3.0e-3
record("coulombs-law-p3", k * 2.0e-9 * 2.0e-9 / separation_p3 ** 2, "N")

# p4: Na+ and Cl- ions, 282 pm apart
separation_p4 = 282e-12
record("coulombs-law-p4", k * e * e / separation_p4 ** 2, "N")

# p5: two spheres each with 2.5e10 excess electrons, 8.0 cm apart
charge_p5 = 2.5e10 * e
separation_p5 = 0.080
record("coulombs-law-p5", k * charge_p5 * charge_p5 / separation_p5 ** 2, "N")

# p6: alpha (+2e) and gold nucleus (+79e); force 2.0 N -> separation
charge_alpha = 2 * e
charge_gold = 79 * e
separation_p6 = math.sqrt(k * charge_alpha * charge_gold / 2.0)
record("coulombs-law-p6", separation_p6, "m")


# ---------------------------------------------------------------
# Type 2: field-strength-point-charge
# ---------------------------------------------------------------

# w: E at 0.30 m from +2.0 uC
record("field-strength-point-charge-w", k * 2.0e-6 / 0.30 ** 2, "N C⁻¹")

# p1: E at 1.2 m from +60 nC
record("field-strength-point-charge-p1", k * 60e-9 / 1.2 ** 2, "N C⁻¹")

# p2: E = F/Q, F = 3.2e-5 N on +4.0 nC
record("field-strength-point-charge-p2", 3.2e-5 / 4.0e-9, "N C⁻¹")

# p3: E at 1.0 nm from a proton
record("field-strength-point-charge-p3", k * e / (1.0e-9) ** 2, "N C⁻¹")

# p4: Q from E = 5.0e4 at r = 0.20 m, in nC
charge_p4 = 5.0e4 * 0.20 ** 2 / k
record("field-strength-point-charge-p4", charge_p4 / 1e-9, "nC")

# p5: r where E = 3.0e6 from Q = 8.0 uC
record("field-strength-point-charge-p5", math.sqrt(k * 8.0e-6 / 3.0e6), "m")

# p6: E at 0.25 m from +3.0 uC, then force on -20 nC
field_p6 = k * 3.0e-6 / 0.25 ** 2
record("field-strength-point-charge-p6", field_p6 * 20e-9, "N")


# ---------------------------------------------------------------
# Type 3: uniform-field-parallel-plates
# ---------------------------------------------------------------

# w: 2.0 kV across 4.0 cm, force on 3.0 nC
field_w3 = 2000 / 0.040
record("uniform-field-parallel-plates-w", field_w3 * 3.0e-9, "N")

# p1: 600 V across 0.050 m
record("uniform-field-parallel-plates-p1", 600 / 0.050, "V m⁻¹")

# p2: F = EQ, E = 2.5e4, Q = 8.0 nC
record("uniform-field-parallel-plates-p2", 2.5e4 * 8.0e-9, "N")

# p3: 1500 V across 8.0 mm
record("uniform-field-parallel-plates-p3", 1500 / 8.0e-3, "V m⁻¹")

# p4: V = Ed, E = 3.2e5, d = 5.0 mm
record("uniform-field-parallel-plates-p4", 3.2e5 * 5.0e-3, "V")

# p5: electron, 250 V across 20 mm -> acceleration
field_p5 = 250 / 20e-3
force_p5 = e * field_p5
record("uniform-field-parallel-plates-p5", force_p5 / m_e, "m s⁻²")

# p6: Ar+ ion (mass 6.64e-26 kg), 1.2 kV across 3.0 cm -> acceleration
field_p6 = 1200 / 0.030
force_p6 = e * field_p6
record("uniform-field-parallel-plates-p6", force_p6 / 6.64e-26, "m s⁻²")


# ---------------------------------------------------------------
# Type 4: electric-potential-energy
# ---------------------------------------------------------------

# w: V at 0.50 m from +4.0 uC
record("electric-potential-energy-w", k * 4.0e-6 / 0.50, "V")

# p1: V at 0.10 m from +25 nC
record("electric-potential-energy-p1", k * 25e-9 / 0.10, "V")

# p2: W = Q dV, Q = 3.0 uC, dV = 250 V
record("electric-potential-energy-p2", 3.0e-6 * 250, "J")

# p3: magnitude of Ep of electron-proton pair at 53 pm
record("electric-potential-energy-p3", k * e * e / 53e-12, "J")

# p4: r where V = 90 kV from +5.0 uC
record("electric-potential-energy-p4", k * 5.0e-6 / 90e3, "m")

# p5: dV between 0.20 m and 0.50 m from +6.0 uC, then W for 2.0 nC
potential_near = k * 6.0e-6 / 0.20
potential_far = k * 6.0e-6 / 0.50
delta_v_p5 = potential_near - potential_far
record("electric-potential-energy-p5", 2.0e-9 * delta_v_p5, "J")

# p6: Ep of alpha and gold nucleus at 4.5e-14 m, in MeV
energy_p6 = k * (2 * e) * (79 * e) / 4.5e-14
record("electric-potential-energy-p6", energy_p6 / (1e6 * eV), "MeV")


# ---------------------------------------------------------------
# Type 5: capacitance
# ---------------------------------------------------------------

# w: 220 uF at 10.0 V
record("capacitance-w", 220e-6 * 10.0, "C")

# p1: C = Q/V, 3.0e-4 C at 6.0 V
record("capacitance-p1", 3.0e-4 / 6.0, "F")

# p2: V = Q/C, 1.5e-3 C on 100 uF
record("capacitance-p2", 1.5e-3 / 100e-6, "V")

# p3: 4700 uF at 25 V, charge in mC
charge_p3 = 4700e-6 * 25
record("capacitance-p3", charge_p3 / 1e-3, "mC")

# p4: 36 nC at 12 V, capacitance in nF
cap_p4 = 36e-9 / 12
record("capacitance-p4", cap_p4 / 1e-9, "nF")

# p5: constant 50 uA for 40 s, reaches 8.0 V, C in uF
charge_p5 = 50e-6 * 40
cap_p5 = charge_p5 / 8.0
record("capacitance-p5", cap_p5 / 1e-6, "μF")

# p6: 12 pF at 5.0 V, number of electrons
charge_p6 = 12e-12 * 5.0
record("capacitance-p6", charge_p6 / e, "")


# ---------------------------------------------------------------
# Type 6: parallel-plate-capacitor
# ---------------------------------------------------------------

# w: A = 0.040 m^2, d = 0.50 mm, air
record("parallel-plate-capacitor-w", eps0 * 0.040 / 0.50e-3, "F")

# p1: A = 0.020 m^2, d = 1.0e-3 m, air
record("parallel-plate-capacitor-p1", eps0 * 0.020 / 1.0e-3, "F")

# p2: A = 0.015 m^2, d = 2.5e-4 m, er = 4.0
record("parallel-plate-capacitor-p2", eps0 * 4.0 * 0.015 / 2.5e-4, "F")

# p3: 25 cm^2, 0.20 mm, er = 2.3, answer in pF
area_p3 = 25e-4
cap_p3 = eps0 * 2.3 * area_p3 / 0.20e-3
record("parallel-plate-capacitor-p3", cap_p3 / 1e-12, "pF")

# p4: d for C = 100 pF, A = 60 cm^2, air; answer in mm
area_p4 = 60e-4
sep_p4 = eps0 * area_p4 / 100e-12
record("parallel-plate-capacitor-p4", sep_p4 / 1e-3, "mm")

# p5: er for C = 4.7 nF, A = 0.012 m^2, d = 0.10 mm
record("parallel-plate-capacitor-p5", 4.7e-9 * 0.10e-3 / (eps0 * 0.012), "")

# p6: 8.0 cm x 8.0 cm plates, 0.50 mm, er = 6.0, 50 V -> charge
area_p6 = 0.080 * 0.080
cap_p6 = eps0 * 6.0 * area_p6 / 0.50e-3
record("parallel-plate-capacitor-p6", cap_p6 * 50, "C")


# ---------------------------------------------------------------
# Type 7: energy-stored-capacitor
# ---------------------------------------------------------------

# w: 2200 uF at 15 V
record("energy-stored-capacitor-w", 0.5 * 2200e-6 * 15 ** 2, "J")

# p1: 1/2 QV, Q = 5.0 mC, V = 20 V
record("energy-stored-capacitor-p1", 0.5 * 5.0e-3 * 20, "J")

# p2: 1/2 CV^2, 100 uF at 50 V
record("energy-stored-capacitor-p2", 0.5 * 100e-6 * 50 ** 2, "J")

# p3: Q^2/2C, Q = 0.60 mC, C = 40 uF
record("energy-stored-capacitor-p3", (0.60e-3) ** 2 / (2 * 40e-6), "J")

# p4: V for 200 J in 32 uF
record("energy-stored-capacitor-p4", math.sqrt(2 * 200 / 32e-6), "V")

# p5: energy delivered by 4700 uF as V falls 12 V -> 4.0 V
energy_start = 0.5 * 4700e-6 * 12 ** 2
energy_end = 0.5 * 4700e-6 * 4.0 ** 2
record("energy-stored-capacitor-p5", energy_start - energy_end, "J")

# p6: 1200 uF at 300 V delivered in 2.0 ms -> mean power in kW
energy_p6 = 0.5 * 1200e-6 * 300 ** 2
power_p6 = energy_p6 / 2.0e-3
record("energy-stored-capacitor-p6", power_p6 / 1e3, "kW")


# ---------------------------------------------------------------
# Type 8: capacitors-series-parallel
# ---------------------------------------------------------------

# w: 2.0 uF and 3.0 uF in series
record("capacitors-series-parallel-w", 1 / (1 / 2.0 + 1 / 3.0), "μF")

# p1: 4.7 uF and 10 uF in parallel
record("capacitors-series-parallel-p1", 4.7 + 10, "μF")

# p2: 6.0 uF and 12 uF in series
record("capacitors-series-parallel-p2", 1 / (1 / 6.0 + 1 / 12), "μF")

# p3: 2200 pF in parallel with 4.7 nF, answer in nF
record("capacitors-series-parallel-p3", 2200e-12 / 1e-9 + 4.7, "nF")

# p4: unknown in series with 10 uF gives 4.0 uF
record("capacitors-series-parallel-p4", 1 / (1 / 4.0 - 1 / 10), "μF")

# p5: (2.0 uF || 4.0 uF) in series with 3.0 uF
parallel_p5 = 2.0 + 4.0
record("capacitors-series-parallel-p5", 1 / (1 / parallel_p5 + 1 / 3.0), "μF")

# p6: 3.0 uF and 6.0 uF in series across 18 V; charge on each, in uC
series_p6 = 1 / (1 / 3.0 + 1 / 6.0)
record("capacitors-series-parallel-p6", series_p6 * 18, "μC")


# ---------------------------------------------------------------
# Type 9: capacitor-discharge
# ---------------------------------------------------------------

# w: 470 uF, 10 kOhm, V0 = 9.0 V, t = 6.0 s
tau_w9 = 10e3 * 470e-6
record("capacitor-discharge-w", 9.0 * math.exp(-6.0 / tau_w9), "V")

# p1: tau = RC, 2200 uF and 1.5 kOhm
record("capacitor-discharge-p1", 1.5e3 * 2200e-6, "s")

# p2: V0 = 12 V, tau = 5.0 s, t = 8.0 s
record("capacitor-discharge-p2", 12 * math.exp(-8.0 / 5.0), "V")

# p3: I0 = 2.0 mA, R = 47 kOhm, C = 100 uF, t = 10 s; answer in uA
tau_p3 = 47e3 * 100e-6
current_p3 = 2.0e-3 * math.exp(-10 / tau_p3)
record("capacitor-discharge-p3", current_p3 / 1e-6, "μA")

# p4: R for tau = 0.25 s with 50 uF, in kOhm
record("capacitor-discharge-p4", (0.25 / 50e-6) / 1e3, "kΩ")

# p5: time for V to fall to 25%, R = 22 kOhm, C = 330 uF
tau_p5 = 22e3 * 330e-6
record("capacitor-discharge-p5", -tau_p5 * math.log(0.25), "s")

# p6: V halves in 14 s through 100 kOhm -> C in uF
tau_p6 = 14 / math.log(2)
record("capacitor-discharge-p6", (tau_p6 / 100e3) / 1e-6, "μF")


# ---------------------------------------------------------------
# Type 10: capacitor-charging
# ---------------------------------------------------------------

# w: V0 = 6.0 V, R = 100 kOhm, C = 22 uF, t = 3.0 s
tau_w10 = 100e3 * 22e-6
record("capacitor-charging-w", 6.0 * (1 - math.exp(-3.0 / tau_w10)), "V")

# p1: V0 = 10 V, tau = 4.0 s, t = 2.0 s
record("capacitor-charging-p1", 10 * (1 - math.exp(-2.0 / 4.0)), "V")

# p2: V0 = 12 V, R = 4.7 kOhm, C = 1000 uF, t = 5.0 s
tau_p2 = 4.7e3 * 1000e-6
record("capacitor-charging-p2", 12 * (1 - math.exp(-5.0 / tau_p2)), "V")

# p3: V0 = 5.0 V, R = 2.2 MOhm, C = 470 nF, t = 0.50 s
tau_p3c = 2.2e6 * 470e-9
record("capacitor-charging-p3", 5.0 * (1 - math.exp(-0.50 / tau_p3c)), "V")

# p4: time to reach 2.0 V from 5.0 V, tau = 3.0 s
record("capacitor-charging-p4", -3.0 * math.log(1 - 2.0 / 5.0), "s")

# p5: time to reach 90%, R = 56 kOhm, C = 220 uF
tau_p5c = 56e3 * 220e-6
record("capacitor-charging-p5", -tau_p5c * math.log(1 - 0.90), "s")

# p6: R so that 100 uF reaches half V0 in 0.20 s, in kOhm
tau_p6c = -0.20 / math.log(1 - 0.5)
record("capacitor-charging-p6", (tau_p6c / 100e-6) / 1e3, "kΩ")


# ---------------------------------------------------------------
# Print
# ---------------------------------------------------------------

for question_id, rounded, unit, raw in results:
    print(f"{question_id:36s} {rounded!r:>14}  {unit:8s} (raw {raw!r})")
