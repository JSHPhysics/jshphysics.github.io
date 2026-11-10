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


def stokes_drag(viscosity, radius, speed):
    """Viscous drag on a sphere from Stokes' law, F = 6πηrv."""
    drag = 6 * math.pi * viscosity * radius * speed
    return drag


def terminal_speed(radius, density_difference, viscosity):
    """Terminal speed of a sphere from the force balance.

    Sinking:  W = U + D  ->  (ρ_s − ρ_f)(4/3)πr³g = 6πηrv
    Rising:   W + D = U  ->  (ρ_f − ρ_s)(4/3)πr³g = 6πηrv
    Either way v = 2 r² g Δρ / (9η), with Δρ the positive difference.
    """
    speed = 2 * radius ** 2 * g * density_difference / (9 * viscosity)
    return speed


# ---------------------------------------------------------------
# Type 9: stokes-drag
# ---------------------------------------------------------------

# w: ball bearing diameter 5.0 mm at 0.030 m/s in glycerol eta 1.4 -> drag
radius_sdw = 5.0e-3 / 2
record("stokes-drag-w", stokes_drag(1.4, radius_sdw, 0.030), "N")

# p1: sphere r = 2.0 mm, v = 0.050 m/s, engine oil eta 0.85 -> drag
record("stokes-drag-p1", stokes_drag(0.85, 2.0e-3, 0.050), "N")

# p2: pollen grain r = 20 um at 0.050 m/s in air eta 1.8e-5 (laminar) -> drag
radius_sdp2 = 20e-6
record("stokes-drag-p2", stokes_drag(1.8e-5, radius_sdp2, 0.050), "N")

# p3: ball r = 1.5 mm at 0.020 m/s in honey, drag 1.2e-3 N -> viscosity
record("stokes-drag-p3", 1.2e-3 / (6 * math.pi * 1.5e-3 * 0.020), "Pa s")

# p4: sphere diameter 3.0 mm, drag 4.5e-4 N, syrup eta 0.30 -> speed
radius_sdp4 = 3.0e-3 / 2
record("stokes-drag-p4", 4.5e-4 / (6 * math.pi * 0.30 * radius_sdp4), "m s⁻¹")

# p5: sphere in engine oil eta 0.60 at 0.080 m/s, drag 3.6e-3 N -> radius in mm
radius_sdp5_m = 3.6e-3 / (6 * math.pi * 0.60 * 0.080)
record("stokes-drag-p5", radius_sdp5_m * 1000, "mm")

# p6: sphere diameter 1.20 cm in honey eta 8.0, drag 0.12 N -> speed in mm/s
radius_sdp6 = 1.20e-2 / 2
speed_sdp6_m = 0.12 / (6 * math.pi * 8.0 * radius_sdp6)
record("stokes-drag-p6", speed_sdp6_m * 1000, "mm s⁻¹")


# ---------------------------------------------------------------
# Type 10: terminal-sinking  (W = U + D)
# ---------------------------------------------------------------

# w: steel ball r = 1.0 mm, 7800, in glycerol 1260, eta 1.4 -> terminal velocity
radius_tsw = 1.0e-3
record("terminal-sinking-w", terminal_speed(radius_tsw, 7800 - 1260, 1.4), "m s⁻¹")

# p1: brass sphere V = 2.0e-7 m^3, 8500, at terminal velocity in water 1000 -> drag = W - U
weight_tsp1 = 8500 * 2.0e-7 * g
upthrust_tsp1 = 1000 * 2.0e-7 * g
record("terminal-sinking-p1", weight_tsp1 - upthrust_tsp1, "N")

# p2: glass bead r = 0.60 mm, 2500, in oil 920, eta 0.30 -> terminal velocity
radius_tsp2 = 0.60e-3
record("terminal-sinking-p2", terminal_speed(radius_tsp2, 2500 - 920, 0.30), "m s⁻¹")

