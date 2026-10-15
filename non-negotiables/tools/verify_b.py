#!/usr/bin/env python3
"""
Independent check (checker B) of practice questions p2, p5 and p6 for
waves, quantum, electricity, circular-shm and thermal-gases.

Every value below was computed from the question text alone, using the
standard constants in SCHEMA.md, before the stored answer was looked at.
The script then compares with answer.value in data/ and prints OK/MISMATCH
(1% tolerance). It does not modify anything in data/.
"""

import json
import math
import os

# --- standard constants from SCHEMA.md ---------------------------------
g = 9.81
c = 3.00e8
e = 1.60e-19
h = 6.63e-34
k = 1.38e-23
R = 8.31
N_A = 6.02e23
m_e = 9.11e-31
m_p = 1.67e-27
m_n = 1.67e-27
pi = math.pi

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")

# id -> (my value, one-line reasoning)
mine = {}


def add(qid, value, reasoning):
    mine[qid] = (value, reasoning)


# =======================================================================
# WAVES
# =======================================================================

# wave-equation
add("wave-equation-p2", 1 / 12, "f = 1/T = 1/12")
T = 20e-6
f = 1 / T
add("wave-equation-p5", (340 / f) * 1e3, "f = 1/20 μs = 5.0e4 Hz; λ = v/f = 340/5e4 m, in mm")
v = 240e3 / 40
add("wave-equation-p6", v / 2.0, "v = 240 km / 40 s = 6000 m/s; λ = v/f = 6000/2.0")

# phase-difference
add("phase-difference-p2", 0.50 / 4.0 * 360, "Δφ = (Δt/T) × 360 = (0.5/4.0) × 360")
lam = 1.5 / 2.5
add("phase-difference-p5", 0.45 / lam * 360, "λ = v/f = 0.6 m; Δφ = (0.45/0.6) × 360")
lam = c / 100e6
add("phase-difference-p6", 0.50 / lam * 2 * pi, "λ = c/f = 3.0 m; Δφ = (0.5/3.0) × 2π rad")

# intensity
add("intensity-p2", 60 / (4 * pi * 2.0**2), "I = P/(4πr²) = 60/(4π × 4)")
I = 50e3 / (4 * pi * (10e3) ** 2)
add("intensity-p5", I * 0.20, "I = 50e3/(4π × 1e8) = 3.98e-5 W/m²; P = I × 0.20 m²")
add("intensity-p6", 0.80 * 1.5 / 6.0, "I ∝ 1/r², I ∝ A² so A ∝ 1/r: 0.80 × 1.5/6.0 mm")

# refractive-index
add("refractive-index-p2", math.degrees(math.asin(math.sin(math.radians(55)) / 1.33)),
    "sin r = sin 55°/1.33")
n = c / 2.10e8
add("refractive-index-p5", math.degrees(math.asin(math.sin(math.radians(35)) / n)),
    "n = c/v = 1.4286; sin r = sin 35°/1.4286")
n = math.sin(math.radians(60)) / math.sin(math.radians(35))
add("refractive-index-p6", c / n, "n = sin 60°/sin 35° = 1.510; v = c/n")

# critical-angle
add("critical-angle-p2", math.degrees(math.asin(1.46 / 1.48)), "sin C = n2/n1 = 1.46/1.48")
n = c / 2.01e8
add("critical-angle-p5", math.degrees(math.asin(1 / n)), "n = c/v = 1.4925; sin C = 1/n")
n = math.sin(math.radians(48)) / math.sin(math.radians(29))
add("critical-angle-p6", math.degrees(math.asin(1 / n)), "n = sin 48°/sin 29° = 1.533; sin C = 1/n")

# double-slit
add("double-slit-p2", 4.8e-3 * 0.40e-3 / 3.0 * 1e9, "λ = ws/D = 4.8e-3 × 0.4e-3 / 3.0, in nm")
w = 22e-3 / 10
add("double-slit-p5", w * 0.60e-3 / 2.0 * 1e9, "1st to 11th bright = 10 spacings → w = 2.2 mm; λ = ws/D")
lam = c / 4.74e14
add("double-slit-p6", lam * 2.4 / 0.20e-3 * 1e3, "λ = c/f = 632.9 nm; w = λD/s in mm")

