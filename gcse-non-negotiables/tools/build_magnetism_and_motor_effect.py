#!/usr/bin/env python3
"""
build_magnetism_and_motor_effect.py — write the revision content of
Topic 12 into data/magnetism-and-motor-effect.json, keeping the existing
calculation type (motor-force) and embedding it in N9.

Content modules:

    mg_diagrams.py   The eight diagrams (SVG)
    mg_nn.py         The non-negotiables N1–N10 (N10 = key words)
    mg_tricky.py     The tricky bits T1–T8 and the flashcards

Tiers from the Pearson spec: 12.1–12.9 both tiers; 12.10–12.14P Higher
only (N7, N8, N9, T5, T6, T7 carry H); 12.14P Physics only (T7 carries P).

Run from the gcse-non-negotiables folder:

    python3 tools/build_magnetism_and_motor_effect.py
    python3 tools/build_manifest.py
"""

import copy
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import mg_nn  # noqa: E402
import mg_tricky  # noqa: E402
from revlib import types  # noqa: E402
from validate import validate_file  # noqa: E402

TOPIC_PATH = os.path.join(HERE, "..", "data", "magnetism-and-motor-effect.json")

# Which calculation types each section embeds (after its worked example)
EMBEDS = {"motor-force-nn": ["motor-force"]}

REVISION = {
    "lede": (
        "Everything in Topic 12, split into two bands. <b>The non-negotiables</b> are poles and the test for a magnet, permanent and induced magnets, field lines, compasses and the Earth, the field around a wire and a solenoid, the motor effect, Fleming's left-hand rule and $F = BIl$. "
        "<b>The tricky bits</b> are the chains the marks are on: fields interact → force → accelerates, the magnet test with its expected result, drawing and marking field diagrams, the Earth's field, the left-hand rule on diagrams, $F = BIl$ the hard way, the d.c. motor and the electromagnet investigation. "
        "The motor effect (12.10 onwards) is <b>Higher only</b>, badged <b>H</b>; the motor itself (12.14P) is also Physics only, badged <b>P</b>."
    ),
    "howto": [
        "Start with the non-negotiables. Do not move on from a section until every practice question is green.",
        "Say every explanation out loud as a chain — current, field around the wire, the wire is in the magnets' field and the fields interact, resultant force, accelerates, left-hand rule — before you read the one on the page.",
        "Read each explanation, then cover it and say it back. For a definition, the bold words are the ones the mark is for.",
        "Do the practice questions <b>before</b> opening the hint or walkthrough. Calculations in EWAU layout on paper first, then type the answer to check it; write the explanation chains out in full before opening the model answer — the marks are on the links, not the conclusion.",
        "For \"explain\" and \"describe how\" questions, write your answer in full sentences, then compare it with the model answer line by line.",
        "Fill in the traffic-light self-check at the end of each section. Anything red or amber is what to revise next.",
    ],
    "bands": [
        {
            "id": "nn",
            "prefix": "N",
            "title": "The non-negotiables",
            "blurb": "Poles, permanent and induced magnets, field lines, compasses and the Earth, the wire and the solenoid, then the Higher-only motor effect, Fleming's left-hand rule and $F = BIl$. If any of these is not yet green, it comes before anything in the second band.",
        },
        {
            "id": "tricky",
            "prefix": "T",
            "title": "The tricky bits",
            "blurb": "The explanations marked on particular words: fields interact → force → accelerates, the magnet test, field diagrams, the Earth, the left-hand rule on diagrams, $F = BIl$ with a twist, the motor and its commutator, the electromagnet investigation. Each one is built on something from the first band.",
        },
    ],
    "factsBlurb": "Topic 12 on flip cards: the poles rule and the magnet test, the field shapes and their marks, the Earth, the wire and solenoid rules, the five-step and six-step motor-effect chains, Fleming's rule and the $F = BIl$ traps. Cover, say the answer out loud, then flip to check.",
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

    sections = copy.deepcopy(mg_nn.SECTIONS + mg_tricky.SECTIONS)
    facts = copy.deepcopy(mg_tricky.FACTS) + copy.deepcopy(mg_nn.FACTS_KW)

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
