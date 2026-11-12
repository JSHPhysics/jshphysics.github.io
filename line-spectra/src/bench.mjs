// The spectroscope bench of Fig 1, drawn once with the Anatomy kit (Node only).
// World units: x and y on the bench top, z up.  Light travels in the -y direction:
// lamp (y = +190) -> gas tube -> slit -> lens -> grating (y = 0) -> screen (y = -130).

import * as k from "/mnt/skills/plugins/anatomy/kit/iso-kit.mjs";
import * as G from "/mnt/skills/plugins/anatomy/kit/lathe.mjs";
import { GRATING_LINES_PER_MM } from "./data.mjs";

export const WIDTH = 860;
export const HEIGHT = 540;

// Heights and positions that the page script also needs.
export const BEAM_Z = 62; // height of the light path above the bench top
export const SCREEN_Y = -130; // the lit face of the screen
export const SCREEN_X = [-18, 166]; // left and right edges of the dark panel
export const SCREEN_Z = [36, 92]; // bottom and top edges of the dark panel
export const BAND_Z = [44, 84]; // bottom and top of the spectrum on the panel
export const TUBE_Y = [144, 108]; // the two ends of the glass tube
export const TUBE_PARK = 58; // how far the tube slides sideways (in x) to leave the beam
export const LAMP_FRONT_Y = 170; // where light leaves the lamp house
export const SLIT_Y = 80;
export const LENS_Y = 40;

// The T-shaped base: a long bar under the rail and a cross bar under the screen.
const BASE_TOP = 0;
const BASE_H = 10;
const FOOT_H = 5;
const BAR = { x: -34, y: -146, w: 68, d: 380, r: 0 };
const CROSS = { x: -34, y: -146, w: 214, d: 30, r: 0 };
const RAIL = { x: -8, y: -112, w: 16, d: 340, r: 1.5 };
const RAIL_H = 5;

const P = k.fitProjection(
  [...k.boxCorners(BAR, -BASE_H - FOOT_H, 0), ...k.boxCorners(CROSS, -BASE_H - FOOT_H, 0), [-24, -133, 100], [172, -133, 100], [0, 210, 98]],
  WIDTH,
  HEIGHT,
  { pad: 26 },
);

const at = (point) => k.iso(point, P);
const S = (paths, style) => k.solidSvg(paths, style);
const L = (d, style) => k.lineSvg(d, style);
const D = (points, style) => k.dotsSvg(points, style);

// A closed outline through 3D points (closed, so it has no loose ends).
function loop(points) {
  const flat = points.map(at);
  let d = "";
  flat.forEach((point, index) => {
    d += (index === 0 ? "M" : "L") + point[0].toFixed(1) + " " + point[1].toFixed(1);
  });
  return d + "Z";
}

// A rectangle on a face that looks along +y (a plane of constant y).
function faceRect(y, x0, x1, z0, z1) {
  return loop([
    [x0, y, z0],
    [x1, y, z0],
    [x1, y, z1],
    [x0, y, z1],
  ]);
}

// Sort floor points from far to near, so nearer ones are painted last.
function byDepth(points) {
  return [...points].sort((a, b) => k.depthOf([a[0], a[1], 0], P) - k.depthOf([b[0], b[1], 0], P));
}

