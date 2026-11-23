// The page's behaviour.
// The build script puts these names in scope before this file runs:
//   P, OBJECTS, TOUR, CHAPTERS, SCENES, SCENE_END, SASH_NOW, SASH_BEFORE, VIEW_WIDTH, VIEW_HEIGHT   (data)
//   curtainSvg, cupboardDoorSvg                          (from moving.mjs)
//   iso, extrude, solidSvg, lineSvg, dotsSvg, towardViewer, translateAlong   (the drawing kit)

// ---------- handles on the page ----------

const stage = document.querySelector(".iso-stage");
const svg = stage.querySelector("svg");
const readout = document.querySelector("[data-readout]");
const panel = document.getElementById("rm-panel");
const chipRow = document.getElementById("rm-chips");
const modeButtons = document.querySelectorAll("[data-mode-button]");
const chapterButtons = document.querySelectorAll("[data-chapter-button]");
const tourPlay = document.getElementById("rm-tour-play");
const tourBack = document.getElementById("rm-tour-back");
const tourNext = document.getElementById("rm-tour-next");
const tourSay = document.getElementById("rm-tour-say");
const tourCount = document.getElementById("rm-tour-count");
const tourTrail = document.getElementById("rm-tour-trail");
const sceneLine = document.getElementById("rm-scene");
const wholeButton = document.getElementById("rm-whole");

const sashGroup = svg.querySelector('[data-part="sash"]');
const curtainFar = svg.querySelector('[data-part="curtain-far"]');
const curtainNear = svg.querySelector('[data-part="curtain-near"]');
const cupboardDoor = svg.querySelector('[data-part="cupboard-door"]');

const still = matchMedia("(prefers-reduced-motion: reduce)");

// The drawing functions that moving.mjs needs, gathered into one object.
const kit = { iso, extrude, solidSvg, lineSvg, dotsSvg, towardViewer };

// ---------- what the student has chosen ----------

const state = {
  mode: "now", // "now" or "missing"
  chapter: 2, // how far the class has read
  selected: null, // id of the object in the panel
  step: -1, // position in the narrator's tour; -1 means not started
  playing: false,
  work: {}, // the student's writing, keyed by "objectId:chapter"
  opened: {}, // later-chapter layers the student has looked at, keyed the same way
};

const STORE_KEY = "offreds-room-work-v1";

// ---------- saved writing ----------

function loadWork() {
  try {
    const raw = localStorage.getItem(STORE_KEY);
    if (raw) {
      const saved = JSON.parse(raw);
      if (saved && typeof saved === "object") {
        state.work = saved;
      }
    }
  } catch (error) {
    // No storage here. The page still works; writing lasts until the tab closes.
  }
}

function saveWork() {
  try {
    localStorage.setItem(STORE_KEY, JSON.stringify(state.work));
  } catch (error) {
    // Nothing to do: see loadWork.
  }
}

// The student's record for one layer of one object.
function workFor(objectId, chapter) {
  const key = objectId + ":" + chapter;
  if (!state.work[key]) {
    state.work[key] = { prediction: "", revealed: false, notes: "" };
  }
  return state.work[key];
}

// Has the student revealed at least one layer of this object?
function isExamined(object) {
  for (const layer of object.layers) {
    const record = state.work[object.id + ":" + layer.chapter];
    if (record && record.revealed) {
      return true;
    }
  }
  return false;
}

// Does this object have questions from a later chapter that the student has not looked at yet?
function hasNew(object) {
  for (const layer of object.layers) {
    const isLater = layer.chapter > 2;
    const isUnlocked = layer.chapter <= state.chapter;
    const key = object.id + ":" + layer.chapter;
    if (isLater && isUnlocked && !state.opened[key]) {
      return true;
    }
  }
  return false;
}

// Record that the student has looked at every unlocked layer of this object.
function markOpened(object) {
  for (const layer of object.layers) {
    if (layer.chapter <= state.chapter) {
      state.opened[object.id + ":" + layer.chapter] = true;
    }
  }
}

