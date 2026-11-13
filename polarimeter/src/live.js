// Live layer of the polarimeter.
// The build script puts these names in scope before this file:
//   iso, cameraOf, towardViewer, translateAlong   (from the drawing kit)
//   M                               (the physics, model.mjs)
//   SCENE                           (the part builders, scene.mjs)
//   P                               (the camera now; it starts as the walkthrough's camera)
//   WIDTH, HEIGHT, AXIS_Z, X, MOVES, PINS (the bench's dimensions and parts)

const stage = document.querySelector(".iso-stage");
const svg = stage.querySelector("svg");
const readout = document.querySelector("[data-readout]");
const still = matchMedia("(prefers-reduced-motion: reduce)");

const DEG = Math.PI / 180;
const WAVE_HEIGHT = 8.5; // world units
const WAVE_LENGTH = 15; // world units

// ---------- state ----------

const state = {
  sample: M.SAMPLES[0],
  concentration: 0.5,
  reading: 90, // the analyser's scale reading, in degrees
  readingTarget: 90,
  alpha: 0, // the rotation the beam is drawn with; eases to the true value
  apart: false,
  apartTime: 0, // 0 = assembled, 1 = fully apart
  focus: [], // families to highlight; empty means all
  step: 0,
};

// The camera: where the bench is seen from. The targets are what it eases to.
const view = {
  azimuth: SCENE.HOME.azimuth,
  elevation: SCENE.HOME.elevation,
  azimuthTarget: SCENE.HOME.azimuth,
  elevationTarget: SCENE.HOME.elevation,
  drawnAzimuth: SCENE.HOME.azimuth, // what the bench was last drawn for
  drawnElevation: SCENE.HOME.elevation,
  drawnApart: 0,
};

// True while the eyepiece end of the bench is the nearer end.
function eyepieceEndNearer() {
  return towardViewer(P)[0] >= 0;
}

function trueAlpha() {
  return M.rotation(state.sample, state.concentration);
}

// ---------- helpers ----------

function fix(value) {
  return (Math.round(value * 10) / 10).toString();
}

function clamp(value, low, high) {
  return Math.min(high, Math.max(low, value));
}

function smoothstep(value) {
  const t = clamp(value, 0, 1);
  return t * t * (3 - 2 * t);
}

// A unit direction in the plane across the beam, at an angle from vertical.
// Positive angles lean towards -y. In this drawing that is clockwise for
// someone at the eyepiece looking towards the lamp, and it also looks
// clockwise on screen, because we see the dial from the eyepiece side.
function across(angle) {
  return [0, -Math.sin(angle * DEG), Math.cos(angle * DEG)];
}

// A point on the beam's axis at x, moved `distance` in the plane direction.
function onBeam(x, angle, distance) {
  const direction = across(angle);
  return [x, direction[1] * distance, AXIS_Z + direction[2] * distance];
}

function pathThrough(points) {
  let d = "";
  for (let index = 0; index < points.length; index++) {
    const spot = iso(points[index], P);
    if (index === 0) {
      d += "M";
    } else {
      d += "L";
    }
    d += fix(spot[0]) + " " + fix(spot[1]);
  }
  return d;
}

// ---------- the light ----------

// One travelling wave from x0 to x1.
//   planeAt(x) gives the plane's angle at x; strength scales the height.
function waveMarkup(x0, x1, planeAt, strength, phase, className) {
  const points = [];
  const steps = Math.max(2, Math.round((x1 - x0) / 1.2));
  for (let index = 0; index <= steps; index++) {
    const x = x0 + ((x1 - x0) * index) / steps;
    const swing = Math.sin((x / WAVE_LENGTH) * Math.PI * 2 - phase);
    points.push(onBeam(x, planeAt(x), WAVE_HEIGHT * strength * swing));
  }
  return '<path class="' + className + '" d="' + pathThrough(points) + '"/>';
}

// The straight line of the ray itself.
function rayMarkup(x0, x1) {
  return '<path class="pm-ray" d="' + pathThrough([[x0, 0, AXIS_Z], [x1, 0, AXIS_Z]]) + '"/>';
}

