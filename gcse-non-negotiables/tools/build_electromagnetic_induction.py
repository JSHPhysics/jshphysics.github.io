#!/usr/bin/env python3
"""
build_electromagnetic_induction.py — write the revision content of
Topic 13 into data/electromagnetic-induction.json, keeping the three
existing calculation types and embedding them: turns in N6, tx-power in
N8, loss in N9. tx-power loses its Higher badge, because 13.10 is a
both-tier statement (author-approved 2026-11-19).

Content modules:

    ei_diagrams.py   The seven diagrams (SVG)
    ei_nn.py         The non-negotiables N1–N10 (N10 = key words)
    ei_tricky.py     The tricky bits T1–T8 and the flashcards

Tiers from the Pearson spec: 13.1P, 13.2, 13.3P, 13.5, 13.6, 13.7P and
13.11P Higher only; 13.4P, 13.8, 13.9 and 13.10 both tiers; the P
statements Physics only.

Run from the gcse-non-negotiables folder:

    python3 tools/build_electromagnetic_induction.py
    python3 tools/build_manifest.py
"""

import copy
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import ei_nn  # noqa: E402
import ei_tricky  # noqa: E402
from revlib import types  # noqa: E402
from validate import validate_file  # noqa: E402

TOPIC_PATH = os.path.join(HERE, "..", "data", "electromagnetic-induction.json")

# Which calculation types each section embeds (after its worked example)
EMBEDS = {"turns-ratio": ["turns"], "transformer-power": ["tx-power"], "transmission-loss": ["loss"]}

REVISION = {
    "lede": (
        "Everything in Topic 13, split into two bands. <b>The non-negotiables</b> are inducing a pd, what sets its size and direction, the alternator and dynamo, the loudspeaker and microphone, the transformer and its two equations, and the national grid with the reason for high voltage. "
        "<b>The tricky bits</b> are the chains the marks are on: the induction chain for a falling magnet, why a dynamo gets harder to turn, generator output graphs, the microphone-versus-loudspeaker and transformer 6-markers, transformer calculations with both equations, the grid as a chain, and the falling-magnet practical. "
        "Most of the topic is <b>Higher only</b>, badged <b>H</b>; the loudspeaker and microphone, the national grid and the pd–current equation are both tiers; the P statements are Physics only."
    ),
    "howto": [
        "Start with the non-negotiables. Do not move on from a section until every practice question is green.",
        "Say every explanation out loud as a chain — moves through the field, changing field, pd induced, current if the circuit is closed — before you read the one on the page.",
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
            "blurb": "Inducing a pd and its size and direction, the alternator and dynamo, the loudspeaker and microphone, the transformer with its two equations, and the national grid. If any of these is not yet green, it comes before anything in the second band.",
        },
        {
            "id": "tricky",
            "prefix": "T",
            "title": "The tricky bits",
            "blurb": "The explanations marked on particular words: the falling magnet, the dynamo that gets harder to turn, output graphs, the two 6-markers, transformer calculations with both equations, the grid chain, the practical. Each one is built on something from the first band.",
        },
    ],
    "factsBlurb": "Topic 13 on flip cards: the induction chain and its lead line, the size and direction rules, slip rings versus the split ring, the speaker and microphone chains, the transformer in three marks, the two transformer equations and the grid chain. Cover, say the answer out loud, then flip to check.",
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

    sections = copy.deepcopy(ei_nn.SECTIONS + ei_tricky.SECTIONS)
    facts = copy.deepcopy(ei_tricky.FACTS) + copy.deepcopy(ei_nn.FACTS_KW)

    # 13.10 is a both-tier statement: the pd-current type is not Higher only
    for calc_type in topic["types"]:
        if calc_type["id"] == "tx-power":
            calc_type["boards"] = ["Foundation", "Higher"]

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
