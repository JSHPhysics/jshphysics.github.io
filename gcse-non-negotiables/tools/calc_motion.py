#!/usr/bin/env python3
"""Compute every answer and every plotted coordinate in data/motion.json.

Run:  python3 tools/calc_motion.py            -> answers, one per line
      python3 tools/calc_motion.py --graphs   -> also prints each graph spec
                                                 as JSON, ready to paste
The graph answers (gradients, areas, read-off values) are computed from the
same coordinates that the graph specs use, so the picture and the stored
answer cannot disagree.
"""

import json
import math
import sys

# Standard values from SCHEMA.md
G = 10  # m/s²

# Unit conversions
METRES_PER_KM = 1000
SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = 3600
HOURS_PER_DAY = 24

# Every graph spec, keyed by question id, collected for the --graphs print
GRAPHS = {}


def sig3(value):
    """Round a number to three significant figures (exact values stay exact)."""
    if value == 0:
        return 0
    # Number of digits before the decimal point
    magnitude = math.floor(math.log10(abs(value)))
    # Decimal places needed for 3 s.f.
    places = 2 - magnitude
    rounded = round(value, places)
    # Report an integer where the rounded value is whole
    if rounded == int(rounded):
        return int(rounded)
    return rounded


def show(question_id, value, unit):
    """Print one answer line."""
    print(f"{question_id:18s} {sig3(value)!s:>10s}  {unit}")


def gradient(point_a, point_b):
    """Gradient of the straight line through two [x, y] points."""
    rise = point_b[1] - point_a[1]
    run = point_b[0] - point_a[0]
    return rise / run


def area_under(points, x_from, x_to):
    """Area between a straight-segment series and the x-axis from x_from to x_to.

    Uses the trapezium rule on every segment, which is exact for straight lines.
    """
    total = 0
    for index in range(len(points) - 1):
        left = points[index]
        right = points[index + 1]
        # Clip the segment to the requested window
        start = max(left[0], x_from)
        end = min(right[0], x_to)
        if end <= start:
            continue
        # y values at the clipped ends (linear interpolation)
        slope = gradient(left, right)
        y_start = left[1] + slope * (start - left[0])
        y_end = left[1] + slope * (end - left[0])
        total += 0.5 * (y_start + y_end) * (end - start)
    return total


def value_at(points, x_wanted):
    """y value of a straight-segment series at a given x."""
    for index in range(len(points) - 1):
        left = points[index]
        right = points[index + 1]
        if left[0] <= x_wanted <= right[0]:
            slope = gradient(left, right)
            return left[1] + slope * (x_wanted - left[0])
    raise ValueError(f"x = {x_wanted} is outside the series")


def check_on_grid(graph, point):
    """Raise if a point the student must read is not on a major gridline crossing."""
    x_axis = graph["x"]
    y_axis = graph["y"]
    x_steps = (point[0] - x_axis["min"]) / x_axis["step"]
    y_steps = (point[1] - y_axis["min"]) / y_axis["step"]
    on_x = abs(x_steps - round(x_steps)) < 1e-9
    on_y = abs(y_steps - round(y_steps)) < 1e-9
    if not (on_x and on_y):
        raise ValueError(f"{point} is not on a major gridline crossing")


# ---------------------------------------------------------------
# Type 1: speed
# ---------------------------------------------------------------
print("# speed")

# w: cyclist 120 m in 8 s
show("speed-w", 120 / 8, "m/s")

# p1: sprinter 200 m in 25 s
show("speed-p1", 200 / 25, "m/s")

# p2: sound at 340 m/s for 2.5 s → distance
show("speed-p2", 340 * 2.5, "m")

# p3: car 36 km in 30 minutes → m/s
car_distance_m = 36 * METRES_PER_KM
car_time_s = 30 * SECONDS_PER_MINUTE
show("speed-p3", car_distance_m / car_time_s, "m/s")

# p4: walker at 1.5 m/s covers 2.7 km → time in s
walk_distance_m = 2.7 * METRES_PER_KM
show("speed-p4", walk_distance_m / 1.5, "s")

# p5: train 45 km in 25 min then 15 km in 5 min → average speed in m/s
train_distance_m = (45 + 15) * METRES_PER_KM
train_time_s = (25 + 5) * SECONDS_PER_MINUTE
show("speed-p5", train_distance_m / train_time_s, "m/s")

# p6: runner 100 m at 5 m/s then 100 m at 4 m/s → average speed
first_time = 100 / 5
second_time = 100 / 4
show("speed-p6", 200 / (first_time + second_time), "m/s")

