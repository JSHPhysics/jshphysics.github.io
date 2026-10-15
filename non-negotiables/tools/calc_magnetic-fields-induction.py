#!/usr/bin/env python3
"""Compute every answer in data/magnetic-fields-induction.json.

Each answer is printed rounded to 3 s.f. with its question id.
Run: python3 tools/calc_magnetic-fields-induction.py
"""

import math

# Standard constants from SCHEMA.md
g = 9.81          # m s^-2
e = 1.60e-19      # C
m_e = 9.11e-31    # kg
m_p = 1.67e-27    # kg
u = 1.66e-27      # kg

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


def sin_deg(angle_degrees):
    """Sine of an angle given in degrees."""
    return math.sin(math.radians(angle_degrees))


def cos_deg(angle_degrees):
    """Cosine of an angle given in degrees."""
    return math.cos(math.radians(angle_degrees))


# ---------------------------------------------------------------
# Type 1: force-on-conductor  (F = BIL sin θ)
# ---------------------------------------------------------------

# w: B = 0.25 T, I = 3.5 A, L = 0.080 m, perpendicular
record("force-on-conductor-w", 0.25 * 3.5 * 0.080, "N")

# p1: motor coil side, B = 0.30 T, I = 2.0 A, L = 0.12 m
record("force-on-conductor-p1", 0.30 * 2.0 * 0.12, "N")

# p2: wire at 30 degrees to the field, B = 0.60 T, I = 4.0 A, L = 0.25 m
record("force-on-conductor-p2", 0.60 * 4.0 * 0.25 * sin_deg(30), "N")

# p3: find B; L = 5.0 cm, I = 6.0 A, F = 1.8e-2 N
length_p3 = 5.0e-2
record("force-on-conductor-p3", 1.8e-2 / (6.0 * length_p3), "T")

# p4: find L in cm; F = 0.24 N, B = 0.80 T, I = 15 A
length_p4 = 0.24 / (0.80 * 15)
record("force-on-conductor-p4", length_p4 * 100, "cm")

# p5: current balance, find I; mass change 0.45 g, L = 60 mm, B = 120 mT
force_p5 = 0.45e-3 * g
record("force-on-conductor-p5", force_p5 / (120e-3 * 60e-3), "A")

# p6: current balance, find B; mass change 1.2 g, L = 4.0 cm, I = 2.5 A
force_p6 = 1.2e-3 * g
record("force-on-conductor-p6", force_p6 / (2.5 * 4.0e-2), "T")


# ---------------------------------------------------------------
# Type 2: force-on-moving-charge  (F = BQv sin θ)
# ---------------------------------------------------------------

# w: electron, B = 0.15 T, v = 2.0e7 m/s, perpendicular
record("force-on-moving-charge-w", 0.15 * e * 2.0e7, "N")

# p1: proton, B = 1.2 T, v = 3.0e6 m/s
record("force-on-moving-charge-p1", 1.2 * e * 3.0e6, "N")

# p2: alpha particle (Q = 2e), B = 0.40 T, v = 1.5e7 m/s, 60 degrees
record("force-on-moving-charge-p2", 0.40 * (2 * e) * 1.5e7 * sin_deg(60), "N")

# p3: find v; electron, F = 2.4e-14 N, B = 5.0 mT
record("force-on-moving-charge-p3", 2.4e-14 / (5.0e-3 * e), "m s⁻¹")

# p4: find B; Mg2+ ion (Q = 2e), F = 5.8e-14 N, v = 4.5e5 m/s
record("force-on-moving-charge-p4", 5.8e-14 / ((2 * e) * 4.5e5), "T")

# p5: electron with KE 500 eV, B = 20 mT: find v then F
ke_p5 = 500 * e
speed_p5 = math.sqrt(2 * ke_p5 / m_e)
record("force-on-moving-charge-p5", 20e-3 * e * speed_p5, "N")

# p6: proton, B = 0.80 T, v = 2.0e6: find F then a = F/m
force_p6_charge = 0.80 * e * 2.0e6
record("force-on-moving-charge-p6", force_p6_charge / m_p, "m s⁻²")


