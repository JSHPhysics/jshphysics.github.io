#!/usr/bin/env python3
"""Compute every answer and every plotted coordinate for the graph type
"astro-graph" in data/astrophysics.json.

Run: python3 tools/calc_astrophysics_graph.py [out.json]

Prints each answer rounded to 3 s.f. with its question id. If an output
path is given, writes the complete type object (with graphs) there so it
can be appended to the topic file.
"""

import json
import math
import sys

# Standard constants from SCHEMA.md
c = 3.00e8              # m s^-1
h = 6.63e-34            # J s
k_B = 1.38e-23          # J K^-1
WIEN = 2.90e-3          # m K

# Conversions quoted in the questions that need them
MPC_IN_M = 3.09e22      # m
YEAR_IN_S = 3.16e7      # s

results = []


def round_sf(value, sf=3):
    """Round a value to the given number of significant figures."""
    if value == 0:
        return 0.0
    magnitude = math.floor(math.log10(abs(value)))
    places = sf - 1 - magnitude
    rounded = round(value, places)
    # Large round numbers are stored as integers so the validator does not
    # mistake 9360000.0 for an unrounded float. Beyond 10^15 an int would
    # pick up binary noise, so those stay as floats (repr 1.01e+27 is fine).
    if places <= 0 and abs(rounded) < 1e15:
        rounded = int(rounded)
    return rounded


def record(question_id, value, unit):
    """Store one answer, rounded to 3 s.f."""
    results.append((question_id, round_sf(value), unit, value))
    return round_sf(value)


def tidy(value, places=4):
    """Round a plotted coordinate so the JSON stays readable."""
    rounded = round(value, places)
    if rounded == int(rounded):
        return int(rounded)
    return rounded


def sample(function, x_values):
    """Sample a function at the given x values; returns [x, y] pairs."""
    points = []
    for x in x_values:
        points.append([tidy(x), tidy(function(x))])
    return points


def frange(start, stop, step):
    """Inclusive range of floats."""
    values = []
    count = int(round((stop - start) / step))
    for index in range(count + 1):
        values.append(start + index * step)
    return values


def scattered_data(x_values, function, fractional_offsets):
    """Plotted 'measurements': the true line value nudged by a few per cent."""
    points = []
    for x, offset in zip(x_values, fractional_offsets):
        points.append([tidy(x), tidy(function(x) * (1 + offset), 2)])
    return points


# ---------------------------------------------------------------
# Worked example: H0 from the gradient of v against d
# ---------------------------------------------------------------
# Best-fit line v = 70 d, with v plotted in 10^3 km s^-1 and d in Mpc.
# The line passes through (0, 0) and (500 Mpc, 35 × 10^3 km s^-1).
H0_w = 70.0             # km s^-1 Mpc^-1


def v_plotted_w(d):
    return H0_w * d / 1000.0


data_w = scattered_data(
    [60, 120, 180, 240, 300, 360, 420, 480],
    v_plotted_w,
    [0.06, -0.05, 0.03, -0.07, 0.02, 0.05, -0.04, -0.02])
fit_w = [[0, 0], [500, tidy(v_plotted_w(500))]]
assert fit_w[1][1] == 35
gradient_w = (35.0 * 1000 - 0) / (500 - 0)
answer_w = record("astro-graph-w", gradient_w, "km s⁻¹ Mpc⁻¹")

# ---------------------------------------------------------------
# p1: luminosity from a marked point on an intensity–distance curve
# ---------------------------------------------------------------
# I = L / (4π d²). With d in 10^16 m and I in 10^-8 W m^-2 the curve is
# I = 80 / d² in plotted units, so X = (4.0, 5.0) sits on gridlines.
K_p1 = 80.0


def intensity_p1(d):
    return K_p1 / d ** 2


points_p1 = sample(intensity_p1, frange(2, 10, 0.5))
d_X = 4.0e16            # m
I_X = intensity_p1(4.0) * 1e-8
assert abs(intensity_p1(4.0) - 5.0) < 1e-9
L_p1 = 4 * math.pi * d_X ** 2 * I_X
answer_p1 = record("astro-graph-p1", L_p1, "W")

