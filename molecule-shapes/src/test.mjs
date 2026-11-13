// Checks the model before anything is drawn.
import * as M from "./model.mjs";

let failures = 0;

function check(label, pass) {
  if (!pass) {
    failures = failures + 1;
    console.log("FAIL", label);
  }
}

for (const molecule of M.MOLECULES) {
  const angles = M.bondAngles(molecule);
  console.log(molecule.id.padEnd(6), molecule.shape.padEnd(22), "bp", M.countOf(molecule, "bond"), "lp", M.countOf(molecule, "lone"), angles.join(", "));

  // The number of electron pairs matches the stated number of regions.
  check(molecule.id + " regions", molecule.pairs.length === molecule.regions);

  // Every quoted angle really exists between two bonds of the model.
  for (const quoted of molecule.quote) {
    const present = angles.some((angle) => Math.abs(angle - quoted) < 0.06);
    check(molecule.id + " quotes " + quoted, present);
  }

  // The protractor starts on two bonds, at the first quoted angle.
  const a = molecule.pairs[molecule.measure[0]];
  const b = molecule.pairs[molecule.measure[1]];
  check(molecule.id + " measures bonds", a.type === "bond" && b.type === "bond");
  check(molecule.id + " measures quoted angle", Math.abs(M.angleBetween(a.dir, b.dir) - molecule.quote[0]) < 0.06);

  // The stem must not run into any electron pair: at least 40 degrees clear.
  const stem = M.fromDown(molecule.mount.polar, molecule.mount.azimuth);
  for (const pair of molecule.pairs) {
    check(molecule.id + " stem clear", M.angleBetween(stem, pair.dir) > 40);
  }

  // In the textbook pose the orientation is a pure turn about the vertical.
  const R = M.orientation(0, molecule.mount.polar, 0, molecule.mount);
  const up = M.matApply(R, [0, 0, 1]);
  check(molecule.id + " textbook pose upright", Math.abs(up[2] - 1) < 1e-9);

  // The stem always follows the carriage on the quadrant.
  const tilted = M.matApply(M.orientation(0, 30, 77, molecule.mount), stem);
  check(molecule.id + " stem on carriage", M.angleBetween(tilted, [Math.sin(Math.PI / 6), 0, -Math.cos(Math.PI / 6)]) < 1e-4);
}

if (failures === 0) {
  console.log("model checks passed");
} else {
  console.log(failures + " model checks failed");
  process.exit(1);
}
