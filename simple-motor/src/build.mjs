// Builds the simple motor page: node build.mjs
// Writes artifact.html (a fragment for the Artifact viewer), site/index.html (the GitHub Pages copy)
// and test-light.html / test-dark.html (for checking).
// The figures are drawn in the browser from geom.mjs + motor.js, so this script only assembles the page.

import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "/mnt/skills/plugins/anatomy/kit/iso-kit.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const read = (name) => readFileSync(join(HERE, name), "utf8");

// Colour tokens: the kit's own light and dark sets, then the JSHPhysics palette laid over them.
const tokens = (pattern) => k.ISO_CSS.match(pattern)[1].trim();
const DARK = tokens(/\.iso\{([^}]*)\}/);
const LIGHT = tokens(/\.iso\[data-theme="light"\]\{([^}]*)\}/);
const LIGHT_EXTRA =
  ";--anatomy-page:#f5f1ea;--anatomy-card:#fbf8f1;--anatomy-text:#4a4d54;--anatomy-strong:#1a1d22;--anatomy-muted:#8a8d94" +
  ";--anatomy-paper:#fbf8f1;--anatomy-face:#fffdf8;--anatomy-top:#fffdf8" +
  ";--anatomy-shade-0:#ddd6c8;--anatomy-shade-1:#e6e0d3;--anatomy-shade-2:#eee8dc;--anatomy-shade-3:#f4efe5" +
  ";--anatomy-lit-top:#ffffff;--anatomy-lit-shade:#f1ebdf" +
  ";--anatomy-hi:#1a1d22;--anatomy-mid:#8a8578;--anatomy-lo:#b9b3a4;--anatomy-faint:#d8d2c4;--anatomy-lit:#000000;--anatomy-dot:#33363c" +
  ";--anatomy-red:#d7263d;--anatomy-green:#3f7d4f;--anatomy-blue:#2b5fb8" +
  ';--anatomy-mono:"IBM Plex Mono",ui-monospace,Menlo,Consolas,monospace' +
  ";--accent:#c4502b;--heat:#c4502b;--cav-paper:#efe9dd;--cav-0:#d3ccbd;--cav-1:#dcd5c7;--cav-2:#e4ddd0;--cav-3:#eae4d8" +
  ";--btn:#fffdf8;--btn-on:#1a1d22;--btn-on-text:#f5f1ea;--rule:#d8d2c4;";
const DARK_EXTRA =
  ";--anatomy-page:#16181d;--anatomy-card:#1d2027;--anatomy-text:#b8b3a8;--anatomy-strong:#ede7db;--anatomy-muted:#8a877f" +
  ";--anatomy-paper:#1d2027;--anatomy-face:#262a33;--anatomy-top:#282c35" +
  ";--anatomy-shade-0:#15171c;--anatomy-shade-1:#191b21;--anatomy-shade-2:#1d2026;--anatomy-shade-3:#21242b" +
  ";--anatomy-lit-top:#343945;--anatomy-lit-shade:#292d37" +
  ";--anatomy-hi:#d9d3c7;--anatomy-mid:#7b7a75;--anatomy-lo:#4a4b4f;--anatomy-faint:#33353c;--anatomy-lit:#ffffff;--anatomy-dot:#ede7db" +
  ";--anatomy-red:#ff7b72;--anatomy-green:#8fd19e;--anatomy-blue:#7fa8ff" +
  ';--anatomy-mono:"IBM Plex Mono",ui-monospace,Menlo,Consolas,monospace' +
  ";--accent:#e8a382;--heat:#f08a55;--cav-paper:#14161a;--cav-0:#0f1114;--cav-1:#121418;--cav-2:#15171b;--cav-3:#181a1f" +
  ";--btn:#262a33;--btn-on:#ede7db;--btn-on-text:#16181d;--rule:#2c2f37;";


const css = read("page.css")
  .replace("/*LIGHT*/", LIGHT + LIGHT_EXTRA)
  .replaceAll("/*DARK*/", DARK + DARK_EXTRA);

const script = read("geom.mjs").replace(/^export /gm, "") + "\n" + read("motor.js") + "\n" + read("speaker.js");

