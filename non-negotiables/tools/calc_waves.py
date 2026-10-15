#!/usr/bin/env python3
"""Compute every answer in data/waves.json.

Each answer is printed rounded to 3 s.f. with its question id, together
with the raw value and any intermediate quantities used in the walkthrough.
Run: python3 tools/calc_waves.py
"""

import math

# Standard constants from SCHEMA.md
c = 3.00e8        # m s^-1, speed of light in vacuum

results = []


def round_sf(value, sf=3):
    """Round a value to a given number of significant figures."""
    if value == 0:
        return 0.0
    magnitude = math.floor(math.log10(abs(value)))
    places = sf - 1 - magnitude
    return round(value, places)


def record(question_id, value, unit, notes="", sf=3):
    """Store one answer, rounded to 3 significant figures (or more if the data justify it)."""
    rounded = round_sf(value, sf)
    results.append((question_id, rounded, unit, value, notes))


def deg(radians):
    """Convert radians to degrees."""
    return math.degrees(radians)


def rad(degrees):
    """Convert degrees to radians."""
    return math.radians(degrees)


# ---------------------------------------------------------------
# Type 1: wave-equation  (v = f lambda, f = 1/T)
# ---------------------------------------------------------------

# w: tuning fork 512 Hz in air at 340 m/s, find wavelength
record("wave-equation-w", 340 / 512, "m")

# p1: ripple tank, f = 8.0 Hz, lambda = 0.045 m, find v
record("wave-equation-p1", 8.0 * 0.045, "m s⁻¹")

# p2: ocean swell, period 12 s, find f
record("wave-equation-p2", 1 / 12, "Hz")

# p3: FM radio 93.5 MHz, find wavelength
record("wave-equation-p3", c / (93.5e6), "m")

# p4: sodium light 589 nm, find frequency
record("wave-equation-p4", c / (589e-9), "Hz")

# p5: bat call, period 20 us, speed 340 m/s, find wavelength in mm (two steps)
f_p5 = 1 / 20e-6
lambda_p5 = 340 / f_p5
record("wave-equation-p5", lambda_p5 * 1000, "mm", f"f = {f_p5}")

# p6: seismic P-wave, 240 km in 40 s, f = 2.0 Hz, find wavelength (two steps)
v_p6 = 240e3 / 40
record("wave-equation-p6", v_p6 / 2.0, "m", f"v = {v_p6}")


# ---------------------------------------------------------------
# Type 2: phase-difference
# ---------------------------------------------------------------

# w: rope wave, points 0.20 m apart, lambda 0.80 m, phase in degrees
record("phase-difference-w", 0.20 / 0.80 * 360, "°")

# p1: two loudspeakers, path difference 1.5 m, lambda 2.0 m, phase in rad
record("phase-difference-p1", 1.5 / 2.0 * 2 * math.pi, "rad")

# p2: time delay 0.50 ms, period 4.0 ms, phase in degrees
record("phase-difference-p2", 0.50 / 4.0 * 360, "°")

# p3: phase 60 deg, lambda 1.2 m, find separation
record("phase-difference-p3", 60 / 360 * 1.2, "m")

# p4: points 30 cm apart, lambda 2.4 m, phase in rad
record("phase-difference-p4", 0.30 / 2.4 * 2 * math.pi, "rad")

# p5: slinky, f = 2.5 Hz, v = 1.5 m/s, points 0.45 m apart, phase in degrees (two steps)
lambda_ph_p5 = 1.5 / 2.5
record("phase-difference-p5", 0.45 / lambda_ph_p5 * 360, "°", f"lambda = {lambda_ph_p5}")

# p6: radio 100 MHz, aerials 0.50 m apart along line of travel, phase in rad (two steps)
lambda_ph_p6 = c / 100e6
record("phase-difference-p6", 0.50 / lambda_ph_p6 * 2 * math.pi, "rad", f"lambda = {lambda_ph_p6}")


# ---------------------------------------------------------------
# Type 3: intensity
# ---------------------------------------------------------------

# w: laser 2.0 mW, beam diameter 1.5 mm, find intensity
area_w = math.pi * (0.75e-3) ** 2
record("intensity-w", 2.0e-3 / area_w, "W m⁻²", f"A = {area_w}")

# p1: radiant heater 60 W over panel area 0.30 m^2
record("intensity-p1", 60 / 0.30, "W m⁻²")

# p2: bulb radiating 60 W, intensity at 2.0 m (point source)
area_p2 = 4 * math.pi * 2.0 ** 2
record("intensity-p2", 60 / area_p2, "W m⁻²", f"A = {area_p2}")

