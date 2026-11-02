#!/usr/bin/env python3
"""Compute every answer and every plotted coordinate for data/waves.json.

Usage:
    python3 tools/calc_waves.py            # print answers only
    python3 tools/calc_waves.py --write    # also write data/waves.json

Every answer.value in the topic file comes from this script. The graph
questions sample their sinusoids here too, so the plotted crests and the
stored answers come from the same numbers.
"""

import json
import math
import os
import sys

# Standard constants from SCHEMA.md
SPEED_OF_LIGHT = 3e8

# Values given in the question text (not on the standard list)
SPEED_OF_SOUND_AIR = 340
SPEED_OF_SOUND_WATER = 1500
SPEED_OF_SOUND_TISSUE = 1540


def tidy(value):
    """Round to 3 s.f., and store an integer when the value is a whole number."""
    if value == 0:
        return 0
    # Whole numbers are stored exactly as integers (e.g. 2000, 1540)
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


def sample_sine(amplitude, wavelength, x_min, x_max, phase_cos, points_per_cycle=24):
    """Sample a sinusoid with its crests and zero crossings landing exactly on the grid.

    phase_cos = False gives y = A sin(2πx/λ)  (starts at zero, first crest at λ/4)
    phase_cos = True  gives y = A cos(2πx/λ)  (starts at a crest)
    Each cycle is split into points_per_cycle steps, so crests, troughs and
    zero crossings are sample points and not interpolated.
    """
    step = wavelength / points_per_cycle
    count = int(round((x_max - x_min) / step))
    points = []
    for index in range(count + 1):
        x = x_min + index * step
        angle = 2 * math.pi * (x - x_min) / wavelength
        if phase_cos:
            y = amplitude * math.cos(angle)
        else:
            y = amplitude * math.sin(angle)
        # Round so that tiny floating-point noise (1e-16) becomes a clean 0
        x_clean = round(x, 4)
        y_clean = round(y, 3)
        if y_clean == 0:
            y_clean = 0
        if x_clean == int(x_clean):
            x_clean = int(x_clean)
        if y_clean == int(y_clean):
            y_clean = int(y_clean)
        points.append([x_clean, y_clean])
    return points


def crest_positions(points):
    """Return the x positions of the crests (maximum y) in a sampled series."""
    peak = max(point[1] for point in points)
    crests = []
    for point in points:
        if abs(point[1] - peak) < 1e-9:
            crests.append(point[0])
    return crests


answers = {}


def record(question_id, value):
    """Store a tidy answer and print it."""
    answers[question_id] = tidy(value)
    print(f"{question_id:28s} {answers[question_id]}")


# ----------------------------------------------------------------------
# Type 1: wave speed from frequency and wavelength
# ----------------------------------------------------------------------

# Worked: loudspeaker, f = 250 Hz, λ = 1.36 m
record("wave-speed-frequency-w", 250 * 1.36)

# p1: ripple tank, f = 4 Hz, λ = 0.05 m
record("wave-speed-frequency-p1", 4 * 0.05)

# p2: sea waves, f = 0.2 Hz, λ = 40 m
record("wave-speed-frequency-p2", 0.2 * 40)

# p3: radio, f = 150 kHz, find λ
f_radio = 150 * 1000
record("wave-speed-frequency-p3", SPEED_OF_LIGHT / f_radio)

# p4: ultrasound, f = 2 MHz, λ = 0.77 mm
f_ultrasound = 2 * 1e6
lambda_ultrasound = 0.77 / 1000
record("wave-speed-frequency-p4", f_ultrasound * lambda_ultrasound)

# p5: 30 waves in 10 s, λ = 2.5 cm (two-step)
f_count = 30 / 10
lambda_count = 2.5 / 100
record("wave-speed-frequency-p5", f_count * lambda_count)

# p6: period 2 ms, v = 340 m/s, find λ (two-step)
period_sound = 2 / 1000
f_sound = 1 / period_sound
record("wave-speed-frequency-p6", SPEED_OF_SOUND_AIR / f_sound)

# ----------------------------------------------------------------------
# Type 2: wave speed from distance and time
# ----------------------------------------------------------------------

# Worked: swimming pool, 12 m in 8 s
record("wave-speed-distance-w", 12 / 8)

# p1: starting pistol, 1700 m in 5 s
record("wave-speed-distance-p1", 1700 / 5)

# p2: ripple tank, 0.9 m in 6 s
record("wave-speed-distance-p2", 0.9 / 6)

# p3: thunder 4 s after flash, find x
record("wave-speed-distance-p3", SPEED_OF_SOUND_AIR * 4)

# p4: P-wave 6000 m/s over 1500 km, find t
distance_pwave = 1500 * 1000
record("wave-speed-distance-p4", distance_pwave / 6000)

# p5: 1.7 km in 5 s, f = 200 Hz, find λ (two-step)
v_p5 = (1.7 * 1000) / 5
record("wave-speed-distance-p5", v_p5 / 200)

