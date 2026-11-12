// Builds the line spectra page: node src/build.mjs
// Writes artifact.html (a fragment for the Artifact viewer), site/index.html (the GitHub Pages copy)
// and test-light.html / test-dark.html (for checking).
// Fig 1 is drawn here with the Anatomy kit (bench.mjs).  The other figures are drawn in the browser by page.js.

import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import katex from "katex";
import * as k from "/mnt/skills/plugins/anatomy/kit/iso-kit.mjs";
import * as bench from "./bench.mjs";
import { ELEMENTS } from "./data.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const OUT = join(HERE, "..");
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

// base.css is the motor page's stylesheet (shared look); spectra.css adds this page's parts.
const css =
  read("base.css")
    .replace("/*LIGHT*/", LIGHT + LIGHT_EXTRA)
    .replaceAll("/*DARK*/", DARK + DARK_EXTRA) + read("spectra.css");

// What the page script needs to know about the Fig 1 drawing.
const BENCH = {
  camera: bench.benchCamera(),
  beamZ: bench.BEAM_Z,
  screenY: bench.SCREEN_Y,
  bandZ: bench.BAND_Z,
  tubeY: bench.TUBE_Y,
  tubePark: bench.TUBE_PARK,
  lampY: bench.LAMP_FRONT_Y,
  slitY: bench.SLIT_Y,
  lensY: bench.LENS_Y,
};
const script = read("data.mjs").replace(/^export /gm, "") + "\nconst BENCH = " + JSON.stringify(BENCH) + ";\n" + read("page.js");

// A group of buttons where one is pressed.  items: [value, label] pairs.
function buttonGroup(name, attribute, items, pressed, idPrefix) {
  let html = `<div class="hd-group" role="group" aria-label="${name}"><span>${name}</span>`;
  for (const [value, label] of items) {
    const on = pressed.includes(value);
    html += `<button type="button" id="${idPrefix}-${value}" data-${attribute}="${value}" aria-pressed="${on}">${label}</button>`;
  }
  return html + `</div>`;
}
const elementItems = ELEMENTS.map((element) => [element.id, element.name]);

const plate1 = k.plateHtml({
  fig: "Fig 1",
  title: "A spectroscope",
  hint: "Choose a source and a gas",
  readout: "",
  keys: [
    { mark: "lit", label: "Glass tube of gas" },
    { mark: "raised", label: "Slit, lens and diffraction grating" },
    { mark: "flat", label: "Dark screen" },
  ],
  caption:
    "Light from the source passes through a narrow slit and then a diffraction grating, which sends each wavelength off at its own angle, so each colour lands in its own place on the screen. The single line at the left end of the screen is light that went straight through. The strip underneath is the same spectrum laid flat against a wavelength scale.",
  body:
    `<div class="iso-stage sp-static" id="stage1">${bench.benchSvg()}</div>` +
    `<div class="sp-stack" id="strip1"></div>` +
    `<div class="hd-controls">` +
    buttonGroup(
      "Source",
      "source",
      [
        ["lamp", "Hot filament"],
        ["gas", "Hot gas"],
        ["both", "Filament through cool gas"],
      ],
      ["gas"],
      "source",
    ) +
    buttonGroup("Gas", "gas", elementItems, ["H"], "gas") +
    `</div>`,
});

const levelItems = [1, 2, 3, 4, 5, 6].map((n) => [String(n), "n = " + n]);
const plate2 = k.plateHtml({
  fig: "Fig 2",
  title: "Inside one hydrogen atom",
  hint: "Next and Back, or the arrow keys",
  readout: "",
  keys: [
    { mark: "lit", label: "Electron (also shown as the dot on the energy ladder)" },
    { mark: "edge", label: "Shells the electron is allowed to be on" },
    { mark: "dashed", label: "Ultraviolet and infrared: light the eye cannot see" },
  ],
  caption:
    "The same electron is shown twice: on its shell in the atom, and as a dot on the energy ladder. Every jump adds an arrow to the ladder and a line to one of the two spectra, in the colour of the light given out or absorbed. The shells are evenly spaced so they fit; the energy ladder is to scale above the break. The ends of the spectra are squashed to fit the ultraviolet and infrared on.",
  body:
    `<div class="sp-fig2"><div class="sp-fig2draw"><div class="sp-scroll"><svg xmlns="http://www.w3.org/2000/svg" id="atom" viewBox="0 0 860 510" role="img" aria-label="A hydrogen atom with six shells on the left and its energy level ladder on the right. An electron moves between shells; each move is matched by an arrow on the ladder and a line on one of two spectra at the bottom, an emission spectrum and an absorption spectrum."></svg></div>` +
    `<p class="sp-swipe">Swipe the diagram sideways to see the energy ladder.</p></div>` +
    `<div class="sp-steps"><div aria-live="polite"><p class="sp-kicker" id="step-count"></p><h3 id="step-title"></h3><p class="sp-stepbody" id="step-body"></p></div>` +
    `<div class="hd-group sp-buttons"><button type="button" id="step-back">Back</button><button type="button" id="step-next">Next</button><button type="button" id="step-replay">Replay</button><button type="button" id="present" aria-pressed="false">Full screen</button></div>` +
    `<div class="hd-controls sp-free">` +
    buttonGroup("Move the electron to", "level", levelItems, ["1"], "level") +
    `<div class="hd-group"><button type="button" id="clear-spectra">Clear spectra</button></div>` +
    `</div></div></div>`,
});