// A double-headed arrow across the beam: the plane of polarisation at x.
function planeMarkup(x, angle, strength) {
  const half = (WAVE_HEIGHT + 3.5) * Math.abs(strength);
  if (half < 1.6) {
    return "";
  }
  const top = onBeam(x, angle, half);
  const bottom = onBeam(x, angle, -half);
  const side = across(angle + 90);
  let d = pathThrough([bottom, top]);
  for (const end of [1, -1]) {
    const tip = onBeam(x, angle, half * end);
    const back = onBeam(x, angle, (half - 2.6) * end);
    const left = [back[0], back[1] + side[1] * 1.7, back[2] + side[2] * 1.7];
    const right = [back[0], back[1] - side[1] * 1.7, back[2] - side[2] * 1.7];
    d += pathThrough([left, tip, right]);
  }
  return '<path class="pm-plane" d="' + d + '"/>';
}

// These groups are replaced whenever the bench is redrawn from a new angle,
// so bindScene() looks them up again each time.
const sceneGroup = svg.querySelector('[data-part="scene"]');
let beamGroups = [];
let grainGroup = null;
let pointerGroup = null;
let pinGroup = null;
let movers = [];

function bindScene() {
  beamGroups = [];
  for (let index = 0; index < 6; index++) {
    beamGroups.push(svg.querySelector('[data-beam="' + index + '"]'));
  }
  grainGroup = svg.querySelector('[data-live="grain"]');
  pointerGroup = svg.querySelector('[data-live="pointer"]');
  pinGroup = svg.querySelector('[data-live="pins"]');
  movers = [];
  for (const group of svg.querySelectorAll("[data-move]")) {
    movers.push({ group: group, move: MOVES[group.dataset.move], family: group.dataset.family, progress: 0 });
  }
}

bindScene();

// Redraw every part for the camera's current angles.
function redrawScene() {
  // The picture makes room for the parts as they come apart.
  const apart = smoothstep(state.apartTime);
  P = SCENE.projectionFor(view.azimuth, view.elevation, apart);
  sceneGroup.innerHTML = SCENE.build(P).join("");
  bindScene();
  view.drawnAzimuth = view.azimuth;
  view.drawnElevation = view.elevation;
  view.drawnApart = state.apartTime;
}

function unpolarisedMarkup(x0, x1, phase) {
  let out = rayMarkup(x0, x1);
  // Three of the many planes the light oscillates in.
  out += waveMarkup(x0, x1, () => 0, 0.85, phase, "pm-wave pm-wave-soft");
  out += waveMarkup(x0, x1, () => 60, 0.85, phase + 2.1, "pm-wave pm-wave-soft");
  out += waveMarkup(x0, x1, () => 120, 0.85, phase + 4.2, "pm-wave pm-wave-soft");
  return out;
}

