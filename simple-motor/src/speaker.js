
// ---------------------------------------------------------------
// The moving-coil loudspeaker.
// A magnet with a W-shaped cross-section (centre pole and outer ring), a coil round the
// centre pole, and a paper cone fixed to the coil.  geom.mjs and motor.js are inlined above this.
// The speaker is drawn cut in half so the W shape and the coil can be seen.
// ---------------------------------------------------------------

// ---------------- sizes (drawing units; the axis of the speaker runs along x) ----------------
const SPK = {
  boardZ: -66, // top of the baseboard
  plate: { x0: -40, x1: -32, r: 34 }, // the back of the magnet, joining the centre to the ring
  pole: { x0: -32, x1: 0, r: 10 }, // the centre pole (north)
  ring: { x0: -32, x1: 0, r: 34, inner: 24 }, // the outer ring (south)
  former: { x0: -24, x1: 12, r: 13 }, // the light tube the coil is wound on
  coil: { turns: [-21, -17, -13, -9], r: 15 }, // where each turn of the coil sits
  cone: { x0: 12, x1: 46, r0: 13, r1: 52 },
  frame: { x0: 46, x1: 50, r: 58, inner: 54 }, // the fixed rim that the cone's edge hangs from
  travel: 5, // how far the cone moves at full current
};
// The half of the speaker that is kept: the half on the +y side of the cut.
const SPK_KEPT = [-Math.PI / 2, Math.PI / 2];
const PITCHES = { low: 0.5, high: 1 }; // cycles per second on screen (a real speaker makes hundreds)
const GRAPH_SECONDS = 4;

// ---------------- the physics ----------------
// In the gap the field points outwards, from the centre pole (N) to the ring (S).
// The current runs round the coil, at right angles to that field, so the force on every part
// of the coil is along the axis.  A positive current here runs anticlockwise seen from the cone end,
// which gives a force into the magnet; a negative current gives a force out of it.

// How far the cone has moved along the axis (positive is outwards, away from the magnet).
function coneShift(current) {
  return -SPK.travel * current;
}

// ---------------- the 3D scene ----------------

