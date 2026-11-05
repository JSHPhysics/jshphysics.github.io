"""
t2lib.py — small helpers shared by the Topic 2 build modules.

The booklet content is authored in Python so that KaTeX can be written as
raw strings. Maths goes between $...$ (inline) or $$...$$ (display);
everything else in a text field is HTML.
"""


# ---------------------------------------------------------------------
# Question shapes
# ---------------------------------------------------------------------


def ewau(equation, working, answer, units):
    """The four lines of an EWAU calculation, as walkthrough steps."""
    return [
        r"<b>Equation:</b> $" + equation + "$",
        r"<b>Working:</b> $" + working + "$",
        r"<b>Answer:</b> $= " + answer + "$",
        r"<b>Units:</b> " + units,
    ]


def numeric(qid, text, value, unit, hint, walkthrough, label=None, graph=None, tolerance=None):
    """A question the app marks: the student types a number."""
    question = {
        "id": qid,
        "type": "numeric",
        "text": text,
        "answer": {"value": value, "unit": unit},
        "hint": hint,
        "walkthrough": walkthrough,
    }
    if tolerance is not None:
        question["answer"]["tolerance"] = tolerance
    if label is not None:
        question["label"] = label
    if graph is not None:
        question["graph"] = graph
    return question


def choice(qid, text, options, correct, explain, hint=None, label=None, graph=None):
    """A multiple-choice question; `correct` is the index of the right option."""
    question = {
        "id": qid,
        "type": "choice",
        "text": text,
        "options": options,
        "correct": correct,
        "explain": explain,
    }
    if hint is not None:
        question["hint"] = hint
    if label is not None:
        question["label"] = label
    if graph is not None:
        question["graph"] = graph
    return question


def written(qid, text, model, lines=3, hint=None, label=None, graph=None):
    """An explain-style question the student self-marks against a model answer."""
    question = {
        "id": qid,
        "type": "written",
        "text": text,
        "model": model,
        "lines": lines,
    }
    if hint is not None:
        question["hint"] = hint
    if label is not None:
        question["label"] = label
    if graph is not None:
        question["graph"] = graph
    return question


def group(qid, text, parts, graph=None):
    """A multi-part question (parts carry labels a, b, c …)."""
    question = {"id": qid, "type": "group", "text": text, "parts": parts}
    if graph is not None:
        question["graph"] = graph
    return question


def marks(points):
    """Format a model answer as a bullet list of mark-scheme points."""
    items = "".join("<li>" + point + "</li>" for point in points)
    return "<ul>" + items + "</ul>"


# ---------------------------------------------------------------------
# Graph shapes (see the Non-negotiables SCHEMA.md for the full spec)
# ---------------------------------------------------------------------


def axis(label, mx, step, mn=0, minor=None):
    result = {"label": label, "min": mn, "max": mx, "step": step}
    if minor is not None:
        result["minor"] = minor
    return result


def line(points):
    return {"kind": "line", "points": points}


def curve(points):
    return {"kind": "curve", "points": points}


def dashed(points):
    return {"kind": "dashed", "points": points}


def tangent(points):
    """A tangent drawn in the accent colour; end points on gridline crossings."""
    return {"kind": "tangent", "points": points}


def mark(x, y, text, drop=False, dx=None, dy=None):
    result = {"x": x, "y": y, "label": text}
    if drop:
        result["drop"] = True
    if dx is not None:
        result["dx"] = dx
    if dy is not None:
        result["dy"] = dy
    return result


def label(x, y, text, anchor="middle"):
    return {"x": x, "y": y, "text": text, "anchor": anchor}


def shade(series_index, start, end):
    return {"series": series_index, "from": start, "to": end}


def graph(x_axis, y_axis, series, alt, marks_list=None, shade_list=None, labels=None):
    spec = {"x": x_axis, "y": y_axis, "series": series, "alt": alt}
    if marks_list:
        spec["marks"] = marks_list
    if shade_list:
        spec["shade"] = shade_list
    if labels:
        spec["labels"] = labels
    return spec


def sample(fn, start, end, count=13):
    """Sample a function for a smooth curve (points rounded for the JSON)."""
    points = []
    for index in range(count):
        x = start + (end - start) * index / (count - 1)
        points.append([round(x, 3), round(fn(x), 3)])
    return points


# ---------------------------------------------------------------------
# Numbers
# ---------------------------------------------------------------------


def sf(value, figures=3):
    """Round a computed answer to a number of significant figures."""
    if value == 0:
        return 0
    from math import floor, log10
    digits = figures - 1 - floor(log10(abs(value)))
    rounded = round(value, digits)
    if digits <= 0:
        return int(rounded)
    return rounded


def fmt(value):
    """Show a number the way a student would write it (no trailing .0)."""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)
