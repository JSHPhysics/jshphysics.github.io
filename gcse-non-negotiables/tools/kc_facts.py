"""
kc_facts.py — Topic 1 Key concepts: the flashcards.

Each card is (question, answer, section id). Keep answers short enough
to say out loud; the section id ties the card to its section so a
hidden section hides its cards.
"""

from revlib import fact

FACTS = [
    # SI units — one card per quantity/unit pair
    fact("SI unit of length?", "metre, m", "si-units"),
    fact("SI unit of mass?", "kilogram, kg (not the gram)", "si-units"),
    fact("SI unit of time?", "second, s", "si-units"),
    fact("SI unit of current?", "ampere (amp), A", "si-units"),
    fact("SI unit of temperature?", "kelvin, K (°C accepted where the question uses it)", "si-units"),
    fact("Unit of force and weight?", "newton, N", "si-units"),
    fact("Unit of energy and work done?", "joule, J", "si-units"),
    fact("Unit of power?", "watt, W (1 W = 1 J/s)", "si-units"),
    fact("Unit of pressure?", "pascal, Pa (1 Pa = 1 N/m²)", "si-units"),
    fact("Unit of frequency?", "hertz, Hz", "si-units"),
    fact("Unit of potential difference?", "volt, V", "si-units"),
    fact("Unit of resistance?", "ohm, Ω", "si-units"),
    fact("Unit of charge?", "coulomb, C", "si-units"),
    fact("Unit of acceleration?", "metre per second squared, m/s²", "si-units"),
    fact("Unit of density?", "kilogram per cubic metre, kg/m³", "si-units"),
    fact("Unit of momentum?", "kilogram metre per second, kg m/s", "si-units"),
    fact("Unit of specific heat capacity?", "J/kg °C", "si-units"),
    fact("Unit of gravitational field strength?", "newton per kilogram, N/kg", "si-units"),
    fact("Which unit symbols take a capital letter?", "Those named after people: N, J, W, Pa, Hz, V, A, C, K, Ω", "si-units"),
    # Prefixes
    fact("giga (G) means ×…", "$10^{9}$ = 1 000 000 000", "prefixes-nn"),
    fact("mega (M) means ×…", "$10^{6}$ = 1 000 000", "prefixes-nn"),
    fact("kilo (k) means ×…", "$10^{3}$ = 1000", "prefixes-nn"),
    fact("centi (c) means ×…", "$10^{-2}$ = 0.01", "prefixes-nn"),
    fact("milli (m) means ×…", "$10^{-3}$ = 0.001", "prefixes-nn"),
    fact("micro (μ) means ×…", "$10^{-6}$ = 0.000 001", "prefixes-nn"),
    fact("nano (n) means ×…", "$10^{-9}$ = 0.000 000 001", "prefixes-nn"),
    # Conversions
    fact("1 hour in seconds?", "3600 s", "converting"),
    fact("1 day in seconds?", "86 400 s (24 × 3600)", "converting"),
    fact("km/h to m/s?", "÷ 3.6 (×1000 ÷ 3600)", "converting"),
    fact("1 m² in cm²?", "10 000 cm² (100 × 100)", "converting"),
    fact("1 m³ in cm³?", "1 000 000 cm³ (100 × 100 × 100)", "converting"),
    fact("1 g/cm³ in kg/m³?", "1000 kg/m³", "converting"),
    fact("1 kWh in joules?", "3 600 000 J ($3.6 \\times 10^{6}$ J)", "converting"),
    fact("Converting to a bigger unit makes the number…", "smaller (3500 m = 3.5 km)", "converting"),
    # Significant figures and standard form
    fact("Do leading zeros count as significant figures?", "No: 0.0047 has 2 s.f.", "sig-figs"),
    fact("How many s.f. should an answer have?", "The same as the least precise data (usually 2 or 3); round only at the end", "sig-figs"),
    fact("Standard form: the rule for the front number?", "Between 1 and 10: $a \\times 10^{n}$ with $1 \\le a < 10$", "standard-form-nn"),
    fact("Calculator shows 2.5E-5. Write it.", "$2.5 \\times 10^{-5}$", "standard-form-nn"),
    # Equation sheet and symbols
    fact("$W$ can mean…", "weight (W = m × g) or work done (W = F × d)", "equation-sheet"),
    fact("$Q$ can mean…", "charge (Q = I × t) or thermal energy (ΔQ = m c Δθ)", "equation-sheet"),
    fact("$P$ can mean…", "power (P = E ÷ t) or pressure (P = F ÷ A)", "equation-sheet"),
    fact("Value of $g$ at GCSE?", "10 N/kg (= 10 m/s²)", "equation-sheet"),
    fact("Speed of light?", "$3 \\times 10^{8}$ m/s", "equation-sheet"),
    # Rearranging and proportion
    fact("To undo a square…", "take the square root of both sides", "rearranging-nn"),
    fact("Make $v$ the subject of $KE = \\tfrac{1}{2} m v^2$", "$v = \\sqrt{2 KE \\div m}$", "rearranging-nn"),
    fact("Make $t$ the subject of $a = (v - u) \\div t$", "$t = (v - u) \\div a$", "rearranging-nn"),
    fact("Percentage change =", "(change ÷ original) × 100", "proportion"),
    fact("Efficiency =", "useful energy output ÷ total energy input (× 100 for %)", "proportion"),
    fact("Directly proportional means…", "double one, double the other; straight line through the origin", "proportion"),
    fact("Inversely proportional means…", "double one, halve the other; x × y is constant", "proportion"),
    fact("$y \\propto x^2$: double $x$ and $y$ becomes…", "4 times bigger", "proportion"),
    fact("EWAU stands for…", "Equation, Working, Answer, Units", "ewau"),
    # Command words
    fact("\"State\" wants…", "a short answer, no reasoning", "command-words"),
    fact("\"Describe\" wants…", "what happens, in order — no why", "command-words"),
    fact("\"Explain\" wants…", "why, with reasons: because / so / therefore", "command-words"),
    fact("\"Calculate\" wants…", "a number with working and a unit (EWAU)", "command-words"),
    fact("\"Determine\" wants…", "a value you get from the graph or data yourself", "command-words"),
    fact("\"Show that\" wants…", "full working arriving at the value given", "command-words"),
    fact("\"Compare\" wants…", "similarities and differences, mentioning both things", "command-words"),
    fact("\"Evaluate\" wants…", "for and against, then a justified conclusion", "command-words"),
    fact("\"Justify\" wants…", "the evidence or reasoning for a given statement", "command-words"),
    fact("\"Suggest\" wants…", "a sensible physics idea applied to a new situation", "command-words"),
    # Graphs and proportionality
    fact("Which variable goes on the x-axis?", "The independent variable (the one you changed)", "graph-skills"),
    fact("Gradient =", "change in y ÷ change in x, from a large triangle on the line of best fit", "graph-skills"),
    fact("A line of best fit should…", "follow the trend with points balanced either side; not join the dots", "graph-skills"),
    fact("Straight line not through the origin is…", "linear, not proportional", "proportionality"),
    # Practicals
    fact("Seven steps to describe a practical?", "Two variables → formula → change (and keep same) → measure (equipment) → use the result → accuracy detail → repeat and calculate a mean", "planning-practical"),
    fact("\"Repeat\" on its own scores…", "nothing — say \"repeat and calculate a mean\"", "planning-practical"),
    fact("Accurate means…", "close to the true value", "evaluating-methods"),
    fact("Precise means…", "repeated readings are close to each other", "evaluating-methods"),
    fact("Resolution means…", "the smallest change an instrument can show", "evaluating-methods"),
    fact("Repeatable vs reproducible?", "Same person, same equipment, same result / different person or method, same result", "evaluating-methods"),
    fact("Random error vs systematic error?", "Scatter above and below / every reading shifted the same way", "evaluating-methods"),
    fact("Repeating and averaging reduces…", "random error only (not systematic)", "evaluating-methods"),
    fact("What to do with an anomalous result?", "Repeat it if you can; otherwise leave it out of the mean and say so", "evaluating-methods"),
    fact("Mass of an adult? of a car?", "about 70 kg; about 1000–1500 kg", "estimation"),
    fact("Walking, running, cycling speeds?", "about 1.5, 3, 6 m/s", "estimation"),
    fact("Power of a kettle? of a person?", "about 2 kW; about 100 W", "estimation"),
]
