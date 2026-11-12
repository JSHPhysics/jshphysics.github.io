// Builds the induction page: node build.mjs
// Writes artifact.html (a fragment for the Artifact viewer), site/index.html (the GitHub Pages copy)
// and test-light.html / test-dark.html (for checking).
// The figures are drawn in the browser from geom.mjs + machine.js + induction.js; this script only assembles the page.

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

const script = read("geom.mjs").replace(/^export /gm, "") + "\n" + read("machine.js") + "\n" + read("induction.js") + "\n" + read("touch.js");

// An empty drawing that the page script fills in.
function stage(id, width, height, label, flat) {
  let cls = "iso-stage";
  let focus = ' tabindex="0"';
  if (flat) {
    cls += " hd-flat";
    focus = "";
  }
  return `<div class="${cls}" id="${id}"${focus} role="group" aria-label="${label}"><svg xmlns="http://www.w3.org/2000/svg" class="iso-svg" viewBox="0 0 ${width} ${height}" role="img" aria-label="${label}"><g data-scene=""></g></svg></div>`;
}

const plateA = k.plateHtml({
  fig: "Fig 1",
  title: "Magnet and coil",
  hint: "Drag to turn it round",
  readout: "",
  keys: [
    { mark: "red", label: "North pole" },
    { mark: "blue", label: "South pole" },
    { mark: "lit", label: "Induced current (conventional)" },
    { mark: "dashed", label: "Dashed labels: the poles the induced current gives the coil" },
  ],
  caption:
    "A bar magnet on a handle, a coil of wire wound on a card tube, and a centre-zero meter. The meter only moves while the magnet is moving.",
  body:
    stage("stage-a", 860, 500, "A model you can turn round: a bar magnet on a handle is pushed into and pulled out of a coil of wire wound on a tube. Leads run from the two ends of the coil to a centre-zero meter. Arrow keys turn the view.", false) +
    `<div class="hd-controls">` +
    `<div class="hd-group"><button type="button" id="push">Push in</button><button type="button" id="pull">Pull out</button><button type="button" id="flip" aria-pressed="false">Turn magnet round</button></div>` +
    `<label class="hd-slider" for="magnet"><span>Move it yourself</span><input type="range" id="magnet" min="0" max="100" step="1" value="0"></label>` +
    `<div class="hd-group" role="group" aria-label="Speed"><span>Speed</span><button type="button" id="speed-slow" data-speed="slow" aria-pressed="true">Slow</button><button type="button" id="speed-fast" data-speed="fast" aria-pressed="false">Fast</button></div>` +
    `<div class="hd-group" role="group" aria-label="Turns on the coil"><span>Turns</span><button type="button" id="turns-5" data-turns="5" aria-pressed="true">5</button><button type="button" id="turns-10" data-turns="10" aria-pressed="false">10</button></div>` +
    `<div class="hd-group" role="group" aria-label="Show"><span>Show</span><button type="button" id="coil-current" data-coil-show="showCurrent" aria-pressed="true">Current</button><button type="button" id="coil-labels" data-coil-show="labels" aria-pressed="true">Labels</button></div>` +
    `</div>`,
});

const plateB = k.plateHtml({
  fig: "Fig 2",
  title: "From the side, with a trace",
  hint: "Moves with Fig 1",
  readout: "",
  keys: [
    { mark: "green", label: "Trace of the meter reading" },
    { mark: "dashed", label: "The magnet's field (sketched)" },
  ],
  caption:
    "The coil is cut through, so each turn shows as a circle at the top and at the bottom. A dot is current coming towards you, a cross is current going away. The trace records the meter reading for the last eight seconds.",
  body: stage("stage-b", 460, 450, "Side view of the magnet and the coil. The coil is shown in section as a row of circles above and below the tube, with dots and crosses for the direction of the induced current. Letters at the ends of the coil show which pole each end becomes. Below, a graph traces the meter reading against time.", true),
});

