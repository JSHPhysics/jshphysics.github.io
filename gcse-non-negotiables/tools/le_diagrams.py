"""
le_diagrams.py — the ray diagrams for Topic 5, as inline SVG strings.

All drawn with a few helpers so every diagram has the same look: solid
rays with an arrowhead half-way along, dashed normals, labelled angles.
Coordinates are in a 480 × 300 box unless the function says otherwise.
Colours come from the page's CSS variables so dark mode works.
"""

from math import atan2, cos, degrees, radians, sin, sqrt

INK = "var(--ink)"
INK2 = "var(--ink-2)"
LINE = "var(--line)"
ACCENT = "var(--accent)"
GLASS = "fill:var(--accent);opacity:0.10;stroke:var(--line);stroke-width:1.5"


def ray(x1, y1, x2, y2, colour=ACCENT, head=True, width=2):
    """A ray from (x1, y1) to (x2, y2) with an arrowhead at its midpoint."""
    svg = "<line x1='%.1f' y1='%.1f' x2='%.1f' y2='%.1f' style='stroke:%s;stroke-width:%s'/>" % (x1, y1, x2, y2, colour, width)
    if head:
        mx = (x1 + x2) / 2
        my = (y1 + y2) / 2
        angle = atan2(y2 - y1, x2 - x1)
        size = 7
        left = (mx - size * cos(angle - 0.5), my - size * sin(angle - 0.5))
        right = (mx - size * cos(angle + 0.5), my - size * sin(angle + 0.5))
        svg += "<polygon points='%.1f,%.1f %.1f,%.1f %.1f,%.1f' style='fill:%s'/>" % (mx, my, left[0], left[1], right[0], right[1], colour)
    return svg


def dashed(x1, y1, x2, y2, colour=INK2):
    return "<line x1='%.1f' y1='%.1f' x2='%.1f' y2='%.1f' style='stroke:%s;stroke-width:1.2;stroke-dasharray:5 4'/>" % (x1, y1, x2, y2, colour)


def solid(x1, y1, x2, y2, colour=LINE, width=2):
    return "<line x1='%.1f' y1='%.1f' x2='%.1f' y2='%.1f' style='stroke:%s;stroke-width:%s'/>" % (x1, y1, x2, y2, colour, width)


def text(x, y, label, size=14, colour=INK, anchor="middle", weight="normal", italic=False):
    style = "fill:%s;font-size:%spx;font-weight:%s;%s" % (colour, size, weight, "font-style:italic;" if italic else "")
    return "<text x='%.1f' y='%.1f' text-anchor='%s' style='%s'>%s</text>" % (x, y, anchor, style, label)


def arc(cx, cy, r, start_deg, end_deg, colour=INK2):
    """A small angle arc from start to end (degrees, SVG orientation: 0 = right, 90 = down)."""
    x1 = cx + r * cos(radians(start_deg))
    y1 = cy + r * sin(radians(start_deg))
    x2 = cx + r * cos(radians(end_deg))
    y2 = cy + r * sin(radians(end_deg))
    large = 1 if abs(end_deg - start_deg) > 180 else 0
    sweep = 1 if end_deg > start_deg else 0
    return "<path d='M %.1f %.1f A %s %s 0 %s %s %.1f %.1f' style='fill:none;stroke:%s;stroke-width:1.2'/>" % (x1, y1, r, r, large, sweep, x2, y2, colour)


def point_on(cx, cy, angle_deg, length):
    return (cx + length * cos(radians(angle_deg)), cy + length * sin(radians(angle_deg)))


# ---------------------------------------------------------------------
# Reflection at a plane mirror
# ---------------------------------------------------------------------

