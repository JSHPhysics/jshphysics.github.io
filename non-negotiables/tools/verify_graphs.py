#!/usr/bin/env python3
"""Independent check of the graph-reading types in data/*.json.

For each of the 15 "-graph" types this script

  1. recomputes the answer to the worked example and to practice questions
     p2, p4 and p6 from the graph coordinates (series points, tangent end
     points, marks, shaded-region bounds) and the standard constants, the
     way a student reading the graph would, and compares with answer.value
     (match = within 2 %);
  2. for all seven questions, checks that every mark and every tangent end
     point sits on a major gridline intersection;
  3. checks that a question whose graph has a tangent or a shade says so;
  4. checks that letters named in the question text exist as marks, and
     that every mark lies on one of the plotted series;
  5. checks that all plotted points lie inside the axis ranges.

It reads data/ only; it never writes to it.

Run:  python3 tools/verify_graphs.py
"""

import json
import math
import os
import re
import sys

# --------------------------------------------------------------------------
# Standard constants (SCHEMA.md, "Standard constants")
# --------------------------------------------------------------------------
G = 6.67e-11
h_planck = 6.63e-34
e_charge = 1.60e-19
k_boltz = 1.38e-23
R_gas = 8.31
c_light = 3.00e8
WIEN = 2.90e-3

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, 'data')

# The practice questions that get a full recomputation
RECOMPUTE_TAGS = ['w', 'p2', 'p4', 'p6']


# --------------------------------------------------------------------------
# Small helpers for reading a graph object
# --------------------------------------------------------------------------

def series(graph, index):
    """Return the series at the given index."""
    return graph['series'][index]


def points(graph, index):
    """Return the point list of a series."""
    return series(graph, index)['points']


def first_point(graph, index):
    """First point of a series."""
    return points(graph, index)[0]


def last_point(graph, index):
    """Last point of a series."""
    return points(graph, index)[-1]


def mark(graph, label):
    """Return (x, y) of the mark with the given label."""
    for m in graph.get('marks', []):
        if m.get('label') == label:
            return (m['x'], m['y'])
    raise KeyError('no mark labelled %r' % label)


def gradient_between(p1, p2):
    """Gradient of the straight line through two points."""
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    return dy / dx


def gradient_of_series(graph, index):
    """Gradient from the first to the last point of a straight series."""
    p1 = first_point(graph, index)
    p2 = last_point(graph, index)
    return gradient_between(p1, p2)


def gradient_of_fit(graph, index):
    """Gradient of the best-fit line attached to a data series."""
    fit = series(graph, index)['fit']
    return gradient_between(fit[0], fit[1])


def value_on_line(graph, index, x):
    """y on a straight (segmented) series at the given x, by interpolation."""
    pts = points(graph, index)
    for i in range(len(pts) - 1):
        xa, ya = pts[i]
        xb, yb = pts[i + 1]
        lo = min(xa, xb)
        hi = max(xa, xb)
        if lo - 1e-9 <= x <= hi + 1e-9:
            if xb == xa:
                return ya
            fraction = (x - xa) / (xb - xa)
            return ya + fraction * (yb - ya)
    raise ValueError('x = %r is outside the series' % x)


def trapezium_area(graph, index, x_from, x_to, baseline=0.0):
    """Area under a straight (segmented) series between two x values.

    Exactly what a student does with geometry: split at the vertices and
    sum the trapezia.
    """
    pts = points(graph, index)
    # Collect every x at which the line changes direction inside the range
    xs = [x_from, x_to]
    for p in pts:
        if x_from < p[0] < x_to:
            xs.append(p[0])
    xs = sorted(set(xs))
    total = 0.0
    for i in range(len(xs) - 1):
        xa = xs[i]
        xb = xs[i + 1]
        ya = value_on_line(graph, index, xa) - baseline
        yb = value_on_line(graph, index, xb) - baseline
        total = total + 0.5 * (ya + yb) * (xb - xa)
    return total


def shade_bounds(graph, index=0):
    """(from, to) of the first shaded region."""
    s = graph['shade'][index]
    return (s['from'], s['to'])


def tangent_index(graph):
    """Index of the tangent series."""
    for i, s in enumerate(graph['series']):
        if s['kind'] == 'tangent':
            return i
    raise KeyError('no tangent series')


def tangent_gradient(graph):
    """Gradient of the tangent from its two end points."""
    return gradient_of_series(graph, tangent_index(graph))


