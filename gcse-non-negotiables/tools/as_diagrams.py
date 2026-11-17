"""
as_diagrams.py — two diagrams for Topic 7, as inline SVG: a circular
orbit with the velocity and force arrows, and the two life cycles of
stars as a flow chart. Same helpers as le_diagrams.py.
"""

from math import cos, radians, sin

from le_diagrams import INK, INK2, LINE, ACCENT, dashed, ray, solid, text


def orbit_svg():
    cx, cy, r = 180, 140, 95
    svg = "<circle cx='%s' cy='%s' r='18' style='fill:var(--accent);opacity:0.5'/>" % (cx, cy)
    svg += text(cx, cy + 4, "Sun", 11, INK)
    svg += "<circle cx='%s' cy='%s' r='%s' style='fill:none;stroke:var(--line);stroke-width:1.2;stroke-dasharray:4 4'/>" % (cx, cy, r)
    for angle in (-60, 30, 120, 210):
        px = cx + r * cos(radians(angle))
        py = cy + r * sin(radians(angle))
        svg += "<circle cx='%.1f' cy='%.1f' r='6' style='fill:var(--ink)'/>" % (px, py)
        # velocity: tangent (anticlockwise)
        vx = -sin(radians(angle))
        vy = cos(radians(angle))
        svg += ray(px, py, px + 45 * vx, py + 45 * vy, ACCENT, True, 2)
        # force: towards the centre
        fx = cx - px
        fy = cy - py
        length = (fx ** 2 + fy ** 2) ** 0.5
        svg += ray(px, py, px + 40 * fx / length, py + 40 * fy / length, INK2, True, 2)
    svg += text(330, 60, "velocity: along the orbit (tangent)", 11, ACCENT, "start")
    svg += ray(310, 56, 326, 56, ACCENT, True, 2)
    svg += text(330, 84, "force of gravity: towards the centre", 11, INK2, "start")
    svg += ray(310, 80, 326, 80, INK2, True, 2)
    svg += text(330, 120, "speed the same at every point;", 11, INK, "start")
    svg += text(330, 136, "direction changes all the time,", 11, INK, "start")
    svg += text(330, 152, "so the velocity changes —", 11, INK, "start")
    svg += text(330, 168, "the planet is accelerating towards the Sun.", 11, INK, "start")
    svg += text(330, 200, "The force is always at right angles", 11, INK2, "start")
    svg += text(330, 216, "to the velocity, so it turns the planet", 11, INK2, "start")
    svg += text(330, 232, "without speeding it up or slowing it down.", 11, INK2, "start")
    return svg


def life_cycle_svg():
    """Two rows of boxes: Sun-like stars above, massive stars below, sharing
    the nebula, protostar and main-sequence stages."""
    def box(x, y, w, label, strong=False):
        style = "fill:var(--accent);opacity:0.18;stroke:var(--accent);stroke-width:1.5" if strong else "fill:var(--line);opacity:0.18;stroke:var(--line);stroke-width:1.2"
        svg = "<rect x='%s' y='%s' width='%s' height='34' rx='6' style='%s'/>" % (x, y, w, style)
        lines = label.split("\n")
        if len(lines) == 1:
            svg += text(x + w / 2, y + 21, label, 11, INK)
        else:
            svg += text(x + w / 2, y + 15, lines[0], 10, INK)
            svg += text(x + w / 2, y + 28, lines[1], 10, INK)
        return svg

    def arrow(x1, y1, x2, y2):
        return ray(x1, y1, x2, y2, INK2, True, 1.5)

    svg = ""
    # shared stages
    svg += box(10, 110, 70, "nebula", True)
    svg += arrow(80, 127, 100, 127)
    svg += box(100, 110, 80, "protostar", True)
    svg += arrow(180, 127, 200, 127)
    svg += box(200, 110, 100, "main sequence\nstar", True)
    # branch
    svg += arrow(300, 118, 330, 60)
    svg += arrow(300, 136, 330, 194)
    svg += text(305, 45, "mass like the Sun", 10, INK2, "start")
    svg += text(305, 222, "mass much larger than the Sun", 10, INK2, "start")
    # sun-like row (y = 40)
    svg += box(330, 40, 80, "red giant")
    svg += arrow(410, 57, 430, 57)
    svg += box(430, 40, 90, "white dwarf")
    svg += arrow(520, 57, 540, 57)
    svg += box(540, 40, 90, "black dwarf")
    # massive row (y = 174)
    svg += box(330, 174, 100, "red\nsupergiant")
    svg += arrow(430, 191, 450, 191)
    svg += box(450, 174, 80, "supernova")
    svg += arrow(530, 185, 555, 160)
    svg += arrow(530, 197, 555, 222)
    svg += box(555, 135, 90, "neutron star")
    svg += box(555, 212, 90, "black hole")
    svg += text(600, 128, "(very massive)", 9, INK2)
    svg += text(600, 262, "(most massive)", 9, INK2)
    svg += text(320, 262, "the heavier the star, the shorter its life and the more violent its end", 10, INK2)
    return svg
