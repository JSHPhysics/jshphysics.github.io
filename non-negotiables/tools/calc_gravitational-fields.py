#!/usr/bin/env python3
"""Compute every answer in data/gravitational-fields.json.

Each answer is printed rounded to 3 s.f. with its question id.
Run: python3 tools/calc_gravitational-fields.py
"""

import math

# Standard constants from SCHEMA.md
G = 6.67e-11        # N m^2 kg^-2
g = 9.81            # m s^-2
M_E = 5.97e24       # kg, Earth mass
R_E = 6.37e6        # m, Earth radius
M_SUN = 1.99e30     # kg, Sun mass
AU = 1.50e11        # m

# Body data given in question text (not on the data sheet)
M_MOON = 7.35e22    # kg
R_MOON = 1.74e6     # m
M_MARS = 6.42e23    # kg
R_MARS = 3.39e6     # m
M_JUP = 1.90e27     # kg
M_VENUS = 4.87e24   # kg
R_VENUS = 6.05e6    # m
M_MERC = 3.30e23    # kg
R_MERC = 2.44e6     # m
M_NEP = 1.02e26     # kg
R_NEP = 2.46e7      # m
M_SAT = 5.68e26     # kg
R_SAT = 5.82e7      # m
M_PLUTO = 1.31e22   # kg
R_PLUTO = 1.19e6    # m

results = []


def record(question_id, value, unit):
    """Store one answer, rounded to 3 significant figures."""
    if value == 0:
        rounded = 0.0
    else:
        # Format to 3 s.f., then parse back so the value is exactly 3 s.f.
        rounded = float(f"{value:.3g}")
        # Whole-number answers below 1e16 are stored as integers so repr is clean;
        # anything larger stays a float and prints in e-notation (e.g. 1.98e+20)
        if rounded == int(rounded) and abs(rounded) < 1e16:
            rounded = int(rounded)
    results.append((question_id, rounded, unit, value))


# ---------------------------------------------------------------
# Type 1: newtons-law-of-gravitation   F = GMm / r^2
# ---------------------------------------------------------------

# w: Earth-Moon force, separation 3.84e8 m
record("newtons-law-of-gravitation-w", G * M_E * M_MOON / (3.84e8) ** 2, "N")

# p1: two 20 kg lead spheres, centres 0.150 m apart
record("newtons-law-of-gravitation-p1", G * 20 * 20 / 0.150 ** 2, "N")

# p2: Sun-Earth force at 1 AU
record("newtons-law-of-gravitation-p2", G * M_SUN * M_E / AU ** 2, "N")

# p3: 850 kg satellite at altitude 400 km above Earth
r_p3 = R_E + 400e3
record("newtons-law-of-gravitation-p3", G * M_E * 850 / r_p3 ** 2, "N")

# p4: Jupiter-Io separation from force 6.35e22 N, Io mass 8.93e22 kg
r_p4 = math.sqrt(G * M_JUP * 8.93e22 / 6.35e22)
record("newtons-law-of-gravitation-p4", r_p4, "m")

# p5: asteroid radius 10.0 km, density 2500 kg/m^3; force on 500 kg probe at surface
volume_p5 = (4 / 3) * math.pi * (10.0e3) ** 3
mass_p5 = volume_p5 * 2500
record("newtons-law-of-gravitation-p5", G * mass_p5 * 500 / (10.0e3) ** 2, "N")

# p6: height above Earth's surface where force is half the surface value
r_p6 = R_E * math.sqrt(2)
record("newtons-law-of-gravitation-p6", r_p6 - R_E, "m")


# ---------------------------------------------------------------
# Type 2: gravitational-field-strength   g = GM / r^2,  g = F / m
# ---------------------------------------------------------------

# w: g at the surface of Mars
record("gravitational-field-strength-w", G * M_MARS / R_MARS ** 2, "N kg⁻¹")

