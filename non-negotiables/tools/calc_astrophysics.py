#!/usr/bin/env python3
"""Compute every answer in data/astrophysics.json.

Each answer is printed rounded to 3 s.f. with its question id, followed by
the raw (unrounded) value. Intermediate quantities used in walkthroughs are
printed as well so the working in the JSON matches this script.
Run: python3 tools/calc_astrophysics.py
"""

import math

# Standard constants from SCHEMA.md
c = 3.00e8          # m s^-1
G = 6.67e-11        # N m^2 kg^-2
sigma = 5.67e-8     # W m^-2 K^-4
wien = 2.90e-3      # m K
AU = 1.50e11        # m
LY = 9.46e15        # m
PC = 3.09e16        # m
M_SUN = 1.99e30     # kg
M_EARTH = 5.97e24   # kg

# Values given in the question text where needed
L_SUN = 3.85e26     # W
R_SUN = 6.96e8      # m
YEAR = 3.16e7       # s
MPC = 1e6 * PC      # m

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
        # Store whole numbers as integers so repr is clean (e.g. 9360000 not
        # 9360000.0); above 1e15 a float's repr is already in e-notation and
        # an int cast would expose binary rounding noise, so leave it a float
        if places <= 0 and abs(rounded) < 1e15:
            rounded = int(rounded)
    results.append((question_id, rounded, unit, value))


def note(label, value):
    """Print an intermediate value used in a walkthrough."""
    print(f"    {label} = {value!r}")


# ---------------------------------------------------------------
# Type 1: distance-units
# ---------------------------------------------------------------

# w: Neptune 30.1 AU -> m
record("distance-units-w", 30.1 * AU, "m")

# p1: Proxima Centauri 4.24 ly -> m
record("distance-units-p1", 4.24 * LY, "m")

# p2: light travel time over 1 AU, in s
record("distance-units-p2", AU / c, "s")

# p3: Sirius 8.14e16 m -> ly
record("distance-units-p3", 8.14e16 / LY, "ly")

# p4: Mars closest approach 54.6 million km -> AU
metres_p4 = 54.6e6 * 1e3
note("distance-units-p4 metres", metres_p4)
record("distance-units-p4", metres_p4 / AU, "AU")

# p5: Voyager 1 at 163 AU -> signal time in hours (two steps)
metres_p5 = 163 * AU
seconds_p5 = metres_p5 / c
note("distance-units-p5 metres", metres_p5)
note("distance-units-p5 seconds", seconds_p5)
record("distance-units-p5", seconds_p5 / 3600, "h")

# p6: Betelgeuse 548 ly -> pc via metres (two steps)
metres_p6 = 548 * LY
note("distance-units-p6 metres", metres_p6)
record("distance-units-p6", metres_p6 / PC, "pc")


# ---------------------------------------------------------------
# Type 2: parallax
# ---------------------------------------------------------------

# w: Vega p = 0.130 arcsec -> pc
record("parallax-w", 1 / 0.130, "pc")

# p1: 61 Cygni p = 0.287 arcsec -> pc
record("parallax-p1", 1 / 0.287, "pc")

# p2: Altair p = 0.195 arcsec -> pc
record("parallax-p2", 1 / 0.195, "pc")

# p3: star at 25.0 pc -> parallax in arcsec
record("parallax-p3", 1 / 25.0, "arcsec")

# p4: parallax 7.50 milliarcseconds -> pc
p_p4 = 7.50e-3
note("parallax-p4 arcsec", p_p4)
record("parallax-p4", 1 / p_p4, "pc")

# p5: Sirius p = 0.379 arcsec -> ly (two steps)
d_pc_p5 = 1 / 0.379
d_m_p5 = d_pc_p5 * PC
note("parallax-p5 pc", d_pc_p5)
note("parallax-p5 metres", d_m_p5)
record("parallax-p5", d_m_p5 / LY, "ly")

# p6: Arcturus p = 0.0889 arcsec -> m (two steps)
d_pc_p6 = 1 / 0.0889
note("parallax-p6 pc", d_pc_p6)
record("parallax-p6", d_pc_p6 * PC, "m")


# ---------------------------------------------------------------
# Type 3: inverse-square
# ---------------------------------------------------------------

# w: intensity of sunlight at Earth (1 AU)
record("inverse-square-w", L_SUN / (4 * math.pi * AU ** 2), "W m⁻²")

# p1: intensity of sunlight at Mars, d = 2.28e11 m
record("inverse-square-p1", L_SUN / (4 * math.pi * (2.28e11) ** 2), "W m⁻²")