def reflection_svg():
    cx, cy = 240, 200
    svg = solid(60, cy, 420, cy, LINE, 3)
    # hatching behind the mirror
    for x in range(70, 420, 20):
        svg += solid(x, cy + 2, x - 8, cy + 12, LINE, 1)
    svg += dashed(cx, cy, cx, 40)
    # incident ray at 40° to the normal, from upper left
    start = point_on(cx, cy, -90 - 40, 150)
    end = point_on(cx, cy, -90 + 40, 150)
    svg += ray(start[0], start[1], cx, cy)
    svg += ray(cx, cy, end[0], end[1])
    svg += arc(cx, cy, 40, -90, -130)
    svg += arc(cx, cy, 40, -90, -50)
    svg += text(cx - 22, cy - 48, "i", 15, INK, "middle", "normal", True)
    svg += text(cx + 22, cy - 48, "r", 15, INK, "middle", "normal", True)
    svg += text(cx, 32, "normal", 12, INK2)
    svg += text(start[0] - 6, start[1] - 8, "incident ray", 12, INK2, "end")
    svg += text(end[0] + 6, end[1] - 8, "reflected ray", 12, INK2, "start")
    svg += text(430, cy + 5, "mirror", 12, INK2, "start")
    svg += text(cx, 250, "angle of incidence i = angle of reflection r, both measured from the normal", 12, INK2)
    return svg


# ---------------------------------------------------------------------
# Refraction through a rectangular glass block
# ---------------------------------------------------------------------

def refraction_svg():
    # block from y=110 to y=200, x 100..380
    top, bottom = 110, 200
    svg = "<rect x='100' y='%s' width='280' height='%s' style='%s'/>" % (top, bottom - top, GLASS)
    svg += text(372, 118 + 14, "glass", 12, INK2, "end")
    svg += text(372, top - 6, "air", 12, INK2, "end")
    # entry point
    ex, ey = 190, top
    # incident at 50° to normal from upper left
    i_deg = 50
    r_deg = 31  # sin r = sin 50 / 1.5 → r ≈ 30.7°
    start = point_on(ex, ey, -90 - i_deg, 110)
    svg += dashed(ex, 40, ex, 260)
    svg += ray(start[0], start[1], ex, ey)
    # refracted ray inside the block
    length_in = (bottom - top) / cos(radians(r_deg))
    exit_pt = point_on(ex, ey, 90 - r_deg, length_in)
    svg += ray(ex, ey, exit_pt[0], exit_pt[1])
    # emergent ray parallel to the incident ray
    svg += dashed(exit_pt[0], 40, exit_pt[0], 270)
    out = point_on(exit_pt[0], exit_pt[1], 90 - i_deg, 70)
    svg += ray(exit_pt[0], exit_pt[1], out[0], out[1])
    # angle arcs and labels
    svg += arc(ex, ey, 34, -90, -90 - i_deg)
    svg += arc(ex, ey, 34, 90, 90 - r_deg)
    svg += text(ex - 30, ey - 24, "i", 15, INK, "middle", "normal", True)
    svg += text(ex + 16, ey + 40, "r", 15, INK, "middle", "normal", True)
    svg += text(ex, 34, "normal", 12, INK2)
    svg += text(exit_pt[0] + 40, 250, "emergent ray, parallel to the incident ray", 12, INK2, "middle")
    svg += text(start[0] - 4, start[1] - 6, "incident ray", 12, INK2, "end")
    svg += text(ex + 50, ey + 60, "bends towards the normal", 11, INK2, "start")
    return svg


# ---------------------------------------------------------------------
# Total internal reflection: three cases in a semicircular block
# ---------------------------------------------------------------------

def tir_case(cx, cy, i_deg, r_deg, label, tir):
    """One semicircular block (flat face on top at y=cy) with a ray from
    below aimed at the centre of the flat face."""
    radius = 60
    svg = "<path d='M %.1f %.1f A %s %s 0 0 0 %.1f %.1f Z' style='%s'/>" % (cx - radius, cy, radius, radius, cx + radius, cy, GLASS)
    svg += dashed(cx, cy - 48, cx, cy + 70)
    start = point_on(cx, cy, 90 + i_deg, radius)
    svg += ray(start[0], start[1], cx, cy)
    if r_deg is not None:
        end = point_on(cx, cy, -90 + r_deg, 50)
        svg += ray(cx, cy, end[0], end[1])
    if tir or r_deg == 90:
        # reflected ray inside the block (weak for the partial case, strong for TIR)
        refl = point_on(cx, cy, 90 - i_deg, radius)
        svg += ray(cx, cy, refl[0], refl[1], ACCENT if tir else INK2, True, 2 if tir else 1)
    svg += text(cx, cy + 92, label, 12, INK2)
    return svg