def x_intercept_of_series(graph, index):
    """x where a straight series (extended) meets y = 0."""
    p1 = first_point(graph, index)
    p2 = last_point(graph, index)
    m = gradient_between(p1, p2)
    # y = y1 + m (x - x1) = 0  ->  x = x1 - y1 / m
    return p1[0] - p1[1] / m


def y_intercept_of_series(graph, index):
    """y where a straight series (extended) meets x = 0."""
    p1 = first_point(graph, index)
    p2 = last_point(graph, index)
    m = gradient_between(p1, p2)
    return p1[1] - m * p1[0]


# --------------------------------------------------------------------------
# Per-question recomputation.  Each entry is a function of (graph, question
# text) returning (my_value, reasoning).  Keyed by question id.
# --------------------------------------------------------------------------

def astro_w(g, q):
    # H0 = gradient of best-fit line; y in 10^3 km/s, x in Mpc
    m = gradient_of_fit(g, 0)
    H0 = m * 1e3
    return H0, 'gradient of fit = %.4g (10^3 km/s)/Mpc -> H0 = %.4g km/s/Mpc' % (m, H0)


def astro_p2(g, q):
    lab = first_point(g, 0)[0]
    obs = first_point(g, 1)[0]
    z = (obs - lab) / lab
    return z, 'z = (%g - %g)/%g = %.4g' % (obs, lab, lab, z)


def astro_p4(g, q):
    # I = (L/4pi) * (1/d^2): gradient = L/4pi; x in 1e-23 m^-2
    m = gradient_of_fit(g, 0) / 1e-23
    L = 4 * math.pi * m
    return L, 'gradient = %.4g W m^-2 / m^-2 = L/4pi -> L = %.4g W' % (m, L)


def astro_p6(g, q):
    m = gradient_of_fit(g, 0)
    H0_kms_Mpc = m * 1e3
    H0_si = H0_kms_Mpc * 1e3 / 3.09e22
    age_s = 1 / H0_si
    age_yr = age_s / 3.16e7
    return age_yr, 'H0 = %.4g km/s/Mpc = %.4g s^-1 -> age = 1/H0 = %.4g s = %.4g yr' % (
        H0_kms_Mpc, H0_si, age_s, age_yr)


def shm_w(g, q):
    # Peaks P and Q give the period; amplitude from the peak height (cm)
    P = mark(g, 'P')
    Q = mark(g, 'Q')
    T = Q[0] - P[0]
    A = P[1] / 100.0
    vmax = 2 * math.pi * A / T
    return vmax, 'T = %g - %g = %g s, A = %g cm -> v_max = 2piA/T = %.4g m/s' % (Q[0], P[0], T, P[1], vmax)


def shm_p2(g, q):
    A = mark(g, 'A')
    B = mark(g, 'B')
    T_ms = B[0] - A[0]
    f = 1 / (T_ms * 1e-3)
    return f, 'T = %g ms -> f = %.4g Hz' % (T_ms, f)


def shm_p4(g, q):
    m = tangent_gradient(g)
    return m, 'tangent gradient = %.4g m/s = v_max' % m


def shm_p6(g, q):
    m = gradient_of_series(g, 0)
    omega = math.sqrt(-m)
    T = 2 * math.pi / omega
    return T, 'gradient = %.4g s^-2 = -omega^2 -> omega = %.4g -> T = %.4g s' % (m, omega, T)


def fc_w(g, q):
    # tangent gradient in V/cm -> V/m
    m = tangent_gradient(g)
    E = abs(m) * 100
    return E, 'tangent gradient = %.4g V/cm -> E = %.4g V/m' % (m, E)


def fc_p2(g, q):
    a, b = shade_bounds(g)
    area = trapezium_area(g, 0, a, b)  # uC * V
    W = area * 1e-6
    return W, 'area = 1/2 x %g uC x %g V = %.4g uJ = %.4g J' % (b, value_on_line(g, 0, b), area, W)


def fc_p4(g, q):
    X = mark(g, 'X')
    return X[0], 'X at t = %g s where V = %g V = 0.37 V0 -> time constant %g s' % (X[0], X[1], X[0])


