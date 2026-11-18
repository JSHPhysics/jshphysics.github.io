"""
fe_diagrams.py — the diagrams for Topic 9 (Forces and their effects), as
inline SVG strings, drawn with the helpers in le_diagrams.py.

    free_body_svg()    a block on a table: weight and normal contact force
    pair_svg()         the interaction pair (book on table) vs the balanced pair
    resultant_svg()    3 N and 4 N at right angles: tip-to-tail and the 5 N resultant
    resolve_svg()      a 10 N pull at 30° split into two components
    triangle_svg()     three forces in equilibrium drawn as a closed triangle
    moment_svg()       a spanner: perpendicular distance, including an angled push
    beam_svg()         a beam on a pivot with a load each side
    lever_svg()        a crowbar: effort, load, pivot and the two distances
    gears_svg()        a small gear driving a large one: teeth, directions, radii
    winch_svg()        the hand winch: handle on gear Y, gear X on the drum, load
"""

from math import cos, radians, sin

from le_diagrams import ACCENT, INK, INK2, LINE, arc, dashed, ray, solid, text


def arrow(x1, y1, x2, y2, colour=ACCENT, width=2.2):
    """A force arrow with its head at the END (not the midpoint as ray() does)."""
    from math import atan2
    svg = "<line x1='%.1f' y1='%.1f' x2='%.1f' y2='%.1f' style='stroke:%s;stroke-width:%s'/>" % (x1, y1, x2, y2, colour, width)
    angle = atan2(y2 - y1, x2 - x1)
    size = 9
    left = (x2 - size * cos(angle - 0.45), y2 - size * sin(angle - 0.45))
    right = (x2 - size * cos(angle + 0.45), y2 - size * sin(angle + 0.45))
    svg += "<polygon points='%.1f,%.1f %.1f,%.1f %.1f,%.1f' style='fill:%s'/>" % (x2, y2, left[0], left[1], right[0], right[1], colour)
    return svg


def box(x, y, w, h, fill="var(--line)", opacity=0.25, stroke=INK2):
    return "<rect x='%s' y='%s' width='%s' height='%s' style='fill:%s;opacity:%s;stroke:%s;stroke-width:1.4'/>" % (x, y, w, h, fill, opacity, stroke)


def dot(x, y, r=3.5, colour=INK):
    return "<circle cx='%.1f' cy='%.1f' r='%s' style='fill:%s'/>" % (x, y, r, colour)


# ---------------------------------------------------------------------

def free_body_svg():
    """Left: the real picture (block on a table). Right: the free body diagram
    — a dot with two labelled arrows of equal length through the centre."""
    svg = ""
    # left: picture
    svg += solid(20, 170, 200, 170, INK2, 3)
    svg += box(70, 110, 100, 60)
    svg += text(120, 145, "block", 12, INK)
    svg += text(110, 195, "the situation", 11, INK2)
    # right: free body diagram
    cx, cy = 340, 140
    svg += box(cx - 35, cy - 25, 70, 50)
    svg += dot(cx, cy)
    svg += arrow(cx, cy, cx, cy + 70, ACCENT)
    svg += text(cx + 12, cy + 62, "weight 5 N", 12, ACCENT, "start")
    svg += arrow(cx, cy, cx, cy - 70, INK)
    svg += text(cx + 12, cy - 55, "normal contact force 5 N", 12, INK, "start")
    svg += text(cx, 235, "free body force diagram: one object, arrows from its centre,", 11, INK2)
    svg += text(cx, 250, "labelled, lengths in proportion", 11, INK2)
    # a crossed-out bad version
    bx, by = 580, 140
    svg += box(bx - 35, by - 25, 70, 50)
    svg += arrow(bx - 30, by + 25, bx - 30, by + 75, ACCENT)
    svg += arrow(bx + 30, by - 25, bx + 30, by - 60, INK)
    svg += solid(bx - 45, by - 70, bx + 45, by + 85, "var(--accent)", 2)
    svg += solid(bx + 45, by - 70, bx - 45, by + 85, "var(--accent)", 2)
    svg += text(bx, 235, "not this: arrows at the edges", 11, INK2)
    svg += text(bx, 250, "(it would spin) and unequal", 11, INK2)
    return svg


