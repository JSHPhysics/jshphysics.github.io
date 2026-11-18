"""
el_diagrams.py — the diagrams for Topic 10 (Electricity and circuits) as
inline SVG. Circuit symbols are drawn by small helpers so every circuit
on the page uses the same symbols as the symbol chart.

    symbols_svg()        the twelve spec symbols (10.2) in a grid
    meters_svg()         ammeter in series, voltmeter in parallel, with a lamp
    series_parallel_svg() two lamps in series and two in parallel
    iv_practical_svg()   the core-practical circuit (10.17a)
    test_circuits_svg()  the series and parallel test circuits (10.17b)
    plug_svg()           a UK plug: live, neutral, earth, fuse
    ac_dc_svg()          d.c. and a.c. traces against time
    sensing_svg()        an LDR in series with a fixed resistor (pd sharing)
"""

from math import cos, radians, sin

from le_diagrams import ACCENT, INK, INK2, LINE, dashed, solid, text

W = 1.8  # wire width


def wire(x1, y1, x2, y2, colour=INK):
    return solid(x1, y1, x2, y2, colour, W)


def wires(points, colour=INK):
    svg = ""
    for index in range(len(points) - 1):
        svg += wire(points[index][0], points[index][1], points[index + 1][0], points[index + 1][1], colour)
    return svg


def circle(cx, cy, r, letter=None, fill="var(--bg)"):
    svg = "<circle cx='%.1f' cy='%.1f' r='%s' style='fill:%s;stroke:var(--ink);stroke-width:%s'/>" % (cx, cy, r, fill, W)
    if letter:
        svg += text(cx, cy + 5, letter, 13, INK, "middle", "600")
    return svg


def rect(x, y, w, h, fill="var(--bg)"):
    return "<rect x='%.1f' y='%.1f' width='%.1f' height='%.1f' style='fill:%s;stroke:var(--ink);stroke-width:%s'/>" % (x, y, w, h, fill, W)


# --- symbols, all drawn horizontally centred on (cx, cy), 40 px long ---

def cell(cx, cy, long_left=True):
    """A cell: the long thin line is the positive terminal."""
    svg = wire(cx - 20, cy, cx - 5, cy) + wire(cx + 5, cy, cx + 20, cy)
    if long_left:
        svg += solid(cx - 5, cy - 14, cx - 5, cy + 14, INK, 1.6)
        svg += solid(cx + 5, cy - 7, cx + 5, cy + 7, INK, 4)
    else:
        svg += solid(cx - 5, cy - 7, cx - 5, cy + 7, INK, 4)
        svg += solid(cx + 5, cy - 14, cx + 5, cy + 14, INK, 1.6)
    return svg


def battery(cx, cy):
    svg = wire(cx - 24, cy, cx - 13, cy) + wire(cx + 13, cy, cx + 24, cy)
    svg += solid(cx - 13, cy - 14, cx - 13, cy + 14, INK, 1.6)
    svg += solid(cx - 5, cy - 7, cx - 5, cy + 7, INK, 4)
    svg += wire(cx - 5, cy, cx + 5, cy)
    svg += solid(cx + 5, cy - 14, cx + 5, cy + 14, INK, 1.6)
    svg += solid(cx + 13, cy - 7, cx + 13, cy + 7, INK, 4)
    return svg


def switch_open(cx, cy):
    svg = wire(cx - 22, cy, cx - 10, cy) + wire(cx + 10, cy, cx + 22, cy)
    svg += circle(cx - 10, cy, 2.5, None, "var(--ink)") + circle(cx + 10, cy, 2.5, None, "var(--ink)")
    svg += wire(cx - 10, cy, cx + 8, cy - 14)
    return svg


def lamp(cx, cy):
    r = 11
    svg = wire(cx - 22, cy, cx - r, cy) + wire(cx + r, cy, cx + 22, cy)
    svg += circle(cx, cy, r)
    d = r * 0.7071
    svg += wire(cx - d, cy - d, cx + d, cy + d) + wire(cx - d, cy + d, cx + d, cy - d)
    return svg


def resistor(cx, cy):
    return wire(cx - 24, cy, cx - 16, cy) + rect(cx - 16, cy - 7, 32, 14) + wire(cx + 16, cy, cx + 24, cy)


