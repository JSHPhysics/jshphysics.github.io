#!/usr/bin/env python3
"""
Independent blind check of every answer in data/*.json for the GCSE
Non-negotiables site.

Every value below was extracted BY HAND from the question text (or from the
graph spec's plotted coordinates) and the answer re-derived from scratch.
tools/calc_*.py were NOT read.

Usage: python3 -I verify_gcse.py [repo_root]
"""
import glob
import json
import math
import os
import re
import sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else "/home/claude/gcse-non-negotiables"
DATA = os.path.join(ROOT, "data")

g = 10.0          # N/kg, standard value per SCHEMA.md
c_light = 3e8     # m/s, standard value per SCHEMA.md
PI = math.pi

# ---------------------------------------------------------------------------
# Expected answers: id -> (value, unit) or (value, unit, note)
# A note records any ambiguity / realism / physics / tier concern.
# ---------------------------------------------------------------------------
E = {}
NOTES = {}


def exp(qid, value, unit, note=None):
    E[qid] = (value, unit)
    if note:
        NOTES.setdefault(qid, []).append(note)


def note(qid, text):
    NOTES.setdefault(qid, []).append(text)


# ======================= units-and-equations ===============================
# si-conversions
exp("si-conversions-w", 35 / 1000, "m")
exp("si-conversions-p1", 120 / 100, "m")
exp("si-conversions-p2", 750 / 1000, "kg")
exp("si-conversions-p3", 3.2 * 1000, "kg")
exp("si-conversions-p4", 2.5 * 3600, "s")
exp("si-conversions-p5", 450 / 10000, "m²")
exp("si-conversions-p6", 1500 / 1e6, "m³")
# prefixes
exp("prefixes-w", 540 * 1000, "J")
exp("prefixes-p1", 20 / 1000, "A")
exp("prefixes-p2", 1.8e9, "W")
exp("prefixes-p3", 2.5e6, "W")
exp("prefixes-p4", 4.7 * 1000, "Ω")
exp("prefixes-p5", 250e-6, "s")
exp("prefixes-p6", 650e-9, "m")
# compound-units
exp("compound-units-w", 90 * 1000 / 3600, "m/s")
exp("compound-units-p1", 108 * 1000 / 3600, "m/s")
exp("compound-units-p2", 1.5 * 3_600_000, "J")
exp("compound-units-p3", 12 * 3.6, "km/h")
exp("compound-units-p4", 2.7 * 1000, "kg/m³")
exp("compound-units-p5", 0.15 / 60, "m/s")
exp("compound-units-p6", 12 * 1000 / 1e6 / 60, "m³/s")
# standard-form (type tagged Higher)
exp("standard-form-w", 9.8e7, "Hz")
exp("standard-form-p1", 1.2e-2, "m")
exp("standard-form-p2", 6.4e6, "m")
exp("standard-form-p3", 6, "")          # 2 500 000 = 2.5e6
exp("standard-form-p4", -7, "")         # 0.000 000 45 = 4.5e-7
exp("standard-form-p5", 3e8 * 2e-6, "m")
exp("standard-form-p6", 1.6e-19 * 5e19, "C")
# rearranging
exp("rearranging-w", 2300 / 230, "A")
exp("rearranging-p1", 450 / g, "kg")
exp("rearranging-p2", 5 / 2500, "m³")
exp("rearranging-p3", 3000 / (60 * g), "m")
exp("rearranging-p4", math.sqrt(2 * 3600 / 50), "m/s")
exp("rearranging-p5", math.sqrt(30 ** 2 - 2 * 2 * 200), "m/s")
exp("rearranging-p6", math.sqrt(2 * 1 / 50), "m")
# percentages-ratios
exp("percentages-ratios-w", 350 / 500 * 100, "%")
exp("percentages-ratios-p1", 324000 / 360000 * 100, "%")
exp("percentages-ratios-p2", 400 / 50, "")
exp("percentages-ratios-p3", (25 - 20) / 20 * 100, "%")
exp("percentages-ratios-p4", 0.28 * 30e6, "J")
exp("percentages-ratios-p5", (12 - 2.4) / 12 * 100, "%")
exp("percentages-ratios-p6", (2.0 - 1.4) / 2.0 * 100, "%")

# =============================== motion ====================================
# speed
exp("speed-w", 120 / 8, "m/s")
exp("speed-p1", 200 / 25, "m/s")
exp("speed-p2", 340 * 2.5, "m")
exp("speed-p3", 36000 / (30 * 60), "m/s")
exp("speed-p4", 2700 / 1.5, "s")
exp("speed-p5", (45000 + 15000) / ((25 + 5) * 60), "m/s")
exp("speed-p6", 200 / (100 / 5 + 100 / 4), "m/s")
# acceleration
exp("acceleration-w", (23 - 5) / 4, "m/s²")
exp("acceleration-p1", (9 - 0) / 3, "m/s²")
exp("acceleration-p2", (12 - 30) / 20, "m/s²",
    "AMBIGUOUS SIGN: asks for 'the acceleration' of a slowing train; stored "
    "value is -0.9. A student who writes 0.9 (deceleration) is marked wrong "
    "('Right size, wrong sign'). Question does not define a positive direction.")
