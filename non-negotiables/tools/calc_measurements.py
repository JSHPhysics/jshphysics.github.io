#!/usr/bin/env python3
"""Compute every answer in data/measurements.json.

Each answer is printed rounded to 3 s.f. with its question id.
Run: python3 tools/calc_measurements.py
"""

import math

# Standard constants from SCHEMA.md
g = 9.81          # m s^-2
e = 1.60e-19      # C
h = 6.63e-34      # J s

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
# Type 1: si-prefixes
# ---------------------------------------------------------------

# w: 650 nm to m
record("si-prefixes-w", 650 * 1e-9, "m")

# p1: 25 us to s
record("si-prefixes-p1", 25 * 1e-6, "s")

# p2: 3.2 kN to N
record("si-prefixes-p2", 3.2 * 1e3, "N")

# p3: 1.8e-11 F to pF
record("si-prefixes-p3", 1.8e-11 / 1e-12, "pF")

# p4: 4.5e9 W to GW
record("si-prefixes-p4", 4.5e9 / 1e9, "GW")

# p5: 35.8 Mm to km (Mm -> m -> km)
metres_p5 = 35.8 * 1e6
record("si-prefixes-p5", metres_p5 / 1e3, "km")

# p6: 0.062 mA to uA (mA -> A -> uA)
amps_p6 = 0.062 * 1e-3
record("si-prefixes-p6", amps_p6 / 1e-6, "μA")


# ---------------------------------------------------------------
# Type 2: derived-units
# ---------------------------------------------------------------

# w: 108 km/h to m/s
record("derived-units-w", 108 * 1000 / 3600, "m s⁻¹")

# p1: 0.92 g/cm^3 to kg/m^3
record("derived-units-p1", 0.92 * 1e-3 / 1e-6, "kg m⁻³")

# p2: 55 litres to m^3
record("derived-units-p2", 55 * 1e-3, "m³")

# p3: 2.5 mm^2 to m^2
record("derived-units-p3", 2.5 * (1e-3) ** 2, "m²")

# p4: 2.6 kWh to J
record("derived-units-p4", 2.6 * 1000 * 3600, "J")

# p5: 100 m in 9.86 s, speed in km/h (two steps)
speed_p5 = 100 / 9.86
record("derived-units-p5", speed_p5 * 3600 / 1000, "km h⁻¹")

# p6: 12.4 kg, 642 cm^3 -> density in kg/m^3 (two steps)
volume_p6 = 642 * 1e-6
record("derived-units-p6", 12.4 / volume_p6, "kg m⁻³")


# ---------------------------------------------------------------
# Type 3: single-uncertainty
# ---------------------------------------------------------------

# w: repeats 1.52, 1.48, 1.55, 1.49 s -> mean, half range, percentage
readings_w = [1.52, 1.48, 1.55, 1.49]
mean_w = sum(readings_w) / len(readings_w)
half_range_w = (max(readings_w) - min(readings_w)) / 2
record("single-uncertainty-w", half_range_w / mean_w * 100, "%")

# p1: 6.4 V +/- 0.1 V -> percentage
record("single-uncertainty-p1", 0.1 / 6.4 * 100, "%")

# p2: micrometer 2.46 mm, uncertainty +/- 0.005 mm -> percentage
record("single-uncertainty-p2", 0.005 / 2.46 * 100, "%")

# p3: string length 0.625 m, uncertainty +/- 1 mm -> percentage
record("single-uncertainty-p3", 0.001 / 0.625 * 100, "%")

# p4: 2.5 % of 0.360 kg -> absolute uncertainty in g
abs_p4_kg = 2.5 / 100 * 0.360
record("single-uncertainty-p4", abs_p4_kg * 1000, "g")

# p5: 10 oscillations in 18.4 s +/- 0.2 s -> percentage uncertainty in T
period_p5 = 18.4 / 10
unc_period_p5 = 0.2 / 10
record("single-uncertainty-p5", unc_period_p5 / period_p5 * 100, "%")

# p6: repeats of current -> mean, half range, percentage
readings_p6 = [0.244, 0.251, 0.247, 0.249, 0.254]
mean_p6 = sum(readings_p6) / len(readings_p6)
half_range_p6 = (max(readings_p6) - min(readings_p6)) / 2
record("single-uncertainty-p6", half_range_p6 / mean_p6 * 100, "%")


# ---------------------------------------------------------------
# Type 4: sums-differences
# ---------------------------------------------------------------

# w: 184.5 +/- 0.5 g minus 62.0 +/- 0.5 g -> absolute uncertainty
record("sums-differences-w", 0.5 + 0.5, "g")

# p1: 47 +/- 2 ohm and 68 +/- 3 ohm in series -> absolute uncertainty
record("sums-differences-p1", 2 + 3, "Ω")