def variable_resistor(cx, cy):
    svg = resistor(cx, cy)
    svg += wire(cx - 16, cy + 13, cx + 16, cy - 13)
    # arrowhead
    svg += "<polygon points='%.1f,%.1f %.1f,%.1f %.1f,%.1f' style='fill:var(--ink)'/>" % (cx + 18, cy - 15, cx + 9, cy - 13, cx + 15, cy - 6)
    return svg


def meter(cx, cy, letter):
    return wire(cx - 24, cy, cx - 12, cy) + circle(cx, cy, 12, letter) + wire(cx + 12, cy, cx + 24, cy)


def motor(cx, cy):
    return meter(cx, cy, "M")


def diode(cx, cy):
    svg = wire(cx - 22, cy, cx - 9, cy) + wire(cx + 9, cy, cx + 22, cy)
    svg += "<polygon points='%.1f,%.1f %.1f,%.1f %.1f,%.1f' style='fill:var(--bg);stroke:var(--ink);stroke-width:%s'/>" % (cx - 9, cy - 9, cx - 9, cy + 9, cx + 9, cy, W)
    svg += solid(cx + 9, cy - 9, cx + 9, cy + 9, INK, W)
    return svg


def led(cx, cy):
    svg = diode(cx, cy)
    for dy in (0, 7):
        svg += solid(cx + 2, cy - 12 - dy, cx + 12, cy - 22 - dy, INK, 1.4)
        svg += "<polygon points='%.1f,%.1f %.1f,%.1f %.1f,%.1f' style='fill:var(--ink)'/>" % (cx + 13, cy - 23 - dy, cx + 7, cy - 21 - dy, cx + 11, cy - 17 - dy)
    return svg


def thermistor(cx, cy):
    svg = resistor(cx, cy)
    svg += solid(cx - 22, cy + 16, cx - 14, cy + 16, INK, 1.6)
    svg += solid(cx - 14, cy + 16, cx + 12, cy - 12, INK, 1.6)
    return svg


def ldr(cx, cy):
    svg = resistor(cx, cy)
    for dx in (0, 8):
        svg += solid(cx - 14 + dx, cy - 26, cx - 4 + dx, cy - 13, INK, 1.4)
        svg += "<polygon points='%.1f,%.1f %.1f,%.1f %.1f,%.1f' style='fill:var(--ink)'/>" % (cx - 3 + dx, cy - 12, cx - 9 + dx, cy - 14, cx - 5 + dx, cy - 19)
    return svg


# ---------------------------------------------------------------------

def symbols_svg():
    items = [
        ("cell", cell), ("battery", battery), ("switch (open)", switch_open), ("lamp", lamp),
        ("resistor", resistor), ("variable resistor", variable_resistor), ("ammeter", lambda x, y: meter(x, y, "A")), ("voltmeter", lambda x, y: meter(x, y, "V")),
        ("motor", motor), ("diode", diode), ("LED", led), ("thermistor", thermistor),
        ("LDR", ldr),
    ]
    svg = ""
    for index, (name, draw) in enumerate(items):
        col = index % 4
        row = index // 4
        cx = 85 + col * 160
        cy = 45 + row * 80
        svg += draw(cx, cy)
        svg += text(cx, cy + 36, name, 11, INK2)
    svg += text(405, 345, "a diode lets current pass in the direction of the arrow only; the LED is a diode that lights when it conducts", 10.5, INK2)
    return svg


