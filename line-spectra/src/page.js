// Page script for "Line Spectra".  data.mjs is inlined above this file, and the build script
// defines BENCH (camera and positions of the Fig 1 drawing) just before it.

const SVG_NS = "http://www.w3.org/2000/svg";
const reducedMotion = matchMedia("(prefers-reduced-motion: reduce)");

// ---------- GCSE or A-level ----------

// Which version of the page is showing: "gcse" (no electronvolts or equations) or "alevel".
let course = "gcse";
try {
  const saved = localStorage.getItem("jsh-spectra-course");
  if (saved === "gcse" || saved === "alevel") {
    course = saved;
  }
} catch (error) {
  // Storage is not available here; the page still works.
}

const pageRoot = document.getElementById("page");
pageRoot.dataset.course = course;

function isGcse() {
  return course === "gcse";
}

// What a shell is called: "shell 3" at GCSE, "n = 3" at A-level.
function shellName(n) {
  if (isGcse()) {
    return "shell " + n;
  }
  return "n = " + n;
}

// ---------- small helpers ----------

// Make an SVG element, set its attributes and add it to a parent.
function svgEl(tag, attributes, parent) {
  const element = document.createElementNS(SVG_NS, tag);
  for (const name in attributes) {
    element.setAttribute(name, attributes[name]);
  }
  if (parent) {
    parent.appendChild(element);
  }
  return element;
}

// Make an HTML element with a class and optional text.
function htmlEl(tag, className, text, parent) {
  const element = document.createElement(tag);
  if (className) {
    element.className = className;
  }
  if (text) {
    element.textContent = text;
  }
  if (parent) {
    parent.appendChild(element);
  }
  return element;
}

function clamp(value, low, high) {
  return Math.min(high, Math.max(low, value));
}

// Smooth start and stop for a share that runs from 0 to 1.
function ease(share) {
  const t = clamp(share, 0, 1);
  return t * t * (3 - 2 * t);
}

// The everyday name of the colour at a wavelength.
function colourName(nm) {
  if (nm < 380) {
    return "ultraviolet";
  }
  if (nm < 450) {
    return "violet";
  }
  if (nm < 476) {
    return "blue";
  }
  if (nm < 495) {
    return "blue-green";
  }
  if (nm < 570) {
    return "green";
  }
  if (nm < 590) {
    return "yellow";
  }
  if (nm < 620) {
    return "orange";
  }
  if (nm <= 750) {
    return "red";
  }
  return "infrared";
}

// Set which button in a group is pressed.
function pressOnly(buttons, chosen) {
  for (const button of buttons) {
    let pressed = "false";
    if (button === chosen) {
      pressed = "true";
    }
    button.setAttribute("aria-pressed", pressed);
  }
}

// ---------- flat spectrum strips (Figs 1, 3 and the questions) ----------

let stripCount = 0;

// Where a wavelength sits across a strip, as a share from 0 to 1.
function stripShare(nm) {
  return (nm - VISIBLE[0]) / (VISIBLE[1] - VISIBLE[0]);
}

// Build one strip.  kind is "emission", "absorption" or "continuous".
// The strip stretches to any width; lines stay 2 px wide.
function makeStrip(kind, lines) {
  stripCount += 1;
  const svg = svgEl("svg", { class: "sp-strip", viewBox: "0 0 1000 40", preserveAspectRatio: "none", "aria-hidden": "true" }, null);
  svg.dataset.kind = kind;
  if (kind === "emission") {
    svgEl("rect", { x: 0, y: 0, width: 1000, height: 40, class: "sp-night" }, svg);
  } else {
    // A rainbow: one colour stop every 10 nm.
    const id = "sp-rainbow-" + stripCount;
    const defs = svgEl("defs", {}, svg);
    const gradient = svgEl("linearGradient", { id: id, x1: 0, x2: 1, y1: 0, y2: 0 }, defs);
    for (let nm = VISIBLE[0]; nm <= VISIBLE[1]; nm += 10) {
      svgEl("stop", { offset: stripShare(nm), "stop-color": wavelengthCss(nm) }, gradient);
    }
    svgEl("rect", { x: 0, y: 0, width: 1000, height: 40, class: "sp-night" }, svg);
    svgEl("rect", { x: 0, y: 0, width: 1000, height: 40, fill: "url(#" + id + ")" }, svg);
  }
  for (const line of lines) {
    if (bandOf(line.nm) !== "visible") {
      continue;
    }
    const x = stripShare(line.nm) * 1000;
    const mark = svgEl("line", { x1: x, x2: x, y1: 0, y2: 40, "vector-effect": "non-scaling-stroke", class: "sp-stripline" }, svg);
    if (kind === "emission") {
      mark.setAttribute("stroke", wavelengthCss(line.nm));
      mark.setAttribute("stroke-opacity", line.level);
    }
    if (kind === "absorption") {
      mark.setAttribute("stroke", "#000");
      mark.setAttribute("stroke-opacity", lineDarkness(line.level));
    }
  }
  return svg;
}

// A labelled row: a small heading and a strip.
function makeRow(parent, label, kind, lines) {
  const row = htmlEl("div", "sp-row", "", parent);
  htmlEl("div", "sp-rowlabel", label, row);
  row.appendChild(makeStrip(kind, lines));
  return row;
}

// The wavelength scale that goes under a stack of strips.
function makeAxis(parent) {
  const axis = htmlEl("div", "sp-axis", "", parent);
  for (let nm = 400; nm <= 750; nm += 50) {
    const tick = htmlEl("span", "sp-tick", String(nm), axis);
    tick.style.left = stripShare(nm) * 100 + "%";
  }
  htmlEl("div", "sp-axisname", "wavelength / nm", parent);
}

// A vertical guide that follows the pointer across a stack of strips, with the wavelength it is at.
// lookup(nm) may return extra text to show for the nearest line.
// Call this each time the stack is redrawn: the pointer listeners are only added the first time.
const guides = new Map();
function attachGuide(stack, lookup) {
  const line = htmlEl("div", "sp-guide", "", stack);
  const label = htmlEl("div", "sp-guidelabel", "", stack);
  line.hidden = true;
  label.hidden = true;
  const firstTime = !guides.has(stack);
  guides.set(stack, { line: line, label: label, lookup: lookup });
  if (!firstTime) {
    return;
  }
  function place(event) {
    const guide = guides.get(stack);
    const box = stack.getBoundingClientRect();
    const share = clamp((event.clientX - box.left) / box.width, 0, 1);
    const nm = VISIBLE[0] + share * (VISIBLE[1] - VISIBLE[0]);
    guide.line.hidden = false;
    guide.label.hidden = false;
    guide.line.style.left = share * 100 + "%";
    let text = Math.round(nm) + " nm";
    if (guide.lookup) {
      const extra = guide.lookup(nm);
      if (extra) {
        text = extra;
      }
    }
    guide.label.textContent = text;
    // Keep the label inside the stack at both ends.
    if (share > 0.7) {
      guide.label.style.left = "auto";
      guide.label.style.right = (1 - share) * 100 + "%";
    } else {
      guide.label.style.right = "auto";
      guide.label.style.left = share * 100 + "%";
    }
  }
  stack.addEventListener("pointermove", place);
  stack.addEventListener("pointerdown", place);
  stack.addEventListener("pointerleave", function () {
    const guide = guides.get(stack);
    guide.line.hidden = true;
    guide.label.hidden = true;
  });
}

// All the lines of several elements together.
function linesOfAll(ids) {
  let list = [];
  for (const id of ids) {
    list = list.concat(linesOf(id));
  }
  return list;
}

// The nearest line to a wavelength, if one is within 4 nm.
function nearestLine(lines, nm) {
  let best = null;
  let bestGap = 4;
  for (const line of lines) {
    const gap = Math.abs(line.nm - nm);
    if (gap < bestGap) {
      best = line;
      bestGap = gap;
    }
  }
  return best;
}

// Text for one line: element, wavelength and photon energy.
function describeLine(line) {
  const element = elementById(line.element);
  let text = element.name + " · " + line.nm.toFixed(1) + " nm";
  if (!isGcse()) {
    text += " · " + photonEnergy(line.nm).toFixed(2) + " eV";
  }
  return text;
}

// ---------- Fig 1: the spectroscope bench ----------

const bench = {
  source: "gas", // "lamp" (hot solid), "gas" (hot gas) or "both" (lamp through cool gas)
  gas: "H",
  slide: 0, // how far the tube has slid out of the beam, in bench units
  frame: 0,
};

const benchStage = document.getElementById("stage1");
const benchSvg = benchStage.querySelector("svg");
const benchPart = (name) => benchSvg.querySelector('[data-part="' + name + '"]');
const benchReadout = benchStage.closest(".iso-figure").querySelector("[data-readout]");

// Bench coordinates to drawing coordinates, using the same camera as the build script.
function benchPoint(x, y, z) {
  const cam = BENCH.camera;
  return [cam.origin[0] + x * cam.ex[0] + y * cam.ey[0] + z * cam.ez[0], cam.origin[1] + x * cam.ex[1] + y * cam.ey[1] + z * cam.ez[1]];
}

// A straight ray of light between two points at beam height.
function benchRay(parent, from, to, colour, width, opacity) {
  const a = benchPoint(from[0], from[1], BENCH.beamZ);
  const b = benchPoint(to[0], to[1], BENCH.beamZ);
  const d = "M" + a[0].toFixed(1) + " " + a[1].toFixed(1) + "L" + b[0].toFixed(1) + " " + b[1].toFixed(1);
  // A dark edge first, so a white ray still shows on a pale page.
  svgEl("path", { d: d, class: "sp-rayedge", "stroke-width": width + 1.6, "stroke-opacity": opacity }, parent);
  svgEl("path", { d: d, class: "sp-ray", stroke: colour, "stroke-width": width, "stroke-opacity": opacity }, parent);
}

