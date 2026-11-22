"""
en_tricky_a.py — Topics 3 and 8 (Energy): the tricky bits T1–T6.

T1 Describing the five spec situations   T4 Work done the hard way
T2 GPE ↔ KE                              T5 Power the hard way
T3 KE traps                              T6 Efficiency the hard way
"""

from revlib import (
    choice, ewau, explain, group, mark_scheme, marks, numeric, practice, section,
    sf, worked, written,
)

G = 10

# ---------------------------------------------------------------------
# T1 · The five situations in 3.5
# ---------------------------------------------------------------------

SITUATIONS_TABLE = (
    "<table class='tbl'><tr><th>Situation (spec 3.5)</th><th>Energy is transferred from…</th><th>…to…</th><th>…by</th></tr>"
    "<tr><td>An object <b>projected upwards</b> (or up a slope)</td><td>kinetic store of the object</td><td>gravitational potential store (and thermal store of the air)</td><td>mechanically — gravity (and air resistance) do work</td></tr>"
    "<tr><td>A moving object <b>hitting an obstacle</b></td><td>kinetic store of the object</td><td>thermal store of the object and obstacle; elastic potential store if it deforms; a little by sound (radiation)</td><td>mechanically — the contact force does work</td></tr>"
    "<tr><td>An object <b>accelerated by a constant force</b></td><td>chemical store of the engine / person (or whatever provides the force)</td><td>kinetic store of the object</td><td>mechanically — the force does work</td></tr>"
    "<tr><td>A <b>vehicle slowing down</b></td><td>kinetic store of the vehicle</td><td>thermal store of the brakes, tyres, road and surroundings</td><td>mechanically — friction does work, then by heating</td></tr>"
    "<tr><td>Bringing water to the boil in an <b>electric kettle</b></td><td>(chemical store of the fuel at the power station →) the kettle element</td><td>thermal store of the water (and the kettle and the surroundings)</td><td>electrically to the element, then by heating to the water</td></tr></table>"
)

section_t1 = section(
    "store-changes", "tricky", "Describing energy changes: the five situations", "3.5, 8.1, 8.7",
    equations=[r"\text{from the } \_\_\_ \text{ store of } \_\_\_ \text{ to the } \_\_\_ \text{ store of } \_\_\_ \text{, by } \_\_\_"],
    blurb="The spec names five situations you must be able to analyse. Each is the same sentence with different words in the gaps. The marks go to the stores, so name them; \"energy is lost\" only scores when you say where to — the surroundings, as thermal energy.",
    checklist=[
        "Describe the store changes for each of the five spec situations",
        "Always name the starting store, the finishing store(s) and the pathway",
        "Say that dissipated energy ends up in the thermal store of the surroundings — never \"lost\"",
    ],
    parts=[
        explain(
            "The sentence and the five situations",
            "<p>Every energy-change answer is this sentence: <b>energy is transferred from the [store] of [object] to the [store] of [object], [pathway].</b> If some is wasted, add: <b>some energy is dissipated to the thermal store of the surroundings by [friction / air resistance / heating].</b></p>" + SITUATIONS_TABLE +
            "<p>The June 2022 Paper 2 question (Q7(a)(iii), a rover <i>descending</i> to Mars on thrusters and a parachute) asked for the energy changes <i>in terms of the work done by forces</i>. The scheme's eight points: <b>work is done by gravity</b>; <b>work is done by the thrusters</b>; <b>air resistance does work on the parachute</b>; this <b>reduces the kinetic store</b>; the <b>gravitational potential store decreases</b>; chemical energy is transferred from the thrusters; energy is transferred to the <b>thermal store</b>; mechanically. The report: \"hardly any candidates talked about work being done against gravity\" — the store changes were the marks most students got; the three <b>work done by [named force]</b> lines were the ones they missed. Name the force, then the store.</p>",
        ),
        worked(
            "A ball hitting a wall",
            "A ball of mass 0.42 kg hits a wall at 12 m/s. Describe the energy transfers when the ball hits the wall. (2 marks)",
            [
                "<b>Starting store:</b> the ball's <b>kinetic store</b> (that is one mark on its own in the June 2023 scheme).",
                "<b>Where it goes:</b> to the <b>elastic potential store</b> of the ball as it squashes, then mostly to the <b>thermal store</b> of the ball, the wall and the surroundings, with a little transferred by radiation as sound.",
                "<b>Answer:</b> Energy is transferred from the kinetic store of the ball to the elastic potential store as it deforms and then to the thermal store of the ball and wall (dissipated to the surroundings), mechanically by the contact force and then by heating.",
            ],
        ),
        practice("Energy changes", [
            written("en-t1-q1", "A car brakes to a stop at traffic lights. Describe the energy transfers. (2)",
                    marks(["From the <b>kinetic store</b> of the car…",
                           "…to the <b>thermal store</b> of the brakes (and tyres and road), <b>by friction</b> (mechanically, then dissipated by heating to the surroundings)."]), lines=3),
            written("en-t1-q2", "A rocket engine accelerates a model rocket upwards with a constant force. Describe the energy transfers. (3)",
                    mark_scheme([
                        ("From", "From the <b>chemical store</b> of the fuel…"),
                        ("To", "…to the <b>kinetic store</b> of the rocket and its <b>gravitational potential store</b> (as it rises)…"),
                        ("Pathway", "…<b>mechanically</b> — the thrust force does work on the rocket; some energy is transferred to the thermal store of the surroundings by heating (hot exhaust) and air resistance."),
                    ]), lines=4),
            written("en-t1-q3", "An electric kettle brings water to the boil. Describe the energy transfers, including the wasted energy. (3)",
                    mark_scheme([
                        ("Electrically", "Energy is transferred <b>electrically</b> (by the current) to the kettle <b>element</b>…"),
                        ("By heating", "…and from the element to the <b>thermal store of the water</b> by <b>heating</b>."),
                        ("Wasted", "Some energy is transferred to the thermal store of the <b>kettle body and the surroundings</b> (dissipated), so not all of it heats the water."),
                    ]), lines=4),
            written("en-t1-q4", "A rover descends towards the surface of Mars, slowed by its thrusters and a parachute. Describe the energy changes in terms of the work done by forces. (3)",
                    mark_scheme([
                        ("Gravity", "<b>Work is done by gravity</b> on the rover as it falls."),
                        ("Thrusters", "<b>Work is done by the thrusters</b> on the rover (chemical energy is transferred from the thrusters)."),
                        ("Air resistance", "<b>Air resistance does work on the parachute</b> (and the rover)."),
                        ("Stores", "This <b>reduces the kinetic store</b> of the rover; its <b>gravitational potential store decreases</b>; energy is transferred to the <b>thermal store</b> (mechanically)."),
                    ], total=3, extra=["Any three of the eight points in the June 2022 2H scheme (Q7(a)(iii)). The store changes alone reached 2 or 3 marks; the <b>work done by [named force]</b> lines were the ones most candidates missed — name the force, then the store. If nothing else scores, \"work = force × distance\" earns one."]), lines=5,
                    hint="Three forces do work on the way down: name each, then say what happens to the stores."),
            choice("en-t1-q5", "A pendulum swings from its highest point to its lowest. Which is the correct description?",
                   ["GPE turns into KE", "Energy is transferred from the gravitational potential store of the bob to its kinetic store, mechanically (gravity does work)", "Energy is lost as the bob speeds up", "Energy is transferred by heating from the string"], 1,
                   "Store, store, pathway. \"GPE to KE\" scores both marks on its own (Nov 2020 1H Q2(a) guidance: \"chemical to (G)PE\", \"KE to GPE in lifting\"); the full sentence with the pathway is the safer habit, because it also answers the questions that ask <i>how</i> the energy was transferred."),
            written("en-t1-q6", "A ball is thrown straight up and comes back down to the thrower's hand, but more slowly than it left. Describe the energy transfers for the whole flight. (3)",
                    mark_scheme([
                        ("Up", "Going up: from the <b>kinetic store</b> of the ball to its <b>gravitational potential store</b>, mechanically."),
                        ("Down", "Coming down: from the <b>gravitational potential store</b> back to the <b>kinetic store</b>."),
                        ("Wasted", "Throughout, <b>air resistance does work</b> and energy is transferred to the <b>thermal store of the air</b>, so the kinetic store holds less at the end than at the start."),
                    ]), lines=4),
        ]),
    ],
)
section_t1["subtopic"] = ["3", "8"]

