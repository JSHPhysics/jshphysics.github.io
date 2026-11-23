// The parts of the room that change shape while the page is open.
// The build script and the page both use this file, so the first frame and every later frame match.
//
// Each function takes "kit" (the drawing functions) and "P" (the camera) and returns SVG markup.

// Where the curtains hang, in room units.
export const CURTAIN = {
  x: 3.4,
  top: 105,
  bottom: 38,
  folds: 5,
};

// The cupboard door: where its hinge is, how wide and thick it is, and its height range.
export const CUPBOARD_DOOR = {
  hingeX: 22,
  hingeY: 53,
  width: 42,
  thick: 1.4,
  zFrom: 4,
  zTo: 98,
};

// Join a list of 3D points into one SVG path.
export function pathThrough(kit, P, points, closed) {
  let d = "";
  for (let index = 0; index < points.length; index++) {
    const flat = kit.iso(points[index], P);
    let command = "L";
    if (index === 0) {
      command = "M";
    }
    d += command + flat[0].toFixed(1) + " " + flat[1].toFixed(1);
  }
  if (closed) {
    d += "Z";
  }
  return d;
}

// One curtain panel between yFrom and yTo.
// "sway" is how far the hem has drifted into the room, in room units.
export function curtainSvg(kit, P, yFrom, yTo, sway) {
  const topPoints = [];
  const hemPoints = [];
  const foldPaths = [];

  for (let fold = 0; fold <= CURTAIN.folds; fold++) {
    const share = fold / CURTAIN.folds;
    const y = yFrom + (yTo - yFrom) * share;

    // Each fold drifts a slightly different amount, so the hem ripples.
    const ripple = 0.7 + 0.3 * Math.sin(fold * 2.1);
    const drift = sway * ripple;

    const top = [CURTAIN.x, y, CURTAIN.top];
    const hem = [CURTAIN.x + drift, y + drift * 0.35, CURTAIN.bottom];
    topPoints.push(top);
    hemPoints.push(hem);

    // The first and last folds are the panel's own edges, so only the inner ones get a line.
    const isInner = fold > 0 && fold < CURTAIN.folds;
    if (isInner) {
      foldPaths.push(pathThrough(kit, P, [top, hem], false));
    }
  }

  // The outline runs along the top, then back along the hem.
  const outline = topPoints.concat(hemPoints.slice().reverse());
  const panel = '<path class="rm-cloth" d="' + pathThrough(kit, P, outline, true) + '"/>';
  const folds = kit.lineSvg(foldPaths.join(""), { tone: "lo" });
  return panel + folds;
}

// The cupboard door at a given opening angle, in degrees. 0 is shut.
export function cupboardDoorSvg(kit, P, degrees) {
  const door = CUPBOARD_DOOR;
  const angle = (degrees * Math.PI) / 180;

  // "along" points from the hinge to the free edge. "out" points out of the door's front face.
  const along = [Math.sin(angle), -Math.cos(angle)];
  const out = [Math.cos(angle), Math.sin(angle)];

  // A floor point on the door: "u" along its width, "t" through its thickness.
  const at = (u, t) => {
    const x = door.hingeX + along[0] * u + out[0] * t;
    const y = door.hingeY + along[1] * u + out[1] * t;
    return [x, y];
  };

  const ring = [at(0, 0), at(door.width, 0), at(door.width, door.thick), at(0, door.thick)];
  const height = door.zTo - door.zFrom;
  const slab = kit.solidSvg(kit.extrude(ring, door.zFrom, height, P), { tone: "hi" });

  // Which broad face is turned towards the viewer?
  const viewer = kit.towardViewer(P);
  const facing = out[0] * viewer[0] + out[1] * viewer[1];
  const frontShows = facing > 0.02;
  const backShows = facing < -0.02;

  // A rectangle drawn on one face of the door.
  const panel = (t, uFrom, uTo, zFrom, zTo) => {
    const a = at(uFrom, t);
    const b = at(uTo, t);
    const corners = [
      [a[0], a[1], zFrom],
      [b[0], b[1], zFrom],
      [b[0], b[1], zTo],
      [a[0], a[1], zTo],
    ];
    return pathThrough(kit, P, corners, true);
  };

  let detail = "";
  if (frontShows) {
    // The front has two framed panels and a round knob near the free edge.
    const face = door.thick + 0.05;
    const lower = panel(face, 5, door.width - 5, door.zFrom + 6, 46);
    const upper = panel(face, 5, door.width - 5, 52, door.zTo - 6);
    detail += kit.lineSvg(lower + upper, { tone: "lo" });
    const knob = at(door.width - 2.6, face);
    detail += kit.dotsSvg([kit.iso([knob[0], knob[1], 49], P)], { size: 1, tone: "hi" });
  }
  if (backShows) {
    // The back is plain: one frame line.
    const face = -0.05;
    const frame = panel(face, 4, door.width - 4, door.zFrom + 5, door.zTo - 5);
    detail += kit.lineSvg(frame, { tone: "lo" });
  }

  return slab + detail;
}