def pair_svg():
    """Interaction pair (book pushes table, table pushes book) against the
    balanced pair on the book alone."""
    svg = ""
    # left: interaction pair
    svg += solid(20, 150, 230, 150, INK2, 3)
    svg += box(80, 100, 90, 50)
    svg += text(125, 130, "book", 12, INK)
    svg += arrow(125, 100, 125, 45, INK)
    svg += text(135, 60, "table pushes book up", 11, INK, "start")
    svg += arrow(125, 150, 125, 205, INK)
    svg += text(135, 200, "book pushes table down", 11, INK, "start")
    svg += text(125, 245, "an interaction pair: same size, opposite,", 11, INK2)
    svg += text(125, 260, "same type (contact), on different objects", 11, INK2)
    # right: balanced forces on one object
    svg += solid(370, 150, 580, 150, INK2, 3)
    svg += box(430, 100, 90, 50)
    svg += text(475, 130, "book", 12, INK)
    svg += arrow(475, 125, 475, 45, INK)
    svg += text(485, 60, "normal contact force", 11, INK, "start")
    svg += arrow(475, 125, 475, 205, ACCENT)
    svg += text(485, 200, "weight (Earth pulls book)", 11, ACCENT, "start")
    svg += text(475, 245, "balanced forces: both on the book,", 11, INK2)
    svg += text(475, 260, "different types (contact and gravity) — not a pair", 11, INK2)
    return svg


def resultant_svg():
    """3 N east and 4 N north at point X: tip-to-tail and the 5 N resultant."""
    scale = 28  # px per newton
    svg = ""
    # left: the forces on the object
    ox, oy = 90, 190
    svg += dot(ox, oy)
    svg += text(ox - 10, oy + 16, "X", 12, INK, "end")
    svg += arrow(ox, oy, ox + 3 * scale, oy, INK)
    svg += text(ox + 1.5 * scale, oy + 18, "3 N", 12, INK)
    svg += arrow(ox, oy, ox, oy - 4 * scale, INK)
    svg += text(ox - 8, oy - 2 * scale, "4 N", 12, INK, "end")
    svg += text(ox + 40, 250, "the two forces", 11, INK2)
    # right: tip to tail
    px, py = 330, 190
    svg += text(px - 10, py + 16, "X", 12, INK, "end")
    svg += arrow(px, py, px + 3 * scale, py, INK)
    svg += text(px + 1.5 * scale, py + 18, "3 N", 12, INK)
    svg += arrow(px + 3 * scale, py, px + 3 * scale, py - 4 * scale, INK)
    svg += text(px + 3 * scale + 8, py - 2 * scale, "4 N", 12, INK, "start")
    svg += arrow(px, py, px + 3 * scale, py - 4 * scale, ACCENT, 3)
    svg += text(px + 1.5 * scale - 8, py - 2.6 * scale, "resultant 5 N", 12, ACCENT, "end")
    svg += arc(px, py, 30, -53, 0)
    svg += text(px + 40, py - 8, "53°", 11, INK2, "start")
    svg += text(px + 50, 250, "tip to tail: scale 1 cm = 1 N; measure the", 11, INK2)
    svg += text(px + 50, 265, "closing line (5.0 cm) and its angle (53° above the 3 N)", 11, INK2)
    # scale bar
    svg += solid(520, 60, 520 + scale, 60, INK, 2)
    svg += solid(520, 55, 520, 65, INK, 1.5)
    svg += solid(520 + scale, 55, 520 + scale, 65, INK, 1.5)
    svg += text(520 + scale / 2, 50, "1 N", 11, INK2)
    return svg