# p1: g at the surface of the Moon
record("gravitational-field-strength-p1", G * M_MOON / R_MOON ** 2, "N kg⁻¹")

# p2: 72 kg astronaut weighs 266 N on Mercury -> g = F/m
record("gravitational-field-strength-p2", 266 / 72, "N kg⁻¹")

# p3: g at ISS altitude 410 km above Earth
r_g_p3 = R_E + 410e3
record("gravitational-field-strength-p3", G * M_E / r_g_p3 ** 2, "N kg⁻¹")

# p4: mass of Venus from g = 8.87 N/kg, R = 6.05e6 m
record("gravitational-field-strength-p4", 8.87 * R_VENUS ** 2 / G, "kg")

# p5: altitude above Earth where g = 2.45 N/kg, in km
r_g_p5 = math.sqrt(G * M_E / 2.45)
record("gravitational-field-strength-p5", (r_g_p5 - R_E) / 1e3, "km")

# p6: weight of 85 kg astronaut on Mercury (find g, then W = mg)
g_merc_p6 = G * M_MERC / R_MERC ** 2
record("gravitational-field-strength-p6", 85 * g_merc_p6, "N")


# ---------------------------------------------------------------
# Type 3: gravitational-potential   V = -GM / r,  Ep = -GMm / r
# ---------------------------------------------------------------

# w: V at the Earth's surface
record("gravitational-potential-w", -G * M_E / R_E, "J kg⁻¹")

# p1: V at the Moon's surface
record("gravitational-potential-p1", -G * M_MOON / R_MOON, "J kg⁻¹")

# p2: Ep of 2000 kg satellite at r = 4.22e7 m from Earth's centre
record("gravitational-potential-p2", -G * M_E * 2000 / 4.22e7, "J")

# p3: V at altitude 2000 km above Earth's surface
r_v_p3 = R_E + 2000e3
record("gravitational-potential-p3", -G * M_E / r_v_p3, "J kg⁻¹")

# p4: distance from Earth's centre where V = -1.50e7 J/kg
record("gravitational-potential-p4", G * M_E / 1.50e7, "m")

# p5: Ep of a 12.0 tonne module at altitude 400 km above Earth
r_v_p5 = R_E + 400e3
mass_p5 = 12.0e3
record("gravitational-potential-p5", -G * M_E * mass_p5 / r_v_p5, "J")

# p6: Neptune radius from surface V = -2.76e8 J/kg and g = 11.2 N/kg
#     V = -GM/R and g = GM/R^2  ->  R = |V| / g
record("gravitational-potential-p6", 2.76e8 / 11.2, "m")


# ---------------------------------------------------------------
# Type 4: work-done-in-field   ΔW = m ΔV
# ---------------------------------------------------------------

# w: lift 1200 kg satellite from Earth's surface to altitude 600 km
V_surface = -G * M_E / R_E
V_600 = -G * M_E / (R_E + 600e3)
record("work-done-in-field-w", 1200 * (V_600 - V_surface), "J")

# p1: 850 kg from V = -6.25e7 to V = -5.30e7 J/kg
record("work-done-in-field-p1", 850 * (-5.30e7 - (-6.25e7)), "J")

# p2: 70 kg astronaut from Moon surface V = -2.82e6 to V = -1.10e6 J/kg
record("work-done-in-field-p2", 70 * (-1.10e6 - (-2.82e6)), "J")

# p3: 450 kg probe from Earth's surface to altitude 3000 km
V_3000 = -G * M_E / (R_E + 3000e3)
record("work-done-in-field-p3", 450 * (V_3000 - V_surface), "J")

# p4: mass lifted by 2.40e9 J from V = -6.25e7 to V = -4.65e7 J/kg
record("work-done-in-field-p4", 2.40e9 / (-4.65e7 - (-6.25e7)), "kg")

