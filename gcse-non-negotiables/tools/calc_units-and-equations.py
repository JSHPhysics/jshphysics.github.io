#!/usr/bin/env python3
"""Compute every answer in data/units-and-equations.json.

Run:  python3 tools/calc_units-and-equations.py
Each line printed is  <question id>  <answer rounded to 3 s.f.>  <unit>
The values in the JSON file are copied from this output.
"""

import math

# Standard values from SCHEMA.md
G = 10  # N/kg


def sig3(value):
    """Round a number to three significant figures (exact values stay exact)."""
    if value == 0:
        return 0
    # Number of digits before the decimal point
    magnitude = math.floor(math.log10(abs(value)))
    # Decimal places needed for 3 s.f.
    places = 2 - magnitude
    rounded = round(value, places)
    # Report an integer where the rounded value is whole
    if rounded == int(rounded):
        return int(rounded)
    return rounded


def show(question_id, value, unit):
    """Print one answer line."""
    print(f"{question_id:22s} {sig3(value)!s:>14s}  {unit}")


# ---------------------------------------------------------------
# Type 1: si-conversions
# ---------------------------------------------------------------
print("# si-conversions")

# w: bolt 35 mm → m
bolt_mm = 35
show("si-conversions-w", bolt_mm / 1000, "m")

# p1: desk 120 cm → m
desk_cm = 120
show("si-conversions-p1", desk_cm / 100, "m")

# p2: rice 750 g → kg
rice_g = 750
show("si-conversions-p2", rice_g / 1000, "kg")

# p3: lorry load 3.2 tonnes → kg
load_tonnes = 3.2
show("si-conversions-p3", load_tonnes * 1000, "kg")

# p4: film 2.5 hours → s (hours → minutes → seconds)
film_hours = 2.5
film_minutes = film_hours * 60
film_seconds = film_minutes * 60
show("si-conversions-p4", film_seconds, "s")

# p5: book cover 450 cm² → m²  (1 m² = 100 × 100 cm²)
cover_cm2 = 450
cm2_per_m2 = 100 * 100
show("si-conversions-p5", cover_cm2 / cm2_per_m2, "m²")

# p6: kettle 1500 cm³ → m³  (1 m³ = 100 × 100 × 100 cm³)
kettle_cm3 = 1500
cm3_per_m3 = 100 * 100 * 100
show("si-conversions-p6", kettle_cm3 / cm3_per_m3, "m³")

# ---------------------------------------------------------------
# Type 2: prefixes
# ---------------------------------------------------------------
print("# prefixes")

KILO = 1000
MEGA = 1000 * 1000
GIGA = 1000 * 1000 * 1000
MILLI = 1 / 1000
MICRO = 1 / (1000 * 1000)
NANO = 1 / (1000 * 1000 * 1000)

# w: kettle 540 kJ → J
show("prefixes-w", 540 * KILO, "J")

# p1: LED current 20 mA → A
show("prefixes-p1", 20 * MILLI, "A")

# p2: power station 1.8 GW → W
show("prefixes-p2", 1.8 * GIGA, "W")

# p3: wind turbine 2.5 MW → W
show("prefixes-p3", 2.5 * MEGA, "W")

# p4: resistor 4.7 kΩ → Ω
show("prefixes-p4", 4.7 * KILO, "Ω")

# p5: camera flash 250 μs → s
show("prefixes-p5", 250 * MICRO, "s")

# p6: red light 650 nm → m
show("prefixes-p6", 650 * NANO, "m")

# ---------------------------------------------------------------
# Type 3: compound-units
# ---------------------------------------------------------------
print("# compound-units")

METRES_PER_KM = 1000
SECONDS_PER_HOUR = 3600
JOULES_PER_KWH = 3600000

# w: car 90 km/h → m/s
show("compound-units-w", 90 * METRES_PER_KM / SECONDS_PER_HOUR, "m/s")

# p1: train 108 km/h → m/s
show("compound-units-p1", 108 * METRES_PER_KM / SECONDS_PER_HOUR, "m/s")

# p2: television 1.5 kWh → J
show("compound-units-p2", 1.5 * JOULES_PER_KWH, "J")

# p3: cyclist 12 m/s → km/h
cyclist_m_per_hour = 12 * SECONDS_PER_HOUR
show("compound-units-p3", cyclist_m_per_hour / METRES_PER_KM, "km/h")

# p4: aluminium 2.7 g/cm³ → kg/m³  (g → kg is ÷1000, cm³ → m³ is ÷1 000 000)
aluminium_kg_per_cm3 = 2.7 / 1000
show("compound-units-p4", aluminium_kg_per_cm3 * cm3_per_m3, "kg/m³")