// A four-sided patch on the face of the screen, between two x positions.
function screenPatch(parent, x0, x1, colour, opacity) {
  const y = BENCH.screenY;
  const corners = [benchPoint(x0, y, BENCH.bandZ[0]), benchPoint(x1, y, BENCH.bandZ[0]), benchPoint(x1, y, BENCH.bandZ[1]), benchPoint(x0, y, BENCH.bandZ[1])];
  let d = "";
  corners.forEach(function (corner, index) {
    let command = "L";
    if (index === 0) {
      command = "M";
    }
    d += command + corner[0].toFixed(1) + " " + corner[1].toFixed(1);
  });
  svgEl("path", { d: d + "Z", fill: colour, "fill-opacity": opacity, stroke: "none" }, parent);
}

// Where first-order light of a wavelength lands on the screen: x = L tan(theta).
function screenX(nm) {
  const distance = -BENCH.screenY;
  return distance * Math.tan(gratingAngle(nm));
}

function emptyGroup(group) {
  while (group.firstChild) {
    group.removeChild(group.firstChild);
  }
}

function drawBench() {
  const lampOn = bench.source !== "gas";
  const tubeUsed = bench.source !== "lamp";
  const glowing = bench.source === "gas";
  const tubeInBeam = bench.slide < 0.5;
  const lines = linesOf(bench.gas);
  const glow = glowCss([bench.gas]);
  let beamColour = "#ffffff";
  if (glowing) {
    beamColour = glow;
  }

  // The lamp window and the gas glow.
  benchPart("lamp-window").dataset.on = String(lampOn);
  const glowPath = benchPart("glow");
  glowPath.style.fill = glow;
  let glowLevel = "0.12";
  if (glowing) {
    glowLevel = "0.85";
  }
  glowPath.style.fillOpacity = glowLevel;

  // The tube slides sideways out of the beam.
  const offset = [BENCH.camera.ex[0] * bench.slide, BENCH.camera.ex[1] * bench.slide];
  benchPart("tube").setAttribute("transform", "translate(" + offset[0].toFixed(1) + " " + offset[1].toFixed(1) + ")");

  // The beam, piece by piece along the bench.
  const nearCap = BENCH.tubeY[0] + 3;
  const farCap = BENCH.tubeY[1] - 3;
  const pieces = ["beam-lamp-tube", "beam-tube", "beam-open", "beam-tube-slit", "beam-slit-lens", "beam-lens-grating", "fan", "screen-light"];
  for (const name of pieces) {
    emptyGroup(benchPart(name));
  }
  if (lampOn) {
    benchRay(benchPart("beam-lamp-tube"), [0, BENCH.lampY], [0, nearCap], beamColour, 3, 1);
    if (tubeUsed && tubeInBeam) {
      benchRay(benchPart("beam-tube"), [0, nearCap], [0, farCap], beamColour, 3, 0.55);
    }
    if (!tubeInBeam) {
      benchRay(benchPart("beam-open"), [0, nearCap], [0, farCap], beamColour, 3, 1);
    }
  }
  const lightReachesSlit = lampOn || (glowing && tubeInBeam);
  if (lightReachesSlit) {
    benchRay(benchPart("beam-tube-slit"), [0, farCap], [0, BENCH.slitY + 1.5], beamColour, 3, 1);
    benchRay(benchPart("beam-slit-lens"), [0, BENCH.slitY - 1.5], [0, BENCH.lensY + 1.5], beamColour, 1.8, 1);
    benchRay(benchPart("beam-lens-grating"), [0, BENCH.lensY - 1.5], [0, 1.5], beamColour, 1.8, 1);
  }

  // After the grating: the straight-through beam and the first-order spectrum.
  const fan = benchPart("fan");
  const light = benchPart("screen-light");
  const grating = [0, -1.5];
  if (lightReachesSlit) {
    benchRay(fan, grating, [0, BENCH.screenY], beamColour, 1.4, 0.9);
    screenPatch(light, -0.8, 0.8, beamColour, 1);
    const absorbing = bench.source === "both" && tubeInBeam;
    if (glowing) {
      // One ray and one bright line for each wavelength the gas gives out.
      for (const line of lines) {
        const x = screenX(line.nm);
        const colour = wavelengthCss(line.nm);
        benchRay(fan, grating, [x, BENCH.screenY], colour, 1.1, line.level);
        screenPatch(light, x - 0.6, x + 0.6, colour, line.level);
      }
    } else {
      // White light: every wavelength, drawn in steps of 5 nm.
      for (let nm = VISIBLE[0]; nm < VISIBLE[1]; nm += 5) {
        const colour = wavelengthCss(nm + 2.5);
        screenPatch(light, screenX(nm), screenX(nm + 5) + 0.15, colour, 1);
      }
      for (let nm = VISIBLE[0]; nm <= VISIBLE[1]; nm += 10) {
        let missing = false;
        if (absorbing) {
          missing = nearestLine(lines, nm) !== null;
        }
        if (!missing) {
          benchRay(fan, grating, [screenX(nm), BENCH.screenY], wavelengthCss(nm), 1.1, 0.75);
        }
      }
      if (absorbing) {
        // The wavelengths the gas has taken out leave dark lines.
        for (const line of lines) {
          const x = screenX(line.nm);
          screenPatch(light, x - 0.6, x + 0.6, "#000", lineDarkness(line.level));
        }
      }
    }
  }

  // The flat copy of the screen, and the readout.
  const flat = document.getElementById("strip1");
  flat.textContent = "";
  const name = elementById(bench.gas).name;
  let kind = "continuous";
  let label = "Continuous spectrum: every colour, no gaps";
  let readout = "Filament lamp · continuous spectrum";
  if (bench.source === "gas") {
    kind = "emission";
    label = "Emission spectrum of " + name.toLowerCase() + ": bright lines on a dark background";
    readout = "Hot " + name.toLowerCase() + " · emission spectrum";
  }
  if (bench.source === "both") {
    kind = "absorption";
    label = "Absorption spectrum of " + name.toLowerCase() + ": dark lines in a continuous spectrum";
    readout = "Lamp through cool " + name.toLowerCase() + " · absorption spectrum";
  }
  let stripLines = lines;
  if (kind === "continuous") {
    stripLines = [];
  }
  makeRow(flat, label, kind, stripLines);
  makeAxis(flat);
  benchReadout.textContent = readout;
}

// Slide the tube towards where it should be, then stop.
function benchTick() {
  let target = 0;
  if (bench.source === "lamp") {
    target = BENCH.tubePark;
  }
  if (reducedMotion.matches) {
    bench.slide = target;
  } else {
    bench.slide += (target - bench.slide) * 0.14;
  }
  if (Math.abs(target - bench.slide) < 0.2) {
    bench.slide = target;
  }
  drawBench();
  if (bench.slide !== target) {
    bench.frame = requestAnimationFrame(benchTick);
  } else {
    bench.frame = 0;
  }
}

function benchChanged() {
  if (!bench.frame) {
    bench.frame = requestAnimationFrame(benchTick);
  }
}

const sourceButtons = Array.from(document.querySelectorAll("[data-source]"));
const gasButtons = Array.from(document.querySelectorAll("[data-gas]"));
for (const button of sourceButtons) {
  button.addEventListener("click", function () {
    bench.source = button.dataset.source;
    pressOnly(sourceButtons, button);
    // The gas buttons do nothing while the tube is out of the beam.
    for (const gasButton of gasButtons) {
      gasButton.disabled = bench.source === "lamp";
    }
    benchChanged();
  });
}
for (const button of gasButtons) {
  button.addEventListener("click", function () {
    bench.gas = button.dataset.gas;
    pressOnly(gasButtons, button);
    benchChanged();
  });
}
drawBench();

// ---------- Fig 2: one hydrogen atom, its energy ladder and its two spectra ----------

const ATOM = {
  centre: [205, 198],
  radii: [0, 28, 54, 80, 106, 132, 158], // shell radius for n = 1..6 (index 0 unused); not to scale
  ladderX: [545, 760],
  zeroY: 44, // where 0 eV is drawn
  perEv: 75, // pixels per eV above the break
  groundY: 372, // where n = 1 is drawn, below a break in the scale
  stripX: [40, 820],
  uvX: 150, // strip x where the visible range starts
  irX: 710, // strip x where the visible range ends
  emissionY: 418,
  absorptionY: 462,
  stripH: 24,
};

// Height on the ladder of level n.
function ladderY(n) {
  if (n === 1) {
    return ATOM.groundY;
  }
  return ATOM.zeroY - levelEnergy(n) * ATOM.perEv;
}

// Where a wavelength sits on the Fig 2 strips, which have squashed ultraviolet and infrared ends.
function atomStripX(nm) {
  if (nm < VISIBLE[0]) {
    const share = (nm - 90) / (VISIBLE[0] - 90);
    return ATOM.stripX[0] + share * (ATOM.uvX - ATOM.stripX[0]);
  }
  if (nm > VISIBLE[1]) {
    const share = clamp((nm - VISIBLE[1]) / (1900 - VISIBLE[1]), 0, 1);
    return ATOM.irX + share * (ATOM.stripX[1] - ATOM.irX);
  }
  return ATOM.uvX + stripShare(nm) * (ATOM.irX - ATOM.uvX);
}

const atomSvg = document.getElementById("atom");
const atomReadout = atomSvg.closest(".iso-figure").querySelector("[data-readout]");

const atom = {
  n: 1, // the level the electron is on (or heading for)
  radius: ATOM.radii[1], // where the electron is drawn
  ladderY: ladderY(1),
  angle: -0.6, // where it is round its shell
  emitted: [], // pairs such as "3-2" that have given out a photon
  absorbed: [], // pairs that have taken a photon in
  latest: "", // the pair most recently used
  photons: [], // photons in flight
  move: null, // the jump in progress
  queue: [], // actions still to do
  wait: 0, // seconds to pause before the next action
  spark: 0, // 1 just after a collision or an absorption, fading to 0
  sparkColour: "", // colour of that flash; empty for a collision
  visible: false,
  frame: 0,
  last: 0,
};

