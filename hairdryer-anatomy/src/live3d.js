
// ---------------------------------------------------------------
// Live behaviour.  geom.mjs and scene.js are inlined above this.
// ---------------------------------------------------------------

const TURN = Math.PI * 2;
const calm = matchMedia("(prefers-reduced-motion: reduce)");

// Ease a value toward a target.  "seconds" is roughly how long it takes.
function ease(value, target, dt, seconds) {
  if (calm.matches) {
    return target;
  }
  const next = value + (target - value) * (1 - Math.exp(-dt / seconds));
  if (Math.abs(target - next) < 0.002) {
    return target;
  }
  return next;
}

// Smooth start and stop between 0 and 1.
function smooth(t) {
  const x = Math.min(1, Math.max(0, t));
  return x * x * (3 - 2 * x);
}

// Mark one button in a group as pressed.
function press(buttons, chosen) {
  buttons.forEach((button) => {
    button.setAttribute("aria-pressed", button === chosen ? "true" : "false");
  });
}

// Let the viewer turn a figure by dragging it or with the arrow keys.
function makeTurnable(figure) {
  const stage = figure.stage;
  let from = null;

  stage.addEventListener("pointerdown", (event) => {
    from = { x: event.clientX, y: event.clientY, azimuth: figure.view.azimuth, elevation: figure.view.elevation };
    stage.setPointerCapture(event.pointerId);
    stage.setAttribute("data-dragging", "");
    figure.touched = true;
  });

  stage.addEventListener("pointermove", (event) => {
    if (!from) {
      return;
    }
    figure.view.azimuth = from.azimuth - (event.clientX - from.x) * 0.45;
    // Touch keeps vertical movement for scrolling the page.
    if (event.pointerType !== "touch") {
      const tilt = from.elevation + (event.clientY - from.y) * 0.3;
      figure.view.elevation = Math.min(70, Math.max(6, tilt));
    }
    figure.dirty = true;
  });

  const release = () => {
    from = null;
    stage.removeAttribute("data-dragging");
  };
  stage.addEventListener("pointerup", release);
  stage.addEventListener("pointercancel", release);

  stage.addEventListener("keydown", (event) => {
    let handled = true;
    if (event.key === "ArrowLeft") {
      figure.view.azimuth += 15;
    } else if (event.key === "ArrowRight") {
      figure.view.azimuth -= 15;
    } else if (event.key === "ArrowUp") {
      figure.view.elevation = Math.min(70, figure.view.elevation + 8);
    } else if (event.key === "ArrowDown") {
      figure.view.elevation = Math.max(6, figure.view.elevation - 8);
    } else {
      handled = false;
    }
    if (handled) {
      event.preventDefault();
      figure.touched = true;
      figure.dirty = true;
    }
  });
}

// ---------------- Figure 1: the whole dryer ----------------

// What each switch position does in a typical 1800 W dryer.
const LEVELS = [
  { name: "off", rpm: 0, watts: 0 },
  { name: "low", rpm: 15000, watts: 900 },
  { name: "high", rpm: 15000, watts: 1800 },
];
const AIR_FLOW = 0.036; // kg of air per second through the barrel
const AIR_HEAT_CAPACITY = 1005; // J per kg per kelvin
const ROOM = 20; // degrees C
const SHOWN_SPEED = 0.6; // turns per second on screen (the real fan does 250)
const CASE_ALPHA = [1, 0.2, 0]; // solid, see-through, hidden

const one = {
  stage: document.getElementById("stage1"),
  scene: document.querySelector("#stage1 [data-scene]"),
  readout: document.querySelectorAll("[data-readout]")[0],
  levelButtons: [...document.querySelectorAll("button[data-level]")],
  caseButtons: [...document.querySelectorAll("button[data-case]")],
  view: { azimuth: 60, elevation: 28, scale: 2.5, centre: [12, 0, 72], width: 860, height: 600 },
  level: 0,
  caseMode: 1,
  caseAlpha: CASE_ALPHA[1],
  touring: !calm.matches,
  touched: false,
  tourClock: 0,
  phi: 0.4, // angle of fan and armature
  speed: 0, // share of full speed, 0 to 1
  hot: 0, // share of full heater power, 0 to 1
  knob: 0,
  visible: true,
  dirty: true,
  lastText: "",
};

