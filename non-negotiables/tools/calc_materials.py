#!/usr/bin/env python3
"""Compute every answer in data/materials.json.

Each answer is printed rounded to 3 s.f. with its question id.
Run: python3 tools/calc_materials.py
"""

import math

# Standard constants from SCHEMA.md
g = 9.81          # m s^-2

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


def circle_area_from_diameter(diameter):
    """Cross-sectional area of a wire from its diameter."""
    area = math.pi * diameter ** 2 / 4
    return area


def sphere_volume(radius):
    """Volume of a sphere."""
    volume = 4 / 3 * math.pi * radius ** 3
    return volume


def cylinder_volume(radius, length):
    """Volume of a cylinder."""
    volume = math.pi * radius ** 2 * length
    return volume


# ---------------------------------------------------------------
# Type 1: density
# ---------------------------------------------------------------

# w: aluminium block 0.120 x 0.080 x 0.050 m, mass 1.30 kg
volume_dw = 0.120 * 0.080 * 0.050
record("density-w", 1.30 / volume_dw, "kg m⁻³")

# p1: 500 ml olive oil (5.00e-4 m^3), mass 0.460 kg
record("density-p1", 0.460 / 5.00e-4, "kg m⁻³")

# p2: gold bar mass 12.4 kg, volume 6.42e-4 m^3
record("density-p2", 12.4 / 6.42e-4, "kg m⁻³")

# p3: steel ball bearing radius 6.0 mm, density 7800 -> mass in grams
radius_p3 = 6.0e-3
volume_p3 = sphere_volume(radius_p3)
mass_p3_kg = 7800 * volume_p3
record("density-p3", mass_p3_kg * 1000, "g")

# p4: copper cylinder radius 1.5 cm, length 8.0 cm, density 8.96 g cm^-3 -> mass in kg
volume_p4_cm3 = cylinder_volume(1.5, 8.0)
mass_p4_g = 8.96 * volume_p4_cm3
record("density-p4", mass_p4_g / 1000, "kg")

# p5: copper wire mass 0.0250 kg, density 8960, area 0.50 mm^2 -> length
volume_p5 = 0.0250 / 8960
area_p5 = 0.50e-6
record("density-p5", volume_p5 / area_p5, "m")

# p6: Mars mass 6.42e23 kg, radius 3.39e6 m -> mean density
volume_p6 = sphere_volume(3.39e6)
record("density-p6", 6.42e23 / volume_p6, "kg m⁻³")


# ---------------------------------------------------------------
# Type 2: hookes-law
# ---------------------------------------------------------------

# w: spring extends 0.060 m under 1.5 N -> k
record("hookes-law-w", 1.5 / 0.060, "N m⁻¹")

# p1: force meter spring k = 120 N/m, extension 0.050 m -> F
record("hookes-law-p1", 120 * 0.050, "N")

# p2: trampoline spring k = 3500 N/m, extension 0.020 m -> F
record("hookes-law-p2", 3500 * 0.020, "N")

# p3: extension 45 mm under 9.0 N -> k
record("hookes-law-p3", 9.0 / 45e-3, "N m⁻¹")

# p4: mattress spring k = 2.4 kN/m, force 36 N -> extension in mm
extension_p4_m = 36 / 2400
record("hookes-law-p4", extension_p4_m * 1000, "mm")

# p5: 0.350 kg mass on spring k = 70 N/m -> extension
weight_p5 = 0.350 * g
record("hookes-law-p5", weight_p5 / 70, "m")

# p6: natural length 0.250 m stretched to 0.410 m by 48 N -> k
extension_p6 = 0.410 - 0.250
record("hookes-law-p6", 48 / extension_p6, "N m⁻¹")


# ---------------------------------------------------------------
# Type 3: springs-combined
# ---------------------------------------------------------------

# w: two identical springs k = 30 N/m in parallel, load 4.5 N -> extension
k_sw = 30 + 30
record("springs-combined-w", 4.5 / k_sw, "m")

