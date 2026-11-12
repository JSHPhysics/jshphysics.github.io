// Shared geometry for the hairdryer figures.
// The build script imports this file, and the page inlines it (with "export" removed),
// so the moving parts are drawn by the same code at build time and in the browser.

const TAU = Math.PI * 2;
const DEG = Math.PI / 180;

// Light bands: the same four-tone thresholds the Anatomy kit uses.
const BANDS = [0, 0.2, 0.42, 0.62];

// ---------- camera ----------

export function cam(P) {
  const a = (P.azimuth ?? 45) * DEG;
  const e = (P.elevation ?? 30) * DEG;
  return {
    sa: Math.sin(a),
    ca: Math.cos(a),
    se: Math.sin(e),
    ce: Math.cos(e),
    k: P.scale * Math.sqrt(1.6),
  };
}

// World point -> screen point.
// The viewer stands in the direction (cos a, sin a) from the origin, looking back at it, with z up.
// Their right-hand side is then (-sin a, cos a), which keeps the picture right-handed:
// left-hand-rule and right-hand-rule checks on the drawing give the true answer.
export function flat(p, P) {
  const c = cam(P);
  const sx = P.origin[0] + (-p[0] * c.sa + p[1] * c.ca) * c.k;
  const sy = P.origin[1] + ((p[0] * c.ca + p[1] * c.sa) * c.se - p[2] * c.ce) * c.k;
  return [sx, sy];
}

// Unit vector pointing at the viewer.
export function viewDir(P) {
  const c = cam(P);
  return [c.ca * c.ce, c.sa * c.ce, c.se];
}

// Unit vector pointing at the light.
export function lightDir(P) {
  const c = cam(P);
  const raw = [-c.sa, c.ca, 1.2];
  const length = Math.hypot(raw[0], raw[1], raw[2]);
  return [raw[0] / length, raw[1] / length, raw[2] / length];
}

const dot = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2];

function bandOf(score) {
  let tone = 0;
  while (tone < BANDS.length && score >= BANDS[tone]) {
    tone += 1;
  }
  return tone;
}

// ---------- frames along the x axis ----------
// Every round part in these figures lies along x.
// A frame is { o: [x, y, z], S: scale }.  Angle 0 points along +y, 90 degrees points up.

export function pt(F, s, r, angle) {
  return [F.o[0] + s, F.o[1] + r * Math.cos(angle), F.o[2] + r * Math.sin(angle)];
}

const radial = (angle) => [0, Math.cos(angle), Math.sin(angle)];
const tangent = (angle) => [0, -Math.sin(angle), Math.cos(angle)];
const AXIS = [1, 0, 0];
const neg = (v) => [-v[0], -v[1], -v[2]];

// ---------- mesh painter ----------

const tenth = (value) => {
  const text = (Math.round(value * 10) / 10).toFixed(1).replace(/\.0$/, "");
  return text === "-0" ? "0" : text;
};

function pathOf(points, closed) {
  let d = "";
  for (let index = 0; index < points.length; index += 1) {
    d += (index ? "L" : "M") + tenth(points[index][0]) + " " + tenth(points[index][1]);
  }
  return d + (closed ? "Z" : "");
}

function signedArea(points) {
  let area = 0;
  for (let index = 0; index < points.length; index += 1) {
    const a = points[index];
    const b = points[(index + 1) % points.length];
    area += a[0] * b[1] - b[0] * a[1];
  }
  return area / 2;
}