function drawOne() {
  const P = cameraFor(one.view);
  one.scene.innerHTML = dryerSvg({ phi: one.phi, caseAlpha: one.caseAlpha, knob: one.knob }, P);
  one.stage.style.setProperty("--hot", one.hot.toFixed(3));

  // Readout, from where the parts are now.
  const setting = LEVELS[one.level];
  const rpm = Math.round((setting.rpm * one.speed) / 500) * 500;
  const rise = (1800 * one.hot) / (AIR_FLOW * AIR_HEAT_CAPACITY);
  let text = setting.name + " · " + rpm.toLocaleString("en-GB") + " rpm · " + setting.watts.toLocaleString("en-GB") + " W";
  if (one.speed > 0.05) {
    text += " · air out " + Math.round(ROOM + rise) + " °C";
  }
  if (text !== one.lastText) {
    one.readout.textContent = text;
    one.lastText = text;
  }
  one.dirty = false;
}

function setLevel(level, byUser) {
  one.level = level;
  if (byUser) {
    one.touring = false;
  }
  press(one.levelButtons, one.levelButtons[level]);
}

function setCase(mode) {
  one.caseMode = mode;
  one.touring = false;
  press(one.caseButtons, one.caseButtons[mode]);
}

function stepOne(dt) {
  // Until someone touches it, the figure walks through Off, Low, High by itself.
  if (one.touched) {
    one.touring = false;
  }
  if (one.touring) {
    one.tourClock += dt;
    const stop = Math.floor(one.tourClock / 3.5) % 3;
    if (stop !== one.level) {
      setLevel(stop, false);
    }
  }
  const setting = LEVELS[one.level];
  const before = [one.speed, one.hot, one.knob, one.caseAlpha].join();
  one.speed = ease(one.speed, setting.rpm > 0 ? 1 : 0, dt, 0.5);
  one.hot = ease(one.hot, setting.watts / 1800, dt, 0.9);
  one.knob = ease(one.knob, one.level, dt, 0.12);
  one.caseAlpha = ease(one.caseAlpha, CASE_ALPHA[one.caseMode], dt, 0.35);
  const after = [one.speed, one.hot, one.knob, one.caseAlpha].join();
  if (!calm.matches && one.speed > 0) {
    one.phi += one.speed * SHOWN_SPEED * TURN * dt;
    one.dirty = true;
  }
  if (before !== after) {
    one.dirty = true;
  }
  if (one.dirty) {
    drawOne();
  }
}

one.levelButtons.forEach((button) => {
  button.addEventListener("click", () => {
    setLevel(Number(button.dataset.level), true);
  });
});

one.caseButtons.forEach((button) => {
  button.addEventListener("click", () => {
    setCase(Number(button.dataset.case));
  });
});

one.stage.addEventListener("keydown", (event) => {
  if (event.key === "0" || event.key === "1" || event.key === "2") {
    event.preventDefault();
    setLevel(Number(event.key), true);
  }
});

makeTurnable(one);

// ---------------- Figure 2: the motor ----------------

const MOTOR_CFG = { o: [0, 0, 0], S: 3, tint: true, lit: false, supply: true };
const STRIP_SECONDS = 4.2; // length of the strip-down animation

const two = {
  stage: document.getElementById("stage2"),
  scene: document.querySelector("#stage2 [data-scene]"),
  readout: document.querySelectorAll("[data-readout]")[1],
  stripButton: document.getElementById("strip"),
  labelButton: document.getElementById("labels"),
  spinButton: document.getElementById("spin"),
  slider: document.getElementById("angle"),
  sliderOut: document.getElementById("angle-out"),
  view: { azimuth: 60, elevation: 28, scale: 1.8, centre: [27, 0, -20], width: 860, height: 560 },
  spinning: !calm.matches,
  labels: true,
  phi: 0.35,
  stripTarget: 0, // 0 = cased, 1 = stripped to the working parts
  strip: 0, // progress of the animation, 0 to 1
  visible: true,
  dirty: true,
  touched: false,
};

