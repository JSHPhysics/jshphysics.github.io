#!/usr/bin/env python3
"""
build_particle_model.py — write the revision content of Topic 14 into
data/particle-model.json, keeping the seven existing calculation types
and embedding them: density in N2, shc / latent / change-of-state in N7,
temperature in N10, boyle in N11, heating-graph in T4. boyle loses its
Higher badge, because 14.19P is a both-tier statement (author-approved
2026-11-19).

Content modules:

    pm_diagrams.py   The six diagrams (SVG)
    pm_nn.py         The non-negotiables N1–N12 (N12 = key words)
    pm_tricky.py     The tricky bits T1–T8 and the flashcards

Tiers from the Pearson spec: only 14.20P (doing work on a gas) is Higher
only; 14.16P–14.20P are Physics only; everything else is both tiers.

Run from the gcse-non-negotiables folder:

    python3 tools/build_particle_model.py
    python3 tools/build_manifest.py
"""

import copy
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import pm_nn  # noqa: E402
import pm_tricky  # noqa: E402
from revlib import types  # noqa: E402
from validate import validate_file  # noqa: E402

TOPIC_PATH = os.path.join(HERE, "..", "data", "particle-model.json")

# Which calculation types each section embeds (after its worked example)
EMBEDS = {
    "density-nn": ["density"],
    "thermal-equations": ["shc", "latent", "change-of-state"],
    "kelvin-nn": ["temperature"],
    "compressing-gas": ["boyle"],
    "heating-cooling-graphs": ["heating-graph"],
}

REVISION = {
    "lede": (
        "Everything in Topic 14, split into two bands. <b>The non-negotiables</b> are the three states and how their particles move, density and its core practical, why solids are denser than gases, changes of state, the two thermal quantities and their equations, insulation, gas pressure from collisions, absolute zero and the kelvin scale, and compressing a gas. "
        "<b>The tricky bits</b> are where the examiners' reports say the marks go: particle-motion answers that score, density with awkward units and scale readings, the density and specific-heat-capacity 6-mark methods, heating and cooling graphs, specific heat capacity against latent heat, explaining gas pressure link by link, and the kelvin traps. "
        "Nearly all of the topic is <b>both tiers</b>; compressing a gas and the force it exerts are Physics only, badged <b>P</b>, and doing work on a gas is Higher Physics only, badged <b>H</b> and <b>P</b>."
    ),
    "howto": [
        "Start with the non-negotiables. Do not move on from a section until every practice question is green.",
        "Say every particle explanation out loud with the particles as the subject — the particles move faster, hit the walls more often and harder — before you read the one on the page.",
        "Read each explanation, then cover it and say it back. For a definition, the bold words are the ones the mark is for.",
        "Do the practice questions <b>before</b> opening the hint or walkthrough. Calculations in EWAU layout on paper first, in SI units, then type the answer to check it; write the explanation chains out in full before opening the model answer — the marks are on the links, not the conclusion.",
        "For \"explain\" and \"describe how\" questions, write your answer in full sentences, then compare it with the model answer line by line.",
        "Fill in the traffic-light self-check at the end of each section. Anything red or amber is what to revise next.",
    ],
    "bands": [
        {
            "id": "nn",
            "prefix": "N",
            "title": "The non-negotiables",
            "blurb": "The three states, density and its practical, changes of state, specific heat capacity and latent heat with their equations, insulation, gas pressure, absolute zero and kelvin, and compressing a gas. If any of these is not yet green, it comes before anything in the second band.",
        },
        {
            "id": "tricky",
            "prefix": "T",
            "title": "The tricky bits",
            "blurb": "The questions marked on particular words and particular steps: particle motion, density the hard way, the two 6-mark methods, heating and cooling graphs, the shortfall in a temperature rise, the gas-pressure chains and the kelvin traps. Each one is built on something from the first band.",
        },
    ],
    "factsBlurb": "Topic 14 on flip cards: the movement phrase for each state, the density routes and their traps, the two thermal definitions and equations, the collision chains for temperature and for volume, absolute zero and the conversions. Cover, say the answer out loud, then flip to check.",
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

    sections = copy.deepcopy(pm_nn.SECTIONS + pm_tricky.SECTIONS)
    facts = copy.deepcopy(pm_tricky.FACTS) + copy.deepcopy(pm_nn.FACTS_KW)

    # 14.19P is a both-tier statement: the Boyle's-law type is not Higher only
    for calc_type in topic["types"]:
        if calc_type["id"] == "boyle":
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
