// VSEPR model for the molecule stand.
// Pure maths, no drawing. The build script and the page both use this file,
// so every angle on screen comes from the same vectors that place the atoms.

const DEG = Math.PI / 180;

// ---------- small vector helpers ----------

export function dot(a, b) {
  return a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
}

export function cross(a, b) {
  return [
    a[1] * b[2] - a[2] * b[1],
    a[2] * b[0] - a[0] * b[2],
    a[0] * b[1] - a[1] * b[0],
  ];
}

export function unit(a) {
  const size = Math.hypot(a[0], a[1], a[2]);
  if (size < 1e-9) {
    return [0, 0, 1];
  }
  return [a[0] / size, a[1] / size, a[2] / size];
}

// Angle between two directions, in degrees.
export function angleBetween(a, b) {
  let c = dot(unit(a), unit(b));
  c = Math.max(-1, Math.min(1, c));
  return Math.acos(c) / DEG;
}

// A direction from a polar angle (measured from straight up, +z)
// and an azimuth (measured from +x towards +y). Both in degrees.
export function fromUp(polar, azimuth) {
  const p = polar * DEG;
  const a = azimuth * DEG;
  return [Math.sin(p) * Math.cos(a), Math.sin(p) * Math.sin(a), Math.cos(p)];
}

// The same, but with the polar angle measured from straight down (-z).
export function fromDown(polar, azimuth) {
  const up = fromUp(polar, azimuth);
  return [up[0], up[1], -up[2]];
}

// Rotate vector v about unit axis n by an angle in degrees (Rodrigues).
export function rotateAbout(v, n, degrees) {
  const t = degrees * DEG;
  const c = Math.cos(t);
  const s = Math.sin(t);
  const nxv = cross(n, v);
  const nv = dot(n, v);
  return [
    v[0] * c + nxv[0] * s + n[0] * nv * (1 - c),
    v[1] * c + nxv[1] * s + n[1] * nv * (1 - c),
    v[2] * c + nxv[2] * s + n[2] * nv * (1 - c),
  ];
}

// ---------- 3 x 3 rotation matrices (row-major) ----------

export function matMul(A, B) {
  const out = [[0, 0, 0], [0, 0, 0], [0, 0, 0]];
  for (let r = 0; r < 3; r++) {
    for (let c = 0; c < 3; c++) {
      out[r][c] = A[r][0] * B[0][c] + A[r][1] * B[1][c] + A[r][2] * B[2][c];
    }
  }
  return out;
}

export function matApply(A, v) {
  return [dot(A[0], v), dot(A[1], v), dot(A[2], v)];
}

export function transpose(A) {
  return [
    [A[0][0], A[1][0], A[2][0]],
    [A[0][1], A[1][1], A[2][1]],
    [A[0][2], A[1][2], A[2][2]],
  ];
}

// Turn about the vertical axis (the turntable).
export function turnZ(degrees) {
  const c = Math.cos(degrees * DEG);
  const s = Math.sin(degrees * DEG);
  return [[c, -s, 0], [s, c, 0], [0, 0, 1]];
}

// Tilt along the quadrant: carries "straight down" to (sin t, 0, -cos t).
export function tiltY(degrees) {
  const c = Math.cos(degrees * DEG);
  const s = Math.sin(degrees * DEG);
  return [[c, 0, -s], [0, 1, 0], [s, 0, c]];
}

// The full orientation of a molecule on the stand.
//   yaw  : turntable angle
//   tilt : where the carriage sits on the quadrant (0 = stem straight down)
//   spin : rotation of the molecule about its own stem
//   mount: { polar, azimuth } of the stem in the molecule's own frame,
//          polar measured from straight down
// With tilt = mount.polar and spin = 0 the molecule stands in its textbook pose.
export function orientation(yaw, tilt, spin, mount) {
  let R = turnZ(-mount.azimuth);
  R = matMul(transpose(tiltY(mount.polar)), R);
  R = matMul(turnZ(spin), R);
  R = matMul(tiltY(tilt), R);
  R = matMul(turnZ(yaw), R);
  return R;
}

// ---------- the elements used ----------
// radius is the ball radius in world units; fill / ink are the ball colours.