function drawBeam(phase) {
  const alpha = state.alpha;
  const tubeLength = X.tubeEnd - X.tubeStart;

  // Angle of the plane at a point inside the tube: it grows steadily along it.
  function planeInTube(x) {
    return alpha * clamp((x - X.tubeStart) / tubeLength, 0, 1);
  }

  beamGroups[0].innerHTML = unpolarisedMarkup(X.lamp + 20, X.lens - 2.5, phase);
  beamGroups[1].innerHTML = unpolarisedMarkup(X.lens + 5, X.polariser - 3, phase);

  let afterPolariser = rayMarkup(X.polariser + 6.5, X.tubeStart - 4);
  afterPolariser += waveMarkup(X.polariser + 6.5, X.tubeStart - 4, () => 0, 1, phase, "pm-wave");
  afterPolariser += planeMarkup(X.polariser + 16, 0, 1);
  beamGroups[2].innerHTML = afterPolariser;

  let inTube = rayMarkup(X.tubeStart, X.tubeEnd);
  inTube += waveMarkup(X.tubeStart, X.tubeEnd, planeInTube, 0.8, phase, "pm-wave");
  for (const x of [-27, -9, 9, 27]) {
    inTube += planeMarkup(x, planeInTube(x), 0.62);
  }
  beamGroups[3].innerHTML = inTube;

  let afterTube = rayMarkup(X.tubeEnd + 4, X.analyser - 3);
  afterTube += waveMarkup(X.tubeEnd + 4, X.analyser - 3, () => alpha, 1, phase, "pm-wave");
  afterTube += planeMarkup(X.tubeEnd + 16, alpha, 1);
  beamGroups[4].innerHTML = afterTube;

  // What is left after the analyser oscillates along the analyser's own direction.
  const passed = M.amplitudeThrough(state.reading, alpha);
  const analyserPlane = 90 + state.reading;
  // The ray itself fades with the fraction of the light that passes.
  let afterAnalyser = rayMarkup(X.analyser + 9.5, X.eyepiece - 9).replace("<path ", '<path opacity="' + (passed * passed).toFixed(2) + '" ');
  // With almost nothing passing, the wave itself fades away instead of leaving a flat line.
  const waveShows = clamp(Math.abs(passed) * 5, 0, 1);
  afterAnalyser += waveMarkup(X.analyser + 9.5, X.eyepiece - 9, () => analyserPlane, passed, phase, "pm-wave").replace("<path ", '<path opacity="' + waveShows.toFixed(2) + '" ');
  afterAnalyser += planeMarkup(X.analyser + 20, analyserPlane, passed);
  beamGroups[5].innerHTML = afterAnalyser;
}

// ---------- the analyser's moving marks ----------


function drawAnalyser() {
  // Fine lines on the filter show the direction it lets light oscillate in.
  const direction = 90 + state.reading;
  const nearer = eyepieceEndNearer();
  // The grain is drawn on whichever face of the filter is towards the viewer.
  let face = X.analyser + 3;
  if (nearer) {
    face = X.analyser + 4.5;
  }
  let d = "";
  for (const offset of [-9, -6, -3, 0, 3, 6, 9]) {
    const reach = Math.sqrt(13 * 13 - offset * offset) - 0.8;
    const side = across(direction + 90);
    const middle = [face, side[1] * offset, AXIS_Z + side[2] * offset];
    const along = across(direction);
    const from = [face, middle[1] - along[1] * reach, middle[2] - along[2] * reach];
    const to = [face, middle[1] + along[1] * reach, middle[2] + along[2] * reach];
    d += pathThrough([from, to]);
  }
  grainGroup.innerHTML = '<path class="pm-grain" d="' + d + '"/>';

  // The pointer on the collar reads against the fixed scale behind it.
  // It is on the eyepiece side, so it cannot be seen from the lamp end.
  if (!nearer) {
    pointerGroup.innerHTML = "";
    return;
  }
  const collarFace = X.analyser + 9.5;
  const inner = onBeam(collarFace, state.reading, 11.5);
  const outer = onBeam(collarFace, state.reading, 18.5);
  const spot = iso(outer, P);
  let out = '<path class="pm-pointer" d="' + pathThrough([inner, outer]) + '"/>';
  out += '<circle class="pm-pointer-dot" cx="' + fix(spot[0]) + '" cy="' + fix(spot[1]) + '" r="1.5"/>';
  pointerGroup.innerHTML = out;
}

// ---------- taking it apart ----------


function progressOf(name) {
  const move = MOVES[name];
  return smoothstep(state.apartTime * 1.25 - move.delay);
}

function placeParts() {
  for (const mover of movers) {
    const progress = smoothstep(state.apartTime * 1.25 - mover.move.delay);
    mover.progress = progress;
    const offset = [mover.move.offset[0] * progress, mover.move.offset[1] * progress, mover.move.offset[2] * progress];
    mover.group.setAttribute("transform", translateAlong(P, offset));
    let opacity = 1;
    if (state.focus.length > 0 && !state.focus.includes(mover.family)) {
      opacity = 0.45;
    }
    mover.group.style.opacity = String(opacity);
  }
  // The light is only shown while the instrument is together.
  const light = clamp(1 - state.apartTime * 5, 0, 1);
  for (const group of beamGroups) {
    group.style.opacity = String(light);
  }
}

