// Live layer of the molecule stand.
// The build script puts these names in scope before this file:
//   iso, depthOf, cameraOf  (from the drawing kit)
//   M                       (the VSEPR model, model.mjs)
//   P, CENTRE, ARC_R, BOND, TABLE_TOP, TABLE_R  (the stand's dimensions)

const stage = document.querySelector(".iso-stage");
const svg = stage.querySelector("svg");
const liveGroup = svg.querySelector('[data-part="live"]');
const readout = document.querySelector("[data-readout]");
const still = matchMedia("(prefers-reduced-motion: reduce)");

// The direction from the model towards the viewer (azimuth 45, elevation 30).
const CAMERA = cameraOf(P);
const TOWARD_VIEWER = [CAMERA.cosA * CAMERA.cosE, CAMERA.sinA * CAMERA.cosE, CAMERA.sinE];

// Screen pixels (in viewBox units) for one world unit.
const K = cameraOf(P).k;

// ---------- state ----------

const view = {
  yaw: -35,
  tilt: 0,
  spin: 0,
  tiltTarget: 0,
  spinTarget: 0,
};

const options = {
  auto: !still.matches,
  lonePairs: true,
  labels: true,
};

let molecule = M.MOLECULES[4];
let waiting = null; // a molecule that loads once the old one has folded away
let mount = molecule.mount;
let centralElement = molecule.central;
let selection = [molecule.measure[0], molecule.measure[1]];

// Six slots, one per possible electron pair.
// bondAmount and loneAmount run from 0 (absent) to 1 (fully there).
const slots = [];
for (let i = 0; i < 6; i++) {
  slots.push({
    dir: [0, 0, 1],
    dirTarget: [0, 0, 1],
    bondAmount: 0,
    bondTarget: 0,
    loneAmount: 0,
    loneTarget: 0,
    element: "H",
    kind: "single",
  });
}

// ---------- loading a molecule ----------

function aimSlotsAt(next, snapDirections) {
  for (let i = 0; i < slots.length; i++) {
    const slot = slots[i];
    const pair = next.pairs[i];
    if (!pair) {
      slot.bondTarget = 0;
      slot.loneTarget = 0;
      continue;
    }
    slot.dirTarget = pair.dir;
    if (snapDirections) {
      slot.dir = pair.dir;
    }
    if (pair.type === "bond") {
      slot.bondTarget = 1;
      slot.loneTarget = 0;
      slot.element = pair.element;
      slot.kind = pair.kind;
    } else {
      slot.bondTarget = 0;
      slot.loneTarget = 1;
    }
  }
}

function install(next, snapDirections) {
  molecule = next;
  mount = next.mount;
  centralElement = next.central;
  selection = [next.measure[0], next.measure[1]];
  aimSlotsAt(next, snapDirections);
  if (snapDirections) {
    // A new family stands in its textbook pose.
    view.tiltTarget = next.mount.polar;
    view.spinTarget = 0;
  }
  showFacts();
}

function choose(next) {
  if (next === molecule && !waiting) {
    return;
  }
  const sameFamily = next.regions === molecule.regions && !waiting;
  if (sameFamily) {
    // Same number of electron pairs: bonds swing and swap with lone pairs.
    install(next, false);
  } else {
    // Different number: fold the old model away, then grow the new one.
    waiting = next;
    for (const slot of slots) {
      slot.bondTarget = 0;
      slot.loneTarget = 0;
    }
    markChosen(next);
  }
  wake();
}

// ---------- geometry of the current frame ----------

function rotationNow() {
  return M.orientation(view.yaw, view.tilt, view.spin, mount);
}

// Direction of the stem / carriage on the quadrant, in world space.
function arcDirection(t) {
  const flat = [Math.sin(t * Math.PI / 180), 0, -Math.cos(t * Math.PI / 180)];
  return M.matApply(M.turnZ(view.yaw), flat);
}

function along(direction, distance) {
  return [
    CENTRE[0] + direction[0] * distance,
    CENTRE[1] + direction[1] * distance,
    CENTRE[2] + direction[2] * distance,
  ];
}

function fix(value) {
  return (Math.round(value * 10) / 10).toString();
}

function pointText(point) {
  return fix(point[0]) + " " + fix(point[1]);
}

// ---------- drawing pieces ----------