# ---------------------------------------------------------------
# Type 2: acceleration
# ---------------------------------------------------------------
print("# acceleration")

# w: motorbike 5 → 23 m/s in 4 s
show("acceleration-w", (23 - 5) / 4, "m/s²")

# p1: sprinter 0 → 9 m/s in 3 s
show("acceleration-p1", (9 - 0) / 3, "m/s²")

# p2: train 30 → 12 m/s in 20 s (negative acceleration)
show("acceleration-p2", (12 - 30) / 20, "m/s²")

# p3: cyclist u = 3 m/s, a = 0.5 m/s², t = 8 s → v
show("acceleration-p3", 3 + 0.5 * 8, "m/s")

# p4: car 54 km/h → 90 km/h in 5 s
u_car = 54 * METRES_PER_KM / SECONDS_PER_HOUR
v_car = 90 * METRES_PER_KM / SECONDS_PER_HOUR
show("acceleration-p4", (v_car - u_car) / 5, "m/s²")

# p5: lift from rest at 1.2 m/s² for 5 s, then stops in 4 s → deceleration (magnitude)
lift_top_speed = 0 + 1.2 * 5
lift_deceleration = (lift_top_speed - 0) / 4
show("acceleration-p5", lift_deceleration, "m/s²")

# p6: car at 72 km/h, deceleration 4 m/s² → time to stop
u_brake = 72 * METRES_PER_KM / SECONDS_PER_HOUR
show("acceleration-p6", (u_brake - 0) / 4, "s")

# ---------------------------------------------------------------
# Type 3: v2-u2
# ---------------------------------------------------------------
print("# v2-u2")

# w: u = 5, a = 4, x = 18 → v
show("v2-u2-w", math.sqrt(5 ** 2 + 2 * 4 * 18), "m/s")

# p1: diver falls 5 m from rest → v
show("v2-u2-p1", math.sqrt(0 + 2 * G * 5), "m/s")

# p2: car 0 → 30 m/s over 150 m → a
show("v2-u2-p2", (30 ** 2 - 0) / (2 * 150), "m/s²")

# p3: plane lands at 60 m/s, a = −3 m/s², stops → x
show("v2-u2-p3", (0 - 60 ** 2) / (2 * -3), "m")

# p4: tennis ball rises 11.25 m, a = −10 → u
show("v2-u2-p4", math.sqrt(0 - 2 * -G * 11.25), "m/s")

# p5: car at 72 km/h, a = −5 m/s², stops → x
u_72 = 72 * METRES_PER_KM / SECONDS_PER_HOUR
show("v2-u2-p5", (0 - u_72 ** 2) / (2 * -5), "m")

# p6: toy rocket rises 320 cm, a = −10 → u
rocket_height_m = 320 / 100
show("v2-u2-p6", math.sqrt(0 - 2 * -G * rocket_height_m), "m/s")

# ---------------------------------------------------------------
# Type 4: dt-graph
# ---------------------------------------------------------------
print("# dt-graph")

# w: runner, speed in first 6 s from the gradient
dt_w_points = [[0, 0], [6, 30], [10, 30]]
GRAPHS["dt-graph-w"] = {
    "x": {"label": "time in s", "min": 0, "max": 10, "step": 1},
    "y": {"label": "distance in m", "min": 0, "max": 40, "step": 5},
    "series": [{"kind": "line", "points": dt_w_points}],
    "marks": [{"x": 6, "y": 30, "label": "A", "drop": True}],
    "alt": "Distance–time graph rising in a straight line from the origin to 30 m at 6 s, then flat at 30 m until 10 s",
}
check_on_grid(GRAPHS["dt-graph-w"], [6, 30])
show("dt-graph-w", gradient([0, 0], [6, 30]), "m/s")

# p1: cyclist, distance at t = 40 s
dt_p1_points = [[0, 0], [20, 120], [30, 120], [50, 200]]
GRAPHS["dt-graph-p1"] = {
    "x": {"label": "time in s", "min": 0, "max": 50, "step": 5},
    "y": {"label": "distance in m", "min": 0, "max": 200, "step": 20},
    "series": [{"kind": "line", "points": dt_p1_points}],
    "marks": [{"x": 40, "y": value_at(dt_p1_points, 40), "label": "P", "drop": True, "dx": 10, "dy": 16}],
    "alt": "Distance–time graph rising to 120 m at 20 s, flat until 30 s, then rising to 200 m at 50 s, with point P marked at 40 s",
}
check_on_grid(GRAPHS["dt-graph-p1"], [40, value_at(dt_p1_points, 40)])
show("dt-graph-p1", value_at(dt_p1_points, 40), "m")