// Draw the parts of Fig 2 that never change.
const atomLayers = {};
function buildAtom() {
  const cx = ATOM.centre[0];
  const cy = ATOM.centre[1];
  // Shells, outermost first so the inner ones are on top for clicking.
  atomLayers.shells = svgEl("g", {}, atomSvg);
  for (let n = 6; n >= 1; n -= 1) {
    svgEl("circle", { cx: cx, cy: cy, r: ATOM.radii[n], class: "sp-shell", "data-shell": n }, atomLayers.shells);
    // A wide invisible ring makes the shell easy to click or tap.
    const hit = svgEl("circle", { cx: cx, cy: cy, r: ATOM.radii[n], class: "sp-shellhit" }, atomLayers.shells);
    hit.addEventListener("click", function () {
      requestLevel(n);
    });
  }
  // Shell labels on a line up and to the right of the nucleus.
  for (let n = 1; n <= 6; n += 1) {
    const x = cx + ATOM.radii[n] * 0.707;
    const y = cy - ATOM.radii[n] * 0.707;
    const label = svgEl("text", { x: x + 4, y: y - 4, class: "sp-shelllabel" }, atomSvg);
    label.textContent = shellName(n);
  }
  svgEl("circle", { cx: cx, cy: cy, r: 9, class: "sp-nucleus" }, atomSvg);
  const plus = svgEl("text", { x: cx, y: cy + 4.5, class: "sp-nucleussign" }, atomSvg);
  plus.textContent = "+";
  const note = svgEl("text", { x: cx, y: cy + ATOM.radii[6] + 18, class: "sp-note", "text-anchor": "middle" }, atomSvg);
  note.textContent = "hydrogen atom (shells not to scale)";

  // The energy ladder.
  const x0 = ATOM.ladderX[0];
  const x1 = ATOM.ladderX[1];
  svgEl("line", { x1: x0, x2: x1, y1: ATOM.zeroY, y2: ATOM.zeroY, class: "sp-level sp-levelfree" }, atomSvg);
  const freeLabel = svgEl("text", { x: x1 + 8, y: ATOM.zeroY + 4, class: "sp-energy" }, atomSvg);
  const freeName = svgEl("text", { x: x0 - 8, y: ATOM.zeroY + 4, class: "sp-levelname", "text-anchor": "end" }, atomSvg);
  if (isGcse()) {
    // Sits above the right-hand end of the dashed line, so it stays inside the drawing.
    freeLabel.textContent = "electron escapes from the atom";
    freeLabel.setAttribute("x", x1);
    freeLabel.setAttribute("y", ATOM.zeroY - 6);
    freeLabel.setAttribute("text-anchor", "end");
  } else {
    freeLabel.textContent = "0 eV";
    freeName.textContent = "free";
  }
  for (let n = 1; n <= 6; n += 1) {
    const y = ladderY(n);
    svgEl("line", { x1: x0, x2: x1, y1: y, y2: y, class: "sp-level" }, atomSvg);
    const name = svgEl("text", { x: x0 - 8, y: y + 4, class: "sp-levelname", "text-anchor": "end" }, atomSvg);
    name.textContent = shellName(n);
    if (!isGcse()) {
      const energy = svgEl("text", { x: x1 + 8, y: y + 4, class: "sp-energy" }, atomSvg);
      energy.textContent = "−" + Math.abs(levelEnergy(n)).toFixed(2) + " eV";
    }
    const hit = svgEl("rect", { x: x0 - 50, y: y - 6, width: x1 - x0 + 120, height: 12, class: "sp-levelhit" }, atomSvg);
    hit.addEventListener("click", function () {
      requestLevel(n);
    });
  }
  // The break in the scale between n = 2 and n = 1.
  const breakY = (ladderY(2) + ATOM.groundY) / 2;
  const zig = "M" + (x0 - 30) + " " + (breakY - 4) + "l10 8l10 -8l10 8";
  svgEl("path", { d: zig, class: "sp-break" }, atomSvg);
  const breakNote = svgEl("text", { x: x0 + 8, y: breakY + 4, class: "sp-note" }, atomSvg);
  const title = svgEl("text", { x: (x0 + x1) / 2, y: 16, class: "sp-note", "text-anchor": "middle" }, atomSvg);
  if (isGcse()) {
    breakNote.textContent = "a much bigger gap than can be drawn";
    title.textContent = "energy of the electron in each shell: higher up = more energy";
  } else {
    breakNote.textContent = "scale broken: 10.2 eV gap";
    title.textContent = "energy levels";
  }

  atomLayers.arrows = svgEl("g", {}, atomSvg);
  // A line that grows on the ladder while a jump is happening.
  atomLayers.trail = svgEl("line", { class: "sp-trail" }, atomSvg);

  // The two strips.
  const sx = ATOM.stripX[0];
  const width = ATOM.stripX[1] - ATOM.stripX[0];
  const defs = svgEl("defs", {}, atomSvg);
  const gradient = svgEl("linearGradient", { id: "atom-rainbow", x1: 0, x2: 1, y1: 0, y2: 0 }, defs);
  for (let nm = VISIBLE[0]; nm <= VISIBLE[1]; nm += 10) {
    svgEl("stop", { offset: stripShare(nm), "stop-color": wavelengthCss(nm) }, gradient);
  }
  const rows = [
    [ATOM.emissionY, "Emission spectrum: the light this atom has given out"],
    [ATOM.absorptionY, "Absorption spectrum: white light after passing the atom"],
  ];
  for (const row of rows) {
    const label = svgEl("text", { x: sx, y: row[0] - 5, class: "sp-note" }, atomSvg);
    label.textContent = row[1];
    svgEl("rect", { x: sx, y: row[0], width: width, height: ATOM.stripH, class: "sp-night" }, atomSvg);
  }
  svgEl("rect", { x: ATOM.uvX, y: ATOM.absorptionY, width: ATOM.irX - ATOM.uvX, height: ATOM.stripH, fill: "url(#atom-rainbow)" }, atomSvg);
  // Mark the ends the eye cannot see.
  for (const y of [ATOM.emissionY, ATOM.absorptionY]) {
    svgEl("rect", { x: sx, y: y, width: ATOM.uvX - sx, height: ATOM.stripH, class: "sp-unseen" }, atomSvg);
    svgEl("rect", { x: ATOM.irX, y: y, width: ATOM.stripX[1] - ATOM.irX, height: ATOM.stripH, class: "sp-unseen" }, atomSvg);
  }
  const bottom = ATOM.absorptionY + ATOM.stripH;
  const zones = [
    [(sx + ATOM.uvX) / 2, "ultraviolet"],
    [(ATOM.irX + ATOM.stripX[1]) / 2, "infrared"],
  ];
  for (const zone of zones) {
    const text = svgEl("text", { x: zone[0], y: bottom + 14, class: "sp-note", "text-anchor": "middle" }, atomSvg);
    text.textContent = zone[1];
  }
  for (let nm = 400; nm <= 700; nm += 50) {
    const x = atomStripX(nm);
    svgEl("line", { x1: x, x2: x, y1: bottom, y2: bottom + 4, class: "sp-ticmark" }, atomSvg);
    const text = svgEl("text", { x: x, y: bottom + 15, class: "sp-note", "text-anchor": "middle" }, atomSvg);
    text.textContent = nm + " nm";
  }
  atomLayers.lines = svgEl("g", {}, atomSvg);

  // Moving things, on top.
  atomLayers.spark = svgEl("circle", { r: 10, class: "sp-spark" }, atomSvg);
  atomLayers.sparkText = svgEl("text", { class: "sp-note sp-sparktext", "text-anchor": "middle" }, atomSvg);
  atomLayers.sparkText.textContent = "collision";
  atomLayers.flashText = svgEl("text", { class: "sp-note sp-flashtext", "text-anchor": "middle" }, atomSvg);
  atomLayers.photons = svgEl("g", {}, atomSvg);
  atomLayers.ladderDot = svgEl("circle", { r: 6, class: "sp-electron" }, atomSvg);
  atomLayers.electron = svgEl("circle", { r: 7, class: "sp-electron" }, atomSvg);
  atomLayers.electronSign = svgEl("text", { class: "sp-electronsign" }, atomSvg);
  atomLayers.electronSign.textContent = "−";
}

// The name of a pair of levels, higher number first, such as "3-2".
function pairKey(a, b) {
  return Math.max(a, b) + "-" + Math.min(a, b);
}

function electronPosition() {
  return [ATOM.centre[0] + atom.radius * Math.cos(atom.angle), ATOM.centre[1] + atom.radius * Math.sin(atom.angle)];
}

// The wavy path of a photon whose middle is at (x, y), travelling in direction (dx, dy).
function photonPath(x, y, dx, dy, nm) {
  // Shorter wavelength, tighter wiggles.  Clamped so ultraviolet and infrared can still be drawn.
  const wave = clamp(nm / 42, 6, 26);
  const half = 30;
  let d = "";
  for (let s = -half; s <= half; s += 1.5) {
    const envelope = Math.exp(-(s * s) / 260);
    const swing = 7 * envelope * Math.sin((2 * Math.PI * s) / wave);
    const px = x + dx * s - dy * swing;
    const py = y + dy * s + dx * swing;
    let command = "L";
    if (s === -half) {
      command = "M";
    }
    d += command + px.toFixed(1) + " " + py.toFixed(1);
  }
  return d;
}