def fc_p6(g, q):
    A = mark(g, 'A')
    B = mark(g, 'B')
    m = gradient_between(A, B)
    RC = -1 / m
    C = 1000e-6
    R_kohm = RC / C / 1e3
    return R_kohm, 'gradient = %.4g s^-1 = -1/RC -> RC = %.4g s -> R = %.4g kOhm' % (m, RC, R_kohm)


def iv_w(g, q):
    X = mark(g, 'X')
    R = X[0] / X[1]
    return R, 'R = V/I = %g/%g = %.4g Ohm' % (X[0], X[1], R)


def iv_p2(g, q):
    X = mark(g, 'X')
    R = X[0] / X[1]
    return R, 'R = V/I = %g/%g = %.4g Ohm' % (X[0], X[1], R)


def iv_p4(g, q):
    A = mark(g, 'A')
    B = mark(g, 'B')
    r = -gradient_between(A, B)
    return r, 'r = -gradient = -(%g - %g)/(%g - %g) = %.4g Ohm' % (B[1], A[1], B[0], A[0], r)


def iv_p6(g, q):
    X = mark(g, 'X')
    return X[1], 'I at X = %g mA' % X[1]


def force_w(g, q):
    m = gradient_of_series(g, 0)
    return m, 'gradient W/m = %.4g N/kg' % m


def force_p2(g, q):
    v = first_point(g, 1)[1]
    return v, 'dashed asymptote at v = %g m/s' % v


def force_p4(g, q):
    m = tangent_gradient(g)
    return m, 'tangent gradient = %.4g m/s^2' % m


def force_p6(g, q):
    P = mark(g, 'P')
    X = mark(g, 'X')
    m = gradient_between(P, X)
    mass = 1 / m
    return mass, 'gradient = %g/%g = %.4g (m/s^2)/N = 1/m -> m = %.4g kg' % (X[1], X[0] - P[0], m, mass)


def grav_w(g, q):
    X = mark(g, 'X')
    return X[1], 'r = 4e6 + 4e6 = 8e6 m; X at (%g, %g) -> g = %g N/kg' % (X[0], X[1], X[1])


def grav_p2(g, q):
    squares = 7.5
    sq = g['x']['step'] * 1e6 * g['y']['step']
    dV = squares * sq
    return dV, '1 large square = %g x 1e6 m x %g N/kg = %.4g J/kg; 7.5 squares = %.4g J/kg' % (
        g['x']['step'], g['y']['step'], sq, dV)


def grav_p4(g, q):
    A = mark(g, 'A')
    B = mark(g, 'B')
    dV = (B[1] - A[1]) * 1e6
    W = 500 * dV
    return W, 'dV = (%g - (%g)) x 1e6 = %.4g J/kg; W = 500 x dV = %.4g J' % (B[1], A[1], dV, W)


def grav_p6(g, q):
    m = gradient_of_fit(g, 0) * 1e7 / 1e21  # s^2 / m^3
    M = 4 * math.pi ** 2 / (G * m)
    return M, 'gradient = %.4g s^2 m^-3 = 4pi^2/GM -> M = %.4g kg' % (m, M)


def motion_w(g, q):
    A = mark(g, 'A')
    B = mark(g, 'B')
    a = gradient_between(A, B)
    return a, 'a = (%g - %g)/(%g - %g) = %.4g m/s^2' % (B[1], A[1], B[0], A[0], a)


def motion_p2(g, q):
    A = mark(g, 'A')
    B = mark(g, 'B')
    a = abs(gradient_between(A, B))
    return a, '|a| = %g/%g = %.4g m/s^2' % (A[1] - B[1], B[0] - A[0], a)


def motion_p4(g, q):
    a, b = shade_bounds(g)
    area = trapezium_area(g, 0, a, b)
    return area, 'trapezium 1/2(%g + %g) x %g = %.4g m' % (value_on_line(g, 0, a), value_on_line(g, 0, b), b - a, area)


def motion_p6(g, q):
    m = tangent_gradient(g)
    return m, 'tangent gradient = %.4g m/s' % m


def flux_w(g, q):
    A = mark(g, 'A')
    emf = A[1] / A[0]
    return emf, 'emf = %g Wb turns / %g s = %.4g V' % (A[1], A[0], emf)


def flux_p2(g, q):
    a, b = shade_bounds(g)
    area = trapezium_area(g, 0, a, b)  # V ms
    return area * 1e-3, 'area = %.4g V ms = %.4g Wb turns' % (area, area * 1e-3)


