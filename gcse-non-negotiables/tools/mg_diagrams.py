"""
mg_diagrams.py — the diagrams for Topic 12 (Magnetism and the motor
effect) as inline SVG, drawn with the helpers in le_diagrams.py and
fe_diagrams.py.

    bar_magnet_svg()   the field of a bar magnet and the uniform field between two poles
    earth_svg()        the Earth as a bar magnet, with a compass
    wire_field_svg()   the field around a straight wire, end on: dot and cross
    solenoid_svg()     the field of a solenoid: straight inside, bar-magnet outside
    motor_effect_svg() a wire between the poles: the two fields, and the force
    flhr_svg()         Fleming's left-hand rule: the three directions
    cases_svg()        three dots-and-crosses cases: force up, force down, no force
    motor_svg()        the d.c. motor end on, with the split ring
"""

from math import cos, radians, sin

from le_diagrams import ACCENT, INK, INK2, LINE, dashed, solid, text
from fe_diagrams import arrow, box, dot


def head(x, y, angle_deg, colour=INK2, size=7):
    """An arrowhead at (x, y) pointing along angle_deg (0 = right, 90 = down)."""
    a = radians(angle_deg)
    left = (x - size * cos(a - 0.5), y - size * sin(a - 0.5))
    right = (x - size * cos(a + 0.5), y - size * sin(a + 0.5))
    return "<polygon points='%.1f,%.1f %.1f,%.1f %.1f,%.1f' style='fill:%s'/>" % (x, y, left[0], left[1], right[0], right[1], colour)


def path(d, colour=INK2, width=1.6):
    return "<path d='%s' style='fill:none;stroke:%s;stroke-width:%s'/>" % (d, colour, width)


def magnet(x, y, w, h, n_right=True, labels=True):
    """A bar magnet from (x, y), N on the right unless n_right is False."""
    svg = box(x, y, w / 2, h, "var(--line)", 0.35)
    svg += box(x + w / 2, y, w / 2, h, "var(--accent)", 0.35)
    if labels:
        left, right = ("S", "N") if n_right else ("N", "S")
        svg += text(x + w / 4, y + h / 2 + 5, left, 14, INK, weight="bold")
        svg += text(x + 3 * w / 4, y + h / 2 + 5, right, 14, INK, weight="bold")
    return svg


def wire_end(x, y, into, r=9):
    """A wire seen end on: a cross for current into the page, a dot for out."""
    svg = "<circle cx='%s' cy='%s' r='%s' style='fill:var(--bg,transparent);stroke:%s;stroke-width:1.8'/>" % (x, y, r, INK)
    if into:
        k = r * 0.55
        svg += solid(x - k, y - k, x + k, y + k, INK, 1.8)
        svg += solid(x - k, y + k, x + k, y - k, INK, 1.8)
    else:
        svg += dot(x, y, 2.8, INK)
    return svg


# ---------------------------------------------------------------------

