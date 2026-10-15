#!/usr/bin/env python3
"""Compute every answer in data/thermal-gases.json.

Each answer is printed rounded to 3 s.f. with its question id.
Run: python3 tools/calc_thermal-gases.py
"""

import math

# Standard constants from SCHEMA.md
k = 1.38e-23      # J K^-1   (Boltzmann constant)
R = 8.31          # J mol^-1 K^-1
N_A = 6.02e23     # mol^-1
eV = 1.60e-19     # J

# Kelvin offset used throughout (A-level data sheets use 273)
ZERO_C_IN_K = 273

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
        # Large round numbers are stored as integers so the JSON is tidy;
        # very large values (10¹⁵ and above) stay as floats such as 6.04e+23
        # because int() of a float that size is not exact
        if places <= 0 and abs(rounded) < 1e15:
            rounded = int(rounded)
    results.append((question_id, rounded, unit, value))


# ---------------------------------------------------------------
# Type 1: temperature-conversion
# ---------------------------------------------------------------

# w: body temperature 37 C -> K
record("temperature-conversion-w", 37 + ZERO_C_IN_K, "K")

# p1: liquid nitrogen boils at 77 K -> C
record("temperature-conversion-p1", 77 - ZERO_C_IN_K, "°C")

# p2: oven at 180 C -> K
record("temperature-conversion-p2", 180 + ZERO_C_IN_K, "K")

# p3: tea cools from 85 C to 22 C; difference in K (same size as in C)
record("temperature-conversion-p3", 85 - 22, "K")

# p4: surface of Sun 5800 K -> C
record("temperature-conversion-p4", 5800 - ZERO_C_IN_K, "°C")

# p5: gas heated from -20 C to 310 K; rise in K (convert first, then subtract)
start_K_p5 = -20 + ZERO_C_IN_K
record("temperature-conversion-p5", 310 - start_K_p5, "K")

# p6: thermometer reads 300 K, later reads 95 C; rise in K (convert then subtract)
end_K_p6 = 95 + ZERO_C_IN_K
record("temperature-conversion-p6", end_K_p6 - 300, "K")


# ---------------------------------------------------------------
# Type 2: specific-heat-capacity
# ---------------------------------------------------------------

# w: kettle, 1.5 kg water from 20 C to 100 C, c = 4200
record("specific-heat-capacity-w", 1.5 * 4200 * (100 - 20), "J")

# p1: copper block 2.0 kg, c = 390, from 15 C to 25 C
record("specific-heat-capacity-p1", 2.0 * 390 * (25 - 15), "J")

# p2: bath, 80 kg water, c = 4200, rise of 30 K
record("specific-heat-capacity-p2", 80 * 4200 * 30, "J")

# p3: aluminium block 0.50 kg, 10 800 J, rise 24.0 K -> c
record("specific-heat-capacity-p3", 10800 / (0.50 * 24.0), "J kg⁻¹ K⁻¹")

# p4: 250 g water, 42 kJ supplied, c = 4200 -> temperature rise
mass_p4 = 250 / 1000
energy_p4 = 42 * 1000
record("specific-heat-capacity-p4", energy_p4 / (mass_p4 * 4200), "K")

# p5: 50 W heater for 4.0 min in 0.60 kg oil, c = 2100 -> rise (two steps)
energy_p5 = 50 * 4.0 * 60
record("specific-heat-capacity-p5", energy_p5 / (0.60 * 2100), "K")

# p6: 8.5 kW shower for 6.0 min, water 12 C -> 38 C, c = 4200 -> mass (two steps)
energy_p6 = 8500 * 6.0 * 60
record("specific-heat-capacity-p6", energy_p6 / (4200 * (38 - 12)), "kg")


# ---------------------------------------------------------------
# Type 3: specific-latent-heat
# ---------------------------------------------------------------

# w: melt 0.25 kg ice at 0 C, L = 334 000
record("specific-latent-heat-w", 0.25 * 334000, "J")

# p1: boil 0.050 kg water at 100 C, L = 2.26e6
record("specific-latent-heat-p1", 0.050 * 2.26e6, "J")

# p2: melt 3.5 kg lead, L = 23 000
record("specific-latent-heat-p2", 3.5 * 23000, "J")

# p3: 0.20 kg ethanol vaporised with 1.68e5 J -> L
record("specific-latent-heat-p3", 1.68e5 / 0.20, "J kg⁻¹")

# p4: 60 kJ melts ice at 0 C, L = 334 000 -> mass in grams
mass_kg_p4 = 60 * 1000 / 334000
record("specific-latent-heat-p4", mass_kg_p4 * 1000, "g")

