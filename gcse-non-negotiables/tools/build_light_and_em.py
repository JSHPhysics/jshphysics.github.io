#!/usr/bin/env python3
"""
build_light_and_em.py — write the revision content of Topic 5 into
data/light-and-em.json. The topic had no calculation types, so this script
also adds the two in le_types.py.

Content modules:

    le_diagrams.py   The ray diagrams (SVG)
    le_types.py      Calculation types: em-wave-speed, lens-power
    le_nn_a.py       The non-negotiables N1–N6
    le_nn_b.py       The non-negotiables N7–N11 (N11 = key words)
    le_tricky.py     The tricky bits T1–T10 and the flashcards

Physics-only sections carry the P tag and Higher-only ones the H tag
(5.1P–5.6P, 5.15P–5.19P; 5.13, 5.16P–5.18P, 5.23 — the last at question
level). The two types are embedded in N5 and N6.

Run from the gcse-non-negotiables folder:

    python3 tools/build_light_and_em.py
    python3 tools/build_manifest.py
"""

import copy
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import le_nn_a  # noqa: E402
import le_nn_b  # noqa: E402
import le_tricky  # noqa: E402
import le_types  # noqa: E402
from revlib import types  # noqa: E402
from validate import validate_file  # noqa: E402

TOPIC_PATH = os.path.join(HERE, "..", "data", "light-and-em.json")

# Which calculation types each section embeds (after its worked example)
EMBEDS = {
    "lenses": ["lens-power"],
    "em-waves": ["em-wave-speed"],
}

REVISION = {
    "lede": (
        "Everything in Topic 5, split into two bands. <b>The non-negotiables</b> are the ray diagrams, the definitions, the order of the spectrum and the uses and dangers you must have at your fingertips. "
        "<b>The tricky bits</b> are where the marks go missing: the practical methods, the explanations in the examiner's words, lens images, and the radiation questions. "
        "Sections marked <b>P</b> are Physics only (not Combined Science); <b>H</b> is Higher tier only."
    ),
    "howto": [
        "Start with the non-negotiables. Do not move on from a section until every practice question is green.",
        "Draw every ray diagram yourself on paper — normal first, angles from the normal, arrows on the rays — before you look at the one on the page.",
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
            "blurb": "Ray diagrams, definitions, the spectrum, uses and dangers, and the two calculations. If any of these is not yet green, it comes before anything in the second band.",
        },
        {
            "id": "tricky",
            "prefix": "T",
            "title": "The tricky bits",
            "blurb": "Practical methods, explanations marked on particular words, lens images, thermal balance and the sources of radiation. Each one is built on something from the first band.",
        },
    ],
    "factsBlurb": "Topic 5 on flip cards: every definition, the spectrum both ways, the uses and dangers per region, the ray-diagram rules and the practical results. Cover, say the answer out loud, then flip to check.",
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

    sections = copy.deepcopy(le_nn_a.SECTIONS + le_nn_b.SECTIONS + le_tricky.SECTIONS)
    facts = copy.deepcopy(le_tricky.FACTS) + copy.deepcopy(le_nn_b.FACTS_KW)

    for section in sections:
        embed_types(section)

    # The topic had no calculation types: add the two written for it
    topic["types"] = copy.deepcopy(le_types.TYPES)

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
