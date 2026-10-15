#!/usr/bin/env python3
"""Compute every answer in data/quantum.json.

Each answer is printed rounded to 3 s.f. with its question id.
Run: python3 tools/calc_quantum.py
"""

import math

# Standard constants from SCHEMA.md
h = 6.63e-34        # J s
c = 3.00e8          # m s^-1
e = 1.60e-19        # C (and 1 eV in J)
m_e = 9.11e-31      # kg
m_p = 1.67e-27      # kg
m_n = 1.67e-27      # kg
u = 1.66e-27        # kg

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
# Type 1: photon-energy   (E = hf = hc/λ)
# ---------------------------------------------------------------

# w: green laser pointer, 532 nm -> E in J
wavelength_w = 532e-9
record("photon-energy-w", h * c / wavelength_w, "J")

# p1: FM radio, f = 98.5 MHz -> E in J
frequency_p1 = 98.5e6
record("photon-energy-p1", h * frequency_p1, "J")

# p2: medical X-ray, λ = 0.10 nm -> E in J
wavelength_p2 = 0.10e-9
record("photon-energy-p2", h * c / wavelength_p2, "J")

# p3: LED photon of 2.5 eV -> λ in nm (convert eV to J, rearrange)
energy_p3 = 2.5 * e
wavelength_p3 = h * c / energy_p3
record("photon-energy-p3", wavelength_p3 / 1e-9, "nm")

# p4: microwave oven photon E = 1.62e-24 J -> f in GHz (rearrange, convert)
energy_p4 = 1.62e-24
frequency_p4 = energy_p4 / h
record("photon-energy-p4", frequency_p4 / 1e9, "GHz")

# p5: germicidal UV lamp 254 nm -> E in eV (two steps: J then eV)
wavelength_p5 = 254e-9
energy_p5_joules = h * c / wavelength_p5
record("photon-energy-p5", energy_p5_joules / e, "eV")

# p6: cobalt-60 gamma photon 1.17 MeV -> f in Hz (two steps: J then f)
energy_p6_joules = 1.17e6 * e
record("photon-energy-p6", energy_p6_joules / h, "Hz")


# ---------------------------------------------------------------
# Type 2: ev-and-joules   (1 eV = 1.60e-19 J; eV = ½mv²)
# ---------------------------------------------------------------

# w: alpha particle KE 5.0 MeV -> J
ke_w_ev = 5.0e6
record("ev-and-joules-w", ke_w_ev * e, "J")

# p1: work function 4.5 eV -> J
record("ev-and-joules-p1", 4.5 * e, "J")

# p2: electron KE 3.2e-18 J -> eV
record("ev-and-joules-p2", 3.2e-18 / e, "eV")

# p3: X-ray tube photon 35 keV -> J (convert keV to eV first)
ke_p3_ev = 35e3
record("ev-and-joules-p3", ke_p3_ev * e, "J")

# p4: fission fragment KE 1.28e-11 J -> MeV (convert J to eV, then to MeV)
ke_p4_ev = 1.28e-11 / e
record("ev-and-joules-p4", ke_p4_ev / 1e6, "MeV")

# p5: electron accelerated through 500 V -> speed (two steps)
ke_p5 = 500 * e
speed_p5 = math.sqrt(2 * ke_p5 / m_e)
record("ev-and-joules-p5", speed_p5, "m s⁻¹")

# p6: proton accelerated through 25 kV -> speed (two steps)
ke_p6 = 25e3 * e
speed_p6 = math.sqrt(2 * ke_p6 / m_p)
record("ev-and-joules-p6", speed_p6, "m s⁻¹")


# ---------------------------------------------------------------
# Type 3: photons-per-second   (P = N × hf, N = P / E)
# ---------------------------------------------------------------

# w: 5.0 mW red laser, 650 nm -> N per second
energy_w3 = h * c / 650e-9
record("photons-per-second-w", 5.0e-3 / energy_w3, "s⁻¹")

# p1: 60 W lamp, photon energy 3.0e-19 J -> N per second
record("photons-per-second-p1", 60 / 3.0e-19, "s⁻¹")

# p2: 10 kW transmitter at 1.0 MHz -> N per second
energy_p2_3 = h * 1.0e6
record("photons-per-second-p2", 10e3 / energy_p2_3, "s⁻¹")

# p3: 20 mW blue LED, 470 nm -> N per second (unit conversions)
energy_p3_3 = h * c / 470e-9
record("photons-per-second-p3", 20e-3 / energy_p3_3, "s⁻¹")

