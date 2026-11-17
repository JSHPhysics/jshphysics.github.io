#!/usr/bin/env python3
"""
build_astronomy.py — write the revision content of Topic 7 into
data/astronomy.json. The topic had no calculation types, so this script
also adds the one in as_types.py.

Content modules:

    as_diagrams.py   The orbit and life-cycle diagrams (SVG)
    as_types.py      Calculation type: weight-elsewhere
    as_nn.py         The non-negotiables N1–N9 (N9 = key words)
    as_tricky.py     The tricky bits T1–T7 and the flashcards

The whole topic is Physics-only (7.1P–7.19P) and has no Higher-only
statements, so every section carries the P tag and none the H tag. The
type is embedded in N2.

Run from the gcse-non-negotiables folder:

    python3 tools/build_astronomy.py
    python3 tools/build_manifest.py
"""

import copy
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import as_nn  # noqa: E402
import as_tricky  # noqa: E402
import as_types  # noqa: E402
from revlib import types  # noqa: E402
from validate import validate_file  # noqa: E402

TOPIC_PATH = os.path.join(HERE, "..", "data", "astronomy.json")

# Which calculation types each section embeds (after its worked example)
EMBEDS = {
    "weight-elsewhere-nn": ["weight-elsewhere"],
}

REVISION = {
    "lede": (
        "Everything in Topic 7, split into two bands. <b>The non-negotiables</b> are the Solar System, weight and g, the kinds of orbit, red-shift, the two theories of the Universe, the life cycles of stars and how we observe them. "
        "<b>The tricky bits</b> are where the marks go missing: the explanations that are marked on particular words — circular orbits, the red-shift chain, why the CMB decided it, how a star stays stable — and the telescope and weight questions. "
        "The whole of Topic 7 is Physics only (not Combined Science), so every section carries <b>P</b>; there is no Higher-only content, so it all applies at both tiers."
    ),
    "howto": [
        "Start with the non-negotiables. Do not move on from a section until every practice question is green.",
        "Draw the orbit diagram yourself — velocity along the orbit, gravity towards the centre — and say the life cycles of stars out loud in order, before you look at the ones on the page.",
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
            "blurb": "The Solar System, weight on other bodies, orbits, red-shift, Big Bang versus Steady State, the life cycles of stars, and how observing has changed. If any of these is not yet green, it comes before anything in the second band.",
        },
        {
            "id": "tricky",
            "prefix": "T",
            "title": "The tricky bits",
            "blurb": "The explanations marked on particular words: how the model of the Solar System changed, circular orbits, the red-shift chain, why the CMB decided it, the balance inside a star, telescopes in space, and weight the hard way. Each one is built on something from the first band.",
        },
    ],
    "factsBlurb": "Topic 7 on flip cards: the planets in order, the g values, the kinds of orbit, the red-shift chain, the two theories and their evidence, every stage of both life cycles, and the telescope arguments. Cover, say the answer out loud, then flip to check.",
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

    sections = copy.deepcopy(as_nn.SECTIONS + as_tricky.SECTIONS)
    facts = copy.deepcopy(as_tricky.FACTS) + copy.deepcopy(as_nn.FACTS_KW)

    for section in sections:
        embed_types(section)

    # The topic had no calculation types: add the one written for it
    topic["types"] = copy.deepcopy(as_types.TYPES)

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