def flux_p4(g, q):
    P = mark(g, 'P')
    Q = mark(g, 'Q')
    T_ms = Q[0] - P[0]
    f = 1 / (T_ms * 1e-3)
    return f, 'T = %g ms -> f = %.4g Hz' % (T_ms, f)


def flux_p6(g, q):
    X = mark(g, 'X')
    vrms = X[1] / math.sqrt(2)
    return vrms, 'V0 = %g V -> Vrms = %.4g V' % (X[1], vrms)


def mat_w(g, q):
    X = mark(g, 'X')
    k = X[1] / (X[0] * 1e-3)
    return k, 'k = %g N / %g mm = %.4g N/m' % (X[1], X[0], k)


def mat_p2(g, q):
    B = mark(g, 'B')
    return B[1] * 1e6, 'breaking stress at B = %g MPa = %.4g Pa' % (B[1], B[1] * 1e6)


def mat_p4(g, q):
    P = mark(g, 'P')
    u = 0.5 * (P[0] * 1e-3) * (P[1] * 1e8)
    return u, '1/2 x %g e-3 x %g e8 = %.4g J/m^3' % (P[0], P[1], u)


def mat_p6(g, q):
    a, b = shade_bounds(g)
    area = trapezium_area(g, 0, a, b)  # kN cm
    W = area * 1e3 * 1e-2
    return W, 'trapezium 1/2(%g + %g) kN x %g cm = %.4g kN cm = %.4g J' % (
        value_on_line(g, 0, a), value_on_line(g, 0, b), b - a, area, W)


def exp_w(g, q):
    P = mark(g, 'P')
    Q = mark(g, 'Q')
    m = gradient_between(P, Q)
    rho = m * 4.0e-7
    return rho, 'gradient = %.4g Ohm/m = rho/A -> rho = %.4g Ohm m' % (m, rho)


def exp_p2(g, q):
    m = gradient_of_fit(g, 0)
    gval = 4 * math.pi ** 2 / m
    return gval, 'gradient = %.4g s^2/m = 4pi^2/g -> g = %.4g m/s^2' % (m, gval)


def exp_p4(g, q):
    P = mark(g, 'P')
    m = P[1] / P[0]
    k = 4 * math.pi ** 2 / m
    return k, 'gradient via P = %g/%g = %.4g s^2/kg = 4pi^2/k -> k = %.4g N/m' % (P[1], P[0], m, k)


def exp_p6(g, q):
    m = gradient_of_fit(g, 0)  # g/cm^3
    rho = m * 1000
    return rho, 'gradient = %.4g g/cm^3 = %.4g kg/m^3' % (m, rho)


def ft_w(g, q):
    a, b = shade_bounds(g)
    area = trapezium_area(g, 0, a, b)  # N ms
    return area * 1e-3, 'area = %.4g N ms = %.4g N s' % (area, area * 1e-3)


def ft_p2(g, q):
    a, b = shade_bounds(g)
    area = trapezium_area(g, 0, a, b)
    return area, 'trapezium = %.4g J' % area


def ft_p4(g, q):
    X = mark(g, 'X')
    P = X[1] * 1e3 / X[0]
    return P, 'P = %g kJ / %g s = %.4g W' % (X[1], X[0], P)


def ft_p6(g, q):
    a, b = shade_bounds(g)
    W = trapezium_area(g, 0, a, b)
    v = math.sqrt(2 * W / 2.5)
    return v, 'W = %.4g J = 1/2 x 2.5 x v^2 -> v = %.4g m/s' % (W, v)


def decay_w(g, q):
    X = mark(g, 'X')
    A0 = first_point(g, 0)[1]
    return X[0], 'A0 = %g, X at (%g, %g): A halves at t = %g s' % (A0, X[0], X[1], X[0])


def decay_p2(g, q):
    P = mark(g, 'P')
    Q = mark(g, 'Q')
    lam = -gradient_between(P, Q)
    return lam, 'gradient = (%g - %g)/(%g - %g) -> lambda = %.4g s^-1' % (Q[1], P[1], Q[0], P[0], lam)


def decay_p4(g, q):
    P = mark(g, 'P')
    Q = mark(g, 'Q')
    lam_min = -gradient_between(P, Q)
    lam = lam_min / 60
    return lam, 'gradient = %.4g min^-1 -> lambda = %.4g s^-1' % (-lam_min, lam)