# diffraction-grating
d = 1e-3 / 500
add("diffraction-grating-p2", d * math.sin(math.radians(18.0)) * 1e9, "d = 1/500 mm = 2.0e-6 m; λ = d sin 18°")
d = 1e-3 / 600
add("diffraction-grating-p5", d * math.sin(math.radians(18.0)) * 1e9, "two first orders 36° apart → θ = 18°; d = 1/600 mm; λ = d sin θ")
d = 1e-3 / 300
lam = c / 4.50e14
add("diffraction-grating-p6", math.degrees(math.asin(lam / d)), "λ = c/f = 666.7 nm; d = 3.333e-6 m; sin θ = λ/d")

# string-harmonics
add("string-harmonics-p2", 2 * 270 / (2 * 0.90), "f1 = v/2L = 150 Hz; 2nd harmonic = 2f1")
v = math.sqrt(72 / 1.25e-3)
add("string-harmonics-p5", v / (2 * 0.60), "v = √(T/μ) = 240 m/s; f1 = v/2L")
lam = 2 * 1.2 / 3
add("string-harmonics-p6", 50 * lam, "3 loops → λ = 2L/3 = 0.80 m; v = fλ")

# pipe-harmonics
add("pipe-harmonics-p2", 2 * 330 / (2 * 0.60), "open pipe: f1 = v/2L = 275 Hz; 2nd harmonic = 550 Hz")
add("pipe-harmonics-p5", 512 * 4 * 0.166, "closed pipe fundamental: L = λ/4 → λ = 0.664 m; v = fλ")
add("pipe-harmonics-p6", 5 * 340 / (4 * 850), "closed pipe 5th harmonic: f = 5v/4L → L = 5v/4f")

# doppler
add("doppler-p2", 500 * 6.0e4 / c, "Δλ = λ v/c = 500 × 6e4/3e8 nm")
add("doppler-p5", 486.1 * (1 + 1.5e7 / c), "Δλ = 486.1 × 1.5e7/3e8 = 24.3 nm; observed = 486.1 + 24.3 (receding)")
f = c / 0.211
add("doppler-p6", f * 4.5e6 / c / 1e6, "f = c/λ = 1.422e9 Hz; Δf = f v/c, in MHz")

# =======================================================================
# QUANTUM
# =======================================================================

# photon-energy
add("photon-energy-p2", h * c / 0.10e-9, "E = hc/λ = 6.63e-34 × 3e8 / 1e-10")
add("photon-energy-p5", h * c / 254e-9 / e, "E = hc/λ = 7.83e-19 J; ÷ 1.6e-19 → eV")
add("photon-energy-p6", 1.17e6 * e / h, "E = 1.17e6 × 1.6e-19 = 1.872e-13 J; f = E/h")

# ev-and-joules
add("ev-and-joules-p2", 3.2e-18 / e, "3.2e-18 / 1.6e-19")
add("ev-and-joules-p5", math.sqrt(2 * e * 500 / m_e), "eV = ½mv² → v = √(2eV/m_e)")
add("ev-and-joules-p6", math.sqrt(2 * e * 25e3 / m_p), "v = √(2eV/m_p) with V = 25 kV")

# photons-per-second
add("photons-per-second-p2", 10e3 / (h * 1.0e6), "E = hf = 6.63e-28 J; N = P/E = 1e4/6.63e-28")
E = h * c / 589e-9
add("photons-per-second-p5", 0.30 * 150 / E, "light power = 45 W; E = hc/λ = 3.377e-19 J; N = 45/E")
E = h * c / 550e-9
add("photons-per-second-p6", 1.4e3 * 2.0 / E, "P = IA = 2800 W; E = hc/λ = 3.616e-19 J; N = P/E")

# threshold-frequency
add("threshold-frequency-p2", 7.5e-19 / h, "f0 = φ/h")
add("threshold-frequency-p5", h * c / 430e-9 / e, "φ = hc/λ0 = 4.626e-19 J → eV")
add("threshold-frequency-p6", h * c / (5.10 * e) * 1e9, "λ0 = hc/φ, φ = 5.10 × 1.6e-19 J, in nm")

