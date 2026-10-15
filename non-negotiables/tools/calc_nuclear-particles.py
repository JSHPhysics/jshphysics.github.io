#!/usr/bin/env python3
"""Compute every answer in data/nuclear-particles.json.

Each answer is printed rounded to 3 s.f. with its question id.
Run: python3 tools/calc_nuclear-particles.py
"""

import math

# Standard constants from SCHEMA.md
c = 3.00e8            # m s^-1
e = 1.60e-19          # C
N_A = 6.02e23         # mol^-1
eps0 = 8.85e-12       # F m^-1
m_e = 9.11e-31        # kg
m_p_kg = 1.67e-27     # kg
u_kg = 1.66e-27       # kg
MeV_per_u = 931.5     # MeV/c^2 per u
eV = 1.60e-19         # J
MeV = 1.60e-13        # J
M_sun = 1.99e30       # kg

# Nucleon masses in u (given in the brief, quoted in questions)
m_p_u = 1.007276
m_n_u = 1.008665

# Time conversions
DAY = 24 * 3600                 # s
YEAR = 365 * 24 * 3600          # s (1 year = 365 days, for questions that say so)
YEAR_STATED = 3.15e7            # s (for questions that quote 1 year = 3.15 × 10⁷ s)

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


def decay_constant(half_life):
    """lambda = ln 2 / t_half (same time unit as t_half)."""
    return math.log(2) / half_life


# ---------------------------------------------------------------
# Type 1: half-life-decay-constant
# ---------------------------------------------------------------

# w: cobalt-60, t_half = 5.27 years -> lambda in s^-1
t_half_w = 5.27 * YEAR
record("half-life-decay-constant-w", decay_constant(t_half_w), "s⁻¹")

# p1: iodine-131, t_half = 8.02 days -> lambda in day^-1
record("half-life-decay-constant-p1", decay_constant(8.02), "day⁻¹")

# p2: technetium-99m, t_half = 6.0 hours -> lambda in hour^-1
record("half-life-decay-constant-p2", decay_constant(6.0), "h⁻¹")

# p3: radon-222, t_half = 3.82 days -> lambda in s^-1
t_half_p3 = 3.82 * DAY
record("half-life-decay-constant-p3", decay_constant(t_half_p3), "s⁻¹")

# p4: carbon-14, lambda = 1.21e-4 year^-1 -> t_half in years
record("half-life-decay-constant-p4", math.log(2) / 1.21e-4, "years")

# p5: plutonium-239, lambda = 9.12e-13 s^-1 -> t_half in years (two steps)
t_half_p5_seconds = math.log(2) / 9.12e-13
record("half-life-decay-constant-p5", t_half_p5_seconds / YEAR_STATED, "years")

# p6: uranium-238, t_half = 4.47e9 years -> lambda in s^-1 (two steps)
t_half_p6_seconds = 4.47e9 * YEAR_STATED
record("half-life-decay-constant-p6", decay_constant(t_half_p6_seconds), "s⁻¹")


# ---------------------------------------------------------------
# Type 2: activity-number-nuclei
# ---------------------------------------------------------------

# w: 1.0 ug of cobalt-60 (60 g/mol), lambda = 4.17e-9 s^-1 -> A
N_w2 = (1.0e-6 / 60) * N_A
record("activity-number-nuclei-w", 4.17e-9 * N_w2, "Bq")

# p1: americium-241 in a smoke detector, N = 7.4e14, lambda = 5.08e-11 s^-1 -> A
record("activity-number-nuclei-p1", 5.08e-11 * 7.4e14, "Bq")

# p2: number of nuclei in 5.0 g of uranium-238 (238 g/mol)
record("activity-number-nuclei-p2", (5.0 / 238) * N_A, "")

# p3: technetium-99m, A = 800 MBq, lambda = 3.21e-5 s^-1 -> N
record("activity-number-nuclei-p3", 800e6 / 3.21e-5, "")

# p4: radium-226 source, N = 2.6e18, A = 36 MBq -> lambda
record("activity-number-nuclei-p4", 36e6 / 2.6e18, "s⁻¹")

# p5: 0.50 mg of polonium-210 (210 g/mol), lambda = 5.80e-8 s^-1 -> A (two steps)
N_p5_2 = (0.50e-3 / 210) * N_A
record("activity-number-nuclei-p5", 5.80e-8 * N_p5_2, "Bq")