# p2: temperature 18.5 +/- 0.5 to 41.0 +/- 0.5 -> absolute uncertainty in rise
record("sums-differences-p2", 0.5 + 0.5, "°C")

# p3: ruler readings 2.3 +/- 0.1 cm and 18.7 +/- 0.1 cm -> percentage uncertainty in length
length_p3 = 18.7 - 2.3
unc_p3 = 0.1 + 0.1
record("sums-differences-p3", unc_p3 / length_p3 * 100, "%")

# p4: spring 125 +/- 1 mm to 183 +/- 1 mm -> percentage uncertainty in extension
extension_p4 = 183 - 125
unc_p4 = 1 + 1
record("sums-differences-p4", unc_p4 / extension_p4 * 100, "%")

# p5: flask 0.428 kg +/- 0.5 %, empty 0.176 kg +/- 0.5 % -> percentage uncertainty in water mass
abs_full_p5 = 0.5 / 100 * 0.428
abs_empty_p5 = 0.5 / 100 * 0.176
mass_p5 = 0.428 - 0.176
unc_p5 = abs_full_p5 + abs_empty_p5
record("sums-differences-p5", unc_p5 / mass_p5 * 100, "%")

# p6: emf 9.0 +/- 0.1 V minus lost volts 2.4 +/- 0.1 V -> percentage uncertainty in terminal pd
pd_p6 = 9.0 - 2.4
unc_p6 = 0.1 + 0.1
record("sums-differences-p6", unc_p6 / pd_p6 * 100, "%")


# ---------------------------------------------------------------
# Type 5: products-quotients
# ---------------------------------------------------------------

# w: m = 48.6 +/- 0.1 g, V = 18.0 +/- 0.5 cm^3 -> percentage uncertainty in density
pct_m_w = 0.1 / 48.6 * 100
pct_V_w = 0.5 / 18.0 * 100
record("products-quotients-w", pct_m_w + pct_V_w, "%")

# p1: V +/- 2 %, I +/- 3 % -> percentage uncertainty in R
record("products-quotients-p1", 2 + 3, "%")

# p2: I = 0.42 +/- 0.01 A, V = 11.8 +/- 0.1 V -> percentage uncertainty in P
pct_I_p2 = 0.01 / 0.42 * 100
pct_V_p2 = 0.1 / 11.8 * 100
record("products-quotients-p2", pct_I_p2 + pct_V_p2, "%")

# p3: V = 3.6 +/- 0.1 V, I = 0.15 +/- 0.01 A -> absolute uncertainty in R
R_p3 = 3.6 / 0.15
pct_p3 = 0.1 / 3.6 * 100 + 0.01 / 0.15 * 100
record("products-quotients-p3", pct_p3 / 100 * R_p3, "Ω")

# p4: d = 25.0 +/- 0.1 m, t = 3.20 +/- 0.05 s -> percentage uncertainty in speed
pct_d_p4 = 0.1 / 25.0 * 100
pct_t_p4 = 0.05 / 3.20 * 100
record("products-quotients-p4", pct_d_p4 + pct_t_p4, "%")

# p5: F = 120 +/- 2 N, l = 0.250 +/- 0.005 m, w = 0.120 +/- 0.005 m -> percentage uncertainty in pressure
pct_F_p5 = 2 / 120 * 100
pct_l_p5 = 0.005 / 0.250 * 100
pct_w_p5 = 0.005 / 0.120 * 100
record("products-quotients-p5", pct_F_p5 + pct_l_p5 + pct_w_p5, "%")

# p6: F = 45 +/- 1 N, d = 2.4 +/- 0.1 m -> absolute uncertainty in W
W_p6 = 45 * 2.4
pct_p6 = 1 / 45 * 100 + 0.1 / 2.4 * 100
record("products-quotients-p6", pct_p6 / 100 * W_p6, "J")


# ---------------------------------------------------------------
# Type 6: powers
# ---------------------------------------------------------------

# w: m 1.5 %, v 2 % -> percentage uncertainty in KE
record("powers-w", 1.5 + 2 * 2.0, "%")

# p1: r 1.2 % -> percentage uncertainty in volume of sphere
record("powers-p1", 3 * 1.2, "%")

# p2: L 0.5 %, T 1.5 % -> percentage uncertainty in g = 4 pi^2 L / T^2
record("powers-p2", 0.5 + 2 * 1.5, "%")

# p3: d = 12.4 +/- 0.1 mm -> percentage uncertainty in area of circle
pct_d_p3 = 0.1 / 12.4 * 100
record("powers-p3", 2 * pct_d_p3, "%")

# p4: m = 0.250 +/- 0.005 kg, v = 3.0 +/- 0.1 m/s -> absolute uncertainty in KE
KE_p4 = 0.5 * 0.250 * 3.0 ** 2
pct_KE_p4 = 0.005 / 0.250 * 100 + 2 * (0.1 / 3.0 * 100)
record("powers-p4", pct_KE_p4 / 100 * KE_p4, "J")

