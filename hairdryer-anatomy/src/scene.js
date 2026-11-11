
// ---------------------------------------------------------------
// Scenes.  Everything is redrawn from geometry each frame, so the
// camera can go anywhere.  geom.mjs is inlined above this file.
// ---------------------------------------------------------------

// A camera that keeps one world point in the middle of the picture.
function cameraFor(view) {
  const P = { origin: [0, 0], scale: view.scale, azimuth: view.azimuth, elevation: view.elevation };
  const middle = flat(view.centre, P);
  P.origin = [view.width / 2 - middle[0], view.height / 2 - middle[1]];
  return P;
}

// A flat round face at position s along the axis.  side is +1 (faces +x) or -1.
// It uses the same angular steps as the wall it closes, so their edges line up.
function discFace(F, s, r, side, stepDegrees) {
  const count = Math.ceil(360 / stepDegrees);
  const pts = [];
  for (let index = 0; index < count; index += 1) {
    pts.push(pt(F, s, r, (TAU * index) / count));
  }
  return { pts, n: side > 0 ? AXIS : neg(AXIS) };
}

// A solid cylinder along the axis from s0 to s1.
function cylinder(F, s0, s1, r) {
  const wall = sector(F, [[s0, r], [s1, r]], 0, 0, TAU, { step: 12 });
  return [...wall.outer, discFace(F, s0, r, -1, 12), discFace(F, s1, r, 1, 12)];
}

// A box in the local directions of angle psi round the axis:
// s along the axis, r outward at psi, t sideways (a quarter turn on from psi).
function localBox(F, psi, s0, s1, r0, r1, t0, t1) {
  const c = Math.cos(psi);
  const n = Math.sin(psi);
  const at = (s, r, t) => [F.o[0] + s, F.o[1] + r * c - t * n, F.o[2] + r * n + t * c];
  const R = radial(psi);
  const T = tangent(psi);
  return [
    { pts: [at(s0, r1, t0), at(s1, r1, t0), at(s1, r1, t1), at(s0, r1, t1)], n: R },
    { pts: [at(s0, r0, t0), at(s1, r0, t0), at(s1, r0, t1), at(s0, r0, t1)], n: neg(R) },
    { pts: [at(s0, r0, t1), at(s1, r0, t1), at(s1, r1, t1), at(s0, r1, t1)], n: T },
    { pts: [at(s0, r0, t0), at(s1, r0, t0), at(s1, r1, t0), at(s0, r1, t0)], n: neg(T) },
    { pts: [at(s1, r0, t0), at(s1, r1, t0), at(s1, r1, t1), at(s1, r0, t1)], n: AXIS },
    { pts: [at(s0, r0, t0), at(s0, r1, t0), at(s0, r1, t1), at(s0, r0, t1)], n: neg(AXIS) },
  ];
}

// Centre of such a box, for depth sorting.
function localPoint(F, psi, s, r, t) {
  return [F.o[0] + s, F.o[1] + r * Math.cos(psi) - t * Math.sin(psi), F.o[2] + r * Math.sin(psi) + t * Math.cos(psi)];
}

// A box set square to the world axes.
function worldBox(x0, x1, y0, y1, z0, z1) {
  const p = (x, y, z) => [x, y, z];
  return [
    { pts: [p(x0, y0, z1), p(x1, y0, z1), p(x1, y1, z1), p(x0, y1, z1)], n: [0, 0, 1] },
    { pts: [p(x0, y0, z0), p(x1, y0, z0), p(x1, y1, z0), p(x0, y1, z0)], n: [0, 0, -1] },
    { pts: [p(x1, y0, z0), p(x1, y1, z0), p(x1, y1, z1), p(x1, y0, z1)], n: [1, 0, 0] },
    { pts: [p(x0, y0, z0), p(x0, y1, z0), p(x0, y1, z1), p(x0, y0, z1)], n: [-1, 0, 0] },
    { pts: [p(x0, y1, z0), p(x1, y1, z0), p(x1, y1, z1), p(x0, y1, z1)], n: [0, 1, 0] },
    { pts: [p(x0, y0, z0), p(x1, y0, z0), p(x1, y0, z1), p(x0, y0, z1)], n: [0, -1, 0] },
  ];
}