# p4: detector receives 1.5e12 photons/s at 1550 nm -> power in nW (rearrange)
energy_p4_3 = h * c / 1550e-9
power_p4 = 1.5e12 * energy_p4_3
record("photons-per-second-p4", power_p4 / 1e-9, "nW")

# p5: 150 W sodium lamp, 30% as light at 589 nm -> N per second (two steps)
light_power_p5 = 0.30 * 150
energy_p5_3 = h * c / 589e-9
record("photons-per-second-p5", light_power_p5 / energy_p5_3, "s⁻¹")

# p6: 1.4 kW/m² on 2.0 m² panel, mean λ 550 nm -> N per second (two steps)
power_p6 = 1.4e3 * 2.0
energy_p6_3 = h * c / 550e-9
record("photons-per-second-p6", power_p6 / energy_p6_3, "s⁻¹")


# ---------------------------------------------------------------
# Type 4: threshold-frequency   (φ = hf₀, λ₀ = hc/φ)
# ---------------------------------------------------------------

# w: sodium φ = 2.28 eV -> f₀
phi_w4 = 2.28 * e
record("threshold-frequency-w", phi_w4 / h, "Hz")

# p1: caesium f₀ = 4.6e14 Hz -> φ in J
record("threshold-frequency-p1", h * 4.6e14, "J")

# p2: copper φ = 7.5e-19 J -> f₀
record("threshold-frequency-p2", 7.5e-19 / h, "Hz")

# p3: zinc f₀ = 1.04e15 Hz -> φ in eV
phi_p3_joules = h * 1.04e15
record("threshold-frequency-p3", phi_p3_joules / e, "eV")

# p4: platinum λ₀ = 196 nm -> φ in J
record("threshold-frequency-p4", h * c / 196e-9, "J")

# p5: lithium λ₀ = 430 nm -> φ in eV (two steps)
phi_p5_joules = h * c / 430e-9
record("threshold-frequency-p5", phi_p5_joules / e, "eV")

# p6: gold φ = 5.10 eV -> λ₀ in nm (two steps)
phi_p6_joules = 5.10 * e
wavelength_p6_4 = h * c / phi_p6_joules
record("threshold-frequency-p6", wavelength_p6_4 / 1e-9, "nm")


# ---------------------------------------------------------------
# Type 5: photoelectric-equation   (hf = φ + KE_max; eV_s = KE_max)
# ---------------------------------------------------------------

# w: sodium φ = 2.28 eV, light 420 nm -> KE_max in J
photon_w5 = h * c / 420e-9
phi_w5 = 2.28 * e
record("photoelectric-equation-w", photon_w5 - phi_w5, "J")

# p1: photon 5.0 eV, φ = 2.9 eV -> KE_max in eV
record("photoelectric-equation-p1", 5.0 - 2.9, "eV")

# p2: f = 1.2e15 Hz on zinc φ = 6.9e-19 J -> KE_max in J
photon_p2_5 = h * 1.2e15
record("photoelectric-equation-p2", photon_p2_5 - 6.9e-19, "J")

# p3: 310 nm on potassium φ = 2.30 eV -> KE_max in eV
photon_p3_5 = h * c / 310e-9
photon_p3_5_ev = photon_p3_5 / e
record("photoelectric-equation-p3", photon_p3_5_ev - 2.30, "eV")

# p4: 250 nm, KE_max = 2.40e-19 J -> φ in eV (rearrange)
photon_p4_5 = h * c / 250e-9
phi_p4_5 = photon_p4_5 - 2.40e-19
record("photoelectric-equation-p4", phi_p4_5 / e, "eV")

# p5: V_s = 0.85 V with 450 nm light -> φ in eV (two steps)
photon_p5_5_ev = (h * c / 450e-9) / e
ke_p5_5_ev = 0.85
record("photoelectric-equation-p5", photon_p5_5_ev - ke_p5_5_ev, "eV")

# p6: 350 nm on caesium φ = 2.10 eV -> stopping potential (two steps)
photon_p6_5_ev = (h * c / 350e-9) / e
ke_p6_5_ev = photon_p6_5_ev - 2.10
record("photoelectric-equation-p6", ke_p6_5_ev, "V")


# ---------------------------------------------------------------
# Type 6: energy-levels   (ΔE = E₁ − E₂ = hf = hc/λ)
# ---------------------------------------------------------------

# w: hydrogen −1.51 eV to −3.40 eV -> λ in nm
delta_w6 = (-1.51) - (-3.40)
wavelength_w6 = h * c / (delta_w6 * e)
record("energy-levels-w", wavelength_w6 / 1e-9, "nm")

