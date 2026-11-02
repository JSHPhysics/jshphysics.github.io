#!/usr/bin/env python3
"""Compute every answer in data/particle-model.json (Edexcel GCSE 1PH0).

Run:  python3 tools/calc_particle-model.py
Prints each question id with its answer rounded to 3 s.f., plus every
plotted coordinate used by the heating-graph type, so the JSON can be
filled from this output rather than from mental arithmetic.
"""

import json

# Standard values from SCHEMA.md
G = 10  # N/kg

# Values given in the question text (not on the standard list)
C_WATER = 4200       # J/kg °C
C_ALUMINIUM = 900    # J/kg °C
C_COPPER = 390       # J/kg °C
L_FUSION_ICE = 334000          # J/kg
L_VAPORISATION_WATER = 2260000  # J/kg
KELVIN_OFFSET = 273

answers = []
graphs = {}


def record(question_id, value, unit):
    """Store one answer: exact when it is a whole number, else 3 s.f."""
    if abs(value - round(value)) < 1e-9:
        # Exact whole-number answers are stored as integers (e.g. 4688000)
        stored = int(round(value))
    else:
        stored = float(f"{value:.3g}")
    answers.append((question_id, stored, unit))


# ---------------------------------------------------------------- density
# ρ = m / V

# w: 540 g aluminium block, 200 cm³ → g/cm³
record("density-w", 540 / 200, "g/cm³")

# p1: pebble 150 g, 60 cm³ → g/cm³
record("density-p1", 150 / 60, "g/cm³")

# p2: 3 m³ of concrete has mass 7200 kg → kg/m³
record("density-p2", 7200 / 3, "kg/m³")

# p3: olive oil 0.92 g/cm³, 500 cm³ bottle → mass in g
record("density-p3", 0.92 * 500, "g")

# p4: air density 1.2 kg/m³, mass of air in a room 60 kg → volume in m³
record("density-p4", 60 / 1.2, "m³")

# p5: brick 20 cm × 10 cm × 6 cm, mass 2.16 kg → g/cm³ (two-step: volume, g)
brick_volume_cm3 = 20 * 10 * 6
brick_mass_g = 2.16 * 1000
record("density-p5", brick_mass_g / brick_volume_cm3, "g/cm³")

# p6: steel bolt 25 cm³, mass 0.195 kg → kg/m³ (two-step: cm³ → m³)
bolt_volume_m3 = 25 / 1000000
record("density-p6", 0.195 / bolt_volume_m3, "kg/m³")


# ------------------------------------------------- specific heat capacity
# ΔQ = m × c × Δθ

# w: 2 kg water 20 → 70 °C
record("shc-w", 2 * C_WATER * (70 - 20), "J")

# p1: 1.5 kg aluminium pan 15 → 115 °C
record("shc-p1", 1.5 * C_ALUMINIUM * (115 - 15), "J")

# p2: 0.5 kg copper block, rise of 40 °C
record("shc-p2", 0.5 * C_COPPER * 40, "J")

# p3: 2 kg iron weight, 50 000 J, rise 50 °C → c
record("shc-p3", 50000 / (2 * 50), "J/kg °C")

# p4: 250 g water in a mug, 42 000 J → temperature rise
mug_mass_kg = 250 / 1000
record("shc-p4", 42000 / (mug_mass_kg * C_WATER), "°C")

# p5: 2 kW kettle for 105 s heats 1 kg water → temperature rise (two-step)
kettle_energy = 2000 * 105
record("shc-p5", kettle_energy / (1 * C_WATER), "°C")

# p6: 3 kW immersion heater, 60 kg water 15 → 55 °C → time in s (two-step)
tank_energy = 60 * C_WATER * (55 - 15)
record("shc-p6", tank_energy / 3000, "s")


# ------------------------------------------------- specific latent heat
# Q = m × L

# w: melt 0.5 kg of ice
record("latent-w", 0.5 * L_FUSION_ICE, "J")

# p1: boil away 2 kg of water
record("latent-p1", 2 * L_VAPORISATION_WATER, "J")

# p2: freeze 1.5 kg of water (energy removed)
record("latent-p2", 1.5 * L_FUSION_ICE, "J")

