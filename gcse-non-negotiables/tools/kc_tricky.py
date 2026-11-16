"""
kc_tricky.py — Topic 1 Key concepts: the tricky bits, T1–T8.

Command words; reading a question; multi-step calculations; graph
skills; proportionality; planning a practical; evaluating a method;
estimation. Working-scientifically skills that every topic draws on.
"""

from revlib import (
    axis, choice, dashed, data, draw, explain, ewau, graph, group, label,
    line, mark, mark_scheme, marks, numeric, practice, section, sf, worked,
    written,
)

G = 10


# =====================================================================
# T1 · Command words
# =====================================================================

section_t1 = section(
    "command-words", "tricky", "Command words: what the examiner wants", "WS",
    blurb="The first word of a question tells you what kind of answer scores. Answer a \"describe\" with an explanation and you have wasted the marks on the wrong thing.",
    checklist=[
        "Tell a describe question from an explain question, and answer each the right way",
        "Know what calculate, determine and show that each require",
        "Structure an evaluate or compare answer so both sides and a conclusion appear",
    ],
    parts=[
        explain(
            "The command words, and what scores",
            "<table class='tbl'><tr><th>Command word</th><th>It wants</th><th>Model one-liner</th></tr>"
            "<tr><td><b>State</b> / <b>Give</b> / <b>Name</b> / <b>Write down</b></td><td>A short answer, no reasoning. One word or one line.</td><td>\"State the unit of power.\" — <i>watt.</i></td></tr>"
            "<tr><td><b>Describe</b></td><td>Say <i>what</i> happens or what something is like, in order. No <i>why</i>.</td><td>\"Describe the motion shown.\" — <i>It accelerates for 5 s, then moves at a constant 10 m/s.</i></td></tr>"
            "<tr><td><b>Explain</b></td><td>Say <i>why</i>, with a reason or a mechanism. Use <i>because</i>, <i>so</i>, <i>therefore</i>.</td><td>\"Explain why the car slows.\" — <i>Friction acts backwards, so there is a resultant force opposite to the motion, so it decelerates.</i></td></tr>"
            "<tr><td><b>Calculate</b></td><td>A number, from an equation, with working and a unit (EWAU).</td><td>\"Calculate the speed.\" — <i>v = x ÷ t = 100 ÷ 8 = 12.5 m/s.</i></td></tr>"
            "<tr><td><b>Determine</b></td><td>A number, but you must get some of the data yourself — usually from a graph (a gradient, an area, a read-off).</td><td>\"Determine the acceleration from the graph.\" — <i>draw the triangle, show the two values, divide.</i></td></tr>"
            "<tr><td><b>Show that</b></td><td>The answer is given; you must produce it with full working, to one more figure than quoted.</td><td>\"Show that the force is about 50 N.\" — <i>F = ma = 2.5 × 20.4 = 51 N ≈ 50 N.</i></td></tr>"
            "<tr><td><b>Estimate</b></td><td>A rough value from sensible assumed numbers that you state.</td><td>\"Estimate the mass of a car.\" — <i>about 1000 kg.</i></td></tr>"
            "<tr><td><b>Compare</b></td><td>Similarities <i>and</i> differences between both things named — mention both every time.</td><td>\"Compare alpha and beta.\" — <i>Both are ionising; alpha is more ionising but less penetrating.</i></td></tr>"
            "<tr><td><b>Evaluate</b></td><td>Points for and against, using the information given, then a conclusion that follows from them.</td><td>\"Evaluate the use of nuclear power.\" — <i>for … against … so overall …</i></td></tr>"
            "<tr><td><b>Justify</b></td><td>Give the evidence or reasoning for a statement that is given to you.</td><td>\"Justify the choice of a 5 A fuse.\" — <i>I = P ÷ V = 920 ÷ 230 = 4 A, so 5 A is the next size up.</i></td></tr>"
            "<tr><td><b>Suggest</b></td><td>Apply your knowledge to an unfamiliar situation; a sensible, physics-based idea scores even if it is not the one in the mark scheme.</td><td>\"Suggest why the reading was lower.\" — <i>some energy was transferred to the surroundings.</i></td></tr>"
            "<tr><td><b>Predict</b></td><td>Say what will happen, from the physics.</td><td>\"Predict the current if the p.d. doubles.\" — <i>it doubles (Ohm's law).</i></td></tr>"
            "<tr><td><b>Draw</b> / <b>Sketch</b> / <b>Plot</b></td><td>Draw: accurate with a ruler. Sketch: the shape and key features, labelled. Plot: points on given axes.</td><td></td></tr>"
            "<tr><td><b>Complete</b></td><td>Fill in the missing parts of a diagram, table or sentence.</td><td></td></tr></table>"
            "<p>The marks are in the word. A 2-mark \"describe\" is two things that happen; a 2-mark \"explain\" is one thing that happens and the reason for it.</p>",
        ),
        explain(
            "Describe is not explain",
            "<p>The most expensive habit at GCSE is answering every question with an explanation. \"Describe how the velocity changes\" is answered by reading the graph: <i>it increases, then stays constant, then decreases to zero</i>. "
            "Writing about forces there earns nothing, however correct. Likewise \"explain\" answered with a description — <i>the ball slows down</i> — scores nothing without the <i>because</i>.</p>"
            "<p>Underline the command word before you read anything else.</p>",
            tone="warn",
        ),
        worked(
            "Same situation, three command words",
            "A ball is dropped and bounces. For each command word, write the kind of answer that scores: (a) <b>Describe</b> the motion of the ball as it falls. (b) <b>Explain</b> why the ball speeds up as it falls. (c) <b>Calculate</b> its speed after 2 s.",
            [
                r"<b>(a) Describe:</b> \"The ball starts from rest and its speed increases (it accelerates) all the way down.\" What happens — no reasons.",
                r"<b>(b) Explain:</b> \"The ball's weight acts downwards and there is no force balancing it, so there is a resultant force downwards, so the ball accelerates (Newton's second law).\" Each <i>so</i> is a reason.",
                r"<b>(c) Calculate:</b> $v = u + a t = 0 + 10 \times 2 = 20$ m/s. Equation, working, answer, unit.",
                r"Three questions about one ball; three different answers. The command word decides which.",
            ],
        ),
        practice("Command words", [
            choice("kc-t1-q1", "\"Describe how the current changes as the potential difference is increased.\" Which answer scores?",
                   ["The current increases because the electrons are pushed harder", "The current increases", "V = I × R", "The resistance stays the same"], 1,
                   "Describe wants what happens, not why. The first option is an explanation — correct physics, wrong command word."),
            choice("kc-t1-q2", "\"Explain why a parachutist reaches a terminal velocity.\" Which answer scores full marks?",
                   ["The parachutist stops accelerating", "Air resistance increases with speed until it equals the weight, so the resultant force is zero, so the velocity stays constant", "Terminal velocity is the maximum velocity", "Because of air resistance"], 1,
                   "Explain needs the chain of reasons: air resistance grows → balances weight → zero resultant → constant velocity. The others describe or give half a reason."),
            choice("kc-t1-q3", "What does \"determine\" usually mean in a graph question?",
                   ["Guess a value", "Read or work out a value from the graph, showing how", "Describe the shape", "Draw the graph"], 1,
                   "Determine means find a value, and you must get some of the data from the graph yourself — a gradient triangle, an area or a read-off, shown on the graph."),
            written("kc-t1-q4", "A question says: \"Show that the kinetic energy of a 1200 kg car moving at 15 m/s is about 135 kJ.\" Write the answer that earns full marks.",
                    marks(["$KE = \\tfrac{1}{2} \\times m \\times v^2$",
                           "$= \\tfrac{1}{2} \\times 1200 \\times 15^2 = \\tfrac{1}{2} \\times 1200 \\times 225$",
                           "$= 135\\,000$ J $= 135$ kJ — the full calculation, ending with the value quoted (give it to at least the precision in the question)."]), lines=3),
            written("kc-t1-q5", "\"Compare the properties of alpha and beta radiation.\" A student writes: \"Alpha is stopped by paper and is very ionising.\" Explain why this answer scores poorly, and improve it.",
                    marks(["A compare answer must mention both things in the question — this answer only talks about alpha.",
                           "It should pair each property: alpha is stopped by paper <b>whereas</b> beta passes through paper and is stopped by a few mm of aluminium.",
                           "Alpha is more ionising <b>than</b> beta. Both are ionising (a similarity) — one similarity and two differences is a safe shape."]), lines=4),
            choice("kc-t1-q6", "An \"evaluate\" question is worth 6 marks. What must the answer contain to reach the top band?",
                   ["Only the advantages", "A list of facts about the topic", "Points for and against, using the data given, and a conclusion that follows from them", "A calculation"], 2,
                   "Evaluate = weigh up. Both sides, drawing on the information in the question, then a judgement that is justified by the points made."),
        ]),
    ],
)


