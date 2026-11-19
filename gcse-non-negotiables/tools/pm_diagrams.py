"""
pm_diagrams.py — the diagrams for Topic 14 (Particle model) as inline
SVG, drawn with the helpers in le_diagrams.py, fe_diagrams.py and
mg_diagrams.py.

    states_svg()      the three states: arrangement and movement
    density_svg()     the density practical: block, displacement, liquid
    pressure_svg()    gas pressure from collisions: cold and hot
    boyle_svg()       a gas compressed at constant temperature
    kelvin_svg()      the Celsius and kelvin scales side by side
    shc_svg()         the specific-heat-capacity practical
"""

from math import cos, radians, sin

from le_diagrams import ACCENT, INK, INK2, LINE, dashed, solid, text
from fe_diagrams import arrow, box, dot
from mg_diagrams import head, path


def particle(x, y, r=6, colour=INK, fill=0.25):
    return "<circle cx='%.1f' cy='%.1f' r='%s' style='fill:%s;fill-opacity:%s;stroke:%s;stroke-width:1.4'/>" % (x, y, r, colour, fill, colour)


def motion_arrow(x, y, angle_deg, length=14, colour=ACCENT):
    a = radians(angle_deg)
    x2 = x + length * cos(a)
    y2 = y + length * sin(a)
    return arrow(x, y, x2, y2, colour, 1.6)


# ---------------------------------------------------------------------

def states_svg():
    svg = ""
    panels = [(110, "solid"), (330, "liquid"), (550, "gas")]
    for cx, state in panels:
        svg += "<rect x='%d' y='40' width='170' height='160' rx='6' style='fill:none;stroke:%s;stroke-width:1.6'/>" % (cx - 85, INK2)
        svg += text(cx, 26, state, 13, INK, weight="bold")
    # solid: regular lattice, touching, small vibration arrows
    for row in range(5):
        for col in range(6):
            x = 110 - 85 + 22 + col * 25
            y = 40 + 22 + row * 28
            svg += particle(x, y, 10)
    svg += motion_arrow(110 - 85 + 22 + 2 * 25 + 11, 40 + 22 + 2 * 28, 0, 9)
    svg += motion_arrow(110 - 85 + 22 + 2 * 25 - 11, 40 + 22 + 2 * 28, 180, 9)
    svg += text(110, 222, "regular, touching, fixed positions", 11, INK2)
    svg += text(110, 238, "vibrate about fixed positions", 11, INK2)
    # liquid: irregular, touching, curved arrows
    liquid_points = [(262, 70), (286, 66), (312, 74), (340, 64), (366, 72), (390, 68), (268, 96), (294, 100), (320, 94), (350, 100), (378, 96), (400, 92),
                     (258, 126), (284, 128), (310, 122), (338, 130), (364, 124), (392, 122), (266, 154), (292, 150), (322, 156), (352, 150), (380, 158), (404, 150),
                     (276, 182), (302, 178), (332, 184), (360, 178), (390, 182)]
    for x, y in liquid_points:
        svg += particle(x, y, 10)
    svg += motion_arrow(330, 130, 20, 22)
    svg += motion_arrow(300, 100, 200, 22)
    svg += text(330, 222, "irregular, touching, no fixed positions", 11, INK2)
    svg += text(330, 238, "move around and flow over each other", 11, INK2)
    # gas: few, far apart, fast straight arrows in all directions
    gas_points = [(490, 70, 30), (590, 60, 160), (545, 110, 250), (610, 130, 300), (480, 150, 80), (560, 170, 10), (515, 190, 140)]
    for x, y, angle in gas_points:
        svg += particle(x, y, 9)
        svg += motion_arrow(x + 9 * cos(radians(angle)), y + 9 * sin(radians(angle)), angle, 24)
    svg += text(550, 222, "random, far apart, no arrangement", 11, INK2)
    svg += text(550, 238, "move fast in straight lines in all directions", 11, INK2)
    return svg


