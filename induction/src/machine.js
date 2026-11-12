
// ---------------------------------------------------------------
// The coil-and-magnets machine, shared with the Simple Motor and Generator page.
// Here it is used as an AC generator (slip rings) or a dynamo (split ring).
// geom.mjs is inlined above this.
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
  // How fast the coil is turned: 0.5 at normal speed, 1 when turned fast.
  let speed = 1;
  if (state.speedFactor !== undefined) {
    speed = state.speedFactor;
  }
  if (state.design === "slip" || state.design === "dynamo") {
    // The coil is turned by hand.  Side A moves at right angles to the axle, and the current
    // induced in it is largest when it cuts straight across the field (coil flat) and zero
    // when it moves along the field (coil upright).  It reverses every half turn.
    const across = Math.cos(state.phi);
    let induced = -state.magnets * state.turnWay * across * speed;
    // What the meter sees.  Slip rings pass the coil's current straight on.
    let meter = state.magnets * state.turnWay * across * speed;
    let contact = 1;
    if (state.design === "dynamo") {
      // The split ring swaps the connections every half turn, so the meter current never reverses.
      // While the brushes are over the gaps (coil upright) nothing reaches the meter.
      contact = brushContact(state.phi);
      meter = state.magnets * state.turnWay * Math.abs(across) * speed * contact;
      induced = induced * contact;
    }
    let sign = 1;
    if (induced < 0) {
      sign = -1;
    }
    const live = Math.min(1, Math.abs(induced) / 0.06);
    return { sign, live, value: induced, meter };
  }
  const live = brushContact(state.phi);
  const sign = currentInSideA(state.phi, state.battery);
  let value = 0;
  if (live > 0) {
    value = sign;
  }
  return { sign, live, value, meter: 0 };
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
  const slip = state.design !== "split"; // true for both generators
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
      if (state.design === "dynamo") {
        // Dynamo: each brush touches the half-ring of whichever side of the coil is next to it.
        let nearSide = sideA;
        if (Math.cos(phi) < 0) {
          nearSide = -sideA;
        }
        // nearSide is the current in the side that is on the +y side of the axle.
        let leaves = nearSide > 0;
        if (side < 0) {
          leaves = nearSide < 0;
        }
        towardsBrush = !leaves;
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
    if (state.design === "slip") {
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
      const swing = coil.meter * 0.95;
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
  const slip = state.design !== "split"; // true for both generators
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

  if (state.design === "slip") {
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
      if (state.design === "split") {
        out += text([x + 10, cy], positive ? "+" : "−", "hd-wsign");
      }
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

  // --- graph: current through the meter against time ---
  out += outputGraph(state, 40, 425, 380, 70);
  return out;
}


// Current through the meter against time, for a fixed stretch of time.
// At normal speed the coil makes two turns in that time; turned fast it makes four.
function outputGraph(state, gx, gy, gw, gh) {
  let out = "";
  const middle = gy - gh / 2;
  const turnsShown = Math.round(state.speedFactor / 0.5) * 2;
  const sweep = turnsShown * TURN;
  out += '<path class="sm-axis" d="M' + gx + " " + (gy - gh) + "L" + gx + " " + gy + "M" + gx + " " + middle + "L" + (gx + gw) + " " + middle + '"/>';

  // The curve.
  const samples = 360;
  let curve = "";
  for (let index = 0; index <= samples; index += 1) {
    const angle = state.turnWay * (sweep * index) / samples;
    const reading = coilState({ design: state.design, phi: angle, magnets: state.magnets, turnWay: state.turnWay, speedFactor: state.speedFactor }).meter;
    const x = gx + (gw * index) / samples;
    const y = middle - (gh / 2) * reading;
    if (index === 0) {
      curve += "M";
    } else {
      curve += "L";
    }
    curve += x.toFixed(1) + " " + y.toFixed(1);
  }
  out += '<path class="sm-curve" d="' + curve + '"/>';

  // A tick for each completed turn of the coil.
  for (let turn = 1; turn <= turnsShown; turn += 1) {
    const x = gx + (gw * turn) / turnsShown;
    out += '<path class="sm-axis" d="M' + x + " " + (middle - 4) + "L" + x + " " + (middle + 4) + '"/>';
    out += '<text class="sm-tick" x="' + x + '" y="' + (gy + 17) + '" text-anchor="middle">turn ' + turn + "</text>";
  }
  out += '<text class="sm-tick" x="' + gx + '" y="' + (gy - gh - 8) + '">current through the meter</text>';
  out += '<text class="sm-tick" x="' + gx + '" y="' + (gy + 17) + '">time →</text>';

  // Where the coil is now.
  let swept = (state.phi * state.turnWay) % sweep;
  if (swept < 0) {
    swept += sweep;
  }
  const nowX = gx + (gw * swept) / sweep;
  const nowY = middle - (gh / 2) * coilState(state).meter;
  out += '<path class="sm-markline" d="M' + nowX.toFixed(1) + " " + middle + "L" + nowX.toFixed(1) + " " + nowY.toFixed(1) + '"/>';
  out += '<circle class="sm-mark" cx="' + nowX.toFixed(1) + '" cy="' + nowY.toFixed(1) + '" r="4.5"/>';
  return out;
}