# =====================================================================
# T2 · Reading a question
# =====================================================================

t2_w_t = 3 * 60
t2_w_v = 540 / t2_w_t
t2_1 = 0.25 * 10
t2_2 = 2.5 * 1000 / (5 * 60)
t2_3 = 0.5 * 0.8 * 12 ** 2
t2_4 = 400 * 0.75

section_t2 = section(
    "reading-questions", "tricky", "Reading the question", "WS",
    blurb="Most lost marks are not physics mistakes. They are a number in the wrong unit, a value that was given but not needed, or an instruction in the last line that was never read.",
    checklist=[
        "Pull out every value with its unit, and convert the ones that need it, before starting",
        "Spot the quantities given that are not needed, and the standard values not given",
        "Notice instructions such as \"to 2 significant figures\", \"ignore air resistance\", \"include the sign\"",
        "Use information from earlier parts of a question in later parts",
    ],
    parts=[
        explain(
            "A routine for every calculation question",
            "<ol class='list'>"
            "<li><b>Underline the command word</b> and read the last sentence first: it says what to find and how to give it (\"to 2 s.f.\", \"in kJ\", \"include the sign\").</li>"
            "<li><b>List every value</b> as symbol = number unit. $m = 250$ g, $t = 3$ min, $v = 15$ m/s. Write the unknown with a question mark: $P = ?$</li>"
            "<li><b>Convert</b> anything not in SI: 250 g → 0.25 kg; 3 min → 180 s; 2 kW → 2000 W. Cross out the old value so you cannot pick it up by mistake.</li>"
            "<li><b>Add the standard values</b> the question will not give you: $g = 10$ N/kg, speed of light $3 \\times 10^8$ m/s. (Speed of sound, density of water and specific heat capacity of water are usually given.)</li>"
            "<li><b>Cross out distractors</b>: a question that gives a car's mass, speed and colour of paint — or its mass, speed and the length of the road — may include a value you do not need. If a symbol does not appear in your equation, leave it.</li>"
            "<li><b>Look back</b> at the earlier parts: part (c) often needs the answer to part (b). \"Use your answer to (b)\" means exactly that, even if (b) was wrong — the marks follow through.</li></ol>",
        ),
        explain(
            "The traps, named",
            "<table class='tbl'><tr><th>Trap</th><th>What it looks like</th><th>Defence</th></tr>"
            "<tr><td>Mixed units</td><td>\"a 500 g mass … 2 km … 5 minutes\"</td><td>Convert in the list, before any equation</td></tr>"
            "<tr><td>Diameter for radius, or area given as a length</td><td>\"a pipe of diameter 4 cm\" then a question needing the radius or the area</td><td>Read the quantity's name, not just its number</td></tr>"
            "<tr><td>Weight for mass</td><td>\"a 600 N box\" used in $F = m a$</td><td>A value in newtons is a weight; divide by $g$ to get the mass</td></tr>"
            "<tr><td>Total vs per second</td><td>\"transfers 3000 J every minute\" in a power question</td><td>Power is per second: ÷ 60</td></tr>"
            "<tr><td>Stated precision</td><td>\"Give your answer to 2 significant figures\"</td><td>Circle it; round at the end</td></tr>"
            "<tr><td>Hidden zero</td><td>\"starts from rest\", \"comes to a stop\", \"dropped\", \"at the top of its flight\"</td><td>$u = 0$ or $v = 0$</td></tr>"
            "<tr><td>Hidden sign</td><td>\"decelerates\", \"slows\", \"thrown upwards\"</td><td>Negative $a$ (or negative $v$ for the opposite direction)</td></tr></table>",
            tone="warn",
        ),
        worked(
            "A question with three traps",
            "A cyclist of mass 70 kg, riding a 12 kg bicycle, travels 540 m along a flat road in 3 minutes. Calculate the cyclist's average speed in m/s.",
            [
                r"Last sentence first: <i>average speed, in m/s</i>. So the answer needs metres and seconds.",
                r"List: $m_\text{cyclist} = 70$ kg, $m_\text{bike} = 12$ kg, $x = 540$ m, $t = 3$ min. Wanted: $v = ?$",
                r"Convert: $3\ \text{min} = 180$ s. Distractors: the two masses — speed does not depend on them. Cross them out.",
                r"$v = \dfrac{x}{t} = \dfrac{540}{180} = 3$ m/s.",
                r"A sense check costs five seconds: 3 m/s is a gentle cycling speed. ✓",
            ],
        ),
        practice("Reading the question", [
            numeric("kc-t2-q1", "A bag of sugar has a mass of 250 g. Calculate its weight. (g = 10 N/kg.)", t2_1, "N",
                    "Grams to kilograms first.",
                    [r"$250\ \text{g} = 0.25$ kg."] + ewau(r"W = m \times g", r"W = 0.25 \times 10", "2.5", "N")),
            numeric("kc-t2-q2", "A lift raises a 300 kg load through 2.5 km of mine shaft in 5 minutes. Calculate the average speed of the lift in m/s.", sf(t2_2), "m/s",
                    "Which values does speed need? Convert those; ignore the rest.",
                    [r"$2.5\ \text{km} = 2500$ m; $5\ \text{min} = 300$ s. The mass is not needed.",
                     r"$v = \dfrac{2500}{300} = 8.3$ m/s (2 s.f.)."]),
            numeric("kc-t2-q3", "A 800 g ball is thrown at 12 m/s. Calculate its kinetic energy.", t2_3, "J",
                    "800 g = 0.8 kg; square the speed.",
                    ewau(r"KE = \tfrac{1}{2} \times m \times v^2", r"KE = \tfrac{1}{2} \times 0.8 \times 12^2 = 0.4 \times 144", "57.6", "J")),
            numeric("kc-t2-q4", "A heater transfers 400 J of energy every second. It is 75% efficient. Calculate the useful power output.", t2_4, "W",
                    "400 J every second is a power of 400 W. Then take 75% of it.",
                    [r"Input power $= 400$ W.", r"Useful output $= 0.75 \times 400 = 300$ W."]),
            choice("kc-t2-q5", "A question says: \"A stone is dropped from a bridge. Calculate its speed after falling for 1.5 s.\" Which value is given without being written down?",
                   ["The height of the bridge", "The initial speed, u = 0, because it is dropped", "The mass of the stone", "The time"], 1,
                   "\"Dropped\" means it starts from rest: u = 0. With a = g = 10 m/s², v = 0 + 10 × 1.5 = 15 m/s. No height or mass is needed."),
            written("kc-t2-q6", "A student is asked for the acceleration of a car that slows from 30 m/s to 10 m/s in 4 s, \"including the sign\". She writes 5 m/s² and loses a mark. Explain the mistake.",
                    marks(["The car is slowing, so $v$ is smaller than $u$: $a = \\dfrac{10 - 30}{4} = -5$ m/s².",
                           "The question said to include the sign, so the negative sign is part of the answer.",
                           "Reading the last line of the question first would have caught it."]), lines=3),
        ]),
    ],
)