def bar_magnet_svg():
    """Left: the loops of a bar magnet, N on the right. Right: two facing poles with a uniform field."""
    svg = ""
    # left panel: bar magnet centred (200, 130)
    mx, my, mw, mh = 120, 115, 160, 30
    svg += text(200, 24, "a bar magnet", 12, INK)
    for d in (24, 50, 80):
        # upper loop from the N face round to the S face
        d_path = "M %d %d C %d %d %d %d %d %d" % (mx + mw + 2, my + 12, mx + mw + d * 2.0, my - d * 1.5, mx - d * 2.0 + 2, my - d * 1.5, mx - 2, my + 12)
        svg += path(d_path)
        svg += head(200, my - d * 1.125 + 3, 180)
        d_path = "M %d %d C %d %d %d %d %d %d" % (mx + mw + 2, my + mh - 12, mx + mw + d * 2.0, my + mh + d * 1.5, mx - d * 2.0 + 2, my + mh + d * 1.5, mx - 2, my + mh - 12)
        svg += path(d_path)
        svg += head(200, my + mh + d * 1.125 - 3, 180)
    # the straight line out of each end
    svg += solid(mx + mw + 2, my + mh / 2, mx + mw + 70, my + mh / 2, INK2, 1.6)
    svg += head(mx + mw + 70, my + mh / 2, 0)
    svg += solid(mx - 70, my + mh / 2, mx - 2, my + mh / 2, INK2, 1.6)
    svg += head(mx - 2, my + mh / 2, 0)
    svg += magnet(mx, my, mw, mh)
    svg += text(200, 258, "lines leave N, enter S, never cross; closest at the poles", 11, INK2)
    # right panel: uniform field between facing poles
    svg += text(560, 24, "a uniform field between two poles", 12, INK)
    svg += magnet(420, 70, 70, 120, labels=False)
    svg += text(455, 136, "N", 16, INK, weight="bold")
    svg += magnet(630, 70, 70, 120, labels=False)
    svg += text(665, 136, "S", 16, INK, weight="bold")
    for i in range(5):
        y = 86 + i * 22
        svg += solid(492, y, 628, y, INK2, 1.6)
        svg += head(566, y, 0)
    svg += text(560, 215, "parallel, equally spaced, N → S:", 11, INK2)
    svg += text(560, 231, "same strength and direction everywhere", 11, INK2)
    return svg


def earth_svg():
    cx, cy, r = 190, 140, 95
    svg = ""
    svg += "<circle cx='%s' cy='%s' r='%s' style='fill:var(--accent);opacity:0.12;stroke:%s;stroke-width:1.6'/>" % (cx, cy, r, INK2)
    # the imaginary bar magnet inside, slightly tilted, S at the top (geographic north)
    svg += "<g transform='rotate(-11 %s %s)'>" % (cx, cy)
    svg += box(cx - 11, cy - 55, 22, 55, "var(--accent)", 0.35)
    svg += box(cx - 11, cy, 22, 55, "var(--line)", 0.35)
    svg += text(cx, cy - 30, "S", 13, INK, weight="bold")
    svg += text(cx, cy + 36, "N", 13, INK, weight="bold")
    # field loops: out of N (bottom), round, into S (top)
    for d in (30, 60):
        svg += path("M %d %d C %d %d %d %d %d %d" % (cx + 8, cy + 57, cx + 70 + d * 1.5, cy + 80 + d, cx + 70 + d * 1.5, cy - 80 - d, cx + 8, cy - 57))
        svg += head(cx + 59 + d * 1.1, cy, 270)
        svg += path("M %d %d C %d %d %d %d %d %d" % (cx - 8, cy + 57, cx - 70 - d * 1.5, cy + 80 + d, cx - 70 - d * 1.5, cy - 80 - d, cx - 8, cy - 57))
        svg += head(cx - 59 - d * 1.1, cy, 270)
    svg += "</g>"
    svg += text(cx, 22, "geographic north: a magnetic S pole", 11, INK2)
    svg += text(cx, 268, "geographic south: a magnetic N pole", 11, INK2)
    # compass on the right, needle N end pointing up (north)
    px, py = 430, 140
    svg += "<circle cx='%s' cy='%s' r='46' style='fill:none;stroke:%s;stroke-width:1.6'/>" % (px, py, INK2)
    svg += "<polygon points='%d,%d %d,%d %d,%d' style='fill:%s'/>" % (px, py - 38, px - 7, py, px + 7, py, ACCENT)
    svg += "<polygon points='%d,%d %d,%d %d,%d' style='fill:%s;opacity:0.5'/>" % (px, py + 38, px - 7, py, px + 7, py, INK2)
    svg += text(px, py - 54, "N", 12, INK, weight="bold")
    svg += text(px, py + 66, "S", 12, INK, weight="bold")
    svg += text(px + 60, py - 20, "the compass needle is a", 11, INK2, anchor="start")
    svg += text(px + 60, py - 5, "small magnet: its N pole", 11, INK2, anchor="start")
    svg += text(px + 60, py + 10, "is pulled towards the", 11, INK2, anchor="start")
    svg += text(px + 60, py + 25, "Earth's magnetic S pole,", 11, INK2, anchor="start")
    svg += text(px + 60, py + 40, "which is near geographic north", 11, INK2, anchor="start")
    return svg


