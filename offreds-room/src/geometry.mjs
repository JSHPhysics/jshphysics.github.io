// The room, drawn once at build time.
// Units: 1 unit is about 2 cm. x runs along the right-hand wall, y along the left-hand wall, z is up.
// The two walls nearest the viewer are cut away. The ceiling is cut away too, apart from one piece.

import * as k from "./vendor/kit/iso-kit.mjs";
import * as G from "./vendor/kit/lathe.mjs";
import { curtainSvg, cupboardDoorSvg, pathThrough } from "./moving.mjs";

export const WIDTH = 640;
export const HEIGHT = 520;

// Room size.
const W = 220;
const D = 190;
const H = 120;

// How far the lower window sash is lifted in each mode. The page eases between them.
export const SASH_NOW = 5;
export const SASH_BEFORE = 25;

const PLINTH = { x: -20, y: -20, w: W + 40, d: D + 40, r: 7 };

export const P = k.fitProjection(
  [...k.boxCorners(PLINTH, -19, 0), [-5, -5, H + 5], [W, -5, H], [-5, D, H]],
  WIDTH,
  HEIGHT,
  { pad: 24 },
);

// ---------- small helpers ----------

const at = (point) => k.iso(point, P);
const S = (paths, style) => k.solidSvg(paths, style);
const L = (d, style) => k.lineSvg(d, style);
const Dots = (points, style) => k.dotsSvg(points, style);

// A box standing on the floor plan (x, y, w, d) from height z, h tall.
function box(x, y, w, d, z, h, style = {}, r = 0.4, bevel = 0) {
  const plan = { x, y, w, d, r };
  return S(k.slabOf(plan, z, h, P, 3, bevel), { tone: "hi", ...style });
}

// A closed outline through 3D points (for frames and panels drawn on a face).
const loop = (points) => pathThrough(k, P, points, true);

// An open line through 3D points.
const line = (points) => pathThrough(k, P, points, false);

// A flat filled shape through 3D points, styled by a CSS class.
const flat = (points, className) => `<path class="${className}" d="${loop(points)}"/>`;

// A rectangle on the left wall's plane (x fixed), given its y and z ranges.
const onLeftWall = (x, y0, y1, z0, z1) => [
  [x, y0, z0],
  [x, y1, z0],
  [x, y1, z1],
  [x, y0, z1],
];

// A rectangle on the right wall's plane (y fixed), given its x and z ranges.
const onRightWall = (y, x0, x1, z0, z1) => [
  [x0, y, z0],
  [x1, y, z0],
  [x1, y, z1],
  [x0, y, z1],
];

// Turn a floor outline about a centre point.
function turned(ring, cx, cy, degrees) {
  const angle = (degrees * Math.PI) / 180;
  const cos = Math.cos(angle);
  const sin = Math.sin(angle);
  return ring.map(([x, y]) => {
    const dx = x - cx;
    const dy = y - cy;
    return [cx + dx * cos - dy * sin, cy + dx * sin + dy * cos];
  });
}

// Wrap markup as one clickable object.
function object(id, label, inner, focusable = true) {
  let extra = ' aria-hidden="true"';
  if (focusable) {
    extra = ` tabindex="0" role="button" aria-label="${label}"`;
  }
  return `<g class="rm-obj" data-obj="${id}"${extra}>${inner}</g>`;
}

// ---------- the stand the model sits on ----------