def meters_svg():
    """A cell driving a lamp: ammeter in series with the lamp, voltmeter
    across it."""
    svg = ""
    # loop: top wire y=40, bottom y=150, left x=60, right x=360
    svg += wires([(60, 150), (60, 40), (150, 40)])
    svg += cell(170, 40)
    svg += wire(190, 40, 360, 40)
    svg += wire(360, 40, 360, 150)
    svg += wire(360, 150, 260, 150)
    svg += meter(236, 150, "A")
    svg += wire(212, 150, 170, 150)
    svg += lamp(148, 150)
    svg += wire(126, 150, 60, 150)
    # voltmeter across the lamp
    svg += wire(126, 150, 126, 215) + wire(170, 150, 170, 215)
    svg += wire(126, 215, 124, 215) + meter(148, 215, "V")
    svg += text(300, 182, "ammeter in series: the current", 11, INK2)
    svg += text(300, 196, "through the lamp passes through it", 11, INK2)
    svg += text(148, 250, "voltmeter in parallel: across the lamp", 11, INK2)
    svg += text(420, 90, "The voltmeter has a very high resistance,", 11, INK, "start")
    svg += text(420, 106, "so almost no current goes through it;", 11, INK, "start")
    svg += text(420, 122, "the ammeter has a very low resistance,", 11, INK, "start")
    svg += text(420, 138, "so it does not change the current it measures.", 11, INK, "start")
    svg += text(420, 170, "Never put a voltmeter in series", 11, ACCENT, "start")
    svg += text(420, 186, "(it would stop the current)", 11, ACCENT, "start")
    svg += text(420, 202, "or an ammeter in parallel", 11, ACCENT, "start")
    svg += text(420, 218, "(it would short the component).", 11, ACCENT, "start")
    return svg


def series_parallel_svg():
    svg = ""
    # series, left
    svg += wires([(40, 130), (40, 40), (100, 40)])
    svg += cell(120, 40)
    svg += wire(140, 40, 260, 40) + wire(260, 40, 260, 130)
    svg += wire(260, 130, 222, 130) + lamp(200, 130) + wire(178, 130, 142, 130) + lamp(120, 130) + wire(98, 130, 40, 130)
    svg += text(150, 175, "series: one loop", 12, INK)
    svg += text(150, 192, "same current everywhere", 11, INK2)
    svg += text(150, 206, "pd shared between the lamps", 11, INK2)
    svg += text(150, 220, "one breaks → both go out", 11, INK2)
    # parallel, right
    svg += wires([(340, 150), (340, 40), (400, 40)])
    svg += cell(420, 40)
    svg += wire(440, 40, 600, 40) + wire(600, 40, 600, 150)
    # two branches between x=380 and x=560 at y=100 and y=150
    svg += wire(340, 100, 340, 100)
    svg += wire(340, 100, 448, 100) + lamp(470, 100) + wire(492, 100, 600, 100)
    svg += wire(340, 150, 448, 150) + lamp(470, 150) + wire(492, 150, 600, 150)
    svg += circle(340, 100, 2.5, None, "var(--ink)") + circle(600, 100, 2.5, None, "var(--ink)")
    svg += text(470, 192, "parallel: branches", 12, INK)
    svg += text(470, 209, "same pd across each branch", 11, INK2)
    svg += text(470, 223, "current splits at the junctions", 11, INK2)
    svg += text(470, 237, "one breaks → the other stays on", 11, INK2)
    return svg


def iv_practical_svg():
    """The 10.17a circuit: supply, variable resistor, ammeter in series
    with the component; voltmeter across the component."""
    svg = ""
    svg += wires([(60, 160), (60, 40), (110, 40)])
    svg += battery(134, 40)
    svg += wire(158, 40, 230, 40)
    svg += variable_resistor(254, 40)
    svg += wire(278, 40, 420, 40) + wire(420, 40, 420, 160)
    svg += wire(420, 160, 330, 160) + meter(306, 160, "A") + wire(282, 160, 232, 160)
    svg += resistor(208, 160)
    svg += wire(184, 160, 60, 160)
    svg += wire(184, 160, 184, 225) + wire(232, 160, 232, 225)
    svg += meter(208, 225, "V")
    svg += text(208, 130, "component under test", 11, INK2)
    svg += text(208, 143, "(resistor, then filament lamp)", 11, INK2)
    svg += text(254, 72, "variable resistor:", 11, INK2)
    svg += text(254, 85, "changes the current", 11, INK2)
    svg += text(306, 192, "ammeter in series", 11, INK2)
    svg += text(208, 262, "voltmeter across the component", 11, INK2)
    svg += text(470, 80, "To get the negative half of the graph,", 11, INK, "start")
    svg += text(470, 96, "reverse the connections to the supply", 11, INK, "start")
    svg += text(470, 112, "(or use a supply with a reversing switch);", 11, INK, "start")
    svg += text(470, 128, "both meters then read negative.", 11, INK, "start")
    svg += text(470, 160, "Switch off between readings, or take", 11, INK, "start")
    svg += text(470, 176, "them quickly, so the resistor does", 11, INK, "start")
    svg += text(470, 192, "not warm up and change its resistance.", 11, INK, "start")
    return svg