// Redraw everything in Fig 2 that can change.
function drawAtom() {
  const position = electronPosition();
  atomLayers.electron.setAttribute("cx", position[0].toFixed(1));
  atomLayers.electron.setAttribute("cy", position[1].toFixed(1));
  atomLayers.electronSign.setAttribute("x", position[0].toFixed(1));
  atomLayers.electronSign.setAttribute("y", (position[1] + 4).toFixed(1));
  atomLayers.ladderDot.setAttribute("cx", ATOM.ladderX[0] + 14);
  atomLayers.ladderDot.setAttribute("cy", atom.ladderY.toFixed(1));

  // The shell the electron is on is drawn darker.
  for (const shell of atomLayers.shells.querySelectorAll(".sp-shell")) {
    let on = "false";
    if (Number(shell.dataset.shell) === atom.n && !atom.move) {
      on = "true";
    }
    shell.dataset.on = on;
  }

  // The collision flash.
  atomLayers.spark.setAttribute("cx", position[0].toFixed(1));
  atomLayers.spark.setAttribute("cy", position[1].toFixed(1));
  atomLayers.spark.setAttribute("r", (10 + (1 - atom.spark) * 16).toFixed(1));
  atomLayers.spark.style.opacity = atom.spark.toFixed(2);
  atomLayers.spark.style.stroke = atom.sparkColour;
  // The word "collision" only shows for a collision, not for light being absorbed.
  let collisionShown = 0;
  if (atom.sparkColour === "") {
    collisionShown = atom.spark;
  }
  atomLayers.sparkText.setAttribute("x", position[0].toFixed(1));
  atomLayers.sparkText.setAttribute("y", (position[1] - 30).toFixed(1));
  atomLayers.sparkText.style.opacity = collisionShown.toFixed(2);

  // While a jump is happening: a growing line on the ladder, and a label saying what is going on.
  const trail = atomLayers.trail;
  const flashText = atomLayers.flashText;
  if (atom.move && atom.move.started) {
    let colour = "";
    if (atom.move.how !== "collision") {
      colour = wavelengthCss(gapWavelength(atom.move.from, atom.move.to));
    }
    const x = ATOM.ladderX[0] + 14;
    trail.setAttribute("x1", x);
    trail.setAttribute("x2", x);
    trail.setAttribute("y1", ladderY(atom.move.from).toFixed(1));
    trail.setAttribute("y2", atom.ladderY.toFixed(1));
    trail.style.stroke = colour;
    trail.style.opacity = "1";
    let words = "";
    if (atom.move.how === "emit") {
      words = "light given out";
    }
    if (atom.move.how === "absorb") {
      words = "light absorbed";
    }
    flashText.textContent = words;
    flashText.setAttribute("x", position[0].toFixed(1));
    flashText.setAttribute("y", (position[1] - 30).toFixed(1));
    flashText.style.opacity = "1";
  } else {
    trail.style.opacity = "0";
    flashText.style.opacity = "0";
  }

  // Photons in flight.
  emptyGroup(atomLayers.photons);
  for (const photon of atom.photons) {
    const path = svgEl("path", { d: photonPath(photon.x, photon.y, photon.dx, photon.dy, photon.nm), class: "sp-photon" }, atomLayers.photons);
    path.setAttribute("stroke", wavelengthCss(photon.nm));
    path.style.opacity = photon.fade.toFixed(2);
    if (bandOf(photon.nm) !== "visible") {
      path.setAttribute("stroke-dasharray", "3 2");
      const text = svgEl("text", { x: photon.x, y: photon.y - 14, class: "sp-note", "text-anchor": "middle" }, atomLayers.photons);
      text.textContent = bandOf(photon.nm);
      text.style.opacity = photon.fade.toFixed(2);
    }
  }
}

// Redraw the arrows on the ladder and the lines on the two strips.  Only needed when a jump finishes.
function drawAtomRecord() {
  emptyGroup(atomLayers.arrows);
  emptyGroup(atomLayers.lines);
  // Every pair used so far, in the order it was first used.
  const pairs = [];
  for (const key of atom.emitted.concat(atom.absorbed)) {
    if (pairs.indexOf(key) < 0) {
      pairs.push(key);
    }
  }
  pairs.forEach(function (key, index) {
    const upper = Number(key.split("-")[0]);
    const lower = Number(key.split("-")[1]);
    const nm = gapWavelength(upper, lower);
    const colour = wavelengthCss(nm);
    const x = ATOM.ladderX[0] + 42 + (index % 8) * 22;
    const top = ladderY(upper);
    const bottom = ladderY(lower);
    const wasEmitted = atom.emitted.indexOf(key) >= 0;
    const wasAbsorbed = atom.absorbed.indexOf(key) >= 0;
    const arrow = svgEl("g", { class: "sp-arrow" }, atomLayers.arrows);
    if (key === atom.latest) {
      arrow.dataset.latest = "true";
    }
    svgEl("line", { x1: x, x2: x, y1: top + 3, y2: bottom - 3, stroke: colour }, arrow);
    if (wasEmitted) {
      // Arrowhead pointing down: the electron fell.
      svgEl("path", { d: "M" + (x - 4) + " " + (bottom - 8) + "L" + x + " " + (bottom - 1) + "L" + (x + 4) + " " + (bottom - 8) + "Z", fill: colour }, arrow);
    }
    if (wasAbsorbed) {
      // Arrowhead pointing up: the electron was lifted.
      svgEl("path", { d: "M" + (x - 4) + " " + (top + 8) + "L" + x + " " + (top + 1) + "L" + (x + 4) + " " + (top + 8) + "Z", fill: colour }, arrow);
    }
    // The matching lines on the strips.
    const sx = atomStripX(nm);
    const unseen = bandOf(nm) !== "visible";
    if (wasEmitted) {
      const line = svgEl("line", { x1: sx, x2: sx, y1: ATOM.emissionY, y2: ATOM.emissionY + ATOM.stripH, stroke: colour, class: "sp-atomline" }, atomLayers.lines);
      if (key === atom.latest) {
        line.dataset.latest = "true";
      }
      if (unseen) {
        line.setAttribute("stroke-dasharray", "3 2");
      }
    }
    if (wasAbsorbed) {
      let stroke = "#000";
      if (unseen) {
        stroke = colour;
      }
      const line = svgEl("line", { x1: sx, x2: sx, y1: ATOM.absorptionY, y2: ATOM.absorptionY + ATOM.stripH, stroke: stroke, class: "sp-atomline" }, atomLayers.lines);
      if (key === atom.latest) {
        line.dataset.latest = "true";
      }
      if (unseen) {
        line.setAttribute("stroke-dasharray", "3 2");
      }
    }
  });
}

// Say what just happened, in the corner of the card.
function describeJump(from, to, how) {
  const nm = gapWavelength(from, to);
  const energy = gapEnergy(from, to).toFixed(2);
  const wavelength = Math.round(nm) + " nm";
  if (isGcse()) {
    // GCSE wording: shells and light, no electronvolts.
    let text = "shell " + from + " → shell " + to + " · ";
    if (how === "collision") {
      return text + "a collision gave it the energy";
    }
    if (how === "emit") {
      text += "light given out";
    } else {
      text += "light absorbed";
    }
    return text + " · " + colourName(nm) + " · " + wavelength;
  }
  let text = "n = " + from + " → " + to + " · ";
  if (how === "collision") {
    text += "collision gave it " + energy + " eV";
    return text;
  }
  if (how === "emit") {
    text += "photon out";
  } else {
    text += "photon absorbed";
  }
  return text + " · " + energy + " eV · " + wavelength + " · " + colourName(nm);
}

// What to say when light of the wrong wavelength goes straight past.
function describePass(nm) {
  if (isGcse()) {
    return colourName(nm) + " light, " + Math.round(nm) + " nm · wrong energy for any jump · passes straight through";
  }
  return Math.round(nm) + " nm photon · " + photonEnergy(nm).toFixed(2) + " eV · no gap matches · not absorbed";
}

// Start the next action in the queue, if nothing is happening.
function nextAction() {
  if (atom.move || atom.wait > 0 || atom.queue.length === 0) {
    return;
  }
  const action = atom.queue.shift();
  const position = electronPosition();
  if (action.do === "wait") {
    atom.wait = action.seconds;
    return;
  }
  if (action.do === "pass") {
    // A photon of the wrong energy goes straight past.
    atom.photons.push({ nm: action.nm, x: -30, y: position[1], dx: 1, dy: 0, fade: 1, life: 560, travelled: 0, role: "pass" });
    atom.wait = 560 / PHOTON_SPEED + 0.3;
    atomReadout.textContent = describePass(action.nm);
    return;
  }
  if (action.do === "jump" || action.do === "kick") {
    const from = atom.n;
    const to = action.to;
    if (from === to) {
      return;
    }
    const move = { from: from, to: to, share: 0, started: false, how: "collision" };
    if (action.do === "jump") {
      if (to < from) {
        move.how = "emit";
      } else {
        move.how = "absorb";
      }
    }
    atom.move = move;
    if (move.how === "collision") {
      atom.spark = 1;
      atom.sparkColour = "";
      move.started = true;
    }
    if (move.how === "emit") {
      // The photon leaves as the electron starts to fall.
      let angle = Math.random() * Math.PI * 2;
      if (typeof action.angle === "number") {
        angle = action.angle;
      }
      atom.photons.push({ nm: gapWavelength(from, to), x: position[0], y: position[1], dx: Math.cos(angle), dy: Math.sin(angle), fade: 0, life: 330, travelled: 0, role: "out" });
      move.started = true;
    }
    if (move.how === "absorb") {
      // The photon comes in from the lamp on the left; the electron waits for it.
      const distance = position[0] + 30;
      atom.photons.push({ nm: gapWavelength(from, to), x: -30, y: position[1], dx: 1, dy: 0, fade: 0, life: distance, travelled: 0, role: "in" });
    }
  }
}

// Finish the jump in progress.
function finishMove() {
  const move = atom.move;
  atom.n = move.to;
  atom.radius = ATOM.radii[move.to];
  atom.ladderY = ladderY(move.to);
  const key = pairKey(move.from, move.to);
  if (move.how === "emit" && atom.emitted.indexOf(key) < 0) {
    atom.emitted.push(key);
  }
  if (move.how === "absorb" && atom.absorbed.indexOf(key) < 0) {
    atom.absorbed.push(key);
  }
  if (move.how !== "collision") {
    atom.latest = key;
  }
  atomReadout.textContent = describeJump(move.from, move.to, move.how);
  atom.move = null;
  atom.wait = 0.8;
  drawAtomRecord();
  syncLevelButtons();
}