// A line through world points, as an SVG path.
function wirePath(points, P, cls, tone) {
  const d = pathOf(points.map((point) => flat(point, P)), false);
  return '<path class="iso-line ' + cls + '" data-tone="' + tone + '" d="' + d + '"/>';
}

// A small round label that always faces the viewer.
function labelSvg(point, P, text, kind) {
  const [x, y] = flat(point, P);
  return '<g class="hd-label" data-kind="' + kind + '" transform="translate(' + x.toFixed(1) + " " + y.toFixed(1) + ')"><circle r="9"/><text y="4" text-anchor="middle">' + text + "</text></g>";
}

// Sort things that sit round the axis: far ones first.
function byDepthSvg(items, P) {
  const V = viewDir(P);
  const sorted = [...items].sort((a, b) => dot(a.at, V) - dot(b.at, V));
  return sorted.map((item) => item.svg).join("");
}

// Painter's order for parts strung along the x axis.
// zones:  [{ x, svg }]                   things at one place along the axis
// shells: [{ x0, x1, back, front }]      tubes that wrap whatever lies between x0 and x1
// A shell's far inside wall is painted first, then what is inside it, then its near outside wall.
function compose(zones, shells, P) {
  const towards = viewDir(P)[0] >= 0 ? 1 : -1;
  if (shells.length === 0) {
    const sorted = [...zones].sort((a, b) => (a.x - b.x) * towards);
    return sorted.map((zone) => zone.svg).join("");
  }
  const ordered = [...shells].sort((a, b) => b.x1 - b.x0 - (a.x1 - a.x0));
  const big = ordered[0];
  const rest = ordered.slice(1);
  const inside = zones.filter((zone) => zone.x > big.x0 && zone.x < big.x1);
  const outside = zones.filter((zone) => !(zone.x > big.x0 && zone.x < big.x1));
  const insideShells = rest.filter((shell) => shell.x0 >= big.x0 - 1e-6 && shell.x1 <= big.x1 + 1e-6);
  const outsideShells = rest.filter((shell) => !(shell.x0 >= big.x0 - 1e-6 && shell.x1 <= big.x1 + 1e-6));
  const packed = { x: (big.x0 + big.x1) / 2, svg: big.back + compose(inside, insideShells, P) + big.front };
  return compose([...outside, packed], outsideShells, P);
}

// A casing tube as a shell.  alpha is how solid it looks (0 = gone).
function tubeShell(F, profile, t, alpha, options) {
  const x0 = F.o[0] + profile[0][0];
  const x1 = F.o[0] + profile[profile.length - 1][0];
  if (alpha < 0.02) {
    return { x0, x1, back: "", front: "" };
  }
  const tube = sector(F, profile, t, 0, TAU, { step: options.step || 9, ends: options.ends || [false, false] });
  const back = meshSvg(mesh(tube.inner, P_NOW), { tone: "lo", cls: "cav", alpha: Math.min(1, alpha * 1.6) });
  const front = meshSvg(mesh([...tube.outer, ...tube.caps], P_NOW), { tone: "hi", crease: "lo", alpha });
  return { x0, x1, back, front };
}

// The camera in use while a scene is being drawn.
let P_NOW = null;