# p2: walker out and back, speed on the return (100 s to 150 s)
dt_p2_points = [[0, 0], [60, 90], [100, 90], [150, 0]]
GRAPHS["dt-graph-p2"] = {
    "x": {"label": "time in s", "min": 0, "max": 150, "step": 10},
    "y": {"label": "distance from home in m", "min": 0, "max": 100, "step": 10},
    "series": [{"kind": "line", "points": dt_p2_points}],
    "alt": "Distance–time graph rising to 90 m at 60 s, flat until 100 s, then falling back to zero at 150 s",
}
check_on_grid(GRAPHS["dt-graph-p2"], [100, 90])
check_on_grid(GRAPHS["dt-graph-p2"], [150, 0])
# Speed is the size of the gradient
show("dt-graph-p2", abs(gradient([100, 90], [150, 0])), "m/s")

# p3: car, how many times faster in section A than section B
dt_p3_points = [[0, 0], [4, 80], [10, 140]]
GRAPHS["dt-graph-p3"] = {
    "x": {"label": "time in s", "min": 0, "max": 10, "step": 1},
    "y": {"label": "distance in m", "min": 0, "max": 160, "step": 20},
    "series": [{"kind": "line", "points": dt_p3_points}],
    "marks": [{"x": 4, "y": 80, "label": "", "drop": True}],
    "labels": [
        {"x": 1.2, "y": 60, "text": "A"},
        {"x": 6.5, "y": 95, "text": "B"},
    ],
    "alt": "Distance–time graph with a steep section A from the origin to 80 m at 4 s, then a shallower section B to 140 m at 10 s",
}
check_on_grid(GRAPHS["dt-graph-p3"], [4, 80])
check_on_grid(GRAPHS["dt-graph-p3"], [10, 140])
speed_a = gradient([0, 0], [4, 80])
speed_b = gradient([4, 80], [10, 140])
show("dt-graph-p3", speed_a / speed_b, "")

# p4: bus, time axis in minutes, speed in first 10 minutes in m/s
dt_p4_points = [[0, 0], [10, 1500], [15, 1500], [30, 3000]]
GRAPHS["dt-graph-p4"] = {
    "x": {"label": "time in minutes", "min": 0, "max": 30, "step": 5},
    "y": {"label": "distance in m", "min": 0, "max": 3000, "step": 500},
    "series": [{"kind": "line", "points": dt_p4_points}],
    "marks": [{"x": 10, "y": 1500, "label": "Q", "drop": True}],
    "alt": "Distance–time graph with time in minutes, rising to 1500 m at 10 minutes, flat until 15 minutes, then rising to 3000 m at 30 minutes",
}
check_on_grid(GRAPHS["dt-graph-p4"], [10, 1500])
bus_time_s = 10 * SECONDS_PER_MINUTE
show("dt-graph-p4", 1500 / bus_time_s, "m/s")

# p5: delivery van out, stop, back → average speed for whole journey
dt_p5_points = [[0, 0], [30, 300], [50, 300], [80, 0]]
GRAPHS["dt-graph-p5"] = {
    "x": {"label": "time in s", "min": 0, "max": 80, "step": 10},
    "y": {"label": "distance from depot in m", "min": 0, "max": 400, "step": 50},
    "series": [{"kind": "line", "points": dt_p5_points}],
    "alt": "Distance–time graph rising to 300 m at 30 s, flat until 50 s, then falling back to zero at 80 s",
}
check_on_grid(GRAPHS["dt-graph-p5"], [30, 300])
check_on_grid(GRAPHS["dt-graph-p5"], [80, 0])
# Total distance travelled is out plus back
van_total_distance = 300 + 300
van_total_time = 80
show("dt-graph-p5", van_total_distance / van_total_time, "m/s")