# p2: star L = 1.2e28 W at d = 4.0e17 m
record("inverse-square-p2", 1.2e28 / (4 * math.pi * (4.0e17) ** 2), "W m⁻²")

# p3: Sirius I = 1.0e-7 W m^-2 at 8.14e16 m -> L
record("inverse-square-p3", 1.0e-7 * 4 * math.pi * (8.14e16) ** 2, "W")

# p4: Saturn at 9.58 AU -> intensity
d_p4 = 9.58 * AU
note("inverse-square-p4 metres", d_p4)
record("inverse-square-p4", L_SUN / (4 * math.pi * d_p4 ** 2), "W m⁻²")

# p5: star L = 40 L_sun, I = 2.6e-8 W m^-2 -> d in ly (two steps)
L_p5 = 40 * L_SUN
d_m_p5 = math.sqrt(L_p5 / (4 * math.pi * 2.6e-8))
note("inverse-square-p5 L", L_p5)
note("inverse-square-p5 d m", d_m_p5)
record("inverse-square-p5", d_m_p5 / LY, "ly")

# p6: probe at Venus 1.08e11 m, panel 3.5 m^2 -> power (two steps)
I_p6 = L_SUN / (4 * math.pi * (1.08e11) ** 2)
note("inverse-square-p6 I", I_p6)
record("inverse-square-p6", I_p6 * 3.5, "W")


# ---------------------------------------------------------------
# Type 4: stefan-boltzmann
# ---------------------------------------------------------------

def luminosity(radius, temperature):
    """Stefan-Boltzmann luminosity of a sphere."""
    return 4 * math.pi * radius ** 2 * sigma * temperature ** 4


# w: Sun r = 6.96e8 m, T = 5800 K -> L
note("stefan-boltzmann-w 4pi r^2", 4 * math.pi * R_SUN ** 2)
record("stefan-boltzmann-w", luminosity(R_SUN, 5800), "W")

# p1: Sirius r = 1.19e9 m, T = 9940 K -> L
record("stefan-boltzmann-p1", luminosity(1.19e9, 9940), "W")

# p2: Proxima r = 1.07e8 m, T = 3040 K -> L
record("stefan-boltzmann-p2", luminosity(1.07e8, 3040), "W")

# p3: Sirius B radius 5840 km, T = 25200 K -> L (km conversion)
r_p3 = 5840e3
note("stefan-boltzmann-p3 r m", r_p3)
record("stefan-boltzmann-p3", luminosity(r_p3, 25200), "W")

# p4: Vega L = 1.54e28 W, r = 1.64e9 m -> T
T4_p4 = 1.54e28 / (4 * math.pi * (1.64e9) ** 2 * sigma)
note("stefan-boltzmann-p4 T^4", T4_p4)
record("stefan-boltzmann-p4", T4_p4 ** 0.25, "K")

# p5: Betelgeuse L = 1.2e5 L_sun, T = 3500 K -> r (two steps)
L_p5 = 1.2e5 * L_SUN
r2_p5 = L_p5 / (4 * math.pi * sigma * 3500 ** 4)
note("stefan-boltzmann-p5 L", L_p5)
note("stefan-boltzmann-p5 r^2", r2_p5)
record("stefan-boltzmann-p5", math.sqrt(r2_p5), "m")

# p6: star r = 2.5 R_sun, T = 7200 K -> L (two steps)
r_p6 = 2.5 * R_SUN
note("stefan-boltzmann-p6 r", r_p6)
record("stefan-boltzmann-p6", luminosity(r_p6, 7200), "W")


# ---------------------------------------------------------------
# Type 5: wien-law
# ---------------------------------------------------------------

# w: Sun peak 500 nm -> T
record("wien-law-w", wien / 500e-9, "K")

# p1: Betelgeuse peak 830 nm -> T
record("wien-law-p1", wien / 830e-9, "K")

# p2: Rigel T = 12100 K -> peak in nm
lam_p2 = wien / 12100
note("wien-law-p2 lambda m", lam_p2)
record("wien-law-p2", lam_p2 / 1e-9, "nm")

# p3: human body 310 K -> peak in um
lam_p3 = wien / 310
note("wien-law-p3 lambda m", lam_p3)
record("wien-law-p3", lam_p3 / 1e-6, "μm")

# p4: furnace peak 1.45 um -> T
record("wien-law-p4", wien / 1.45e-6, "K")

# p5: peak frequency 3.4e14 Hz -> T (two steps)
lam_p5 = c / 3.4e14
note("wien-law-p5 lambda m", lam_p5)
record("wien-law-p5", wien / lam_p5, "K")

