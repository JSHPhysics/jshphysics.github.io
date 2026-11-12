
// ---------------------------------------------------------------
// Electromagnetic induction.
// Part 1: a bar magnet pushed into and pulled out of a coil.
// Part 2: a coil turned between magnets (AC generator and dynamo), drawn by machine.js.
// geom.mjs and machine.js are inlined above this.
// ---------------------------------------------------------------

// ---------------- Part 1: sizes (drawing units) ----------------
const TUBE = { x0: -30, x1: 30, r: 20, wall: 1.5 }; // the card tube the coil is wound on
const WIRE = { x0: -26, x1: 26, r: 21.5 }; // the coil itself
const BAR = { length: 60, half: 8, out: -100, inside: 0 }; // the magnet, and where its centre can be
const BOARD_Z = -50; // top of the baseboard
const SPEEDS = { slow: 50, fast: 100 }; // how fast the magnet is moved, in units per second
const TRACE_SECONDS = 8; // how much history the graph shows

// ---------------- Part 1: the physics ----------------

// Share of the magnet's flux that passes through one turn of wire,
// when the turn is a distance z along the axis from the middle of the magnet.
// (This is the on-axis field of a uniformly magnetised bar, which is largest at its middle.)
function fluxThroughTurn(z) {
  const toFarEnd = z + BAR.length / 2;
  const toNearEnd = z - BAR.length / 2;
  const first = toFarEnd / Math.hypot(toFarEnd, WIRE.r);
  const second = toNearEnd / Math.hypot(toNearEnd, WIRE.r);
  return (first - second) / 2;
}

// Flux linkage: the flux through every turn added up, with the magnet's centre at x.
function fluxLinkage(x, turns) {
  const samples = 8;
  let total = 0;
  for (let index = 0; index < samples; index += 1) {
    const turnAt = WIRE.x0 + ((WIRE.x1 - WIRE.x0) * (index + 0.5)) / samples;
    total += fluxThroughTurn(turnAt - x);
  }
  return (total / samples) * turns;
}

// How quickly the flux linkage changes as the magnet moves (per unit of distance).
function linkageSlope(x, turns) {
  return fluxLinkage(x + 0.5, turns) - fluxLinkage(x - 0.5, turns);
}

// Scale the meter so the largest reading (10 turns, moved fast) is about full scale.
let steepest = 0;
for (let x = BAR.out; x <= BAR.inside; x += 1) {
  steepest = Math.max(steepest, Math.abs(linkageSlope(x, 10)));
}
const METER_SCALE = 1 / (steepest * SPEEDS.fast);

// The meter reading (-1 to 1) for a magnet at x moving at the given velocity.
// Faraday's law: the induced e.m.f. is minus the rate of change of flux linkage.
// A positive reading means current flowing round the coil anticlockwise as seen from its far (+x) end.
function meterReading(state) {
  const rate = state.pole * linkageSlope(state.x, state.turns) * state.velocity;
  const reading = -rate * METER_SCALE;
  return Math.max(-1.15, Math.min(1.15, reading));
}

// ---------------- Part 1: the 3D scene ----------------

// The coil of wire as two paths: the half behind the tube and the half in front of it.
function helixPaths(F, turns, P) {
  const V = viewDir(P);
  const count = turns * 36;
  let back = "";
  let front = "";
  let run = [];
  let near = null;
  for (let index = 0; index <= count; index += 1) {
    const share = index / count;
    const angle = -Math.PI / 2 + share * turns * TAU;
    const screen = flat(pt(F, WIRE.x0 + (WIRE.x1 - WIRE.x0) * share, WIRE.r, angle), P);
    const facing = dot(radial(angle), V) > 0;
    if (near === null) {
      near = facing;
    }
    if (facing !== near) {
      // The wire has just passed round the edge of the tube: finish this run and start the next.
      run.push(screen);
      if (near) {
        front += pathOf(run, false);
      } else {
        back += pathOf(run, false);
      }
      run = [screen];
      near = facing;
      continue;
    }
    run.push(screen);
  }
  if (run.length > 1) {
    if (near) {
      front += pathOf(run, false);
    } else {
      back += pathOf(run, false);
    }
  }
  return { back, front };
}