// ---------- base ----------
function base() {
  const out = [];
  out.push(`<path class="iso-halo" d="${k.haloOf(BAR, -BASE_H - FOOT_H, BASE_H, P)}"/>`);
  out.push(`<path class="iso-halo" d="${k.haloOf(CROSS, -BASE_H - FOOT_H, BASE_H, P)}"/>`);
  const feet = [
    [-22, -134],
    [22, -128],
    [168, -134],
    [168, -128],
    [-22, 222],
    [22, 222],
    [-22, 50],
    [22, 50],
  ];
  for (const [x, y] of byDepth(feet)) {
    out.push(S(k.cylinder(x, y, 7, -BASE_H - FOOT_H, 1.6, P, 24), { tone: "lo" }));
    out.push(S(k.cylinder(x, y, 5.4, -BASE_H - FOOT_H + 1.6, FOOT_H - 1.6, P, 24), { tone: "mid" }));
  }
  // One T-shaped plate.
  const ring = [
    [-34, -146],
    [180, -146],
    [180, -116],
    [34, -116],
    [34, 234],
    [-34, 234],
  ];
  out.push(S(k.extrude(ring, -BASE_H, BASE_H, P, { convex: false, bevel: 1.2 }), { tone: "mid" }));
  // A groove that follows the T, 5 in from the edge.
  const groove = [
    [-29, -141],
    [175, -141],
    [175, -121],
    [29, -121],
    [29, 229],
    [-29, 229],
  ];
  out.push(L(k.onTop(groove, BASE_TOP, P, true), { tone: "lo" }));
  // Screws at the corners.
  const screws = [
    [-24, -136],
    [170, -136],
    [170, -126],
    [-24, 224],
    [24, 224],
    [24, -108],
  ];
  out.push(L(screws.map(([x, y]) => k.ring(x, y, 2.2, BASE_TOP, P, 14)).join(""), { tone: "lo" }));
  out.push(D(screws.map(([x, y]) => at([x, y, BASE_TOP])), { size: 0.5 }));
  // A ruler strip along the near edge of the long bar.
  const strip = { x: 17, y: -104, w: 7, d: 320, r: 1 };
  out.push(S(k.slabOf(strip, BASE_TOP, 0.6, P, 3), { tone: "lo", crease: "none" }));
  const ticks = k.topTicks(strip.y + 4, strip.y + strip.d - 4, 4, 5, strip.x + 0.6, 0.6, [1.6, 2.8], P, "y");
  out.push(L(ticks.minor, { tone: "lo" }), L(ticks.major, { tone: "mid" }));
  out.push(D([at([strip.x + 3.5, strip.y + 2, 0.6]), at([strip.x + 3.5, strip.y + strip.d - 2, 0.6])], { size: 0.45 }));
  // A maker's plate on the cross bar: its rule lines stand for printed text.
  const plate = { x: 92, y: -140, w: 40, d: 12, r: 1.5 };
  out.push(S(k.slabOf(plate, BASE_TOP, 0.8, P, 4), { tone: "lo", crease: "none" }));
  out.push(L(k.planOutline(k.insetPlan(plate, 1.6), 0.8, P, 4), { tone: "faint" }));
  out.push(L(k.lineOnTop([96, -136.5], [124, -136.5], 0.8, P), { tone: "lo", free: true }));
  out.push(L(k.lineOnTop([96, -134], [116, -134], 0.8, P), { tone: "lo", free: true }));
  out.push(L(k.lineOnTop([96, -131.5], [120, -131.5], 0.8, P), { tone: "lo", free: true }));
  out.push(D([at([129, -138, 0.8]), at([129, -130, 0.8])], { size: 0.4 }));
  return out.join("");
}

// ---------- rail ----------
function farStop() {
  const out = [];
  out.push(S(k.slabOf({ x: -11, y: -117, w: 22, d: 5, r: 1.2 }, BASE_TOP, 8, P, 3, 0.5), { tone: "mid" }));
  out.push(D([at([-7, -114.5, 8]), at([7, -114.5, 8])], { size: 0.45 }));
  return out.join("");
}
function rail() {
  const out = [];
  out.push(S(k.slabOf(RAIL, BASE_TOP, RAIL_H, P, 3, 0.5), { tone: "mid" }));
  // A centre groove from stop to stop.
  out.push(L(k.lineOnTop([0, -112], [0, 228], RAIL_H, P), { tone: "faint" }));
  return out.join("");
}
function nearStop() {
  const out = [];
  out.push(S(k.slabOf({ x: -11, y: 228, w: 22, d: 5, r: 1.2 }, BASE_TOP, 8, P, 3, 0.5), { tone: "mid" }));
  out.push(D([at([-7, 230.5, 8]), at([7, 230.5, 8])], { size: 0.45 }));
  return out.join("");
}