# p6: CMB T = 2.73 K -> peak frequency (two steps)
lam_p6 = wien / 2.73
note("wien-law-p6 lambda m", lam_p6)
record("wien-law-p6", c / lam_p6, "Hz")


# ---------------------------------------------------------------
# Type 6: wien-stefan-combined
# ---------------------------------------------------------------

# w: peak 580 nm, L = 2.3e27 W -> r
T_w = wien / 580e-9
r2_w = 2.3e27 / (4 * math.pi * sigma * T_w ** 4)
note("wien-stefan-combined-w T", T_w)
note("wien-stefan-combined-w r^2", r2_w)
record("wien-stefan-combined-w", math.sqrt(r2_w), "m")

# p1: peak 290 nm, r = 2.0e9 m -> L
T_p1 = wien / 290e-9
note("wien-stefan-combined-p1 T", T_p1)
record("wien-stefan-combined-p1", luminosity(2.0e9, T_p1), "W")

# p2: red giant peak 1000 nm, r = 3.5e10 m -> L
T_p2 = wien / 1000e-9
note("wien-stefan-combined-p2 T", T_p2)
record("wien-stefan-combined-p2", luminosity(3.5e10, T_p2), "W")

# p3: peak 480 nm, L = 8.0e26 W -> r in km
T_p3 = wien / 480e-9
r2_p3 = 8.0e26 / (4 * math.pi * sigma * T_p3 ** 4)
r_p3 = math.sqrt(r2_p3)
note("wien-stefan-combined-p3 T", T_p3)
note("wien-stefan-combined-p3 r^2", r2_p3)
note("wien-stefan-combined-p3 r m", r_p3)
record("wien-stefan-combined-p3", r_p3 / 1e3, "km")

# p4: peak 725 nm, L = 9.5e29 W -> r in m
T_p4 = wien / 725e-9
r2_p4 = 9.5e29 / (4 * math.pi * sigma * T_p4 ** 4)
note("wien-stefan-combined-p4 T", T_p4)
note("wien-stefan-combined-p4 r^2", r2_p4)
record("wien-stefan-combined-p4", math.sqrt(r2_p4), "m")

# p5: peak 362.5 nm, r = 1.2e9 m -> L / L_sun
T_p5 = wien / 362.5e-9
L_p5 = luminosity(1.2e9, T_p5)
note("wien-stefan-combined-p5 T", T_p5)
note("wien-stefan-combined-p5 L", L_p5)
record("wien-stefan-combined-p5", L_p5 / L_SUN, "")

# p6: peak 1160 nm, L = 1.2e30 W -> r / R_sun
T_p6 = wien / 1160e-9
r2_p6 = 1.2e30 / (4 * math.pi * sigma * T_p6 ** 4)
r_p6 = math.sqrt(r2_p6)
note("wien-stefan-combined-p6 T", T_p6)
note("wien-stefan-combined-p6 r^2", r2_p6)
note("wien-stefan-combined-p6 r m", r_p6)
record("wien-stefan-combined-p6", r_p6 / R_SUN, "")


# ---------------------------------------------------------------
# Type 7: redshift
# ---------------------------------------------------------------

# w: H-alpha 656.3 nm observed at 662.9 nm -> v
z_w = (662.9 - 656.3) / 656.3
note("redshift-w z", z_w)
record("redshift-w", z_w * c, "m s⁻¹")

# p1: z = 0.025 -> v
record("redshift-p1", 0.025 * c, "m s⁻¹")

# p2: shift 12.4 nm on 486.1 nm line -> z
record("redshift-p2", 12.4 / 486.1, "")

# p3: v = 1.8e6 m/s, rest 393.4 nm -> observed wavelength in nm
z_p3 = 1.8e6 / c
shift_p3 = z_p3 * 393.4
note("redshift-p3 z", z_p3)
note("redshift-p3 shift nm", shift_p3)
record("redshift-p3", 393.4 + shift_p3, "nm")

# p4: v = 4500 km/s, rest 656.3 nm -> shift in nm
z_p4 = 4500e3 / c
note("redshift-p4 z", z_p4)
record("redshift-p4", z_p4 * 656.3, "nm")

# p5: 21 cm line, rest 21.11 cm observed 21.80 cm -> v in km/s (two steps)
z_p5 = (21.80 - 21.11) / 21.11
v_p5 = z_p5 * c
note("redshift-p5 z", z_p5)
note("redshift-p5 v m/s", v_p5)
record("redshift-p5", v_p5 / 1e3, "km s⁻¹")