function countExamined() {
  let count = 0;
  for (const object of OBJECTS) {
    if (isExamined(object)) {
      count += 1;
    }
  }
  return count;
}

function countWords(text) {
  const words = text.trim().split(/\s+/);
  if (words.length === 1 && words[0] === "") {
    return 0;
  }
  return words.length;
}

function findObject(id) {
  for (const object of OBJECTS) {
    if (object.id === id) {
      return object;
    }
  }
  return null;
}

// ---------- small DOM helper ----------

function make(tag, className, text) {
  const element = document.createElement(tag);
  if (className) {
    element.className = className;
  }
  if (text) {
    element.textContent = text;
  }
  return element;
}

// ---------- the moving parts of the model ----------

// Where each moving part is now. The loop eases these toward their targets.
const motion = {
  sash: SASH_NOW,
  ghost: 0,
  door: 0,
  light: 0,
  clock: 0,
};

// Set by a chapter scene while the missing light fitting should show.
let lightTarget = 0;

// ---------- the camera ----------

// The camera is the SVG's viewBox. "camera" is where it is now; "cameraTarget" is where it is heading.
const FULL_VIEW = { x: 0, y: 0, w: VIEW_WIDTH, h: VIEW_HEIGHT };
const camera = { x: 0, y: 0, w: VIEW_WIDTH, h: VIEW_HEIGHT };
let cameraTarget = { x: 0, y: 0, w: VIEW_WIDTH, h: VIEW_HEIGHT };

// The box, in drawing units, that holds every part of the named objects.
function boxOf(ids) {
  let left = Infinity;
  let top = Infinity;
  let right = -Infinity;
  let bottom = -Infinity;
  for (const id of ids) {
    for (const group of svg.querySelectorAll('[data-obj="' + id + '"]')) {
      // Parts that have been taken out only count when they are showing.
      const isGhost = group.classList.contains("rm-ghost");
      if (isGhost && state.mode !== "missing") {
        continue;
      }
      const box = group.getBBox();
      left = Math.min(left, box.x);
      top = Math.min(top, box.y);
      right = Math.max(right, box.x + box.width);
      bottom = Math.max(bottom, box.y + box.height);
    }
  }
  if (left === Infinity) {
    return null;
  }
  return { x: left, y: top, w: right - left, h: bottom - top };
}

// A view that frames the named objects with some of the room around them.
function frameFor(ids) {
  const box = boxOf(ids);
  if (!box) {
    return { x: 0, y: 0, w: VIEW_WIDTH, h: VIEW_HEIGHT };
  }
  const shape = VIEW_WIDTH / VIEW_HEIGHT;

  // Wide enough for the object with room to spare, and never closer than about 2.5 times.
  let width = Math.max(box.w * 1.9, box.h * 1.7 * shape, VIEW_WIDTH / 2.5);
  width = Math.min(width, VIEW_WIDTH);
  const height = width / shape;

  // Centre on the object, then keep the view inside the drawing.
  let x = box.x + box.w / 2 - width / 2;
  let y = box.y + box.h / 2 - height / 2;
  x = Math.max(0, Math.min(VIEW_WIDTH - width, x));
  y = Math.max(0, Math.min(VIEW_HEIGHT - height, y));
  return { x: x, y: y, w: width, h: height };
}

// Point the camera at some objects, or at the whole room when "ids" is null.
function lookAt(ids) {
  if (ids) {
    cameraTarget = frameFor(ids);
  } else {
    cameraTarget = { x: 0, y: 0, w: VIEW_WIDTH, h: VIEW_HEIGHT };
  }
  const zoomedIn = cameraTarget.w < VIEW_WIDTH - 1;
  wholeButton.hidden = !zoomedIn;
  run();
}

function cameraSettled() {
  return camera.x === cameraTarget.x && camera.y === cameraTarget.y && camera.w === cameraTarget.w && camera.h === cameraTarget.h;
}

function sashTarget() {
  if (state.mode === "missing") {
    return SASH_BEFORE;
  }
  return SASH_NOW;
}

function ghostTarget() {
  if (state.mode === "missing") {
    return 1;
  }
  return 0;
}