exp("acceleration-p3", 3 + 0.5 * 8, "m/s")
exp("acceleration-p4", (90 / 3.6 - 54 / 3.6) / 5, "m/s²")
_v_lift = 1.2 * 5
exp("acceleration-p5", _v_lift / 4, "m/s²")
exp("acceleration-p6", (72 / 3.6) / 4, "s")
# v2-u2  (type is Foundation+Higher; p4-p6 tagged Higher)
exp("v2-u2-w", math.sqrt(5 ** 2 + 2 * 4 * 18), "m/s")
exp("v2-u2-p1", math.sqrt(2 * g * 5), "m/s")
exp("v2-u2-p2", (30 ** 2 - 0) / (2 * 150), "m/s²")
exp("v2-u2-p3", (0 - 60 ** 2) / (2 * -3), "m")
exp("v2-u2-p4", math.sqrt(2 * g * 11.25), "m/s")
exp("v2-u2-p5", (0 - (72 / 3.6) ** 2) / (2 * -5), "m",
    "TIER CONSISTENCY: tagged Higher, but it is the same rearrangement "
    "(find x from u, v=0, a) as p3, which is tagged Foundation; the only "
    "extra step is km/h -> m/s, which p-level 'unit conversion' questions "
    "treat as Foundation elsewhere.")
exp("v2-u2-p6", math.sqrt(2 * g * 3.20), "m/s")
# dt-graph  (values read from graph spec coordinates)
exp("dt-graph-w", (30 - 0) / (6 - 0), "m/s")
exp("dt-graph-p1", 160, "m")                       # point P (40,160)
exp("dt-graph-p2", (90 - 0) / (150 - 100), "m/s")
exp("dt-graph-p3", ((80 - 0) / 4) / ((140 - 80) / (10 - 4)), "")
exp("dt-graph-p4", 1500 / (10 * 60), "m/s")
exp("dt-graph-p5", (300 + 300) / 80, "m/s")
exp("dt-graph-p6", ((900 - 200) / (60 - 40)) * 3.6, "km/h")
# vt-graph
exp("vt-graph-w", (20 - 0) / 8, "m/s²")
exp("vt-graph-p1", 15 * (50 - 10), "m")
exp("vt-graph-p2", 0.5 * 4 * 10, "m")
exp("vt-graph-p3", (20 - 0) / (14 - 6), "m/s²")
exp("vt-graph-p4", 0.5 * (10 + 25) * 6, "m")
exp("vt-graph-p5", (32 - 0) / (12 - 4), "m/s²")   # tangent (4,0)-(12,32)
exp("vt-graph-p6", 0.5 * (20 + 40) * 20, "m")
# orbital-speed (type tagged Higher)
_orb_note = ("SPEC: v = 2πr/T is NOT in Edexcel GCSE Physics 1PH0 (Topic 7 "
             "astronomy is qualitative: 7.6P/7.7P; Appendix 2 has no orbital "
             "equation). It is an Edexcel IGCSE (4PH1) equation.")
exp("orbital-speed-w", 2 * PI * 6.8e6 / (92 * 60), "m/s", _orb_note)
exp("orbital-speed-p1", 2 * PI * 4.2e7 / (24 * 3600), "m/s")
exp("orbital-speed-p2", 2 * PI * 6.9e6 / 5700, "m/s")
exp("orbital-speed-p3", 2 * PI * 3.84e8 / (27.3 * 86400), "m/s")
exp("orbital-speed-p4", 3870 * 12 * 3600 / (2 * PI), "m")
exp("orbital-speed-p5", 2 * PI * 1.5e11 / (365 * 86400), "m/s")
exp("orbital-speed-p6", 2140 * 7.66 * 3600 / (2 * PI), "m")

# ========================= forces-and-momentum =============================
exp("weight-and-mass-w", 65 * g, "N")
exp("weight-and-mass-p1", 1200 * g, "N")
exp("weight-and-mass-p2", 2.5 * g, "N")
exp("weight-and-mass-p3", 48 / g, "kg")
exp("weight-and-mass-p4", 0.400 * g, "N")
exp("weight-and-mass-p5", (800 / g) * 1.6, "N")
exp("weight-and-mass-p6", 555 / (1500 / g), "N/kg")
# resultant-force
exp("resultant-force-w", 920 - 850, "N")
exp("resultant-force-p1", 3000 - 1200, "N")
exp("resultant-force-p2", 150 + 220, "N")
exp("resultant-force-p3", 4500 - 1700, "N")
exp("resultant-force-p4", 2400 - 1800, "N")
exp("resultant-force-p5", 70 * g - 560, "N")
exp("resultant-force-p6", 6200 - 500 * g, "N")
# newtons-second-law
exp("newtons-second-law-w", 1500 * 2, "N")
exp("newtons-second-law-p1", 2 * 1.5, "N")
exp("newtons-second-law-p2", 80 * 0.75, "N")
exp("newtons-second-law-p3", 18000 / 1.2, "kg")
exp("newtons-second-law-p4", 0.6 / 0.300, "m/s²")
exp("newtons-second-law-p5", (2500 - 700) / 1200, "m/s²")
exp("newtons-second-law-p6", (8000 - 500 * g) / 500, "m/s²")
# stopping-distance
exp("stopping-distance-w", 15 * 0.6 + 14, "m")
exp("stopping-distance-p1", 20 * 0.7, "m")
exp("stopping-distance-p2", 12 + 24, "m")
exp("stopping-distance-p3", 18 / 24, "s")
exp("stopping-distance-p4", (54 / 3.6) * 0.8, "m")
exp("stopping-distance-p5", 30 * 0.5 + 75, "m")
exp("stopping-distance-p6", 60 - 25 * 0.8, "m")
# momentum (Higher)
exp("momentum-w", 1200 * 15, "kg m/s")
exp("momentum-p1", 70 * 8, "kg m/s")
exp("momentum-p2", 0.16 * 35, "kg m/s")
exp("momentum-p3", 240000 / 16, "kg")
exp("momentum-p4", 9 / 0.450, "m/s")
exp("momentum-p5", 75 * (100 / 12.5), "kg m/s")
exp("momentum-p6", (150 / g) * 1.2, "kg m/s")
# conservation-of-momentum (Higher)
exp("conservation-of-momentum-w", 2 * 3 / (2 + 1), "m/s")
exp("conservation-of-momentum-p1", 1200 * 10 / (1200 + 800), "m/s")
exp("conservation-of-momentum-p2", 8000 * 4 / (8000 + 12000), "m/s")
exp("conservation-of-momentum-p3", 60 * 2 / 40, "m/s")
exp("conservation-of-momentum-p4", 0.010 * 400 / 4, "m/s")
exp("conservation-of-momentum-p5", (0.5 * 6 - 0.5 * 1.5) / 0.3, "m/s")
exp("conservation-of-momentum-p6", (3 * 4 + 2 * 1.5) / (3 + 2), "m/s")
# force-from-momentum-change (Higher)
exp("force-from-momentum-change-w", 0.4 * 20 / 0.05, "N")
exp("force-from-momentum-change-p1", 1000 * 15 / 3, "N")
exp("force-from-momentum-change-p2", 0.06 * 50 / 0.004, "N")
exp("force-from-momentum-change-p3", 1200 * 12 / 72000, "s")
exp("force-from-momentum-change-p4", 0.160 * 30 / 0.02, "N")
_m_climber = 800 / g
exp("force-from-momentum-change-p5", _m_climber * 6 / 0.4, "N",
    "PHYSICS: (mv-mu)/t gives the RESULTANT force (1200 N). The question asks "
    "for the force the ROPE exerts; strictly rope force = resultant + weight = "
    "1200 + 800 = 2000 N. Giving the weight (800 N) rather than the mass "
    "invites the careful student to include it. Stored 1200 N is the usual "
    "GCSE mark-scheme answer but the wording is open to challenge.")