# =====================================================================
# T3 · Multi-step calculations
# =====================================================================

t3_w_a = (24 - 0) / 8
t3_w_F = 1500 * t3_w_a
t3_1_v = 60 / 3
t3_1_p = 1200 * t3_1_v
t3_2_P = 2.5 * 230
t3_2_E = t3_2_P * 3 * 60
t3_3_W = 50 * 10
t3_3_E = t3_3_W * 12
t3_4_V = 0.02 * 0.1 * 0.05
t3_4_m = 8000 * t3_4_V
t3_5_GPE = 0.5 * 10 * 1.8
t3_5_v = (2 * t3_5_GPE / 0.5) ** 0.5

section_t3 = section(
    "multi-step", "tricky", "Multi-step calculations", "WS",
    blurb="Two equations, one after the other. The hard part is seeing which quantity links them, and not rounding in between.",
    checklist=[
        "Plan the chain: which equation gives the quantity the second equation needs?",
        "Carry the full value from step one into step two",
        "Lay out each step as its own EWAU with its own unit",
        "Check that the final unit matches what was asked for",
    ],
    parts=[
        explain(
            "Finding the chain",
            "<p>A 4- or 5-mark calculation almost always needs two equations. The method:</p>"
            "<ol class='list'>"
            "<li>Write the equation that contains the <b>quantity you want</b>. Which of its inputs are you missing?</li>"
            "<li>Find an equation that gives that <b>missing quantity</b> from the values you do have. That is step one.</li>"
            "<li>Do step one in full, with its unit. Do step two with the unrounded result.</li></ol>"
            "<p>Chains that come up again and again:</p>"
            "<table class='tbl'><tr><th>Want</th><th>Given</th><th>Chain</th></tr>"
            "<tr><td>force on a car</td><td>mass, change in speed, time</td><td>$a = \\dfrac{v - u}{t}$ then $F = m a$</td></tr>"
            "<tr><td>energy from the mains</td><td>current, p.d., time</td><td>$P = I V$ then $E = P t$</td></tr>"
            "<tr><td>work done lifting</td><td>mass, height</td><td>$W = m g$ then $E = F \\times d$ (or $GPE = m g h$ in one go)</td></tr>"
            "<tr><td>mass of a block</td><td>dimensions, density</td><td>$V = l \\times w \\times h$ then $m = \\rho V$</td></tr>"
            "<tr><td>speed at the bottom of a drop</td><td>height</td><td>$GPE = m g h$, set $KE = GPE$, then $v = \\sqrt{2 KE / m}$</td></tr>"
            "<tr><td>power of a motor</td><td>force, distance, time</td><td>$E = F d$ then $P = E / t$</td></tr>"
            "<tr><td>wavelength</td><td>speed, period</td><td>$f = 1 / T$ then $\\lambda = v / f$</td></tr></table>",
        ),
        explain(
            "Do not round in the middle",
            "<p>If step one gives $a = 2.666\\,6\\ldots$ m/s², use <b>2.6666</b> (or the calculator's memory) in step two, not 2.7. Rounding to 2.7 then multiplying by 1500 kg gives 4050 N instead of 4000 N — outside the examiner's tolerance, and a lost mark for a correct method.</p>",
            tone="warn",
        ),
        worked(
            "Two equations, one chain",
            "A car of mass 1500 kg accelerates from rest to 24 m/s in 8 s. Calculate the resultant force on the car.",
            [
                r"Want: force. $F = m \times a$ — have $m$, missing $a$.",
                r"Get $a$ from the speeds and time: $a = \dfrac{v - u}{t} = \dfrac{24 - 0}{8} = 3$ m/s².",
                r"Now $F = m \times a = 1500 \times 3 = 4500$ N.",
                r"Two EWAUs, each with its unit; the second uses the first's unrounded result.",
            ],
        ),
        practice("Multi-step", [
            group("kc-t3-q1", "A 1200 kg car travels 60 m in 3 s at constant speed.", [
                numeric("kc-t3-q1a", "Calculate its speed.", t3_1_v, "m/s", "x ÷ t.",
                        ewau(r"v = \dfrac{x}{t}", r"v = \dfrac{60}{3}", "20", "m/s"), label="a"),
                numeric("kc-t3-q1b", "Calculate its momentum.", t3_1_p, "kg m/s", "p = m × v with the speed from (a).",
                        ewau(r"p = m \times v", r"p = 1200 \times 20", "24\\,000", "kg m/s"), label="b"),
            ]),
            numeric("kc-t3-q2", "A 230 V hairdryer draws a current of 2.5 A for 3 minutes. Calculate the energy transferred.", t3_2_E, "J",
                    "Power first (P = IV), then energy (E = P t) with the time in seconds.",
                    [r"$P = I \times V = 2.5 \times 230 = 575$ W.", r"$t = 3 \times 60 = 180$ s.", r"$E = P \times t = 575 \times 180 = 103\,500$ J."]),
            numeric("kc-t3-q3", "A crane lifts a 50 kg load through 12 m. Calculate the work done. (g = 10 N/kg.)", t3_3_E, "J",
                    "Weight first, then work = force × distance.",
                    [r"$W = m \times g = 50 \times 10 = 500$ N.", r"$E = F \times d = 500 \times 12 = 6000$ J."]),
            numeric("kc-t3-q4", "A steel block measures 2 cm × 10 cm × 5 cm. The density of steel is 8000 kg/m³. Calculate the mass of the block.", t3_4_m, "kg",
                    "Volume in m³ first (convert each length to metres), then m = ρ × V.",
                    [r"$V = 0.02 \times 0.10 \times 0.05 = 0.0001$ m³ ($= 1 \times 10^{-4}$ m³).", r"$m = \rho \times V = 8000 \times 0.0001 = 0.8$ kg."]),
            group("kc-t3-q5", "A 0.5 kg ball is dropped from a height of 1.8 m. Ignore air resistance. (g = 10 N/kg.)", [
                numeric("kc-t3-q5a", "Calculate the gravitational potential energy lost by the ball as it falls.", t3_5_GPE, "J", "GPE = m g h.",
                        ewau(r"GPE = m \times g \times h", r"GPE = 0.5 \times 10 \times 1.8", "9", "J"), label="a"),
                numeric("kc-t3-q5b", "Calculate the speed of the ball just before it hits the ground.", t3_5_v, "m/s", "All the GPE becomes KE: ½ m v² = 9 J, then square-root.",
                        [r"$KE = GPE = 9$ J.", r"$v^2 = \dfrac{2 \times 9}{0.5} = 36$.", r"$v = \sqrt{36} = 6$ m/s."], label="b"),
            ]),
            written("kc-t3-q6", "A student calculates a force in two steps. In step one she gets an acceleration of 1.333… m/s² and writes it down as 1.3 m/s². In step two she multiplies by 900 kg and gets 1170 N; the mark scheme says 1200 N. Explain why she lost the final mark and what she should have done.",
                    marks(["She rounded the intermediate value (1.333… to 1.3) and the rounding error was multiplied up in step two.",
                           "1.333… × 900 = 1200 N; 1.3 × 900 = 1170 N, which is outside the accepted range.",
                           "Carry the full value (or at least one extra significant figure) between steps; round only the final answer."]), lines=3),
        ]),
    ],
)


# =====================================================================
# T4 · Graph skills
# =====================================================================