# p3: Sun luminosity 3.85e26 W, intensity at Earth 1360 W/m^2, find distance
r_p3 = math.sqrt(3.85e26 / (4 * math.pi * 1360))
record("intensity-p3", r_p3, "m")

# p4: I proportional to A^2: 12 mW/m^2 at 3.0 cm amplitude, find I at 5.0 cm
record("intensity-p4", 12 * (5.0 / 3.0) ** 2, "mW m⁻²")

# p5: transmitter 50 kW isotropic, 10 km away, aerial area 0.20 m^2, power received (two steps)
I_p5 = 50e3 / (4 * math.pi * (10e3) ** 2)
record("intensity-p5", I_p5 * 0.20, "W", f"I = {I_p5}")

# p6: amplitude 0.80 mm at 1.5 m; amplitude at 6.0 m (two steps)
intensity_ratio_p6 = (1.5 / 6.0) ** 2
record("intensity-p6", 0.80 * math.sqrt(intensity_ratio_p6), "mm", f"I ratio = {intensity_ratio_p6}")


# ---------------------------------------------------------------
# Type 4: refractive-index  (n = c/v, n1 sin t1 = n2 sin t2)
# ---------------------------------------------------------------

# w: air to glass n = 1.52, incidence 40 deg
sin_w = math.sin(rad(40)) / 1.52
record("refractive-index-w", deg(math.asin(sin_w)), "°", f"sin = {sin_w}")

# p1: speed in diamond 1.24e8, find n
record("refractive-index-p1", c / 1.24e8, "")

# p2: air to water n = 1.33, incidence 55 deg
sin_p2 = math.sin(rad(55)) / 1.33
record("refractive-index-p2", deg(math.asin(sin_p2)), "°", f"sin = {sin_p2}")

# p3: air to perspex, incidence 50, refraction 30, find n
record("refractive-index-p3", math.sin(rad(50)) / math.sin(rad(30)), "")

# p4: water (1.33) to glass (1.52), angle in water 40 deg, find angle in glass
sin_p4 = 1.33 * math.sin(rad(40)) / 1.52
record("refractive-index-p4", deg(math.asin(sin_p4)), "°", f"sin = {sin_p4}")

# p5: speed in oil 2.10e8, air incidence 35 deg, find refraction angle (two steps)
n_p5 = c / 2.10e8
sin_p5 = math.sin(rad(35)) / n_p5
record("refractive-index-p5", deg(math.asin(sin_p5)), "°", f"n = {n_p5}, sin = {sin_p5}")

# p6: air incidence 60, refraction 35 in plastic; find speed in plastic (two steps)
n_p6 = math.sin(rad(60)) / math.sin(rad(35))
record("refractive-index-p6", c / n_p6, "m s⁻¹", f"n = {n_p6}")


# ---------------------------------------------------------------
# Type 5: critical-angle  (sin C = n2/n1)
# ---------------------------------------------------------------

# w: glass 1.50 to air
record("critical-angle-w", deg(math.asin(1 / 1.50)), "°", f"sin C = {1/1.50}")

# p1: water 1.33 to air
record("critical-angle-p1", deg(math.asin(1 / 1.33)), "°", f"sin C = {1/1.33}")

# p2: fibre core 1.48, cladding 1.46
record("critical-angle-p2", deg(math.asin(1.46 / 1.48)), "°", f"sin C = {1.46/1.48}")

# p3: cubic zirconia C = 27.8 deg, find n
record("critical-angle-p3", 1 / math.sin(rad(27.8)), "", f"sin C = {math.sin(rad(27.8))}")

# p4: core 1.52, C = 78.0 deg, find cladding index
record("critical-angle-p4", 1.52 * math.sin(rad(78.0)), "", f"sin C = {math.sin(rad(78.0))}")

# p5: speed in perspex 2.01e8, find C (two steps)
n_ca_p5 = c / 2.01e8
record("critical-angle-p5", deg(math.asin(1 / n_ca_p5)), "°", f"n = {n_ca_p5}, sin C = {1/n_ca_p5}")

# p6: air incidence 48, refraction 29, find C (two steps)
n_ca_p6 = math.sin(rad(48)) / math.sin(rad(29))
record("critical-angle-p6", deg(math.asin(1 / n_ca_p6)), "°", f"n = {n_ca_p6}, sin C = {1/n_ca_p6}")


# ---------------------------------------------------------------
# Type 6: double-slit  (lambda = ax/D)
# ---------------------------------------------------------------

# w: a = 0.50 mm, D = 2.0 m, lambda = 600 nm, find x in mm
record("double-slit-w", 600e-9 * 2.0 / 0.50e-3 * 1000, "mm")

