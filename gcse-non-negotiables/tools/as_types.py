"""
as_types.py — the one calculation type for Topic 7, in the plain-text
notation the calculation cards use.

    weight-elsewhere   W = m × g with the g of the body you are standing on
"""


def q(qid, question, hint, walkthrough, value, unit):
    if isinstance(value, float) and value.is_integer():
        value = int(value)
    return {"id": qid, "question": question, "hint": hint, "walkthrough": walkthrough, "answer": {"value": value, "unit": unit}}


WEIGHT_ELSEWHERE = {
    "id": "weight-elsewhere",
    "name": "Weight on other bodies: W = m × g",
    "equations": ["W = m × g", "g: Earth 10 N/kg, Moon 1.6 N/kg, Mars 3.7 N/kg, Jupiter 25 N/kg"],
    "boards": ["Foundation", "Higher"],
    "method": "Weight is the force of gravity on a mass: W = m × g. The mass of an object is the same everywhere; its weight changes because g — the gravitational field strength — is different on each body (it depends on the body's mass and radius). Use the g the question gives for that body. To find g from a weight, g = W ÷ m; to find the mass from a weight on another body, m = W ÷ g for that body, and that mass is the same back on Earth.",
    "commonErrors": [
        "Using Earth's g for a weight on the Moon or Mars",
        "Saying the mass changes on the Moon — only the weight changes",
        "Giving the unit of g as N (it is N/kg) or of weight as kg (it is N)",
        "Dividing by the wrong g when converting a Moon weight back to an Earth weight",
    ],
    "worked": {
        "id": "weight-elsewhere-w",
        "question": "An astronaut has a mass of 80 kg. Calculate her weight on the Moon, where g = 1.6 N/kg.",
        "steps": [
            "Known: m = 80 kg, g (Moon) = 1.6 N/kg. Unknown: W.",
            "W = m × g",
            "W = 80 × 1.6",
            "W = 128 N (on Earth it would be 800 N; her mass is 80 kg in both places)",
        ],
        "answer": {"value": 128, "unit": "N"},
    },
    "practice": [
        q("weight-elsewhere-p1", "A rover has a mass of 900 kg. Calculate its weight on Mars, where g = 3.7 N/kg.",
          "W = m × g with the Martian g.",
          ["m = 900 kg, g = 3.7 N/kg, find W.", "W = m × g = 900 × 3.7", "W = 3330 N"], 3330, "N"),
        q("weight-elsewhere-p2", "A 2 kg rock weighs 3.2 N on the Moon. Calculate the gravitational field strength on the Moon.",
          "g = W ÷ m.",
          ["W = 3.2 N, m = 2 kg, find g.", "g = W ÷ m = 3.2 ÷ 2", "g = 1.6 N/kg"], 1.6, "N/kg"),
        q("weight-elsewhere-p3", "A probe weighs 1500 N on Jupiter, where g = 25 N/kg. Calculate its mass.",
          "m = W ÷ g.",
          ["W = 1500 N, g = 25 N/kg, find m.", "m = W ÷ g = 1500 ÷ 25", "m = 60 kg (the same mass anywhere)"], 60, "kg"),
        q("weight-elsewhere-p4", "An object weighs 600 N on Earth (g = 10 N/kg). Calculate its weight on the Moon (g = 1.6 N/kg).",
          "Find the mass first, then multiply by the Moon's g.",
          ["Mass: m = W ÷ g = 600 ÷ 10 = 60 kg.", "On the Moon: W = m × g = 60 × 1.6", "W = 96 N"], 96, "N"),
        q("weight-elsewhere-p5", "A 0.5 kg hammer is dropped on the Moon (g = 1.6 N/kg). Calculate the force of gravity on it.",
          "The force of gravity is the weight: W = m × g.",
          ["m = 0.5 kg, g = 1.6 N/kg.", "W = 0.5 × 1.6", "W = 0.8 N"], 0.8, "N"),
        q("weight-elsewhere-p6", "A satellite of mass 400 kg is in orbit where g = 8.7 N/kg. Calculate the gravitational force on it.",
          "Gravity still acts in orbit — that is what keeps it there. W = m × g.",
          ["m = 400 kg, g = 8.7 N/kg.", "W = 400 × 8.7", "W = 3480 N (towards the Earth's centre)"], 3480, "N"),
    ],
}

TYPES = [WEIGHT_ELSEWHERE]