# A force–extension data set with a best-fit line through the origin, gradient 25 N/m → k
fe_points = [[0.02, 0.6], [0.04, 0.9], [0.06, 1.6], [0.08, 1.9], [0.10, 2.6], [0.12, 2.9]]
graph_t4_w = graph(
    axis("extension in m", 0.12, 0.02), axis("force in N", 3, 0.5),
    [data(fe_points), line([[0, 0], [0.12, 3.0]])],
    "Force against extension: six plotted points scattered closely around a straight line of best fit from the origin to (0.12, 3.0).",
    marks_list=[mark(0.12, 3.0, "B", drop=True), mark(0.04, 1.0, "A", drop=True)],
)
t4_w_grad = (3.0 - 1.0) / (0.12 - 0.04)

# Velocity–time for the practice: gradient and intercept
vt_points = [[0, 4], [10, 24]]
graph_t4_1 = graph(
    axis("time in s", 10, 2), axis("velocity in m/s", 25, 5),
    [line(vt_points)],
    "Velocity–time graph: a straight line from (0, 4) to (10, 24).",
    marks_list=[mark(10, 24, "P", drop=True)],
)
t4_1_grad = (24 - 4) / 10
t4_1_int = 4

# Resistance of a wire against length: data with a line of best fit
rl_points = [[0.2, 1.1], [0.4, 2.0], [0.6, 3.1], [0.8, 3.9], [1.0, 5.1]]
graph_t4_2 = graph(
    axis("length in m", 1.0, 0.2), axis("resistance in Ω", 6, 1),
    [data(rl_points), line([[0, 0], [1.0, 5.0]])],
    "Resistance of a wire against its length: five points close to a straight line of best fit from the origin to (1.0, 5.0).",
)
t4_2 = 5.0 / 1.0

blank_grid = graph(
    axis("time in s", 8, 1), axis("distance in m", 40, 5),
    [], "A blank grid for drawing on",
)
answer_grid = graph(
    axis("time in s", 8, 1), axis("distance in m", 40, 5),
    [line([[0, 0], [4, 20], [6, 20], [8, 40]])],
    "Distance–time graph: 0 to 20 m in 4 s, flat to 6 s, then 20 m to 40 m by 8 s.",
)

section_t4 = section(
    "graph-skills", "tricky", "Graph skills: plotting, best fit, gradient", "WS",
    equations=[r"\text{gradient} = \dfrac{\text{change in } y}{\text{change in } x}"],
    blurb="Plotting with the right scale, drawing a line of best fit through the scatter, and taking a gradient from a big triangle. Each is a mark, and each is lost the same way every year.",
    checklist=[
        "Choose axes and a scale that use more than half the grid, with sensible intervals",
        "Plot points as small crosses, accurate to half a small square",
        "Draw a line (or smooth curve) of best fit with roughly equal points either side, ignoring anomalies",
        "Find a gradient from a triangle that spans at least half the line, using points on the line, not data points",
        "Read an intercept and say what it means",
    ],
    parts=[
        explain(
            "Plotting and the line of best fit",
            "<p><b>Axes:</b> the independent variable (the one you changed) goes on the $x$-axis, the dependent (the one you measured) on the $y$-axis. Label each with <i>quantity in unit</i>, as Edexcel does: <i>extension in m</i>. "
            "<b>Scale:</b> pick a scale so the points fill more than half the grid in each direction, going up in 1s, 2s, 5s or 10s (never 3s or 7s). The axes do not have to start at zero — unless you need the origin, for proportionality or an intercept.</p>"
            "<p><b>Points:</b> small, neat crosses (×), plotted to within half a small square. Big blobs cost the plotting mark.</p>"
            "<p><b>Line of best fit:</b> a single thin straight line (ruler) or smooth curve that follows the trend with about as many points above it as below. It does <b>not</b> join the dots, does not have to pass through every point, and does not have to go through the origin unless the physics says so. An <b>anomalous</b> point — one clearly off the trend — is circled and ignored.</p>",
        ),
        explain(
            "Gradient and intercept",
            "<p>To find a gradient:</p>"
            "<ol class='list'>"
            "<li>Draw a right-angled triangle on the line of best fit, as large as possible — at least half the length of the line. Small triangles give inaccurate gradients and lose the mark.</li>"
            "<li>Use two points <b>on the line</b> where it crosses grid lines, not two of the plotted data points (they are not on the line).</li>"
            "<li>$\\text{gradient} = \\dfrac{\\text{change in } y}{\\text{change in } x}$, with the two values read from the axes and written down.</li>"
            "<li>The gradient has a unit: $y$-unit per $x$-unit. For force against extension it is N/m — the spring constant.</li></ol>"
            "<p>The <b>intercept</b> is where the line crosses the $y$-axis (at $x = 0$). It usually means a value \"at the start\" or a fixed offset: the initial velocity on a $v$–$t$ graph, the friction that must be overcome before a trolley moves, the resistance of the leads in a circuit.</p>",
            graph=graph_t4_w,
            after="<p>In the graph above, the triangle from A to B spans most of the line: $\\text{gradient} = \\dfrac{3.0 - 1.0}{0.12 - 0.04} = \\dfrac{2.0}{0.08} = 25$ N/m. Using two data points instead (say the first and last) would give 23.0 N/m — close, but it is not what the line says, and the examiner is checking that you used the line.</p>",
        ),
        worked(
            "Determining a value from a graph",
            "The graph in the explanation shows force against extension for a spring. Determine the spring constant.",
            [
                r"The spring constant is the gradient of a force–extension graph ($F = k \times x$, so $k = F \div x$).",
                r"Choose two points on the line of best fit on gridline crossings: A $(0.04,\ 1.0)$ and B $(0.12,\ 3.0)$.",
                r"$\text{gradient} = \dfrac{3.0 - 1.0}{0.12 - 0.04} = \dfrac{2.0}{0.08} = 25$.",
                r"$k = 25$ N/m. The unit comes from the axes: newtons on $y$ per metre on $x$.",
            ],
        ),
        practice("Graphs", [
            group("kc-t4-q1", "The graph shows the velocity of a car.", [
                numeric("kc-t4-q1a", "Determine the gradient of the line.", t4_1_grad, "m/s²",
                        "Pick two points on the line: (0, 4) and P (10, 24).",
                        [r"$\text{gradient} = \dfrac{24 - 4}{10 - 0} = \dfrac{20}{10} = 2$ m/s²."], label="a"),
                numeric("kc-t4-q1b", "State the intercept on the velocity axis.", t4_1_int, "m/s",
                        "Where the line meets the vertical axis.",
                        [r"The line crosses the velocity axis at 4 m/s."], label="b"),
                choice("kc-t4-q1c", "What does the intercept represent?",
                       ["The maximum velocity", "The velocity at time zero — the car was already moving at 4 m/s", "The acceleration", "The distance travelled"], 1,
                       "At t = 0 the velocity is 4 m/s: the car was already moving when timing started. The gradient (2 m/s²) is the acceleration.", label="c"),
            ], graph=graph_t4_1),
            group("kc-t4-q2", "A student measures the resistance of different lengths of the same wire and plots the results.", [
                numeric("kc-t4-q2a", "Determine the gradient of the line of best fit.", t4_2, "Ω/m",
                        "Use the line, not the points: it runs from the origin to (1.0, 5.0).",
                        [r"$\text{gradient} = \dfrac{5.0 - 0}{1.0 - 0} = 5$ Ω/m."], label="a"),
                choice("kc-t4-q2b", "Why is a large triangle used to find the gradient?",
                       ["It looks neater", "Reading errors on the axes are a smaller fraction of a large change, so the gradient is more accurate", "Small triangles are not allowed", "The line is only straight in the middle"], 1,
                       "Each reading has an uncertainty of about half a small square; the bigger the triangle, the smaller that is as a fraction of the values used.", label="b"),
                written("kc-t4-q2c", "The point at 0.6 m lies slightly above the line. Explain whether the student should have drawn the line through it.",
                        marks(["No. A line of best fit follows the overall trend of all the points, with points balanced on either side.",
                               "It does not need to pass through every point (or any of them); the scatter is normal experimental variation.",
                               "Only a point far from the trend is treated as anomalous — this one is close to the line and is simply left where it is."]), lines=3, label="c"),
            ], graph=graph_t4_2),
            draw("kc-t4-q3", "A walker covers 20 m in the first 4 s, stands still for 2 s, then walks a further 20 m in the next 2 s. Draw the distance–time graph on the grid (tap the grid to place the points in order, or draw it on paper).",
                 blank_grid, "Three straight sections: from (0, 0) up to (4, 20); flat to (6, 20); then up to (8, 40). The last section is steeper because the walker is faster.",
                 answer_graph=answer_grid, check=True,
                 hint="Four points: the start, the end of each stage. Distance keeps the value it had while the walker stands still."),
            choice("kc-t4-q4", "A student's $y$-axis scale goes up in 3s (0, 3, 6, 9 …). Why would this lose a mark?",
                   ["Scales must start at zero", "Points cannot be plotted accurately when each small square is an awkward fraction", "The axis is too long", "It would not lose a mark"], 1,
                   "With 3 per large square each small square is 0.3 — hard to plot and to read. Scales go up in 1, 2, 5 or 10 (× any power of ten)."),
        ]),
    ],
)


