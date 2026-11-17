#!/usr/bin/env python3
"""
build_radioactivity.py — write the revision content of Topic 6 into
data/radioactivity.json, keeping its six calculation types as they are.

Content modules:

    ra_diagrams.py   Penetration, Rutherford scattering, chain reaction (SVG)
    ra_nn_a.py       The non-negotiables N1–N5
    ra_nn_b.py       The non-negotiables N6–N10 (N10 = key words)
    ra_tricky.py     The tricky bits T1–T9 and the flashcards

Nothing in Topic 6 is Higher-only; 6.33P–6.46P are Physics-only, so T5–T9
carry the P tag. The six types are embedded per EMBEDS.

Run from the gcse-non-negotiables folder:

    python3 tools/build_radioactivity.py
    python3 tools/build_manifest.py
"""

import copy
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import ra_nn_a  # noqa: E402
import ra_nn_b  # noqa: E402
import ra_tricky  # noqa: E402
from revlib import types  # noqa: E402
from validate import validate_file  # noqa: E402

TOPIC_PATH = os.path.join(HERE, "..", "data", "radioactivity.json")

# Which calculation types each section embeds (after its worked example)
EMBEDS = {
    "isotopes": ["nuclear-notation"],
    "background": ["background-count"],
    "decays": ["nuclear-equations"],
    "half-life-nn": ["half-life-fraction", "half-life-time", "decay-graph"],
}

REVISION = {
    "lede": (
        "Everything in Topic 6, split into two bands. <b>The non-negotiables</b> are the atom, the three radiations, decay equations, half-life, the dangers and the uses — the facts and one-step calculations you must have at your fingertips. "
        "<b>The tricky bits</b> are where the marks go missing: the history of the atomic model, choosing a source with reasons, half-life with a background, the explain questions, and (for Physics) tumours, PET, fission and fusion. "
        "Sections marked <b>P</b> are Physics only (not Combined Science); nothing in this topic is Higher-only."
    ),
    "howto": [
        "Start with the non-negotiables. Do not move on from a section until every practice question is green.",
        "Learn the definitions as sentences — the bold words are the ones the mark is for.",
        "For every decay, say what happens to the mass number and the atomic number; then every equation balances itself.",
        "Do the practice questions <b>before</b> opening the hint or walkthrough. Half-life calculations: write each halving on its own line.",
        "For \"explain\" questions, write your answer in full sentences, then compare it with the model answer line by line.",
        "Fill in the traffic-light self-check at the end of each section. Anything red or amber is what to revise next.",
    ],
    "bands": [
        {
            "id": "nn",
            "prefix": "N",
            "title": "The non-negotiables",
            "blurb": "The atom, isotopes, the radiations, decay equations, half-life, dangers and uses. If any of these is not yet green, it comes before anything in the second band.",
        },
        {
            "id": "tricky",
            "prefix": "T",
            "title": "The tricky bits",
            "blurb": "The atomic model, choosing a source, half-life with a background, the explain questions, and the Physics-only nuclear content. Each one is built on something from the first band.",
        },
    ],
    "factsBlurb": "Topic 6 on flip cards: every definition, the radiations, every decay's effect on A and Z, the uses with reasons, the dangers, Rutherford's conclusions, the reactor and fusion. Cover, say the answer out loud, then flip to check.",
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

    sections = copy.deepcopy(ra_nn_a.SECTIONS + ra_nn_b.SECTIONS + ra_tricky.SECTIONS)
    facts = copy.deepcopy(ra_tricky.FACTS) + copy.deepcopy(ra_nn_b.FACTS_KW)

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