// Where the strip-down animation has got to:
// first the parts slide apart, then the casing fades, then what is left closes up again.
function stripPose(progress) {
  let explode = 0;
  if (progress < 0.4) {
    explode = smooth(progress / 0.4);
  } else if (progress < 0.62) {
    explode = 1;
  } else {
    explode = 1 - smooth((progress - 0.62) / 0.38);
  }
  const fade = smooth((progress - 0.36) / 0.24);
  return { explode, caseAlpha: 0.3 * (1 - fade) };
}

function drawTwo() {
  const pose = stripPose(two.strip);
  // Keep the parts in the middle of the picture as they spread out.
  two.view.centre[0] = 27 + 42 * pose.explode;
  const P = cameraFor(two.view);
  two.scene.innerHTML = motorSvg(MOTOR_CFG, { phi: two.phi, explode: pose.explode, caseAlpha: pose.caseAlpha, labels: two.labels }, P);

  // Angle of the armature, and the total turning effect from the three coils.
  const degrees = Math.round((((two.phi % TURN) + TURN) % TURN) / TURN * 360) % 360;
  let torque = 0;
  let full = 0;
  for (let coil = 0; coil < 3; coil += 1) {
    torque += coilTorque(coil, two.phi);
    if (Math.abs(coilCurrent(coil, two.phi)) === 1) {
      full += 1;
    }
  }
  // The three coils together peak at 1.5 times what one coil gives at its best.
  const share = Math.round((torque / 1.5) * 100);
  let phase = "cased";
  if (two.strip > 0 && two.strip < 1) {
    phase = two.stripTarget === 1 ? "taking apart" : "rebuilding";
  } else if (two.strip === 1) {
    phase = "working parts only";
  }
  two.readout.textContent = phase + " · " + degrees + "° · " + full + " coil on full current · turning force " + share + "%";
  two.slider.value = String(degrees);
  two.sliderOut.textContent = degrees + "°";
  two.dirty = false;
}

function setSpinning(on) {
  two.spinning = on;
  two.spinButton.textContent = on ? "Pause" : "Spin";
  two.spinButton.setAttribute("aria-pressed", on ? "true" : "false");
}

function stepTwo(dt) {
  if (two.spinning) {
    two.phi += 0.12 * TURN * dt;
    two.dirty = true;
  }
  if (two.strip !== two.stripTarget) {
    const step = calm.matches ? 1 : dt / STRIP_SECONDS;
    if (two.stripTarget > two.strip) {
      two.strip = Math.min(1, two.strip + step);
    } else {
      two.strip = Math.max(0, two.strip - step);
    }
    two.dirty = true;
  }
  if (two.dirty) {
    drawTwo();
  }
}

two.stripButton.addEventListener("click", () => {
  two.stripTarget = two.stripTarget === 1 ? 0 : 1;
  two.stripButton.textContent = two.stripTarget === 1 ? "Rebuild" : "Strip down";
});

two.labelButton.addEventListener("click", () => {
  two.labels = !two.labels;
  two.labelButton.setAttribute("aria-pressed", two.labels ? "true" : "false");
  two.dirty = true;
});

two.spinButton.addEventListener("click", () => {
  setSpinning(!two.spinning);
});

two.slider.addEventListener("input", () => {
  // Turning it by hand stops the automatic spin.
  setSpinning(false);
  two.phi = (Number(two.slider.value) / 360) * TURN;
  two.dirty = true;
});

two.stage.addEventListener("keydown", (event) => {
  if (event.key === " ") {
    event.preventDefault();
    setSpinning(!two.spinning);
  }
});

makeTurnable(two);


// ---------------- Figure 3: the wiring, seen end-on ----------------
// A flat diagram looking along the shaft.  It turns with the armature in Fig 2.