function plinth() {
  const out = [];
  out.push(`<path class="iso-halo" d="${k.haloOf(PLINTH, -19, 13, P)}"/>`);

  // Four feet, far ones first.
  const feet = k.corners(PLINTH, 18);
  feet.sort((a, b) => k.depthOf([a[0], a[1], 0], P) - k.depthOf([b[0], b[1], 0], P));
  for (const [x, y] of feet) {
    out.push(S(k.cylinder(x, y, 8, -19, 1.6, P, 28), { tone: "lo" }));
    out.push(S(k.cylinder(x, y, 6.2, -17.4, 3.4, P, 28), { tone: "lo" }));
  }

  out.push(S(k.slabOf(PLINTH, -14, 8, P, 8, 1.4), { tone: "lo" }));

  // A screw in each corner of the stand.
  const screws = k.corners(PLINTH, 8);
  out.push(L(screws.map(([x, y]) => k.ring(x, y, 2.2, -6, P, 16)).join(""), { tone: "lo" }));
  out.push(Dots(screws.map(([x, y]) => at([x, y, -6])), { size: 0.55 }));

  // A scale strip along the right-hand margin: one small tick every 5 units (10 cm).
  const strip = { x: W + 6, y: 12, w: 8, d: 160, r: 1 };
  out.push(S(k.slabOf(strip, -6, 0.6, P, 3), { tone: "lo", crease: "none" }));
  const ticks = k.topTicks(strip.y + 5, strip.y + strip.d - 5, 5, 5, strip.x, -5.4, [2.2, 4], P, "y");
  out.push(L(ticks.minor, { tone: "lo" }));
  out.push(L(ticks.major, { tone: "mid" }));
  out.push(Dots([at([strip.x + 6, strip.y + 2.5, -5.4]), at([strip.x + 6, strip.y + strip.d - 2.5, -5.4])], { size: 0.45 }));

  // A label plate on the front margin, with rule lines standing for engraved text.
  const plate = { x: 28, y: D + 7, w: 56, d: 9, r: 1 };
  out.push(S(k.slabOf(plate, -6, 0.6, P, 3), { tone: "lo", crease: "none" }));
  const rules = [2.4, 4.5, 6.6]
    .map((offset) => k.lineOnTop([plate.x + 6, plate.y + offset], [plate.x + plate.w - 12 - offset * 2, plate.y + offset], -5.4, P))
    .join("");
  out.push(L(rules, { tone: "lo", free: true }));
  out.push(Dots([at([plate.x + 2.6, plate.y + 4.5, -5.4]), at([plate.x + plate.w - 2.6, plate.y + 4.5, -5.4])], { size: 0.45 }));

  return out.join("");
}

// ---------- floor and walls ----------

function floor() {
  const out = [];
  const slab = { x: -5, y: -5, w: W + 5, d: D + 5, r: 0.5 };
  out.push(S(k.slabOf(slab, -6, 6, P, 2, 0.8), { tone: "mid" }));

  // Narrow floorboards, each running from the back wall to the cut edge.
  let boards = "";
  for (let y = 8; y < D; y += 8) {
    boards += k.lineOnTop([0, y], [W, y], 0, P);
  }
  out.push(L(boards, { tone: "faint" }));
  return out.join("");
}

function walls() {
  const out = [];
  const left = { x: -5, y: -5, w: 5, d: D + 5, r: 0.3 };
  const right = { x: 0, y: -5, w: W, d: 5, r: 0.3 };

  // A cornice line near the top of each wall, wrapping onto the cut end.
  const leftCornice = L(k.sideSeam(left, H - 7, P, 2), { tone: "faint" });
  const rightCornice = L(k.sideSeam(right, H - 7, P, 2), { tone: "faint" });
  out.push(S(k.slabOf(left, 0, H, P, 2, 0.8), { tone: "mid", inner: leftCornice }));
  out.push(S(k.slabOf(right, 0, H, P, 2, 0.8), { tone: "mid", inner: rightCornice }));

  // Skirting boards. The left one stops either side of the door.
  out.push(box(0, 0, 1.2, 146, 0, 6, { tone: "mid" }, 0.2));
  out.push(box(0, 186, 1.2, 4, 0, 6, { tone: "mid" }, 0.2));
  out.push(box(1.2, 0, W - 1.2, 1.2, 0, 6, { tone: "mid" }, 0.2));
  return out.join("");
}

// ---------- things on the right-hand wall ----------

