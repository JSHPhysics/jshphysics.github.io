#!/usr/bin/env python3
"""
rehome_topics.py — move the calculation types into Edexcel spec-order topics.

One-off restructure (November 2026). The GCSE site started as ten
calculation groupings; it now follows the Edexcel 1PH0 specification,
one page per topic, with Topics 3 and 8 (energy; work and power) merged
and Topic 1 kept as its own "key concepts" page. Every calculation type
and every question keeps its id, so nothing a student has done is lost.

Run from the gcse-non-negotiables folder:
    python3 tools/rehome_topics.py
then
    python3 tools/build_manifest.py
"""

import json
import os
import shutil

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DATA = os.path.join(ROOT, "data")
OLD = os.path.join(DATA, "_old")

# The new topics, in order. `types` lists (old file, type id) pairs to move in.
TOPICS = [
    {
        "id": "key-concepts", "order": 10, "spec": "Topic 1",
        "title": "Key concepts: units and equations",
        "subtitle": "SI units, prefixes, standard form, converting compound units and rearranging equations",
        "figure": "measurements",
        "types": [("units-and-equations", t) for t in ["si-conversions", "prefixes", "compound-units", "standard-form", "rearranging", "percentages-ratios"]],
    },
    {
        "id": "motion-and-forces", "order": 20, "spec": "Topic 2",
        "title": "Motion and forces",
        "subtitle": "Vectors and scalars, motion graphs, Newton's laws, momentum and stopping distances",
        "figure": "motion-graph",
        "types": [("motion", t) for t in ["speed", "acceleration", "v2-u2", "dt-graph", "vt-graph"]]
        + [("forces-and-momentum", t) for t in ["weight-and-mass", "resultant-force", "newtons-second-law", "stopping-distance", "momentum", "conservation-of-momentum", "force-from-momentum-change", "force-graph"]],
    },
    {
        "id": "energy-and-work", "order": 30, "spec": "Topics 3 and 8",
        "title": "Energy, work and power",
        "subtitle": "Energy stores and transfers, conservation, efficiency, work done and power",
        "figure": "circular-shm",
        "types": [("energy", t) for t in ["kinetic-energy", "gravitational-potential-energy", "work-done", "power", "efficiency", "energy-transfers", "energy-graph"]],
    },
    {
        "id": "waves", "order": 40, "spec": "Topic 4",
        "title": "Waves",
        "subtitle": "Transverse and longitudinal waves, the wave equation, sound and ultrasound",
        "figure": "waves",
        "types": [("waves", t) for t in ["wave-speed-frequency", "wave-speed-distance", "period-frequency", "echoes", "wave-graph"]],
    },
    {
        "id": "light-and-em", "order": 50, "spec": "Topic 5",
        "title": "Light and the electromagnetic spectrum",
        "subtitle": "Reflection, refraction, lenses, colour and the electromagnetic spectrum",
        "figure": "quantum",
        "types": [],
        "placeholder": "The notes, tricky bits and flashcards for this topic are being written. Check back soon.",
    },
    {
        "id": "radioactivity", "order": 60, "spec": "Topic 6",
        "title": "Radioactivity",
        "subtitle": "Atomic structure, types of radiation, decay equations, half-life and uses of radiation",
        "figure": "half-life",
        "types": [("radioactivity", t) for t in ["nuclear-notation", "nuclear-equations", "half-life-fraction", "half-life-time", "background-count", "decay-graph"]],
    },
    {
        "id": "astronomy", "order": 70, "spec": "Topic 7",
        "title": "Astronomy",
        "subtitle": "The Solar System, orbits, red-shift, the Big Bang and the life cycle of stars",
        "figure": "astrophysics",
        "types": [],
        "placeholder": "The notes, tricky bits and flashcards for this topic are being written. Check back soon.",
    },
    {
        "id": "forces-and-their-effects", "order": 90, "spec": "Topic 9",
        "title": "Forces and their effects",
        "subtitle": "Contact and non-contact forces, vector diagrams, moments and the principle of moments",
        "figure": "forces",
        "types": [("forces-and-matter", t) for t in ["moment", "balance"]],
    },
    {
        "id": "electricity-and-circuits", "order": 100, "spec": "Topic 10",
        "title": "Electricity and circuits",
        "subtitle": "Charge, current, potential difference, resistance, series and parallel circuits, power and the mains",
        "figure": "circuit",
        "types": [("electricity", t) for t in ["charge", "ohm", "eqv", "electrical-power", "ept", "circuits", "iv-graph"]],
    },
    {
        "id": "static-electricity", "order": 110, "spec": "Topic 11",
        "title": "Static electricity",
        "subtitle": "Charging by friction, electric fields, sparks and earthing",
        "figure": "electric-fields-capacitors",
        "types": [],
        "placeholder": "The notes, tricky bits and flashcards for this topic are being written. Check back soon.",
    },
    {
        "id": "magnetism-and-motor-effect", "order": 120, "spec": "Topic 12",
        "title": "Magnetism and the motor effect",
        "subtitle": "Magnetic fields, electromagnets, the motor effect and Fleming's left-hand rule",
        "figure": "magnetism",
        "types": [("magnetism", "motor-force")],
    },
    {
        "id": "electromagnetic-induction", "order": 130, "spec": "Topic 13",
        "title": "Electromagnetic induction",
        "subtitle": "Induced potential difference, generators, transformers and the National Grid",
        "figure": "magnetic-fields-induction",
        "types": [("magnetism", t) for t in ["turns", "tx-power", "loss"]],
    },
    {
        "id": "particle-model", "order": 140, "spec": "Topic 14",
        "title": "Particle model",
        "subtitle": "Density, states of matter, specific heat capacity, latent heat and gas pressure",
        "figure": "particle-model",
        "types": [("particle-model", t) for t in ["density", "shc", "latent", "change-of-state", "temperature", "boyle", "heating-graph"]],
    },
    {
        "id": "forces-and-matter", "order": 150, "spec": "Topic 15",
        "title": "Forces and matter",
        "subtitle": "Elastic and inelastic distortion, Hooke's law, energy in a spring, pressure in fluids",
        "figure": "materials",
        "types": [("forces-and-matter", t) for t in ["hooke", "elastic", "fx-graph", "pressure", "liquid"]],
    },
]