def decay_p6(g, q):
    X = mark(g, 'X')
    bg = first_point(g, 1)[1]
    C0 = first_point(g, 0)[1]
    return X[0], 'corrected: %g - %g = %g at t = 0; X: %g - %g = %g (half) at t = %g min' % (
        C0, bg, C0 - bg, X[1], bg, X[1] - bg, X[0])


def pe_w(g, q):
    X = mark(g, 'X')
    return X[0] * 1e14, 'x-intercept X at f = %g x 1e14 Hz' % X[0]


def pe_p2(g, q):
    X = mark(g, 'X')
    return X[1], 'V_s at X = %g V -> KE_max = %g eV' % (X[1], X[1])


def pe_p4(g, q):
    A = mark(g, 'A')
    B = mark(g, 'B')
    m = gradient_between(A, B) / 1e14  # V s
    hval = m * e_charge
    return hval, 'gradient = %.4g V s = h/e -> h = %.4g J s' % (m, hval)


def pe_p6(g, q):
    f0 = x_intercept_of_series(g, 1) * 1e14
    phi_J = h_planck * f0
    phi_eV = phi_J / e_charge
    # alternative a student might use: extrapolate the line to the V axis
    Vint = y_intercept_of_series(g, 1)
    return phi_eV, 'metal B x-intercept f0 = %.4g Hz -> phi = h f0 = %.4g J = %.4g eV (V-axis intercept route gives %.4g eV)' % (
        f0, phi_J, phi_eV, -Vint)


def th_w(g, q):
    A = mark(g, 'A')
    B = mark(g, 'B')
    m = gradient_between(A, B)
    cval = 2000 / (0.80 * m)
    return cval, 'gradient = %.4g K/s; c = P/(m x grad) = %.4g J/kg/K' % (m, cval)


def th_p2(g, q):
    A = mark(g, 'A')
    B = mark(g, 'B')
    dt = B[0] - A[0]
    L = 250 * dt / 0.20
    return L, 'flat section %g s; L = 250 x %g / 0.20 = %.4g J/kg' % (dt, dt, L)


def th_p4(g, q):
    A = mark(g, 'A')
    B = mark(g, 'B')
    m = gradient_between(A, B) * 1e3  # Pa/K
    N = m * 2.0e-3 / k_boltz
    return N, 'gradient = %.4g Pa/K = Nk/V -> N = %.4g' % (m, N)


def th_p6(g, q):
    A = mark(g, 'A')
    B = mark(g, 'B')
    m = gradient_between(A, B) / 60  # K/s
    P = 0.60 * 2000 * m
    return P, 'gradient = %.4g K/min = %.4g K/s -> P = mc x grad = %.4g W' % (m * 60, m, P)


def wave_w(g, q):
    A = mark(g, 'A')
    B = mark(g, 'B')
    T_ms = B[0] - A[0]
    f = 1 / (T_ms * 1e-3)
    return f, 'T = %g ms -> f = %.4g Hz' % (T_ms, f)


def wave_p2(g, q):
    P = mark(g, 'P')
    Q = mark(g, 'Q')
    lam = Q[0] - P[0]
    return lam, 'lambda = %g - %g = %.4g m' % (Q[0], P[0], lam)


def wave_p4(g, q):
    A = mark(g, 'A')
    B = mark(g, 'B')
    T_us = B[0] - A[0]
    f_kHz = 1 / (T_us * 1e-6) / 1e3
    return f_kHz, 'T = %g us -> f = %.4g kHz' % (T_us, f_kHz)


def wave_p6(g, q):
    P = mark(g, 'P')
    Q = mark(g, 'Q')
    # wavelength from the curve: distance between successive zero crossings
    # going the same way; the alt text says 8 m, check from the points
    pts = points(g, 0)
    # find first point after the start where y returns to ~0 from below
    lam = None
    for i in range(2, len(pts)):
        if pts[i - 1][1] < 0 and pts[i][1] >= -1e-9 and pts[i][1] < 1e-3:
            lam = pts[i][0]
            break
    dx = Q[0] - P[0]
    phase = dx / lam * 2 * math.pi
    return phase, 'lambda = %g m (from curve), dx = %g m -> %.4g lambda -> %.4g rad' % (lam, dx, dx / lam, phase)