function picture() {
  const out = [];
  // The frame stands 1.5 proud of the wall.
  out.push(box(80, 0, 30, 1.5, 64, 30, {}, 0.2));
  // The mount inside the frame.
  out.push(L(loop(onRightWall(1.55, 83, 107, 67, 91)), { tone: "mid" }));

  // Three irises: a stem rising from the bottom of the mount to a flower head.
  const stems = [
    [[90, 67], [89.2, 76], [88, 82]],
    [[95, 67], [95.4, 78], [95, 86]],
    [[100, 67], [101, 75], [102.4, 80.5]],
  ];
  let stemPaths = "";
  const heads = [];
  for (const stem of stems) {
    const points = stem.map(([x, z]) => [x, 1.55, z]);
    stemPaths += line(points);
    heads.push(at(points[points.length - 1]));
  }
  out.push(L(stemPaths, { tone: "mid" }));
  out.push(`<g class="rm-iris">${Dots(heads, { size: 1.5, tone: "hi" })}</g>`);
  return out.join("");
}

// The sheet of glass that is missing from the picture frame.
function pictureGlass() {
  const pane = onRightWall(1.7, 83, 107, 67, 91);
  const glint = line([[85, 1.7, 67], [97, 1.7, 91]]) + line([[90, 1.7, 67], [102, 1.7, 91]]);
  return `<path class="rm-pane" d="${loop(pane)}"/>` + L(glint, { tone: "mid" });
}

// A mirror of the kind a room like this would once have had.
function mirror() {
  const out = [];
  out.push(box(126, 0, 22, 1.5, 58, 34, {}, 0.2));
  out.push(`<path class="rm-pane" d="${loop(onRightWall(1.55, 129, 145, 61, 89))}"/>`);
  const glint = line([[131, 1.55, 61], [139, 1.55, 89]]) + line([[135, 1.55, 61], [143, 1.55, 89]]);
  out.push(L(glint, { tone: "mid" }));
  return out.join("");
}

// ---------- things on the left-hand wall ----------

function cupboardBody() {
  const out = [];
  const body = { x: 0, y: 10, w: 22, d: 44, r: 0.5 };
  const plinthLine = L(k.sideSeam(body, 4, P, 3), { tone: "faint" });
  out.push(S(k.slabOf(body, 0, 100, P, 3, 0.6), { tone: "hi", inner: plinthLine }));
  out.push(box(0, 9, 23.5, 46, 100, 3, {}, 0.5, 0.5));

  // The inside, seen through the door opening: back, one side and the floor.
  const opening = onLeftWall(22.05, 12, 52, 6, 97);
  const back = onLeftWall(2, 12, 52, 6, 97);
  const side = [[22, 12, 6], [2, 12, 6], [2, 12, 97], [22, 12, 97]];
  const base = [[22, 12, 6], [22, 52, 6], [2, 52, 6], [2, 12, 6]];

  const inside = [];
  inside.push(`<path class="rm-in rm-in-back" d="${loop(back)}"/>`);
  inside.push(`<path class="rm-in rm-in-side" d="${loop(side)}"/>`);
  inside.push(`<path class="rm-in rm-in-floor" d="${loop(base)}"/>`);
  // A rail across the back with a row of hooks on it.
  // (Looking down into the cupboard, the top of the back wall is hidden, so the rail sits at z 74.)
  inside.push(L(line([[2, 12, 74], [2, 52, 74]]), { tone: "mid" }));
  const hooks = [17, 23, 29, 35, 41].map((y) => at([2, y, 72.4]));
  inside.push(Dots(hooks, { size: 0.8, tone: "hi" }));
  // The scratched message, on the cupboard floor towards the back.
  const scratches = [30, 28, 26]
    .map((y, index) => line([[4.5, y, 6.05], [13 - index * 1.7, y, 6.05]]))
    .join("");
  inside.push(`<g class="rm-message">${L(scratches, { tone: "hi", free: true })}</g>`);

  out.push(`<clipPath id="rm-cupboard-clip"><path d="${loop(opening)}"/></clipPath>`);
  out.push(`<g clip-path="url(#rm-cupboard-clip)">${inside.join("")}</g>`);
  out.push(L(loop(opening), { tone: "mid" }));
  return out.join("");
}