const plateC = k.plateHtml({
  fig: "Fig 3",
  title: "A coil turned between magnets",
  hint: "Drag to turn it round",
  readout: "",
  keys: [
    { mark: "red", label: "North pole" },
    { mark: "blue", label: "South pole" },
    { mark: "dashed", label: "Magnetic field, N to S" },
    { mark: "lit", label: "Induced current (conventional)" },
  ],
  caption:
    "One side of the coil and the ring it joins are coloured yellow so you can follow them round. The orange arrows show which way each long side is moving. The box on the board is a centre-zero meter.",
  body:
    stage("stage-c", 860, 560, "A model you can turn round: a rectangular coil on an axle is turned between a north and a south magnet. As an AC generator its ends join two slip rings, each with its own brush. As a dynamo its ends join the two halves of a split ring. Leads run from the brushes to a meter. Arrow keys turn the view; space starts and stops it.", false) +
    `<div class="hd-controls">` +
    `<div class="hd-group" role="group" aria-label="Machine"><span>Machine</span><button type="button" id="design-slip" data-design="slip" aria-pressed="true">AC generator · slip rings</button><button type="button" id="design-dynamo" data-design="dynamo" aria-pressed="false">Dynamo · split ring</button></div>` +
    `<div class="hd-group"><button type="button" id="spin" aria-pressed="true">Pause</button><button type="button" id="reverse" aria-pressed="false">Reverse turning</button><button type="button" id="magnets" aria-pressed="false">Swap magnets</button></div>` +
    `<div class="hd-group" role="group" aria-label="Turning speed"><span>Turn it</span><button type="button" id="rate-normal" data-rate="0.5" aria-pressed="true">Slowly</button><button type="button" id="rate-fast" data-rate="1" aria-pressed="false">Fast</button></div>` +
    `<label class="hd-slider" for="angle"><span>Coil</span><input type="range" id="angle" min="0" max="359" step="1" value="0"><output id="angle-out" for="angle">0°</output></label>` +
    `<div class="hd-group" role="group" aria-label="Show"><span>Show</span><button type="button" id="gen-current" data-gen-show="showCurrent" aria-pressed="true">Current</button><button type="button" id="gen-motion" data-gen-show="showForces" aria-pressed="true">Motion</button><button type="button" id="gen-field" data-gen-show="showField" aria-pressed="true">Field</button><button type="button" id="gen-labels" data-gen-show="labels" aria-pressed="true">Labels</button></div>` +
    `</div>`,
});

const plateD = k.plateHtml({
  fig: "Fig 4",
  title: "Seen along the axle, with the output",
  hint: "Turns with Fig 3",
  readout: "",
  keys: [
    { mark: "green", label: "Current through the meter" },
    { mark: "red", label: "North pole" },
    { mark: "blue", label: "South pole" },
  ],
  caption:
    "The view from the ring end. A dot is current coming towards you, a cross is current going away. The graph covers the same stretch of time at either speed, so turning the coil fast fits in twice as many turns.",
  body: stage("stage-d", 460, 460, "The generator seen along its axle from the ring end, between a north and a south magnet. The coil appears as a line with a circle at each end showing the direction of the induced current and an arrow showing which way that side is moving. Below, a graph shows the current through the meter against time: a wave that goes above and below zero for the AC generator, and a row of humps that stay above zero for the dynamo.", true),
});

// The equation.  The artifact uses the browser's built-in MathML; the site copy uses the shared KaTeX.
const TEX = {
  faraday: "\\varepsilon = -N\\,\\dfrac{\\Delta\\Phi}{\\Delta t}",
};
const MATHML = {
  faraday: `<math display="block"><mrow><mi>ε</mi><mo>=</mo><mo>−</mo><mi>N</mi><mfrac><mrow><mi mathvariant="normal">Δ</mi><mi mathvariant="normal">Φ</mi></mrow><mrow><mi mathvariant="normal">Δ</mi><mi>t</mi></mrow></mfrac></mrow></math>`,
};
const FONTS = `<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,700&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap">`;

