"""
ei_diagrams.py — the diagrams for Topic 13 (Electromagnetic induction)
as inline SVG, drawn with the helpers in le_diagrams.py, fe_diagrams.py
and mg_diagrams.py.

    induction_svg()    a magnet pushed into a coil joined to a meter, and the meter kick
    generator_svg()    the alternator (slip rings) and the dynamo (split ring) side by side
    outputs_svg()      the output graphs: a.c., d.c., and turning faster
    speaker_mic_svg()  a loudspeaker and a microphone in section
    transformer_svg()  an iron core with primary and secondary coils
    grid_svg()         the national grid from power station to home
    drop_svg()         the falling-magnet practical (tube, coil, voltmeter, rule)
"""

from math import pi, sin

from le_diagrams import ACCENT, INK, INK2, LINE, dashed, solid, text
from fe_diagrams import arrow, box, dot
from mg_diagrams import head, magnet, path, wire_end


def coil_side(x, y, turns, rx=9, ry=30, colour=INK, gap=14):
    """A coil seen from the side: a row of ellipses along a horizontal axis."""
    svg = ""
    for i in range(turns):
        svg += "<ellipse cx='%.1f' cy='%s' rx='%s' ry='%s' style='fill:none;stroke:%s;stroke-width:2'/>" % (x + i * gap, y, rx, ry, colour)
    return svg


def meter(x, y, r, label, needle_deg=0):
    """A round meter with a centre-zero needle; needle_deg is the swing from vertical (+ right)."""
    svg = "<circle cx='%s' cy='%s' r='%s' style='fill:none;stroke:%s;stroke-width:1.6'/>" % (x, y, r, INK)
    svg += solid(x - r * 0.6, y - r * 0.55, x + r * 0.6, y - r * 0.55, LINE, 1)
    svg += text(x, y + r * 0.6, label, 11, INK2)
    from math import cos, radians
    a = radians(needle_deg)
    svg += solid(x, y + r * 0.2, x + r * 0.75 * sin(a), y + r * 0.2 - r * 0.75 * cos(a), ACCENT, 2.2)
    svg += dot(x, y + r * 0.2, 3, INK)
    svg += text(x, y - r * 0.68, "0", 9, INK2)
    return svg


def sine_path(x0, y0, width, amp, cycles, points=120, rectify=False):
    d = ""
    for i in range(points + 1):
        t = i / points
        v = sin(2 * pi * cycles * t)
        if rectify:
            v = abs(v)
        x = x0 + t * width
        y = y0 - amp * v
        d += ("M" if i == 0 else " L") + " %.1f %.1f" % (x, y)
    return d


# ---------------------------------------------------------------------

def induction_svg():
    svg = ""
    svg += text(330, 22, "push a magnet into a coil: the meter kicks", 12, INK)
    # coil centred (330, 140)
    svg += coil_side(290, 140, 7, rx=9, ry=34)
    # magnet approaching from the left, moving right
    svg += magnet(80, 125, 150, 30)
    svg += arrow(235, 110, 285, 110, ACCENT, 2.4)
    svg += text(260, 100, "moving in", 11, ACCENT)
    # leads to the meter
    # two leads: the left end of the coil to the meter's lower terminal, the right end to its upper one
    svg += solid(290, 174, 290, 225, INK2, 1.6)
    svg += solid(290, 225, 520, 225, INK2, 1.6)
    svg += solid(520, 225, 520, 172, INK2, 1.6)
    svg += solid(374, 174, 374, 205, INK2, 1.6)
    svg += solid(374, 205, 470, 205, INK2, 1.6)
    svg += solid(470, 205, 470, 140, INK2, 1.6)
    svg += solid(470, 140, 490, 140, INK2, 1.6)
    svg += meter(520, 140, 30, "V", needle_deg=35)
    svg += text(560, 196, "centre-zero", 10, INK2)
    svg += text(330, 250, "pull it out: the needle kicks the other way · hold it still: nothing", 11, INK2)
    svg += text(330, 268, "faster, a stronger magnet or more turns: a bigger kick", 11, INK2)
    return svg


