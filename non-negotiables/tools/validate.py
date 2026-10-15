#!/usr/bin/env python3
"""Validate one or more Non-negotiables topic JSON files against SCHEMA.md.

Usage: python3 tools/validate.py data/kinematics.json [more files...]
Exit code 0 when every file passes, 1 otherwise.
"""

import json
import re
import sys

# The five exam-board tags the app understands
VALID_BOARDS = {"AQA", "OCR A", "OCR B", "Edexcel", "WJEC"}

# kebab-case identifiers only
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

# Characters that indicate LaTeX or HTML slipped into plain-text fields
FORBIDDEN = re.compile(r"(\\\(|\\\[|\$|<[a-z/][^>]*>|\^\{|_\{)")


def check_text(problems, where, text, min_len=1):
    """Check a plain-text field: non-empty string, no LaTeX/HTML markup."""
    if not isinstance(text, str):
        problems.append(f"{where}: expected a string")
        return
    if len(text.strip()) < min_len:
        problems.append(f"{where}: empty or too short")
    if FORBIDDEN.search(text):
        problems.append(f"{where}: contains LaTeX or HTML markup: {text[:60]!r}")


def check_lines(problems, where, lines, lo, hi):
    """Check an array of plain-text working lines."""
    if not isinstance(lines, list):
        problems.append(f"{where}: expected a list of strings")
        return
    if not (lo <= len(lines) <= hi):
        problems.append(f"{where}: {len(lines)} lines, expected {lo}–{hi}")
    for index, line in enumerate(lines):
        check_text(problems, f"{where}[{index}]", line)


def check_answer(problems, where, answer):
    """Check an answer object: numeric value, string unit, optional tolerance."""
    if not isinstance(answer, dict):
        problems.append(f"{where}: expected an object")
        return
    value = answer.get("value")
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        problems.append(f"{where}.value: must be a JSON number, got {value!r}")
    if "unit" not in answer or not isinstance(answer["unit"], str):
        problems.append(f"{where}.unit: must be a string (use \"\" if dimensionless)")
    tolerance = answer.get("tolerance")
    if tolerance is not None:
        if not isinstance(tolerance, (int, float)) or not (0 < tolerance <= 0.2):
            problems.append(f"{where}.tolerance: must be a fraction between 0 and 0.2")
    # Flag suspicious precision: an answer with more than 5 s.f. is usually unrounded
    if isinstance(value, float):
        digits = re.sub(r"[^0-9]", "", repr(value).split("e")[0]).lstrip("0")
        if len(digits) > 5:
            problems.append(f"{where}.value: {value!r} looks unrounded (give 3 s.f.)")


def check_boards(problems, where, boards):
    """Check a boards array: non-empty subset of VALID_BOARDS."""
    if not isinstance(boards, list) or not boards:
        problems.append(f"{where}: must be a non-empty list")
        return
    for board in boards:
        if board not in VALID_BOARDS:
            problems.append(f"{where}: unknown board {board!r}; valid: {sorted(VALID_BOARDS)}")


GRAPH_KINDS = {"line", "curve", "dashed", "data", "tangent"}


def check_axis(problems, where, axis):
    """Check one graph axis: label, numeric range, step dividing the range."""
    if not isinstance(axis, dict):
        problems.append(f"{where}: missing or not an object")
        return
    check_text(problems, f"{where}.label", axis.get("label"))
    for key in ("min", "max", "step"):
        value = axis.get(key)
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            problems.append(f"{where}.{key}: must be a number")
            return
    span = axis["max"] - axis["min"]
    if span <= 0:
        problems.append(f"{where}: max must exceed min")
        return
    majors = span / axis["step"]
    if abs(majors - round(majors)) > 1e-6:
        problems.append(f"{where}: step {axis['step']} does not divide the range {span} exactly")
    if majors > 20:
        problems.append(f"{where}: {majors:.0f} major divisions is too many (max 20)")


