#!/usr/bin/env node
// Render a graph spec (JSON file or inline JSON) to an SVG file so an author
// can look at it. Usage: node tools/render_graph.js spec.json out.svg
const fs = require("fs");
const path = require("path");
const graphs = require(path.join(__dirname, "..", "js", "graphs.js"));

const [,, specArg, outPath] = process.argv;
if (!specArg) {
  console.error("usage: node tools/render_graph.js <spec.json | '{...}'> [out.svg]");
  process.exit(2);
}
const raw = fs.existsSync(specArg) ? fs.readFileSync(specArg, "utf8") : specArg;
const spec = JSON.parse(raw);
const problems = graphs.validate(spec);
if (problems.length) {
  console.error("Invalid graph spec:\n  " + problems.join("\n  "));
  process.exit(1);
}
const result = graphs.render(spec);
// Standalone SVG with simple styling so it opens in any viewer
const styled = result.svg.replace("<svg ", "<svg style=\"background:#fff;font-family:sans-serif\" ").replace("</svg>",
  "<style>text{font-size:12px;fill:#333}.g-minor line{stroke:#e6e6e6;stroke-width:.6}.g-major line{stroke:#bdbdbd}.g-axis line{stroke:#000;stroke-width:1.4}" +
  ".g-line{fill:none;stroke:#000;stroke-width:2}.g-dashed{fill:none;stroke:#444;stroke-dasharray:5 4}.g-tangent{fill:none;stroke:#c33;stroke-width:1.6}" +
  ".g-data path{fill:none;stroke:#000;stroke-width:1.6}.g-shade{fill:#c33;opacity:.16}.g-drop{stroke:#c33;stroke-dasharray:3 3}.g-mark{fill:#fff;stroke:#c33;stroke-width:2}" +
  ".g-marklabel{font-weight:600;font-size:13px;fill:#a22;font-style:italic}.g-label{font-style:italic}</style></svg>");
const wrapped = "<!-- y: " + result.yLabel + "   x: " + result.xLabel + " -->\n" + styled;
if (outPath) {
  fs.writeFileSync(outPath, wrapped);
  console.log("wrote " + outPath);
} else {
  process.stdout.write(wrapped);
}