// An empty drawing that the page script fills in.
const stage = (id, width, height, label, flat) =>
  `<div class="iso-stage${flat ? " hd-flat" : ""}" id="${id}"${flat ? "" : ' tabindex="0"'} role="group" aria-label="${label}"><svg xmlns="http://www.w3.org/2000/svg" class="iso-svg" viewBox="0 0 ${width} ${height}" role="img" aria-label="${label}"><g data-scene=""></g></svg></div>`;

const plate1 = k.plateHtml({
  fig: "Fig 1",
  title: "Simple DC motor",
  hint: "Drag to turn it round",
  readout: "",
  keys: [
    { mark: "red", label: "North pole" },
    { mark: "blue", label: "South pole" },
    { mark: "dashed", label: "Magnetic field, N to S" },
    { mark: "green", label: "Force on each long side of the coil" },
  ],
  caption:
    "One side of the coil and its half of the split ring are coloured yellow so you can follow them round. The white arrowheads show conventional current. The dashed lines are the magnetic field, from N to S.",
  body:
    stage("stage1", 860, 560, "A simple DC motor on a baseboard that you can turn round. A rectangular coil sits on an axle between a north and a south magnet. The ends of the coil join the two halves of a split-ring commutator, which two brushes touch. Leads run from the brushes to a cell. Arrow keys turn the view; space starts and stops the motor.") +
    `<div class="hd-controls">` +
    `<div class="hd-group"><button type="button" id="spin" aria-pressed="true">Pause</button><button type="button" id="battery" aria-pressed="false">Reverse cell</button><button type="button" id="magnets" aria-pressed="false">Swap magnets</button></div>` +
    `<label class="hd-slider" for="angle"><span>Coil</span><input type="range" id="angle" min="0" max="359" step="1" value="0"><output id="angle-out" for="angle">0°</output></label>` +
    `<div class="hd-group" role="group" aria-label="Show"><span>Show</span><button type="button" id="show-current" data-show="showCurrent" aria-pressed="true">Current</button><button type="button" id="show-forces" data-show="showForces" aria-pressed="true">Forces</button><button type="button" id="show-field" data-show="showField" aria-pressed="true">Field</button><button type="button" id="show-labels" data-show="labels" aria-pressed="true">Labels</button></div>` +
    `</div>`,
});

const plate2 = k.plateHtml({
  fig: "Fig 2",
  title: "Seen along the axle",
  hint: "Turns with Fig 1",
  readout: "",
  keys: [
    { mark: "green", label: "Force, and the size of the turning effect" },
    { mark: "red", label: "North pole" },
    { mark: "blue", label: "South pole" },
  ],
  caption:
    "The view from the commutator end. A dot is current coming towards you, a cross is current going away. The graph shows how the turning effect changes over one turn.",
  body: stage("stage2", 460, 460, "The motor seen along its axle from the commutator end, with a north magnet on one side and a south magnet on the other. The coil appears as a line with a circle at each end showing the current direction, a force arrow on each, the split ring in the middle and a brush on each side. Below it, a graph of turning effect against coil angle rises and falls twice per turn, dropping to zero while the coil is within 10 degrees of upright.", true),
});

const plate3 = k.plateHtml({
  fig: "Fig 3",
  title: "The split ring, step by step",
  hint: "Next and Back move all three figures",
  readout: "",
  keys: [
    { mark: "lit", label: "Yellow half-ring: joined to the yellow side of the coil" },
    { mark: "raised", label: "Copper half-ring: joined to the other side" },
    { mark: "green", label: "Force" },
  ],
  caption:
    "A close-up of the split-ring commutator from the same end as Fig 2. The ring turns with the coil; the two brushes and their leads stay still. The arrowheads on the leads show conventional current.",
  body:
    `<div class="sm-stepper">` +
    stage("stage3", 460, 410, "Close-up of the split-ring commutator seen along the axle. Two half-rings, one yellow and one copper, turn with the coil between a fixed positive brush and a fixed negative brush. Circles at the ends of the coil show the current direction in each side, with a force arrow on each.", true) +
    `<div class="sm-steptext" aria-live="polite"><p class="sm-stepcount" id="step-count"></p><h3 id="step-title"></h3><p id="step-body"></p>` +
    `<div class="hd-group sm-stepbuttons"><button type="button" id="step-back">Back</button><button type="button" id="step-next">Next</button></div></div>` +
    `</div>`,
});