// How fast light is drawn moving (pixels per second) and how long a jump between shells takes (seconds).
// Both are slow enough to follow by eye.
const PHOTON_SPEED = 150;
const JUMP_SECONDS = 1.5;

// Advance Fig 2 by dt seconds.
function stepAtom(dt) {
  if (atom.wait > 0) {
    atom.wait -= dt;
  }
  nextAction();
  // Photons.
  const kept = [];
  for (const photon of atom.photons) {
    const step = PHOTON_SPEED * dt;
    photon.x += photon.dx * step;
    photon.y += photon.dy * step;
    photon.travelled += step;
    // Fade in over the first 40 px, so light grows out of the electron instead of popping into view.
    const fadeIn = clamp(photon.travelled / 40, 0, 1);
    let fadeOut = 1;
    if (photon.role === "out" || photon.role === "pass") {
      // Fade over the last 80 px of its path.
      fadeOut = clamp((photon.life - photon.travelled) / 80, 0, 1);
    }
    if (photon.role === "in") {
      // Shrink into the electron over the last 30 px.
      fadeOut = clamp((photon.life - photon.travelled) / 30, 0, 1);
    }
    photon.fade = Math.min(fadeIn, fadeOut);
    if (photon.travelled < photon.life) {
      kept.push(photon);
    } else if (photon.role === "in" && atom.move) {
      // The light has reached the electron: a flash in its colour, and now the electron can jump.
      atom.move.started = true;
      atom.spark = 1;
      atom.sparkColour = wavelengthCss(photon.nm);
    }
  }
  atom.photons = kept;
  // The electron.
  if (atom.move && atom.move.started) {
    atom.move.share += dt / JUMP_SECONDS;
    const share = ease(atom.move.share);
    const from = atom.move.from;
    const to = atom.move.to;
    atom.radius = ATOM.radii[from] + (ATOM.radii[to] - ATOM.radii[from]) * share;
    atom.ladderY = ladderY(from) + (ladderY(to) - ladderY(from)) * share;
    if (atom.move.share >= 1) {
      finishMove();
    }
  }
  // The electron drifts round its shell between jumps (not when reduced motion is asked for).
  if (!atom.move && !reducedMotion.matches) {
    atom.angle += 0.45 * dt;
  }
  atom.spark = Math.max(0, atom.spark - dt / 0.9);
}

// True while a jump, some light or a pause is still playing.
function atomBusy() {
  return atom.move !== null || atom.photons.length > 0 || atom.queue.length > 0 || atom.wait > 0 || atom.spark > 0;
}

function atomTick(now) {
  let dt = 1 / 60;
  if (atom.last) {
    dt = Math.min((now - atom.last) / 1000, 1 / 20);
  }
  atom.last = now;
  stepAtom(dt);
  drawAtom();
  // Keep going while something is playing.  When idle, keep the slow drift only if the figure is on screen.
  const drifting = atom.visible && !reducedMotion.matches;
  if (atomBusy() || drifting) {
    atom.frame = requestAnimationFrame(atomTick);
  } else {
    atom.frame = 0;
  }
}

// Start the animation loop if it is not already running.
// A jump that the student asked for always plays as an animation: seeing it happen is the point of the figure.
function runAtom() {
  if (!atom.frame) {
    atom.last = 0;
    atom.frame = requestAnimationFrame(atomTick);
  }
}

// The student asks for the electron to go to level n.
function requestLevel(n) {
  // Work out where the electron will be once everything already queued has happened.
  let final = atom.n;
  if (atom.move) {
    final = atom.move.to;
  }
  for (const action of atom.queue) {
    if (action.do === "jump" || action.do === "kick") {
      final = action.to;
    }
  }
  if (n === final || atom.queue.length > 2) {
    return;
  }
  atom.queue.push({ do: "jump", to: n });
  runAtom();
}

const levelButtons = Array.from(document.querySelectorAll("[data-level]"));
function syncLevelButtons() {
  for (const button of levelButtons) {
    button.textContent = shellName(Number(button.dataset.level));
    let pressed = "false";
    if (Number(button.dataset.level) === atom.n) {
      pressed = "true";
    }
    button.setAttribute("aria-pressed", pressed);
  }
}
for (const button of levelButtons) {
  button.addEventListener("click", function () {
    requestLevel(Number(button.dataset.level));
  });
}
document.getElementById("clear-spectra").addEventListener("click", function () {
  atom.emitted = [];
  atom.absorbed = [];
  atom.latest = "";
  drawAtomRecord();
  atomReadout.textContent = "spectra cleared";
});

// ---------- Fig 2: the step-by-step walkthrough ----------

const UP_LEFT = Math.PI * 1.2;
const STAGES = [
  {
    title: "Electrons sit on fixed shells",
    gcseTitle: "Electrons sit on fixed shells",
    gcse: "The electron in a hydrogen atom can only be in certain shells, at fixed distances from the nucleus. The further out the shell, the more energy the electron has. The ladder on the right shows the energy of each shell. Normally the electron sits in the lowest one, shell 1.",
    body: "The electron in a hydrogen atom can only be on certain shells. Each shell has a fixed energy, shown on the ladder on the right. The energies are negative because the electron is bound to the nucleus: 0 eV would be an electron that has escaped. The lowest shell, n = 1, is the ground state.",
    start: { n: 1, emitted: [], absorbed: [] },
    actions: [],
  },
  {
    title: "Exciting the atom",
    gcseTitle: "Exciting the atom",
    gcse: "Heat a gas, or pass a current through it, and its atoms collide hard. A collision can give the electron enough energy to jump out to a higher shell. Watch the dot climb the ladder as the electron moves outwards.",
    body: "Heat a gas, or pass a current through it, and its atoms collide hard. A collision can give the electron exactly enough energy to jump to a higher shell. The atom is now excited. Watch the dot climb the ladder as the electron moves outwards.",
    start: { n: 1, emitted: [], absorbed: [] },
    actions: [{ do: "wait", seconds: 0.6 }, { do: "kick", to: 3 }],
  },
  {
    title: "Falling back gives out a photon",
    gcseTitle: "Falling back gives out light",
    gcse: "The electron soon falls back to a lower shell. The energy it loses leaves the atom as electromagnetic radiation. A fall from shell 3 to shell 2 always gives out the same amount of energy, which is red light with a wavelength of 656 nm. One bright line appears in the emission spectrum.",
    body: "An excited electron soon falls to a lower shell. The energy it loses leaves as one photon. Falling from n = 3 to n = 2 loses 3.40 − 1.51 = 1.89 eV, and a 1.89 eV photon is red light of wavelength 656 nm. One bright line appears in the emission spectrum.",
    start: { n: 3, emitted: [], absorbed: [] },
    actions: [{ do: "wait", seconds: 0.6 }, { do: "jump", to: 2, angle: -0.25 }],
  },
  {
    title: "A bigger fall, a bluer photon",
    gcseTitle: "A bigger fall, bluer light",
    gcse: "This time a collision lifts the electron to shell 4. The fall to shell 2 is bigger, so more energy is given out. More energy means a higher frequency and a shorter wavelength: 486 nm, which is blue-green. A different fall gives a different line.",
    body: "This time a collision lifts the electron to n = 4. The fall to n = 2 is larger, 2.55 eV, so the photon has more energy, a higher frequency and a shorter wavelength: 486 nm, blue-green. A different gap gives a different line.",
    start: { n: 2, emitted: ["3-2"], absorbed: [] },
    actions: [{ do: "wait", seconds: 0.5 }, { do: "kick", to: 4 }, { do: "wait", seconds: 0.4 }, { do: "jump", to: 2, angle: 0.3 }],
  },
  {
    title: "The emission spectrum",
    gcseTitle: "The emission spectrum",
    gcse: "Falls from shells 5 and 6 to shell 2 add two violet lines. The shells are fixed, so hydrogen can only give out these exact wavelengths and nothing in between. That set of lines is hydrogen's emission spectrum, and no other element has the same one.",
    body: "Falls from n = 5 and n = 6 to n = 2 add two violet lines. The gaps between shells are fixed, so hydrogen can only give out these exact wavelengths and nothing in between. That set of lines is hydrogen's emission spectrum, and no other element has the same one.",
    start: { n: 2, emitted: ["3-2", "4-2"], absorbed: [] },
    actions: [{ do: "kick", to: 5 }, { do: "jump", to: 2, angle: -0.5 }, { do: "kick", to: 6 }, { do: "jump", to: 2, angle: 0.15 }],
  },
  {
    title: "Lines the eye cannot see",
    gcseTitle: "Lines the eye cannot see",
    gcse: "A fall all the way to shell 1 gives out so much energy that the radiation is ultraviolet. A small fall, such as shell 4 to shell 3, gives out infrared. Both are real lines in the spectrum, drawn dashed here, but only falls that end on shell 2 give visible light.",
    body: "A fall to n = 1 is a huge gap, 10.2 eV or more, so the photon is ultraviolet. A fall to n = 3 is a small gap and the photon is infrared. Both are real lines in the spectrum, drawn dashed here, but only falls that end on n = 2 give visible light.",
    start: { n: 2, emitted: ["3-2", "4-2", "5-2", "6-2"], absorbed: [] },
    actions: [{ do: "jump", to: 1, angle: -0.3 }, { do: "kick", to: 4 }, { do: "jump", to: 3, angle: 0.4 }, { do: "jump", to: 2, angle: -0.6 }],
  },
  {
    title: "Now shine white light through",
    gcseTitle: "Now shine white light through",
    gcse: "White light contains every wavelength. Here the atom is not glowing, and its electron is in shell 2. Green light arrives from the lamp on the left. Its energy is not exactly right to lift the electron to any higher shell, so the atom cannot absorb it. The light passes straight through.",
    body: "White light contains photons of every energy. Here the atom is cool enough not to glow, with its electron on n = 2. A green photon of 2.30 eV arrives from the lamp on the left. No gap above n = 2 is exactly 2.30 eV, so the atom cannot take it in. The photon passes straight through.",
    start: { n: 2, emitted: ["3-2", "4-2", "5-2", "6-2", "2-1", "4-3"], absorbed: [] },
    actions: [{ do: "wait", seconds: 0.5 }, { do: "pass", nm: 540 }],
  },
  {
    title: "The right photon is absorbed",
    gcseTitle: "The right light is absorbed",
    gcse: "Red light of 656 nm carries exactly the energy needed to lift the electron from shell 2 to shell 3. The atom absorbs it and the electron jumps up. That light never reaches the screen, so a dark line appears in the continuous spectrum at 656 nm.",
    body: "A red photon of exactly 1.89 eV does match a gap: n = 2 to n = 3. The atom absorbs it and the electron jumps up. That photon never reaches the screen, so a dark line appears in the continuous spectrum at 656 nm.",
    start: { n: 2, emitted: ["3-2", "4-2", "5-2", "6-2", "2-1", "4-3"], absorbed: [] },
    actions: [{ do: "wait", seconds: 0.5 }, { do: "jump", to: 3 }],
  },
  {
    title: "Why the line stays dark",
    gcseTitle: "Why the line stays dark",
    gcse: "The electron soon falls back and gives out red light again. But it leaves in a random direction, and almost never straight on towards the screen. So the light that carries on has lost most of its 656 nm, and the line stays dark.",
    body: "The electron soon falls back and gives out a red photon again. But it leaves in a random direction, and almost never straight on towards the screen. So the light that carries on has lost most of its 656 nm photons, and the line stays dark.",
    start: { n: 3, emitted: ["3-2", "4-2", "5-2", "6-2", "2-1", "4-3"], absorbed: ["3-2"] },
    actions: [{ do: "wait", seconds: 0.6 }, { do: "jump", to: 2, angle: UP_LEFT }],
  },
  {
    title: "Same gaps, same lines",
    gcseTitle: "Same jumps, same lines",
    gcse: "The other jumps up from shell 2 take out 486, 434 and 410 nm. Look at the two strips: the dark lines sit exactly where the bright lines do, because absorbing and emitting use the same jumps. An element can be recognised from either kind of spectrum.",
    body: "The other jumps up from n = 2 take out 486, 434 and 410 nm. Look at the two strips: the dark lines sit exactly where the bright lines do, because absorbing and emitting use the same gaps. An element can be recognised from either kind of spectrum.",
    start: { n: 2, emitted: ["3-2", "4-2", "5-2", "6-2", "2-1", "4-3"], absorbed: ["3-2"] },
    actions: [{ do: "jump", to: 4 }, { do: "jump", to: 2, angle: UP_LEFT }, { do: "jump", to: 5 }, { do: "jump", to: 2, angle: 2.2 }, { do: "jump", to: 6 }],
  },
  {
    title: "Your turn",
    gcseTitle: "Your turn",
    gcse: "Use the buttons under the figure, or click a shell, to move the electron yourself. Moving down gives out light; moving up absorbs light. Before each move, predict whether the light will be visible, ultraviolet or infrared. Which jump gives out the most energy?",
    body: "Use the buttons under the figure, or click a shell or a level, to move the electron yourself. Moving down gives out a photon; moving up absorbs one. Before each move, predict whether the photon will be visible, ultraviolet or infrared. Which jump gives the photon with the most energy?",
    start: null,
    actions: [],
  },
];