# ---------------------------------------------------------------
# p2: redshift from a shifted spectral line
# ---------------------------------------------------------------
LAB_p2 = 500.0          # nm
OBS_p2 = 520.0          # nm
z_p2 = (OBS_p2 - LAB_p2) / LAB_p2
answer_p2 = record("astro-graph-p2", z_p2, "")

# ---------------------------------------------------------------
# p3: peak wavelength from a black-body curve, then Wien's law
# ---------------------------------------------------------------
# T = 5800 K gives λ_max = 2.90 × 10^-3 / 5800 = 500 nm exactly.
T_p3 = 5800.0


def planck(wavelength_m, temperature):
    """Spectral radiance (unnormalised) of a black body."""
    if wavelength_m <= 0:
        return 0.0
    exponent = h * c / (wavelength_m * k_B * temperature)
    return (1.0 / wavelength_m ** 5) / (math.exp(exponent) - 1)


peak_value = planck(500e-9, T_p3)


def relative_intensity_p3(wavelength_nm):
    return planck(wavelength_nm * 1e-9, T_p3) / peak_value


wavelengths_p3 = [0, 100, 200, 250, 300, 350, 400, 450, 500, 550,
                  600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]
points_p3 = sample(relative_intensity_p3, wavelengths_p3)
lambda_max_p3 = WIEN / T_p3
assert abs(lambda_max_p3 - 500e-9) < 1e-15
answer_p3 = record("astro-graph-p3", WIEN / 500e-9, "K")

# ---------------------------------------------------------------
# p4: luminosity of the Sun from the gradient of I against 1 / d²
# ---------------------------------------------------------------
# I = (L / 4π)(1 / d²): gradient = L / 4π. Plotted: x in 10^-23 m^-2,
# I in W m^-2. Line through (0, 0) and (4.0, 1200) → gradient 3.0 × 10^25 W.
GRADIENT_p4 = 3.0e25    # W


def intensity_p4(x_plotted):
    return GRADIENT_p4 * x_plotted * 1e-23


data_p4 = scattered_data(
    [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5],
    intensity_p4,
    [0.04, -0.03, 0.02, -0.04, 0.03, -0.02, 0.01])
fit_p4 = [[0, 0], [4, tidy(intensity_p4(4))]]
assert fit_p4[1][1] == 1200
gradient_p4 = (1200 - 0) / (4.0e-23 - 0)
L_p4 = 4 * math.pi * gradient_p4
answer_p4 = record("astro-graph-p4", L_p4, "W")

# ---------------------------------------------------------------
# p5: redshift from shifted lines, then recession velocity (two-step)
# ---------------------------------------------------------------
LAB_p5 = 650.0          # nm
OBS_p5 = 675.0          # nm
z_p5 = (OBS_p5 - LAB_p5) / LAB_p5
v_p5 = z_p5 * c
answer_p5 = record("astro-graph-p5", v_p5, "m s⁻¹")

# ---------------------------------------------------------------
# p6: H0 from a v–d graph, then the age of the universe (two-step)
# ---------------------------------------------------------------
# Best-fit line v = 75 d through (0, 0) and (400 Mpc, 30 × 10^3 km s^-1).
H0_p6 = 75.0            # km s^-1 Mpc^-1


def v_plotted_p6(d):
    return H0_p6 * d / 1000.0


data_p6 = scattered_data(
    [50, 100, 150, 200, 250, 300, 350],
    v_plotted_p6,
    [-0.06, 0.05, -0.03, 0.06, -0.04, 0.03, -0.02])
fit_p6 = [[0, 0], [400, tidy(v_plotted_p6(400))]]
assert fit_p6[1][1] == 30
gradient_p6 = (30.0 * 1000 - 0) / (400 - 0)          # km s^-1 Mpc^-1
H0_si_p6 = gradient_p6 * 1000 / MPC_IN_M              # s^-1
age_s_p6 = 1 / H0_si_p6
age_years_p6 = age_s_p6 / YEAR_IN_S
answer_p6 = record("astro-graph-p6", age_years_p6, "years")

# ---------------------------------------------------------------
# Print the answers
# ---------------------------------------------------------------
for question_id, rounded, unit, raw in results:
    print(f"{question_id:18s} {rounded!r:>14} {unit:14s} (raw {raw:.6g})")