def wire_field_svg():
    svg = ""
    for panel, (cx, into, label, direction) in enumerate([(150, False, "current out of the page (dot)", "anticlockwise"), (520, True, "current into the page (cross)", "clockwise")]):
        cy = 150
        svg += text(cx, 16, label, 12, INK)
        for r in (26, 50, 80, 116):
            svg += "<circle cx='%s' cy='%s' r='%s' style='fill:none;stroke:%s;stroke-width:1.5'/>" % (cx, cy, r, INK2)
            # arrowhead at the top of each circle
            angle = 180 if not into else 0
            svg += head(cx, cy - r, angle)
        svg += wire_end(cx, cy, into, 10)
        svg += text(cx, 284, direction + " · circles further apart: field weaker", 11, INK2)
    svg += text(335, 140, "right-hand grip:", 11, INK2)
    svg += text(335, 155, "thumb = current,", 11, INK2)
    svg += text(335, 170, "fingers = field", 11, INK2)
    return svg


def solenoid_svg():
    svg = ""
    x0, x1, cy = 200, 440, 135
    # outer bar-magnet-like loops first (behind the coil)
    for d in (16, 36, 60):
        svg += path("M %d %d C %d %d %d %d %d %d" % (x1 + 6, cy - 30, x1 + 60 + d * 2, cy - 60 - d * 1.6, x0 - 60 - d * 2, cy - 60 - d * 1.6, x0 - 6, cy - 30))
        svg += head(320, cy - 45 - d * 1.2 + 1, 180)
        svg += path("M %d %d C %d %d %d %d %d %d" % (x1 + 6, cy + 30, x1 + 60 + d * 2, cy + 60 + d * 1.6, x0 - 60 - d * 2, cy + 60 + d * 1.6, x0 - 6, cy + 30))
        svg += head(320, cy + 45 + d * 1.2 - 1, 180)
    # straight lines inside and out of the ends
    for y in (cy - 18, cy, cy + 18):
        svg += solid(x0 - 60, y, x1 + 60, y, INK2, 1.6)
        svg += head(320, y, 0)
        svg += head(x1 + 60, y, 0)
    # the coil: a row of ellipses
    turns = 9
    for i in range(turns):
        x = x0 + i * (x1 - x0) / (turns - 1)
        svg += "<ellipse cx='%.1f' cy='%s' rx='9' ry='38' style='fill:none;stroke:%s;stroke-width:2.2'/>" % (x, cy, INK)
    svg += text(x0 - 95, cy - 50, "S", 16, INK, weight="bold")
    svg += text(x1 + 95, cy - 50, "N", 16, INK, weight="bold")
    svg += text(320, 282, "inside: the fields of the turns add — strong and almost uniform", 12, INK)
    svg += text(320, 298, "outside: they largely cancel — weaker, the shape of a bar magnet's field", 12, INK)
    return svg