def test_circuits_svg():
    """10.17b: two resistors in series, then in parallel, with the meters
    needed to find the pd across each and the current in each."""
    svg = ""
    # series (left)
    svg += wires([(40, 150), (40, 40), (90, 40)])
    svg += cell(110, 40)
    svg += wire(130, 40, 300, 40) + wire(300, 40, 300, 150)
    svg += wire(300, 150, 254, 150) + meter(230, 150, "A") + wire(206, 150, 194, 150)
    svg += resistor(170, 150) + wire(146, 150, 124, 150) + resistor(100, 150) + wire(76, 150, 40, 150)
    svg += wire(76, 150, 76, 205) + wire(124, 150, 124, 205) + meter(100, 205, "V")
    svg += wire(146, 150, 146, 205) + wire(194, 150, 194, 205) + meter(170, 205, "V")
    svg += text(170, 245, "series: one ammeter is enough", 11, INK2)
    svg += text(170, 259, "(same current everywhere); a voltmeter across", 11, INK2)
    svg += text(170, 273, "each resistor — the two pds add up to the cell's", 11, INK2)
    # parallel (right)
    svg += wires([(380, 170), (380, 40), (430, 40)])
    svg += cell(450, 40)
    svg += wire(470, 40, 620, 40) + wire(620, 40, 620, 170)
    svg += wire(380, 110, 456, 110) + meter(480, 110, "A") + wire(504, 110, 516, 110) + resistor(540, 110) + wire(564, 110, 620, 110)
    svg += wire(380, 170, 456, 170) + meter(480, 170, "A") + wire(504, 170, 516, 170) + resistor(540, 170) + wire(564, 170, 620, 170)
    svg += circle(380, 110, 2.5, None, "var(--ink)") + circle(620, 110, 2.5, None, "var(--ink)")
    svg += text(500, 245, "parallel: an ammeter in each branch", 11, INK2)
    svg += text(500, 259, "(the two currents add up to the cell's); one voltmeter", 11, INK2)
    svg += text(500, 273, "across either resistor — the pd is the same", 11, INK2)
    return svg


def plug_svg():
    """A UK three-pin plug seen from the inside: earth top, live right
    (with the fuse), neutral left; cable clamp at the bottom."""
    svg = ""
    svg += "<path d='M 150 60 Q 150 30 180 30 L 420 30 Q 450 30 450 60 L 450 250 Q 450 280 420 280 L 180 280 Q 150 280 150 250 Z' style='fill:var(--line);opacity:0.12;stroke:var(--ink-2);stroke-width:1.6'/>"
    # pins (seen from inside as small rectangles)
    svg += rect(290, 48, 20, 34, "var(--line)")
    svg += text(318, 70, "earth pin", 10, INK2, "start")
    svg += rect(200, 150, 18, 30, "var(--line)")
    svg += text(209, 142, "neutral pin", 10, INK2)
    svg += rect(382, 150, 18, 30, "var(--line)")
    svg += text(391, 142, "live pin", 10, INK2)
    # fuse on the live side
    svg += rect(360, 215, 60, 16, "var(--bg)")
    svg += text(390, 227, "fuse", 10, INK)
    # cable in from the bottom
    svg += rect(270, 262, 60, 10, "var(--line)")
    svg += text(300, 300, "cable clamp (grips the outer insulation)", 10, INK2)
    # wires
    svg += solid(300, 272, 300, 82, "var(--ok, #1f7a4d)", 4)   # earth, green/yellow
    svg += "<line x1='300' y1='272' x2='300' y2='82' style='stroke:#e0c020;stroke-width:4;stroke-dasharray:8 8'/>"
    svg += solid(285, 268, 209, 180, "#2c6fd1", 4)                # neutral, blue
    svg += solid(315, 268, 391, 231, "#8b5a2b", 4)                 # live, brown, to the fuse
    svg += solid(391, 215, 391, 180, "#8b5a2b", 4)
    # labels
    svg += text(480, 60, "earth: green and yellow", 11, INK, "start")
    svg += text(480, 76, "at 0 V; a safety path for current", 11, INK2, "start")
    svg += text(480, 92, "if the live touches the metal case", 11, INK2, "start")
    svg += text(480, 125, "live: brown — at 230 V (a.c.),", 11, INK, "start")
    svg += text(480, 141, "carries the current in; the fuse", 11, INK2, "start")
    svg += text(480, 157, "and the switch are in this wire", 11, INK2, "start")
    svg += text(480, 190, "neutral: blue — at 0 V,", 11, INK, "start")
    svg += text(480, 206, "completes the circuit back", 11, INK2, "start")
    svg += text(480, 222, "to the supply", 11, INK2, "start")
    svg += text(480, 255, "BLue → Left, BRown → Right,", 11, INK2, "start")
    svg += text(480, 271, "the striped wire to the top", 11, INK2, "start")
    return svg


