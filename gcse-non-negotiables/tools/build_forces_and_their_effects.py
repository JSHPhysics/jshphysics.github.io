#!/usr/bin/env python3
"""
build_forces_and_their_effects.py — write the revision content of Topic 9
into data/forces-and-their-effects.json, keeping its two calculation
types (moment, balance) and embedding them in N6 and N7.

Content modules:

    fe_diagrams.py   The ten diagrams (SVG)
    fe_nn.py         The non-negotiables N1–N10 (N10 = key words)
    fe_tricky.py     The tricky bits T1–T8 and the flashcards

Tags: 9.6P–9.9P are Physics-only (N6, N7, N8, T5, T6, T7 carry P);
9.3 and 9.5 are Higher-only in the spec (T1–T4 carry H).

Run from the gcse-non-negotiables folder:

    python3 tools/build_forces_and_their_effects.py
    python3 tools/build_manifest.py
"""

import copy
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import fe_nn  # noqa: E402
import fe_tricky  # noqa: E402
from revlib import types  # noqa: E402
from validate import validate_file  # noqa: E402

TOPIC_PATH = os.path.join(HERE, "..", "data", "forces-and-their-effects.json")

# Which calculation types each section embeds (after its worked example)
EMBEDS = {
    "moment-nn": ["moment"],
    "balance-nn": ["balance"],
}

REVISION = {
    "lede": (
        "Everything in Topic 9, split into two bands. <b>The non-negotiables</b> are the kinds of force, interaction pairs, vectors, free body diagrams, resultant forces, moments and the principle of moments, levers and gears, and lubrication. "
        "<b>The tricky bits</b> are where the marks go missing: scale drawings and resolving, equilibrium, explaining motion, moments with a twist, levers as force multipliers, and the hand-winch 6-marker on gears, force and work. "
        "Sections marked <b>P</b> are Physics only (not Combined Science); <b>H</b> is Higher tier only."
    ),
    "howto": [
        "Start with the non-negotiables. Do not move on from a section until every practice question is green.",
        "Draw every free body diagram and scale drawing yourself on paper — ruler, protractor, stated scale — before you look at the one on the page.",
        "Read each explanation, then cover it and say it back. For a definition, the bold words are the ones the mark is for.",
        "Do the practice questions <b>before</b> opening the hint or walkthrough. Calculations in EWAU layout on paper first, then type the answer to check it.",
        "For \"explain\" and \"describe how\" questions, write your answer in full sentences, then compare it with the model answer line by line.",
        "Fill in the traffic-light self-check at the end of each section. Anything red or amber is what to revise next.",
    ],
    "bands": [
        {
            "id": "nn",
            "prefix": "N",
            "title": "The non-negotiables",
            "blurb": "Forces and fields, interaction pairs, vectors, free body diagrams, resultants, moments, the principle of moments, levers, gears and lubrication, with the two calculations. If any of these is not yet green, it comes before anything in the second band.",
        },
        {
            "id": "tricky",
            "prefix": "T",
            "title": "The tricky bits",
            "blurb": "Scale drawings, resolving, the closed triangle, explaining motion, moments with angles and beam weights, levers and work, and the winch question where the equation has to be written in the parts of the machine. Each one is built on something from the first band.",
        },
    ],
    "factsBlurb": "Topic 9 on flip cards: the force types, the pair rules, vectors and scalars, the free-body rules, the moments and gears facts, the examiner phrases, and the winch equations in the parts of the machine. Cover, say the answer out loud, then flip to check.",
}


def embed_types(section):
    """Insert a `types` part after the section's worked example."""
    ids = EMBEDS.get(section["id"])
    if not ids:
        return
    part = types(ids, "Calculation practice")
    parts = section["parts"]
    insert_at = len(parts)
    for index, existing in enumerate(parts):
        if existing["kind"] == "practice":
            insert_at = index
            break
    for index, existing in enumerate(parts):
        if existing["kind"] == "worked":
            insert_at = index + 1
    parts.insert(insert_at, part)


def main():
    with open(TOPIC_PATH, encoding="utf-8") as handle:
        topic = json.load(handle)

    sections = copy.deepcopy(fe_nn.SECTIONS + fe_tricky.SECTIONS)
    facts = copy.deepcopy(fe_tricky.FACTS) + copy.deepcopy(fe_nn.FACTS_KW)

    for section in sections:
        embed_types(section)


    rebuilt = {}
    for key in ("id", "title", "subtitle", "spec", "order", "figure"):
        if key in topic:
            rebuilt[key] = topic[key]
    for key, value in REVISION.items():
        rebuilt[key] = value
    rebuilt["sections"] = sections
    rebuilt["facts"] = facts
    for key, value in topic.items():
        if key not in rebuilt and key not in REVISION and key != "placeholder":
            rebuilt[key] = value

    with open(TOPIC_PATH, "w", encoding="utf-8") as handle:
        json.dump(rebuilt, handle, ensure_ascii=False, indent=2)
        handle.write("\n")

    problems = validate_file(TOPIC_PATH)
    if problems:
        for problem in problems:
            print("PROBLEM:", problem)
        sys.exit(1)

    questions = 0
    for section in sections:
        for part in section["parts"]:
            if part["kind"] == "practice":
                for question in part["questions"]:
                    questions += len(question["parts"]) if question["type"] == "group" else 1
    print(
        "wrote", os.path.normpath(TOPIC_PATH), "-",
        len(sections), "sections,", questions, "section questions,",
        len(facts), "facts,", len(rebuilt["types"]), "types",
    )


if __name__ == "__main__":
    main()
