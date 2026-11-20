#!/usr/bin/env python3
"""
build_forces_and_matter.py — write the revision content of Topic 15 into
data/forces-and-matter.json, keeping the five existing calculation types
and embedding them: hooke in N3, elastic in N4, fx-graph in N5, pressure
in N7, liquid in N11. No type changes its boards.

Content modules:

    fm_diagrams.py   The six diagrams (SVG)
    fm_nn.py         The non-negotiables N1–N13 (N13 = key words)
    fm_tricky.py     The tricky bits T1–T7 and the flashcards

Tiers from the Pearson spec: 15.1–15.6 both tiers and both sciences;
15.7P–15.17P Physics only; 15.14P (P = h rho g) is the only Higher-only
statement.

Run from the gcse-non-negotiables folder:

    python3 tools/build_forces_and_matter.py
    python3 tools/build_manifest.py
"""

import copy
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import fm_nn  # noqa: E402
import fm_tricky  # noqa: E402
from revlib import types  # noqa: E402
from validate import validate_file  # noqa: E402

TOPIC_PATH = os.path.join(HERE, "..", "data", "forces-and-matter.json")

# Which calculation types each section embeds (after its worked example)
EMBEDS = {
    "hooke-nn": ["hooke"],
    "energy-stored": ["elastic"],
    "linear-nonlinear": ["fx-graph"],
    "pressure-nn": ["pressure"],
    "liquid-pressure": ["liquid"],
}

REVISION = {
    "lede": (
        "Everything in Topic 15, split into two bands. <b>The non-negotiables</b> are why distorting needs two forces, elastic and inelastic distortion, Hooke's law and the energy stored, linear and non-linear graphs, the spring core practical, pressure as force per unit area, pressure in fluids and the atmosphere, pressure in liquids with depth and density, and upthrust with floating and sinking. "
        "<b>The tricky bits</b> are where the examiners' reports say the marks go: extension not length, reading force–extension graphs, the spring practical as a 6-mark method, pressure with awkward areas, the two pressure graphs, the four-stage upthrust chain and floating in the mark-scheme words. "
        "Springs (15.1–15.6) are <b>both tiers and both sciences</b>; everything about pressure and upthrust is Physics only, badged <b>P</b>, and the liquid-column equation is Higher Physics only, badged <b>H</b> and <b>P</b>."
    ),
    "howto": [
        "Start with the non-negotiables. Do not move on from a section until every practice question is green.",
        "Before any spring calculation write the extension down first — loaded length minus unloaded length, in metres — then pick the equation.",
        "Read each explanation, then cover it and say it back. For a definition, the bold words are the ones the mark is for.",
        "Do the practice questions <b>before</b> opening the hint or walkthrough. Calculations in EWAU layout on paper first, with areas in m² and extensions in m, then type the answer to check it; write the explanation chains out in full before opening the model answer — the marks are on the links, not the conclusion.",
        "For \"explain\" and \"describe how\" questions, write your answer in full sentences, then compare it with the model answer line by line.",
        "Fill in the traffic-light self-check at the end of each section. Anything red or amber is what to revise next.",
    ],
    "bands": [
        {
            "id": "nn",
            "prefix": "N",
            "title": "The non-negotiables",
            "blurb": "Two forces, elastic and inelastic, Hooke's law and the energy stored, the graph shapes, the spring practical, pressure on a surface and in fluids, the atmosphere, depth and density, the liquid-column equation, upthrust and floating. If any of these is not yet green, it comes before anything in the second band.",
        },
        {
            "id": "tricky",
            "prefix": "T",
            "title": "The tricky bits",
            "blurb": "The questions marked on particular steps and particular words: extension not length, the three readings from a force–extension graph, the 6-mark spring method, total areas and square millimetres, the two pressure graphs, the Archimedes chain and the second floating mark. Each one is built on something from the first band.",
        },
    ],
    "factsBlurb": "Topic 15 on flip cards: the definitions, the two spring equations and their units, extension versus length, the graph readings, the practical's accuracy points, the pressure examples and conversions, the three reasons pressure falls with height, depth and density, the liquid-column equation and its trap, upthrust and the floating condition. Cover, say the answer out loud, then flip to check.",
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

    sections = copy.deepcopy(fm_nn.SECTIONS + fm_tricky.SECTIONS)
    facts = copy.deepcopy(fm_tricky.FACTS) + copy.deepcopy(fm_nn.FACTS_KW)

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