// The part of the magnet between two positions along the axis, as tinted boxes.
function barPiece(state, from, to, P) {
  const middle = state.x;
  // Which half is the north pole: the +x half when pole is +1.
  let leftPole = "s";
  let rightPole = "n";
  if (state.pole < 0) {
    leftPole = "n";
    rightPole = "s";
  }
  const halves = [
    { a: middle - BAR.length / 2, b: middle, pole: leftPole },
    { a: middle, b: middle + BAR.length / 2, pole: rightPole },
  ];
  // Paint the half that is further from the viewer first.
  if (viewDir(P)[0] < 0) {
    halves.reverse();
  }
  let out = "";
  for (const half of halves) {
    const low = Math.max(half.a, from);
    const high = Math.min(half.b, to);
    if (high - low < 0.05) {
      continue;
    }
    const faces = worldBox(low, high, -BAR.half, BAR.half, -BAR.half, BAR.half);
    out += meshSvg(mesh(faces, P), { tone: "hi", crease: "lo", tint: { pole: half.pole, alpha: 0.55 } });
  }
  return out;
}

function coilScene(state, P) {
  const V = viewDir(P);
  const F = { o: [0, 0, 0] };
  const solid = (faces, options) => meshSvg(mesh(faces, P), options);
  const reading = state.reading;
  const live = Math.min(1, Math.abs(reading) / 0.06);
  let way = 1;
  if (reading < 0) {
    way = -1;
  }
  const items = [];
  const depth = (point) => point[0] * V[0] + point[1] * V[1] + 0.15 * point[2] * V[2];
  const add = (at, svg) => {
    items.push({ depth: depth(at), svg });
  };

  // --- baseboard, with the two leads to the meter lying on it ---
  let out = solid(worldBox(-190, 78, -62, 44, BOARD_Z - 6, BOARD_Z), { tone: "mid" });
  const floor = BOARD_Z + 0.2;
  out += linePath([[-26, 0, floor], [-26, -38, floor], [22, -38, floor]], P, "hd-lead", "hi");
  out += linePath([[26, 0, floor], [26, -26, floor]], P, "hd-lead", "hi");
  if (state.showCurrent && live > 0) {
    // A positive current runs along the coil from its -x end to its +x end,
    // so it comes from the meter along the first lead and goes back along the second.
    out += '<g opacity="' + live.toFixed(2) + '">';
    out += arrowHead([-2, -38, floor], [-way, 0, 0], P, "sm-currenthead");
    out += arrowHead([26, -13, floor], [0, -way, 0], P, "sm-currenthead");
    out += "</g>";
  }

  // --- the coil on its tube, with whatever part of the magnet is inside it ---
  {
    let group = "";
    // The wire drops from each end of the coil to the board.
    group += linePath([[-26, 0, -WIRE.r], [-26, 0, floor]], P, "hd-lead", "hi");
    group += linePath([[26, 0, -WIRE.r], [26, 0, floor]], P, "hd-lead", "hi");
    // Two cradles under the tube.
    [-14, 14].forEach((x) => {
      group += solid(worldBox(x - 3, x + 3, -9, 9, BOARD_Z, -20.4), { tone: "mid" });
    });
    const helix = helixPaths(F, state.turns, P);
    const tube = sector(F, [[TUBE.x0, TUBE.r], [TUBE.x1, TUBE.r]], TUBE.wall, 0, TAU, { step: 9, ends: [true, true] });
    group += '<path class="iso-line ind-wire" d="' + helix.back + '"/>';
    group += solid(tube.inner, { tone: "lo", cls: "cav", alpha: 0.55 });
    group += barPiece(state, TUBE.x0, TUBE.x1 + 1, P);
    group += solid([...tube.outer, ...tube.caps], { tone: "hi", crease: "lo", alpha: 0.3 });
    group += '<path class="iso-line ind-wire" d="' + helix.front + '"/>';
    add([0, 0, 0], group);
  }

  // --- the part of the magnet outside the tube, and the handle it is pushed with ---
  {
    const handle = [
      solid(cylinder(F, state.x - 78, state.x - 70, 5), { tone: "mid" }),
      solid(cylinder(F, state.x - 70, state.x - BAR.length / 2, 2), { tone: "mid" }),
      barPiece(state, -1000, TUBE.x0, P),
    ];
    // Paint from the far end towards the viewer.
    if (V[0] < 0) {
      handle.reverse();
    }
    add([state.x - 50, 0, 0], handle.join(""));
  }

  // --- the meter: a box with a centre-zero dial on its top ---
  {
    const top = BOARD_Z + 12;
    let meter = solid(worldBox(22, 58, -50, -26, BOARD_Z, top), { tone: "hi", crease: "lo" });
    const scale = [];
    for (let step = -5; step <= 5; step += 1) {
      const angle = step * 0.2;
      scale.push([40 + 18 * Math.sin(angle), -46 + 18 * Math.cos(angle), top + 0.1]);
    }
    meter += linePath(scale, P, "", "lo");
    meter += linePath([[40, -31, top + 0.1], [40, -28, top + 0.1]], P, "", "mid");
    const swing = reading * 0.9;
    meter += linePath([[40, -46, top + 0.1], [40 + 16 * Math.sin(swing), -46 + 16 * Math.cos(swing), top + 0.1]], P, "sm-needle", "lit");
    add([40, -38, BOARD_Z + 6], meter);
  }

  items.sort((a, b) => a.depth - b.depth);
  out += items.map((item) => item.svg).join("");

  // --- overlays: current arrowheads on the coil, and pole labels ---
  if (state.showCurrent && live > 0) {
    // Put the arrowheads where the wire crosses the side of the tube that faces the viewer.
    let facing = Math.atan2(V[2], V[1]);
    let turnsRound = (facing + Math.PI / 2) / TAU;
    if (turnsRound < 0) {
      turnsRound += 1;
    }
    const chosen = [Math.round(state.turns * 0.25), Math.round(state.turns * 0.75) - 1];
    out += '<g opacity="' + live.toFixed(2) + '">';
    for (const turn of chosen) {
      const share = (turn + turnsRound) / state.turns;
      const point = pt(F, WIRE.x0 + (WIRE.x1 - WIRE.x0) * share, WIRE.r, facing);
      const along = tangent(facing);
      out += arrowHead(point, [0, along[1] * way, along[2] * way], P, "sm-currenthead");
    }
    out += "</g>";
  }
  if (state.labels) {
    // The magnet's own poles.
    out += labelSvg([state.x + state.pole * 22, 0, BAR.half + 14], P, "N", "n");
    out += labelSvg([state.x - state.pole * 22, 0, BAR.half + 14], P, "S", "s");
    // The poles the induced current gives the coil.  A positive current makes its +x end a north pole.
    if (live > 0) {
      let nearEnd = "s";
      let farEnd = "n";
      if (way < 0) {
        nearEnd = "n";
        farEnd = "s";
      }
      out += '<g class="ind-induced3d" opacity="' + live.toFixed(2) + '">';
      out += labelSvg([TUBE.x0 - 4, 0, TUBE.r + 22], P, nearEnd.toUpperCase(), nearEnd);
      out += labelSvg([TUBE.x1 + 4, 0, TUBE.r + 22], P, farEnd.toUpperCase(), farEnd);
      out += "</g>";
    }
  }
  return out;
}

