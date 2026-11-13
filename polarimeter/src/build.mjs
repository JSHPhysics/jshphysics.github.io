// Builds polarimeter.html: one self-contained page.
//   node build.mjs
// Every part is drawn once here with the kit, in its own group, so the page
// can slide the groups apart (explode) without redrawing them.
// The light beam, the analyser's pointer and the numbered pins are drawn in
// the page by live.js.

import { readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "./vendor/kit/iso-kit.mjs";
import * as G from "./vendor/kit/lathe.mjs";
import { kitScript } from "./vendor/scripts/inline-kit.mjs";
import * as M from "./model.mjs";
import { createScene } from "./scene.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));

// node build.mjs            builds the stand-alone page beside this file
// node build.mjs --site     builds the copy for jshphysics.github.io: link back to
//                           the gallery, 44px touch targets, and writes ../index.html
const SITE = process.argv.includes("--site");

// ---------- checks on the model before drawing ----------

function near(a, b) {
  return Math.abs(a - b) < 1e-9;
}

const sucrose = M.SAMPLES.find((sample) => sample.id === "sucrose");
const checks = [
  near(M.rotation(sucrose, 0.5), 33.25),
  near(M.brightness(0, 0), 0),
  near(M.brightness(90, 0), 1),
  near(M.brightness(33.25, 33.25), 0),
  near(M.brightness(45, 0), 0.5),
];
if (checks.includes(false)) {
  console.log("model checks failed", checks);
  process.exit(1);
}

// ---------- the bench, drawn for the walkthrough's camera ----------

const scene = createScene(k, G);
const WIDTH = scene.WIDTH;
const HEIGHT = scene.HEIGHT;
const PINS = scene.PINS;
const P = scene.baseProjection();
const figureBody = [`<g data-part="scene">${scene.build(P).join("")}</g>`];


const svg = k.figureSvg({
  width: WIDTH,
  height: HEIGHT,
  label:
    "A polarimeter on an optical bench. From left to right: a sodium lamp in a housing, a lens, a polariser, a glass sample tube, a rotating analyser in front of a fixed angle scale, and an eyepiece. A wave shows the light: oscillating in every plane before the polariser, in one plane after it, twisting inside the sample, and reduced or blocked by the analyser.",
  body: figureBody,
});

// ---------- the panel ----------

const sampleButtons = M.SAMPLES.map((sample) => `<button type="button" class="chip" data-sample="${sample.id}" aria-pressed="false">${sample.name}</button>`).join("");

const pinButtons = PINS.map((pin) => `<button type="button" class="pin-chip" data-pin="${pin.family}" aria-pressed="false"><b>${pin.number}</b>${pin.name}</button>`).join("");

let backLink = "";
if (SITE) {
  backLink = `<a class="site-back" href="../">← All JSHPhysics tools</a>`;
}

const panel = `
<aside class="panel">
  <header class="panel-head">
    ${backLink}
    <p class="eyebrow">A-level chemistry · optical isomerism</p>
    <h1>The polarimeter</h1>
  </header>

  <section class="walk" aria-live="polite">
    <p class="walk-count" data-walk="count"></p>
    <h2 data-walk="title"></h2>
    <p class="walk-text" data-walk="text"></p>
    <div class="walk-buttons">
      <button type="button" class="plain" data-walk="back">Back</button>
      <button type="button" class="plain primary" data-walk="next">Next</button>
    </div>
  </section>

  <section class="view">
    <div class="eye" data-eye role="img" aria-label="View through the eyepiece"></div>
    <div class="view-facts">
      <p class="view-label">Through the eyepiece</p>
      <p class="view-number" data-value="brightness"></p>
      <p class="view-hint" data-value="verdict"></p>
    </div>
  </section>

  <section class="bench-controls" aria-label="Controls">
    <div class="chips" role="group" aria-label="Sample in the tube">${sampleButtons}</div>
    <label class="slider"><span>Concentration</span><input type="range" min="0.1" max="1" step="0.05" data-control="concentration"><output data-value="concentration"></output></label>
    <label class="slider"><span>Analyser</span><input type="range" min="-90" max="90" step="0.5" data-control="analyser"><output data-value="analyser"></output></label>
    <div class="row">
      <button type="button" class="plain" data-action="nudge-down" aria-label="Turn the analyser half a degree anticlockwise">− 0.5°</button>
      <button type="button" class="plain" data-action="nudge-up" aria-label="Turn the analyser half a degree clockwise">+ 0.5°</button>
      <button type="button" class="plain" data-action="explode">Take apart</button>
      <button type="button" class="plain" data-action="zoom" aria-pressed="true">Zoom to step</button>
      <button type="button" class="plain" data-action="tilt-up" aria-label="Tilt the bench to look from higher up">Tilt ▲</button>
      <button type="button" class="plain" data-action="tilt-down" aria-label="Tilt the bench to look from lower down">Tilt ▼</button>
      <button type="button" class="plain" data-action="reset-view">Reset view</button>
      <button type="button" class="plain" data-action="theme">Light / dark</button>
    </div>
  </section>

  <section class="sum">
    <math display="block"><mi>α</mi><mo>=</mo><mo>[</mo><mi>α</mi><mo>]</mo><mo>×</mo><mi>l</mi><mo>×</mo><mi>c</mi></math>
    <p class="sum-line" data-value="sum"></p>
    <p class="sum-note" data-value="sample-note"></p>
  </section>
</aside>`;

const card = k.plateHtml({
  fig: "Fig 1",
  title: "Polarimeter",
  hint: "Drag to turn the bench",
  readout: "",
  keys: [],
  caption: "",
  body: `<div class="iso-stage" tabindex="0" role="application" aria-label="Polarimeter. Arrow keys turn and tilt the bench.">${svg}</div>`,
});

const under = `
<div class="pins" role="group" aria-label="Parts">${pinButtons}</div>
<p class="note">The wave shows the direction the light oscillates in, not its true size: real light waves are far too small to see. Positive angles are clockwise as the observer sees them, looking through the eyepiece towards the lamp. The (+) and (−) enantiomers use an example specific rotation of ±60°; the sucrose value is the measured one.</p>`;

const PAGE_STYLE = readFileSync(join(HERE, "page.css"), "utf8");

let layoutClass = "layout";
if (SITE) {
  layoutClass = "layout site";
}
const body = `<style>${PAGE_STYLE}</style><div class="${layoutClass}"><div class="figure-side">${card}${under}</div>${panel}</div>`;

// ---------- the page script ----------

const modelSource = readFileSync(join(HERE, "model.mjs"), "utf8").replace(/^export /gm, "");
const liveSource = readFileSync(join(HERE, "live.js"), "utf8");
const sceneSource = readFileSync(join(HERE, "scene.mjs"), "utf8").replace(/^export /gm, "");
const latheSource = readFileSync(join(HERE, "vendor", "kit", "lathe.mjs"), "utf8")
  .replace(/^import .*$/gm, "")
  .replace(/^export /gm, "");

const script = `
${kitScript()}
const M = (() => {
${modelSource}
return { SAMPLES, TUBE_LENGTH_DM, rotation, amplitudeThrough, brightness, sayAngle };
})();
// The kit's round-part module and the scene builder, so the page can redraw
// the bench from any angle with the same code the build used.
const k = { iso, depthOf, cameraOf, towardViewer, fitProjection, boxCorners, corners, haloOf, slabOf, cylinder, planOutline, insetPlan, ring, lineOnTop, topTicks, sideArc, sideSeam, solidSvg, lineSvg, dotsSvg };
const G = (() => {
${latheSource}
return { frameAlong, disc, ringBand, solidOf, circleOf, spokesOf, ribsOf, pointOf, outlineOf };
})();
const SCENE = (() => {
${sceneSource}
return createScene(k, G);
})();
{
let P = ${JSON.stringify(P)};
const WIDTH = SCENE.WIDTH;
const HEIGHT = SCENE.HEIGHT;
const AXIS_Z = SCENE.AXIS_Z;
const X = SCENE.X;
const MOVES = SCENE.MOVES;
const PINS = SCENE.PINS;
${liveSource}
}
`;

let html = k.pageHtml({ title: "The polarimeter", theme: "light", body: body, script: script, width: 1280 });
const fonts =
  '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>' +
  '<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">';
html = html.replace("</head>", fonts + "</head>");
html = html.replace("<!doctype html>", "<!DOCTYPE html>");

let outFile = join(HERE, "polarimeter.html");
if (SITE) {
  // The site page carries the site's name, an author line and the gallery's saved theme.
  html = html.replace("<title>The polarimeter</title>", "<title>The polarimeter · JSHPhysics</title>");
  const meta =
    '<meta name="description" content="A polarimeter on an optical bench: take it apart, follow the light through polariser, sample and analyser, and measure the rotation of an optically active sample.">' +
    '<meta name="author" content="Joshua Stafford-Haworth (JSHPhysics)">';
  html = html.replace("</head>", meta + "</head>");
  outFile = join(HERE, "..", "index.html");
}
writeFileSync(outFile, html);
console.log("wrote " + outFile, Math.round(html.length / 1024) + " KB");