// An "exam-style explanation": a titled, numbered chain of reasoning in the author's own wording.
function examBox(title, steps) {
  const items = steps.map((step) => `<li>${step}</li>`).join("");
  return `<div class="exam-box"><p class="exam-kicker">Exam-style explanation</p><h2>${title}</h2><ol>${items}</ol></div>`;
}
function examSection(boxes) {
  return `<section class="exam" aria-label="Exam-style explanations">${boxes.join("")}</section>`;
}
const EXAM = {
  wire: examBox("The motor effect on a single wire", [
    "There is a current in the wire.",
    "This creates a magnetic field around the wire.",
    "This interacts with the permanent magnetic field.",
    "This causes a resultant force on the wire, so the wire accelerates.",
    "You can find the direction of the force using Fleming's left-hand rule.",
  ]),
  motor: examBox("The motor effect in a motor", [
    "There is a current in the coil.",
    "This creates a magnetic field around the coil.",
    "This interacts with the permanent magnetic field.",
    "This causes a resultant force on the coil.",
    "The direction of the force is opposite on either side of the coil.",
    "So the coil rotates.",
  ]),
  speaker: examBox("The motor effect in a loudspeaker", [
    "There is a current in the coil.",
    "This creates a magnetic field around the coil.",
    "This interacts with the permanent magnetic field.",
    "This causes a resultant force on the coil.",
    "The direction of the force is the same on either side of the coil.",
    "So the coil moves forwards or backwards. You can find the direction using Fleming's left-hand rule.",
    "With an alternating current, the force alternates back and forth at the same frequency as the current.",
  ]),
  induction: examBox("Induction", [
    "The wire or coil moves through the magnetic field of the permanent magnet.",
    "So the wire or coil experiences a changing magnetic field.",
    "This induces a potential difference across the wire or coil.",
    "If the wire or coil is in a closed circuit, a current flows.",
  ]),
};

// target: "artifact" or "site".
function pageBody(target) {
  const site = target === "site";
  let faraday = `<div class="hd-math">${MATHML.faraday}</div>`;
  let back = "";
  let sibling = "";
  if (site) {
    faraday = `<div class="hd-math" data-tex="${TEX.faraday}"></div>`;
    back = `<a class="hd-back" href="../">← All JSHPhysics tools</a>`;
    sibling = ` Run it the other way, with a cell in place of the meter, and it is a motor: see the <a href="../simple-motor/">simple motor</a>.`;
  }
  return `<div class="iso hd-page">
<header class="hd-head">
${back}
<p class="hd-eyebrow">JSHPhysics · Electricity and magnetism</p>
<h1>Electromagnetic induction</h1>
<p class="hd-lede">Change the magnetic field through a coil and a potential difference is induced across it. Start with a magnet and a coil, then see the same idea at work in an AC generator and a dynamo.</p>
</header>
<h2 class="ind-part"><span>Part 1</span>A magnet and a coil</h2>
${plateA}
${plateB}
${examSection([EXAM.induction])}
<section class="hd-notes" aria-label="A magnet and a coil">
<div><h2>What it takes</h2><p>A potential difference is induced across the coil only while the magnetic field through it is changing. Leave the magnet still, inside or outside the coil, and the meter reads zero however strong the magnet is.</p></div>
<div><h2>Making it bigger</h2><p>Move the magnet faster, or put more turns on the coil. Try Fast, then 10 turns. A stronger magnet does the same. Dragging the slider yourself, the quicker you drag, the further the needle swings.</p></div>
<div><h2>Reversing it</h2><p>Pull the magnet out and the needle swings the other way. Turn the magnet round so the other pole leads and it reverses too. Do both and it is back the way it started.</p></div>
<div><h2>It opposes the change</h2><p>The induced current turns the coil into an electromagnet. Push a north pole in and the near end of the coil becomes a north pole, which repels it. Pull it out and that end becomes a south pole, which attracts it. Either way you have to do work to keep the magnet moving, and that work is where the electrical energy comes from.</p></div>
<div><h2>Faraday's law</h2><p>The induced e.m.f. equals the rate of change of flux linkage:</p>${faraday}<p>The trace in Fig 2 is the gradient of the flux linkage through the coil. It returns to zero once the magnet stops, even though the flux linkage is then at its largest.</p></div>
</section>
<h2 class="ind-part"><span>Part 2</span>A coil turning between magnets</h2>
${plateC}
${plateD}
<section class="hd-notes" aria-label="Generators">
<div><h2>The same idea, turning</h2><p>Here the magnets stay still and the coil moves. As it turns, the field through the coil keeps changing, so a potential difference is induced the whole time it is turning. The current is largest when the long sides cut straight across the field, and zero when they move along it.</p></div>
<div data-for="slip"><h2>The AC generator</h2><p>Each end of the coil is joined to its own slip ring, and each ring stays on its own brush. The current in the coil reverses every half turn, and the rings pass it straight on, so the meter swings one way and then the other. That is alternating current.</p></div>
<div data-for="dynamo" hidden><h2>The dynamo</h2><p>The ends of the coil are joined to the two halves of a split ring. The current in the coil still reverses every half turn, but at that moment the halves swap brushes. The current through the meter always flows the same way. It rises and falls, but it never reverses: direct current.</p></div>
<div><h2>Turning it faster</h2><p>The field through the coil changes more quickly, so the current is larger. Each turn also takes less time, so the peaks come closer together. Compare Slowly and Fast on the graph in Fig 4.</p></div>
<div><h2>Reversing it</h2><p>Turn the coil the other way, or swap the magnets, and every induced current reverses.${sibling}</p></div>
</section>
<section class="sm-compare" aria-label="AC generator and dynamo compared">
<h2>AC generator or dynamo?</h2>
<div class="sm-tablewrap"><table>
<thead><tr><th scope="col"></th><th scope="col">AC generator (alternator)</th><th scope="col">Dynamo</th></tr></thead>
<tbody>
<tr><th scope="row">Rings</th><td>Two slip rings, one joined to each end of the coil</td><td>One split ring, half joined to each end of the coil</td></tr>
<tr><th scope="row">Current in the coil</th><td>Reverses every half turn</td><td>Reverses every half turn</td></tr>
<tr><th scope="row">At the brushes</th><td>Each ring stays on its own brush</td><td>The halves swap brushes every half turn</td></tr>
<tr><th scope="row">Current in the circuit</th><td>Alternating: one way, then the other</td><td>Direct: always the same way, rising and falling</td></tr>
<tr><th scope="row">Graph</th><td>A wave above and below zero</td><td>A row of humps, all on one side of zero</td></tr>
</tbody>
</table></div>
</section>
<footer class="hd-foot">Joshua Stafford-Haworth · JSHPhysics · @educatorJSH</footer>
</div>`;
}