def check_graph(problems, where, graph):
    """Check a graph spec: axes, series, marks, shaded regions."""
    if not isinstance(graph, dict):
        problems.append(f"{where}: must be an object")
        return
    check_axis(problems, f"{where}.x", graph.get("x"))
    check_axis(problems, f"{where}.y", graph.get("y"))
    x_axis = graph.get("x") if isinstance(graph.get("x"), dict) else {}
    y_axis = graph.get("y") if isinstance(graph.get("y"), dict) else {}

    def inside(point):
        """Is a point within the axis ranges (with a little slack)?"""
        if not all(isinstance(axis.get(k), (int, float)) for axis in (x_axis, y_axis) for k in ("min", "max")):
            return True
        return (x_axis["min"] - 1e-9 <= point[0] <= x_axis["max"] + 1e-9 and
                y_axis["min"] - 1e-9 <= point[1] <= y_axis["max"] + 1e-9)

    series_list = graph.get("series")
    if not isinstance(series_list, list) or not series_list:
        problems.append(f"{where}.series: must be a non-empty list")
        series_list = []
    for index, series in enumerate(series_list):
        swhere = f"{where}.series[{index}]"
        if not isinstance(series, dict):
            problems.append(f"{swhere}: must be an object")
            continue
        kind = series.get("kind", "line")
        if kind not in GRAPH_KINDS:
            problems.append(f"{swhere}.kind: unknown kind {kind!r}")
        points = series.get("points")
        minimum = 1 if kind == "data" else 2
        if not isinstance(points, list) or len(points) < minimum:
            problems.append(f"{swhere}.points: need at least {minimum} point(s)")
            continue
        for pindex, point in enumerate(points):
            if (not isinstance(point, list) or len(point) != 2 or
                    not all(isinstance(v, (int, float)) and not isinstance(v, bool) for v in point)):
                problems.append(f"{swhere}.points[{pindex}]: must be [x, y] numbers")
            elif not inside(point):
                problems.append(f"{swhere}.points[{pindex}]: {point} lies outside the axes")
        if kind == "curve" and len(points) < 8:
            problems.append(f"{swhere}: a curve needs at least 8 points to look smooth")
        if kind == "tangent" and len(points) != 2:
            problems.append(f"{swhere}: a tangent is exactly two end points")
        fit = series.get("fit")
        if fit is not None and (not isinstance(fit, list) or len(fit) != 2):
            problems.append(f"{swhere}.fit: must be two end points")

    for index, mark in enumerate(graph.get("marks", []) or []):
        if not isinstance(mark, dict) or not all(isinstance(mark.get(k), (int, float)) for k in ("x", "y")):
            problems.append(f"{where}.marks[{index}]: x and y must be numbers")
        elif not inside([mark["x"], mark["y"]]):
            problems.append(f"{where}.marks[{index}]: lies outside the axes")

    for index, region in enumerate(graph.get("shade", []) or []):
        if not isinstance(region, dict) or not all(isinstance(region.get(k), (int, float)) for k in ("from", "to")):
            problems.append(f"{where}.shade[{index}]: from and to must be numbers")
        elif region.get("series", 0) >= len(series_list):
            problems.append(f"{where}.shade[{index}]: series index out of range")

    if "alt" in graph:
        check_text(problems, f"{where}.alt", graph["alt"], min_len=10)


def check_question(problems, where, question, expected_id, is_worked):
    """Check a worked example or a practice question."""
    if not isinstance(question, dict):
        problems.append(f"{where}: expected an object")
        return

    if question.get("id") != expected_id:
        problems.append(f"{where}.id: expected {expected_id!r}, got {question.get('id')!r}")

    check_text(problems, f"{where}.question", question.get("question"), min_len=20)

    if is_worked:
        check_lines(problems, f"{where}.steps", question.get("steps"), 3, 9)
    else:
        check_text(problems, f"{where}.hint", question.get("hint"), min_len=10)
        check_lines(problems, f"{where}.walkthrough", question.get("walkthrough"), 2, 8)

    check_answer(problems, f"{where}.answer", question.get("answer"))

    if "graph" in question:
        check_graph(problems, f"{where}.graph", question["graph"])

    if "boards" in question:
        check_boards(problems, f"{where}.boards", question["boards"])