# p6: 30 m in 10 s, one crest every 4 s, find λ (two-step)
v_p6 = 30 / 10
f_p6 = 1 / 4
record("wave-speed-distance-p6", v_p6 / f_p6)

# ----------------------------------------------------------------------
# Type 3: period and frequency
# ----------------------------------------------------------------------

# Worked: 20 waves in 5 s, find period
f_worked = 20 / 5
record("period-frequency-w", 1 / f_worked)

# p1: 30 waves in 6 s, find f
record("period-frequency-p1", 30 / 6)

# p2: mains 50 Hz, find T
record("period-frequency-p2", 1 / 50)

# p3: T = 4 ms, find f
record("period-frequency-p3", 1 / (4 / 1000))

# p4: dolphin 20 kHz, find T in ms
period_dolphin_s = 1 / (20 * 1000)
record("period-frequency-p4", period_dolphin_s * 1000)

# p5: pendulum 25 swings in 20 s, find T (two-step)
f_pendulum = 25 / 20
record("period-frequency-p5", 1 / f_pendulum)

# p6: heart 72 beats per minute, find T (two-step)
f_heart = 72 / 60
record("period-frequency-p6", 1 / f_heart)

# ----------------------------------------------------------------------
# Type 4: echoes and ultrasound
# ----------------------------------------------------------------------

# Worked: sonar echo after 0.4 s in water
record("echoes-w", SPEED_OF_SOUND_WATER * 0.4 / 2)

# p1: cliff echo after 2 s
record("echoes-p1", SPEED_OF_SOUND_AIR * 2 / 2)

# p2: bat echo after 0.05 s
record("echoes-p2", SPEED_OF_SOUND_AIR * 0.05 / 2)

# p3: ultrasound echo after 0.2 ms in tissue, depth in cm
depth_p3_m = SPEED_OF_SOUND_TISSUE * (0.2 / 1000) / 2
record("echoes-p3", depth_p3_m * 100)

# p4: seabed 450 m deep, find echo time
record("echoes-p4", 2 * 450 / SPEED_OF_SOUND_WATER)

# p5: foetal head, echoes at 0.08 ms and 0.20 ms, width in cm (two-step)
near_m = SPEED_OF_SOUND_TISSUE * (0.08 / 1000) / 2
far_m = SPEED_OF_SOUND_TISSUE * (0.20 / 1000) / 2
record("echoes-p5", (far_m - near_m) * 100)

# p6: sonar 1.6 s then 0.9 s, how much shallower (two-step)
depth_first = SPEED_OF_SOUND_WATER * 1.6 / 2
depth_second = SPEED_OF_SOUND_WATER * 0.9 / 2
record("echoes-p6", depth_first - depth_second)

# ----------------------------------------------------------------------
# Type 5: reading wave graphs (sampled sinusoids)
# ----------------------------------------------------------------------

graphs = {}

# Worked: displacement–distance, A = 3 cm, λ = 4 m, 0–8 m, sine form
pts_w = sample_sine(3, 4, 0, 8, phase_cos=False)
crests_w = crest_positions(pts_w)
graphs["wave-graph-w"] = pts_w
record("wave-graph-w", crests_w[1] - crests_w[0])

# p1: displacement–time (loudspeaker cone), A = 2 mm, T = 4 ms, 0–8 ms, cosine form; amplitude
pts_p1 = sample_sine(2, 4, 0, 8, phase_cos=True)
graphs["wave-graph-p1"] = pts_p1
record("wave-graph-p1", max(point[1] for point in pts_p1))

# p2: displacement–distance (rope), A = 10 cm, λ = 8 m, 0–20 m, sine form; wavelength
pts_p2 = sample_sine(10, 8, 0, 20, phase_cos=False)
crests_p2 = crest_positions(pts_p2)
graphs["wave-graph-p2"] = pts_p2
record("wave-graph-p2", crests_p2[1] - crests_p2[0])

# p3: displacement–time (oscilloscope), A = 3 mm, T = 4 ms, 0–10 ms, sine form; frequency (two-step)
pts_p3 = sample_sine(3, 4, 0, 10, phase_cos=False)
crests_p3 = crest_positions(pts_p3)
graphs["wave-graph-p3"] = pts_p3
period_p3_ms = crests_p3[1] - crests_p3[0]
period_p3_s = period_p3_ms / 1000
record("wave-graph-p3", 1 / period_p3_s)

# p4: displacement–time (float on water), A = 4 cm, T = 0.4 s, 0–1 s, cosine form; frequency (two-step)
pts_p4 = sample_sine(4, 0.4, 0, 1, phase_cos=True)
crests_p4 = crest_positions(pts_p4)
graphs["wave-graph-p4"] = pts_p4
period_p4_s = crests_p4[1] - crests_p4[0]
record("wave-graph-p4", 1 / period_p4_s)