export const ELEMENTS = {
  H: { radius: 9, fill: "#f3f1ea", ink: "#26262a" },
  Be: { radius: 12.5, fill: "#b8d46c", ink: "#26262a" },
  B: { radius: 12.5, fill: "#eab0a2", ink: "#26262a" },
  C: { radius: 13.5, fill: "#3b3b40", ink: "#ffffff" },
  N: { radius: 13.5, fill: "#4a6fe0", ink: "#ffffff" },
  O: { radius: 12.5, fill: "#e0484d", ink: "#ffffff" },
  F: { radius: 11.5, fill: "#a6d98c", ink: "#26262a" },
  P: { radius: 14.5, fill: "#e8933c", ink: "#26262a" },
  S: { radius: 14.5, fill: "#ecc83e", ink: "#26262a" },
  Cl: { radius: 12.5, fill: "#3fae5c", ink: "#ffffff" },
  Br: { radius: 14.5, fill: "#a54a30", ink: "#ffffff" },
  Xe: { radius: 15, fill: "#58b4c8", ink: "#26262a" },
};

// ---------- mounts ----------
// Where the stand's stem enters the central atom, in the molecule's frame.

const MOUNT_BELOW = { polar: 0, azimuth: 0 };
const MOUNT_FIVE = { polar: 55, azimuth: 60 };
const MOUNT_SIX = { polar: 54.7, azimuth: 45 };

// ---------- helpers that build electron-pair lists ----------

function bond(element, direction, order) {
  let kind = "single";
  if (order === 2) {
    kind = "double";
  }
  if (order === "dative") {
    kind = "dative";
  }
  return { type: "bond", element: element, dir: unit(direction), kind: kind };
}

function lone(direction) {
  return { type: "lone", element: null, dir: unit(direction), kind: "lone" };
}

// Polar angle (from the axis) of three bonds spaced 120 degrees apart in
// azimuth, so that the angle between any two of them is `angle`.
//   cos(angle) = 1 - 1.5 sin^2(polar)
function polarForThree(angle) {
  const sinSquared = (1 - Math.cos(angle * DEG)) / 1.5;
  return Math.asin(Math.sqrt(sinSquared)) / DEG;
}

const TETRA = 2 * Math.atan(Math.SQRT2) / DEG; // 109.47...
const NH3_POLAR = polarForThree(107);

// ---------- the molecules ----------
// pairs  : every electron pair (region) around the central atom
// quote  : the bond angles a student should quote, checked by test.mjs
// measure: the two pairs the protractor starts on