// ---------- the numbered pins ----------


function drawPins() {
  let out = "";
  for (const pin of PINS) {
    const progress = progressOf(pin.rides);
    const move = MOVES[pin.rides];
    const foot = iso([pin.at[0] + move.offset[0] * progress, pin.at[1] + move.offset[1] * progress, pin.at[2] + move.offset[2] * progress], P);
    let className = "pm-pin";
    if (state.focus.includes(pin.family)) {
      className += " pm-pin-on";
    }
    out += '<g class="' + className + '">';
    // Most pins stand on a short stem; a pin can ask for a longer one to clear its neighbour.
    let stem = 9;
    if (pin.stem) {
      stem = pin.stem;
    }
    const head = foot[1] - stem - 8;
    out += '<path d="M' + fix(foot[0]) + " " + fix(foot[1]) + "L" + fix(foot[0]) + " " + fix(foot[1] - stem) + '"/>';
    out += '<circle cx="' + fix(foot[0]) + '" cy="' + fix(head) + '" r="8"/>';
    out += '<text x="' + fix(foot[0]) + '" y="' + fix(head) + '">' + pin.number + "</text>";
    out += "</g>";
  }
  pinGroup.innerHTML = out;
}

// ---------- words and numbers ----------

const nodes = {
  concentration: document.querySelector("[data-value='concentration']"),
  analyser: document.querySelector("[data-value='analyser']"),
  brightness: document.querySelector("[data-value='brightness']"),
  verdict: document.querySelector("[data-value='verdict']"),
  sum: document.querySelector("[data-value='sum']"),
  sampleNote: document.querySelector("[data-value='sample-note']"),
  eye: document.querySelector("[data-eye]"),
  concentrationSlider: document.querySelector("[data-control='concentration']"),
  analyserSlider: document.querySelector("[data-control='analyser']"),
  explode: document.querySelector("[data-action='explode']"),
};

function number(text) {
  return "<mn>" + text + "</mn>";
}

let lastWords = "";

function showNumbers() {
  const alpha = trueAlpha();
  const light = M.brightness(state.reading, state.alpha);
  const percent = Math.round(light * 100);

  // The eyepiece view: sodium yellow, dimmed by the fraction of light that passes.
  const shade = Math.pow(light, 1 / 2.2);
  const red = Math.round(255 * shade);
  const green = Math.round(190 * shade);
  const blue = Math.round(40 * shade);
  nodes.eye.style.background = "rgb(" + red + "," + green + "," + blue + ")";

  const words = [M.sayAngle(state.reading), percent, state.sample.id, state.concentration].join("|");
  if (words === lastWords) {
    return;
  }
  lastWords = words;

  readout.textContent = "analyser " + M.sayAngle(state.reading) + " · " + percent + "% of the light passes";
  nodes.analyser.textContent = M.sayAngle(state.reading);
  nodes.concentration.textContent = state.concentration.toFixed(2) + " g cm⁻³";
  nodes.brightness.textContent = percent + "% of the light";

  let verdict = "Turn the analyser to find the darkest point.";
  if (light < 0.0005) {
    verdict = "Darkest. The scale reads the rotation: " + M.sayAngle(state.reading) + ".";
  } else if (light < 0.01) {
    verdict = "Nearly dark. Use the ± 0.5° buttons.";
  }
  nodes.verdict.textContent = verdict;

  let specific = M.sayAngle(state.sample.specific).replace("°", "");
  if (state.sample.specific === 0) {
    specific = "0";
  }
  let sum = "<math><mi>α</mi><mo>=</mo>";
  sum += number(specific) + "<mo>×</mo>" + number(M.TUBE_LENGTH_DM.toFixed(1)) + "<mo>×</mo>" + number(state.concentration.toFixed(2));
  sum += "<mo>=</mo>" + number(M.sayAngle(alpha)) + "</math>";
  nodes.sum.innerHTML = sum;

  let note = state.sample.note;
  if (state.sample.specific !== 0) {
    if (state.sample.real) {
      note += " Measured specific rotation.";
    } else {
      note += " Example specific rotation.";
    }
  }
  nodes.sampleNote.textContent = note + " l is the tube length in dm, c the concentration in g cm⁻³.";
  stage.setAttribute("aria-valuetext", readout.textContent);
}