const plate3 = k.plateHtml({
  fig: "Fig 3",
  title: "Elements to try",
  hint: "Move across the strips to read a line",
  readout: "",
  keys: [],
  caption:
    "Real line positions for six elements. Choose one to see its spectrum, or several to see what a mixture gives: every line of every element, on one strip. Brighter lines are stronger, but the range of brightness is compressed so that weak lines can still be seen. A screen can only approximate the colour of each wavelength.",
  body:
    `<div class="hd-controls">` +
    buttonGroup("Elements", "pick", elementItems, ["H"], "pick") +
    buttonGroup(
      "Show",
      "kind",
      [
        ["emission", "Emission"],
        ["absorption", "Absorption"],
      ],
      ["emission"],
      "kind",
    ) +
    `</div>` +
    `<div class="sp-stack" id="mixer"></div>`,
});

const plate4 = k.plateHtml({
  fig: "Fig 4",
  title: "Decipher the spectrum",
  hint: "Drag references onto the unknown",
  readout: "",
  keys: [],
  caption:
    "Eight unknown spectra, from one element to a crowded mixture. Drag a reference spectrum by its name and lay it over the unknown to see whether its lines match; drop it there to add it to your mixture, whose spectrum is drawn underneath the unknown. Tapping a reference name, or the buttons, does the same. When your mixture matches the unknown line for line, press Check. Show answer gives the full reasoning.",
  body:
    `<div class="sp-quizhead"><div class="sp-dots" id="quiz-dots" role="group" aria-label="Questions"></div>` +
    `<div aria-live="polite"><p class="sp-kicker" id="quiz-count"></p><p class="sp-prompt" id="quiz-prompt"></p></div></div>` +
    `<div class="sp-stack" id="quiz-stack"></div>` +
    `<div class="sp-answer"><div class="hd-group" role="group" aria-label="Elements in your mixture" id="quiz-choices"></div>` +
    `<div class="hd-group"><button type="button" id="quiz-check">Check</button><button type="button" id="quiz-show">Show answer</button><button type="button" id="quiz-back">Back</button><button type="button" id="quiz-next">Next question</button></div>` +
    `<p class="sp-feedback" id="quiz-feedback" aria-live="polite"></p></div>`,
});

// The equations, written once in TeX.  The artifact gets MathML made here by KaTeX (no stylesheet needed);
// the site copy typesets the same TeX in the browser with the shared KaTeX.
const TEX = {
  photon: "E = hf",
  gap: "\\Delta E = hf = \\dfrac{hc}{\\lambda}",
  levels: "E_n = -\\dfrac{13.6\\ \\text{eV}}{n^2}",
  grating: "d\\sin\\theta = n\\lambda",
  worked1: "\\Delta E = ({-}1.51) - ({-}3.40) = 1.89\\ \\text{eV}",
  worked2: "\\Delta E = 1.89 \\times 1.60\\times10^{-19} = 3.02\\times10^{-19}\\ \\text{J}",
  worked3: "\\lambda = \\dfrac{hc}{\\Delta E} = \\dfrac{6.63\\times10^{-34} \\times 3.00\\times10^{8}}{3.02\\times10^{-19}} = 6.59\\times10^{-7}\\ \\text{m}",
};
// Check the worked example before printing it.
const workedJoules = 1.89 * 1.6e-19;
const workedMetres = (6.63e-34 * 3.0e8) / Number(workedJoules.toPrecision(3));
if (workedJoules.toPrecision(3) !== "3.02e-19" || workedMetres.toPrecision(3) !== "6.59e-7") {
  throw new Error("worked example does not match: " + workedJoules + " " + workedMetres);
}