# photoelectric-equation
add("photoelectric-equation-p2", h * 1.2e15 - 6.9e-19, "KEmax = hf − φ = 7.956e-19 − 6.9e-19")
add("photoelectric-equation-p5", h * c / 450e-9 / e - 0.85, "hc/λ = 4.42e-19 J = 2.7625 eV; φ = hf − eVs = 2.7625 − 0.85 eV")
add("photoelectric-equation-p6", h * c / 350e-9 / e - 2.10, "hc/λ = 3.552 eV; Vs = (hf − φ)/e = 3.552 − 2.10 V")

# energy-levels
add("energy-levels-p2", 3.36e-19 / h, "f = E/h")
add("energy-levels-p5", h * c / (13.6 * e) * 1e9, "λ = hc/E with E = 13.6 × 1.6e-19 J, in nm")
dE = (13.6 - 1.51) * e
add("energy-levels-p6", dE / h, "ΔE = 12.09 eV = 1.934e-18 J; f = ΔE/h")

# de-broglie
add("de-broglie-p2", h / 4.5e-24, "λ = h/p")
p = math.sqrt(2 * m_e * e * 1.5e3)
add("de-broglie-p5", h / p, "p = √(2 m_e e V) = 2.091e-23; λ = h/p")
p = math.sqrt(2 * m_n * 0.025 * e)
add("de-broglie-p6", h / p, "KE = 0.025 × 1.6e-19 = 4e-21 J; p = √(2 m_n KE) = 3.655e-24; λ = h/p")

# specific-charge
add("specific-charge-p2", 2 * e / (2 * m_p + 2 * m_n), "q/m = 2e/(4 × 1.67e-27)")
add("specific-charge-p5", 3 * e / (3 * m_p + 4 * m_n), "q/m = 3e/(7 × 1.67e-27)")
add("specific-charge-p6", (e / m_e) / (e / m_p), "(e/m_e)/(e/m_p) = m_p/m_e = 1.67e-27/9.11e-31")

# =======================================================================
# ELECTRICITY
# =======================================================================

# charge-current-time
add("charge-current-time-p2", 540 / 45, "I = Q/t")
add("charge-current-time-p5", 2.5e-6 * 4.0 / e, "Q = It = 1.0e-5 C; N = Q/e")
add("charge-current-time-p6", 3.0e20 * e / 8.0, "Q = Ne = 48 C; I = Q/t")

# pd-energy-charge
add("pd-energy-charge-p2", 2.4e3 / 200, "V = W/Q")
add("pd-energy-charge-p5", 230 * 0.50 * 180, "Q = It = 90 C; E = VQ = 230 × 90")
add("pd-energy-charge-p6", 360 / (1.5 * 40), "Q = It = 60 C; V = W/Q")

# resistance-v-i
add("resistance-v-i-p2", 230 / 20, "I = V/R")
add("resistance-v-i-p5", 230 / (2400 / 120), "I = Q/t = 2400/120 = 20 A; R = V/I")
add("resistance-v-i-p6", 9.0 / (4.2 / 0.35), "R = 4.2/0.35 = 12 Ω; I = 9.0/12")

# resistivity
add("resistivity-p2", 1.7e-8 * 25 / 1.0e-6, "R = ρL/A")
A = 1.7e-8 * 4.0 / 0.50
add("resistivity-p5", math.sqrt(4 * A / pi) * 1e3, "A = ρL/R = 1.36e-7 m²; d = √(4A/π), in mm")
Rw = 2.5 / 0.80
add("resistivity-p6", Rw * 1.3e-7 / 0.60, "R = V/I = 3.125 Ω; ρ = RA/L")

# resistor-combinations
add("resistor-combinations-p2", 1 / (1 / 20 + 1 / 30), "parallel: 20 × 30/50")
add("resistor-combinations-p5", 1 / (1 / 40 + 1 / 60), "series 10 + 30 = 40; 40 ∥ 60 = 24")
Rp = 1 / (1 / 12 + 1 / 6.0)
add("resistor-combinations-p6", 1 / (1 / (Rp + 5.0) + 1 / 18), "12 ∥ 6 = 4; + 5 = 9; 9 ∥ 18 = 6")