# p6: train, speed in final 20 s converted to km/h
dt_p6_points = [[0, 0], [20, 200], [40, 200], [60, 900]]
GRAPHS["dt-graph-p6"] = {
    "x": {"label": "time in s", "min": 0, "max": 60, "step": 10},
    "y": {"label": "distance in m", "min": 0, "max": 1000, "step": 100},
    "series": [{"kind": "line", "points": dt_p6_points}],
    "marks": [
        {"x": 40, "y": 200, "label": "R", "drop": True, "dx": 6, "dy": 16},
        {"x": 60, "y": 900, "label": "S", "drop": True, "dx": -16, "dy": -6},
    ],
    "alt": "Distance–time graph rising to 200 m at 20 s, flat until 40 s at point R, then rising steeply to 900 m at 60 s at point S",
}
check_on_grid(GRAPHS["dt-graph-p6"], [40, 200])
check_on_grid(GRAPHS["dt-graph-p6"], [60, 900])
train_speed_ms = gradient([40, 200], [60, 900])
train_speed_kmh = train_speed_ms * SECONDS_PER_HOUR / METRES_PER_KM
show("dt-graph-p6", train_speed_kmh, "km/h")

# ---------------------------------------------------------------
# Type 5: vt-graph
# ---------------------------------------------------------------
print("# vt-graph")

# w: acceleration in the first 8 s from the gradient
vt_w_points = [[0, 0], [8, 20], [12, 20]]
GRAPHS["vt-graph-w"] = {
    "x": {"label": "time in s", "min": 0, "max": 12, "step": 2},
    "y": {"label": "velocity in m/s", "min": 0, "max": 25, "step": 5},
    "series": [{"kind": "line", "points": vt_w_points}],
    "marks": [{"x": 8, "y": 20, "label": "A", "drop": True}],
    "alt": "Velocity–time graph rising in a straight line from the origin to 20 m/s at 8 s, then constant at 20 m/s until 12 s",
}
check_on_grid(GRAPHS["vt-graph-w"], [8, 20])
show("vt-graph-w", gradient([0, 0], [8, 20]), "m/s²")

# p1: train, distance in the constant-velocity section (rectangle)
vt_p1_points = [[0, 0], [10, 15], [50, 15], [60, 0]]
GRAPHS["vt-graph-p1"] = {
    "x": {"label": "time in s", "min": 0, "max": 60, "step": 10},
    "y": {"label": "velocity in m/s", "min": 0, "max": 20, "step": 5},
    "series": [{"kind": "line", "points": vt_p1_points}],
    "shade": [{"series": 0, "from": 10, "to": 50}],
    "alt": "Velocity–time graph rising to 15 m/s at 10 s, constant until 50 s with that section shaded, then falling to zero at 60 s",
}
check_on_grid(GRAPHS["vt-graph-p1"], [10, 15])
check_on_grid(GRAPHS["vt-graph-p1"], [50, 15])
show("vt-graph-p1", area_under(vt_p1_points, 10, 50), "m")

# p2: sprinter, distance while accelerating (triangle)
vt_p2_points = [[0, 0], [4, 10], [10, 10]]
GRAPHS["vt-graph-p2"] = {
    "x": {"label": "time in s", "min": 0, "max": 10, "step": 1},
    "y": {"label": "velocity in m/s", "min": 0, "max": 12, "step": 2},
    "series": [{"kind": "line", "points": vt_p2_points}],
    "shade": [{"series": 0, "from": 0, "to": 4}],
    "alt": "Velocity–time graph rising from the origin to 10 m/s at 4 s with that triangle shaded, then constant at 10 m/s until 10 s",
}
check_on_grid(GRAPHS["vt-graph-p2"], [4, 10])
show("vt-graph-p2", area_under(vt_p2_points, 0, 4), "m")

# p3: car, deceleration between 6 s and 14 s
vt_p3_points = [[0, 20], [6, 20], [14, 0]]
GRAPHS["vt-graph-p3"] = {
    "x": {"label": "time in s", "min": 0, "max": 16, "step": 2},
    "y": {"label": "velocity in m/s", "min": 0, "max": 25, "step": 5},
    "series": [{"kind": "line", "points": vt_p3_points}],
    "marks": [{"x": 6, "y": 20, "label": "B", "drop": True}],
    "alt": "Velocity–time graph constant at 20 m/s until 6 s at point B, then falling in a straight line to zero at 14 s",
}
check_on_grid(GRAPHS["vt-graph-p3"], [6, 20])
check_on_grid(GRAPHS["vt-graph-p3"], [14, 0])
# Deceleration is the size of the negative gradient
show("vt-graph-p3", abs(gradient([6, 20], [14, 0])), "m/s²")