# p5: displacement–distance (ripple tank), A = 2 mm, λ = 20 cm, 0–40 cm, sine; f = 2.5 Hz; speed (two-step)
pts_p5 = sample_sine(2, 20, 0, 40, phase_cos=False)
crests_p5 = crest_positions(pts_p5)
graphs["wave-graph-p5"] = pts_p5
lambda_p5_cm = crests_p5[1] - crests_p5[0]
lambda_p5_m = lambda_p5_cm / 100
record("wave-graph-p5", 2.5 * lambda_p5_m)

# p6: displacement–distance (sound in air), A = 0.4 mm, λ = 1 m, 0–3 m, cosine; f = 340 Hz; speed (two-step)
pts_p6 = sample_sine(0.4, 1, 0, 3, phase_cos=True)
crests_p6 = crest_positions(pts_p6)
graphs["wave-graph-p6"] = pts_p6
lambda_p6_m = crests_p6[1] - crests_p6[0]
record("wave-graph-p6", 340 * lambda_p6_m)

print()
print("Crest positions used for the graph answers:")
print("  worked", crests_w)
print("  p2    ", crests_p2)
print("  p3    ", crests_p3)
print("  p4    ", crests_p4)
print("  p5    ", crests_p5)
print("  p6    ", crests_p6)
print("Points per graph:", {key: len(value) for key, value in graphs.items()})


# ----------------------------------------------------------------------
# The topic file itself. Every answer.value below is answers[id].
# ----------------------------------------------------------------------

def ans(question_id, unit):
    """Build an answer object from the computed value."""
    return {"value": answers[question_id], "unit": unit}


BOTH = ["Foundation", "Higher"]