function markSample() {
  for (const button of document.querySelectorAll("[data-sample]")) {
    let pressed = "false";
    if (button.dataset.sample === state.sample.id) {
      pressed = "true";
    }
    button.setAttribute("aria-pressed", pressed);
  }
}

function markPins() {
  for (const button of document.querySelectorAll("[data-pin]")) {
    let pressed = "false";
    if (state.focus.length === 1 && state.focus[0] === button.dataset.pin) {
      pressed = "true";
    }
    button.setAttribute("aria-pressed", pressed);
  }
}

// ---------- zooming in on the part a step is about ----------

const WHOLE = [0, 0, WIDTH, HEIGHT];
const zoom = {
  on: true,
  box: [0, 0, WIDTH, HEIGHT], // the viewBox now: x, y, width, height
  target: [0, 0, WIDTH, HEIGHT],
};

// The viewBox that frames a stretch of the bench.
//   frame = [first x, last x, top z], in world units
function boxFor(frame) {
  // Project the corners of the region to find its extent on screen.
  let left = Infinity;
  let right = -Infinity;
  let top = Infinity;
  let bottom = -Infinity;
  for (const x of [frame[0], frame[1]]) {
    for (const y of [-30, 30]) {
      for (const z of [-10, frame[2]]) {
        const spot = iso([x, y, z], P);
        left = Math.min(left, spot[0]);
        right = Math.max(right, spot[0]);
        top = Math.min(top, spot[1]);
        bottom = Math.max(bottom, spot[1]);
      }
    }
  }
  // Add a margin, then widen or heighten to the figure's own proportions.
  const margin = 14;
  let width = right - left + margin * 2;
  let height = bottom - top + margin * 2;
  const shape = WIDTH / HEIGHT;
  if (width / height < shape) {
    width = height * shape;
  } else {
    height = width / shape;
  }
  // Never zoom out further than the whole figure.
  if (width >= WIDTH) {
    return WHOLE;
  }
  const centreX = (left + right) / 2;
  const centreY = (top + bottom) / 2;
  return [centreX - width / 2, centreY - height / 2, width, height];
}

function aimZoom() {
  const frame = STEPS[state.step].frame;
  if (zoom.on && frame && !state.apart) {
    zoom.target = boxFor(frame);
  } else {
    zoom.target = WHOLE;
  }
}

// ---------- the walkthrough ----------

