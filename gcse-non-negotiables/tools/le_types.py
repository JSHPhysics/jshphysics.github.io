"""
le_types.py — the two calculation types for Topic 5, in the plain-text
notation the calculation cards use (not TeX).

    em-wave-speed   v = f × λ for electromagnetic waves, c = 3 × 10⁸ m/s
    lens-power      P = 1 / f   (Physics only)

Each has a worked example and exactly six practice questions, ids
<type>-w and <type>-p1 … -p6, as the validator requires.
"""

C = 3.0e8


def q(qid, question, hint, walkthrough, value, unit, tolerance=None):
    if isinstance(value, float) and value.is_integer():
        value = int(value)
    answer = {"value": value, "unit": unit}
    if tolerance is not None:
        answer["tolerance"] = tolerance
    return {"id": qid, "question": question, "hint": hint, "walkthrough": walkthrough, "answer": answer}


EM_WAVE_SPEED = {
    "id": "em-wave-speed",
    "name": "EM waves: v = f × λ with c = 3 × 10⁸ m/s",
    "equations": ["v = f × λ", "c = 3 × 10⁸ m/s"],
    "boards": ["Foundation", "Higher"],
    "method": "All electromagnetic waves travel at 3 × 10⁸ m/s in a vacuum (and almost that in air), so for an EM wave the speed is already known: v = 3 × 10⁸ m/s. Use v = f × λ to find the frequency (f = v ÷ λ) or the wavelength (λ = v ÷ f). Convert first: kHz × 10³, MHz × 10⁶, GHz × 10⁹; nm × 10⁻⁹, mm × 10⁻³, cm × 10⁻². Use the ×10ˣ key and give large or small answers in standard form.",
    "commonErrors": [
        "Leaving GHz, MHz or nm unconverted — the 2022 report: \"learn the multiples of units to be able to use correct powers of 10\"",
        "Multiplying v by f when the question wants a wavelength instead of dividing",
        "Writing 300 000 000 with the wrong number of zeros instead of 3 × 10⁸",
        "Using the speed of sound (340 m/s) for a radio wave or light",
    ],
    "worked": {
        "id": "em-wave-speed-w",
        "question": "A mobile phone transmits microwaves at a frequency of 1.8 GHz. Calculate their wavelength. (speed of EM waves = 3 × 10⁸ m/s)",
        "steps": [
            "Known: f = 1.8 GHz = 1.8 × 10⁹ Hz, v = 3 × 10⁸ m/s. Unknown: λ.",
            "v = f × λ → λ = v ÷ f",
            "λ = 3 × 10⁸ ÷ 1.8 × 10⁹",
            "λ = 0.167 m (to 3 s.f.)",
        ],
        "answer": {"value": 0.167, "unit": "m"},
    },
    "practice": [
        q("em-wave-speed-p1", "A radio station broadcasts at 100 MHz. Calculate the wavelength of its radio waves. (v = 3 × 10⁸ m/s)",
          "100 MHz = 1 × 10⁸ Hz; λ = v ÷ f.",
          ["f = 100 MHz = 1 × 10⁸ Hz, v = 3 × 10⁸ m/s, find λ.", "λ = v ÷ f = 3 × 10⁸ ÷ 1 × 10⁸", "λ = 3 m"], 3, "m"),
        q("em-wave-speed-p2", "Microwaves in an oven have a wavelength of 12 cm. Calculate their frequency. (v = 3 × 10⁸ m/s)",
          "12 cm = 0.12 m; f = v ÷ λ.",
          ["λ = 12 cm = 0.12 m, v = 3 × 10⁸ m/s, find f.", "f = v ÷ λ = 3 × 10⁸ ÷ 0.12", "f = 2.5 × 10⁹ Hz (2.5 GHz)"], 2.5e9, "Hz"),
        q("em-wave-speed-p3", "Ultraviolet light has a wavelength of 280 nm. Calculate its frequency. (v = 3 × 10⁸ m/s)",
          "280 nm = 280 × 10⁻⁹ m = 2.8 × 10⁻⁷ m; f = v ÷ λ. Type the answer as 1.07e15.",
          ["λ = 280 nm = 2.8 × 10⁻⁷ m, v = 3 × 10⁸ m/s, find f.", "f = v ÷ λ = 3 × 10⁸ ÷ 2.8 × 10⁻⁷", "f = 1.07 × 10¹⁵ Hz (the 2024 scheme accepted anything rounding to 1.1 × 10¹⁵)"], 1.07e15, "Hz", tolerance=0.05),
        q("em-wave-speed-p4", "Red light has a frequency of 4.3 × 10¹⁴ Hz. Calculate its wavelength in metres. (v = 3 × 10⁸ m/s)",
          "λ = v ÷ f. Type the answer as 7.0e-7.",
          ["f = 4.3 × 10¹⁴ Hz, v = 3 × 10⁸ m/s, find λ.", "λ = v ÷ f = 3 × 10⁸ ÷ 4.3 × 10¹⁴", "λ = 7.0 × 10⁻⁷ m (700 nm)"], 6.98e-7, "m"),
        q("em-wave-speed-p5", "A Wi-Fi router uses a frequency of 5 GHz. Calculate the wavelength in centimetres. (v = 3 × 10⁸ m/s)",
          "5 GHz = 5 × 10⁹ Hz; find λ in metres, then × 100.",
          ["f = 5 GHz = 5 × 10⁹ Hz, v = 3 × 10⁸ m/s, find λ.", "λ = v ÷ f = 3 × 10⁸ ÷ 5 × 10⁹ = 0.06 m", "λ = 6 cm"], 6, "cm"),
        q("em-wave-speed-p6", "X-rays of wavelength 1 × 10⁻¹⁰ m are used in a hospital. Calculate their frequency. (v = 3 × 10⁸ m/s)",
          "f = v ÷ λ. Type the answer as 3e18.",
          ["λ = 1 × 10⁻¹⁰ m, v = 3 × 10⁸ m/s, find f.", "f = v ÷ λ = 3 × 10⁸ ÷ 1 × 10⁻¹⁰", "f = 3 × 10¹⁸ Hz"], 3e18, "Hz"),
    ],
}