# p6: sodium line rest 589.0 nm observed 588.7 nm (blueshift) -> speed of approach in km/s
z_p6 = (589.0 - 588.7) / 589.0
v_p6 = z_p6 * c
note("redshift-p6 z", z_p6)
note("redshift-p6 v m/s", v_p6)
record("redshift-p6", v_p6 / 1e3, "km s⁻¹")


# ---------------------------------------------------------------
# Type 8: hubble-law
# ---------------------------------------------------------------

H0 = 70.0  # km s^-1 Mpc^-1

# w: d = 50 Mpc -> v in km/s
record("hubble-law-w", H0 * 50, "km s⁻¹")

# p1: d = 120 Mpc -> v
record("hubble-law-p1", H0 * 120, "km s⁻¹")

# p2: v = 21000 km/s -> d in Mpc
record("hubble-law-p2", 21000 / H0, "Mpc")

# p3: d = 2.5e24 m -> Mpc -> v
d_mpc_p3 = 2.5e24 / MPC
note("hubble-law-p3 d Mpc", d_mpc_p3)
record("hubble-law-p3", H0 * d_mpc_p3, "km s⁻¹")

# p4: v = 1.2e7 m/s -> km/s -> d in Mpc
v_kms_p4 = 1.2e7 / 1e3
note("hubble-law-p4 v km/s", v_kms_p4)
record("hubble-law-p4", v_kms_p4 / H0, "Mpc")

# p5: z = 0.030 -> v -> d in Mpc (two steps)
v_p5 = 0.030 * c
v_kms_p5 = v_p5 / 1e3
note("hubble-law-p5 v m/s", v_p5)
note("hubble-law-p5 v km/s", v_kms_p5)
record("hubble-law-p5", v_kms_p5 / H0, "Mpc")

# p6: d = 3.5e8 ly -> m -> Mpc -> v (two steps)
d_m_p6 = 3.5e8 * LY
d_mpc_p6 = d_m_p6 / MPC
note("hubble-law-p6 d m", d_m_p6)
note("hubble-law-p6 d Mpc", d_mpc_p6)
record("hubble-law-p6", H0 * d_mpc_p6, "km s⁻¹")


# ---------------------------------------------------------------
# Type 9: hubble-age
# ---------------------------------------------------------------

def H0_si(h0_km_s_mpc):
    """Convert H0 from km s^-1 Mpc^-1 to s^-1."""
    return h0_km_s_mpc * 1e3 / MPC


# w: H0 = 70 -> age in years
H_w = H0_si(70)
t_s_w = 1 / H_w
note("hubble-age-w H0 s^-1", H_w)
note("hubble-age-w t s", t_s_w)
record("hubble-age-w", t_s_w / YEAR, "years")

# p1: H0 = 70 -> s^-1
record("hubble-age-p1", H0_si(70), "s⁻¹")

# p2: H0 = 2.3e-18 s^-1 -> age in years
t_s_p2 = 1 / 2.3e-18
note("hubble-age-p2 t s", t_s_p2)
record("hubble-age-p2", t_s_p2 / YEAR, "years")

# p3: H0 = 67.4 -> age in billions of years
H_p3 = H0_si(67.4)
t_s_p3 = 1 / H_p3
t_yr_p3 = t_s_p3 / YEAR
note("hubble-age-p3 H0 s^-1", H_p3)
note("hubble-age-p3 t s", t_s_p3)
note("hubble-age-p3 t yr", t_yr_p3)
record("hubble-age-p3", t_yr_p3 / 1e9, "billion years")

# p4: age 13.0e9 yr -> H0 in km s^-1 Mpc^-1
t_s_p4 = 13.0e9 * YEAR
H_si_p4 = 1 / t_s_p4
note("hubble-age-p4 t s", t_s_p4)
note("hubble-age-p4 H0 s^-1", H_si_p4)
record("hubble-age-p4", H_si_p4 * MPC / 1e3, "km s⁻¹ Mpc⁻¹")

# p5: galaxy v = 6500 km/s at d = 100 Mpc -> H0 -> age in years (two steps)
H_kms_p5 = 6500 / 100
H_si_p5 = H0_si(H_kms_p5)
t_s_p5 = 1 / H_si_p5
note("hubble-age-p5 H0 km/s/Mpc", H_kms_p5)
note("hubble-age-p5 H0 s^-1", H_si_p5)
note("hubble-age-p5 t s", t_s_p5)
record("hubble-age-p5", t_s_p5 / YEAR, "years")

