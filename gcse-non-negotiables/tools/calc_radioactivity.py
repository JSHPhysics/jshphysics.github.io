#!/usr/bin/env python3
"""Compute every answer and every plotted coordinate for data/radioactivity.json.

Usage:
    python3 tools/calc_radioactivity.py            # print answers only
    python3 tools/calc_radioactivity.py --write    # also write data/radioactivity.json

Every answer.value in the topic file comes from this script. The decay
graphs are sampled exponentials computed here, and each graph answer is
computed from the same function, so the curve and the answer agree.
"""

import json
import math
import os
import sys


def tidy(value):
    """Round to 3 s.f., and store an integer when the value is a whole number."""
    if value == 0:
        return 0
    # Whole numbers are stored exactly as integers (e.g. 17190, 2100)
    if abs(value - round(value)) < 1e-9:
        return int(round(value))
    # Otherwise round to three significant figures
    magnitude = math.floor(math.log10(abs(value)))
    decimals = 2 - magnitude
    rounded = round(value, decimals)
    # A rounded value that became whole is still stored as an integer
    if abs(rounded - round(rounded)) < 1e-9:
        return int(round(rounded))
    return rounded


def half_lives_between(start, finish):
    """Count how many halvings take start down to finish (must be exact)."""
    count = 0
    current = start
    while current > finish + 1e-9:
        current = current / 2
        count = count + 1
    # Guard against data that is not an exact power-of-two ratio
    if abs(current - finish) > 1e-9:
        raise ValueError(f"{start} does not halve exactly to {finish}")
    return count


def remaining_after(start, number_of_half_lives):
    """Halve a starting value the given number of times."""
    current = start
    for _ in range(number_of_half_lives):
        current = current / 2
    return current


def activity(initial, half_life, time, background=0):
    """Exponential decay A(t) = A₀ × 0.5^(t / T½), plus any constant background."""
    return background + initial * (0.5 ** (time / half_life))


def sample_decay(initial, half_life, t_min, t_max, dt, background=0):
    """Sample the decay curve every dt from t_min to t_max, rounding tidily."""
    count = int(round((t_max - t_min) / dt))
    points = []
    for index in range(count + 1):
        t = t_min + index * dt
        a = activity(initial, half_life, t, background)
        t_clean = round(t, 4)
        a_clean = round(a, 2)
        if t_clean == int(t_clean):
            t_clean = int(t_clean)
        if a_clean == int(a_clean):
            a_clean = int(a_clean)
        points.append([t_clean, a_clean])
    return points


answers = {}


def record(question_id, value):
    """Store a tidy answer and print it."""
    answers[question_id] = tidy(value)
    print(f"{question_id:26s} {answers[question_id]}")


# ----------------------------------------------------------------------
# Type 1: nuclear notation
# ----------------------------------------------------------------------

# Worked: carbon-14, neutrons
record("nuclear-notation-w", 14 - 6)

# p1: sodium-23, protons = atomic number
record("nuclear-notation-p1", 11)

# p2: uranium-238, nucleons = mass number
record("nuclear-notation-p2", 238)

# p3: iodine-131, neutrons
record("nuclear-notation-p3", 131 - 53)

# p4: cobalt with 27 protons and 33 neutrons, mass number
record("nuclear-notation-p4", 27 + 33)

# p5: chlorine-37 vs chlorine-35 (atomic number 17), extra neutrons
neutrons_cl37 = 37 - 17
neutrons_cl35 = 35 - 17
record("nuclear-notation-p5", neutrons_cl37 - neutrons_cl35)

# p6: lead-206, neutrons minus protons
neutrons_pb206 = 206 - 82
record("nuclear-notation-p6", neutrons_pb206 - 82)

# ----------------------------------------------------------------------
# Type 2: balancing nuclear equations
# ----------------------------------------------------------------------

ALPHA_MASS = 4
ALPHA_CHARGE = 2
BETA_CHARGE = -1

# Worked: radium-226 alpha → radon, mass number
record("nuclear-equations-w", 226 - ALPHA_MASS)

# p1: uranium-238 (92) alpha → thorium, atomic number
record("nuclear-equations-p1", 92 - ALPHA_CHARGE)

# p2: carbon-14 (6) beta-minus → nitrogen, atomic number
record("nuclear-equations-p2", 6 - BETA_CHARGE)

# p3: polonium-210 alpha → lead, mass number
record("nuclear-equations-p3", 210 - ALPHA_MASS)

# p4: strontium-90 (38) beta-minus → yttrium, atomic number
record("nuclear-equations-p4", 38 - BETA_CHARGE)

# p5: thorium-232 (90): alpha then beta-minus, atomic number (two-step)
after_alpha = 90 - ALPHA_CHARGE
after_beta = after_alpha - BETA_CHARGE
record("nuclear-equations-p5", after_beta)

# p6: uranium-238 → radon-222, number of alpha particles (two-step)
mass_lost = 238 - 222
record("nuclear-equations-p6", mass_lost / ALPHA_MASS)

# ----------------------------------------------------------------------
# Type 3: half-life, fraction and activity remaining
# ----------------------------------------------------------------------

# Worked: 800 Bq, half-life 2 h, after 6 h
n_w = 6 / 2
record("half-life-fraction-w", remaining_after(800, int(n_w)))

# p1: fraction after 2 half-lives
record("half-life-fraction-p1", remaining_after(1, 2))

# p2: 1200 Bq after 2 half-lives
record("half-life-fraction-p2", remaining_after(1200, 2))

# p3: 640 counts/min, half-life 8 days, after 24 days
n_p3 = 24 / 8
record("half-life-fraction-p3", remaining_after(640, int(n_p3)))