# ---------------------------------------------------------------
# Type 3: circular-path-radius  (r = mv/(BQ), T = 2πm/(BQ))
# ---------------------------------------------------------------

# w: proton, v = 4.0e6 m/s, B = 0.50 T
record("circular-path-radius-w", m_p * 4.0e6 / (0.50 * e), "m")

# p1: electron, v = 5.0e6 m/s, B = 2.0e-3 T
record("circular-path-radius-p1", m_e * 5.0e6 / (2.0e-3 * e), "m")

# p2: period of a proton orbit, B = 1.5 T
record("circular-path-radius-p2", 2 * math.pi * m_p / (1.5 * e), "s")

# p3: find B; alpha (m = 6.64e-27 kg, Q = 2e), v = 1.2e7, r = 25 cm
m_alpha = 6.64e-27
record("circular-path-radius-p3", m_alpha * 1.2e7 / (0.25 * 2 * e), "T")

# p4: find v; electron, r = 4.5 cm, B = 1.2 mT
record("circular-path-radius-p4", 1.2e-3 * e * 4.5e-2 / m_e, "m s⁻¹")

# p5: argon ion, mass 40 u, Q = e, r = 0.40 m, B = 0.60 T: find mass then v
m_argon = 40 * u
record("circular-path-radius-p5", 0.60 * e * 0.40 / m_argon, "m s⁻¹")

# p6: cyclotron frequency for a proton in B = 1.8 T: period then f in MHz
period_p6 = 2 * math.pi * m_p / (1.8 * e)
record("circular-path-radius-p6", (1 / period_p6) / 1e6, "MHz")


# ---------------------------------------------------------------
# Type 4: accelerate-then-deflect  (eV = ½mv², r = mv/(BQ))
# ---------------------------------------------------------------

# w: electron through 2000 V, B = 5.0 mT: v then r in cm
speed_w4 = math.sqrt(2 * e * 2000 / m_e)
record("accelerate-then-deflect-w", m_e * speed_w4 / (5.0e-3 * e) * 100, "cm")

# p1: proton through 5000 V, B = 0.20 T: r in m
speed_p1_4 = math.sqrt(2 * e * 5000 / m_p)
record("accelerate-then-deflect-p1", m_p * speed_p1_4 / (0.20 * e), "m")

# p2: electron through 400 V, B = 1.5e-3 T: r in m
speed_p2_4 = math.sqrt(2 * e * 400 / m_e)
record("accelerate-then-deflect-p2", m_e * speed_p2_4 / (1.5e-3 * e), "m")

# p3: alpha (m = 6.64e-27, Q = 2e) through 12 kV, B = 0.80 T: r in cm
speed_p3_4 = math.sqrt(2 * (2 * e) * 12e3 / m_alpha)
record("accelerate-then-deflect-p3", m_alpha * speed_p3_4 / (0.80 * 2 * e) * 100, "cm")

# p4: electron through 1.2 kV must have r = 8.0 cm: find B in mT
speed_p4_4 = math.sqrt(2 * e * 1.2e3 / m_e)
field_p4_4 = m_e * speed_p4_4 / (8.0e-2 * e)
record("accelerate-then-deflect-p4", field_p4_4 * 1e3, "mT")

# p5: proton must have r = 0.50 m in B = 0.30 T: v then V in MV
speed_p5_4 = 0.30 * e * 0.50 / m_p
voltage_p5_4 = m_p * speed_p5_4 ** 2 / (2 * e)
record("accelerate-then-deflect-p5", voltage_p5_4 / 1e6, "MV")

# p6: singly charged ion through 2.5 kV, r = 0.120 m, B = 0.45 T: mass
#     m = B² Q r² / (2V)
mass_p6_4 = 0.45 ** 2 * e * 0.120 ** 2 / (2 * 2.5e3)
record("accelerate-then-deflect-p6", mass_p6_4, "kg")