// faces: [{ pts: [p3, ...], n: [x, y, z], soft: [bool per edge], two: bool }]
// Edge i joins pts[i] to pts[i + 1].  A "soft" edge lies inside one curved surface.
// Returns the paths for one solid: fill, tone buckets, creases and outline.
export function mesh(faces, P) {
  const V = viewDir(P);
  const L = lightDir(P);
  const fills = [];
  const buckets = [[], [], [], [], []];
  const edges = new Map();
  let sum = [0, 0, 0];
  let count = 0;

  for (const face of faces) {
    let normal = face.n;
    let facing = dot(normal, V);
    if (face.two && facing < 0) {
      normal = neg(normal);
      facing = -facing;
    }
    for (const p of face.pts) {
      sum = [sum[0] + p[0], sum[1] + p[1], sum[2] + p[2]];
      count += 1;
    }
    if (facing <= 1e-6) {
      continue;
    }
    const screen = face.pts.map((p) => flat(p, P));
    const ordered = signedArea(screen) < 0 ? [...screen].reverse() : screen;
    const d = pathOf(ordered, true);
    fills.push(d);
    buckets[bandOf(dot(normal, L))].push(d);

    for (let index = 0; index < screen.length; index += 1) {
      const a = screen[index];
      const b = screen[(index + 1) % screen.length];
      const ka = tenth(a[0]) + " " + tenth(a[1]);
      const kb = tenth(b[0]) + " " + tenth(b[1]);
      if (ka === kb) {
        continue;
      }
      const key = ka < kb ? ka + "|" + kb : kb + "|" + ka;
      const soft = Boolean(face.soft && face.soft[index]);
      const seen = edges.get(key);
      if (seen) {
        seen.count += 1;
        seen.soft = seen.soft && soft;
      } else {
        edges.set(key, { count: 1, soft, d: "M" + ka + "L" + kb });
      }
    }
  }

  let outline = "";
  let crease = "";
  for (const edge of edges.values()) {
    if (edge.count === 1) {
      // Seen by one visible face only: a silhouette or a limb.
      outline += edge.d;
    } else if (!edge.soft) {
      // Shared by two visible faces across a real corner.
      crease += edge.d;
    }
  }

  return {
    fill: fills.join(""),
    shades: buckets.slice(0, 4).map((list) => list.join("")),
    top: buckets[4].join(""),
    crease,
    outline,
    centre: count ? [sum[0] / count, sum[1] / count, sum[2] / count] : [0, 0, 0],
  };
}

// One solid as SVG, using the kit's own classes so it takes the kit's tones.
// options.alpha (0 to 1) makes the solid see-through: used for casings.
export function meshSvg(m, options = {}) {
  const tone = options.tone || "hi";
  const crease = options.crease || "faint";
  const cls = options.cls ? " " + options.cls : "";
  const lit = options.lit ? ' data-lit=""' : "";
  const ghost = options.alpha !== undefined && options.alpha < 0.999;
  let fillOpen = "";
  let fillClose = "";
  let edgeOpacity = "";
  if (ghost) {
    fillOpen = '<g opacity="' + options.alpha.toFixed(3) + '">';
    fillClose = "</g>";
    edgeOpacity = ' opacity="' + Math.min(1, options.alpha * 2.4).toFixed(3) + '"';
  }
  let out = '<g class="iso-solid' + cls + '" data-seamless=""' + lit + ">";
  out += fillOpen;
  out += '<path class="iso-fill" d="' + m.fill + '"/>';
  m.shades.forEach((d, shade) => {
    if (d) {
      out += '<path class="iso-shade" data-shade="' + shade + '" d="' + d + '"/>';
    }
  });
  if (m.top) {
    out += '<path class="iso-top" d="' + m.top + '"/>';
  }
  if (options.tint) {
    out += '<path class="hd-tint" data-pole="' + options.tint.pole + '" style="opacity:' + options.tint.alpha + '" d="' + m.fill + '"/>';
  }
  out += fillClose;
  if (m.crease) {
    out += '<path class="iso-line iso-crease" data-tone="' + crease + '"' + edgeOpacity + ' d="' + m.crease + '"/>';
  }
  if (options.inner) {
    out += options.inner;
  }
  out += '<path class="iso-line iso-edge" data-tone="' + tone + '"' + edgeOpacity + ' d="' + m.outline + '"/>';
  return out + "</g>";
}

// ---------- shapes ----------