# p4: technetium-99m, half-life 6 h, after 1 day, fraction
n_p4 = 24 / 6
record("half-life-fraction-p4", remaining_after(1, int(n_p4)))

# p5: 3200 Bq, half-life 20 min, after 2 h (two-step: convert then count)
n_p5 = (2 * 60) / 20
record("half-life-fraction-p5", remaining_after(3200, int(n_p5)))

# p6: 2400 nuclei, half-life 55 s, after 165 s, how many have decayed (two-step)
n_p6 = 165 / 55
left_p6 = remaining_after(2400, int(n_p6))
record("half-life-fraction-p6", 2400 - left_p6)

# ----------------------------------------------------------------------
# Type 4: half-life, counting half-lives and finding times
# ----------------------------------------------------------------------

# Worked: 1600 → 200 Bq, half-life 4 h, time
n_hw = half_lives_between(1600, 200)
record("half-life-time-w", n_hw * 4)

# p1: 800 → 50 Bq, number of half-lives
record("half-life-time-p1", half_lives_between(800, 50))

# p2: 6000 → 750 counts/s, half-life 30 min, time
record("half-life-time-p2", half_lives_between(6000, 750) * 30)

# p3: 400 → 50 Bq in 36 min, half-life
record("half-life-time-p3", 36 / half_lives_between(400, 50))

# p4: 2400 → 300 counts/min in 2 h, half-life in minutes
record("half-life-time-p4", (2 * 60) / half_lives_between(2400, 300))

# p5: carbon-14, 1/8 remaining, half-life 5730 years, age (two-step)
n_p5_hl = half_lives_between(1, 1 / 8)
record("half-life-time-p5", n_p5_hl * 5730)

# p6: 1920 → 120 counts/s in 1 min 20 s, half-life in s (two-step)
time_p6_s = 60 + 20
record("half-life-time-p6", time_p6_s / half_lives_between(1920, 120))

# ----------------------------------------------------------------------
# Type 5: count rate with background (Higher)
# ----------------------------------------------------------------------

# Worked: measured 540, background 40, half-life 10 min, corrected after 20 min
corrected_w = 540 - 40
record("background-count-w", remaining_after(corrected_w, int(20 / 10)))

# p1: measured 275, background 25, corrected
record("background-count-p1", 275 - 25)

# p2: measured 650, background 50, half-life 15 min, detector reading after 15 min
corrected_p2 = 650 - 50
record("background-count-p2", remaining_after(corrected_p2, 1) + 50)

# p3: measured 1300 → 180, background 20, number of half-lives
record("background-count-p3", half_lives_between(1300 - 20, 180 - 20))

# p4: measured 820 → 120 in 30 min, background 20, half-life
record("background-count-p4", 30 / half_lives_between(820 - 20, 120 - 20))

# p5: background 180 counts per hour, measured 243 counts/min, half-life 5 min, corrected after 20 min
background_p5_per_min = 180 / 60
corrected_p5 = 243 - background_p5_per_min
record("background-count-p5", remaining_after(corrected_p5, int(20 / 5)))

# p6: measured 1030, background 30, half-life 8 days, time until detector reads 155
record("background-count-p6", half_lives_between(1030 - 30, 155 - 30) * 8)

# ----------------------------------------------------------------------
# Type 6: reading a decay graph (sampled exponentials)
# ----------------------------------------------------------------------

graphs = {}

# Worked: A₀ = 800 Bq, T½ = 20 s, 0–100 s; half-life
graphs["decay-graph-w"] = sample_decay(800, 20, 0, 100, 5)
half_w = activity(800, 20, 20)
assert abs(half_w - 400) < 1e-9
record("decay-graph-w", 20)

# p1: count rate 1200 counts/min, T½ = 15 min, 0–90 min; half-life
graphs["decay-graph-p1"] = sample_decay(1200, 15, 0, 90, 5)
assert abs(activity(1200, 15, 15) - 600) < 1e-9
record("decay-graph-p1", 15)

# p2: A₀ = 800 Bq, T½ = 30 s, 0–120 s; activity at X (t = 60 s)
graphs["decay-graph-p2"] = sample_decay(800, 30, 0, 120, 6)
record("decay-graph-p2", activity(800, 30, 60))

# p3: A₀ = 400 Bq, T½ = 10 min, 0–40 min; number of half-lives in 40 min
graphs["decay-graph-p3"] = sample_decay(400, 10, 0, 40, 2)
assert abs(activity(400, 10, 10) - 200) < 1e-9
record("decay-graph-p3", 40 / 10)

# p4: count rate 3200 counts/s, T½ = 4 h, 0–24 h; time to fall to 400 counts/s
graphs["decay-graph-p4"] = sample_decay(3200, 4, 0, 24, 1.5)
n_p4_graph = half_lives_between(3200, 400)
record("decay-graph-p4", n_p4_graph * 4)
assert abs(activity(3200, 4, 12) - 400) < 1e-9

# p5: A₀ = 6400 Bq, T½ = 10 min, 0–40 min; half-life from graph then activity at 60 min (two-step)
graphs["decay-graph-p5"] = sample_decay(6400, 10, 0, 40, 2.5)
assert abs(activity(6400, 10, 10) - 3200) < 1e-9
record("decay-graph-p5", activity(6400, 10, 60))

# p6 (Higher): measured count rate = 100 background + 800 × 0.5^(t/10), 0–60 min; half-life
graphs["decay-graph-p6"] = sample_decay(800, 10, 0, 60, 2.5, background=100)
assert abs(activity(800, 10, 0, 100) - 900) < 1e-9
assert abs(activity(800, 10, 10, 100) - 500) < 1e-9
record("decay-graph-p6", 10)

