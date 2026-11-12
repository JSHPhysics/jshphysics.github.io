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

const script = read("geom.mjs").replace(/^export /gm, "") + "\n" + read("motor.js");

// An empty drawing that the page script fills in.
const stage = (id, width, height, label, flat) =>
  `<div class="iso-stage${flat ? " hd-flat" : ""}" id="${id}"${flat ? "" : ' tabindex="0"'} role="group" aria-label="${label}"><svg xmlns="http://www.w3.org/2000/svg" class="iso-svg" viewBox="0 0 ${width} ${height}" role="img" aria-label="${label}"><g data-scene=""></g></svg></div>`;

const plate1 = k.plateHtml({
  fig: "Fig 1",
  title: "Coil, magnets and rings",
  hint: "Drag to turn it round",
  readout: "",
  keys: [
    { mark: "red", label: "North pole" },
    { mark: "blue", label: "South pole" },
    { mark: "dashed", label: "Magnetic field, N to S" },
    { mark: "green", label: "Force on each long side (motor)" },
  ],
  caption:
    "One side of the coil and the ring it joins are coloured yellow so you can follow them round. The white arrowheads show conventional current. In the generator, the orange arrows show which way each long side is moving, and the box on the board is a meter.",
  body:
    stage("stage1", 860, 560, "A model on a baseboard that you can turn round. A rectangular coil sits on an axle between a north and a south magnet. As a DC motor, the ends of the coil join the two halves of a split-ring commutator and leads run from two brushes to a cell. As an AC generator, the ends join two separate slip rings, each with its own brush, and the leads run to a meter. Arrow keys turn the view; space starts and stops it.") +
    `<div class="hd-controls">` +
    `<div class="hd-group" role="group" aria-label="Machine"><span>Machine</span><button type="button" id="design-split" data-design="split" aria-pressed="true">DC motor · split ring</button><button type="button" id="design-slip" data-design="slip" aria-pressed="false">AC generator · slip rings</button></div>` +
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
    { mark: "green", label: "Force (motor), and the graph line" },
    { mark: "red", label: "North pole" },
    { mark: "blue", label: "South pole" },
  ],
  caption:
    "The view from the ring end of the axle. A dot is current coming towards you, a cross is current going away. The graph shows one turn: the turning effect for the motor, or the current through the meter for the generator.",
  body: stage("stage2", 460, 460, "The motor seen along its axle from the commutator end, with a north magnet on one side and a south magnet on the other. The coil appears as a line with a circle at each end showing the current direction, a force arrow on each, the split ring in the middle and a brush on each side. Below it, a graph of turning effect against coil angle rises and falls twice per turn, dropping to zero while the coil is within 10 degrees of upright.", true),
});