# =====================================================================
# T5 · Proportionality
# =====================================================================

prop_graph = graph(
    axis("x", 10, 2), axis("y", 25, 5),
    [line([[0, 0], [10, 20]]), line([[0, 5], [10, 25]])],
    "Two parallel straight lines: A from the origin to (10, 20), B from (0, 5) to (10, 25). Only A shows direct proportion.",
    labels=[label(9.6, 17.2, "A: through the origin", anchor="end"), label(1.6, 11.8, "B: intercept 5", anchor="start")],
)

inv_points = [[round(x, 2), round(20 / x, 2)] for x in [1, 1.25, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10]]
inv_graph = graph(
    axis("volume in cm³", 10, 2), axis("pressure in kPa", 20, 5),
    [{"kind": "curve", "points": inv_points}],
    "A curve falling from (1, 20) towards the x-axis: pressure against volume at constant temperature.",
)

t5_q2 = 4 * 2 ** 2
t5_q3 = 12 / 3

section_t5 = section(
    "proportionality", "tricky", "Proportionality: from graphs and from data", "WS",
    equations=[r"y \propto x \iff \dfrac{y}{x} = \text{constant}", r"y \propto \dfrac{1}{x} \iff x \times y = \text{constant}"],
    blurb="\"Directly proportional\" is a precise claim: a straight line through the origin, or a constant ratio. A straight line on its own is not enough.",
    checklist=[
        "State what a graph must show for two quantities to be directly proportional",
        "Test a data table for direct proportion (constant y ÷ x) and inverse proportion (constant x × y)",
        "Describe a straight-line graph with an intercept correctly (linear, not proportional)",
        "Use a proportionality to predict a value",
    ],
    parts=[
        explain(
            "Proportional, linear, or neither",
            "<table class='tbl'><tr><th>Relationship</th><th>Graph</th><th>Test with numbers</th><th>Say</th></tr>"
            "<tr><td>Directly proportional, $y \\propto x$</td><td>Straight line <b>through the origin</b></td><td>$y \\div x$ is the same for every pair</td><td>\"$y$ is directly proportional to $x$\"</td></tr>"
            "<tr><td>Linear with an intercept</td><td>Straight line <b>not</b> through the origin</td><td>equal steps in $x$ give equal steps in $y$, but $y \\div x$ changes</td><td>\"$y$ increases linearly with $x$\" — not proportional</td></tr>"
            "<tr><td>Inversely proportional, $y \\propto \\dfrac{1}{x}$</td><td>Curve falling towards the axis, never touching it</td><td>$x \\times y$ is the same for every pair</td><td>\"$y$ is inversely proportional to $x$\"</td></tr>"
            "<tr><td>Proportional to the square, $y \\propto x^2$</td><td>Curve getting steeper through the origin</td><td>$y \\div x^2$ is constant; doubling $x$ gives $4y$</td><td>\"$y$ is proportional to $x$ squared\"</td></tr></table>",
            graph=prop_graph,
            after="<p>Line A passes through the origin: doubling $x$ from 4 to 8 doubles $y$ from 8 to 16 — proportional. Line B has the same gradient but an intercept of 5: doubling $x$ from 4 to 8 takes $y$ from 13 to 21, not double. B is <i>linear</i>, and \"$y$ increases by the same amount for each unit increase in $x$\" is the correct description; \"proportional\" would be marked wrong.</p>",
        ),
        explain(
            "Inverse proportion looks like this",
            "<p>Pressure against volume for a fixed mass of gas at constant temperature ($P_1 V_1 = P_2 V_2$). Every point on the curve has $P \\times V = 20$: $(1, 20)$, $(2, 10)$, $(4, 5)$, $(8, 2.5)$. The curve never reaches either axis.</p>"
            "<p>To get a straight line from an inverse relationship, plot $y$ against $\\dfrac{1}{x}$ — then it goes through the origin like any proportional graph.</p>",
            graph=inv_graph,
        ),
        worked(
            "Testing a data table",
            "A student records the current through a component at several potential differences: 2 V → 0.4 A; 4 V → 0.8 A; 6 V → 1.2 A; 8 V → 1.5 A. Is the current directly proportional to the potential difference?",
            [
                r"Test: $I \div V$ should be constant. $0.4 \div 2 = 0.2$; $0.8 \div 4 = 0.2$; $1.2 \div 6 = 0.2$; $1.5 \div 8 = 0.1875$.",
                r"The ratio is constant for the first three pairs and drops for the last, so the current is proportional to the p.d. <b>up to about 6 V</b>, then increases less than proportionally.",
                r"On a graph this is a straight line through the origin that starts to curve over — the resistance is increasing (a filament lamp getting hot).",
                r"The sentence: \"Up to 6 V, $I$ is directly proportional to $V$ because $I \div V$ is constant (0.2 A/V); above 6 V it is not, because the ratio falls.\"",
            ],
        ),
        practice("Proportionality", [
            choice("kc-t5-q1", "A graph of extension against force is a straight line through the origin up to 8 N, then curves upwards. Which statement is correct?",
                   ["Extension is proportional to force for all forces shown", "Extension is proportional to force up to 8 N only", "Extension is never proportional to force", "Extension is inversely proportional to force"], 1,
                   "Through the origin and straight = proportional. Where the line curves, equal increases in force no longer give equal increases in extension — the limit of proportionality has been passed."),
            numeric("kc-t5-q2", "The kinetic energy of an object is 4 J at a certain speed. Calculate the kinetic energy when the speed is doubled.", t5_q2, "J",
                    "KE ∝ v²: double v, multiply KE by 2² = 4.",
                    [r"$KE \propto v^2$, so $KE = 4 \times 2^2 = 16$ J."]),
            numeric("kc-t5-q3", "A gas has a pressure of 12 kPa at a volume of 2 m³. The temperature stays the same and the volume is increased to 6 m³. Calculate the new pressure.", t5_q3, "kPa",
                    "Inversely proportional: P × V is constant.",
                    [r"$P_1 V_1 = P_2 V_2$: $12 \times 2 = P_2 \times 6$.", r"$P_2 = \dfrac{24}{6} = 4$ kPa."]),
            choice("kc-t5-q4", "A set of results: x = 2, y = 7; x = 4, y = 11; x = 6, y = 15. Which description is correct?",
                   ["y is directly proportional to x", "y increases linearly with x but is not proportional to it", "y is inversely proportional to x", "y is proportional to x²"], 1,
                   "Equal steps (x up by 2, y up by 4) make it linear, but y ÷ x is 3.5, 2.75, 2.5 — not constant — so it is not proportional. The line would have an intercept of 3."),
            written("kc-t5-q5", "Describe the graph you would expect if you plotted the current through a fixed resistor against the potential difference across it, and state what the graph shows about the relationship.",
                    marks(["A straight line through the origin.",
                           "This shows the current is directly proportional to the potential difference (Ohm's law), because doubling V doubles I.",
                           "The gradient is 1 ÷ R (or: the resistance is constant)."]), lines=3),
            written("kc-t5-q6", "A student plots pressure against volume for a gas and gets a curve. Explain how she could plot the data to get a straight line, and what the line would show.",
                    marks(["Plot pressure against 1 ÷ volume (or volume against 1 ÷ pressure).",
                           "If pressure is inversely proportional to volume this gives a straight line through the origin.",
                           "Because P ∝ 1/V means P × V is constant: the gradient of the line is that constant."]), lines=3),
        ]),
    ],
)


