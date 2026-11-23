// Builds the finished page.
//   node build.mjs          writes offreds-room.html here: the stand-alone page
//   node build.mjs --site   writes ../index.html: the copy for jshphysics.github.io, with the
//                           link back to the gallery, the gallery's saved theme and 44px controls
// It draws the room, then joins the drawing, the styles, the content and the behaviour into one HTML file.
// It needs the Anatomy skill's kit/ and scripts/ folders at ./vendor/ (not committed).

import { readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "./vendor/kit/iso-kit.mjs";
import { kitScript } from "./vendor/scripts/inline-kit.mjs";
import { roomSvg, P, SASH_NOW, SASH_BEFORE } from "./geometry.mjs";
import { OBJECTS, TOUR, CHAPTERS } from "./content.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const read = (name) => readFileSync(join(HERE, name), "utf8");

const SITE = process.argv.includes("--site");

let TITLE = "Offred's Room";
if (SITE) {
  TITLE = "Offred's Room · JSHPhysics";
}

// The site copy links back to the gallery and reads the theme the gallery saved.
let backLink = "";
let layoutClass = "rm-page";
let savedTheme = "";
let siteMeta = "";
if (SITE) {
  backLink = `<a class="site-back" href="../">← All JSHPhysics tools</a>`;
  layoutClass = "rm-page site";
  savedTheme = `
  try {
    var saved = localStorage.getItem("jsh-theme");
    if (saved === "light" || saved === "dark") {
      root.setAttribute("data-theme", saved);
    }
  } catch (error) {
    // No storage here: fall through to the device setting.
  }`;
  siteMeta =
    '<meta name="description" content="A cutaway model of Offred\'s room from chapter 2 of The Handmaid\'s Tale. Click each object, predict, then find the words in the novel.">' +
    '<meta name="author" content="Joshua Stafford-Haworth (JSHPhysics)">';
}

// ---------- the card that holds the model ----------

const card = k.plateHtml({
  fig: "Fig 1",
  title: "Offred's room",
  hint: "Click any object",
  readout: "0 of " + OBJECTS.length + " examined · ch. 2 · the room now",
  keys: [
    { mark: "lit", label: "The object you have chosen" },
    { mark: "dashed", label: "Taken out of the room" },
    { mark: "red", label: "Her gloves, the only strong colour" },
  ],
  caption:
    "A cutaway model of the room in chapter 2. Two walls and the ceiling are removed so you can see in. The disc floating above the room is the one piece of ceiling left in, so you can see the plaster wreath. It is drawn from above. The scale strip on the stand is marked every 10 cm.",
  body: `<div class="iso-stage" role="group" aria-label="Model of Offred's room">${roomSvg()}</div>`,
});

// ---------- the controls ----------

const modeControl = `
<fieldset class="rm-seg">
  <legend>Show</legend>
  <div class="rm-seg-row">
    <button class="rm-btn" type="button" data-mode-button="now" aria-pressed="true">The room now</button>
    <button class="rm-btn" type="button" data-mode-button="missing" aria-pressed="false">What has been taken out</button>
  </div>
</fieldset>`;

const chapterButtons = CHAPTERS.map((chapter) => {
  let pressed = "false";
  if (chapter === 2) {
    pressed = "true";
  }
  return `<button class="rm-btn" type="button" data-chapter-button="${chapter}" aria-pressed="${pressed}">Chapter ${chapter}</button>`;
}).join("");

const chapterControl = `
<fieldset class="rm-seg">
  <legend>We have read up to</legend>
  <div class="rm-seg-row">${chapterButtons}</div>
</fieldset>`;

const tour = `
<section class="rm-tour" aria-label="The narrator's eye">
  <div class="rm-tour-row">
    <span class="rm-label">The narrator's eye</span>
    <span class="rm-tour-count" id="rm-tour-count">0 of ${TOUR.length}</span>
  </div>
  <p class="rm-tour-say" id="rm-tour-say" aria-live="polite"></p>
  <div class="rm-tour-row">
    <button class="rm-btn" type="button" id="rm-tour-play">Play</button>
    <button class="rm-btn" type="button" id="rm-tour-back">Back</button>
    <button class="rm-btn" type="button" id="rm-tour-next">Next</button>
  </div>
  <p class="rm-trail" id="rm-tour-trail"></p>
</section>`;

const teacher = `
<details class="rm-teacher">
  <summary>Notes for the teacher</summary>
  <ul>
    <li>The page quotes nothing from the novel. Students find and copy the words themselves, so they need the text in front of them.</li>
    <li>Chapter references follow the standard numbering: the room in chapter 2, the cupboard in chapter 9, the cushion in chapter 10, the study conversation in chapter 29. Check them against your edition before the lesson.</li>
    <li>"What has been taken out" shows the light fitting, the glass in the picture, a fully opening window and a mirror. The first three are stated in chapter 2. The mirror is an inference from the remark that mirrors are few, and its questions ask students to notice that difference.</li>
    <li>The reason these things were removed is self-harm, and the chapter 29 layer returns to it. The page never describes it, so students meet it in the novel's own words. You may want to set the chapter buttons yourself and brief the class first.</li>
    <li>The cupboard is drawn but the narrator never mentions it in chapter 2. Its first question uses that gap to open a discussion of narrative reliability.</li>
    <li>Writing is kept in the browser on that device only. "Copy my notes" gives students plain text to paste into their own document.</li>
  </ul>
</details>`;

// ---------- the script ----------

// moving.mjs is shared with the build, so strip its "export" keywords for the page.
const moving = read("moving.mjs").replace(/^export /gm, "");

const data = `
const P = ${JSON.stringify(P)};
const OBJECTS = ${JSON.stringify(OBJECTS)};
const TOUR = ${JSON.stringify(TOUR)};
const CHAPTERS = ${JSON.stringify(CHAPTERS)};
const SASH_NOW = ${SASH_NOW};
const SASH_BEFORE = ${SASH_BEFORE};
`;

// The page's own code sits in a block so its names cannot collide with the kit's.
const script = kitScript() + "\n{\n" + data + moving + read("live.js") + "\n}\n";
const safeScript = script.replace(/<\/(script)/gi, "<\\/$1");

// ---------- the document ----------

const html = `<!DOCTYPE html>
<html lang="en" class="iso">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${TITLE}</title>
<script>
// Follow the viewer's theme. If nothing has set one, use the device setting.
(function () {
  var root = document.documentElement;${savedTheme}
  if (!root.getAttribute("data-theme")) {
    var dark = window.matchMedia("(prefers-color-scheme: dark)").matches;
    root.setAttribute("data-theme", dark ? "dark" : "light");
  }
})();
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap">
${siteMeta}
<style>${k.ISO_CSS}${read("page.css")}</style>
</head>
<body>
<main class="${layoutClass}">
  <header class="rm-head">
    ${backLink}
    <p class="rm-eyebrow">The Handmaid's Tale · Chapter 2</p>
    <h1>Offred's room</h1>
    <p class="rm-lede">Offred's room holds a few plain pieces of furniture and several gaps where things have been removed. Click an object, write a prediction, then find the words in your copy of the novel.</p>
  </header>

  <div class="rm-layout">
    <section class="rm-left">
      <div class="rm-controls">${modeControl}${chapterControl}</div>
      ${card}
      ${tour}
      <div>
        <div class="rm-label" id="rm-chips-label">Objects</div>
        <div class="rm-chips" id="rm-chips" role="group" aria-labelledby="rm-chips-label" style="margin-top:8px"></div>
      </div>
    </section>
    <aside class="rm-panel" id="rm-panel" aria-live="polite"></aside>
  </div>

  ${teacher}
  <footer class="rm-foot">Built by Joshua Stafford-Haworth · JSHPhysics · @educatorJSH</footer>
</main>
<script type="module">${safeScript}</script>
</body>
</html>`;

let outFile = join(HERE, "offreds-room.html");
if (SITE) {
  outFile = join(HERE, "..", "index.html");
}
writeFileSync(outFile, html);
console.log("wrote " + outFile, Math.round(html.length / 1024) + " KB");
