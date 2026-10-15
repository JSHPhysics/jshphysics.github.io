"""
Independent check of practice answers (p2, p5, p6) for:
  gravitational-fields, electric-fields-capacitors, magnetic-fields-induction,
  nuclear-particles, astrophysics

Every value below was computed from the question text and the SCHEMA.md
standard constants only, BEFORE looking at the stored answer. The stored
value is read from data/ at the end purely for comparison. Nothing in data/
is modified.

Run:  python3 tools/verify_c.py
"""

import json
import math
import os

# ---------------------------------------------------------------------------
# Standard constants (SCHEMA.md)
# ---------------------------------------------------------------------------
g = 9.81
c = 3.00e8
e = 1.60e-19
h = 6.63e-34
G = 6.67e-11
k = 1.38e-23
R_gas = 8.31
N_A = 6.02e23
eps0 = 8.85e-12
mu0 = 4 * math.pi * 1e-7
sigma = 5.67e-8
m_e = 9.11e-31
m_p = 1.67e-27
m_n = 1.67e-27
u = 1.66e-27
u_MeV = 931.5
eV = 1.60e-19
MeV = 1.60e-13
wien = 2.90e-3
AU = 1.50e11
ly = 9.46e15
pc = 3.09e16
M_E = 5.97e24
R_E = 6.37e6
M_S = 1.99e30
kC = 1 / (4 * math.pi * eps0)   # Coulomb constant

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")

# id -> my independently computed value
mine = {}


def put(qid, value):
    """Register my value for a question id."""
    mine[qid] = value


# ===========================================================================
# GRAVITATIONAL FIELDS
# ===========================================================================

# newtons-law-of-gravitation
# p2: Sun on Earth at 1 AU
put("newtons-law-of-gravitation-p2", G * M_S * M_E / AU ** 2)

# p5: asteroid radius 10.0 km, density 2500, probe 500 kg on surface
r_ast = 10.0e3
M_ast = 2500 * (4 / 3) * math.pi * r_ast ** 3
put("newtons-law-of-gravitation-p5", G * M_ast * 500 / r_ast ** 2)

# p6: height where force is half surface value -> r = R*sqrt(2)
put("newtons-law-of-gravitation-p6", R_E * math.sqrt(2) - R_E)

# gravitational-field-strength
# p2: 266 N on 72 kg
put("gravitational-field-strength-p2", 266 / 72)

# p5: altitude (km) where g = 2.45 N/kg
r_245 = math.sqrt(G * M_E / 2.45)
put("gravitational-field-strength-p5", (r_245 - R_E) / 1000)

# p6: weight of 85 kg on Mercury
put("gravitational-field-strength-p6", 85 * G * 3.30e23 / (2.44e6) ** 2)

# gravitational-potential
# p2: 2000 kg at r = 4.22e7 m -> Ep = -GMm/r
put("gravitational-potential-p2", -G * M_E * 2000 / 4.22e7)

# p5: 12.0 tonnes at 400 km altitude
put("gravitational-potential-p5", -G * M_E * 12000 / (R_E + 400e3))

# p6: V = -GM/R, g = GM/R^2 -> R = -V/g
put("gravitational-potential-p6", 2.76e8 / 11.2)

# work-done-in-field
# p2: W = m * dV
put("work-done-in-field-p2", 70 * (-1.10e6 - (-2.82e6)))

# p5: Mars lander from 300 km orbit to surface: GMm(1/R - 1/(R+h))
M_mars = 6.42e23
R_mars = 3.39e6
put("work-done-in-field-p5", G * M_mars * 900 * (1 / R_mars - 1 / (R_mars + 300e3)))

# p6: meteoroid 25 kg from 8.00e7 m to Earth surface
put("work-done-in-field-p6", G * M_E * 25 * (1 / R_E - 1 / 8.00e7))

# escape-velocity
# p2: Mars
put("escape-velocity-p2", math.sqrt(2 * G * M_mars / R_mars))

# p5: asteroid radius 500 m, density 2000
r_a5 = 500
M_a5 = 2000 * (4 / 3) * math.pi * r_a5 ** 3
put("escape-velocity-p5", math.sqrt(2 * G * M_a5 / r_a5))