# =====================================================================
# T6 · Planning a practical
# =====================================================================

section_t6 = section(
    "planning-practical", "tricky", "Planning a practical: the 6-mark method question", "WS",
    blurb="\"Describe how you would investigate…\" is worth six marks and most students get two. The same seven steps answer every version of it, in every topic.",
    checklist=[
        "Pick out the two variables a \"describe a method\" question is asking about",
        "Name the formula or relationship that links them",
        "Say which variable you change, how, and what you keep the same",
        "Say which variable you measure, how, and with what equipment",
        "Say what you will do with the results (a calculation or a graph)",
        "Give one specific detail that makes the results accurate",
        "Say you will repeat the readings and calculate a mean (both halves, or no mark)",
    ],
    parts=[
        explain(
            "Seven steps, every time",
            "<p>Whenever a question says <i>describe how you would investigate</i>, <i>plan an experiment</i> or <i>design a method</i>, write your answer in these seven steps, in this order. Each step is a mark, and examiners are looking for exactly these things.</p>"
            "<ol class='list'>"
            "<li><b>Read the question, and write down the two variables you are being asked to investigate.</b> One is the thing you will change (the independent variable); the other is the thing you will measure (the dependent variable).</li>"
            "<li><b>Figure out which formula links them.</b> Write it down. It tells you what else must be kept the same, and what to do with the results at the end.</li>"
            "<li><b>Say which one you will change and how you will change it</b> — e.g. \"add masses to the trolley\". Give a range or a number of values (\"five different masses\"), and say what you will keep the same so it is a fair test.</li>"
            "<li><b>Say which one you will measure, and how you will measure it, including the equipment to use</b> — e.g. \"record the speed at each light gate, and measure the distance between them with a ruler\".</li>"
            "<li><b>Say what you will do with the result</b> — e.g. \"use $a = F \\div m$ to calculate the acceleration\" or \"plot a graph of $F$ against $a$ and calculate the gradient\".</li>"
            "<li><b>Add a detail about the practical to make sure you get accurate results</b> — e.g. \"release the trolley from the same point each time\", \"keep the ramp at the same angle\", \"use light gates rather than a stopwatch so there is no reaction time\". One specific, relevant detail is enough.</li>"
            "<li><b>Say you will repeat the readings and calculate a mean.</b> Both halves are needed: writing \"repeat the experiment\" on its own does <b>not</b> get the mark — you must also say that you will <b>calculate a mean</b> of the repeats.</li>"
            "</ol>"
            "<p>Write the steps as numbered points, not as one paragraph. A labelled diagram of the equipment is worth adding if you have time, but it does not replace the words.</p>",
        ),
        explain(
            "Where the marks go missing",
            "<p>The two most common ways to lose marks are <b>describing the equipment without saying what you measure with it</b> (\"use a voltmeter\" earns nothing; \"use a voltmeter to measure the potential difference across the wire\" does), "
            "and <b>stopping after you have collected the data</b>. The question asked how you would <i>investigate</i> the link between the two variables, so the calculation or graph that shows the link is a mark in its own right. "
            "And the easiest mark on the paper is the one most often thrown away: <b>\"repeat\" alone scores nothing — \"repeat and calculate a mean\" scores</b>.</p>",
            tone="warn",
        ),
        worked(
            "Investigating resistance and length",
            "Describe how you would investigate how the resistance of a wire depends on its length. (6 marks)",
            [
                r"<b>Step 1 — the two variables.</b> I am investigating <b>length</b> of wire (independent, the one I change) and <b>resistance</b> (dependent, the one I measure).",
                r"<b>Step 2 — the formula.</b> Resistance is found from $R = V \div I$, so I need to measure the potential difference across the wire and the current through it. I expect $R$ to be proportional to length.",
                r"<b>Step 3 — what I change and how.</b> Stretch the wire along a metre rule and connect it into a circuit with crocodile clips. Change the length by moving one clip along the wire: 20 cm, 40 cm, 60 cm, 80 cm, 100 cm. Keep the same wire, the same cell and the current small so the wire does not heat up.",
                r"<b>Step 4 — what I measure and how.</b> For each length, read the potential difference across the wire with a voltmeter in parallel, and the current with an ammeter in series. Measure the length with the metre rule.",
                r"<b>Step 5 — what I do with the results.</b> Calculate $R = V \div I$ for each length, then plot a graph of resistance against length. A straight line through the origin shows $R \propto$ length.",
                r"<b>Step 6 — accuracy.</b> Switch the circuit off between readings so the wire does not warm up (its resistance would rise), and check the ammeter reads zero with the circuit open.",
                r"<b>Step 7 — repeat and mean.</b> Take three readings of $V$ and $I$ at each length and <b>calculate a mean</b> resistance before plotting.",
                r"<b>As it would be written in the exam:</b> seven numbered sentences, one per step — about ten lines. Every sentence contains either a variable, a piece of equipment and what it measures, or what is done with a number.",
            ],
        ),
        practice("Planning a practical", [
            written("kc-t6-q1",
                    "A student has a spring, a clamp stand, a metre rule and a set of 100 g masses. Describe how the student could investigate how the <b>extension</b> of the spring depends on the <b>force</b> applied to it. (6 marks)",
                    mark_scheme([
                        ("Variables", "Identifies the two variables: the <b>force</b> (weight of the hanging masses) is changed (independent) and the <b>extension</b> is measured (dependent)."),
                        ("Formula", "States that they are linked by $F = k \\times x$ (Hooke's law), with $F = m \\times g$ giving the force from each mass."),
                        ("Change", "Changes the force by adding 100 g masses one at a time (at least five values), using the same spring throughout."),
                        ("Measure", "Measures the extension with the metre rule: the new length minus the original (unstretched) length, read at eye level against a pointer."),
                        ("Use the result", "Plots a graph of force against extension; a straight line through the origin shows $F \\propto x$ and the gradient is the spring constant $k$."),
                        ("Accuracy", "One specific detail: reads the rule at eye level to avoid parallax, or fixes a pointer to the spring, or does not exceed the limit of proportionality (checks the spring returns to its original length)."),
                        ("Repeat &amp; mean", "Repeats the readings for each force (e.g. by unloading and reloading) <b>and calculates a mean</b> extension. \"Repeat\" on its own does not score."),
                    ], total=6, extra=[
                        "\"Use a ruler\" on its own does not earn the <i>Measure</i> mark — say what is measured and how the extension is found from it.",
                        "The <i>Use the result</i> mark needs the graph (or the calculation of $k$), not just \"record the results in a table\".",
                    ]),
                    lines=8,
                    hint="Step 1: the variables are force and extension. What do you add to change the force, and what must you subtract to get the extension?",
                    ),
            written("kc-t6-q2",
                    "Describe how you would investigate how the <b>current</b> through a filament lamp depends on the <b>potential difference</b> across it. (6 marks)",
                    mark_scheme([
                        ("Variables", "Identifies the two variables: the <b>potential difference</b> across the lamp is changed (independent) and the <b>current</b> through it is measured (dependent)."),
                        ("Formula", "States that they are linked by $V = I \\times R$, and that for a filament lamp the resistance is expected to increase as it heats up."),
                        ("Change", "Changes the potential difference using a variable resistor (or a variable power supply) in series, taking at least five values from zero upwards, using the same lamp."),
                        ("Measure", "Measures the current with an ammeter in series with the lamp and the potential difference with a voltmeter in parallel across it."),
                        ("Use the result", "Plots a graph of current against potential difference (an $I$–$V$ graph); a curve that flattens shows the resistance increasing. Or calculates $R = V \\div I$ at each p.d. and shows it rising."),
                        ("Accuracy", "One specific detail: switches off between readings so the lamp cools between measurements, or reverses the connections to take negative values as well, or uses meters with a suitable range."),
                        ("Repeat &amp; mean", "Repeats each reading <b>and calculates a mean</b> current for each potential difference. \"Repeat\" on its own does not score."),
                    ], total=6, extra=[
                        "Swapping the ammeter and voltmeter round (ammeter in parallel) loses the <i>Measure</i> mark.",
                    ]),
                    lines=8,
                    hint="What do you put in the circuit to change the p.d.? Where does each meter go?",
                    ),
        ], intro="Write the full answer on paper, as seven numbered points, before you open the mark scheme. Then mark yourself one mark per row — the question is out of six, so any six of the seven rows score."),
    ],
)