function windowAndCurtains() {
  const out = [];
  // Open air behind everything, so a lifted sash shows a dark gap.
  out.push(flat(onLeftWall(0.1, 66, 126, 46, 100), "rm-air"));
  // The far jamb.
  out.push(box(0, 64, 1.6, 2, 46, 56, {}, 0.2));
  // The fixed upper sash: glass and one glazing bar.
  out.push(`<path class="rm-glass" d="${loop(onLeftWall(0.3, 66.6, 125.4, 73, 99.4))}"/>`);
  out.push(L(line([[0.3, 96, 73], [0.3, 96, 99.4]]), { tone: "mid" }));

  // The lower sash slides up. The page moves this group.
  const sash = [];
  sash.push(box(0.3, 66.6, 1.1, 58.8, 46, 28.5, {}, 0.2));
  sash.push(`<path class="rm-glass" d="${loop(onLeftWall(1.45, 68.6, 123.4, 48, 72.5))}"/>`);
  sash.push(L(line([[1.45, 96, 48], [1.45, 96, 72.5]]), { tone: "mid" }));
  sash.push(Dots([at([1.45, 86, 47]), at([1.45, 106, 47])], { size: 0.6, tone: "hi" }));
  out.push(`<g data-part="sash" transform="${k.translateAlong(P, [0, 0, SASH_NOW])}">${sash.join("")}</g>`);

  // The near jamb, the head and the sill.
  out.push(box(0, 126, 1.6, 2, 46, 56, {}, 0.2));
  out.push(box(0, 64, 1.8, 64, 100, 2, {}, 0.2));
  out.push(box(0, 63, 3.2, 66, 44, 2, {}, 0.3, 0.4));

  // Two curtains. The page redraws these as the air moves them.
  out.push(`<g data-part="curtain-far">${curtainSvg(k, P, 55, 67, 0)}</g>`);
  out.push(`<g data-part="curtain-near">${curtainSvg(k, P, 125, 137, 0)}</g>`);

  // The rod, on two brackets, with a finial at each end.
  out.push(box(0, 59.4, 3.6, 1.2, 104.2, 0.9, { tone: "mid" }, 0.2));
  out.push(box(0, 131.4, 3.6, 1.2, 104.2, 0.9, { tone: "mid" }, 0.2));
  out.push(box(2.8, 52, 1.3, 88, 105, 1.3, {}, 0.5));
  out.push(Dots([at([3.4, 52, 105.6]), at([3.4, 140, 105.6])], { size: 1, tone: "hi" }));
  return out.join("");
}

function door() {
  const out = [];
  // The dark hallway beyond.
  out.push(flat(onLeftWall(0.1, 149, 183, 0, 100), "rm-air"));
  // The far jamb and the head of the frame.
  out.push(box(0, 146, 1.6, 3, 0, 100, {}, 0.2));
  out.push(box(0, 146, 1.8, 40, 100, 3, {}, 0.2));

  // The door itself, standing a little open because it will not shut.
  const ajar = (12 * Math.PI) / 180;
  const hinge = [0.9, 149.2];
  const along = [Math.sin(ajar), Math.cos(ajar)];
  const out2 = [Math.cos(ajar), -Math.sin(ajar)];
  const point = (u, t) => [hinge[0] + along[0] * u + out2[0] * t, hinge[1] + along[1] * u + out2[1] * t];
  const ring = [point(0, 0), point(33.4, 0), point(33.4, 1.5), point(0, 1.5)];
  out.push(S(k.extrude(ring, 0.6, 98.8, P), { tone: "hi" }));

  // Two framed panels and a knob on the face turned to the room.
  const panel = (z0, z1) => {
    const a = point(5, 1.55);
    const b = point(28.4, 1.55);
    return loop([[a[0], a[1], z0], [b[0], b[1], z0], [b[0], b[1], z1], [a[0], a[1], z1]]);
  };
  out.push(L(panel(8, 44) + panel(52, 92), { tone: "lo" }));
  const knob = point(30.6, 1.55);
  out.push(Dots([at([knob[0], knob[1], 48])], { size: 1.1, tone: "hi" }));

  // The near jamb.
  out.push(box(0, 183, 1.6, 3, 0, 100, {}, 0.2));
  return out.join("");
}