def tir_svg():
    svg = text(90, 22, "i below the critical angle", 12, INK)
    svg += text(270, 22, "i = the critical angle", 12, INK)
    svg += text(450, 22, "i above the critical angle", 12, INK)
    svg += tir_case(90, 130, 25, 39, "refracts out of the glass", False)
    svg += tir_case(270, 130, 42, 90, "refracted ray along the surface: r = 90°", False)
    svg += tir_case(450, 130, 60, None, "total internal reflection", True)
    svg += text(270, 250, "Glass below the flat face, air above. The ray enters through the curved face aimed at the centre, so it does not bend there.", 11, INK2)
    return svg


# ---------------------------------------------------------------------
# Lenses
# ---------------------------------------------------------------------

def lens_shape(cx, cy, height, converging=True):
    if converging:
        return "<path d='M %.1f %.1f Q %.1f %.1f %.1f %.1f Q %.1f %.1f %.1f %.1f Z' style='%s'/>" % (
            cx, cy - height, cx + 16, cy, cx, cy + height, cx - 16, cy, cx, cy - height, GLASS)
    return "<path d='M %.1f %.1f L %.1f %.1f Q %.1f %.1f %.1f %.1f L %.1f %.1f Q %.1f %.1f %.1f %.1f Z' style='%s'/>" % (
        cx - 9, cy - height, cx + 9, cy - height, cx + 2, cy, cx + 9, cy + height, cx - 9, cy + height, cx - 2, cy, cx - 9, cy - height, GLASS)


def arrow_up(x, base_y, tip_y, colour=INK, label=None):
    svg = solid(x, base_y, x, tip_y, colour, 2.5)
    direction = -1 if tip_y < base_y else 1
    svg += "<polygon points='%.1f,%.1f %.1f,%.1f %.1f,%.1f' style='fill:%s'/>" % (x, tip_y, x - 5, tip_y - 8 * direction, x + 5, tip_y - 8 * direction, colour)
    if label:
        svg += text(x, (tip_y - 10) if direction < 0 else (tip_y + 16), label, 12, colour)
    return svg


def converging_lens_svg(object_distance, focal_length, title):
    """Ray diagram for a converging lens; distances in px, object height 40.
    Uses the three construction rays; the image is found from the lens equation."""
    cx, cy = 250, 150
    f = focal_length
    u = object_distance
    h = 40
    svg = solid(30, cy, 470, cy, LINE, 1)
    svg += lens_shape(cx, cy, 70, True)
    for sign in (-1, 1):
        for k in (1, 2):
            x = cx + sign * k * f
            svg += solid(x, cy - 5, x, cy + 5, INK2, 1.5)
            svg += text(x, cy + 20, ("F" if k == 1 else "2F"), 11, INK2)
    ox = cx - u
    svg += arrow_up(ox, cy, cy - h, INK, "object")
    if u > f:
        v = u * f / (u - f)
        m = -v / u
        ix = cx + v
        ih = h * (-m)
        # ray 1: parallel then through F on the far side
        svg += ray(ox, cy - h, cx, cy - h)
        far = (ix + 60, cy - h + (cy + ih - (cy - h)) * (ix + 60 - cx) / (ix - cx))
        svg += ray(cx, cy - h, far[0], far[1])
        # ray 2: through the optical centre, straight on
        svg += ray(ox, cy - h, cx, cy)
        svg += ray(cx, cy, ix + 60, cy + ih * (ix + 60 - cx) / (ix - cx))
        svg += arrow_up(ix, cy, cy + ih, ACCENT, "image")
        svg += text(ix, cy + ih + 30, "real, inverted", 11, ACCENT)
    else:
        v = u * f / (f - u)  # virtual image distance, on the object side
        m = v / u
        ix = cx - v
        ih = h * m
        # ray 1: parallel then through F on the far side; extend backwards (dashed)
        svg += ray(ox, cy - h, cx, cy - h)
        fx = cx + f
        slope = (cy - (cy - h)) / (fx - cx)
        svg += ray(cx, cy - h, 460, cy - h + slope * (460 - cx))
        svg += dashed(cx, cy - h, ix, cy - ih, ACCENT)
        # ray 2: through the optical centre
        svg += ray(ox, cy - h, cx, cy)
        slope2 = h / u
        svg += ray(cx, cy, 460, cy + slope2 * (460 - cx))
        svg += dashed(cx, cy, ix, cy - ih, ACCENT)
        svg += arrow_up(ix, cy, cy - ih, ACCENT, "image")
        svg += text(ix, cy + 40, "virtual, upright, magnified", 11, ACCENT)
    svg += text(250, 16, title, 13, INK)
    return svg