exp("force-from-momentum-change-p6", (0.2 * 8 + 60 * 0.05) / 0.2, "m/s")
# force-graph
exp("force-graph-w", 1 / ((5 - 0) / (10 - 0)), "kg")          # a-F gradient 0.5
exp("force-graph-p1", 50, "m/s",
    "GRAPH READ: curve reaches 49.66 m/s at t=40 s, asymptote 50 m/s; a "
    "student reads ~50. Fine.")
exp("force-graph-p2", 6, "N")                                    # P (6,1.5)
exp("force-graph-p3", (20 - 0) / (2 - 0), "m/s²")
exp("force-graph-p4", 2, "N")                                    # intercept (2,0)
exp("force-graph-p5", 0.5 * ((6 - 2) + (8 - 0)) * 400 / 1000, "kg m/s")  # ms
exp("force-graph-p6", 1 / ((3 - 0) / (12 - 3)), "kg")

# =============================== energy ====================================
exp("kinetic-energy-w", 0.5 * 60 * 8 ** 2, "J")
exp("kinetic-energy-p1", 0.5 * 1000 * 20 ** 2, "J")
exp("kinetic-energy-p2", 0.5 * 0.16 * 30 ** 2, "J")
exp("kinetic-energy-p3", 0.5 * 1500 * (72 / 3.6) ** 2 / 1000, "kJ")
exp("kinetic-energy-p4", 0.5 * 0.250 * 12 ** 2, "J")
exp("kinetic-energy-p5", math.sqrt(2 * 2560 / 80), "m/s")
exp("kinetic-energy-p6", math.sqrt(2 * 2500e3 / 20000), "m/s")
# gpe
exp("gravitational-potential-energy-w", 50 * g * 12, "J")
exp("gravitational-potential-energy-p1", 2 * g * 1.5, "J")
exp("gravitational-potential-energy-p2", 800 * g * 20, "J")
exp("gravitational-potential-energy-p3", 9000 / (60 * g), "m")
exp("gravitational-potential-energy-p4", 45000 / (g * 15), "kg")
exp("gravitational-potential-energy-p5", 150 * 2.4, "J",
    "REALISM: a van floor 2.4 m above the ground is high (typical ~1 m).")
exp("gravitational-potential-energy-p6", 70 * g * (500 * 0.20) / 1000, "kJ")
# work-done
exp("work-done-w", 40 * 5, "J")
exp("work-done-p1", 600 * 50, "J")
exp("work-done-p2", 120 * 3, "J",
    "REALISM: a luggage rack 3 m up is high (train racks ~1.8 m).")
exp("work-done-p3", 4500 / 30, "N")
exp("work-done-p4", 2500 / 20, "m")
exp("work-done-p5", 3000 * (2 * 60) / 1000, "kJ")
exp("work-done-p6", (1200 * 2) * 50 / 1000, "kJ")
# power
exp("power-w", 3000 / 20, "W")
exp("power-p1", 180000 / 90, "W")
exp("power-p2", 1500 / 2.5, "W")
exp("power-p3", 2000 * 5 * 60 / 1000, "kJ")
exp("power-p4", 9000 / 60, "s")
exp("power-p5", 50 * g * 8 / 20, "W")
exp("power-p6", 1500 * 12 / 30, "W")
# efficiency
exp("efficiency-w", 350 / 500, "")
exp("efficiency-p1", 108 / 120 * 100, "%")
exp("efficiency-p2", 6 / 60, "")
exp("efficiency-p3", 0.80 * 2500, "J")
exp("efficiency-p4", 45 / 0.30, "kJ")
exp("efficiency-p5", (50 * g * 24) / 20000, "")
exp("efficiency-p6", 9000 / (400 * 30) * 100, "%")
# energy-transfers
exp("energy-transfers-w", math.sqrt(2 * g * 5), "m/s")
exp("energy-transfers-p1", 500 * g * 20, "J")
exp("energy-transfers-p2", math.sqrt(2 * g * 7.2), "m/s")
exp("energy-transfers-p3", 14 ** 2 / (2 * g), "m")
exp("energy-transfers-p4", math.sqrt(2 * g * 1.80), "m/s")
exp("energy-transfers-p5", math.sqrt(2 * (60 * g * 30 - 6000) / 60), "m/s")
exp("energy-transfers-p6", 2 * g * 4 - 0.5 * 2 * 6 ** 2, "J")
# energy-graph
exp("energy-graph-w", 150 * 8, "J")
exp("energy-graph-p1", 0.5 * 0.5 * 120, "J")
exp("energy-graph-p2", ((400 - 0) / (5 - 0)) / g, "kg")
exp("energy-graph-p3", (3000 - 0) / (20 - 0), "W")
exp("energy-graph-p4", 100 * 6 + 0.5 * 4 * 100, "J")
exp("energy-graph-p5", 2 * ((250 - 0) / (100 - 0)), "kg")
exp("energy-graph-p6", ((6000 / 20) / 500) * 100, "%")