def generator_svg():
    svg = ""
    for cx, title, split in ((170, "alternator: slip rings → a.c.", False), (500, "dynamo: split ring → d.c.", True)):
        cy = 130
        svg += text(cx, 22, title, 12, INK)
        svg += magnet(cx - 130, 70, 36, 120, labels=False)
        svg += text(cx - 112, 136, "N", 14, INK, weight="bold")
        svg += magnet(cx + 94, 70, 36, 120, labels=False)
        svg += text(cx + 112, 136, "S", 14, INK, weight="bold")
        for i in range(4):
            y = 88 + i * 28
            svg += solid(cx - 92, y, cx + 92, y, INK2, 1.2)
            svg += head(cx + 40, y, 0)
        # the coil, slightly tilted, as a rectangle seen in perspective
        svg += "<polygon points='%d,%d %d,%d %d,%d %d,%d' style='fill:none;stroke:%s;stroke-width:3'/>" % (cx - 55, cy - 40, cx + 55, cy - 28, cx + 55, cy + 40, cx - 55, cy + 28, INK)
        svg += arrow(cx - 70, cy - 60, cx - 30, cy - 75, ACCENT, 2)
        svg += text(cx - 52, cy - 82, "turned", 10, ACCENT)
        # rings below the coil
        ry = 210
        if split:
            svg += "<path d='M %d %d A 18 18 0 0 1 %d %d' style='fill:none;stroke:%s;stroke-width:6'/>" % (cx - 2, ry - 18, cx - 2, ry + 18, INK)
            svg += "<path d='M %d %d A 18 18 0 0 0 %d %d' style='fill:none;stroke:%s;stroke-width:6'/>" % (cx + 2, ry - 18, cx + 2, ry + 18, INK2)
            svg += text(cx, ry + 36, "two halves, turn with the coil", 10, INK2)
        else:
            svg += "<circle cx='%d' cy='%d' r='18' style='fill:none;stroke:%s;stroke-width:6'/>" % (cx - 22, ry, INK)
            svg += "<circle cx='%d' cy='%d' r='18' style='fill:none;stroke:%s;stroke-width:6'/>" % (cx + 22, ry, INK2)
            svg += text(cx, ry + 36, "two complete rings, one per end of the coil", 10, INK2)
        if split:
            svg += box(cx - 39, ry - 5, 18, 10, "var(--accent)", 0.6)
            svg += box(cx + 21, ry - 5, 18, 10, "var(--accent)", 0.6)
            svg += text(cx - 30, ry - 12, "brush", 9, INK2)
            svg += text(cx + 30, ry - 12, "brush", 9, INK2)
        else:
            svg += box(cx - 60, ry - 5, 18, 10, "var(--accent)", 0.6)
            svg += box(cx + 42, ry - 5, 18, 10, "var(--accent)", 0.6)
            svg += text(cx - 51, ry - 12, "brush", 9, INK2)
            svg += text(cx + 51, ry - 12, "brush", 9, INK2)
    return svg


def outputs_svg():
    svg = ""
    panels = [
        (20, "alternator: a.c.", False, 1.0, 2.0),
        (260, "dynamo: d.c. (one direction, not steady)", True, 1.0, 2.0),
        (500, "a.c., coil turned twice as fast", False, 1.4, 4.0),
    ]
    for x0, title, rect, amp_scale, cycles in panels:
        w, h = 210, 160
        y0 = 150  # the zero line
        svg += text(x0 + w / 2, 22, title, 11, INK)
        # axes
        svg += solid(x0 + 10, y0, x0 + w, y0, INK2, 1.2)
        svg += solid(x0 + 10, y0 - 70, x0 + 10, y0 + 70, INK2, 1.2)
        svg += head(x0 + w, y0, 0)
        svg += head(x0 + 10, y0 - 70, 270)
        svg += text(x0 + w - 4, y0 + 14, "time", 10, INK2, anchor="end")
        svg += text(x0 + 14, y0 - 60, "pd", 10, INK2, anchor="start")
        svg += path(sine_path(x0 + 10, y0, w - 20, 48 * amp_scale, cycles, rectify=rect), ACCENT, 2.2)
        if not rect:
            svg += dashed(x0 + 10, y0 - 48 * amp_scale, x0 + w, y0 - 48 * amp_scale, LINE)
            svg += text(x0 + w - 4, y0 - 48 * amp_scale - 4, "peak", 9, INK2, anchor="end")
    svg += text(360, 256, "faster turning: the peak pd is larger AND the frequency is higher (more cycles in the same time)", 11, INK2)
    return svg


