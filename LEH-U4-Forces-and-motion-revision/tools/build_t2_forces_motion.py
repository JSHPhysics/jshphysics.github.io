#!/usr/bin/env python3
"""
build_t2_forces_motion.py — the source of truth for data/t2-forces-motion.json.

The content lives in four modules next to this script:

    t2_nn_a.py      The non-negotiables N1–N8
    t2_nn_b.py      The non-negotiables N9–N15
    t2_tricky_a.py  The tricky bits T1–T7
    t2_tricky_b.py  The tricky bits T8–T13, plus the key-facts flip cards

Every numeric answer is computed in Python inside those modules, never
typed from memory. Run from the app folder (LEH-U4-Forces-and-motion-revision):

    python3 tools/build_t2_forces_motion.py

Maths is written between $...$ (inline) or $$...$$ (display) and is
typeset by KaTeX in the browser. Everything else in a text field is HTML.
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import t2_nn_a  # noqa: E402
import t2_nn_b  # noqa: E402
import t2_tricky_a  # noqa: E402
import t2_tricky_b  # noqa: E402


# ---------------------------------------------------------------------
# Sections hidden from the U4 page
#
# The modules hold the whole of Topic 2, but the U4 scheme stops short of
# Newton's third law (and its balanced-forces trap), momentum, circular
# motion, inertial mass and the stopping-distance work (those spec points come later). Listing a section
# id here keeps its content in the modules but leaves it out of the JSON —
# and out of its key-fact cards — so the page only shows what U4 have been
# taught. Remove an id from this set to publish that section.
# ---------------------------------------------------------------------

HIDDEN_SECTIONS = {
    "newton-third",            # N13 · Newton's third law (2.23)
    "momentum",                # N14 · Momentum p = mv (2.24)
    "stopping-distance",       # N15 · Stopping distances and reaction time (2.27–2.30)
    "third-law-trap",          # T5 · Third-law pairs vs balanced forces (2.23)
    "circular-motion",         # T6 · Circular motion (2.20–2.21)
    "inertial-mass",           # T7 · Inertial mass (2.22)
    "conservation-momentum",   # T8 · Conservation of momentum (2.23–2.25)
    "force-momentum",          # T9 · F = Δp/t and safety features (2.26, 2.31)
    "braking-v-squared",       # T10 · Braking distance ∝ v² (2.32P, 2.33P)
}


# ---------------------------------------------------------------------
# The topic
# ---------------------------------------------------------------------

topic = {
    "id": "t2-forces-motion",
    "order": 1,
    "title": "Topic 2 - Forces and Motion (LEH, U4)",
    "subtitle": "Vectors, motion graphs, Newton's first and second laws, the force–mass–acceleration practical, reaction time and estimation — the Topic 2 spec points taught in U4 (Edexcel GCSE Physics 1PH0)",
    "stage": "GCSE Physics · Edexcel 1PH0",
    "lede": (
        "Everything in Topic 2, split into two bands. <b>The non-negotiables</b> are the facts and single-step calculations you must get right every time, "
        "without thinking. <b>The tricky bits</b> are where the marks are usually lost: multi-step calculations, explanations, and the ideas that look "
        "simple but have a trap in them. Each item is explained, shown in a worked example, then practised straight away."
    ),
    "howto": [
        "Start with the non-negotiables. Do not move on from a section until every practice question is green.",
        "Read each explanation, then cover it and say it back to yourself. For an equation, write it out with every symbol labelled.",
        "Study the worked example one step at a time and notice <i>how</i> the answer is laid out, not just what it is.",
        "Do the practice questions <b>before</b> opening the hint or walkthrough. Write every calculation in EWAU layout on paper first, then type the answer to check it.",
        "For \"explain\" questions, write your answer on paper in full sentences, then compare it with the model answer point by point before you mark yourself.",
        "Fill in the traffic-light self-check at the end of each section. Anything red or amber is what to revise next — and what to ask about in class.",
    ],
    "bands": [
        {
            "id": "nn",
            "prefix": "N",
            "title": "The non-negotiables",
            "blurb": "Recall and single-step calculations that must be automatic. If any of these is not yet green, it comes before anything in the second band.",
        },
        {
            "id": "tricky",
            "prefix": "T",
            "title": "The tricky bits",
            "blurb": "Multi-step calculations, explanation marks and the misconceptions that cost marks every year. Each one is built on something from the first band.",
        },
        {
            "id": "facts",
            "prefix": "K",
            "title": "Key facts",
            "blurb": "The whole topic on flip cards, for cover-and-test revision once the sections above are done.",
        },
    ],
    "sections": [],
}

all_sections = []
all_sections.extend(t2_nn_a.SECTIONS)
all_sections.extend(t2_nn_b.SECTIONS)
all_sections.extend(t2_tricky_a.SECTIONS)
all_sections.extend(t2_tricky_b.SECTIONS)

# Leave out the sections that are not on the U4 page
for section in all_sections:
    if section["id"] in HIDDEN_SECTIONS:
        continue
    topic["sections"].append(section)

# The key facts are their own band at the end; drop the cards of hidden sections
facts = t2_tricky_b.section_facts
facts["band"] = "facts"
for part in facts["parts"]:
    kept_items = []
    for item in part["items"]:
        if item["section"] in HIDDEN_SECTIONS:
            continue
        kept_items.append(item)
    part["items"] = kept_items
topic["sections"].append(facts)

# Every hidden id must be a real section, or a typo would silently hide nothing
known_ids = {section["id"] for section in all_sections}
for hidden_id in HIDDEN_SECTIONS:
    if hidden_id not in known_ids:
        print("PROBLEM: hidden section id not found:", hidden_id)
        sys.exit(1)


# ---------------------------------------------------------------------
# Checks that catch authoring slips before the browser does
# ---------------------------------------------------------------------


def leaf_questions(section):
    """Every markable question in a section, flattening groups."""
    leaves = []
    for part in section["parts"]:
        if part["kind"] != "practice":
            continue
        for question in part["questions"]:
            if question["type"] == "group":
                leaves.extend(question["parts"])
            else:
                leaves.append(question)
    return leaves


def check_graph(spec, where, problems):
    """Points must lie inside the axes; steps must divide the range."""
    for axis_name in ("x", "y"):
        axis_spec = spec[axis_name]
        span = axis_spec["max"] - axis_spec["min"]
        majors = span / axis_spec["step"]
        if abs(majors - round(majors)) > 1e-9:
            problems.append(where + ": " + axis_name + " step does not divide the range")
        if majors > 20:
            problems.append(where + ": " + axis_name + " has more than 20 major divisions")
    for series in spec["series"]:
        for point in series["points"]:
            inside_x = spec["x"]["min"] - 1e-9 <= point[0] <= spec["x"]["max"] + 1e-9
            inside_y = spec["y"]["min"] - 1e-9 <= point[1] <= spec["y"]["max"] + 1e-9
            if not (inside_x and inside_y):
                problems.append(where + ": point " + str(point) + " is outside the axes")
    for item in spec.get("marks", []) + spec.get("labels", []):
        inside_x = spec["x"]["min"] <= item["x"] <= spec["x"]["max"]
        inside_y = spec["y"]["min"] <= item["y"] <= spec["y"]["max"]
        if not (inside_x and inside_y):
            problems.append(where + ": mark/label at " + str((item["x"], item["y"])) + " is outside the axes")


def validate(topic_data):
    problems = []
    seen_ids = set()
    band_ids = {band["id"] for band in topic_data["bands"]}
    for section in topic_data["sections"]:
        where = section["id"]
        if section["id"] in seen_ids:
            problems.append("duplicate section id " + section["id"])
        seen_ids.add(section["id"])
        if section.get("band") not in band_ids:
            problems.append(where + ": unknown band " + str(section.get("band")))
        for part in section["parts"]:
            if part.get("graph"):
                check_graph(part["graph"], where + "/" + part["title"], problems)
            if part["kind"] == "practice":
                for question in part["questions"]:
                    if question.get("graph"):
                        check_graph(question["graph"], question["id"], problems)
        for question in leaf_questions(section):
            if question["id"] in seen_ids:
                problems.append("duplicate question id " + question["id"])
            seen_ids.add(question["id"])
            if question["type"] == "numeric":
                value = question["answer"]["value"]
                if not isinstance(value, (int, float)) or isinstance(value, bool):
                    problems.append(question["id"] + ": answer value is not a number")
                if not question.get("walkthrough"):
                    problems.append(question["id"] + ": missing walkthrough")
            if question["type"] == "choice":
                if not (0 <= question["correct"] < len(question["options"])):
                    problems.append(question["id"] + ": correct index out of range")
            if question["type"] == "written" and not question.get("model"):
                problems.append(question["id"] + ": missing model answer")
            if question.get("graph"):
                check_graph(question["graph"], question["id"], problems)
    return problems


def main():
    problems = validate(topic)
    if problems:
        for problem in problems:
            print("PROBLEM:", problem)
        sys.exit(1)

    out = os.path.join(HERE, "..", "data", "t2-forces-motion.json")
    with open(out, "w", encoding="utf-8") as handle:
        json.dump(topic, handle, ensure_ascii=False, indent=1)

    # Count the questions for the summary line
    count = 0
    for section in topic["sections"]:
        count += len(leaf_questions(section))
    print("wrote", os.path.normpath(out), "-", len(topic["sections"]), "sections,", count, "questions;",
          len(HIDDEN_SECTIONS), "sections hidden:", ", ".join(sorted(HIDDEN_SECTIONS)))


if __name__ == "__main__":
    main()
