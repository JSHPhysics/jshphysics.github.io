/*
 * figures.js — one technical drawing per topic, as inline SVG.
 *
 * Each figure is drawn in a 320 × 200 box in the style of a blueprint or a
 * graph-paper sketch: thin strokes in currentColor, dashed construction
 * lines, dimension arrows, and a small number of accent strokes. Parts that
 * move carry classes the stylesheet animates (.draw, .swing, .orbit, .travel,
 * .pulse). Everything is pure markup, so the same figure can sit on a card
 * and in a page header and be morphed between them.
 *
 * figures.render(topicId) → SVG string (empty string for an unknown id)
 */
(function (root, factory) {
  if (typeof module === "object" && module.exports) {
    module.exports = factory();
  } else {
    root.figures = factory();
  }
}(typeof self !== "undefined" ? self : this, function () {

  /* ------------------------------------------------------------------
     Drawing helpers
     ------------------------------------------------------------------ */

  // A line with an arrowhead at the end
  function arrow(x1, y1, x2, y2, cls) {
    const angle = Math.atan2(y2 - y1, x2 - x1);
    const size = 7;
    const leftX = x2 - size * Math.cos(angle - 0.45);
    const leftY = y2 - size * Math.sin(angle - 0.45);
    const rightX = x2 - size * Math.cos(angle + 0.45);
    const rightY = y2 - size * Math.sin(angle + 0.45);
    const className = cls ? " class=\"" + cls + "\"" : "";
    return "<line" + className + " x1=\"" + x1 + "\" y1=\"" + y1 + "\" x2=\"" + x2 + "\" y2=\"" + y2 + "\"/>" +
      "<polyline" + className + " points=\"" + leftX.toFixed(1) + "," + leftY.toFixed(1) + " " + x2 + "," + y2 + " " +
      rightX.toFixed(1) + "," + rightY.toFixed(1) + "\"/>";
  }

  // A dimension line between two points with end ticks and a label
  function dimension(x1, y1, x2, y2, label, offset) {
    const dx = x2 - x1;
    const dy = y2 - y1;
    const length = Math.hypot(dx, dy) || 1;
    const nx = -dy / length;
    const ny = dx / length;
    const shift = offset || 0;
    const ax = x1 + nx * shift;
    const ay = y1 + ny * shift;
    const bx = x2 + nx * shift;
    const by = y2 + ny * shift;
    const tick = 4;
    const midX = (ax + bx) / 2 + nx * 10;
    const midY = (ay + by) / 2 + ny * 10;
    return "<g class=\"dim\">" +
      "<line x1=\"" + ax + "\" y1=\"" + ay + "\" x2=\"" + bx + "\" y2=\"" + by + "\"/>" +
      "<line x1=\"" + (ax - nx * tick) + "\" y1=\"" + (ay - ny * tick) + "\" x2=\"" + (ax + nx * tick) + "\" y2=\"" + (ay + ny * tick) + "\"/>" +
      "<line x1=\"" + (bx - nx * tick) + "\" y1=\"" + (by - ny * tick) + "\" x2=\"" + (bx + nx * tick) + "\" y2=\"" + (by + ny * tick) + "\"/>" +
      "<text x=\"" + midX.toFixed(1) + "\" y=\"" + midY.toFixed(1) + "\" text-anchor=\"middle\">" + label + "</text>" +
      "</g>";
  }

  // Dashed construction line
  function dash(x1, y1, x2, y2) {
    return "<line class=\"cons\" x1=\"" + x1 + "\" y1=\"" + y1 + "\" x2=\"" + x2 + "\" y2=\"" + y2 + "\"/>";
  }

  function text(x, y, label, anchor) {
    return "<text x=\"" + x + "\" y=\"" + y + "\" text-anchor=\"" + (anchor || "start") + "\">" + label + "</text>";
  }

  // Points along a sine wave as an SVG path
  function sinePath(x0, y0, width, amplitude, cycles, steps) {
    let path = "";
    const count = steps || 80;
    for (let index = 0; index <= count; index += 1) {
      const x = x0 + (width * index) / count;
      const y = y0 - amplitude * Math.sin((2 * Math.PI * cycles * index) / count);
      path += (index === 0 ? "M" : "L") + x.toFixed(1) + "," + y.toFixed(1);
    }
    return path;
  }

  // A resistor between two points (horizontal): the IEC / BS 3939 rectangle
  function resistor(x, y, width) {
    const height = 14;
    return "<rect x=\"" + x + "\" y=\"" + (y - height / 2) + "\" width=\"" + width + "\" height=\"" + height + "\"/>";
  }

  // A coil spring between (x, y1) and (x, y2), vertical
  function spring(x, y1, y2, coils) {
    const n = coils || 8;
    const step = (y2 - y1) / n;
    let path = "M" + x + "," + y1;
    for (let index = 0; index < n; index += 1) {
      const y = y1 + step * (index + 0.5);
      path += "L" + (x + (index % 2 === 0 ? 10 : -10)) + "," + y.toFixed(1);
    }
    path += "L" + x + "," + y2;
    return path;
  }

  function wrap(inner, cls) {
    return "<svg class=\"fig " + (cls || "") + "\" viewBox=\"0 0 320 200\" xmlns=\"http://www.w3.org/2000/svg\" aria-hidden=\"true\" focusable=\"false\">" +
      inner + "</svg>";
  }

  /* ------------------------------------------------------------------
     The figures
     ------------------------------------------------------------------ */

  const drawings = {

    // A vernier-style scale with a bracketed reading and its uncertainty
    "measurements": function () {
      let ticks = "";
      for (let index = 0; index <= 24; index += 1) {
        const x = 30 + index * 11;
        const height = index % 5 === 0 ? 18 : (index % 5 === 0 ? 12 : 8);
        ticks += "<line x1=\"" + x + "\" y1=\"118\" x2=\"" + x + "\" y2=\"" + (118 - height) + "\"/>";
      }
      let labels = "";
      for (let index = 0; index <= 24; index += 5) {
        labels += text(30 + index * 11, 132, String(index), "middle");
      }
      return wrap(
        "<g class=\"draw\">" +
        "<line x1=\"20\" y1=\"118\" x2=\"300\" y2=\"118\"/>" + ticks +
        "</g>" +
        "<g class=\"lbl\">" + labels + "</g>" +
        // The object being measured
        "<rect class=\"acc draw\" x=\"52\" y=\"62\" width=\"123\" height=\"30\" rx=\"2\"/>" +
        dimension(52, 50, 175, 50, "11.2 ± 0.1", 0) +
        // Reading pointer
        dash(175, 62, 175, 118) +
        "<g class=\"pulse\">" + arrow(175, 160, 175, 124, "acc") + "</g>"
      );
    },

    // A projectile arc with velocity components and range
    "kinematics": function () {
      // Parabola from (40,160) peaking at (160, 60) landing at (280,160)
      const path = "M40,160 Q160,-40 280,160";
      return wrap(
        "<line x1=\"20\" y1=\"160\" x2=\"300\" y2=\"160\"/>" +
        "<path class=\"draw arc\" d=\"" + path + "\"/>" +

        // Initial velocity and its components
        arrow(40, 160, 92, 108, "acc") +
        arrow(40, 160, 92, 160, "cons") +
        arrow(40, 160, 40, 108, "cons") +
        text(96, 104, "u") +
        text(96, 174, "u cos θ") +
        text(16, 104, "u sin θ", "start") +
        // Angle arc
        "<path class=\"cons\" d=\"M66,160 A26,26 0 0 0 58,142\"/>" +
        text(70, 150, "θ") +
        dimension(40, 182, 280, 182, "R", 0) +
        dimension(160, 160, 160, 60, "H", 0) +
        // Travelling dot
        "<circle class=\"travel acc\" r=\"4\" style=\"offset-path: path('" + path + "')\"/>"
      );
    },

    // A block on an incline with weight resolved into components
    "forces": function () {
      // Incline from (30,170) to (270,70)
      const angle = Math.atan2(100, 240);
      const bx = 150;
      const by = 170 - (bx - 30) * Math.tan(angle);
      const cos = Math.cos(angle);
      const sin = Math.sin(angle);
      // Block corners (a square sitting on the slope)
      const size = 34;
      const ux = cos;
      const uy = -sin;
      const vx = sin;
      const vy = cos;
      const p1x = bx - (size / 2) * ux;
      const p1y = by - (size / 2) * uy;
      const p2x = bx + (size / 2) * ux;
      const p2y = by + (size / 2) * uy;
      const p3x = p2x - size * vx;
      const p3y = p2y - size * vy;
      const p4x = p1x - size * vx;
      const p4y = p1y - size * vy;
      const cx = (p1x + p3x) / 2;
      const cy = (p1y + p3y) / 2;
      return wrap(
        "<polygon class=\"draw\" points=\"30,170 270,170 270,70\"/>" +
        "<polygon class=\"acc draw\" points=\"" + [p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y].map(function (n) { return n.toFixed(1); }).join(",") + "\"/>" +
        // Weight straight down
        arrow(cx, cy, cx, cy + 70, "") +
        text(cx + 6, cy + 74, "W") +
        // Components: along and perpendicular to slope
        arrow(cx, cy, cx - 70 * sin * cos, cy + 70 * sin * sin, "cons") +
        arrow(cx, cy, cx + 70 * sin * cos, cy + 70 * cos * cos, "cons") +
        text(cx - 60, cy + 14, "W sin θ", "end") +
        text(cx + 8, cy + 52, "W cos θ") +
        // Normal reaction
        arrow(cx, cy, cx - 55 * sin, cy - 55 * cos, "acc") +
        text(cx - 55 * sin - 4, cy - 55 * cos - 6, "R", "end") +
        // Slope angle at the bottom-right vertex (270,170): arc from the base
        // round to the hypotenuse, label on the bisector just inside the arc
        "<path class=\"cons\" d=\"M234,170 A36,36 0 0 1 " + (270 - 36 * cos).toFixed(1) + "," + (170 - 36 * sin).toFixed(1) + "\"/>" +
        text(221, 164, "θ", "middle")
      );
    },

    // Two trolleys about to collide, with momentum arrows
    "momentum-energy": function () {
      return wrap(
        "<line x1=\"20\" y1=\"140\" x2=\"300\" y2=\"140\"/>" +
        // Trolley 1 (moving)
        "<g class=\"slide-right\">" +
        "<rect class=\"acc draw\" x=\"50\" y=\"100\" width=\"60\" height=\"34\" rx=\"3\"/>" +
        "<circle cx=\"64\" cy=\"137\" r=\"5\"/><circle cx=\"96\" cy=\"137\" r=\"5\"/>" +
        arrow(110, 117, 160, 117, "acc") +
        text(80, 92, "m₁", "middle") +
        text(135, 110, "u₁", "middle") +
        "</g>" +
        // Trolley 2 (at rest)
        "<rect class=\"draw\" x=\"200\" y=\"100\" width=\"60\" height=\"34\" rx=\"3\"/>" +
        "<circle cx=\"214\" cy=\"137\" r=\"5\"/><circle cx=\"246\" cy=\"137\" r=\"5\"/>" +
        text(230, 92, "m₂", "middle") +
        // Energy bar underneath: KE before / after
        "<g class=\"lbl\">" +
        text(50, 176, "p = m₁u₁ + m₂u₂") +
        "</g>" +
        dash(200, 60, 200, 100) +
        dash(50, 60, 50, 100) +
        dimension(50, 60, 200, 60, "s", 0)
      );
    },

    // A spring under load with extension dimensioned
    "materials": function () {
      return wrap(
        // Ceiling
        "<line x1=\"120\" y1=\"20\" x2=\"200\" y2=\"20\"/>" +
        "<g class=\"hatch\">" +
        "<line x1=\"125\" y1=\"20\" x2=\"118\" y2=\"12\"/><line x1=\"140\" y1=\"20\" x2=\"133\" y2=\"12\"/>" +
        "<line x1=\"155\" y1=\"20\" x2=\"148\" y2=\"12\"/><line x1=\"170\" y1=\"20\" x2=\"163\" y2=\"12\"/>" +
        "<line x1=\"185\" y1=\"20\" x2=\"178\" y2=\"12\"/><line x1=\"200\" y1=\"20\" x2=\"193\" y2=\"12\"/>" +
        "</g>" +
        // Unstretched spring (construction)
        "<path class=\"cons\" d=\"" + spring(90, 20, 100, 8) + "\"/>" +
        dash(70, 100, 110, 100) +
        // Stretched spring (animated between two lengths)
        "<g class=\"stretch\">" +
        "<path class=\"acc\" d=\"" + spring(160, 20, 130, 8) + "\"/>" +
        "<rect class=\"acc draw\" x=\"142\" y=\"130\" width=\"36\" height=\"26\" rx=\"2\"/>" +
        arrow(160, 156, 160, 186, "") +
        text(166, 186, "F") +
        "</g>" +
        // Natural length level (fixed) and the moving spring-end level
        dash(160, 100, 230, 100) +
        "<g class=\"shift\">" + dash(160, 130, 230, 130) + "</g>" +
        // Δx: a dimension whose lower end tracks the spring (scaled about y = 100),
        // with the label moved to its midpoint separately so the glyph is not squashed
        "<g class=\"dim dx-line\" style=\"transform-origin: 230px 100px\">" +
        "<line x1=\"230\" y1=\"100\" x2=\"230\" y2=\"130\"/>" +
        "<line x1=\"226\" y1=\"100\" x2=\"234\" y2=\"100\"/>" +
        "<line x1=\"226\" y1=\"130\" x2=\"234\" y2=\"130\"/>" +
        "</g>" +
        "<g class=\"dim dx-label\"><text x=\"242\" y=\"119\">Δx</text></g>" +
        dimension(60, 20, 60, 100, "L", 0)
      );
    },

    // A travelling wave with wavelength and amplitude marked. The markers
    // sit inside the moving group, duplicated one wavelength back, so they
    // travel with the crests and the wrap-around is seamless.
    "waves": function () {
      const wave = sinePath(0, 100, 320, 36, 2.5, 120);
      // Crests at x = 32, 160, 288 (period 128); troughs at 96, 224
      // One wavelength's worth of markers; repeated every 128 px so the
      // pattern is continuous across the box however far the group has moved
      function markers(shift) {
        return "<g transform=\"translate(" + shift + ",0)\">" +
          dash(32, 44, 32, 64) + dash(160, 44, 160, 64) +
          dimension(32, 44, 160, 44, "λ", 0) +
          dimension(224, 100, 224, 136, "A", 0) +
          "</g>";
      }
      return wrap(
        "<line class=\"cons\" x1=\"20\" y1=\"100\" x2=\"300\" y2=\"100\"/>" +
        "<g class=\"wave\">" +
        "<path class=\"acc draw\" d=\"" + wave + "\"/>" +
        "<path class=\"acc\" transform=\"translate(-128,0)\" d=\"" + wave + "\"/>" +
        markers(-256) + markers(-128) + markers(0) + markers(128) +
        "</g>" +
        text(300, 92, "x", "end")
      );
    },

    // Energy levels with a downward transition emitting a photon
    "quantum": function () {
      const levels = [160, 118, 92, 76, 66];
      let lines = "";
      const names = ["n = 1", "n = 2", "n = 3", "n = 4", "∞"];
      levels.forEach(function (y, index) {
        lines += "<line x1=\"60\" y1=\"" + y + "\" x2=\"200\" y2=\"" + y + "\"/>" + text(206, y + 4, names[index]);
      });
      return wrap(
        "<g class=\"draw\">" + lines + "</g>" +
        // Electron dropping from n=3 to n=2
        "<g class=\"drop\">" +
        "<circle class=\"acc\" cx=\"130\" cy=\"92\" r=\"4\"/>" +
        "</g>" +
        arrow(130, 92, 130, 120, "acc") +
        // Photon leaving
        "<g class=\"photon\">" +
        "<path class=\"acc\" d=\"" + sinePath(140, 106, 90, 5, 4, 60) + "\"/>" +
        arrow(230, 106, 250, 106, "acc") +
        "</g>" +
        text(260, 110, "hf") +
        dimension(44, 118, 44, 92, "ΔE", 0) +
        text(60, 186, "E = −13.6 eV / n²")
      );
    },

    // A series circuit with current markers moving round it
    "electricity": function () {
      const loop = "M60,50 L260,50 L260,150 L60,150 Z";
      return wrap(
        // Wires: gaps for the resistor (130–190 on top) and the ammeter (circle r = 12 at 160 on the bottom)
        "<path class=\"draw\" d=\"M60,50 L130,50 M190,50 L260,50 L260,150 L174,150 M146,150 L60,150\"/>" +
        // Cell on the left side
        "<line x1=\"60\" y1=\"50\" x2=\"60\" y2=\"88\"/><line x1=\"60\" y1=\"112\" x2=\"60\" y2=\"150\"/>" +
        "<line x1=\"46\" y1=\"88\" x2=\"74\" y2=\"88\"/><line x1=\"52\" y1=\"98\" x2=\"68\" y2=\"98\"/>" +
        "<line x1=\"46\" y1=\"104\" x2=\"74\" y2=\"104\"/><line x1=\"52\" y1=\"112\" x2=\"68\" y2=\"112\"/>" +
        text(28, 104, "ε, r") +
        // Resistor on top
        "<g class=\"acc\">" + resistor(130, 50, 60) + "</g>" +
        text(160, 74, "R", "middle") +
        // Ammeter at the bottom
        "<circle cx=\"160\" cy=\"150\" r=\"12\"/>" + text(160, 154, "A", "middle") +
        // Voltmeter across R
        "<path class=\"cons\" d=\"M130,50 L130,22 L190,22 L190,50\"/>" +
        "<circle class=\"cons-fill\" cx=\"160\" cy=\"22\" r=\"10\"/>" + text(160, 26, "V", "middle") +
        // Charge carriers
        "<circle class=\"travel acc\" r=\"3\" style=\"offset-path: path('" + loop + "'); animation-delay: 0s\"/>" +
        "<circle class=\"travel acc\" r=\"3\" style=\"offset-path: path('" + loop + "'); animation-delay: -1.3s\"/>" +
        "<circle class=\"travel acc\" r=\"3\" style=\"offset-path: path('" + loop + "'); animation-delay: -2.6s\"/>" +
        text(272, 104, "I")
      );
    },

    // A pendulum swinging through its arc
    "circular-shm": function () {
      return wrap(
        "<line x1=\"100\" y1=\"28\" x2=\"220\" y2=\"28\"/>" +
        "<g class=\"hatch\"><line x1=\"110\" y1=\"28\" x2=\"104\" y2=\"20\"/><line x1=\"130\" y1=\"28\" x2=\"124\" y2=\"20\"/>" +
        "<line x1=\"150\" y1=\"28\" x2=\"144\" y2=\"20\"/><line x1=\"170\" y1=\"28\" x2=\"164\" y2=\"20\"/>" +
        "<line x1=\"190\" y1=\"28\" x2=\"184\" y2=\"20\"/><line x1=\"210\" y1=\"28\" x2=\"204\" y2=\"20\"/></g>" +
        dash(160, 28, 160, 170) +
        // Arc of motion
        "<path class=\"cons\" d=\"M98,142 A130,130 0 0 0 222,142\"/>" +
        // Amplitude marks
        dimension(160, 176, 222, 176, "A", 0) +
        // Pendulum: string and bob rotate about the pivot
        "<g class=\"swing\" style=\"transform-origin: 160px 28px\">" +
        "<line class=\"acc\" x1=\"160\" y1=\"28\" x2=\"160\" y2=\"158\"/>" +
        "<circle class=\"acc fill\" cx=\"160\" cy=\"164\" r=\"9\"/>" +
        "</g>" +
        // Angle marker: a dashed arc from the vertical to the string. The
        // visible part of this circle is a dash whose length follows the
        // swing angle (see fig-theta-arc in figures.css)
        "<circle class=\"cons theta-arc\" cx=\"160\" cy=\"28\" r=\"42\" style=\"transform-origin: 160px 28px\"/>" +
        // θ sits at the middle of that arc: an arm rotated by half the
        // swing angle, with the glyph counter-rotated so it stays upright
        "<g class=\"theta-arm\" style=\"transform-origin: 160px 28px\">" +
        "<text class=\"theta-glyph\" x=\"160\" y=\"88\" text-anchor=\"middle\">θ</text>" +
        "</g>" +
        text(130, 100, "L", "end")
      );
    },

    // Gas particles in a box with a piston
    "thermal-gases": function () {
      const particles = [
        [80, 70, 3, 2], [130, 120, -2, 3], [190, 80, 2, -3], [110, 150, -3, -1],
        [220, 140, 1, 2], [160, 60, -2, -2], [90, 110, 2, 2], [200, 110, -3, 2],
        [150, 95, 3, 1], [240, 70, -1, 3],
      ];
      let dots = "";
      particles.forEach(function (particle, index) {
        dots += "<g class=\"jitter\" style=\"--dx: " + (particle[2] * 4) + "px; --dy: " + (particle[3] * 4) + "px; animation-delay: " + (-index * 0.37) + "s\">" +
          "<circle class=\"acc fill\" cx=\"" + particle[0] + "\" cy=\"" + particle[1] + "\" r=\"3.5\"/></g>";
      });
      return wrap(
        "<path class=\"draw\" d=\"M60,40 L60,170 L260,170 L260,40\"/>" +
        // Piston
        "<rect class=\"draw\" x=\"60\" y=\"40\" width=\"200\" height=\"10\"/>" +
        "<line x1=\"160\" y1=\"40\" x2=\"160\" y2=\"14\"/>" +
        arrow(160, 14, 160, 36, "acc") +
        text(170, 24, "p") +
        dots +
        dimension(276, 50, 276, 170, "V", 0) +
        text(60, 190, "pV = NkT")
      );
    },

    // A planet with a satellite in a circular orbit. The radius vector, the
    // satellite and its velocity vector rotate together; the labels are
    // counter-rotated so they stay upright.
    "gravitational-fields": function () {
      return wrap(
        "<circle class=\"draw\" cx=\"160\" cy=\"100\" r=\"28\"/>" +
        "<g class=\"hatch\"><path d=\"M143,82 Q160,96 177,82 M137,100 Q160,112 183,100 M143,118 Q160,106 177,118\"/></g>" +
        "<circle class=\"cons\" cx=\"160\" cy=\"100\" r=\"88\"/>" +
        text(160, 104, "M", "middle") +
        "<g class=\"orbit ccw\" style=\"transform-origin: 160px 100px\">" +
        arrow(160, 100, 243, 100, "") +
        "<g class=\"upright\"><text x=\"204\" y=\"94\" text-anchor=\"middle\">r</text></g>" +
        "<rect class=\"acc fill\" x=\"243\" y=\"95\" width=\"10\" height=\"10\"/>" +
        arrow(248, 100, 248, 58, "acc") +
        "<g class=\"upright\"><text class=\"acc\" x=\"258\" y=\"66\">v</text></g>" +
        "</g>" +
        text(40, 186, "F = GMm / r²")
      );
    },

    // Two charges with field lines between them
    "electric-fields-capacitors": function () {
      let lines = "";
      const curves = [-60, -30, 0, 30, 60];
      curves.forEach(function (bend) {
        lines += "<path class=\"draw\" d=\"M100,100 Q160," + (100 + bend * 1.6) + " 220,100\"/>";
        // Arrowhead at the midpoint
        const midY = 100 + bend * 0.8;
        lines += "<polyline points=\"156," + (midY - 4) + " 162," + midY + " 156," + (midY + 4) + "\"/>";
      });
      return wrap(
        lines +
        "<path class=\"cons draw\" d=\"M100,100 Q40,20 60,100 Q40,180 100,100\"/>" +
        "<path class=\"cons draw\" d=\"M220,100 Q280,20 260,100 Q280,180 220,100\"/>" +
        "<circle class=\"acc fill\" cx=\"100\" cy=\"100\" r=\"12\"/>" +
        "<circle class=\"acc fill\" cx=\"220\" cy=\"100\" r=\"12\"/>" +
        "<g class=\"on-fill\"><line x1=\"94\" y1=\"100\" x2=\"106\" y2=\"100\"/><line x1=\"100\" y1=\"94\" x2=\"100\" y2=\"106\"/>" +
        "<line x1=\"214\" y1=\"100\" x2=\"226\" y2=\"100\"/></g>" +
        dimension(100, 150, 220, 150, "r", 0) +
        text(90, 72, "+Q", "end") + text(232, 72, "−q") +
        text(40, 186, "F = Qq / 4πε₀r²")
      );
    },

    // A charged particle circling in a magnetic field out of the page
    "magnetic-fields-induction": function () {
      let dots = "";
      for (let row = 0; row < 4; row += 1) {
        for (let column = 0; column < 6; column += 1) {
          const x = 60 + column * 40;
          const y = 50 + row * 40;
          dots += "<circle class=\"bdot\" cx=\"" + x + "\" cy=\"" + y + "\" r=\"4\"/><circle class=\"fill\" cx=\"" + x + "\" cy=\"" + y + "\" r=\"1.2\"/>";
        }
      }
      return wrap(
        dots +
        "<circle class=\"cons\" cx=\"160\" cy=\"110\" r=\"56\"/>" +
        // Radius, particle, velocity (tangent) and force (to the centre) rotate as one
        "<g class=\"orbit ccw\" style=\"transform-origin: 160px 110px\">" +
        arrow(160, 110, 212, 110, "") +
        "<g class=\"upright\"><text x=\"186\" y=\"104\" text-anchor=\"middle\">r</text></g>" +
        "<circle class=\"acc fill\" cx=\"216\" cy=\"110\" r=\"5\"/>" +
        arrow(216, 110, 216, 70, "acc") +
        "<g class=\"upright\"><text class=\"acc\" x=\"222\" y=\"76\">v</text></g>" +
        arrow(216, 110, 180, 110, "acc") +
        "<g class=\"upright\"><text class=\"acc\" x=\"190\" y=\"124\">F</text></g>" +
        "</g>" +
        text(282, 54, "B", "end") +
        text(40, 186, "r = mv / BQ")
      );
    },

    // A decay curve with half-life steps
    "nuclear-particles": function () {
      let path = "";
      for (let index = 0; index <= 100; index += 1) {
        const x = 50 + index * 2.4;
        const y = 160 - 120 * Math.pow(0.5, index / 25);
        path += (index === 0 ? "M" : "L") + x.toFixed(1) + "," + y.toFixed(1);
      }
      return wrap(
        "<line x1=\"50\" y1=\"20\" x2=\"50\" y2=\"160\"/>" +
        arrow(50, 160, 300, 160, "") +
        "<path class=\"acc draw slow\" d=\"" + path + "\"/>" +
        dash(50, 100, 110, 100) + dash(110, 100, 110, 160) +
        dash(50, 130, 170, 130) + dash(170, 130, 170, 160) +
        dash(50, 145, 230, 145) + dash(230, 145, 230, 160) +
        text(44, 44, "N₀", "end") + text(44, 104, "N₀/2", "end") + text(44, 134, "N₀/4", "end") +
        text(110, 176, "t½", "middle") + text(170, 176, "2t½", "middle") + text(230, 176, "3t½", "middle") +
        text(300, 150, "t", "end") +
        text(190, 60, "N = N₀e^(−λt)")
      );
    },

    // Stellar parallax: the Earth's orbit, the Sun and a nearby star
    "astrophysics": function () {
      return wrap(
        // Distant stars
        "<g class=\"lbl\"><text x=\"40\" y=\"30\">✦</text><text x=\"280\" y=\"50\">✦</text><text x=\"230\" y=\"24\">✦</text><text x=\"60\" y=\"70\">✦</text></g>" +
        // Earth's orbit (seen edge on as an ellipse)
        "<ellipse class=\"cons\" cx=\"100\" cy=\"150\" rx=\"60\" ry=\"18\"/>" +
        "<circle class=\"acc fill\" cx=\"100\" cy=\"150\" r=\"7\"/>" +
        text(100, 178, "Sun", "middle") +
        // Earth at two positions
        "<circle class=\"fill\" cx=\"40\" cy=\"150\" r=\"4\"/>" +
        "<circle class=\"fill\" cx=\"160\" cy=\"150\" r=\"4\"/>" +
        // Nearby star
        "<g class=\"pulse\"><circle class=\"acc fill\" cx=\"250\" cy=\"60\" r=\"5\"/></g>" +
        // Sight lines
        "<line class=\"draw\" x1=\"40\" y1=\"150\" x2=\"250\" y2=\"60\"/>" +
        "<line class=\"draw\" x1=\"160\" y1=\"150\" x2=\"250\" y2=\"60\"/>" +
        dash(100, 150, 250, 60) +
        // Parallax angle
        "<path class=\"acc\" d=\"M222,72 A30,30 0 0 1 224,84\"/>" +
        text(214, 84, "p", "end") +
        dimension(40, 118, 100, 118, "1 AU", 0) +
        text(40, 196, "d = 1 / p")
      );
    },
  };

  function render(topicId) {
    const draw = drawings[topicId];
    if (!draw) {
      return "";
    }
    return draw();
  }

  return { render: render, ids: Object.keys(drawings) };
}));