# p5: 900 kg Mars lander from Mars surface to altitude 300 km
V_mars_surface = -G * M_MARS / R_MARS
V_mars_300 = -G * M_MARS / (R_MARS + 300e3)
record("work-done-in-field-p5", 900 * (V_mars_300 - V_mars_surface), "J")

# p6: energy released by 25 kg meteoroid falling from r = 8.00e7 m to Earth's surface
V_far = -G * M_E / 8.00e7
record("work-done-in-field-p6", 25 * (V_far - V_surface), "J")


# ---------------------------------------------------------------
# Type 5: escape-velocity   v = sqrt(2GM / r)
# ---------------------------------------------------------------

# w: Earth
record("escape-velocity-w", math.sqrt(2 * G * M_E / R_E), "m s⁻¹")

# p1: Moon
record("escape-velocity-p1", math.sqrt(2 * G * M_MOON / R_MOON), "m s⁻¹")

# p2: Mars
record("escape-velocity-p2", math.sqrt(2 * G * M_MARS / R_MARS), "m s⁻¹")

# p3: Jupiter, radius 69 900 km, answer in km/s
v_jup = math.sqrt(2 * G * M_JUP / 69900e3)
record("escape-velocity-p3", v_jup / 1e3, "km s⁻¹")

# p4: mass of Venus from escape speed 10.4 km/s and radius 6.05e6 m
v_venus = 10.4e3
record("escape-velocity-p4", v_venus ** 2 * R_VENUS / (2 * G), "kg")

# p5: asteroid radius 500 m, density 2000 kg/m^3
volume_ast = (4 / 3) * math.pi * 500 ** 3
mass_ast = volume_ast * 2000
record("escape-velocity-p5", math.sqrt(2 * G * mass_ast / 500), "m s⁻¹")

# p6: planet with surface g = 25.0 N/kg and radius 7.00e7 m: GM = gR^2 first
GM_p6 = 25.0 * (7.00e7) ** 2
record("escape-velocity-p6", math.sqrt(2 * GM_p6 / 7.00e7), "m s⁻¹")


# ---------------------------------------------------------------
# Type 6: orbital-speed-and-period
#   v = sqrt(GM / r),  T = 2πr / v,  T^2 = 4π^2 r^3 / GM
# ---------------------------------------------------------------

# w: ISS at altitude 400 km: v then T
r_iss = R_E + 400e3
v_iss = math.sqrt(G * M_E / r_iss)
record("orbital-speed-and-period-w", 2 * math.pi * r_iss / v_iss, "s")

# p1: Moon's orbital speed, r = 3.84e8 m
record("orbital-speed-and-period-p1", math.sqrt(G * M_E / 3.84e8), "m s⁻¹")

# p2: period of satellite at r = 7.00e6 m from Earth's centre
record("orbital-speed-and-period-p2", math.sqrt(4 * math.pi ** 2 * (7.00e6) ** 3 / (G * M_E)), "s")

# p3: GPS satellite at altitude 20 200 km, period in hours
r_gps = R_E + 20200e3
T_gps = math.sqrt(4 * math.pi ** 2 * r_gps ** 3 / (G * M_E))
record("orbital-speed-and-period-p3", T_gps / 3600, "h")

# p4: orbital radius around Mars for T = 2.00 h
T_mars_orb = 2.00 * 3600
record("orbital-speed-and-period-p4", (G * M_MARS * T_mars_orb ** 2 / (4 * math.pi ** 2)) ** (1 / 3), "m")

# p5: Europa r = 6.71e8 m around Jupiter: v then T in days
v_europa = math.sqrt(G * M_JUP / 6.71e8)
T_europa = 2 * math.pi * 6.71e8 / v_europa
record("orbital-speed-and-period-p5", T_europa / 86400, "days")

# p6: satellite with period 95.0 min around Earth: r then altitude in km
T_p6 = 95.0 * 60
r_p6_orb = (G * M_E * T_p6 ** 2 / (4 * math.pi ** 2)) ** (1 / 3)
record("orbital-speed-and-period-p6", (r_p6_orb - R_E) / 1e3, "km")