# =====================================================================
# T7 · Evaluating a method: accuracy, precision, errors
# =====================================================================

section_t7 = section(
    "evaluating-methods", "tricky", "Evaluating a method: accuracy, precision and errors", "WS",
    blurb="Accurate is not the same as precise, repeatable is not the same as reproducible, and \"human error\" is not an answer. The vocabulary is examined.",
    checklist=[
        "Define accuracy, precision, resolution, repeatable and reproducible",
        "Tell a random error from a systematic error, and say what reduces each",
        "Identify an anomalous result and say what to do with it",
        "Explain why repeating and averaging improves a result (and what it does not fix)",
    ],
    parts=[
        explain(
            "The words",
            "<table class='tbl'><tr><th>Word</th><th>Means</th><th>Example</th></tr>"
            "<tr><td><b>Accurate</b></td><td>Close to the true value</td><td>A balance reading 0.500 kg for a 500 g mass</td></tr>"
            "<tr><td><b>Precise</b></td><td>Repeated readings are close to each other (small spread)</td><td>0.512, 0.513, 0.512 kg — precise, but not accurate if the true value is 0.500 kg</td></tr>"
            "<tr><td><b>Resolution</b></td><td>The smallest change an instrument can show</td><td>A millimetre rule has a resolution of 1 mm; a digital balance 0.01 g</td></tr>"
            "<tr><td><b>Repeatable</b></td><td>The <i>same</i> person with the <i>same</i> equipment gets the same result again</td><td>Three timings within 0.1 s of each other</td></tr>"
            "<tr><td><b>Reproducible</b></td><td>A <i>different</i> person, or different equipment or method, gets the same result</td><td>Another group's value for $g$ agrees with yours</td></tr>"
            "<tr><td><b>Valid</b></td><td>The experiment actually tests what it claims to — only the independent variable was changed</td><td>Changing the force without also changing the mass</td></tr>"
            "<tr><td><b>Random error</b></td><td>Scatter: readings vary unpredictably above and below the true value</td><td>Reaction time on a stopwatch; reading a scale from slightly different angles</td></tr>"
            "<tr><td><b>Systematic error</b></td><td>Every reading is shifted the same way</td><td>A zero error on a balance; a rule with a worn end; a stopwatch that runs slow</td></tr>"
            "<tr><td><b>Zero error</b></td><td>A systematic error where the instrument reads something when it should read zero</td><td>A newtonmeter that reads 0.2 N with nothing on it</td></tr>"
            "<tr><td><b>Anomalous result</b></td><td>A reading that does not fit the pattern of the others</td><td>19.8, 20.1, 27.3, 20.0 s — the 27.3 s</td></tr></table>",
        ),
        explain(
            "What fixes what",
            "<p><b>Repeating and taking a mean</b> reduces the effect of <b>random</b> error, because the scatter above and below averages out. It does <b>nothing</b> for a <b>systematic</b> error — if the balance always reads 5 g high, the mean reads 5 g high too. Systematic errors are fixed by checking the zero, calibrating against a known value, or changing the method.</p>"
            "<p><b>An anomalous result</b> should be repeated if possible. If it cannot be, it is left out of the mean and circled on the graph — but you must say so.</p>"
            "<p><b>\"Human error\"</b> is never a creditworthy answer. Say what the error actually is: <i>reaction time when starting the stopwatch</i>, <i>parallax when reading the rule</i>, <i>the thermometer not being at the same depth each time</i>. Then say what reduces it: <i>light gates</i>, <i>reading at eye level</i>, <i>a clamp to hold the thermometer</i>.</p>"
            "<p><b>Higher resolution</b> means a smaller uncertainty in each reading — a digital stopwatch (0.01 s) over a wall clock (1 s) — but it does not help if the reading is dominated by reaction time (about 0.2 s).</p>",
            tone="warn",
        ),
        worked(
            "Evaluating a set of results",
            "A student times a pendulum's swing five times: 1.62 s, 1.58 s, 1.60 s, 1.91 s, 1.59 s. Her stopwatch has a resolution of 0.01 s. (a) Identify any anomalous result. (b) Calculate the mean. (c) Suggest one source of random error and how to reduce it. (d) Explain whether a stopwatch of resolution 0.001 s would improve the result.",
            [
                r"<b>(a)</b> 1.91 s is anomalous: it is far from the others, which are all within 0.04 s of each other.",
                r"<b>(b)</b> Leave it out: $\text{mean} = \dfrac{1.62 + 1.58 + 1.60 + 1.59}{4} = 1.60$ s (not divided by 5).",
                r"<b>(c)</b> Reaction time when starting and stopping the stopwatch — the student cannot press the button at exactly the end of a swing. Reduce it by timing ten swings and dividing by ten, so the reaction time is a smaller fraction of the measured time; or use a light gate.",
                r"<b>(d)</b> No. The reaction time (about 0.2 s) is much bigger than the resolution of either stopwatch, so a finer scale adds digits without adding accuracy. The limiting error is the method, not the instrument.",
            ],
        ),
        practice("Evaluating", [
            choice("kc-t7-q1", "A student's three readings of a resistance are 4.72 Ω, 4.71 Ω and 4.73 Ω. The true value is 5.00 Ω. The readings are:",
                   ["Accurate and precise", "Precise but not accurate", "Accurate but not precise", "Neither"], 1,
                   "The readings are close together (precise) but all well below the true value (not accurate) — the sign of a systematic error."),
            choice("kc-t7-q2", "Which of these is a systematic error?",
                   ["Starting the stopwatch slightly late on some runs and slightly early on others", "A balance that reads 2 g with nothing on the pan", "Reading a ruler from different angles each time", "Wind gusts affecting a falling object"], 1,
                   "A zero error shifts every reading the same way — systematic. The others vary from reading to reading: random."),
            written("kc-t7-q3", "Explain the difference between a repeatable result and a reproducible result.",
                    marks(["Repeatable: the same experimenter, using the same method and equipment, gets the same (or very similar) result when they do it again.",
                           "Reproducible: a different experimenter, or a different method or equipment, gets the same result."]), lines=2),
            written("kc-t7-q4", "A student measures the time for a ball to fall 2 m using a stopwatch and gets 0.74 s. Another student says \"the error was human error\". Explain why this is a poor evaluation, and give a better one.",
                    marks(["\"Human error\" does not say what went wrong or how to fix it, so it earns no credit.",
                           "The actual source is reaction time: the student cannot start and stop the stopwatch at exactly the right instants, which adds a random error of about 0.2 s to a fall of under a second.",
                           "Improvement: use a light gate or an electromagnetic release with an electronic timer, so the timing starts and stops automatically; or time a longer fall so the reaction time is a smaller fraction."]), lines=4),
            choice("kc-t7-q5", "Repeating readings and calculating a mean reduces the effect of:",
                   ["Systematic errors", "Random errors", "Zero errors", "All errors"], 1,
                   "Averaging cancels scatter — random error. A systematic shift is in every reading, so it survives the averaging unchanged."),
            written("kc-t7-q6", "A student measures a spring's extension with a rule whose end is worn, so every length reads 2 mm too short. State the type of error, explain its effect on a graph of force against extension, and describe how to correct it.",
                    marks(["A systematic (zero) error.",
                           "Every extension would be wrong by the same amount — but extension is a difference of two lengths, so the 2 mm cancels; if instead the raw lengths were plotted, the whole line would shift and the intercept would be wrong while the gradient stayed correct.",
                           "Correct it by measuring from a clear mark (e.g. the 10 cm line) rather than the worn end, or by subtracting the zero error from each reading."]), lines=4),
        ]),
    ],
)