# p3: falling-ball viscometer: steel ball r = 1.0 mm, 7800, oil 880, v = 0.060 m/s -> eta
radius_tsp3 = 1.0e-3
viscosity_tsp3 = 2 * radius_tsp3 ** 2 * g * (7800 - 880) / (9 * 0.060)
record("terminal-sinking-p3", viscosity_tsp3, "Pa s")

# p4: steel sphere r = 2.0 mm, 7800, in syrup eta 1.5, v = 0.0375 m/s -> fluid density
radius_tsp4 = 2.0e-3
density_difference_tsp4 = 9 * 1.5 * 0.0375 / (2 * radius_tsp4 ** 2 * g)
record("terminal-sinking-p4", 7800 - density_difference_tsp4, "kg m⁻³")

# p5: lead shot 11300 in glycerol 1260, eta 1.4, v = 0.050 m/s -> radius in mm
radius_tsp5_squared = 9 * 1.4 * 0.050 / (2 * g * (11300 - 1260))
radius_tsp5_m = math.sqrt(radius_tsp5_squared)
record("terminal-sinking-p5", radius_tsp5_m * 1000, "mm")

# p6: fog droplet r = 8.0 um, 1000, in air eta 1.8e-5, upthrust ignored (W = D) -> terminal velocity
radius_tsp6 = 8.0e-6
record("terminal-sinking-p6", terminal_speed(radius_tsp6, 1000, 1.8e-5), "m s⁻¹")


# ---------------------------------------------------------------
# Type 11: terminal-rising  (W + D = U)
# ---------------------------------------------------------------

# w: air bubble r = 2.0 mm, air 1.2, in glycerol 1260, eta 1.4 -> terminal velocity
radius_trw = 2.0e-3
record("terminal-rising-w", terminal_speed(radius_trw, 1260 - 1.2, 1.4), "m s⁻¹")

# p1: table-tennis ball rising at terminal velocity, U = 0.330 N, W = 0.026 N -> drag = U - W
record("terminal-rising-p1", 0.330 - 0.026, "N")

# p2: polystyrene bead r = 50 um, 50, rising in water 1000, eta 1.0e-3 -> terminal velocity
radius_trp2 = 50e-6
record("terminal-rising-p2", terminal_speed(radius_trp2, 1000 - 50, 1.0e-3), "m s⁻¹")

# p3: oil droplet r = 0.10 mm, 900, rising in water 1000, eta 1.0e-3 -> terminal velocity
radius_trp3 = 0.10e-3
record("terminal-rising-p3", terminal_speed(radius_trp3, 1000 - 900, 1.0e-3), "m s⁻¹")

# p4: bubble r = 1.5 mm rises at 2.0 mm/s in syrup 1400, weight negligible (D = U) -> eta
radius_trp4 = 1.5e-3
speed_trp4 = 2.0e-3
viscosity_trp4 = 2 * radius_trp4 ** 2 * g * 1400 / (9 * speed_trp4)
record("terminal-rising-p4", viscosity_trp4, "Pa s")

# p5: wooden bead r = 1.0 mm rises at 0.0030 m/s in oil 900, eta 0.40 -> bead density
radius_trp5 = 1.0e-3
density_difference_trp5 = 9 * 0.40 * 0.0030 / (2 * radius_trp5 ** 2 * g)
record("terminal-rising-p5", 900 - density_difference_trp5, "kg m⁻³")

# p6: air bubble rises at 5.0 mm/s in water 1000, eta 1.0e-3, weight negligible -> radius in um
speed_trp6 = 5.0e-3
radius_trp6_squared = 9 * 1.0e-3 * speed_trp6 / (2 * g * 1000)
radius_trp6_m = math.sqrt(radius_trp6_squared)
record("terminal-rising-p6", radius_trp6_m * 1e6, "μm")


# ---------------------------------------------------------------
# Print
# ---------------------------------------------------------------

for question_id, rounded, unit, raw in results:
    print(f"{question_id:28s} {rounded!r:>14}  {unit:14s} (raw {raw!r})")
