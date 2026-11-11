// Builds the hairdryer page: node build3d.mjs
// Writes artifact.html (the page body to publish) and test-light.html / test-dark.html (for checking).
// Both figures are drawn in the browser from geom.mjs + scene.js, so this script only assembles the page.

import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "/mnt/skills/plugins/anatomy/kit/iso-kit.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const read = (name) => readFileSync(join(HERE, name), "utf8");

// Colour tokens: the kit's own light and dark sets, plus a few for this page.
const tokens = (pattern) => k.ISO_CSS.match(pattern)[1].trim();
const DARK = tokens(/\.iso\{([^}]*)\}/);
const LIGHT = tokens(/\.iso\[data-theme="light"\]\{([^}]*)\}/);
// The JSHPhysics house palette (cream and ink, with a dark mode), laid over the kit's tokens.
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

const script = read("geom.mjs").replace(/^export /gm, "") + "\n" + read("field.mjs").replace(/^export /gm, "") + "\n" + read("scene.js") + "\n" + read("live3d.js");

// An empty drawing that the page script fills in.
const stage = (id, width, height, label) =>
  `<div class="iso-stage" id="${id}" tabindex="0" role="group" aria-label="${label}"><svg xmlns="http://www.w3.org/2000/svg" class="iso-svg" viewBox="0 0 ${width} ${height}" role="img" aria-label="${label}"><g data-scene=""></g></svg></div>`;

const plate1 = k.plateHtml({
  fig: "Fig 1",
  title: "Hairdryer",
  hint: "Drag to turn it round",
  readout: "off",
  keys: [
    { mark: "lit", label: "Motor armature: the part that turns" },
    { mark: "raised", label: "Casing: make it solid, see-through or hidden" },
    { mark: "dim", label: "Heater coils glow orange when current flows" },
  ],
  caption:
    "From the back: air inlet, fan, motor, heater, nozzle. The motor and fan are drawn about 400 times slower than real life so you can see them turn.",
  body:
    stage("stage1", 860, 600, "A hairdryer you can turn round. Inside the casing, from the back: a fan, a small DC motor on three struts, and a heater made of two coils of wire on crossed mica boards. Arrow keys turn the view; keys 0, 1 and 2 set the switch to off, low and high.") +
    `<div class="hd-controls">` +
    `<div class="hd-group" role="group" aria-label="Hairdryer switch"><span>Switch</span><button type="button" id="level-0" data-level="0" aria-pressed="true">Off</button><button type="button" id="level-1" data-level="1" aria-pressed="false">Low</button><button type="button" id="level-2" data-level="2" aria-pressed="false">High</button></div>` +
    `<div class="hd-group" role="group" aria-label="Casing"><span>Casing</span><button type="button" id="case-0" data-case="0" aria-pressed="false">Solid</button><button type="button" id="case-1" data-case="1" aria-pressed="true">See-through</button><button type="button" id="case-2" data-case="2" aria-pressed="false">Hidden</button></div>` +
    `</div>`,
});

const plate2 = k.plateHtml({
  fig: "Fig 2",
  title: "The motor, enlarged",
  hint: "Drag to turn it round",
  readout: "",
  keys: [
    { mark: "red", label: "North pole" },
    { mark: "blue", label: "South pole" },
    { mark: "lit", label: "Lead from the + terminal" },
    { mark: "raised", label: "Lead from the − terminal" },
  ],
  caption:
    "Strip down slides the parts apart, removes the can and end caps, then closes up what is left: two magnets, the armature, the commutator, two brushes and the supply. Each armature pole is an electromagnet. Strong tint: that coil carries the full current. Pale tint: it shares the current with another coil.",
  body:
    stage("stage2", 860, 560, "The hairdryer's DC motor, which you can turn round. Two curved magnets, one north and one south, sit either side of a three-pole armature. Two carbon brushes press on a three-segment commutator, and leads run from the brushes to the positive and negative terminals of a supply. Arrow keys turn the view; space starts and stops the armature.") +
    `<div class="hd-controls">` +
    `<div class="hd-group"><button type="button" id="strip">Strip down</button><button type="button" id="labels" aria-pressed="true">Labels</button><button type="button" id="spin" aria-pressed="true">Pause</button></div>` +
    `<label class="hd-slider" for="angle"><span>Armature</span><input type="range" id="angle" min="0" max="359" step="1" value="0"><output id="angle-out" for="angle">0°</output></label>` +
    `</div>`,
});


