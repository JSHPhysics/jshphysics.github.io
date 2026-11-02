#!/usr/bin/env python3
"""Compute every answer and every plotted coordinate for data/electricity.json.

Run:  python3 tools/calc_electricity.py
Copy the printed values into the JSON; never type an answer from memory.
"""

import json
import math


def sig3(value):
    """Round a number to three significant figures (integers stay exact)."""
    if value == 0:
        return 0
    magnitude = math.floor(math.log10(abs(value)))
    scale = 10 ** (magnitude - 2)
    rounded = round(value / scale) * scale
    # Return an int when the value is a whole number, so JSON stays tidy
    if abs(rounded - round(rounded)) < 1e-9:
        return int(round(rounded))
    return round(rounded, 10)


def show(question_id, value, unit):
    """Print one answer line."""
    print(f"{question_id:22s} {sig3(value)} {unit}")


# ---------------------------------------------------------------------------
# Type 1: charge-current-time   Q = I × t
# ---------------------------------------------------------------------------
print("# charge-current-time")

# Worked: torch bulb, 0.25 A for 2 minutes
t_w = 2 * 60
show("charge-w", 0.25 * t_w, "C")

# p1: kettle, 8 A for 150 s
show("charge-p1", 8 * 150, "C")

# p2: car starter motor, 120 A for 3 s
show("charge-p2", 120 * 3, "C")

# p3: hair dryer, 450 C in 90 s → I
show("charge-p3", 450 / 90, "A")

# p4: LED, 20 mA for 5 minutes → Q
i_p4 = 20 / 1000
t_p4 = 5 * 60
show("charge-p4", i_p4 * t_p4, "C")

# p5: smoke alarm, 0.9 C in 2.5 minutes → I in mA
t_p5 = 2.5 * 60
i_p5 = 0.9 / t_p5
show("charge-p5", i_p5 * 1000, "mA")

# p6: 12 Ω heater on 24 V for 3 minutes → I first, then Q
i_p6 = 24 / 12
t_p6 = 3 * 60
show("charge-p6", i_p6 * t_p6, "C")


# ---------------------------------------------------------------------------
# Type 2: pd-current-resistance   V = I × R
# ---------------------------------------------------------------------------
print("# pd-current-resistance")

# Worked: buzzer, 0.5 A through 6 Ω
show("ohm-w", 0.5 * 6, "V")

# p1: car headlamp, 4 A through 3 Ω
show("ohm-p1", 4 * 3, "V")

# p2: toy motor, 0.3 A through 20 Ω
show("ohm-p2", 0.3 * 20, "V")

# p3: kettle, 230 V and 10 A → R
show("ohm-p3", 230 / 10, "Ω")

# p4: 2.2 kΩ resistor carrying 5 mA → V
r_p4 = 2.2 * 1000
i_p4 = 5 / 1000
show("ohm-p4", i_p4 * r_p4, "V")

# p5: 9 V battery across 1.5 kΩ → I in mA
r_p5 = 1.5 * 1000
i_p5 = 9 / r_p5
show("ohm-p5", i_p5 * 1000, "mA")

# p6: 90 C in 30 s through 4 Ω → I first, then V
i_p6 = 90 / 30
show("ohm-p6", i_p6 * 4, "V")


# ---------------------------------------------------------------------------
# Type 3: energy-charge-pd   E = Q × V
# ---------------------------------------------------------------------------
print("# energy-charge-pd")

# Worked: 20 C through a 12 V car battery
show("eqv-w", 20 * 12, "J")

# p1: 1.5 V cell, 40 C
show("eqv-p1", 40 * 1.5, "J")

# p2: 230 V mains, 50 C through a hair dryer
show("eqv-p2", 50 * 230, "J")

# p3: motorbike battery, 900 J by 75 C → V
show("eqv-p3", 900 / 75, "V")

# p4: lantern battery, 3 kJ at 6 V → Q
e_p4 = 3 * 1000
show("eqv-p4", e_p4 / 6, "C")

# p5: games console, 230 V, 0.5 A for 20 minutes → Q first, then E
t_p5 = 20 * 60
q_p5 = 0.5 * t_p5
show("eqv-p5", q_p5 * 230, "J")

# p6: bicycle dynamo lamp, 0.2 A for 2 minutes transfers 72 J → Q first, then V
t_p6 = 2 * 60
q_p6 = 0.2 * t_p6
show("eqv-p6", 72 / q_p6, "V")


# ---------------------------------------------------------------------------
# Type 4: electrical-power   P = I × V  and  P = I² × R
# ---------------------------------------------------------------------------
print("# electrical-power")

# Worked: kettle, 230 V, 10 A
show("power-w", 10 * 230, "W")

# p1: laptop charger, 20 V, 3 A
show("power-p1", 3 * 20, "W")

# p2: toaster element, 2 A through 12 Ω
show("power-p2", 2 ** 2 * 12, "W")

# p3: 1.84 kW fan heater on 230 V → I
p_p3 = 1.84 * 1000
show("power-p3", p_p3 / 230, "A")

# p4: car rear-window heater, 5 A, 60 W → R
show("power-p4", 60 / 5 ** 2, "Ω")

# p5: 230 V immersion heater of 46 Ω → I first, then P
i_p5 = 230 / 46
show("power-p5", i_p5 * 230, "W")

# p6: lamp rated 24 W at 12 V → I first, then R
i_p6 = 24 / 12
show("power-p6", 12 / i_p6, "Ω")


# ---------------------------------------------------------------------------
# Type 5: energy-power-time   E = P × t  and  E = I × V × t
# ---------------------------------------------------------------------------
print("# energy-power-time")