export const MOLECULES = [
  {
    id: "BeCl2", formula: "BeCl<sub>2</sub>", central: "Be", regions: 2,
    shape: "Linear", also: "",
    electronShape: "Linear",
    mount: MOUNT_BELOW,
    pairs: [bond("Cl", [1, 0, 0]), bond("Cl", [-1, 0, 0])],
    quote: [180], measure: [0, 1],
    why: "Two bonding pairs and no lone pairs. The two pairs get as far apart as they can, on opposite sides of the beryllium atom.",
  },
  {
    id: "CO2", formula: "CO<sub>2</sub>", central: "C", regions: 2,
    shape: "Linear", also: "",
    electronShape: "Linear",
    mount: MOUNT_BELOW,
    pairs: [bond("O", [1, 0, 0], 2), bond("O", [-1, 0, 0], 2)],
    quote: [180], measure: [0, 1],
    why: "Each C=O double bond counts as one region of electron density. Two regions and no lone pairs give a linear molecule.",
  },
  {
    id: "BF3", formula: "BF<sub>3</sub>", central: "B", regions: 3,
    shape: "Trigonal planar", also: "",
    electronShape: "Trigonal planar",
    mount: MOUNT_BELOW,
    pairs: [bond("F", fromUp(90, 90)), bond("F", fromUp(90, 210)), bond("F", fromUp(90, 330))],
    quote: [120], measure: [1, 2],
    why: "Three bonding pairs and no lone pairs repel equally, so the three bonds lie flat in one plane, 120° apart.",
  },
  {
    id: "SO2", formula: "SO<sub>2</sub>", central: "S", regions: 3,
    shape: "Bent", also: "V-shaped, non-linear, angular",
    electronShape: "Trigonal planar",
    mount: MOUNT_BELOW,
    pairs: [lone([0, 0, 1]), bond("O", fromDown(59.5, 0), 2), bond("O", fromDown(59.5, 180), 2)],
    quote: [119], measure: [1, 2],
    why: "Two S=O double bonds (one region each) and one lone pair. The lone pair repels more strongly than the bonds, closing the angle slightly from 120° to 119°.",
  },
  {
    id: "CH4", formula: "CH<sub>4</sub>", central: "C", regions: 4,
    shape: "Tetrahedral", also: "",
    electronShape: "Tetrahedral",
    mount: MOUNT_BELOW,
    pairs: [bond("H", [0, 0, 1]), bond("H", fromUp(TETRA, 90)), bond("H", fromUp(TETRA, 210)), bond("H", fromUp(TETRA, 330))],
    quote: [109.5], measure: [2, 3],
    why: "Four bonding pairs and no lone pairs repel equally and point to the corners of a tetrahedron, 109.5° apart.",
  },
  {
    id: "NH4+", formula: "NH<sub>4</sub><sup>+</sup>", central: "N", regions: 4,
    shape: "Tetrahedral", also: "",
    electronShape: "Tetrahedral",
    mount: MOUNT_BELOW,
    pairs: [bond("H", [0, 0, 1], "dative"), bond("H", fromUp(TETRA, 90)), bond("H", fromUp(TETRA, 210)), bond("H", fromUp(TETRA, 330))],
    quote: [109.5], measure: [2, 3],
    why: "Ammonia's lone pair forms a dative covalent (coordinate) bond to H⁺, shown by the arrow. Once formed it is the same as the other three bonds, so there are four equal bonding pairs: tetrahedral, 109.5°.",
  },
  {
    id: "NH3", formula: "NH<sub>3</sub>", central: "N", regions: 4,
    shape: "Trigonal pyramidal", also: "pyramidal",
    electronShape: "Tetrahedral",
    mount: MOUNT_BELOW,
    pairs: [lone([0, 0, 1]), bond("H", fromDown(NH3_POLAR, 90)), bond("H", fromDown(NH3_POLAR, 210)), bond("H", fromDown(NH3_POLAR, 330))],
    quote: [107], measure: [2, 3],
    why: "Three bonding pairs and one lone pair. Lone pair–bond pair repulsion is stronger than bond pair–bond pair repulsion, so the bonds are pushed together from 109.5° to 107°.",
  },
  {
    id: "H2O", formula: "H<sub>2</sub>O", central: "O", regions: 4,
    shape: "Bent", also: "V-shaped, non-linear, angular",
    electronShape: "Tetrahedral",
    mount: MOUNT_BELOW,
    pairs: [lone(fromUp(57, 90)), lone(fromUp(57, 270)), bond("H", fromDown(52.25, 0)), bond("H", fromDown(52.25, 180))],
    quote: [104.5], measure: [2, 3],
    why: "Two bonding pairs and two lone pairs. Lone pair–lone pair repulsion is the strongest of all, so the bonds are squeezed to 104.5°: about 2.5° less for each lone pair.",
  },
  {
    id: "PCl5", formula: "PCl<sub>5</sub>", central: "P", regions: 5,
    shape: "Trigonal bipyramidal", also: "trigonal bipyramid",
    electronShape: "Trigonal bipyramidal",
    mount: MOUNT_FIVE,
    pairs: [bond("Cl", [0, 0, 1]), bond("Cl", [0, 0, -1]), bond("Cl", fromUp(90, 0)), bond("Cl", fromUp(90, 120)), bond("Cl", fromUp(90, 240))],
    quote: [90, 120], measure: [0, 2],
    why: "Five bonding pairs and no lone pairs. Three bonds lie in a plane at 120° to each other; the other two point straight up and down, at 90° to that plane.",
  },
  {
    id: "SF4", formula: "SF<sub>4</sub>", central: "S", regions: 5,
    shape: "Seesaw", also: "distorted tetrahedral",
    electronShape: "Trigonal bipyramidal",
    mount: MOUNT_FIVE,
    pairs: [
      bond("F", [-Math.sin(3.45 * DEG), 0, Math.cos(3.45 * DEG)]),
      bond("F", [-Math.sin(3.45 * DEG), 0, -Math.cos(3.45 * DEG)]),
      lone(fromUp(90, 0)),
      bond("F", fromUp(90, 180 - 50.8)),
      bond("F", fromUp(90, 180 + 50.8)),
    ],
    quote: [101.6, 87.8], measure: [3, 4],
    why: "Four bonding pairs and one lone pair. The lone pair takes a position in the middle plane, where it has most room, and pushes all four bonds away from itself. Mark schemes usually accept about 102° and 87°.",
  },
  {
    id: "ClF3", formula: "ClF<sub>3</sub>", central: "Cl", regions: 5,
    shape: "T-shaped", also: "",
    electronShape: "Trigonal bipyramidal",
    mount: MOUNT_FIVE,
    pairs: [
      bond("F", [Math.sin(2.5 * DEG), 0, Math.cos(2.5 * DEG)]),
      bond("F", [Math.sin(2.5 * DEG), 0, -Math.cos(2.5 * DEG)]),
      bond("F", fromUp(90, 0)),
      lone(fromUp(90, 120)),
      lone(fromUp(90, 240)),
    ],
    quote: [87.5], measure: [0, 2],
    why: "Three bonding pairs and two lone pairs. Both lone pairs sit in the middle plane and push the top and bottom bonds towards the third, closing 90° to 87.5°.",
  },
  {
    id: "XeF2", formula: "XeF<sub>2</sub>", central: "Xe", regions: 5,
    shape: "Linear", also: "",
    electronShape: "Trigonal bipyramidal",
    mount: MOUNT_FIVE,
    pairs: [bond("F", [0, 0, 1]), bond("F", [0, 0, -1]), lone(fromUp(90, 0)), lone(fromUp(90, 120)), lone(fromUp(90, 240))],
    quote: [180], measure: [0, 1],
    why: "Two bonding pairs and three lone pairs. The three lone pairs spread round the middle plane 120° apart, leaving the two bonds opposite each other.",
  },
  {
    id: "SF6", formula: "SF<sub>6</sub>", central: "S", regions: 6,
    shape: "Octahedral", also: "",
    electronShape: "Octahedral",
    mount: MOUNT_SIX,
    pairs: [bond("F", [0, 0, 1]), bond("F", [0, 0, -1]), bond("F", [1, 0, 0]), bond("F", [0, 1, 0]), bond("F", [-1, 0, 0]), bond("F", [0, -1, 0])],
    quote: [90], measure: [2, 3],
    why: "Six bonding pairs and no lone pairs point to the corners of an octahedron. Every bond is at 90° to its four neighbours.",
  },
  {
    id: "BrF5", formula: "BrF<sub>5</sub>", central: "Br", regions: 6,
    shape: "Square pyramidal", also: "square-based pyramid",
    electronShape: "Octahedral",
    mount: MOUNT_SIX,
    pairs: [lone([0, 0, 1]), bond("F", [0, 0, -1]), bond("F", fromDown(84.8, 0)), bond("F", fromDown(84.8, 90)), bond("F", fromDown(84.8, 180)), bond("F", fromDown(84.8, 270))],
    quote: [84.8], measure: [1, 2],
    why: "Five bonding pairs and one lone pair. The lone pair pushes the four bonds of the square base away from itself, so the angle to the fifth bond closes from 90° to about 85°.",
  },
  {
    id: "XeF4", formula: "XeF<sub>4</sub>", central: "Xe", regions: 6,
    shape: "Square planar", also: "",
    electronShape: "Octahedral",
    mount: MOUNT_SIX,
    pairs: [lone([0, 0, 1]), lone([0, 0, -1]), bond("F", [1, 0, 0]), bond("F", [0, 1, 0]), bond("F", [-1, 0, 0]), bond("F", [0, -1, 0])],
    quote: [90], measure: [2, 3],
    why: "Four bonding pairs and two lone pairs. The lone pairs sit opposite each other, as far apart as possible, leaving the four bonds flat in a square at 90°.",
  },
];

// ---------- facts worked out from the vectors ----------

export function countOf(molecule, type) {
  let count = 0;
  for (const pair of molecule.pairs) {
    if (pair.type === type) {
      count = count + 1;
    }
  }
  return count;
}

// Every distinct bond angle in a molecule, smallest first, to 0.1 degree.
export function bondAngles(molecule) {
  const found = [];
  for (let i = 0; i < molecule.pairs.length; i++) {
    for (let j = i + 1; j < molecule.pairs.length; j++) {
      const a = molecule.pairs[i];
      const b = molecule.pairs[j];
      if (a.type !== "bond" || b.type !== "bond") {
        continue;
      }
      const angle = Math.round(angleBetween(a.dir, b.dir) * 10) / 10;
      if (!found.includes(angle)) {
        found.push(angle);
      }
    }
  }
  found.sort((p, q) => p - q);
  return found;
}

// Format an angle the way it is quoted: 109.5°, 120°, 104.5°.
export function sayAngle(angle) {
  const rounded = Math.round(angle * 10) / 10;
  let text = rounded.toFixed(1);
  if (text.endsWith(".0")) {
    text = text.slice(0, -2);
  }
  return text + "°";
}