// A rod between two world points: an ink line with a paler line on top.
function rodMarkup(from, to, radius, className) {
  const a = iso(from, P);
  const b = iso(to, P);
  const d = "M" + pointText(a) + "L" + pointText(b);
  const width = radius * 2 * K;
  let out = "";
  out += '<path class="mk-edge" d="' + d + '" stroke-width="' + fix(width + 1.3) + '"/>';
  out += '<path class="' + className + '" d="' + d + '" stroke-width="' + fix(width) + '"/>';
  return out;
}

// The arrow head on a dative bond, pointing at the atom that accepted the pair.
function arrowMarkup(from, to) {
  const a = iso(from, P);
  const b = iso(to, P);
  const length = Math.hypot(b[0] - a[0], b[1] - a[1]);
  if (length < 9) {
    return "";
  }
  const tx = (b[0] - a[0]) / length;
  const ty = (b[1] - a[1]) / length;
  const mx = a[0] + (b[0] - a[0]) * 0.55;
  const my = a[1] + (b[1] - a[1]) * 0.55;
  const tip = [mx + tx * 4.4, my + ty * 4.4];
  const left = [mx - tx * 2.6 - ty * 4.6, my - ty * 2.6 + tx * 4.6];
  const right = [mx - tx * 2.6 + ty * 4.6, my - ty * 2.6 - tx * 4.6];
  return '<path class="mk-arrow" d="M' + pointText(tip) + "L" + pointText(left) + "L" + pointText(right) + 'Z"/>';
}

function ballMarkup(centre, element, scale, selected) {
  const data = M.ELEMENTS[element];
  const c = iso(centre, P);
  const r = data.radius * K * scale;
  let out = "";
  out += '<circle class="mk-ball" cx="' + fix(c[0]) + '" cy="' + fix(c[1]) + '" r="' + fix(r) + '" fill="url(#mk-' + element + ')"/>';
  if (selected) {
    out += '<circle class="mk-pick" cx="' + fix(c[0]) + '" cy="' + fix(c[1]) + '" r="' + fix(r + 2.4) + '"/>';
  }
  if (options.labels && scale > 0.7) {
    const size = r * 1.02;
    out += '<text class="mk-symbol" x="' + fix(c[0]) + '" y="' + fix(c[1]) + '" font-size="' + fix(size) + '" fill="' + data.ink + '">' + element + "</text>";
  }
  return out;
}

// A lone pair: the outline of a small ball at the atom joined to a larger
// ball further out, with its two electrons.
function lobeMarkup(baseCentre, tipCentre, amount) {
  const c0 = iso(baseCentre, P);
  const c1 = iso(tipCentre, P);
  const r0 = 3.4 * K * amount;
  const r1 = 10 * K * amount;
  const dx = c1[0] - c0[0];
  const dy = c1[1] - c0[1];
  const gap = Math.hypot(dx, dy);
  let out = "";
  if (gap <= r1 - r0 + 0.01) {
    // Seen end-on: the far ball hides the near one.
    out += '<circle class="mk-lobe" cx="' + fix(c1[0]) + '" cy="' + fix(c1[1]) + '" r="' + fix(r1) + '"/>';
  } else {
    const heading = Math.atan2(dy, dx);
    const spread = Math.acos((r0 - r1) / gap);
    const p0a = [c0[0] + r0 * Math.cos(heading + spread), c0[1] + r0 * Math.sin(heading + spread)];
    const p0b = [c0[0] + r0 * Math.cos(heading - spread), c0[1] + r0 * Math.sin(heading - spread)];
    const p1a = [c1[0] + r1 * Math.cos(heading + spread), c1[1] + r1 * Math.sin(heading + spread)];
    const p1b = [c1[0] + r1 * Math.cos(heading - spread), c1[1] + r1 * Math.sin(heading - spread)];
    let largeFar = 0;
    if (2 * spread > Math.PI) {
      largeFar = 1;
    }
    let largeNear = 0;
    if (2 * Math.PI - 2 * spread > Math.PI) {
      largeNear = 1;
    }
    let d = "M" + pointText(p0a) + "L" + pointText(p1a);
    d += "A" + fix(r1) + " " + fix(r1) + " 0 " + largeFar + " 0 " + pointText(p1b);
    d += "L" + pointText(p0b);
    d += "A" + fix(r0) + " " + fix(r0) + " 0 " + largeNear + " 0 " + pointText(p0a) + "Z";
    out += '<path class="mk-lobe" d="' + d + '"/>';
  }
  // The two electrons sit side by side across the lobe.
  let nx = 1;
  let ny = 0;
  if (gap > 0.5) {
    nx = -dy / gap;
    ny = dx / gap;
  }
  const offset = 3.9 * K * amount;
  const dotRadius = 1.7 * K * amount;
  out += '<circle class="mk-electron" cx="' + fix(c1[0] + nx * offset) + '" cy="' + fix(c1[1] + ny * offset) + '" r="' + fix(dotRadius) + '"/>';
  out += '<circle class="mk-electron" cx="' + fix(c1[0] - nx * offset) + '" cy="' + fix(c1[1] - ny * offset) + '" r="' + fix(dotRadius) + '"/>';
  return out;
}