CALC = {
    'astro-graph-w': astro_w, 'astro-graph-p2': astro_p2, 'astro-graph-p4': astro_p4, 'astro-graph-p6': astro_p6,
    'shm-graph-w': shm_w, 'shm-graph-p2': shm_p2, 'shm-graph-p4': shm_p4, 'shm-graph-p6': shm_p6,
    'field-capacitor-graph-w': fc_w, 'field-capacitor-graph-p2': fc_p2,
    'field-capacitor-graph-p4': fc_p4, 'field-capacitor-graph-p6': fc_p6,
    'iv-graph-w': iv_w, 'iv-graph-p2': iv_p2, 'iv-graph-p4': iv_p4, 'iv-graph-p6': iv_p6,
    'force-graph-w': force_w, 'force-graph-p2': force_p2, 'force-graph-p4': force_p4, 'force-graph-p6': force_p6,
    'gravity-graph-w': grav_w, 'gravity-graph-p2': grav_p2, 'gravity-graph-p4': grav_p4, 'gravity-graph-p6': grav_p6,
    'motion-graph-w': motion_w, 'motion-graph-p2': motion_p2, 'motion-graph-p4': motion_p4, 'motion-graph-p6': motion_p6,
    'flux-emf-graph-w': flux_w, 'flux-emf-graph-p2': flux_p2, 'flux-emf-graph-p4': flux_p4, 'flux-emf-graph-p6': flux_p6,
    'fx-stress-strain-graph-w': mat_w, 'fx-stress-strain-graph-p2': mat_p2,
    'fx-stress-strain-graph-p4': mat_p4, 'fx-stress-strain-graph-p6': mat_p6,
    'experiment-graph-w': exp_w, 'experiment-graph-p2': exp_p2, 'experiment-graph-p4': exp_p4, 'experiment-graph-p6': exp_p6,
    'ft-fs-graph-w': ft_w, 'ft-fs-graph-p2': ft_p2, 'ft-fs-graph-p4': ft_p4, 'ft-fs-graph-p6': ft_p6,
    'decay-graph-w': decay_w, 'decay-graph-p2': decay_p2, 'decay-graph-p4': decay_p4, 'decay-graph-p6': decay_p6,
    'photoelectric-graph-w': pe_w, 'photoelectric-graph-p2': pe_p2,
    'photoelectric-graph-p4': pe_p4, 'photoelectric-graph-p6': pe_p6,
    'thermal-graph-w': th_w, 'thermal-graph-p2': th_p2, 'thermal-graph-p4': th_p4, 'thermal-graph-p6': th_p6,
    'wave-graph-w': wave_w, 'wave-graph-p2': wave_p2, 'wave-graph-p4': wave_p4, 'wave-graph-p6': wave_p6,
}


# --------------------------------------------------------------------------
# Structural checks on every graph
# --------------------------------------------------------------------------

def on_gridline(value, axis):
    """True when value sits on a major gridline of the axis."""
    step = axis['step']
    n = (value - axis['min']) / step
    return abs(n - round(n)) < 1e-6


def gridline_exceptions(graph):
    """List the marks and tangent end points that are off a major gridline."""
    out = []
    for m in graph.get('marks', []):
        ok_x = on_gridline(m['x'], graph['x'])
        ok_y = on_gridline(m['y'], graph['y'])
        if not (ok_x and ok_y):
            out.append('mark %s at (%r, %r)' % (m.get('label', '?'), m['x'], m['y']))
    for i, s in enumerate(graph.get('series', [])):
        if s['kind'] != 'tangent':
            continue
        for p in s['points']:
            ok_x = on_gridline(p[0], graph['x'])
            ok_y = on_gridline(p[1], graph['y'])
            if not (ok_x and ok_y):
                out.append('tangent end at (%r, %r)' % (p[0], p[1]))
    return out


def wording_exceptions(question, graph):
    """Tangent or shade present but not mentioned in the question text."""
    out = []
    text = question.lower()
    has_tangent = any(s['kind'] == 'tangent' for s in graph.get('series', []))
    has_shade = bool(graph.get('shade'))
    if has_tangent and 'tangent' not in text:
        out.append('tangent drawn but not mentioned')
    if has_shade and 'shade' not in text:
        out.append('region shaded but not mentioned')
    return out