def density_svg():
    svg = ""
    # left: regular block with a ruler, on a balance
    svg += text(120, 22, "regular solid", 12, INK)
    svg += "<rect x='60' y='70' width='120' height='70' style='fill:var(--line);fill-opacity:0.35;stroke:%s;stroke-width:1.6'/>" % INK
    svg += solid(60, 155, 180, 155, INK2, 1.2)
    for i in range(0, 13):
        svg += solid(60 + i * 10, 155, 60 + i * 10, 150 if i % 5 else 146, INK2, 1)
    svg += text(120, 172, "ruler: length, width, height", 10, INK2)
    svg += "<rect x='70' y='190' width='100' height='28' rx='4' style='fill:none;stroke:%s;stroke-width:1.4'/>" % INK2
    svg += text(120, 208, "balance: mass", 10, INK2)
    svg += text(120, 244, "V = l × w × h", 11, INK2)
    # middle: measuring cylinder before and after
    svg += text(340, 22, "irregular solid", 12, INK)
    for x0, level, label_text in ((280, 150, "before"), (360, 118, "after")):
        svg += "<path d='M %d 60 L %d 220 Q %d 232 %d 232 Q %d 232 %d 220 L %d 60' style='fill:none;stroke:%s;stroke-width:1.6'/>" % (x0, x0, x0, x0 + 20, x0 + 40, x0 + 40, x0 + 40, INK)
        svg += "<rect x='%d' y='%d' width='40' height='%d' style='fill:var(--accent);fill-opacity:0.18'/>" % (x0, level, 220 - level)
        for i in range(0, 9):
            svg += solid(x0, 70 + i * 18, x0 + 8 if i % 2 else x0 + 12, 70 + i * 18, INK2, 1)
        svg += text(x0 + 20, 250, label_text, 10, INK2)
    # the stone in the second cylinder
    svg += "<path d='M 372 205 l 10 -12 l 14 6 l 2 14 l -16 8 z' style='fill:var(--ink-2);fill-opacity:0.5;stroke:%s;stroke-width:1.2'/>" % INK
    svg += dashed(320, 150, 360, 150, LINE)
    svg += dashed(320, 118, 360, 118, LINE)
    svg += text(342, 138, "rise = V", 10, ACCENT)
    svg += text(340, 290, "volume = after − before (the whole object under the water)", 10, INK2)
    # right: liquid in a cylinder on a balance
    svg += text(560, 22, "liquid", 12, INK)
    x0 = 540
    svg += "<path d='M %d 60 L %d 200 Q %d 212 %d 212 Q %d 212 %d 200 L %d 60' style='fill:none;stroke:%s;stroke-width:1.6'/>" % (x0, x0, x0, x0 + 20, x0 + 40, x0 + 40, x0 + 40, INK)
    svg += "<rect x='%d' y='120' width='40' height='80' style='fill:var(--accent);fill-opacity:0.18'/>" % x0
    svg += "<rect x='510' y='222' width='100' height='26' rx='4' style='fill:none;stroke:%s;stroke-width:1.4'/>" % INK2
    svg += text(560, 239, "balance", 10, INK2)
    svg += text(560, 262, "mass of cylinder + liquid − empty cylinder;", 10, INK2)
    svg += text(560, 276, "volume read off the scale", 10, INK2)
    return svg


def pressure_svg():
    svg = ""
    for cx, title, speed, note in ((170, "cold gas", 14, "slower particles: fewer, gentler collisions each second"), (500, "hot gas, same volume", 26, "faster particles: more frequent, harder collisions")):
        svg += text(cx, 22, title, 12, INK)
        svg += "<rect x='%d' y='40' width='220' height='170' rx='4' style='fill:none;stroke:%s;stroke-width:2'/>" % (cx - 110, INK)
        pts = [(-70, 30, 200), (-20, 60, 320), (40, 25, 40), (80, 70, 150), (-60, 110, 80), (10, 120, 260), (60, 140, 10), (-30, 150, 330)]
        for dx, dy, angle in pts:
            x = cx + dx
            y = 40 + dy
            svg += particle(x, y, 7)
            svg += motion_arrow(x + 7 * cos(radians(angle)), y + 7 * sin(radians(angle)), angle, speed)
        # a collision arrow on the right wall: force outwards
        svg += arrow(cx + 112, 125, cx + 140, 125, ACCENT, 2.4)
        svg += text(cx + 128, 112, "force", 10, ACCENT)
        svg += text(cx, 236, note, 11, INK2)
    svg += text(335, 262, "pressure = the force of the collisions per unit area of the walls, at right angles to the wall", 11, INK2)
    return svg


def boyle_svg():
    svg = ""
    for cx, title, width, count, pressure in ((170, "volume V, pressure P", 200, 10, "P"), (500, "volume V ÷ 2, pressure 2P", 100, 10, "2P")):
        svg += text(cx, 22, title, 12, INK)
        x0 = cx - 110
        svg += "<rect x='%d' y='50' width='%d' height='150' style='fill:none;stroke:%s;stroke-width:2'/>" % (x0, width, INK)
        # piston
        svg += "<rect x='%d' y='48' width='10' height='154' style='fill:var(--ink-2);fill-opacity:0.6;stroke:%s;stroke-width:1.2'/>" % (x0 + width, INK)
        svg += solid(x0 + width + 10, 125, x0 + width + 60, 125, INK, 4)
        if width < 150:
            svg += arrow(x0 + width + 90, 125, x0 + width + 62, 125, ACCENT, 2.4)
            svg += text(x0 + width + 110, 112, "pushed in", 10, ACCENT)
        # the same particles, closer together
        pts = [(0.15, 0.2, 30), (0.5, 0.15, 200), (0.85, 0.3, 120), (0.3, 0.5, 300), (0.7, 0.55, 20), (0.1, 0.8, 80), (0.45, 0.85, 250), (0.9, 0.8, 160), (0.6, 0.35, 340), (0.25, 0.65, 190)]
        for fx, fy, angle in pts:
            x = x0 + 12 + fx * (width - 24)
            y = 50 + 12 + fy * 126
            svg += particle(x, y, 6)
            svg += motion_arrow(x + 6 * cos(radians(angle)), y + 6 * sin(radians(angle)), angle, 12)
        svg += text(cx, 226, "same number of particles, same speed (same temperature)", 10, INK2)
    svg += text(335, 254, "half the volume: each particle hits the walls twice as often, so the pressure doubles — P₁V₁ = P₂V₂", 11, INK2)
    return svg