let stageIndex = 0;
const stepCount = document.getElementById("step-count");
const stepTitle = document.getElementById("step-title");
const stepBody = document.getElementById("step-body");
const stepBack = document.getElementById("step-back");
const stepNext = document.getElementById("step-next");
const stepReplay = document.getElementById("step-replay");

function showStage(index) {
  stageIndex = clamp(index, 0, STAGES.length - 1);
  const stage = STAGES[stageIndex];
  stepCount.textContent = "Step " + (stageIndex + 1) + " of " + STAGES.length;
  let title = stage.title;
  let body = stage.body;
  if (isGcse()) {
    title = stage.gcseTitle;
    body = stage.gcse;
  }
  stepTitle.textContent = title;
  stepBody.textContent = body;
  stepBack.disabled = stageIndex === 0;
  stepNext.disabled = stageIndex === STAGES.length - 1;
  stepReplay.disabled = stage.actions.length === 0;
  // Put the atom in the state this step starts from, then play the step.
  atom.queue = [];
  atom.move = null;
  atom.photons = [];
  atom.wait = 0;
  atom.spark = 0;
  if (stage.start) {
    atom.n = stage.start.n;
    atom.emitted = stage.start.emitted.slice();
    atom.absorbed = stage.start.absorbed.slice();
    atom.latest = "";
    atomReadout.textContent = "electron on " + shellName(atom.n);
  }
  atom.radius = ATOM.radii[atom.n];
  atom.ladderY = ladderY(atom.n);
  for (const action of stage.actions) {
    atom.queue.push(action);
  }
  drawAtomRecord();
  syncLevelButtons();
  drawAtom();
  runAtom();
}
stepBack.addEventListener("click", function () {
  showStage(stageIndex - 1);
});
stepNext.addEventListener("click", function () {
  showStage(stageIndex + 1);
});
stepReplay.addEventListener("click", function () {
  showStage(stageIndex);
});

// Bring the whole of Fig 2 into view if part of it is off the screen.
const atomCard = atomSvg.closest(".iso-figure");
atomCard.classList.add("sp-fig2card");
function showWholeCard() {
  let behaviour = "smooth";
  if (reducedMotion.matches) {
    behaviour = "auto";
  }
  // The framed part of the figure (without the caption underneath) is what has to fit.
  const frame = atomCard.querySelector(".iso-plate");
  const box = frame.getBoundingClientRect();
  const fits = box.height <= window.innerHeight;
  const offScreen = box.top < 0 || box.bottom > window.innerHeight;
  if (fits && offScreen) {
    frame.scrollIntoView({ block: "center", behavior: behaviour });
  }
}
stepBack.addEventListener("click", showWholeCard);
stepNext.addEventListener("click", showWholeCard);

// Full screen: Fig 2 fills the window, for showing to a class.
const presentButton = document.getElementById("present");
let presenting = false;
function setPresenting(on) {
  presenting = on;
  atomCard.classList.toggle("sp-present", on);
  presentButton.setAttribute("aria-pressed", String(on));
  if (on) {
    presentButton.textContent = "Exit full screen";
    // Ask the browser for real full screen too.  Where that is refused, the figure still fills the window.
    if (atomCard.requestFullscreen) {
      atomCard.requestFullscreen().catch(function () {});
    }
  } else {
    presentButton.textContent = "Full screen";
    if (document.fullscreenElement && document.exitFullscreen) {
      document.exitFullscreen().catch(function () {});
    }
  }
}
presentButton.addEventListener("click", function () {
  setPresenting(!presenting);
});
// Leaving real full screen (for example with Esc) also leaves the presenting layout.
document.addEventListener("fullscreenchange", function () {
  if (!document.fullscreenElement && presenting) {
    setPresenting(false);
  }
});
// While presenting: Esc leaves, and the arrow keys or a clicker step through.
document.addEventListener("keydown", function (event) {
  if (!presenting) {
    return;
  }
  if (event.key === "Escape") {
    setPresenting(false);
  }
  if (event.key === "ArrowRight" || event.key === "PageDown") {
    event.preventDefault();
    showStage(stageIndex + 1);
  }
  if (event.key === "ArrowLeft" || event.key === "PageUp") {
    event.preventDefault();
    showStage(stageIndex - 1);
  }
});
// Outside presenting, the arrow keys work when Fig 2's step panel has the focus.
document.querySelector(".sp-steps").addEventListener("keydown", function (event) {
  if (presenting) {
    return;
  }
  if (event.key === "ArrowRight") {
    showStage(stageIndex + 1);
  }
  if (event.key === "ArrowLeft") {
    showStage(stageIndex - 1);
  }
});

buildAtom();
showStage(0);
new IntersectionObserver(
  function (entries) {
    atom.visible = entries[entries.length - 1].isIntersecting;
    if (atom.visible) {
      runAtom();
    }
  },
  { rootMargin: "100px 0px" },
).observe(atomSvg);

// ---------- Fig 3: elements to try, alone and mixed ----------

const mixer = {
  picked: ["H"],
  kind: "emission",
};
const mixerStack = document.getElementById("mixer");
const mixerReadout = mixerStack.closest(".iso-figure").querySelector("[data-readout]");
const pickButtons = Array.from(document.querySelectorAll("[data-pick]"));
const kindButtons = Array.from(document.querySelectorAll("[data-kind]"));

function drawMixer() {
  mixerStack.textContent = "";
  if (mixer.picked.length === 0) {
    htmlEl("p", "sp-empty", "Choose at least one element to see its spectrum.", mixerStack);
    mixerReadout.textContent = "no element chosen";
    return;
  }
  // Keep the rows in the same order as the buttons.
  const ordered = [];
  for (const element of ELEMENTS) {
    if (mixer.picked.indexOf(element.id) >= 0) {
      ordered.push(element.id);
    }
  }
  for (const id of ordered) {
    makeRow(mixerStack, elementById(id).name, mixer.kind, linesOf(id));
  }
  if (ordered.length > 1) {
    const names = ordered.map((id) => elementById(id).name.toLowerCase());
    makeRow(mixerStack, "Mixture: " + names.join(" + "), mixer.kind, linesOfAll(ordered));
  }
  makeAxis(mixerStack);
  attachGuide(mixerStack, function (nm) {
    const line = nearestLine(linesOfAll(ordered), nm);
    if (line) {
      return describeLine(line);
    }
    return "";
  });
  let count = 0;
  for (const line of linesOfAll(ordered)) {
    if (bandOf(line.nm) === "visible") {
      count += 1;
    }
  }
  mixerReadout.textContent = ordered.join(" + ") + " · " + count + " visible lines";
}
for (const button of pickButtons) {
  button.addEventListener("click", function () {
    const id = button.dataset.pick;
    const at = mixer.picked.indexOf(id);
    if (at >= 0) {
      mixer.picked.splice(at, 1);
      button.setAttribute("aria-pressed", "false");
    } else {
      mixer.picked.push(id);
      button.setAttribute("aria-pressed", "true");
    }
    drawMixer();
  });
}
for (const button of kindButtons) {
  button.addEventListener("click", function () {
    mixer.kind = button.dataset.kind;
    pressOnly(kindButtons, button);
    drawMixer();
  });
}
drawMixer();