const STEPS = [
  {
    title: "The whole instrument",
    text: "This is a polarimeter. It measures how far a substance rotates plane-polarised light. Drag the bench to turn it, take it apart to see each piece, or tap a numbered part below the picture. Press Next to follow the light through it, one part at a time.",
    focus: [], sample: "water", concentration: 0.5, reading: 90,
    frame: null,
  },
  {
    title: "Light from the lamp",
    text: "A sodium lamp gives light of a single wavelength (589 nm), so all of it is rotated by the same amount. The lens makes the beam parallel. This light is unpolarised: it oscillates in every plane at right angles to its direction of travel.",
    focus: ["lamp", "lens"], sample: "water", concentration: 0.5, reading: 90,
    frame: [-166, -58, 96],
  },
  {
    title: "The polariser",
    text: "The polariser is a filter that only lets through light oscillating in one plane: here, vertical. The light that leaves it is plane-polarised.",
    focus: ["polariser"], sample: "water", concentration: 0.5, reading: 90,
    frame: [-112, -28, 92],
  },
  {
    title: "The analyser",
    text: "The analyser is a second polarising filter, and it can be turned. When its direction is at 90° to the polariser's, no light passes and the view through the eyepiece goes dark. With water in the tube that happens at 0° on the scale.",
    focus: ["analyser", "scale", "eyepiece"], sample: "water", concentration: 0.5, reading: 0,
    frame: [34, 138, 100],
  },
  {
    title: "An optically active sample",
    text: "Now the tube holds a solution of one enantiomer. Its chiral molecules rotate the plane of polarisation, a little more for every molecule the light meets. The light reaching the analyser is no longer at 90° to it, so some gets through.",
    focus: ["tube"], sample: "plus", concentration: 0.5, reading: 0,
    frame: [-74, 88, 96],
  },
  {
    title: "Measuring the rotation",
    text: "Turn the analyser until the view is darkest again. The angle it had to turn is the rotation: +30.0°, clockwise. A substance that rotates the plane clockwise is dextrorotatory, labelled (+).",
    focus: ["analyser", "scale"], sample: "plus", concentration: 0.5, reading: 30,
    frame: [34, 138, 100],
  },
  {
    title: "The other enantiomer",
    text: "The mirror-image isomer rotates the plane by the same angle in the opposite direction: −30.0°, anticlockwise. It is laevorotatory, labelled (−). Rotating plane-polarised light in opposite directions is how two enantiomers are told apart.",
    focus: ["tube", "analyser", "scale"], sample: "minus", concentration: 0.5, reading: -30,
    frame: [-46, 138, 100],
  },
  {
    title: "A racemic mixture",
    text: "A racemic mixture contains equal amounts of both enantiomers. Each clockwise rotation is cancelled by an equal anticlockwise one, so there is no overall rotation: the mixture is optically inactive, and the view is dark at 0° again.",
    focus: ["tube"], sample: "racemic", concentration: 0.5, reading: 0,
    frame: [-46, 138, 100],
  },
  {
    title: "Your turn",
    text: "Choose a sample, change its concentration and find the dark position yourself. The rotation is proportional to the concentration and to the length of the tube. Then take the instrument apart to see each piece.",
    focus: [], sample: "sucrose", concentration: 0.5, reading: 0,
    frame: null,
  },
];

const walk = {
  count: document.querySelector("[data-walk='count']"),
  title: document.querySelector("[data-walk='title']"),
  text: document.querySelector("[data-walk='text']"),
  back: document.querySelector("button[data-walk='back']"),
  next: document.querySelector("button[data-walk='next']"),
};

// Turn the bench back to the angle the walkthrough uses, by the shorter way round.
function homeView() {
  let azimuth = SCENE.HOME.azimuth;
  while (azimuth - view.azimuth > 180) {
    azimuth = azimuth - 360;
  }
  while (view.azimuth - azimuth > 180) {
    azimuth = azimuth + 360;
  }
  view.azimuthTarget = azimuth;
  view.elevationTarget = SCENE.HOME.elevation;
}

function setSample(id) {
  state.sample = M.SAMPLES.find((sample) => sample.id === id);
  markSample();
}

function showStep(index) {
  state.step = clamp(index, 0, STEPS.length - 1);
  const step = STEPS[state.step];
  if (state.step === 0) {
    walk.count.textContent = "Overview";
  } else {
    walk.count.textContent = "Step " + state.step + " of " + (STEPS.length - 1);
  }
  // Each step is shown from the same angle, so the zoom frames what it describes.
  homeView();
  walk.title.textContent = step.title;
  walk.text.textContent = step.text;
  walk.back.disabled = state.step === 0;
  walk.next.disabled = state.step === STEPS.length - 1;
  state.focus = step.focus;
  setSample(step.sample);
  state.concentration = step.concentration;
  state.readingTarget = step.reading;
  nodes.concentrationSlider.value = String(state.concentration);
  if (state.apart) {
    toggleApart();
  }
  markPins();
  aimZoom();
  redraw();
}

walk.back.addEventListener("click", () => showStep(state.step - 1));
walk.next.addEventListener("click", () => showStep(state.step + 1));

// ---------- controls ----------

for (const button of document.querySelectorAll("[data-sample]")) {
  button.addEventListener("click", () => {
    setSample(button.dataset.sample);
    redraw();
  });
}