# p5: 2.0 kW heater for 5.0 min boils water, L = 2.26e6 -> mass (two steps)
energy_lh_p5 = 2000 * 5.0 * 60
record("specific-latent-heat-p5", energy_lh_p5 / 2.26e6, "kg")

# p6: runner loses 350 W by evaporation for 1 hour, L = 2.4e6 -> mass (two steps)
energy_lh_p6 = 350 * 3600
record("specific-latent-heat-p6", energy_lh_p6 / 2.4e6, "kg")


# ---------------------------------------------------------------
# Type 4: heating-with-change-of-state
# ---------------------------------------------------------------

# w: 0.40 kg ice at -10 C -> water at 0 C; c_ice = 2100, L_f = 334 000
warm_w = 0.40 * 2100 * 10
melt_w = 0.40 * 334000
record("heating-with-change-of-state-w", warm_w + melt_w, "J")

# p1: 0.50 kg water at 80 C -> steam at 100 C; c = 4200, L_v = 2.26e6
warm_p1 = 0.50 * 4200 * (100 - 80)
boil_p1 = 0.50 * 2.26e6
record("heating-with-change-of-state-p1", warm_p1 + boil_p1, "J")

# p2: 2.0 kg solid lead at 327 C -> liquid at 400 C; L_f = 23 000, c_liquid = 140
melt_p2 = 2.0 * 23000
warm_p2 = 2.0 * 140 * (400 - 327)
record("heating-with-change-of-state-p2", melt_p2 + warm_p2, "J")

# p3: 30 g ice at 0 C -> water at 20 C; L_f = 334 000, c = 4200 (grams -> kg)
mass_p3 = 30 / 1000
melt_p3 = mass_p3 * 334000
warm_p3 = mass_p3 * 4200 * 20
record("heating-with-change-of-state-p3", melt_p3 + warm_p3, "J")

# p4: 1.5 kW heater; 0.20 kg ice at 0 C -> water at 50 C -> time
melt_p4 = 0.20 * 334000
warm_p4 = 0.20 * 4200 * 50
record("heating-with-change-of-state-p4", (melt_p4 + warm_p4) / 1500, "s")

# p5: 0.080 kg water at 25 C -> steam at 100 C; c = 4200, L_v = 2.26e6
warm_p5 = 0.080 * 4200 * (100 - 25)
boil_p5 = 0.080 * 2.26e6
record("heating-with-change-of-state-p5", warm_p5 + boil_p5, "J")

# p6: freezer removes 50 kJ; water at 15 C -> ice at 0 C -> mass
energy_per_kg_p6 = 4200 * 15 + 334000
record("heating-with-change-of-state-p6", 50000 / energy_per_kg_p6, "kg")


# ---------------------------------------------------------------
# Type 5: thermal-equilibrium
# ---------------------------------------------------------------

# w: 0.20 kg water at 80 C + 0.30 kg water at 20 C (same c cancels)
final_w = (0.20 * 80 + 0.30 * 20) / (0.20 + 0.30)
record("thermal-equilibrium-w", final_w, "°C")

# p1: bath 60 kg at 55 C + 40 kg at 15 C
final_p1 = (60 * 55 + 40 * 15) / (60 + 40)
record("thermal-equilibrium-p1", final_p1, "°C")

# p2: 0.50 kg copper (390) at 100 C into 1.0 kg water (4200) at 20 C
mc_copper_p2 = 0.50 * 390
mc_water_p2 = 1.0 * 4200
final_p2 = (mc_copper_p2 * 100 + mc_water_p2 * 20) / (mc_copper_p2 + mc_water_p2)
record("thermal-equilibrium-p2", final_p2, "°C")

# p3: 1.2 litres at 90 C + 0.80 litres at 10 C, density 1000 kg m^-3
mass_hot_p3 = 1.2
mass_cold_p3 = 0.80
final_p3 = (mass_hot_p3 * 90 + mass_cold_p3 * 10) / (mass_hot_p3 + mass_cold_p3)
record("thermal-equilibrium-p3", final_p3, "°C")

# p4: mass of water at 15 C to add to 0.50 kg at 95 C for final 40 C
heat_lost_p4 = 0.50 * (95 - 40)
record("thermal-equilibrium-p4", heat_lost_p4 / (40 - 15), "kg")