def diverging_lens_svg():
    cx, cy = 250, 150
    f = 70
    u = 120
    h = 40
    svg = solid(30, cy, 470, cy, LINE, 1)
    svg += lens_shape(cx, cy, 70, False)
    for sign in (-1, 1):
        x = cx + sign * f
        svg += solid(x, cy - 5, x, cy + 5, INK2, 1.5)
        svg += text(x, cy + 20, "F", 11, INK2)
    ox = cx - u
    svg += arrow_up(ox, cy, cy - h, INK, "object")
    v = u * f / (u + f)
    ix = cx - v
    ih = h * v / u
    # ray 1: parallel, then diverges as if from the near F
    svg += ray(ox, cy - h, cx, cy - h)
    fx = cx - f
    slope = (cy - h - cy) / (cx - fx)
    svg += ray(cx, cy - h, 460, cy - h + slope * (460 - cx))
    svg += dashed(fx, cy, cx, cy - h, ACCENT)
    # ray 2: through the centre
    svg += ray(ox, cy - h, cx, cy)
    svg += ray(cx, cy, 460, cy + (h / u) * (460 - cx))
    svg += arrow_up(ix, cy, cy - ih, ACCENT, "image")
    svg += text(ix, cy + 40, "virtual, upright, diminished", 11, ACCENT)
    svg += text(250, 24, "Diverging lens: the image is always virtual, upright and smaller", 13, INK)
    return svg


# ---------------------------------------------------------------------
# Colour: a red object in white light and in blue light
# ---------------------------------------------------------------------

def colour_svg():
    svg = ""
    for index, (incoming, reflected, label, seen) in enumerate([
        ("white light", "red", "red object in white light", "looks red"),
        ("blue light", None, "red object in blue light", "looks black"),
    ]):
        ox = 130 + index * 230
        svg += "<rect x='%s' y='120' width='60' height='60' rx='6' style='fill:#c0392b;opacity:0.85'/>" % (ox - 30)
        svg += ray(ox - 100, 60, ox - 30, 125, INK2)
        svg += text(ox - 60, 50, incoming, 11, INK2)
        if reflected:
            svg += ray(ox + 30, 125, ox + 110, 60, "#c0392b")
            svg += text(ox + 70, 50, "only red reflected", 11, "#c0392b")
        else:
            svg += text(ox + 70, 50, "nothing reflected", 11, INK2)
            svg += text(ox, 170, "all absorbed", 10, "#fff")
        svg += text(ox, 205, label, 12, INK)
        svg += text(ox, 222, seen, 12, INK, "middle", "bold")
    return svg


# ---------------------------------------------------------------------
# The EM spectrum strip
# ---------------------------------------------------------------------

def spectrum_svg():
    regions = ["radio", "micro-wave", "infrared", "visible", "ultra-violet", "X-rays", "gamma"]
    svg = ""
    width = 60
    for index, name in enumerate(regions):
        x = 20 + index * width
        shade = 0.08 + index * 0.06
        svg += "<rect x='%s' y='60' width='%s' height='50' style='fill:var(--accent);opacity:%.2f;stroke:var(--line);stroke-width:1'/>" % (x, width, shade)
        parts = name.split("-")
        if len(parts) == 2:
            svg += text(x + width / 2, 80, parts[0] + "-", 11, INK)
            svg += text(x + width / 2, 96, parts[1], 11, INK)
        else:
            svg += text(x + width / 2, 90, name, 11, INK)
    svg += ray(20, 140, 440, 140, INK2)
    svg += text(230, 160, "frequency increases  ·  energy increases  ·  danger increases", 12, INK)
    svg += ray(440, 190, 20, 190, INK2)
    svg += text(230, 210, "wavelength increases", 12, INK)
    svg += text(20, 48, "about 1 m and longer", 10, INK2, "start")
    svg += text(440, 48, "shorter than an atom", 10, INK2, "end")
    svg += text(230, 48, "visible: 400–700 nm", 10, INK2)
    return svg
