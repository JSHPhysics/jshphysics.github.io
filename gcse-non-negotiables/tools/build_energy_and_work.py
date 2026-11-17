#!/usr/bin/env python3
"""
build_energy_and_work.py — write the revision content of Topics 3 and 8
into data/energy-and-work.json, keeping its calculation types as they are.

Content modules:

    en_nn_a.py       The non-negotiables N1–N6
    en_nn_b.py       The non-negotiables N7–N11
    en_keywords.py   Key words (N12) and their flashcards
    en_tricky_a.py   The tricky bits T1–T6
    en_tricky_b.py   The tricky bits T7–T11 and the flashcards

This page covers two specification topics, so it declares `subtopics`
(Topic 3, Topic 8) and every section carries `subtopic`; the app shows a
"Both · Topic 3 · Topic 8" picker. The seven calculation types are
embedded in the sections listed in EMBEDS. Nothing is Higher-only or
Physics-only in these topics (checked against the specification).

Run from the gcse-non-negotiables folder:

    python3 tools/build_energy_and_work.py
    python3 tools/build_manifest.py
"""

import copy
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import en_keywords  # noqa: E402
import en_nn_a  # noqa: E402
import en_nn_b  # noqa: E402
import en_tricky_a  # noqa: E402
import en_tricky_b  # noqa: E402
from revlib import types  # noqa: E402
from validate import validate_file  # noqa: E402

TOPIC_PATH = os.path.join(HERE, "..", "data", "energy-and-work.json")

# Which calculation types each section embeds (after its worked example)
EMBEDS = {
    "gpe": ["gravitational-potential-energy"],
    "ke": ["kinetic-energy"],
    "work": ["work-done"],
    "power-nn": ["power"],
    "efficiency-nn": ["efficiency"],
    "gpe-ke": ["energy-transfers"],
    "energy-graphs": ["energy-graph"],
}

REVISION = {
    "subtopics": [
        {"id": "3", "label": "Topic 3", "title": "Conservation of energy (Paper 1)"},
        {"id": "8", "label": "Topic 8", "title": "Energy — forces doing work (Paper 2)"},
    ],
    "lede": (
        "Topics 3 and 8 share most of their physics — stores, conservation, kinetic and gravitational potential energy, efficiency, dissipation — "
        "so they are on one page. Topic 3 (Paper 1) adds insulation and energy resources; Topic 8 (Paper 2) adds work done and power. "
        "Use the picker below to see one topic at a time. <b>The non-negotiables</b> are the definitions and single-step calculations that must be automatic; "
        "<b>the tricky bits</b> are the multi-step calculations and the explanations where the marks go missing."
    ),
    "howto": [
        "Choose <b>Both</b>, <b>Topic 3</b> or <b>Topic 8</b> under the heading. Sections shared by both topics show under either.",
        "Start with the non-negotiables. Do not move on from a section until every practice question is green.",
        "Read each explanation, then cover it and say it back. For an equation, write it out with every symbol labelled and its unit.",
        "Do the practice questions <b>before</b> opening the hint or walkthrough. Write every calculation in EWAU layout on paper first, then type the answer to check it.",
        "For \"explain\" and \"state what is meant by\" questions, write your answer in full sentences, then compare it with the model answer word by word — the bold words are the ones that score.",
        "Fill in the traffic-light self-check at the end of each section. Anything red or amber is what to revise next.",
    ],
    "bands": [
        {
            "id": "nn",
            "prefix": "N",
            "title": "The non-negotiables",
            "blurb": "The stores and pathways, the law of conservation, the five equations and the definitions. If any of these is not yet green, it comes before anything in the second band.",
        },
        {
            "id": "tricky",
            "prefix": "T",
            "title": "The tricky bits",
            "blurb": "Describing energy changes in the examiner's words, chaining equations, working backwards from an efficiency, and the explanations that are marked on particular phrases.",
        },
    ],
    "factsBlurb": "Topics 3 and 8 on flip cards: every store, pathway, equation, definition and standard explanation. Cover, say the answer out loud, then flip to check. The cards follow the Topic 3 / Topic 8 picker.",
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

    sections = copy.deepcopy(
        en_nn_a.SECTIONS + en_nn_b.SECTIONS + [en_keywords.section_keywords]
        + en_tricky_a.SECTIONS + en_tricky_b.SECTIONS
    )
    facts = copy.deepcopy(en_tricky_b.FACTS) + copy.deepcopy(en_keywords.FACTS)

    for section in sections:
        if "subtopic" not in section:
            raise SystemExit("section " + section["id"] + " has no subtopic")
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
    by_subtopic = {"3": 0, "8": 0}
    for section in sections:
        for name in section["subtopic"]:
            by_subtopic[name] += 1
    print(
        "wrote", os.path.normpath(TOPIC_PATH), "-",
        len(sections), "sections (Topic 3:", by_subtopic["3"], "/ Topic 8:", str(by_subtopic["8"]) + "),",
        questions, "section questions,", len(facts), "facts,", len(rebuilt["types"]), "types kept",
    )


if __name__ == "__main__":
    main()