# p6: iodine-131, t_half = 8.02 days, A = 5.0e8 Bq -> N (two steps)
lambda_p6_2 = decay_constant(8.02 * DAY)
record("activity-number-nuclei-p6", 5.0e8 / lambda_p6_2, "")


# ---------------------------------------------------------------
# Type 3: exponential-decay
# ---------------------------------------------------------------

# w: iodine-131, lambda = 1.00e-6 s^-1, A0 = 8.0e5 Bq, t = 20 days -> A
t_w3 = 20 * DAY
record("exponential-decay-w", 8.0e5 * math.exp(-1.00e-6 * t_w3), "Bq")

# p1: phosphorus-32 tracer, lambda = 0.0485 day^-1, t = 30 days -> fraction remaining
record("exponential-decay-p1", math.exp(-0.0485 * 30), "")

# p2: radon-222, N0 = 6.0e20, lambda = 2.1e-6 s^-1, t = 1.5e5 s -> N
record("exponential-decay-p2", 6.0e20 * math.exp(-2.1e-6 * 1.5e5), "")

# p3: A0 = 1.2e6 Bq falls to 3.0e5 Bq, lambda = 4.5e-7 s^-1 -> t in days
t_p3_3_seconds = math.log(1.2e6 / 3.0e5) / 4.5e-7
record("exponential-decay-p3", t_p3_3_seconds / DAY, "days")

# p4: activity falls to 60% in 12 hours -> lambda in s^-1
t_p4_3 = 12 * 3600
record("exponential-decay-p4", math.log(1 / 0.60) / t_p4_3, "s⁻¹")

# p5: cobalt-60, t_half = 5.27 years, A0 = 2.0e10 Bq, t = 12 years -> A (two steps)
lambda_p5_3 = decay_constant(5.27)
record("exponential-decay-p5", 2.0e10 * math.exp(-lambda_p5_3 * 12), "Bq")

# p6: carbon-14, t_half = 5730 years, activity is 62% of original -> age (two steps)
lambda_p6_3 = decay_constant(5730)
record("exponential-decay-p6", math.log(1 / 0.62) / lambda_p6_3, "years")


# ---------------------------------------------------------------
# Type 4: whole-half-lives
# ---------------------------------------------------------------

# w: technetium-99m, t_half = 6.0 h, A0 = 800 MBq, after 24 h -> A
n_w4 = 24 / 6.0
record("whole-half-lives-w", 800 / (2 ** n_w4), "MBq")

# p1: iodine-131, t_half = 8.0 days, fraction remaining after 24 days
n_p1_4 = 24 / 8.0
record("whole-half-lives-p1", 1 / (2 ** n_p1_4), "")

# p2: radon-220, t_half = 55 s, A0 = 4000 Bq, after 165 s -> A
n_p2_4 = 165 / 55
record("whole-half-lives-p2", 4000 / (2 ** n_p2_4), "Bq")

# p3: activity falls from 9.6e4 Bq to 3.0e3 Bq, t_half = 15 h -> time in hours
ratio_p3_4 = 9.6e4 / 3.0e3
n_p3_4 = math.log2(ratio_p3_4)
record("whole-half-lives-p3", n_p3_4 * 15, "h")

# p4: fluorine-18, t_half = 110 min, A0 = 640 MBq, after 5.5 hours -> A
t_p4_4_minutes = 5.5 * 60
n_p4_4 = t_p4_4_minutes / 110
record("whole-half-lives-p4", 640 / (2 ** n_p4_4), "MBq")

# p5: carbon-14, t_half = 5730 years, activity is 1/16 of original -> age (two steps)
n_p5_4 = math.log2(16)
record("whole-half-lives-p5", n_p5_4 * 5730, "years")

# p6: activity falls from 2.4e6 Bq to 7.5e4 Bq in 60 min -> t_half (two steps)
ratio_p6_4 = 2.4e6 / 7.5e4
n_p6_4 = math.log2(ratio_p6_4)
record("whole-half-lives-p6", 60 / n_p6_4, "min")


# ---------------------------------------------------------------
# Type 5: mass-energy
# ---------------------------------------------------------------

# w: reactor converts 2.5e-5 kg of mass per day -> energy
record("mass-energy-w", 2.5e-5 * c ** 2, "J")

# p1: nuclear reaction, mass decrease 3.0e-29 kg -> energy
record("mass-energy-p1", 3.0e-29 * c ** 2, "J")

# p2: electron-positron annihilation at rest -> total energy
record("mass-energy-p2", 2 * m_e * c ** 2, "J")