# ================================ waves ====================================
exp("wave-speed-frequency-w", 250 * 1.36, "m/s")
exp("wave-speed-frequency-p1", 4 * 0.05, "m/s")
exp("wave-speed-frequency-p2", 0.2 * 40, "m/s")
exp("wave-speed-frequency-p3", c_light / 150e3, "m")
exp("wave-speed-frequency-p4", 2e6 * 0.77e-3, "m/s")
exp("wave-speed-frequency-p5", (30 / 10) * 0.025, "m/s")
exp("wave-speed-frequency-p6", 340 / (1 / 2e-3), "m")
# wave-speed-distance
exp("wave-speed-distance-w", 12 / 8, "m/s")
exp("wave-speed-distance-p1", 1700 / 5, "m/s")
exp("wave-speed-distance-p2", 0.9 / 6, "m/s")
exp("wave-speed-distance-p3", 340 * 4, "m")
exp("wave-speed-distance-p4", 1500e3 / 6000, "s")
exp("wave-speed-distance-p5", (1700 / 5) / 200, "m")
exp("wave-speed-distance-p6", (30 / 10) / (1 / 4), "m")
# period-frequency
exp("period-frequency-w", 1 / (20 / 5), "s")
exp("period-frequency-p1", 30 / 6, "Hz")
exp("period-frequency-p2", 1 / 50, "s")
exp("period-frequency-p3", 1 / 4e-3, "Hz")
exp("period-frequency-p4", 1 / 20e3 * 1000, "ms")
exp("period-frequency-p5", 20 / 25, "s")
exp("period-frequency-p6", 60 / 72, "s")
# echoes
exp("echoes-w", 1500 * 0.4 / 2, "m")
exp("echoes-p1", 340 * 2 / 2, "m")
exp("echoes-p2", 340 * 0.05 / 2, "m")
exp("echoes-p3", 1540 * 0.2e-3 / 2 * 100, "cm")
exp("echoes-p4", 2 * 450 / 1500, "s")
exp("echoes-p5", 1540 * (0.20e-3 - 0.08e-3) / 2 * 100, "cm")
exp("echoes-p6", 1500 * (1.6 - 0.9) / 2, "m")
# wave-graph (read from plotted coordinates)
exp("wave-graph-w", 5 - 1, "m")          # crests at x=1 and x=5
exp("wave-graph-p1", 2, "mm")            # peak displacement 2
exp("wave-graph-p2", 10 - 2, "m")        # crests at 2 and 10
exp("wave-graph-p3", 1 / ((5 - 1) * 1e-3), "Hz")     # crests at 1 ms and 5 ms
exp("wave-graph-p4", 1 / (0.4 - 0.0), "Hz")          # crests at 0 and 0.4 s
exp("wave-graph-p5", 2.5 * ((25 - 5) / 100), "m/s")  # crests at 5 cm and 25 cm
exp("wave-graph-p6", 340 * (1 - 0), "m/s")           # crests at 0 and 1 m