function doorTarget() {
  if (state.chapter >= 9) {
    return 150;
  }
  return 0;
}

// Move "current" a fraction of the way to "target". "seconds" sets how quickly.
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

function drawModel() {
  // The window sash.
  sashGroup.setAttribute("transform", translateAlong(P, [0, 0, motion.sash]));

  // The curtains: the wider the window is open, the more the air moves them.
  const openness = motion.sash / SASH_BEFORE;
  let breeze = 0.5;
  let breezeNear = 0.5;
  if (!still.matches) {
    breeze = 0.55 + 0.45 * Math.sin(motion.clock * 1.15);
    breezeNear = 0.55 + 0.45 * Math.sin(motion.clock * 0.9 + 1.7);
  }
  const reach = 3.4 * openness;
  curtainFar.innerHTML = curtainSvg(kit, P, 55, 67, reach * breeze);
  curtainNear.innerHTML = curtainSvg(kit, P, 125, 137, reach * breezeNear);

  // The cupboard door.
  cupboardDoor.innerHTML = cupboardDoorSvg(kit, P, motion.door);

  // The things that have been taken out, and the light fitting when a scene shows it.
  svg.style.setProperty("--rm-ghost", motion.ghost.toFixed(3));
  svg.style.setProperty("--rm-light", motion.light.toFixed(3));

  // The camera.
  const view = camera.x.toFixed(2) + " " + camera.y.toFixed(2) + " " + camera.w.toFixed(2) + " " + camera.h.toFixed(2);
  svg.setAttribute("viewBox", view);
}

let frame = 0;
let lastTime = 0;
let visible = false;

function tick(now) {
  let dt = 1 / 60;
  if (lastTime) {
    dt = Math.min((now - lastTime) / 1000, 1 / 30);
  }
  lastTime = now;
  motion.clock += dt;

  motion.sash = ease(motion.sash, sashTarget(), dt, 0.32);
  motion.ghost = ease(motion.ghost, ghostTarget(), dt, 0.28);
  motion.door = ease(motion.door, doorTarget(), dt, 0.45);
  motion.light = ease(motion.light, lightTarget, dt, 0.5);
  camera.x = ease(camera.x, cameraTarget.x, dt, 0.36);
  camera.y = ease(camera.y, cameraTarget.y, dt, 0.36);
  camera.w = ease(camera.w, cameraTarget.w, dt, 0.36);
  camera.h = ease(camera.h, cameraTarget.h, dt, 0.36);
  drawModel();

  // The curtains keep moving, so the loop only stops for reduced motion or when off screen.
  const partsSettled = motion.sash === sashTarget() && motion.ghost === ghostTarget() && motion.door === doorTarget();
  const settled = partsSettled && motion.light === lightTarget && cameraSettled();
  const keepGoing = visible && (!still.matches || !settled);
  if (keepGoing) {
    frame = requestAnimationFrame(tick);
  } else {
    frame = 0;
  }
}

function run() {
  if (!frame && visible) {
    lastTime = 0;
    frame = requestAnimationFrame(tick);
  }
}

// ---------- readout, chips and highlights ----------

function describeMode() {
  if (state.mode === "missing") {
    return "what has been taken out";
  }
  return "the room now";
}

function updateReadout() {
  const text = countExamined() + " of " + OBJECTS.length + " examined · ch. " + state.chapter + " · " + describeMode();
  if (readout.textContent !== text) {
    readout.textContent = text;
  }
}

function updateHighlights() {
  const groups = svg.querySelectorAll("[data-obj]");
  let eyeObject = null;
  if (state.step >= 0) {
    eyeObject = TOUR[state.step].object;
  }

  // Everything the tour has reached so far.
  const seen = {};
  for (let index = 0; index <= state.step; index++) {
    const visited = TOUR[index].object;
    if (visited) {
      seen[visited] = true;
    }
  }

  for (const group of groups) {
    const id = group.dataset.obj;
    group.toggleAttribute("data-on", id === state.selected);
    group.toggleAttribute("data-eye", id === eyeObject);
    group.toggleAttribute("data-seen", Boolean(seen[id]));
    const object = findObject(id);
    group.toggleAttribute("data-new", Boolean(object) && hasNew(object));
  }

  // Chapter and mode flags that the stylesheet reads.
  svg.dataset.mode = state.mode;
  svg.toggleAttribute("data-ch9", state.chapter >= 9);
  svg.toggleAttribute("data-ch10", state.chapter >= 10);
  svg.toggleAttribute("data-ch29", state.chapter >= 29);
}

