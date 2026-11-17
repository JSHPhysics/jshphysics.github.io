#!/usr/bin/env python3
"""
build_motion_and_forces.py — write the revision content of Topic 2 into
data/motion-and-forces.json, keeping its calculation types as they are.

The content came from the LEH U4 Topic 2 page and lives in:

    mf_nn_a.py       The non-negotiables N1–N8
    mf_nn_b.py       The non-negotiables N9–N15
    mf_tricky_a.py   The tricky bits T1–T7
    mf_tricky_b.py   The tricky bits T8–T13 and the U4 flashcards
    mf_keywords.py   Key words section, the Newton's-third-law momentum
                     explanation, and extra flashcards
    mf_exam.py       Questions and notes added after checking the content
                     against the examiners' reports and mark schemes
                     (see motion-and-forces_notes.md)

This script adapts the U4 sections for this site: renames the sections
whose ids clash with calculation-type ids, embeds the thirteen types in
the sections they belong to, turns the generic practical-planning section
into "apply the seven steps" (the recipe lives in Topic 1), adds the
third-law explanation to T8, tags Higher-only and Physics-only sections,
and merges the flashcards. Nothing here is hidden: the whole topic shows.

Run from the gcse-non-negotiables folder:

    python3 tools/build_motion_and_forces.py
    python3 tools/build_manifest.py
"""

import copy
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import mf_exam  # noqa: E402
import mf_keywords  # noqa: E402
import mf_nn_a  # noqa: E402
import mf_nn_b  # noqa: E402
import mf_tricky_a  # noqa: E402
import mf_tricky_b  # noqa: E402
from revlib import explain, types  # noqa: E402
from validate import validate_file  # noqa: E402

TOPIC_PATH = os.path.join(HERE, "..", "data", "motion-and-forces.json")

# Section ids that clash with calculation-type ids get a suffix
RENAMES = {
    "speed": "speed-nn",
    "acceleration": "acceleration-nn",
    "momentum": "momentum-nn",
    "stopping-distance": "stopping-distance-nn",
}

# Which calculation types each section embeds (after its worked example)
EMBEDS = {
    "speed-nn": ["speed"],
    "acceleration-nn": ["acceleration"],
    "suvat": ["v2-u2"],
    "dt-graphs": ["dt-graph"],
    "vt-graphs": ["vt-graph"],
    "newton-first": ["resultant-force"],
    "f-ma": ["newtons-second-law", "force-graph"],
    "weight": ["weight-and-mass"],
    "momentum-nn": ["momentum"],
    "stopping-distance-nn": ["stopping-distance"],
    "conservation-momentum": ["conservation-of-momentum"],
    "force-momentum": ["force-from-momentum-change"],
}

# Tier and separate-science tags
TAGS = {
    "momentum-nn": ["H"],
    "conservation-momentum": ["H"],
    "force-momentum": ["H"],
    "circular-motion": ["H"],
    "inertial-mass": ["H"],
    "braking-v-squared": ["P"],
}

REVISION = {
    "lede": (
        "Everything in Topic 2, split into two bands. <b>The non-negotiables</b> are the definitions, facts and single-step calculations you must get right every time, "
        "without thinking. <b>The tricky bits</b> are where the marks are usually lost: multi-step calculations, explanations, and the ideas that look "
        "simple but have a trap in them. Each item is explained, shown in a worked example, then practised straight away."
    ),
    "howto": [
        "Start with the non-negotiables. Do not move on from a section until every practice question is green.",
        "Read each explanation, then cover it and say it back to yourself. For an equation, write it out with every symbol labelled.",
        "Study the worked example one step at a time and notice <i>how</i> the answer is laid out, not just what it is.",
        "Do the practice questions <b>before</b> opening the hint or walkthrough. Write every calculation in EWAU layout on paper first, then type the answer to check it.",
        "For \"explain\" and \"state what is meant by\" questions, write your answer on paper in full sentences, then compare it with the model answer word by word before you mark yourself.",
        "Fill in the traffic-light self-check at the end of each section. Anything red or amber is what to revise next — and what to ask about in class.",
    ],
    "bands": [
        {
            "id": "nn",
            "prefix": "N",
            "title": "The non-negotiables",
            "blurb": "Definitions, recall and single-step calculations that must be automatic. If any of these is not yet green, it comes before anything in the second band.",
        },
        {
            "id": "tricky",
            "prefix": "T",
            "title": "The tricky bits",
            "blurb": "Multi-step calculations, explanation marks and the misconceptions that cost marks every year. Each one is built on something from the first band.",
        },
    ],
    "factsBlurb": "The whole topic on flip cards: every definition, equation, typical value and graph rule. Cover, say the answer out loud, then flip to check.",
}