def resolve_svg():
    """A 10 N pull on a sledge at 30° above the horizontal, split into
    horizontal and vertical components by scale drawing."""
    scale = 22
    ox, oy = 120, 200
    ang = radians(30)
    fx = ox + 10 * scale * cos(ang)
    fy = oy - 10 * scale * sin(ang)
    svg = ""
    svg += solid(20, oy + 20, 420, oy + 20, INK2, 3)
    svg += box(ox - 50, oy, 100, 20)
    svg += text(ox, oy + 14, "sledge", 11, INK)
    svg += arrow(ox, oy, fx, fy, ACCENT, 3)
    svg += text(fx - 60, fy - 10, "10 N pull", 12, ACCENT, "start")
    # components
    svg += dashed(fx, fy, fx, oy)
    svg += dashed(fx, fy, ox, fy)
    svg += arrow(ox, oy, fx, oy, INK)
    svg += text(ox + 100, oy - 8, "horizontal component", 11, INK, "start")
    svg += text(ox + 100, oy + 40, "measures 8.7 cm → 8.7 N", 11, INK2, "start")
    svg += arrow(ox, oy, ox, fy, INK)
    svg += text(ox - 8, (oy + fy) / 2, "vertical", 11, INK, "end")
    svg += text(ox - 8, (oy + fy) / 2 + 14, "5.0 cm → 5 N", 11, INK2, "end")
    svg += arc(ox, oy, 40, -30, 0)
    svg += text(ox + 48, oy - 8, "30°", 11, INK2, "start")
    svg += text(470, 120, "Scale 1 cm = 1 N.", 12, INK, "start")
    svg += text(470, 140, "Draw the force to scale at the", 11, INK2, "start")
    svg += text(470, 155, "right angle, drop perpendiculars", 11, INK2, "start")
    svg += text(470, 170, "to the two directions, measure.", 11, INK2, "start")
    svg += text(470, 195, "The two components together", 11, INK2, "start")
    svg += text(470, 210, "have exactly the same effect", 11, INK2, "start")
    svg += text(470, 225, "as the one 10 N force.", 11, INK2, "start")
    return svg


def triangle_svg():
    """A sign hanging from two strings at 90° to each other; the three forces
    close into a right-angled triangle."""
    svg = ""
    # left: the picture
    ax, ay = 60, 40
    bx, by = 260, 40
    px, py = 160, 140
    svg += solid(30, ay, 290, ay, INK2, 4)
    svg += solid(ax, ay, px, py, INK, 2)
    svg += solid(bx, by, px, py, INK, 2)
    svg += box(px - 40, py, 80, 40)
    svg += text(px, py + 25, "sign 10 N", 11, INK)
    svg += dot(px, py)
    svg += arrow(px, py, px - 56, py - 56, ACCENT)
    svg += text(px - 70, py - 60, "T₁", 12, ACCENT, "end")
    svg += arrow(px, py, px + 56, py - 56, ACCENT)
    svg += text(px + 70, py - 60, "T₂", 12, ACCENT, "start")
    svg += arrow(px, py, px, py + 80, INK)
    svg += text(px + 8, py + 78, "W = 10 N", 11, INK, "start")
    svg += text(160, 250, "three forces on the knot, resultant zero", 11, INK2)
    # right: the closed triangle, tip to tail, scale 8 px per N
    s = 8
    sx, sy = 420, 60
    wx, wy = sx, sy + 10 * s
    # T1 from the bottom of W goes up-left at 45°: its length is 10/√2 ≈ 7.07 N
    t = 10 / 2 ** 0.5
    t1x = wx - t * s * cos(radians(45))
    t1y = wy - t * s * sin(radians(45))
    svg += arrow(sx, sy, wx, wy, INK)
    svg += text(wx + 8, (sy + wy) / 2, "W 10 N", 11, INK, "start")
    svg += arrow(wx, wy, t1x, t1y, ACCENT)
    svg += text(t1x - 6, t1y + 26, "T₁ 7.1 N", 11, ACCENT, "end")
    svg += arrow(t1x, t1y, sx, sy, ACCENT)
    svg += text(t1x - 6, t1y - 14, "T₂ 7.1 N", 11, ACCENT, "end")
    svg += text(450, 250, "drawn tip to tail the forces close:", 11, INK2)
    svg += text(450, 265, "measure T₁ and T₂ from the drawing", 11, INK2)
    return svg