// A piece of tube wall between angles a0 and a1 (radians), following a profile [[s, r], ...].
// t is the wall thickness.  Returns the faces in groups so a cutaway can paint
// the far inside wall before the things inside it and the near outside wall after them.
export function sector(F, profile, t, a0, a1, options = {}) {
  const ends = options.ends || [false, false];
  const full = Math.abs(a1 - a0 - TAU) < 1e-9;
  const steps = Math.max(2, Math.ceil((a1 - a0) / ((options.step || 6) * DEG)));
  const angleAt = (index) => a0 + ((a1 - a0) * index) / steps;
  const outer = [];
  const inner = [];
  const cuts = [];
  const caps = [];
  const last = profile.length - 2;

  for (let j = 0; j <= last; j += 1) {
    const [s0, r0] = profile[j];
    const [s1, r1] = profile[j + 1];
    const slope = (r1 - r0) / (s1 - s0 || 1);
    const norm = Math.hypot(1, slope);

    for (let i = 0; i < steps; i += 1) {
      const ta = angleAt(i);
      const tb = angleAt(i + 1);
      const mid = radial((ta + tb) / 2);
      const n = [-slope / norm, mid[1] / norm, mid[2] / norm];
      const firstSide = !full && i === 0;
      const lastSide = !full && i === steps - 1;
      // Edge order: rim at s0, side at tb, rim at s1, side at ta.
      const soft = [j !== 0, !lastSide, j !== last, !firstSide];
      outer.push({
        pts: [pt(F, s0, r0, ta), pt(F, s0, r0, tb), pt(F, s1, r1, tb), pt(F, s1, r1, ta)],
        n,
        soft,
      });
      inner.push({
        pts: [pt(F, s0, r0 - t, ta), pt(F, s0, r0 - t, tb), pt(F, s1, r1 - t, tb), pt(F, s1, r1 - t, ta)],
        n: neg(n),
        soft,
      });
    }

    if (!full) {
      // The two flat faces where the wall was cut along its length.
      cuts.push({
        pts: [pt(F, s0, r0 - t, a0), pt(F, s0, r0, a0), pt(F, s1, r1, a0), pt(F, s1, r1 - t, a0)],
        n: neg(tangent(a0)),
        soft: [j !== 0, false, j !== last, false],
      });
      cuts.push({
        pts: [pt(F, s0, r0 - t, a1), pt(F, s0, r0, a1), pt(F, s1, r1, a1), pt(F, s1, r1 - t, a1)],
        n: tangent(a1),
        soft: [j !== 0, false, j !== last, false],
      });
    }
  }

  // The ring-shaped faces at either end.
  [0, 1].forEach((which) => {
    if (!ends[which]) {
      return;
    }
    const [s, r] = which === 0 ? profile[0] : profile[profile.length - 1];
    for (let i = 0; i < steps; i += 1) {
      const ta = angleAt(i);
      const tb = angleAt(i + 1);
      const firstSide = !full && i === 0;
      const lastSide = !full && i === steps - 1;
      caps.push({
        pts: [pt(F, s, r - t, ta), pt(F, s, r, ta), pt(F, s, r, tb), pt(F, s, r - t, tb)],
        n: which === 0 ? neg(AXIS) : AXIS,
        soft: [!firstSide, false, !lastSide, false],
      });
    }
  });

  return { outer, inner, cuts, caps, all: [...outer, ...inner, ...cuts, ...caps] };
}

// A box that points outward from the axis at angle psi:
// s0..s1 along the axis, r0..r1 away from it, and w either side.
export function radialBox(F, s0, s1, r0, r1, w, psi) {
  const c = Math.cos(psi);
  const n = Math.sin(psi);
  const at = (s, r, t) => [F.o[0] + s, F.o[1] + r * c - t * n, F.o[2] + r * n + t * c];
  const R = radial(psi);
  const T = tangent(psi);
  return [
    { pts: [at(s0, r1, -w), at(s1, r1, -w), at(s1, r1, w), at(s0, r1, w)], n: R },
    { pts: [at(s0, r0, -w), at(s1, r0, -w), at(s1, r0, w), at(s0, r0, w)], n: neg(R) },
    { pts: [at(s0, r0, w), at(s1, r0, w), at(s1, r1, w), at(s0, r1, w)], n: T },
    { pts: [at(s0, r0, -w), at(s1, r0, -w), at(s1, r1, -w), at(s0, r1, -w)], n: neg(T) },
    { pts: [at(s1, r0, -w), at(s1, r1, -w), at(s1, r1, w), at(s1, r0, w)], n: AXIS },
    { pts: [at(s0, r0, -w), at(s0, r1, -w), at(s0, r1, w), at(s0, r0, w)], n: neg(AXIS) },
  ];
}