def kelvin_svg():
    svg = ""
    svg += text(330, 22, "the two temperature scales", 12, INK)
    # two vertical scales
    y_top, y_bot = 50, 230
    span = 400  # kelvin from 0 to 400
    def y_of_k(k):
        return y_bot - (k / span) * (y_bot - y_top)
    for x, label_text, offset, unit in ((230, "Celsius", -273, "°C"), (430, "kelvin", 0, "K")):
        svg += solid(x, y_top, x, y_bot, INK, 2)
        svg += text(x, 44, label_text, 11, INK)
        for k, kl in ((0, "0 K"), (273, "273 K"), (373, "373 K")):
            yy = y_of_k(k)
            svg += solid(x - 8, yy, x + 8, yy, INK, 1.6)
            value = k + offset
            lab = (("%d %s" % (value, unit)).replace("-", "\u2212")) if unit == "°C" else kl
            svg += text(x - 14 if unit == "°C" else x + 14, yy + 4, lab, 11, INK2, anchor="end" if unit == "°C" else "start")
    for k, name in ((0, "absolute zero"), (273, "ice melts"), (373, "water boils")):
        yy = y_of_k(k)
        svg += dashed(238, yy, 422, yy, LINE)
        svg += text(330, yy - 5, name, 10, INK2)
    svg += text(330, 258, "K = °C + 273 · °C = K − 273 · a change of 1 °C is a change of 1 K", 11, INK2)
    return svg


def shc_svg():
    svg = ""
    svg += text(330, 22, "finding the specific heat capacity of water", 12, INK)
    # beaker with lagging
    svg += "<rect x='230' y='70' width='160' height='150' rx='4' style='fill:var(--line);fill-opacity:0.25;stroke:%s;stroke-width:1.4;stroke-dasharray:5 3'/>" % INK2
    svg += "<path d='M 250 70 L 250 210 L 370 210 L 370 70' style='fill:none;stroke:%s;stroke-width:1.8'/>" % INK
    svg += "<rect x='251' y='100' width='118' height='109' style='fill:var(--accent);fill-opacity:0.15'/>"
    svg += text(310, 236, "insulation (lagging) round and under the beaker", 10, INK2)
    # heater: a rod with a coil at the bottom
    svg += solid(290, 40, 290, 180, INK, 3)
    for i in range(4):
        svg += "<ellipse cx='290' cy='%d' rx='12' ry='4' style='fill:none;stroke:%s;stroke-width:1.6'/>" % (160 + i * 7, INK)
    svg += text(236, 60, "immersion heater", 10, INK2, anchor="end")
    svg += solid(240, 57, 286, 57, LINE)
    # thermometer
    svg += "<rect x='334' y='40' width='8' height='150' rx='4' style='fill:none;stroke:%s;stroke-width:1.4'/>" % INK
    svg += "<rect x='336' y='120' width='4' height='68' style='fill:var(--accent)'/>"
    svg += text(352, 60, "thermometer", 10, INK2, anchor="start")
    # stirrer label and leads to the joulemeter
    svg += solid(290, 40, 290, 30, INK, 1.4)
    svg += solid(290, 30, 470, 30, INK2, 1.4)
    svg += solid(470, 30, 470, 70, INK2, 1.4)
    svg += "<rect x='430' y='70' width='80' height='44' rx='4' style='fill:none;stroke:%s;stroke-width:1.6'/>" % INK
    svg += text(470, 90, "joulemeter", 10, INK)
    svg += text(470, 104, "(or V, I and t)", 9, INK2)
    svg += solid(470, 114, 470, 150, INK2, 1.4)
    svg += text(470, 166, "power supply", 10, INK2)
    # balance note
    svg += text(140, 100, "measure first:", 10, INK)
    svg += text(140, 116, "mass of water", 10, INK2)
    svg += text(140, 130, "(balance)", 10, INK2)
    svg += text(140, 160, "start temperature", 10, INK2)
    svg += text(330, 262, "energy in (J) and temperature rise (°C): c = ΔQ ÷ (m × Δθ)", 11, INK2)
    return svg