# p6: v = sqrt(2 g R)
put("escape-velocity-p6", math.sqrt(2 * 25.0 * 7.00e7))

# orbital-speed-and-period
# p2: period at r = 7.00e6 m around Earth
put("orbital-speed-and-period-p2", 2 * math.pi * math.sqrt((7.00e6) ** 3 / (G * M_E)))

# p5: Europa around Jupiter, period in days
M_J = 1.90e27
put("orbital-speed-and-period-p5", 2 * math.pi * math.sqrt((6.71e8) ** 3 / (G * M_J)) / 86400)

# p6: period 95.0 min -> altitude in km
T_95 = 95.0 * 60
r_95 = (G * M_E * T_95 ** 2 / (4 * math.pi ** 2)) ** (1 / 3)
put("orbital-speed-and-period-p6", (r_95 - R_E) / 1000)

# geostationary-orbit
# p2: Jupiter synchronous orbit radius
T_J = 9.93 * 3600
put("geostationary-orbit-p2", (G * M_J * T_J ** 2 / (4 * math.pi ** 2)) ** (1 / 3))

# p5: Pluto synchronous altitude in km
T_P = 6.39 * 86400
r_P = (G * 1.31e22 * T_P ** 2 / (4 * math.pi ** 2)) ** (1 / 3)
put("geostationary-orbit-p5", (r_P - 1.19e6) / 1000)

# p6: Mercury rotation period from synchronous altitude, in days
r_M = 2.44e6 + 2.38e8
put("geostationary-orbit-p6", 2 * math.pi * math.sqrt(r_M ** 3 / (G * 3.30e23)) / 86400)

# keplers-third-law
# p2: T_B = T_A (r_B/r_A)^1.5
put("keplers-third-law-p2", 97.0 * (2.80e7 / 7.00e6) ** 1.5)

# p5: from geostationary (24.0 h at 4.22e7) to 800 km altitude, in minutes
r_800 = R_E + 800e3
put("keplers-third-law-p5", 24.0 * 60 * (r_800 / 4.22e7) ** 1.5)

# p6: from Moon (27.3 d at 3.84e8) to T = 1.00 d -> altitude in m
r_1d = 3.84e8 * (1.00 / 27.3) ** (2 / 3)
put("keplers-third-law-p6", r_1d - R_E)

# ===========================================================================
# ELECTRIC FIELDS & CAPACITORS
# ===========================================================================

# coulombs-law
# p2: electron-proton at 5.3e-11 m
put("coulombs-law-p2", kC * e * e / (5.3e-11) ** 2)

# p5: two spheres each 2.5e10 electrons, 8.0 cm apart
q_sph = 2.5e10 * e
put("coulombs-law-p5", kC * q_sph * q_sph / 0.080 ** 2)

# p6: separation where force between alpha (2e) and gold (79e) is 2.0 N
put("coulombs-law-p6", math.sqrt(kC * 2 * 79 * e * e / 2.0))

# field-strength-point-charge
# p2: E = F/q
put("field-strength-point-charge-p2", 3.2e-5 / 4.0e-9)

# p5: r where E = 3.0e6 for Q = 8.0 uC
put("field-strength-point-charge-p5", math.sqrt(kC * 8.0e-6 / 3.0e6))

# p6: field from +3.0 uC at 0.25 m, force on -20 nC (answer unit N)
E_p6 = kC * 3.0e-6 / 0.25 ** 2
put("field-strength-point-charge-p6", E_p6 * 20e-9)

# uniform-field-parallel-plates
# p2: F = EQ
put("uniform-field-parallel-plates-p2", 8.0e-9 * 2.5e4)

# p5: electron acceleration, 250 V across 20 mm
E_gun = 250 / 0.020
put("uniform-field-parallel-plates-p5", e * E_gun / m_e)

# p6: argon ion acceleration, 1.2 kV across 3.0 cm
E_ar = 1200 / 0.030
put("uniform-field-parallel-plates-p6", e * E_ar / 6.64e-26)

# electric-potential-energy
# p2: W = Q dV
put("electric-potential-energy-p2", 3.0e-6 * 250)