# p6: H0 = 68 -> Hubble distance c/H0 in ly (two steps)
H_si_p6 = H0_si(68)
d_m_p6 = c / H_si_p6
note("hubble-age-p6 H0 s^-1", H_si_p6)
note("hubble-age-p6 d m", d_m_p6)
record("hubble-age-p6", d_m_p6 / LY, "ly")


# ---------------------------------------------------------------
# Type 10: magnitudes (AQA only)
# ---------------------------------------------------------------

# w: Sirius m = -1.46, d = 2.64 pc -> M
term_w = 5 * math.log10(2.64 / 10)
note("magnitudes-w 5log(d/10)", term_w)
record("magnitudes-w", -1.46 - term_w, "")

# p1: m = 6.0, d = 100 pc -> M
term_p1 = 5 * math.log10(100 / 10)
note("magnitudes-p1 5log(d/10)", term_p1)
record("magnitudes-p1", 6.0 - term_p1, "")

# p2: Polaris M = -3.6, d = 133 pc -> m
term_p2 = 5 * math.log10(133 / 10)
note("magnitudes-p2 5log(d/10)", term_p2)
record("magnitudes-p2", -3.6 + term_p2, "")

# p3: Deneb m = 1.25, M = -8.4 -> d in pc
exponent_p3 = (1.25 - (-8.4)) / 5
note("magnitudes-p3 exponent", exponent_p3)
record("magnitudes-p3", 10 * 10 ** exponent_p3, "pc")

# p4: m = 4.8, d = 820 ly -> pc -> M
d_pc_p4 = 820 * LY / PC
term_p4 = 5 * math.log10(d_pc_p4 / 10)
note("magnitudes-p4 d pc", d_pc_p4)
note("magnitudes-p4 5log(d/10)", term_p4)
record("magnitudes-p4", 4.8 - term_p4, "")

# p5: parallax 0.0125 arcsec, m = 3.5 -> d -> M (two steps)
d_pc_p5 = 1 / 0.0125
term_p5 = 5 * math.log10(d_pc_p5 / 10)
note("magnitudes-p5 d pc", d_pc_p5)
note("magnitudes-p5 5log(d/10)", term_p5)
record("magnitudes-p5", 3.5 - term_p5, "")

# p6: Cepheid M = -4.0, m = 12.0 -> d in pc -> ly (two steps)
exponent_p6 = (12.0 - (-4.0)) / 5
d_pc_p6 = 10 * 10 ** exponent_p6
d_m_p6 = d_pc_p6 * PC
note("magnitudes-p6 exponent", exponent_p6)
note("magnitudes-p6 d pc", d_pc_p6)
note("magnitudes-p6 d m", d_m_p6)
record("magnitudes-p6", d_m_p6 / LY, "ly")


# ---------------------------------------------------------------
# Type 11: schwarzschild-radius (AQA, OCR B)
# ---------------------------------------------------------------

def schwarzschild(mass):
    """Schwarzschild radius of a mass."""
    return 2 * G * mass / c ** 2


# w: Sun -> R_s
record("schwarzschild-radius-w", schwarzschild(M_SUN), "m")

# p1: stellar black hole M = 2.4e31 kg
record("schwarzschild-radius-p1", schwarzschild(2.4e31), "m")

# p2: Sagittarius A* M = 8.2e36 kg
record("schwarzschild-radius-p2", schwarzschild(8.2e36), "m")

# p3: R_s = 60 km -> M
R_p3 = 60e3
note("schwarzschild-radius-p3 R m", R_p3)
record("schwarzschild-radius-p3", R_p3 * c ** 2 / (2 * G), "kg")

# p4: Earth -> R_s in mm
R_p4 = schwarzschild(M_EARTH)
note("schwarzschild-radius-p4 R m", R_p4)
record("schwarzschild-radius-p4", R_p4 / 1e-3, "mm")

# p5: 15 solar masses -> R_s in km (two steps)
M_p5 = 15 * M_SUN
R_p5 = schwarzschild(M_p5)
note("schwarzschild-radius-p5 M", M_p5)
note("schwarzschild-radius-p5 R m", R_p5)
record("schwarzschild-radius-p5", R_p5 / 1e3, "km")

# p6: M87* R_s = 1.9e13 m -> M in solar masses (two steps)
M_p6 = 1.9e13 * c ** 2 / (2 * G)
note("schwarzschild-radius-p6 M kg", M_p6)
record("schwarzschild-radius-p6", M_p6 / M_SUN, "solar masses")


# ---------------------------------------------------------------
# Print
# ---------------------------------------------------------------

print()
for question_id, rounded, unit, raw in results:
    print(f"{question_id:28s} {rounded!r:>14}  {unit:16s} (raw {raw!r})")