# p3: Sun radiates 3.9e26 W -> mass lost per second
record("mass-energy-p3", 3.9e26 / c ** 2, "kg")

# p4: explosion releases 4.5 MJ -> mass equivalent in kg
record("mass-energy-p4", 4.5e6 / c ** 2, "kg")

# p5: 1.2 GW reactor runs for one year -> mass converted (two steps)
E_p5_5 = 1.2e9 * YEAR_STATED
record("mass-energy-p5", E_p5_5 / c ** 2, "kg")

# p6: 1.0 ug of antimatter annihilates with 1.0 ug of matter -> energy (two steps)
mass_p6_5 = 2 * 1.0e-9
record("mass-energy-p6", mass_p6_5 * c ** 2, "J")


# ---------------------------------------------------------------
# Type 6: mev-u-si-conversions
# ---------------------------------------------------------------

# w: rest energy of an electron in MeV
E_w6_J = m_e * c ** 2
record("mev-u-si-conversions-w", E_w6_J / MeV, "MeV")

# p1: energy equivalent of 1 u in J
record("mev-u-si-conversions-p1", u_kg * c ** 2, "J")

# p2: rest energy of a proton in MeV (data-sheet mass)
E_p2_6_J = m_p_kg * c ** 2
record("mev-u-si-conversions-p2", E_p2_6_J / MeV, "MeV")

# p3: pion rest energy 140 MeV -> mass in kg
E_p3_6_J = 140 * MeV
record("mev-u-si-conversions-p3", E_p3_6_J / c ** 2, "kg")

# p4: kaon rest energy 494 MeV -> mass in u
record("mev-u-si-conversions-p4", 494 / MeV_per_u, "u")

# p5: muon mass 1.88e-28 kg -> rest energy in MeV (two steps)
E_p5_6_J = 1.88e-28 * c ** 2
record("mev-u-si-conversions-p5", E_p5_6_J / MeV, "MeV")

# p6: W boson mass 80.4 GeV/c^2 -> mass in kg (two steps)
E_p6_6_J = 80.4e9 * eV
record("mev-u-si-conversions-p6", E_p6_6_J / c ** 2, "kg")


# ---------------------------------------------------------------
# Type 7: mass-defect-binding-energy
# ---------------------------------------------------------------

def mass_defect(Z, A, nuclear_mass_u):
    """Mass defect in u from proton number, nucleon number and nuclear mass."""
    neutrons = A - Z
    return Z * m_p_u + neutrons * m_n_u - nuclear_mass_u


# Nuclear masses in u (six decimal places, quoted in the questions)
m_He4 = 4.001506
m_C12 = 11.996706
m_Li7 = 7.014356
m_H2 = 2.013553
m_O16 = 15.990523
m_Ca40 = 39.951611

# w: helium-4 -> binding energy in MeV
dm_w7 = mass_defect(2, 4, m_He4)
record("mass-defect-binding-energy-w", dm_w7 * MeV_per_u, "MeV")

# p1: carbon-12 -> mass defect in u
record("mass-defect-binding-energy-p1", mass_defect(6, 12, m_C12), "u")

# p2: iron-56 given mass defect 0.528 u -> binding energy in MeV
record("mass-defect-binding-energy-p2", 0.528 * MeV_per_u, "MeV")

# p3: lithium-7 -> binding energy in J (via kg and c^2)
dm_p3_7_u = mass_defect(3, 7, m_Li7)
dm_p3_7_kg = dm_p3_7_u * u_kg
record("mass-defect-binding-energy-p3", dm_p3_7_kg * c ** 2, "J")

# p4: deuterium -> mass defect in kg
dm_p4_7_u = mass_defect(1, 2, m_H2)
record("mass-defect-binding-energy-p4", dm_p4_7_u * u_kg, "kg")

# p5: oxygen-16 -> binding energy per nucleon in MeV (two steps)
dm_p5_7 = mass_defect(8, 16, m_O16)
BE_p5_7 = dm_p5_7 * MeV_per_u
record("mass-defect-binding-energy-p5", BE_p5_7 / 16, "MeV")

# p6: calcium-40 -> binding energy per nucleon in MeV (two steps)
dm_p6_7 = mass_defect(20, 40, m_Ca40)
BE_p6_7 = dm_p6_7 * MeV_per_u
record("mass-defect-binding-energy-p6", BE_p6_7 / 40, "MeV")