print()
print("Points per graph:", {key: len(value) for key, value in graphs.items()})
print("Check points on the curves:")
print("  worked  A(20) =", activity(800, 20, 20))
print("  p1      A(15) =", activity(1200, 15, 15))
print("  p2      A(60) =", activity(800, 30, 60))
print("  p3      A(10) =", activity(400, 10, 10))
print("  p4      A(12) =", activity(3200, 4, 12))
print("  p5      A(10) =", activity(6400, 10, 10), " A(60) =", activity(6400, 10, 60))
print("  p6      A(0) =", activity(800, 10, 0, 100), " A(10) =", activity(800, 10, 10, 100))


# ----------------------------------------------------------------------
# The topic file itself. Every answer.value below is answers[id].
# ----------------------------------------------------------------------

def ans(question_id, unit):
    """Build an answer object from the computed value."""
    return {"value": answers[question_id], "unit": unit}


BOTH = ["Foundation", "Higher"]
HIGHER = ["Higher"]

topic = {
    "id": "radioactivity",
    "title": "Radioactivity",
    "subtitle": "Half-life, activity, nuclear equations and decay graphs",
    "order": 60,
    "figure": "nuclear-particles",
    "types": [
        {
            "id": "nuclear-notation",
            "name": "Protons, neutrons and nucleons from a nuclide",
            "equations": ["mass number = number of protons + number of neutrons", "number of neutrons = mass number − atomic number"],
            "boards": BOTH,
            "method": "The atomic number (the lower number in the symbol) is the number of protons. The mass number (the upper number) is the total number of nucleons, protons plus neutrons. So neutrons = mass number − atomic number. Isotopes of an element have the same atomic number but different mass numbers, so they differ only in the number of neutrons.",
            "commonErrors": [
                "Giving the mass number as the number of neutrons",
                "Subtracting the wrong way round, or adding the two numbers",
                "Thinking isotopes have different numbers of protons: it is the number of neutrons that changes"
            ],
            "worked": {
                "id": "nuclear-notation-w",
                "question": "A nucleus of carbon-14 has mass number 14 and atomic number 6. How many neutrons does the nucleus contain?",
                "steps": [
                    "Known: mass number = 14, atomic number = 6. Unknown: number of neutrons.",
                    "number of neutrons = mass number − atomic number",
                    "number of neutrons = 14 − 6",
                    "number of neutrons = 8"
                ],
                "answer": ans("nuclear-notation-w", "")
            },
            "practice": [
                {
                    "id": "nuclear-notation-p1",
                    "question": "A nucleus of sodium-23 has mass number 23 and atomic number 11. How many protons does the nucleus contain?",
                    "hint": "The atomic number is the number of protons.",
                    "walkthrough": [
                        "Atomic number = 11.",
                        "The atomic number is the number of protons.",
                        "number of protons = 11"
                    ],
                    "answer": ans("nuclear-notation-p1", "")
                },
                {
                    "id": "nuclear-notation-p2",
                    "question": "A nucleus of uranium-238 has mass number 238 and atomic number 92. How many nucleons does the nucleus contain?",
                    "hint": "Nucleons means protons and neutrons together, which is the mass number.",
                    "walkthrough": [
                        "Mass number = 238.",
                        "The mass number is the total number of protons and neutrons (nucleons).",
                        "number of nucleons = 238"
                    ],
                    "answer": ans("nuclear-notation-p2", "")
                },
                {
                    "id": "nuclear-notation-p3",
                    "question": "Iodine-131 is used in medicine. Its nucleus has mass number 131 and atomic number 53. How many neutrons does the nucleus contain?",
                    "hint": "Neutrons = mass number − atomic number.",
                    "walkthrough": [
                        "mass number = 131, atomic number = 53",
                        "number of neutrons = 131 − 53",
                        "number of neutrons = 78"
                    ],
                    "answer": ans("nuclear-notation-p3", "")
                },
                {
                    "id": "nuclear-notation-p4",
                    "question": "A nucleus of cobalt contains 27 protons and 33 neutrons. What is the mass number of this nucleus?",
                    "hint": "Mass number = protons + neutrons.",
                    "walkthrough": [
                        "protons = 27, neutrons = 33",
                        "mass number = 27 + 33",
                        "mass number = 60"
                    ],
                    "answer": ans("nuclear-notation-p4", "")
                },
                {
                    "id": "nuclear-notation-p5",
                    "question": "Chlorine has atomic number 17 and two common isotopes, chlorine-35 (mass number 35) and chlorine-37 (mass number 37). How many more neutrons does a chlorine-37 nucleus have than a chlorine-35 nucleus?",
                    "hint": "Work out the neutrons in each isotope (mass number − 17), then subtract.",
                    "walkthrough": [
                        "chlorine-37: neutrons = 37 − 17 = 20",
                        "chlorine-35: neutrons = 35 − 17 = 18",
                        "difference = 20 − 18",
                        "difference = 2"
                    ],
                    "answer": ans("nuclear-notation-p5", "")
                },
                {
                    "id": "nuclear-notation-p6",
                    "question": "A nucleus of lead-206 has mass number 206 and atomic number 82. How many more neutrons than protons does the nucleus contain?",
                    "hint": "Find the number of neutrons first (206 − 82), then compare it with the number of protons.",
                    "walkthrough": [
                        "protons = atomic number = 82",
                        "neutrons = 206 − 82 = 124",
                        "difference = 124 − 82",
                        "difference = 42"
                    ],
                    "answer": ans("nuclear-notation-p6", "")
                }
            ]
        },
        {
            "id": "nuclear-equations",
            "name": "Balancing nuclear equations",
            "equations": ["alpha decay: mass number − 4, atomic number − 2", "beta-minus decay: mass number unchanged, atomic number + 1"],
            "boards": BOTH,
            "method": "The mass numbers must add up to the same total on both sides of a nuclear equation, and so must the atomic numbers. An alpha particle is a helium nucleus (mass number 4, atomic number 2), so the daughter nucleus has a mass number 4 lower and an atomic number 2 lower. A beta-minus particle is an electron (mass number 0, atomic number −1), so the mass number stays the same and the atomic number goes up by 1.",
            "commonErrors": [
                "Taking 2 off the mass number in alpha decay instead of 4",
                "Lowering the atomic number by 1 in beta-minus decay instead of raising it by 1",
                "Changing the mass number in beta decay: the electron has mass number 0"
            ],
            "worked": {
                "id": "nuclear-equations-w",
                "question": "Radium-226 (mass number 226, atomic number 88) decays by emitting an alpha particle to form a nucleus of radon. What is the mass number of the radon nucleus?",
                "steps": [
                    "Known: parent mass number 226, alpha particle mass number 4. Unknown: daughter mass number.",
                    "Mass numbers balance: 226 = (daughter mass number) + 4",
                    "daughter mass number = 226 − 4",
                    "mass number of radon = 222"
                ],
                "answer": ans("nuclear-equations-w", "")
            },
            "practice": [
                {
                    "id": "nuclear-equations-p1",
                    "question": "Uranium-238 (mass number 238, atomic number 92) decays by emitting an alpha particle to form a nucleus of thorium. What is the atomic number of the thorium nucleus?",
                    "hint": "An alpha particle carries away 2 protons, so the atomic number falls by 2.",
                    "walkthrough": [
                        "Atomic numbers balance: 92 = (thorium atomic number) + 2",
                        "thorium atomic number = 92 − 2",
                        "atomic number = 90"
                    ],
                    "answer": ans("nuclear-equations-p1", "")
                },
                {
                    "id": "nuclear-equations-p2",
                    "question": "Carbon-14 (mass number 14, atomic number 6) decays by emitting a beta-minus particle to form a nucleus of nitrogen. What is the atomic number of the nitrogen nucleus?",
                    "hint": "A beta-minus particle has atomic number −1, so the daughter's atomic number must be 1 higher to balance.",
                    "walkthrough": [
                        "Atomic numbers balance: 6 = (nitrogen atomic number) + (−1)",
                        "nitrogen atomic number = 6 + 1",
                        "atomic number = 7"
                    ],
                    "answer": ans("nuclear-equations-p2", "")
                },
                {
                    "id": "nuclear-equations-p3",
                    "question": "Polonium-210 (mass number 210, atomic number 84) decays by emitting an alpha particle to form a nucleus of lead. What is the mass number of the lead nucleus?",
                    "hint": "The alpha particle takes away 4 nucleons.",
                    "walkthrough": [
                        "Mass numbers balance: 210 = (lead mass number) + 4",
                        "lead mass number = 210 − 4",
                        "mass number = 206"
                    ],
                    "answer": ans("nuclear-equations-p3", "")
                },
                {
                    "id": "nuclear-equations-p4",
                    "question": "Strontium-90 (mass number 90, atomic number 38) decays by emitting a beta-minus particle to form a nucleus of yttrium. What is the atomic number of the yttrium nucleus?",
                    "hint": "In beta-minus decay a neutron becomes a proton, so the atomic number goes up by 1.",
                    "walkthrough": [
                        "Atomic numbers balance: 38 = (yttrium atomic number) + (−1)",
                        "yttrium atomic number = 38 + 1",
                        "atomic number = 39"
                    ],
                    "answer": ans("nuclear-equations-p4", "")
                },
                {
                    "id": "nuclear-equations-p5",
                    "question": "Thorium-232 (mass number 232, atomic number 90) emits an alpha particle. The nucleus formed then emits a beta-minus particle. What is the atomic number of the nucleus after both decays?",
                    "hint": "Do the decays one at a time: alpha takes 2 off the atomic number, then beta-minus adds 1.",
                    "walkthrough": [
                        "after the alpha decay: atomic number = 90 − 2 = 88",
                        "after the beta-minus decay: atomic number = 88 + 1",
                        "atomic number = 89"
                    ],
                    "answer": ans("nuclear-equations-p5", "")
                },
                {
                    "id": "nuclear-equations-p6",
                    "question": "Uranium-238 (mass number 238, atomic number 92) decays through a series of alpha and beta-minus decays to radon-222 (mass number 222, atomic number 86). How many alpha particles are emitted in this series?",
                    "hint": "Only alpha decays change the mass number, by 4 each time; compare the two mass numbers.",
                    "walkthrough": [
                        "Beta-minus decays do not change the mass number.",
                        "change in mass number = 238 − 222 = 16",
                        "number of alpha particles = 16 / 4",
                        "number of alpha particles = 4"
                    ],
                    "answer": ans("nuclear-equations-p6", ""),
                    "boards": HIGHER
                }
            ]
        },
        {
            "id": "half-life-fraction",
            "name": "Half-life: fraction and activity remaining",
            "equations": ["number of half-lives = time / half-life", "fraction remaining after n half-lives = 1 / 2ⁿ"],
            "boards": BOTH,
            "method": "Each half-life halves what is left. Work out how many half-lives fit in the time (time ÷ half-life, in matching units), then halve the starting activity, count rate or number of nuclei that many times. Give a fraction as a decimal (1/4 = 0.25) unless the question asks for an activity or a count rate.",
            "commonErrors": [
                "Dividing by the number of half-lives (÷ 3) instead of halving three times (÷ 8)",
                "Counting the half-lives with the time in the wrong unit (hours against minutes)",
                "Giving the amount that has decayed when the question asks for the amount remaining, or the other way round"
            ],
            "worked": {
                "id": "half-life-fraction-w",
                "question": "A radioactive source has an activity of 800 Bq. Its half-life is 2 hours. Calculate the activity of the source after 6 hours.",
                "steps": [
                    "Known: starting activity 800 Bq, half-life 2 h, time 6 h. Unknown: activity after 6 h.",
                    "number of half-lives = 6 / 2 = 3",
                    "800 → 400 → 200 → 100",
                    "activity = 100 Bq"
                ],
                "answer": ans("half-life-fraction-w", "Bq")
            },
            "practice": [
                {
                    "id": "half-life-fraction-p1",
                    "question": "What fraction of the radioactive nuclei in a sample remain undecayed after 2 half-lives? Give your answer as a decimal.",
                    "hint": "Halve 1 twice.",
                    "walkthrough": [
                        "After 1 half-life, 1/2 remains.",
                        "After 2 half-lives, 1/2 × 1/2 = 1/4 remains.",
                        "fraction = 0.25"
                    ],
                    "answer": ans("half-life-fraction-p1", "")
                },
                {
                    "id": "half-life-fraction-p2",
                    "question": "A source in a school laboratory has an activity of 1200 Bq. Calculate its activity after 2 half-lives.",
                    "hint": "Halve 1200 twice.",
                    "walkthrough": [
                        "1200 → 600 after 1 half-life",
                        "600 → 300 after 2 half-lives",
                        "activity = 300 Bq"
                    ],
                    "answer": ans("half-life-fraction-p2", "Bq")
                },
                {
                    "id": "half-life-fraction-p3",
                    "question": "Iodine-131 has a half-life of 8 days. A sample gives a count rate of 640 counts/min. Calculate the count rate from the sample after 24 days.",
                    "hint": "Find the number of half-lives (24 ÷ 8) first, then halve 640 that many times.",
                    "walkthrough": [
                        "number of half-lives = 24 / 8 = 3",
                        "640 → 320 → 160 → 80",
                        "count rate = 80 counts/min"
                    ],
                    "answer": ans("half-life-fraction-p3", "counts/min")
                },
                {
                    "id": "half-life-fraction-p4",
                    "question": "Technetium-99m, used in medical imaging, has a half-life of 6 hours. What fraction of the technetium-99m injected into a patient remains after 1 day? Give your answer as a decimal.",
                    "hint": "Change 1 day into hours before counting the half-lives.",
                    "walkthrough": [
                        "1 day = 24 hours, so number of half-lives = 24 / 6 = 4",
                        "1 → 1/2 → 1/4 → 1/8 → 1/16",
                        "fraction = 1/16 = 0.0625"
                    ],
                    "answer": ans("half-life-fraction-p4", "")
                },
                {
                    "id": "half-life-fraction-p5",
                    "question": "A radioactive gas has a half-life of 20 minutes. A sample of the gas has an activity of 3200 Bq. Calculate the activity of the sample after 2 hours.",
                    "hint": "Change 2 hours into minutes, divide by 20 to count the half-lives, then halve 3200 that many times.",
                    "walkthrough": [
                        "2 hours = 120 minutes",
                        "number of half-lives = 120 / 20 = 6",
                        "3200 → 1600 → 800 → 400 → 200 → 100 → 50",
                        "activity = 50 Bq"
                    ],
                    "answer": ans("half-life-fraction-p5", "Bq")
                },
                {
                    "id": "half-life-fraction-p6",
                    "question": "A sample contains 2400 undecayed nuclei of a radon isotope with a half-life of 55 s. How many of these nuclei have decayed after 165 s?",
                    "hint": "Find how many remain after 165 ÷ 55 half-lives, then subtract from 2400.",
                    "walkthrough": [
                        "number of half-lives = 165 / 55 = 3",
                        "remaining: 2400 → 1200 → 600 → 300",
                        "decayed = 2400 − 300",
                        "decayed = 2100 nuclei"
                    ],
                    "answer": ans("half-life-fraction-p6", "")
                }
            ]
        },
        {
            "id": "half-life-time",
            "name": "Half-life: counting half-lives and finding times",
            "equations": ["number of half-lives = how many times the activity halves", "time taken = number of half-lives × half-life", "half-life = time taken / number of half-lives"],
            "boards": BOTH,
            "method": "Halve the starting value again and again until you reach the final value, and count the halvings: that is the number of half-lives. Multiply by the half-life to get the time taken, or divide the time taken by the number of half-lives to find the half-life itself. Keep the units consistent: a half-life in minutes gives a time in minutes.",
            "commonErrors": [
                "Dividing the start by the finish and calling that the number of half-lives (1600 / 200 = 8 means 3 half-lives, not 8)",
                "Mixing hours and minutes between the half-life and the time taken",
                "Counting the starting value as the first half-life"
            ],
            "worked": {
                "id": "half-life-time-w",
                "question": "The activity of a source falls from 1600 Bq to 200 Bq. The half-life of the source is 4 hours. Calculate the time this takes.",
                "steps": [
                    "Known: 1600 Bq falls to 200 Bq, half-life 4 h. Unknown: time taken.",
                    "1600 → 800 → 400 → 200, so 3 half-lives",
                    "time = 3 × 4",
                    "time = 12 hours"
                ],
                "answer": ans("half-life-time-w", "hours")
            },
            "practice": [
                {
                    "id": "half-life-time-p1",
                    "question": "The activity of a radioactive source falls from 800 Bq to 50 Bq. How many half-lives have passed?",
                    "hint": "Keep halving 800 until you reach 50 and count the halvings.",
                    "walkthrough": [
                        "800 → 400 → 200 → 100 → 50",
                        "That is 4 halvings.",
                        "number of half-lives = 4"
                    ],
                    "answer": ans("half-life-time-p1", "")
                },
                {
                    "id": "half-life-time-p2",
                    "question": "A source used in a hospital has a half-life of 30 minutes. Its count rate falls from 6000 counts/s to 750 counts/s. Calculate the time this takes.",
                    "hint": "Count the halvings from 6000 to 750, then multiply by 30 minutes.",
                    "walkthrough": [
                        "6000 → 3000 → 1500 → 750, so 3 half-lives",
                        "time = 3 × 30",
                        "time = 90 minutes"
                    ],
                    "answer": ans("half-life-time-p2", "minutes")
                },
                {
                    "id": "half-life-time-p3",
                    "question": "The activity of a source falls from 400 Bq to 50 Bq in 36 minutes. Calculate the half-life of the source.",
                    "hint": "Count the halvings, then divide 36 minutes by that number.",
                    "walkthrough": [
                        "400 → 200 → 100 → 50, so 3 half-lives in 36 minutes",
                        "half-life = 36 / 3",
                        "half-life = 12 minutes"
                    ],
                    "answer": ans("half-life-time-p3", "minutes")
                },
                {
                    "id": "half-life-time-p4",
                    "question": "The count rate from a sample falls from 2400 counts/min to 300 counts/min in 2 hours. Calculate the half-life of the sample in minutes.",
                    "hint": "Change 2 hours into minutes, count the halvings, then divide.",
                    "walkthrough": [
                        "2400 → 1200 → 600 → 300, so 3 half-lives",
                        "2 hours = 120 minutes",
                        "half-life = 120 / 3",
                        "half-life = 40 minutes"
                    ],
                    "answer": ans("half-life-time-p4", "minutes")
                },
                {
                    "id": "half-life-time-p5",
                    "question": "Carbon-14 has a half-life of 5730 years. A bone found at a dig contains one eighth of the carbon-14 it had when the animal died. Calculate the age of the bone.",
                    "hint": "How many halvings take 1 down to 1/8? Multiply that by 5730 years.",
                    "walkthrough": [
                        "1 → 1/2 → 1/4 → 1/8, so 3 half-lives",
                        "age = 3 × 5730",
                        "age = 17 190 years"
                    ],
                    "answer": ans("half-life-time-p5", "years")
                },
                {
                    "id": "half-life-time-p6",
                    "question": "A detector reading from a short-lived source falls from 1920 counts/s to 120 counts/s in 1 minute 20 seconds. Calculate the half-life of the source in seconds.",
                    "hint": "Change 1 minute 20 seconds into seconds, count the halvings from 1920 to 120, then divide.",
                    "walkthrough": [
                        "1920 → 960 → 480 → 240 → 120, so 4 half-lives",
                        "1 minute 20 seconds = 80 s",
                        "half-life = 80 / 4",
                        "half-life = 20 s"
                    ],
                    "answer": ans("half-life-time-p6", "s")
                }
            ]
        },
        {
            "id": "background-count",
            "name": "Count rate with background",
            "equations": ["corrected count rate = measured count rate − background count rate"],
            "boards": HIGHER,
            "method": "A detector always records some background radiation, so subtract the background count rate from every reading before using half-life ideas; the corrected count rate is what the source alone gives. Then halve, count half-lives or find a time exactly as before. If the question asks what the detector will read, add the background back on at the end.",
            "commonErrors": [
                "Halving the measured count rate without taking the background off first",
                "Subtracting the background from the starting reading but not from the final one",
                "Forgetting to add the background back on when the question asks what the detector reads",
                "Background given per hour while the readings are per minute: convert it first"
            ],
            "worked": {
                "id": "background-count-w",
                "question": "With a source in front of it, a detector reads 540 counts/min. The background count rate is 40 counts/min. The half-life of the source is 10 minutes. Calculate the corrected count rate from the source after 20 minutes.",
                "steps": [
                    "Known: measured 540 counts/min, background 40 counts/min, half-life 10 min, time 20 min.",
                    "corrected count rate now = 540 − 40 = 500 counts/min",
                    "number of half-lives = 20 / 10 = 2",
                    "500 → 250 → 125",
                    "corrected count rate = 125 counts/min"
                ],
                "answer": ans("background-count-w", "counts/min")
            },
            "practice": [
                {
                    "id": "background-count-p1",
                    "question": "A Geiger counter placed near a rock sample reads 275 counts/min. With the rock removed it reads 25 counts/min. Calculate the corrected count rate from the rock.",
                    "hint": "The reading with the rock removed is the background; subtract it.",
                    "walkthrough": [
                        "measured = 275 counts/min, background = 25 counts/min",
                        "corrected = 275 − 25",
                        "corrected count rate = 250 counts/min"
                    ],
                    "answer": ans("background-count-p1", "counts/min")
                },
                {
                    "id": "background-count-p2",
                    "question": "A detector near a source reads 650 counts/min. The background count rate is 50 counts/min and the half-life of the source is 15 minutes. What will the detector read after 15 minutes?",
                    "hint": "Take the background off, halve once, then add the background back on because the question asks for the detector reading.",
                    "walkthrough": [
                        "corrected now = 650 − 50 = 600 counts/min",
                        "after 1 half-life: 600 / 2 = 300 counts/min from the source",
                        "detector reading = 300 + 50",
                        "reading = 350 counts/min"
                    ],
                    "answer": ans("background-count-p2", "counts/min")
                },
                {
                    "id": "background-count-p3",
                    "question": "The reading on a detector near a source falls from 1300 counts/min to 180 counts/min. The background count rate is 20 counts/min. How many half-lives have passed?",
                    "hint": "Subtract 20 from both readings before counting the halvings.",
                    "walkthrough": [
                        "corrected start = 1300 − 20 = 1280 counts/min",
                        "corrected finish = 180 − 20 = 160 counts/min",
                        "1280 → 640 → 320 → 160",
                        "number of half-lives = 3"
                    ],
                    "answer": ans("background-count-p3", "")
                },
                {
                    "id": "background-count-p4",
                    "question": "The reading on a detector near a source falls from 820 counts/min to 120 counts/min in 30 minutes. The background count rate is 20 counts/min. Calculate the half-life of the source.",
                    "hint": "Correct both readings for background, count the halvings, then divide 30 minutes by that number.",
                    "walkthrough": [
                        "corrected start = 820 − 20 = 800 counts/min",
                        "corrected finish = 120 − 20 = 100 counts/min",
                        "800 → 400 → 200 → 100, so 3 half-lives in 30 minutes",
                        "half-life = 30 / 3 = 10 minutes"
                    ],
                    "answer": ans("background-count-p4", "minutes")
                },
                {
                    "id": "background-count-p5",
                    "question": "Before an experiment a student records 180 background counts in one hour. With a source present the detector reads 243 counts/min. The half-life of the source is 5 minutes. Calculate the corrected count rate from the source after 20 minutes.",
                    "hint": "Change the background into counts per minute first, subtract it, then halve for 20 ÷ 5 half-lives.",
                    "walkthrough": [
                        "background = 180 / 60 = 3 counts/min",
                        "corrected now = 243 − 3 = 240 counts/min",
                        "number of half-lives = 20 / 5 = 4",
                        "240 → 120 → 60 → 30 → 15",
                        "corrected count rate = 15 counts/min"
                    ],
                    "answer": ans("background-count-p5", "counts/min")
                },
                {
                    "id": "background-count-p6",
                    "question": "A detector near a source reads 1030 counts/min. The background count rate is 30 counts/min and the half-life of the source is 8 days. Calculate how long it takes for the detector reading to fall to 155 counts/min.",
                    "hint": "Correct both the starting and the final reading for background, count the halvings, then multiply by 8 days.",
                    "walkthrough": [
                        "corrected start = 1030 − 30 = 1000 counts/min",
                        "corrected finish = 155 − 30 = 125 counts/min",
                        "1000 → 500 → 250 → 125, so 3 half-lives",
                        "time = 3 × 8 = 24 days"
                    ],
                    "answer": ans("background-count-p6", "days")
                }
            ]
        },
        {
            "id": "decay-graph",
            "name": "Reading a decay graph",
            "equations": ["half-life = time for the activity to halve", "number of half-lives = time / half-life"],
            "boards": BOTH,
            "method": "Find the starting activity (or count rate) where the curve meets the vertical axis, halve it, and read across to the curve and down to the time axis: that time is the half-life. Check it by halving again, which should take the same time. If there is a background line, measure the count rates from the background line, not from zero.",
            "commonErrors": [
                "Reading the time when the activity reaches zero instead of the time to reach half of the starting value",
                "Halving the time axis instead of the activity axis",
                "Ignoring the background count rate line on a count-rate graph",
                "Taking the end of the graph as the end of the decay: the curve never actually reaches zero"
            ],
            "worked": {
                "id": "decay-graph-w",
                "question": "The graph shows how the activity of a radioactive source changes with time. The dashed lines show the reading at half of the starting activity. Use the graph to find the half-life of the source.",
                "steps": [
                    "Starting activity (at t = 0) = 800 Bq.",
                    "Half of this is 400 Bq.",
                    "Reading across at 400 Bq and down to the time axis gives 20 s.",
                    "half-life = 20 s"
                ],
                "answer": ans("decay-graph-w", "s"),
                "graph": {
                    "x": {"label": "time in s", "min": 0, "max": 100, "step": 10},
                    "y": {"label": "activity in Bq", "min": 0, "max": 800, "step": 100},
                    "series": [
                        {"kind": "curve", "points": graphs["decay-graph-w"]},
                        {"kind": "dashed", "points": [[0, 400], [20, 400], [20, 0]]}
                    ],
                    "alt": "Activity–time graph falling from 800 Bq at 0 s to 400 Bq at 20 s, with dashed lines marking that reading, and on to 25 Bq at 100 s"
                }
            },
            "practice": [
                {
                    "id": "decay-graph-p1",
                    "question": "The graph shows the count rate from a radioactive sample against time. Use the graph to find the half-life of the sample.",
                    "hint": "Read the count rate at t = 0, halve it, and find the time when the curve reaches that value.",
                    "walkthrough": [
                        "Starting count rate = 1200 counts/minute.",
                        "Half of this is 600 counts/minute.",
                        "The curve reaches 600 counts/minute at 15 minutes.",
                        "half-life = 15 minutes"
                    ],
                    "answer": ans("decay-graph-p1", "minutes"),
                    "graph": {
                        "x": {"label": "time in minutes", "min": 0, "max": 90, "step": 15},
                        "y": {"label": "count rate in counts/minute", "min": 0, "max": 1200, "step": 200},
                        "series": [{"kind": "curve", "points": graphs["decay-graph-p1"]}],
                        "alt": "Count rate–time graph falling from 1200 counts per minute at 0 minutes to 600 at 15 minutes and on towards 19 at 90 minutes"
                    }
                },
                {
                    "id": "decay-graph-p2",
                    "question": "The graph shows the activity of a source against time. Point X marks the activity 60 s after the start. Use the graph to find the activity at X.",
                    "hint": "Go up from 60 s on the time axis to the curve, then read across to the activity axis.",
                    "walkthrough": [
                        "X is at t = 60 s on the curve.",
                        "Reading across from X to the activity axis gives 200 Bq.",
                        "activity = 200 Bq"
                    ],
                    "answer": ans("decay-graph-p2", "Bq"),
                    "graph": {
                        "x": {"label": "time in s", "min": 0, "max": 120, "step": 15},
                        "y": {"label": "activity in Bq", "min": 0, "max": 800, "step": 100},
                        "series": [{"kind": "curve", "points": graphs["decay-graph-p2"]}],
                        "marks": [{"x": 60, "y": 200, "label": "X"}],
                        "alt": "Activity–time graph falling from 800 Bq at 0 s to 200 Bq at the marked point X at 60 s, and on to 50 Bq at 120 s"
                    }
                },
                {
                    "id": "decay-graph-p3",
                    "question": "The graph shows the activity of a radioactive source against time. Use the graph to find how many half-lives occur in the first 40 minutes.",
                    "hint": "Find the half-life from the graph first (the time for 400 Bq to fall to 200 Bq), then divide 40 minutes by it.",
                    "walkthrough": [
                        "Starting activity = 400 Bq; half of this is 200 Bq.",
                        "The curve reaches 200 Bq at 10 minutes, so the half-life is 10 minutes.",
                        "number of half-lives in 40 minutes = 40 / 10",
                        "number of half-lives = 4"
                    ],
                    "answer": ans("decay-graph-p3", ""),
                    "graph": {
                        "x": {"label": "time in minutes", "min": 0, "max": 40, "step": 5},
                        "y": {"label": "activity in Bq", "min": 0, "max": 400, "step": 50},
                        "series": [{"kind": "curve", "points": graphs["decay-graph-p3"]}],
                        "alt": "Activity–time graph falling from 400 Bq at 0 minutes to 200 Bq at 10 minutes and 25 Bq at 40 minutes"
                    }
                },
                {
                    "id": "decay-graph-p4",
                    "question": "The graph shows the count rate from a sample of a radioactive isotope against time. Use the graph to find how long it takes for the count rate to fall to 400 counts/s.",
                    "hint": "Read across from 400 counts/s to the curve, then down to the time axis.",
                    "walkthrough": [
                        "Starting count rate = 3200 counts/s.",
                        "3200 → 1600 → 800 → 400 is 3 half-lives, and the curve shows each halving takes 4 hours.",
                        "The curve reaches 400 counts/s at 12 hours.",
                        "time = 12 hours"
                    ],
                    "answer": ans("decay-graph-p4", "hours"),
                    "graph": {
                        "x": {"label": "time in hours", "min": 0, "max": 24, "step": 2},
                        "y": {"label": "count rate in counts/s", "min": 0, "max": 3200, "step": 400},
                        "series": [{"kind": "curve", "points": graphs["decay-graph-p4"]}],
                        "alt": "Count rate–time graph falling from 3200 counts per second at 0 hours to 1600 at 4 hours, 400 at 12 hours and 50 at 24 hours"
                    }
                },
                {
                    "id": "decay-graph-p5",
                    "question": "The graph shows the activity of a radioactive source during the first 40 minutes after it is prepared. Use the graph to find the half-life, then calculate the activity of the source 60 minutes after it is prepared.",
                    "hint": "Find the time for 6400 Bq to halve to 3200 Bq, work out how many of those half-lives fit in 60 minutes, then halve 6400 that many times.",
                    "walkthrough": [
                        "Starting activity = 6400 Bq; the curve reaches 3200 Bq at 10 minutes, so the half-life is 10 minutes.",
                        "number of half-lives in 60 minutes = 60 / 10 = 6",
                        "6400 → 3200 → 1600 → 800 → 400 → 200 → 100",
                        "activity = 100 Bq"
                    ],
                    "answer": ans("decay-graph-p5", "Bq"),
                    "graph": {
                        "x": {"label": "time in minutes", "min": 0, "max": 40, "step": 5},
                        "y": {"label": "activity in Bq", "min": 0, "max": 6400, "step": 800},
                        "series": [{"kind": "curve", "points": graphs["decay-graph-p5"]}],
                        "alt": "Activity–time graph falling from 6400 Bq at 0 minutes to 3200 Bq at 10 minutes and 400 Bq at 40 minutes"
                    }
                },
                {
                    "id": "decay-graph-p6",
                    "question": "The graph shows the reading on a detector placed near a radioactive source. The dashed line shows the background count rate, which was measured before the source was brought in. Use the graph to find the half-life of the source.",
                    "hint": "Subtract the background (100 counts/minute) from the starting reading, halve what is left, add the background back on, and find the time when the curve reaches that reading.",
                    "walkthrough": [
                        "At t = 0 the detector reads 900 counts/minute; background = 100 counts/minute.",
                        "Count rate from the source alone = 900 − 100 = 800 counts/minute.",
                        "After one half-life the source gives 400 counts/minute, so the detector reads 400 + 100 = 500 counts/minute.",
                        "The curve reaches 500 counts/minute at 10 minutes.",
                        "half-life = 10 minutes"
                    ],
                    "answer": ans("decay-graph-p6", "minutes"),
                    "boards": HIGHER,
                    "graph": {
                        "x": {"label": "time in minutes", "min": 0, "max": 60, "step": 10},
                        "y": {"label": "count rate in counts/minute", "min": 0, "max": 1000, "step": 100},
                        "series": [
                            {"kind": "curve", "points": graphs["decay-graph-p6"]},
                            {"kind": "dashed", "points": [[0, 100], [60, 100]]}
                        ],
                        "labels": [{"x": 46, "y": 55, "text": "background"}],
                        "alt": "Detector count rate against time falling from 900 counts per minute at 0 minutes to 500 at 10 minutes and levelling towards the dashed background line at 100 counts per minute"
                    }
                }
            ]
        }
    ]
}


def write_topic():
    """Write data/radioactivity.json next to this script's project root."""
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    out_path = os.path.join(root, "data", "radioactivity.json")
    with open(out_path, "w", encoding="utf-8") as handle:
        json.dump(topic, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
    print(f"wrote {out_path}")


if __name__ == "__main__":
    if "--write" in sys.argv:
        write_topic()