const FONTS = `<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,700&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap">`;

// target: "artifact" or "site".
function pageBody(target) {
  const site = target === "site";
  function math(name) {
    if (site) {
      return `<div class="hd-math" data-tex="${TEX[name].replace(/"/g, "&quot;")}"></div>`;
    }
    return `<div class="hd-math">${katex.renderToString(TEX[name], { output: "mathml", displayMode: true })}</div>`;
  }
  let back = "";
  if (site) {
    back = `<a class="hd-back" href="../">← All JSHPhysics tools</a>`;
  }
  return `<div class="iso hd-page" id="page" data-course="gcse">
<header class="hd-head">
${back}
<p class="hd-eyebrow">JSHPhysics · Atoms and light</p>
<h1>Emission and absorption spectra</h1>
<p class="hd-lede">Every element gives out, and takes in, its own exact set of colours. Start with what a spectroscope shows, go inside one atom to see why, then use the patterns to work out which elements are in an unknown sample.</p>
<div class="hd-controls sp-course">${buttonGroup(
    "Level",
    "course-pick",
    [
      ["gcse", "GCSE"],
      ["alevel", "A-level"],
    ],
    ["gcse"],
    "course",
  )}</div>
</header>
${plate1}
<section class="hd-notes" aria-label="Three kinds of spectrum">
<div><h2>Continuous spectrum</h2><p>A hot solid, such as a lamp filament, gives out every wavelength. The screen shows an unbroken band from violet to red. Choose Hot filament to see it.</p></div>
<div><h2>Emission spectrum</h2><p>A hot, low-pressure gas glows with only a few exact wavelengths. The screen is dark apart from separate bright lines. Change the gas and the lines change.</p></div>
<div><h2>Absorption spectrum</h2><p>Shine the filament through the same gas when it is cool. The screen shows the continuous band again, but with dark lines in it. Compare them with the bright lines for the same gas.</p></div>
<div data-for="alevel"><h2>How the grating sorts the light</h2><p>The grating has 1000 slits in every millimetre. Light of each wavelength leaves it at its own angle:</p>${math("grating")}<p>Longer wavelengths are turned through bigger angles, so red lands furthest from the straight-through line.</p></div>
<div data-for="gcse"><h2>How the light is spread out</h2><p>The grating is a slide ruled with very fine lines. Like a prism, it sends each wavelength off in a slightly different direction, so the colours land side by side. Here red lands furthest from the straight-through line.</p></div>
</section>
${plate2}
<section class="hd-notes" data-for="gcse" aria-label="Why atoms give line spectra">
<div><h2>Electrons in shells</h2><p>Electrons orbit the nucleus in shells at fixed distances. An electron in a shell further from the nucleus has more energy. It cannot sit in between two shells.</p></div>
<div><h2>Giving out radiation</h2><p>When an electron falls to a lower shell, the atom emits electromagnetic radiation. Each possible fall gives out one exact wavelength. A bigger fall gives out more energy, which means a shorter wavelength.</p></div>
<div><h2>Absorbing radiation</h2><p>An atom can absorb electromagnetic radiation, and an electron moves to a higher shell. It only works if the radiation carries exactly the energy for that jump. Every other wavelength passes straight through.</p></div>
<div><h2>Why lines, not a rainbow</h2><p>The shells are fixed, so only certain jumps are possible, and each jump is one line at one wavelength. Different elements have different shells, so each has its own set of lines.</p></div>
<div><h2>Dark lines match bright lines</h2><p>Absorbing and emitting use the same jumps between the same shells. So the dark lines in an element's absorption spectrum sit at the same wavelengths as the bright lines in its emission spectrum.</p></div>
<div><h2>Where the absorbed light goes</h2><p>The electron soon falls back and the atom gives the light out again, but in a random direction. Very little of it carries on towards the screen, so the line still looks dark.</p></div>
</section>
<section class="hd-notes" data-for="alevel" aria-label="Why atoms give line spectra">
<div><h2>Energy levels</h2><p>An electron in an atom can only have certain energies. Each allowed energy is a shell, or energy level. The electron cannot sit in between, so it can only gain or lose energy in fixed amounts.</p></div>
<div><h2>One jump, one photon</h2><p>When an electron falls from a higher level to a lower one, the energy it loses leaves as a single photon. The photon's energy sets its frequency:</p>${math("photon")}<p>A bigger fall means a higher frequency and a shorter wavelength.</p></div>
<div><h2>Why lines, not a rainbow</h2><p>The gaps between levels are fixed, so only certain photon energies are possible. Each one is a line at one wavelength:</p>${math("gap")}<p>Different elements have different levels, so each has its own set of lines.</p></div>
<div><h2>Absorption uses the same gaps</h2><p>An atom can only absorb a photon whose energy exactly matches a gap between two of its levels. Those photons are removed from white light, and all the others pass through. The dark lines sit at the same wavelengths as the bright ones.</p></div>
<div><h2>Where the absorbed light goes</h2><p>The excited atom soon gives the photon out again, but in a random direction. Very little of it carries on in the direction of the original beam, so the line still looks dark against the bright spectrum either side.</p></div>
<div><h2>Going further: hydrogen's levels</h2><p>Hydrogen has one electron, and its levels follow a simple rule:</p>${math("levels")}<p>In a cool gas almost every atom is in n = 1, so cool hydrogen absorbs in the ultraviolet. Dark lines at visible wavelengths need atoms already in n = 2, which happens in the hot outer layers of stars.</p></div>
</section>
<section class="sp-worked" data-for="alevel" aria-label="Worked example">
<h2>Worked example: the red line of hydrogen</h2>
<p>An electron falls from n = 3 (−1.51 eV) to n = 2 (−3.40 eV). The photon carries away the difference:</p>
${math("worked1")}
<p>Convert to joules, using 1 eV = 1.60 × 10<sup>−19</sup> J:</p>
${math("worked2")}
<p>Then find the wavelength:</p>
${math("worked3")}
<p>That is about 660 nm, which is red light. The measured line is at 656 nm; the small difference comes from rounding the level energies to three significant figures. Try the same calculation for n = 4 to n = 2 and check it against Fig 2.</p>
</section>
${plate3}
<section class="hd-notes" aria-label="Using spectra">
<div><h2>A fingerprint</h2><p>No two elements have the same set of lines. If every bright line of an element appears in a spectrum, at exactly the right wavelengths, that element is present.</p></div>
<div><h2>Mixtures</h2><p>A mixture shows the lines of all its elements at once. To decipher it, match one element at a time and tick off its lines, until every line is explained.</p></div>
<div><h2>Position, not colour</h2><p>Two elements can both have a yellow line. What matters is the exact wavelength, and whether the element's other lines are there too. One matching line is never enough.</p></div>
<div><h2>What it is used for</h2><p>Spectra tell astronomers what stars are made of without going there. The same idea identifies the metal in a flame test and checks the gas in a discharge lamp.</p></div>
</section>
<h2 class="ind-part"><span>Now you try</span>Decipher the spectrum</h2>
${plate4}
<p class="sp-source">Line positions are measured wavelengths in air from the NIST Handbook of Basic Atomic Spectroscopic Data (neutral atoms). Only the stronger visible lines of each element are shown.</p>
<footer class="hd-foot">Joshua Stafford-Haworth · JSHPhysics · @educatorJSH</footer>
</div>`;
}

