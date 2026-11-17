"""
ra_diagrams.py — three diagrams for Topic 6, as inline SVG:
penetration of alpha, beta and gamma; Rutherford's scattering; a chain
reaction. Same helpers and colours as le_diagrams.py.
"""

from math import cos, radians, sin

from le_diagrams import INK, INK2, LINE, ACCENT, dashed, ray, solid, text


def penetration_svg():
    """Three sources on the left; paper, aluminium and lead barriers; each
    radiation stops where it stops."""
    svg = ""
    rows = [("alpha α", 60, "stopped by paper (or a few cm of air, or skin)"),
            ("beta β", 130, "stopped by a few mm of aluminium"),
            ("gamma γ", 200, "reduced by thick lead or concrete; never fully stopped")]
    barriers = [("paper", 170, 4), ("aluminium", 270, 10), ("lead", 380, 26)]
    for name, x, width in barriers:
        svg += "<rect x='%s' y='30' width='%s' height='200' style='fill:var(--line);opacity:0.35'/>" % (x, width)
        svg += text(x + width / 2, 24, name, 11, INK2)
    for name, y, note in rows:
        svg += "<circle cx='40' cy='%s' r='9' style='fill:var(--accent);opacity:0.8'/>" % y
        svg += text(40, y + 28, name, 12, INK)
        end = 170 if name.startswith("alpha") else 270 if name.startswith("beta") else 470
        if name.startswith("gamma"):
            svg += ray(50, y, 380, y, ACCENT, True, 2)
            svg += ray(406, y, 470, y, ACCENT, True, 1)
        else:
            svg += ray(50, y, end, y, ACCENT, True, 2)
            svg += text(end - 6, y - 8, "✕", 12, ACCENT, "end")
    svg += text(250, 258, "ionising power: alpha most, then beta, gamma least · penetration the other way round", 11, INK2)
    return svg


def rutherford_svg():
    """Alpha particles fired at a gold foil: most straight through, a few
    deflected, very few bounced back by a tiny nucleus."""
    svg = ""
    cx, cy = 300, 130
    svg += "<rect x='%s' y='40' width='6' height='180' style='fill:var(--line);opacity:0.35'/>" % (cx - 3)
    svg += text(cx, 32, "gold foil (a few atoms thick)", 11, INK2)
    svg += "<circle cx='%s' cy='%s' r='4' style='fill:var(--ink)'/>" % (cx, cy)
    svg += text(cx + 10, cy - 8, "nucleus", 10, INK2, "start")
    # most straight through
    for y in (70, 100, 160, 185):
        svg += ray(40, y, 560, y, ACCENT, True, 1.5)
    # a few deflected a little
    svg += ray(40, 118, cx, 120, ACCENT, True, 1.5)
    svg += ray(cx, 120, 560, 70, ACCENT, True, 1.5)
    svg += ray(40, 142, cx, 140, ACCENT, True, 1.5)
    svg += ray(cx, 140, 560, 200, ACCENT, True, 1.5)
    # very few bounced back
    svg += ray(40, 130, cx - 6, 130, INK, True, 2)
    svg += ray(cx - 6, 130, 40, 150, INK, True, 2)
    svg += text(100, 58, "most pass straight through → the atom is mostly empty space", 11, INK, "start")
    svg += text(330, 228, "a few deflected → the nucleus is positively charged", 11, INK, "start")
    svg += text(40, 252, "very few (about 1 in 8000) bounce back → the nucleus is tiny, dense and holds most of the mass", 11, INK, "start")
    return svg


def chain_svg():
    """One fission producing three neutrons, two of which cause further fissions."""
    svg = ""

    def nucleus(x, y, label, size=14):
        return ("<circle cx='%s' cy='%s' r='%s' style='fill:var(--accent);opacity:0.25;stroke:var(--accent);stroke-width:1.5'/>" % (x, y, size)
                + text(x, y + 4, label, 10, INK))

    def neutron(x, y):
        return "<circle cx='%s' cy='%s' r='4' style='fill:var(--ink)'/>" % (x, y)

    svg += neutron(30, 130)
    svg += ray(36, 130, 76, 130, INK2, True, 1.2)
    svg += text(30, 118, "n", 11, INK2)
    svg += nucleus(95, 130, "U-235")
    # products of first fission
    svg += nucleus(118, 104, "", 7)
    svg += nucleus(118, 156, "", 7)
    svg += text(70, 190, "two daughter nuclei", 10, INK2)
    for angle in (-40, 0, 40):
        ex = 95 + 85 * cos(radians(angle))
        ey = 130 + 85 * sin(radians(angle))
        svg += ray(112, 130, ex, ey, INK2, True, 1.2)
        svg += neutron(ex, ey)
    svg += text(185, 150, "2 or 3 neutrons", 10, INK2)
    svg += text(185, 115, "+ energy", 10, ACCENT)
    # second generation: top and bottom neutrons travel on and hit new nuclei
    svg += ray(166, 73, 243, 62, INK2, False, 1.2)
    svg += ray(166, 187, 243, 198, INK2, False, 1.2)
    for (nx, ny) in ((260, 60), (260, 200)):
        svg += nucleus(nx, ny, "U-235")
        for angle in (-35, 0, 35):
            ex = nx + 70 * cos(radians(angle))
            ey = ny + 70 * sin(radians(angle))
            svg += ray(nx + 16, ny, ex, ey, INK2, True, 1.2)
            svg += neutron(ex, ey)
    svg += text(400, 135, "…and so on: a chain reaction", 11, INK, "start")
    svg += text(20, 250, "drawn uncontrolled: two neutrons go on each time, so the fissions multiply; in a reactor the control rods absorb neutrons so that on average only one does", 10, INK2, "start")
    return svg