function updateChips() {
  for (const chip of chipRow.querySelectorAll("[data-chip]")) {
    const object = findObject(chip.dataset.chip);
    chip.setAttribute("aria-pressed", String(object.id === state.selected));
    chip.toggleAttribute("data-done", isExamined(object));
    chip.toggleAttribute("data-new", hasNew(object));
  }
}

function updateButtons() {
  for (const button of modeButtons) {
    button.setAttribute("aria-pressed", String(button.dataset.modeButton === state.mode));
  }
  for (const button of chapterButtons) {
    button.setAttribute("aria-pressed", String(Number(button.dataset.chapterButton) === state.chapter));
  }
}

// ---------- the question panel ----------

function renderIntro() {
  panel.replaceChildren();
  panel.append(make("h2", "", "Question the room"));
  panel.append(
    make(
      "p",
      "",
      "In chapter 2 Offred describes the room she has been given in the Commander's house. Someone decided what goes in a Handmaid's room and what is kept out of it.",
    ),
  );

  const steps = make("ol", "rm-steps");
  const lines = [
    "Click any object in the model. Start with the chair: it is the first thing she names.",
    "Write a prediction before you look anything up. The questions unlock when you have written at least three words.",
    "Find the words in your copy of the novel and write them down with what you notice.",
    "Press a chapter button when your class reaches that chapter. The model shows what changes and outlines the objects that have new questions.",
    "Use the other button above the model to see what has been taken out of the room.",
  ];
  for (const line of lines) {
    steps.append(make("li", "", line));
  }
  panel.append(steps);
  panel.append(renderFoot());
}

// One layer of one object: a prediction, then the questions it unlocks.
function renderLayer(object, layer) {
  const box = make("section", "rm-layer");

  let title = "Chapter " + layer.chapter;
  if (layer.unmentioned) {
    title = "Chapter 2 · not mentioned";
  }
  box.append(make("div", "rm-layer-title", title));

  // A layer from a chapter the class has not reached stays shut, with no spoilers.
  if (layer.chapter > state.chapter) {
    box.append(make("div", "rm-locked", "There is more to say about this once you have read chapter " + layer.chapter + ". Set the chapter above the model when you get there."));
    return box;
  }

  const record = workFor(object.id, layer.chapter);
  const fieldId = "rm-predict-" + object.id + "-" + layer.chapter;

  const promptLabel = make("label", "rm-prompt", layer.predict);
  promptLabel.htmlFor = fieldId;
  box.append(promptLabel);

  const prediction = make("textarea", "rm-text");
  prediction.id = fieldId;
  prediction.placeholder = "Your prediction";
  prediction.value = record.prediction;
  box.append(prediction);

  const gate = make("div", "rm-gate");
  const revealButton = make("button", "rm-btn", "Show the questions");
  revealButton.type = "button";
  const gateNote = make("span", "", "");
  gate.append(revealButton, gateNote);
  box.append(gate);

  const reveal = make("div", "rm-reveal");
  box.append(reveal);

  // Fill in the unlocked part.
  const showReveal = () => {
    reveal.replaceChildren();

    const find = make("div", "rm-block");
    find.append(make("div", "rm-label", "Find it"));
    find.append(make("p", "", layer.find));
    reveal.append(find);

    const closer = make("div", "rm-block");
    closer.append(make("div", "rm-label", "Look closer"));
    const list = make("ul", "");
    for (const question of layer.closer) {
      list.append(make("li", "", question));
    }
    closer.append(list);
    reveal.append(closer);

    const zoom = make("div", "rm-block");
    zoom.append(make("div", "rm-label", "Zoom out"));
    zoom.append(make("p", "", layer.zoom));
    reveal.append(zoom);

    const notesId = "rm-notes-" + object.id + "-" + layer.chapter;
    const notesLabel = make("label", "rm-label", "Your quotation and what you notice");
    notesLabel.htmlFor = notesId;
    const notes = make("textarea", "rm-text");
    notes.id = notesId;
    notes.placeholder = "Copy the words from the novel, then say what they do";
    notes.value = record.notes;
    notes.addEventListener("input", () => {
      record.notes = notes.value;
      saveWork();
    });
    reveal.append(notesLabel, notes);
  };

  // Keep the gate in step with what has been typed.
  const updateGate = () => {
    if (record.revealed) {
      gate.hidden = true;
      return;
    }
    const words = countWords(prediction.value);
    const ready = words >= 3;
    revealButton.disabled = !ready;
    if (ready) {
      gateNote.textContent = "";
    } else {
      gateNote.textContent = "Write at least three words first.";
    }
  };

  prediction.addEventListener("input", () => {
    record.prediction = prediction.value;
    saveWork();
    updateGate();
  });

  revealButton.addEventListener("click", () => {
    record.revealed = true;
    saveWork();
    showReveal();
    updateGate();
    updateChips();
    updateReadout();
  });

  if (record.revealed) {
    showReveal();
  }
  updateGate();
  return box;
}