function windowSeat() {
  const out = [];
  const seat = { x: 0, y: 62, w: 16, d: 68, r: 0.8 };
  const lid = L(k.sideSeam(seat, 17.5, P, 3), { tone: "faint" });
  out.push(S(k.slabOf(seat, 0, 20, P, 3, 0.6), { tone: "hi", inner: lid }));
  // Three framed panels on the front.
  let panels = "";
  for (const y of [65, 87, 109]) {
    panels += loop(onLeftWall(16.05, y, y + 18, 3, 15));
  }
  out.push(L(panels, { tone: "lo" }));
  return out.join("");
}

function cushion() {
  const out = [];
  const plan = { x: 2.5, y: 85, w: 11.5, d: 22, r: 3 };
  out.push(S(k.slabOf(plan, 20, 3.6, P, 6, 0.5), { tone: "hi" }));
  out.push(L(k.planOutline(k.insetPlan(plan, 1.6), 23.6, P, 6), { tone: "lo" }));
  // The stitched word. It stays hidden until the class reaches chapter 10.
  const word = k.faceTextSvg(k.topMatrix([8.6, 96], 23.6, P, "y"), "FAITH", { size: 3.1, tone: "hi", anchor: "middle" });
  out.push(`<g class="rm-word">${word}</g>`);
  return out.join("");
}

// ---------- things on the floor ----------

function ellipse(cx, cy, rx, ry, count = 56) {
  const ring = [];
  for (let index = 0; index < count; index++) {
    const angle = (index / count) * Math.PI * 2;
    ring.push([cx + Math.cos(angle) * rx, cy + Math.sin(angle) * ry]);
  }
  return ring;
}

function rug() {
  const out = [];
  out.push(S(k.extrude(ellipse(100, 112, 46, 30), 0, 0.9, P), { tone: "hi" }));
  // The braid: one oval inside another, down to the middle.
  let braid = "";
  for (const share of [0.9, 0.78, 0.66, 0.54, 0.42, 0.3, 0.18]) {
    braid += k.onTop(ellipse(100, 112, 46 * share, 30 * share, 44), 0.9, P, true);
  }
  out.push(L(braid, { tone: "lo" }));
  return out.join("");
}

// Sunlight through a four-pane window, lying on the floor and the rug.
function sunlight() {
  const corner = { a: [22, 74], b: [22, 120], c: [78, 136], d: [78, 90] };
  const mix = (p, q, share) => [p[0] + (q[0] - p[0]) * share, p[1] + (q[1] - p[1]) * share];
  const spot = (u, v) => mix(mix(corner.a, corner.d, u), mix(corner.b, corner.c, u), v);
  const spans = [[0, 0.46], [0.54, 1]];
  let panes = "";
  for (const [u0, u1] of spans) {
    for (const [v0, v1] of spans) {
      panes += k.onTop([spot(u0, v0), spot(u1, v0), spot(u1, v1), spot(u0, v1)], 0.95, P, true);
    }
  }
  return `<path class="rm-sun" d="${panes}"/>`;
}