// A rider that clamps to the rail at y = centre, with a thumb screw, a collar and a post up to postTop.
function rider(centre, postTop) {
  const out = [];
  const plan = { x: -13, y: centre - 9, w: 26, d: 18, r: 2 };
  out.push(S(k.slabOf(plan, RAIL_H, 6, P, 4, 0.5), { tone: "mid" }));
  out.push(D([at([-9.5, centre + 6, RAIL_H + 6]), at([9.5, centre + 6, RAIL_H + 6]), at([-9.5, centre - 6, RAIL_H + 6]), at([9.5, centre - 6, RAIL_H + 6])], { size: 0.4, tone: "lo" }));
  // Thumb screw on a lug at the near side.
  out.push(S(k.slabOf({ x: 13, y: centre - 3, w: 6.5, d: 6, r: 1 }, RAIL_H, 3, P, 2), { tone: "mid", crease: "none" }));
  out.push(S(k.cylinder(16.4, centre, 2.7, RAIL_H + 3, 5, P, 18), { tone: "mid" }));
  out.push(L(k.knurl(16.4, centre, 2.7, RAIL_H + 3, RAIL_H + 8, 16, P), { tone: "lo" }));
  if (postTop > 0) {
    out.push(S(k.cylinder(0, centre, 4.6, RAIL_H + 6, 3, P, 24), { tone: "mid" }));
    out.push(S(k.cylinder(0, centre, 2.6, RAIL_H + 9, postTop - RAIL_H - 9, P, 20), { tone: "mid", crease: "none" }));
    out.push(L(k.sideArc(0, centre, 2.6, RAIL_H + 15, P, 12), { tone: "faint" }));
  }
  return out.join("");
}

// ---------- screen ----------
function screen() {
  const out = [];
  const board = { x: -24, y: SCREEN_Y - 3, w: 196, d: 3, r: 1 };
  // Two feet and posts.
  for (const x of [-12, 160]) {
    out.push(S(k.slabOf({ x: x - 7, y: -142, w: 14, d: 21, r: 2 }, BASE_TOP, 4, P, 3, 0.4), { tone: "mid" }));
    out.push(D([at([x, -124.5, 4])], { size: 0.45 }));
    out.push(S(k.cylinder(x, -136.5, 2.6, 4, 24, P, 18), { tone: "mid", crease: "none" }));
  }
  out.push(S(k.slabOf(board, 26, 72, P, 3, 0.5), { tone: "mid" }));
  // The dark panel the light lands on, with a scale hanging from its lower edge.
  out.push(`<path class="sp-panel" d="${faceRect(SCREEN_Y, SCREEN_X[0], SCREEN_X[1], SCREEN_Z[0], SCREEN_Z[1])}"/>`);
  const ticks = k.sideTicks(SCREEN_X[0] + 2, SCREEN_X[1] - 2, 4, 5, SCREEN_Y, SCREEN_Z[0], [1.6, 2.8], P);
  out.push(L(ticks.minor, { tone: "lo" }), L(ticks.major, { tone: "mid" }));
  out.push(D([at([-21, SCREEN_Y, 95]), at([169, SCREEN_Y, 95]), at([-21, SCREEN_Y, 29]), at([169, SCREEN_Y, 29])], { size: 0.45 }));
  return out.join("");
}