# p3: 1 130 000 J boils what mass of water
record("latent-p3", 1130000 / L_VAPORISATION_WATER, "kg")

# p4: 300 g of candle wax needs 52 500 J to melt → L
wax_mass_kg = 300 / 1000
record("latent-p4", 52500 / wax_mass_kg, "J/kg")

# p5: 1.5 kW kettle boiling for 4 minutes → mass boiled away (two-step)
boil_energy = 1500 * (4 * 60)
record("latent-p5", boil_energy / L_VAPORISATION_WATER, "kg")

# p6: 400 W heater melts 2 kg of ice → time in s (two-step)
melt_energy = 2 * L_FUSION_ICE
record("latent-p6", melt_energy / 400, "s")


# ----------------------------------------- heating with a change of state

# w: 0.5 kg ice at 0 °C melted then warmed to 20 °C
w_melt = 0.5 * L_FUSION_ICE
w_warm = 0.5 * C_WATER * 20
record("change-of-state-w", w_melt + w_warm, "J")

# p1: 2 kg water 80 → 100 °C then boiled away
p1_warm = 2 * C_WATER * (100 - 80)
p1_boil = 2 * L_VAPORISATION_WATER
record("change-of-state-p1", p1_warm + p1_boil, "J")

# p2: 0.2 kg ice at 0 °C melted then warmed to 40 °C
p2_melt = 0.2 * L_FUSION_ICE
p2_warm = 0.2 * C_WATER * 40
record("change-of-state-p2", p2_melt + p2_warm, "J")

# p3: 500 g water at 60 °C heated to 100 °C and boiled away
p3_mass_kg = 500 / 1000
p3_warm = p3_mass_kg * C_WATER * (100 - 60)
p3_boil = p3_mass_kg * L_VAPORISATION_WATER
record("change-of-state-p3", p3_warm + p3_boil, "J")

# p4: 0.4 kg water at 30 °C cooled to 0 °C then frozen → energy removed in kJ
p4_cool = 0.4 * C_WATER * 30
p4_freeze = 0.4 * L_FUSION_ICE
record("change-of-state-p4", (p4_cool + p4_freeze) / 1000, "kJ")

# p5 (Higher): 2 kW heater, 1 kg ice at 0 °C melted and warmed to 30 °C → time
p5_melt = 1 * L_FUSION_ICE
p5_warm = 1 * C_WATER * 30
record("change-of-state-p5", (p5_melt + p5_warm) / 2000, "s")

# p6 (Higher): 1.5 kg water 60 → 100 °C and boiled away in 25 minutes → power
p6_warm = 1.5 * C_WATER * (100 - 60)
p6_boil = 1.5 * L_VAPORISATION_WATER
p6_time = 25 * 60
record("change-of-state-p6", (p6_warm + p6_boil) / p6_time, "W")


# ----------------------------------------------------- temperature scales
# K = °C + 273

# w: 25 °C → K
record("temperature-w", 25 + KELVIN_OFFSET, "K")

# p1: boiling water 100 °C → K
record("temperature-p1", 100 + KELVIN_OFFSET, "K")

# p2: absolute zero 0 K → °C
record("temperature-p2", 0 - KELVIN_OFFSET, "°C")

# p3: −40 °C → K
record("temperature-p3", -40 + KELVIN_OFFSET, "K")

# p4: gas warmed from 20 °C to 80 °C → change in kelvin
record("temperature-p4", 80 - 20, "K")

# p5: gas at 27 °C, kelvin temperature doubled → new temperature in °C (two-step)
p5_kelvin = 27 + KELVIN_OFFSET
p5_doubled = 2 * p5_kelvin
record("temperature-p5", p5_doubled - KELVIN_OFFSET, "°C")

# p6: room 22 °C, freezer 255 K → difference in °C (two-step)
freezer_celsius = 255 - KELVIN_OFFSET
record("temperature-p6", 22 - freezer_celsius, "°C")


# ---------------------------------------------- gas pressure and volume
# P₁ × V₁ = P₂ × V₂