function renderObject(object) {
  panel.replaceChildren();
  panel.append(make("h2", "", object.name));

  if (object.absent) {
    panel.append(make("p", "", "This object is not in the room. It appears only when the model shows what has been taken out."));
  }

  for (const layer of object.layers) {
    panel.append(renderLayer(object, layer));
  }
  panel.append(renderFoot());
}

// The bottom of the panel: copy or clear the student's writing.
function renderFoot() {
  const foot = make("div", "rm-panel-foot");
  const copyButton = make("button", "rm-btn", "Copy my notes");
  copyButton.type = "button";
  const clearButton = make("button", "rm-btn", "Clear my notes");
  clearButton.type = "button";
  const status = make("div", "rm-status", "");
  status.setAttribute("role", "status");
  foot.append(copyButton, clearButton, status);

  copyButton.addEventListener("click", () => {
    const text = notesAsText();
    // If the browser refuses the clipboard, show the text so it can be copied by hand.
    const showByHand = () => {
      let area = foot.querySelector(".rm-export");
      if (!area) {
        area = make("textarea", "rm-text rm-export");
        area.id = "rm-export";
        area.readOnly = true;
        area.setAttribute("aria-label", "Your notes, ready to copy");
        foot.append(area);
      }
      area.value = text;
      area.focus();
      area.select();
      status.textContent = "Copying was blocked here. Your notes are selected below: press Ctrl+C or Cmd+C.";
    };
    try {
      navigator.clipboard.writeText(text).then(
        () => {
          status.textContent = "Copied. Paste your notes into your own document.";
        },
        showByHand,
      );
    } catch (error) {
      showByHand();
    }
  });

  // Clearing takes two clicks, so one slip does not lose a lesson's work.
  let armed = false;
  clearButton.addEventListener("click", () => {
    if (!armed) {
      armed = true;
      clearButton.textContent = "Click again to clear everything";
      return;
    }
    state.work = {};
    saveWork();
    armed = false;
    render();
    const freshStatus = panel.querySelector(".rm-status");
    if (freshStatus) {
      freshStatus.textContent = "Your notes have been cleared.";
    }
  });

  return foot;
}

