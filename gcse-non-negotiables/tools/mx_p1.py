"""
mx_p1.py — Mixed-topic questions: the opening section on finding the
join (band "start", M1) and the Paper 1 blends (band "p1", P1-1 … P1-6).

Each section is a blend the examiners set repeatedly: the chain is
given as a table (quantity → equation → unit at the hand-over), a worked
example modelled on a real question with new numbers, and a multi-part
practice group. The physics of each stage lives on its topic page; here
the practice is the hand-over.

M1   Finding the join
P1-1 GPE → KE → speed, then acceleration or dissipation (2 + 3)
P1-2 Momentum, force and time, then kinetic energy (2 + 3 + 6)
P1-3 Stopping distances as work and energy (2 + 3 + 8)
P1-4 The wave equation on light (4 + 5)
P1-5 Radioactivity meets energy (6 + 3 + 7)
P1-6 Thermal balance (5 + 7 + 3)
"""

from revlib import (
    axis, choice, ewau, explain, fact, graph, group, line, curve, marks,
    numeric, practice, section, worked, written, sample,
)

# ---------------------------------------------------------------------
# M1 · Finding the join
# ---------------------------------------------------------------------

section_m1 = section(
    "join", "start", "Finding the join: how a blended question hands over from one topic to the next", "all topics",
    equations=[r"\text{stage 1} \xrightarrow{\ \text{one quantity}\ } \text{stage 2} \xrightarrow{\ \text{one quantity}\ } \text{stage 3}"],
    blurb="A long exam question rarely stays in one topic. It hands a quantity from one topic to the next — an energy, a force, a volume, a potential difference — and the marks sit at those hand-overs: the right equation picked for each stage, the units matched at the join, the number carried forward (even a wrong one), and each stage labelled so the examiner can give the stage its mark.",
    checklist=[
        "Name the quantity that each stage hands to the next before starting the arithmetic",
        "Convert units at the join (kJ to J, cm to m, g to kg, minutes to seconds) before the next equation",
        "Carry a stage's answer forward and label every stage, so error carried forward can score",
    ],
    parts=[
        explain(
            "The four habits",
            "<table class='tbl'><tr><th>Habit</th><th>Why it scores</th><th>Example</th></tr>"
            "<tr><td><b>Find the join</b></td><td>each stage of a chain has its own equation; the output of one is the input of the next</td><td>GPE from a height → the <i>same number</i> as KE → a speed from $\\tfrac{1}{2}mv^2$</td></tr>"
            "<tr><td><b>Match units at the join</b></td><td>the examiners' reports name the same slips every year: kJ left as kJ, cm in a squared term, minutes into $E = Pt$, mm² into $P = F/A$</td><td>$E = Pt$ needs seconds: 5.0 minutes is 300 s</td></tr>"
            "<tr><td><b>Carry forward and label</b></td><td>mark schemes give a mark per stage and allow \"error carried forward\" — a wrong stage 1 still lets stages 2 and 3 score if they use it correctly and are shown</td><td>June 2025 2H Q9(a)(ii): starting from the wrong upthrust still scored 3 of 4</td></tr>"
            "<tr><td><b>Check the join makes sense</b></td><td>a speed of 300 m/s for a trolley, a pool 35 m deep, a spring constant of 2.5 N/m for a stiff spring — the number itself tells you a join went wrong</td><td>\"look at the result of a calculation to see if the value makes sense\" (June 2025 report)</td></tr></table>"
            "<p>The chains on this page are the ones that have come up in the June 2023, 2024 and 2025 papers. Each section names the join, lays the chain out as a table, and works one example modelled on the real question with new numbers. The physics of each stage is on its topic page — this page practises the hand-over.</p>",
        ),
        worked(
            "A trolley, a runway and a staircase",
            "A trolley is lifted onto a runway 0.30 m high and gains 4.8 J of gravitational potential energy. (a) Show that the mass of the trolley is about 1.6 kg. (b) Calculate the speed the trolley would have at the bottom of the runway if all the GPE became kinetic energy. (c) The measured speed is 2.1 m/s. Suggest why. (d) A student of mass 52 kg runs up a 3.0 m staircase in 4.0 s; calculate her power. ($g = 10$ N/kg; 9 marks)",
            [
                "(a) Stage 1, Topic 3: $\\Delta GPE = m g \\Delta h$, so $m = \\Delta GPE \\div (g \\Delta h) = 4.8 \\div (10 \\times 0.30) = 1.6$ kg.",
                "(b) <b>The join</b>: the GPE <i>is</i> the KE at the bottom — 4.8 J hands over. $KE = \\tfrac{1}{2} m v^2$, so $v^2 = 2 KE \\div m = 2 \\times 4.8 \\div 1.6 = 6.0$.",
                "$v = \\sqrt{6.0} = 2.4$ m/s (2.45) — a sensible trolley speed.",
                "(c) The measured speed is lower because some of the energy is <b>transferred to the surroundings by friction and air resistance</b> (dissipated as heating), so less than 4.8 J is in the kinetic store — not \"energy is lost\".",
                "(d) Stage 3, Topic 8: work done against gravity $= m g h = 52 \\times 10 \\times 3.0 = 1560$ J; power $= E \\div t = 1560 \\div 4.0 = 390$ W (2 s.f.).",
            ],
        ),
        practice("Finding the join", [
            group("mx-m1-q1", "A 0.50 kg ball is dropped from a height of 1.8 m. $g = 10$ N/kg.", [
                numeric("mx-m1-q1a", "Calculate the gravitational potential energy it loses as it falls.", 9.0, "J",
                        "$\\Delta \\text{GPE} = m g \\Delta h$.",
                        ewau(r"\Delta GPE = m g \Delta h", r"\Delta GPE = 0.50 \times 10 \times 1.8", "9.0", "J"), label="a"),
                numeric("mx-m1-q1b", "Calculate its speed just before it lands, assuming no air resistance.", 6.0, "m/s",
                        "The 9.0 J hands over to KE: $v^2 = 2\\text{KE} \\div m$.",
                        [r"$KE = 9.0$ J (the join)", r"$v^2 = 2 KE \div m = 2 \times 9.0 \div 0.50 = 36$", r"$v = 6.0$ m/s"], label="b"),
                written("mx-m1-q1c", "The measured landing speed is 5.6 m/s. Explain the difference. (2)",
                        marks(["Some of the energy is <b>transferred to the surroundings</b> by <b>air resistance</b> (work done against it, dissipated by heating), so less than 9.0 J is in the kinetic store.", "A smaller KE means a smaller speed — $v = \\sqrt{2 KE / m}$ (do not say the energy is \"lost\": say where it went)."]), lines=2, label="c"),
            ]),
            choice("mx-m1-q2", "In a chain calculation, stage 1 gives a wrong energy. What should you do in stage 2?",
                   ["Stop — no more marks are available", "Use the wrong value, show the working, and label the stage: error carried forward lets stage 2 score", "Guess a better value", "Leave stage 2 blank"], 1,
                   "Mark schemes give a mark per stage."),
            choice("mx-m1-q3", "A heater of power 60 W runs for 5.0 minutes before its energy goes into $\\Delta Q = mc\\Delta\\theta$. The join needs…",
                   ["$E = 60 \\times 5.0 = 300$ J", "$E = 60 \\times 300 = 18\\,000$ J, because t must be in seconds", "$E = 60 \\div 5.0$ J", "no conversion"], 1,
                   "Minutes to seconds at the join."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# P1-1 · GPE → KE → speed, then acceleration or dissipation
# ---------------------------------------------------------------------

section_a1 = section(
    "gpe-ke-speed", "p1", "GPE to KE to speed, then acceleration or dissipation", "2.9, 2.10, 3.2–3.5",
    equations=[r"\Delta GPE = m g \Delta h \ \rightarrow\ KE = \tfrac{1}{2} m v^2 \ \rightarrow\ v", r"\text{dissipated} = \Delta GPE - KE_{\text{measured}}"],
    blurb="The skier, the trolley, the roller coaster, the falling ball: a height becomes an energy, the energy becomes a speed, and then the question turns a corner — into an acceleration over the slope (Topic 2) or into the energy dissipated (Topic 3). The joins are the energy ($GPE = KE$) and the speed (into the equation of motion).",
    checklist=[
        "Hand the GPE over as KE and get the speed from $\\tfrac{1}{2}mv^2$",
        "Hand the measured speed on to the next stage — an acceleration (Higher) or a comparison with the expected speed",
        "Find the energy dissipated as GPE − KE and say where it went",
    ],
    parts=[
        explain(
            "The chain",
            "<table class='tbl'><tr><th>Stage</th><th>Equation</th><th>Hands over</th><th>Watch</th></tr>"
            "<tr><td>height → energy</td><td>$\\Delta GPE = m g \\Delta h$ (Topic 3)</td><td>an energy in J</td><td>$\\Delta h$ is the vertical height, not the slope length</td></tr>"
            "<tr><td>energy → speed</td><td>$KE = \\tfrac{1}{2} m v^2$, so $v = \\sqrt{2 KE \\div m}$</td><td>a speed in m/s</td><td>square-root at the end; a kJ must become J first</td></tr>"
            "<tr><td>speed → acceleration</td><td>$v^2 - u^2 = 2 a x$ (Topic 2) [H]</td><td>$a$ in m/s²</td><td>$x$ is the distance along the slope; $u = 0$ from rest</td></tr>"
            "<tr><td>measured speed → dissipation</td><td>energy dissipated $= \\Delta GPE - \\tfrac{1}{2} m v_{\\text{measured}}^2$</td><td>an energy in J</td><td>say where it went: work against friction / air resistance, transferred to the surroundings by heating</td></tr></table>"
            "<p>June 2025 1H Q6: a skier's height from $\\Delta GPE$ (2), then the acceleration from rest to 27 m/s over a 200 m slope (3), then \"explain how to determine the energy dissipated\" (2) — measure the speed at the bottom, find the KE, subtract from the GPE. June 2025 2H Q2 did the same with a trolley (mass from the GPE, expected velocity, one way to reduce the gap). The \"suggest one way to reduce the gap\" mark is a practical one: reduce friction (lubricate the wheels, a smoother runway) or air resistance.</p>",
        ),
        worked(
            "The skier",
            "A skier of mass 64 kg starts from rest at the top of a slope and loses 32 000 J of gravitational potential energy on the way down. (a) Calculate the height of the slope. (b) Calculate the speed at the bottom if no energy were dissipated. (c) Her actual speed at the bottom is 25 m/s; calculate the energy dissipated and say where it went. ($g = 10$ N/kg; 6 marks)",
            [
                "(a) $\\Delta h = \\Delta GPE \\div (m g) = 32\\,000 \\div (64 \\times 10) = 50$ m.",
                "(b) Join: $KE = 32\\,000$ J. $v^2 = 2 KE \\div m = 2 \\times 32\\,000 \\div 64 = 1000$, so $v = 32$ m/s (31.6).",
                "(c) Actual $KE = \\tfrac{1}{2} \\times 64 \\times 25^2 = 20\\,000$ J; dissipated $= 32\\,000 - 20\\,000 = 12\\,000$ J, transferred to the surroundings by work done against friction and air resistance.",
            ],
        ),
        practice("GPE to KE to speed", [
            group("mx-a1-q1", "A roller-coaster car of mass 500 kg is released from rest at the top of a 40 m drop. $g = 10$ N/kg.", [
                numeric("mx-a1-q1a", "Calculate the gravitational potential energy lost in the drop.", 200000, "J",
                        "$m g \\Delta h$.",
                        ewau(r"\Delta GPE = m g \Delta h", r"\Delta GPE = 500 \times 10 \times 40", "200\\,000", "J"), label="a"),
                numeric("mx-a1-q1b", "Calculate the speed at the bottom if all of this becomes kinetic energy.", 28.3, "m/s",
                        "$v = \\sqrt{2\\,KE \\div m}$.",
                        [r"$v^2 = 2 \times 200\,000 \div 500 = 800$", r"$v = \sqrt{800} = 28$ m/s (28.3)"], label="b"),
                numeric("mx-a1-q1c", "The measured speed at the bottom is 26 m/s. Calculate the energy dissipated during the drop.", 31000, "J",
                        "GPE − actual KE.",
                        [r"$KE = \tfrac{1}{2} \times 500 \times 26^2 = 169\,000$ J", r"dissipated $= 200\,000 - 169\,000 = 31\,000$ J"], label="c"),
                numeric("mx-a1-q1d", "The track from the top to the bottom is 120 m long. Use the measured speed to calculate the average acceleration along the track.", 2.82, "m/s²",
                        "$v^2 - u^2 = 2ax$ with $u = 0$.",
                        ewau(r"v^2 - u^2 = 2 a x", r"26^2 - 0 = 2 \times a \times 120", "2.8", "m/s² (2.82)"), label="d", tags=["H"]),
            ]),
            written("mx-a1-q2", "Describe how a student could determine the energy dissipated as a trolley runs down a ramp. (3)",
                    marks(["Measure the <b>vertical height</b> of the start above the bottom and the trolley's <b>mass</b>; calculate $\\Delta GPE = m g \\Delta h$.", "Measure the trolley's <b>speed at the bottom</b> (light gate and interrupt card, or distance and time) and calculate $KE = \\tfrac{1}{2} m v^2$.", "Energy dissipated $= \\Delta GPE - KE$ — the difference transferred to the surroundings by friction and air resistance."]), lines=3),
            choice("mx-a1-q3", "A student uses the slope length (200 m) as $\\Delta h$ in $m g \\Delta h$. The GPE comes out…",
                   ["correct", "too large — Δh is the vertical height (50 m), not the distance along the slope", "too small", "in the wrong unit"], 1,
                   "Height is vertical; the slope length belongs in $v^2 - u^2 = 2ax$."),
        ]),
    ],
)

# ---------------------------------------------------------------------
# P1-2 · Momentum, force and time, then kinetic energy
# ---------------------------------------------------------------------

section_a2 = section(
    "momentum-force-ke", "p1", "Momentum, force and time, then kinetic energy", "2.20–2.26, 3.3",
    tags=["H"],
    equations=[r"p = m v \ \rightarrow\ F = \dfrac{\Delta(mv)}{t}", r"KE = \tfrac{1}{2} m v^2"],
    blurb="A kick, a collision, a beta particle leaving a nucleus: the same mass and speed feed three different equations. Momentum ($mv$) goes into the force–time equation and into conservation; kinetic energy ($\\tfrac{1}{2}mv^2$) answers the energy part. The join is the speed, and the trap is giving $\\tfrac{1}{2}mv^2$ when momentum was asked for.",
    checklist=[
        "Find momentum, then the force from the change in momentum and the contact time",
        "Explain a collision with conservation of momentum and Newton's third law",
        "Find the kinetic energy of the same object, including a beta particle from its mass and speed",
    ],
    parts=[
        explain(
            "The chain",
            "<table class='tbl'><tr><th>Stage</th><th>Equation</th><th>Hands over</th><th>Watch</th></tr>"
            "<tr><td>mass and speed → momentum</td><td>$p = m v$ (Topic 2) [H]</td><td>$p$ in kg m/s</td><td>the unit mark is often separate: kg m/s</td></tr>"
            "<tr><td>momentum → force or time</td><td>$F = \\Delta(mv) \\div t$ [H]</td><td>$F$ in N, or $t$ in s</td><td>$\\Delta(mv)$ is the <i>change</i>: from rest it equals $mv$</td></tr>"
            "<tr><td>collision → shared speed</td><td>total momentum before = total momentum after [H]</td><td>$v$ after</td><td>the combined mass is larger, so the speed is smaller than the moving trolley's</td></tr>"
            "<tr><td>same mass and speed → energy</td><td>$KE = \\tfrac{1}{2} m v^2$ (Topic 3)</td><td>$KE$ in J</td><td>square the speed; for a beta particle keep the powers of ten: $9.1 \\times 10^{-31}$ kg</td></tr></table>"
            "<p>June 2025 1H Q8: momentum of a kicked ball with its unit (3), the contact time from the force (2), Newton's third law on foot and ball (3), and why two trolleys that stick together move more slowly than the moving one did (3). Q9(a)(iii) on the same paper: the kinetic energy of a beta particle from $m = 9.1 \\times 10^{-31}$ kg and $v = 3.8 \\times 10^{6}$ m/s. The third-law explanation needs the <b>pair</b> named (the force of the foot on the ball and the force of the ball on the foot), <b>equal in size</b>, <b>opposite in direction</b>, on <b>different objects</b> — Topic 2 N15.</p>",
        ),
        worked(
            "The kick",
            "A football of mass 0.45 kg is kicked from rest and leaves the boot at 30 m/s. (a) Calculate its momentum. (b) The boot is in contact with the ball for 0.0060 s; calculate the average force on the ball. (c) Calculate the ball's kinetic energy. (d) The ball then hits a stationary 0.45 kg ball and they move off together; calculate their speed. (9 marks)",
            [
                "(a) $p = m v = 0.45 \\times 30 = 13.5$ kg m/s [H].",
                "(b) $F = \\Delta(mv) \\div t = 13.5 \\div 0.0060 = 2250$ N (the change is the full 13.5 kg m/s because it started from rest) [H].",
                "(c) Same mass and speed, different equation: $KE = \\tfrac{1}{2} m v^2 = \\tfrac{1}{2} \\times 0.45 \\times 30^2 = 203$ J (202.5).",
                "(d) Momentum is conserved: $13.5 = (0.45 + 0.45) \\times v$, so $v = 15$ m/s — half, because the mass doubled [H]. (The KE after is $\\tfrac{1}{2} \\times 0.90 \\times 15^2 = 101$ J: half the KE has gone to heating and sound.)",
            ],
        ),
        practice("Momentum and energy", [
            group("mx-a2-q1", "A tennis ball of mass 0.058 kg is served from rest and leaves the racket at 50 m/s.", [
                numeric("mx-a2-q1a", "Calculate the momentum of the ball as it leaves the racket.", 2.9, "kg m/s",
                        "$p = m v$.",
                        ewau(r"p = m v", r"p = 0.058 \times 50", "2.9", "kg m/s"), label="a", tags=["H"]),
                numeric("mx-a2-q1b", "The racket is in contact with the ball for 0.0050 s. Calculate the average force on the ball.", 580, "N",
                        "$F = \\Delta(mv) \\div t$.",
                        ewau(r"F = \Delta(mv) \div t", r"F = 2.9 \div 0.0050", "580", "N"), label="b", tags=["H"]),
                numeric("mx-a2-q1c", "Calculate the kinetic energy of the ball.", 72.5, "J",
                        "$\\tfrac{1}{2} m v^2$.",
                        ewau(r"KE = \tfrac{1}{2} m v^2", r"KE = \tfrac{1}{2} \times 0.058 \times 50^2", "73", "J (72.5)"), label="c"),
                written("mx-a2-q1d", "Explain, using Newton's third law, why the racket strings are pushed back as the ball is hit. (3)",
                        marks(["The racket exerts a <b>force on the ball</b> (forwards); by Newton's third law the ball exerts a force <b>on the racket</b>.", "The two forces are <b>equal in size</b> and <b>opposite in direction</b>, and act on <b>different objects</b> (one on the ball, one on the racket).", "The force of the ball on the strings pushes them backwards (distorts them) while the ball accelerates forwards."]), lines=3, label="d"),
            ]),
            numeric("mx-a2-q2", "A 1500 kg car moving at 20 m/s is brought to rest in 2.5 s by a barrier. Calculate the average force on the car.", 12000, "N",
                    "Change in momentum ÷ time.",
                    [r"$\Delta(mv) = 1500 \times 20 - 0 = 30\,000$ kg m/s"] + ewau(r"F = \Delta(mv) \div t", r"F = 30\,000 \div 2.5", "12\\,000", "N")),
            written("mx-a2-q3", "Trolley S, moving at 0.60 m/s, collides with an identical stationary trolley T and they stick together. Explain, using momentum, why their combined velocity is less than 0.60 m/s. (3)",
                    marks(["Momentum is <b>conserved</b> in the collision: the total momentum after equals S's momentum before.", "After the collision the <b>same momentum is shared by twice the mass</b> (S and T together).", "Since $p = mv$, a larger mass with the same momentum has a <b>smaller velocity</b> — 0.30 m/s here."]), lines=3, tags=["H"]),
        ]),
    ],
)

# ---------------------------------------------------------------------
# P1-3 · Stopping distances as work and energy
# ---------------------------------------------------------------------

section_a3 = section(
    "stopping-energy", "p1", "Stopping distances as work and energy", "2.27–2.33P, 3.3, 8.1",
    tags=["P"],
    equations=[r"\text{braking force} \times \text{braking distance} = \tfrac{1}{2} m v^2", r"\text{thinking distance} = v \times \text{reaction time}"],
    blurb="A braking car is an energy question wearing a motion costume: the work done by the brakes equals the kinetic energy taken away, so braking force × braking distance $= \\tfrac{1}{2}mv^2$. That is why braking distance grows with the square of the speed, why a larger mass needs a longer distance, and why the brakes get hot. The join is the KE.",
    checklist=[
        "Find a braking distance from the kinetic energy and the braking force (or the force from the distance)",
        "Explain why braking distance is proportional to $v^2$ and thinking distance to $v$",
        "Add thinking and braking distances, and say where the kinetic energy goes",
    ],
    parts=[
        explain(
            "The chain",
            "<table class='tbl'><tr><th>Stage</th><th>Equation</th><th>Hands over</th><th>Watch</th></tr>"
            "<tr><td>speed → kinetic energy</td><td>$KE = \\tfrac{1}{2} m v^2$ (Topic 3)</td><td>an energy in J</td><td>square the speed: double the speed, four times the energy</td></tr>"
            "<tr><td>energy → braking distance</td><td>work done $= F \\times d$ (Topic 8), and $F d = KE$</td><td>$d$ in m, or $F$ in N</td><td>the braking force is roughly constant, so $d \\propto v^2$</td></tr>"
            "<tr><td>speed → thinking distance</td><td>distance $=$ speed $\\times$ reaction time (Topic 2)</td><td>$d$ in m</td><td>$\\propto v$, not $v^2$</td></tr>"
            "<tr><td>both → stopping distance</td><td>stopping $=$ thinking $+$ braking</td><td>—</td><td>the KE is transferred to the thermal store of the brakes (and surroundings) by the work done</td></tr></table>"
            "<p>Topic 2's stopping-distance questions ask for the <i>factors</i>; the blended version asks for the <i>numbers</i>, and the only route is through energy. June 2025 1H Q6(a)(iii) (\"explain how to determine the energy dissipated\") is the same idea in reverse. The $v^2$ explanation (2.32P–2.33P, Physics only): braking distance is proportional to the KE, and KE is proportional to $v^2$, so doubling the speed <b>quadruples</b> the braking distance while only doubling the thinking distance.</p>",
        ),
        worked(
            "A car braking",
            "A car of mass 1200 kg travels at 20 m/s. The driver's reaction time is 0.70 s and the brakes exert a constant force of 6000 N. (a) Calculate the thinking distance. (b) Calculate the car's kinetic energy. (c) Calculate the braking distance. (d) State the stopping distance. (e) Explain what would happen to the braking distance at 40 m/s. (8 marks)",
            [
                "(a) Thinking distance $= v t = 20 \\times 0.70 = 14$ m.",
                "(b) $KE = \\tfrac{1}{2} m v^2 = \\tfrac{1}{2} \\times 1200 \\times 20^2 = 240\\,000$ J.",
                "(c) Join: the brakes must do 240 000 J of work. $F d = KE$, so $d = 240\\,000 \\div 6000 = 40$ m.",
                "(d) Stopping distance $= 14 + 40 = 54$ m.",
                "(e) At 40 m/s the KE is four times as large ($v^2$), so with the same braking force the braking distance is four times as large: 160 m [P]. The thinking distance only doubles, to 28 m.",
            ],
        ),
        practice("Stopping as energy", [
            group("mx-a3-q1", "A van of mass 2500 kg is travelling at 15 m/s when the driver brakes with a constant braking force of 7500 N.", [
                numeric("mx-a3-q1a", "Calculate the kinetic energy of the van.", 281250, "J",
                        "$\\tfrac{1}{2} m v^2$.",
                        ewau(r"KE = \tfrac{1}{2} m v^2", r"KE = \tfrac{1}{2} \times 2500 \times 15^2", "281\\,000", "J (281 250)"), label="a"),
                numeric("mx-a3-q1b", "Calculate the braking distance.", 37.5, "m",
                        "Work done by the brakes = KE: $d = \\text{KE} \\div F$.",
                        ewau(r"F d = \text{KE}", r"d = 281\,250 \div 7500", "37.5", "m"), label="b"),
                numeric("mx-a3-q1c", "The driver's reaction time is 0.80 s. Calculate the stopping distance.", 49.5, "m",
                        "Thinking distance + braking distance.",
                        [r"thinking $= 15 \times 0.80 = 12$ m", r"stopping $= 12 + 37.5 = 49.5$ m"], label="c"),
                written("mx-a3-q1d", "State where the van's kinetic energy has been transferred to by the time it stops. (2)",
                        marks(["The brakes do <b>work</b> on the van (friction between the pads and discs): the kinetic energy is transferred to the <b>thermal store</b> of the brakes.", "It is then dissipated to the <b>surroundings</b> by heating (and a little as sound)."]), lines=2, label="d"),
            ]),
            written("mx-a3-q2", "Explain why doubling the speed of a car quadruples its braking distance but only doubles its thinking distance. (3)",
                    marks(["The brakes must do work equal to the car's <b>kinetic energy</b>, and $KE = \\tfrac{1}{2} m v^2$ is proportional to $v^2$: double the speed, four times the energy.", "With a roughly <b>constant braking force</b>, work $= F d$, so the braking distance is proportional to the KE — four times as far.", "The thinking distance is speed × reaction time, so it is proportional to $v$ and only doubles."]), lines=3, tags=["P"]),
            numeric("mx-a3-q3", "A car of mass 900 kg stops in a braking distance of 25 m from a speed of 18 m/s. Calculate the average braking force.", 5832, "N",
                    "$F = \\text{KE} \\div d$.",
                    [r"$KE = \tfrac{1}{2} \times 900 \times 18^2 = 145\,800$ J"] + ewau(r"F = KE \div d", r"F = 145\,800 \div 25", "5800", "N (5832)")),
        ]),
    ],
)

# ---------------------------------------------------------------------
# P1-4 · The wave equation on light
# ---------------------------------------------------------------------

section_a4 = section(
    "wave-equation-light", "p1", "The wave equation applied to light: what changes at a boundary", "4.6, 5.9",
    equations=[r"v = f \lambda", r"\text{frequency fixed; speed and wavelength change together}"],
    blurb="Topic 4's equation with Topic 5's numbers: light slows down entering glass, its wavelength shortens in the same proportion, and its frequency does not change at all. The question gives speeds and wavelengths in two media and asks for the one you have not got — the join is the frequency, which is the same on both sides of the boundary.",
    checklist=[
        "Use $v = f\\lambda$ for light with wavelengths in nm converted to m",
        "State which of speed, wavelength and frequency change when light enters a medium, and why",
        "Find the change in speed from the change in wavelength at constant frequency",
    ],
    parts=[
        explain(
            "The chain",
            "<table class='tbl'><tr><th>Stage</th><th>Equation</th><th>Hands over</th><th>Watch</th></tr>"
            "<tr><td>speed and wavelength in air → frequency</td><td>$f = v \\div \\lambda$ (Topic 4)</td><td>$f$ in Hz</td><td>$\\lambda$ in metres: 470 nm $= 470 \\times 10^{-9}$ m</td></tr>"
            "<tr><td>frequency → speed in glass</td><td>$v = f \\lambda$ with the wavelength in glass</td><td>$v$ in m/s</td><td>the <b>frequency is unchanged</b> at the boundary — it is set by the source</td></tr>"
            "<tr><td>two speeds → the change</td><td>$\\Delta v = v_{\\text{air}} - v_{\\text{glass}}$</td><td>—</td><td>light <b>slows</b> entering glass (Topic 5: that is why it refracts); wavelength <b>shortens</b> in the same ratio</td></tr></table>"
            "<p>June 2025 1H Q5(b): leaving glass for air the wavelength <b>increases</b> (1) and the frequency <b>stays the same</b> (1); then the change in speed of blue light entering glass from $f = 6.4 \\times 10^{14}$ Hz, 470 nm in air and 350 nm in glass (3). The frequency does not change because the number of wave crests arriving each second at the boundary must equal the number leaving it — waves are not created or destroyed there. Speed and wavelength change together, $v \\propto \\lambda$ at fixed $f$: 350/470 of the speed.</p>",
        ),
        worked(
            "Red light into water",
            "Red light has a frequency of $4.6 \\times 10^{14}$ Hz and travels at $3.0 \\times 10^{8}$ m/s in air. In water its wavelength is 490 nm. (a) Calculate its wavelength in air. (b) Calculate its speed in water. (c) State what happens to its frequency as it enters the water. (6 marks)",
            [
                "(a) $\\lambda = v \\div f = 3.0 \\times 10^{8} \\div (4.6 \\times 10^{14}) = 6.5 \\times 10^{-7}$ m $= 650$ nm.",
                "(b) Join: the frequency is the same in water. $v = f \\lambda = 4.6 \\times 10^{14} \\times 490 \\times 10^{-9}$.",
                "$v = 2.3 \\times 10^{8}$ m/s (2.25) — slower than in air, as refraction towards the normal requires.",
                "(c) The frequency is <b>unchanged</b>: it is fixed by the source, and the number of crests crossing the boundary each second is the same on both sides.",
            ],
        ),
        practice("The wave equation on light", [
            group("mx-a4-q1", "Green light of frequency $5.5 \\times 10^{14}$ Hz travels at $3.0 \\times 10^{8}$ m/s in air and at $2.0 \\times 10^{8}$ m/s in glass.", [
                numeric("mx-a4-q1a", "Calculate the wavelength of the green light in air, in nm.", 545, "nm",
                        "$\\lambda = v \\div f$, then $\\times 10^{9}$ for nm.",
                        [r"$\lambda = v \div f = 3.0 \times 10^{8} \div (5.5 \times 10^{14}) = 5.45 \times 10^{-7}$ m"] + ewau(r"\lambda = v \div f", r"\lambda = 5.45 \times 10^{-7} \text{ m} \times 10^{9}", "545", "nm"), label="a"),
                numeric("mx-a4-q1b", "Calculate its wavelength in glass, in nm.", 364, "nm",
                        "Same frequency; $\\lambda = v \\div f$ with the glass speed.",
                        [r"$\lambda = v \div f = 2.0 \times 10^{8} \div (5.5 \times 10^{14}) = 3.64 \times 10^{-7}$ m"] + ewau(r"\lambda = v \div f", r"\lambda = 3.64 \times 10^{-7} \text{ m} \times 10^{9}", "364", "nm"), label="b"),
                choice("mx-a4-q1c", "As the light enters the glass…",
                       ["speed, wavelength and frequency all decrease", "speed and wavelength decrease; frequency stays the same", "frequency decreases; speed and wavelength stay the same", "wavelength increases"], 1,
                       "Frequency is set by the source; v and λ change together.", label="c"),
            ]),
            written("mx-a4-q2", "Explain why the frequency of light does not change when it passes from air into glass, but its wavelength does. (2)",
                    marks(["The frequency is fixed by the <b>source</b>: the number of waves arriving at the boundary each second equals the number leaving it, so $f$ is the same on both sides.", "The light <b>slows down</b> in glass, and with $v = f\\lambda$ at constant $f$ the <b>wavelength shortens</b> in the same proportion as the speed."]), lines=2),
            numeric("mx-a4-q3", "Light of wavelength 600 nm in air (speed $3.0 \\times 10^{8}$ m/s) enters a plastic in which its wavelength is 400 nm. Calculate its speed in the plastic.", 2.0e8, "m/s",
                    "$v \\propto \\lambda$ at constant f: $v = 3.0 \\times 10^8 \\times 400 \\div 600$.",
                    [r"$f = v \div \lambda = 3.0 \times 10^{8} \div (600 \times 10^{-9}) = 5.0 \times 10^{14}$ Hz"] + ewau(r"v = f \lambda", r"v = 5.0 \times 10^{14} \times 400 \times 10^{-9}", r"2.0 \times 10^{8}", "m/s")),
        ]),
    ],
)

# ---------------------------------------------------------------------
# P1-5 · Radioactivity meets energy
# ---------------------------------------------------------------------

decay_points = sample(lambda t: 100 * 0.5 ** (t / 110), 0, 440, 23)
graph_decay = graph(
    axis("time in min", 440, 55), axis("percentage of fluorine-18 remaining", 100, 20),
    [curve(decay_points)],
    "Decay curve for fluorine-18: 100 percent at time zero falling to 50 percent at 110 minutes, 25 percent at 220 minutes and 12.5 percent at 330 minutes.",
)

section_a5 = section(
    "nuclear-energy", "p1", "Radioactivity meets energy: half-life curves, fusion, and nuclear power", "6.14–6.16, 6.25P–6.28, 7.3P, 3.11",
    equations=[r"\text{half-life from the curve} \rightarrow \text{fraction left}", r"E = m c^2 \text{ (supplied when needed)}"],
    blurb="Topic 6 questions keep reaching into Topic 3 and Topic 7: a decay curve gives a fraction remaining, a fusion question asks for the mass turned into energy with an equation it supplies, and nuclear power is compared as an energy resource with a ratio. The joins are a percentage read off a graph, an energy in joules, and a power in gigawatts.",
    checklist=[
        "Read a half-life from a decay curve and the fraction remaining after a given time",
        "Use a supplied $E = mc^2$ to find the mass lost in fusion, with the unit",
        "Compare nuclear power outputs with a ratio to the significant figures asked",
    ],
    parts=[
        explain(
            "The chain",
            "<table class='tbl'><tr><th>Stage</th><th>Equation or reading</th><th>Hands over</th><th>Watch</th></tr>"
            "<tr><td>curve → half-life</td><td>the time for the activity (or amount) to halve (Topic 6)</td><td>$t_{1/2}$</td><td>read two points, not one; the curve never reaches zero</td></tr>"
            "<tr><td>time → fraction left</td><td>count half-lives: $100\\% \\to 50\\% \\to 25\\% \\to 12.5\\%$</td><td>a percentage</td><td>at a time that is not a whole number of half-lives, <b>read the graph</b></td></tr>"
            "<tr><td>fusion → energy from mass</td><td>$E = m c^2$, supplied; $m = E \\div c^2$</td><td>$m$ in kg</td><td>$c^2 = 9.0 \\times 10^{16}$; the unit mark is for kg; the mass of the products is <b>less</b> than the reactants</td></tr>"
            "<tr><td>power stations → comparison</td><td>ratio $= P_1 \\div P_2$ (Topic 3 resources)</td><td>a number</td><td>to the significant figures asked; GW stays GW on both sides</td></tr></table>"
            "<p>June 2025 1H Q4: the percentage of fluorine-18 remaining after 150 min from a decay curve (2), what happens when a positron meets an electron (2, Topic 6 PET), one neutron and one uranium nucleus (3), and the ratio of Finland's to the UK's nuclear power to 2 s.f. (2). Q10(b): describe fusion (2) and the mass decrease equivalent to $3.9 \\times 10^{26}$ J with its unit (2), $c = 3.0 \\times 10^{8}$ m/s — $E = mc^2$ is <b>not on the equation list</b>; it was supplied in the question. Fusion's energy comes from the mass lost when light nuclei join; \"two hydrogen nuclei join to form helium, and energy is released\" — Topic 6 N9 / Topic 7 N7.</p>",
        ),
        worked(
            "Fluorine-18 and the Sun",
            "(a) The graph shows the decay of fluorine-18. Use it to find the half-life, and the percentage remaining after 275 min. (b) The Sun transfers $3.9 \\times 10^{26}$ J of energy every second by fusion. Use $E = mc^2$ with $c = 3.0 \\times 10^8$ m/s to calculate the mass lost each second, with its unit. (6 marks)",
            [
                "(a) 100 % → 50 % takes 110 min: half-life = <b>110 min</b> (check: 50 % → 25 % at 220 min).",
                "275 min is 2.5 half-lives; reading the curve at 275 min gives about <b>18 %</b> (two half-lives would be 25 %, three 12.5 %).",
                "(b) $m = E \\div c^2 = 3.9 \\times 10^{26} \\div (3.0 \\times 10^{8})^2 = 3.9 \\times 10^{26} \\div 9.0 \\times 10^{16}$.",
                "$m = 4.3 \\times 10^{9}$ <b>kg</b> every second — the mass of the helium formed is less than that of the hydrogen that fused by this amount.",
            ],
            graph=graph_decay,
        ),
        practice("Radioactivity and energy", [
            group("mx-a5-q1", "Use the decay curve for fluorine-18.", [
                numeric("mx-a5-q1a", "State the percentage remaining after 220 min.", 25, "%",
                        "Two half-lives.",
                        ["220 min is two half-lives: 100 → 50 → 25 %."], label="a", tolerance=0.04),
                numeric("mx-a5-q1b", "A hospital receives a sample at 10:00 and uses it at 15:30. Calculate the percentage of the fluorine-18 that is left by then.", 12.5, "%",
                        "5.5 hours = 330 min = three half-lives.",
                        [r"$330 \div 110 = 3$ half-lives: $100 \to 50 \to 25 \to 12.5$ %"], label="b", tolerance=0.04),
                written("mx-a5-q1c", "Fluorine-18 is a positron emitter used in PET scans. Describe what happens when a positron meets an electron. (2)",
                        marks(["The positron and electron <b>annihilate</b> each other — both particles are destroyed (their mass becomes energy).", "<b>Two gamma rays</b> are emitted in opposite directions, which the scanner detects to locate the source."]), lines=2, label="c", tags=["P"]),
            ], graph=graph_decay),
            numeric("mx-a5-q2", "In a fusion reaction $1.2 \\times 10^{-29}$ kg of mass is converted to energy. Use $E = mc^2$ with $c = 3.0 \\times 10^8$ m/s to calculate the energy released.", 1.08e-12, "J",
                    "$E = m c^2$ (supplied).",
                    ewau(r"E = m c^2", r"E = 1.2 \times 10^{-29} \times (3.0 \times 10^{8})^2", r"1.1 \times 10^{-12}", "J (1.08)"), tolerance=0.03),
            numeric("mx-a5-q3", "France generates about 61 GW from nuclear power and the UK about 5.9 GW. Calculate the ratio of France's nuclear power to the UK's, to 2 significant figures.", 10, "",
                    "$61 \\div 5.9$.",
                    [r"ratio $= 61 \div 5.9 = 10.3 = 10$ (2 s.f.)"], tolerance=0.05),
            numeric("mx-a5-q5", "A beta particle (mass $9.1 \\times 10^{-31}$ kg) leaves a nucleus at $4.0 \\times 10^{6}$ m/s. Calculate its kinetic energy.", 7.3e-18, "J",
                    "$\\tfrac{1}{2} m v^2$ with the powers of ten kept.",
                    ewau(r"KE = \tfrac{1}{2} m v^2", r"KE = \tfrac{1}{2} \times 9.1 \times 10^{-31} \times (4.0 \times 10^{6})^2", r"7.3 \times 10^{-18}", "J (7.28)")),
            written("mx-a5-q4", "Describe the process of nuclear fusion and state where the energy released comes from. (3)",
                    marks(["Two <b>light nuclei</b> (e.g. hydrogen) <b>join</b> to form a heavier nucleus (helium).", "It needs very <b>high temperature and pressure</b> so the nuclei can get close enough despite their repulsion.", "Energy is released because the <b>mass of the product is less</b> than the mass of the nuclei that fused — the lost mass becomes energy ($E = mc^2$, supplied)."]), lines=3),
        ]),
    ],
)

# ---------------------------------------------------------------------
# P1-6 · Thermal balance
# ---------------------------------------------------------------------

section_a6 = section(
    "thermal-balance", "p1", "Thermal balance: radiation in equals radiation out", "5.20P–5.23, 7.7P–7.9P",
    equations=[r"\text{power absorbed} = \text{power emitted} \Rightarrow \text{constant temperature}", r"\text{hotter} \rightarrow \text{emits more}"],
    blurb="Why is a planet's average temperature steady? Because it absorbs radiation from the Sun at the same rate as it emits infrared to space. Warm it and it emits more until the two balance again; cool it and it emits less. The same balance holds a star in its stable phase between gravity and the pressure from fusion. The join is the rate of energy transfer.",
    tags=["H"],
    checklist=[
        "Explain a constant temperature as a balance between radiation absorbed and radiation emitted",
        "Explain what happens to the temperature when the balance is disturbed, and how a new balance is reached",
        "Apply the same balance idea to a star's stable phase",
    ],
    parts=[
        explain(
            "The chain",
            "<table class='tbl'><tr><th>Stage</th><th>Idea</th><th>Hands over</th><th>Watch</th></tr>"
            "<tr><td>Sun → planet</td><td>the planet <b>absorbs</b> radiation (mostly visible) at a steady rate</td><td>power in, W</td><td>absorbed, not just \"receives\"</td></tr>"
            "<tr><td>planet → space</td><td>every object <b>emits</b> infrared; the <b>hotter</b> it is, the <b>more it emits</b> per second (and at shorter wavelengths)</td><td>power out, W</td><td>the rate depends on the temperature — this is the lever</td></tr>"
            "<tr><td>balance</td><td>power in = power out → <b>constant temperature</b>; in > out → warms until out rises to match; in < out → cools until out falls to match</td><td>—</td><td>a change in the <i>balance</i>, not in the Sun, is what greenhouse gases do: they reduce the infrared escaping</td></tr>"
            "<tr><td>a star (Topic 7)</td><td>stable phase: the <b>inward force of gravity</b> balances the <b>outward pressure</b> from fusion</td><td>—</td><td>a different balance, same shape of answer: name both, say they are equal</td></tr></table>"
            "<p>June 2025 1H Q7(d) (4 marks): explain why Ceres' average temperature stays constant. The marks: it <b>absorbs</b> radiation from the Sun; it <b>emits</b> radiation (infrared); the rate of emission <b>equals</b> the rate of absorption; if it were hotter it would emit more than it absorbs and cool (or the reverse), so the temperature settles where they balance. Four ideas, four marks — Topic 5 T6.</p>",
        ),
        worked(
            "A planet at constant temperature",
            "Explain why the average temperature of a planet with no atmosphere stays constant. (4 marks)",
            [
                "The planet <b>absorbs</b> radiation from the Sun at a steady rate.",
                "It also <b>emits</b> radiation (infrared) to space, and the rate at which it emits depends on its temperature — a hotter surface emits more.",
                "Its temperature is constant because the <b>rate of emission equals the rate of absorption</b>: energy in per second = energy out per second.",
                "If the temperature rose it would emit more than it absorbs and cool back down; if it fell it would emit less and warm up — so it settles at the temperature where the two rates balance.",
            ],
        ),
        practice("Thermal balance", [
            written("mx-a6-q1", "A planet moves into an orbit closer to its star. Explain what happens to its average temperature. (3)",
                    marks(["Closer to the star it <b>absorbs</b> radiation at a <b>greater rate</b>.", "Absorption is now greater than emission, so its temperature <b>rises</b>.", "As it warms it <b>emits more</b> radiation, until the rate of emission again <b>equals</b> the rate of absorption — it settles at a new, higher constant temperature."]), lines=3),
            choice("mx-a6-q2", "A planet's temperature is constant. Which statement is correct?",
                   ["It absorbs no radiation", "It emits no radiation", "It absorbs and emits radiation at the same rate", "It absorbs more than it emits"], 2,
                   "Balance of rates."),
            written("mx-a6-q3", "Explain why a star in its main (stable) phase does not collapse or expand. (2)",
                    marks(["The <b>inward force of gravity</b> (the star's own weight pulling inwards) is balanced by…", "…the <b>outward pressure</b> produced by the fusion reactions in the core (thermal and radiation pressure), so the forces are in equilibrium."]), lines=2, tags=["P"]),
            written("mx-a6-q4", "The Earth's atmosphere contains gases that absorb some of the infrared the surface emits. Explain how this affects the balance of radiation and the Earth's average temperature. (3)",
                    marks(["The planet still absorbs radiation from its star at the same rate.", "Greenhouse gases <b>absorb some of the infrared</b> the surface emits and re-emit part of it back down, so <b>less escapes to space</b>: emission to space is less than absorption.", "The planet <b>warms</b> until the surface emits enough extra infrared for the rate escaping to space to equal the rate absorbed again — a higher constant temperature."]), lines=3),
        ]),
    ],
)

SECTIONS_START = [section_m1]
SECTIONS_P1 = [section_a1, section_a2, section_a3, section_a4, section_a5, section_a6]