def ac_dc_svg():
    """Two small graphs: a d.c. trace (flat line) and an a.c. trace (sine)."""
    svg = ""
    for index, (title, kind) in enumerate((("d.c. — a cell or battery", "dc"), ("a.c. — the mains", "ac"))):
        ox = 60 + index * 330
        oy = 150
        svg += wire(ox, oy - 100, ox, oy + 60, INK2)
        svg += wire(ox, oy, ox + 250, oy, INK2)
        svg += text(ox + 250, oy + 16, "time", 11, INK2, "end")
        svg += text(ox - 8, oy - 90, "pd", 11, INK2, "end")
        svg += text(ox + 125, oy - 115, title, 12, INK)
        if kind == "dc":
            svg += solid(ox, oy - 60, ox + 250, oy - 60, ACCENT, 2.5)
            svg += text(ox + 125, oy + 40, "same direction, steady size", 11, INK2)
        else:
            path = "M"
            for step in range(0, 251, 5):
                y = oy - 70 * sin(radians(step * 360 / 125))
                path += " %.1f %.1f" % (ox + step, y)
            svg += "<path d='%s' style='fill:none;stroke:var(--accent);stroke-width:2.5'/>" % path
            svg += dashed(ox + 125, oy - 80, ox + 125, oy + 20, INK2)
            svg += text(ox + 62, oy + 95, "one cycle = 1/50 s", 11, INK2)
            svg += text(ox + 125, oy + 112, "direction reverses 100 times a second; UK mains 50 Hz, about 230 V", 10.5, INK2)
    return svg


def sensing_svg():
    """An LDR in series with a fixed resistor across a supply; the output
    is the pd across the resistor."""
    svg = ""
    svg += wires([(60, 190), (60, 40), (150, 40)])
    svg += cell(170, 40)
    svg += wire(190, 40, 380, 40) + wire(380, 40, 380, 190)
    svg += wire(380, 190, 304, 190)
    svg += ldr(280, 190)
    svg += wire(256, 190, 224, 190)
    svg += resistor(200, 190)
    svg += wire(176, 190, 60, 190)
    svg += wire(176, 190, 176, 250) + wire(224, 190, 224, 250) + meter(200, 250, "V")
    svg += text(200, 290, "output: the pd across the fixed resistor", 11, INK2)
    svg += text(420, 70, "Bright: the LDR's resistance is low, so it", 11, INK, "start")
    svg += text(420, 86, "takes a small share of the supply pd —", 11, INK2, "start")
    svg += text(420, 102, "most of the pd is across the resistor: high output.", 11, INK2, "start")
    svg += text(420, 134, "Dark: the LDR's resistance is high, so it", 11, INK, "start")
    svg += text(420, 150, "takes most of the supply pd —", 11, INK2, "start")
    svg += text(420, 166, "little is left across the resistor: low output.", 11, INK2, "start")
    svg += text(420, 198, "Swap the two components and the output", 11, INK2, "start")
    svg += text(420, 214, "rises in the dark instead — a night light.", 11, INK2, "start")
    svg += text(420, 246, "A thermistor works the same way with", 11, INK2, "start")
    svg += text(420, 262, "temperature in place of light.", 11, INK2, "start")
    return svg