# ============================ radioactivity ================================
exp("nuclear-notation-w", 14 - 6, "")
exp("nuclear-notation-p1", 11, "")
exp("nuclear-notation-p2", 238, "")
exp("nuclear-notation-p3", 131 - 53, "")
exp("nuclear-notation-p4", 27 + 33, "")
exp("nuclear-notation-p5", (37 - 17) - (35 - 17), "")
exp("nuclear-notation-p6", (206 - 82) - 82, "")
# nuclear-equations
exp("nuclear-equations-w", 226 - 4, "")
exp("nuclear-equations-p1", 92 - 2, "")
exp("nuclear-equations-p2", 6 + 1, "")
exp("nuclear-equations-p3", 210 - 4, "")
exp("nuclear-equations-p4", 38 + 1, "")
exp("nuclear-equations-p5", 90 - 2 + 1, "")
exp("nuclear-equations-p6", (238 - 222) / 4, "")
# half-life-fraction
exp("half-life-fraction-w", 800 / 2 ** (6 / 2), "Bq")
exp("half-life-fraction-p1", 1 / 2 ** 2, "")
exp("half-life-fraction-p2", 1200 / 2 ** 2, "Bq")
exp("half-life-fraction-p3", 640 / 2 ** (24 / 8), "counts/min")
exp("half-life-fraction-p4", 1 / 2 ** (24 / 6), "")
exp("half-life-fraction-p5", 3200 / 2 ** (120 / 20), "Bq")
exp("half-life-fraction-p6", 2400 - 2400 / 2 ** (165 / 55), "")
# half-life-time
exp("half-life-time-w", math.log2(1600 / 200) * 4, "hours")
exp("half-life-time-p1", math.log2(800 / 50), "")
exp("half-life-time-p2", math.log2(6000 / 750) * 30, "minutes")
exp("half-life-time-p3", 36 / math.log2(400 / 50), "minutes")
exp("half-life-time-p4", 120 / math.log2(2400 / 300), "minutes")
exp("half-life-time-p5", math.log2(8) * 5730, "years")
exp("half-life-time-p6", 80 / math.log2(1920 / 120), "s")
# background-count (Higher)
exp("background-count-w", (540 - 40) / 2 ** (20 / 10), "counts/min")
exp("background-count-p1", 275 - 25, "counts/min")
exp("background-count-p2", (650 - 50) / 2 + 50, "counts/min")
exp("background-count-p3", math.log2((1300 - 20) / (180 - 20)), "")
exp("background-count-p4", 30 / math.log2((820 - 20) / (120 - 20)), "minutes")
exp("background-count-p5", (243 - 180 / 60) / 2 ** (20 / 5), "counts/min")
exp("background-count-p6", math.log2((1030 - 30) / (155 - 30)) * 8, "days")
# decay-graph (read from plotted coordinates)
exp("decay-graph-w", 20, "s")                  # 800 -> 400 at t=20
exp("decay-graph-p1", 15, "minutes")           # 1200 -> 600 at t=15
exp("decay-graph-p2", 200, "Bq")               # point (60,200)
exp("decay-graph-p3", 40 / 10, "")             # 400->200 at 10 min
exp("decay-graph-p4", 12, "hours")             # 400 at t=12
exp("decay-graph-p5", 6400 / 2 ** (60 / 10), "Bq")   # 6400->3200 at 10 min
exp("decay-graph-p6", 10, "minutes")           # corrected 800 -> 400 (total 500) at t=10

# ============================== electricity ================================
exp("charge-w", 0.25 * 2 * 60, "C")
exp("charge-p1", 8 * 150, "C")
exp("charge-p2", 120 * 3, "C")
exp("charge-p3", 450 / 90, "A")
exp("charge-p4", 20e-3 * 5 * 60, "C")
exp("charge-p5", 0.9 / (2.5 * 60) * 1000, "mA")
exp("charge-p6", (24 / 12) * 3 * 60, "C")
# ohm
exp("ohm-w", 0.5 * 6, "V")
exp("ohm-p1", 4 * 3, "V")
exp("ohm-p2", 0.3 * 20, "V")
exp("ohm-p3", 230 / 10, "Ω")
exp("ohm-p4", 5e-3 * 2200, "V")
exp("ohm-p5", 9 / 1500 * 1000, "mA")
exp("ohm-p6", (90 / 30) * 4, "V")
# eqv
exp("eqv-w", 20 * 12, "J")
exp("eqv-p1", 40 * 1.5, "J")
exp("eqv-p2", 50 * 230, "J")
exp("eqv-p3", 900 / 75, "V")
exp("eqv-p4", 3000 / 6, "C")
exp("eqv-p5", 0.5 * 20 * 60 * 230, "J")
exp("eqv-p6", 72 / (0.2 * 2 * 60), "V")
# power (electrical)
exp("power-w", 10 * 230, "W")        # NB: id 'power-w' also exists in energy.json
exp("power-p1", 3 * 20, "W")
exp("power-p2", 2 ** 2 * 12, "W")
exp("power-p3", 1840 / 230, "A")
exp("power-p4", 60 / 5 ** 2, "Ω")
exp("power-p5", 230 ** 2 / 46, "W")
exp("power-p6", 12 ** 2 / 24, "Ω")
# ept
exp("ept-w", 2000 * 3 * 60, "J")
exp("ept-p1", 60 * 50, "J")
exp("ept-p2", 0.5 * 230 * 40, "J")
exp("ept-p3", 90e3 / (2 * 60), "W")
exp("ept-p4", 450e3 / 1500 / 60, "minutes")
exp("ept-p5", 5 ** 2 * 12 * 4 * 60, "J")
exp("ept-p6", 5 * 2 * 1.5 * 3600 / 1000, "kJ")
# circuits
exp("circuits-w", 6 / (3 + 9), "A")
exp("circuits-p1", 5 + 15 + 20, "Ω")
exp("circuits-p2", 0.3 + 0.5, "A")
exp("circuits-p3", 0.2 * 30, "V")
exp("circuits-p4", (15 + 25) / 1000, "A")
exp("circuits-p5", (12 / (8 + 16)) * 16, "V")
exp("circuits-p6", 6 / 3 + 6 / 6, "A")
# iv-graph
exp("iv-graph-w", 6 / 1.5, "Ω")
exp("iv-graph-p1", 4 / 0.8, "Ω")
exp("iv-graph-p2", 5 / 0.2, "Ω")
exp("iv-graph-p3", 3 / 60e-3, "Ω")
exp("iv-graph-p4", 6 / 2, "Ω")
exp("iv-graph-p5", 20, "mA")               # curve point (0.7, 20)
exp("iv-graph-p6", 2 * 1000, "Ω")          # curve point (40, 2 kΩ)

