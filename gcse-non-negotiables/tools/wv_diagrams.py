"""
wv_diagrams.py — the two wave diagrams for Topic 4, as inline SVG.
Same helpers and colours as le_diagrams.py.
"""

from math import cos, pi, sin

from le_diagrams import INK, INK2, LINE, ACCENT, dashed, ray, solid, text


def transverse_svg():
    """A transverse wave (displacement against distance) with amplitude,
    wavelength, crest and trough labelled."""
    left, right, mid = 40, 440, 150
    amp = 60
    wavelength = 160
    svg = solid(left, mid, right + 20, mid, LINE, 1)
    svg += ray(left, mid, right + 20, mid, INK2, False)
    svg += text(right + 20, mid + 14, "distance →", 11, INK2, "end")
    svg += "<text x='%s' y='%s' font-size='11' style='fill:%s' transform='rotate(-90 %s %s)' text-anchor='middle'>displacement</text>" % (left - 24, mid, INK2, left - 24, mid)
    points = []
    steps = 200
    for index in range(steps + 1):
        x = left + (right - left) * index / steps
        y = mid - amp * sin(2 * pi * (x - left) / wavelength)
        points.append("%.1f,%.1f" % (x, y))
    svg += "<polyline points='%s' style='fill:none;stroke:%s;stroke-width:2.5'/>" % (" ".join(points), ACCENT)
    crest_x = left + wavelength / 4
    trough_x = left + 3 * wavelength / 4
    next_crest = crest_x + wavelength
    # amplitude
    svg += dashed(crest_x, mid, crest_x, mid - amp, INK)
    svg += text(crest_x + 8, mid - amp / 2 + 4, "amplitude", 12, INK, "start")
    svg += text(crest_x - 30, mid - amp + 4, "crest", 11, INK2)
    svg += text(trough_x, mid + amp + 18, "trough", 11, INK2)
    # wavelength crest to crest
    svg += dashed(crest_x, mid - amp - 22, crest_x, mid - amp - 4, INK2)
    svg += dashed(next_crest, mid - amp - 22, next_crest, mid - amp - 4, INK2)
    svg += ray(crest_x, mid - amp - 18, next_crest, mid - amp - 18, INK, False)
    svg += text((crest_x + next_crest) / 2, mid - amp - 26, "wavelength λ (crest to crest)", 12, INK)
    # wavelength trough to trough too
    svg += ray(trough_x, mid + amp + 30, trough_x + wavelength, mid + amp + 30, INK2, False)
    svg += text(trough_x + wavelength / 2, mid + amp + 44, "also λ: trough to trough, or any point to the same point on the next wave", 10, INK2)
    svg += text(240, 22, "A transverse wave: the oscillations are at right angles to the direction the wave travels", 12, INK)
    return svg


def longitudinal_svg():
    """A longitudinal wave on a slinky: coils bunched (compressions) and
    spread (rarefactions), with the direction of travel and of oscillation."""
    left, right, mid = 40, 440, 110
    wavelength = 160
    svg = ""
    # coils: vertical lines whose spacing varies sinusoidally
    count = 60
    for index in range(count):
        base = left + (right - left) * index / (count - 1)
        shift = 10 * sin(2 * pi * (base - left) / wavelength)
        x = base + shift
        svg += solid(x, mid - 22, x, mid + 22, ACCENT, 1.6)
    comp1 = left + wavelength / 2
    rare1 = left + wavelength
    svg += text(comp1, mid - 34, "compression", 11, INK)
    svg += text(comp1 + wavelength, mid - 34, "compression", 11, INK)
    svg += text(rare1, mid + 44, "rarefaction", 11, INK)
    svg += text(rare1 + wavelength, mid + 44, "rarefaction", 11, INK)
    # wavelength between compressions
    svg += ray(comp1, mid - 52, comp1 + wavelength, mid - 52, INK, False)
    svg += text(comp1 + wavelength / 2, mid - 58, "wavelength λ (compression to compression)", 11, INK)
    # direction of travel and oscillation
    svg += ray(left, mid + 70, right, mid + 70, INK2)
    svg += text(240, mid + 88, "direction of energy transfer →", 11, INK2)
    svg += ray(200, mid + 100, 280, mid + 100, INK)
    svg += ray(280, mid + 110, 200, mid + 110, INK)
    svg += text(240, mid + 128, "the coils oscillate back and forth along the same line", 11, INK)
    svg += text(240, 18, "A longitudinal wave: the oscillations are parallel to the direction the wave travels", 12, INK)
    return svg
