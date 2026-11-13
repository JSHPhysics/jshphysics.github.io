// Builds molecule-stand.html: one self-contained page.
//   node build.mjs
// The stand (base, turntable, post, tray) is drawn once here with the kit.
// The molecule, the quadrant and the protractor are drawn in the page by live.js.

import { readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "./vendor/kit/iso-kit.mjs";
import * as G from "./vendor/kit/lathe.mjs";
import { kitScript } from "./vendor/scripts/inline-kit.mjs";
import * as M from "./model.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));

// node build.mjs            builds the stand-alone page beside this file
// node build.mjs --site     builds the copy for jshphysics.github.io: link back to
//                           the gallery, 44px touch targets, and writes ../index.html
const SITE = process.argv.includes("--site");

// ---------- dimensions (world units, z up) ----------

const WIDTH = 640;
const HEIGHT = 560;

const PLATE = { x: -104, y: -84, w: 208, d: 168, r: 10 };
const PLATE_H = 10;
const FOOT_H = 5;

const TABLE_R = 54;
const TABLE_TOP = 5;

const CENTRE = [0, 0, 126]; // the central atom
const ARC_R = 66; // radius of the quadrant
const BOND = 46; // centre-to-centre bond length
const POST_TOP = CENTRE[2] - ARC_R - 2.6;

const TRAY = { x: 68, y: -56, w: 30, d: 112, r: 4 };
const TRAY_H = 5;
const TRAY_BALLS = [9, 7, 10, 7, 11];

const RACK_X = -100;

const P = k.fitProjection(
  [
    ...k.boxCorners(PLATE, -PLATE_H - FOOT_H, 0),
    [0, 0, CENTRE[2] + 64],
    [70, 0, CENTRE[2]],
    [-70, 0, CENTRE[2]],
    [0, 70, CENTRE[2]],
    [0, -70, CENTRE[2]],
  ],
  WIDTH,
  HEIGHT,
  { pad: 22 },
);

const at = (point) => k.iso(point, P);
const S = (paths, style) => k.solidSvg(paths, style);
const L = (d, style) => k.lineSvg(d, style);
const D = (points, style) => k.dotsSvg(points, style);
const byDepth = (points) => [...points].sort((a, b) => k.depthOf([a[0], a[1], 0], P) - k.depthOf([b[0], b[1], 0], P));

// ---------- the static parts ----------

function plate() {
  const out = [`<path class="iso-halo" d="${k.haloOf(PLATE, -PLATE_H - FOOT_H, PLATE_H, P)}"/>`];
  // Four feet, each a pad and a stem.
  for (const [x, y] of byDepth(k.corners(PLATE, 22))) {
    out.push(S(k.cylinder(x, y, 8, -PLATE_H - FOOT_H, 1.6, P, 28), { tone: "lo" }));
    out.push(S(k.cylinder(x, y, 6.2, -PLATE_H - FOOT_H + 1.6, FOOT_H - 1.6, P, 28), { tone: "mid" }));
  }
  out.push(S(k.slabOf(PLATE, -PLATE_H, PLATE_H, P, 8, 1.6), { tone: "mid" }));
  out.push(L(k.sideSeam(PLATE, -3, P, 8), { tone: "faint" }));
  // A groove round the top, and a screw in each corner.
  out.push(L(k.planOutline(k.insetPlan(PLATE, 5), 0, P), { tone: "lo" }));
  const screws = k.corners(PLATE, 11);
  out.push(L(screws.map(([x, y]) => k.ring(x, y, 2.4, 0, P, 16)).join(""), { tone: "lo" }));
  out.push(D(screws.map(([x, y]) => at([x, y, 0])), { size: 0.55 }));
  // The fixed degree scale that the turntable turns inside.
  out.push(L(k.ring(0, 0, TABLE_R + 3, 0, P, 72), { tone: "lo" }));
  const scale = k.radialTicks(0, 0, TABLE_R + 3, 72, 6, 0, [2.4, 4.6], P);
  out.push(L(scale.minor, { tone: "lo" }), L(scale.major, { tone: "mid" }));
  return out.join("");
}

// A rack of spare bond rods at the back.
function rack() {
  const out = [];
  for (const y of [-40, 26]) {
    out.push(S(k.slabOf({ x: RACK_X, y: y, w: 26, d: 5, r: 1.2 }, 0, 3, P, 3, 0.4), { tone: "mid" }));
    out.push(D([at([RACK_X + 2.5, y + 2.5, 3]), at([RACK_X + 23.5, y + 2.5, 3])], { size: 0.4 }));
  }
  for (const x of [RACK_X + 4.5, RACK_X + 9.5, RACK_X + 14.5, RACK_X + 19.5]) {
    out.push(S(k.slabOf({ x: x, y: -50, w: 3, d: 90, r: 1.4 }, 3, 3, P, 3), { tone: "hi", crease: "lo" }));
  }
  return out.join("");
}

// A bull's-eye level in the far corner.
function level() {
  const out = [];
  const x = PLATE.x + 40;
  const y = PLATE.y + 16;
  out.push(S(k.cylinder(x, y, 8, 0, 3, P, 36, 0.5), { tone: "mid" }));
  out.push(L(k.ring(x, y, 5.6, 3, P, 32), { tone: "lo" }));
  out.push(L(k.ring(x, y, 2.2, 3, P, 20), { tone: "mid" }));
  out.push(D([at([x + 0.6, y - 0.4, 3])], { size: 0.7, tone: "hi" }));
  return out.join("");
}

function turntable() {
  const out = [];
  out.push(S(k.cylinder(0, 0, TABLE_R, 0, TABLE_TOP, P, 72, 1), { tone: "hi", crease: "lo" }));
  out.push(L(k.knurl(0, 0, TABLE_R, 1.2, TABLE_TOP, 150, P, 0.3), { tone: "lo" }));
  out.push(L(k.sideArc(0, 0, TABLE_R, 1.2, P, 60), { tone: "faint" }));
  out.push(L(k.ring(0, 0, TABLE_R - 4, TABLE_TOP, P, 72), { tone: "lo" }));
  out.push(L(k.ring(0, 0, TABLE_R - 15, TABLE_TOP, P, 72), { tone: "faint" }));
  out.push(L(k.ring(0, 0, 20, TABLE_TOP, P, 48), { tone: "faint" }));
  // Hub, collar with a grub screw, and the post.
  out.push(S(k.cylinder(0, 0, 13, TABLE_TOP, 4, P, 40, 0.6), { tone: "mid" }));
  const bolts = [0, 1, 2, 3, 4, 5].map((index) => {
    const angle = (index / 6) * Math.PI * 2 + 0.3;
    return at([Math.cos(angle) * 9.6, Math.sin(angle) * 9.6, TABLE_TOP + 4]);
  });
  out.push(D(bolts, { size: 0.45 }));
  out.push(S(k.cylinder(0, 0, 6.5, TABLE_TOP + 4, 7, P, 32, 0.4), { tone: "mid" }));
  out.push(L(k.knurl(0, 0, 6.5, TABLE_TOP + 4, TABLE_TOP + 11, 30, P, 0.3), { tone: "lo" }));
  out.push(S(k.cylinder(0, 0, 3, TABLE_TOP + 11, POST_TOP - 8 - TABLE_TOP - 11, P, 28), { tone: "mid", crease: "none" }));
  out.push(L([30, 42].map((z) => k.sideArc(0, 0, 3, z, P, 16)).join(""), { tone: "faint" }));
  // The clamp that holds the foot of the quadrant.
  out.push(S(k.cylinder(0, 0, 5.4, POST_TOP - 8, 8, P, 32, 0.4), { tone: "mid" }));
  out.push(L(k.sideArc(0, 0, 5.4, POST_TOP - 4, P, 20), { tone: "lo" }));
  return out.join("");
}

// A tray of spare atoms at the front.
function tray() {
  const out = [];
  out.push(S(k.slabOf(TRAY, 0, TRAY_H, P, 5, 0.8), { tone: "mid" }));
  out.push(L(k.planOutline(k.insetPlan(TRAY, 3), TRAY_H, P, 5), { tone: "faint" }));
  out.push(D(k.corners(TRAY, 3).map(([x, y]) => at([x, y, TRAY_H])), { size: 0.4 }));
  const x = TRAY.x + TRAY.w / 2;
  TRAY_BALLS.forEach((radius, index) => {
    const y = TRAY.y + 14 + index * 21;
    out.push(L(k.ring(x, y, radius * 0.8, TRAY_H, P, 28), { tone: "lo" }));
    out.push(S(G.sphereOf([x, y, TRAY_H + radius * 0.82], radius, P), { tone: "hi" }));
  });
  return out.join("");
}

// A ruler strip along the front-left edge and a brake knob at the front corner.
function trim() {
  const out = [];
  const strip = { x: -84, y: PLATE.y + PLATE.d - 13, w: 124, d: 7, r: 1 };
  out.push(S(k.slabOf(strip, 0, 0.6, P, 3), { tone: "lo", crease: "none" }));
  const ticks = k.topTicks(strip.x + 4, strip.x + strip.w - 4, 4, 5, strip.y + 0.8, 0.6, [2, 3.6], P);
  out.push(L(ticks.minor, { tone: "lo" }), L(ticks.major, { tone: "mid" }));
  out.push(D([at([strip.x + 2, strip.y + 3.5, 0.6]), at([strip.x + strip.w - 2, strip.y + 3.5, 0.6])], { size: 0.45 }));
  const knob = [54, PLATE.y + PLATE.d - 14];
  out.push(S(k.cylinder(knob[0], knob[1], 4, 0, 2, P, 24), { tone: "mid" }));
  out.push(S(k.cylinder(knob[0], knob[1], 7, 2, 6, P, 36, 0.5), { tone: "mid" }));
  out.push(L(k.knurl(knob[0], knob[1], 7, 2, 8, 40, P), { tone: "lo" }));
  out.push(L(k.lineOnTop([knob[0], knob[1]], [knob[0] - 7, knob[1]], 8, P), { tone: "hi" }));
  out.push(D([at([knob[0], knob[1], 8])], { size: 0.5, tone: "hi" }));
  return out.join("");
}

// ---------- ball colours ----------

function mixHex(hex, other, share) {
  const parts = [1, 3, 5].map((index) => {
    const a = parseInt(hex.slice(index, index + 2), 16);
    const b = parseInt(other.slice(index, index + 2), 16);
    return Math.round(a + (b - a) * share).toString(16).padStart(2, "0");
  });
  return "#" + parts.join("");
}

function gradients() {
  const out = [];
  for (const [name, data] of Object.entries(M.ELEMENTS)) {
    out.push(
      `<radialGradient id="mk-${name}" cx="0.36" cy="0.3" r="0.8">` +
        `<stop offset="0" stop-color="${mixHex(data.fill, "#ffffff", 0.55)}"/>` +
        `<stop offset="0.45" stop-color="${data.fill}"/>` +
        `<stop offset="1" stop-color="${mixHex(data.fill, "#000000", 0.38)}"/>` +
        `</radialGradient>`,
    );
  }
  return `<defs>${out.join("")}</defs>`;
}

// ---------- the figure ----------

const svg = k.figureSvg({
  width: WIDTH,
  height: HEIGHT,
  label:
    "A ball-and-stick molecule held on a stand. The stand has a turntable, a post and a quarter-circle scale along which the molecule tilts. Lone pairs are shown as lobes with two electrons. A protractor arc between two bonds shows the bond angle.",
  body: [gradients(), plate(), rack(), level(), turntable(), tray(), trim(), `<g data-part="live" class="mk"></g>`],
});

// ---------- the panel beside the figure ----------

function moleculeButtons() {
  const groups = [];
  for (const regions of [2, 3, 4, 5, 6]) {
    const buttons = M.MOLECULES.filter((entry) => entry.regions === regions)
      .map((entry) => `<button type="button" class="chip" data-molecule="${entry.id}" aria-pressed="false">${entry.formula}</button>`)
      .join("");
    groups.push(`<div class="chip-row"><span class="chip-label">${regions} electron pairs</span><span class="chips">${buttons}</span></div>`);
  }
  return groups.join("");
}

let backLink = "";
if (SITE) {
  backLink = `<a class="site-back" href="../">← All JSHPhysics tools</a>`;
}

const panel = `
<aside class="panel">
  <header class="panel-head">
    ${backLink}
    <p class="eyebrow">A-level chemistry · bonding and structure</p>
    <h1>Shapes of molecules</h1>
  </header>

  <section class="picker" aria-label="Choose a molecule">${moleculeButtons()}</section>

  <section class="facts" aria-live="polite">
    <p class="formula" data-fact="formula"></p>
    <h2 data-fact="shape"></h2>
    <p class="also" data-fact="also"></p>
    <dl>
      <div><dt>Bonding pairs</dt><dd data-fact="bonding"></dd></div>
      <div><dt>Lone pairs</dt><dd data-fact="lone"></dd></div>
      <div><dt>Electron pairs arranged</dt><dd data-fact="arrangement"></dd></div>
      <div><dt>Bond angle</dt><dd data-fact="angles"></dd></div>
    </dl>
    <p class="reading" data-fact="reading"></p>
    <p class="why" data-fact="why"></p>
  </section>

  <section class="controls" aria-label="View controls">
    <label class="slider"><span>Tilt</span><input type="range" min="0" max="90" step="1" data-control="tilt"><output data-value="tilt"></output></label>
    <label class="slider"><span>Spin</span><input type="range" min="-180" max="180" step="1" data-control="spin"><output data-value="spin"></output></label>
    <div class="toggles">
      <label><input type="checkbox" data-toggle="auto"> Turn slowly</label>
      <label><input type="checkbox" data-toggle="lonePairs"> Lone pairs</label>
      <label><input type="checkbox" data-toggle="labels"> Symbols</label>
      <button type="button" class="plain" data-action="reset">Reset view</button>
      <button type="button" class="plain" data-action="theme">Light / dark</button>
    </div>
  </section>
</aside>`;

const card = k.plateHtml({
  fig: "Fig 1",
  title: "Molecule stand",
  hint: "Drag to turn and tilt · tap two atoms to measure",
  readout: "Tetrahedral · 109.5°",
  keys: [],
  caption: "",
  body: `<div class="iso-stage" tabindex="0" role="application" aria-label="Molecule model. Arrow keys turn and tilt it; comma and full stop spin it.">${svg}</div>`,
});

const legend = `
<p class="legend">
  <span><i class="key key-rod"></i>single bond</span>
  <span><i class="key key-double"></i>double bond</span>
  <span><i class="key key-dative"></i>dative (coordinate) bond</span>
  <span><i class="key key-lobe"></i>lone pair</span>
  <span><i class="key key-arc"></i>bond angle</span>
</p>
<p class="note">Electron pairs repel and get as far apart as they can. Repulsion is strongest between two lone pairs, weaker between a lone pair and a bonding pair, and weakest between two bonding pairs. Angles are measured values; exam boards name some shapes differently, so the alternatives are listed under each name.</p>`;

const PAGE_STYLE = readFileSync(join(HERE, "page.css"), "utf8");

let layoutClass = "layout";
if (SITE) {
  layoutClass = "layout site";
}

const body = `<style>${PAGE_STYLE}</style><div class="${layoutClass}"><div class="figure-side">${card}${legend}</div>${panel}</div>`;

// ---------- the page script ----------

const modelSource = readFileSync(join(HERE, "model.mjs"), "utf8").replace(/^export /gm, "");
const liveSource = readFileSync(join(HERE, "live.js"), "utf8");

const script = `
${kitScript()}
const M = (() => {
${modelSource}
return { MOLECULES, ELEMENTS, orientation, matApply, turnZ, angleBetween, rotateAbout, cross, dot, unit, countOf, sayAngle };
})();
{
const P = ${JSON.stringify(P)};
const WIDTH = ${WIDTH};
const HEIGHT = ${HEIGHT};
const CENTRE = ${JSON.stringify(CENTRE)};
const ARC_R = ${ARC_R};
const BOND = ${BOND};
const TABLE_TOP = ${TABLE_TOP};
const TABLE_R = ${TABLE_R};
${liveSource}
}
`;

let html = k.pageHtml({ title: "Shapes of molecules", theme: "light", body: body, script: script, width: 1240 });
const fonts =
  '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>' +
  '<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">';
html = html.replace("</head>", fonts + "</head>");
html = html.replace("<!doctype html>", "<!DOCTYPE html>");

let outFile = join(HERE, "molecule-stand.html");
if (SITE) {
  // The site page carries the site's name, an author line and the gallery's saved theme.
  html = html.replace("<title>Shapes of molecules</title>", "<title>Shapes of molecules · JSHPhysics</title>");
  const meta =
    '<meta name="description" content="A ball-and-stick molecule on a stand that turns and tilts: 15 A-level molecules with shape names, lone pairs and a protractor that measures any bond angle.">' +
    '<meta name="author" content="Joshua Stafford-Haworth (JSHPhysics)">';
  html = html.replace("</head>", meta + "</head>");
  outFile = join(HERE, "..", "index.html");
}
writeFileSync(outFile, html);
console.log("wrote " + outFile, Math.round(html.length / 1024) + " KB");