# ---------------------------------------------------------------------
# T2 · GPE ↔ KE
# ---------------------------------------------------------------------

q2_1 = (2 * G * 5) ** 0.5
q2_2 = 17.2 ** 2 / (2 * G)
q2_3_gpe = 0.5 * G * 1.2
q2_3_v = (2 * q2_3_gpe / 0.5) ** 0.5
q2_4_ke = 0.5 * 60 * 8 ** 2
q2_4_h = q2_4_ke / (60 * G)
q2_5_gpe = 1.6 * G * 0.26
q2_5_v = (2 * G * 0.26) ** 0.5

section_t2 = section(
    "gpe-ke", "tricky", "GPE to KE: speeds from heights, heights from speeds", "3.4, 3.5, 8.7",
    equations=[r"m g \Delta h = \tfrac{1}{2} m v^{2}", r"v = \sqrt{2 g \Delta h}", r"\Delta h = \dfrac{v^{2}}{2 g}"],
    blurb="If nothing is wasted, the GPE an object loses equals the KE it gains. Set the two equations equal; the mass cancels, so the speed does not depend on the mass.",
    checklist=[
        "Set ΔGPE = KE and solve for v or Δh",
        "Explain why the mass cancels",
        "Explain why the real speed is less than the calculated one (energy dissipated)",
    ],
    parts=[
        explain(
            "The method",
            "<p>A falling object (or one rolling down a slope with no friction) transfers energy from its gravitational potential store to its kinetic store. By conservation of energy:</p>"
            "<p>$$m g \\Delta h = \\tfrac{1}{2} m v^{2}$$</p>"
            "<p>The mass is on both sides, so it <b>cancels</b>: $g \\Delta h = \\tfrac{1}{2} v^{2}$. That is why a heavy ball and a light ball dropped together hit the ground at the same speed. Rearranged:</p>"
            "<p>$$v = \\sqrt{2 g \\Delta h} \\qquad \\text{and} \\qquad \\Delta h = \\dfrac{v^{2}}{2 g}$$</p>"
            "<p>Two ways to lay it out in the exam, both credited: (1) calculate the GPE in joules, say KE = that, then find $v$; or (2) go straight to $v^{2} = 2 g \\Delta h$ (the June 2023 scheme accepted either, and also $v^{2} - u^{2} = 2ax$ from Topic 2, which is the same equation).</p>"
            "<p><b>The real speed is always less</b> than this. Some energy is transferred to the thermal store of the surroundings by friction and air resistance, so the kinetic store gets less than the whole of the GPE. \"Reduce friction\" is a reason; a question asking <i>how</i> to reduce the gap wants a <b>method</b> — lubricate the wheels, steepen the runway, streamline the trolley (June 2025 report).</p>",
        ),
        worked(
            "Speed at the bottom of a drop",
            "A trolley of mass 1.6 kg is released from rest at the top of a runway 26 cm above the bench. Calculate the speed you would expect it to have at the bottom. ($g = 10$ N/kg)",
            [
                r"<b>Convert:</b> $\Delta h = 26\ \text{cm} = 0.26$ m. (The June 2025 report: not converting this was the most common error.)",
                r"<b>Energy:</b> $\Delta GPE = m g \Delta h = 1.6 \times 10 \times 0.26 = 4.16$ J, so $KE = 4.16$ J.",
                r"<b>Speed:</b> $\tfrac{1}{2} m v^{2} = 4.16 \Rightarrow v^{2} = \dfrac{2 \times 4.16}{1.6} = 5.2$.",
                r"<b>Square root:</b> $v = \sqrt{5.2} = 2.3$ m/s. (Dropping the square root cost a mark.)",
            ],
        ),
        practice("GPE and KE", [
            numeric("en-t2-q1", "A stone is dropped from a height of 5.0 m. Calculate its speed just before it hits the ground, ignoring air resistance. ($g = 10$ N/kg)",
                    sf(q2_1, 2), "m/s", "$v^2 = 2$ g Δh.",
                    [r"$m g \Delta h = \tfrac{1}{2} m v^{2}$, so $v^{2} = 2 g \Delta h = 2 \times 10 \times 5.0 = 100$.", r"$v = \sqrt{100} = 10$ m/s."]),
            numeric("en-t2-q2", "A ball hits the ground at 17.2 m/s. Calculate the height it was dropped from, ignoring air resistance. ($g = 10$ N/kg)",
                    sf(q2_2, 3), "m", "$\\Delta h = v^2 \\div (2g)$.",
                    [r"$v^{2} = 2 g \Delta h \Rightarrow \Delta h = \dfrac{v^{2}}{2 g} = \dfrac{17.2^{2}}{2 \times 10} = \dfrac{296}{20}$.", r"$\Delta h = 14.8$ m."]),
            group("en-t2-q3", "A 0.50 kg ball rolls down a frictionless ramp of vertical height 1.2 m, starting from rest. ($g = 10$ N/kg)", [
                numeric("en-t2-q3a", "Calculate the GPE it loses.", q2_3_gpe, "J", "m g Δh.",
                        ewau(r"\Delta GPE = m g \Delta h", r"\Delta GPE = 0.50 \times 10 \times 1.2", "6.0", "J"), label="a"),
                numeric("en-t2-q3b", "Calculate its speed at the bottom.", sf(q2_3_v, 2), "m/s", "$\\text{KE} = 6.0$ J; $v^2 = 2\\text{KE} \\div m$.",
                        [r"$KE = 6.0$ J, so $v^{2} = \dfrac{2 \times 6.0}{0.50} = 24$.", r"$v = \sqrt{24} = 4.9$ m/s."], label="b"),
            ]),
            group("en-t2-q4", "A 60 kg skateboarder rolls at 8.0 m/s towards a ramp. Ignore friction. ($g = 10$ N/kg)", [
                numeric("en-t2-q4a", "Calculate his kinetic energy.", q2_4_ke, "J", "½ $m v^2$.",
                        ewau(r"KE = \tfrac{1}{2} m v^{2}", r"KE = \tfrac{1}{2} \times 60 \times 8.0^{2}", "1920", "J"), label="a"),
                numeric("en-t2-q4b", "Calculate the maximum height he reaches on the ramp.", sf(q2_4_h, 2), "m", "All the KE becomes GPE: $\\Delta h = \\text{KE} \\div (m g)$.",
                        [r"$m g \Delta h = 1920 \Rightarrow \Delta h = \dfrac{1920}{60 \times 10}$.", r"$\Delta h = 3.2$ m."], label="b"),
                written("en-t2-q4c", "The real height is less than this. Explain why. (2)",
                        marks(["Friction and air resistance <b>do work</b> on the skateboarder…",
                               "…transferring some energy to the <b>thermal store of the surroundings</b>, so less energy reaches the gravitational store."]), lines=3, label="c"),
            ]),
            choice("en-t2-q5", "Two balls of mass 1 kg and 3 kg are dropped from the same height. Ignoring air resistance, which hits the ground faster?",
                   ["The 3 kg ball, three times as fast", "The 1 kg ball", "Both at the same speed — the mass cancels", "The 3 kg ball, slightly faster"], 2,
                   "$m g \\Delta h = \\tfrac{1}{2} m v^2$: m is on both sides, so $v = \\sqrt{2 g \\Delta h}$ for any mass."),
            written("en-t2-q6", "A student measures the speed of a trolley at the bottom of a runway and finds it is less than the value calculated from the GPE lost. Suggest one way to reduce the difference. (1)",
                    marks(["A <b>method</b>: <b>lubricate</b> (oil) the wheel axles / make the runway <b>steeper</b> / use a more <b>streamlined</b> trolley / use an <b>air track</b> instead of the runway (the June 2025 2H guidance, Q2(a)(iii)). (\"Reduce friction\" on its own is a reason, not a method, and scored nothing in June 2025.)"]), lines=2),
        ]),
    ],
)
section_t2["subtopic"] = ["3", "8"]

