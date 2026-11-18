#!/usr/bin/env python3
"""
build_electricity_and_circuits.py — write the revision content of Topic 10
into data/electricity-and-circuits.json, keeping its seven calculation
types and embedding them in the sections they belong to.

Content modules:

    el_diagrams.py   The circuit diagrams, plug and a.c./d.c. traces (SVG)
    el_nn_a.py       The non-negotiables N1–N6
    el_nn_b.py       The non-negotiables N7–N12 (N12 = key words)
    el_tricky.py     The tricky bits T1–T9 and the flashcards

The whole topic is in Combined Science at both tiers: no section carries
H or P.

Run from the gcse-non-negotiables folder:

    python3 tools/build_electricity_and_circuits.py
    python3 tools/build_manifest.py
"""

import copy
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import el_nn_a  # noqa: E402
import el_nn_b  # noqa: E402
import el_tricky  # noqa: E402
from revlib import types  # noqa: E402
from validate import validate_file  # noqa: E402

TOPIC_PATH = os.path.join(HERE, "..", "data", "electricity-and-circuits.json")

# Which calculation types each section embeds (after its worked example)
EMBEDS = {
    "charge-nn": ["charge"],
    "pd-energy": ["eqv"],
    "ohm-nn": ["ohm"],
    "circuits-nn": ["circuits"],
    "iv-characteristics": ["iv-graph"],
    "power-nn": ["electrical-power", "ept"],
}

REVISION = {
    "lede": (
        "Everything in Topic 10, split into two bands. <b>The non-negotiables</b> are charge and current, the symbols and meters, the seven equations, the series and parallel rules, the three I–V graphs, LDRs and thermistors, the heating effect, power, and the mains. "
        "<b>The tricky bits</b> are where the marks go missing: the two core practicals, explaining the curves, two-step circuit calculations, sensing circuits, power ratings and fuses, the safety chains, and the electron model behind it all. "
        "The whole of Topic 10 is in Combined Science at both tiers, so nothing here carries an H or P badge."
    ),
    "howto": [
        "Start with the non-negotiables. Do not move on from a section until every practice question is green.",
        "Draw every circuit yourself with a ruler — ammeter in series, voltmeter across — before you look at the one on the page.",
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
            "blurb": "Charge, current, pd, resistance, series and parallel, the I–V graphs, LDRs and thermistors, heating, power and the mains, with the seven calculations. If any of these is not yet green, it comes before anything in the second band.",
        },
        {
            "id": "tricky",
            "prefix": "T",
            "title": "The tricky bits",
            "blurb": "The core practicals, the curves explained, circuits in two steps, sensing circuits, ratings and fuses, the safety chains, the electron model and the seven-step plans. Each one is built on something from the first band.",
        },
    ],
    "factsBlurb": "Topic 10 on flip cards: the definitions, the equations and when to use each, the series and parallel rules, the three graphs, the mains numbers, the safety chains word for word. Cover, say the answer out loud, then flip to check.",
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

    sections = copy.deepcopy(el_nn_a.SECTIONS + el_nn_b.SECTIONS + el_tricky.SECTIONS)
    facts = copy.deepcopy(el_tricky.FACTS) + copy.deepcopy(el_nn_b.FACTS_KW)

    for section in sections:
        embed_types(section)

    # Two of the circuits type's questions were badged Higher when the
    # types were first written; 10.14 and 10.15 are at both tiers.
    for calc_type in topic["types"]:
        if calc_type["id"] == "circuits":
            for question in calc_type["practice"]:
                question.pop("boards", None)


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
