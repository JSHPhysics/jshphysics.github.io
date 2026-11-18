"""
se_diagrams.py — the diagrams for Topic 11 (Static electricity) as inline
SVG, drawn with the helpers in le_diagrams.py and fe_diagrams.py.

    rubbing_svg()     a polythene rod rubbed with a cloth: electrons move to the rod
    forces_svg()      like charges repel, unlike attract (two hanging balls)
    induction_svg()   a charged comb above a scrap of paper: the near side is induced
    earthing_svg()    a negative and a positive object earthed: which way the electrons go
    sprayer_svg()     a paint sprayer: charged droplets spreading, the earthed car
    fuelling_svg()    refuelling with a bonding line and an earth
    fields_svg()      the field of a point charge and the field between parallel plates
"""

from math import cos, radians, sin

from le_diagrams import ACCENT, INK, INK2, LINE, dashed, solid, text
from fe_diagrams import arrow, box, dot


def sign(x, y, plus, size=9, colour=INK):
    """A + or − sign centred on (x, y)."""
    svg = solid(x - size / 2, y, x + size / 2, y, colour, 1.8)
    if plus:
        svg += solid(x, y - size / 2, x, y + size / 2, colour, 1.8)
    return svg


def charges(points, plus, colour=INK):
    svg = ""
    for x, y in points:
        svg += sign(x, y, plus, 7, colour)
    return svg


# ---------------------------------------------------------------------

def rubbing_svg():
    svg = ""
    # before (left): neutral rod and cloth
    svg += text(150, 28, "before rubbing", 12, INK)
    svg += box(50, 60, 200, 26, "var(--line)", 0.2)
    svg += text(150, 50, "polythene rod: equal + and −", 11, INK2)
    svg += charges([(70, 70), (110, 70), (150, 70), (190, 70), (230, 70)], True)
    svg += charges([(90, 78), (130, 78), (170, 78), (210, 78), (240, 78)], False)
    svg += "<path d='M 60 140 Q 150 115 240 140 L 240 170 Q 150 145 60 170 Z' style='fill:var(--accent);opacity:0.18;stroke:var(--ink-2);stroke-width:1.2'/>"
    svg += text(150, 195, "cloth: equal + and −", 11, INK2)
    svg += charges([(90, 150), (150, 142), (210, 150)], True)
    svg += charges([(120, 152), (180, 148), (150, 158)], False)
    # arrow
    svg += arrow(290, 120, 350, 120, INK2, 2.5)
    svg += text(320, 108, "rub", 11, INK2)
    # after (right)
    svg += text(500, 28, "after rubbing", 12, INK)
    svg += box(400, 60, 200, 26, "var(--line)", 0.2)
    svg += text(500, 50, "rod gained electrons: negative", 11, INK2)
    svg += charges([(420, 70), (460, 70), (500, 70), (540, 70), (580, 70)], True)
    svg += charges([(440, 78), (480, 78), (520, 78), (560, 78), (590, 78), (430, 68), (510, 66)], False)
    svg += "<path d='M 410 140 Q 500 115 590 140 L 590 170 Q 500 145 410 170 Z' style='fill:var(--accent);opacity:0.18;stroke:var(--ink-2);stroke-width:1.2'/>"
    svg += text(500, 195, "cloth lost electrons: positive (same size)", 11, INK2)
    svg += charges([(440, 150), (500, 142), (560, 150)], True)
    svg += charges([(500, 158)], False)
    # electrons moving from cloth to rod
    svg += arrow(470, 135, 470, 92, ACCENT, 2.2)
    svg += arrow(530, 135, 530, 92, ACCENT, 2.2)
    svg += text(620, 115, "electrons", 11, ACCENT, "start")
    svg += text(620, 129, "move from", 11, ACCENT, "start")
    svg += text(620, 143, "cloth to rod", 11, ACCENT, "start")
    svg += text(350, 230, "Only electrons move. Protons stay in their nuclei. Charge is not made: what the rod gains, the cloth loses.", 11, INK2)
    return svg