// ---------- the protractor ----------

// Points along the arc from direction a to direction b, at a given radius.
function sweepBetween(a, b, radius) {
  const angle = M.angleBetween(a, b);
  let normal = M.cross(a, b);
  if (Math.hypot(normal[0], normal[1], normal[2]) < 0.02) {
    // Opposite bonds: any plane through them will do, so pick the one that
    // faces the viewer: its normal is the view direction with the part
    // along the bond taken away.
    const along = M.dot(TOWARD_VIEWER, a);
    normal = [
      TOWARD_VIEWER[0] - a[0] * along,
      TOWARD_VIEWER[1] - a[1] * along,
      TOWARD_VIEWER[2] - a[2] * along,
    ];
    if (Math.hypot(normal[0], normal[1], normal[2]) < 0.05) {
      normal = M.cross(a, [0, 0, 1]);
    }
  }
  normal = M.unit(normal);
  const points = [];
  const steps = Math.max(2, Math.ceil(angle / 4));
  for (let i = 0; i <= steps; i++) {
    const direction = M.rotateAbout(a, normal, (angle * i) / steps);
    points.push(along(direction, radius));
  }
  return { angle: angle, normal: normal, points: points };
}

let measuredAngle = 0;
let labelMarkup = "";

function protractorItem(directions) {
  labelMarkup = "";
  const first = slots[selection[0]];
  const second = slots[selection[1]];
  if (first.bondAmount < 0.6 || second.bondAmount < 0.6) {
    return null;
  }
  const a = directions[selection[0]];
  const b = directions[selection[1]];
  const radius = 28;
  const sweep = sweepBetween(a, b, radius);
  measuredAngle = sweep.angle;

  const centre = iso(CENTRE, P);
  const screen = sweep.points.map((point) => iso(point, P));
  let arc = "";
  for (let i = 0; i < screen.length; i++) {
    if (i === 0) {
      arc += "M";
    } else {
      arc += "L";
    }
    arc += pointText(screen[i]);
  }
  const sector = "M" + pointText(centre) + arc.replace("M", "L") + "Z";

  // A tick every 10 degrees, counted from the first bond.
  let ticks = "";
  for (let degrees = 10; degrees < sweep.angle - 1; degrees += 10) {
    const direction = M.rotateAbout(a, sweep.normal, degrees);
    let reach = 2.2;
    if (degrees % 30 === 0) {
      reach = 4;
    }
    ticks += "M" + pointText(iso(along(direction, radius), P)) + "L" + pointText(iso(along(direction, radius - reach), P));
  }

  let out = "";
  out += '<path class="mk-sector" d="' + sector + '"/>';
  out += '<path class="mk-arc" d="' + arc + '"/>';
  out += '<path class="mk-tick" d="' + ticks + '"/>';

  // The reading floats just outside the middle of the arc, drawn last of all.
  const middle = M.rotateAbout(a, sweep.normal, sweep.angle / 2);
  const spot = iso(along(middle, radius + 12), P);
  // Keep the reading clear of the central atom, even when the arc points at us.
  let outX = spot[0] - centre[0];
  let outY = spot[1] - centre[1];
  let outLength = Math.hypot(outX, outY);
  if (outLength < 1) {
    outX = 1;
    outY = 1;
    outLength = Math.SQRT2;
  }
  const clear = (M.ELEMENTS[centralElement].radius + 13) * K;
  if (outLength < clear) {
    spot[0] = centre[0] + (outX / outLength) * clear;
    spot[1] = centre[1] + (outY / outLength) * clear;
  }
  labelMarkup = '<text class="mk-angle" x="' + fix(spot[0]) + '" y="' + fix(spot[1]) + '">' + M.sayAngle(sweep.angle) + "</text>";

  return { depth: depthOf(along(middle, radius * 0.7), P), markup: out };
}