def speaker_mic_svg():
    svg = ""
    # loudspeaker, left
    cx = 170
    svg += text(cx, 22, "loudspeaker: current → movement", 12, INK)
    # permanent magnet: centre pole and outer ring (section)
    svg += box(60, 110, 80, 40, "var(--accent)", 0.35)
    svg += text(100, 135, "N", 13, INK, weight="bold")
    svg += box(60, 60, 80, 24, "var(--line)", 0.4)
    svg += box(60, 176, 80, 24, "var(--line)", 0.4)
    svg += text(100, 77, "S", 12, INK, weight="bold")
    svg += text(100, 193, "S", 12, INK, weight="bold")
    # coil in the gaps, on a former attached to the cone
    for y in (92, 98, 104):
        svg += wire_end(150, y, True, 3)
        svg += wire_end(150, y + 64, False, 3)
    svg += solid(158, 86, 158, 174, INK, 2)
    # cone
    svg += solid(158, 86, 250, 40, INK, 2.2)
    svg += solid(158, 174, 250, 220, INK, 2.2)
    svg += text(200, 98, "cone", 11, INK2)
    svg += arrow(175, 130, 215, 130, ACCENT, 2.4)
    svg += arrow(195, 150, 160, 150, ACCENT, 1.6)
    svg += text(310, 100, "sound", 11, INK2)
    for r in (14, 24, 34):
        svg += "<path d='M %d %d A %d %d 0 0 1 %d %d' style='fill:none;stroke:%s;stroke-width:1.2'/>" % (262, 130 - r, r, r, 262, 130 + r, INK2)
    svg += text(cx, 248, "a.c. in the coil → force on the coil (motor effect)", 11, INK2)
    svg += text(cx, 264, "→ the cone moves in and out at the same frequency", 11, INK2)
    # microphone, right
    cx = 520
    svg += text(cx, 22, "microphone: movement → pd induced", 12, INK)
    svg += box(560, 110, 80, 40, "var(--accent)", 0.35)
    svg += text(600, 135, "N", 13, INK, weight="bold")
    svg += box(560, 60, 80, 24, "var(--line)", 0.4)
    svg += box(560, 176, 80, 24, "var(--line)", 0.4)
    svg += text(600, 77, "S", 12, INK, weight="bold")
    svg += text(600, 193, "S", 12, INK, weight="bold")
    for y in (92, 98, 104):
        svg += wire_end(550, y, True, 3)
        svg += wire_end(550, y + 64, False, 3)
    svg += solid(542, 86, 542, 174, INK, 2)
    # diaphragm (flat)
    svg += solid(536, 60, 536, 200, INK, 3)
    svg += text(520, 56, "diaphragm", 10, INK2, anchor="end")
    for r in (14, 24, 34):
        svg += "<path d='M %d %d A %d %d 0 0 1 %d %d' style='fill:none;stroke:%s;stroke-width:1.2'/>" % (470, 130 - r, r, r, 470, 130 + r, INK2)
    svg += text(430, 95, "sound", 11, INK2)
    svg += arrow(500, 130, 532, 130, ACCENT, 2.4)
    svg += text(cx, 248, "sound makes the diaphragm and coil vibrate in the field", 11, INK2)
    svg += text(cx, 264, "→ a changing field for the coil → an alternating pd is induced", 11, INK2)
    return svg


def transformer_svg():
    svg = ""
    svg += text(330, 22, "a transformer: two coils on one iron core", 12, INK)
    # core: a rectangle frame
    svg += "<rect x='220' y='60' width='220' height='150' style='fill:none;stroke:%s;stroke-width:22;opacity:0.55'/>" % LINE
    svg += text(330, 140, "soft iron core", 11, INK2)
    # primary coil on the left limb (5 turns), secondary on the right (10 turns)
    for i in range(5):
        y = 85 + i * 20
        svg += "<ellipse cx='220' cy='%d' rx='22' ry='8' style='fill:none;stroke:%s;stroke-width:2.2'/>" % (y, INK)
    for i in range(10):
        y = 75 + i * 12
        svg += "<ellipse cx='440' cy='%d' rx='22' ry='5' style='fill:none;stroke:%s;stroke-width:2.2'/>" % (y, ACCENT)
    svg += solid(150, 85, 198, 85, INK, 1.8)
    svg += solid(150, 165, 198, 165, INK, 1.8)
    svg += "<circle cx='140' cy='125' r='14' style='fill:none;stroke:%s;stroke-width:1.6'/>" % INK
    svg += path("M 131 125 q 4.5 -8 9 0 q 4.5 8 9 0", INK, 1.6)
    svg += solid(140, 111, 140, 85, INK, 1.8)
    svg += solid(140, 139, 140, 165, INK, 1.8)
    svg += solid(462, 75, 520, 75, ACCENT, 1.8)
    svg += solid(462, 183, 520, 183, ACCENT, 1.8)
    svg += text(140, 190, "a.c. supply", 11, INK2)
    svg += text(140, 205, "primary coil, Nₚ turns", 11, INK2)
    svg += text(520, 205, "secondary coil, Nₛ turns", 11, INK2)
    svg += text(520, 220, "to the load", 11, INK2)
    svg += text(330, 250, "alternating current in the primary → changing magnetic field in the core →", 11, INK2)
    svg += text(330, 266, "an alternating pd is induced in the secondary (here Nₛ > Nₚ: step-up)", 11, INK2)
    return svg