# p1: a = 0.25 mm, D = 1.5 m, lambda = 520 nm, find x in mm
record("double-slit-p1", 520e-9 * 1.5 / 0.25e-3 * 1000, "mm")

# p2: a = 0.40 mm, D = 3.0 m, x = 4.8 mm, find lambda in nm
record("double-slit-p2", 0.40e-3 * 4.8e-3 / 3.0 * 1e9, "nm")

# p3: lambda = 589 nm, D = 2.5 m, x = 1.8 mm, find a in mm
record("double-slit-p3", 589e-9 * 2.5 / 1.8e-3 * 1000, "mm")

# p4: a = 0.30 mm, lambda = 450 nm, x = 2.7 mm, find D in m
record("double-slit-p4", 0.30e-3 * 2.7e-3 / 450e-9, "m")

# p5: 1st to 11th bright fringe = 22 mm -> x; a = 0.60 mm, D = 2.0 m; lambda in nm (two steps)
x_p5 = 22e-3 / 10
record("double-slit-p5", 0.60e-3 * x_p5 / 2.0 * 1e9, "nm", f"x = {x_p5}")

# p6: He-Ne f = 4.74e14 Hz -> lambda; a = 0.20 mm, D = 2.4 m; x in mm (two steps)
lambda_ds_p6 = c / 4.74e14
record("double-slit-p6", lambda_ds_p6 * 2.4 / 0.20e-3 * 1000, "mm", f"lambda = {lambda_ds_p6}")


# ---------------------------------------------------------------
# Type 7: diffraction-grating  (d sin theta = n lambda)
# ---------------------------------------------------------------

# w: 300 lines/mm, lambda 600 nm, 2nd order angle
d_w = 1e-3 / 300
sin_dg_w = 2 * 600e-9 / d_w
record("diffraction-grating-w", deg(math.asin(sin_dg_w)), "°", f"d = {d_w}, sin = {sin_dg_w}")

# p1: d = 2.0e-6 m, lambda 500 nm, 1st order angle
sin_dg_p1 = 500e-9 / 2.0e-6
record("diffraction-grating-p1", deg(math.asin(sin_dg_p1)), "°", f"sin = {sin_dg_p1}")

# p2: 500 lines/mm, 1st order at 18.0 deg, find lambda in nm
d_p2 = 1e-3 / 500
record("diffraction-grating-p2", d_p2 * math.sin(rad(18.0)) * 1e9, "nm", f"d = {d_p2}")

# p3: lambda 589 nm, 2nd order at 42.0 deg, find lines per mm
d_p3 = 2 * 589e-9 / math.sin(rad(42.0))
record("diffraction-grating-p3", 1e-3 / d_p3, "lines per mm", f"d = {d_p3}")

# p4: 600 lines/mm, lambda 650 nm, highest order visible
d_p4 = 1e-3 / 600
n_max_p4 = d_p4 / 650e-9
record("diffraction-grating-p4", math.floor(n_max_p4), "", f"d = {d_p4}, d/lambda = {n_max_p4}")

# p5: 600 lines/mm, angle between the two 1st-order beams 36.0 deg, find lambda in nm (two steps)
theta_p5 = 36.0 / 2
d_p5 = 1e-3 / 600
record("diffraction-grating-p5", d_p5 * math.sin(rad(theta_p5)) * 1e9, "nm", f"theta = {theta_p5}, d = {d_p5}")

# p6: f = 4.50e14 Hz -> lambda; 300 lines/mm; 1st order angle (two steps)
lambda_dg_p6 = c / 4.50e14
d_p6 = 1e-3 / 300
sin_dg_p6 = lambda_dg_p6 / d_p6
record("diffraction-grating-p6", deg(math.asin(sin_dg_p6)), "°", f"lambda = {lambda_dg_p6}, d = {d_p6}, sin = {sin_dg_p6}")


# ---------------------------------------------------------------
# Type 8: string-harmonics  (lambda = 2L/n, f_n = nv/2L, v = sqrt(T/mu))
# ---------------------------------------------------------------

# w: guitar string L = 0.65 m, v = 420 m/s, fundamental
record("string-harmonics-w", 420 / (2 * 0.65), "Hz")

# p1: rope L = 1.2 m, third harmonic wavelength
record("string-harmonics-p1", 2 * 1.2 / 3, "m")

# p2: cello string L = 0.90 m, v = 270 m/s, second harmonic
record("string-harmonics-p2", 2 * 270 / (2 * 0.90), "Hz")

# p3: violin string L = 32.5 cm, f1 = 196 Hz, find v
record("string-harmonics-p3", 2 * 0.325 * 196, "m s⁻¹")