def moment_svg():
    """A spanner on a nut. Left: force at right angles, distance d. Right: the
    same force pushed at an angle — the perpendicular distance is shorter."""
    svg = ""
    for i, (angled, label) in enumerate(((False, "force at right angles to the spanner"), (True, "the same force at an angle"))):
        ox = 110 + i * 310
        oy = 110
        # nut and spanner
        svg += "<circle cx='%s' cy='%s' r='14' style='fill:var(--line);opacity:0.5;stroke:%s;stroke-width:1.4'/>" % (ox, oy, INK2)
        svg += dot(ox, oy, 3, INK)
        svg += box(ox, oy - 8, 170, 16)
        hx = ox + 160
        if not angled:
            svg += arrow(hx, oy, hx, oy + 70, ACCENT, 3)
            svg += text(hx + 8, oy + 62, "F = 20 N", 12, ACCENT, "start")
            svg += dashed(ox, oy + 95, hx, oy + 95, INK2)
            svg += text((ox + hx) / 2, oy + 112, "d = 0.30 m (perpendicular distance)", 11, INK2)
            svg += text(ox + 85, oy + 135, "moment = 20 × 0.30 = 6 N m", 12, INK)
        else:
            ang = radians(50)
            ex = hx + 70 * cos(ang)
            ey = oy + 70 * sin(ang)
            svg += arrow(hx, oy, ex, ey, ACCENT, 3)
            svg += text(ex + 6, ey, "F = 20 N", 12, ACCENT, "start")
            svg += dashed(hx, oy, hx + 40, oy, INK2)
            svg += arc(hx, oy, 26, 0, 50)
            svg += text(hx + 32, oy + 24, "50°", 11, INK2, "start")
            # perpendicular distance from pivot to the line of action
            # line of action through (hx, oy) with direction (cos ang, sin ang)
            # foot of perpendicular from (ox, oy): t = ((ox-hx)cos + 0) ... compute
            dxl, dyl = cos(ang), sin(ang)
            tpar = (ox - hx) * dxl + (oy - oy) * dyl
            footx = hx + tpar * dxl
            footy = oy + tpar * dyl
            svg += dashed(footx, footy, hx, oy, INK2)
            svg += dashed(ox, oy, footx, footy, INK2)
            svg += text(ox - 20, oy - 100, "perpendicular distance from the pivot", 11, INK2, "start")
            svg += text(ox - 20, oy - 86, "to the line of action: 0.30 × sin 50° = 0.23 m", 11, INK2, "start")
            svg += text(ox + 85, oy + 135, "moment = 20 × 0.23 = 4.6 N m — smaller", 12, INK)
        svg += text(ox + 85, oy + 158, label, 11, INK2)
    return svg


def beam_svg():
    """A uniform beam on a pivot with a load each side, for the principle of
    moments: anticlockwise on the left, clockwise on the right."""
    svg = ""
    px, py = 300, 150
    svg += box(60, py - 8, 480, 16)
    svg += "<polygon points='%s,%s %s,%s %s,%s' style='fill:var(--line);opacity:0.5;stroke:%s;stroke-width:1.4'/>" % (px, py + 8, px - 22, py + 50, px + 22, py + 50, INK2)
    svg += solid(40, py + 50, 560, py + 50, INK2, 3)
    svg += text(px, py + 68, "pivot", 11, INK2)
    # left load 200 N at 1.5 m
    lx = px - 180
    svg += arrow(lx, py + 8, lx, py + 8 + 60, ACCENT, 3)
    svg += text(lx - 8, py + 60, "200 N", 12, ACCENT, "end")
    svg += dashed(lx, py - 30, lx, py - 10)
    svg += dashed(px, py - 30, px, py - 10)
    svg += solid(lx, py - 22, px, py - 22, INK2, 1.2)
    svg += text((lx + px) / 2, py - 30, "1.5 m", 11, INK2)
    # right load 300 N at 1.0 m
    rx = px + 120
    svg += arrow(rx, py + 8, rx, py + 8 + 90, ACCENT, 3)
    svg += text(rx + 8, py + 90, "300 N", 12, ACCENT, "start")
    svg += dashed(rx, py - 30, rx, py - 10)
    svg += solid(px, py - 22, rx, py - 22, INK2, 1.2)
    svg += text((px + rx) / 2, py - 30, "1.0 m", 11, INK2)
    # turning arrows
    svg += arc(px, py, 70, 250, 200, INK2)
    svg += text(px - 95, py - 55, "anticlockwise", 11, INK2, "end")
    svg += text(px - 95, py - 41, "200 × 1.5 = 300 N m", 11, INK2, "end")
    svg += arc(px, py, 70, 290, 340, INK2)  # clockwise on screen
    svg += text(px + 95, py - 55, "clockwise", 11, INK2, "start")
    svg += text(px + 95, py - 41, "300 × 1.0 = 300 N m", 11, INK2, "start")
    svg += text(px, 40, "balanced: sum of clockwise moments = sum of anticlockwise moments", 12, INK)
    return svg