const plate4 = k.plateHtml({
  fig: "Fig 4",
  title: "Loudspeaker, cut in half",
  hint: "Drag to turn it round",
  readout: "",
  keys: [
    { mark: "red", label: "North pole (centre)" },
    { mark: "blue", label: "South pole (outer ring)" },
    { mark: "dashed", label: "Magnetic field in the gap" },
    { mark: "green", label: "Force on the coil" },
  ],
  caption:
    "A moving-coil loudspeaker sliced down the middle. The magnet's cut face is a W on its side: a centre pole inside an outer ring. The coil sits in the gap round the centre pole and is fixed to the paper cone. The motion is drawn far slower than a real speaker.",
  body:
    stage("stage4", 860, 520, "A loudspeaker cut in half that you can turn round. A magnet with a centre north pole and an outer south ring has a coil in the gap round the centre pole. The coil is wound on a light tube joined to a paper cone, whose outer edge hangs from a fixed rim. Leads run from the coil to a signal source. Arrow keys turn the view; space starts and stops it.") +
    `<div class="hd-controls">` +
    `<div class="hd-group"><button type="button" id="spk-play" aria-pressed="true">Pause</button></div>` +
    `<div class="hd-group" role="group" aria-label="Pitch"><span>Pitch</span><button type="button" id="pitch-low" data-pitch="low" aria-pressed="true">Low</button><button type="button" id="pitch-high" data-pitch="high" aria-pressed="false">High</button></div>` +
    `<div class="hd-group" role="group" aria-label="Volume"><span>Volume</span><button type="button" id="volume-quiet" data-volume="0.5" aria-pressed="true">Quiet</button><button type="button" id="volume-loud" data-volume="1" aria-pressed="false">Loud</button></div>` +
    `<label class="hd-slider" for="spk-current"><span>Current by hand</span><input type="range" id="spk-current" min="-100" max="100" step="1" value="0"></label>` +
    `<div class="hd-group" role="group" aria-label="Show"><span>Show</span><button type="button" id="spk-show-current" data-spk-show="showCurrent" aria-pressed="true">Current</button><button type="button" id="spk-show-forces" data-spk-show="showForces" aria-pressed="true">Forces</button><button type="button" id="spk-show-field" data-spk-show="showField" aria-pressed="true">Field</button><button type="button" id="spk-show-labels" data-spk-show="labels" aria-pressed="true">Labels</button></div>` +
    `</div>`,
});

const plate5 = k.plateHtml({
  fig: "Fig 5",
  title: "Cross-section, with the signal",
  hint: "Moves with Fig 4",
  readout: "",
  keys: [
    { mark: "green", label: "Force on the coil, and the graph line" },
    { mark: "red", label: "North pole" },
    { mark: "blue", label: "South pole" },
  ],
  caption:
    "The same cut face, flat on. Each turn of the coil shows as a circle above and below the centre pole. A dot is current coming towards you, a cross is current going away. The curved lines to the right are the sound leaving the cone.",
  body: stage("stage5", 460, 430, "Cross-section of the loudspeaker. The magnet is a W shape on its side with a north pole in the middle and south poles outside. The coil appears as circles in the two gaps, with dots and crosses for the current and an arrow for the force. The cone flares out to the right. Below, a graph shows the alternating current in the coil against time.", true),
});

// The equations.  The artifact uses the browser's built-in MathML; the site copy uses the shared KaTeX.
const TEX = {
  force: "F = BIL",
  moment: "\\text{moment} = F \\times d",
};
const MATHML = {
  force: `<math display="block"><mrow><mi>F</mi><mo>=</mo><mi>B</mi><mi>I</mi><mi>L</mi></mrow></math>`,
  moment: `<math display="block"><mrow><mtext>moment</mtext><mo>=</mo><mi>F</mi><mo>×</mo><mi>d</mi></mrow></math>`,
};
const FONTS = `<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,700&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap">`;