// ---------- Decipher the spectrum: questions that get harder ----------

const OTHER = "other"; // the answer "an element that is not in the reference set"
const QUESTIONS = [
  {
    level: "Warm-up",
    prompt: "This lamp contains one element. Which one?",
    sample: ["Na"],
    references: ["H", "Li", "Na"],
    kind: "emission",
    hint: "Find the brightest line in the unknown spectrum. Which reference has a bright line at exactly that wavelength?",
    explain:
      "Sodium. Almost all of its light is in one bright yellow line at 589 nm (really two lines, 589.0 and 589.6 nm, too close to separate here). Hydrogen and lithium have nothing bright there, and their own lines (656 nm for hydrogen, 671 nm for lithium) are missing from the unknown.",
  },
  {
    level: "One element",
    prompt: "One element again, but this time every reference has several lines. Which is it?",
    sample: ["H"],
    references: ["H", "He", "Hg"],
    kind: "emission",
    hint: "Counting lines is not enough. Use the guide line to check that every line in the unknown sits at exactly the same wavelength as a line in your chosen reference.",
    explain:
      "Hydrogen. The unknown has a red line at 656 nm, blue-green at 486 nm and violet lines at 434 and 410 nm, and every one lines up with hydrogen. Helium's strongest line is yellow (588 nm) and mercury's is green (546 nm); the unknown has no line at either.",
  },
  {
    level: "Two elements",
    prompt: "This lamp contains a mixture of two elements. Which two?",
    sample: ["H", "Li"],
    references: ["H", "He", "Li", "Na"],
    kind: "emission",
    hint: "There are two red lines close together. Do they belong to the same element? An element is present only if all of its bright lines appear.",
    explain:
      "Hydrogen and lithium. The two red lines are different elements: 656 nm is hydrogen and 671 nm is lithium. Lithium also gives the orange line at 610 nm, and hydrogen gives 486, 434 and 410 nm. Every line in the unknown is now accounted for, so nothing else is needed. Helium has a red line at 668 nm, between the other two, but nothing in the unknown sits there, and helium's bright yellow line at 588 nm is missing as well. Sodium is ruled out because there is nothing at 589 nm.",
  },
  {
    level: "Two elements, one trap",
    prompt: "Two elements. Be careful: two of the references have a bright yellow line in almost the same place.",
    sample: ["He", "Na"],
    references: ["H", "He", "Li", "Na"],
    kind: "emission",
    hint: "Helium's yellow line is at 587.6 nm and sodium's is at 589.0 nm. A single line cannot settle it. Look for each element's other lines.",
    explain:
      "Helium and sodium. The yellow lines nearly overlap (587.6 nm for helium, 589.0 and 589.6 nm for sodium), so the yellow region alone cannot tell you. Helium is confirmed by its other lines at 447, 502, 668 and 707 nm. Sodium is confirmed because the yellow feature is wider than helium's single line, and by sodium's faint lines at 569 and 616 nm. Hydrogen is out: there is no line at 656 or 486 nm. Lithium is out too: the red line is helium's at 668 nm, not lithium's at 671 nm, and lithium's orange line at 610 nm is missing.",
  },
  {
    level: "Three elements",
    prompt: "A mixture of three elements, with all six references to choose from.",
    sample: ["H", "Li", "Hg"],
    references: ["H", "He", "Li", "Na", "Ne", "Hg"],
    kind: "emission",
    hint: "Work one element at a time. Start with a line that only one element could have made, such as the bright green line, then tick off the rest of that element's lines.",
    explain:
      "Hydrogen, lithium and mercury. The green line at 546 nm can only be mercury, which also explains 405, 436, 577 and 579 nm. The far-red line at 671 nm and the orange line at 610 nm are lithium. That leaves 656, 486 and 410 nm, which are hydrogen. Notice the pair near 435 nm: hydrogen (434.0 nm) and mercury (435.8 nm) sit side by side. Helium is out (nothing at 588 or 502 nm), sodium is out (nothing at 589 nm) and neon is out (its many orange and red lines are missing).",
  },
  {
    level: "A crowded spectrum",
    prompt: "How many elements are in this one? Choose every element you can prove is present.",
    sample: ["Ne", "Hg"],
    references: ["H", "He", "Li", "Na", "Ne", "Hg"],
    kind: "emission",
    hint: "One element here has so many lines that it hides others. Tick it off first, then see which lines are left over. Remember that an element is only present if its strongest lines are there.",
    explain:
      "Neon and mercury. Neon's forest of lines from 585 to 725 nm accounts for everything in the orange and red, and neon also has one green line at 540 nm. The lines left over are 405, 436 and 546 nm (with 577 and 579 nm in the yellow), which are mercury. Sodium is the trap: neon has lines at 585 and 588 nm, right beside sodium's 589 nm, but sodium's faint 569 nm line is missing and the yellow lines match neon exactly. Hydrogen is out because nothing appears at 486 nm or exactly at 656 nm, even though neon has lines on either side of it.",
  },
  {
    level: "Something new",
    prompt: "During the solar eclipse of 1868, astronomers pointed a spectroscope at the glowing gas at the edge of the Sun and saw bright lines like these. Which elements can you identify?",
    sample: ["H", "He"],
    references: ["H", "Li", "Na", "Hg"],
    kind: "emission",
    extra: true,
    hint: "Identify what you can. Then ask: is every line in the unknown explained? Check the yellow line very carefully against sodium.",
    explain:
      "Hydrogen, plus an element that is not in the reference set. Hydrogen explains 656, 486, 434 and 410 nm. The yellow line is at 587.6 nm, close to sodium's 589.0 nm but not at it, and the lines at 447, 502, 668 and 707 nm match none of the references (668 nm is near lithium's 671 nm, but lithium's orange line at 610 nm is missing). In 1868 no element known on Earth had these lines. It was named helium, after helios, the Greek word for the Sun, and it was not found on Earth until 1895.",
  },
  {
    level: "Dark lines",
    prompt: "White light has passed through a cool mixture of gases. The skill is the same, but now the lines are dark. Which elements are in the gas?",
    sample: ["H", "Na", "Li"],
    references: ["H", "He", "Li", "Na", "Ne", "Hg"],
    kind: "absorption",
    hint: "A dark line in an absorption spectrum sits at the same wavelength as the bright line in that element's emission spectrum. Match dark lines to bright lines exactly as before.",
    explain:
      "Hydrogen, sodium and lithium. The dark lines at 656, 486, 434 and 410 nm are hydrogen. The strong dark line at 589 nm is sodium (helium's would be at 587.6 nm, and helium's other lines at 447 and 502 nm are missing). The dark lines at 671 and 610 nm are lithium. This is how the gases in a star's outer layers are identified: the hot interior gives a continuous spectrum and the cooler gas above it removes its own wavelengths.",
  },
];

const quiz = {
  index: 0,
  picked: [], // what the student has ticked on this question
  solved: [], // true for each question answered correctly
  shown: [], // true for each question whose answer has been revealed
};
const quizStack = document.getElementById("quiz-stack");
const quizReadout = quizStack.closest(".iso-figure").querySelector("[data-readout]");
const quizCount = document.getElementById("quiz-count");
const quizPrompt = document.getElementById("quiz-prompt");
const quizChoices = document.getElementById("quiz-choices");
const quizFeedback = document.getElementById("quiz-feedback");
const quizDots = document.getElementById("quiz-dots");

// The right answer to a question, as a sorted list.
function quizAnswer(question) {
  const answer = [];
  for (const id of question.sample) {
    if (question.references.indexOf(id) >= 0) {
      answer.push(id);
    } else if (answer.indexOf(OTHER) < 0) {
      answer.push(OTHER);
    }
  }
  return answer.sort();
}

function choiceName(id) {
  if (id === OTHER) {
    return "An element not shown";
  }
  return elementById(id).name;
}

function drawQuizDots() {
  quizDots.textContent = "";
  QUESTIONS.forEach(function (question, index) {
    const dot = htmlEl("button", "sp-dot", String(index + 1), quizDots);
    dot.type = "button";
    dot.setAttribute("aria-label", "Question " + (index + 1) + ": " + question.level);
    if (index === quiz.index) {
      dot.setAttribute("aria-current", "true");
    }
    if (quiz.solved[index]) {
      dot.dataset.state = "solved";
    } else if (quiz.shown[index]) {
      dot.dataset.state = "shown";
    }
    dot.addEventListener("click", function () {
      showQuestion(index);
    });
  });
}

// The row that shows the student's own mixture, and the parts of it that get redrawn.
const mixture = {
  row: null, // the "Your mixture" row
  chips: null, // where the removable element names go
  strip: null, // the preview spectrum
  empty: null, // the prompt shown while nothing has been added
  references: {}, // reference rows by element symbol
};

// Add an element to the student's mixture, or take it out if it is already there.
function togglePick(id) {
  const at = quiz.picked.indexOf(id);
  if (at >= 0) {
    quiz.picked.splice(at, 1);
  } else {
    quiz.picked.push(id);
  }
  drawMixture();
}