def lever_svg():
    """A crowbar lifting a rock: small effort far from the pivot, large load
    close to it."""
    svg = ""
    px, py = 150, 170
    # ground and pivot (fulcrum)
    svg += solid(20, py + 30, 580, py + 30, INK2, 3)
    svg += "<polygon points='%s,%s %s,%s %s,%s' style='fill:var(--line);opacity:0.5;stroke:%s;stroke-width:1.4'/>" % (px, py, px - 16, py + 30, px + 16, py + 30, INK2)
    svg += text(px, py + 48, "pivot", 11, INK2)
    # bar from (px-60, py+15) to (px+380, py-40): slight tilt
    x0, y0 = px - 70, py + 14
    x1, y1 = px + 400, py - 44
    svg += "<line x1='%s' y1='%s' x2='%s' y2='%s' style='stroke:%s;stroke-width:9;stroke-linecap:round'/>" % (x0, y0, x1, y1, INK2)
    # rock on the short end
    svg += "<ellipse cx='%s' cy='%s' rx='30' ry='24' style='fill:var(--line);opacity:0.5;stroke:%s;stroke-width:1.4'/>" % (px - 63, py - 14, INK2)
    svg += arrow(px - 63, py - 14, px - 63, py + 45, ACCENT, 3)
    svg += text(px - 63, py - 50, "load 600 N", 12, ACCENT)
    # effort on the long end
    ex = px + 380
    ey = py - 41
    svg += arrow(ex, ey - 70, ex, ey - 6, INK, 3)
    svg += text(ex + 10, ey - 50, "effort 100 N", 12, INK, "start")
    # distances
    svg += dashed(px - 63, py + 60, px - 63, py + 80)
    svg += dashed(px, py + 60, px, py + 80)
    svg += dashed(ex, py + 60, ex, py + 80)
    svg += solid(px - 63, py + 72, px, py + 72, INK2, 1.2)
    svg += text(px - 31, py + 95, "0.2 m", 11, INK2)
    svg += solid(px, py + 72, ex, py + 72, INK2, 1.2)
    svg += text((px + ex) / 2, py + 95, "1.2 m", 11, INK2)
    svg += text(330, 50, "effort × effort distance = load × load distance", 12, INK)
    svg += text(330, 70, "100 × 1.2 = 600 × 0.2 = 120 N m", 12, INK2)
    return svg


def gear(cx, cy, r, teeth, colour=INK2):
    """A gear wheel drawn as a circle with small rectangular teeth."""
    svg = "<circle cx='%s' cy='%s' r='%s' style='fill:var(--line);opacity:0.25;stroke:%s;stroke-width:1.4'/>" % (cx, cy, r, colour)
    for i in range(teeth):
        a = 2 * 3.14159265 * i / teeth
        x1 = cx + r * cos(a)
        y1 = cy + r * sin(a)
        x2 = cx + (r + 7) * cos(a)
        y2 = cy + (r + 7) * sin(a)
        svg += "<line x1='%.1f' y1='%.1f' x2='%.1f' y2='%.1f' style='stroke:%s;stroke-width:4;stroke-linecap:round'/>" % (x1, y1, x2, y2, colour)
    svg += dot(cx, cy, 3, INK)
    return svg


def gears_svg():
    """A small driving gear (10 teeth) turning a large driven gear (20 teeth)."""
    svg = ""
    sx, sy, sr = 150, 140, 40
    lr = 80
    lx, ly = sx + sr + lr + 12, 140
    svg += gear(sx, sy, sr, 10)
    svg += gear(lx, ly, lr, 20)
    svg += text(sx, sy - sr - 22, "driving gear A: 10 teeth", 11, INK)
    svg += text(lx, ly - lr - 22, "driven gear B: 20 teeth", 11, INK)
    # rotation arrows
    svg += arc(sx, sy, sr - 14, 200, 340, ACCENT)
    svg += arrow(sx + (sr - 14) * cos(radians(340)), sy + (sr - 14) * sin(radians(340)), sx + (sr - 14) * cos(radians(350)), sy + (sr - 14) * sin(radians(350)), ACCENT)
    svg += text(sx, sy + sr + 30, "clockwise, 2 turns", 11, ACCENT)
    svg += arc(lx, ly, lr - 20, 340, 200, ACCENT)
    svg += arrow(lx + (lr - 20) * cos(radians(200)), ly + (lr - 20) * sin(radians(200)), lx + (lr - 20) * cos(radians(190)), ly + (lr - 20) * sin(radians(190)), ACCENT)
    svg += text(lx, ly + lr + 30, "anticlockwise, 1 turn", 11, ACCENT)
    # tooth force at the contact point
    tx = sx + sr + 6
    svg += arrow(tx, sy - 30, tx, sy + 2, INK, 2.2)
    svg += text(tx - 6, sy - 34, "F", 12, INK, "end")
    # radii
    svg += dashed(sx, sy, sx - sr, sy)
    svg += text(sx - sr / 2, sy - 6, "r", 11, INK2)
    svg += dashed(lx, ly, lx + lr, ly)
    svg += text(lx + lr / 2, ly - 6, "2r", 11, INK2)
    # notes
    svg += text(470, 22, "F: the force between the teeth, the same on both", 11, INK2, "start")
    svg += text(470, 42, "moment on A = F × r", 12, INK, "start")
    svg += text(470, 62, "moment on B = F × 2r — twice as big", 12, INK, "start")
    svg += text(470, 90, "B turns half as many times as A", 11, INK2, "start")
    svg += text(470, 105, "(turns ratio = teeth ratio = 10 : 20)", 11, INK2, "start")
    svg += text(470, 130, "B turns the opposite way to A", 11, INK2, "start")
    svg += text(470, 160, "small driving large: more moment,", 11, INK2, "start")
    svg += text(470, 175, "slower — a force multiplier", 11, INK2, "start")
    svg += text(470, 195, "large driving small: less moment,", 11, INK2, "start")
    svg += text(470, 210, "faster — a speed multiplier", 11, INK2, "start")
    return svg


