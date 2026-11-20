"""
fm_diagrams.py — the diagrams for Topic 15 (Forces and matter) as inline
SVG, drawn with the helpers in le_diagrams.py and fe_diagrams.py.

    two_forces_svg()    stretching needs two forces: hands, and a spring on a hook
    practical_svg()     the spring core practical: stand, spring, ruler, pointer, masses
    normal_svg()        fluid pressure acts normal to every surface
    depth_svg()         pressure in a liquid: the same depth, two densities
    upthrust_svg()      upthrust from the pressure difference on a submerged block
    floating_svg()      floating, sinking and the weight of fluid displaced
"""

from le_diagrams import ACCENT, INK, INK2, LINE, dashed, solid, text
from fe_diagrams import arrow, box, dot


def spring(x, y_top, y_bottom, width=18, coils=8, colour=INK):
    """A zig-zag spring from (x, y_top) to (x, y_bottom)."""
    length = y_bottom - y_top
    lead = 10
    step = (length - 2 * lead) / (coils * 2)
    points = ["%.1f,%.1f" % (x, y_top), "%.1f,%.1f" % (x, y_top + lead)]
    yy = y_top + lead
    side = 1
    for _ in range(coils * 2):
        yy += step
        points.append("%.1f,%.1f" % (x + side * width / 2, yy))
        side = -side
    points.append("%.1f,%.1f" % (x, y_bottom - lead + step))
    points.append("%.1f,%.1f" % (x, y_bottom))
    return "<polyline points='%s' style='fill:none;stroke:%s;stroke-width:2;stroke-linejoin:round'/>" % (" ".join(points), colour)


def mass(cx, y_top, w=36, h=26, label=None):
    svg = box(cx - w / 2, y_top, w, h, "var(--line)", 0.5)
    if label:
        svg += text(cx, y_top + h / 2 + 4, label, 11, INK)
    return svg


# ---------------------------------------------------------------------

def two_forces_svg():
    svg = ""
    # left panel: a spring pulled at both ends
    svg += text(165, 24, "pulled at both ends", 13, INK, weight="bold")
    svg += "<polyline points='70,80 80,80 84,68 92,92 100,68 108,92 116,68 124,92 132,68 140,92 148,68 156,92 164,68 172,92 180,68 188,92 196,68 204,92 212,68 220,92 228,68 236,92 244,68 252,80 262,80' style='fill:none;stroke:%s;stroke-width:2;stroke-linejoin:round'/>" % INK
    svg += arrow(70, 80, 22, 80, ACCENT, 2.4)
    svg += arrow(262, 80, 310, 80, ACCENT, 2.4)
    svg += text(46, 66, "F", 13, ACCENT, italic=True)
    svg += text(286, 66, "F", 13, ACCENT, italic=True)
    svg += text(165, 120, "two equal and opposite forces:", 11, INK2)
    svg += text(165, 136, "the spring stretches and stays still", 11, INK2)
    # middle panel: one force only
    svg += text(400, 24, "one force only", 13, INK, weight="bold")
    svg += "<polyline points='330,80 340,80 344,68 352,92 360,68 368,92 376,68 384,92 392,68 400,92 408,68 416,92 424,68 432,92 440,68 448,80 458,80' style='fill:none;stroke:%s;stroke-width:2;stroke-linejoin:round'/>" % INK
    svg += arrow(458, 80, 506, 80, ACCENT, 2.4)
    svg += text(482, 66, "F", 13, ACCENT, italic=True)
    svg += text(400, 120, "a resultant force: the whole spring", 11, INK2)
    svg += text(400, 136, "accelerates, it does not stretch", 11, INK2)
    # right panel: hanging from a hook — the hook supplies the second force
    svg += text(600, 24, "hung from a hook", 13, INK, weight="bold")
    svg += solid(560, 40, 640, 40, INK2, 3)
    svg += "<rect x='560' y='34' width='80' height='6' style='fill:%s;fill-opacity:0.3'/>" % LINE
    svg += spring(600, 40, 118, 18, 7)
    svg += mass(600, 118, 34, 24, "m")
    svg += arrow(632, 86, 632, 46, ACCENT, 2.2)
    svg += text(640, 70, "pull of hook", 10, ACCENT, anchor="start")
    svg += arrow(600, 142, 600, 176, ACCENT, 2.2)
    svg += text(612, 164, "weight", 10, ACCENT, anchor="start")
    svg += text(600, 194, "the support pulls up while the", 11, INK2)
    svg += text(600, 208, "weight pulls down: two forces", 11, INK2)
    return "<svg viewBox='0 0 680 220' xmlns='http://www.w3.org/2000/svg' role='img'>%s</svg>" % svg