def forces_svg():
    svg = ""
    for index, (title, left_plus, right_plus, repel) in enumerate((("like charges repel", False, False, True), ("unlike charges attract", False, True, False))):
        ox = 160 + index * 330
        svg += text(ox, 28, title, 12, INK)
        # two threads from a bar
        svg += solid(ox - 90, 45, ox + 90, 45, INK2, 3)
        tilt = 28 if repel else -12
        for side in (-1, 1):
            top_x = ox + side * (40 if repel else 60)
            ball_x = top_x + side * tilt
            ball_y = 150
            svg += solid(top_x, 45, ball_x, ball_y - 16, INK2, 1.2)
            plus = left_plus if side < 0 else right_plus
            svg += "<circle cx='%s' cy='%s' r='16' style='fill:var(--bg);stroke:var(--ink);stroke-width:1.6'/>" % (ball_x, ball_y)
            svg += sign(ball_x, ball_y, plus, 10)
            # force arrow
            direction = side if repel else -side
            length = 42 if repel else 22
            svg += arrow(ball_x + direction * 20, ball_y, ball_x + direction * (20 + length), ball_y, ACCENT, 2.5)
        svg += text(ox, 200, "force on each ball shown; equal and opposite", 11, INK2)
    svg += text(325, 230, "Each ball feels a force — so each accelerates in the direction of the force. The forces are an interaction pair.", 11, INK2)
    return svg


def induction_svg():
    svg = ""
    # comb
    svg += box(120, 30, 220, 22, "var(--line)", 0.25)
    for i in range(12):
        svg += solid(130 + i * 18, 52, 130 + i * 18, 70, INK2, 2)
    svg += charges([(150, 41), (190, 41), (230, 41), (270, 41), (310, 41)], False)
    svg += text(360, 45, "negatively charged comb", 11, INK, "start")
    # paper
    svg += box(170, 120, 120, 50, "var(--bg)", 1)
    svg += text(230, 190, "scrap of paper: neutral overall", 11, INK2)
    svg += charges([(190, 130), (230, 130), (270, 130)], True)
    svg += charges([(190, 160), (230, 160), (270, 160)], False)
    svg += arrow(230, 148, 230, 157, INK2, 1.6)
    svg += text(300, 134, "near side: electrons pushed away, left positive", 11, INK2, "start")
    svg += text(300, 164, "far side: electrons gather, negative", 11, INK2, "start")
    # forces
    svg += arrow(150, 120, 150, 92, ACCENT, 2.5)
    svg += text(140, 100, "attraction (near, +)", 11, ACCENT, "end")
    svg += arrow(150, 172, 150, 186, INK2, 1.6)
    svg += text(140, 184, "repulsion (far, −): weaker", 11, INK2, "end")
    svg += text(330, 225, "The attraction is on the nearer charges, so it is the larger force: the paper is pulled up. A neutral object is always attracted, never repelled.", 10.5, INK2)
    return svg


def earthing_svg():
    svg = ""
    for index, (title, plus) in enumerate((("negatively charged object", False), ("positively charged object", True))):
        ox = 170 + index * 330
        svg += text(ox, 28, title, 12, INK)
        svg += "<rect x='%s' y='50' width='120' height='60' rx='8' style='fill:var(--line);opacity:0.2;stroke:var(--ink);stroke-width:1.6'/>" % (ox - 60)
        svg += charges([(ox - 35, 70), (ox, 70), (ox + 35, 70), (ox - 18, 92), (ox + 18, 92)], plus)
        # wire to earth
        svg += solid(ox, 110, ox, 170, INK, 2)
        svg += solid(ox - 24, 170, ox + 24, 170, INK, 2)
        svg += solid(ox - 15, 178, ox + 15, 178, INK, 2)
        svg += solid(ox - 6, 186, ox + 6, 186, INK, 2)
        svg += text(ox + 34, 180, "earth", 11, INK2, "start")
        # electron flow
        if plus:
            svg += arrow(ox + 12, 165, ox + 12, 118, ACCENT, 2.2)
            svg += text(ox + 20, 145, "electrons flow up from earth", 11, ACCENT, "start")
        else:
            svg += arrow(ox + 12, 118, ox + 12, 165, ACCENT, 2.2)
            svg += text(ox + 20, 145, "electrons flow down to earth", 11, ACCENT, "start")
        svg += text(ox, 215, "object left neutral" if True else "", 11, INK2)
    svg += text(335, 240, "Earthing: a conducting path lets electrons move until the excess charge is gone. It is always electrons that move, either way.", 10.5, INK2)
    return svg