def motor_effect_svg():
    svg = ""
    # left panel: the wire between the poles, the uniform field, the force
    svg += text(170, 24, "the wire between the poles (end on)", 12, INK)
    svg += magnet(30, 70, 50, 130, labels=False)
    svg += text(55, 142, "N", 16, INK, weight="bold")
    svg += magnet(260, 70, 50, 130, labels=False)
    svg += text(285, 142, "S", 16, INK, weight="bold")
    for i in range(5):
        y = 86 + i * 24
        svg += solid(82, y, 258, y, INK2, 1.4)
        svg += head(120, y, 0)
        svg += head(230, y, 0)
    svg += wire_end(170, 134, False, 11)
    svg += arrow(170, 118, 170, 60, ACCENT, 2.6)
    svg += text(195, 58, "force", 12, ACCENT, anchor="start")
    svg += text(170, 228, "current out of the page, field N → S", 11, INK2)
    svg += text(170, 244, "force on the wire: up (left-hand rule)", 11, INK2)
    # right panel: the two fields added — bunched below the wire, spread above
    cx, cy = 530, 134
    svg += text(cx, 24, "why: the two fields interact", 12, INK)
    # the combined field: lines pass above curving away, bunch underneath
    for i, yoff in enumerate((-72, -50, -28)):
        svg += path("M %d %d C %d %d %d %d %d %d" % (cx - 130, cy + yoff, cx - 40, cy + yoff - 28, cx + 40, cy + yoff - 28, cx + 130, cy + yoff))
        svg += head(cx + 130, cy + yoff, 0)
    for i, yoff in enumerate((18, 30, 42, 56, 74)):
        svg += path("M %d %d C %d %d %d %d %d %d" % (cx - 130, cy + yoff, cx - 40, cy + yoff - 6, cx + 40, cy + yoff - 6, cx + 130, cy + yoff))
        svg += head(cx + 130, cy + yoff, 0)
    svg += wire_end(cx, cy, False, 11)
    svg += arrow(cx, cy - 16, cx, cy - 58, ACCENT, 2.6)
    svg += text(cx, 228, "the wire's own field (anticlockwise) adds to the magnet's field below", 11, INK2)
    svg += text(cx, 244, "and cancels it above: strong below, weak above, so the force is up", 11, INK2)
    return svg


def flhr_svg():
    svg = ""
    svg += text(330, 24, "Fleming's left-hand rule: three directions at right angles", 12, INK)
    # a stylised left hand: palm facing the viewer, thumb up, first finger right, second finger towards the viewer
    px, py = 150, 150
    svg += "<rect x='%d' y='%d' width='70' height='80' rx='14' style='fill:var(--line);opacity:0.3;stroke:%s;stroke-width:1.4'/>" % (px - 35, py - 30, INK2)
    # thumb (up)
    svg += arrow(px - 20, py - 28, px - 20, py - 95, ACCENT, 3)
    svg += text(px - 20, py - 103, "thuMb · Motion (force)", 11, ACCENT)
    # first finger (to the right)
    svg += arrow(px + 35, py - 10, px + 115, py - 10, INK, 3)
    svg += text(px + 75, py - 20, "First finger · Field (N → S)", 11, INK)
    # second finger (towards the viewer, drawn down-left in oblique view)
    svg += arrow(px + 10, py + 20, px - 40, py + 90, INK2, 3)
    svg += text(px - 20, py + 108, "seCond finger · Current (+ → −)", 11, INK2)
    # the three axes on the right as a reminder
    ax, ay = 470, 160
    svg += arrow(ax, ay, ax, ay - 80, ACCENT, 2.4)
    svg += text(ax, ay - 88, "force", 11, ACCENT)
    svg += arrow(ax, ay, ax + 100, ay, INK, 2.4)
    svg += text(ax + 108, ay + 4, "field", 11, INK, anchor="start")
    svg += arrow(ax, ay, ax - 55, ay + 55, INK2, 2.4)
    svg += text(ax - 60, ay + 70, "current (out of the page)", 11, INK2)
    svg += text(330, 276, "each at right angles to the other two; parallel current and field: no force", 11, INK2)
    return svg


