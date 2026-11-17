#!/usr/bin/env python3
"""
build_waves.py — write the revision content of Topic 4 into
data/waves.json, keeping its five calculation types as they are.

Content modules:

    wv_diagrams.py   The transverse and longitudinal wave drawings (SVG)
    wv_nn.py         The non-negotiables N1–N9 (N9 = key words)
    wv_tricky.py     The tricky bits T1–T7 and the flashcards

Higher-only and Physics-only (4.8P, 4.12P–4.15P are both) carry the H and
P tags: N8, T4, T5. The five types are embedded per EMBEDS.

Run from the gcse-non-negotiables folder:

    python3 tools/build_waves.py
    python3 tools/build_manifest.py
"""

import copy
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import wv_nn  # noqa: E402
import wv_tricky  # noqa: E402
from revlib import types  # noqa: E402
from validate import validate_file  # noqa: E402

TOPIC_PATH = os.path.join(HERE, "..", "data", "waves.json")

# Which calculation types each section embeds (after its worked example)
EMBEDS = {
    "wave-equations": ["wave-speed-frequency", "wave-speed-distance"],
    "period-nn": ["period-frequency"],
    "wave-graphs-hard": ["wave-graph"],
    "echo-distances": ["echoes"],
}

REVISION = {
    "lede": (
        "Everything in Topic 4, split into two bands. <b>The non-negotiables</b> are the definitions, the two wave equations, the two kinds of wave and the measuring methods you must have at your fingertips. "
        "<b>The tricky bits</b> are where the marks go missing: reading the right thing off a graph, the explanation phrases, echo distances, seismic conclusions and the core practical. "
        "Sections marked <b>H</b> are Higher tier only; <b>P</b> is Physics only (not Combined Science)."
    ),
    "howto": [
        "Start with the non-negotiables. Do not move on from a section until every practice question is green.",
        "Learn the definitions as sentences — the bold words are the ones the mark is for.",
        "Do the practice questions <b>before</b> opening the hint or walkthrough. Calculations in EWAU layout on paper first, then type the answer to check it.",
        "For \"explain\" and \"describe how\" questions, write your answer in full sentences, then compare it with the model answer line by line.",
        "Fill in the traffic-light self-check at the end of each section. Anything red or amber is what to revise next.",
    ],
    "bands": [
        {
            "id": "nn",
            "prefix": "N",
            "title": "The non-negotiables",
            "blurb": "Definitions, the two equations, transverse and longitudinal, measuring methods and the ear. If any of these is not yet green, it comes before anything in the second band.",
        },
        {
            "id": "tricky",
            "prefix": "T",
            "title": "The tricky bits",
            "blurb": "Graphs with the wrong axis, explanation phrases, refraction of waves, echo distances, seismic waves and the core practical. Each one is built on something from the first band.",
        },
    ],
    "factsBlurb": "Topic 4 on flip cards: every definition, the equations, the methods and the standard explanations. Cover, say the answer out loud, then flip to check.",
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

    sections = copy.deepcopy(wv_nn.SECTIONS + wv_tricky.SECTIONS)
    facts = copy.deepcopy(wv_tricky.FACTS) + copy.deepcopy(wv_nn.FACTS_KW)

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