def sprayer_svg():
    svg = ""
    # nozzle
    svg += box(40, 110, 70, 30, "var(--line)", 0.3)
    svg += text(75, 160, "nozzle at a high", 11, INK2)
    svg += text(75, 174, "negative pd", 11, INK2)
    # droplets spreading in a cone
    import random
    random.seed(4)
    for i in range(26):
        t = 0.15 + 0.85 * (i / 26)
        spread = 60 * t
        x = 115 + 300 * t
        y = 125 + random.uniform(-spread, spread)
        svg += "<circle cx='%.1f' cy='%.1f' r='3' style='fill:var(--accent)'/>" % (x, y)
        svg += solid(x - 2, y, x + 2, y, "var(--bg)", 1)
    svg += text(260, 50, "charged droplets repel one another → spread into a fine, even mist", 11, INK2)
    # car panel
    svg += "<path d='M 440 60 Q 480 40 520 60 L 540 190 L 430 190 Z' style='fill:var(--line);opacity:0.25;stroke:var(--ink);stroke-width:1.6'/>"
    svg += text(485, 215, "car body, earthed", 11, INK2)
    svg += charges([(470, 100), (500, 90), (480, 140), (510, 150), (460, 170)], True)
    svg += solid(485, 190, 485, 235, INK, 1.6) + solid(465, 235, 505, 235, INK, 1.6) + solid(473, 242, 497, 242, INK, 1.6)
    svg += arrow(400, 125, 435, 115, ACCENT, 2.2)
    svg += text(580, 100, "the droplets are attracted", 11, INK, "start")
    svg += text(580, 116, "to the oppositely charged", 11, INK, "start")
    svg += text(580, 132, "(induced) surface, even round", 11, INK, "start")
    svg += text(580, 148, "the back: an even coat,", 11, INK, "start")
    svg += text(580, 164, "less paint wasted", 11, INK, "start")
    return svg


def fuelling_svg():
    svg = ""
    # tanker
    svg += "<rect x='40' y='80' width='200' height='70' rx='20' style='fill:var(--line);opacity:0.25;stroke:var(--ink);stroke-width:1.6'/>"
    svg += text(140, 120, "fuel tanker", 12, INK)
    # aircraft wing / tank
    svg += "<path d='M 420 70 L 640 90 L 640 150 L 420 160 Z' style='fill:var(--line);opacity:0.25;stroke:var(--ink);stroke-width:1.6'/>"
    svg += text(530, 120, "aircraft fuel tank", 12, INK)
    # hose
    svg += "<path d='M 240 115 Q 330 60 420 110' style='fill:none;stroke:var(--accent);stroke-width:7'/>"
    svg += text(330, 50, "fuel rushing through the hose: friction → charge builds up", 11, INK2)
    # bonding line
    svg += dashed(240, 140, 420, 145, INK)
    svg += text(330, 165, "bonding line: a conductor joining tanker and aircraft", 11, INK)
    svg += text(330, 179, "so they stay at the same potential — no spark between them", 11, INK2)
    # earth
    svg += solid(140, 150, 140, 215, INK, 1.6) + solid(120, 215, 160, 215, INK, 1.6) + solid(128, 222, 152, 222, INK, 1.6)
    svg += text(170, 212, "earth wire: charge flows away to the ground", 11, INK2, "start")
    return svg


def fields_svg():
    svg = ""
    # point charge (left)
    cx, cy = 150, 130
    svg += text(cx, 25, "field around a point charge", 12, INK)
    for k in range(8):
        a = radians(k * 45)
        x1 = cx + 18 * cos(a)
        y1 = cy + 18 * sin(a)
        x2 = cx + 85 * cos(a)
        y2 = cy + 85 * sin(a)
        svg += arrow(x1, y1, x2, y2, INK, 1.6)
    svg += "<circle cx='%s' cy='%s' r='14' style='fill:var(--bg);stroke:var(--ink);stroke-width:1.6'/>" % (cx, cy)
    svg += sign(cx, cy, True, 10)
    svg += text(cx, 240, "radial; arrows away from +, towards −;", 11, INK2)
    svg += text(cx, 254, "lines spread out: the field weakens with distance", 11, INK2)
    # parallel plates (right)
    px = 420
    svg += text(px + 90, 25, "field between parallel plates", 12, INK)
    svg += box(px, 50, 180, 10, "var(--ink)", 0.9)
    svg += box(px, 200, 180, 10, "var(--ink)", 0.9)
    svg += charges([(px + 20 + i * 35, 44) for i in range(5)], True, INK)
    svg += charges([(px + 20 + i * 35, 222) for i in range(5)], False, INK)
    for i in range(6):
        x = px + 15 + i * 30
        svg += arrow(x, 62, x, 196, INK, 1.6)
    svg += text(px + 90, 240, "uniform: parallel, equally spaced, straight,", 11, INK2)
    svg += text(px + 90, 254, "from + plate to − plate; the same strength everywhere", 11, INK2)
    return svg