# ---------------------------------------------------------------
# Type 8: reaction-energy-from-masses
# ---------------------------------------------------------------

# Nuclear masses in u
m_Ra226 = 225.977098
m_Rn222 = 221.970364
m_H3 = 3.015500
m_U235 = 234.993422
m_Ba141 = 140.883667
m_Kr92 = 91.906392
m_Po210 = 209.936758
m_Pb206 = 205.929447
m_N14 = 13.999231
m_O17 = 16.994740

# w: Ra-226 -> Rn-222 + He-4
dm_w8 = m_Ra226 - (m_Rn222 + m_He4)
record("reaction-energy-from-masses-w", dm_w8 * MeV_per_u, "MeV")

# p1: H-2 + H-3 -> He-4 + n
dm_p1_8 = (m_H2 + m_H3) - (m_He4 + m_n_u)
record("reaction-energy-from-masses-p1", dm_p1_8 * MeV_per_u, "MeV")

# p2: U-235 + n -> Ba-141 + Kr-92 + 3n
dm_p2_8 = (m_U235 + m_n_u) - (m_Ba141 + m_Kr92 + 3 * m_n_u)
record("reaction-energy-from-masses-p2", dm_p2_8 * MeV_per_u, "MeV")

# p3: Po-210 -> Pb-206 + He-4, energy in J (via kg)
dm_p3_8_u = m_Po210 - (m_Pb206 + m_He4)
dm_p3_8_kg = dm_p3_8_u * u_kg
record("reaction-energy-from-masses-p3", dm_p3_8_kg * c ** 2, "J")

# p4: D-D fusion releases 3.27 MeV -> mass decrease in kg
dm_p4_8_u = 3.27 / MeV_per_u
record("reaction-energy-from-masses-p4", dm_p4_8_u * u_kg, "kg")

# p5: N-14 + He-4 -> O-17 + p, energy absorbed in MeV (two steps)
dm_p5_8 = (m_N14 + m_He4) - (m_O17 + m_p_u)
Q_p5_8 = dm_p5_8 * MeV_per_u
record("reaction-energy-from-masses-p5", -Q_p5_8, "MeV")

# p6: Li-7 + p -> 2 He-4, energy per mole of Li-7 in J (two steps)
dm_p6_8 = (m_Li7 + m_p_u) - 2 * m_He4
Q_p6_8_J = dm_p6_8 * MeV_per_u * MeV
record("reaction-energy-from-masses-p6", Q_p6_8_J * N_A, "J")


# ---------------------------------------------------------------
# Type 9: energy-from-binding-energy-per-nucleon
# ---------------------------------------------------------------

# w: D + T -> He-4 + n; BE/A: D 1.11, T 2.83, He-4 7.07
BE_D = 2 * 1.11
BE_T = 3 * 2.83
BE_He4_w = 4 * 7.07
record("energy-from-be-per-nucleon-w", BE_He4_w - (BE_D + BE_T), "MeV")

# p1: U-235 + n -> Ba-141 + Kr-92 + 3n; BE/A: U 7.59, Ba 8.33, Kr 8.51
BE_U235 = 235 * 7.59
BE_Ba141 = 141 * 8.33
BE_Kr92 = 92 * 8.51
record("energy-from-be-per-nucleon-p1", (BE_Ba141 + BE_Kr92) - BE_U235, "MeV")

# p2: He-3 + He-3 -> He-4 + 2p; BE/A: He-3 2.57, He-4 7.07
BE_He3 = 3 * 2.57
record("energy-from-be-per-nucleon-p2", 4 * 7.07 - 2 * BE_He3, "MeV")

# p3: U-238 -> Th-234 + He-4, energy in J; BE/A: U 7.570, Th 7.597, He 7.074
BE_U238 = 238 * 7.570
BE_Th234 = 234 * 7.597
BE_He4_p3 = 4 * 7.074
Q_p3_9_MeV = (BE_Th234 + BE_He4_p3) - BE_U238
record("energy-from-be-per-nucleon-p3", Q_p3_9_MeV * MeV, "J")

# p4: n + Pu-239 -> Xe-134 + Zr-103 + 3n releases 189 MeV;
#     BE/A: Pu 7.56, Xe 8.41 -> BE/A of Zr-103
BE_Pu239 = 239 * 7.56
BE_Xe134 = 134 * 8.41
BE_Zr103 = 189 + BE_Pu239 - BE_Xe134
record("energy-from-be-per-nucleon-p4", BE_Zr103 / 103, "MeV")