def grid_svg():
    svg = ""
    svg += text(360, 22, "the national grid", 12, INK)
    y = 140
    stages = [
        (60, "power station", "25 kV"),
        (200, "step-up", "400 kV"),
        (360, "pylons: long cables", ""),
        (520, "step-down", "230 V"),
        (660, "homes", ""),
    ]
    for i, (x, label, volts) in enumerate(stages):
        if label.startswith("step"):
            svg += "<rect x='%d' y='%d' width='70' height='60' style='fill:var(--accent);opacity:0.25;stroke:%s;stroke-width:1.6'/>" % (x - 35, y - 30, INK)
            svg += text(x, y - 4, label, 11, INK)
            svg += text(x, y + 12, "transformer", 10, INK2)
        elif label == "homes":
            svg += "<polygon points='%d,%d %d,%d %d,%d' style='fill:none;stroke:%s;stroke-width:1.8'/>" % (x - 30, y - 10, x, y - 38, x + 30, y - 10, INK)
            svg += box(x - 24, y - 10, 48, 40, "var(--line)", 0.4)
            svg += text(x, y + 50, label, 11, INK)
        elif label.startswith("pylons"):
            for px in (x - 40, x + 40):
                svg += solid(px, y + 30, px, y - 50, INK, 1.6)
                svg += solid(px - 16, y - 30, px + 16, y - 30, INK, 1.6)
                svg += solid(px - 12, y - 10, px + 12, y - 10, INK, 1.6)
            svg += text(x, y + 50, label, 11, INK)
        else:
            svg += box(x - 40, y - 20, 80, 50, "var(--line)", 0.4)
            svg += "<rect x='%d' y='%d' width='14' height='40' style='fill:var(--ink-2);opacity:0.5'/>" % (x - 20, y - 60)
            svg += text(x, y + 50, label, 11, INK)
        if volts:
            svg += text(x, y + 66 if label == "power station" else y + 50, volts, 11, ACCENT, weight="bold")
    # cables between stages
    for (x1, _, _), (x2, _, _) in zip(stages, stages[1:]):
        svg += solid(x1 + 40, y, x2 - 40, y, INK2, 1.6)
    svg += text(360, 236, "step up to a very high pd so the current is small: little energy is wasted heating the cables;", 11, INK2)
    svg += text(360, 252, "step down near homes to a safe 230 V", 11, INK2)
    return svg


def drop_svg():
    svg = ""
    svg += text(330, 22, "the falling-magnet investigation", 12, INK)
    # tube
    svg += "<rect x='300' y='40' width='40' height='200' rx='4' style='fill:none;stroke:%s;stroke-width:1.6;stroke-dasharray:4 3'/>" % INK2
    # coil around the tube near the bottom
    for i in range(6):
        svg += "<ellipse cx='320' cy='%d' rx='28' ry='6' style='fill:none;stroke:%s;stroke-width:2'/>" % (170 + i * 8, INK)
    # magnet inside the tube, falling
    svg += "<g transform='rotate(90 320 90)'>" + magnet(290, 80, 60, 20) + "</g>"
    svg += arrow(360, 70, 360, 130, ACCENT, 2.2)
    svg += text(372, 100, "falls", 11, ACCENT, anchor="start")
    # height arrow and rule
    svg += solid(250, 50, 250, 170, INK2, 1.2)
    for i in range(0, 13):
        svg += solid(244 if i % 5 else 240, 50 + i * 10, 250, 50 + i * 10, INK2, 1)
    svg += text(232, 112, "h", 12, INK, anchor="end", italic=True)
    svg += text(220, 128, "metre rule", 10, INK2, anchor="end")
    svg += dashed(255, 50, 300, 50, LINE)
    svg += dashed(255, 170, 300, 170, LINE)
    # voltmeter
    svg += solid(348, 190, 440, 190, INK2, 1.6)
    svg += solid(348, 214, 440, 214, INK2, 1.6)
    svg += solid(440, 190, 440, 150, INK2, 1.6)
    svg += solid(440, 214, 440, 230, INK2, 1.6)
    svg += solid(440, 230, 470, 230, INK2, 1.6)
    svg += solid(470, 230, 470, 150, INK2, 1.6)
    svg += meter(455, 125, 26, "V", needle_deg=28)
    svg += text(500, 120, "set to a.c.;", 10, INK2, anchor="start")
    svg += text(500, 132, "read the maximum", 10, INK2, anchor="start")
    svg += text(330, 268, "change h in equal steps, record the maximum reading, repeat and average, plot reading against h", 11, INK2)
    return svg