# Patterns in which a question names a marked point
LETTER_PATTERNS = [
    r'\bpoints? ([A-Z])\b',
    r'\bmarked ([A-Z])\b',
    r'\bat ([A-Z])\b',
    r'\bthrough ([A-Z])\b',
    r'\bsection ([A-Z])([A-Z])\b',
    r'\bbetween ([A-Z]) and ([A-Z])\b',
    r'\bfrom ([A-Z]) to ([A-Z])\b',
    r'\bfrom point ([A-Z]) to point ([A-Z])\b',
    r'\bup to ([A-Z])\b',
    r'\bpoints ([A-Z]), ([A-Z]), ([A-Z]) and ([A-Z])\b',
    r'\bpoints ([A-Z]) and ([A-Z])\b',
    r'\bpeaks ([A-Z]) and ([A-Z])\b',
    r'\bpeak ([A-Z])\b',
    r'\b([A-Z]) is the point\b',
    r'(?<!where )\b([A-Z]) is its\b',
    r'\b([A-Z]) and ([A-Z]) are\b',
    r'\b([A-Z]) marks\b',
]

# Letters that are physics symbols in these questions, never point labels
SYMBOL_LETTERS = set('VIERFTNQLAW')  # only applied for the generic "at X" pattern


def named_letters(question):
    """Set of single capital letters the question uses as point names."""
    found = set()
    for pat in LETTER_PATTERNS:
        for m in re.finditer(pat, question):
            for grp in m.groups():
                if grp is not None:
                    found.add(grp)
    return found


def mark_consistency(question, graph):
    """Named letters missing from marks, and marks that are off every series."""
    out = []
    labels = set(m.get('label') for m in graph.get('marks', []))
    text_labels = set(l['text'] for l in graph.get('labels', []))
    for letter in sorted(named_letters(question)):
        if letter in labels:
            continue
        # "metal A" / "metal B" style labels are free-text labels
        if any(letter in t.split() for t in text_labels):
            continue
        # a lone physics symbol caught by the loose "at X" pattern
        if letter in SYMBOL_LETTERS and re.search(r'\bat %s\b' % letter, question) and not re.search(r'\b(point|marked) %s\b' % letter, question):
            continue
        out.append('question names %s but no such mark' % letter)
    # every mark should lie on a plotted series (or its best-fit line)
    for m in graph.get('marks', []):
        if mark_on_any_series(graph, m['x'], m['y']):
            continue
        out.append('mark %s at (%r, %r) is not on any plotted series' % (m.get('label', '?'), m['x'], m['y']))
    return out


def mark_on_any_series(graph, x, y):
    """True when (x, y) lies on some series within a small tolerance."""
    y_span = graph['y']['max'] - graph['y']['min']
    tol = 0.01 * y_span
    for s in graph['series']:
        pts = s['points'] if s['kind'] != 'data' else s.get('fit')
        if not pts:
            continue
        for i in range(len(pts) - 1):
            xa, ya = pts[i]
            xb, yb = pts[i + 1]
            lo = min(xa, xb)
            hi = max(xa, xb)
            if lo - 1e-9 <= x <= hi + 1e-9:
                if xb == xa:
                    if min(ya, yb) - tol <= y <= max(ya, yb) + tol:
                        return True
                    continue
                fraction = (x - xa) / (xb - xa)
                y_line = ya + fraction * (yb - ya)
                if abs(y_line - y) <= tol:
                    return True
    return False


def square_count_check(question, graph):
    """For questions that state 'contains N large squares', integrate the
    curve over the shaded range and compare with N.  Returns a message or None.
    """
    m = re.search(r'contains ([0-9.]+) large squares', question)
    if m is None:
        return None
    stated = float(m.group(1))
    sh = graph['shade'][0]
    pts = points(graph, sh['series'])
    # trapezium-rule integral of the plotted curve between the bounds
    area = 0.0
    for i in range(len(pts) - 1):
        xa, ya = pts[i]
        xb, yb = pts[i + 1]
        lo = max(xa, sh['from'])
        hi = min(xb, sh['to'])
        if hi <= lo:
            continue
        # interpolate y at lo and hi
        y_lo = ya + (lo - xa) / (xb - xa) * (yb - ya)
        y_hi = ya + (hi - xa) / (xb - xa) * (yb - ya)
        area = area + 0.5 * (y_lo + y_hi) * (hi - lo)
    square = graph['x']['step'] * graph['y']['step']
    counted = area / square
    if abs(counted - stated) / stated > 0.03:
        return 'question says %g large squares, curve integrates to %.3g' % (stated, counted)
    return None