for (const button of document.querySelectorAll("[data-pin]")) {
  button.addEventListener("click", () => {
    const family = button.dataset.pin;
    if (state.focus.length === 1 && state.focus[0] === family) {
      state.focus = [];
    } else {
      state.focus = [family];
    }
    markPins();
    redraw();
  });
}

nodes.concentrationSlider.addEventListener("input", () => {
  state.concentration = Number(nodes.concentrationSlider.value);
  redraw();
});

function setReading(value) {
  const snapped = Math.round(clamp(value, -90, 90) * 10) / 10;
  state.readingTarget = snapped;
  state.reading = snapped;
  redraw();
}

nodes.analyserSlider.addEventListener("input", () => {
  setReading(Number(nodes.analyserSlider.value));
});

document.querySelector("[data-action='nudge-up']").addEventListener("click", () => {
  setReading(state.readingTarget + 0.5);
});

document.querySelector("[data-action='nudge-down']").addEventListener("click", () => {
  setReading(state.readingTarget - 0.5);
});

function toggleApart() {
  state.apart = !state.apart;
  if (state.apart) {
    nodes.explode.textContent = "Put together";
  } else {
    nodes.explode.textContent = "Take apart";
  }
  nodes.explode.setAttribute("aria-pressed", String(state.apart));
  // The whole bench is shown while it is apart.
  aimZoom();
}

const zoomButton = document.querySelector("[data-action='zoom']");

zoomButton.addEventListener("click", () => {
  zoom.on = !zoom.on;
  zoomButton.setAttribute("aria-pressed", String(zoom.on));
  aimZoom();
  redraw();
});

nodes.explode.addEventListener("click", () => {
  toggleApart();
  // Every part is shown at full strength while the instrument is apart.
  state.focus = [];
  markPins();
  redraw();
});

document.querySelector("[data-action='theme']").addEventListener("click", () => {
  let next = "light";
  if (document.body.dataset.theme === "light") {
    next = "dark";
  }
  document.body.dataset.theme = next;
  try {
    localStorage.setItem("jsh-theme", next);
  } catch (error) {
    // Storage can be unavailable; the theme still changes for this visit.
  }
});

try {
  const saved = localStorage.getItem("jsh-theme");
  if (saved === "light" || saved === "dark") {
    document.body.dataset.theme = saved;
  }
} catch (error) {
  // No saved theme: keep the page's own.
}

// ---------- pointer and keys: turn and tilt the bench ----------

let hold = null;

function tiltBy(amount) {
  view.elevationTarget = clamp(view.elevationTarget + amount, SCENE.TILT_RANGE[0], SCENE.TILT_RANGE[1]);
  redraw();
}

stage.addEventListener("pointerdown", (event) => {
  hold = { x: event.clientX, y: event.clientY, azimuth: view.azimuth, elevation: view.elevation, touch: event.pointerType === "touch", turning: false };
});

stage.addEventListener("pointermove", (event) => {
  if (!hold) {
    return;
  }
  const dx = event.clientX - hold.x;
  const dy = event.clientY - hold.y;
  if (!hold.turning) {
    // A mostly sideways move starts a turn; on a touch screen an up-and-down
    // move is left alone so the page can still scroll.
    if (Math.abs(dx) < 6 && Math.abs(dy) < 6) {
      return;
    }
    if (hold.touch && Math.abs(dy) > Math.abs(dx)) {
      hold = null;
      return;
    }
    hold.turning = true;
    stage.setPointerCapture(event.pointerId);
  }
  view.azimuth = hold.azimuth + dx * 0.45;
  view.azimuthTarget = view.azimuth;
  if (!hold.touch) {
    // With a mouse, dragging up and down tilts the bench as well.
    view.elevation = clamp(hold.elevation + dy * 0.3, SCENE.TILT_RANGE[0], SCENE.TILT_RANGE[1]);
    view.elevationTarget = view.elevation;
  }
  redraw();
});

function release() {
  hold = null;
}

stage.addEventListener("pointerup", release);
stage.addEventListener("pointercancel", release);