# p5: snail 15 cm per minute → m/s
snail_m_per_minute = 15 / 100
show("compound-units-p5", snail_m_per_minute / 60, "m/s")

# p6: tap 12 litres per minute → m³/s  (1 litre = 1000 cm³)
tap_cm3_per_minute = 12 * 1000
tap_m3_per_minute = tap_cm3_per_minute / cm3_per_m3
show("compound-units-p6", tap_m3_per_minute / 60, "m³/s")

# ---------------------------------------------------------------
# Type 4: standard-form
# ---------------------------------------------------------------
print("# standard-form")

# w: 9.8 × 10⁷ Hz → ordinary number
show("standard-form-w", 9.8 * 10 ** 7, "Hz")

# p1: 1.2 × 10⁻² m → ordinary number
show("standard-form-p1", 1.2 * 10 ** -2, "m")

# p2: 6.4 × 10⁶ m → ordinary number
show("standard-form-p2", 6.4 * 10 ** 6, "m")

# p3: 2 500 000 Hz = 2.5 × 10ⁿ → n
ultrasound_hz = 2500000
n_ultrasound = math.log10(ultrasound_hz / 2.5)
show("standard-form-p3", n_ultrasound, "")

# p4: 0.000 000 45 m = 4.5 × 10ⁿ → n
blue_m = 0.00000045
n_blue = math.log10(blue_m / 4.5)
show("standard-form-p4", round(n_blue), "")

# p5: distance = speed × time = 3 × 10⁸ × 2 × 10⁻⁶
pulse_time = 2 * 10 ** -6
speed_of_light = 3 * 10 ** 8
show("standard-form-p5", speed_of_light * pulse_time, "m")

# p6: total charge = 5 × 10¹⁹ × 1.6 × 10⁻¹⁹
electron_count = 5 * 10 ** 19
electron_charge = 1.6 * 10 ** -19
show("standard-form-p6", electron_count * electron_charge, "C")

# ---------------------------------------------------------------
# Type 5: rearranging
# ---------------------------------------------------------------
print("# rearranging")

# w: P = I × V, find I: kettle 2300 W at 230 V
show("rearranging-w", 2300 / 230, "A")

# p1: W = m × g, find m: weight 450 N
show("rearranging-p1", 450 / G, "kg")

# p2: ρ = m / V, find V: glass 2500 kg/m³, 5 kg
show("rearranging-p2", 5 / 2500, "m³")

# p3: GPE = m × g × h, find h: 60 kg climber gains 3000 J
show("rearranging-p3", 3000 / (60 * G), "m")

# p4: KE = ½ × m × v², find v: 3600 J, 50 kg
v_squared = 2 * 3600 / 50
show("rearranging-p4", math.sqrt(v_squared), "m/s")

# p5: v² − u² = 2 × a × x, find u: v = 30, a = 2, x = 200
u_squared = 30 ** 2 - 2 * 2 * 200
show("rearranging-p5", math.sqrt(u_squared), "m/s")

# p6: E = ½ × k × x², find x: E = 1 J, k = 50 N/m
x_squared = 2 * 1 / 50
show("rearranging-p6", math.sqrt(x_squared), "m")

# ---------------------------------------------------------------
# Type 6: percentages-ratios
# ---------------------------------------------------------------
print("# percentages-ratios")

# w: motor efficiency: 350 J useful from 500 J
show("percentages-ratios-w", 350 / 500 * 100, "%")

# p1: kettle efficiency: 324 000 J useful from 360 000 J
show("percentages-ratios-p1", 324000 / 360000 * 100, "%")

# p2: transformer turns ratio 400 : 50
show("percentages-ratios-p2", 400 / 50, "")

# p3: percentage change in speed 20 → 25 m/s
show("percentages-ratios-p3", (25 - 20) / 20 * 100, "%")

# p4: 28% of 30 MJ, in J
fuel_energy_j = 30 * MEGA
show("percentages-ratios-p4", 28 / 100 * fuel_energy_j, "J")

# p5: LED 12 W input, 2.4 W wasted → efficiency
led_useful = 12 - 2.4
show("percentages-ratios-p5", led_useful / 12 * 100, "%")

# p6: ball 0.5 kg dropped from 2.0 m, rebounds to 1.4 m → % GPE lost
gpe_before = 0.5 * G * 2.0
gpe_after = 0.5 * G * 1.4
gpe_lost = gpe_before - gpe_after
show("percentages-ratios-p6", gpe_lost / gpe_before * 100, "%")