def main():
    # Load the old files once, keyed by file stem
    old_files = {}
    for name in os.listdir(DATA):
        if not name.endswith(".json") or name in ("manifest.json", "config.json"):
            continue
        with open(os.path.join(DATA, name), encoding="utf-8") as handle:
            old_files[name[:-5]] = json.load(handle)

    # Index every type by (old file, id) and remember which were used
    index = {}
    for stem, topic in old_files.items():
        for calc_type in topic["types"]:
            index[(stem, calc_type["id"])] = calc_type
    used = set()

    # Move the old files aside before writing, so a rerun cannot read its own output
    os.makedirs(OLD, exist_ok=True)
    for stem in old_files:
        shutil.move(os.path.join(DATA, stem + ".json"), os.path.join(OLD, stem + ".json"))

    total_types = 0
    total_questions = 0
    for spec in TOPICS:
        types = []
        for key in spec["types"]:
            if key not in index:
                raise SystemExit("missing type: " + str(key))
            if key in used:
                raise SystemExit("type used twice: " + str(key))
            used.add(key)
            types.append(index[key])
        topic = {
            "id": spec["id"],
            "title": spec["title"],
            "subtitle": spec["subtitle"],
            "spec": spec["spec"],
            "order": spec["order"],
            "figure": spec["figure"],
        }
        if spec.get("placeholder"):
            topic["placeholder"] = spec["placeholder"]
        topic["types"] = types
        with open(os.path.join(DATA, spec["id"] + ".json"), "w", encoding="utf-8") as handle:
            json.dump(topic, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        total_types += len(types)
        total_questions += sum(len(t["practice"]) for t in types)
        print(f"{spec['id']:28} {len(types):2} types")

    unused = [key for key in index if key not in used]
    if unused:
        raise SystemExit("types not placed: " + str(unused))
    print(f"\n{len(TOPICS)} topics, {total_types} types, {total_questions} practice questions; old files in data/_old/")


if __name__ == "__main__":
    main()