const plate3 = k.plateHtml({
  fig: "Fig 3",
  title: "Wiring, seen along the shaft",
  hint: "Turns with Fig 2",
  readout: "",
  keys: [
    { mark: "lit", label: "Full current: one coil on its own between the brushes" },
    { mark: "raised", label: "Half current: two coils in series" },
    { mark: "red", label: "North pole" },
    { mark: "blue", label: "South pole" },
    { mark: "green", label: "Force on each side of a coil" },
  ],
  caption:
    "The three coils A, B and C are joined end to end in a ring. Each join is soldered to one commutator segment (the dots). The + and − brushes touch two of the three segments, so the current always has two routes round the ring. Beside each coil, a dot marks current coming out of the page and a cross marks current going in. The thin lines are the magnetic field, drawn from the inner face of the N magnet to the inner face of the S magnet. Curved and Straight are simplified pictures. Computed solves for the field in this cross-section, including the iron arms, the steel can and the coil currents.",
  body: `<div class="iso-stage hd-flat" id="stage3"><svg xmlns="http://www.w3.org/2000/svg" class="iso-svg" viewBox="0 0 460 430" role="img" aria-label="End-on wiring diagram of the motor. Three coils, A, B and C, are joined in a ring. Each join connects to one of three commutator segments. Two fixed brushes, plus and minus, touch the commutator on opposite sides. Current flows from the plus brush through one coil directly, and through the other two coils in series, to the minus brush."><g data-scene=""></g></svg></div><div class="hd-controls"><div class="hd-group" role="group" aria-label="Magnetic field"><span>Field</span><button type="button" id="field-curved" data-field="curved" aria-pressed="true">Curved</button><button type="button" id="field-straight" data-field="straight" aria-pressed="false">Straight</button><button type="button" id="field-computed" data-field="computed" aria-pressed="false">Computed</button></div></div>`,
});

// The two equations.  The published artifact uses the browser's built-in MathML;
// the GitHub Pages copy uses the site's self-hosted KaTeX (lessons/vendor).
const TEX = {
  torque: "F = BIL",
  heat: "\\Delta T = \\dfrac{P}{\\dot{m}\\,c} = \\dfrac{1800}{0.036 \\times 1005} \\approx 50\\ \\mathrm{K}",
};
const MATHML = {
  torque: `<math display="block"><mrow><mi>F</mi><mo>=</mo><mi>B</mi><mi>I</mi><mi>L</mi></mrow></math>`,
  heat: `<math display="block"><mrow><mi mathvariant="normal">Δ</mi><mi>T</mi><mo>=</mo><mfrac><mi>P</mi><mrow><mover><mi>m</mi><mo>˙</mo></mover><mi>c</mi></mrow></mfrac><mo>=</mo><mfrac><mn>1800</mn><mrow><mn>0.036</mn><mo>×</mo><mn>1005</mn></mrow></mfrac><mo>≈</mo><mn>50</mn><mspace width="0.25em"/><mi mathvariant="normal">K</mi></mrow></math>`,
};
const FONTS = `<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,700&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap">`;