# p5: W = kQq (1/r1 - 1/r2), magnitude
put("electric-potential-energy-p5", abs(kC * 6.0e-6 * 2.0e-9 * (1 / 0.20 - 1 / 0.50)))

# p6: EPE of alpha + gold at 4.5e-14 m, in MeV
put("electric-potential-energy-p6", kC * 2 * 79 * e * e / 4.5e-14 / MeV)

# capacitance
# p2: V = Q/C
put("capacitance-p2", 1.5e-3 / 100e-6)

# p5: Q = It, C = Q/V in uF
Q_p5 = 50e-6 * 40
put("capacitance-p5", Q_p5 / 8.0 * 1e6)

# p6: number of electrons = CV/e
put("capacitance-p6", 12e-12 * 5.0 / e)

# parallel-plate-capacitor
# p2: C = eps_r eps0 A/d
put("parallel-plate-capacitor-p2", 4.0 * eps0 * 0.015 / 2.5e-4)

# p5: eps_r = C d / (eps0 A)
put("parallel-plate-capacitor-p5", 4.7e-9 * 0.10e-3 / (eps0 * 0.012))

# p6: square plates side 8.0 cm, d = 0.50 mm, eps_r 6.0, 50 V -> Q
C_p6 = 6.0 * eps0 * (0.080 ** 2) / 0.50e-3
put("parallel-plate-capacitor-p6", C_p6 * 50)

# energy-stored-capacitor
# p2: E = 1/2 C V^2
put("energy-stored-capacitor-p2", 0.5 * 100e-6 * 50 ** 2)

# p5: energy delivered = 1/2 C (V1^2 - V2^2)
put("energy-stored-capacitor-p5", 0.5 * 4700e-6 * (12 ** 2 - 4.0 ** 2))

# p6: mean power in kW
E_flash = 0.5 * 1200e-6 * 300 ** 2
put("energy-stored-capacitor-p6", E_flash / 2.0e-3 / 1000)

# capacitors-series-parallel
# p2: 6 and 12 in series (uF)
put("capacitors-series-parallel-p2", 1 / (1 / 6.0 + 1 / 12.0))

# p5: (2 || 4) in series with 3
C_par = 2.0 + 4.0
put("capacitors-series-parallel-p5", 1 / (1 / C_par + 1 / 3.0))

# p6: 3 and 6 in series across 18 V -> charge on each in uC
C_ser = 1 / (1 / 3.0 + 1 / 6.0)
put("capacitors-series-parallel-p6", C_ser * 18)

# capacitor-discharge
# p2: V = V0 exp(-t/RC)
put("capacitor-discharge-p2", 12 * math.exp(-8.0 / 5.0))

# p5: t = -RC ln(0.25)
RC_p5 = 330e-6 * 22e3
put("capacitor-discharge-p5", -RC_p5 * math.log(0.25))

# p6: halves in 14 s through 100 kOhm -> C in uF
put("capacitor-discharge-p6", 14 / (100e3 * math.log(2)) * 1e6)

# capacitor-charging
# p2: V = V0 (1 - exp(-t/RC))
RC_ch2 = 1000e-6 * 4.7e3
put("capacitor-charging-p2", 12 * (1 - math.exp(-5.0 / RC_ch2)))

# p5: time to 90%: t = -RC ln(0.1)
RC_ch5 = 220e-6 * 56e3
put("capacitor-charging-p5", -RC_ch5 * math.log(0.10))

# p6: reaches half in 0.20 s with 100 uF -> R in kOhm
put("capacitor-charging-p6", 0.20 / (100e-6 * math.log(2)) / 1000)

# ===========================================================================
# MAGNETIC FIELDS & INDUCTION
# ===========================================================================

# force-on-conductor
# p2: F = BIL sin(theta)
put("force-on-conductor-p2", 0.60 * 4.0 * 0.25 * math.sin(math.radians(30)))

# p5: current balance: F = (0.45 g) * 9.81 ; I = F/(BL)
F_cb = 0.45e-3 * g
put("force-on-conductor-p5", F_cb / (0.120 * 0.060))

# p6: B = F/(IL), F = 1.2 g weight
F_mag = 1.2e-3 * g
put("force-on-conductor-p6", F_mag / (2.5 * 0.040))