// ---------- the stand's moving parts ----------

function quadrantItems() {
  const items = [];
  const inner = ARC_R - 2.6;
  const outer = ARC_R + 2.6;
  for (let t = -10; t < 100; t += 5) {
    const d0 = arcDirection(t);
    const d1 = arcDirection(t + 5);
    const a0 = iso(along(d0, inner), P);
    const a1 = iso(along(d1, inner), P);
    const b0 = iso(along(d0, outer), P);
    const b1 = iso(along(d1, outer), P);
    let out = "";
    out += '<path class="mk-plate" d="M' + pointText(a0) + "L" + pointText(a1) + "L" + pointText(b1) + "L" + pointText(b0) + 'Z"/>';
    out += '<path class="mk-plate-edge" d="M' + pointText(a0) + "L" + pointText(a1) + "M" + pointText(b0) + "L" + pointText(b1) + '"/>';
    if (t === -10) {
      out += '<path class="mk-plate-edge" d="M' + pointText(a0) + "L" + pointText(b0) + '"/>';
    }
    if (t === 95) {
      out += '<path class="mk-plate-edge" d="M' + pointText(a1) + "L" + pointText(b1) + '"/>';
    }
    // Scale: a tick every 10 degrees, longer every 30.
    if (t >= 0 && t <= 90 && t % 10 === 0) {
      let reach = inner + 2.2;
      if (t % 30 === 0) {
        reach = inner + 3.8;
      }
      out += '<path class="mk-scale" d="M' + pointText(a0) + "L" + pointText(iso(along(d0, reach), P)) + '"/>';
    }
    const middle = arcDirection(t + 2.5);
    items.push({ depth: depthOf(along(middle, ARC_R), P), markup: out });
  }
  return items;
}

function carriageItems(centralRadius) {
  const items = [];
  const d = arcDirection(view.tilt);
  const from = along(d, centralRadius - 1);
  const to = along(d, ARC_R - 2.6);
  items.push({
    depth: depthOf(along(d, (centralRadius + ARC_R) / 2), P),
    markup: rodMarkup(from, to, 1.5, "mk-stem"),
  });
  const knob = iso(along(d, ARC_R), P);
  let out = "";
  out += '<circle class="mk-carriage" cx="' + fix(knob[0]) + '" cy="' + fix(knob[1]) + '" r="' + fix(4.6 * K) + '"/>';
  out += '<circle class="mk-carriage-dot" cx="' + fix(knob[0]) + '" cy="' + fix(knob[1]) + '" r="' + fix(1.1 * K) + '"/>';
  items.push({ depth: depthOf(along(d, ARC_R), P) + 1.5, markup: out });
  return items;
}

// The index mark on the turntable, so its turning can be seen.
function turntableMark() {
  const angle = view.yaw * Math.PI / 180;
  const c = Math.cos(angle);
  const s = Math.sin(angle);
  const from = iso([c * (TABLE_R - 15), s * (TABLE_R - 15), TABLE_TOP], P);
  const to = iso([c * (TABLE_R - 4), s * (TABLE_R - 4), TABLE_TOP], P);
  const opposite = iso([-c * (TABLE_R - 9), -s * (TABLE_R - 9), TABLE_TOP], P);
  let out = "";
  out += '<path class="mk-index" d="M' + pointText(from) + "L" + pointText(to) + '"/>';
  out += '<circle class="mk-index-dot" cx="' + fix(opposite[0]) + '" cy="' + fix(opposite[1]) + '" r="0.9"/>';
  return out;
}

// ---------- one frame ----------

let atomsOnScreen = []; // for tapping: { slot, x, y, r, depth }