# =============================== magnetism =================================
exp("motor-force-w", 0.4 * 3 * 0.5, "N")
exp("motor-force-p1", 0.1 * 2.5 * 0.4, "N")
exp("motor-force-p2", 0.5 * 0.3 * 1.2, "N")
exp("motor-force-p3", 0.06 / (1.5 * 0.2), "T")
exp("motor-force-p4", 0.15 * 5 * 0.08, "N")
exp("motor-force-p5", 0.12 / (0.2 * 0.30), "A")
exp("motor-force-p6", 0.1 * (6 / 2) * 0.5, "N")
# turns
exp("turns-w", 230 * 120 / 2300, "V")
exp("turns-p1", 12 * 500 / 100, "V")
exp("turns-p2", 230 * 25 / 1150, "V")
exp("turns-p3", 920 * 8 / 230, "turns")
exp("turns-p4", 40 * 230 / 20, "turns")
exp("turns-p5", 1500 * 400 / 25, "turns")
exp("turns-p6", 230 * (2000 - 1600) / 1600, "V")
# tx-power
exp("tx-power-w", 230 * 0.5 / 23, "A")
exp("tx-power-p1", 12 * 2 / 48, "A")
exp("tx-power-p2", 11.5 * 6 / 230, "A")
exp("tx-power-p3", 230 * 20e-3 / 5, "A")
exp("tx-power-p4", 230 * 0.2 / 4, "V")
exp("tx-power-p5", (230 * 50 / 1000) * 2 / 230, "A")
exp("tx-power-p6", 12 * 5 / (12 * 1200 / 60), "A")
# loss
exp("loss-w", 20 ** 2 * 5, "W")
exp("loss-p1", 40 ** 2 * 0.5, "W")
exp("loss-p2", 50 ** 2 * 10, "W")
exp("loss-p3", math.sqrt(1800 / 2), "A")
exp("loss-p4", 60 ** 2 * (0.05 * 20), "W")
exp("loss-p5", (100e3 / 2000) ** 2 * 4 / 1000, "kW")
exp("loss-p6", (60e3 / 4000) ** 2 * 0.4, "W")

# ============================ particle-model ===============================
exp("density-w", 540 / 200, "g/cm³")
exp("density-p1", 150 / 60, "g/cm³")
exp("density-p2", 7200 / 3, "kg/m³")
exp("density-p3", 0.92 * 500, "g")
exp("density-p4", 60 / 1.2, "m³",
    "REALISM: a 50 m³ classroom is small (about 4 m x 4 m x 3 m); typical "
    "classrooms are 150-200 m³.")
exp("density-p5", 2160 / (20 * 10 * 6), "g/cm³")
exp("density-p6", 0.195 / (25e-6), "kg/m³")
# shc
exp("shc-w", 2 * 4200 * (70 - 20), "J")
exp("shc-p1", 1.5 * 900 * (115 - 15), "J")
exp("shc-p2", 0.5 * 390 * 40, "J")
exp("shc-p3", 50000 / (2 * 50), "J/kg °C")
exp("shc-p4", 42000 / (0.250 * 4200), "°C")
exp("shc-p5", 2000 * 105 / (1 * 4200), "°C")
exp("shc-p6", 60 * 4200 * (55 - 15) / 3000, "s")
# latent
exp("latent-w", 0.5 * 334000, "J")
exp("latent-p1", 2 * 2_260_000, "J")
exp("latent-p2", 1.5 * 334000, "J")
exp("latent-p3", 1_130_000 / 2_260_000, "kg")
exp("latent-p4", 52500 / 0.300, "J/kg")
exp("latent-p5", 1500 * 4 * 60 / 2_260_000, "kg")
exp("latent-p6", 2 * 334000 / 400, "s")
# change-of-state
exp("change-of-state-w", 0.5 * 334000 + 0.5 * 4200 * 20, "J")
exp("change-of-state-p1", 2 * 4200 * 20 + 2 * 2_260_000, "J")
exp("change-of-state-p2", 0.2 * 334000 + 0.2 * 4200 * 40, "J")
exp("change-of-state-p3", 0.5 * 4200 * 40 + 0.5 * 2_260_000, "J")
exp("change-of-state-p4", (0.4 * 4200 * 30 + 0.4 * 334000) / 1000, "kJ")
exp("change-of-state-p5", (1 * 334000 + 1 * 4200 * 30) / 2000, "s")
exp("change-of-state-p6", (1.5 * 4200 * 40 + 1.5 * 2_260_000) / (25 * 60), "W")
# temperature
exp("temperature-w", 25 + 273, "K")
exp("temperature-p1", 100 + 273, "K")
exp("temperature-p2", 0 - 273, "°C")
exp("temperature-p3", -40 + 273, "K")
exp("temperature-p4", 80 - 20, "K")
exp("temperature-p5", 2 * (27 + 273) - 273, "°C")
exp("temperature-p6", 22 - (255 - 273), "°C")
# boyle (Higher)
exp("boyle-w", 100 * 600 / 200, "kPa")
exp("boyle-p1", 100 * 50 / 20, "kPa")
exp("boyle-p2", 300 * 2 / 100, "cm³")
exp("boyle-p3", 100 * 1500 / 120, "cm³")
exp("boyle-p4", 100 * 2400 / 12, "kPa")
exp("boyle-p5", 240 - 100 * 240 / 160, "cm³")
exp("boyle-p6", 100 * (20 * 15) / (20 * 5), "kPa")
# heating-graph (read from plotted coordinates)
exp("heating-graph-w", 60, "°C")                       # plateau at 60
exp("heating-graph-p1", 80, "°C")                      # plateau at 80
exp("heating-graph-p2", 540 - 60, "s")                 # plateau 60..540 s
exp("heating-graph-p3", (20 + (100 - 20) * 2 / 4) - 20, "°C")   # 60 - 20
exp("heating-graph-p4", 30 * (7 - 2) * 60, "J")        # plateau 2..7 min
exp("heating-graph-p5", 40 / (0.4 * ((50 - 10) / (200 - 0))), "J/kg °C")
exp("heating-graph-p6", 40 * (500 - 100) / 0.2, "J/kg")