function chair() {
  const out = [];
  // Seat at 84..106 by 4..26, facing into the room.
  const x0 = 84;
  for (const [x, y] of [[x0, 4], [x0 + 19.6, 4], [x0, 23.6], [x0 + 19.6, 23.6]]) {
    out.push(box(x, y, 2.4, 2.4, 0, 20, {}, 0.3));
  }
  // A stretcher between the front legs.
  out.push(box(x0 + 2.4, 24.2, 17.2, 1.2, 7, 1.6, {}, 0.2));
  out.push(box(x0 - 0.6, 3.4, 23.2, 23.2, 20, 2.6, {}, 1.2, 0.5));
  // The back: two posts, three slats and a top rail.
  out.push(box(x0, 4, 2.4, 2.4, 22.6, 24, {}, 0.3));
  for (const x of [x0 + 5.6, x0 + 10, x0 + 14.4]) {
    out.push(box(x, 4.4, 2, 1.4, 22.6, 22, {}, 0.2));
  }
  out.push(box(x0 + 19.6, 4, 2.4, 2.4, 22.6, 24, {}, 0.3));
  out.push(box(x0 - 0.4, 3.8, 22.8, 2.8, 44.6, 4.4, {}, 0.8, 0.4));
  return out.join("");
}

function table() {
  const out = [];
  const x0 = 119;
  for (const [x, y] of [[x0, 6], [x0 + 31.6, 6], [x0, 25.6], [x0 + 31.6, 25.6]]) {
    out.push(box(x, y, 2.4, 2.4, 0, 30, {}, 0.3));
  }
  // The apron under the top, with one shallow drawer in it.
  out.push(box(x0 + 0.6, 6.6, 32.8, 20.8, 29, 4.4, {}, 0.3));
  out.push(L(loop(onRightWall(27.45, x0 + 9, x0 + 25, 30, 32.6)), { tone: "lo" }));
  out.push(Dots([at([x0 + 17, 27.45, 31.3])], { size: 0.7, tone: "hi" }));
  out.push(box(x0 - 2, 4, 38, 26, 33.4, 2.4, {}, 1, 0.6));
  return out.join("");
}

function lamp() {
  const out = [];
  const x = 140;
  const y = 16;
  out.push(S(k.cylinder(x, y, 5, 35.8, 1.8, P, 28, 0.4), { tone: "hi" }));
  out.push(S(k.cylinder(x, y, 1.1, 37.6, 12, P, 14), { tone: "hi", crease: "none" }));
  // A plain cone shade.
  const axis = G.frameOf([x, y, 0], [0, 0, 1], [1, 0, 0], [0, 1, 0]);
  out.push(S(G.solidOf([[49, 8.4], [60.5, 5]], axis, P), { tone: "hi" }));
  return out.join("");
}

function bed() {
  const out = [];
  // Headboard against the wall.
  out.push(box(165, 1.4, 48, 2.8, 0, 46, {}, 1, 0.5));
  out.push(L(loop(onRightWall(4.25, 170, 208, 28, 41)), { tone: "lo" }));
  // Two legs at the foot, then the frame.
  out.push(box(166, 100.6, 3, 3, 0, 10, {}, 0.3));
  out.push(box(209, 100.6, 3, 3, 0, 10, {}, 0.3));
  out.push(box(166, 4.2, 46, 99.6, 10, 5, {}, 0.8));
  // Mattress, then the white cover with its raised flock pattern.
  out.push(box(167, 5, 44, 98, 15, 8.6, {}, 3));
  const cover = { x: 166.4, y: 27, w: 45.2, d: 76.4, r: 3 };
  out.push(S(k.slabOf(cover, 15.6, 9.4, P, 5, 0.6), { tone: "hi" }));
  out.push(L(k.planOutline(k.insetPlan(cover, 3.2), 25, P, 5), { tone: "faint" }));
  out.push(Dots(k.dotGrid(cover.x + 7, cover.y + 7, 6, 11, 6.3, 25, P), { size: 0.4, tone: "lo" }));
  // Pillow.
  const pillow = { x: 171.5, y: 7, w: 35, d: 16, r: 4.5 };
  out.push(S(k.slabOf(pillow, 23.6, 4.6, P, 6, 0.6), { tone: "hi" }));
  out.push(L(k.planOutline(k.insetPlan(pillow, 2), 28.2, P, 6), { tone: "faint" }));
  // Footboard.
  out.push(box(165, 103.8, 48, 2.6, 0, 27, {}, 1, 0.5));
  out.push(L(loop(onRightWall(106.45, 170, 208, 6, 22)), { tone: "lo" }));
  return out.join("");
}