# p5: 4p -> He-4 (BE/A 7.07); Sun 3.9e26 W -> He-4 nuclei formed per second (two steps)
E_per_He4_J = 4 * 7.07 * MeV
record("energy-from-be-per-nucleon-p5", 3.9e26 / E_per_He4_J, "s⁻¹")

# p6: 3 He-4 -> C-12; BE/A: He 7.074, C 7.680; energy from forming 1.0 g of C-12 (two steps)
Q_p6_9_MeV = 12 * 7.680 - 3 * 4 * 7.074
Q_p6_9_J = Q_p6_9_MeV * MeV
N_p6_9 = (1.0 / 12) * N_A
record("energy-from-be-per-nucleon-p6", Q_p6_9_J * N_p6_9, "J")


# ---------------------------------------------------------------
# Type 10: nuclear-radius-density
# ---------------------------------------------------------------

r0 = 1.2e-15  # m


def nuclear_radius(A):
    """R = r0 * A^(1/3)."""
    return r0 * A ** (1 / 3)


# w: uranium-238 radius
record("nuclear-radius-density-w", nuclear_radius(238), "m")

# p1: iron-56 radius
record("nuclear-radius-density-p1", nuclear_radius(56), "m")

# p2: carbon-12 radius
record("nuclear-radius-density-p2", nuclear_radius(12), "m")

# p3: radius 4.8e-15 m -> nucleon number
record("nuclear-radius-density-p3", (4.8e-15 / r0) ** 3, "")

# p4: gold-197 radius in fm
record("nuclear-radius-density-p4", nuclear_radius(197) / 1e-15, "fm")

# p5: density of a helium-4 nucleus, mass 6.64e-27 kg (two steps)
R_p5_10 = nuclear_radius(4)
V_p5_10 = (4 / 3) * math.pi * R_p5_10 ** 3
record("nuclear-radius-density-p5", 6.64e-27 / V_p5_10, "kg m⁻³")

# p6: neutron star, mass 2.8e30 kg, density 2.3e17 kg m^-3 -> radius in km (two steps)
V_p6_10 = 2.8e30 / 2.3e17
R_p6_10 = (3 * V_p6_10 / (4 * math.pi)) ** (1 / 3)
record("nuclear-radius-density-p6", R_p6_10 / 1e3, "km")


# ---------------------------------------------------------------
# Type 11: closest-approach
# ---------------------------------------------------------------

def closest_approach(Z, KE_J):
    """d = 2 Z e^2 / (4 pi eps0 KE)."""
    return 2 * Z * e ** 2 / (4 * math.pi * eps0 * KE_J)


# w: 5.0 MeV alpha on gold (Z = 79)
KE_w11 = 5.0 * MeV
record("closest-approach-w", closest_approach(79, KE_w11), "m")

# p1: alpha with KE 8.0e-13 J on silver (Z = 47)
record("closest-approach-p1", closest_approach(47, 8.0e-13), "m")

# p2: alpha with KE 6.4e-13 J on copper (Z = 29)
record("closest-approach-p2", closest_approach(29, 6.4e-13), "m")

# p3: 4.8 MeV alpha on aluminium (Z = 13)
KE_p3_11 = 4.8 * MeV
record("closest-approach-p3", closest_approach(13, KE_p3_11), "m")

# p4: KE needed to reach 3.0e-14 m from a gold nucleus, in MeV
KE_p4_11_J = 2 * 79 * e ** 2 / (4 * math.pi * eps0 * 3.0e-14)
record("closest-approach-p4", KE_p4_11_J / MeV, "MeV")

# p5: alpha speed 1.5e7 m/s, mass 6.64e-27 kg, on gold (two steps)
KE_p5_11 = 0.5 * 6.64e-27 * (1.5e7) ** 2
record("closest-approach-p5", closest_approach(79, KE_p5_11), "m")

# p6: 6.0 MeV alpha reaches 2.4e-14 m -> Z of target (two steps)
KE_p6_11 = 6.0 * MeV
Z_p6_11 = 4 * math.pi * eps0 * 2.4e-14 * KE_p6_11 / (2 * e ** 2)
record("closest-approach-p6", Z_p6_11, "")


# ---------------------------------------------------------------
# Print
# ---------------------------------------------------------------

for question_id, rounded, unit, raw in results:
    print(f"{question_id:40s} {rounded:<14.6g} {unit:10s} (raw {raw:.6g})")
