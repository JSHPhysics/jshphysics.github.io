#!/usr/bin/env python3
"""
build_mixed_questions.py — write the "Mixed-topic questions" page into
data/mixed-questions.json. The page has no calculation types: it is made
of the blends that the June 2023, 2024 and 2025 papers set, each one a
chain across two or three topics with the hand-over as the skill.

Content modules:

    mx_p1.py   The opening section (M1) and the Paper 1 blends (P1-1 … P1-6)
    mx_p2.py   The Paper 2 blends (P2-1 … P2-8) and the flashcards

Tiers follow the topics each stage comes from: the sections are untagged
so every student sees the page, and the parts that are Higher (momentum,
v² − u² = 2ax, scale drawings, the transformer chain) or Physics only
(pressure, upthrust, braking ∝ v², PET, the loudspeaker) carry their tag.
Thermal balance (5.22–5.23 / 7.x) and the pressure and upthrust sections
are tagged whole.

Run from the gcse-non-negotiables folder:

    python3 tools/build_mixed_questions.py
    python3 tools/build_manifest.py
"""

import copy
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import mx_p1  # noqa: E402
import mx_p2  # noqa: E402
from validate import validate_file  # noqa: E402

TOPIC_PATH = os.path.join(HERE, "..", "data", "mixed-questions.json")

TOPIC = {
    "id": "mixed-questions",
    "title": "Mixed-topic questions",
    "subtitle": "The blends the examiners set: two or three topics in one question, and the join between them",
    "spec": "All topics",
    "order": 160,
    "figure": "measurements",
    "lede": (
        "The long questions on both papers hand a quantity from one topic to the next — an energy, a force, a volume, a potential difference — and the marks sit at the hand-over. "
        "This page collects the blends that the June 2023, 2024 and 2025 papers set: <b>Paper 1</b> joins motion to energy, light to the wave equation, and radioactivity to energy and stars; <b>Paper 2</b> joins density to latent heat, pressure to forces and particles, springs to force diagrams, upthrust to moments, work to efficiency, electricity to energy and heat, and induction to the devices around it. "
        "Each section names the join, lays the chain out as a table, works one example modelled on the real question with new numbers, and practises the hand-over. The physics of every stage is on its topic page — this page is about carrying the number across. "
        "Parts that are Higher or Physics only carry their tag; the page itself is for everyone."
    ),
    "howto": [
        "Start with M1 and learn the four habits: find the join, match the units there, carry forward and label, check the number makes sense.",
        "Before each chain, say which quantity each stage hands to the next and what unit it must be in. Then do the arithmetic.",
        "Do every multi-part question in one go on paper, EWAU for each stage, before checking any part — in the exam the parts come together.",
        "For the written parts, write the chain in full sentences with the physics object as the subject, then compare with the model answer line by line.",
        "If a stage is red, go back to its topic page (the section is named in the chain table) before moving on.",
        "Fill in the traffic-light self-check at the end of each section. Anything red or amber is what to revise next.",
    ],
    "bands": [
        {
            "id": "start",
            "prefix": "M",
            "title": "Start here",
            "blurb": "How a blended question is built and marked, and the four habits that collect the marks at the joins.",
        },
        {
            "id": "p1",
            "prefix": "P1-",
            "title": "Paper 1 blends",
            "blurb": "Motion into energy (GPE → KE → speed, momentum beside kinetic energy, stopping distances as work), waves into light, and radioactivity into energy and stars.",
        },
        {
            "id": "p2",
            "prefix": "P2-",
            "title": "Paper 2 blends",
            "blurb": "Density into latent heat, pressure into forces and particles, springs into force diagrams, upthrust into moments, work into efficiency and power, electricity into energy, induction into its neighbouring devices, and electricity into heat.",
        },
    ],
    "factsBlurb": "The joins on flip cards: which quantity each chain hands over, the unit it must be in, and the one-line version of each blend. Cover, say the answer out loud, then flip to check.",
}


def main():
    sections = copy.deepcopy(mx_p1.SECTIONS_START + mx_p1.SECTIONS_P1 + mx_p2.SECTIONS_P2)
    facts = copy.deepcopy(mx_p2.FACTS)
    topic = dict(TOPIC)
    topic["sections"] = sections
    topic["facts"] = facts
    topic["types"] = []
    with open(TOPIC_PATH, "w", encoding="utf-8") as handle:
        json.dump(topic, handle, ensure_ascii=False, indent=2)
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
                    questions += 1 + len(question.get("parts", []))
    print("wrote", os.path.relpath(TOPIC_PATH, os.getcwd()), "-", len(sections), "sections,", questions, "section questions,", len(facts), "facts")


if __name__ == "__main__":
    main()