# p5: coffee 0.25 kg (4200) at 85 C + milk 0.050 kg (3900) at 5 C
mc_coffee_p5 = 0.25 * 4200
mc_milk_p5 = 0.050 * 3900
final_p5 = (mc_coffee_p5 * 85 + mc_milk_p5 * 5) / (mc_coffee_p5 + mc_milk_p5)
record("thermal-equilibrium-p5", final_p5, "°C")

# p6: horseshoe 1.2 kg (450) into 5.0 kg water (4200) at 15 C; final 32 C -> initial T
heat_gained_p6 = 5.0 * 4200 * (32 - 15)
drop_p6 = heat_gained_p6 / (1.2 * 450)
record("thermal-equilibrium-p6", 32 + drop_p6, "°C")


# ---------------------------------------------------------------
# Type 6: ideal-gas-moles
# ---------------------------------------------------------------

# w: 2.0 mol at 300 K in 0.050 m^3 -> p
record("ideal-gas-moles-w", 2.0 * R * 300 / 0.050, "Pa")

# p1: 0.50 mol at 1.0e5 Pa and 290 K -> V
record("ideal-gas-moles-p1", 0.50 * R * 290 / 1.0e5, "m³")

# p2: tyre 0.020 m^3 at 2.5e5 Pa and 295 K -> n
record("ideal-gas-moles-p2", 2.5e5 * 0.020 / (R * 295), "mol")

# p3: 1.5 mol in 36 litres at 120 kPa -> T
volume_p3 = 36 * 1e-3
pressure_p3 = 120 * 1e3
record("ideal-gas-moles-p3", pressure_p3 * volume_p3 / (1.5 * R), "K")

# p4: 0.040 mol in 500 cm^3 at 25 C -> p in kPa
volume_p4 = 500 * 1e-6
temp_p4 = 25 + ZERO_C_IN_K
pressure_p4 = 0.040 * R * temp_p4 / volume_p4
record("ideal-gas-moles-p4", pressure_p4 / 1e3, "kPa")

# p5: 0.25 mol helium at 20 C and 101 kPa -> V in litres (two steps)
temp_p5 = 20 + ZERO_C_IN_K
volume_p5 = 0.25 * R * temp_p5 / (101 * 1e3)
record("ideal-gas-moles-p5", volume_p5 * 1e3, "litres")

# p6: 0.80 mol at 1.2e5 Pa in 0.018 m^3 -> T in C (find K, then convert)
temp_K_p6 = 1.2e5 * 0.018 / (0.80 * R)
record("ideal-gas-moles-p6", temp_K_p6 - ZERO_C_IN_K, "°C")


# ---------------------------------------------------------------
# Type 7: ideal-gas-molecules
# ---------------------------------------------------------------

# w: 1.0e5 Pa, 0.025 m^3, 300 K -> N
record("ideal-gas-molecules-w", 1.0e5 * 0.025 / (k * 300), "")

# p1: 3.5 mol -> N
record("ideal-gas-molecules-p1", 3.5 * N_A, "")

# p2: 4.0e22 molecules in 1.5e-3 m^3 at 320 K -> p
record("ideal-gas-molecules-p2", 4.0e22 * k * 320 / 1.5e-3, "Pa")

# p3: 1.5e25 molecules -> n
record("ideal-gas-molecules-p3", 1.5e25 / N_A, "mol")

# p4: 250 cm^3 at 101 kPa and 20 C -> N
volume_m_p4 = 250 * 1e-6
pressure_m_p4 = 101 * 1e3
temp_m_p4 = 20 + ZERO_C_IN_K
record("ideal-gas-molecules-p4", pressure_m_p4 * volume_m_p4 / (k * temp_m_p4), "")

# p5: nitrogen 0.050 m^3 at 8.0e6 Pa and 290 K, molar mass 0.028 -> mass (two steps)
moles_p5 = 8.0e6 * 0.050 / (R * 290)
record("ideal-gas-molecules-p5", moles_p5 * 0.028, "kg")

# p6: 12 g CO2, molar mass 44 g mol^-1 -> N (two steps)
moles_p6 = 12 / 44
record("ideal-gas-molecules-p6", moles_p6 * N_A, "")


# ---------------------------------------------------------------
# Type 8: gas-two-states
# ---------------------------------------------------------------

# w: Boyle, 2.0e5 Pa at 0.030 m^3 -> 0.012 m^3, constant T
record("gas-two-states-w", 2.0e5 * 0.030 / 0.012, "Pa")

# p1: pressure law, 2.4e5 Pa at 280 K -> 310 K
record("gas-two-states-p1", 2.4e5 * 310 / 280, "Pa")

# p2: Charles, 3.0e-3 m^3 at 290 K -> 350 K
record("gas-two-states-p2", 3.0e-3 * 350 / 290, "m³")