// ---------------- the motor ----------------
// cfg:   { o: [x, y, z] centre of the rear face, S: size, tint, lit, supply }
// state: { phi, explode (0-1), caseAlpha (0-1), labels }
// Returns { zones, shells, labels } in world x, ready for compose().
function motorParts(cfg, state, P) {
  const S = cfg.S;
  const m = (value) => value * S;
  const e = state.explode;
  const alpha = state.caseAlpha;
  const zones = [];
  const shells = [];
  let labels = "";

  // How far each group has slid along the axis.
  const capOff = m(-14) * e;
  const brushOff = m(-5) * e;
  const canOff = m(34) * e;
  const frontOff = m(44) * e;
  const at = (offset) => ({ o: [cfg.o[0] + offset, cfg.o[1], cfg.o[2]] });
  const F = at(0);
  const solid = (faces, options) => meshSvg(mesh(faces, P), options);

  // Shaft, in pieces so each can be ordered against the caps.
  zones.push({ x: cfg.o[0] + m(-6), svg: solid(cylinder(F, m(-10), m(-2), m(1.5)), { tone: "mid" }) });
  zones.push({ x: cfg.o[0] + m(0.75), svg: solid(cylinder(F, m(-2), m(3.5), m(1.5)), { tone: "mid" }) });
  zones.push({ x: cfg.o[0] + m(31), svg: solid(cylinder(F, m(28.8), m(33), m(1.5)), { tone: "mid" }) });
  zones.push({ x: cfg.o[0] + m(35.2), svg: solid(cylinder(F, m(33), m(37.5), m(1.5)), { tone: "mid" }) });
  const comm = commutatorSvg(cfg, state.phi, P);
  zones.push({ x: cfg.o[0] + m(38.8), svg: solid(cylinder(F, m(37.5), m(40), m(1.5)), { tone: "mid" }) + (viewDir(P)[0] > 0.05 ? comm.mark : "") });

  // Rear cap (plastic, carries the brushes) and front end of the can.
  if (alpha >= 0.02) {
    const FC = at(capOff);
    const rear = solid([...cylinder(FC, m(-2), 0, m(4)), ...cylinder(FC, 0, m(2.5), m(14))], { tone: "mid", alpha });
    shells.push({ x0: FC.o[0] + m(-2), x1: FC.o[0] + m(2.5), back: "", front: rear });
    const FF = at(frontOff);
    const front = solid([...cylinder(FF, m(33), m(35.5), m(14)), ...cylinder(FF, m(35.5), m(37.5), m(4))], { tone: "hi", crease: "lo", alpha });
    shells.push({ x0: FF.o[0] + m(33), x1: FF.o[0] + m(37.5), back: "", front });
  }

  // The steel can.
  const FK = at(canOff);
  shells.push(tubeShell(FK, [[m(2.5), m(14)], [m(33), m(14)]], m(1.2), alpha, { step: 10 }));

  // Supply, terminal tags and leads (large motor only).  They travel with the rear cap.
  if (cfg.supply) {
    const FC = at(capOff);
    const FB = at(brushOff);
    const items = [];
    const box = worldBox(FC.o[0] + m(-22), FC.o[0] + m(-8), cfg.o[1] - m(9), cfg.o[1] + m(9), cfg.o[2] - m(30), cfg.o[2] - m(21));
    items.push({ at: [FC.o[0] + m(-15), cfg.o[1], cfg.o[2] - m(25.5)], svg: solid(box, { tone: "mid" }) });
    [
      { angle: MOTOR.brushPlus, y: -5, sign: "+", tone: "lit" },
      { angle: MOTOR.brushMinus, y: 5, sign: "−", tone: "mid" },
    ].forEach((lead) => {
      const post = worldBox(FC.o[0] + m(-16.2), FC.o[0] + m(-13.8), cfg.o[1] + m(lead.y - 1.2), cfg.o[1] + m(lead.y + 1.2), cfg.o[2] - m(21), cfg.o[2] - m(18.5));
      const postTop = [FC.o[0] + m(-15), cfg.o[1] + m(lead.y), cfg.o[2] - m(18.5)];
      items.push({ at: postTop, svg: solid(post, { tone: "hi", crease: "lo" }) });
      // Lead: from the brush arm, back through the cap, then down to the supply post.
      const a = pt(FB, m(2.5), m(7.6), lead.angle);
      const b = pt(FC, m(-15), m(7.6), lead.angle);
      items.push({ at: [(a[0] + b[0]) / 2, (b[1] + postTop[1]) / 2, (b[2] + postTop[2]) / 2], svg: wirePath([a, b, postTop], P, "hd-lead", lead.tone) });
      if (state.labels) {
        labels += labelSvg([postTop[0], cfg.o[1] + m(lead.y * 2.7), postTop[2] - m(1)], P, lead.sign, lead.sign === "+" ? "plus" : "minus");
      }
    });
    zones.push({ x: FC.o[0] + m(-15), svg: byDepthSvg(items, P) });
  }

  // Commutator and the two brushes.
  {
    const FB = at(brushOff);
    const items = [];
    items.push({ at: pt(F, m(6), 0, 0), svg: solid(cylinder(F, m(3.5), m(8.5), m(4.2)), { tone: "hi", crease: "lo" }) + comm.gaps + solid(cylinder(F, m(8.5), m(11.2), m(1.5)), { tone: "mid" }) });
    [MOTOR.brushPlus, MOTOR.brushMinus].forEach((angle) => {
      const arm = solid(radialBox(FB, m(2.5), m(6.2), m(7.2), m(8), m(1), angle), { tone: "mid" });
      const carbon = solid(radialBox(FB, m(4.6), m(7.4), m(4.2), m(7.2), m(1.3), angle), { tone: "hi", crease: "lo" });
      items.push({ at: pt(FB, m(6), m(6), angle), svg: arm + carbon });
    });
    zones.push({ x: cfg.o[0] + m(6), svg: byDepthSvg(items, P) });
  }

  // Magnets and armature.
  {
    const items = [];
    items.push({ at: pt(F, m(20), 0, 0), svg: rotorSvg(cfg, state.phi, P) });
    [
      { centre: MOTOR.north, pole: "n", text: "N" },
      { centre: MOTOR.south, pole: "s", text: "S" },
    ].forEach((magnet) => {
      const faces = sector(F, [[m(11), m(12.8)], [m(30), m(12.8)]], m(1.8), magnet.centre - 34 * DEG, magnet.centre + 34 * DEG, { ends: [true, true] }).all;
      items.push({ at: pt(F, m(20), m(12), magnet.centre), svg: solid(faces, { tone: "mid", crease: "lo", tint: { pole: magnet.pole, alpha: 0.5 } }) });
      if (state.labels) {
        labels += labelSvg(pt(F, m(20.5), m(19), magnet.centre), P, magnet.text, magnet.pole);
      }
    });
    zones.push({ x: cfg.o[0] + m(20), svg: byDepthSvg(items, P) });
  }

  return { zones, shells, labels };
}