# ---------------------------------------------------------------
# Type 5: flux-and-flux-linkage  (Φ = BA cos θ, NΦ)
# ---------------------------------------------------------------

# w: 200 turns, A = 4.0e-3 m², B = 0.15 T: flux linkage
record("flux-and-flux-linkage-w", 200 * 0.15 * 4.0e-3, "Wb turns")

# p1: single loop, A = 0.025 m², B = 0.80 T: flux
record("flux-and-flux-linkage-p1", 0.80 * 0.025, "Wb")

# p2: 500 turns, A = 1.2e-3 m², B = 0.050 T: flux linkage
record("flux-and-flux-linkage-p2", 500 * 0.050 * 1.2e-3, "Wb turns")

# p3: 150 turns, A = 25 cm², B = 40 mT: flux linkage
area_p3_5 = 25e-4
record("flux-and-flux-linkage-p3", 150 * 40e-3 * area_p3_5, "Wb turns")

# p4: find B; flux 3.6e-4 Wb through circular coil radius 3.0 cm
area_p4_5 = math.pi * 0.030 ** 2
record("flux-and-flux-linkage-p4", 3.6e-4 / area_p4_5, "T")

# p5: 300 turns, diameter 8.0 cm, B = 0.20 T, normal at 60° to field
area_p5_5 = math.pi * 0.040 ** 2
record("flux-and-flux-linkage-p5", 300 * 0.20 * area_p5_5 * cos_deg(60), "Wb turns")

# p6: find N; flux linkage 0.090 Wb turns, B = 0.30 T, square side 5.0 cm
area_p6_5 = 0.050 ** 2
flux_p6_5 = 0.30 * area_p6_5
record("flux-and-flux-linkage-p6", 0.090 / flux_p6_5, "")


# ---------------------------------------------------------------
# Type 6: faradays-law  (ε = NΔΦ/Δt)
# ---------------------------------------------------------------

# w: 250 turns, A = 3.0e-3 m², B falls 0.40 T to 0 in 0.050 s
record("faradays-law-w", 250 * (0.40 * 3.0e-3) / 0.050, "V")

# p1: 100 turns, A = 2.0e-3 m², field changing at 2.5 T/s
record("faradays-law-p1", 100 * 2.5 * 2.0e-3, "V")

# p2: flux linkage 0.60 to 0.15 Wb turns in 0.30 s
record("faradays-law-p2", (0.60 - 0.15) / 0.30, "V")

# p3: 400 turns, A = 12 cm², withdrawn from 80 mT in 20 ms
flux_p3_6 = 80e-3 * 12e-4
record("faradays-law-p3", 400 * flux_p3_6 / 20e-3, "V")

# p4: find Δt; 50 turns, A = 0.040 m², B = 0.25 T removed, e.m.f. 4.0 V
record("faradays-law-p4", 50 * (0.25 * 0.040) / 4.0, "s")

# p5: find N; B rises 0 to 0.60 T in 0.15 s, A = 8.0 cm², e.m.f. 3.2 V
flux_p5_6 = 0.60 * 8.0e-4
rate_p5_6 = flux_p5_6 / 0.15
record("faradays-law-p5", 3.2 / rate_p5_6, "")

# p6: 120 turns, R = 15 Ω, A = 5.0e-3 m², B 0.90 to 0.30 T in 0.040 s: current
emf_p6_6 = 120 * ((0.90 - 0.30) * 5.0e-3) / 0.040
record("faradays-law-p6", emf_p6_6 / 15, "A")


# ---------------------------------------------------------------
# Type 7: motional-emf  (ε = BLv)
# ---------------------------------------------------------------

# w: aircraft, B_v = 4.5e-5 T, L = 60 m, v = 250 m/s
record("motional-emf-w", 4.5e-5 * 60 * 250, "V")

# p1: rod, B = 0.20 T, L = 0.50 m, v = 3.0 m/s
record("motional-emf-p1", 0.20 * 0.50 * 3.0, "V")

# p2: train axle, B_v = 5.0e-5 T, L = 1.5 m, v = 40 m/s
record("motional-emf-p2", 5.0e-5 * 1.5 * 40, "V")