function draw() {
  const R = rotationNow();
  const central = M.ELEMENTS[centralElement];
  const items = [];
  const directions = [];
  atomsOnScreen = [];

  for (let i = 0; i < slots.length; i++) {
    const slot = slots[i];
    const u = M.matApply(R, slot.dir);
    directions.push(u);

    if (slot.bondAmount > 0.02) {
      const data = M.ELEMENTS[slot.element];
      const reach = BOND * slot.bondAmount;
      const atomCentre = along(u, reach);
      const from = along(u, central.radius - 2);
      const to = along(u, Math.max(central.radius - 1, reach - data.radius + 2));
      let rods = "";
      if (slot.kind === "double") {
        // Two rods side by side, set apart across the bond.
        let side = M.cross(u, M.matApply(R, [0, 0, 1]));
        if (Math.hypot(side[0], side[1], side[2]) < 0.1) {
          side = M.cross(u, M.matApply(R, [0, 1, 0]));
        }
        side = M.unit(side);
        for (const sign of [-1, 1]) {
          const shift = [side[0] * 3 * sign, side[1] * 3 * sign, side[2] * 3 * sign];
          const f = [from[0] + shift[0], from[1] + shift[1], from[2] + shift[2]];
          const t = [to[0] + shift[0], to[1] + shift[1], to[2] + shift[2]];
          rods += rodMarkup(f, t, 1.7, "mk-rod");
        }
      } else {
        rods += rodMarkup(from, to, 2.5, "mk-rod");
        if (slot.kind === "dative" && slot.bondAmount > 0.9) {
          rods += arrowMarkup(from, to);
        }
      }
      items.push({ depth: depthOf(along(u, (central.radius + reach) / 2), P), markup: rods });

      const scale = Math.min(1, slot.bondAmount * 1.25);
      const picked = selection.includes(i) && slot.bondAmount > 0.6;
      const depth = depthOf(atomCentre, P);
      items.push({ depth: depth, markup: ballMarkup(atomCentre, slot.element, scale, picked) });
      const spot = iso(atomCentre, P);
      atomsOnScreen.push({ slot: i, x: spot[0], y: spot[1], r: data.radius * K + 3, depth: depth });
    }

    if (slot.loneAmount > 0.02 && options.lonePairs) {
      const base = along(u, central.radius - 2);
      const tip = along(u, central.radius + 15 * slot.loneAmount);
      items.push({ depth: depthOf(tip, P) + 0.5, markup: lobeMarkup(base, tip, slot.loneAmount) });
    }
  }

  items.push({ depth: depthOf(CENTRE, P), markup: ballMarkup(CENTRE, centralElement, 1, false) });

  const protractor = protractorItem(directions);
  if (protractor) {
    items.push(protractor);
  }
  for (const item of quadrantItems()) {
    items.push(item);
  }
  for (const item of carriageItems(central.radius)) {
    items.push(item);
  }

  items.sort((p, q) => p.depth - q.depth);
  let markup = turntableMark();
  for (const item of items) {
    markup += item.markup;
  }
  markup += labelMarkup;
  liveGroup.innerHTML = markup;

  showReading(protractor !== null);
}

// ---------- words beside the figure ----------

const factNodes = {
  shape: document.querySelector("[data-fact='shape']"),
  also: document.querySelector("[data-fact='also']"),
  formula: document.querySelector("[data-fact='formula']"),
  bonding: document.querySelector("[data-fact='bonding']"),
  lone: document.querySelector("[data-fact='lone']"),
  arrangement: document.querySelector("[data-fact='arrangement']"),
  angles: document.querySelector("[data-fact='angles']"),
  why: document.querySelector("[data-fact='why']"),
  reading: document.querySelector("[data-fact='reading']"),
};

function markChosen(which) {
  for (const button of document.querySelectorAll("[data-molecule]")) {
    let pressed = "false";
    if (button.dataset.molecule === which.id) {
      pressed = "true";
    }
    button.setAttribute("aria-pressed", pressed);
  }
}

function showFacts() {
  factNodes.shape.textContent = molecule.shape;
  if (molecule.also) {
    factNodes.also.textContent = "also called " + molecule.also;
  } else {
    factNodes.also.textContent = "";
  }
  factNodes.formula.innerHTML = molecule.formula;
  factNodes.bonding.textContent = String(M.countOf(molecule, "bond"));
  factNodes.lone.textContent = String(M.countOf(molecule, "lone"));
  factNodes.arrangement.textContent = molecule.electronShape;
  factNodes.angles.textContent = molecule.quote.map(M.sayAngle).join(" and ");
  factNodes.why.textContent = molecule.why;
  markChosen(molecule);
}

let lastReading = "";