// ---------------- Part 1: the side view and the trace ----------------

function coilSideSvg(state) {
  const reading = state.reading;
  const live = Math.min(1, Math.abs(reading) / 0.06);
  const cy = 118;
  const px = (x) => 300 + x * 1.3;
  const fixed = (value) => value.toFixed(1);
  let out = "";

  // --- the magnet's field, sketched as loops from its north end round to its south end ---
  const northX = px(state.x + state.pole * (BAR.length / 2));
  const southX = px(state.x - state.pole * (BAR.length / 2));
  const reach = state.pole * 58;
  [-1, 1].forEach((side) => {
    [34, 60].forEach((height) => {
      const p0 = [northX, cy + side * 6];
      const p1 = [northX + reach, cy + side * height * 1.5];
      const p2 = [southX - reach, cy + side * height * 1.5];
      const p3 = [southX, cy + side * 6];
      out += '<path class="hd-wflux" d="M' + fixed(p0[0]) + " " + fixed(p0[1]) + "C" + fixed(p1[0]) + " " + fixed(p1[1]) + " " + fixed(p2[0]) + " " + fixed(p2[1]) + " " + fixed(p3[0]) + " " + fixed(p3[1]) + '"/>';
      // Arrowhead half way round, pointing from north towards south.
      const midX = (p0[0] + 3 * p1[0] + 3 * p2[0] + p3[0]) / 8;
      const midY = (p0[1] + 3 * p1[1] + 3 * p2[1] + p3[1]) / 8;
      let turn = 180;
      if (southX > northX) {
        turn = 0;
      }
      out += '<path class="hd-wfluxhead" transform="translate(' + fixed(midX) + " " + fixed(midY) + ") rotate(" + turn + ')" d="M5 0L-4 -4L-4 4Z"/>';
    });
  });

  // --- the handle and the magnet ---
  const barLeft = px(state.x - BAR.length / 2);
  const barMiddle = px(state.x);
  const barHalf = BAR.half * 1.3;
  out += '<path class="ind-rod" d="M' + fixed(px(state.x - 70)) + " " + cy + "L" + fixed(barLeft) + " " + cy + '"/>';
  out += '<rect class="ind-bar" x="' + fixed(px(state.x - 78)) + '" y="' + (cy - 7) + '" width="' + fixed(8 * 1.3) + '" height="14"/>';
  let leftPole = "s";
  let rightPole = "n";
  if (state.pole < 0) {
    leftPole = "n";
    rightPole = "s";
  }
  const halfWidth = (BAR.length / 2) * 1.3;
  [
    { x: barLeft, pole: leftPole },
    { x: barMiddle, pole: rightPole },
  ].forEach((half) => {
    out += '<rect class="ind-bar" x="' + fixed(half.x) + '" y="' + fixed(cy - barHalf) + '" width="' + fixed(halfWidth) + '" height="' + fixed(barHalf * 2) + '"/>';
    out += '<rect class="hd-tint" data-pole="' + half.pole + '" style="opacity:.55" x="' + fixed(half.x) + '" y="' + fixed(cy - barHalf) + '" width="' + fixed(halfWidth) + '" height="' + fixed(barHalf * 2) + '"/>';
    out += '<text class="hd-wtext hd-wname hd-w' + half.pole + '" x="' + fixed(half.x + halfWidth / 2) + '" y="' + (cy + 5) + '" text-anchor="middle">' + half.pole.toUpperCase() + "</text>";
  });

  // --- the tube, and the coil seen in section: one circle per turn along the top and the bottom ---
  out += '<rect class="ind-tube" x="' + fixed(px(TUBE.x0)) + '" y="' + (cy - 26) + '" width="' + fixed(px(TUBE.x1) - px(TUBE.x0)) + '" height="52"/>';
  for (let turn = 0; turn < state.turns; turn += 1) {
    const x = px(WIRE.x0 + ((WIRE.x1 - WIRE.x0) * (turn + 0.5)) / state.turns);
    [-1, 1].forEach((side) => {
      const y = cy + side * 31;
      out += '<circle class="hd-wside" cx="' + fixed(x) + '" cy="' + y + '" r="3.7"/>';
      if (live === 0) {
        return;
      }
      // Seen from this side, a positive current comes towards you along the top of the coil
      // and goes away from you along the bottom.
      const towardsViewer = reading * side < 0;
      if (towardsViewer) {
        out += '<circle class="hd-wdot" opacity="' + live.toFixed(2) + '" cx="' + fixed(x) + '" cy="' + y + '" r="1.4"/>';
      } else {
        out += '<path class="hd-wcross ind-cross" opacity="' + live.toFixed(2) + '" d="M' + fixed(x - 2.3) + " " + (y - 2.3) + 'l4.6 4.6m0 -4.6l-4.6 4.6"/>';
      }
    });
  }

  // --- the poles the induced current gives the coil ---
  if (live > 0) {
    let nearEnd = "s";
    let farEnd = "n";
    if (reading < 0) {
      nearEnd = "n";
      farEnd = "s";
    }
    // The letters sit just outside each end of the coil, above the tube.
    out += '<g opacity="' + live.toFixed(2) + '">';
    out += '<text class="hd-wtext hd-wname hd-w' + nearEnd + '" x="' + fixed(px(TUBE.x0) - 13) + '" y="' + (cy - 44) + '" text-anchor="middle">' + nearEnd.toUpperCase() + "</text>";
    out += '<text class="hd-wtext hd-wname hd-w' + farEnd + '" x="' + fixed(px(TUBE.x1) + 13) + '" y="' + (cy - 44) + '" text-anchor="middle">' + farEnd.toUpperCase() + "</text>";
    out += '<text class="sm-tick ind-halo" x="' + fixed(px(0)) + '" y="' + (cy - 46) + '" text-anchor="middle">coil acts as</text>';
    out += "</g>";
  }

  // --- leads to the meter, and the meter ---
  const meterX = 415;
  const meterY = 232;
  let liveFlag = "0";
  if (live > 0) {
    liveFlag = "1";
  }
  out += '<path class="sm-lead" data-live="' + liveFlag + '" d="M' + fixed(px(WIRE.x0)) + " " + (cy + 66) + "L" + fixed(px(WIRE.x0)) + " " + (meterY + 12) + "L" + (meterX - 24) + " " + (meterY + 12) + '"/>';
  out += '<path class="sm-lead" data-live="' + liveFlag + '" d="M' + fixed(px(WIRE.x1)) + " " + (cy + 66) + "L" + fixed(px(WIRE.x1)) + " " + (meterY - 12) + "L" + (meterX - 24) + " " + (meterY - 12) + '"/>';
  out += '<path class="sm-lead" data-live="' + liveFlag + '" d="M' + fixed(px(WIRE.x0)) + " " + (cy + 35) + "L" + fixed(px(WIRE.x0)) + " " + (cy + 66) + "M" + fixed(px(WIRE.x1)) + " " + (cy + 35) + "L" + fixed(px(WIRE.x1)) + " " + (cy + 66) + '"/>';
  out += '<circle class="hd-wside" cx="' + meterX + '" cy="' + meterY + '" r="27"/>';
  out += '<path class="sm-axis" d="M' + meterX + " " + (meterY - 27) + "L" + meterX + " " + (meterY - 20) + '"/>';
  const swing = reading * 0.95;
  out += '<path class="sm-meterneedle" d="M' + meterX + " " + (meterY + 12) + "L" + fixed(meterX + 30 * Math.sin(swing)) + " " + fixed(meterY + 12 - 30 * Math.cos(swing)) + '"/>';

  // --- the trace: meter reading against time ---
  const gx = 40;
  const gw = 380;
  const middle = 385;
  const half = 45;
  out += '<path class="sm-axis" d="M' + gx + " " + (middle - half) + "L" + gx + " " + (middle + half) + "M" + gx + " " + middle + "L" + (gx + gw) + " " + middle + '"/>';
  out += '<text class="sm-tick" x="' + gx + '" y="' + (middle - half - 8) + '">meter reading</text>';
  out += '<text class="sm-tick" x="' + (gx + gw) + '" y="' + (middle + half + 14) + '" text-anchor="end">time →</text>';
  let trace = "";
  let lastX = gx + gw;
  let lastY = middle;
  state.trace.forEach((sample, index) => {
    const age = state.clock - sample.time;
    const x = gx + gw * (1 - age / TRACE_SECONDS);
    const y = middle - half * Math.max(-1, Math.min(1, sample.reading));
    if (index === 0) {
      trace += "M";
    } else {
      trace += "L";
    }
    trace += fixed(x) + " " + fixed(y);
    lastX = x;
    lastY = y;
  });
  if (trace) {
    out += '<path class="ind-trace" d="' + trace + '"/>';
  }
  out += '<circle class="sm-mark" cx="' + fixed(lastX) + '" cy="' + fixed(lastY) + '" r="4"/>';
  return out;
}