# ---------------------------------------------------------------------
# T3 · KE traps
# ---------------------------------------------------------------------

q3_1 = 0.5 * 900 * 25 ** 2
q3_2 = 0.5 * 0.045 * 60 ** 2
q3_3 = (2 * 3600 / 50) ** 0.5
q3_4_a = 0.5 * 1500 * 10 ** 2
q3_4_b = 0.5 * 1500 * 30 ** 2
q3_5 = 0.5 * 2.5e5 * 80 ** 2

section_t3 = section(
    "ke-traps", "tricky", "Kinetic energy: the traps", "3.2, 8.9",
    equations=[r"KE = \tfrac{1}{2} m v^{2}", r"v = \sqrt{\dfrac{2 \times KE}{m}}"],
    blurb="The KE equation is short, but it is the one calculation the examiners' reports complain about every year: the square, the half, the units and the square root.",
    checklist=[
        "Square only the speed, then multiply by the mass, then halve",
        "Convert grams, km/h and kJ before substituting",
        "Explain why doubling the speed quadruples the KE, and use it in braking-distance questions",
        "Rearrange for v and remember the square root",
    ],
    parts=[
        explain(
            "Four traps, four fixes",
            "<table class='tbl'><tr><th>Trap</th><th>What happens</th><th>Fix</th></tr>"
            "<tr><td>Not squaring $v$</td><td>answer far too small (the 2023 scheme: 2.52 J instead of 30 J, one mark of two)</td><td>write the equation out with the ² before substituting; square first on the calculator</td></tr>"
            "<tr><td>Forgetting the ½</td><td>answer twice too big (60.5 J instead of 30 J)</td><td>the ½ is the last thing you do: ÷ 2</td></tr>"
            "<tr><td>Wrong units</td><td>grams, km/h or kJ give wrong powers of ten</td><td>convert <i>before</i> you substitute: $g \\div 1000$, km/$h \\div 3.6$; give the answer in J then convert if asked</td></tr>"
            "<tr><td>Stopping at $v^{2}$</td><td>54 m/s instead of 7.4 m/s — loses the last mark</td><td>the last line is always $v = \\sqrt{\\ldots}$; sense-check the size</td></tr></table>"
            "<p><b>Speed squared.</b> Because $v$ is squared, doubling the speed makes the KE four times bigger; trebling it, nine times. That is why braking distance goes up with $v^{2}$ (the brakes have four times the energy to remove), and why a small increase in speed makes a crash much worse.</p>"
            "<p><b>Standard form.</b> Answers like 153 600 J are easy to get wrong by a zero. The examiners' advice: \"it often helps to put answers in standard form rather than risk writing too many or too few 000s\" — $1.5 \\times 10^{5}$ J.</p>",
        ),
        worked(
            "Speed from kinetic energy",
            "A 35 kg child has 950 J of kinetic energy. Calculate her speed. (3 marks)",
            [
                r"<b>Equation:</b> $KE = \tfrac{1}{2} m v^{2}$.",
                r"<b>Substitute:</b> $950 = \tfrac{1}{2} \times 35 \times v^{2}$.",
                r"<b>Rearrange:</b> $v^{2} = \dfrac{2 \times 950}{35} = 54.3$ (1 mark for this line).",
                r"<b>Square root:</b> $v = \sqrt{54.3} = 7.4$ m/s (the last mark).",
            ],
        ),
        practice("KE traps", [
            numeric("en-t3-q1", "A 900 kg car travels at 25 m/s. Calculate its kinetic energy. Give your answer in standard form.",
                    q3_1, "J", "½ × 900 × 625. Type the answer as 2.8125e5 or 281250.",
                    ewau(r"KE = \tfrac{1}{2} m v^{2}", r"KE = \tfrac{1}{2} \times 900 \times 25^{2} = \tfrac{1}{2} \times 900 \times 625", "281\\,250 = 2.8 \\times 10^{5}", "J")),
            numeric("en-t3-q2", "A golf ball of mass 45 g leaves the tee at 60 m/s. Calculate its kinetic energy.",
                    q3_2, "J", "45 g = 0.045 kg.",
                    ewau(r"KE = \tfrac{1}{2} m v^{2}", r"KE = \tfrac{1}{2} \times 0.045 \times 60^{2}", "81", "J")),
            numeric("en-t3-q3", "A 50 kg cyclist has 3600 J of kinetic energy. Calculate her speed.",
                    sf(q3_3, 2), "m/s", "$v^2 = 2 \\times 3600 \\div 50$, then square root.",
                    [r"$v^{2} = \dfrac{2 \times 3600}{50} = 144$.", r"$v = \sqrt{144} = 12$ m/s."]),
            group("en-t3-q4", "A 1500 kg van travels at 10 m/s, then speeds up to 30 m/s.", [
                numeric("en-t3-q4a", "Calculate its kinetic energy at 10 m/s.", q3_4_a, "J", "½ × 1500 × 100.",
                        ewau(r"KE = \tfrac{1}{2} m v^{2}", r"KE = \tfrac{1}{2} \times 1500 \times 10^{2}", "75\\,000", "J"), label="a"),
                numeric("en-t3-q4b", "Calculate its kinetic energy at 30 m/s.", q3_4_b, "J", "Three times the speed → nine times the KE.",
                        ewau(r"KE = \tfrac{1}{2} m v^{2}", r"KE = \tfrac{1}{2} \times 1500 \times 30^{2}", "675\\,000", "J — nine times as much"), label="b"),
                written("en-t3-q4c", "Explain why the braking distance at 30 m/s is much more than three times the braking distance at 10 m/s. (2)",
                        marks(["The brakes must do <b>work equal to the kinetic energy</b> to stop the van, and KE $\\propto v^{2}$, so there is <b>nine times</b> as much energy to transfer.",
                               "With the same braking force, work = force × distance, so the braking distance is about <b>nine times</b> as long, not three."]), lines=3, label="c"),
            ]),
            numeric("en-t3-q5", "An aircraft of mass 2.5 × 10⁵ kg lands at 80 m/s. Calculate its kinetic energy. Give your answer in standard form.",
                    q3_5, "J", "Enter 2.5 ×10ˣ 5 on the calculator. Type the answer as 8e8.",
                    ewau(r"KE = \tfrac{1}{2} m v^{2}", r"KE = \tfrac{1}{2} \times 2.5 \times 10^{5} \times 80^{2}", "8.0 \\times 10^{8}", "J")),
            choice("en-t3-q6", "A student calculates the KE of a 2 kg ball moving at 3 m/s as $\\tfrac{1}{2} \\times 2^2 \\times 3 = 6$ J. What has gone wrong?",
                   ["Nothing, 6 J is right", "The mass has been squared instead of the speed; it should be $\\tfrac{1}{2} \\times 2 \\times 3^2 = 9$ J", "The ½ should not be there", "The units are wrong"], 1,
                   "Only the speed is squared. $\\tfrac{1}{2} \\times 2 \\times 9 = 9$ J."),
        ]),
    ],
)
section_t3["subtopic"] = ["3", "8"]

