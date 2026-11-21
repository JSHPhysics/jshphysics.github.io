#!/usr/bin/env python3
"""
build_mixed_questions.py — write the two "Mixed-topic questions" pages,
data/mixed-paper-1.json and data/mixed-paper-2.json. Each page opens
with "Finding the join" (M1) and then has one section per blend that the
June 2023, 2024 and 2025 papers set for that paper, each a chain across
two or three topics with the hand-over as the skill. Neither page has
calculation types.

Content modules:

    mx_p1.py   The opener (built per page with its own question ids) and
               the Paper 1 blends (P1-1 … P1-6)
    mx_p2.py   The Paper 2 blends (P2-1 … P2-8) and the flashcards for
               both pages (each page keeps the cards of its own sections)

Tiers follow the topics each stage comes from: a section is tagged when
its whole blend is Higher or Physics only (momentum, induction, thermal
balance H; stopping-by-energy, pressure, upthrust P), and the parts that
are Higher (v² − u² = 2ax, scale drawings, the transformer chain) or
Physics only (braking ∝ v², PET, the loudspeaker) carry their tag.

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

DATA = os.path.join(HERE, "..", "data")

TOPIC_P1 = {
    "id": "mixed-paper-1",
    "title": "Mixed-topic questions: Paper 1",
    "subtitle": "The blends the examiners set on Paper 1: two or three topics in one question, and the join between them",
    "spec": "Paper 1 · Topics 1–7",
    "order": 160,
    "figure": "measurements",
    "lede": (
        "The long questions on Paper 1 hand a quantity from one topic to the next — an energy, a speed, a frequency, a fraction read off a graph — and the marks sit at the hand-over. "
        "This page collects the blends that the June 2023, 2024 and 2025 Paper 1 questions set: motion into energy (GPE → KE → speed, momentum beside kinetic energy, stopping distances as work), the wave equation on light, and radioactivity into energy and stars. "
        "Each section names the join, lays the chain out as a table, works one example modelled on the real question with new numbers, and practises the hand-over. The physics of every stage is on its topic page — this page is about carrying the number across. "
        "Sections and parts that are Higher or Physics only carry their tag."
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
    ],
    "factsBlurb": "The Paper 1 joins on flip cards: which quantity each chain hands over, the unit it must be in, and the one-line version of each blend. Cover, say the answer out loud, then flip to check.",
}

TOPIC_P2 = {
    "id": "mixed-paper-2",
    "title": "Mixed-topic questions: Paper 2",
    "subtitle": "The blends the examiners set on Paper 2: two or three topics in one question, and the join between them",
    "spec": "Paper 2 · Topics 8–15",
    "order": 161,
    "figure": "measurements",
    "lede": (
        "The long questions on Paper 2 hand a quantity from one topic to the next — an energy, a force, a volume, a potential difference — and the marks sit at the hand-over. "
        "This page collects the blends that the June 2023, 2024 and 2025 Paper 2 questions set: density into latent heat, pressure into forces and particles, springs into force diagrams, upthrust into moments, work into efficiency and power, electricity into energy and heat, and induction into the devices around it. "
        "Each section names the join, lays the chain out as a table, works one example modelled on the real question with new numbers, and practises the hand-over. The physics of every stage is on its topic page — this page is about carrying the number across. "
        "Sections and parts that are Higher or Physics only carry their tag."
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
            "id": "p2",
            "prefix": "P2-",
            "title": "Paper 2 blends",
            "blurb": "Density into latent heat, pressure into forces and particles, springs into force diagrams, upthrust into moments, work into efficiency and power, electricity into energy, induction into its neighbouring devices, and electricity into heat.",
        },
    ],
    "factsBlurb": "The Paper 2 joins on flip cards: which quantity each chain hands over, the unit it must be in, and the one-line version of each blend. Cover, say the answer out loud, then flip to check.",
}


def write_page(topic_spec, sections, facts):
    """Write one page's topic file and validate it."""
    path = os.path.join(DATA, topic_spec["id"] + ".json")
    topic = dict(topic_spec)
    topic["sections"] = copy.deepcopy(sections)
    topic["facts"] = copy.deepcopy(facts)
    topic["types"] = []
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(topic, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    problems = validate_file(path)
    if problems:
        for problem in problems:
            print("PROBLEM:", problem)
        sys.exit(1)
    questions = 0
    for section in topic["sections"]:
        for part in section["parts"]:
            if part["kind"] == "practice":
                for question in part["questions"]:
                    questions += 1 + len(question.get("parts", []))
    print("wrote", os.path.relpath(path, os.getcwd()), "-", len(topic["sections"]), "sections,", questions, "section questions,", len(topic["facts"]), "facts")


def facts_for(sections):
    """The flashcards whose section is on this page."""
    ids = set(section["id"] for section in sections)
    return [fact for fact in mx_p2.FACTS if fact["section"] in ids]


def main():
    page_one = mx_p1.SECTIONS_START + mx_p1.SECTIONS_P1
    page_two = mx_p1.SECTIONS_START_P2 + mx_p2.SECTIONS_P2
    write_page(TOPIC_P1, page_one, facts_for(page_one))
    write_page(TOPIC_P2, page_two, facts_for(page_two))


if __name__ == "__main__":
    main()