topic = {
    "id": "waves",
    "title": "Waves",
    "subtitle": "The wave equation, wave speed, echoes and wave graphs",
    "order": 50,
    "figure": "waves",
    "types": [
        {
            "id": "wave-speed-frequency",
            "name": "Wave speed from frequency and wavelength",
            "equations": ["v = f × λ"],
            "boards": BOTH,
            "method": "Use this when you know any two of wave speed, frequency and wavelength. Wave speed equals frequency multiplied by wavelength: put the frequency in hertz and the wavelength in metres, and the speed comes out in m/s. If the speed is given, rearrange to f = v / λ or λ = v / f.",
            "commonErrors": [
                "Leaving the frequency in kHz or MHz instead of converting to Hz",
                "Leaving the wavelength in cm or mm instead of converting to metres",
                "Multiplying v by f when the question asks for a wavelength, instead of dividing",
                "Forgetting that radio waves and light travel at 3 × 10⁸ m/s"
            ],
            "worked": {
                "id": "wave-speed-frequency-w",
                "question": "A loudspeaker produces a sound wave of frequency 250 Hz. The wavelength of the sound in the air is 1.36 m. Calculate the speed of the sound.",
                "steps": [
                    "Known: f = 250 Hz, λ = 1.36 m. Unknown: v.",
                    "v = f × λ",
                    "v = 250 × 1.36",
                    "v = 340 m/s"
                ],
                "answer": ans("wave-speed-frequency-w", "m/s")
            },
            "practice": [
                {
                    "id": "wave-speed-frequency-p1",
                    "question": "In a ripple tank the dipper vibrates at 4 Hz and the waves it makes have a wavelength of 0.05 m. Calculate the speed of the water waves.",
                    "hint": "Wave speed = frequency × wavelength; both values are already in Hz and m.",
                    "walkthrough": [
                        "f = 4 Hz, λ = 0.05 m, find v.",
                        "v = f × λ = 4 × 0.05",
                        "v = 0.2 m/s"
                    ],
                    "answer": ans("wave-speed-frequency-p1", "m/s")
                },
                {
                    "id": "wave-speed-frequency-p2",
                    "question": "Waves on the sea pass a buoy with a frequency of 0.2 Hz. The distance from one crest to the next is 40 m. Calculate the speed of the waves.",
                    "hint": "The crest-to-crest distance is the wavelength; multiply it by the frequency.",
                    "walkthrough": [
                        "f = 0.2 Hz, λ = 40 m, find v.",
                        "v = f × λ = 0.2 × 40",
                        "v = 8 m/s"
                    ],
                    "answer": ans("wave-speed-frequency-p2", "m/s")
                },
                {
                    "id": "wave-speed-frequency-p3",
                    "question": "A radio station broadcasts at a frequency of 150 kHz. Radio waves travel at 3 × 10⁸ m/s. Calculate the wavelength of the radio waves.",
                    "hint": "Change 150 kHz into Hz (× 1000), then rearrange v = f × λ to λ = v / f.",
                    "walkthrough": [
                        "f = 150 kHz = 150 000 Hz, v = 3 × 10⁸ m/s, find λ.",
                        "v = f × λ → λ = v / f",
                        "λ = 300 000 000 / 150 000",
                        "λ = 2000 m"
                    ],
                    "answer": ans("wave-speed-frequency-p3", "m")
                },
                {
                    "id": "wave-speed-frequency-p4",
                    "question": "An ultrasound scanner sends waves of frequency 2 MHz into body tissue. In the tissue the waves have a wavelength of 0.77 mm. Calculate the speed of the ultrasound in the tissue.",
                    "hint": "Convert 2 MHz to 2 000 000 Hz and 0.77 mm to 0.00077 m before you multiply.",
                    "walkthrough": [
                        "f = 2 MHz = 2 000 000 Hz, λ = 0.77 mm = 0.00077 m, find v.",
                        "v = f × λ = 2 000 000 × 0.00077",
                        "v = 1540 m/s"
                    ],
                    "answer": ans("wave-speed-frequency-p4", "m/s")
                },
                {
                    "id": "wave-speed-frequency-p5",
                    "question": "A student counts 30 waves passing a point in a ripple tank in 10 s. The wavelength of the waves is 2.5 cm. Calculate the wave speed in m/s.",
                    "hint": "Find the frequency first (number of waves ÷ time), and change 2.5 cm into metres.",
                    "walkthrough": [
                        "f = 30 / 10 = 3 Hz",
                        "λ = 2.5 cm = 0.025 m",
                        "v = f × λ = 3 × 0.025",
                        "v = 0.075 m/s"
                    ],
                    "answer": ans("wave-speed-frequency-p5", "m/s")
                },
                {
                    "id": "wave-speed-frequency-p6",
                    "question": "A microphone connected to an oscilloscope shows that a sound wave has a period of 2 ms. The speed of sound in air is 340 m/s. Calculate the wavelength of the sound.",
                    "hint": "Frequency = 1 / period with the period in seconds; then λ = v / f.",
                    "walkthrough": [
                        "T = 2 ms = 0.002 s, so f = 1 / 0.002 = 500 Hz",
                        "v = f × λ → λ = v / f",
                        "λ = 340 / 500",
                        "λ = 0.68 m"
                    ],
                    "answer": ans("wave-speed-frequency-p6", "m")
                }
            ]
        },
        {
            "id": "wave-speed-distance",
            "name": "Wave speed from distance and time",
            "equations": ["v = x / t"],
            "boards": BOTH,
            "method": "Use this when a wave front or a pulse travels a measured distance in a measured time. Wave speed = distance travelled / time taken, the same speed equation as for a moving object. Change km to m and minutes to seconds first; rearrange to x = v × t for a distance or t = x / v for a time.",
            "commonErrors": [
                "Dividing the time by the distance",
                "Leaving a distance in km or cm when the speed is wanted in m/s",
                "Using the crest-to-crest distance (the wavelength) as the distance travelled"
            ],
            "worked": {
                "id": "wave-speed-distance-w",
                "question": "A water wave travels 12 m along a swimming pool in 8 s. Calculate the speed of the wave.",
                "steps": [
                    "Known: x = 12 m, t = 8 s. Unknown: v.",
                    "v = x / t",
                    "v = 12 / 8",
                    "v = 1.5 m/s"
                ],
                "answer": ans("wave-speed-distance-w", "m/s")
            },
            "practice": [
                {
                    "id": "wave-speed-distance-p1",
                    "question": "The sound of a starting pistol travels 1700 m across a lake in 5 s. Calculate the speed of the sound.",
                    "hint": "Speed = distance ÷ time; both values are already in m and s.",
                    "walkthrough": [
                        "x = 1700 m, t = 5 s, find v.",
                        "v = x / t = 1700 / 5",
                        "v = 340 m/s"
                    ],
                    "answer": ans("wave-speed-distance-p1", "m/s")
                },
                {
                    "id": "wave-speed-distance-p2",
                    "question": "In a ripple tank a wave front travels 0.9 m across the tank in 6 s. Calculate the speed of the wave front.",
                    "hint": "Speed = distance ÷ time; expect a small answer because water waves in a tank are slow.",
                    "walkthrough": [
                        "x = 0.9 m, t = 6 s, find v.",
                        "v = x / t = 0.9 / 6",
                        "v = 0.15 m/s"
                    ],
                    "answer": ans("wave-speed-distance-p2", "m/s")
                },
                {
                    "id": "wave-speed-distance-p3",
                    "question": "A lightning flash is seen and the thunder is heard 4 s later. The speed of sound in air is 340 m/s. Calculate how far away the lightning was.",
                    "hint": "The light arrives almost instantly, so the 4 s is the time the sound takes: x = v × t.",
                    "walkthrough": [
                        "v = 340 m/s, t = 4 s, find x.",
                        "v = x / t → x = v × t",
                        "x = 340 × 4",
                        "x = 1360 m"
                    ],
                    "answer": ans("wave-speed-distance-p3", "m")
                },
                {
                    "id": "wave-speed-distance-p4",
                    "question": "A P-wave from an earthquake travels through rock at 6000 m/s. Calculate the time it takes to reach a seismometer 1500 km away.",
                    "hint": "Change 1500 km into metres, then rearrange to t = x / v.",
                    "walkthrough": [
                        "x = 1500 km = 1 500 000 m, v = 6000 m/s, find t.",
                        "v = x / t → t = x / v",
                        "t = 1 500 000 / 6000",
                        "t = 250 s"
                    ],
                    "answer": ans("wave-speed-distance-p4", "s")
                },
                {
                    "id": "wave-speed-distance-p5",
                    "question": "A sound wave travels 1.7 km through air in 5 s. The frequency of the sound is 200 Hz. Calculate the wavelength of the sound.",
                    "hint": "Find the speed from distance ÷ time first (in m/s), then use λ = v / f.",
                    "walkthrough": [
                        "x = 1.7 km = 1700 m, t = 5 s",
                        "v = x / t = 1700 / 5 = 340 m/s",
                        "v = f × λ → λ = v / f = 340 / 200",
                        "λ = 1.7 m"
                    ],
                    "answer": ans("wave-speed-distance-p5", "m")
                },
                {
                    "id": "wave-speed-distance-p6",
                    "question": "Waves travel 30 m across a harbour in 10 s. One wave crest reaches the harbour wall every 4 s. Calculate the wavelength of the waves.",
                    "hint": "Speed = 30 / 10; the time between crests is the period, so f = 1 / 4; then λ = v / f.",
                    "walkthrough": [
                        "v = x / t = 30 / 10 = 3 m/s",
                        "T = 4 s, so f = 1 / 4 = 0.25 Hz",
                        "v = f × λ → λ = v / f = 3 / 0.25",
                        "λ = 12 m"
                    ],
                    "answer": ans("wave-speed-distance-p6", "m")
                }
            ]
        },
        {
            "id": "period-frequency",
            "name": "Period and frequency",
            "equations": ["f = number of waves / time taken", "T = 1 / f", "f = 1 / T"],
            "boards": BOTH,
            "method": "Frequency is the number of complete waves each second, so count the waves and divide by the time in seconds to get a value in hertz. Period is the time for one complete wave, and it equals 1 divided by the frequency. Change milliseconds to seconds, and anything per minute to per second, before you take 1 over it.",
            "commonErrors": [
                "Dividing the time by the number of waves when the question asks for frequency",
                "Forgetting that 1 ms = 0.001 s before working out 1 / T",
                "Treating beats per minute as a frequency in hertz without dividing by 60"
            ],
            "worked": {
                "id": "period-frequency-w",
                "question": "A student counts 20 complete waves passing a point in a ripple tank in 5 s. Calculate the period of the waves.",
                "steps": [
                    "Known: 20 waves in 5 s. Unknown: T.",
                    "f = number of waves / time = 20 / 5 = 4 Hz",
                    "T = 1 / f",
                    "T = 1 / 4",
                    "T = 0.25 s"
                ],
                "answer": ans("period-frequency-w", "s")
            },
            "practice": [
                {
                    "id": "period-frequency-p1",
                    "question": "A vibrating ruler clamped to a bench completes 30 vibrations in 6 s. Calculate the frequency of the vibrations.",
                    "hint": "Frequency = number of vibrations ÷ time in seconds.",
                    "walkthrough": [
                        "30 vibrations in 6 s, find f.",
                        "f = 30 / 6",
                        "f = 5 Hz"
                    ],
                    "answer": ans("period-frequency-p1", "Hz")
                },
                {
                    "id": "period-frequency-p2",
                    "question": "The UK mains electricity supply has a frequency of 50 Hz. Calculate the period of the mains supply.",
                    "hint": "Period = 1 / frequency.",
                    "walkthrough": [
                        "f = 50 Hz, find T.",
                        "T = 1 / f = 1 / 50",
                        "T = 0.02 s"
                    ],
                    "answer": ans("period-frequency-p2", "s")
                },
                {
                    "id": "period-frequency-p3",
                    "question": "An oscilloscope trace shows that a sound wave has a period of 4 ms. Calculate the frequency of the sound.",
                    "hint": "Change 4 ms into seconds first, then f = 1 / T.",
                    "walkthrough": [
                        "T = 4 ms = 0.004 s, find f.",
                        "f = 1 / T = 1 / 0.004",
                        "f = 250 Hz"
                    ],
                    "answer": ans("period-frequency-p3", "Hz")
                },
                {
                    "id": "period-frequency-p4",
                    "question": "A dolphin produces clicks with a frequency of 20 kHz. Calculate the period of the sound. Give your answer in ms.",
                    "hint": "Change 20 kHz into Hz, find T = 1 / f in seconds, then multiply by 1000 to get ms.",
                    "walkthrough": [
                        "f = 20 kHz = 20 000 Hz, find T.",
                        "T = 1 / f = 1 / 20 000 = 0.00005 s",
                        "0.00005 s × 1000 = 0.05 ms",
                        "T = 0.05 ms"
                    ],
                    "answer": ans("period-frequency-p4", "ms")
                },
                {
                    "id": "period-frequency-p5",
                    "question": "A pendulum completes 25 full swings in 20 s. Calculate the period of the pendulum.",
                    "hint": "Find the frequency from swings ÷ time first, then T = 1 / f.",
                    "walkthrough": [
                        "f = 25 / 20 = 1.25 Hz",
                        "T = 1 / f = 1 / 1.25",
                        "T = 0.8 s"
                    ],
                    "answer": ans("period-frequency-p5", "s")
                },
                {
                    "id": "period-frequency-p6",
                    "question": "A resting heart beats 72 times in one minute. Calculate the period of the heartbeat.",
                    "hint": "Change one minute into seconds to find the frequency in Hz, then T = 1 / f.",
                    "walkthrough": [
                        "f = 72 / 60 = 1.2 Hz",
                        "T = 1 / f = 1 / 1.2",
                        "T = 0.833 s"
                    ],
                    "answer": ans("period-frequency-p6", "s")
                }
            ]
        },
        {
            "id": "echoes",
            "name": "Echoes and ultrasound",
            "equations": ["x = v × t", "distance to the surface = v × t / 2"],
            "boards": BOTH,
            "method": "Use this when a sound or ultrasound pulse goes out, reflects from a surface and comes back. The time given is for the there-and-back journey, so the distance to the surface is half of speed × time. The speed of sound (340 m/s in air, 1500 m/s in water, 1540 m/s in body tissue) is given in the question. To find a time, double the distance first and then divide by the speed.",
            "commonErrors": [
                "Forgetting to halve: the pulse travels to the surface and back, so speed × time is twice the distance",
                "Using the speed of sound in air for a pulse travelling through water or body tissue",
                "Leaving a time in ms when the speed is in m/s"
            ],
            "worked": {
                "id": "echoes-w",
                "question": "A ship sends a sonar pulse towards the seabed and receives the echo 0.4 s later. The speed of sound in sea water is 1500 m/s. Calculate the depth of the sea below the ship.",
                "steps": [
                    "Known: v = 1500 m/s, t = 0.4 s for the round trip. Unknown: depth.",
                    "x = v × t = 1500 × 0.4 = 600 m (there and back)",
                    "depth = 600 / 2",
                    "depth = 300 m"
                ],
                "answer": ans("echoes-w", "m")
            },
            "practice": [
                {
                    "id": "echoes-p1",
                    "question": "A hiker shouts towards a cliff and hears the echo 2 s later. The speed of sound in air is 340 m/s. Calculate the distance from the hiker to the cliff.",
                    "hint": "The sound goes to the cliff and back in 2 s, so halve the total distance.",
                    "walkthrough": [
                        "v = 340 m/s, t = 2 s, find the distance to the cliff.",
                        "x = v × t = 340 × 2 = 680 m (there and back)",
                        "distance = 680 / 2",
                        "distance = 340 m"
                    ],
                    "answer": ans("echoes-p1", "m")
                },
                {
                    "id": "echoes-p2",
                    "question": "A bat sends out a click and hears the echo from a moth 0.05 s later. The speed of sound in air is 340 m/s. Calculate the distance from the bat to the moth.",
                    "hint": "Speed × time gives the there-and-back distance; the moth is half of that away.",
                    "walkthrough": [
                        "v = 340 m/s, t = 0.05 s, find the distance to the moth.",
                        "x = v × t = 340 × 0.05 = 17 m (there and back)",
                        "distance = 17 / 2",
                        "distance = 8.5 m"
                    ],
                    "answer": ans("echoes-p2", "m")
                },
                {
                    "id": "echoes-p3",
                    "question": "An ultrasound scanner sends a pulse into a patient. The echo from the far side of the liver returns 0.2 ms after the pulse is sent. The speed of ultrasound in body tissue is 1540 m/s. Calculate the depth of the far side of the liver below the skin. Give your answer in cm.",
                    "hint": "Change 0.2 ms to seconds, work out speed × time, halve it, then change metres to cm.",
                    "walkthrough": [
                        "v = 1540 m/s, t = 0.2 ms = 0.0002 s",
                        "x = v × t = 1540 × 0.0002 = 0.308 m (there and back)",
                        "depth = 0.308 / 2 = 0.154 m",
                        "depth = 15.4 cm"
                    ],
                    "answer": ans("echoes-p3", "cm")
                },
                {
                    "id": "echoes-p4",
                    "question": "A fishing boat is in water 450 m deep. The speed of sound in sea water is 1500 m/s. Calculate the time for a sonar pulse to travel from the boat to the seabed and back.",
                    "hint": "Double the depth to get the distance travelled, then t = x / v.",
                    "walkthrough": [
                        "distance there and back = 2 × 450 = 900 m, v = 1500 m/s, find t.",
                        "x = v × t → t = x / v",
                        "t = 900 / 1500",
                        "t = 0.6 s"
                    ],
                    "answer": ans("echoes-p4", "s")
                },
                {
                    "id": "echoes-p5",
                    "question": "In an ultrasound scan of a foetus, one echo returns from the near side of the head 0.08 ms after the pulse is sent, and another returns from the far side of the head 0.20 ms after the pulse is sent. The speed of ultrasound in body tissue is 1540 m/s. Calculate the width of the head. Give your answer in cm.",
                    "hint": "Find the depth of each side (speed × time ÷ 2, with times in seconds), then subtract.",
                    "walkthrough": [
                        "near side: 1540 × 0.00008 / 2 = 0.0616 m",
                        "far side: 1540 × 0.00020 / 2 = 0.154 m",
                        "width = 0.154 − 0.0616 = 0.0924 m",
                        "width = 9.24 cm"
                    ],
                    "answer": ans("echoes-p5", "cm")
                },
                {
                    "id": "echoes-p6",
                    "question": "A survey ship's sonar echo from the seabed takes 1.6 s to return. The ship moves to a second position where the echo takes 0.9 s. The speed of sound in sea water is 1500 m/s. Calculate how much shallower the water is at the second position.",
                    "hint": "Work out the depth at each position (speed × time ÷ 2), then find the difference.",
                    "walkthrough": [
                        "first depth = 1500 × 1.6 / 2 = 1200 m",
                        "second depth = 1500 × 0.9 / 2 = 675 m",
                        "difference = 1200 − 675",
                        "difference = 525 m"
                    ],
                    "answer": ans("echoes-p6", "m")
                }
            ]
        },
        {
            "id": "wave-graph",
            "name": "Reading wave graphs",
            "equations": ["wavelength = distance from one crest to the next", "period = time from one crest to the next", "f = 1 / T", "v = f × λ"],
            "boards": BOTH,
            "method": "Check the horizontal axis first: on a displacement–distance graph the gap from one crest to the next is the wavelength, and on a displacement–time graph that gap is the period. Amplitude is the height of a crest above the centre line, not crest to trough. Read the values where the crests sit on gridlines, then use f = 1 / T or v = f × λ if the question asks for a frequency or a speed.",
            "commonErrors": [
                "Reading a wavelength off a displacement–time graph: the gap between crests on a time axis is the period",
                "Taking crest-to-trough as the amplitude: amplitude is measured from the centre line",
                "Measuring crest to the next trough (half a wavelength) instead of crest to crest",
                "Leaving a wavelength in cm when calculating a wave speed in m/s"
            ],
            "worked": {
                "id": "wave-graph-w",
                "question": "The graph shows the displacement of the water surface along a line across a pond at one instant. Use the graph to find the wavelength of the wave.",
                "steps": [
                    "The horizontal axis is distance, so crest to crest is the wavelength.",
                    "First crest at 1 m, next crest at 5 m.",
                    "λ = 5 − 1",
                    "λ = 4 m"
                ],
                "answer": ans("wave-graph-w", "m"),
                "graph": {
                    "x": {"label": "distance in m", "min": 0, "max": 8, "step": 1},
                    "y": {"label": "displacement in cm", "min": -4, "max": 4, "step": 2},
                    "series": [{"kind": "curve", "points": graphs["wave-graph-w"]}],
                    "alt": "Displacement–distance graph of a water wave with amplitude 3 cm and crests at 1 m and 5 m"
                }
            },
            "practice": [
                {
                    "id": "wave-graph-p1",
                    "question": "The graph shows how the displacement of a loudspeaker cone changes with time. Use the graph to find the amplitude of the vibration.",
                    "hint": "Amplitude is the maximum displacement from the centre line (zero), not from trough to crest.",
                    "walkthrough": [
                        "The centre line is at 0 mm.",
                        "Each crest reaches 2 mm above the centre line.",
                        "amplitude = 2 mm"
                    ],
                    "answer": ans("wave-graph-p1", "mm"),
                    "graph": {
                        "x": {"label": "time in ms", "min": 0, "max": 8, "step": 1},
                        "y": {"label": "displacement in mm", "min": -3, "max": 3, "step": 1},
                        "series": [{"kind": "curve", "points": graphs["wave-graph-p1"]}],
                        "alt": "Displacement–time graph of a loudspeaker cone, starting at a crest of 2 mm with a period of 4 ms"
                    }
                },
                {
                    "id": "wave-graph-p2",
                    "question": "A long rope is shaken so that a wave travels along it. The graph shows the displacement of the rope against distance along it at one instant. Use the graph to find the wavelength of the wave.",
                    "hint": "Distance axis, so read the gap between two neighbouring crests.",
                    "walkthrough": [
                        "Crests are at 2 m, 10 m and 18 m.",
                        "λ = 10 − 2",
                        "λ = 8 m"
                    ],
                    "answer": ans("wave-graph-p2", "m"),
                    "graph": {
                        "x": {"label": "distance in m", "min": 0, "max": 20, "step": 2},
                        "y": {"label": "displacement in cm", "min": -15, "max": 15, "step": 5},
                        "series": [{"kind": "curve", "points": graphs["wave-graph-p2"]}],
                        "alt": "Displacement–distance graph of a wave on a rope with amplitude 10 cm and crests at 2 m, 10 m and 18 m"
                    }
                },
                {
                    "id": "wave-graph-p3",
                    "question": "A microphone is connected to an oscilloscope. The graph shows the trace for a sound wave. Use the graph to find the frequency of the sound.",
                    "hint": "Time axis, so crest to crest gives the period in ms; change it to seconds and use f = 1 / T.",
                    "walkthrough": [
                        "Crests at 1 ms and 5 ms, so T = 5 − 1 = 4 ms",
                        "T = 4 ms = 0.004 s",
                        "f = 1 / T = 1 / 0.004",
                        "f = 250 Hz"
                    ],
                    "answer": ans("wave-graph-p3", "Hz"),
                    "graph": {
                        "x": {"label": "time in ms", "min": 0, "max": 10, "step": 1},
                        "y": {"label": "displacement in mm", "min": -4, "max": 4, "step": 2},
                        "series": [{"kind": "curve", "points": graphs["wave-graph-p3"]}],
                        "alt": "Displacement–time graph of a sound wave with amplitude 3 mm and crests at 1 ms, 5 ms and 9 ms"
                    }
                },
                {
                    "id": "wave-graph-p4",
                    "question": "A float bobs up and down on water waves. The graph shows the displacement of the float against time. Use the graph to find the frequency of the waves.",
                    "hint": "Read the period from one crest to the next on the time axis, then f = 1 / T.",
                    "walkthrough": [
                        "Crests at 0 s, 0.4 s and 0.8 s, so T = 0.4 s",
                        "f = 1 / T = 1 / 0.4",
                        "f = 2.5 Hz"
                    ],
                    "answer": ans("wave-graph-p4", "Hz"),
                    "graph": {
                        "x": {"label": "time in s", "min": 0, "max": 1, "step": 0.1},
                        "y": {"label": "displacement in cm", "min": -6, "max": 6, "step": 2},
                        "series": [{"kind": "curve", "points": graphs["wave-graph-p4"]}],
                        "alt": "Displacement–time graph of a float with amplitude 4 cm, starting at a crest, with crests at 0 s, 0.4 s and 0.8 s"
                    }
                },
                {
                    "id": "wave-graph-p5",
                    "question": "The graph shows the displacement of the water surface along a ripple tank at one instant. The dipper making the waves vibrates at 2.5 Hz. Use the graph to find the speed of the waves in m/s.",
                    "hint": "Read the wavelength crest to crest in cm, change it to metres, then v = f × λ.",
                    "walkthrough": [
                        "Crests at 5 cm and 25 cm, so λ = 25 − 5 = 20 cm",
                        "λ = 20 cm = 0.2 m",
                        "v = f × λ = 2.5 × 0.2",
                        "v = 0.5 m/s"
                    ],
                    "answer": ans("wave-graph-p5", "m/s"),
                    "graph": {
                        "x": {"label": "distance in cm", "min": 0, "max": 40, "step": 5},
                        "y": {"label": "displacement in mm", "min": -3, "max": 3, "step": 1},
                        "series": [{"kind": "curve", "points": graphs["wave-graph-p5"]}],
                        "alt": "Displacement–distance graph of ripple tank waves with amplitude 2 mm and crests at 5 cm and 25 cm"
                    }
                },
                {
                    "id": "wave-graph-p6",
                    "question": "The graph shows the displacement of air particles along a line in front of a loudspeaker at one instant. The loudspeaker produces a note of frequency 340 Hz. Use the graph to find the speed of sound in the air.",
                    "hint": "Distance axis, so crest to crest is the wavelength in m; then v = f × λ.",
                    "walkthrough": [
                        "Crests at 0 m, 1 m, 2 m and 3 m, so λ = 1 m",
                        "v = f × λ = 340 × 1",
                        "v = 340 m/s"
                    ],
                    "answer": ans("wave-graph-p6", "m/s"),
                    "graph": {
                        "x": {"label": "distance in m", "min": 0, "max": 3, "step": 0.5},
                        "y": {"label": "displacement in mm", "min": -0.6, "max": 0.6, "step": 0.2},
                        "series": [{"kind": "curve", "points": graphs["wave-graph-p6"]}],
                        "alt": "Displacement–distance graph of a sound wave with amplitude 0.4 mm, starting at a crest, with crests at 0 m, 1 m, 2 m and 3 m"
                    }
                }
            ]
        }
    ]
}


def write_topic():
    """Write data/waves.json next to this script's project root."""
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    out_path = os.path.join(root, "data", "waves.json")
    with open(out_path, "w", encoding="utf-8") as handle:
        json.dump(topic, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
    print(f"wrote {out_path}")


if __name__ == "__main__":
    if "--write" in sys.argv:
        write_topic()