# =====================================================================
# T8 · Estimation
# =====================================================================

t8_w = 70 * 10 * 0.5
t8_1 = 1000 * 10
t8_2 = 2000 * 2 * 60 * 60  # 2 kW for 2 hours in J
t8_3 = 70 * 10 * 3  # climbing 3 m of stairs
t8_4 = 100 / 60

section_t8 = section(
    "estimation", "tricky", "Estimation questions", "WS",
    equations=[],
    blurb="\"Estimate…\" means choose sensible values, say what you chose, calculate, and round. The method earns most of the marks, and the exact number is not what is being checked.",
    checklist=[
        "Recall sensible everyday values: masses, speeds, times, heights, powers",
        "State assumed values before using them",
        "Give an estimate to one or two significant figures with a unit, and sense-check it",
    ],
    parts=[
        explain(
            "How to answer an estimation question",
            "<p>An estimation question is marked on your <b>method and sensible values</b>, not on hitting one exact number. The examiner wants to see:</p>"
            "<ol class='list'><li><b>Assumed values</b>, written down with units — a mass, a speed, a time or distance.</li>"
            "<li>The <b>equation</b> you are using.</li>"
            "<li>The <b>calculation</b>, to 1 or 2 significant figures.</li>"
            "<li>A <b>sense check</b>: compare with something you know.</li></ol>"
            "<table class='tbl'><tr><th>Useful values to know</th><th></th></tr>"
            "<tr><td>Mass of an adult</td><td>70 kg</td></tr>"
            "<tr><td>Mass of a car</td><td>1000–1500 kg</td></tr>"
            "<tr><td>Height of a room / a floor of a building</td><td>3 m</td></tr>"
            "<tr><td>Height of a table</td><td>0.8 m</td></tr>"
            "<tr><td>Walking, running, cycling speed</td><td>1.5, 3, 6 m/s</td></tr>"
            "<tr><td>Car in town (30 mph), on a motorway (70 mph)</td><td>13, 30 m/s</td></tr>"
            "<tr><td>Power of a kettle, a car engine, a person</td><td>2 kW, 100 kW, 100 W</td></tr>"
            "<tr><td>Power of a phone charger, an LED lamp</td><td>5 W, 10 W</td></tr>"
            "<tr><td>Mass of an apple, a bag of sugar, a litre of water</td><td>0.1 kg, 1 kg, 1 kg</td></tr>"
            "<tr><td>Reaction time</td><td>0.2–0.7 s</td></tr>"
            "<tr><td>Speed of sound in air; speed of light</td><td>340 m/s; $3 \\times 10^8$ m/s</td></tr></table>"
            "<p>Any answer within a factor of two or so of the examiner's will be accepted <i>if your assumptions are stated and sensible</i>. An unexplained number on its own is not.</p>",
        ),
        worked(
            "Estimating an energy",
            "Estimate the work done by a student climbing one flight of stairs.",
            [
                r"<b>Assume:</b> mass $\approx 70$ kg; height of one floor $\approx 3$ m; $g = 10$ N/kg.",
                r"Work done against gravity $= $ gain in GPE $= m \times g \times h = 70 \times 10 \times 3 = 2100$ J.",
                r"Estimate: about $2000$ J (2 kJ).",
                r"<b>Sense check:</b> a chocolate bar stores about 1 MJ, so one flight of stairs is a tiny fraction of it — which matches experience.",
            ],
        ),
        practice("Estimation", [
            numeric("kc-t8-q1", "Estimate the weight of a family car.", t8_1, "N",
                    "Mass of a car ≈ 1000 kg; W = m × g.",
                    [r"Assume $m \approx 1000$ kg. $W = 1000 \times 10 = 10\,000$ N (about 10 kN)."], tolerance=0.6),
            numeric("kc-t8-q2", "Estimate the energy transferred by an electric heater left on for two hours.", t8_2, "J",
                    "A heater is about 2 kW; two hours in seconds.",
                    [r"Assume $P \approx 2000$ W; $t = 2 \times 3600 = 7200$ s.", r"$E = P \times t = 2000 \times 7200 \approx 1.4 \times 10^{7}$ J (about 14 MJ, or 4 kWh)."], tolerance=0.6),
            numeric("kc-t8-q3", "Estimate the power of a student who runs up a flight of stairs in 3 s.", 700, "W",
                    "Work done ≈ 2100 J (from the worked example); divide by the time.",
                    [r"$E \approx 70 \times 10 \times 3 = 2100$ J.", r"$P = \dfrac{E}{t} = \dfrac{2100}{3} = 700$ W — several times the 100 W a person sustains all day, which is why you cannot keep it up."], tolerance=0.5),
            numeric("kc-t8-q4", "Estimate the time it takes sound to travel the length of a football pitch.", 0.3, "s",
                    "A pitch is about 100 m; sound travels at 340 m/s.",
                    [r"$t = \dfrac{x}{v} = \dfrac{100}{340} \approx 0.3$ s."], tolerance=0.4),
            written("kc-t8-q5", "Describe how you would estimate the kinetic energy of a cyclist.",
                    marks(["State sensible assumed values: mass of cyclist plus bicycle about 80 kg; cycling speed about 6 m/s.",
                           "Use $KE = \\tfrac{1}{2} \\times m \\times v^2$.",
                           "$KE \\approx \\tfrac{1}{2} \\times 80 \\times 6^2 \\approx 1400$ J, given to 1 or 2 significant figures.",
                           "Sense-check it against a known value (e.g. a few times the energy to climb a step)."]), lines=4),
            choice("kc-t8-q6", "Which is the best estimate of the height of a two-storey house?", ["1 m", "3 m", "7 m", "30 m"], 2,
                   "Each floor is about 3 m, plus the roof: around 7 m. 30 m is a ten-storey block; 3 m is one floor."),
        ]),
    ],
)


SECTIONS = [section_t1, section_t2, section_t3, section_t4, section_t5, section_t6, section_t7, section_t8]