def rename_ids(sections, facts):
    """Apply RENAMES to section ids and to the facts that point at them."""
    for section in sections:
        if section["id"] in RENAMES:
            section["id"] = RENAMES[section["id"]]
    for item in facts:
        if item.get("section") in RENAMES:
            item["section"] = RENAMES[item["section"]]


def embed_types(section):
    """Insert a `types` part after the section's worked example (or before its
    first practice part when there is no worked example)."""
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


def adapt_planning(section):
    """The seven-step recipe lives in Topic 1; here it is applied to the
    trolley practical. Replace the generic explanation with a pointer."""
    section["title"] = "Apply the seven steps: the trolley practical"
    section["blurb"] = "The seven-step recipe for a \"describe how you would investigate\" question is in Topic 1. Here it is applied to this topic's core practical, with two 6-mark questions to write in full."
    section["checklist"] = [
        "Write a full 6-mark method for the force–mass–acceleration practical using the seven steps",
        "Say what is changed, what is measured and with what, and what is done with the results",
        "Give one accuracy detail, and say you will repeat and calculate a mean",
    ]
    pointer = explain(
        "The seven steps, in one line each",
        "<p>From <a href='#key-concepts/planning-practical'>Topic 1, T6</a>: (1) the two variables; (2) the formula that links them; (3) what you change and how, and what you keep the same; "
        "(4) what you measure, how, and with what equipment; (5) what you do with the results — a calculation or a graph; (6) one detail that makes the results accurate; "
        "(7) repeat the readings <b>and calculate a mean</b>. One mark each; the question is out of six, so any six of the seven score.</p>"
        "<p>For this practical the equipment is the trolley on a runway, a string over a pulley to a mass hanger, a card and two light gates with a data logger. The worked example below shows the recipe applied to force and acceleration; the questions use the same kit for mass, and for a ramp.</p>",
    )
    # Drop the generic seven-step explanation; keep the "where marks go missing" box
    section["parts"] = [pointer] + [part for part in section["parts"] if not (part["kind"] == "explain" and part["title"] == "Seven steps, every time")]


def adapt_conservation(section):
    """Add the Newton's-third-law explanation, worked answer and questions."""
    parts = section["parts"]
    # After the existing worked example, before the practice
    practice_index = next(index for index, part in enumerate(parts) if part["kind"] == "practice")
    parts.insert(practice_index, mf_keywords.explain_n3_momentum)
    parts.insert(practice_index + 1, mf_keywords.worked_n3_momentum)
    parts[practice_index + 2]["questions"].extend(mf_keywords.practice_n3_momentum)
    section["checklist"].append("Explain, using Newton's third law, why momentum is conserved in a collision or explosion (four steps)")


def add_exam_findings(section):
    """Append the questions and explanations from mf_exam.ADDITIONS."""
    addition = mf_exam.ADDITIONS.get(section["id"])
    if not addition:
        return
    questions, explains = addition
    parts = section["parts"]
    if questions:
        practice_part = next(part for part in parts if part["kind"] == "practice")
        practice_part["questions"].extend(copy.deepcopy(questions))
    if explains:
        last_explain = max(index for index, part in enumerate(parts) if part["kind"] == "explain")
        for offset, part in enumerate(explains):
            parts.insert(last_explain + 1 + offset, copy.deepcopy(part))


def main():
    with open(TOPIC_PATH, encoding="utf-8") as handle:
        topic = json.load(handle)

    sections = copy.deepcopy(
        mf_nn_a.SECTIONS + mf_nn_b.SECTIONS + mf_tricky_a.SECTIONS + mf_tricky_b.SECTIONS
    )
    facts = copy.deepcopy(mf_tricky_b.section_facts["parts"][0]["items"])
    facts.extend(copy.deepcopy(mf_keywords.facts_extra))
    facts.extend(copy.deepcopy(mf_exam.FACTS))

    rename_ids(sections, facts)

    for section in sections:
        # The U4 app called the spec reference "lessons"
        if "lessons" in section:
            section["spec"] = section.pop("lessons")
        if section["id"] in TAGS:
            section["tags"] = TAGS[section["id"]]
        if section["id"] == "planning-practical":
            adapt_planning(section)
        if section["id"] == "conservation-momentum":
            adapt_conservation(section)
        if section["id"] == "estimation":
            section["title"] = "Estimation in motion questions"
        add_exam_findings(section)
        embed_types(section)

    # Key words go last in the non-negotiables band
    last_nn = max(index for index, section in enumerate(sections) if section["band"] == "nn")
    sections.insert(last_nn + 1, copy.deepcopy(mf_keywords.section_keywords))

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
        len(facts), "facts,", len(rebuilt["types"]), "types kept",
    )


if __name__ == "__main__":
    main()