const moduleScript = `<script type="module">${script.replace(/<\/(script)/gi, "<\\/$1")}</script>`;
const style = `<style>${k.ISO_CSS}${css}</style>`;

// 1. The artifact: a fragment, wrapped by the viewer.
const body = `<title>Line Spectra</title>
<meta name="claude:viewport-fit-sides" content="cover">
${FONTS}
${style}
${pageBody("artifact")}
${moduleScript}`;
writeFileSync(join(OUT, "artifact.html"), body);

// 2. The GitHub Pages copy: a complete page that follows the gallery's saved theme and uses its KaTeX.
const sitePage = `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Line Spectra · JSHPhysics</title>
<meta name="description" content="How emission and absorption spectra work: a spectroscope, electron jumps in a hydrogen atom linked to its spectral lines, six elements to mix, and eight spectra to decipher.">
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
mkdirSync(join(OUT, "site"), { recursive: true });
writeFileSync(join(OUT, "site", "index.html"), sitePage);

// 3. Test pages, one for each theme.
for (const theme of ["light", "dark"]) {
  const page = `<!doctype html><html lang="en" data-theme="${theme}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><style>body{margin:0;font:14px system-ui,sans-serif}[hidden]{display:none!important}</style></head><body>${body}</body></html>`;
  writeFileSync(join(OUT, `test-${theme}.html`), page);
}
console.log("wrote artifact.html", Math.round(body.length / 1024) + " KB");