# w: 100 kPa, 600 cm³ → 200 cm³
record("boyle-w", 100 * 600 / 200, "kPa")

# p1: syringe 100 kPa, 50 cm³ → 20 cm³
record("boyle-p1", 100 * 50 / 20, "kPa")

# p2: bubble 300 kPa, 2 cm³ → 100 kPa at surface
record("boyle-p2", 300 * 2 / 100, "cm³")

# p3: balloon 1.5 litres at 100 kPa squeezed to 120 kPa → cm³
balloon_cm3 = 1.5 * 1000
record("boyle-p3", 100 * balloon_cm3 / 120, "cm³")

# p4: cylinder 12 litres fills 2400 litres at 100 kPa → original pressure
record("boyle-p4", 100 * 2400 / 12, "kPa")

# p5: 100 kPa, 240 cm³ → 160 kPa → decrease in volume (two-step)
p5_v2 = 100 * 240 / 160
record("boyle-p5", 240 - p5_v2, "cm³")

# p6: piston, area 20 cm², length 15 cm → 5 cm, 100 kPa → P₂ (two-step)
piston_v1 = 20 * 15
piston_v2 = 20 * 5
record("boyle-p6", 100 * piston_v1 / piston_v2, "kPa")


# ---------------------------------------------- reading heating graphs
# All points chosen on major gridline intersections.

# w: wax, melting point read off the flat section
w_points = [[0, 20], [4, 60], [8, 60], [12, 100]]
graphs["heating-graph-w"] = w_points
record("heating-graph-w", w_points[1][1], "°C")

# p1: a liquid, boiling point read off
p1_points = [[0, 20], [3, 80], [10, 80]]
graphs["heating-graph-p1"] = p1_points
record("heating-graph-p1", p1_points[1][1], "°C")

# p2: ice, time spent melting = length of the flat section (s)
p2_points = [[0, -10], [60, 0], [540, 0], [600, 5]]
graphs["heating-graph-p2"] = p2_points
record("heating-graph-p2", p2_points[2][0] - p2_points[1][0], "s")

# p3: water in a kettle, temperature rise in the first 2 minutes
p3_points = [[0, 20], [4, 100], [8, 100]]
graphs["heating-graph-p3"] = p3_points
p3_gradient = (p3_points[1][1] - p3_points[0][1]) / (p3_points[1][0] - p3_points[0][0])
p3_at_two = p3_points[0][1] + p3_gradient * 2
record("heating-graph-p3", p3_at_two - p3_points[0][1], "°C")

# p4: solid, 30 W heater; melting time in minutes → energy to melt (two-step)
p4_points = [[0, 20], [2, 50], [7, 50], [10, 80]]
graphs["heating-graph-p4"] = p4_points
p4_melt_minutes = p4_points[2][0] - p4_points[1][0]
p4_melt_seconds = p4_melt_minutes * 60
p4_power = 30
record("heating-graph-p4", p4_power * p4_melt_seconds, "J")

# p5 (Higher): 0.4 kg solid, 40 W heater; c from the gradient of the first section
p5_points = [[0, 10], [200, 50], [500, 50], [600, 60]]
graphs["heating-graph-p5"] = p5_points
p5_gradient = (p5_points[1][1] - p5_points[0][1]) / (p5_points[1][0] - p5_points[0][0])
p5_power = 40
p5_mass = 0.4
record("heating-graph-p5", p5_power / (p5_mass * p5_gradient), "J/kg °C")

# p6: 0.2 kg solid, 40 W heater; melting time → energy → L (two-step)
p6_points = [[0, 20], [100, 50], [500, 50], [800, 80]]
graphs["heating-graph-p6"] = p6_points
p6_melt_seconds = p6_points[2][0] - p6_points[1][0]
p6_power = 40
p6_mass = 0.2
p6_energy = p6_power * p6_melt_seconds
record("heating-graph-p6", p6_energy / p6_mass, "J/kg")


# ------------------------------------------------------------------ output
for question_id, value, unit in answers:
    print(f"{question_id:24s} {value!r:>12}  {unit}")

print()
print("Graph points:")
for question_id, points in graphs.items():
    print(f"{question_id:24s} {json.dumps(points)}")
