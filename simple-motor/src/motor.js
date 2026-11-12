
// ---------------------------------------------------------------
// The simple (school) DC motor: one coil, a split-ring commutator,
// two brushes and two flat magnets.  geom.mjs is inlined above this.
// Everything is redrawn from geometry each frame, so the camera can go anywhere.
// ---------------------------------------------------------------

const TURN = Math.PI * 2;
const calm = matchMedia("(prefers-reduced-motion: reduce)");

// ---------------- sizes (drawing units) ----------------
const COIL = { half: 40, x0: -40, x1: 40, wire: 1.6 }; // half-width of the coil, and where it starts and ends along the axle
const RING = { x0: 50, x1: 66, r: 8, thick: 3, halfAngle: 80 * DEG }; // split-ring commutator
const MAGNET = { x0: -36, x1: 36, near: 52, far: 78, z0: -22, z1: 22 }; // each magnet block
const BASE_Z = -56; // top of the baseboard

// ---------------- small helpers ----------------

// A camera that keeps one world point in the middle of the picture.
function cameraFor(view) {
  const P = { origin: [0, 0], scale: view.scale, azimuth: view.azimuth, elevation: view.elevation };
  const middle = flat(view.centre, P);
  P.origin = [view.width / 2 - middle[0], view.height / 2 - middle[1]];
  return P;
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

// A flat round face at position s along the axle.
function discFace(F, s, r, side) {
  const pts = [];
  for (let index = 0; index < 30; index += 1) {
    pts.push(pt(F, s, r, (TAU * index) / 30));
  }
  return { pts, n: side > 0 ? AXIS : neg(AXIS) };
}

// A solid cylinder along the axle from s0 to s1.
function cylinder(F, s0, s1, r) {
  const wall = sector(F, [[s0, r], [s1, r]], 0, 0, TAU, { step: 12 });
  return [...wall.outer, discFace(F, s0, r, -1), discFace(F, s1, r, 1)];
}

// A line through world points.
function linePath(points, P, cls, tone) {
  const d = pathOf(points.map((point) => flat(point, P)), false);
  return '<path class="iso-line ' + cls + '" data-tone="' + tone + '" d="' + d + '"/>';
}

// An arrowhead at a world point, pointing along a world direction.
function arrowHead(point, direction, P, cls) {
  const from = flat(point, P);
  const to = flat([point[0] + direction[0], point[1] + direction[1], point[2] + direction[2]], P);
  const turn = (Math.atan2(to[1] - from[1], to[0] - from[0]) * 180) / Math.PI;
  return '<path class="' + cls + '" transform="translate(' + from[0].toFixed(1) + " " + from[1].toFixed(1) + ") rotate(" + turn.toFixed(1) + ')" d="M6 0L-4 -5L-4 5Z"/>';
}

// A small round label that always faces the viewer.
function labelSvg(point, P, text, kind) {
  const at = flat(point, P);
  return '<g class="hd-label" data-kind="' + kind + '" transform="translate(' + at[0].toFixed(1) + " " + at[1].toFixed(1) + ')"><circle r="10"/><text y="4" text-anchor="middle">' + text + "</text></g>";
}

// ---------------- the physics ----------------
// phi is the angle of side A of the coil: 0 when it points towards +y (the right-hand magnet
// when seen from the commutator end), 90 degrees when it points straight up.
// battery: +1 or -1 (which way round the cell is).  magnets: +1 (field from left to right) or -1.

// Current in side A, along the axle towards the commutator (+x) when positive.
// Each brush touches whichever half-ring is on its side, so the current in a side
// depends only on which side of the axle it is on at that moment.
function currentInSideA(phi, battery) {
  if (Math.cos(phi) >= 0) {
    return battery;
  }
  return -battery;
}

// Is the coil getting any current?  Each half-ring covers 160 degrees, so for 10 degrees either side
// of upright each brush is over a gap in the ring: the circuit is broken and no current flows.
// Returns 0 in the gap and 1 with full contact, with a short ramp at the edges so arrows fade in and out.
const GAP_EDGE = Math.cos(RING.halfAngle);
function brushContact(phi) {
  const across = Math.abs(Math.cos(phi));
  const share = (across - GAP_EDGE) / 0.06;
  return Math.min(1, Math.max(0, share));
}

// Turning effect as a share of its largest value.  Positive is anticlockwise seen from the commutator end.
// Force on each long side is B I L, straight up or down; its lever arm is the side's distance across from the axle.
// With no current (brushes over the gaps) there is no force at all.
function turningEffect(phi, battery, magnets) {
  if (brushContact(phi) === 0) {
    return 0;
  }
  return battery * magnets * Math.abs(Math.cos(phi));
}

// What the coil is doing, for either design.
// state.design is "split" (DC motor with a split-ring commutator) or "slip" (AC generator with slip rings).
// Returns { sign, live, value }:
//   sign  - direction of the current in side A (+1 is towards the ring end of the axle)
//   live  - 0 to 1, used to fade arrows out when there is no current
//   value - the current in side A as a share of its largest size, with its sign
function coilState(state) {
  if (state.design === "slip") {
    // Generator: the coil is turned by hand.  Side A moves at right angles to the axle,
    // and the current induced in it is largest when it cuts straight across the field (coil flat)
    // and zero when it moves along the field (coil upright).  It reverses every half turn.
    const value = -state.magnets * state.turnWay * Math.cos(state.phi);
    const size = Math.abs(value);
    return { sign: value >= 0 ? 1 : -1, live: Math.min(1, size / 0.12), value };
  }
  const live = brushContact(state.phi);
  const sign = currentInSideA(state.phi, state.battery);
  return { sign, live, value: live > 0 ? sign : 0 };
}

// Where each brush sits along the axle.  Split ring: both brushes on the one ring.
// Slip rings: one brush on each ring.
function brushSpan(state, side) {
  if (state.design === "slip") {
    return side < 0 ? [51, 56] : [60, 65];
  }
  return [55, 61];
}

// ---------------- the 3D scene ----------------

function motorScene(state, P) {
  const V = viewDir(P);
  const F = { o: [0, 0, 0] };
  const solid = (faces, options) => meshSvg(mesh(faces, P), options);
  const phi = state.phi;
  const coil = coilState(state);
  const sideA = coil.sign;
  const slip = state.design === "slip";
  const items = [];
  // Depth for sorting: mostly how far towards the viewer across the floor, with a little for height.
  const depth = (point) => point[0] * V[0] + point[1] * V[1] + 0.15 * point[2] * V[2];
  const add = (at, svg) => {
    items.push({ depth: depth(at), svg });
  };

  // Which magnet is north.  With magnets = +1 the field runs from -y to +y.
  const northSide = state.magnets > 0 ? -1 : 1;

  // --- baseboard, with the leads from the brush posts to the cell lying on it ---
  let out = solid(worldBox(-72, 98, -88, 88, BASE_Z - 6, BASE_Z), { tone: "mid" });
  const plusSide = state.battery > 0 ? -1 : 1; // the positive brush is on the -y side when battery = +1
  [-1, 1].forEach((side) => {
    let tone = side === plusSide ? "lit" : "mid";
    if (slip) {
      tone = "hi";
    }
    const span = brushSpan(state, side);
    const postX = (span[0] + span[1]) / 2;
    const route = [
      [postX, side * 32, BASE_Z + 0.2],
      [88, side * 32, BASE_Z + 0.2],
      [88, side * 15, BASE_Z + 0.2],
    ];
    out += linePath(route, P, "hd-lead", tone);
    // An arrowhead on the lead, pointing the way conventional current flows in it.
    if (state.showCurrent && coil.live > 0) {
      // Motor: from the + terminal to its brush, and from the other brush back to the - terminal.
      let towardsBrush = side === plusSide;
      if (slip) {
        // Generator: current leaves the coil through the ring joined to whichever side carries it towards the rings.
        // The -y brush is on side A's ring.
        const leavesHere = side < 0 ? sideA > 0 : sideA < 0;
        towardsBrush = !leavesHere;
      }
      const head = arrowHead([(postX + 88) / 2, side * 32, BASE_Z + 0.2], [towardsBrush ? -1 : 1, 0, 0], P, "sm-currenthead");
      out += '<g opacity="' + coil.live.toFixed(2) + '">' + head + "</g>";
    }
  });

  // --- magnets on their stands ---
  [-1, 1].forEach((side) => {
    const y0 = side < 0 ? -MAGNET.far : MAGNET.near;
    const y1 = side < 0 ? -MAGNET.near : MAGNET.far;
    const stand = solid(worldBox(MAGNET.x0 + 6, MAGNET.x1 - 6, y0 + 3, y1 - 3, BASE_Z, MAGNET.z0), { tone: "mid" });
    const pole = side === northSide ? "n" : "s";
    const block = solid(worldBox(MAGNET.x0, MAGNET.x1, y0, y1, MAGNET.z0, MAGNET.z1), { tone: "hi", crease: "lo", tint: { pole, alpha: 0.5 } });
    add([0, (y0 + y1) / 2, -10], stand + block);
  });

  // --- field lines from the north face to the south face ---
  if (state.showField) {
    let field = "";
    [-24, 0, 24].forEach((x) => {
      field += linePath([[x, -MAGNET.near, 0], [x, MAGNET.near, 0]], P, "sm-field", "mid");
      field += arrowHead([x, -22 * state.magnets, 0], [0, state.magnets, 0], P, "sm-fieldhead");
    });
    add([0, 0, -6], field);
  }

  // --- two posts that carry the axle ---
  [-60, 72].forEach((x) => {
    add([x, 0, -20], solid(worldBox(x - 3, x + 3, -6, 6, BASE_Z, 5), { tone: "mid" }));
  });

  // --- axle, in lengths so each can be ordered against the coil and the commutator ---
  [
    [-66, -41.5],
    [-38.5, 38.5],
    [41.5, RING.x0],
    [RING.x1, 78],
  ].forEach((span) => {
    add([(span[0] + span[1]) / 2, 0, 0], solid(cylinder(F, span[0], span[1], 2.4), { tone: "mid" }));
  });

  // --- the coil: side A (tinted), side B, the far end and the two near-end pieces ---
  const w = COIL.wire;
  [0, 1].forEach((index) => {
    const psi = phi + index * Math.PI;
    const tint = index === 0 ? { pole: "a", alpha: 0.75 } : null;
    const long = solid(radialBox(F, COIL.x0, COIL.x1, COIL.half - w, COIL.half + w, w, psi), { tone: "hi", crease: "lo", tint });
    add(pt(F, 0, COIL.half, psi), long);
    const nearEnd = solid(radialBox(F, COIL.x1 - w, COIL.x1 + w, RING.r - 1, COIL.half + w, w, psi), { tone: "hi", crease: "lo", tint });
    add(pt(F, COIL.x1, COIL.half / 2 + 4, psi), nearEnd);
    const ringTint = { pole: index === 0 ? "a" : "cu", alpha: 0.75 };
    if (slip) {
      // Slip rings: two complete rings side by side.  Side A joins the first, side B the second,
      // so side B's lead has to pass through the middle of the first ring to reach its own.
      const ringSpan = index === 0 ? [50, 57] : [59, 66];
      const leadEnd = index === 0 ? 50 : 59;
      const leadR = index === 0 ? [RING.r - 2.6, RING.r] : [2.4, 5];
      add(pt(F, 45, leadR[1], psi), solid(radialBox(F, COIL.x1, leadEnd, leadR[0], leadR[1], w, psi), { tone: "hi", crease: "lo", tint }));
      const ring = sector(F, [[ringSpan[0], RING.r], [ringSpan[1], RING.r]], RING.thick, 0, TAU, { ends: [true, true], step: 10 }).all;
      add(pt(F, (ringSpan[0] + ringSpan[1]) / 2, 0, 0), solid(ring, { tone: "hi", crease: "lo", tint: ringTint }));
    } else {
      const lead = solid(radialBox(F, COIL.x1, RING.x0, RING.r - 2.6, RING.r, w, psi), { tone: "hi", crease: "lo", tint });
      add(pt(F, 45, RING.r, psi), lead);
      // Each half of the split ring is joined to one side of the coil and turns with it.
      const half = sector(F, [[RING.x0, RING.r], [RING.x1, RING.r]], RING.thick, psi - RING.halfAngle, psi + RING.halfAngle, { ends: [true, true], step: 10 }).all;
      add(pt(F, 58, RING.r - 1.5, psi), solid(half, { tone: "hi", crease: "lo", tint: ringTint }));
    }
  });
  add(pt(F, COIL.x0, 0, 0), solid(radialBox(F, COIL.x0 - w, COIL.x0 + w, -COIL.half - w, COIL.half + w, w, phi), { tone: "hi", crease: "lo" }));

  // --- brushes: a carbon block each side of the split ring, on an arm from a post ---
  [-1, 1].forEach((side) => {
    const y0 = side < 0 ? -32 : RING.r;
    const y1 = side < 0 ? -RING.r : 32;
    const span = brushSpan(state, side);
    const postX = (span[0] + span[1]) / 2;
    add([postX, side * 18, 0], solid(worldBox(span[0], span[1], y0, y1, -2.5, 2.5), { tone: "hi", crease: "lo" }));
    add([postX, side * 32, -28], solid(worldBox(postX - 2.5, postX + 2.5, side * 32 - 2.5, side * 32 + 2.5, BASE_Z, 2.5), { tone: "mid" }));
  });

  // --- the cell, with a terminal each side ---
  {
    let cell = solid(worldBox(82, 94, -12, 12, BASE_Z, BASE_Z + 12), { tone: "hi", crease: "lo" });
    [-1, 1].forEach((side) => {
      cell += solid(worldBox(86, 90, Math.min(side * 12, side * 15), Math.max(side * 12, side * 15), BASE_Z + 4, BASE_Z + 8), { tone: "mid" });
    });
    // The + and - labels belong to the cell, so anything in front of the cell hides them too.
    if (state.labels && !slip) {
      cell += labelSvg([88, plusSide * 25, BASE_Z + 14], P, "+", "plus");
      cell += labelSvg([88, -plusSide * 25, BASE_Z + 14], P, "−", "minus");
    }
    if (slip) {
      // In the generator the box is a centre-zero meter: its needle swings one way, then the other.
      const top = BASE_Z + 12.2;
      const swing = coil.value * 0.95;
      const tip = [88 - 9 * Math.cos(swing), 9 * Math.sin(swing), top];
      cell += linePath([[84, -8, top], [80, 0, top], [84, 8, top]], P, "", "lo");
      cell += linePath([[92, 0, top], tip], P, "sm-needle", "lit");
    }
    add([88, 0, BASE_Z + 6], cell);
  }

  items.sort((a, b) => a.depth - b.depth);
  out += items.map((item) => item.svg).join("");

  // --- overlays: current arrows, force arrows and labels ---
  // Arrows fade out as the brushes reach the gaps in the ring, and back in on the other side.
  const live = coil.live;
  if (live > 0) {
    out += '<g opacity="' + live.toFixed(2) + '">';
  }
  if (state.showCurrent && live > 0) {
    // Side A, side B and the far end, each with an arrowhead pointing the way the current flows.
    const along = sideA > 0 ? [1, 0, 0] : [-1, 0, 0];
    out += arrowHead(pt(F, 0, COIL.half, phi), along, P, "sm-currenthead");
    out += arrowHead(pt(F, 0, COIL.half, phi + Math.PI), neg(along), P, "sm-currenthead");
    // At the far end the current crosses from side B to side A when it flows towards the commutator in A.
    const across = radial(phi);
    const farWay = sideA > 0 ? across : neg(across);
    out += arrowHead(pt(F, COIL.x0, 0.01, phi), farWay, P, "sm-currenthead");
  }
  if (state.showForces && slip) {
    // Generator: show which way each long side is moving (for Fleming's right-hand rule).
    [0, 1].forEach((index) => {
      const psi = phi + index * Math.PI;
      const way = tangent(psi);
      const start = pt(F, 0, COIL.half, psi);
      const end = [start[0], start[1] + way[1] * state.turnWay * 28, start[2] + way[2] * state.turnWay * 28];
      out += linePath([start, end], P, "sm-motion", "hi");
      out += arrowHead(end, [0, way[1] * state.turnWay, way[2] * state.turnWay], P, "sm-motionhead");
    });
  }
  if (state.showForces && live > 0 && !slip) {
    [0, 1].forEach((index) => {
      const psi = phi + index * Math.PI;
      const current = index === 0 ? sideA : -sideA;
      // F = I (along x) x B (along y) = straight up for a positive current in a left-to-right field.
      const up = current * state.magnets;
      const start = pt(F, 0, COIL.half, psi);
      const end = [start[0], start[1], start[2] + up * 30];
      out += linePath([start, end], P, "sm-force", "hi");
      out += arrowHead(end, [0, 0, up], P, "sm-forcehead");
    });
  }
  if (live > 0) {
    out += "</g>";
  }
  if (state.labels) {
    const northY = northSide * (MAGNET.near + MAGNET.far) / 2;
    out += labelSvg([0, northY, MAGNET.z1 + 12], P, "N", "n");
    out += labelSvg([0, -northY, MAGNET.z1 + 12], P, "S", "s");
  }
  return out;
}

// ---------------- the end-on diagram and the turning-effect graph ----------------

function endOnSvg(state) {
  const cx = 230;
  const cy = 170;
  const phi = state.phi;
  const coil = coilState(state);
  const sideA = coil.sign;
  const slip = state.design === "slip";
  const xy = (p) => p[0].toFixed(1) + " " + p[1].toFixed(1);
  // Seen from the commutator end: +y is to the right and up is up.
  const pol = (r, angle) => [cx + r * Math.cos(angle), cy - r * Math.sin(angle)];
  const text = (p, value, cls) => '<text class="hd-wtext ' + cls + '" x="' + p[0].toFixed(1) + '" y="' + (p[1] + 5).toFixed(1) + '" text-anchor="middle">' + value + "</text>";
  let out = "";

  // Magnets: north on the left when magnets = +1.
  [-1, 1].forEach((side) => {
    const isNorth = (side < 0) === (state.magnets > 0);
    const x = side < 0 ? cx - 200 : cx + 150;
    out += '<rect class="sm-magnet" x="' + x + '" y="' + (cy - 60) + '" width="50" height="120"/>';
    out += '<rect class="hd-tint" data-pole="' + (isNorth ? "n" : "s") + '" style="opacity:.5" x="' + x + '" y="' + (cy - 60) + '" width="50" height="120"/>';
    out += text([x + 25, cy], isNorth ? "N" : "S", "hd-wname " + (isNorth ? "hd-wn" : "hd-ws"));
  });

  // Field lines from north to south.
  [-40, -20, 0, 20, 40].forEach((offset) => {
    const y = cy + offset;
    out += '<path class="hd-wflux" d="M' + (cx - 150) + " " + y + "L" + (cx + 150) + " " + y + '"/>';
    const headX = cx - 120 * state.magnets;
    const turn = state.magnets > 0 ? 0 : 180;
    out += '<path class="hd-wfluxhead" transform="translate(' + headX + " " + y + ") rotate(" + turn + ')" d="M5 0L-4 -4L-4 4Z"/>';
  });

  // The coil, seen edge-on: a line through the axle with a long side at each end.
  out += '<path class="sm-coilline" d="M' + xy(pol(110, phi)) + "L" + xy(pol(110, phi + Math.PI)) + '"/>';

  if (slip) {
    // Slip rings: two complete rings.  They are really the same size, one behind the other;
    // the far one (yellow, joined to the yellow side) is drawn larger so both can be seen.
    out += '<circle class="sm-ring" data-half="a" cx="' + cx + '" cy="' + cy + '" r="30"/>';
    out += '<circle class="sm-ring" data-half="b" cx="' + cx + '" cy="' + cy + '" r="19"/>';
    out += '<circle class="hd-wshaft" cx="' + cx + '" cy="' + cy + '" r="7"/>';
    // One brush on each ring.
    out += '<rect class="hd-wbrush" x="' + (cx - 56) + '" y="' + (cy - 8) + '" width="22" height="16"/>';
    out += '<rect class="hd-wbrush" x="' + (cx + 23) + '" y="' + (cy - 8) + '" width="33" height="16"/>';
  } else {
    // Split ring: half A is joined to side A.
    [0, 1].forEach((index) => {
      const centre = phi + index * Math.PI;
      let d = "";
      for (let step = 0; step <= 16; step += 1) {
        const angle = centre - RING.halfAngle + (2 * RING.halfAngle * step) / 16;
        d += (step ? "L" : "M") + xy(pol(24, angle));
      }
      out += '<path class="sm-ring" data-half="' + (index === 0 ? "a" : "b") + '" d="' + d + '"/>';
    });
    out += '<circle class="hd-wshaft" cx="' + cx + '" cy="' + cy + '" r="7"/>';

    // Brushes, fixed either side of the ring.  The positive one is on the left when battery = +1.
    [-1, 1].forEach((side) => {
      const positive = (side < 0) === (state.battery > 0);
      const x = side < 0 ? cx - 50 : cx + 30;
      out += '<rect class="hd-wbrush" x="' + x + '" y="' + (cy - 9) + '" width="20" height="18"/>';
      out += text([x + 10, cy], positive ? "+" : "−", "hd-wsign");
    });
  }

  // The two long sides, end-on, with their currents and the force on each.
  [0, 1].forEach((index) => {
    const psi = phi + index * Math.PI;
    const current = index === 0 ? sideA : -sideA;
    const at = pol(110, psi);
    out += '<circle class="hd-wside" data-side="' + (index === 0 ? "a" : "b") + '" cx="' + at[0].toFixed(1) + '" cy="' + at[1].toFixed(1) + '" r="10"/>';
    if (slip) {
      // Generator: an arrow showing which way this side is moving.
      const way = tangent(psi);
      const fromX = at[0] + way[1] * state.turnWay * 13;
      const fromY = at[1] - way[2] * state.turnWay * 13;
      const toX = at[0] + way[1] * state.turnWay * 44;
      const toY = at[1] - way[2] * state.turnWay * 44;
      const turn = (Math.atan2(toY - fromY, toX - fromX) * 180) / Math.PI;
      out += '<path class="sm-motionline" d="M' + fromX.toFixed(1) + " " + fromY.toFixed(1) + "L" + toX.toFixed(1) + " " + toY.toFixed(1) + '"/>';
      out += '<path class="sm-motionhead" transform="translate(' + toX.toFixed(1) + " " + toY.toFixed(1) + ") rotate(" + turn.toFixed(1) + ')" d="M6 0L-4 -5L-4 5Z"/>';
    }
    // No dot, cross or force arrow when there is no current.
    const live = coil.live;
    if (live === 0) {
      return;
    }
    out += '<g opacity="' + live.toFixed(2) + '">';
    if (current > 0) {
      // Towards the commutator end, which is towards the viewer: out of the page.
      out += '<circle class="hd-wdot" cx="' + at[0].toFixed(1) + '" cy="' + at[1].toFixed(1) + '" r="3"/>';
    } else {
      out += '<path class="hd-wcross" d="M' + (at[0] - 5.5).toFixed(1) + " " + (at[1] - 5.5).toFixed(1) + 'l11 11m0 -11l-11 11"/>';
    }
    if (!slip) {
      const up = current * state.magnets;
      const startY = at[1] - up * 14;
      const endY = at[1] - up * 52;
      out += '<path class="hd-wforce" d="M' + at[0].toFixed(1) + " " + startY.toFixed(1) + "L" + at[0].toFixed(1) + " " + endY.toFixed(1) + '"/>';
      out += '<path class="hd-wforcehead" transform="translate(' + at[0].toFixed(1) + " " + endY.toFixed(1) + ") rotate(" + (up > 0 ? -90 : 90) + ')" d="M6 0L-4 -5L-4 5Z"/>';
    }
    out += "</g>";
  });

  // --- graph over one turn: turning effect (motor) or current through the meter (generator) ---
  const gx = 40;
  const gy = 425;
  const gw = 380;
  const gh = 70;
  // The generator's current goes both ways, so its zero line is half way up.
  const valueAt = (angle) => {
    if (slip) {
      // Which direction the meter calls positive is a free choice; this one starts the graph at a peak.
      return -coilState({ design: "slip", phi: angle, magnets: state.magnets, turnWay: state.turnWay }).value;
    }
    return Math.abs(turningEffect(angle, 1, 1));
  };
  const yOf = (value) => {
    if (slip) {
      return gy - gh / 2 - (gh / 2) * value;
    }
    return gy - gh * value;
  };
  out += '<path class="sm-axis" d="M' + gx + " " + (gy - gh) + "L" + gx + " " + gy + "M" + gx + " " + yOf(0) + "L" + (gx + gw) + " " + yOf(0) + '"/>';
  let curve = "";
  for (let degrees = 0; degrees <= 360; degrees += 1) {
    curve += (degrees ? "L" : "M") + (gx + (gw * degrees) / 360).toFixed(1) + " " + yOf(valueAt(degrees * DEG)).toFixed(1);
  }
  out += '<path class="sm-curve" d="' + curve + '"/>';
  [0, 90, 180, 270, 360].forEach((degrees) => {
    const x = gx + (gw * degrees) / 360;
    out += '<path class="sm-axis" d="M' + x + " " + gy + "L" + x + " " + (gy + 4) + '"/>';
    out += '<text class="sm-tick" x="' + x + '" y="' + (gy + 17) + '" text-anchor="middle">' + degrees + "°</text>";
  });
  out += '<text class="sm-tick" x="' + gx + '" y="' + (gy - gh - 8) + '">' + (slip ? "current through the meter" : "turning effect") + "</text>";
  const turns = (((phi % TURN) + TURN) % TURN) / TURN;
  const markX = gx + gw * turns;
  const markY = yOf(valueAt(phi));
  out += '<path class="sm-markline" d="M' + markX.toFixed(1) + " " + yOf(0) + "L" + markX.toFixed(1) + " " + markY.toFixed(1) + '"/>';
  out += '<circle class="sm-mark" cx="' + markX.toFixed(1) + '" cy="' + markY.toFixed(1) + '" r="4.5"/>';
  return out;
}

// ---------------- the split ring, close up, for the step-through ----------------

// One half turn, stage by stage.  Angles are for side A (yellow), with the cell and magnets the normal way round.
const STAGES_SPLIT = [
  {
    angle: 0,
    title: "Coil flat: full turning effect",
    body: "The copper half of the ring touches the + brush and the yellow half touches the − brush. Current goes in through the copper half, round the coil, and out through the yellow half. The yellow side is pushed up and the other side is pushed down.",
  },
  {
    angle: 45,
    title: "Turning: same contacts",
    body: "Each half of the ring is still on the same brush, so the current and both forces are unchanged. The forces now act closer to the line of the axle, so the turning effect is smaller.",
  },
  {
    angle: 76,
    title: "The gaps reach the brushes",
    body: "The ring has turned with the coil. Each half is about to slide off its brush. The turning effect is small, but it is still in the same direction.",
  },
  {
    angle: 90,
    title: "Coil upright: the dead zone",
    body: "Each brush is over a gap in the ring. The circuit is broken, so there is no current and no force. The coil keeps going only because it is already moving.",
  },
  {
    angle: 104,
    title: "The halves have swapped brushes",
    body: "The yellow half now touches the + brush and the copper half touches the − brush. Current flows round the coil the opposite way to before. That is the whole job of the split ring.",
  },
  {
    angle: 135,
    title: "Reversed current, same turning",
    body: "The yellow side is now on the left. Because its current has reversed, it is pushed down. The side on the right is pushed up, exactly as before, so the coil keeps turning the same way.",
  },
  {
    angle: 180,
    title: "Half a turn done",
    body: "The coil is flat again with its two sides swapped over. The next half turn repeats the same stages, and the ring swaps the connections back. Without the split ring the forces would have reversed at upright and turned the coil back.",
  },
];

// One full turn of the generator, stage by stage.  Turning anticlockwise, magnets the normal way round.
const STAGES_SLIP = [
  {
    angle: 0,
    title: "Coil flat: largest current",
    body: "The yellow side is moving straight up through the field and the other side straight down, so they cut across the field as fast as they can. The induced current is at its largest. It leaves through the copper ring, goes through the meter, and comes back through the yellow ring.",
  },
  {
    angle: 45,
    title: "Turning: current falling",
    body: "The sides are now moving partly along the field, so they cut across it more slowly and the current is smaller. Its direction has not changed. Each ring is on the same brush as before, and always will be.",
  },
  {
    angle: 90,
    title: "Coil upright: no current",
    body: "For a moment both sides are moving along the field lines and not cutting them, so nothing is induced. Nothing has been disconnected: each ring is still touching its own brush.",
  },
  {
    angle: 135,
    title: "Current reversed",
    body: "The yellow side is now moving down through the field, so the current in it has reversed. The yellow ring is still on the same brush, so the current through the meter has reversed too. A split ring would have swapped brushes here and kept the meter current the same way.",
  },
  {
    angle: 180,
    title: "Flat again: largest current, the other way",
    body: "Half a turn done. The sides have swapped places and the current is at its largest again, in the opposite direction to stage 1.",
  },
  {
    angle: 270,
    title: "Upright again: no current",
    body: "The sides are moving along the field once more, and the current passes through zero on its way back.",
  },
  {
    angle: 360,
    title: "One turn, one cycle",
    body: "Back at the start. One full turn of the coil gives one full cycle of alternating current: one way, zero, the other way, zero. Slip rings pass on whatever the coil produces. A split ring swaps the connections every half turn.",
  },
];

function stagesFor(state) {
  if (state.design === "slip") {
    return STAGES_SLIP;
  }
  return STAGES_SPLIT;
}

function ringSvg(state) {
  const cx = 230;
  const cy = 200;
  const phi = state.phi;
  const coil = coilState(state);
  const sideA = coil.sign;
  const live = coil.live;
  const slip = state.design === "slip";
  const xy = (p) => p[0].toFixed(1) + " " + p[1].toFixed(1);
  const pol = (r, angle) => [cx + r * Math.cos(angle), cy - r * Math.sin(angle)];
  const text = (p, value, cls) => '<text class="hd-wtext ' + cls + '" x="' + p[0].toFixed(1) + '" y="' + (p[1] + 5).toFixed(1) + '" text-anchor="middle">' + value + "</text>";
  let out = "";

  // Field direction, along the top.
  const northLeft = state.magnets > 0;
  out += text([40, 26], northLeft ? "N" : "S", northLeft ? "hd-wn" : "hd-ws");
  out += text([420, 26], northLeft ? "S" : "N", northLeft ? "hd-ws" : "hd-wn");
  out += '<path class="hd-wflux" d="M62 26L398 26"/>';
  out += '<path class="hd-wfluxhead" transform="translate(' + (northLeft ? 390 : 70) + " 26) rotate(" + (northLeft ? 0 : 180) + ')" d="M6 0L-5 -5L-5 5Z"/>';
  out += '<text class="sm-tick" x="230" y="18" text-anchor="middle">field</text>';

  // Leads.  Each leaves the outer end of its brush and drops down, clear of the coil when the coil is flat.
  const bottom = cy + 168;
  [-1, 1].forEach((side) => {
    const elbowX = side < 0 ? cx - 112 : cx + 112;
    const brushEnd = side < 0 ? cx - 106 : cx + 106;
    let d = "M" + brushEnd + " " + cy + "L" + elbowX + " " + cy + "L" + elbowX + " " + bottom;
    if (slip) {
      // Generator: both leads run on to the meter in the middle.
      d += "L" + (cx + side * 16) + " " + bottom;
    }
    out += '<path class="sm-lead" data-live="' + (live > 0 ? "1" : "0") + '" d="' + d + '"/>';

    // Which way conventional current flows in this lead: up towards the brush, or down away from it.
    let up = false;
    if (slip) {
      // Current leaves the coil through the ring joined to whichever side carries it towards the rings.
      // The left brush is on the yellow ring (side A).
      const leavesHere = side < 0 ? sideA > 0 : sideA < 0;
      up = !leavesHere;
    } else {
      const positive = (side < 0) === (state.battery > 0);
      up = positive;
      out += '<circle class="hd-wside" cx="' + elbowX + '" cy="' + (bottom + 12) + '" r="12"/>';
      out += text([elbowX, bottom + 12], positive ? "+" : "−", "");
    }
    if (live > 0) {
      out += '<path class="sm-leadhead" opacity="' + live.toFixed(2) + '" transform="translate(' + elbowX + " " + (cy + 100) + ") rotate(" + (up ? -90 : 90) + ')" d="M7 0L-5 -6L-5 6Z"/>';
    }
  });
  if (slip) {
    // The meter: a dial whose needle swings either side of zero.
    out += '<circle class="hd-wside" cx="' + cx + '" cy="' + bottom + '" r="17"/>';
    const swing = coil.value * 1.0;
    out += '<path class="sm-meterneedle" d="M' + cx + " " + (bottom + 8) + "L" + (cx + 15 * Math.sin(swing)).toFixed(1) + " " + (bottom + 8 - 15 * Math.cos(swing)).toFixed(1) + '"/>';
    out += '<path class="sm-axis" d="M' + cx + " " + (bottom - 17) + "L" + cx + " " + (bottom - 12) + '"/>';
  }

  // The coil, edge-on, joined to the ring or rings.
  out += '<path class="sm-coilline" d="M' + xy(pol(128, phi)) + "L" + xy(pol(128, phi + Math.PI)) + '"/>';
  if (slip) {
    // Two complete rings, really the same size and one behind the other.
    // The far one (yellow, joined to the yellow side) is drawn larger so both can be seen.
    out += '<circle class="sm-ring sm-ringbig" data-half="a" cx="' + cx + '" cy="' + cy + '" r="60"/>';
    out += '<circle class="sm-ring sm-ringbig" data-half="b" cx="' + cx + '" cy="' + cy + '" r="34"/>';
    // A mark on each ring so its turning can be seen, on the side its part of the coil joins.
    out += '<path class="sm-ringmark" d="M' + xy(pol(52, phi)) + "L" + xy(pol(68, phi)) + '"/>';
    out += '<path class="sm-ringmark" d="M' + xy(pol(26, phi + Math.PI)) + "L" + xy(pol(42, phi + Math.PI)) + '"/>';
    out += '<circle class="hd-wshaft" cx="' + cx + '" cy="' + cy + '" r="12"/>';
    // Left brush on the outer (yellow) ring; right brush reaches over to the inner (copper) ring.
    out += '<rect class="hd-wbrush" x="' + (cx - 106) + '" y="' + (cy - 15) + '" width="37" height="30"/>';
    out += '<rect class="hd-wbrush" x="' + (cx + 43) + '" y="' + (cy - 15) + '" width="63" height="30"/>';
  } else {
    [0, 1].forEach((index) => {
      const centre = phi + index * Math.PI;
      let d = "";
      for (let step = 0; step <= 24; step += 1) {
        const angle = centre - RING.halfAngle + (2 * RING.halfAngle * step) / 24;
        d += (step ? "L" : "M") + xy(pol(62, angle));
      }
      out += '<path class="sm-ring sm-ringbig" data-half="' + (index === 0 ? "a" : "b") + '" d="' + d + '"/>';
    });
    out += '<circle class="hd-wshaft" cx="' + cx + '" cy="' + cy + '" r="12"/>';
    [-1, 1].forEach((side) => {
      const brushX = side < 0 ? cx - 106 : cx + 70;
      out += '<rect class="hd-wbrush" x="' + brushX + '" y="' + (cy - 15) + '" width="36" height="30"/>';
    });
  }

  // The two long sides with their currents, and forces (motor) or motion (generator).
  [0, 1].forEach((index) => {
    const psi = phi + index * Math.PI;
    const current = index === 0 ? sideA : -sideA;
    const at = pol(128, psi);
    out += '<circle class="hd-wside" data-side="' + (index === 0 ? "a" : "b") + '" cx="' + at[0].toFixed(1) + '" cy="' + at[1].toFixed(1) + '" r="11"/>';
    if (slip) {
      const way = tangent(psi);
      const fromX = at[0] + way[1] * state.turnWay * 15;
      const fromY = at[1] - way[2] * state.turnWay * 15;
      const toX = at[0] + way[1] * state.turnWay * 46;
      const toY = at[1] - way[2] * state.turnWay * 46;
      const turn = (Math.atan2(toY - fromY, toX - fromX) * 180) / Math.PI;
      out += '<path class="sm-motionline" d="M' + fromX.toFixed(1) + " " + fromY.toFixed(1) + "L" + toX.toFixed(1) + " " + toY.toFixed(1) + '"/>';
      out += '<path class="sm-motionhead" transform="translate(' + toX.toFixed(1) + " " + toY.toFixed(1) + ") rotate(" + turn.toFixed(1) + ')" d="M6 0L-4 -5L-4 5Z"/>';
    }
    if (live === 0) {
      return;
    }
    out += '<g opacity="' + live.toFixed(2) + '">';
    if (current > 0) {
      out += '<circle class="hd-wdot" cx="' + at[0].toFixed(1) + '" cy="' + at[1].toFixed(1) + '" r="3.2"/>';
    } else {
      out += '<path class="hd-wcross" d="M' + (at[0] - 6).toFixed(1) + " " + (at[1] - 6).toFixed(1) + 'l12 12m0 -12l-12 12"/>';
    }
    if (!slip) {
      const up = current * state.magnets;
      const startY = at[1] - up * 15;
      const endY = at[1] - up * 50;
      out += '<path class="hd-wforce" d="M' + at[0].toFixed(1) + " " + startY.toFixed(1) + "L" + at[0].toFixed(1) + " " + endY.toFixed(1) + '"/>';
      out += '<path class="hd-wforcehead" transform="translate(' + at[0].toFixed(1) + " " + endY.toFixed(1) + ") rotate(" + (up > 0 ? -90 : 90) + ')" d="M6 0L-4 -5L-4 5Z"/>';
    }
    out += "</g>";
  });
  return out;
}

// ---------------- live behaviour ----------------

const motor = {
  stage: document.getElementById("stage1"),
  scene: document.querySelector("#stage1 [data-scene]"),
  flat: document.querySelector("#stage2 [data-scene]"),
  ring: document.querySelector("#stage3 [data-scene]"),
  stepBack: document.getElementById("step-back"),
  stepNext: document.getElementById("step-next"),
  stepCount: document.getElementById("step-count"),
  stepTitle: document.getElementById("step-title"),
  stepBody: document.getElementById("step-body"),
  stageIndex: -1, // which stage of the step-through is showing; -1 means free running
  target: null, // angle the coil is being moved to, or null
  readouts: document.querySelectorAll("[data-readout]"),
  spinButton: document.getElementById("spin"),
  slider: document.getElementById("angle"),
  sliderOut: document.getElementById("angle-out"),
  batteryButton: document.getElementById("battery"),
  forcesButton: document.getElementById("show-forces"),
  designButtons: [...document.querySelectorAll("button[data-design]")],
  design: "split", // "split": DC motor with a split ring.  "slip": AC generator with slip rings.
  turnWay: 1, // generator only: +1 turned anticlockwise (seen from the ring end), -1 clockwise
  magnetButton: document.getElementById("magnets"),
  toggles: [...document.querySelectorAll("button[data-show]")],
  view: { azimuth: 38, elevation: 30, scale: 2.35, centre: [10, 0, -20], width: 860, height: 560 },
  phi: 0.5, // angle of side A
  speed: 0, // radians per second
  spinning: !calm.matches,
  battery: 1,
  magnets: 1,
  showCurrent: true,
  showForces: true,
  showField: true,
  labels: true,
  dirty: true,
};

function draw() {
  const P = cameraFor(motor.view);
  motor.scene.innerHTML = motorScene(motor, P);
  motor.flat.innerHTML = endOnSvg(motor);
  motor.ring.innerHTML = ringSvg(motor);

  const degrees = Math.round((((motor.phi % TURN) + TURN) % TURN) / TURN * 360) % 360;
  if (motor.design === "slip") {
    // Generator readouts.
    const value = coilState(motor).value;
    const share = Math.round(Math.abs(value) * 100);
    let text = degrees + "° · current " + share + "% of its largest";
    if (share < 3) {
      text = degrees + "° · coil upright: sides moving along the field, no current";
    }
    let turned = "turned anticlockwise";
    if (motor.turnWay < 0) {
      turned = "turned clockwise";
    }
    motor.readouts[0].textContent = text;
    motor.readouts[1].textContent = "seen from the ring end · " + turned;
    motor.readouts[2].textContent = degrees + "° · each ring on its own brush";
  } else {
    // Motor readouts.
    const effect = turningEffect(motor.phi, motor.battery, motor.magnets);
    const share = Math.round(Math.abs(effect) * 100);
    let way = "anticlockwise";
    if (motor.battery * motor.magnets < 0) {
      way = "clockwise";
    }
    let text = degrees + "° · turning effect " + share + "% · " + way;
    let contact = "each half of the ring on a brush";
    if (brushContact(motor.phi) === 0) {
      text = degrees + "° · brushes over the gaps: no current, no force";
      contact = "brushes over the gaps";
    }
    motor.readouts[0].textContent = text;
    motor.readouts[1].textContent = "seen from the commutator end · " + way;
    motor.readouts[2].textContent = degrees + "° · " + contact;
  }
  motor.slider.value = String(degrees);
  motor.sliderOut.textContent = degrees + "°";
  motor.dirty = false;
}

function setSpinning(on) {
  motor.spinning = on;
  if (!on) {
    motor.speed = 0;
  }
  motor.spinButton.textContent = on ? "Pause" : "Spin";
  motor.spinButton.setAttribute("aria-pressed", on ? "true" : "false");
}

// Show one stage of the step-through and send the coil to its angle.
function showStage(index) {
  const stages = stagesFor(motor);
  motor.stageIndex = index;
  if (index < 0) {
    motor.target = null;
    motor.stepCount.textContent = "Step-through";
    if (motor.design === "slip") {
      motor.stepTitle.textContent = "One full turn, stage by stage";
      motor.stepBody.textContent = "Press Next to stop the generator and walk through what the slip rings do. All three figures move together.";
    } else {
      motor.stepTitle.textContent = "One half turn, stage by stage";
      motor.stepBody.textContent = "Press Next to stop the motor and walk through what the split ring does. All three figures move together.";
    }
    motor.stepBack.disabled = true;
    motor.stepNext.disabled = false;
    return;
  }
  // The explanations assume the cell, the magnets and the turning are all the normal way round.
  motor.battery = 1;
  motor.magnets = 1;
  motor.turnWay = 1;
  motor.batteryButton.setAttribute("aria-pressed", "false");
  motor.magnetButton.setAttribute("aria-pressed", "false");
  setSpinning(false);
  const stageNow = stages[index];
  motor.target = stageNow.angle * DEG;
  motor.stepCount.textContent = "Stage " + (index + 1) + " of " + stages.length + " · coil at " + stageNow.angle + "°";
  motor.stepTitle.textContent = stageNow.title;
  motor.stepBody.textContent = stageNow.body;
  motor.stepBack.disabled = index === 0;
  motor.stepNext.disabled = index === stages.length - 1;
  motor.dirty = true;
}

// Switch between the DC motor (split ring) and the AC generator (slip rings).
function setDesign(name) {
  motor.design = name;
  motor.speed = 0;
  motor.designButtons.forEach((button) => {
    button.setAttribute("aria-pressed", button.dataset.design === name ? "true" : "false");
  });
  // Some controls mean something different for each machine.
  if (name === "slip") {
    motor.batteryButton.textContent = "Reverse turning";
    motor.batteryButton.setAttribute("aria-pressed", motor.turnWay < 0 ? "true" : "false");
    motor.forcesButton.textContent = "Motion";
  } else {
    motor.batteryButton.textContent = "Reverse cell";
    motor.batteryButton.setAttribute("aria-pressed", motor.battery < 0 ? "true" : "false");
    motor.forcesButton.textContent = "Forces";
  }
  // Show the notes that belong to this machine.
  document.querySelectorAll("[data-for]").forEach((block) => {
    block.hidden = block.dataset.for !== name;
  });
  showStage(-1);
  motor.dirty = true;
}

function step(dt) {
  if (motor.target !== null) {
    // Glide to the stage's angle by the shorter way round.
    let gap = (motor.target - motor.phi) % TURN;
    if (gap > Math.PI) {
      gap -= TURN;
    }
    if (gap < -Math.PI) {
      gap += TURN;
    }
    const most = 1.4 * dt;
    if (calm.matches || Math.abs(gap) <= most) {
      motor.phi = motor.target;
      motor.target = null;
    } else {
      motor.phi += Math.sign(gap) * most;
    }
    motor.dirty = true;
  }
  if (motor.spinning && motor.design === "slip") {
    // Generator: someone turns the handle at a steady speed.
    motor.phi += motor.turnWay * 1.5 * dt;
    motor.dirty = true;
  }
  if (motor.spinning && motor.design !== "slip") {
    // The turning effect speeds the coil up; friction slows it down.
    // So it surges twice a turn and coasts through the upright position.
    const push = 4.1 * turningEffect(motor.phi, motor.battery, motor.magnets);
    const drag = 1.2 * motor.speed;
    motor.speed += (push - drag) * dt;
    motor.phi += motor.speed * dt;
    motor.dirty = true;
  }
  if (motor.dirty) {
    draw();
  }
}

motor.spinButton.addEventListener("click", () => {
  setSpinning(!motor.spinning);
  // Running the motor leaves the step-through.
  if (motor.spinning) {
    showStage(-1);
  }
});

motor.stepNext.addEventListener("click", () => {
  showStage(Math.min(stagesFor(motor).length - 1, motor.stageIndex + 1));
});

motor.stepBack.addEventListener("click", () => {
  showStage(Math.max(0, motor.stageIndex - 1));
});

motor.slider.addEventListener("input", () => {
  // Turning it by hand stops the motor.
  setSpinning(false);
  motor.target = null;
  motor.phi = (Number(motor.slider.value) / 360) * TURN;
  motor.dirty = true;
});

motor.batteryButton.addEventListener("click", () => {
  // Motor: turn the cell round.  Generator: turn the handle the other way.
  if (motor.design === "slip") {
    motor.turnWay = -motor.turnWay;
    motor.batteryButton.setAttribute("aria-pressed", motor.turnWay < 0 ? "true" : "false");
  } else {
    motor.battery = -motor.battery;
    motor.batteryButton.setAttribute("aria-pressed", motor.battery < 0 ? "true" : "false");
  }
  motor.dirty = true;
});

motor.designButtons.forEach((button) => {
  button.addEventListener("click", () => {
    setDesign(button.dataset.design);
  });
});

motor.magnetButton.addEventListener("click", () => {
  motor.magnets = -motor.magnets;
  motor.magnetButton.setAttribute("aria-pressed", motor.magnets < 0 ? "true" : "false");
  motor.dirty = true;
});

motor.toggles.forEach((button) => {
  button.addEventListener("click", () => {
    const key = button.dataset.show;
    motor[key] = !motor[key];
    button.setAttribute("aria-pressed", motor[key] ? "true" : "false");
    motor.dirty = true;
  });
});

// Drag to turn the model round; arrow keys do the same.
{
  const stage = motor.stage;
  let from = null;
  stage.addEventListener("pointerdown", (event) => {
    from = { x: event.clientX, y: event.clientY, azimuth: motor.view.azimuth, elevation: motor.view.elevation };
    stage.setPointerCapture(event.pointerId);
    stage.setAttribute("data-dragging", "");
  });
  stage.addEventListener("pointermove", (event) => {
    if (!from) {
      return;
    }
    motor.view.azimuth = from.azimuth - (event.clientX - from.x) * 0.45;
    // Touch keeps vertical movement for scrolling the page.
    if (event.pointerType !== "touch") {
      const tilt = from.elevation + (event.clientY - from.y) * 0.3;
      motor.view.elevation = Math.min(70, Math.max(8, tilt));
    }
    motor.dirty = true;
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
      motor.view.azimuth += 15;
    } else if (event.key === "ArrowRight") {
      motor.view.azimuth -= 15;
    } else if (event.key === "ArrowUp") {
      motor.view.elevation = Math.min(70, motor.view.elevation + 8);
    } else if (event.key === "ArrowDown") {
      motor.view.elevation = Math.max(8, motor.view.elevation - 8);
    } else if (event.key === " ") {
      setSpinning(!motor.spinning);
    } else {
      handled = false;
    }
    if (handled) {
      event.preventDefault();
      motor.dirty = true;
    }
  });
}

let lastTime = 0;

function frame(now) {
  let dt = 1 / 60;
  if (lastTime) {
    dt = Math.min((now - lastTime) / 1000, 1 / 20);
  }
  lastTime = now;
  step(dt);
  requestAnimationFrame(frame);
}

// Test hook: lets a check script pose the model directly.
window.__motor = { motor, setSpinning, draw, showStage, setDesign };

if (calm.matches) {
  setSpinning(false);
}
setDesign("split");
draw();
requestAnimationFrame(frame);
