#!/usr/bin/env python3
"""Compute every answer for data/magnetism.json.

Run:  python3 tools/calc_magnetism.py
Copy the printed values into the JSON; never type an answer from memory.
"""

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
# Type 1: motor-force   F = B × I × l
# ---------------------------------------------------------------------------
print("# motor-force")

# Worked: 0.5 m wire, 3 A, 0.4 T
show("motor-force-w", 0.4 * 3 * 0.5, "N")

# p1: 0.4 m wire on a balance, 2.5 A, 0.1 T
show("motor-force-p1", 0.1 * 2.5 * 0.4, "N")

# p2: loudspeaker coil, 1.2 m of wire, 0.3 A, 0.5 T
show("motor-force-p2", 0.5 * 0.3 * 1.2, "N")

# p3: electromagnet gap, 0.06 N on 0.2 m carrying 1.5 A → B
show("motor-force-p3", 0.06 / (1.5 * 0.2), "T")

# p4: toy car motor, 8 cm of wire, 5 A, 0.15 T → F
l_p4 = 8 / 100
show("motor-force-p4", 0.15 * 5 * l_p4, "N")

# p5: crane motor, 30 cm of wire, 0.2 T, 0.12 N → l in m first, then I
l_p5 = 30 / 100
show("motor-force-p5", 0.12 / (0.2 * l_p5), "A")

# p6: model train, 6 V across 2 Ω of wire → I first, then F with 0.1 T and 0.5 m
i_p6 = 6 / 2
show("motor-force-p6", 0.1 * i_p6 * 0.5, "N")


# ---------------------------------------------------------------------------
# Type 2: transformer-turns   V_p / V_s = N_p / N_s
# ---------------------------------------------------------------------------
print("# transformer-turns")

# Worked: mains adapter, 230 V, 2300 primary turns, 120 secondary turns → V_s
show("turns-w", 230 * 120 / 2300, "V")

# p1: lab step-up, 12 V, 100 primary turns, 500 secondary turns → V_s
show("turns-p1", 12 * 500 / 100, "V")

# p2: phone charger, 230 V, 1150 primary turns, 25 secondary turns → V_s
show("turns-p2", 230 * 25 / 1150, "V")

# p3: doorbell, 230 V to 8 V with 920 primary turns → N_s
show("turns-p3", 920 * 8 / 230, "turns")

# p4: laptop charger, 230 V to 20 V with 40 secondary turns → N_p
show("turns-p4", 40 * 230 / 20, "turns")

# p5: power-station step-up, 25 kV to 400 kV with 1500 primary turns → N_s
show("turns-p5", 1500 * 400 / 25, "turns")

# p6: model railway controller, 2000 turns in total, 1600 on the primary, 230 V → N_s first, then V_s
n_s_p6 = 2000 - 1600
show("turns-p6", 230 * n_s_p6 / 1600, "V")


# ---------------------------------------------------------------------------
# Type 3: transformer-power   V_p × I_p = V_s × I_s
# ---------------------------------------------------------------------------
print("# transformer-power")

# Worked: 230 V, 0.5 A primary; 23 V secondary → I_s
show("tx-power-w", 230 * 0.5 / 23, "A")

# p1: lab step-up, 12 V, 2 A primary; 48 V secondary → I_s
show("tx-power-p1", 12 * 2 / 48, "A")

# p2: games console adapter, 230 V primary; 11.5 V, 6 A secondary → I_p
show("tx-power-p2", 11.5 * 6 / 230, "A")

# p3: phone charger, 230 V, 20 mA primary; 5 V secondary → I_s in A
i_p_p3 = 20 / 1000
show("tx-power-p3", 230 * i_p_p3 / 5, "A")

# p4: halogen lights, 230 V, 0.2 A primary; 4 A secondary → V_s
show("tx-power-p4", 230 * 0.2 / 4, "V")

# p5: garden lights, 230 V, 1000:50 turns, 2 A secondary → V_s first, then I_p
v_s_p5 = 230 * 50 / 1000
show("tx-power-p5", v_s_p5 * 2 / 230, "A")

# p6: lab step-up on 12 V a.c., 60:1200 turns, 5 A primary → V_s first, then I_s
v_s_p6 = 12 * 1200 / 60
show("tx-power-p6", 12 * 5 / v_s_p6, "A")


# ---------------------------------------------------------------------------
# Type 4: transmission-loss   P = I² × R  (and P = I × V to find the current)
# ---------------------------------------------------------------------------
print("# transmission-loss")

# Worked: 5 Ω of cable, 20 A
show("loss-w", 20 ** 2 * 5, "W")

# p1: overhead line to a farm, 0.5 Ω, 40 A
show("loss-p1", 40 ** 2 * 0.5, "W")

# p2: 10 Ω line, 50 A
show("loss-p2", 50 ** 2 * 10, "W")

# p3: wind-turbine cable, 1800 W lost in 2 Ω → I
show("loss-p3", math.sqrt(1800 / 2), "A")

# p4: 0.05 Ω per km, 20 km, 60 A → R first, then loss
r_p4 = 0.05 * 20
show("loss-p4", 60 ** 2 * r_p4, "W")

# p5: 100 kW sent at 2000 V through 4 Ω → I first, then loss in kW
p_p5 = 100 * 1000
i_p5 = p_p5 / 2000
show("loss-p5", i_p5 ** 2 * 4 / 1000, "kW")

# p6: 60 kW sent at 400 V through 0.4 Ω; then stepped up to 4000 V → new loss
p_p6 = 60 * 1000
i_before = p_p6 / 400
loss_before = i_before ** 2 * 0.4
print("loss-p6 (before step-up, for the walkthrough):", sig3(loss_before), "W")
i_after = p_p6 / 4000
show("loss-p6", i_after ** 2 * 0.4, "W")