def range_exceptions(graph):
    """Points outside the axis ranges."""
    out = []
    xa = graph['x']
    ya = graph['y']
    for i, s in enumerate(graph.get('series', [])):
        pts = list(s['points'])
        if s.get('fit'):
            pts = pts + list(s['fit'])
        for p in pts:
            if p[0] < xa['min'] - 1e-9 or p[0] > xa['max'] + 1e-9 or p[1] < ya['min'] - 1e-9 or p[1] > ya['max'] + 1e-9:
                out.append('series %d point (%r, %r) outside axes' % (i, p[0], p[1]))
    return out


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main():
    files = sorted(f for f in os.listdir(DATA) if f.endswith('.json') and f != 'manifest.json')
    checked = 0
    matched = 0
    mismatched = []
    grid_issues = []
    word_issues = []
    mark_issues = []
    range_issues = []
    graphs_seen = 0

    for fname in files:
        with open(os.path.join(DATA, fname)) as fh:
            topic = json.load(fh)
        t = topic['types'][-1]
        if not t['id'].endswith('-graph'):
            print('!! last type of %s is %s, not a graph type' % (fname, t['id']))
            continue
        print('=' * 90)
        print(topic['id'], '/', t['id'])
        questions = [('w', t['worked'])] + [('p%d' % (i + 1), q) for i, q in enumerate(t['practice'])]
        for tag, q in questions:
            g = q.get('graph')
            if g is None:
                print('  %-34s NO GRAPH' % q['id'])
                continue
            graphs_seen = graphs_seen + 1
            # structural checks on every graph
            for issue in gridline_exceptions(g):
                grid_issues.append('%s: %s' % (q['id'], issue))
            for issue in wording_exceptions(q['question'], g):
                word_issues.append('%s: %s' % (q['id'], issue))
            for issue in mark_consistency(q['question'], g):
                mark_issues.append('%s: %s' % (q['id'], issue))
            for issue in range_exceptions(g):
                range_issues.append('%s: %s' % (q['id'], issue))
            sq = square_count_check(q['question'], g)
            if sq is not None:
                word_issues.append('%s: %s' % (q['id'], sq))
            # recomputation for the chosen questions
            if tag not in RECOMPUTE_TAGS:
                continue
            fn = CALC.get(q['id'])
            if fn is None:
                print('  %-34s (no calculation written)' % q['id'])
                continue
            mine, reasoning = fn(g, q['question'])
            stored = q['answer']['value']
            unit = q['answer'].get('unit', '')
            checked = checked + 1
            if stored == 0:
                ok = abs(mine) < 1e-9
            else:
                ok = abs(mine - stored) / abs(stored) <= 0.02
            if ok:
                matched = matched + 1
                verdict = 'OK'
            else:
                verdict = 'MISMATCH'
                mismatched.append((q['id'], q['question'], mine, stored, unit, reasoning))
            print('  %-34s mine=%-14.6g stored=%-14.6g %-6s %s' % (q['id'], mine, stored, unit, verdict))
            print('  %-34s   %s' % ('', reasoning))

    print()
    print('=' * 90)
    print('GRIDLINE EXCEPTIONS (marks / tangent end points off a major gridline)')
    for s in grid_issues or ['  none']:
        print('  ' + s if not s.startswith('  ') else s)
    print()
    print('WORDING EXCEPTIONS (tangent / shade present but not mentioned)')
    for s in word_issues or ['  none']:
        print('  ' + s if not s.startswith('  ') else s)
    print()
    print('MARK CONSISTENCY EXCEPTIONS')
    for s in mark_issues or ['  none']:
        print('  ' + s if not s.startswith('  ') else s)
    print()
    print('AXIS RANGE EXCEPTIONS')
    for s in range_issues or ['  none']:
        print('  ' + s if not s.startswith('  ') else s)
    print()
    print('MISMATCHES')
    for qid, text, mine, stored, unit, reasoning in mismatched or []:
        print('  %s: mine=%.6g stored=%.6g %s' % (qid, mine, stored, unit))
        print('     Q: %s' % text)
        print('     reasoning: %s' % reasoning)
    if not mismatched:
        print('  none')
    print()
    print('graphs seen: %d   checked: %d   matched: %d   mismatched: %d' % (graphs_seen, checked, matched, len(mismatched)))
    return 0 if not mismatched else 1


if __name__ == '__main__':
    sys.exit(main())
