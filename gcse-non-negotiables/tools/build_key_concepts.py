#!/usr/bin/env python3
"""
build_key_concepts.py — write the revision content of Topic 1 into
data/key-concepts.json, keeping its calculation types as they are.

The content lives in three modules next to this script:

    kc_nn.py       The non-negotiables N1–N9
    kc_tricky.py   The tricky bits T1–T8
    kc_facts.py    The flashcards

Run from the gcse-non-negotiables folder:

    python3 tools/build_key_concepts.py
    python3 tools/build_manifest.py

The calculation types (and their answers) are the JSON file's own; this
script only replaces the revision fields around them.
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import kc_facts  # noqa: E402
import kc_nn  # noqa: E402
import kc_tricky  # noqa: E402
from validate import validate_file  # noqa: E402

TOPIC_PATH = os.path.join(HERE, "..", "data", "key-concepts.json")

REVISION = {
    "lede": (
        "Topic 1 is short — units, prefixes, converting, significant figures, standard form — but it is the toolkit every "
        "other topic uses, so this page also carries the skills that are examined everywhere: the equation sheet, rearranging, "
        "proportion, EWAU, command words, graphs, and the practical-method questions."
    ),
    "howto": [
        "Start with the non-negotiables and do not move on from a section until its practice is green.",
        "Read each explanation, then cover it and say it back. For a table of units or prefixes, test yourself with the flashcards at the bottom.",
        "Study the worked example one step at a time and notice <i>how</i> the answer is laid out, not just what it is.",
        "Do the practice questions before opening the hint or walkthrough. Calculations on paper in EWAU, then type the answer to check it.",
        "For \"explain\" questions, write the answer in full sentences first, then compare it with the model answer point by point before you mark yourself.",
        "Fill in the self-check at the end of each section. Anything red or amber is what to revise next.",
    ],
    "bands": [
        {
            "id": "nn",
            "prefix": "N",
            "title": "The non-negotiables",
            "blurb": "Units, prefixes, conversions and the maths every calculation needs. These must be automatic: nothing in any other topic works without them.",
        },
        {
            "id": "tricky",
            "prefix": "T",
            "title": "The tricky bits",
            "blurb": "Working as a physicist: reading the question, command words, graphs, proportionality, planning and evaluating a practical, and estimating. These are the marks that are not about knowing any physics at all.",
        },
    ],
    "sections": kc_nn.SECTIONS + kc_tricky.SECTIONS,
    "facts": kc_facts.FACTS,
    "factsBlurb": "The whole topic on flip cards: every unit, every prefix, every command word. Cover, say the answer out loud, then flip to check.",
}


def main():
    with open(TOPIC_PATH, encoding="utf-8") as handle:
        topic = json.load(handle)

    # Rebuild the topic with the revision fields in a readable order,
    # keeping everything that is not ours exactly as it was
    rebuilt = {}
    for key in ("id", "title", "subtitle", "spec", "order", "figure"):
        if key in topic:
            rebuilt[key] = topic[key]
    for key, value in REVISION.items():
        rebuilt[key] = value
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

    # Summary
    questions = 0
    for section in rebuilt["sections"]:
        for part in section["parts"]:
            if part["kind"] == "practice":
                for question in part["questions"]:
                    questions += len(question["parts"]) if question["type"] == "group" else 1
    print(
        "wrote", os.path.normpath(TOPIC_PATH), "-",
        len(rebuilt["sections"]), "sections,", questions, "section questions,",
        len(rebuilt["facts"]), "facts,", len(rebuilt["types"]), "types kept",
    )


if __name__ == "__main__":
    main()