# force-on-moving-charge
# p2: F = Bqv sin(theta), alpha q = 2e
put("force-on-moving-charge-p2", 0.40 * 2 * e * 1.5e7 * math.sin(math.radians(60)))

# p5: 500 eV electron in 20 mT
v_500 = math.sqrt(2 * 500 * eV / m_e)
put("force-on-moving-charge-p5", 0.020 * e * v_500)

# p6: a = Bqv/m for proton
put("force-on-moving-charge-p6", 0.80 * e * 2.0e6 / m_p)

# circular-path-radius
# p2: T = 2 pi m/(Bq) for proton in 1.5 T
put("circular-path-radius-p2", 2 * math.pi * m_p / (1.5 * e))

# p5: v = Bqr/m for argon 40 u
put("circular-path-radius-p5", 0.60 * e * 0.40 / (40 * u))

# p6: cyclotron frequency f = Bq/(2 pi m) in MHz
put("circular-path-radius-p6", 1.8 * e / (2 * math.pi * m_p) / 1e6)

# accelerate-then-deflect
# p2: electron through 400 V then B = 1.5e-3 T -> r
v_400 = math.sqrt(2 * e * 400 / m_e)
put("accelerate-then-deflect-p2", m_e * v_400 / (e * 1.5e-3))

# p5: protons r = 0.50 m in 0.30 T -> accelerating p.d. in MV
v_ring = e * 0.30 * 0.50 / m_p
put("accelerate-then-deflect-p5", 0.5 * m_p * v_ring ** 2 / e / 1e6)

# p6: m = B^2 r^2 q / (2V)
put("accelerate-then-deflect-p6", (0.45 ** 2) * (0.120 ** 2) * e / (2 * 2500))

# flux-and-flux-linkage
# p2: N B A
put("flux-and-flux-linkage-p2", 500 * 0.050 * 1.2e-3)

# p5: N B A cos(theta), circular coil diameter 8.0 cm
A_coil = math.pi * (0.040) ** 2
put("flux-and-flux-linkage-p5", 300 * 0.20 * A_coil * math.cos(math.radians(60)))

# p6: N = flux linkage / (B A), square side 5.0 cm
put("flux-and-flux-linkage-p6", 0.090 / (0.30 * 0.050 ** 2))

# faradays-law
# p2: emf = d(N phi)/dt
put("faradays-law-p2", (0.60 - 0.15) / 0.30)

# p5: N = emf dt / (dB A), A = 8.0 cm^2
put("faradays-law-p5", 3.2 * 0.15 / (0.60 * 8.0e-4))

# p6: emf = N A dB/dt ; I = emf / R
emf_p6 = 120 * 5.0e-3 * (0.90 - 0.30) / 0.040
put("faradays-law-p6", emf_p6 / 15)

# motional-emf
# p2: emf = B L v
put("motional-emf-p2", 5.0e-5 * 1.5 * 40)

# p5: falling rod, v = g t after 0.50 s
v_rod = g * 0.50
put("motional-emf-p5", 0.12 * 0.80 * v_rod)

# p6: I = BLv / R
put("motional-emf-p6", 0.50 * 0.40 * 6.0 / 2.0)

# transformers
# p2: Vs = Vp Ns/Np
put("transformers-p2", 12 * 2000 / 50)

# p5: Vs = 240 * 60/1200 = 12 V ; I = V/R
V_s = 240 * 60 / 1200
put("transformers-p5", V_s / 6.0)

# p6: efficiency = (Pin - loss)/Pin
P_in = 230 * 8.0
put("transformers-p6", (P_in - 120) / P_in * 100)

# ac-rms-values
# p2: V0 = Vrms sqrt2
put("ac-rms-values-p2", 110 * math.sqrt(2))

# p5: mean power = V0^2/(2R)
put("ac-rms-values-p5", 12 ** 2 / (2 * 8.0))

# p6: I0 = sqrt2 * P/Vrms
put("ac-rms-values-p6", math.sqrt(2) * 2000 / 230)

# ===========================================================================
# NUCLEAR & PARTICLES
# ===========================================================================

year = 3.15e7

# half-life-decay-constant
# p2: lambda = ln2 / 6.0 h
put("half-life-decay-constant-p2", math.log(2) / 6.0)