function showReading(hasProtractor) {
  let text = molecule.shape;
  let detail = "Tap two outer atoms to measure the angle between their bonds.";
  if (hasProtractor) {
    const said = M.sayAngle(measuredAngle);
    const first = slots[selection[0]].element;
    const second = slots[selection[1]].element;
    text = molecule.shape + " · " + said;
    detail = first + "–" + centralElement + "–" + second + " bond angle: " + said;
  }
  if (text !== lastReading) {
    lastReading = text;
    readout.textContent = text;
    factNodes.reading.textContent = detail;
    stage.setAttribute("aria-valuetext", detail);
  }
}

// ---------- the frame loop ----------

let frame = 0;
let last = 0;
let visible = true;
let dragging = false;
let restUntil = 0;

function ease(current, target, dt, seconds) {
  if (still.matches) {
    return target;
  }
  const next = current + (target - current) * (1 - Math.exp(-dt / seconds));
  if (Math.abs(target - next) < 0.002) {
    return target;
  }
  return next;
}

function tick(now) {
  let dt = 1 / 60;
  if (last) {
    dt = Math.min((now - last) / 1000, 1 / 30);
  }
  last = now;
  let busy = false;

  // Electron pairs grow, shrink and swing towards their targets.
  let folded = true;
  for (const slot of slots) {
    slot.bondAmount = ease(slot.bondAmount, slot.bondTarget, dt, 0.13);
    slot.loneAmount = ease(slot.loneAmount, slot.loneTarget, dt, 0.13);
    const mixed = [
      ease(slot.dir[0], slot.dirTarget[0], dt, 0.2),
      ease(slot.dir[1], slot.dirTarget[1], dt, 0.2),
      ease(slot.dir[2], slot.dirTarget[2], dt, 0.2),
    ];
    slot.dir = M.unit(mixed);
    if (slot.bondAmount !== slot.bondTarget || slot.loneAmount !== slot.loneTarget) {
      busy = true;
    }
    if (M.angleBetween(slot.dir, slot.dirTarget) > 0.05) {
      busy = true;
    }
    if (slot.bondAmount > 0.03 || slot.loneAmount > 0.03) {
      folded = false;
    }
  }
  if (waiting && folded) {
    const next = waiting;
    waiting = null;
    install(next, true);
    busy = true;
  }

  // The carriage and the spin settle on their targets.
  if (!dragging) {
    view.tilt = ease(view.tilt, view.tiltTarget, dt, 0.22);
    view.spin = ease(view.spin, view.spinTarget, dt, 0.22);
    if (view.tilt !== view.tiltTarget || view.spin !== view.spinTarget) {
      busy = true;
    }
  }

  // The turntable turns slowly by itself until someone takes hold.
  const turning = options.auto && !dragging && now > restUntil && !still.matches;
  if (turning) {
    view.yaw = view.yaw + 12 * dt;
    busy = true;
  }
  if (options.auto && now <= restUntil) {
    busy = true;
  }

  draw();
  syncSliders();

  if (visible && (busy || dragging)) {
    frame = requestAnimationFrame(tick);
  } else {
    frame = 0;
  }
}

function wake() {
  if (!frame && visible) {
    last = 0;
    frame = requestAnimationFrame(tick);
  }
}

function rest() {
  restUntil = performance.now() + 5000;
}

new IntersectionObserver((entries) => {
  visible = entries[entries.length - 1].isIntersecting;
  if (visible) {
    wake();
  }
}).observe(stage);

// ---------- pointer: drag to turn and tilt, tap an atom to measure ----------

let pointerStart = null;

function toViewBox(event) {
  const box = svg.getBoundingClientRect();
  const x = ((event.clientX - box.left) / box.width) * WIDTH;
  const y = ((event.clientY - box.top) / box.height) * HEIGHT;
  return [x, y];
}

function clamp(value, low, high) {
  return Math.min(high, Math.max(low, value));
}

stage.addEventListener("pointerdown", (event) => {
  stage.setPointerCapture(event.pointerId);
  pointerStart = { x: event.clientX, y: event.clientY, yaw: view.yaw, tilt: view.tilt, moved: false };
  dragging = true;
  rest();
  wake();
});