# current-pd-circuits
add("current-pd-circuits-p2", 6.0 / 12, "parallel → full 6.0 V across 12 Ω; I = V/R")
Rp = 1 / (1 / 6.0 + 1 / 3.0)
add("current-pd-circuits-p5", 9.0 / (2.0 + Rp), "6 ∥ 3 = 2 Ω; total 4 Ω; I = 9/4")
Rp = 1 / (1 / 12 + 1 / 6.0)
I = 12 / (3.0 + Rp)
add("current-pd-circuits-p6", I * Rp, "12 ∥ 6 = 4 Ω; total 7 Ω; I = 12/7; V = I × 4")

# power-energy
add("power-energy-p2", 12**2 / 4.0, "P = V²/R")
add("power-energy-p5", 230**2 / 1.8e3, "R = V²/P")
add("power-energy-p6", 24 * 4.0 * 300, "E = VIt = 24 × 4 × 300")

# emf-internal-resistance
add("emf-internal-resistance-p2", 9.0 / (16 + 2.0), "I = ε/(R + r)")
I = 4.5 / (2.6 + 0.40)
add("emf-internal-resistance-p5", I**2 * 2.6, "I = 4.5/3.0 = 1.5 A; P = I²R")
# 0.20(6.0 + r) = 0.30(3.8 + r) → 1.2 − 1.14 = 0.1 r
add("emf-internal-resistance-p6", (0.20 * 6.0 - 0.30 * 3.8) / (0.30 - 0.20),
    "ε = I1(R1 + r) = I2(R2 + r) → r = (1.2 − 1.14)/0.10")

# potential-divider
add("potential-divider-p2", 5.0 * 1.5 / (1.5 + 3.5), "V1 = Vs R1/(R1 + R2)")
I = (9.0 - 3.0) / 5.0e3
add("potential-divider-p5", 3.0 / I / 1e3, "thermistor p.d. = 6.0 V → I = 6/5k = 1.2 mA; R = 3.0/1.2 mA in kΩ")
I = (6.0 - 2.4) / 1.8e3
add("potential-divider-p6", 2.4 / I / 1e3, "V1 = 3.6 V → I = 3.6/1.8k = 2.0 mA; R2 = 2.4/2.0 mA in kΩ")

# drift-velocity
add("drift-velocity-p2", 5.8e28 * 4.0e-7 * 1.2e-4 * e, "I = nAve")
I = 3.0 / 2.0
add("drift-velocity-p5", I / (8.5e28 * 2.0e-7 * e), "I = V/R = 1.5 A; v = I/(nAe)")
A = pi * (0.030e-3 / 2) ** 2
add("drift-velocity-p6", 0.250 / (3.4e28 * A * e), "A = π(1.5e-5)² = 7.07e-10 m²; v = I/(nAe)")

# =======================================================================
# CIRCULAR-SHM
# =======================================================================

# angular-velocity
add("angular-velocity-p2", 2 * pi * 2.5, "ω = 2πf")
w = 180 * 2 * pi / 60
add("angular-velocity-p5", 0.34 * w, "ω = 180 × 2π/60 = 18.85 rad/s; v = ωr")
add("angular-velocity-p6", 2 * pi * 6.9e6 / 7.6e3, "T = 2πr/v")

# centripetal-acceleration
add("centripetal-acceleration-p2", 120**2 * 0.25, "a = ω²r")
add("centripetal-acceleration-p5", 4 * pi**2 * 1.50e11 / (3.16e7) ** 2, "a = 4π²r/T²")
w = 24 * 2 * pi / 60
add("centripetal-acceleration-p6", w**2 * 6.0, "ω = 24 × 2π/60 = 2.513 rad/s; a = ω²r")

# centripetal-force
add("centripetal-force-p2", 65 * 1.5**2 * 5.0, "F = mω²r")
w = 40 * 2 * pi / 60
add("centripetal-force-p5", 2.5 * w**2 * 1.6, "ω = 40 × 2π/60 = 4.189 rad/s; T = mω²r")
w = 2 * pi / 5.8e3
add("centripetal-force-p6", 450 * w**2 * 7.0e6, "ω = 2π/T; F = mω²r")

# vertical-circle
add("vertical-circle-p2", 0.30 * g + 0.30 * 4.0**2 / 0.90, "bottom: T = mg + mv²/r")
add("vertical-circle-p5", 70 * g + 70 * 150**2 / 500, "bottom: N = mg + mv²/r = 686.7 + 3150")
m = 0.025
add("vertical-circle-p6", math.sqrt((0.30 + m * g) * 0.20 / m), "top: N + mg = mv²/r → v = √((N + mg) r/m)")