# p3: sealed can, 1.0e5 Pa at 20 C -> 180 C
T1_p3 = 20 + ZERO_C_IN_K
T2_p3 = 180 + ZERO_C_IN_K
record("gas-two-states-p3", 1.0e5 * T2_p3 / T1_p3, "Pa")

# p4: 2.0 litres at 100 kPa, 300 K -> 250 kPa, 450 K; V2 in litres
record("gas-two-states-p4", 100 * 2.0 * 450 / (250 * 300), "litres")

# p5: bubble 0.50 cm^3 at 3.5e5 Pa, 277 K -> 1.0e5 Pa, 293 K; V2 in cm^3
record("gas-two-states-p5", 3.5e5 * 0.50 * 293 / (277 * 1.0e5), "cm³")

# p6: 27 C, 1.2e5 Pa, 0.040 m^3 -> 2.0e5 Pa, 0.030 m^3; T2 in C (two steps)
T1_p6 = 27 + ZERO_C_IN_K
T2_p6 = T1_p6 * 2.0e5 * 0.030 / (1.2e5 * 0.040)
record("gas-two-states-p6", T2_p6 - ZERO_C_IN_K, "°C")


# ---------------------------------------------------------------
# Type 9: kinetic-theory
# ---------------------------------------------------------------

# w: air at 1.0e5 Pa, density 1.2 -> c_rms
record("kinetic-theory-w", math.sqrt(3 * 1.0e5 / 1.2), "m s⁻¹")

# p1: helium at 1.0e5 Pa, density 0.166 -> c_rms
record("kinetic-theory-p1", math.sqrt(3 * 1.0e5 / 0.166), "m s⁻¹")

# p2: nitrogen molecule 4.65e-26 kg at 300 K -> c_rms
record("kinetic-theory-p2", math.sqrt(3 * k * 300 / 4.65e-26), "m s⁻¹")

# p3: hydrogen molecule 3.34e-27 kg, c_rms = 2000 -> T
record("kinetic-theory-p3", 3.34e-27 * 2000 ** 2 / (3 * k), "K")

# p4: oxygen density 1.43, c_rms = 460 -> p
record("kinetic-theory-p4", (1 / 3) * 1.43 * 460 ** 2, "Pa")

# p5: CO2 molar mass 0.044 at 350 K -> m then c_rms (two steps)
mass_molecule_p5 = 0.044 / N_A
record("kinetic-theory-p5", math.sqrt(3 * k * 350 / mass_molecule_p5), "m s⁻¹")

# p6: 5.0e23 molecules of 6.6e-26 kg in 0.020 m^3 at 1.2e5 Pa -> c_rms (two steps)
total_mass_p6 = 5.0e23 * 6.6e-26
mean_square_p6 = 3 * 1.2e5 * 0.020 / total_mass_p6
record("kinetic-theory-p6", math.sqrt(mean_square_p6), "m s⁻¹")


# ---------------------------------------------------------------
# Type 10: kinetic-energy-internal-energy
# ---------------------------------------------------------------

# w: mean KE at 300 K
record("kinetic-energy-internal-energy-w", 1.5 * k * 300, "J")

# p1: mean KE at 20 C
record("kinetic-energy-internal-energy-p1", 1.5 * k * (20 + ZERO_C_IN_K), "J")

# p2: U for 2.0 mol at 400 K
record("kinetic-energy-internal-energy-p2", 1.5 * 2.0 * R * 400, "J")

# p3: mean KE 1.0e-20 J -> T
record("kinetic-energy-internal-energy-p3", 2 * 1.0e-20 / (3 * k), "K")

# p4: U for 3.0e24 molecules at 27 C
record("kinetic-energy-internal-energy-p4", 1.5 * 3.0e24 * k * (27 + ZERO_C_IN_K), "J")

# p5: U from pV: 2.0e5 Pa, 0.015 m^3 (nRT = pV, then U = 1.5 pV)
nRT_p5 = 2.0e5 * 0.015
record("kinetic-energy-internal-energy-p5", 1.5 * nRT_p5, "J")

# p6: mean KE at 5800 K in eV (J first, then convert)
ke_joules_p6 = 1.5 * k * 5800
record("kinetic-energy-internal-energy-p6", ke_joules_p6 / eV, "eV")


# ---------------------------------------------------------------
# Print
# ---------------------------------------------------------------

for question_id, rounded, unit, raw in results:
    print(f"{question_id:38s} {rounded!r:>14}  {unit:14s} (raw {raw!r})")