// ---------- the motor's electrical model ----------
// Three coils, joined in a ring, each joint soldered to one commutator segment.
// Two brushes, half a turn apart, press on the commutator.
// Angles are in the same frame as the drawing: 0 along +y, 90 degrees up.

export const MOTOR = {
  north: 105 * DEG, // middle of the north magnet
  south: 285 * DEG, // middle of the south magnet
  brushPlus: 123 * DEG,
  brushMinus: 303 * DEG,
  segmentLag: 42 * DEG, // each segment sits this far behind its pole
  flip: 195 * DEG, // a pole is "north" while it is within a quarter turn of this angle
};

const wrap = (angle) => {
  let value = angle % TAU;
  if (value > Math.PI) {
    value -= TAU;
  }
  if (value <= -Math.PI) {
    value += TAU;
  }
  return value;
};

// Current in coil k (0, 1, 2) when the rotor is at angle phi.
// +1 or -1: this coil is alone between the brushes and takes the full current.
// +0.5 or -0.5: it shares the other path with a second coil.
// Positive current makes the pole's outer face a north pole.
export function coilCurrent(k, phi) {
  const psi = phi + (k * TAU) / 3;
  const x = wrap(psi - MOTOR.flip);
  const size = Math.abs(x);
  if (size < 30 * DEG) {
    return 1;
  }
  if (size < 90 * DEG) {
    return 0.5;
  }
  if (size > 150 * DEG) {
    return -1;
  }
  return -0.5;
}

// Turning effect on pole k, as a share of the largest one pole can feel.
export function coilTorque(k, phi) {
  const psi = phi + (k * TAU) / 3;
  return coilCurrent(k, phi) * Math.sin(MOTOR.south - psi);
}

// ---------- the moving parts ----------

// The three-pole armature at angle phi.  Rebuilt every frame.
export function rotorSvg(cfg, phi, P) {
  const F = { o: cfg.o };
  const m = (value) => value * cfg.S;
  const V = viewDir(P);
  const pieces = [];

  for (let k = 0; k < 3; k += 1) {
    const psi = phi + (k * TAU) / 3;
    const current = coilCurrent(k, phi);

    // The winding: a block of wire wrapped round the pole's arm.
    const windingFaces = radialBox(F, m(11.2), m(28.8), m(3.6), m(8), m(4.4), psi);
    const winding = mesh(windingFaces, P);
    // Wire turns: lines round the block at four levels.
    let turns = "";
    const c = Math.cos(psi);
    const n = Math.sin(psi);
    const at = (s, r, t) => flat([F.o[0] + s, F.o[1] + r * c - t * n, F.o[2] + r * n + t * c], P);
    const sides = [
      { normal: tangent(psi), a: [m(11.2), m(4.4)], b: [m(28.8), m(4.4)] },
      { normal: neg(tangent(psi)), a: [m(11.2), -m(4.4)], b: [m(28.8), -m(4.4)] },
      { normal: AXIS, a: [m(28.8), -m(4.4)], b: [m(28.8), m(4.4)] },
    ];
    for (const side of sides) {
      if (dot(side.normal, V) <= 0.02) {
        continue;
      }
      for (let level = 1; level <= 4; level += 1) {
        const r = m(3.6) + (m(4.4) * level) / 5;
        turns += pathOf([at(side.a[0], r, side.a[1]), at(side.b[0], r, side.b[1])], false);
      }
    }
    pieces.push({
      depth: dot(winding.centre, V),
      svg: meshSvg(winding, { tone: "mid", inner: turns ? '<path class="iso-line" data-tone="lo" d="' + turns + '"/>' : "" }),
    });

    // The pole shoe: the curved iron face that passes the magnets.
    const shoeFaces = sector(F, [[m(13), m(10.5)], [m(27), m(10.5)]], m(2.5), psi - 38 * DEG, psi + 38 * DEG, { ends: [true, true], step: 12 }).all;
    const shoe = mesh(shoeFaces, P);
    const tint = cfg.tint ? { pole: current > 0 ? "n" : "s", alpha: Math.abs(current) === 1 ? 0.42 : 0.16 } : null;
    pieces.push({
      depth: dot(shoe.centre, V),
      svg: meshSvg(shoe, { tone: "hi", crease: "lo", lit: Boolean(cfg.lit), tint }),
    });
  }

  pieces.sort((a, b) => a.depth - b.depth);
  return pieces.map((piece) => piece.svg).join("");
}