// ---------------- the whole dryer ----------------
const DRYER = {
  axis: [0, 0, 110],
  profile: [[-66, 36], [28, 36], [86, 25]],
  motor: { o: [-36, 0, 110], S: 1, lit: true, tint: false, supply: false },
  fan: { o: [0, 0, 110], s: -52, r0: 7.4, r1: 31.5, blades: 9 },
};

// A coil of wire round the axis, split into the part behind the axis and the part in front.
function helixPaths(F, x0, x1, r, turns, start, P) {
  const V = viewDir(P);
  const count = Math.round(turns * 28);
  let back = "";
  let front = "";
  let run = [];
  let near = null;
  for (let index = 0; index <= count; index += 1) {
    const share = index / count;
    const angle = start + share * turns * TAU;
    const screen = flat(pt(F, x0 + (x1 - x0) * share, r, angle), P);
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

// state: { phi, caseAlpha, knob (0-2), labels }
function dryerSvg(state, P) {
  P_NOW = P;
  const V = viewDir(P);
  const F = { o: DRYER.axis };
  const Z = DRYER.axis[2];
  const alpha = state.caseAlpha;
  const solid = (faces, options) => meshSvg(mesh(faces, P), options);
  const zones = [];
  const shells = [];

  // Handle and switch.  The viewer is always above, so the handle is painted first.
  const handle = solid(worldBox(-27, 3, -11, 11, Z - 118, Z - 34), { tone: "hi", crease: "lo" });
  const knobZ = Z - 78 + state.knob * 9;
  const slot = wirePath([[3.05, -3.6, Z - 80], [3.05, 3.6, Z - 80], [3.05, 3.6, Z - 50], [3.05, -3.6, Z - 50], [3.05, -3.6, Z - 80]], P, "", "mid");
  const knob = solid(worldBox(3, 5.4, -2.8, 2.8, knobZ, knobZ + 8), { tone: "hi", crease: "lo" });
  let out = V[0] > 0 ? handle + slot + knob : knob + handle;

  // Casing: rear cap, body tube, nozzle.
  if (alpha >= 0.02) {
    const rear = [...sector(F, [[-84, 31], [-80, 36], [-66, 36]], 0, 0, TAU, { step: 9 }).outer, discFace(F, -84, 31, -1, 9), discFace(F, -66, 36, 1, 9)];
    zones.push({ x: -75, svg: solid(rear, { tone: "hi", crease: "lo", alpha }) });
  }
  shells.push(tubeShell(F, DRYER.profile, 2, alpha, { step: 9 }));
  shells.push(tubeShell(F, [[86, 25], [108, 23.5]], 2, alpha, { step: 9, ends: [false, true] }));

  // Fan.
  const fan = fanSvg(DRYER.fan, state.phi, P);
  zones.push({ x: -52, svg: fan.back + solid(cylinder(F, -58, -46, 8), { tone: "hi", crease: "lo" }) + fan.front });

  // Motor on three struts.
  const motorState = { phi: state.phi, explode: 0, caseAlpha: 0.3, labels: false };
  const motor = motorParts(DRYER.motor, motorState, P);
  const struts = [130, 215, 300].map((degrees) => {
    const angle = degrees * DEG;
    return { at: pt(F, -18, 24, angle), svg: solid(radialBox(F, -19.2, -16.8, 14, 34, 1.2, angle), { tone: "mid" }) };
  });
  const farStruts = struts.filter((strut) => dot(strut.at, V) - dot(pt(F, -18, 0, 0), V) < 0);
  const nearStruts = struts.filter((strut) => dot(strut.at, V) - dot(pt(F, -18, 0, 0), V) >= 0);
  zones.push({ x: -18, svg: byDepthSvg(farStruts, P) + compose(motor.zones, motor.shells, P) + byDepthSvg(nearStruts, P) });

  // Heater: two coils on a cross of mica boards, with the safety parts on one board.
  {
    const outer = helixPaths(F, 12, 70, 19, 6.5, 45 * DEG, P);
    const inner = helixPaths(F, 12, 70, 9, 9.5, 225 * DEG, P);
    const heat = (d, level) => (d ? '<path class="iso-line hd-heat" data-level="' + level + '" d="' + d + '"/>' : "");
    const items = [];
    [45, 135, 225, 315].forEach((degrees) => {
      const angle = degrees * DEG;
      items.push({ at: pt(F, 41, 11, angle), svg: solid(radialBox(F, 8, 74, 0.5, 22, 0.5, angle), { tone: "mid" }) });
    });
    // Parts on the board faces that look towards +y and up: four diodes, a thermal fuse and a thermostat.
    const up = 135 * DEG;
    const down = 315 * DEG;
    [16, 20, 24, 28].forEach((s) => {
      items.push({ at: localPoint(F, up, s, 11, -2), svg: solid(localBox(F, up, s - 1, s + 1, 10.6, 15.4, -2.5, -0.5), { tone: "hi", crease: "lo" }) });
    });
    items.push({ at: localPoint(F, down, 42, 11, 2), svg: solid(localBox(F, down, 37, 47, 11.8, 14.2, 0.5, 2.9), { tone: "hi", crease: "lo" }) });
    items.push({ at: localPoint(F, down, 58, 11, 2), svg: solid(localBox(F, down, 55, 61, 10, 16, 0.5, 3.1), { tone: "hi", crease: "lo" }) });
    zones.push({ x: 41, svg: heat(outer.back, 1) + heat(inner.back, 2) + byDepthSvg(items, P) + heat(inner.front, 2) + heat(outer.front, 1) });
  }

  // Ring that holds the front of the heater.
  zones.push({ x: 75, svg: solid(sector(F, [[74, 25], [76, 25]], 5, 0, TAU, { step: 9, ends: [true, true] }).all, { tone: "mid" }) });

  out += compose(zones, shells, P);
  return out;
}

// The motor on its own, with supply, labels and the strip-down animation.
function motorSvg(cfg, state, P) {
  P_NOW = P;
  const parts = motorParts(cfg, state, P);
  return compose(parts.zones, parts.shells, P) + parts.labels;
}