# p1: 200 and 300 N/m in parallel -> combined k
record("springs-combined-p1", 200 + 300, "N m⁻¹")

# p2: 40 and 60 N/m in series -> combined k
record("springs-combined-p2", 1 / (1 / 40 + 1 / 60), "N m⁻¹")

# p3: two identical 80 N/m springs in series, force 2.0 N -> extension in mm
k_sp3 = 1 / (1 / 80 + 1 / 80)
extension_sp3_m = 2.0 / k_sp3
record("springs-combined-p3", extension_sp3_m * 1000, "mm")

# p4: series combination 12 N/m, one spring 20 N/m -> the other
record("springs-combined-p4", 1 / (1 / 12 - 1 / 20), "N m⁻¹")

# p5: three identical 45 N/m springs in parallel supporting 0.60 kg -> extension
k_sp5 = 3 * 45
weight_sp5 = 0.60 * g
record("springs-combined-p5", weight_sp5 / k_sp5, "m")

# p6: series 120 and 180 N/m, total extension 0.090 m -> force
k_sp6 = 1 / (1 / 120 + 1 / 180)
record("springs-combined-p6", k_sp6 * 0.090, "N")


# ---------------------------------------------------------------
# Type 4: young-modulus
# ---------------------------------------------------------------

# w: steel wire L = 2.00 m, d = 0.50 mm, F = 60 N, ext = 3.0 mm -> E
area_yw = circle_area_from_diameter(0.50e-3)
stress_yw = 60 / area_yw
strain_yw = 3.0e-3 / 2.00
record("young-modulus-w", stress_yw / strain_yw, "Pa")

# p1: F = 250 N on area 1.25e-6 m^2 -> stress
record("young-modulus-p1", 250 / 1.25e-6, "Pa")

# p2: stress 1.2e8 Pa, strain 8.0e-4 -> E
record("young-modulus-p2", 1.2e8 / 8.0e-4, "Pa")

# p3: wire 3.50 m extends 2.1 mm -> strain
record("young-modulus-p3", 2.1e-3 / 3.50, "")

# p4: F = 180 N, diameter 0.80 mm -> stress
area_yp4 = circle_area_from_diameter(0.80e-3)
record("young-modulus-p4", 180 / area_yp4, "Pa")

# p5: copper wire L = 1.80 m, d = 0.60 mm, F = 40 N, ext = 2.1 mm -> E
area_yp5 = circle_area_from_diameter(0.60e-3)
stress_yp5 = 40 / area_yp5
strain_yp5 = 2.1e-3 / 1.80
record("young-modulus-p5", stress_yp5 / strain_yp5, "Pa")

# p6: nylon line E = 3.0e9, d = 0.40 mm, L = 1.5 m, ext = 12 mm -> force
strain_yp6 = 12e-3 / 1.5
stress_yp6 = 3.0e9 * strain_yp6
area_yp6 = circle_area_from_diameter(0.40e-3)
record("young-modulus-p6", stress_yp6 * area_yp6, "N")


# ---------------------------------------------------------------
# Type 5: wire-extension
# ---------------------------------------------------------------

# w: steel wire E = 2.0e11, L = 1.50 m, d = 0.40 mm, F = 25 N -> extension in mm
area_ww = circle_area_from_diameter(0.40e-3)
extension_ww = 25 * 1.50 / (area_ww * 2.0e11)
record("wire-extension-w", extension_ww * 1000, "mm")

# p1: copper wire A = 5.0e-7, L = 2.5 m, F = 20 N, E = 1.2e11 -> extension in m
record("wire-extension-p1", 20 * 2.5 / (5.0e-7 * 1.2e11), "m")

# p2: lift cable A = 3.0e-4, L = 40 m, F = 9000 N, E = 2.0e11 -> extension in m
record("wire-extension-p2", 9000 * 40 / (3.0e-4 * 2.0e11), "m")