const moduleScript = `<script type="module">${script.replace(/<\/(script)/gi, "<\\/$1")}</script>`;
const style = `<style>${k.ISO_CSS}${css}</style>`;

// 1. The artifact: a fragment, wrapped by the viewer.
const body = `<title>Electromagnetic Induction</title>
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
<title>Electromagnetic Induction · JSHPhysics</title>
<meta name="description" content="Interactive 3D models of electromagnetic induction: a magnet pushed into a coil, an AC generator with slip rings and a dynamo with a split ring.">
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

// 3. Test pages.  A hash such as #x=-40&v=80&turns=10&design=dynamo&phi=0.6&rate=1 poses the figures for a screenshot.
const poser = `<script>addEventListener("load",()=>setTimeout(()=>{const h=window.__induction;if(!h)return;const q=new URLSearchParams(location.hash.slice(1));const c=h.coilFig;const g=h.gen;if(q.has("x")){c.touring=false;c.target=null;c.x=Number(q.get("x"));c.previousX=c.x;c.hold=Number(q.get("v")||0)}if(q.has("turns"))c.turns=Number(q.get("turns"));if(q.has("pole"))c.pole=Number(q.get("pole"));if(q.has("az")){c.view.azimuth=Number(q.get("az"));g.view.azimuth=Number(q.get("az"))}if(q.has("design")){document.getElementById("design-"+q.get("design")).click()}if(q.has("rate"))g.speedFactor=Number(q.get("rate"));if(q.has("phi")){h.setGenSpinning(false);g.phi=Number(q.get("phi"))}g.dirty=true},300))</script>`;
for (const theme of ["light", "dark"]) {
  const page = `<!doctype html><html lang="en" data-theme="${theme}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><style>body{margin:0;font:14px system-ui,sans-serif}[hidden]{display:none!important}</style></head><body>${body}${poser}</body></html>`;
  writeFileSync(join(HERE, `test-${theme}.html`), page);
}
console.log("wrote artifact.html", Math.round(body.length / 1024) + " KB");