stage.addEventListener("pointermove", (event) => {
  if (!pointerStart) {
    return;
  }
  const dx = event.clientX - pointerStart.x;
  const dy = event.clientY - pointerStart.y;
  if (Math.hypot(dx, dy) > 6) {
    pointerStart.moved = true;
  }
  if (pointerStart.moved) {
    view.yaw = pointerStart.yaw + dx * 0.55;
    view.tilt = clamp(pointerStart.tilt - dy * 0.4, 0, 90);
    view.tiltTarget = view.tilt;
    rest();
  }
});

function pickAtom(event) {
  const spot = toViewBox(event);
  let best = null;
  for (const atom of atomsOnScreen) {
    const distance = Math.hypot(atom.x - spot[0], atom.y - spot[1]);
    if (distance > atom.r) {
      continue;
    }
    if (!best || atom.depth > best.depth) {
      best = atom;
    }
  }
  if (!best) {
    return;
  }
  if (selection.includes(best.slot)) {
    return;
  }
  // Keep the newest two atoms tapped.
  selection = [selection[1], best.slot];
}

function endPointer(event) {
  if (!pointerStart) {
    return;
  }
  if (!pointerStart.moved) {
    pickAtom(event);
  }
  pointerStart = null;
  dragging = false;
  rest();
  wake();
}

stage.addEventListener("pointerup", endPointer);
stage.addEventListener("pointercancel", endPointer);

stage.addEventListener("keydown", (event) => {
  let used = true;
  if (event.key === "ArrowLeft") {
    view.yaw = view.yaw - 10;
  } else if (event.key === "ArrowRight") {
    view.yaw = view.yaw + 10;
  } else if (event.key === "ArrowUp") {
    view.tiltTarget = clamp(view.tiltTarget + 10, 0, 90);
  } else if (event.key === "ArrowDown") {
    view.tiltTarget = clamp(view.tiltTarget - 10, 0, 90);
  } else if (event.key === "," || event.key === "<") {
    view.spinTarget = view.spinTarget - 15;
  } else if (event.key === "." || event.key === ">") {
    view.spinTarget = view.spinTarget + 15;
  } else {
    used = false;
  }
  if (used) {
    event.preventDefault();
    rest();
    wake();
  }
});

// ---------- controls beside the figure ----------

const tiltSlider = document.querySelector("[data-control='tilt']");
const spinSlider = document.querySelector("[data-control='spin']");
const tiltValue = document.querySelector("[data-value='tilt']");
const spinValue = document.querySelector("[data-value='spin']");
let slidersHeld = false;

function syncSliders() {
  if (!slidersHeld) {
    tiltSlider.value = String(Math.round(view.tilt));
    spinSlider.value = String(Math.round(view.spin));
  }
  tiltValue.textContent = Math.round(view.tilt) + "°";
  spinValue.textContent = Math.round(view.spin) + "°";
}

tiltSlider.addEventListener("input", () => {
  slidersHeld = true;
  view.tiltTarget = Number(tiltSlider.value);
  rest();
  wake();
});

spinSlider.addEventListener("input", () => {
  slidersHeld = true;
  view.spinTarget = Number(spinSlider.value);
  rest();
  wake();
});

for (const slider of [tiltSlider, spinSlider]) {
  slider.addEventListener("change", () => {
    slidersHeld = false;
  });
}

for (const button of document.querySelectorAll("[data-molecule]")) {
  button.addEventListener("click", () => {
    const next = M.MOLECULES.find((entry) => entry.id === button.dataset.molecule);
    choose(next);
  });
}

function bindToggle(name, onChange) {
  const box = document.querySelector("[data-toggle='" + name + "']");
  box.checked = options[name];
  box.addEventListener("change", () => {
    options[name] = box.checked;
    if (onChange) {
      onChange();
    }
    wake();
  });
}

bindToggle("auto", () => {
  restUntil = 0;
});
bindToggle("lonePairs");
bindToggle("labels");

document.querySelector("[data-action='reset']").addEventListener("click", () => {
  view.tiltTarget = mount.polar;
  view.spinTarget = 0;
  view.yaw = -35;
  selection = [molecule.measure[0], molecule.measure[1]];
  wake();
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

// ---------- start ----------

install(molecule, true);
view.tilt = view.tiltTarget;
for (const slot of slots) {
  slot.bondAmount = slot.bondTarget;
  slot.loneAmount = slot.loneTarget;
}
draw();
syncSliders();
wake();
