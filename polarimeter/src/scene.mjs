// The polarimeter's parts, drawn with the kit for any camera.
// The build script uses this for the first picture; the page uses the same
// code to redraw the bench whenever it is turned or tilted.
//
//   const scene = createScene(k, G);   k = the kit, G = its round-part module
//   scene.build(P)                     the figure's markup for projection P

export function createScene(k, G) {
  // ---------- dimensions (world units; the light travels along +x) ----------

  const WIDTH = 900;
  const HEIGHT = 500;

  const AXIS_Z = 58; // height of the optical axis
  const PLATE = { x: -176, y: -40, w: 342, d: 80, r: 8 };
  const PLATE_H = 8;
  const FOOT_H = 4;
  const RAIL = { x: -168, y: -9, w: 326, d: 18, r: 1.5 };
  const RAIL_H = 5;
  const CARRIAGE_TOP = 10;

  const X_LAMP = -140;
  const X_LENS = -100;
  const X_POLARISER = -68;
  const X_TUBE_START = -36;
  const X_TUBE_END = 36;
  const X_ANALYSER = 72;
  const X_EYEPIECE = 112;


  // ---------- how far each part travels when the instrument comes apart ----------
  // offset is in world units; delay staggers the start of each part's move.

  const MOVES = {
    lampBase: { offset: [0, 0, 0], delay: 0 },
    lampHousing: { offset: [0, 0, 62], delay: 0 },
    lensHolder: { offset: [0, 0, 0], delay: 0 },
    lens: { offset: [10, 0, 0], delay: 0.1 },
    polariserHolder: { offset: [0, 0, 0], delay: 0 },
    polariserFilter: { offset: [10, 0, 0], delay: 0.1 },
    polariserRing: { offset: [19, 0, 0], delay: 0.2 },
    trough: { offset: [0, 0, 0], delay: 0 },
    capLeft: { offset: [-9, 0, 40], delay: 0.15 },
    beamTube: { offset: [0, 0, 40], delay: 0 },
    glass: { offset: [0, 0, 40], delay: 0.05 },
    capRight: { offset: [9, 0, 40], delay: 0.15 },
    analyserHolder: { offset: [0, 0, 0], delay: 0 },
    analyserFilter: { offset: [9, 0, 0], delay: 0.1 },
    analyserCollar: { offset: [18, 0, 0], delay: 0.2 },
    eyepieceBody: { offset: [14, 0, 0], delay: 0 },
    eyepieceLens: { offset: [23, 0, 0], delay: 0.1 },
    eyepieceCup: { offset: [31, 0, 0], delay: 0.2 },
  };

  // The numbered pins: where each stands, and which moving part it rides on.
  const PINS = [
    { number: 1, family: "lamp", name: "Sodium lamp", rides: "lampHousing", at: [X_LAMP, 0, 87] },
    { number: 2, family: "lens", name: "Lens", rides: "lens", at: [X_LENS + 2, 0, AXIS_Z + 14.5] },
    { number: 3, family: "polariser", name: "Polariser", rides: "polariserFilter", at: [X_POLARISER + 3, 0, AXIS_Z + 18.5] },
    { number: 4, family: "tube", name: "Sample tube", rides: "glass", at: [0, 0, AXIS_Z + 8] },
    { number: 5, family: "analyser", name: "Analyser", rides: "analyserCollar", at: [X_ANALYSER + 7, 0, AXIS_Z + 18.5] },
    { number: 6, family: "scale", name: "Angle scale", rides: "analyserHolder", at: [X_ANALYSER, 0, AXIS_Z + 27], stem: 24 },
    { number: 7, family: "eyepiece", name: "Eyepiece", rides: "eyepieceBody", at: [X_EYEPIECE + 9, 0, AXIS_Z + 9] },
  ];


  // The camera the walkthrough uses.
  const HOME = { azimuth: 58, elevation: 30 };
  const TILT_RANGE = [14, 62];

  // Points that must stay inside the picture.
  //   apart: 0 when the instrument is together, 1 when it is fully taken apart
  // Taken apart, the lamp housing rises and the eyepiece slides along the rail,
  // so the picture needs more room at the top and at the eyepiece end.
  function keyPoints(apart) {
    const top = 92 + (150 - 92) * apart;
    const end = 134 + (166 - 134) * apart;
    return [
      ...k.boxCorners(PLATE, -PLATE_H - FOOT_H, 0),
      [X_LAMP - 20, -18, top],
      [X_LAMP - 20, 18, top],
      [X_LAMP + 20, -18, top],
      [X_LAMP + 20, 18, top],
      [X_ANALYSER, -27, AXIS_Z + 27],
      [X_ANALYSER, 27, AXIS_Z + 27],
      [end, 0, AXIS_Z + 12],
    ];
  }

  // The camera for a given angle: the bench is fitted to the picture at every
  // angle, so it is always as large as it can be. The extra room at the top
  // is for the numbered pins.
  function projectionFor(azimuth, elevation, apart) {
    return k.fitProjection(keyPoints(apart), WIDTH, HEIGHT, { pad: 22, headroom: 26, azimuth: azimuth, elevation: elevation });
  }

  function baseProjection() {
    return projectionFor(HOME.azimuth, HOME.elevation, 0);
  }

  function build(P) {
    // Which way the viewer is looking from decides which faces show and
    // which end of the bench is painted first.
    const viewer = k.towardViewer(P);
    const FRONT = viewer[0] >= 0; // the eyepiece end is nearer than the lamp end
    let SIDE = 1; // +1 when the +y side of the bench faces the viewer
    if (viewer[1] < 0) {
      SIDE = -1;
    }
    let FACE = -1; // sign of the end face of a holder that the viewer can see
    if (FRONT) {
      FACE = 1;
    }

    const AXIS = G.frameAlong([0, 0, AXIS_Z], [1, 0, 0]);

    const at = (point) => k.iso(point, P);
    const S = (paths, style) => k.solidSvg(paths, style);
    const L = (d, style) => k.lineSvg(d, style);
    const D = (points, style) => k.dotsSvg(points, style);

    function fix(value) {
      return (Math.round(value * 10) / 10).toString();
    }

    // A closed path through world points.
    function loop(points) {
      const parts = points.map((point, index) => {
        const spot = at(point);
        let letter = "L";
        if (index === 0) {
          letter = "M";
        }
        return letter + fix(spot[0]) + " " + fix(spot[1]);
      });
      return parts.join("") + "Z";
    }

    // A circle of radius r around the optical axis at position x.
    function circleAt(x, r) {
      const points = [];
      for (let index = 0; index < 48; index++) {
        const angle = (index / 48) * Math.PI * 2;
        points.push([x, r * Math.cos(angle), AXIS_Z + r * Math.sin(angle)]);
      }
      return loop(points);
    }

    // A group the page can slide: id names it, family is used to dim or highlight it.
    function part(id, family, markup) {
      return `<g data-move="${id}" data-family="${family}">${markup}</g>`;
    }

    // A carriage on the rail with a clamp screw and a post up to a holder.
    function carriage(x, halfWidth, postTop) {
      const out = [];
      out.push(S(k.slabOf({ x: x - halfWidth, y: -13, w: halfWidth * 2, d: 26, r: 1.5 }, RAIL_H, CARRIAGE_TOP - RAIL_H, P, 4, 0.5), { tone: "mid" }));
      const screw = G.frameAlong([x, 13 * SIDE, RAIL_H + 2.5], [0, SIDE, 0]);
      out.push(S(G.disc(0, 3, 2.3, screw, P), { tone: "mid" }));
      out.push(L(G.ribsOf(screw, 0, 3, 2.3, 14, P), { tone: "lo" }));
      if (postTop > CARRIAGE_TOP) {
        out.push(S(k.cylinder(x, 0, 4.2, CARRIAGE_TOP, 2.5, P, 24, 0.3), { tone: "mid" }));
        out.push(S(k.cylinder(x, 0, 2.6, CARRIAGE_TOP + 2.5, postTop - CARRIAGE_TOP - 2.5, P, 24), { tone: "mid", crease: "none" }));
      }
      return out.join("");
    }

    // ---------- the bench ----------

    function bench() {
      const out = [`<path class="iso-halo" d="${k.haloOf(PLATE, -PLATE_H - FOOT_H, PLATE_H, P)}"/>`];
      const feet = [...k.corners(PLATE, 16)].sort((a, b) => k.depthOf([a[0], a[1], 0], P) - k.depthOf([b[0], b[1], 0], P));
      for (const [x, y] of feet) {
        out.push(S(k.cylinder(x, y, 6.5, -PLATE_H - FOOT_H, 1.4, P, 24), { tone: "lo" }));
        out.push(S(k.cylinder(x, y, 5, -PLATE_H - FOOT_H + 1.4, FOOT_H - 1.4, P, 24), { tone: "mid" }));
      }
      out.push(S(k.slabOf(PLATE, -PLATE_H, PLATE_H, P, 6, 1.2), { tone: "mid" }));
      out.push(L(k.planOutline(k.insetPlan(PLATE, 4), 0, P), { tone: "lo" }));
      const screws = k.corners(PLATE, 9);
      out.push(L(screws.map(([x, y]) => k.ring(x, y, 2, 0, P, 14)).join(""), { tone: "lo" }));
      out.push(D(screws.map(([x, y]) => at([x, y, 0])), { size: 0.5 }));
      // The rail, with a ruler strip beside it.
      out.push(S(k.slabOf(RAIL, 0, RAIL_H, P, 3, 0.6), { tone: "hi", crease: "lo" }));
      out.push(L(k.lineOnTop([RAIL.x, 0], [RAIL.x + RAIL.w, 0], RAIL_H, P), { tone: "faint" }));
      const strip = { x: -160, y: 20, w: 310, d: 7, r: 1 };
      out.push(S(k.slabOf(strip, 0, 0.6, P, 3), { tone: "lo", crease: "none" }));
      const ticks = k.topTicks(strip.x + 5, strip.x + strip.w - 5, 5, 5, strip.y + 0.8, 0.6, [2, 3.8], P);
      out.push(L(ticks.minor, { tone: "lo" }), L(ticks.major, { tone: "mid" }));
      out.push(D([at([strip.x + 2, strip.y + 3.5, 0.6]), at([strip.x + strip.w - 2, strip.y + 3.5, 0.6])], { size: 0.4 }));
      return out.join("");
    }

    // ---------- 1: the sodium lamp ----------

    function lampBase() {
      const out = [];
      out.push(carriage(X_LAMP, 20, 0));
      out.push(S(k.slabOf({ x: X_LAMP - 18, y: -16, w: 36, d: 32, r: 2 }, CARRIAGE_TOP, 6, P, 4, 0.6), { tone: "mid" }));
      out.push(D(k.corners({ x: X_LAMP - 18, y: -16, w: 36, d: 32, r: 2 }, 3.5).map(([x, y]) => at([x, y, 16])), { size: 0.45 }));
      // The lamp holder and the sodium discharge tube standing in it.
      out.push(S(k.cylinder(X_LAMP, 0, 7, 16, 9, P, 32, 0.5), { tone: "mid" }));
      out.push(L(k.sideArc(X_LAMP, 0, 7, 20, P, 24), { tone: "lo" }));
      out.push(S(k.cylinder(X_LAMP, 0, 5.2, 25, 44, P, 28, 2.4), { tone: "hi", className: "pm-bulb" }));
      out.push(L(k.sideArc(X_LAMP, 0, 5.2, 34, P, 20) + k.sideArc(X_LAMP, 0, 5.2, 60, P, 20), { tone: "lo" }));
      return out.join("");
    }

    function lampHousing() {
      const out = [];
      const box = { x: X_LAMP - 20, y: -18, w: 40, d: 36, r: 3 };
      out.push(S(k.slabOf(box, 16, 68, P, 6, 1.2), { tone: "mid" }));
      out.push(L(k.sideSeam(box, 20, P, 6), { tone: "faint" }));
      // Cooling slots on the side, each a closed slot.
      let slots = "";
      for (const z of [62, 67, 72, 77]) {
        slots += loop([[X_LAMP - 13, 18 * SIDE, z], [X_LAMP + 13, 18 * SIDE, z], [X_LAMP + 13, 18 * SIDE, z + 1.6], [X_LAMP - 13, 18 * SIDE, z + 1.6]]);
      }
      out.push(L(slots, { tone: "lo" }));
      // The exit window on the end face, on the optical axis.
      if (FRONT) {
        out.push(L(circleAt(X_LAMP + 20, 9.5), { tone: "mid" }));
        out.push(`<path class="pm-window" d="${circleAt(X_LAMP + 20, 7)}"/>`);
      }
      // A raised cap that lets the heat out.
      const cap = k.insetPlan(box, 5);
      out.push(S(k.slabOf(cap, 84, 3, P, 4, 0.5), { tone: "mid" }));
      out.push(D(k.corners(cap, 3).map(([x, y]) => at([x, y, 87])), { size: 0.4 }));
      return out.join("");
    }

    // ---------- 2: the lens ----------

    function lensHolder() {
      const out = [];
      out.push(carriage(X_LENS, 8, AXIS_Z - 14));
      out.push(S(G.ringBand(X_LENS - 2.5, X_LENS + 2.5, 10, 14.5, AXIS, P), { tone: "mid" }));
      out.push(L(G.circleOf(AXIS, X_LENS + 2.5 * FACE, 12.2, P), { tone: "faint" }));
      return out.join("");
    }

    function lens() {
      const out = [];
      out.push(S(G.solidOf([[X_LENS + 1, 0], [X_LENS + 1, 10], [X_LENS + 3, 10], [X_LENS + 4.6, 5, 1], [X_LENS + 5, 0]], AXIS, P), { tone: "hi", className: "pm-glass" }));
      return out.join("");
    }

    // ---------- 3: the polariser ----------

    function polariserHolder() {
      const out = [];
      out.push(carriage(X_POLARISER, 8, AXIS_Z - 18));
      out.push(S(G.ringBand(X_POLARISER - 3, X_POLARISER + 3, 13, 18.5, AXIS, P), { tone: "mid" }));
      out.push(L(G.circleOf(AXIS, X_POLARISER + 3 * FACE, 16, P), { tone: "faint" }));
      out.push(D([0, 1, 2, 3].map((index) => at(G.pointOf(AXIS, X_POLARISER + 3 * FACE, 16, index * Math.PI / 2 + Math.PI / 4))), { size: 0.4 }));
      return out.join("");
    }

    function polariserFilter() {
      const out = [];
      out.push(S(G.disc(X_POLARISER + 3, X_POLARISER + 4.5, 13, AXIS, P), { tone: "hi", className: "pm-filter" }));
      // Fine lines show the direction the filter lets light oscillate in: vertical.
      // The grain is drawn on whichever face of the filter is towards the viewer.
      let grainFace = X_POLARISER + 3;
      if (FRONT) {
        grainFace = X_POLARISER + 4.5;
      }
      let lines = "";
      for (const y of [-9, -6, -3, 0, 3, 6, 9]) {
        const reach = Math.sqrt(13 * 13 - y * y) - 0.8;
        const from = at([grainFace, y, AXIS_Z - reach]);
        const to = at([grainFace, y, AXIS_Z + reach]);
        lines += "M" + fix(from[0]) + " " + fix(from[1]) + "L" + fix(to[0]) + " " + fix(to[1]);
      }
      out.push(`<path class="pm-grain" d="${lines}"/>`);
      return out.join("");
    }

    function polariserRing() {
      const out = [];
      out.push(S(G.ringBand(X_POLARISER + 4.5, X_POLARISER + 6.5, 11, 14.5, AXIS, P), { tone: "mid" }));
      if (FRONT) {
        out.push(D([0, 1, 2].map((index) => at(G.pointOf(AXIS, X_POLARISER + 6.5, 12.8, index * Math.PI * 2 / 3 + 0.5))), { size: 0.4 }));
      }
      return out.join("");
    }

    // ---------- 4: the sample tube ----------

    function trough() {
      const out = [];
      out.push(S(k.slabOf({ x: -40, y: -13, w: 80, d: 26, r: 1.5 }, RAIL_H, CARRIAGE_TOP - RAIL_H, P, 4, 0.5), { tone: "mid" }));
      for (const x of [-30, 30]) {
        const screw = G.frameAlong([x, 13 * SIDE, RAIL_H + 2.5], [0, SIDE, 0]);
        out.push(S(G.disc(0, 3, 2.3, screw, P), { tone: "mid" }));
        out.push(L(G.ribsOf(screw, 0, 3, 2.3, 14, P), { tone: "lo" }));
      }
      // Two V-blocks that the tube rests in.
      // The far V-block is painted first.
      let blockXs = [-24, 20];
      if (!FRONT) {
        blockXs = [20, -24];
      }
      for (const x of blockXs) {
        const block = { x: x, y: -11, w: 5, d: 22, r: 0.8 };
        out.push(S(k.slabOf(block, CARRIAGE_TOP, AXIS_Z - 6 - CARRIAGE_TOP, P, 3, 0.5), { tone: "mid" }));
        out.push(L(k.sideSeam(block, CARRIAGE_TOP + 4, P, 3), { tone: "faint" }));
      }
      return out.join("");
    }

    function tubeCap(x0, x1) {
      const out = [];
      out.push(S(G.disc(x0, x1, 10.5, AXIS, P), { tone: "mid" }));
      out.push(L(G.ribsOf(AXIS, x0, x1, 10.5, 40, P), { tone: "lo" }));
      // The glass window shows on the end of the cap that faces the viewer.
      let endFace = x0;
      if (FRONT) {
        endFace = x1;
      }
      out.push(L(G.circleOf(AXIS, endFace, 6.5, P), { tone: "mid" }));
      out.push(`<path class="pm-glasswindow" d="${circleAt(endFace, 6.5)}"/>`);
      return out.join("");
    }

    function tubeGlass() {
      const out = [];
      const glass = G.outlineOf([[X_TUBE_START, 0], [X_TUBE_START, 8], [X_TUBE_END, 8], [X_TUBE_END, 0]], AXIS, P);
      out.push(`<path class="pm-tube" d="${glass.fill}"/>`);
      out.push(`<path class="pm-tube-edge" d="${glass.outline}"/>`);
      // A highlight along the top of the glass, and the liquid's level marks.
      const shineFrom = at([X_TUBE_START + 3, 3 * SIDE, AXIS_Z + 7.2]);
      const shineTo = at([X_TUBE_END - 3, 3 * SIDE, AXIS_Z + 7.2]);
      out.push(`<path class="pm-shine" d="M${fix(shineFrom[0])} ${fix(shineFrom[1])}L${fix(shineTo[0])} ${fix(shineTo[1])}"/>`);
      return out.join("");
    }

    // ---------- 5 and 6: the analyser and its scale ----------

    function analyserHolder() {
      const out = [];
      out.push(carriage(X_ANALYSER, 9, AXIS_Z - 26));
      // The fixed scale plate: a tick every 5 degrees, longer every 30.
      out.push(S(G.ringBand(X_ANALYSER - 3, X_ANALYSER + 3, 13, 27, AXIS, P), { tone: "mid" }));
      // The scale is engraved on the side that faces the eyepiece.
      if (FRONT) {
        out.push(L(G.circleOf(AXIS, X_ANALYSER + 3, 20.5, P), { tone: "lo" }));
        out.push(L(G.spokesOf(AXIS, X_ANALYSER + 3, 23.6, 27, 72, P), { tone: "lo" }));
        out.push(L(G.spokesOf(AXIS, X_ANALYSER + 3, 20.5, 27, 12, P), { tone: "mid" }));
        // The zero of the scale is at the top.
        out.push(D([at(G.pointOf(AXIS, X_ANALYSER + 3, 18.9, Math.PI / 2))], { size: 0.55, tone: "hi" }));
      }
      return out.join("");
    }

    function analyserFilter() {
      const out = [];
      out.push(S(G.disc(X_ANALYSER + 3, X_ANALYSER + 4.5, 13, AXIS, P), { tone: "hi", className: "pm-filter" }));
      out.push(`<g data-live="grain"></g>`);
      return out.join("");
    }

    function analyserCollar() {
      const out = [];
      out.push(S(G.ringBand(X_ANALYSER + 4.5, X_ANALYSER + 9.5, 11, 18.5, AXIS, P), { tone: "hi", crease: "lo" }));
      out.push(L(G.ribsOf(AXIS, X_ANALYSER + 4.5, X_ANALYSER + 9.5, 18.5, 56, P), { tone: "lo" }));
      if (FRONT) {
        out.push(L(G.circleOf(AXIS, X_ANALYSER + 9.5, 13.5, P), { tone: "faint" }));
      }
      out.push(`<g data-live="pointer"></g>`);
      return out.join("");
    }

    // ---------- 7: the eyepiece ----------

    function eyepieceBody() {
      const out = [];
      out.push(carriage(X_EYEPIECE, 8, AXIS_Z - 12.5));
      out.push(S(G.ringBand(X_EYEPIECE - 3, X_EYEPIECE + 3, 9, 12.5, AXIS, P), { tone: "mid" }));
      out.push(S(G.solidOf([[X_EYEPIECE - 9, 0], [X_EYEPIECE - 9, 9], [X_EYEPIECE + 6, 9], [X_EYEPIECE + 6, 7], [X_EYEPIECE + 13, 7], [X_EYEPIECE + 13, 0]], AXIS, P), { tone: "mid" }));
      out.push(L(G.ribsOf(AXIS, X_EYEPIECE + 6, X_EYEPIECE + 13, 7, 30, P), { tone: "lo" }));
      if (FRONT) {
        out.push(L(G.circleOf(AXIS, X_EYEPIECE + 13, 5.2, P), { tone: "lo" }));
      }
      return out.join("");
    }

    function eyepieceLens() {
      return S(G.solidOf([[X_EYEPIECE + 13, 0], [X_EYEPIECE + 13, 5.2], [X_EYEPIECE + 14, 5.2], [X_EYEPIECE + 15, 2.6, 1], [X_EYEPIECE + 15.3, 0]], AXIS, P), { tone: "hi", className: "pm-glass" });
    }

    function eyepieceCup() {
      const out = [];
      out.push(S(G.ringBand(X_EYEPIECE + 14, X_EYEPIECE + 19, 5, 9.5, AXIS, P), { tone: "lo" }));
      if (FRONT) {
        out.push(L(G.circleOf(AXIS, X_EYEPIECE + 19, 7.2, P), { tone: "faint" }));
      }
      return out.join("");
    }


    // ---------- the figure, painted from the lamp end to the eyepiece end ----------

    const beam = (index) => `<g data-beam="${index}" class="pm-beam"></g>`;

    const middle = [
      // The housing always goes on after the lamp it covers, so the two stay as one entry.
      part("lampBase", "lamp", lampBase()) + part("lampHousing", "lamp", lampHousing()),
      beam(0),
      part("lensHolder", "lens", lensHolder()),
      part("lens", "lens", lens()),
      beam(1),
      part("polariserHolder", "polariser", polariserHolder()),
      part("polariserFilter", "polariser", polariserFilter()),
      part("polariserRing", "polariser", polariserRing()),
      beam(2),
      part("trough", "tube", trough()),
      part("capLeft", "tube", tubeCap(X_TUBE_START - 4, X_TUBE_START + 2)),
      part("beamTube", "tube", beam(3)),
      part("glass", "tube", tubeGlass()),
      part("capRight", "tube", tubeCap(X_TUBE_END - 2, X_TUBE_END + 4)),
      beam(4),
      part("analyserHolder", "scale", analyserHolder()),
      part("analyserFilter", "analyser", analyserFilter()),
      part("analyserCollar", "analyser", analyserCollar()),
      beam(5),
      part("eyepieceBody", "eyepiece", eyepieceBody()),
      part("eyepieceLens", "eyepiece", eyepieceLens()),
      part("eyepieceCup", "eyepiece", eyepieceCup()),
    ];

    // From the lamp end, the far parts are the eyepiece ones, so paint in reverse.
    if (!FRONT) {
      middle.reverse();
    }
    return [bench(), ...middle, `<g data-live="pins" class="pm-pins"></g>`];
  }

  return {
    build: build,
    baseProjection: baseProjection,
    projectionFor: projectionFor,
    WIDTH: WIDTH,
    HEIGHT: HEIGHT,
    AXIS_Z: AXIS_Z,
    HOME: HOME,
    TILT_RANGE: TILT_RANGE,
    MOVES: MOVES,
    PINS: PINS,
    X: { lamp: X_LAMP, lens: X_LENS, polariser: X_POLARISER, tubeStart: X_TUBE_START, tubeEnd: X_TUBE_END, analyser: X_ANALYSER, eyepiece: X_EYEPIECE },
  };
}