# ---------------------------------------------------------------
# Type 7: geostationary-orbit   r^3 = GM T^2 / 4π^2, altitude = r - R
# ---------------------------------------------------------------

def sync_radius(mass, period_s):
    """Radius of a synchronous orbit for a body of given mass and rotation period."""
    return (G * mass * period_s ** 2 / (4 * math.pi ** 2)) ** (1 / 3)


# w: Earth, T = 24.0 h, altitude above surface
r_geo = sync_radius(M_E, 24.0 * 3600)
record("geostationary-orbit-w", r_geo - R_E, "m")

# p1: Mars, T = 24.6 h, orbital radius
record("geostationary-orbit-p1", sync_radius(M_MARS, 24.6 * 3600), "m")

# p2: Jupiter, T = 9.93 h, orbital radius
record("geostationary-orbit-p2", sync_radius(M_JUP, 9.93 * 3600), "m")

# p3: Neptune, T = 16.1 h, altitude above surface
r_nep = sync_radius(M_NEP, 16.1 * 3600)
record("geostationary-orbit-p3", r_nep - R_NEP, "m")

# p4: Saturn, T = 10.7 h, altitude in km
r_sat = sync_radius(M_SAT, 10.7 * 3600)
record("geostationary-orbit-p4", (r_sat - R_SAT) / 1e3, "km")

# p5: Pluto, T = 6.39 days, altitude in km
r_pluto = sync_radius(M_PLUTO, 6.39 * 86400)
record("geostationary-orbit-p5", (r_pluto - R_PLUTO) / 1e3, "km")

# p6: Mercury: synchronous satellite at altitude 2.38e8 m -> rotation period in days
r_merc = R_MERC + 2.38e8
T_merc = math.sqrt(4 * math.pi ** 2 * r_merc ** 3 / (G * M_MERC))
record("geostationary-orbit-p6", T_merc / 86400, "days")


# ---------------------------------------------------------------
# Type 8: keplers-third-law   T^2 ∝ r^3
# ---------------------------------------------------------------

# w: Mars at 1.52 AU, Earth 1.00 year -> Mars period in years
record("keplers-third-law-w", 1.00 * (1.52 / 1.00) ** 1.5, "years")

# p1: Jupiter at 5.20 AU -> period in years
record("keplers-third-law-p1", 1.00 * (5.20 / 1.00) ** 1.5, "years")

# p2: satellite A r = 7.00e6 m, T = 97.0 min; B r = 2.80e7 m -> T_B in min
record("keplers-third-law-p2", 97.0 * (2.80e7 / 7.00e6) ** 1.5, "min")

# p3: Saturn period 29.5 years -> orbital radius in AU
record("keplers-third-law-p3", 1.00 * (29.5 / 1.00) ** (2 / 3), "AU")

# p4: Io r = 4.22e8 m, T = 1.77 days; Callisto T = 16.7 days -> r in m
record("keplers-third-law-p4", 4.22e8 * (16.7 / 1.77) ** (2 / 3), "m")

# p5: geostationary r = 4.22e7 m, T = 24.0 h; satellite at altitude 800 km -> T in min
r_800 = R_E + 800e3
T_800_h = 24.0 * (r_800 / 4.22e7) ** 1.5
record("keplers-third-law-p5", T_800_h * 60, "min")

# p6: Moon r = 3.84e8 m, T = 27.3 days; satellite with T = 1.00 day -> altitude in m
r_one_day = 3.84e8 * (1.00 / 27.3) ** (2 / 3)
record("keplers-third-law-p6", r_one_day - R_E, "m")


# ---------------------------------------------------------------
# Print
# ---------------------------------------------------------------

for question_id, rounded, unit, raw in results:
    print(f"{question_id:34s} {rounded!r:>14}  {unit:10s} (raw {raw!r})")