# p5: T1/2 in years
put("half-life-decay-constant-p5", math.log(2) / 9.12e-13 / year)

# p6: lambda in s^-1 for 4.47e9 y
put("half-life-decay-constant-p6", math.log(2) / (4.47e9 * year))

# activity-number-nuclei
# p2: N = (m/M) N_A
put("activity-number-nuclei-p2", 5.0 / 238 * N_A)

# p5: A = lambda N for 0.50 mg Po-210
N_po = 0.50e-3 / 210 * N_A
put("activity-number-nuclei-p5", 5.80e-8 * N_po)

# p6: N = A / lambda for I-131, half-life 8.02 d
lam_I = math.log(2) / (8.02 * 86400)
put("activity-number-nuclei-p6", 5.0e8 / lam_I)

# exponential-decay
# p2: N = N0 exp(-lambda t)
put("exponential-decay-p2", 6.0e20 * math.exp(-2.1e-6 * 1.5e5))

# p5: Co-60 after 12 y
put("exponential-decay-p5", 2.0e10 * math.exp(-math.log(2) * 12 / 5.27))

# p6: C-14 at 62%
put("exponential-decay-p6", -math.log(0.62) * 5730 / math.log(2))

# whole-half-lives
# p2: 165 s = 3 half-lives of 55 s
put("whole-half-lives-p2", 4000 / 2 ** 3)

# p5: 1/16 -> 4 half-lives
put("whole-half-lives-p5", 4 * 5730)

# p6: 2.4e6 / 7.5e4 = 32 = 2^5 in 60 min
n_hl = math.log(2.4e6 / 7.5e4) / math.log(2)
put("whole-half-lives-p6", 60 / n_hl)

# mass-energy
# p2: 2 m_e c^2
put("mass-energy-p2", 2 * m_e * c ** 2)

# p5: m = P t / c^2
put("mass-energy-p5", 1.2e9 * year / c ** 2)

# p6: 2.0 ug total annihilates
put("mass-energy-p6", 2.0e-9 * c ** 2)

# mev-u-si-conversions
# p2: proton rest energy in MeV using m_p = 1.67e-27
put("mev-u-si-conversions-p2", m_p * c ** 2 / MeV)

# p5: muon 1.88e-28 kg
put("mev-u-si-conversions-p5", 1.88e-28 * c ** 2 / MeV)

# p6: W boson 80.4 GeV/c^2 in kg
put("mev-u-si-conversions-p6", 80.4e9 * eV / c ** 2)

# mass-defect-binding-energy
# p2: 0.528 u -> MeV
put("mass-defect-binding-energy-p2", 0.528 * u_MeV)

# p5: O-16 BE per nucleon
mp_u = 1.007276
mn_u = 1.008665
dm_O = 8 * mp_u + 8 * mn_u - 15.990523
put("mass-defect-binding-energy-p5", dm_O * u_MeV / 16)

# p6: Ca-40 BE per nucleon
dm_Ca = 20 * mp_u + 20 * mn_u - 39.951611
put("mass-defect-binding-energy-p6", dm_Ca * u_MeV / 40)

# reaction-energy-from-masses
# p2: U-235 + n -> Ba-141 + Kr-92 + 3n
dm_fis = (234.993422 + 1.008665) - (140.883667 + 91.906392 + 3 * 1.008665)
put("reaction-energy-from-masses-p2", dm_fis * u_MeV)

# p5: N-14 + He-4 -> O-17 + p ; endothermic, min energy = (products - reactants)
dm_ruth = (16.994740 + 1.007276) - (13.999231 + 4.001506)
put("reaction-energy-from-masses-p5", dm_ruth * u_MeV)

# p6: p + Li-7 -> 2 He-4 ; per mole in J
dm_cw = (7.014356 + 1.007276) - 2 * 4.001506
put("reaction-energy-from-masses-p6", dm_cw * u_MeV * MeV * N_A)

# energy-from-be-per-nucleon
# p2: 2 He-3 -> He-4 + 2p : E = BE(He4) - 2 BE(He3)
put("energy-from-be-per-nucleon-p2", 4 * 7.07 - 2 * 3 * 2.57)