# p1: −0.85 eV to −3.40 eV -> ΔE in eV
record("energy-levels-p1", (-0.85) - (-3.40), "eV")

# p2: transition releases 3.36e-19 J -> f
record("energy-levels-p2", 3.36e-19 / h, "Hz")

# p3: mercury −5.5 eV to −10.4 eV -> λ in nm
delta_p3_6 = (-5.5) - (-10.4)
wavelength_p3_6 = h * c / (delta_p3_6 * e)
record("energy-levels-p3", wavelength_p3_6 / 1e-9, "nm")

# p4: sodium 589 nm emitted dropping to −5.14 eV -> upper level in eV
delta_p4_6_ev = (h * c / 589e-9) / e
record("energy-levels-p4", -5.14 + delta_p4_6_ev, "eV")

# p5: ionise hydrogen from −13.6 eV -> longest λ in nm (two steps)
ionisation_joules = 13.6 * e
wavelength_p5_6 = h * c / ionisation_joules
record("energy-levels-p5", wavelength_p5_6 / 1e-9, "nm")

# p6: hydrogen −1.51 eV to −13.6 eV -> f of emitted photon (two steps: eV -> J -> f)
delta_p6_6_ev = (-1.51) - (-13.6)
delta_p6_6_joules = delta_p6_6_ev * e
record("energy-levels-p6", delta_p6_6_joules / h, "Hz")


# ---------------------------------------------------------------
# Type 7: de-broglie   (λ = h/p = h/mv)
# ---------------------------------------------------------------

# w: electron at 2.0e6 m/s -> λ
record("de-broglie-w", h / (m_e * 2.0e6), "m")

# p1: proton at 5.0e5 m/s -> λ
record("de-broglie-p1", h / (m_p * 5.0e5), "m")

# p2: electron with momentum 4.5e-24 kg m/s -> λ
record("de-broglie-p2", h / 4.5e-24, "m")

# p3: tennis ball 58 g at 50 m/s -> λ (convert g)
mass_p3_7 = 58e-3
record("de-broglie-p3", h / (mass_p3_7 * 50), "m")

# p4: electrons with λ = 0.15 nm -> speed (rearrange, convert nm)
wavelength_p4_7 = 0.15e-9
record("de-broglie-p4", h / (m_e * wavelength_p4_7), "m s⁻¹")

# p5: electron accelerated through 1.5 kV -> λ (two steps)
ke_p5_7 = 1.5e3 * e
speed_p5_7 = math.sqrt(2 * ke_p5_7 / m_e)
record("de-broglie-p5", h / (m_e * speed_p5_7), "m")

# p6: thermal neutron KE 0.025 eV -> λ (two steps via momentum)
ke_p6_7 = 0.025 * e
momentum_p6_7 = math.sqrt(2 * m_n * ke_p6_7)
record("de-broglie-p6", h / momentum_p6_7, "m")


# ---------------------------------------------------------------
# Type 8: specific-charge   (specific charge = Q / m)
# ---------------------------------------------------------------

# w: electron
record("specific-charge-w", e / m_e, "C kg⁻¹")

# p1: proton
record("specific-charge-p1", e / m_p, "C kg⁻¹")

# p2: alpha particle ⁴He²⁺, mass = 2 m_p + 2 m_n
mass_alpha = 2 * m_p + 2 * m_n
record("specific-charge-p2", (2 * e) / mass_alpha, "C kg⁻¹")

# p3: Ca²⁺ ion, mass 40 u (convert u)
mass_p3_8 = 40 * u
record("specific-charge-p3", (2 * e) / mass_p3_8, "C kg⁻¹")

# p4: specific charge 2.4e7 C/kg, charge +3e -> mass (rearrange)
charge_p4_8 = 3 * e
record("specific-charge-p4", charge_p4_8 / 2.4e7, "kg")

# p5: ⁷Li nucleus (3 p, 4 n) -> specific charge (two steps)
mass_p5_8 = 3 * m_p + 4 * m_n
record("specific-charge-p5", (3 * e) / mass_p5_8, "C kg⁻¹")

# p6: ratio of specific charge of electron to that of proton (two steps)
sc_electron = e / m_e
sc_proton = e / m_p
record("specific-charge-p6", sc_electron / sc_proton, "")


# ---------------------------------------------------------------
# Print
# ---------------------------------------------------------------

for question_id, rounded, unit, raw in results:
    print(f"{question_id:28s} {rounded!r:>14}  {unit:10s} (raw {raw!r})")