stage.addEventListener("keydown", (event) => {
  let used = true;
  if (event.key === "ArrowRight") {
    view.azimuthTarget = view.azimuthTarget + 15;
  } else if (event.key === "ArrowLeft") {
    view.azimuthTarget = view.azimuthTarget - 15;
  } else if (event.key === "ArrowUp") {
    tiltBy(8);
  } else if (event.key === "ArrowDown") {
    tiltBy(-8);
  } else {
    used = false;
  }
  if (used) {
    event.preventDefault();
    redraw();
  }
});

document.querySelector("[data-action='tilt-up']").addEventListener("click", () => tiltBy(8));
document.querySelector("[data-action='tilt-down']").addEventListener("click", () => tiltBy(-8));

document.querySelector("[data-action='reset-view']").addEventListener("click", () => {
  homeView();
  redraw();
});

// ---------- the frame loop ----------

let frame = 0;
let last = 0;
let visible = true;
let phase = 0;

function ease(current, target, dt, seconds) {
  if (still.matches) {
    return target;
  }
  const next = current + (target - current) * (1 - Math.exp(-dt / seconds));
  if (Math.abs(target - next) < 0.01) {
    return target;
  }
  return next;
}

function drawAll() {
  placeParts();
  drawBeam(phase);
  drawAnalyser();
  drawPins();
  showNumbers();
  if (document.activeElement !== nodes.analyserSlider) {
    nodes.analyserSlider.value = String(state.reading);
  }
}

function tick(now) {
  let dt = 1 / 60;
  if (last) {
    dt = Math.min((now - last) / 1000, 1 / 30);
  }
  last = now;

  state.reading = ease(state.reading, state.readingTarget, dt, 0.28);
  state.alpha = ease(state.alpha, trueAlpha(), dt, 0.25);

  // Coming apart and going back together take about a second each way.
  let apartGoal = 0;
  if (state.apart) {
    apartGoal = 1;
  }
  if (still.matches) {
    state.apartTime = apartGoal;
  } else if (state.apartTime < apartGoal) {
    state.apartTime = Math.min(apartGoal, state.apartTime + dt / 1.1);
  } else if (state.apartTime > apartGoal) {
    state.apartTime = Math.max(apartGoal, state.apartTime - dt / 1.1);
  }

  // The camera eases to its targets; the bench is redrawn only when it has moved.
  view.azimuth = ease(view.azimuth, view.azimuthTarget, dt, 0.25);
  view.elevation = ease(view.elevation, view.elevationTarget, dt, 0.25);
  const cameraSettled = view.azimuth === view.azimuthTarget && view.elevation === view.elevationTarget;
  if (view.azimuth !== view.drawnAzimuth || view.elevation !== view.drawnElevation || state.apartTime !== view.drawnApart) {
    redrawScene();
    aimZoom();
  }

  // The view glides to the part the step is about.
  let zoomSettled = true;
  for (let index = 0; index < 4; index++) {
    zoom.box[index] = ease(zoom.box[index], zoom.target[index], dt, 0.3);
    if (zoom.box[index] !== zoom.target[index]) {
      zoomSettled = false;
    }
  }
  svg.setAttribute("viewBox", zoom.box.map((value) => value.toFixed(2)).join(" "));

  const settled = cameraSettled && zoomSettled && state.reading === state.readingTarget && state.alpha === trueAlpha() && state.apartTime === apartGoal;

  // The wave travels towards the eyepiece.
  if (!still.matches) {
    phase = phase + dt * 5;
  }

  drawAll();

  const keepGoing = visible && (!still.matches || !settled);
  if (keepGoing) {
    frame = requestAnimationFrame(tick);
  } else {
    frame = 0;
  }
}

function redraw() {
  if (!frame && visible) {
    last = 0;
    frame = requestAnimationFrame(tick);
  }
}

new IntersectionObserver((entries) => {
  visible = entries[entries.length - 1].isIntersecting;
  if (visible) {
    redraw();
  }
}).observe(stage);

// ---------- start ----------

showStep(0);
zoom.box = zoom.target.slice();
state.reading = state.readingTarget;
state.alpha = trueAlpha();
drawAll();
redraw();