LENS_POWER = {
    "id": "lens-power",
    "name": "Power of a lens: P = 1 ÷ f",
    "equations": ["P = 1 / f", "f in metres, P in dioptres (D)"],
    "boards": ["Foundation", "Higher"],
    "method": "The power of a lens is 1 divided by its focal length, with the focal length in metres. The unit is the dioptre, D. A converging lens has a positive power; a diverging lens has a negative focal length and so a negative power. A shorter focal length (a fatter, more curved lens) means a higher power. To find the focal length from the power, f = 1 ÷ P — and finish the calculation: the 2022 report says candidates stopped at 1/f.",
    "commonErrors": [
        "Leaving the focal length in centimetres (20 cm gives P = 0.05 D instead of 5 D)",
        "Stopping at 1/f = 0.25 instead of finishing f = 4 m — or giving 1/P instead of P",
        "Forgetting the minus sign for a diverging lens",
        "Writing the unit as m or W instead of D (dioptres)",
    ],
    "worked": {
        "id": "lens-power-w",
        "question": "A converging lens has a focal length of 20 cm. Calculate its power.",
        "steps": [
            "Known: f = 20 cm = 0.20 m. Unknown: P.",
            "P = 1 / f",
            "P = 1 / 0.20",
            "P = 5 D",
        ],
        "answer": {"value": 5, "unit": "D"},
    },
    "practice": [
        q("lens-power-p1", "A converging lens has a focal length of 25 cm. Calculate its power.",
          "25 cm = 0.25 m; P = 1 ÷ f.",
          ["f = 25 cm = 0.25 m, find P.", "P = 1 / f = 1 / 0.25", "P = 4 D"], 4, "D"),
        q("lens-power-p2", "A camera lens has a focal length of 50 mm. Calculate its power.",
          "50 mm = 0.050 m.",
          ["f = 50 mm = 0.050 m, find P.", "P = 1 / f = 1 / 0.050", "P = 20 D"], 20, "D"),
        q("lens-power-p3", "A pair of reading glasses has lenses of power +2.5 D. Calculate the focal length of a lens in metres.",
          "f = 1 ÷ P. Finish the calculation.",
          ["P = 2.5 D, find f.", "f = 1 / P = 1 / 2.5", "f = 0.4 m (40 cm)"], 0.4, "m"),
        q("lens-power-p4", "A diverging lens has a focal length of −40 cm. Calculate its power.",
          "Keep the minus sign; −40 cm = −0.40 m.",
          ["f = −40 cm = −0.40 m, find P.", "P = 1 / f = 1 / (−0.40)", "P = −2.5 D"], -2.5, "D"),
        q("lens-power-p5", "Lens A has a focal length of 10 cm and lens B has a focal length of 40 cm. Calculate how many times more powerful lens A is than lens B.",
          "Find both powers, then divide.",
          ["P_A = 1 / 0.10 = 10 D; P_B = 1 / 0.40 = 2.5 D.", "10 ÷ 2.5 = 4", "Lens A is 4 times more powerful (the shorter focal length is the more powerful lens)"], 4, ""),
        q("lens-power-p6", "A magnifying glass has a power of 8 D. Calculate its focal length in centimetres.",
          "f = 1 ÷ P in metres, then × 100.",
          ["P = 8 D, find f.", "f = 1 / P = 1 / 8 = 0.125 m", "f = 12.5 cm"], 12.5, "cm"),
    ],
}

TYPES = [EM_WAVE_SPEED, LENS_POWER]