# p3: brass wire d = 0.90 mm, L = 2.2 m, F = 36 N, E = 1.0e11 -> extension in mm
area_wp3 = circle_area_from_diameter(0.90e-3)
extension_wp3 = 36 * 2.2 / (area_wp3 * 1.0e11)
record("wire-extension-p3", extension_wp3 * 1000, "mm")

# p4: tendon E = 1.5e9, A = 60 mm^2, L = 0.20 m, F = 900 N -> extension in mm
area_wp4 = 60e-6
extension_wp4 = 900 * 0.20 / (area_wp4 * 1.5e9)
record("wire-extension-p4", extension_wp4 * 1000, "mm")

# p5: 12 kg mass on nylon rope E = 3.0e9, d = 6.0 mm, L = 10 m -> extension in mm
weight_wp5 = 12 * g
area_wp5 = circle_area_from_diameter(6.0e-3)
extension_wp5 = weight_wp5 * 10 / (area_wp5 * 3.0e9)
record("wire-extension-p5", extension_wp5 * 1000, "mm")

# p6: steel string d = 0.25 mm, E = 2.0e11, F = 70 N, extension 2.0 mm -> length
area_wp6 = circle_area_from_diameter(0.25e-3)
length_wp6 = 2.0e-3 * area_wp6 * 2.0e11 / 70
record("wire-extension-p6", length_wp6, "m")


# ---------------------------------------------------------------
# Type 6: elastic-energy
# ---------------------------------------------------------------

# w: k = 250 N/m compressed 0.060 m -> energy
record("elastic-energy-w", 0.5 * 250 * 0.060 ** 2, "J")

# p1: straight line to 12 N at 0.30 m -> energy
record("elastic-energy-p1", 0.5 * 12 * 0.30, "J")

# p2: k = 800 N/m, extension 0.050 m -> energy
record("elastic-energy-p2", 0.5 * 800 * 0.050 ** 2, "J")

# p3: wire, 80 N gives 1.6 mm (linear) -> energy
record("elastic-energy-p3", 0.5 * 80 * 1.6e-3, "J")

# p4: catapult stores 2.4 J at 0.20 m -> k
record("elastic-energy-p4", 2 * 2.4 / 0.20 ** 2, "N m⁻¹")

# p5: k = 60 N/m with 0.50 kg hung -> energy stored
weight_ep5 = 0.50 * g
extension_ep5 = weight_ep5 / 60
record("elastic-energy-p5", 0.5 * weight_ep5 * extension_ep5, "J")

# p6: k = 400 N/m compressed by 32 N -> energy stored
compression_ep6 = 32 / 400
record("elastic-energy-p6", 0.5 * 32 * compression_ep6, "J")


# ---------------------------------------------------------------
# Type 7: pressure
# ---------------------------------------------------------------

# w: diver at 25 m in seawater 1030, atmospheric 1.01e5 -> total pressure
water_pw = 25 * 1030 * g
record("pressure-w", 1.01e5 + water_pw, "Pa")

# p1: hydraulic press force 4500 N on area 0.015 m^2 -> pressure
record("pressure-p1", 4500 / 0.015, "Pa")

# p2: swimming pool depth 1.8 m, water 1000 -> pressure due to water
record("pressure-p2", 1.8 * 1000 * g, "Pa")

# p3: stiletto heel area 1.2 cm^2, force 300 N -> pressure
record("pressure-p3", 300 / 1.2e-4, "Pa")

# p4: water pressure 2.0e5 Pa -> depth
record("pressure-p4", 2.0e5 / (1000 * g), "m")

# p5: oil tank depth 3.2 m, oil 850, atmospheric 1.01e5 -> total pressure
oil_pp5 = 3.2 * 850 * g
record("pressure-p5", 1.01e5 + oil_pp5, "Pa")

# p6: submarine hatch area 0.80 m^2 at depth 60 m in seawater 1030 -> force due to water
pressure_pp6 = 60 * 1030 * g
record("pressure-p6", pressure_pp6 * 0.80, "N")


# ---------------------------------------------------------------
# Type 8: upthrust
# ---------------------------------------------------------------