# ---------------------------------------------------------------------
# T4 · Work done the hard way
# ---------------------------------------------------------------------

q4_1 = 1200 * 15
q4_2 = 0.5 * 1000 * 20 ** 2 / 50
q4_3 = 0.5 * 800 * 12 ** 2 / 4000
q4_4 = 150 * 2.0
# 4.5: pull a 12 kg box 3 m up a ramp with 50 N; vertical rise 1.0 m
q4_5_work = 50 * 3.0
q4_5_gpe = 12 * G * 1.0
q4_5_wasted = q4_5_work - q4_5_gpe

section_t4 = section(
    "work-hard", "tricky", "Work done the hard way", "8.5, 8.6, 8.7",
    equations=[r"E = F \times d", r"\text{work done by brakes} = KE", r"\text{work done lifting} = m g \Delta h"],
    blurb="Work done links force and distance to energy, so it joins Topic 2 to Topic 8. Three uses: work done by a braking force, work done lifting against gravity, and work done against friction up a ramp.",
    checklist=[
        "Use work done = KE to find a braking force or braking distance",
        "Use work done = weight × height for lifting, and compare it with the work actually put in",
        "Find the energy wasted as the difference between work done and useful energy gained",
        "Use only the distance moved in the direction of the force",
    ],
    parts=[
        explain(
            "Three set-ups",
            "<p><b>1. Brakes.</b> To stop a moving vehicle the brakes must transfer all of its kinetic energy to the thermal store. The work done by the braking force equals the KE:</p>"
            "<p>$$F \\times d = \\tfrac{1}{2} m v^{2}$$</p>"
            "<p>Given the KE and the braking force, this gives the braking distance; given the KE and the distance, it gives the force. It is also the proof that braking distance $\\propto v^{2}$.</p>"
            "<p><b>2. Lifting.</b> The force needed to lift something steadily is its weight, $m g$, so the work done lifting it through a height $h$ is $m g h$ — which is the GPE it gains. If a machine is used (a pulley, a ramp), the work the person does is <i>force applied × distance the person pulls</i>, and it is always <b>more</b> than $m g h$: the difference is wasted (friction, stretching the rope, lifting the pulley itself).</p>"
            "<p><b>3. Ramps.</b> Pushing a box up a ramp: work done = push × distance <b>along the ramp</b> (that is the direction of the force). GPE gained = $m g$ × <b>vertical</b> height. Work done − GPE gained = energy transferred to the thermal store by friction.</p>"
            "<p>The June 2025 Paper 2 report warns about mixing up <b>work done</b> (force × distance moved) and <b>moment</b> (force × perpendicular distance from a pivot) — both are \"force × distance\" but they are different things, and confusing them capped a 6-mark answer at level 2.</p>",
        ),
        worked(
            "Braking distance from work done",
            "A 1000 kg car travelling at 20 m/s brakes with a constant force of 5000 N. Calculate the braking distance.",
            [
                r"<b>KE to remove:</b> $KE = \tfrac{1}{2} m v^{2} = \tfrac{1}{2} \times 1000 \times 20^{2} = 200\,000$ J.",
                r"<b>Work done by brakes = KE:</b> $F \times d = 200\,000$.",
                r"<b>Rearrange:</b> $d = \dfrac{200\,000}{5000} = 40$ m.",
            ],
        ),
        practice("Work done", [
            numeric("en-t4-q1", "A 1200 N braking force stops a car in 15 m. Calculate the kinetic energy the car had.",
                    q4_1, "J", "Work done by the brakes = KE.",
                    ewau(r"E = F \times d", r"E = 1200 \times 15", "18\\,000", "J")),
            numeric("en-t4-q2", "A 1000 kg car travelling at 20 m/s stops in 50 m. Calculate the average braking force.",
                    q4_2, "N", "$\\text{KE} = \\tfrac{1}{2} m v^2$, then $F = E \\div d$.",
                    [r"$KE = \tfrac{1}{2} \times 1000 \times 20^{2} = 200\,000$ J.", r"$F = \dfrac{E}{d} = \dfrac{200\,000}{50} = 4000$ N."]),
            numeric("en-t4-q3", "An 800 kg car travelling at 12 m/s brakes with a force of 4000 N. Calculate its braking distance.",
                    q4_3, "m", "$d = \\text{KE} \\div F$.",
                    [r"$KE = \tfrac{1}{2} \times 800 \times 12^{2} = 57\,600$ J.", r"$d = \dfrac{57\,600}{4000} = 14.4$ m."]),
            numeric("en-t4-q4", "A box weighing 150 N is lifted 2.0 m onto a shelf. Calculate the minimum work done.",
                    q4_4, "J", "The lifting force equals the weight.",
                    ewau(r"E = F \times d", r"E = 150 \times 2.0", "300", "J")),
            group("en-t4-q5", "A student pushes a 12 kg box 3.0 m up a ramp with a force of 50 N along the ramp. The top of the ramp is 1.0 m above the bottom. ($g = 10$ N/kg)", [
                numeric("en-t4-q5a", "Calculate the work done by the student.", q4_5_work, "J", "Force × distance along the ramp.",
                        ewau(r"E = F \times d", r"E = 50 \times 3.0", "150", "J"), label="a"),
                numeric("en-t4-q5b", "Calculate the GPE gained by the box.", q4_5_gpe, "J", "m g × vertical height.",
                        ewau(r"\Delta GPE = m g \Delta h", r"\Delta GPE = 12 \times 10 \times 1.0", "120", "J"), label="b"),
                numeric("en-t4-q5c", "Calculate the energy transferred to the thermal store by friction.", q4_5_wasted, "J", "Work done − GPE gained.",
                        [r"$150 - 120 = 30$ J, dissipated by friction between the box and the ramp."], label="c"),
            ]),
            written("en-t4-q6", "A pulley system lifts a 20 kg load through 1.5 m. The person pulling the rope does 400 J of work. Explain why this is more than the GPE gained by the load. (3)",
                    mark_scheme([
                        ("GPE", "GPE gained $= 20 \\times 10 \\times 1.5 = 300$ J, which is less than 400 J."),
                        ("Reason 1", "Work is also done <b>lifting the pulley and rope</b> themselves (they have weight) / <b>stretching the rope</b>."),
                        ("Reason 2", "Work is done against <b>friction</b> in the pulley, transferring energy to the <b>thermal store</b> of the surroundings."),
                    ], extra=["The June 2023 scheme accepted the mass of the pulley/rope or the rope stretching; it ignored \"pulling at an angle\" and vague references to the person."]), lines=4),
        ]),
    ],
)
section_t4["subtopic"] = ["8"]