print(f"(p6 intermediate: H0 = {H0_si_p6:.4g} s^-1, 1/H0 = {age_s_p6:.4g} s)")
print(f"(p4 intermediate: gradient = {gradient_p4:.4g} W)")

# ---------------------------------------------------------------
# The type object
# ---------------------------------------------------------------
BOARDS = ["AQA", "OCR A", "OCR B", "Edexcel", "WJEC"]

SPECTRUM_Y = {"label": "intensity / arbitrary units", "min": 0, "max": 1, "step": 0.2}

type_object = {
    "id": "astro-graph",
    "name": "Reading astrophysics graphs",
    "equations": [
        "v = H₀d: gradient of v against d is H₀",
        "age of universe ≈ 1 / H₀ (H₀ in s⁻¹)",
        "λ_max T = 2.90 × 10⁻³ m K",
        "L = 4πd²I",
        "z = Δλ / λ = v / c"
    ],
    "boards": BOARDS,
    "method": "Decide what the graph feature represents before you read anything: on v against d the gradient is H₀; on a black-body curve the peak gives λ_max for Wien's law; on an intensity–distance graph a marked point gives d and I for L = 4πd²I; on a spectrum the gap between the laboratory line and the observed line is Δλ. Read coordinates from gridline intersections, convert any scaled axis units (10³ km s⁻¹, nm, 10¹⁶ m) to SI where the equation needs it, then substitute.",
    "commonErrors": [
        "Reading an axis labelled v / 10³ km s⁻¹ and forgetting the factor of 10³",
        "Using the observed wavelength instead of the laboratory wavelength in the denominator of z = Δλ / λ",
        "Leaving λ_max in nm when using Wien's law",
        "Converting H₀ to s⁻¹ with 1 pc instead of 1 Mpc"
    ],
    "worked": {
        "id": "astro-graph-w",
        "question": "The graph shows the recession velocity v of eight galaxies plotted against their distance d from Earth, with a best-fit line drawn through the origin. Use the gradient of the best-fit line to determine the Hubble constant in km s⁻¹ Mpc⁻¹.",
        "steps": [
            "Known: v = H₀d, so the gradient of v against d is H₀. Read two points on the best-fit line, far apart: (0, 0) and (500 Mpc, 35 × 10³ km s⁻¹).",
            "The v axis is in units of 10³ km s⁻¹, so the second point is v = 35 000 km s⁻¹ at d = 500 Mpc.",
            "Gradient = (35 000 − 0) / (500 − 0) = 70 km s⁻¹ Mpc⁻¹",
            "H₀ = 70 km s⁻¹ Mpc⁻¹"
        ],
        "answer": {"value": answer_w, "unit": "km s⁻¹ Mpc⁻¹"},
        "graph": {
            "x": {"label": "d / Mpc", "min": 0, "max": 500, "step": 50},
            "y": {"label": "v / 10³ km s⁻¹", "min": 0, "max": 40, "step": 5},
            "series": [
                {"kind": "data", "points": data_w, "fit": fit_w}
            ],
            "alt": "Recession velocity against distance for eight galaxies scattered about a best-fit line through the origin that reaches 35 × 10³ km s⁻¹ at 500 Mpc"
        }
    },
    "practice": [
        {
            "id": "astro-graph-p1",
            "question": "The graph shows how the intensity I of radiation from a star varies with distance d from the star. Point X is marked. Use the coordinates of X to determine the luminosity of the star.",
            "hint": "Read d and I at X, convert both axis units (10¹⁶ m and 10⁻⁸ W m⁻²), then use L = 4πd²I.",
            "walkthrough": [
                "At X: d = 4.0 × 10¹⁶ m and I = 5.0 × 10⁻⁸ W m⁻².",
                "L = 4πd²I = 4π × (4.0 × 10¹⁶)² × 5.0 × 10⁻⁸",
                "L = 4π × 1.6 × 10³³ × 5.0 × 10⁻⁸ = 4π × 8.0 × 10²⁵",
                "L = 1.01 × 10²⁷ W"
            ],
            "answer": {"value": answer_p1, "unit": "W"},
            "graph": {
                "x": {"label": "d / 10¹⁶ m", "min": 0, "max": 10, "step": 1},
                "y": {"label": "I / 10⁻⁸ W m⁻²", "min": 0, "max": 20, "step": 5},
                "series": [
                    {"kind": "curve", "points": points_p1}
                ],
                "marks": [{"x": 4, "y": 5, "label": "X", "drop": True}],
                "alt": "Inverse-square curve of intensity against distance falling from 20 × 10⁻⁸ W m⁻² at 2 × 10¹⁶ m to 0.8 × 10⁻⁸ W m⁻² at 10 × 10¹⁶ m, with point X at 4 × 10¹⁶ m and 5 × 10⁻⁸ W m⁻²"
            }
        },
        {
            "id": "astro-graph-p2",
            "question": "The graph shows part of the spectrum of a distant galaxy. The dashed line marks the wavelength of a spectral line measured in the laboratory; the solid line marks the same spectral line observed in the galaxy's light. Use the graph to determine the redshift z of the galaxy.",
            "hint": "z = Δλ / λ, where λ is the laboratory wavelength and Δλ is the shift between the two lines.",
            "walkthrough": [
                "Laboratory wavelength λ = 500 nm; observed wavelength = 520 nm.",
                "Δλ = 520 − 500 = 20 nm",
                "z = Δλ / λ = 20 / 500",
                "z = 0.040"
            ],
            "answer": {"value": answer_p2, "unit": ""},
            "graph": {
                "x": {"label": "λ / nm", "min": 480, "max": 540, "step": 10},
                "y": SPECTRUM_Y,
                "series": [
                    {"kind": "dashed", "points": [[500, 0], [500, 1]]},
                    {"kind": "line", "points": [[520, 0], [520, 1]]}
                ],
                "labels": [
                    {"x": 498, "y": 0.93, "text": "laboratory", "anchor": "end"},
                    {"x": 522, "y": 0.93, "text": "observed"}
                ],
                "alt": "Wavelength axis from 480 nm to 540 nm with a dashed vertical line at the laboratory wavelength of 500 nm and a solid vertical line at the observed wavelength of 520 nm"
            }
        },
        {
            "id": "astro-graph-p3",
            "question": "The graph shows the black-body spectrum of a star: the relative intensity of its radiation plotted against wavelength λ. The peak of the curve is marked X. Use the graph and Wien's displacement law to determine the surface temperature of the star.",
            "hint": "Read λ_max at X, convert nm to m, then T = 2.90 × 10⁻³ / λ_max.",
            "walkthrough": [
                "The peak X is at λ_max = 500 nm = 5.00 × 10⁻⁷ m.",
                "λ_max T = 2.90 × 10⁻³ m K, so T = 2.90 × 10⁻³ / λ_max",
                "T = 2.90 × 10⁻³ / 5.00 × 10⁻⁷",
                "T = 5800 K"
            ],
            "answer": {"value": answer_p3, "unit": "K"},
            "graph": {
                "x": {"label": "λ / nm", "min": 0, "max": 1500, "step": 100},
                "y": {"label": "relative intensity", "min": 0, "max": 1, "step": 0.2},
                "series": [
                    {"kind": "curve", "points": points_p3}
                ],
                "marks": [{"x": 500, "y": 1, "label": "X", "drop": True, "dx": 10, "dy": 16}],
                "alt": "Black-body curve rising steeply from zero to a peak marked X at 500 nm and relative intensity 1.0, then falling gradually to about 0.2 at 1500 nm"
            }
        },
        {
            "id": "astro-graph-p4",
            "question": "A space probe travelling away from the Sun measures the intensity I of sunlight at several distances d. The graph shows I plotted against 1 / d² with a best-fit line through the origin. Use the gradient of the line to determine the luminosity of the Sun.",
            "hint": "I = L / (4πd²), so a graph of I against 1 / d² has gradient L / 4π; remember the x axis is in units of 10⁻²³ m⁻².",
            "walkthrough": [
                "I = (L / 4π) × (1 / d²), so gradient = L / 4π.",
                "Two points on the line: (0, 0) and (4.0 × 10⁻²³ m⁻², 1200 W m⁻²).",
                "Gradient = (1200 − 0) / (4.0 × 10⁻²³ − 0) = 3.0 × 10²⁵ W",
                "L = 4π × gradient = 4π × 3.0 × 10²⁵",
                "L = 3.77 × 10²⁶ W"
            ],
            "answer": {"value": answer_p4, "unit": "W"},
            "graph": {
                "x": {"label": "1 / d² / 10⁻²³ m⁻²", "min": 0, "max": 4, "step": 0.5},
                "y": {"label": "I / W m⁻²", "min": 0, "max": 1200, "step": 200},
                "series": [
                    {"kind": "data", "points": data_p4, "fit": fit_p4}
                ],
                "alt": "Intensity against 1 over distance squared for seven measurements scattered about a best-fit line through the origin that reaches 1200 W m⁻² at 4.0 × 10⁻²³ m⁻²"
            }
        },
        {
            "id": "astro-graph-p5",
            "question": "The graph shows a spectral line from a galaxy in a distant cluster. The dashed line is the laboratory wavelength of the line and the solid line is the wavelength observed in the galaxy's spectrum. Use the graph to determine the recession velocity of the galaxy.",
            "hint": "Find z = Δλ / λ from the two wavelengths first, then v = zc.",
            "walkthrough": [
                "Laboratory wavelength λ = 650 nm; observed wavelength = 675 nm, so Δλ = 25 nm.",
                "z = Δλ / λ = 25 / 650 = 0.0385",
                "v = zc = 0.0385 × 3.00 × 10⁸",
                "v = 1.15 × 10⁷ m s⁻¹"
            ],
            "answer": {"value": answer_p5, "unit": "m s⁻¹"},
            "graph": {
                "x": {"label": "λ / nm", "min": 640, "max": 690, "step": 5},
                "y": SPECTRUM_Y,
                "series": [
                    {"kind": "dashed", "points": [[650, 0], [650, 1]]},
                    {"kind": "line", "points": [[675, 0], [675, 1]]}
                ],
                "labels": [
                    {"x": 648, "y": 0.93, "text": "laboratory", "anchor": "end"},
                    {"x": 677, "y": 0.93, "text": "observed"}
                ],
                "alt": "Wavelength axis from 640 nm to 690 nm with a dashed vertical line at the laboratory wavelength of 650 nm and a solid vertical line at the observed wavelength of 675 nm"
            }
        },
        {
            "id": "astro-graph-p6",
            "question": "The graph shows recession velocity v against distance d for seven galaxies, with a best-fit line through the origin. Use the gradient of the line to find the Hubble constant and hence estimate the age of the universe in years. Take 1 Mpc = 3.09 × 10²² m and 1 year = 3.16 × 10⁷ s.",
            "hint": "Find H₀ in km s⁻¹ Mpc⁻¹ from the gradient, convert it to s⁻¹ (km → m, Mpc → m), then age = 1 / H₀ in seconds before converting to years.",
            "walkthrough": [
                "Points on the line: (0, 0) and (400 Mpc, 30 × 10³ km s⁻¹).",
                "H₀ = gradient = 30 000 / 400 = 75 km s⁻¹ Mpc⁻¹",
                "H₀ = 75 × 10³ / 3.09 × 10²² = 2.43 × 10⁻¹⁸ s⁻¹",
                "Age ≈ 1 / H₀ = 1 / 2.43 × 10⁻¹⁸ = 4.12 × 10¹⁷ s",
                "Age = 4.12 × 10¹⁷ / 3.16 × 10⁷ = 1.30 × 10¹⁰ years"
            ],
            "answer": {"value": answer_p6, "unit": "years"},
            "graph": {
                "x": {"label": "d / Mpc", "min": 0, "max": 400, "step": 50},
                "y": {"label": "v / 10³ km s⁻¹", "min": 0, "max": 30, "step": 5},
                "series": [
                    {"kind": "data", "points": data_p6, "fit": fit_p6}
                ],
                "alt": "Recession velocity against distance for seven galaxies scattered about a best-fit line through the origin that reaches 30 × 10³ km s⁻¹ at 400 Mpc"
            }
        }
    ]
}

if len(sys.argv) > 1:
    with open(sys.argv[1], "w", encoding="utf-8") as handle:
        json.dump(type_object, handle, ensure_ascii=False, indent=2)
    print(f"wrote {sys.argv[1]}")