// Redraw the preview: the spectrum that the chosen references would give together.
function drawMixture() {
  const question = QUESTIONS[quiz.index];
  // Only real elements have lines; "an element not shown" adds nothing to the preview.
  const chosen = [];
  for (const id of question.references) {
    if (quiz.picked.indexOf(id) >= 0) {
      chosen.push(id);
    }
  }
  // The preview strip.
  const strip = makeStrip(question.kind, linesOfAll(chosen));
  mixture.strip.replaceWith(strip);
  mixture.strip = strip;
  mixture.empty.hidden = chosen.length > 0;
  mixture.row.dataset.filled = String(chosen.length > 0);
  // One removable name for each element in the mixture.
  mixture.chips.textContent = "";
  for (const id of chosen) {
    const chip = htmlEl("button", "sp-chip", elementById(id).name + " ×", mixture.chips);
    chip.type = "button";
    chip.setAttribute("aria-label", "Remove " + elementById(id).name + " from your mixture");
    chip.addEventListener("click", function () {
      togglePick(id);
    });
  }
  // Mark the references that are in the mixture, and keep the answer buttons in step.
  for (const id in mixture.references) {
    mixture.references[id].dataset.used = String(chosen.indexOf(id) >= 0);
  }
  for (const button of quizChoices.querySelectorAll("button")) {
    const id = button.id.replace("quiz-choice-", "");
    button.setAttribute("aria-pressed", String(quiz.picked.indexOf(id) >= 0));
  }
}

// Let a reference row be dragged.  The picture of its spectrum follows the pointer up and down,
// staying lined up in wavelength, so it can be laid over the unknown to compare.
// Dropping it on the unknown or on "Your mixture" adds it to the mixture.
function makeDraggable(row, id) {
  const label = row.querySelector(".sp-rowlabel");
  const strip = row.querySelector(".sp-strip");
  let drag = null;
  let justDragged = false; // true for a moment after a drag, so the release is not also counted as a tap

  function start(event) {
    // A finger on the strip scrolls the page, so touch dragging starts from the label (the handle).
    const onLabel = event.currentTarget === label;
    if (!onLabel && event.pointerType !== "mouse") {
      return;
    }
    drag = { startY: event.clientY, ghost: null, pointer: event.pointerId, target: event.currentTarget };
    event.currentTarget.setPointerCapture(event.pointerId);
  }

  function move(event) {
    if (!drag || event.pointerId !== drag.pointer) {
      return;
    }
    const moved = event.clientY - drag.startY;
    if (!drag.ghost && Math.abs(moved) > 6) {
      // Start dragging: make a see-through copy of the strip.
      const box = strip.getBoundingClientRect();
      const ghost = strip.cloneNode(true);
      ghost.classList.add("sp-ghost");
      ghost.dataset.kind = strip.dataset.kind;
      ghost.style.left = box.left + "px";
      ghost.style.width = box.width + "px";
      ghost.style.height = box.height + "px";
      document.body.appendChild(ghost);
      drag.ghost = ghost;
      drag.top = box.top;
      row.dataset.dragging = "true";
      mixture.row.dataset.target = "true";
    }
    if (drag.ghost) {
      drag.ghost.style.top = drag.top + moved + "px";
      event.preventDefault();
    }
  }

  function end(event) {
    if (!drag || event.pointerId !== drag.pointer) {
      return;
    }
    const wasDragging = drag.ghost !== null;
    if (wasDragging) {
      // Dropped on the unknown or on the mixture row?
      const ghostBox = drag.ghost.getBoundingClientRect();
      const middle = (ghostBox.top + ghostBox.bottom) / 2;
      const top = quizStack.querySelector("[data-unknown]").getBoundingClientRect().top;
      const bottom = mixture.row.getBoundingClientRect().bottom;
      drag.ghost.remove();
      delete row.dataset.dragging;
      delete mixture.row.dataset.target;
      if (middle >= top && middle <= bottom && quiz.picked.indexOf(id) < 0) {
        togglePick(id);
      }
      justDragged = true;
      setTimeout(function () {
        justDragged = false;
      }, 0);
    }
    drag = null;
  }

  for (const handle of [label, strip]) {
    handle.addEventListener("pointerdown", start);
    handle.addEventListener("pointermove", move);
    handle.addEventListener("pointerup", end);
    handle.addEventListener("pointercancel", end);
  }
  // The label is also a button: Enter, Space or a tap adds or removes the element.
  label.setAttribute("role", "button");
  label.setAttribute("tabindex", "0");
  label.addEventListener("click", function () {
    if (!justDragged) {
      togglePick(id);
    }
  });
  label.addEventListener("keydown", function (event) {
    if (event.key === "Enter" || event.key === " ") {
      event.preventDefault();
      togglePick(id);
    }
  });
}

function showQuestion(index) {
  quiz.index = clamp(index, 0, QUESTIONS.length - 1);
  quiz.picked = [];
  const question = QUESTIONS[quiz.index];
  quizCount.textContent = "Question " + (quiz.index + 1) + " of " + QUESTIONS.length + " · " + question.level;
  quizPrompt.textContent = question.prompt;
  quizFeedback.textContent = "";
  quizFeedback.dataset.state = "";
  // The unknown spectrum on top, then the student's mixture, then one reference for each candidate.
  quizStack.textContent = "";
  const unknown = makeRow(quizStack, "Unknown", question.kind, linesOfAll(question.sample));
  unknown.dataset.unknown = "true";
  mixture.row = makeRow(quizStack, "Your mixture", question.kind, []);
  mixture.row.dataset.mixture = "true";
  mixture.strip = mixture.row.querySelector(".sp-strip");
  mixture.chips = htmlEl("span", "sp-chips", "", mixture.row.querySelector(".sp-rowlabel"));
  mixture.empty = htmlEl("div", "sp-mixempty", "Drag a reference spectrum up to here to add it. Your mixture's spectrum will appear, to compare with the unknown.", mixture.row);
  mixture.references = {};
  for (const id of question.references) {
    const row = makeRow(quizStack, elementById(id).name + " (reference)", question.kind, linesOf(id));
    row.dataset.reference = id;
    mixture.references[id] = row;
    makeDraggable(row, id);
  }
  makeAxis(quizStack);
  attachGuide(quizStack, null);
  // One toggle for each candidate.
  quizChoices.textContent = "";
  const choices = question.references.slice();
  if (question.extra) {
    choices.push(OTHER);
  }
  for (const id of choices) {
    const button = htmlEl("button", "", choiceName(id), quizChoices);
    button.type = "button";
    button.id = "quiz-choice-" + id;
    button.setAttribute("aria-pressed", "false");
    button.addEventListener("click", function () {
      togglePick(id);
    });
  }
  drawMixture();
  document.getElementById("quiz-back").disabled = quiz.index === 0;
  document.getElementById("quiz-next").disabled = quiz.index === QUESTIONS.length - 1;
  drawQuizDots();
  let done = 0;
  for (const solved of quiz.solved) {
    if (solved) {
      done += 1;
    }
  }
  quizReadout.textContent = done + " of " + QUESTIONS.length + " solved";
}

document.getElementById("quiz-check").addEventListener("click", function () {
  const question = QUESTIONS[quiz.index];
  const answer = quizAnswer(question);
  if (quiz.picked.length === 0) {
    quizFeedback.dataset.state = "hint";
    quizFeedback.textContent = "Choose at least one element first.";
    return;
  }
  let right = 0;
  let extra = 0;
  for (const id of quiz.picked) {
    if (answer.indexOf(id) >= 0) {
      right += 1;
    } else {
      extra += 1;
    }
  }
  const missing = answer.length - right;
  if (missing === 0 && extra === 0) {
    quiz.solved[quiz.index] = true;
    quizFeedback.dataset.state = "right";
    quizFeedback.textContent = "Correct. " + question.explain;
  } else {
    let text = "Not yet. ";
    if (right === 1) {
      text += "1 of your choices is right. ";
    }
    if (right > 1) {
      text += right + " of your choices are right. ";
    }
    if (extra === 1) {
      text += "1 of your choices is not in the sample. ";
    }
    if (extra > 1) {
      text += extra + " of your choices are not in the sample. ";
    }
    if (missing > 0) {
      text += "Something is still missing. ";
    }
    quizFeedback.dataset.state = "hint";
    quizFeedback.textContent = text + "Hint: " + question.hint;
  }
  drawQuizDots();
  let done = 0;
  for (const solved of quiz.solved) {
    if (solved) {
      done += 1;
    }
  }
  quizReadout.textContent = done + " of " + QUESTIONS.length + " solved";
});
document.getElementById("quiz-show").addEventListener("click", function () {
  const question = QUESTIONS[quiz.index];
  quiz.shown[quiz.index] = true;
  quizFeedback.dataset.state = "shown";
  quizFeedback.textContent = "Answer: " + question.explain;
  // Build the answer as the mixture, so it can be seen against the unknown.
  quiz.picked = quizAnswer(question).slice();
  drawMixture();
  drawQuizDots();
});
document.getElementById("quiz-back").addEventListener("click", function () {
  showQuestion(quiz.index - 1);
});
document.getElementById("quiz-next").addEventListener("click", function () {
  showQuestion(quiz.index + 1);
});
showQuestion(0);

// ---------- the GCSE / A-level switch ----------

const courseButtons = Array.from(document.querySelectorAll("[data-course-pick]"));
function showCourse() {
  pageRoot.dataset.course = course;
  for (const button of courseButtons) {
    let pressed = "false";
    if (button.dataset.coursePick === course) {
      pressed = "true";
    }
    button.setAttribute("aria-pressed", pressed);
  }
}
for (const button of courseButtons) {
  button.addEventListener("click", function () {
    if (button.dataset.coursePick === course) {
      return;
    }
    course = button.dataset.coursePick;
    try {
      localStorage.setItem("jsh-spectra-course", course);
    } catch (error) {
      // Not saved; the choice still applies to this visit.
    }
    showCourse();
    // Redraw the parts whose labels and wording depend on the course.
    atomSvg.textContent = "";
    buildAtom();
    showStage(stageIndex);
    drawMixer();
  });
}
showCourse();

// For checking the page: lets a test put the figures in a known state.
window.__spectra = { bench: bench, benchChanged: benchChanged, atom: atom, showStage: showStage, showQuestion: showQuestion, QUESTIONS: QUESTIONS, quizAnswer: quizAnswer };