# p4: steel cable T = 80 N, mu = 2.0 g/m, find v  [AQA, WJEC]
mu_p4 = 2.0e-3
record("string-harmonics-p4", math.sqrt(80 / mu_p4), "m s⁻¹", f"mu = {mu_p4}")

# p5: piano wire T = 72 N, mu = 1.25e-3 kg/m, L = 0.60 m, fundamental (two steps)  [AQA, WJEC]
v_sh_p5 = math.sqrt(72 / 1.25e-3)
record("string-harmonics-p5", v_sh_p5 / (2 * 0.60), "Hz", f"v = {v_sh_p5}")

# p6: Melde's: f = 50 Hz, L = 1.2 m, 3 loops, find v (two steps)
lambda_sh_p6 = 2 * 1.2 / 3
record("string-harmonics-p6", 50 * lambda_sh_p6, "m s⁻¹", f"lambda = {lambda_sh_p6}")


# ---------------------------------------------------------------
# Type 9: pipe-harmonics
# ---------------------------------------------------------------

# w: open organ pipe L = 0.85 m, v = 340, fundamental
lambda_pipe_w = 2 * 0.85
record("pipe-harmonics-w", 340 / lambda_pipe_w, "Hz", f"lambda = {lambda_pipe_w}")

# p1: closed bottle L = 0.25 m, v = 340, fundamental
lambda_pipe_p1 = 4 * 0.25
record("pipe-harmonics-p1", 340 / lambda_pipe_p1, "Hz", f"lambda = {lambda_pipe_p1}")

# p2: open flute L = 0.60 m, v = 330, second harmonic
record("pipe-harmonics-p2", 2 * 330 / (2 * 0.60), "Hz")

# p3: closed clarinet-like pipe, f1 = 256 Hz, v = 340, find L in cm
L_p3 = 340 / (4 * 256)
record("pipe-harmonics-p3", L_p3 * 100, "cm", f"L = {L_p3}")

# p4: closed pan pipe L = 45 cm, v = 343, third harmonic
record("pipe-harmonics-p4", 3 * 343 / (4 * 0.45), "Hz")

# p5: resonance tube, f = 512 Hz, L = 16.6 cm, find v (two steps)
lambda_pipe_p5 = 4 * 0.166
record("pipe-harmonics-p5", 512 * lambda_pipe_p5, "m s⁻¹", f"lambda = {lambda_pipe_p5}")

# p6: closed pipe fifth harmonic at 850 Hz, v = 340, find L (two steps)
lambda_pipe_p6 = 340 / 850
record("pipe-harmonics-p6", 5 * lambda_pipe_p6 / 4, "m", f"lambda = {lambda_pipe_p6}")


# ---------------------------------------------------------------
# Type 10: doppler  (df/f = v/c, dlambda/lambda = v/c)
# ---------------------------------------------------------------

# w: H-alpha 656.3 nm observed at 658.5 nm, find v
dlambda_w = 658.5 - 656.3
record("doppler-w", dlambda_w / 656.3 * c, "m s⁻¹", f"dlambda = {dlambda_w}")

# p1: satellite 1.5 GHz at 7500 m/s, find df in Hz
record("doppler-p1", 7500 / c * 1.5e9, "Hz")

# p2: star receding at 6.0e4 m/s, lambda 500 nm, find dlambda in nm
record("doppler-p2", 6.0e4 / c * 500, "nm")

# p3: radar 10.5 GHz, shift 1.75 kHz, find v
record("doppler-p3", 1.75e3 / 10.5e9 * c, "m s⁻¹")

# p4: Ca K line 393.4 nm observed 393.8 nm, find v in km/s
dlambda_p4 = 393.8 - 393.4
record("doppler-p4", dlambda_p4 / 393.4 * c / 1000, "km s⁻¹", f"dlambda = {dlambda_p4}")

# p5: galaxy receding at 1.5e7 m/s, emitted 486.1 nm, find observed wavelength in nm (two steps)
dlambda_p5 = 1.5e7 / c * 486.1
# The emitted wavelength is given to 4 s.f., so the observed wavelength is kept to 4 s.f.
record("doppler-p5", 486.1 + dlambda_p5, "nm", f"dlambda = {dlambda_p5}", sf=4)

# p6: 21.1 cm line, galaxy receding at 4.5e6 m/s, find df in MHz (two steps)
f_dop_p6 = c / 0.211
record("doppler-p6", 4.5e6 / c * f_dop_p6 / 1e6, "MHz", f"f = {f_dop_p6}")


# ---------------------------------------------------------------
# Print
# ---------------------------------------------------------------

for question_id, rounded, unit, raw, notes in results:
    print(f"{question_id:26s} {rounded!r:>14}  {unit:14s} (raw {raw!r}) {notes}")