// target: "artifact" or "site".
function pageBody(target) {
  const site = target === "site";
  const math = (name) => (site ? `<div class="hd-math" data-tex="${TEX[name]}"></div>` : `<div class="hd-math">${MATHML[name]}</div>`);
  const back = site ? `<a class="hd-back" href="../">← All JSHPhysics tools</a>` : "";
  const sibling = site ? ` The <a href="../hairdryer-anatomy/">hairdryer motor</a> shows how.` : "";
  return `<div class="iso hd-page">
<header class="hd-head">
${back}
<p class="hd-eyebrow">JSHPhysics · Electricity and magnetism</p>
<h1>The simple motor and loudspeaker</h1>
<p class="hd-lede">One coil of wire, two magnets, and a split ring that swaps the connections every half turn. Run it, turn it by hand, then reverse the cell or swap the magnets and predict which way it will go. The loudspeaker at the end uses the same force to make sound.</p>
</header>
${plate1}
<section class="hd-notes" data-for="split" aria-label="How the motor works">
<div><h2>The motor effect</h2><p>A wire carrying a current across a magnetic field feels a force at right angles to both the current and the field:</p>${math("force")}<p>Only the two long sides of the coil count. The field runs across them, so one is pushed up and the other down.</p></div>
<div><h2>Fleming's left-hand rule</h2><p>First finger along the field (N to S), second finger along the current, and the thumb gives the force. Pause the motor, pick a side of the coil, and check the green arrow against your hand.</p></div>
<div><h2>The split ring</h2><p>Each half of the ring is joined to one side of the coil and turns with it. The brushes stay still. Every half turn the two halves swap brushes, so the current in the coil reverses and the side that is now on the left is still pushed the same way.</p></div>
<div><h2>Why it needs the split ring</h2><p>Without it, the yellow side would be pushed up on one side of the axle and still pushed up on the other, which would turn the coil back again. It would rock to the upright position and stop.</p></div>
</section>
${plate2}
${plate3}
<section class="hd-notes" data-for="split" aria-label="Turning effect">
<div><h2>The force stays the same</h2><p>While current flows, the long sides are always at right angles to the field, so the force on each is the same size. What changes is how far the force acts from the axle:</p>${math("moment")}<p>When the coil is flat the distance is greatest. As it turns towards upright the distance shrinks, so the turning effect falls.</p></div>
<div><h2>The dead zone</h2><p>Near upright, each brush is over a gap in the split ring. The circuit is broken, no current flows, and the force arrows disappear. A running motor coasts through on its own momentum, then the brushes meet the other halves of the ring and the forces return. Stop it in the dead zone and it will not start again without a push.</p></div>
<div><h2>Reversing it</h2><p>Reverse the cell and the current in each side reverses, so both forces reverse. Swap the magnets and the field reverses, with the same result. Do both and the motor turns the original way.</p></div>
<div><h2>Making it better</h2><p>More turns on the coil, a larger current or stronger magnets all give a larger force. Real motors also use several coils at different angles, so there is never a dead spot.${sibling}</p></div>
</section>
<h2 class="ind-part"><span>Also the motor effect</span>The loudspeaker</h2>
${plate4}
${plate5}
<section class="hd-notes" aria-label="How the loudspeaker works">
<div><h2>The same force, in a straight line</h2><p>The coil sits in the gap between the centre pole and the outer ring, where the field points outwards. The current runs round the coil, at right angles to that field, so the force on every part of the coil is along the axis:</p>${math("force")}<p>Use Fleming's left-hand rule on any circle in Fig 5 to check the arrow.</p></div>
<div><h2>Why it vibrates</h2><p>The signal is an alternating current. Each time the current reverses, the force reverses, so the coil is pushed out, then pulled in. The cone is fixed to the coil and moves with it.</p></div>
<div><h2>Making sound</h2><p>The moving cone pushes the air in front of it, squashing it and then stretching it. Those pressure changes travel away as a sound wave with the same frequency as the current.</p></div>
<div><h2>Pitch and volume</h2><p>A higher frequency current makes the cone vibrate more times each second: a higher note. A larger current gives a larger force, so the cone moves further: a louder sound. Try the Pitch and Volume buttons.</p></div>
<div><h2>A steady current</h2><p>Pause it and drag Current by hand. The cone moves to a new position and stays there. A steady current makes no sound, because the cone has to keep moving to make a wave.</p></div>
<div><h2>Why the magnet is this shape</h2><p>With a centre pole inside a ring, the field crosses the gap in every direction outwards, so the whole length of the coil sits in the field and every part of it is pushed the same way.</p></div>
</section>
<footer class="hd-foot">Joshua Stafford-Haworth · JSHPhysics · @educatorJSH</footer>
</div>`;
}