const three = {
  stage: document.getElementById("stage3"),
  scene: document.querySelector("#stage3 [data-scene]"),
  readout: document.querySelectorAll("[data-readout]")[2],
  fieldButtons: [...document.querySelectorAll("button[data-field]")],
  mode: "curved", // "curved", "straight" or "computed" (flux lines from the solver)
  field: makeField(),
  fieldPhi: null, // rotor angle the solver was last set up for
  settling: 0, // frames still to spend refining the solution
  shown: null,
  visible: true,
};
const FLUX_SPACING = 4; // difference in A between neighbouring flux lines
const COIL_NAMES = ["A", "B", "C"];
// Direction of the magnetic field in the diagram: from the north magnet towards the south magnet.
const FIELD = [Math.cos(MOTOR.south), Math.sin(MOTOR.south)];

// Which commutator segment (0, 1, 2) a brush at this angle is touching.
function segmentUnder(brushAngle, phi) {
  let best = 0;
  let bestGap = 10;
  for (let k = 0; k < 3; k += 1) {
    const centre = phi + (k * TURN) / 3 - MOTOR.segmentLag;
    let gap = (centre - brushAngle) % TURN;
    if (gap > Math.PI) {
      gap -= TURN;
    }
    if (gap < -Math.PI) {
      gap += TURN;
    }
    if (Math.abs(gap) < bestGap) {
      bestGap = Math.abs(gap);
      best = k;
    }
  }
  return best;
}