// ---------- grating on its turntable ----------
function grating() {
  const out = [];
  out.push(S(k.slabOf({ x: -22, y: -22, w: 44, d: 44, r: 6 }, RAIL_H, 4, P, 6, 0.5), { tone: "mid" }));
  out.push(S(k.cylinder(0, 0, 19, RAIL_H + 4, 5, P, 56, 0.6), { tone: "mid" }));
  out.push(L(k.knurl(0, 0, 19, RAIL_H + 6, RAIL_H + 9, 70, P, 0.3), { tone: "lo" }));
  out.push(L(k.sideArc(0, 0, 19, RAIL_H + 6, P, 36), { tone: "faint" }));
  const top = RAIL_H + 9;
  out.push(L(k.ring(0, 0, 17, top, P, 56), { tone: "lo" }));
  const ticks = k.radialTicks(0, 0, 17, 72, 6, top, [1.2, 2.6], P);
  out.push(L(ticks.minor, { tone: "lo" }), L(ticks.major, { tone: "mid" }));
  // The frame that holds the grating, standing across the beam.
  const frame = { x: -16, y: -1.5, w: 32, d: 3, r: 1 };
  out.push(S(k.slabOf({ x: -17, y: -3.5, w: 34, d: 7, r: 1.5 }, top, 3, P, 3, 0.4), { tone: "mid" }));
  out.push(S(k.slabOf(frame, top + 3, 88 - top - 3, P, 3, 0.4), { tone: "hi" }));
  // The ruled window: every ruling runs from the bottom edge of the window to the top edge.
  const faceY = 1.5;
  const rulings = [];
  for (let x = -10; x <= 10.01; x += 1) {
    rulings.push(k.segment([x, faceY, 46], [x, faceY, 78], P));
  }
  out.push(`<path class="sp-window" d="${faceRect(faceY, -11, 11, 46, 78)}"/>`);
  out.push(L(rulings.join(""), { tone: "lo" }));
  out.push(L(faceRect(faceY, -11, 11, 46, 78), { tone: "hi" }));
  out.push(D([at([-13.5, faceY, 85]), at([13.5, faceY, 85]), at([-13.5, faceY, 21]), at([13.5, faceY, 21])], { size: 0.4 }));
  out.push(k.faceTextSvg(k.sideMatrix([0, faceY], 36, P, "left"), GRATING_LINES_PER_MM + " lines/mm", { size: 2.7, tone: "mid", anchor: "middle" }));
  return out.join("");
}

// ---------- lens ----------
function lens() {
  const out = [];
  out.push(rider(LENS_Y, 40));
  const holder = { x: -15, y: LENS_Y - 1.5, w: 30, d: 3, r: 2 };
  out.push(S(k.slabOf(holder, 40, 46, P, 4, 0.4), { tone: "mid" }));
  const faceY = LENS_Y + 1.5;
  out.push(`<path class="sp-glass" d="${k.sideRing([0, faceY, BEAM_Z], 11, "y", P, 40)}"/>`);
  out.push(L(k.sideRing([0, faceY, BEAM_Z], 12.4, "y", P, 40), { tone: "mid" }));
  out.push(L(k.sideRing([0, faceY, BEAM_Z], 11, "y", P, 40), { tone: "hi" }));
  const clips = [];
  for (const angle of [90, 210, 330]) {
    const radians = (angle * Math.PI) / 180;
    clips.push(at([Math.cos(radians) * 13.6, faceY, BEAM_Z + Math.sin(radians) * 13.6]));
  }
  out.push(D(clips, { size: 0.5 }));
  return out.join("");
}

// ---------- slit ----------
function slit() {
  const out = [];
  out.push(rider(SLIT_Y, 38));
  const plate = { x: -14, y: SLIT_Y - 1.5, w: 28, d: 3, r: 1 };
  out.push(S(k.slabOf(plate, 38, 50, P, 3, 0.4), { tone: "mid" }));
  const faceY = SLIT_Y + 1.5;
  // The slit itself is a closed, very narrow slot.
  out.push(`<path class="sp-slot" d="${faceRect(faceY, -0.7, 0.7, 50, 74)}"/>`);
  // Two jaw plates with their screws.
  out.push(L(faceRect(faceY, -9, -0.7, 47, 77), { tone: "lo" }));
  out.push(L(faceRect(faceY, 0.7, 9, 47, 77), { tone: "lo" }));
  out.push(D([at([-5, faceY, 74]), at([5, faceY, 74]), at([-5, faceY, 50]), at([5, faceY, 50])], { size: 0.4 }));
  out.push(D([at([-11.5, faceY, 85]), at([11.5, faceY, 85])], { size: 0.45 }));
  return out.join("");
}