// target: "artifact" (a fragment for the Artifact viewer) or "site" (the copy that lives in the GitHub Pages repo).
function pageBody(target) {
  const site = target === "site";
  const mathml = {
    torque: site ? `<div class="hd-math" data-tex="${TEX.torque}"></div>` : `<div class="hd-math">${MATHML.torque}</div>`,
    heat: site ? `<div class="hd-math" data-tex="${TEX.heat}"></div>` : `<div class="hd-math">${MATHML.heat}</div>`,
  };
  const back = site ? `<a class="hd-back" href="../">← All JSHPhysics tools</a>` : "";
  const eyebrow = `<p class="hd-eyebrow">JSHPhysics · Electricity and magnetism</p>`;
  return `<div class="iso hd-page">
<header class="hd-head">
${back}
${eyebrow}<h1>Inside a hairdryer</h1>
<p class="hd-lede">A hairdryer does two jobs. A small DC motor drives a fan that pushes air through the barrel, and a coil of resistance wire heats that air on its way out. Turn the dryer round, hide its casing, then take the motor apart.</p>
</header>
${plate1}
<section class="hd-notes" aria-label="Parts of the hairdryer">
<div><h2>Fan and motor</h2><p>The fan sits on the motor's shaft, just inside the air inlet. The motor is a low-voltage DC type, so the mains supply reaches it through a dropper coil and four diodes (the bridge rectifier: the row of four small blocks on the heater board).</p></div>
<div><h2>Heater</h2><p>Nichrome wire wound on a cross of mica boards. Mica does not conduct and does not burn. Low uses one element (900 W), High uses both (1800 W).</p></div>
<div><h2>Safety parts</h2><p>The square block on the board is a bimetallic thermostat. It opens the circuit if the air stops moving and the heater gets too hot. The long block beside it is a one-shot thermal fuse.</p></div>
<div><h2>How hot is the air?</h2><p>All the electrical power ends up heating the air that passes through. On High, 0.036 kg of air (specific heat capacity 1005 J/(kg K)) passes each second:</p>${mathml.heat}<p>Room air at 20 °C leaves at about 70 °C.</p></div>
</section>
${plate2}
${plate3}
<section class="hd-notes" aria-label="How the motor works">
<div><h2>Three coils, two brushes</h2><p>The coils are not wired to the terminals one each. They form a closed ring, and the brushes tap that ring at two points. From the + brush the current splits: one route goes through a single coil, the other through the remaining two in series. All three coils carry current all the time.</p></div>
<div><h2>Using Fleming's left-hand rule</h2><p>Each coil is wound round its arm, so its two long sides run along the shaft: in Fig 3 they point out of and into the page (the dot and the cross). Apply the rule to those sides, with the field running from N to S. The stripes across each coil are only its end turns. They lie in the page, and the forces on the front and back end turns cancel.</p></div>
<div><h2>Two forces make a turning pair</h2><p>The current in the two sides of a coil is in opposite directions, so the two forces are opposite. Together they twist the coil, exactly as in the one-coil motor. Each of these coils is that same rectangular coil, moved out from the shaft on its arm.</p></div>
<div><h2>What the computed field shows</h2><p>Switch Field to Computed for this. Iron carries flux far more easily than air, so the lines crowd into whichever arms face the magnets, cross the air gap almost at right angles to the iron, and return round the steel can. The copper sits beside the arms where the field is weak. In this model only about a fifth of the turning force acts on the copper. The rest acts on the iron.</p></div>
<div><h2>Cogging</h2><p>Three iron arms passing two magnets also give a pull that has nothing to do with the current: the arms prefer to sit lined up with the magnets. It adds to the drive for part of each sixth of a turn and opposes it for the rest, averaging zero. You can feel it as notches when you turn a small motor by hand.</p></div>
<div><h2>What changes as it turns</h2><p>Every sixth of a turn a gap in the commutator passes a brush. That brush moves on to the next segment, so a different coil becomes the one on its own, and one coil has its current reversed. Pause Fig 2 and drag the Armature slider to step through it.</p></div>
<div><h2>Where the current goes</h2><p>Follow the lead from the + terminal: it reaches one carbon brush, crosses to the copper commutator, runs through the armature coils, and leaves by the other brush to the − terminal.</p></div>
<div><h2>Force on a wire</h2><p>A wire carrying a current across a magnetic field feels a force at right angles to both:</p>${mathml.torque}<p>The coils sit in the field between the N and S magnets, so the forces on them turn the armature.</p></div>
<div><h2>Commutator and brushes</h2><p>The brushes stay still. The commutator turns with the armature. Each time a gap passes a brush, the current in one coil reverses, so its pole swaps between north and south.</p></div>
<div><h2>Why it keeps turning</h2><p>A pole swaps to south just as it reaches the S magnet. Like poles repel, so it is pushed on round instead of stopping there. Pause it and drag the Armature slider slowly past a magnet to watch the tint change.</p></div>
<div><h2>Why three poles?</h2><p>The one-coil motor in a textbook has two dead spots each turn where the force is zero. With three coils at 120° there is always at least one in a good position, so the motor starts from any angle.</p></div>
</section>
<footer class="hd-foot">Joshua Stafford-Haworth · JSHPhysics · @educatorJSH</footer>
</div>`;
}

const moduleScript = `<script type="module">${script.replace(/<\/(script)/gi, "<\\/$1")}</script>`;
const style = `<style>${k.ISO_CSS}${css}</style>`;

// 1. The artifact: a fragment, wrapped by the viewer.
const body = `<title>Hairdryer Anatomy</title>
<meta name="claude:viewport-fit-sides" content="cover">
${FONTS}
${style}
${pageBody("artifact")}
${moduleScript}`;

// 2. The GitHub Pages copy: a complete page that follows the gallery's saved theme and uses its KaTeX.
const sitePage = `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Hairdryer Anatomy · JSHPhysics</title>
<meta name="description" content="Interactive 3D hairdryer and DC motor: turn it round, strip it down, and see how the coils, commutator and magnets make it turn.">
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

writeFileSync(join(HERE, "artifact.html"), body);

// Test pages.  A hash such as #az=200&el=20&case=2&strip=1&level=2 poses the figures for a screenshot.
const poser = `<script>addEventListener("load",()=>setTimeout(()=>{const h=window.__hairdryer;const q=new URLSearchParams(location.hash.slice(1));if(!h)return;for(const f of [h.one,h.two]){if(q.has("az"))f.view.azimuth=Number(q.get("az"));if(q.has("el"))f.view.elevation=Number(q.get("el"));f.touched=true;f.dirty=true}if(q.has("case"))h.setCase(Number(q.get("case")));if(q.has("level"))h.setLevel(Number(q.get("level")),true);if(q.has("strip")){h.two.strip=Number(q.get("strip"));h.two.stripTarget=h.two.strip}if(q.has("phi")){h.setSpinning(false);h.two.phi=Number(q.get("phi"))}},300))</script>`;
for (const theme of ["light", "dark"]) {
  const page = `<!doctype html><html lang="en" data-theme="${theme}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><style>body{margin:0;font:14px system-ui,sans-serif}[hidden]{display:none!important}</style></head><body>${body}${poser}</body></html>`;
  writeFileSync(join(HERE, `test-${theme}.html`), page);
}
console.log("wrote artifact.html", Math.round(body.length / 1024) + " KB");