function wiringSvg(phi, mode) {
  const computed = mode === "computed";
  const cx = 230;
  const cy = 215;
  // Angles run anticlockwise from the right, as in a maths diagram.
  const pol = (r, a) => [cx + r * Math.cos(a), cy - r * Math.sin(a)];
  const xy = (p) => p[0].toFixed(1) + " " + p[1].toFixed(1);
  const arc = (r, a0, a1) => {
    let d = "";
    const steps = 16;
    for (let index = 0; index <= steps; index += 1) {
      d += (index ? "L" : "M") + xy(pol(r, a0 + ((a1 - a0) * index) / steps));
    }
    return d;
  };
  const text = (p, value, cls) => '<text class="hd-wtext ' + cls + '" x="' + p[0].toFixed(1) + '" y="' + (p[1] + 5).toFixed(1) + '" text-anchor="middle">' + value + "</text>";
  let out = "";

  if (computed) {
    // The steel can, which carries the flux back round the outside.
    out += '<circle class="hd-wyoke" cx="' + cx + '" cy="' + cy + '" r="' + (FIELD_GRID.yoke.r0 + FIELD_GRID.yoke.r1) / 2 + '"/>';
    // Flux lines from the solver, with arrowheads where they cross the air gap.
    const lines = fluxLines(three.field, FLUX_SPACING, (x, y) => [cx + x, cy - y]);
    out += '<path class="hd-wflux" d="' + lines.d + '"/>';
    lines.heads.forEach((head) => {
      out += '<path class="hd-wfluxhead" transform="translate(' + head[0].toFixed(1) + " " + head[1].toFixed(1) + ") rotate(" + head[2].toFixed(1) + ')" d="M5 0L-4 -4L-4 4Z"/>';
    });
  } else if (mode === "curved") {
    // Smooth lines from the inner face of the north magnet to the inner face of the south magnet.
    // The faces are curved, and a field line leaves a pole face at right angles to it,
    // so each line sets off straight towards the shaft and the lines draw together in the middle.
    [-33, -22, -11, 0, 11, 22, 33].forEach((offset) => {
      const startAngle = MOTOR.north + offset * DEG;
      const endAngle = MOTOR.south - offset * DEG;
      const p0 = pol(150, startAngle);
      const p3 = pol(150, endAngle);
      // Control points on the same radius as each end, so the line starts and finishes radially.
      const p1 = pol(60, startAngle);
      const p2 = pol(60, endAngle);
      out += '<path class="hd-wflux" d="M' + xy(p0) + "C" + xy(p1) + " " + xy(p2) + " " + xy(p3) + '"/>';
      // Arrowhead a fifth of the way along, pointing from north to south.
      const t = 0.2;
      const u = 1 - t;
      const at = [0, 1].map((i) => u * u * u * p0[i] + 3 * u * u * t * p1[i] + 3 * u * t * t * p2[i] + t * t * t * p3[i]);
      const slope = [0, 1].map((i) => 3 * u * u * (p1[i] - p0[i]) + 6 * u * t * (p2[i] - p1[i]) + 3 * t * t * (p3[i] - p2[i]));
      const turn = (Math.atan2(slope[1], slope[0]) * 180) / Math.PI;
      out += '<path class="hd-wfluxhead" transform="translate(' + xy(at) + ") rotate(" + turn.toFixed(1) + ')" d="M5 0L-4 -4L-4 4Z"/>';
    });
  } else {
    // The field, drawn as straight lines from the north magnet to the south magnet.
    [-120, -40, 40, 120].forEach((offset) => {
      // Across the field direction by "offset", then along it.
      const along = (distance) => [cx + FIELD[0] * distance - FIELD[1] * offset, cy - (FIELD[1] * distance + FIELD[0] * offset)];
      const reach = Math.sqrt(150 * 150 - offset * offset) - 8;
      const turn = (Math.atan2(-FIELD[1], FIELD[0]) * 180) / Math.PI;
      out += '<path class="hd-wfield" d="M' + xy(along(-reach)) + "L" + xy(along(reach)) + '"/>';
      out += '<path class="hd-wfieldhead" transform="translate(' + xy(along(0)) + ") rotate(" + turn.toFixed(1) + ')" d="M5 0L-4 -4L-4 4Z"/>';
    });
  }

  // The two fixed magnets.
  [
    { centre: MOTOR.north, pole: "n", name: "N" },
    { centre: MOTOR.south, pole: "s", name: "S" },
  ].forEach((magnet) => {
    const a0 = magnet.centre - 40 * DEG;
    const a1 = magnet.centre + 40 * DEG;
    const band = arc(150, a0, a1) + arc(170, a1, a0).replace("M", "L") + "Z";
    out += '<path class="hd-tint" data-pole="' + magnet.pole + '" style="opacity:.5" d="' + band + '"/>';
    out += '<path class="iso-line" data-tone="mid" d="' + band + '"/>';
    out += text(pol(160, magnet.centre), magnet.name, "hd-wname hd-w" + magnet.pole);
  });

  // The three poles with their coils, and the wires to the commutator.
  for (let k = 0; k < 3; k += 1) {
    const psi = phi + (k * TURN) / 3;
    const current = coilCurrent(k, phi);
    const width = Math.abs(current) === 1 ? 3.4 : 1.6;
    const tone = Math.abs(current) === 1 ? "lit" : "mid";

    // The pole: a block pointing outward, tinted by the pole it has become.
    const c = Math.cos(psi);
    const n = Math.sin(psi);
    const local = (r, t) => [cx + r * c - t * n, cy - (r * n + t * c)];
    const block = "M" + xy(local(78, -24)) + "L" + xy(local(138, -24)) + "L" + xy(local(138, 24)) + "L" + xy(local(78, 24)) + "Z";
    out += '<path class="hd-wpole" d="' + block + '"/>';
    out += '<path class="hd-tint" data-pole="' + (current > 0 ? "n" : "s") + '" style="opacity:' + (Math.abs(current) === 1 ? 0.45 : 0.18) + '" d="' + block + '"/>';
    // The wire across the near end of the coil.  These parts lie in the page and give no turning force.
    let turns = "";
    for (let level = 0; level < 5; level += 1) {
      const r = 88 + level * 10;
      turns += "M" + xy(local(r, -24)) + "L" + xy(local(r, 24));
    }
    out += '<path class="iso-line" data-tone="lo" d="' + turns + '"/>';

    // The two long sides of the coil run along the shaft, so in this view they are seen end-on.
    // A dot means current coming out of the page, a cross means current going in.
    // For a north pole the current comes out on the anticlockwise side and goes in on the other.
    [1, -1].forEach((side) => {
      const outOfPage = current * side > 0;
      const at = local(108, side * 33);
      out += '<circle class="hd-wside" data-tone="' + tone + '" cx="' + at[0].toFixed(1) + '" cy="' + at[1].toFixed(1) + '" r="7.5"/>';
      if (outOfPage) {
        out += '<circle class="hd-wdot" cx="' + at[0].toFixed(1) + '" cy="' + at[1].toFixed(1) + '" r="2.4"/>';
      } else {
        out += '<path class="hd-wcross" d="M' + (at[0] - 4.4).toFixed(1) + " " + (at[1] - 4.4).toFixed(1) + "l8.8 8.8m0 -8.8l-8.8 8.8" + '"/>';
      }
      // Force on this side, from Fleming's left-hand rule: F is at right angles to the current and to the field.
      // With the current along the shaft and the field in the page, F = I x B lies in the page.
      const sign = outOfPage ? 1 : -1;
      let fy = -sign * FIELD[1];
      let fz = sign * FIELD[0];
      let length = Math.abs(current) === 1 ? 34 : 20;
      if (computed) {
        // Use the field the solver found at this spot instead of the straight-line one.
        const B = fieldAt(three.field, at[0] - cx, cy - at[1]);
        const strength = Math.hypot(B[0], B[1]) || 1e-9;
        fy = (-sign * B[1]) / strength;
        fz = (sign * B[0]) / strength;
        length = Math.min(46, (Math.abs(current) * strength * 34) / 0.3);
      }
      const start = [at[0] + fy * 10, at[1] - fz * 10];
      const end = [at[0] + fy * (10 + length), at[1] - fz * (10 + length)];
      const turn = (Math.atan2(end[1] - start[1], end[0] - start[0]) * 180) / Math.PI;
      out += '<path class="hd-wforce" d="M' + xy(start) + "L" + xy(end) + '"/>';
      out += '<path class="hd-wforcehead" transform="translate(' + xy(end) + ") rotate(" + turn.toFixed(1) + ')" d="M6 0L-4 -5L-4 5Z"/>';
    });
    out += text(local(108, 0), COIL_NAMES[k], "hd-wname");

    // Each coil joins the segment behind it to the segment ahead of it.
    const tabBehind = pol(46, psi - MOTOR.segmentLag);
    const tabAhead = pol(46, psi - MOTOR.segmentLag + TURN / 3);
    const wires = [
      [tabBehind, local(62, -17), local(88, -24)],
      [local(88, 24), local(62, 17), tabAhead],
    ];
    wires.forEach((points) => {
      out += '<path class="iso-line" data-tone="' + tone + '" style="stroke-width:' + width + 'px" d="M' + points.map(xy).join("L") + '"/>';
      // An arrowhead half way along, pointing the way the current flows.
      const a = current > 0 ? points[0] : points[2];
      const b = points[1];
      const angle = (Math.atan2(b[1] - a[1], b[0] - a[0]) * 180) / Math.PI;
      const mid = [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2];
      out += '<path class="hd-warrow" data-tone="' + tone + '" transform="translate(' + xy(mid) + ") rotate(" + angle.toFixed(1) + ')" d="M5 0L-4 -4.5L-4 4.5Z"/>';
    });
  }

  // Commutator: three copper segments with gaps between them.
  for (let k = 0; k < 3; k += 1) {
    const centre = phi + (k * TURN) / 3 - MOTOR.segmentLag;
    out += '<path class="hd-wseg" d="' + arc(38, centre - 54 * DEG, centre + 54 * DEG) + '"/>';
    out += '<circle class="hd-wtab" cx="' + pol(46, centre)[0].toFixed(1) + '" cy="' + pol(46, centre)[1].toFixed(1) + '" r="3"/>';
  }
  out += '<circle class="hd-wshaft" cx="' + cx + '" cy="' + cy + '" r="9"/>';

  // The two fixed brushes, pressing on the commutator from inside the diagram's ring.
  [
    { angle: MOTOR.brushPlus, sign: "+" },
    { angle: MOTOR.brushMinus, sign: "−" },
  ].forEach((brush) => {
    const c = Math.cos(brush.angle);
    const n = Math.sin(brush.angle);
    const local = (r, t) => [cx + r * c - t * n, cy - (r * n + t * c)];
    out += '<path class="hd-wbrush" d="M' + xy(local(13, -8)) + "L" + xy(local(33, -8)) + "L" + xy(local(33, 8)) + "L" + xy(local(13, 8)) + 'Z"/>';
    out += text(local(23, 0), brush.sign, "hd-wsign");
  });
  return out;
}