# p4: motorbike, distance in the first 6 s (trapezium)
vt_p4_points = [[0, 10], [6, 25], [8, 25]]
GRAPHS["vt-graph-p4"] = {
    "x": {"label": "time in s", "min": 0, "max": 8, "step": 1},
    "y": {"label": "velocity in m/s", "min": 0, "max": 30, "step": 5},
    "series": [{"kind": "line", "points": vt_p4_points}],
    "shade": [{"series": 0, "from": 0, "to": 6}],
    "alt": "Velocity–time graph starting at 10 m/s and rising in a straight line to 25 m/s at 6 s with that trapezium shaded, then constant until 8 s",
}
check_on_grid(GRAPHS["vt-graph-p4"], [0, 10])
check_on_grid(GRAPHS["vt-graph-p4"], [6, 25])
show("vt-graph-p4", area_under(vt_p4_points, 0, 6), "m")

# p5 (Higher): rocket, tangent to a curve at X gives the acceleration
# The curve is v = 0.25 t², so the gradient at t is 0.5 t
def rocket_velocity(time):
    """Velocity of the model rocket at a given time."""
    return 0.25 * time ** 2


def rocket_gradient(time):
    """Gradient of the velocity–time curve at a given time."""
    return 0.5 * time


tangent_time = 8
tangent_point = [tangent_time, rocket_velocity(tangent_time)]
tangent_slope = rocket_gradient(tangent_time)
# Tangent end points chosen on gridline crossings: t = 4 and t = 12
tangent_start_t = 4
tangent_end_t = 12
tangent_start = [tangent_start_t, tangent_point[1] + tangent_slope * (tangent_start_t - tangent_time)]
tangent_end = [tangent_end_t, tangent_point[1] + tangent_slope * (tangent_end_t - tangent_time)]
# Sample the curve every second (13 points) for a smooth plot
rocket_curve = []
sample_time = 0
while sample_time <= 12:
    rocket_curve.append([sample_time, rocket_velocity(sample_time)])
    sample_time += 1
GRAPHS["vt-graph-p5"] = {
    "x": {"label": "time in s", "min": 0, "max": 12, "step": 2},
    "y": {"label": "velocity in m/s", "min": 0, "max": 40, "step": 4},
    "series": [
        {"kind": "curve", "points": rocket_curve},
        {"kind": "tangent", "points": [tangent_start, tangent_end]},
    ],
    "marks": [{"x": tangent_point[0], "y": tangent_point[1], "label": "X", "drop": True, "dx": 10, "dy": 16}],
    "alt": "Velocity–time curve bending upwards from the origin to 36 m/s at 12 s, with point X at 8 s and the tangent at X drawn from (4, 0) to (12, 32)",
}
check_on_grid(GRAPHS["vt-graph-p5"], tangent_start)
check_on_grid(GRAPHS["vt-graph-p5"], tangent_end)
check_on_grid(GRAPHS["vt-graph-p5"], tangent_point)
# Student reads the gradient from the two tangent end points
show("vt-graph-p5", gradient(tangent_start, tangent_end), "m/s²")

# p6: tram journey in three sections → total distance (two triangles + rectangle)
vt_p6_points = [[0, 0], [10, 20], [30, 20], [40, 0]]
GRAPHS["vt-graph-p6"] = {
    "x": {"label": "time in s", "min": 0, "max": 40, "step": 5},
    "y": {"label": "velocity in m/s", "min": 0, "max": 25, "step": 5},
    "series": [
        {"kind": "line", "points": vt_p6_points},
        {"kind": "dashed", "points": [[10, 0], [10, 20]]},
        {"kind": "dashed", "points": [[30, 0], [30, 20]]},
    ],
    "shade": [{"series": 0, "from": 0, "to": 40}],
    "alt": "Velocity–time graph rising to 20 m/s at 10 s, constant until 30 s, then falling to zero at 40 s, with the whole area under the line shaded and dashed lines at 10 s and 30 s",
}
check_on_grid(GRAPHS["vt-graph-p6"], [10, 20])
check_on_grid(GRAPHS["vt-graph-p6"], [30, 20])
check_on_grid(GRAPHS["vt-graph-p6"], [40, 0])
tram_first = area_under(vt_p6_points, 0, 10)
tram_middle = area_under(vt_p6_points, 10, 30)
tram_last = area_under(vt_p6_points, 30, 40)
show("vt-graph-p6", tram_first + tram_middle + tram_last, "m")

# ---------------------------------------------------------------
# Optional: print the graph specs ready to paste into the JSON
# ---------------------------------------------------------------
if "--graphs" in sys.argv:
    print()
    print("# graph specs")
    for question_id, graph in GRAPHS.items():
        print(f"## {question_id}")
        print(json.dumps(graph, ensure_ascii=False))