// The gaps between the three commutator segments, and the mark on the shaft end.
export function commutatorSvg(cfg, phi, P) {
  const F = { o: cfg.o };
  const m = (value) => value * cfg.S;
  const V = viewDir(P);
  let gaps = "";
  for (let k = 0; k < 3; k += 1) {
    // A segment is centred segmentLag behind its pole, so the gaps sit 60 degrees either side of that.
    const angle = phi + (k * TAU) / 3 - MOTOR.segmentLag + 60 * DEG;
    if (dot(radial(angle), V) < 0.06) {
      continue;
    }
    gaps += pathOf([flat(pt(F, m(3.5), m(4.2), angle), P), flat(pt(F, m(8.5), m(4.2), angle), P)], false);
  }
  const mark = pathOf([flat(pt(F, m(40), 0, 0), P), flat(pt(F, m(40), m(3.4), phi), P)], false);
  return {
    gaps: gaps ? '<path class="iso-line" data-tone="hi" d="' + gaps + '"/>' : "",
    mark: '<path class="iso-line" data-tone="lit" d="' + mark + '"/>',
  };
}

// The fan blades at angle phi, split into those behind the hub and those in front.
export function fanSvg(cfg, phi, P) {
  const F = { o: cfg.o };
  const V = viewDir(P);
  const hubDepth = dot(pt(F, cfg.s, 0, 0), V);
  const blades = [];
  for (let k = 0; k < cfg.blades; k += 1) {
    const t = phi + (k * TAU) / cfg.blades;
    const a = pt(F, cfg.s - 4, cfg.r0, t - 0.34);
    const b = pt(F, cfg.s + 4, cfg.r0, t + 0.34);
    const c = pt(F, cfg.s + 5, cfg.r1, t + 0.13);
    const d = pt(F, cfg.s - 5, cfg.r1, t - 0.13);
    // Normal of the (slightly twisted) blade, from its two diagonals.
    const p = [c[0] - a[0], c[1] - a[1], c[2] - a[2]];
    const q = [d[0] - b[0], d[1] - b[1], d[2] - b[2]];
    const raw = [p[1] * q[2] - p[2] * q[1], p[2] * q[0] - p[0] * q[2], p[0] * q[1] - p[1] * q[0]];
    const length = Math.hypot(raw[0], raw[1], raw[2]) || 1;
    const blade = mesh([{ pts: [a, b, c, d], n: [raw[0] / length, raw[1] / length, raw[2] / length], two: true }], P);
    blades.push({ depth: dot(blade.centre, V), svg: meshSvg(blade, { tone: "mid" }) });
  }
  blades.sort((x, y) => x.depth - y.depth);
  let back = "";
  let front = "";
  for (const blade of blades) {
    if (blade.depth < hubDepth) {
      back += blade.svg;
    } else {
      front += blade.svg;
    }
  }
  return { back, front };
}