# shm-kinematics
add("shm-kinematics-p2", 8.0**2 * 0.030, "a = ω²x")
w = 2 * pi * 440
add("shm-kinematics-p5", 0.60 * math.cos(w * 0.50e-3), "x = A cos(ωt), ω = 2π × 440, t = 5e-4 s, in mm")
w = 2 * pi * 1.5
add("shm-kinematics-p6", w * math.sqrt(0.080**2 - 0.050**2), "v = ω√(A² − x²)")

# mass-spring
add("mass-spring-p2", 1 / (2 * pi) * math.sqrt(2.2e4 / 350), "f = (1/2π)√(k/m)")
kk = 0.30 * g / 0.045
add("mass-spring-p5", 2 * pi * math.sqrt(0.30 / kk), "k = mg/e = 65.4 N/m; T = 2π√(m/k) (= 2π√(e/g))")
T = 15 / 20
add("mass-spring-p6", 4 * pi**2 * 0.60 / T**2, "T = 0.75 s; k = 4π²m/T²")

# pendulum
add("pendulum-p2", 1 / (2 * pi) * math.sqrt(g / 0.25), "f = (1/2π)√(g/L)")
T = 2 * pi * math.sqrt(1.2 / g)
add("pendulum-p5", 120 / T, "T = 2π√(1.2/9.81) = 2.198 s; N = 120/T")
T = 38.0 / 25
add("pendulum-p6", g * T**2 / (4 * pi**2), "T = 1.52 s; L = gT²/4π²")

# shm-energy
add("shm-energy-p2", 0.5 * 0.20 * 12**2 * 0.040**2, "KEmax = ½mω²A²")
add("shm-energy-p5", 0.5 * 0.30 * 8.0**2 * (0.10**2 - 0.060**2), "KE = ½mω²(A² − x²)")
add("shm-energy-p6", 0.12 * math.sqrt(50 / 0.40), "vmax = ωA = A√(k/m)")

# =======================================================================
# THERMAL-GASES
# =======================================================================

# temperature-conversion
add("temperature-conversion-p2", 180 + 273, "T/K = θ/°C + 273")
add("temperature-conversion-p5", 310 - (-20 + 273), "−20 °C = 253 K; rise = 310 − 253")
add("temperature-conversion-p6", (95 + 273) - 300, "95 °C = 368 K; rise = 368 − 300")

# specific-heat-capacity
add("specific-heat-capacity-p2", 80 * 4200 * 30, "E = mcΔθ")
E = 50 * 240
add("specific-heat-capacity-p5", E / (0.60 * 2100), "E = Pt = 12 000 J; Δθ = E/mc")
E = 8.5e3 * 360
add("specific-heat-capacity-p6", E / (4200 * (38 - 12)), "E = Pt = 3.06e6 J; m = E/(cΔθ)")

# specific-latent-heat
add("specific-latent-heat-p2", 3.5 * 23000, "E = mL")
add("specific-latent-heat-p5", 2.0e3 * 300 / 2.26e6, "E = Pt = 6.0e5 J; m = E/L")
add("specific-latent-heat-p6", 350 * 3600 / 2.4e6, "E = Pt = 1.26e6 J; m = E/L")

# heating-with-change-of-state
add("heating-with-change-of-state-p2", 2.0 * 23000 + 2.0 * 140 * (400 - 327), "mL + mcΔθ = 46 000 + 20 440")
add("heating-with-change-of-state-p5", 0.080 * 4200 * 75 + 0.080 * 2.26e6, "mcΔθ + mL = 25 200 + 180 800")
add("heating-with-change-of-state-p6", 50e3 / (4200 * 15 + 334000), "E = m(cΔθ + L) → m = 50 000/(63 000 + 334 000)")