// ---------------- live behaviour: shared helpers ----------------

// Mark one button in a group as pressed.
function pressOnly(buttons, chosen) {
  buttons.forEach((button) => {
    let pressed = "false";
    if (button === chosen) {
      pressed = "true";
    }
    button.setAttribute("aria-pressed", pressed);
  });
}

// Let the viewer turn a 3D figure by dragging it or with the arrow keys.
function makeTurnable(figure) {
  const stage = figure.stage;
  let from = null;

  stage.addEventListener("pointerdown", (event) => {
    from = { x: event.clientX, y: event.clientY, azimuth: figure.view.azimuth, elevation: figure.view.elevation };
    stage.setPointerCapture(event.pointerId);
    stage.setAttribute("data-dragging", "");
  });

  stage.addEventListener("pointermove", (event) => {
    if (!from) {
      return;
    }
    figure.view.azimuth = from.azimuth - (event.clientX - from.x) * 0.45;
    // Touch keeps vertical movement for scrolling the page.
    if (event.pointerType !== "touch") {
      const tilt = from.elevation + (event.clientY - from.y) * 0.3;
      figure.view.elevation = Math.min(70, Math.max(8, tilt));
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
    if (event.key === "ArrowLeft") {
      figure.view.azimuth += 15;
    } else if (event.key === "ArrowRight") {
      figure.view.azimuth -= 15;
    } else if (event.key === "ArrowUp") {
      figure.view.elevation = Math.min(70, figure.view.elevation + 8);
    } else if (event.key === "ArrowDown") {
      figure.view.elevation = Math.max(8, figure.view.elevation - 8);
    } else {
      return;
    }
    event.preventDefault();
    figure.dirty = true;
  });
  addTiltButtons(stage, (step) => {
    const tilt = figure.view.elevation + step;
    figure.view.elevation = Math.min(70, Math.max(8, tilt));
    figure.dirty = true;
  });
}

// ---------------- Part 1: live behaviour ----------------

const coilFig = {
  stage: document.getElementById("stage-a"),
  scene: document.querySelector("#stage-a [data-scene]"),
  flatStage: document.getElementById("stage-b"),
  flat: document.querySelector("#stage-b [data-scene]"),
  readout: document.querySelectorAll("[data-readout]")[0],
  flatReadout: document.querySelectorAll("[data-readout]")[1],
  pushButton: document.getElementById("push"),
  pullButton: document.getElementById("pull"),
  flipButton: document.getElementById("flip"),
  speedButtons: [...document.querySelectorAll("button[data-speed]")],
  turnButtons: [...document.querySelectorAll("button[data-turns]")],
  toggles: [...document.querySelectorAll("button[data-coil-show]")],
  slider: document.getElementById("magnet"),
  view: { azimuth: -62, elevation: 26, scale: 2.05, centre: [-56, -9, -24], width: 860, height: 500 },
  x: BAR.out, // where the middle of the magnet is
  previousX: BAR.out,
  velocity: 0, // how fast it is moving, smoothed
  drive: 0, // the speed it is being pushed at
  target: null, // where a Push in or Pull out is taking it, or null
  speed: "slow",
  turns: 5,
  pole: 1, // +1: north pole leads into the coil
  reading: 0,
  trace: [],
  clock: 0,
  showCurrent: true,
  labels: true,
  touring: !calm.matches, // until someone touches it, it pushes in and pulls out by itself
  tourWait: 1,
  visible: true,
  dirty: true,
};

function drawCoil() {
  const c = coilFig;
  c.scene.innerHTML = coilScene(c, cameraFor(c.view));
  c.flat.innerHTML = coilSideSvg(c);

  // Say what is happening, in words.
  let motion = "magnet still";
  if (c.velocity > 3) {
    motion = "magnet moving in";
  }
  if (c.velocity < -3) {
    motion = "magnet moving out";
  }
  let needle = "no current";
  if (c.reading > 0.03) {
    needle = "needle to the right";
  }
  if (c.reading < -0.03) {
    needle = "needle to the left";
  }
  c.readout.textContent = motion + " · " + needle;
  c.flatReadout.textContent = c.turns + " turns · reading " + Math.round(c.reading * 100) + "% of full scale";
  c.slider.value = String(Math.round(c.x - BAR.out));
  c.dirty = false;
}

function stepCoil(dt) {
  const c = coilFig;

  // The self-running demonstration: push in, wait, pull out, wait.
  if (c.touring && c.target === null) {
    c.tourWait -= dt;
    if (c.tourWait <= 0) {
      if (c.x < (BAR.out + BAR.inside) / 2) {
        c.target = BAR.inside;
      } else {
        c.target = BAR.out;
      }
      c.tourWait = 1.5;
    }
  }

  // Move towards the target at the chosen speed, easing in and out.
  if (c.target !== null) {
    const top = SPEEDS[c.speed];
    let wanted = 6 * (c.target - c.x);
    wanted = Math.max(-top, Math.min(top, wanted));
    c.drive += (wanted - c.drive) * (1 - Math.exp(-dt / 0.08));
    c.x += c.drive * dt;
    if (Math.abs(c.target - c.x) < 0.2 && Math.abs(c.drive) < 2) {
      c.x = c.target;
      c.target = null;
      c.drive = 0;
    }
  }

  // Work out how fast the magnet is really moving (it may be being dragged by the slider).
  const measured = (c.x - c.previousX) / dt;
  c.previousX = c.x;
  c.velocity += (measured - c.velocity) * (1 - Math.exp(-dt / 0.05));
  if (Math.abs(c.velocity) < 0.05) {
    c.velocity = 0;
  }
  // Test hook: pretend the magnet is moving at a fixed speed, for still screenshots.
  if (c.hold !== undefined) {
    c.velocity = c.hold;
  }
  c.reading = meterReading(c);

  // Record the reading for the trace, and drop anything older than the graph shows.
  c.clock += dt;
  c.trace.push({ time: c.clock, reading: c.reading });
  while (c.trace.length > 0 && c.clock - c.trace[0].time > TRACE_SECONDS) {
    c.trace.shift();
  }
  drawCoil();
}

function stopTour() {
  coilFig.touring = false;
}

coilFig.pushButton.addEventListener("click", () => {
  stopTour();
  coilFig.target = BAR.inside;
});

coilFig.pullButton.addEventListener("click", () => {
  stopTour();
  coilFig.target = BAR.out;
});

coilFig.flipButton.addEventListener("click", () => {
  // Turn the magnet round.  It is taken out first, so nothing is induced by the turn itself.
  stopTour();
  const c = coilFig;
  c.pole = -c.pole;
  c.x = BAR.out;
  c.previousX = BAR.out;
  c.velocity = 0;
  c.drive = 0;
  c.target = null;
  let pressed = "false";
  if (c.pole < 0) {
    pressed = "true";
  }
  c.flipButton.setAttribute("aria-pressed", pressed);
});

coilFig.speedButtons.forEach((button) => {
  button.addEventListener("click", () => {
    stopTour();
    coilFig.speed = button.dataset.speed;
    pressOnly(coilFig.speedButtons, button);
  });
});

coilFig.turnButtons.forEach((button) => {
  button.addEventListener("click", () => {
    stopTour();
    coilFig.turns = Number(button.dataset.turns);
    pressOnly(coilFig.turnButtons, button);
  });
});

coilFig.toggles.forEach((button) => {
  button.addEventListener("click", () => {
    const key = button.dataset.coilShow;
    coilFig[key] = !coilFig[key];
    let pressed = "false";
    if (coilFig[key]) {
      pressed = "true";
    }
    button.setAttribute("aria-pressed", pressed);
  });
});

coilFig.slider.addEventListener("input", () => {
  // Moving the magnet by hand: how fast you drag sets how big the reading is.
  stopTour();
  coilFig.target = null;
  coilFig.drive = 0;
  coilFig.x = BAR.out + Number(coilFig.slider.value);
});

coilFig.stage.addEventListener("pointerdown", stopTour);
makeTurnable(coilFig);

// ---------------- Part 2: live behaviour ----------------

const gen = {
  stage: document.getElementById("stage-c"),
  scene: document.querySelector("#stage-c [data-scene]"),
  flatStage: document.getElementById("stage-d"),
  flat: document.querySelector("#stage-d [data-scene]"),
  readout: document.querySelectorAll("[data-readout]")[2],
  flatReadout: document.querySelectorAll("[data-readout]")[3],
  designButtons: [...document.querySelectorAll("button[data-design]")],
  rateButtons: [...document.querySelectorAll("button[data-rate]")],
  spinButton: document.getElementById("spin"),
  reverseButton: document.getElementById("reverse"),
  magnetButton: document.getElementById("magnets"),
  toggles: [...document.querySelectorAll("button[data-gen-show]")],
  slider: document.getElementById("angle"),
  sliderOut: document.getElementById("angle-out"),
  view: { azimuth: 38, elevation: 30, scale: 2.35, centre: [10, 0, -20], width: 860, height: 560 },
  design: "slip", // "slip": AC generator.  "dynamo": split ring.
  phi: 0.5, // angle of the yellow side of the coil
  spinning: !calm.matches,
  speedFactor: 0.5, // 0.5 at normal speed, 1 when turned fast
  turnWay: 1, // +1 anticlockwise seen from the ring end
  magnets: 1,
  battery: 1, // not used by the generators; the shared drawing code expects it
  showCurrent: true,
  showForces: true, // shown as "Motion" on this page
  showField: true,
  labels: true,
  visible: true,
  dirty: true,
};

function drawGen() {
  const g = gen;
  g.scene.innerHTML = motorScene(g, cameraFor(g.view));
  g.flat.innerHTML = endOnSvg(g);

  const degrees = Math.round((((g.phi % TURN) + TURN) % TURN) / TURN * 360) % 360;
  const state = coilState(g);
  const share = Math.round(Math.abs(state.meter) * 100);
  let text = degrees + "° · meter " + share + "% of full scale";
  if (share < 2) {
    text = degrees + "° · coil upright: no current";
  }
  let turned = "turned anticlockwise";
  if (g.turnWay < 0) {
    turned = "turned clockwise";
  }
  let kind = "alternating current";
  if (g.design === "dynamo") {
    kind = "direct current, pulsing";
  }
  g.readout.textContent = text;
  g.flatReadout.textContent = "seen from the ring end · " + turned + " · " + kind;
  g.slider.value = String(degrees);
  g.sliderOut.textContent = degrees + "°";
  g.dirty = false;
}

function setGenSpinning(on) {
  gen.spinning = on;
  let label = "Spin";
  let pressed = "false";
  if (on) {
    label = "Pause";
    pressed = "true";
  }
  gen.spinButton.textContent = label;
  gen.spinButton.setAttribute("aria-pressed", pressed);
}

function stepGen(dt) {
  if (gen.spinning) {
    // Someone turns the handle at a steady speed: twice as fast when "Fast" is chosen.
    gen.phi += gen.turnWay * 1.5 * (gen.speedFactor / 0.5) * dt;
    gen.dirty = true;
  }
  if (gen.dirty) {
    drawGen();
  }
}

gen.designButtons.forEach((button) => {
  button.addEventListener("click", () => {
    gen.design = button.dataset.design;
    pressOnly(gen.designButtons, button);
    // Show the notes that belong to this machine.
    document.querySelectorAll("[data-for]").forEach((block) => {
      block.hidden = block.dataset.for !== gen.design;
    });
    gen.dirty = true;
  });
});

gen.rateButtons.forEach((button) => {
  button.addEventListener("click", () => {
    gen.speedFactor = Number(button.dataset.rate);
    pressOnly(gen.rateButtons, button);
    gen.dirty = true;
  });
});

gen.spinButton.addEventListener("click", () => {
  setGenSpinning(!gen.spinning);
});

gen.reverseButton.addEventListener("click", () => {
  gen.turnWay = -gen.turnWay;
  let pressed = "false";
  if (gen.turnWay < 0) {
    pressed = "true";
  }
  gen.reverseButton.setAttribute("aria-pressed", pressed);
  gen.dirty = true;
});

gen.magnetButton.addEventListener("click", () => {
  gen.magnets = -gen.magnets;
  let pressed = "false";
  if (gen.magnets < 0) {
    pressed = "true";
  }
  gen.magnetButton.setAttribute("aria-pressed", pressed);
  gen.dirty = true;
});

gen.toggles.forEach((button) => {
  button.addEventListener("click", () => {
    const key = button.dataset.genShow;
    gen[key] = !gen[key];
    let pressed = "false";
    if (gen[key]) {
      pressed = "true";
    }
    button.setAttribute("aria-pressed", pressed);
    gen.dirty = true;
  });
});

gen.slider.addEventListener("input", () => {
  // Setting the angle by hand stops the turning, and shows that moment frozen.
  setGenSpinning(false);
  gen.phi = (Number(gen.slider.value) / 360) * TURN;
  gen.dirty = true;
});

gen.stage.addEventListener("keydown", (event) => {
  if (event.key === " ") {
    event.preventDefault();
    setGenSpinning(!gen.spinning);
  }
});

makeTurnable(gen);

// ---------------- one loop for the whole page ----------------

// Only animate a part while one of its figures is on screen.
const onScreen = new Map();
const watcher = new IntersectionObserver((entries) => {
  for (const entry of entries) {
    onScreen.set(entry.target, entry.isIntersecting);
  }
  coilFig.visible = onScreen.get(coilFig.stage) !== false || onScreen.get(coilFig.flatStage) !== false;
  gen.visible = onScreen.get(gen.stage) !== false || onScreen.get(gen.flatStage) !== false;
}, { rootMargin: "120px 0px" });
[coilFig.stage, coilFig.flatStage, gen.stage, gen.flatStage].forEach((stage) => {
  watcher.observe(stage);
});

let lastTime = 0;

function frame(now) {
  let dt = 1 / 60;
  if (lastTime) {
    dt = Math.min((now - lastTime) / 1000, 1 / 20);
  }
  lastTime = now;
  if (coilFig.visible) {
    stepCoil(dt);
  }
  if (gen.visible) {
    stepGen(dt);
  }
  requestAnimationFrame(frame);
}

// Test hook: lets a check script pose the figures directly.
window.__induction = { coilFig, gen, drawCoil, drawGen, setGenSpinning, meterReading };

if (calm.matches) {
  setGenSpinning(false);
}
drawCoil();
drawGen();
requestAnimationFrame(frame);