# w: steel block volume 2.0e-3 m^3 in water 1000 -> upthrust
record("upthrust-w", 1000 * 2.0e-3 * g, "N")

# p1: air tank volume 0.012 m^3 in seawater 1030 -> upthrust
record("upthrust-p1", 1030 * 0.012 * g, "N")

# p2: helium balloon 0.50 m^3 in air 1.2 -> upthrust
record("upthrust-p2", 1.2 * 0.50 * g, "N")

# p3: stone 250 cm^3 in water -> upthrust
record("upthrust-p3", 1000 * 250e-6 * g, "N")

# p4: boat weight 5000 N floating in water -> volume displaced
record("upthrust-p4", 5000 / (1000 * g), "m³")

# p5: aluminium block mass 0.540 kg, density 2700, in water -> apparent weight
weight_up5 = 0.540 * g
volume_up5 = 0.540 / 2700
upthrust_up5 = 1000 * volume_up5 * g
record("upthrust-p5", weight_up5 - upthrust_up5, "N")

# p6: wooden cylinder mass 1.6 kg, cross-section 0.020 m^2 floating in water -> depth submerged
weight_up6 = 1.6 * g
volume_up6 = weight_up6 / (1000 * g)
record("upthrust-p6", volume_up6 / 0.020, "m")


# ---------------------------------------------------------------
# Type 9: stokes-terminal
# ---------------------------------------------------------------

# w: steel ball r = 1.0 mm, 7800, in glycerol 1260, eta 1.4 -> terminal velocity
radius_sw = 1.0e-3
volume_sw = sphere_volume(radius_sw)
weight_sw = 7800 * volume_sw * g
upthrust_sw = 1260 * volume_sw * g
drag_sw = weight_sw - upthrust_sw
record("stokes-terminal-w", drag_sw / (6 * math.pi * 1.4 * radius_sw), "m s⁻¹")

# p1: sphere r = 2.0 mm, v = 0.050 m/s, eta 0.85 -> drag
record("stokes-terminal-p1", 6 * math.pi * 0.85 * 2.0e-3 * 0.050, "N")

# p2: raindrop r = 0.50 mm at 4.0 m/s in air eta 1.8e-5 -> drag
record("stokes-terminal-p2", 6 * math.pi * 1.8e-5 * 0.50e-3 * 4.0, "N")

# p3: ball r = 1.5 mm at 0.020 m/s, drag 1.2e-3 N -> viscosity
record("stokes-terminal-p3", 1.2e-3 / (6 * math.pi * 1.5e-3 * 0.020), "Pa s")

# p4: sphere diameter 3.0 mm, drag 4.5e-4 N, eta 0.30 -> speed
radius_sp4 = 3.0e-3 / 2
record("stokes-terminal-p4", 4.5e-4 / (6 * math.pi * 0.30 * radius_sp4), "m s⁻¹")

# p5: fog droplet r = 10 um, 1000, air eta 1.8e-5, ignore upthrust -> terminal velocity
radius_sp5 = 10e-6
weight_sp5 = 1000 * sphere_volume(radius_sp5) * g
record("stokes-terminal-p5", weight_sp5 / (6 * math.pi * 1.8e-5 * radius_sp5), "m s⁻¹")

# p6: glass bead r = 0.80 mm, 2500, in oil 900, eta 0.25 -> terminal velocity
radius_sp6 = 0.80e-3
volume_sp6 = sphere_volume(radius_sp6)
weight_sp6 = 2500 * volume_sp6 * g
upthrust_sp6 = 900 * volume_sp6 * g
drag_sp6 = weight_sp6 - upthrust_sp6
record("stokes-terminal-p6", drag_sp6 / (6 * math.pi * 0.25 * radius_sp6), "m s⁻¹")


# ---------------------------------------------------------------
# Print
# ---------------------------------------------------------------

for question_id, rounded, unit, raw in results:
    print(f"{question_id:28s} {rounded!r:>14}  {unit:14s} (raw {raw!r})")