# thermal-equilibrium
# m1 c1 (T1 − T) = m2 c2 (T − T2)
T = (0.50 * 390 * 100 + 1.0 * 4200 * 20) / (0.50 * 390 + 1.0 * 4200)
add("thermal-equilibrium-p2", T, "0.5 × 390 × (100 − T) = 1.0 × 4200 × (T − 20) → T = 103 500/4395")
T = (0.25 * 4200 * 85 + 0.050 * 3900 * 5) / (0.25 * 4200 + 0.050 * 3900)
add("thermal-equilibrium-p5", T, "1050(85 − T) = 195(T − 5) → T = 90 225/1245")
add("thermal-equilibrium-p6", 32 + 5.0 * 4200 * (32 - 15) / (1.2 * 450),
    "1.2 × 450 × (T − 32) = 5 × 4200 × 17 = 357 000 → T = 32 + 661.1")

# ideal-gas-moles
add("ideal-gas-moles-p2", 2.5e5 * 0.020 / (R * 295), "n = pV/RT")
add("ideal-gas-moles-p5", 0.25 * R * 293 / 101e3 * 1e3, "V = nRT/p with T = 293 K, in litres")
add("ideal-gas-moles-p6", 1.2e5 * 0.018 / (0.80 * R) - 273, "T = pV/nR = 324.9 K → °C")

# ideal-gas-molecules
add("ideal-gas-molecules-p2", 4.0e22 * k * 320 / 1.5e-3, "p = NkT/V")
n = 8.0e6 * 0.050 / (R * 290)
add("ideal-gas-molecules-p5", n * 0.028, "n = pV/RT = 166.0 mol; m = nM")
add("ideal-gas-molecules-p6", 12 / 44 * N_A, "n = 12/44 = 0.2727 mol; N = n N_A")

# gas-two-states
add("gas-two-states-p2", 3.0e-3 * 350 / 290, "V2 = V1 T2/T1 at constant p")
add("gas-two-states-p5", 3.5e5 * 0.50 * 293 / (1.0e5 * 277), "V2 = p1 V1 T2/(p2 T1), in cm³")
add("gas-two-states-p6", 2.0e5 * 0.030 * 300 / (1.2e5 * 0.040) - 273, "T2 = p2 V2 T1/(p1 V1) = 375 K → °C")

# kinetic-theory
add("kinetic-theory-p2", math.sqrt(3 * k * 300 / 4.65e-26), "c_rms = √(3kT/m)")
add("kinetic-theory-p5", math.sqrt(3 * R * 350 / 0.044), "c_rms = √(3RT/M)")
add("kinetic-theory-p6", math.sqrt(3 * 1.2e5 * 0.020 / (5.0e23 * 6.6e-26)), "pV = ⅓Nm<c²> → c_rms = √(3pV/Nm)")

# kinetic-energy-internal-energy
add("kinetic-energy-internal-energy-p2", 1.5 * 2.0 * R * 400, "U = (3/2) nRT")
add("kinetic-energy-internal-energy-p5", 1.5 * 2.0e5 * 0.015, "U = (3/2) pV")
add("kinetic-energy-internal-energy-p6", 1.5 * k * 5800 / e, "<KE> = (3/2) kT, in eV")


# =======================================================================
# compare with stored answers
# =======================================================================

def main():
    files = ["waves", "quantum", "electricity", "circular-shm", "thermal-gases"]
    stored = {}
    for name in files:
        path = os.path.join(DATA_DIR, name + ".json")
        with open(path, encoding="utf-8") as fh:
            topic = json.load(fh)
        for t in topic["types"]:
            for p in t["practice"]:
                stored[p["id"]] = (p["answer"]["value"], p["answer"].get("unit", ""), p["answer"].get("tolerance"))

    checked = 0
    ok = 0
    mismatches = []
    for qid, (val, why) in mine.items():
        if qid not in stored:
            print(f"{qid}: NOT FOUND in data")
            continue
        sval, unit, tol = stored[qid]
        checked += 1
        if sval == 0:
            rel = abs(val - sval)
        else:
            rel = abs(val - sval) / abs(sval)
        status = "OK" if rel <= 0.01 else "MISMATCH"
        if status == "OK":
            ok += 1
        else:
            mismatches.append((qid, val, sval, unit, why))
        print(f"{status:8s} {qid:38s} mine={val:.4g}  stored={sval}  {unit}  ({rel*100:.2f}%)")

    print()
    print(f"checked={checked} matches={ok} mismatches={len(mismatches)}")
    for qid, val, sval, unit, why in mismatches:
        print(f"  {qid}: mine={val:.4g} stored={sval} {unit} -- {why}")


if __name__ == "__main__":
    main()