# p5: 4p -> He-4 releasing 4 * 7.07 MeV ; rate = L / E
E_He4 = 4 * 7.07 * MeV
put("energy-from-be-per-nucleon-p5", 3.9e26 / E_He4)

# p6: triple alpha: E per reaction = 12*7.680 - 3*4*7.074 ; 1.0 g C-12 = N_A/12 nuclei
E_3a = (12 * 7.680 - 12 * 7.074) * MeV
put("energy-from-be-per-nucleon-p6", E_3a * N_A / 12)

# nuclear-radius-density
# p2: r = r0 A^(1/3)
r0 = 1.2e-15
put("nuclear-radius-density-p2", r0 * 12 ** (1 / 3))

# p5: He-4 density
r_He = r0 * 4 ** (1 / 3)
put("nuclear-radius-density-p5", 6.64e-27 / ((4 / 3) * math.pi * r_He ** 3))

# p6: neutron star radius in km
put("nuclear-radius-density-p6", (3 * 2.8e30 / (4 * math.pi * 2.3e17)) ** (1 / 3) / 1000)

# closest-approach
# p2: d = k (2e)(Ze)/Ek, Z = 29
put("closest-approach-p2", kC * 2 * 29 * e * e / 6.4e-13)

# p5: Ek = 1/2 m v^2 , Z = 79
Ek_a = 0.5 * 6.64e-27 * (1.5e7) ** 2
put("closest-approach-p5", kC * 2 * 79 * e * e / Ek_a)

# p6: Z = Ek d / (k 2 e^2)
Ek_6 = 6.0e6 * eV
put("closest-approach-p6", Ek_6 * 2.4e-14 / (kC * 2 * e * e))

# ===========================================================================
# ASTROPHYSICS
# ===========================================================================

L_sun = 3.85e26
R_sun = 6.96e8

# distance-units
# p2: t = AU / c
put("distance-units-p2", AU / c)

# p5: 163 AU in hours
put("distance-units-p5", 163 * AU / c / 3600)

# p6: 548 ly in pc
put("distance-units-p6", 548 * ly / pc)

# parallax
# p2: d = 1/p
put("parallax-p2", 1 / 0.195)

# p5: Sirius in ly
put("parallax-p5", (1 / 0.379) * pc / ly)

# p6: Arcturus in m
put("parallax-p6", (1 / 0.0889) * pc)

# inverse-square
# p2: I = L / (4 pi d^2)
put("inverse-square-p2", 1.2e28 / (4 * math.pi * (4.0e17) ** 2))

# p5: d = sqrt(L/(4 pi I)) in ly
L_40 = 40 * L_sun
put("inverse-square-p5", math.sqrt(L_40 / (4 * math.pi * 2.6e-8)) / ly)

# p6: power on 3.5 m^2 panel near Venus
I_venus = L_sun / (4 * math.pi * (1.08e11) ** 2)
put("inverse-square-p6", I_venus * 3.5)

# stefan-boltzmann
# p2: L = 4 pi r^2 sigma T^4
put("stefan-boltzmann-p2", 4 * math.pi * (1.07e8) ** 2 * sigma * 3040 ** 4)

# p5: r = sqrt(L / (4 pi sigma T^4))
L_bet = 1.2e5 * L_sun
put("stefan-boltzmann-p5", math.sqrt(L_bet / (4 * math.pi * sigma * 3500 ** 4)))

# p6: 2.5 R_sun, 7200 K
put("stefan-boltzmann-p6", 4 * math.pi * (2.5 * R_sun) ** 2 * sigma * 7200 ** 4)

# wien-law
# p2: lambda_max in nm
put("wien-law-p2", wien / 12100 * 1e9)

# p5: peak frequency 3.4e14 Hz -> lambda = c/f -> T
lam_p5 = c / 3.4e14
put("wien-law-p5", wien / lam_p5)

# p6: CMB 2.73 K -> peak frequency via lambda
lam_cmb = wien / 2.73
put("wien-law-p6", c / lam_cmb)

# wien-stefan-combined
# p2: T from Wien then L
T_rg = wien / 1000e-9
put("wien-stefan-combined-p2", 4 * math.pi * (3.5e10) ** 2 * sigma * T_rg ** 4)