function gloves() {
  const out = [];
  // Each glove: a cuff, a palm, a thumb and four fingers, turned a little so the pair looks dropped.
  const glove = (cx, cy, degrees, thumbSide) => {
    const parts = [];
    const shape = (plan, steps) => turned(k.roundedPlan(plan, steps), cx, cy, degrees);
    const red = { tone: "hi", className: "rm-red" };
    const cuff = shape({ x: cx - 3.3, y: cy - 9.4, w: 6.6, d: 4.4, r: 0.9 }, 3);
    const palm = shape({ x: cx - 3.6, y: cy - 5.4, w: 7.2, d: 7.4, r: 1.4 }, 4);
    let thumbX = cx + 3.2;
    if (thumbSide < 0) {
      thumbX = cx - 5.6;
    }
    const thumb = shape({ x: thumbX, y: cy - 4.2, w: 2.4, d: 5.2, r: 1.1 }, 4);
    parts.push(S(k.extrude(cuff, 25, 1.2, P), red));
    parts.push(S(k.extrude(thumb, 25, 1.3, P), red));
    parts.push(S(k.extrude(palm, 25, 1.5, P), red));
    // Fingers, each a slightly different length.
    const lengths = [5.4, 6.4, 6.8, 5.8];
    for (let index = 0; index < 4; index++) {
      const finger = shape({ x: cx - 3.6 + index * 1.82, y: cy + 1.6, w: 1.74, d: lengths[index], r: 0.8 }, 3);
      parts.push(S(k.extrude(finger, 25, 1.4, P), red));
    }
    return parts.join("");
  };
  out.push(glove(181, 62, -16, 1));
  out.push(glove(196, 68, 20, -1));
  return out.join("");
}

// ---------- the one piece of ceiling that is kept ----------

const ROSE = { x: 137, y: 89, r: 19 };

// The light fitting that once hung from the middle of the wreath.
function chandelier() {
  const out = [];
  const { x, y } = ROSE;
  // Lower finial, hub and the ring that carries the candle cups.
  out.push(S(k.cylinder(x, y, 1.5, 90, 4, P, 14), { tone: "hi" }));
  out.push(S(k.cylinder(x, y, 3.4, 94, 4, P, 20, 0.3), { tone: "hi" }));
  out.push(S(k.cylinder(x, y, 11.5, 96.6, 1.4, P, 44, 0.3), { tone: "hi" }));
  // Six cups round the ring, far ones first.
  const cups = [];
  for (let index = 0; index < 6; index++) {
    const angle = (index / 6) * Math.PI * 2 + 0.3;
    cups.push([x + Math.cos(angle) * 9.6, y + Math.sin(angle) * 9.6]);
  }
  cups.sort((a, b) => k.depthOf([a[0], a[1], 0], P) - k.depthOf([b[0], b[1], 0], P));
  const hubDepth = k.depthOf([x, y, 0], P);
  const stem = S(k.cylinder(x, y, 0.9, 98, 20, P, 12), { tone: "hi", crease: "none" });
  let stemDrawn = false;
  for (const [cx, cy] of cups) {
    const isNearer = k.depthOf([cx, cy, 0], P) > hubDepth;
    if (isNearer && !stemDrawn) {
      // The stem goes in once the cups behind it are down.
      out.push(stem);
      stemDrawn = true;
    }
    out.push(S(k.cylinder(cx, cy, 1.6, 98, 4.6, P, 14), { tone: "hi" }));
  }
  if (!stemDrawn) {
    out.push(stem);
  }
  return out.join("");
}