// Bring the solver up to date with the rotor, a few sweeps at a time.
// Returns true while the picture is still changing.
function refineField(phi) {
  if (three.fieldPhi !== phi) {
    const currents = [coilCurrent(0, phi), coilCurrent(1, phi), coilCurrent(2, phi)];
    setRotor(three.field, phi, currents, MOTOR.north, MOTOR.south);
    // The first solve starts from nothing, so give it a head start.
    const sweeps = three.fieldPhi === null ? 700 : 14;
    three.fieldPhi = phi;
    relax(three.field, sweeps);
    three.settling = 240;
    return true;
  }
  if (three.settling > 0) {
    three.settling -= 1;
    const change = relax(three.field, 14);
    if (change < 2e-4) {
      three.settling = 0;
    }
    return true;
  }
  return false;
}

function drawThree(phi) {
  const stamp = three.mode + phi;
  let changed = three.shown !== stamp;
  if (three.mode === "computed" && refineField(phi)) {
    changed = true;
  }
  if (!changed) {
    return;
  }
  three.shown = stamp;
  three.scene.innerHTML = wiringSvg(phi, three.mode);

  // Say in words which way the current is going.
  const plus = segmentUnder(MOTOR.brushPlus, phi);
  const minus = segmentUnder(MOTOR.brushMinus, phi);
  let alone = 0;
  let pair = [];
  if (minus === (plus + 1) % 3) {
    // Coil "plus" joins the two live segments directly.
    alone = plus;
    pair = [(plus + 2) % 3, (plus + 1) % 3];
  } else {
    alone = minus;
    pair = [plus, (plus + 1) % 3];
  }
  three.readout.textContent = "+ → " + COIL_NAMES[alone] + " → −   and   + → " + COIL_NAMES[pair[0]] + " → " + COIL_NAMES[pair[1]] + " → −";
}