# =========================== forces-and-matter =============================
exp("hooke-w", 25 * 0.2, "N")
exp("hooke-p1", 40 * 0.15, "N")
exp("hooke-p2", 500 * 0.04, "N")
exp("hooke-p3", 8 / 0.16, "N/m")
exp("hooke-p4", 30 / 2000 * 1000, "mm",
    "REALISM: 2000 N/m is far too soft for a car suspension spring (real "
    "~20-50 kN/m) and 30 N is a trivial load for one; the numbers are fine "
    "for the maths but the context is off.")
exp("hooke-p5", 0.6 * g / 120 * 100, "cm")
exp("hooke-p6", 1.8 / ((21 - 15) / 100), "N/m")
# elastic
exp("elastic-w", 0.5 * 200 * 0.1 ** 2, "J")
exp("elastic-p1", 0.5 * 400 * 0.05 ** 2, "J",
    "REALISM: pogo-stick spring at 400 N/m (real ~10-30 kN/m); minor.")
exp("elastic-p2", 0.5 * 30 * 0.4 ** 2, "J")
exp("elastic-p3", 0.5 * 150 * 0.08 ** 2, "J")
exp("elastic-p4", 0.5 * 6000 * 0.015 ** 2, "J")
exp("elastic-p5", math.sqrt(2 * 0.9 / 20), "m")
exp("elastic-p6", math.sqrt(2 * 0.45 / 1000) * 100, "cm")
# moment
exp("moment-w", 20 * 0.5, "N m")
exp("moment-p1", 50 * 0.3, "N m")
exp("moment-p2", 8 * 0.75, "N m")
exp("moment-p3", 150 * 0.40, "N m")
exp("moment-p4", 36 / 0.9, "N")
exp("moment-p5", 2 * g * 0.25, "N m")
exp("moment-p6", 3 / (1.5 * g) * 100, "cm")
# balance
exp("balance-w", 300 * 2 / 400, "m")
exp("balance-p1", 20 * 0.3 / 0.6, "N")
exp("balance-p2", 50 * 0.4 / 80, "m")
exp("balance-p3", 6 * 25 / 15, "N")
exp("balance-p4", 40 * 1.5 / 30, "m")
exp("balance-p5", (10 * 0.2 + 5 * 0.6) / 0.5, "N")
exp("balance-p6", (300 * 1 + 200 * 2) / 350, "m")
# pressure
exp("pressure-w", 600 / 0.5, "Pa")
exp("pressure-p1", 200 / 0.4, "Pa")
exp("pressure-p2", 900 / 0.03, "Pa")
exp("pressure-p3", 50 / (20 / 1e4), "Pa",
    "REALISM: a drawing-pin head of 20 cm² is ~5 cm across (real heads are "
    "~1 cm²), and 50 N of thumb force is large.")
exp("pressure-p4", 200e3 * 0.015, "N")
exp("pressure-p5", 60 * g / 0.04, "Pa")
exp("pressure-p6", 4000 * g / (2000 / 1e4) / 1000, "kPa")
# liquid (Higher)
exp("liquid-w", 3 * 1000 * g, "Pa")
exp("liquid-p1", 2 * 1000 * g, "Pa")
exp("liquid-p2", 50 * 1030 * g, "Pa")
exp("liquid-p3", 4500 / (0.5 * g), "kg/m³")
exp("liquid-p4", 120e3 / (1000 * g), "m")
exp("liquid-p5", (15 * 1000 * g + 100e3) / 1000, "kPa")
exp("liquid-p6", 40 * 1030 * g * 0.5, "N")
# fx-graph (read from plotted coordinates)
exp("fx-graph-w", (16 - 0) / ((8 - 0) / 100), "N/m")
exp("fx-graph-p1", 6, "cm")                       # A (6,3)
exp("fx-graph-p2", 12, "N")                       # L (6,12)
exp("fx-graph-p3", 0.5 * (10 / 100) * 8, "J")
exp("fx-graph-p4", (10 - 0) / ((40 - 0) / 1000), "N/m")
exp("fx-graph-p5", 0.5 * (6 / 100) * 9, "J")
exp("fx-graph-p6", 4 / g, "kg")                   # B (8 cm, 4 N)

# ---------------------------------------------------------------------------
# Tier expectations (caller's list of Higher-only content)
# type-id -> reason it should be Higher-only
# ---------------------------------------------------------------------------
HIGHER_ONLY_TYPES = {
    "momentum": "momentum",
    "conservation-of-momentum": "momentum",
    "force-from-momentum-change": "momentum",
    "motor-force": "F = BIl",
    "turns": "transformers",
    "tx-power": "transformers",
    "standard-form": "standard form",
    "boyle": "P1V1 = P2V2",
    "liquid": "pressure in liquids",
    "background-count": "count rate with background",
}
# question-level checks: id -> reason it should carry ["Higher"]
HIGHER_ONLY_QUESTIONS = {
    "vt-graph-p5": "tangent to a curve",
    "force-graph-p5": "momentum (area under F-t)",
    "decay-graph-p6": "count rate with background",
    "rearranging-p5": "v²−u²=2ax rearrangement",
    "v2-u2-p4": "v²−u²=2ax rearrangement for u",
    "v2-u2-p6": "v²−u²=2ax rearrangement for u",
}


# ---------------------------------------------------------------------------
# Walkthrough final-line check (purely mechanical: does the last line of the
# walkthrough/steps contain the stored answer value?)
# ---------------------------------------------------------------------------
NUM_RE = re.compile(r"[-−]?\d[\d\s,]*\.?\d*(?:\s*×\s*10[⁰¹²³⁴⁵⁶⁷⁸⁹⁻]+)?")
SUP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻", "0123456789-")


def numbers_in(text):
    out = []
    for m in NUM_RE.finditer(text):
        s = m.group(0).replace("−", "-").replace(",", "").strip()
        s = re.sub(r"\s+(?=\d)", "", s)  # "52 500" -> "52500"
        s = s.strip()
        if "×" in s:
            mant, exp_ = s.split("×")
            exp_ = exp_.strip()[2:].translate(SUP)
            try:
                out.append(float(mant) * 10 ** int(exp_))
            except ValueError:
                pass
            continue
        s = s.rstrip(".")
        try:
            out.append(float(s))
        except ValueError:
            pass
    return out


def last_line_matches(lines, value):
    if not lines:
        return False
    last = lines[-1]
    nums = numbers_in(last)
    for n in nums:
        if value == 0:
            if abs(n) < 1e-9:
                return True
        elif abs(n - value) / abs(value) <= 0.01:
            return True
    return False


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    files = sorted(
        f for f in glob.glob(os.path.join(DATA, "*.json"))
        if os.path.basename(f) not in ("manifest.json", "config.json")
    )
    total = 0
    value_issues = []
    unit_issues = []
    tier_issues = []
    walk_issues = []
    missing = []
    seen = set()

    for f in files:
        d = json.load(open(f))
        topic = d["id"]
        for t in d["types"]:
            type_boards = t["boards"]
            # type-level tier check
            if t["id"] in HIGHER_ONLY_TYPES and type_boards != ["Higher"]:
                tier_issues.append(
                    f"{topic}/{t['id']}: type boards {type_boards} but content is "
                    f"Higher-only ({HIGHER_ONLY_TYPES[t['id']]})")
            qs = [("worked", t["worked"])] + [("practice", q) for q in t["practice"]]
            for kind, q in qs:
                total += 1
                qid = q["id"]
                key = qid
                # 'power-*' ids are duplicated between energy.json and
                # electricity.json; disambiguate by topic.
                if qid.startswith("power-") and topic == "energy":
                    key = "energy:" + qid
                seen.add(key)
                stored_v = q["answer"]["value"]
                stored_u = q["answer"]["unit"]
                lookup = key if key in E else qid
                if lookup not in E or (topic == "energy" and qid.startswith("power-")):
                    # energy power questions handled below with their own table
                    pass
                if topic == "energy" and qid.startswith("power-"):
                    mine = ENERGY_POWER[qid]
                elif qid in E:
                    mine = E[qid]
                else:
                    missing.append(qid)
                    continue
                my_v, my_u = mine
                # value
                if stored_v == 0:
                    ok = abs(my_v) < 1e-9
                else:
                    ok = abs(my_v - stored_v) / abs(stored_v) <= 0.01
                if not ok:
                    value_issues.append(
                        f"{qid}: stored {stored_v} {stored_u} | mine {my_v:.6g} {my_u}")
                # unit
                if my_u != stored_u:
                    unit_issues.append(
                        f"{qid}: stored unit '{stored_u}' | expected '{my_u}'")
                # walkthrough last line
                lines = q.get("walkthrough") or q.get("steps") or []
                if not last_line_matches(lines, stored_v):
                    walk_issues.append(
                        f"{qid}: last line '{lines[-1] if lines else ''}' does not "
                        f"contain stored value {stored_v}")
                # question-level tier
                q_boards = q.get("boards", type_boards)
                if qid in HIGHER_ONLY_QUESTIONS and q_boards != ["Higher"]:
                    tier_issues.append(
                        f"{qid}: boards {q_boards} but needs Higher "
                        f"({HIGHER_ONLY_QUESTIONS[qid]})")

    # report
    print(f"Files checked: {len(files)}")
    print(f"Questions checked: {total}")
    print(f"Expected-answer table entries used: {len(seen)}")
    if missing:
        print("\nNO EXPECTATION WRITTEN FOR:", missing)

    def section(title, items):
        print(f"\n=== {title} ({len(items)}) ===")
        for i in items:
            print("  -", i)

    section("VALUE DISCREPANCIES (> 1%)", value_issues)
    section("UNIT DISCREPANCIES", unit_issues)
    section("TIER TAG CONCERNS", tier_issues)
    section("WALKTHROUGH FINAL LINE vs ANSWER", walk_issues)
    print(f"\n=== NOTES (ambiguity / physics / realism / spec) ({len(NOTES)}) ===")
    for qid, ns in NOTES.items():
        for n in ns:
            print(f"  - {qid}: {n}")


# energy.json 'power' type shares ids with electricity.json 'power' type.
ENERGY_POWER = {
    "power-w": (3000 / 20, "W"),
    "power-p1": (180000 / 90, "W"),
    "power-p2": (1500 / 2.5, "W"),
    "power-p3": (2000 * 5 * 60 / 1000, "kJ"),
    "power-p4": (9000 / 60, "s"),
    "power-p5": (50 * g * 8 / 20, "W"),
    "power-p6": (1500 * 12 / 30, "W"),
}
# Electricity 'power' entries in E (above) overwrote the energy ones written
# earlier in the file; redefine the electricity ones explicitly so E is
# unambiguous.
E["power-w"] = (10 * 230, "W")
E["power-p1"] = (3 * 20, "W")
E["power-p2"] = (2 ** 2 * 12, "W")
E["power-p3"] = (1840 / 230, "A")
E["power-p4"] = (60 / 5 ** 2, "Ω")
E["power-p5"] = (230 ** 2 / 46, "W")
E["power-p6"] = (12 ** 2 / 24, "Ω")

if __name__ == "__main__":
    main()