# p5: L / L_sun
T_p5 = wien / 362.5e-9
L_p5 = 4 * math.pi * (1.2e9) ** 2 * sigma * T_p5 ** 4
put("wien-stefan-combined-p5", L_p5 / L_sun)

# p6: r / R_sun
T_p6 = wien / 1160e-9
r_p6 = math.sqrt(1.2e30 / (4 * math.pi * sigma * T_p6 ** 4))
put("wien-stefan-combined-p6", r_p6 / R_sun)

# redshift
# p2: z = d_lambda / lambda
put("redshift-p2", 12.4 / 486.1)

# p5: v = c d_lambda / lambda in km/s
put("redshift-p5", c * (21.80 - 21.11) / 21.11 / 1000)

# p6: Andromeda approaching, |d_lambda| = 0.3 nm
put("redshift-p6", c * (589.0 - 588.7) / 589.0 / 1000)

# hubble-law
# p2: d = v / H0
put("hubble-law-p2", 21000 / 70)

# p5: v = z c ; d = v / H0
v_z = 0.030 * c / 1000
put("hubble-law-p5", v_z / 70)

# p6: d in Mpc then v = H0 d
d_Mpc = 3.5e8 * ly / pc / 1e6
put("hubble-law-p6", 70 * d_Mpc)

# hubble-age
# p2: t = 1/H0 in years (1 y = 3.16e7 s)
put("hubble-age-p2", 1 / 2.3e-18 / 3.16e7)

# p5: H0 from one galaxy then age
H0_p5 = 6500e3 / (100e6 * pc)
put("hubble-age-p5", 1 / H0_p5 / 3.16e7)

# p6: Hubble distance c/H0 in ly, H0 = 68 km/s/Mpc
H0_p6 = 68e3 / (1e6 * pc)
put("hubble-age-p6", c / H0_p6 / ly)

# magnitudes
# p2: m = M + 5 log10(d/10)
put("magnitudes-p2", -3.6 + 5 * math.log10(133 / 10))

# p5: d = 1/p = 80 pc ; M = m - 5 log10(d/10)
d_p5 = 1 / 0.0125
put("magnitudes-p5", 3.5 - 5 * math.log10(d_p5 / 10))

# p6: d = 10^((m - M)/5 + 1) pc -> ly
d_cep = 10 ** ((12.0 - (-4.0)) / 5 + 1)
put("magnitudes-p6", d_cep * pc / ly)

# schwarzschild-radius
# p2: r = 2GM/c^2
put("schwarzschild-radius-p2", 2 * G * 8.2e36 / c ** 2)

# p5: 15 solar masses, km
put("schwarzschild-radius-p5", 2 * G * 15 * M_S / c ** 2 / 1000)

# p6: M = r c^2 / (2G) in solar masses
put("schwarzschild-radius-p6", 1.9e13 * c ** 2 / (2 * G) / M_S)


# ===========================================================================
# Compare with stored answers
# ===========================================================================

def main():
    files = [
        "gravitational-fields",
        "electric-fields-capacitors",
        "magnetic-fields-induction",
        "nuclear-particles",
        "astrophysics",
    ]
    stored = {}
    for name in files:
        path = os.path.join(DATA_DIR, name + ".json")
        with open(path) as fh:
            doc = json.load(fh)
        for t in doc["types"]:
            for p in t["practice"]:
                stored[p["id"]] = (p["answer"]["value"], p["answer"].get("unit", ""))

    checked = 0
    ok = 0
    bad = 0
    missing = []
    for qid in mine:
        if qid not in stored:
            missing.append(qid)
            continue
        sv, unit = stored[qid]
        mv = mine[qid]
        checked += 1
        if sv == 0:
            match = abs(mv) < 1e-12
        else:
            match = abs(mv - sv) / abs(sv) <= 0.01
        if match:
            ok += 1
            flag = "OK"
        else:
            bad += 1
            flag = "MISMATCH"
        print(f"{flag:9s} {qid:42s} mine={mv:.4g}  stored={sv:.4g} {unit}")

    print()
    print(f"checked={checked} ok={ok} mismatch={bad}")
    if missing:
        print("ids not found in data:", missing)


if __name__ == "__main__":
    main()