def check_type(problems, where, ctype, seen_type_ids):
    """Check one calculation type and everything inside it."""
    if not isinstance(ctype, dict):
        problems.append(f"{where}: expected an object")
        return

    type_id = ctype.get("id")
    if not isinstance(type_id, str) or not KEBAB.match(type_id):
        problems.append(f"{where}.id: must be kebab-case, got {type_id!r}")
    elif type_id in seen_type_ids:
        problems.append(f"{where}.id: duplicate id {type_id!r}")
    else:
        seen_type_ids.add(type_id)

    check_text(problems, f"{where}.name", ctype.get("name"), min_len=5)

    equations = ctype.get("equations")
    if not isinstance(equations, list) or not equations:
        problems.append(f"{where}.equations: must be a non-empty list")
    else:
        for index, equation in enumerate(equations):
            check_text(problems, f"{where}.equations[{index}]", equation)

    check_boards(problems, f"{where}.boards", ctype.get("boards"))
    check_text(problems, f"{where}.method", ctype.get("method"), min_len=40)
    check_lines(problems, f"{where}.commonErrors", ctype.get("commonErrors"), 2, 4)

    check_question(problems, f"{where}.worked", ctype.get("worked"), f"{type_id}-w", True)

    practice = ctype.get("practice")
    if not isinstance(practice, list) or len(practice) != 6:
        count = len(practice) if isinstance(practice, list) else "none"
        problems.append(f"{where}.practice: must have exactly 6 questions, found {count}")
        practice = practice if isinstance(practice, list) else []
    for index, question in enumerate(practice):
        check_question(problems, f"{where}.practice[{index}]", question, f"{type_id}-p{index + 1}", False)


def validate_file(path):
    """Validate one topic file; return a list of problem strings."""
    problems = []

    try:
        with open(path, encoding="utf-8") as handle:
            topic = json.load(handle)
    except Exception as error:
        return [f"{path}: cannot parse JSON: {error}"]

    if not isinstance(topic, dict):
        return [f"{path}: top level must be an object"]

    topic_id = topic.get("id")
    if not isinstance(topic_id, str) or not KEBAB.match(topic_id):
        problems.append(f"id: must be kebab-case, got {topic_id!r}")
    else:
        # The file name must match the id
        file_stem = path.split("/")[-1].removesuffix(".json")
        if file_stem != topic_id:
            problems.append(f"id {topic_id!r} does not match file name {file_stem!r}")

    check_text(problems, "title", topic.get("title"), min_len=3)
    check_text(problems, "subtitle", topic.get("subtitle"), min_len=5)

    if not isinstance(topic.get("order"), int):
        problems.append("order: must be an integer")

    types = topic.get("types")
    if not isinstance(types, list) or not types:
        problems.append("types: must be a non-empty list")
        types = []

    seen_type_ids = set()
    for index, ctype in enumerate(types):
        check_type(problems, f"types[{index}]", ctype, seen_type_ids)

    return problems


def main(paths):
    """Validate every path given; print a report; return the exit code."""
    all_ok = True

    for path in paths:
        problems = validate_file(path)
        if problems:
            all_ok = False
            print(f"FAIL {path}: {len(problems)} problem(s)")
            for problem in problems:
                print(f"  - {problem}")
        else:
            # Count content for the summary line
            with open(path, encoding="utf-8") as handle:
                topic = json.load(handle)
            type_count = len(topic["types"])
            print(f"OK   {path}: {type_count} types, {type_count * 7} questions")

    return 0 if all_ok else 1


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1:]))
