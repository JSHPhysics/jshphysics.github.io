#!/usr/bin/env python3
"""
build_static_electricity.py — write the revision content of Topic 11 into
data/static-electricity.json. The topic has no calculation types (it is
an explain topic) and none are added.

Content modules:

    se_diagrams.py   The seven diagrams (SVG)
    se_nn.py         The non-negotiables N1–N8 (N8 = key words)
    se_tricky.py     The tricky bits T1–T7 and the flashcards

The whole topic is Physics-only (11.1P–11.10P) and has no Higher-only
statements, so every section carries the P tag and none the H tag.

Run from the gcse-non-negotiables folder:

    python3 tools/build_static_electricity.py
    python3 tools/build_manifest.py
"""

import copy
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import se_nn  # noqa: E402
import se_tricky  # noqa: E402
from revlib import types  # noqa: E402
from validate import validate_file  # noqa: E402

TOPIC_PATH = os.path.join(HERE, "..", "data", "static-electricity.json")

# Which calculation types each section embeds (after its worked example)
EMBEDS = {}

REVISION = {
    "lede": (
        "Everything in Topic 11, split into two bands. <b>The non-negotiables</b> are charging by friction, the force rule, the three phenomena, earthing, sprayers, the fuelling danger and electric fields. "
        "<b>The tricky bits</b> are the chains the marks are on: electrons and force → acceleration, induction, sparks, the fuelling 6-marker, sprayer advantages with reasons, drawing fields and explaining with them. "
        "The whole of Topic 11 is Physics only (not Combined Science), so every section carries <b>P</b>; there is no Higher-only content, so it all applies at both tiers."
    ),
    "howto": [
        "Start with the non-negotiables. Do not move on from a section until every practice question is green.",
        "Say every explanation out loud as a chain — friction, electrons, which way, what charge; or like charges, repel, force, direction, accelerates — before you read the one on the page.",
        "Read each explanation, then cover it and say it back. For a definition, the bold words are the ones the mark is for.",
        "Do the practice questions <b>before</b> opening the hint or walkthrough. Write the explanation chains out in full on paper before opening the model answer — the marks are on the links, not the conclusion.",
        "For \"explain\" and \"describe how\" questions, write your answer in full sentences, then compare it with the model answer line by line.",
        "Fill in the traffic-light self-check at the end of each section. Anything red or amber is what to revise next.",
    ],
    "bands": [
        {
            "id": "nn",
            "prefix": "N",
            "title": "The non-negotiables",
            "blurb": "Charging by friction, the force rule, shocks and lightning and induction, earthing, sprayers, the fuelling danger, and electric fields. If any of these is not yet green, it comes before anything in the second band.",
        },
        {
            "id": "tricky",
            "prefix": "T",
            "title": "The tricky bits",
            "blurb": "The explanations marked on particular words: the electron chain and the force → acceleration chain, induction, sparks, the fuelling question, sprayers with reasons, drawing fields and explaining with them. Each one is built on something from the first band.",
        },
    ],
    "factsBlurb": "Topic 11 on flip cards: the charging chain, the force chain, induction in four steps, the spark chain, both halves of the fuelling question, the sprayer pairs and the field rules. Cover, say the answer out loud, then flip to check.",
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

    sections = copy.deepcopy(se_nn.SECTIONS + se_tricky.SECTIONS)
    facts = copy.deepcopy(se_tricky.FACTS) + copy.deepcopy(se_nn.FACTS_KW)

    for section in sections:
        embed_types(section)

    # An explain topic: no calculation types
    topic["types"] = []

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