# p3: find v; L = 25 cm, B = 0.60 T, e.m.f. 0.45 V
record("motional-emf-p3", 0.45 / (0.60 * 0.25), "m s⁻¹")

# p4: car 1.8 m wide at 108 km/h, B_v = 4.8e-5 T: e.m.f. in mV
speed_p4_7 = 108 * 1000 / 3600
record("motional-emf-p4", 4.8e-5 * 1.8 * speed_p4_7 * 1e3, "mV")

# p5: falling rod, L = 0.80 m, falls 0.50 s from rest, B = 0.12 T
speed_p5_7 = g * 0.50
record("motional-emf-p5", 0.12 * 0.80 * speed_p5_7, "V")

# p6: rod L = 0.40 m, B = 0.50 T, v = 6.0 m/s, R = 2.0 Ω: current
emf_p6_7 = 0.50 * 0.40 * 6.0
record("motional-emf-p6", emf_p6_7 / 2.0, "A")


# ---------------------------------------------------------------
# Type 8: transformers  (N_s/N_p = V_s/V_p, I_p V_p = I_s V_s)
# ---------------------------------------------------------------

# w: V_p = 230 V, V_s = 12 V, N_p = 1150: N_s
record("transformers-w", 1150 * 12 / 230, "")

# p1: N_p = 400, N_s = 20, V_p = 230 V: V_s
record("transformers-p1", 230 * 20 / 400, "V")

# p2: N_p = 50, N_s = 2000, V_p = 12 V: V_s
record("transformers-p2", 12 * 2000 / 50, "V")

# p3: find N_p; V_p = 230 V, V_s = 5.0 V, N_s = 30
record("transformers-p3", 30 * 230 / 5.0, "")

# p4: ideal; V_p = 230 V, V_s = 12 V, I_s = 4.0 A: I_p
record("transformers-p4", 12 * 4.0 / 230, "A")

# p5: N_p = 1200, N_s = 60, V_p = 240 V, lamp 6.0 Ω: V_s then I_s
voltage_p5_8 = 240 * 60 / 1200
record("transformers-p5", voltage_p5_8 / 6.0, "A")

# p6: input 230 V, 8.0 A; 120 W lost: efficiency in %
power_in_p6 = 230 * 8.0
power_out_p6 = power_in_p6 - 120
record("transformers-p6", power_out_p6 / power_in_p6 * 100, "%")


# ---------------------------------------------------------------
# Type 9: ac-rms-values  (V_rms = V₀/√2, I_rms = I₀/√2)
# ---------------------------------------------------------------

# w: V₀ = 325 V: V_rms
record("ac-rms-values-w", 325 / math.sqrt(2), "V")

# p1: I₀ = 2.4 A: I_rms
record("ac-rms-values-p1", 2.4 / math.sqrt(2), "A")

# p2: V_rms = 110 V: V₀
record("ac-rms-values-p2", 110 * math.sqrt(2), "V")

# p3: peak-to-peak 17.0 V on oscilloscope: V_rms
peak_p3_9 = 17.0 / 2
record("ac-rms-values-p3", peak_p3_9 / math.sqrt(2), "V")

# p4: I_rms = 35 mA: I₀ in mA
record("ac-rms-values-p4", 35 * math.sqrt(2), "mA")

# p5: V₀ = 12 V across 8.0 Ω: V_rms then mean power
v_rms_p5_9 = 12 / math.sqrt(2)
record("ac-rms-values-p5", v_rms_p5_9 ** 2 / 8.0, "W")

# p6: 2.0 kW heater on 230 V r.m.s.: I_rms then I₀
i_rms_p6_9 = 2000 / 230
record("ac-rms-values-p6", i_rms_p6_9 * math.sqrt(2), "A")


# ---------------------------------------------------------------
# Print
# ---------------------------------------------------------------

for question_id, rounded, unit, raw in results:
    print(f"{question_id:30s} {rounded!r:>14}  {unit:10s} (raw {raw!r})")