def practical_svg():
    svg = ""
    # stand
    svg += box(40, 230, 150, 10, "var(--line)", 0.5)
    svg += solid(60, 230, 60, 30, INK2, 4)
    svg += solid(60, 40, 170, 40, INK2, 4)
    svg += "<rect x='50' y='34' width='20' height='12' style='fill:%s;fill-opacity:0.4'/>" % LINE
    # ruler
    svg += box(196, 40, 22, 190, "var(--line)", 0.2, INK2)
    for i in range(0, 191, 10):
        length = 10 if i % 50 == 0 else 6
        svg += solid(196, 40 + i, 196 + length, 40 + i, INK2, 1)
    svg += text(207, 246, "ruler", 10, INK2)
    svg += text(207, 258, "(mm)", 10, INK2)
    # unstretched spring (ghost) and stretched spring
    svg += "<g style='opacity:0.35'>%s</g>" % spring(150, 40, 110, 16, 6, INK2)
    svg += spring(150, 40, 160, 16, 6, INK)
    svg += mass(150, 160, 30, 20, "")
    svg += text(150, 174, "100 g", 9, INK)
    # pointer and readings
    svg += solid(150, 110, 194, 110, ACCENT, 1.4)
    svg += solid(150, 160, 194, 160, ACCENT, 1.4)
    svg += text(232, 114, "reading with no load", 10, INK2, anchor="start")
    svg += text(232, 164, "reading with the load", 10, INK2, anchor="start")
    svg += arrow(222, 118, 222, 154, ACCENT, 1.8)
    svg += arrow(222, 152, 222, 118, ACCENT, 1.8)
    svg += text(232, 140, "extension = difference", 10, ACCENT, anchor="start")
    svg += text(232, 190, "read both at eye level,", 10, INK2, anchor="start")
    svg += text(232, 204, "pointer against the scale", 10, INK2, anchor="start")
    # right side: the graph sketch
    gx, gy, gw, gh = 430, 40, 200, 170
    svg += solid(gx, gy + gh, gx + gw, gy + gh, INK2, 1.6)
    svg += solid(gx, gy + gh, gx, gy, INK2, 1.6)
    svg += text(gx + gw / 2, gy + gh + 22, "extension", 11, INK2)
    svg += text(gx - 10, gy + gh / 2, "force", 11, INK2, anchor="end")
    svg += solid(gx, gy + gh, gx + 130, gy + gh - 120, ACCENT, 2.2)
    svg += "<path d='M %d %d Q %d %d %d %d' style='fill:none;stroke:%s;stroke-width:2.2'/>" % (gx + 130, gy + gh - 120, gx + 170, gy + gh - 150, gx + 195, gy + gh - 158, ACCENT)
    svg += dot(gx + 130, gy + gh - 120, 3.5, INK)
    svg += text(gx + 120, gy + gh - 130, "limit of proportionality", 10, INK, anchor="end")
    svg += dashed(gx, gy + gh - 60, gx + 65, gy + gh - 60, INK2)
    svg += dashed(gx + 65, gy + gh - 60, gx + 65, gy + gh, INK2)
    svg += text(gx + 70, gy + gh - 28, "gradient = k", 10, INK2, anchor="start")
    svg += text(gx + 100, gy + gh + 40, "area under the line = work done", 10, INK2)
    svg += text(gx + 100, 24, "force–extension graph", 13, INK, weight="bold")
    svg += text(140, 24, "the practical", 13, INK, weight="bold")
    return "<svg viewBox='0 0 660 270' xmlns='http://www.w3.org/2000/svg' role='img'>%s</svg>" % svg