# ---------------------------------------------------------------------
# T5 · Power the hard way
# ---------------------------------------------------------------------

q5_1 = 75 * G * 0.20 * 25 / 60
q5_2 = 2000 * 1.5 * 60
q5_3 = 150e3 / (2.5e3)
q5_4 = 1.2e6 / 3.0e3 / 60
q5_5 = 500 * 8

section_t5 = section(
    "power-hard", "tricky", "Power the hard way", "8.12, 8.13",
    equations=[r"P = \dfrac{E}{t}", r"E = P \times t", r"t = \dfrac{E}{P}"],
    blurb="The power equation is easy; the questions are not, because the energy usually has to be found first (from m g Δh, ½ $m v^2$ or $F \\times d$) and the time is rarely given in seconds.",
    checklist=[
        "Find the energy first (GPE, KE or work done), then divide by the time",
        "Convert minutes and hours to seconds, kW to W, MJ to J",
        "Rearrange for energy or time",
        "Describe the step-ups / stairs experiment for measuring a person's power",
    ],
    parts=[
        explain(
            "The chain, and the units",
            "<p>Most power questions are two steps: <b>energy first, then divide by time.</b></p>"
            "<table class='tbl'><tr><th>Situation</th><th>Energy to find</th><th>Then</th></tr>"
            "<tr><td>person or motor lifting</td><td>$E = m g \\Delta h$ (weight × height)</td><td rowspan='3'>$P = \\dfrac{E}{t}$</td></tr>"
            "<tr><td>something accelerating</td><td>$E = \\tfrac{1}{2} m v^{2}$</td></tr>"
            "<tr><td>force moving something</td><td>$E = F \\times d$</td></tr></table>"
            "<p>Units that catch people: a <b>kW</b> is 1000 W; a <b>MJ</b> is $10^{6}$ J; <b>minutes × 60</b> and <b>hours × 3600</b> for seconds. The June 2023 Paper 2 scheme gave one mark of two for \"7.2\" when the answer was 2.0 h — a time conversion missed.</p>"
            "<p><b>Significant figures:</b> \"give your answer to 2 significant figures\" is a mark. 409.41 W → 410 W, not 409 (that is 3 s.f.) and not 409.4. The June 2025 report: \"significant figures were often confused with decimal places\".</p>"
            "<p><b>Measuring your own power</b> (the suggested practical): measure your <b>mass</b> on bathroom scales and find your weight ($m g$); measure the <b>height</b> of a step or flight of stairs with a metre rule; <b>time</b> yourself climbing with a stopwatch; energy = weight × height; power = energy ÷ time. Repeat and average the time.</p>",
        ),
        worked(
            "Power of a student doing step-ups",
            "A student of mass 75 kg steps up onto a 20 cm high box 25 times in 60 s. Calculate her average power. ($g = 10$ N/kg)",
            [
                r"<b>Height climbed in total:</b> $25 \times 0.20 = 5.0$ m (centimetres to metres).",
                r"<b>Energy:</b> $E = m g \Delta h = 75 \times 10 \times 5.0 = 3750$ J.",
                r"<b>Power:</b> $P = \dfrac{E}{t} = \dfrac{3750}{60} = 62.5$ W $\approx 63$ W.",
            ],
        ),
        practice("Power", [
            numeric("en-t5-q1", "A 75 kg student steps onto a 20 cm box 25 times in 60 s. Calculate her average power. ($g = 10$ N/kg)",
                    sf(q5_1, 3), "W", "Total height = 25 × 0.20 m.",
                    [r"$\Delta h = 25 \times 0.20 = 5.0$ m; $E = 75 \times 10 \times 5.0 = 3750$ J.", r"$P = \dfrac{3750}{60} = 62.5$ W."]),
            numeric("en-t5-q2", "A 2 kW kettle runs for 1.5 minutes. Calculate the energy transferred.",
                    q5_2, "J", "2000 W × 90 s.",
                    ewau(r"E = P \times t", r"E = 2000 \times 90", "180\\,000", "J")),
            numeric("en-t5-q3", "A crane motor rated at 2.5 kW lifts a load, giving it 150 kJ of GPE. Calculate the minimum time this takes.",
                    q5_3, "s", "$t = E \\div P$, both in base units.",
                    ewau(r"t = \dfrac{E}{P}", r"t = \dfrac{150 \times 10^{3}}{2.5 \times 10^{3}}", "60", "s")),
            numeric("en-t5-q4", "A 3.0 kW heater transfers 1.2 MJ to a room. Calculate how long it was on, in minutes.",
                    sf(q5_4, 3), "min", "Find the seconds, then ÷ 60.",
                    [r"$t = \dfrac{E}{P} = \dfrac{1.2 \times 10^{6}}{3.0 \times 10^{3}} = 400$ s.", r"$400 \div 60 = 6.67$ min."]),
            numeric("en-t5-q5", "A cyclist pushes with a force of 500 N while travelling at a steady 8 m/s. Calculate her power output.",
                    q5_5, "W", "In 1 s she moves 8 m, so work done per second = $F \\times 8$.",
                    [r"Work done each second $= F \times d = 500 \times 8 = 4000$ J.", r"So $P = 4000$ W (power = force × speed)."]),
            written("en-t5-q6", "Describe how a student could measure their own power by running up a flight of stairs. (4)",
                    mark_scheme([
                        ("Weight", "Measure <b>mass</b> with scales and find the <b>weight</b> ($W = m g$)."),
                        ("Height", "Measure the <b>vertical height</b> of the stairs with a metre rule (one step × number of steps)."),
                        ("Time", "<b>Time</b> the run with a stopwatch."),
                        ("Calculate", "Energy = <b>weight × height</b>; power = <b>energy ÷ time</b>."),
                        ("Repeat", "<b>Repeat and calculate a mean</b> time."),
                    ], total=4), lines=5, hint="Three measurements with instruments, then the two calculations."),
        ]),
    ],
)
section_t5["subtopic"] = ["8"]