three.fieldButtons.forEach((button) => {
  button.addEventListener("click", () => {
    three.mode = button.dataset.field;
    press(three.fieldButtons, button);
  });
});

// ---------------- one loop for all the figures ----------------

// Only animate a figure while it is on screen.
const watcher = new IntersectionObserver((entries) => {
  for (const entry of entries) {
    if (entry.target === one.stage) {
      one.visible = entry.isIntersecting;
    }
    if (entry.target === two.stage) {
      two.visible = entry.isIntersecting;
    }
    if (entry.target === three.stage) {
      three.visible = entry.isIntersecting;
    }
  }
}, { rootMargin: "120px 0px" });
watcher.observe(one.stage);
watcher.observe(two.stage);
watcher.observe(three.stage);

let lastTime = 0;

function frame(now) {
  let dt = 1 / 60;
  if (lastTime) {
    dt = Math.min((now - lastTime) / 1000, 1 / 20);
  }
  lastTime = now;
  if (one.visible) {
    stepOne(dt);
  }
  // The armature keeps turning if either the motor or its wiring diagram is on screen.
  if (two.visible || three.visible) {
    stepTwo(dt);
  }
  if (three.visible) {
    drawThree(two.phi);
  }
  requestAnimationFrame(frame);
}

// Test hook: lets a check script pose the figures directly.
window.__hairdryer = { one, two, setLevel, setCase, setSpinning, drawOne, drawTwo };

if (calm.matches) {
  setSpinning(false);
}
drawOne();
drawTwo();
drawThree(two.phi);
// Self-check: the coil the words call "alone" must be the one the model gives full current.
for (let d = 5; d < 360; d += 10) {
  const angle = (d / 360) * TURN;
  const p = segmentUnder(MOTOR.brushPlus, angle);
  const q = segmentUnder(MOTOR.brushMinus, angle);
  const lone = q === (p + 1) % 3 ? p : q;
  console.assert(Math.abs(coilCurrent(lone, angle)) === 1 && p !== q, "wiring mismatch at " + d);
  console.assert(Math.sign(coilCurrent(lone, angle)) === (q === (p + 1) % 3 ? 1 : -1), "direction mismatch at " + d);
}
requestAnimationFrame(frame);