// One turn of the coil, as the half behind the former and the half in front of it.
function turnPaths(F, x, P) {
  const V = viewDir(P);
  let back = "";
  let front = "";
  let run = [];
  let near = null;
  for (let degrees = -90; degrees <= 90; degrees += 10) {
    const angle = degrees * DEG;
    const screen = flat(pt(F, x, SPK.coil.r, angle), P);
    const facing = dot(radial(angle), V) > 0;
    if (near === null) {
      near = facing;
    }
    if (facing !== near) {
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

function speakerScene(state, P) {
  const V = viewDir(P);
  const F = { o: [0, 0, 0] };
  const shift = coneShift(state.current);
  const live = Math.min(1, Math.abs(state.current) / 0.06);
  const paint = (faces, options) => meshSvg(mesh(faces, P), options);
  // A round part cut in half: profile is [[x, radius], ...], thick is how far in from that radius it goes.
  const halfOf = (profile, thick, ends) => sector(F, profile, thick, SPK_KEPT[0], SPK_KEPT[1], { ends, step: 9 });
  const floor = SPK.boardZ + 0.2;

  // --- baseboard, stands, and the box that supplies the signal ---
  let out = paint(worldBox(-62, 86, -46, 74, SPK.boardZ - 6, SPK.boardZ), { tone: "mid" });
  out += paint(worldBox(-28, -4, 3, 15, SPK.boardZ, -33.6), { tone: "mid" });
  out += paint(worldBox(46, 50, 3, 11, SPK.boardZ, -57.8), { tone: "mid" });

  // The two leads: from the coil former, down to the board and across to the signal box.
  const leads =
    linePath([[6 + shift, 0, -SPK.former.r], [6, -8, -42], [6, -8, floor], [6, -25, floor], [40, -25, floor]], P, "hd-lead", "lit") +
    linePath([[2 + shift, 0, -SPK.former.r], [2, -14, -42], [2, -14, floor], [2, -31, floor], [40, -31, floor]], P, "hd-lead", "mid");
  let source = paint(worldBox(40, 72, -38, -18, SPK.boardZ, SPK.boardZ + 10), { tone: "hi", crease: "lo" });
  if (state.labels) {
    source += labelSvg([56, -28, SPK.boardZ + 20], P, "~", "plus");
  }
  // The leads and the box are on the near side of the cut, so they are painted last from that side.
  const cutSide = V[1] < 0;
  if (!cutSide) {
    out += leads + source;
  }

  // --- the three groups along the axis: back of the magnet, magnet with coil, cone ---
  const groups = [];

  {
    const plate = halfOf([[SPK.plate.x0, SPK.plate.r], [SPK.plate.x1, SPK.plate.r]], SPK.plate.r - 0.2, [true, true]);
    groups.push({ x: -36, svg: paint(plate.all, { tone: "mid" }) });
  }

  {
    const pole = halfOf([[SPK.pole.x0, SPK.pole.r], [SPK.pole.x1, SPK.pole.r]], SPK.pole.r - 0.2, [false, true]);
    const ring = halfOf([[SPK.ring.x0, SPK.ring.r], [SPK.ring.x1, SPK.ring.r]], SPK.ring.r - SPK.ring.inner, [false, true]);
    const former = halfOf([[SPK.former.x0 + shift, SPK.former.r], [0, SPK.former.r]], 1, [true, false]);
    const north = { pole: "n", alpha: 0.5 };
    const south = { pole: "s", alpha: 0.5 };
    let coilBack = "";
    let coilFront = "";
    for (const turn of SPK.coil.turns) {
      const paths = turnPaths(F, turn + shift, P);
      coilBack += paths.back;
      coilFront += paths.front;
    }
    // Far walls first, working inwards; then near walls, working outwards; then the cut faces.
    let svg = paint(ring.inner, { tone: "lo", tint: south });
    svg += '<path class="iso-line ind-wire" d="' + coilBack + '"/>';
    svg += paint(former.inner, { tone: "lo", cls: "cav" });
    svg += paint([...pole.outer, ...pole.caps], { tone: "hi", crease: "lo", tint: north });
    svg += paint([...former.outer, ...former.caps], { tone: "hi", crease: "lo" });
    svg += '<path class="iso-line ind-wire" d="' + coilFront + '"/>';
    svg += paint([...ring.outer, ...ring.caps], { tone: "hi", crease: "lo", tint: south });
    svg += paint(ring.cuts, { tone: "hi", crease: "lo", tint: south });
    svg += paint(pole.cuts, { tone: "hi", crease: "lo", tint: north });
    svg += paint(former.cuts, { tone: "hi" });
    groups.push({ x: -16, svg });
  }

  {
    const former = halfOf([[0, SPK.former.r], [SPK.cone.x0 + shift, SPK.former.r]], 1, [false, false]);
    const cone = halfOf([[SPK.cone.x0 + shift, SPK.cone.r0], [SPK.cone.x1 + shift, SPK.cone.r1]], 1.2, [false, true]);
    const frame = halfOf([[SPK.frame.x0, SPK.frame.r], [SPK.frame.x1, SPK.frame.r]], SPK.frame.r - SPK.frame.inner, [true, true]);
    let svg = paint(frame.inner, { tone: "lo" });
    svg += paint(cone.inner, { tone: "lo", cls: "cav" });
    svg += paint(former.inner, { tone: "lo", cls: "cav" });
    svg += paint(former.outer, { tone: "hi", crease: "lo" });
    svg += paint([...cone.outer, ...cone.caps], { tone: "hi", crease: "lo" });
    svg += paint([...frame.outer, ...frame.caps], { tone: "mid" });
    svg += paint([...former.cuts, ...cone.cuts, ...frame.cuts], { tone: "hi" });
    groups.push({ x: 25, svg });
  }

  // Paint the group furthest from the viewer first.
  groups.sort((a, b) => (a.x - b.x) * V[0]);
  out += groups.map((group) => group.svg).join("");

  if (!cutSide) {
    // Seen from behind there is no cut face to mark up.
    return out;
  }
  out += leads + source;

  // --- markings on the cut face ---
  // The field in the gap, from the centre pole out to the ring.
  if (state.showField) {
    [-1, 1].forEach((side) => {
      [-29.5, -1.5].forEach((x) => {
        out += linePath([[x, 0, side * SPK.pole.r], [x, 0, side * SPK.ring.inner]], P, "sm-field", "mid");
        out += arrowHead([x, 0, side * 19], [0, 0, side], P, "sm-fieldhead");
      });
    });
  }

  // Each turn of the coil where the cut goes through it: a dot or a cross for the current.
  let way = 1;
  if (state.current < 0) {
    way = -1;
  }
  [-1, 1].forEach((side) => {
    for (const turn of SPK.coil.turns) {
      const at = flat([turn + shift, 0, side * SPK.coil.r], P);
      out += '<circle class="hd-wside" cx="' + at[0].toFixed(1) + '" cy="' + at[1].toFixed(1) + '" r="3.6"/>';
      if (!state.showCurrent || live === 0) {
        continue;
      }
      // A positive current comes out of the cut face at the top of the coil and goes in at the bottom.
      const outOfFace = way * side > 0;
      if (outOfFace) {
        out += '<circle class="hd-wdot" opacity="' + live.toFixed(2) + '" cx="' + at[0].toFixed(1) + '" cy="' + at[1].toFixed(1) + '" r="1.4"/>';
      } else {
        out += '<path class="hd-wcross ind-cross" opacity="' + live.toFixed(2) + '" d="M' + (at[0] - 2.2).toFixed(1) + " " + (at[1] - 2.2).toFixed(1) + 'l4.4 4.4m0 -4.4l-4.4 4.4"/>';
      }
    }
  });

  // The force on the coil: along the axis, the same way at the top and the bottom.
  if (state.showForces && live > 0) {
    const push = -way; // +1 is out of the magnet, towards the cone
    const length = 8 + 20 * Math.abs(state.current);
    out += '<g opacity="' + live.toFixed(2) + '">';
    [-1, 1].forEach((side) => {
      const start = [-15 + shift, 0, side * 19.5];
      const end = [start[0] + push * length, 0, side * 19.5];
      out += linePath([start, end], P, "sm-force", "hi");
      out += arrowHead(end, [push, 0, 0], P, "sm-forcehead");
    });
    out += "</g>";
  }

  if (state.labels) {
    out += labelSvg([-27, 0, 0], P, "N", "n");
    out += labelSvg([-16, 0, 29], P, "S", "s");
    out += labelSvg([-16, 0, -29], P, "S", "s");
  }
  return out;
}

// ---------------- the cross-section diagram, with the signal graph ----------------

function speakerSectionSvg(state) {
  const cy = 150;
  const k = 2.2;
  const px = (x) => 150 + x * k;
  const py = (r) => cy - r * k;
  const fixed = (value) => value.toFixed(1);
  const shift = coneShift(state.current);
  const live = Math.min(1, Math.abs(state.current) / 0.06);
  let way = 1;
  if (state.current < 0) {
    way = -1;
  }
  let out = "";

  // Sound: bands of squashed air moving away from the cone while it is playing.
  if (state.playing) {
    const frequency = PITCHES[state.pitch];
    const spacing = 46 / (frequency / 0.5);
    const start = px(SPK.cone.x1) + 16;
    const offset = ((state.clock * frequency) % 1) * spacing;
    for (let x = start + offset; x < 452; x += spacing) {
      const far = (x - start) / (452 - start);
      const tall = 70 + 50 * far;
      const strength = state.volume * 0.75 * (1 - far);
      out += '<path class="spk-wave" opacity="' + strength.toFixed(2) + '" d="M' + fixed(x) + " " + fixed(cy - tall) + "Q" + fixed(x + 16) + " " + cy + " " + fixed(x) + " " + fixed(cy + tall) + '"/>';
    }
  }

  // The magnet: one piece with a W-shaped section (drawn on its side, opening towards the cone).
  const outline = [
    [SPK.plate.x0, -SPK.ring.r],
    [0, -SPK.ring.r],
    [0, -SPK.ring.inner],
    [SPK.plate.x1, -SPK.ring.inner],
    [SPK.plate.x1, -SPK.pole.r],
    [0, -SPK.pole.r],
    [0, SPK.pole.r],
    [SPK.plate.x1, SPK.pole.r],
    [SPK.plate.x1, SPK.ring.inner],
    [0, SPK.ring.inner],
    [0, SPK.ring.r],
    [SPK.plate.x0, SPK.ring.r],
  ];
  let shape = "";
  outline.forEach((corner, index) => {
    if (index === 0) {
      shape += "M";
    } else {
      shape += "L";
    }
    shape += fixed(px(corner[0])) + " " + fixed(py(corner[1]));
  });
  out += '<path class="sm-magnet" d="' + shape + 'Z"/>';
  // Tint the three limbs: north in the middle, south outside.
  const limbWidth = (0 - SPK.plate.x1) * k;
  const limbs = [
    { top: SPK.pole.r, bottom: -SPK.pole.r, pole: "n" },
    { top: SPK.ring.r, bottom: SPK.ring.inner, pole: "s" },
    { top: -SPK.ring.inner, bottom: -SPK.ring.r, pole: "s" },
  ];
  limbs.forEach((limb) => {
    out += '<rect class="hd-tint" data-pole="' + limb.pole + '" style="opacity:.5" x="' + fixed(px(SPK.plate.x1)) + '" y="' + fixed(py(limb.top)) + '" width="' + fixed(limbWidth) + '" height="' + fixed((limb.top - limb.bottom) * k) + '"/>';
    out += '<text class="hd-wtext hd-wname hd-w' + limb.pole + '" x="' + fixed(px(-27)) + '" y="' + fixed(py((limb.top + limb.bottom) / 2) + 5) + '" text-anchor="middle">' + limb.pole.toUpperCase() + "</text>";
  });
  out += '<path class="sm-magnet" style="fill:none" d="' + shape + 'Z"/>';

  // The field in the two gaps: outwards from the centre pole to the outer limbs.
  [-1, 1].forEach((side) => {
    [-29.5, -1.5].forEach((x) => {
      out += '<path class="hd-wflux" d="M' + fixed(px(x)) + " " + fixed(py(side * SPK.pole.r)) + "L" + fixed(px(x)) + " " + fixed(py(side * SPK.ring.inner)) + '"/>';
      let turn = -90;
      if (side < 0) {
        turn = 90;
      }
      out += '<path class="hd-wfluxhead" transform="translate(' + fixed(px(x)) + " " + fixed(py(side * 19)) + ") rotate(" + turn + ')" d="M5 0L-4 -4L-4 4Z"/>';
    });
  });

  // The fixed rim, and the flexible edge that joins the cone to it.
  [-1, 1].forEach((side) => {
    const rimTop = py(side * SPK.frame.r);
    const rimBottom = py(side * SPK.frame.inner);
    out += '<rect class="ind-bar" x="' + fixed(px(SPK.frame.x0)) + '" y="' + fixed(Math.min(rimTop, rimBottom)) + '" width="' + fixed((SPK.frame.x1 - SPK.frame.x0) * k) + '" height="' + fixed(Math.abs(rimTop - rimBottom)) + '"/>';
    out += '<path class="spk-edge" d="M' + fixed(px(SPK.cone.x1 + shift)) + " " + fixed(py(side * SPK.cone.r1)) + "L" + fixed(px(SPK.frame.x0 + 2)) + " " + fixed(py(side * SPK.frame.inner)) + '"/>';
    // The former and the cone, which move together.
    out += '<path class="spk-cone" d="M' + fixed(px(SPK.former.x0 + shift)) + " " + fixed(py(side * SPK.former.r)) + "L" + fixed(px(SPK.cone.x0 + shift)) + " " + fixed(py(side * SPK.cone.r0)) + "L" + fixed(px(SPK.cone.x1 + shift)) + " " + fixed(py(side * SPK.cone.r1)) + '"/>';
  });

  // The coil, cut through: one circle per turn above the centre pole and one below.
  [-1, 1].forEach((side) => {
    for (const turn of SPK.coil.turns) {
      const x = px(turn + shift);
      const y = py(side * SPK.coil.r);
      out += '<circle class="hd-wside" cx="' + fixed(x) + '" cy="' + fixed(y) + '" r="3.6"/>';
      if (live === 0) {
        continue;
      }
      const outOfPage = way * side > 0;
      if (outOfPage) {
        out += '<circle class="hd-wdot" opacity="' + live.toFixed(2) + '" cx="' + fixed(x) + '" cy="' + fixed(y) + '" r="1.4"/>';
      } else {
        out += '<path class="hd-wcross ind-cross" opacity="' + live.toFixed(2) + '" d="M' + fixed(x - 2.2) + " " + fixed(y - 2.2) + 'l4.4 4.4m0 -4.4l-4.4 4.4"/>';
      }
    }
    // The force on this part of the coil.
    if (live > 0) {
      const push = -way;
      const length = (8 + 20 * Math.abs(state.current)) * k;
      const startX = px(-15 + shift);
      const y = py(side * 19.7);
      const endX = startX + push * length;
      let turn = 0;
      if (push < 0) {
        turn = 180;
      }
      out += '<g opacity="' + live.toFixed(2) + '">';
      out += '<path class="hd-wforce" d="M' + fixed(startX) + " " + fixed(y) + "L" + fixed(endX) + " " + fixed(y) + '"/>';
      out += '<path class="hd-wforcehead" transform="translate(' + fixed(endX) + " " + fixed(y) + ") rotate(" + turn + ')" d="M6 0L-4 -5L-4 5Z"/>';
      out += "</g>";
    }
  });

  // --- graph: the current in the coil against time ---
  const gx = 40;
  const gw = 380;
  const middle = 365;
  const half = 40;
  out += '<path class="sm-axis" d="M' + gx + " " + (middle - half) + "L" + gx + " " + (middle + half) + "M" + gx + " " + middle + "L" + (gx + gw) + " " + middle + '"/>';
  out += '<text class="sm-tick" x="' + gx + '" y="' + (middle - half - 8) + '">current in the coil</text>';
  if (state.playing) {
    out += '<text class="sm-tick" x="' + (gx + gw) + '" y="' + (middle + half + 14) + '" text-anchor="end">time →</text>';
    const frequency = PITCHES[state.pitch];
    let curve = "";
    for (let step = 0; step <= 240; step += 1) {
      const time = (GRAPH_SECONDS * step) / 240;
      const value = state.volume * Math.sin(TAU * frequency * time);
      if (step === 0) {
        curve += "M";
      } else {
        curve += "L";
      }
      curve += fixed(gx + (gw * step) / 240) + " " + fixed(middle - half * value);
    }
    out += '<path class="sm-curve" d="' + curve + '"/>';
    const nowX = gx + gw * ((state.clock % GRAPH_SECONDS) / GRAPH_SECONDS);
    const nowY = middle - half * state.current;
    out += '<path class="sm-markline" d="M' + fixed(nowX) + " " + middle + "L" + fixed(nowX) + " " + fixed(nowY) + '"/>';
    out += '<circle class="sm-mark" cx="' + fixed(nowX) + '" cy="' + fixed(nowY) + '" r="4.5"/>';
  } else {
    // Set by hand: a steady current, so a level line.
    const level = middle - half * state.current;
    out += '<path class="sm-curve" d="M' + gx + " " + fixed(level) + "L" + (gx + gw) + " " + fixed(level) + '"/>';
    out += '<text class="sm-tick" x="' + gx + '" y="' + (middle + half + 14) + '">steady current: the cone moves and stays there</text>';
  }
  return out;
}

// ---------------- live behaviour ----------------

const spk = {
  stage: document.getElementById("stage4"),
  scene: document.querySelector("#stage4 [data-scene]"),
  flatStage: document.getElementById("stage5"),
  flat: document.querySelector("#stage5 [data-scene]"),
  readout: document.querySelectorAll("[data-readout]")[3],
  flatReadout: document.querySelectorAll("[data-readout]")[4],
  playButton: document.getElementById("spk-play"),
  pitchButtons: [...document.querySelectorAll("button[data-pitch]")],
  volumeButtons: [...document.querySelectorAll("button[data-volume]")],
  toggles: [...document.querySelectorAll("button[data-spk-show]")],
  slider: document.getElementById("spk-current"),
  view: { azimuth: -66, elevation: 22, scale: 2.45, centre: [10, 8, -12], width: 860, height: 520 },
  playing: !calm.matches,
  clock: 0,
  pitch: "low",
  volume: 0.5, // 0.5 quiet, 1 loud
  current: 0, // -1 to 1
  showCurrent: true,
  showForces: true,
  showField: true,
  labels: true,
  visible: true,
  dirty: true,
};

function drawSpeaker() {
  spk.scene.innerHTML = speakerScene(spk, cameraFor(spk.view));
  spk.flat.innerHTML = speakerSectionSvg(spk);

  const share = Math.round(spk.current * 100);
  let text = "no current · cone at rest";
  if (share > 2) {
    text = "current +" + share + "% · coil and cone pulled in";
  }
  if (share < -2) {
    text = "current −" + Math.abs(share) + "% · coil and cone pushed out";
  }
  spk.readout.textContent = text;
  let mode = "set by hand";
  if (spk.playing) {
    mode = "alternating current · cone vibrating";
  }
  spk.flatReadout.textContent = mode;
  spk.slider.value = String(share);
  spk.dirty = false;
}

function setSpeakerPlaying(on) {
  spk.playing = on;
  let label = "Play";
  let pressed = "false";
  if (on) {
    label = "Pause";
    pressed = "true";
  }
  spk.playButton.textContent = label;
  spk.playButton.setAttribute("aria-pressed", pressed);
  spk.dirty = true;
}

function stepSpeaker(dt) {
  if (spk.playing) {
    spk.clock += dt;
    spk.current = spk.volume * Math.sin(TAU * PITCHES[spk.pitch] * spk.clock);
    spk.dirty = true;
  }
  if (spk.dirty) {
    drawSpeaker();
  }
}

// Mark one button in a group as pressed.
function speakerPress(buttons, chosen) {
  buttons.forEach((button) => {
    let pressed = "false";
    if (button === chosen) {
      pressed = "true";
    }
    button.setAttribute("aria-pressed", pressed);
  });
}

spk.playButton.addEventListener("click", () => {
  setSpeakerPlaying(!spk.playing);
});

spk.pitchButtons.forEach((button) => {
  button.addEventListener("click", () => {
    spk.pitch = button.dataset.pitch;
    speakerPress(spk.pitchButtons, button);
    spk.dirty = true;
  });
});

spk.volumeButtons.forEach((button) => {
  button.addEventListener("click", () => {
    spk.volume = Number(button.dataset.volume);
    speakerPress(spk.volumeButtons, button);
    spk.dirty = true;
  });
});

spk.toggles.forEach((button) => {
  button.addEventListener("click", () => {
    const key = button.dataset.spkShow;
    spk[key] = !spk[key];
    let pressed = "false";
    if (spk[key]) {
      pressed = "true";
    }
    button.setAttribute("aria-pressed", pressed);
    spk.dirty = true;
  });
});

spk.slider.addEventListener("input", () => {
  // Setting the current by hand stops the signal and holds a steady current.
  setSpeakerPlaying(false);
  spk.current = Number(spk.slider.value) / 100;
  spk.dirty = true;
});

// Drag to turn the model round; arrow keys do the same.
{
  const stage = spk.stage;
  let from = null;
  stage.addEventListener("pointerdown", (event) => {
    from = { x: event.clientX, y: event.clientY, azimuth: spk.view.azimuth, elevation: spk.view.elevation };
    stage.setPointerCapture(event.pointerId);
    stage.setAttribute("data-dragging", "");
  });
  stage.addEventListener("pointermove", (event) => {
    if (!from) {
      return;
    }
    spk.view.azimuth = from.azimuth - (event.clientX - from.x) * 0.45;
    // Touch keeps vertical movement for scrolling the page.
    if (event.pointerType !== "touch") {
      const tilt = from.elevation + (event.clientY - from.y) * 0.3;
      spk.view.elevation = Math.min(70, Math.max(8, tilt));
    }
    spk.dirty = true;
  });
  const release = () => {
    from = null;
    stage.removeAttribute("data-dragging");
  };
  stage.addEventListener("pointerup", release);
  stage.addEventListener("pointercancel", release);
  stage.addEventListener("keydown", (event) => {
    if (event.key === "ArrowLeft") {
      spk.view.azimuth += 15;
    } else if (event.key === "ArrowRight") {
      spk.view.azimuth -= 15;
    } else if (event.key === "ArrowUp") {
      spk.view.elevation = Math.min(70, spk.view.elevation + 8);
    } else if (event.key === "ArrowDown") {
      spk.view.elevation = Math.max(8, spk.view.elevation - 8);
    } else if (event.key === " ") {
      setSpeakerPlaying(!spk.playing);
    } else {
      return;
    }
    event.preventDefault();
    spk.dirty = true;
  });
}

// Only animate while the speaker is on screen.
const speakerSeen = new Map();
const speakerWatcher = new IntersectionObserver((entries) => {
  for (const entry of entries) {
    speakerSeen.set(entry.target, entry.isIntersecting);
  }
  spk.visible = speakerSeen.get(spk.stage) !== false || speakerSeen.get(spk.flatStage) !== false;
}, { rootMargin: "120px 0px" });
speakerWatcher.observe(spk.stage);
speakerWatcher.observe(spk.flatStage);

let speakerLast = 0;

function speakerFrame(now) {
  let dt = 1 / 60;
  if (speakerLast) {
    dt = Math.min((now - speakerLast) / 1000, 1 / 20);
  }
  speakerLast = now;
  if (spk.visible) {
    stepSpeaker(dt);
  }
  requestAnimationFrame(speakerFrame);
}

// Test hook: lets a check script pose the speaker directly.
window.__speaker = { spk, drawSpeaker, setSpeakerPlaying };

if (calm.matches) {
  setSpeakerPlaying(false);
}
drawSpeaker();
requestAnimationFrame(speakerFrame);