const plate3 = k.plateHtml({
  fig: "Fig 3",
  title: "The rings, step by step",
  hint: "Next and Back move all three figures",
  readout: "",
  keys: [
    { mark: "lit", label: "Yellow ring or half-ring: joined to the yellow side of the coil" },
    { mark: "raised", label: "Copper ring or half-ring: joined to the other side" },
    { mark: "green", label: "Force (motor)" },
  ],
  caption:
    "A close-up from the same end as Fig 2. The rings turn with the coil; the brushes and their leads stay still. The arrowheads on the leads show conventional current. The two slip rings are really the same size, one behind the other. The far one is drawn larger so you can see both.",
  body:
    `<div class="sm-stepper">` +
    stage("stage3", 460, 410, "Close-up of the split-ring commutator seen along the axle. Two half-rings, one yellow and one copper, turn with the coil between a fixed positive brush and a fixed negative brush. Circles at the ends of the coil show the current direction in each side, with a force arrow on each.", true) +
    `<div class="sm-steptext" aria-live="polite"><p class="sm-stepcount" id="step-count"></p><h3 id="step-title"></h3><p id="step-body"></p>` +
    `<div class="hd-group sm-stepbuttons"><button type="button" id="step-back">Back</button><button type="button" id="step-next">Next</button></div></div>` +
    `</div>`,
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
<h1>The simple motor and generator</h1>
<p class="hd-lede">One coil of wire between two magnets makes a DC motor with a split ring, or an AC generator with slip rings. Switch between the two, run each one, and step through what the rings do.</p>
</header>
${plate1}
<section class="hd-notes" data-for="split" aria-label="How the motor works">
<div><h2>The motor effect</h2><p>A wire carrying a current across a magnetic field feels a force at right angles to both the current and the field:</p>${math("force")}<p>Only the two long sides of the coil count. The field runs across them, so one is pushed up and the other down.</p></div>
<div><h2>Fleming's left-hand rule</h2><p>First finger along the field (N to S), second finger along the current, and the thumb gives the force. Pause the motor, pick a side of the coil, and check the green arrow against your hand.</p></div>
<div><h2>The split ring</h2><p>Each half of the ring is joined to one side of the coil and turns with it. The brushes stay still. Every half turn the two halves swap brushes, so the current in the coil reverses and the side that is now on the left is still pushed the same way.</p></div>
<div><h2>Why it needs the split ring</h2><p>Without it, the yellow side would be pushed up on one side of the axle and still pushed up on the other, which would turn the coil back again. It would rock to the upright position and stop.</p></div>
</section>
<section class="hd-notes" data-for="slip" aria-label="How the generator works" hidden>
<div><h2>The generator effect</h2><p>Turn a coil in a magnetic field and its long sides cut across the field. That induces a potential difference across the ends of the coil, and a current if the circuit is complete. There is no cell: the energy comes from whoever turns the handle.</p></div>
<div><h2>Fleming's right-hand rule</h2><p>First finger along the field (N to S), thumb along the motion, and the second finger gives the induced current. Pause it, pick a side of the coil, and check the orange motion arrow and the white arrowhead against your hand.</p></div>
<div><h2>Slip rings</h2><p>Two complete rings, one joined to each end of the coil. Each ring always touches the same brush. Whatever the coil produces is passed straight on to the circuit, with nothing swapped.</p></div>
<div><h2>Why the current alternates</h2><p>Each long side moves up through the field for half a turn and down through it for the other half. The current induced in it reverses each time, so the current through the meter goes one way, then the other.</p></div>
</section>
${plate2}
${plate3}
<section class="hd-notes" data-for="split" aria-label="Turning effect">
<div><h2>The force stays the same</h2><p>While current flows, the long sides are always at right angles to the field, so the force on each is the same size. What changes is how far the force acts from the axle:</p>${math("moment")}<p>When the coil is flat the distance is greatest. As it turns towards upright the distance shrinks, so the turning effect falls.</p></div>
<div><h2>The dead zone</h2><p>Near upright, each brush is over a gap in the split ring. The circuit is broken, no current flows, and the force arrows disappear. A running motor coasts through on its own momentum, then the brushes meet the other halves of the ring and the forces return. Stop it in the dead zone and it will not start again without a push.</p></div>
<div><h2>Reversing it</h2><p>Reverse the cell and the current in each side reverses, so both forces reverse. Swap the magnets and the field reverses, with the same result. Do both and the motor turns the original way.</p></div>
<div><h2>Making it better</h2><p>More turns on the coil, a larger current or stronger magnets all give a larger force. Real motors also use several coils at different angles, so there is never a dead spot.${sibling}</p></div>
</section>
<section class="hd-notes" data-for="slip" aria-label="Size of the current" hidden>
<div><h2>Largest when flat</h2><p>The induced current depends on how fast the sides cut across the field. When the coil is flat the sides are moving straight across it, so the current is largest.</p></div>
<div><h2>Zero when upright</h2><p>When the coil is upright the sides are moving along the field lines and not cutting them, so for a moment nothing is induced. Unlike the motor's dead zone, nothing is disconnected.</p></div>
<div><h2>Reversing it</h2><p>Turn the coil the other way and every current reverses. Swap the magnets and the same thing happens. Do both and the current is back the way it started.</p></div>
<div><h2>Making it bigger</h2><p>Turn the coil faster, use stronger magnets or put more turns on the coil. Turning it faster also raises the frequency: more cycles each second.</p></div>
</section>
<section class="sm-compare" aria-label="Split ring and slip rings compared">
<h2>Split ring or slip rings?</h2>
<div class="sm-tablewrap"><table>
<thead><tr><th scope="col"></th><th scope="col">Split-ring commutator</th><th scope="col">Slip rings</th></tr></thead>
<tbody>
<tr><th scope="row">What it is</th><td>One ring cut into two halves, with a gap between them</td><td>Two complete rings, side by side on the axle</td></tr>
<tr><th scope="row">Joined to the coil</th><td>One half to each end of the coil</td><td>One ring to each end of the coil</td></tr>
<tr><th scope="row">At the brushes</th><td>The halves swap brushes every half turn</td><td>Each ring stays on its own brush</td></tr>
<tr><th scope="row">What that does</th><td>Reverses the connection to the coil every half turn</td><td>Passes the coil's current on unchanged</td></tr>
<tr><th scope="row">Found in</th><td>DC motor; dynamo (DC generator)</td><td>AC generator (alternator)</td></tr>
</tbody>
</table></div>
</section>
<footer class="hd-foot">Joshua Stafford-Haworth · JSHPhysics · @educatorJSH</footer>
</div>`;
}

const moduleScript = `<script type="module">${script.replace(/<\/(script)/gi, "<\\/$1")}</script>`;
const style = `<style>${k.ISO_CSS}${css}</style>`;

// 1. The artifact: a fragment, wrapped by the viewer.
const body = `<title>Simple Motor and Generator</title>
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
<title>Simple Motor and Generator · JSHPhysics</title>
<meta name="description" content="Interactive 3D model of the simple DC motor (split ring) and AC generator (slip rings), with current, field and force arrows and a step-by-step guide to the rings.">
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
const poser = `<script>addEventListener("load",()=>setTimeout(()=>{const h=window.__motor;if(!h)return;const q=new URLSearchParams(location.hash.slice(1));const m=h.motor;if(q.has("phi")){h.setSpinning(false);m.phi=Number(q.get("phi"))}if(q.has("az"))m.view.azimuth=Number(q.get("az"));if(q.has("el"))m.view.elevation=Number(q.get("el"));if(q.has("battery"))m.battery=Number(q.get("battery"));if(q.has("magnets"))m.magnets=Number(q.get("magnets"));if(q.has("design"))h.setDesign(q.get("design"));if(q.has("stage"))h.showStage(Number(q.get("stage")));m.dirty=true},300))</script>`;
for (const theme of ["light", "dark"]) {
  const page = `<!doctype html><html lang="en" data-theme="${theme}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><style>body{margin:0;font:14px system-ui,sans-serif}[hidden]{display:none!important}</style></head><body>${body}${poser}</body></html>`;
  writeFileSync(join(HERE, `test-${theme}.html`), page);
}
console.log("wrote artifact.html", Math.round(body.length / 1024) + " KB");