// All of the student's writing as plain text, in the order of the room.
function notesAsText() {
  const lines = ["Offred's room: my notes", ""];
  let wroteAnything = false;
  for (const object of OBJECTS) {
    for (const layer of object.layers) {
      const record = state.work[object.id + ":" + layer.chapter];
      if (!record) {
        continue;
      }
      const hasPrediction = record.prediction.trim() !== "";
      const hasNotes = record.notes.trim() !== "";
      if (!hasPrediction && !hasNotes) {
        continue;
      }
      wroteAnything = true;
      lines.push(object.name + " (chapter " + layer.chapter + ")");
      if (hasPrediction) {
        lines.push("My prediction: " + record.prediction.trim());
      }
      if (hasNotes) {
        lines.push("Quotation and notes: " + record.notes.trim());
      }
      lines.push("");
    }
  }
  if (!wroteAnything) {
    lines.push("Nothing written yet.");
  }
  return lines.join("\n");
}

// ---------- the narrator's tour ----------

let tourTimer = 0;

function updateTour() {
  const total = TOUR.length;
  if (state.step < 0) {
    tourSay.textContent = "Press play to follow her eyes round the room, in the order she describes it.";
    tourCount.textContent = "0 of " + total;
    tourTrail.textContent = "";
  } else {
    tourSay.textContent = TOUR[state.step].say;
    tourCount.textContent = state.step + 1 + " of " + total;

    // The trail lists every stop so far, so the order itself can be studied.
    const names = [];
    for (let index = 0; index <= state.step; index++) {
      const stop = TOUR[index];
      if (stop.object) {
        names.push(findObject(stop.object).name.replace("The ", "").toLowerCase());
      } else {
        names.push("(a bell)");
      }
    }
    tourTrail.textContent = names.join(", ");
  }

  if (state.playing) {
    tourPlay.textContent = "Pause";
  } else if (state.step >= total - 1) {
    tourPlay.textContent = "Play again";
  } else {
    tourPlay.textContent = "Play";
  }
  tourBack.disabled = state.step <= 0;
  tourNext.disabled = state.step >= total - 1;
}

function stopTour() {
  state.playing = false;
  clearTimeout(tourTimer);
  tourTimer = 0;
}

function goToStep(step) {
  state.step = Math.max(-1, Math.min(TOUR.length - 1, step));
  updateHighlights();
  updateTour();

  // The camera follows her eyes. The floor and the bell are shown with the whole room.
  let target = null;
  if (state.step >= 0) {
    target = TOUR[state.step].object;
  }
  if (target && target !== "floor") {
    lookAt([target]);
  } else {
    lookAt(null);
  }
}

function scheduleNextStep() {
  clearTimeout(tourTimer);
  tourTimer = setTimeout(() => {
    if (!state.playing) {
      return;
    }
    if (state.step >= TOUR.length - 1) {
      stopTour();
      updateTour();
      lookAt(null);
      return;
    }
    goToStep(state.step + 1);
    scheduleNextStep();
  }, 2600);
}

function playTour() {
  // Playing from the end starts again from the top.
  if (state.step >= TOUR.length - 1) {
    state.step = -1;
  }
  cancelScene();
  // The tour belongs to chapter 2 and to the room as it is now.
  state.mode = "now";
  state.selected = null;
  state.playing = true;
  goToStep(state.step + 1);
  render();
  scheduleNextStep();
}

// ---------- changing things ----------

function render() {
  updateHighlights();
  updateButtons();
  updateChips();
  updateReadout();
  updateTour();
  const object = findObject(state.selected);
  if (object) {
    renderObject(object);
  } else {
    renderIntro();
  }
  stage.setAttribute("aria-label", "Model of Offred's room. " + countExamined() + " of " + OBJECTS.length + " objects examined. Showing " + describeMode() + ", read up to chapter " + state.chapter + ".");
  run();
}

function select(id) {
  stopTour();
  cancelScene();
  state.selected = id;
  // The mirror only exists in the "taken out" view, so choosing it switches to that view.
  const object = findObject(id);
  if (object && object.absent) {
    state.mode = "missing";
  }
  if (object) {
    markOpened(object);
  }
  render();

  // Move in on the chosen object. The floor is the whole room, so it stays wide.
  if (id === "floor") {
    lookAt(null);
  } else {
    lookAt([id]);
  }

  // On a narrow screen the panel sits below the model, so bring it into view.
  const stacked = matchMedia("(max-width: 980px)").matches;
  if (stacked) {
    let behavior = "smooth";
    if (still.matches) {
      behavior = "auto";
    }
    panel.scrollIntoView({ behavior: behavior, block: "start" });
  }
}

