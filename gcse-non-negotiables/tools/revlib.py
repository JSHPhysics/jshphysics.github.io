"""
revlib.py — helpers for authoring the revision content of a GCSE topic.

A topic's notes are written in Python (one module per band) so that
KaTeX can be typed as raw strings and every numeric answer is computed,
never typed. The build script for the topic merges the result into the
topic's JSON file, keeping the calculation `types` as they are.

Conventions (see SCHEMA.md, "Revision content"):
- text fields are HTML; maths goes between $...$ or $$...$$
- `equations` on a section are TeX without dollars
- question ids are global: <topic>-<section>-q<n>
"""

from math import floor, log10


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


def numeric(qid, text, value, unit, hint, walkthrough, label=None, graph=None, tolerance=None, tags=None):
    """A question the app marks: the student types a number."""
    # Whole-number answers are stored as integers so they read cleanly
    if isinstance(value, float) and value.is_integer():
        value = int(value)
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
    if tags:
        question["tags"] = tags
    return question


def choice(qid, text, options, correct, explain, hint=None, label=None, graph=None, tags=None):
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
    if tags:
        question["tags"] = tags
    return question


def written(qid, text, model, lines=3, hint=None, label=None, graph=None, tags=None):
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
    if tags:
        question["tags"] = tags
    return question


def draw(qid, text, grid, model, answer_graph=None, check=False, hint=None, label=None, tags=None):
    """A sketch on a grid; checked against answer_graph when `check` is true."""
    question = {
        "id": qid,
        "type": "draw",
        "text": text,
        "grid": grid,
        "model": model,
    }
    if answer_graph is not None:
        question["answerGraph"] = answer_graph
    if check:
        question["check"] = True
    if hint is not None:
        question["hint"] = hint
    if label is not None:
        question["label"] = label
    if tags:
        question["tags"] = tags
    return question


def group(qid, text, parts, graph=None, tags=None):
    """A multi-part question (parts carry labels a, b, c …)."""
    question = {"id": qid, "type": "group", "text": text, "parts": parts}
    if graph is not None:
        question["graph"] = graph
    if tags:
        question["tags"] = tags
    return question


def marks(points):
    """A model answer as a bullet list of mark-scheme points."""
    items = "".join("<li>" + point + "</li>" for point in points)
    return "<ul>" + items + "</ul>"


def mark_scheme(points, total=None, extra=None):
    """A model answer as a one-row-per-mark table.

    `points` is a list of (short label, what the student must write).
    `total` caps the marks when there are more rows than marks.
    `extra` is an optional list of lines about what is also accepted or
    what gets no credit."""
    count = len(points)
    if total is None:
        total = count
    if total == count:
        head = "<p><b>" + str(total) + " mark" + ("s" if total != 1 else "") + "</b> — one mark per row.</p>"
    else:
        head = "<p><b>" + str(total) + " marks</b> — one mark per row below, any " + str(total) + " of the " + str(count) + ".</p>"
    html = head + "<table class='tbl'><tr><th>Point</th><th>For</th><th>What you need to write</th></tr>"
    number = 0
    for short, detail in points:
        number += 1
        html += "<tr><td><b>" + str(number) + "</b></td><td>" + short + "</td><td>" + detail + "</td></tr>"
    html += "</table>"
    if extra:
        html += "<ul>"
        for line in extra:
            html += "<li>" + line + "</li>"
        html += "</ul>"
    return html


# ---------------------------------------------------------------------
# Parts
# ---------------------------------------------------------------------


def explain(title, html, tone=None, graph=None, after=None):
    part = {"kind": "explain", "title": title, "html": html}
    if tone:
        part["tone"] = tone
    if graph is not None:
        part["graph"] = graph
    if after:
        part["after"] = after
    return part


def worked(title, question, steps, graph=None):
    part = {"kind": "worked", "title": title, "question": question, "steps": steps}
    if graph is not None:
        part["graph"] = graph
    return part


def practice(title, questions, intro=None):
    part = {"kind": "practice", "title": title, "questions": questions}
    if intro:
        part["intro"] = intro
    return part


def types(ids, title="Calculations", intro=None):
    part = {"kind": "types", "ids": ids, "title": title}
    if intro:
        part["intro"] = intro
    return part


def section(sid, band, title, spec, parts, checklist, equations=None, blurb=None, tags=None):
    result = {
        "id": sid,
        "band": band,
        "title": title,
        "spec": spec,
        "equations": equations or [],
        "parts": parts,
        "checklist": checklist,
    }
    if blurb:
        result["blurb"] = blurb
    if tags:
        result["tags"] = tags
    return result


def fact(q, a, section_id):
    return {"q": q, "a": a, "section": section_id}


# ---------------------------------------------------------------------
# Graph shapes (see SCHEMA.md "Graph questions")
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
    return {"kind": "tangent", "points": points}


def data(points):
    """Plotted data points (crosses), no line."""
    return {"kind": "data", "points": points}


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
        points.append([round(x, 4), round(fn(x), 4)])
    return points


# ---------------------------------------------------------------------
# Diagrams: a small inline-SVG wrapper
# ---------------------------------------------------------------------


def diagram(svg_inner, width, height, caption=None):
    """An inline SVG inside <figure class="diagram">. Use the classes
    d-ink, d-accent, d-fill and d-readout for theme-aware colours."""
    html = "<figure class='diagram'><svg viewBox='0 0 " + str(width) + " " + str(height) + "' role='img'>" + svg_inner + "</svg>"
    if caption:
        html += "<figcaption>" + caption + "</figcaption>"
    html += "</figure>"
    return html


# ---------------------------------------------------------------------
# Numbers
# ---------------------------------------------------------------------


def sf(value, figures=3):
    """Round a computed answer to a number of significant figures."""
    if value == 0:
        return 0
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