function ceilingRose() {
  const out = [];
  const { x, y, r } = ROSE;
  out.push(S(k.cylinder(x, y, r, 118, 3, P, 64, 0.8), { tone: "hi" }));

  // The wreath: a ring of leaves, with a bead line outside it.
  out.push(L(k.ring(x, y, r - 2.2, 121, P, 56), { tone: "faint" }));
  let leaves = "";
  const count = 18;
  for (let index = 0; index < count; index++) {
    const angle = (index / count) * Math.PI * 2;
    const cx = x + Math.cos(angle) * 12;
    const cy = y + Math.sin(angle) * 12;
    // A leaf is a small pointed oval lying along the ring, tilted outward.
    const tilt = angle + Math.PI / 2 + 0.5;
    const tip = [Math.cos(tilt) * 2.9, Math.sin(tilt) * 2.9];
    const side = [-Math.sin(tilt) * 1.15, Math.cos(tilt) * 1.15];
    const leaf = [
      [cx - tip[0], cy - tip[1]],
      [cx + side[0], cy + side[1]],
      [cx + tip[0], cy + tip[1]],
      [cx - side[0], cy - side[1]],
    ];
    leaves += k.onTop(leaf, 121, P, true);
  }
  out.push(L(leaves, { tone: "mid" }));
  // The blank, plastered-over centre.
  out.push(L(k.ring(x, y, 6, 121, P, 32), { tone: "lo" }));

  return out.join("");
}

// ---------- put it together, back to front ----------

export function roomSvg() {
  const body = [];
  body.push(plinth());
  body.push(object("floor", "The floor and the sunlight", floor()));
  body.push(walls());

  body.push(object("picture", "The picture", picture()));
  body.push(`<g class="rm-ghost" data-obj="picture" aria-hidden="true">${pictureGlass()}</g>`);
  body.push(`<g class="rm-ghost rm-obj" data-obj="mirror" aria-hidden="true">${mirror()}</g>`);

  body.push(object("cupboard", "The cupboard", cupboardBody()));
  body.push(object("window", "The window and curtains", windowAndCurtains()));
  body.push(object("door", "The door", door()));

  // A soft shadow on the floor, straight under the piece of ceiling, so it reads as high up.
  body.push(`<path class="rm-shadow" d="${k.onTop(k.circleRing(ROSE.x, ROSE.y, ROSE.r, 40), 0, P, true)}"/>`);
  body.push(object("rug", "The rug", rug()));
  body.push(object("floor", "Sunlight on the floor", sunlight(), false));

  body.push(object("cupboard", "The cupboard door", `<g data-part="cupboard-door">${cupboardDoorSvg(k, P, 0)}</g>`, false));
  body.push(object("windowseat", "The window seat and cushion", windowSeat() + cushion()));

  body.push(object("chair", "The chair", chair()));
  body.push(object("table", "The table", table()));
  body.push(object("lamp", "The lamp", lamp()));
  body.push(object("bed", "The bed", bed()));
  body.push(object("gloves", "The red gloves", gloves()));

  body.push(`<g class="rm-ghost rm-obj" data-obj="ceiling" aria-hidden="true">${chandelier()}</g>`);
  body.push(object("ceiling", "The ceiling wreath", ceilingRose()));

  return k.figureSvg({
    width: WIDTH,
    height: HEIGHT,
    label:
      "A cutaway model of Offred's room from chapter 2 of The Handmaid's Tale: a chair, a table and a lamp, a picture, a single bed with red gloves on it, a braided rug, a window with a seat and cushion, a cupboard, a door standing ajar, and one piece of ceiling carrying a plaster wreath with a blank centre.",
    body,
  });
}