function setMode(mode) {
  stopTour();
  cancelScene();
  state.mode = mode;
  render();
  // The view may need to widen or narrow now that parts have appeared or gone.
  if (state.selected && state.selected !== "floor") {
    lookAt([state.selected]);
  }
}

// ---------- chapter scenes ----------

let sceneTimer = 0;

function showSceneLine(text) {
  sceneLine.textContent = text;
  sceneLine.toggleAttribute("data-show", text !== "");
}

function cancelScene() {
  clearTimeout(sceneTimer);
  sceneTimer = 0;
  lightTarget = 0;
  showSceneLine("");
}

// Play the beats of a chapter one after another, then pull back to the whole room.
function playScene(chapter) {
  const beats = SCENES[chapter];
  let index = 0;

  const nextBeat = () => {
    if (index >= beats.length) {
      // Finished: show the whole room and say where the new questions are.
      lightTarget = 0;
      lookAt(null);
      if (chapter > 2) {
        showSceneLine(SCENE_END);
      } else {
        showSceneLine("");
      }
      run();
      return;
    }
    const beat = beats[index];
    index += 1;
    showSceneLine(beat.say);
    lookAt(beat.focus);
    if (beat.light) {
      lightTarget = 1;
    } else {
      lightTarget = 0;
    }
    run();
    sceneTimer = setTimeout(nextBeat, beat.hold);
  };

  nextBeat();
}

function setChapter(chapter) {
  stopTour();
  cancelScene();
  const movedOn = chapter > state.chapter;
  state.chapter = chapter;
  state.selected = null;
  render();
  if (movedOn) {
    playScene(chapter);
  } else {
    // Going back: no scene, only the whole room at the earlier chapter.
    lookAt(null);
    showSceneLine("Back at chapter " + chapter + ".");
    sceneTimer = setTimeout(() => showSceneLine(""), 2400);
  }
}

// ---------- wiring ----------

// Chips: one per object, in the order of the room.
for (const object of OBJECTS) {
  const chip = make("button", "rm-chip", object.name.replace("The ", ""));
  chip.type = "button";
  chip.dataset.chip = object.id;
  chip.addEventListener("click", () => select(object.id));
  chipRow.append(chip);
}

for (const button of modeButtons) {
  button.addEventListener("click", () => setMode(button.dataset.modeButton));
}

for (const button of chapterButtons) {
  button.addEventListener("click", () => setChapter(Number(button.dataset.chapterButton)));
}

// Clicking the model: find which object the click landed on.
svg.addEventListener("click", (event) => {
  const group = event.target.closest("[data-obj]");
  if (group) {
    select(group.dataset.obj);
  }
});

// Keyboard: Enter or Space on a focused object selects it; Escape lets go.
svg.addEventListener("keydown", (event) => {
  const group = event.target.closest("[data-obj]");
  const isPress = event.key === "Enter" || event.key === " ";
  if (group && isPress) {
    event.preventDefault();
    select(group.dataset.obj);
  }
  if (event.key === "Escape") {
    state.selected = null;
    render();
    lookAt(null);
  }
});

wholeButton.addEventListener("click", () => {
  cancelScene();
  stopTour();
  updateTour();
  lookAt(null);
});

tourPlay.addEventListener("click", () => {
  if (state.playing) {
    stopTour();
    updateTour();
  } else {
    playTour();
  }
});

tourBack.addEventListener("click", () => {
  stopTour();
  cancelScene();
  goToStep(state.step - 1);
});

tourNext.addEventListener("click", () => {
  stopTour();
  cancelScene();
  goToStep(state.step + 1);
});

// Only animate while the model is on screen.
const watcher = new IntersectionObserver(
  (entries) => {
    visible = entries[entries.length - 1].isIntersecting;
    if (visible) {
      run();
    }
  },
  { rootMargin: "120px 0px" },
);
watcher.observe(stage);

loadWork();
drawModel();
render();