// ---------- gas tube on its slide ----------
// The fixed part: a rider carrying a bar that sticks out sideways for the tube to slide along.
function tubeSlide() {
  const out = [];
  const centre = (TUBE_Y[0] + TUBE_Y[1]) / 2;
  out.push(rider(centre, 0));
  const bar = { x: -14, y: centre - 5, w: 92, d: 10, r: 1.5 };
  out.push(S(k.slabOf(bar, RAIL_H + 6, 4, P, 3, 0.4), { tone: "mid" }));
  out.push(L(k.lineOnTop([-14, centre], [78, centre], RAIL_H + 10, P), { tone: "faint" }));
  out.push(S(k.slabOf({ x: 75, y: centre - 6, w: 3, d: 12, r: 1 }, RAIL_H + 6, 7, P, 2), { tone: "mid" }));
  return out.join("");
}
// The moving part, built with the tube in the beam.  Returns the markup and the tube's outline for the glow.
function tubeCarriage() {
  const out = [];
  const centre = (TUBE_Y[0] + TUBE_Y[1]) / 2;
  const top = RAIL_H + 10;
  out.push(S(k.slabOf({ x: -11, y: centre - 8, w: 22, d: 16, r: 2 }, top, 4, P, 3, 0.4), { tone: "mid" }));
  out.push(D([at([-8, centre + 5.5, top + 4]), at([8, centre + 5.5, top + 4])], { size: 0.4, tone: "lo" }));
  out.push(S(k.cylinder(0, centre, 4.4, top + 4, 3, P, 22), { tone: "mid" }));
  out.push(S(k.cylinder(0, centre, 2.6, top + 7, BEAM_Z - 14 - top - 7, P, 18), { tone: "mid", crease: "none" }));
  // A cradle bar under the tube with a clip at each end.
  out.push(S(k.slabOf({ x: -3, y: TUBE_Y[1] + 3, w: 6, d: TUBE_Y[0] - TUBE_Y[1] - 6, r: 1 }, BEAM_Z - 14, 3, P, 2, 0.3), { tone: "mid" }));
  const axis = G.frameAlong([0, TUBE_Y[1], BEAM_Z], [0, 1, 0]);
  const length = TUBE_Y[0] - TUBE_Y[1];
  const farClip = S(k.slabOf({ x: -2.5, y: TUBE_Y[1] + 5, w: 5, d: 2.4, r: 0.6 }, BEAM_Z - 11, 2.6, P, 2), { tone: "mid", crease: "none" });
  const nearClip = S(k.slabOf({ x: -2.5, y: TUBE_Y[0] - 7.4, w: 5, d: 2.4, r: 0.6 }, BEAM_Z - 11, 2.6, P, 2), { tone: "mid", crease: "none" });
  out.push(farClip, nearClip);
  // Far electrode cap, glass, near electrode cap.
  out.push(S(G.disc(-3, 0, 8.6, axis, P), { tone: "mid" }));
  const glass = G.solidOf(
    [
      [0, 7.6],
      [length, 7.6],
    ],
    axis,
    P,
  );
  out.push(S(glass, { tone: "hi", lit: true }));
  out.push(`<path class="sp-glow" data-part="glow" d="${glass.fill}"/>`);
  out.push(L(G.arcOf(axis, 5, 7.6, P) + G.arcOf(axis, length - 5, 7.6, P), { tone: "lo" }));
  out.push(`<g data-part="beam-tube"></g>`);
  out.push(S(G.disc(length, length + 3, 8.6, axis, P), { tone: "mid" }));
  out.push(D([at([0, TUBE_Y[0] + 3, BEAM_Z + 5]), at([0, TUBE_Y[0] + 3, BEAM_Z - 5])], { size: 0.5 }));
  return out.join("");
}