def winch_svg():
    """The hand winch of the June 2025 question, as modelled here: a handle
    (bar) on the axle of small gear Y, which drives large gear X; X is fixed
    to the drum; the rope round the drum lifts the load."""
    svg = ""
    xx, xy, xr = 250, 120, 75
    yx, yy, yr = xx + xr + 25 + 8, 120, 25
    dr = 25
    svg += gear(xx, xy, xr, 24)
    svg += gear(yx, yy, yr, 8)
    # drum on X's axle (drawn as an inner circle)
    svg += "<circle cx='%s' cy='%s' r='%s' style='fill:var(--accent);opacity:0.18;stroke:%s;stroke-width:1.4'/>" % (xx, xy, dr, INK2)
    svg += text(xx, xy - 4, "drum", 11, INK)
    svg += text(xx, xy + 10, "r = 0.05 m", 10, INK2)
    svg += text(xx, xy - xr - 22, "gear X: 24 teeth, radius 0.15 m", 11, INK)
    svg += text(yx + 20, yy + yr + 30, "gear Y: 8 teeth, radius 0.05 m", 11, INK)
    # handle: bar from Y's centre out to the right-down with a knob
    hx = yx + 150 * cos(radians(-35))
    hy = yy + 150 * sin(radians(-35))
    svg += "<line x1='%s' y1='%s' x2='%.1f' y2='%.1f' style='stroke:%s;stroke-width:6;stroke-linecap:round'/>" % (yx, yy, hx, hy, INK2)
    svg += dot(hx, hy, 6, INK2)
    svg += text(hx + 12, hy - 2, "handle (bar), length 0.30 m", 11, INK, "start")
    # effort at the knob, perpendicular to the bar
    ex = hx + 55 * cos(radians(55))
    ey = hy + 55 * sin(radians(55))
    svg += arrow(hx, hy, ex, ey, ACCENT, 3)
    svg += text(ex + 6, ey + 8, "effort E", 12, ACCENT, "start")
    # rope from the drum down to the load
    rope_x = xx - dr
    svg += solid(rope_x, xy, rope_x, 250, INK, 2)
    svg += box(rope_x - 28, 250, 56, 36, "var(--accent)", 0.3)
    svg += text(rope_x, 273, "load", 11, INK)
    svg += arrow(rope_x, 286, rope_x, 330, ACCENT, 3)
    svg += text(rope_x + 10, 320, "W = 600 N", 12, ACCENT, "start")
    # turning sense
    svg += text(yx + 20, yy + yr + 46, "Y turns 3 times for each turn of X", 11, INK2)
    svg += arc(xx, xy, xr + 16, 100, 250, INK2)
    svg += text(xx - xr - 24, xy + 4, "X and the drum", 11, INK2, "end")
    svg += text(xx - xr - 24, xy + 18, "turn together", 11, INK2, "end")
    svg += text(300, 350, "one turn of the handle: the effort moves 2π × 0.30 m; the drum turns ⅓ of a turn and the load rises ⅓ × 2π × 0.05 m", 10.5, INK2)
    return svg