# Worked: 2 kW kettle for 3 minutes
p_w = 2 * 1000
t_w = 3 * 60
show("ept-w", p_w * t_w, "J")

# p1: 60 W desk lamp for 50 s
show("ept-p1", 60 * 50, "J")

# p2: television, 230 V, 0.5 A, 40 s
show("ept-p2", 0.5 * 230 * 40, "J")

# p3: microwave, 90 kJ in 2 minutes → P
e_p3 = 90 * 1000
t_p3 = 2 * 60
show("ept-p3", e_p3 / t_p3, "W")

# p4: 1.5 kW heater transfers 450 kJ → t in minutes
p_p4 = 1.5 * 1000
e_p4 = 450 * 1000
t_p4 = e_p4 / p_p4
show("ept-p4", t_p4 / 60, "minutes")

# p5: 12 Ω element, 5 A, 4 minutes → P first (I²R), then E
p_p5 = 5 ** 2 * 12
t_p5 = 4 * 60
show("ept-p5", p_p5 * t_p5, "J")

# p6: phone charger, 5 V, 2 A, 1.5 hours → P first, then E in kJ
p_p6 = 2 * 5
t_p6 = 1.5 * 3600
show("ept-p6", p_p6 * t_p6 / 1000, "kJ")


# ---------------------------------------------------------------------------
# Type 6: series-parallel
# ---------------------------------------------------------------------------
print("# series-parallel")

# Worked: 3 Ω and 9 Ω in series on 6 V → total R, then I
r_w = 3 + 9
show("circuits-w", 6 / r_w, "A")

# p1: 5 Ω, 15 Ω and 20 Ω in series → total R
show("circuits-p1", 5 + 15 + 20, "Ω")

# p2: two sidelights in parallel, 0.3 A and 0.5 A → battery current
show("circuits-p2", 0.3 + 0.5, "A")

# p3: series circuit current 0.2 A, 30 Ω resistor → p.d. across it
show("circuits-p3", 0.2 * 30, "V")

# p4: two LEDs in parallel, 15 mA and 25 mA → total current in A
show("circuits-p4", (15 + 25) / 1000, "A")

# p5 (Higher): 12 V, 8 Ω and 16 Ω in series → I first, then p.d. across 16 Ω
i_p5 = 12 / (8 + 16)
show("circuits-p5", i_p5 * 16, "V")

# p6 (Higher): 6 V, 3 Ω and 6 Ω in parallel → each branch current, then total
i_branch_a = 6 / 3
i_branch_b = 6 / 6
show("circuits-p6", i_branch_a + i_branch_b, "A")


# ---------------------------------------------------------------------------
# Type 7: iv-graph   every question carries a graph
# ---------------------------------------------------------------------------
print("# iv-graph")


def sample(function, xs):
    """Sample a function at the given x values, rounding to 3 s.f."""
    points = []
    for x in xs:
        y = function(x)
        points.append([sig3(x), sig3(y)])
    return points


# Worked: resistor, straight line through (8, 2); X at (6, 1.5)
show("iv-graph-w", 6 / 1.5, "Ω")

# p1: resistor, straight line to (5, 1.0); X at (4, 0.8)
show("iv-graph-p1", 4 / 0.8, "Ω")

# p2: resistor, straight line to (10, 0.4); X at (5, 0.2)
show("iv-graph-p2", 5 / 0.2, "Ω")

# p3: resistor with a mA axis, line to (4, 80); X at (3 V, 60 mA)
i_p3 = 60 / 1000
show("iv-graph-p3", 3 / i_p3, "Ω")

# p4: filament lamp, saturating exponential I = 3.2 × (1 − e^(−V / V0)), X at (6, 2)
# V0 is chosen so that I(6) = 3.2 × (1 − 3/8) = 2 exactly
LAMP_SATURATION = 3.2
LAMP_V0 = 6 / math.log(8 / 3)


def lamp(v):
    """Filament lamp curve: finite slope at the origin, flattening as the filament heats."""
    return LAMP_SATURATION * (1 - math.exp(-v / LAMP_V0))


lamp_xs = [0, 0.5, 1, 1.5, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lamp_points = sample(lamp, lamp_xs)
print("lamp points:", json.dumps(lamp_points))
show("iv-graph-p4", 6 / lamp(6), "Ω")

# p5: diode, exponential rise I = a × (e^(bV) − 1) mA with b = 12; a is chosen so I(0.7) = 20 exactly
DIODE_B = 12
DIODE_A = 20 / (math.exp(DIODE_B * 0.7) - 1)


def diode(v):
    """Diode curve in mA: almost nothing at low p.d., then a steep exponential rise."""
    return DIODE_A * (math.exp(DIODE_B * v) - 1)


diode_xs = [round(0.05 * index, 2) for index in range(0, 17)]
diode_points = sample(diode, diode_xs)
print("diode points:", json.dumps(diode_points))
show("iv-graph-p5", diode(0.7), "mA")

# p6: thermistor, R = 10 × 0.2^(θ / 40) kΩ; read at 40 °C, answer in Ω
def thermistor(theta):
    """Thermistor curve in kΩ: exponential fall, exactly 2 kΩ at 40 °C."""
    return 10 * 0.2 ** (theta / 40)


thermistor_xs = list(range(0, 65, 5))
thermistor_points = sample(thermistor, thermistor_xs)
print("thermistor points:", json.dumps(thermistor_points))
show("iv-graph-p6", thermistor(40) * 1000, "Ω")