def normal_svg():
    svg = ""
    svg += text(330, 24, "pressure in a fluid acts at right angles to every surface", 13, INK, weight="bold")
    # tank
    x0, y0, w, h = 120, 60, 260, 170
    svg += solid(x0, y0, x0, y0 + h, INK, 3)
    svg += solid(x0, y0 + h, x0 + w, y0 + h, INK, 3)
    svg += solid(x0 + w, y0 + h, x0 + w, y0, INK, 3)
    svg += "<rect x='%d' y='%d' width='%d' height='%d' style='fill:%s;fill-opacity:0.15'/>" % (x0, y0 + 20, w, h - 20, ACCENT)
    svg += "<path d='M %d %d q 20 -8 40 0 t 40 0 t 40 0 t 40 0 t 40 0 t 40 0 t 20 0' style='fill:none;stroke:%s;stroke-width:1.6'/>" % (x0, y0 + 20, ACCENT)
    # arrows on walls: perpendicular, longer with depth
    for i, yy in enumerate([100, 140, 180, 215]):
        length = 14 + i * 7
        svg += arrow(x0 + 4 + length, yy, x0 + 4, yy, ACCENT, 1.8)
        svg += arrow(x0 + w - 4 - length, yy, x0 + w - 4, yy, ACCENT, 1.8)
    for xx in [160, 200, 240, 280, 320, 360]:
        svg += arrow(xx, y0 + h - 44, xx, y0 + h - 4, ACCENT, 1.8)
    # a submerged object with arrows on all faces
    bx, by = 230, 110
    svg += box(bx, by, 40, 40, "var(--line)", 0.6)
    svg += arrow(bx - 22, by + 20, bx - 2, by + 20, INK, 1.6)
    svg += arrow(bx + 62, by + 20, bx + 42, by + 20, INK, 1.6)
    svg += arrow(bx + 20, by - 20, bx + 20, by - 2, INK, 1.6)
    svg += arrow(bx + 20, by + 64, bx + 20, by + 42, INK, 1.6)
    svg += text(250, 262, "the arrows get longer with depth; on the block they push on every face", 11, INK2)
    # right: the aeroplane window
    svg += text(540, 60, "aeroplane window", 12, INK, weight="bold")
    svg += "<rect x='500' y='80' width='80' height='110' rx='18' style='fill:none;stroke:%s;stroke-width:2.4'/>" % INK
    svg += text(540, 110, "inside", 10, INK2)
    svg += text(540, 124, "80 kPa", 10, INK2)
    svg += text(620, 110, "outside", 10, INK2, anchor="start")
    svg += text(620, 124, "23 kPa", 10, INK2, anchor="start")
    svg += arrow(540, 150, 598, 150, ACCENT, 2.2)
    svg += text(540, 212, "net force outward,", 10, INK2)
    svg += text(540, 226, "normal to the window", 10, INK2)
    return "<svg viewBox='0 0 660 275' xmlns='http://www.w3.org/2000/svg' role='img'>%s</svg>" % svg


def depth_svg():
    svg = ""
    svg += text(330, 24, "pressure in a liquid: deeper, and denser, means more", 13, INK, weight="bold")
    for cx, label, dens in [(170, "fresh water", 0.15), (430, "sea water", 0.3)]:
        x0, y0, w, h = cx - 90, 50, 180, 180
        svg += solid(x0, y0, x0, y0 + h, INK, 2.4)
        svg += solid(x0, y0 + h, x0 + w, y0 + h, INK, 2.4)
        svg += solid(x0 + w, y0 + h, x0 + w, y0, INK, 2.4)
        svg += "<rect x='%d' y='%d' width='%d' height='%d' style='fill:%s;fill-opacity:%s'/>" % (x0, y0 + 10, w, h - 10, ACCENT, dens)
        svg += text(cx, y0 + h + 22, label, 12, INK)
        svg += text(cx, y0 + h + 38, "1000 kg/m³" if dens < 0.2 else "1030 kg/m³", 10, INK2)
        # arrows on the right wall, lengthening with depth
        scale = 1.0 if dens < 0.2 else 1.3
        for i, dy in enumerate([30, 70, 110, 150]):
            length = (10 + i * 10) * scale
            svg += arrow(x0 + w - 4 - length, y0 + dy + 10, x0 + w - 4, y0 + dy + 10, ACCENT, 1.8)
        # depth marker
        svg += dashed(x0 + 20, y0 + 10, x0 + 20, y0 + 160, INK2)
        svg += arrow(x0 + 20, y0 + 10, x0 + 20, y0 + 160, INK2, 1.4)
        svg += text(x0 + 28, y0 + 90, "h", 12, INK, anchor="start", italic=True)
    svg += text(600, 80, "P = h ρ g", 13, INK, italic=True)
    svg += text(600, 104, "same h, larger ρ,", 10, INK2)
    svg += text(600, 118, "larger P", 10, INK2)
    svg += text(600, 150, "the column of liquid", 10, INK2)
    svg += text(600, 164, "above has more weight", 10, INK2)
    svg += text(600, 178, "when it is deeper", 10, INK2)
    svg += text(600, 192, "or denser", 10, INK2)
    return "<svg viewBox='0 0 660 275' xmlns='http://www.w3.org/2000/svg' role='img'>%s</svg>" % svg