# p5: V = 12.0 +/- 0.2 V, R = 36 +/- 1 ohm -> percentage uncertainty in P = V^2 / R
pct_V_p5 = 0.2 / 12.0 * 100
pct_R_p5 = 1 / 36 * 100
record("powers-p5", 2 * pct_V_p5 + pct_R_p5, "%")

# p6: r = 2.50 +/- 0.05 cm -> absolute uncertainty in volume of sphere (cm^3)
V_p6 = 4 / 3 * math.pi * 2.50 ** 3
pct_r_p6 = 0.05 / 2.50 * 100
record("powers-p6", 3 * pct_r_p6 / 100 * V_p6, "cm³")


# ---------------------------------------------------------------
# Type 7: graph-gradient
# ---------------------------------------------------------------

# w: R-L graph points (0.20 m, 1.6 ohm), (0.80 m, 6.4 ohm); A = 2.5e-7 m^2 -> resistivity
gradient_w = (6.4 - 1.6) / (0.80 - 0.20)
record("graph-gradient-w", gradient_w * 2.5e-7, "Ω m")

# p1: v-t graph points (2.0 s, 5.0 m/s), (8.0 s, 23.0 m/s) -> acceleration
record("graph-gradient-p1", (23.0 - 5.0) / (8.0 - 2.0), "m s⁻²")

# p2: F-x graph points (0.020 m, 5.0 N), (0.080 m, 20.0 N) -> spring constant
record("graph-gradient-p2", (20.0 - 5.0) / (0.080 - 0.020), "N m⁻¹")

# p3: T^2-L graph points (0.40 m, 1.61 s^2), (1.00 m, 4.02 s^2) -> g = 4 pi^2 / gradient
gradient_p3 = (4.02 - 1.61) / (1.00 - 0.40)
record("graph-gradient-p3", 4 * math.pi ** 2 / gradient_p3, "m s⁻²")

# p4: V_s-f graph points (6.0e14 Hz, 0.45 V), (9.0e14 Hz, 1.69 V) -> h = e x gradient
gradient_p4 = (1.69 - 0.45) / (9.0e14 - 6.0e14)
record("graph-gradient-p4", e * gradient_p4, "J s")

# p5: V-I graph of a cell points (0.20 A, 1.40 V), (0.60 A, 1.08 V) -> emf (intercept)
gradient_p5 = (1.08 - 1.40) / (0.60 - 0.20)
emf_p5 = 1.40 - gradient_p5 * 0.20
record("graph-gradient-p5", emf_p5, "V")

# p6: temperature-time graph points (60 s, 24.0 C), (240 s, 36.0 C); P = 50 W, m = 0.50 kg -> c
gradient_p6 = (36.0 - 24.0) / (240 - 60)
record("graph-gradient-p6", 50 / (0.50 * gradient_p6), "J kg⁻¹ K⁻¹")


# ---------------------------------------------------------------
# Type 8: percentage-error
# ---------------------------------------------------------------

# w: measured g = 9.65 vs accepted 9.81 -> percentage error
record("percentage-error-w", abs(9.65 - 9.81) / 9.81 * 100, "%")

# p1: speed of sound 336 vs 343 m/s
record("percentage-error-p1", abs(336 - 343) / 343 * 100, "%")

# p2: copper resistivity 1.80e-8 vs 1.68e-8
record("percentage-error-p2", abs(1.80e-8 - 1.68e-8) / 1.68e-8 * 100, "%")

# p3: percentage difference between 24.5 and 26.3 N/m using the mean
mean_k_p3 = (24.5 + 26.3) / 2
record("percentage-error-p3", abs(26.3 - 24.5) / mean_k_p3 * 100, "%")

# p4: density 2.65 g/cm^3 vs accepted 2700 kg/m^3 (convert first)
density_p4 = 2.65 * 1000
record("percentage-error-p4", abs(density_p4 - 2700) / 2700 * 100, "%")

# p5: pendulum L = 0.500 m, T = 1.45 s -> g then percentage error vs 9.81
g_p5 = 4 * math.pi ** 2 * 0.500 / 1.45 ** 2
record("percentage-error-p5", abs(g_p5 - g) / g * 100, "%")

# p6: R from V = 4.80 V, I = 0.210 A, marked 22 ohm -> percentage error
R_p6 = 4.80 / 0.210
record("percentage-error-p6", abs(R_p6 - 22) / 22 * 100, "%")


# ---------------------------------------------------------------
# Print
# ---------------------------------------------------------------

for question_id, rounded, unit, raw in results:
    print(f"{question_id:28s} {rounded!r:>14}  {unit:14s} (raw {raw!r})")