def cases_svg():
    svg = ""
    panels = [
        (120, False, "current out, field →", "force up", (0, -1)),
        (360, True, "current in, field →", "force down", (0, 1)),
        (600, None, "current along the field", "no force", None),
    ]
    for cx, into, label, result, direction in panels:
        cy = 140
        svg += text(cx, 24, label, 12, INK)
        svg += magnet(cx - 110, 70, 36, 130, labels=False)
        svg += text(cx - 92, 142, "N", 14, INK, weight="bold")
        svg += magnet(cx + 74, 70, 36, 130, labels=False)
        svg += text(cx + 92, 142, "S", 14, INK, weight="bold")
        for i in range(4):
            y = 92 + i * 30
            svg += solid(cx - 72, y, cx + 72, y, INK2, 1.4)
            svg += head(cx + 30, y, 0)
        if into is None:
            # a wire lying along the field: a horizontal rod with the current arrow
            svg += box(cx - 60, cy - 5, 120, 10, "var(--ink-2)", 0.5)
            svg += arrow(cx - 40, cy - 16, cx + 40, cy - 16, INK, 2)
            svg += text(cx, cy - 24, "I", 12, INK, italic=True)
        else:
            svg += wire_end(cx, cy, into, 10)
            dy = direction[1]
            start = cy - 16 if dy < 0 else cy + 16
            svg += arrow(cx, start, cx, cy + dy * 60, ACCENT, 2.6)
        svg += text(cx, 232, result, 12, ACCENT if direction else INK2, weight="bold")
    return svg


def motor_svg():
    svg = ""
    # left: end-on view of the coil between the poles
    svg += text(200, 24, "the coil end on: one side pushed up, the other down", 12, INK)
    svg += magnet(30, 70, 50, 150, labels=False)
    svg += text(55, 152, "N", 16, INK, weight="bold")
    svg += magnet(320, 70, 50, 150, labels=False)
    svg += text(345, 152, "S", 16, INK, weight="bold")
    for i in range(5):
        y = 92 + i * 28
        svg += solid(82, y, 318, y, INK2, 1.2)
        svg += head(200, y, 0)
    # the coil as a flat rectangle seen edge on: left side (dot) and right side (cross)
    svg += solid(130, 145, 270, 145, INK, 3)
    svg += dot(200, 145, 4, INK2)
    svg += wire_end(130, 145, False, 10)
    svg += wire_end(270, 145, True, 10)
    svg += arrow(130, 128, 130, 78, ACCENT, 2.6)
    svg += arrow(270, 162, 270, 212, ACCENT, 2.6)
    svg += text(110, 70, "F", 12, ACCENT, italic=True)
    svg += text(290, 224, "F", 12, ACCENT, italic=True)
    svg += text(200, 170, "axle", 10, INK2)
    svg += text(200, 252, "current out on the left, in on the right: the forces are", 11, INK2)
    svg += text(200, 267, "opposite on either side, so the coil turns (here, clockwise)", 11, INK2)
    # right: the split ring and brushes
    cx, cy = 560, 150
    svg += text(cx, 24, "the split-ring commutator", 12, INK)
    svg += "<path d='M %d %d A 40 40 0 0 1 %d %d' style='fill:none;stroke:%s;stroke-width:9'/>" % (cx - 3, cy - 40, cx - 3, cy + 40, INK)
    svg += "<path d='M %d %d A 40 40 0 0 0 %d %d' style='fill:none;stroke:%s;stroke-width:9'/>" % (cx + 3, cy - 40, cx + 3, cy + 40, INK2)
    svg += box(cx - 72, cy - 7, 24, 14, "var(--accent)", 0.6)
    svg += box(cx + 48, cy - 7, 24, 14, "var(--accent)", 0.6)
    svg += text(cx - 60, cy - 14, "brush", 10, INK2)
    svg += text(cx + 60, cy - 14, "brush", 10, INK2)
    svg += solid(cx - 100, cy, cx - 72, cy, INK2, 1.6)
    svg += solid(cx + 72, cy, cx + 100, cy, INK2, 1.6)
    svg += text(cx - 108, cy + 4, "+", 13, INK, anchor="end", weight="bold")
    svg += text(cx + 108, cy + 4, "−", 13, INK, anchor="start", weight="bold")
    svg += text(cx, cy + 4, "gap", 9, INK2)
    svg += text(cx, 225, "each half is joined to one side of the coil and turns with it;", 11, INK2)
    svg += text(cx, 240, "every half turn the halves swap brushes, so the current in the coil", 11, INK2)
    svg += text(cx, 255, "reverses and the coil keeps turning the same way", 11, INK2)
    return svg