const moduleScript = `<script type="module">${script.replace(/<\/(script)/gi, "<\\/$1")}</script>`;
const style = `<style>${k.ISO_CSS}${css}</style>`;

// 1. The artifact: a fragment, wrapped by the viewer.
const body = `<title>Simple Motor and Loudspeaker</title>
<meta name="claude:viewport-fit-sides" content="cover">
${FONTS}
${style}
${pageBody("artifact")}
${moduleScript}`;
writeFileSync(join(HERE, "artifact.html"), body);

// 2. The GitHub Pages copy: a complete page that follows the gallery's saved theme and uses its KaTeX.
const sitePage = `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Simple Motor and Loudspeaker · JSHPhysics</title>
<meta name="description" content="Interactive 3D models of the simple DC motor, with a step-by-step guide to its split-ring commutator, and the moving-coil loudspeaker.">
<meta name="author" content="Joshua Stafford-Haworth (JSHPhysics)">
<script>
// Use the theme chosen on the gallery page, if there is one.
try {
  var savedTheme = localStorage.getItem("jsh-theme");
  if (savedTheme) {
    document.documentElement.setAttribute("data-theme", savedTheme);
  }
} catch (error) {}
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
${FONTS}
<link rel="stylesheet" href="../lessons/vendor/katex.min.css">
${style}
</head>
<body>
${pageBody("site")}
<script src="../lessons/vendor/katex.min.js"></script>
<script>
// Typeset the equations.
document.querySelectorAll("[data-tex]").forEach(function (box) {
  if (window.katex) {
    window.katex.render(box.getAttribute("data-tex"), box, { displayMode: true, throwOnError: false });
  } else {
    box.textContent = box.getAttribute("data-tex");
  }
});
</script>
${moduleScript}
</body>
</html>
`;
mkdirSync(join(HERE, "site"), { recursive: true });
writeFileSync(join(HERE, "site", "index.html"), sitePage);

// 3. Test pages.  A hash such as #phi=0.5&az=120&el=25&battery=-1&magnets=-1 poses the model for a screenshot.
const poser = `<script>addEventListener("load",()=>setTimeout(()=>{const h=window.__motor;if(!h)return;const q=new URLSearchParams(location.hash.slice(1));const m=h.motor;if(q.has("phi")){h.setSpinning(false);m.phi=Number(q.get("phi"))}if(q.has("az"))m.view.azimuth=Number(q.get("az"));if(q.has("el"))m.view.elevation=Number(q.get("el"));if(q.has("battery"))m.battery=Number(q.get("battery"));if(q.has("magnets"))m.magnets=Number(q.get("magnets"));const s=window.__speaker;if(s&&q.has("spk")){s.setSpeakerPlaying(false);s.spk.current=Number(q.get("spk"));s.spk.dirty=true}if(s&&q.has("spkaz")){s.spk.view.azimuth=Number(q.get("spkaz"));s.spk.dirty=true}if(q.has("stage"))h.showStage(Number(q.get("stage")));m.dirty=true},300))</script>`;
for (const theme of ["light", "dark"]) {
  const page = `<!doctype html><html lang="en" data-theme="${theme}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><style>body{margin:0;font:14px system-ui,sans-serif}[hidden]{display:none!important}</style></head><body>${body}${poser}</body></html>`;
  writeFileSync(join(HERE, `test-${theme}.html`), page);
}
console.log("wrote artifact.html", Math.round(body.length / 1024) + " KB");