def upthrust_svg():
    svg = ""
    svg += text(330, 24, "where upthrust comes from", 13, INK, weight="bold")
    x0, y0, w, h = 60, 50, 260, 190
    svg += solid(x0, y0, x0, y0 + h, INK, 2.4)
    svg += solid(x0, y0 + h, x0 + w, y0 + h, INK, 2.4)
    svg += solid(x0 + w, y0 + h, x0 + w, y0, INK, 2.4)
    svg += "<rect x='%d' y='%d' width='%d' height='%d' style='fill:%s;fill-opacity:0.15'/>" % (x0, y0 + 14, w, h - 14, ACCENT)
    bx, by, bw, bh = 150, 110, 80, 70
    svg += box(bx, by, bw, bh, "var(--line)", 0.6)
    # top face: short arrows down; bottom face: long arrows up
    for xx in [bx + 16, bx + 40, bx + 64]:
        svg += arrow(xx, by - 24, xx, by - 2, ACCENT, 1.8)
        svg += arrow(xx, by + bh + 44, xx, by + bh + 2, ACCENT, 1.8)
    # sides cancel
    svg += arrow(bx - 30, by + 35, bx - 2, by + 35, INK2, 1.6)
    svg += arrow(bx + bw + 30, by + 35, bx + bw + 2, by + 35, INK2, 1.6)
    svg += text(190, 84, "smaller pressure on the top", 10, INK2)
    svg += text(190, 256, "larger pressure on the bottom", 10, INK2)
    svg += text(190, 272, "sideways forces cancel; the vertical ones do not", 11, INK2)
    # right: free body
    svg += text(500, 60, "forces on the block", 12, INK, weight="bold")
    svg += box(470, 110, 60, 60, "var(--line)", 0.6)
    svg += arrow(500, 110, 500, 60, ACCENT, 2.6)
    svg += text(512, 80, "upthrust", 11, ACCENT, anchor="start")
    svg += text(512, 94, "= weight of fluid displaced", 10, ACCENT, anchor="start")
    svg += arrow(500, 170, 500, 236, INK, 2.6)
    svg += text(512, 210, "weight", 11, INK, anchor="start")
    svg += text(500, 262, "sinks if weight > upthrust", 11, INK2)
    return "<svg viewBox='0 0 660 284' xmlns='http://www.w3.org/2000/svg' role='img'>%s</svg>" % svg


def floating_svg():
    svg = ""
    svg += text(330, 24, "floating: the object sinks until the fluid displaced weighs as much as it does", 13, INK, weight="bold")
    panels = [(120, "wood", 0.45, "floats high: little water", "displaced weighs as much"),
              (330, "ice", 0.9, "floats low: most of it under,", "displaced water = its weight"),
              (540, "steel", 1.0, "sinks: even fully under, the", "displaced water weighs less")]
    for cx, label, frac, l1, l2 in panels:
        x0, y0, w, h = cx - 85, 50, 170, 150
        svg += solid(x0, y0, x0, y0 + h, INK, 2)
        svg += solid(x0, y0 + h, x0 + w, y0 + h, INK, 2)
        svg += solid(x0 + w, y0 + h, x0 + w, y0, INK, 2)
        water_top = y0 + 30
        svg += "<rect x='%d' y='%d' width='%d' height='%d' style='fill:%s;fill-opacity:0.15'/>" % (x0, water_top, w, y0 + h - water_top, ACCENT)
        bw, bh = 60, 50
        if label == "steel":
            by = y0 + h - bh - 4
        else:
            by = water_top - bh * (1 - frac)
        svg += box(cx - bw / 2, by, bw, bh, "var(--line)", 0.75)
        svg += text(cx, by + bh / 2 + 4, label, 11, INK)
        # forces
        up_len = 30 if label != "steel" else 18
        svg += arrow(cx + 42, by + bh / 2 + 16, cx + 42, by + bh / 2 + 16 - up_len, ACCENT, 1.8)
        svg += arrow(cx + 56, by + bh / 2 - 16, cx + 56, by + bh / 2 - 16 + 30, INK, 1.8)
        svg += text(cx, y0 + h + 22, l1, 10, INK2)
        svg += text(cx, y0 + h + 36, l2, 10, INK2)
    svg += text(330, 262, "arrows: upthrust (coloured) and weight (black). Floating means they are equal.", 11, INK2)
    return "<svg viewBox='0 0 660 272' xmlns='http://www.w3.org/2000/svg' role='img'>%s</svg>" % svg