// ---------- lamp house ----------
function lamp() {
  const out = [];
  const centre = 190;
  out.push(rider(centre, 36));
  const box = { x: -18, y: LAMP_FRONT_Y, w: 36, d: 40, r: 4 };
  const seam = k.sideSeam(box, 42, P, 6);
  out.push(S(k.slabOf(box, 36, 54, P, 6, 0.8), { tone: "mid", inner: L(seam, { tone: "faint" }) }));
  // A chimney with three closed vent slots.
  const cap = k.insetPlan(box, 7);
  out.push(S(k.slabOf(cap, 90, 5, P, 4, 0.5), { tone: "mid" }));
  for (const y of [182, 190, 198]) {
    out.push(L(k.planOutline({ x: -7, y: y - 1.2, w: 14, d: 2.4, r: 1.2 }, 95, P, 4), { tone: "lo" }));
  }
  // A round window in the near side: it glows when the lamp is on.
  const side = 18;
  out.push(`<path class="sp-lampwindow" data-part="lamp-window" d="${k.sideRing([side, centre, BEAM_Z], 7, "x", P, 36)}"/>`);
  out.push(L(k.sideRing([side, centre, BEAM_Z], 8.6, "x", P, 36), { tone: "mid" }));
  out.push(L(k.sideRing([side, centre, BEAM_Z], 7, "x", P, 36), { tone: "hi" }));
  const bolts = [];
  for (const angle of [45, 135, 225, 315]) {
    const radians = (angle * Math.PI) / 180;
    bolts.push(at([side, centre + Math.cos(radians) * 10.4, BEAM_Z + Math.sin(radians) * 10.4]));
  }
  out.push(D(bolts, { size: 0.45 }));
  // Rating plate and two terminals on the back.
  const back = LAMP_FRONT_Y + 40;
  out.push(L(faceRect(back, -11, 3, 70, 80), { tone: "lo" }));
  out.push(L(k.segment([-9, back, 77], [1, back, 77], P), { tone: "lo", free: true }));
  out.push(L(k.segment([-9, back, 73.5], [-2, back, 73.5], P), { tone: "lo", free: true }));
  // Terminal block on the base, and the two leads down to it.
  out.push(S(k.slabOf({ x: -30, y: 216, w: 14, d: 12, r: 1.5 }, BASE_TOP, 5, P, 3, 0.4), { tone: "mid" }));
  out.push(k.wireSvg(at([-9, back, 48]), at([-26, 222, 5]), { via: [at([-9, back + 6, 30]), at([-26, 222, 22])], tone: "mid" }));
  out.push(k.wireSvg(at([-3, back, 48]), at([-20, 222, 5]), { via: [at([-3, back + 6, 30]), at([-20, 222, 22])], tone: "mid" }));
  return out.join("");
}

// The whole drawing, back to front.  Empty groups marked data-part are filled in by the page script.
export function benchSvg() {
  const body = [
    base(),
    farStop(),
    rail(),
    screen(),
    `<g data-part="screen-light"></g>`,
    `<g data-part="fan"></g>`,
    grating(),
    `<g data-part="beam-lens-grating"></g>`,
    lens(),
    `<g data-part="beam-slit-lens"></g>`,
    slit(),
    `<g data-part="beam-tube-slit"></g>`,
    tubeSlide(),
    `<g data-part="tube" transform="${k.translateAlong(P, [0, 0, 0])}">${tubeCarriage()}</g>`,
    `<g data-part="beam-open"></g>`,
    `<g data-part="beam-lamp-tube"></g>`,
    lamp(),
    nearStop(),
  ];
  return k.figureSvg({
    width: WIDTH,
    height: HEIGHT,
    label:
      "A spectroscope on an optical bench. From left to right: a lamp house, a glass tube of gas on a sideways slide, a narrow slit, a lens, a diffraction grating on a turntable, and a dark screen. Light from the source passes through the slit and the grating spreads it into its colours across the screen.",
    body,
  });
}

// The page script places light with the same camera: screen = origin + x*ex + y*ey + z*ez.
export function benchCamera() {
  const origin = at([0, 0, 0]);
  const x = at([1, 0, 0]);
  const y = at([0, 1, 0]);
  const z = at([0, 0, 1]);
  return {
    origin,
    ex: [x[0] - origin[0], x[1] - origin[1]],
    ey: [y[0] - origin[0], y[1] - origin[1]],
    ez: [z[0] - origin[0], z[1] - origin[1]],
  };
}