# ---------------------------------------------------------------------
# T6 · Efficiency the hard way
# ---------------------------------------------------------------------

q6_1 = 0.27  # efficiency given
q6_1_in = 2.16e6 / 0.27
q6_2 = 60 * 0.4
q6_3_in = 500 * G * 4.0
q6_3_eff = (500 * G * 4.0) / 25000
q6_4 = 0.9 * 0.5
q6_5 = 1500 / 0.75

section_t6 = section(
    "efficiency-hard", "tricky", "Efficiency the hard way", "3.11, 3.12, 8.15",
    equations=[r"\text{total in} = \dfrac{\text{useful out}}{\text{efficiency}}", r"\text{wasted} = \text{total} - \text{useful}"],
    blurb="The hard efficiency questions make you find the input from the output, chain two efficiencies, or explain how to make something more efficient. The decimal-versus-percentage trap is in all of them.",
    checklist=[
        "Find the total input from the useful output and the efficiency",
        "Find the efficiency of a motor from m g Δh and the electrical energy supplied",
        "Explain how the efficiency of a device can be increased (reduce the wasted transfer)",
        "Sense-check: input bigger than useful output, efficiency below 1",
    ],
    parts=[
        explain(
            "Working backwards, and chaining",
            "<p>$$\\text{efficiency} = \\dfrac{\\text{useful}}{\\text{total}} \\quad\\Rightarrow\\quad \\text{total} = \\dfrac{\\text{useful}}{\\text{efficiency}}$$</p>"
            "<p>A 27% efficient solar panel that must deliver 2.16 MJ needs $2.16 \\div 0.27 = 8.0$ MJ of sunlight. The June 2022 report called this \"mathematically challenging for many\"; the candidate who scored wrote \"0.27 × asked-for input = given output\" and solved it.</p>"
            "<p><b>Two stages:</b> if a power station is 40% efficient and the cables are 90% efficient, the fraction delivered is $0.40 \\times 0.90 = 0.36$ — multiply the decimals.</p>"
            "<p><b>Increasing efficiency</b> (spec 3.12) means <b>reducing the wasted transfer</b>, so the answer is always one of: <b>lubricate</b> moving parts (less friction); <b>insulate</b> (less transfer to surroundings by heating); <b>streamline</b> (less air resistance); use <b>thicker wires</b> / lower-current transmission (less heating of wires); <b>replace</b> a filament lamp with an LED. Say what is wasted, then how you reduce it.</p>",
        ),
        worked(
            "Efficiency of a motor from a lift",
            "A motor is supplied with 25 000 J of energy and lifts a 500 kg load through 4.0 m. Calculate its efficiency. ($g = 10$ N/kg)",
            [
                r"<b>Useful energy:</b> $\Delta GPE = m g \Delta h = 500 \times 10 \times 4.0 = 20\,000$ J.",
                r"<b>Efficiency:</b> $\dfrac{\text{useful}}{\text{total}} = \dfrac{20\,000}{25\,000} = 0.80$, or 80%.",
                r"<b>Sense check:</b> below 1 ✓; the other 5000 J is in the thermal store of the motor and surroundings.",
            ],
        ),
        practice("Efficiency", [
            numeric("en-t6-q1", "A solar panel is 27% efficient. It must transfer 2.16 MJ usefully. Calculate the energy that must fall on it, in MJ.",
                    sf(2.16 / 0.27, 2), "MJ", "total = useful ÷ 0.27 — the input must be bigger.",
                    ewau(r"\text{total} = \dfrac{\text{useful}}{\text{efficiency}}", r"\text{total} = \dfrac{2.16}{0.27}", "8.0", "MJ")),
            numeric("en-t6-q2", "A 60 W filament lamp is 40% efficient. Calculate the wasted power.",
                    60 - q6_2, "W", "Useful = 0.4 × 60; wasted = total − useful.",
                    [r"Useful $= 0.40 \times 60 = 24$ W.", r"Wasted $= 60 - 24 = 36$ W, transferred by heating to the surroundings."]),
            group("en-t6-q3", "A lift motor is supplied with 25 000 J and raises a 500 kg lift car through 4.0 m. ($g = 10$ N/kg)", [
                numeric("en-t6-q3a", "Calculate the useful energy transferred to the lift car.", q6_3_in, "J", "m g Δh.",
                        ewau(r"\Delta GPE = m g \Delta h", r"\Delta GPE = 500 \times 10 \times 4.0", "20\\,000", "J"), label="a"),
                numeric("en-t6-q3b", "Calculate the efficiency of the motor as a decimal.", q6_3_eff, "", "useful ÷ total.",
                        ewau(r"\text{efficiency} = \dfrac{\text{useful}}{\text{total}}", r"\text{efficiency} = \dfrac{20\,000}{25\,000}", "0.80", "no unit"), label="b", tolerance=0.02),
            ]),
            numeric("en-t6-q4", "A power station is 50% efficient and the cables carrying its electricity are 90% efficient. Calculate the overall efficiency from fuel to home, as a decimal.",
                    q6_4, "", "Multiply the two decimals.",
                    [r"$0.50 \times 0.90 = 0.45$ — 45% of the fuel's energy reaches the home."], tolerance=0.02),
            numeric("en-t6-q5", "A pump is 75% efficient and transfers 1500 J usefully to the water each second. Calculate the power supplied to the pump.",
                    q6_5, "W", "total = useful ÷ 0.75.",
                    ewau(r"\text{total} = \dfrac{\text{useful}}{\text{efficiency}}", r"\text{total} = \dfrac{1500}{0.75}", "2000", "W")),
            written("en-t6-q6", "Explain how the efficiency of an electric motor could be increased. (2)",
                    marks(["Energy is wasted by <b>friction</b> in the bearings (transferred to the thermal store of the surroundings)…",
                           "…so <b>lubricate</b> the bearings to <b>reduce friction</b>, so less of the input energy is wasted and a larger fraction is transferred usefully."]), lines=3,
                    hint="Name the wasted transfer, then say how to reduce it."),
            written("en-t6-q7", "A student calculates that an oven supplied with 1200 kJ transfers 1500 kJ to the food. Explain why this cannot be right. (2)",
                    marks(["The useful output cannot be <b>more than the input</b> — energy <b>cannot be created</b> (conservation of energy).",
                           "So the efficiency would be more than 1 (125%), which is impossible; the student has probably swapped the useful and total values or used 55 instead of 0.55."]), lines=3),
        ]),
    ],
)
section_t6["subtopic"] = ["3", "8"]

SECTIONS = [section_t1, section_t2, section_t3, section_t4, section_t5, section_t6]
