/*
 * graphs.js — exam-style graphs from a small declarative spec.
 *
 * A question may carry a "graph" object (see SCHEMA.md). This module turns
 * it into an SVG: a plot area with major and minor gridlines, numbered
 * axes, one or more plotted series, marked points, shaded regions and
 * free labels. Axis titles are returned separately so the app can typeset
 * them with KaTeX.
 *
 *   graphs.render(spec) → { svg, xLabel, yLabel }
 *   graphs.validate(spec) → [problem strings]  (used by the tests)
 */
(function (root, factory) {
  if (typeof module === "object" && module.exports) {
    module.exports = factory();
  } else {
    root.graphs = factory();
  }
}(typeof self !== "undefined" ? self : this, function () {

  // Plot geometry in SVG user units
  const WIDTH = 520;
  const HEIGHT = 340;
  const PAD_LEFT = 58;
  const PAD_RIGHT = 22;
  const PAD_TOP = 26;
  const PAD_BOTTOM = 44;

  function esc(text) {
    return String(text)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  // Format a tick value without floating-point noise
  function tickText(value, step) {
    const decimals = Math.max(0, Math.min(6, -Math.floor(Math.log10(step)) ));
    const rounded = Number(value.toFixed(decimals));
    if (Object.is(rounded, -0)) {
      return "0";
    }
    return String(rounded);
  }

  // Build an axis scale: value → pixel
  function makeScale(axis, pixelMin, pixelMax) {
    const span = axis.max - axis.min;
    return function (value) {
      return pixelMin + ((value - axis.min) / span) * (pixelMax - pixelMin);
    };
  }

  // How many minor divisions per major step give a readable grid
  function minorDivisions(axis) {
    if (axis.minor) {
      return axis.minor;
    }
    const majors = Math.round((axis.max - axis.min) / axis.step);
    if (majors <= 6) {
      return 5;
    }
    if (majors <= 12) {
      return 2;
    }
    return 1;
  }

  // Catmull–Rom spline through points, as an SVG path
  function smoothPath(points, sx, sy) {
    if (points.length < 3) {
      return linePath(points, sx, sy);
    }
    let d = "M" + sx(points[0][0]).toFixed(1) + "," + sy(points[0][1]).toFixed(1);
    for (let index = 0; index < points.length - 1; index += 1) {
      const p0 = points[Math.max(0, index - 1)];
      const p1 = points[index];
      const p2 = points[index + 1];
      const p3 = points[Math.min(points.length - 1, index + 2)];
      const c1x = p1[0] + (p2[0] - p0[0]) / 6;
      const c1y = p1[1] + (p2[1] - p0[1]) / 6;
      const c2x = p2[0] - (p3[0] - p1[0]) / 6;
      const c2y = p2[1] - (p3[1] - p1[1]) / 6;
      d += "C" + sx(c1x).toFixed(1) + "," + sy(c1y).toFixed(1) + " " +
        sx(c2x).toFixed(1) + "," + sy(c2y).toFixed(1) + " " +
        sx(p2[0]).toFixed(1) + "," + sy(p2[1]).toFixed(1);
    }
    return d;
  }

  function linePath(points, sx, sy) {
    let d = "";
    points.forEach(function (point, index) {
      d += (index === 0 ? "M" : "L") + sx(point[0]).toFixed(1) + "," + sy(point[1]).toFixed(1);
    });
    return d;
  }

  // Interpolate y on a series at x (linear between points)
  function interpolate(points, x) {
    for (let index = 0; index < points.length - 1; index += 1) {
      const a = points[index];
      const b = points[index + 1];
      if ((x >= a[0] && x <= b[0]) || (x <= a[0] && x >= b[0])) {
        if (b[0] === a[0]) {
          return a[1];
        }
        return a[1] + ((x - a[0]) / (b[0] - a[0])) * (b[1] - a[1]);
      }
    }
    return null;
  }

  // Points of a series clipped to [from, to] on x, including interpolated ends
  function clipSeries(points, from, to) {
    const inside = [];
    const startY = interpolate(points, from);
    if (startY !== null) {
      inside.push([from, startY]);
    }
    points.forEach(function (point) {
      if (point[0] > from && point[0] < to) {
        inside.push(point);
      }
    });
    const endY = interpolate(points, to);
    if (endY !== null) {
      inside.push([to, endY]);
    }
    return inside;
  }

  function render(spec) {
    const x = spec.x;
    const y = spec.y;
    const plotLeft = PAD_LEFT;
    const plotRight = WIDTH - PAD_RIGHT;
    const plotTop = PAD_TOP;
    const plotBottom = HEIGHT - PAD_BOTTOM;
    const sx = makeScale(x, plotLeft, plotRight);
    const sy = makeScale(y, plotBottom, plotTop);

    let svg = "";

    // ---- grid ----
    const xMinor = minorDivisions(x);
    const yMinor = minorDivisions(y);
    const xMajors = Math.round((x.max - x.min) / x.step);
    const yMajors = Math.round((y.max - y.min) / y.step);

    svg += "<g class=\"g-minor\">";
    for (let index = 0; index <= xMajors * xMinor; index += 1) {
      if (index % xMinor === 0) {
        continue;
      }
      const value = x.min + (index * x.step) / xMinor;
      const px = sx(value).toFixed(1);
      svg += "<line x1=\"" + px + "\" y1=\"" + plotTop + "\" x2=\"" + px + "\" y2=\"" + plotBottom + "\"/>";
    }
    for (let index = 0; index <= yMajors * yMinor; index += 1) {
      if (index % yMinor === 0) {
        continue;
      }
      const value = y.min + (index * y.step) / yMinor;
      const py = sy(value).toFixed(1);
      svg += "<line x1=\"" + plotLeft + "\" y1=\"" + py + "\" x2=\"" + plotRight + "\" y2=\"" + py + "\"/>";
    }
    svg += "</g>";

    svg += "<g class=\"g-major\">";
    for (let index = 0; index <= xMajors; index += 1) {
      const px = sx(x.min + index * x.step).toFixed(1);
      svg += "<line x1=\"" + px + "\" y1=\"" + plotTop + "\" x2=\"" + px + "\" y2=\"" + plotBottom + "\"/>";
    }
    for (let index = 0; index <= yMajors; index += 1) {
      const py = sy(y.min + index * y.step).toFixed(1);
      svg += "<line x1=\"" + plotLeft + "\" y1=\"" + py + "\" x2=\"" + plotRight + "\" y2=\"" + py + "\"/>";
    }
    svg += "</g>";

    // ---- shaded regions (under the grid lines of the data) ----
    if (spec.shade) {
      spec.shade.forEach(function (region) {
        const series = spec.series[region.series || 0];
        const clipped = clipSeries(series.points, region.from, region.to);
        if (clipped.length < 2) {
          return;
        }
        const baseline = region.baseline !== undefined ? region.baseline : Math.max(y.min, 0);
        let d = "M" + sx(clipped[0][0]).toFixed(1) + "," + sy(baseline).toFixed(1);
        clipped.forEach(function (point) {
          d += "L" + sx(point[0]).toFixed(1) + "," + sy(point[1]).toFixed(1);
        });
        d += "L" + sx(clipped[clipped.length - 1][0]).toFixed(1) + "," + sy(baseline).toFixed(1) + "Z";
        svg += "<path class=\"g-shade\" d=\"" + d + "\"/>";
      });
    }

    // ---- axes ----
    const xAxisY = sy(Math.min(Math.max(0, y.min), y.max)).toFixed(1);
    const yAxisX = sx(Math.min(Math.max(0, x.min), x.max)).toFixed(1);
    svg += "<g class=\"g-axis\">";
    svg += "<line x1=\"" + plotLeft + "\" y1=\"" + xAxisY + "\" x2=\"" + plotRight + "\" y2=\"" + xAxisY + "\"/>";
    svg += "<line x1=\"" + yAxisX + "\" y1=\"" + plotTop + "\" x2=\"" + yAxisX + "\" y2=\"" + plotBottom + "\"/>";
    svg += "</g>";

    // ---- tick labels ----
    svg += "<g class=\"g-ticks\">";
    for (let index = 0; index <= xMajors; index += 1) {
      const value = x.min + index * x.step;
      svg += "<text x=\"" + sx(value).toFixed(1) + "\" y=\"" + (plotBottom + 16) + "\" text-anchor=\"middle\">" + tickText(value, x.step) + "</text>";
    }
    for (let index = 0; index <= yMajors; index += 1) {
      const value = y.min + index * y.step;
      svg += "<text x=\"" + (plotLeft - 8) + "\" y=\"" + (sy(value) + 4).toFixed(1) + "\" text-anchor=\"end\">" + tickText(value, y.step) + "</text>";
    }
    svg += "</g>";

    // ---- series ----
    (spec.series || []).forEach(function (series) {
      const kind = series.kind || "line";
      if (kind === "data") {
        svg += "<g class=\"g-data\">";
        series.points.forEach(function (point) {
          const px = sx(point[0]);
          const py = sy(point[1]);
          svg += "<path d=\"M" + (px - 4).toFixed(1) + "," + (py - 4).toFixed(1) + "L" + (px + 4).toFixed(1) + "," + (py + 4).toFixed(1) +
            "M" + (px - 4).toFixed(1) + "," + (py + 4).toFixed(1) + "L" + (px + 4).toFixed(1) + "," + (py - 4).toFixed(1) + "\"/>";
        });
        svg += "</g>";
        if (series.fit) {
          svg += "<path class=\"g-line\" d=\"" + linePath(series.fit, sx, sy) + "\"/>";
        }
        return;
      }
      const path = kind === "curve" ? smoothPath(series.points, sx, sy) : linePath(series.points, sx, sy);
      const cls = kind === "dashed" ? "g-dashed" : (kind === "tangent" ? "g-tangent" : "g-line");
      svg += "<path class=\"" + cls + "\" d=\"" + path + "\"/>";
    });

    // ---- marks ----
    (spec.marks || []).forEach(function (mark) {
      const px = sx(mark.x);
      const py = sy(mark.y);
      if (mark.drop) {
        svg += "<line class=\"g-drop\" x1=\"" + px.toFixed(1) + "\" y1=\"" + py.toFixed(1) + "\" x2=\"" + px.toFixed(1) + "\" y2=\"" + plotBottom + "\"/>";
        svg += "<line class=\"g-drop\" x1=\"" + plotLeft + "\" y1=\"" + py.toFixed(1) + "\" x2=\"" + px.toFixed(1) + "\" y2=\"" + py.toFixed(1) + "\"/>";
      }
      svg += "<circle class=\"g-mark\" cx=\"" + px.toFixed(1) + "\" cy=\"" + py.toFixed(1) + "\" r=\"4\"/>";
      if (mark.label) {
        const dx = mark.dx !== undefined ? mark.dx : 9;
        const dy = mark.dy !== undefined ? mark.dy : -9;
        svg += "<text class=\"g-marklabel\" x=\"" + (px + dx).toFixed(1) + "\" y=\"" + (py + dy).toFixed(1) + "\">" + esc(mark.label) + "</text>";
      }
    });

    // ---- free labels ----
    (spec.labels || []).forEach(function (label) {
      svg += "<text class=\"g-label\" x=\"" + sx(label.x).toFixed(1) + "\" y=\"" + sy(label.y).toFixed(1) + "\" text-anchor=\"" + (label.anchor || "start") + "\">" + esc(label.text) + "</text>";
    });

    const markup = "<svg class=\"graph-svg\" viewBox=\"0 0 " + WIDTH + " " + HEIGHT + "\" xmlns=\"http://www.w3.org/2000/svg\" role=\"img\" aria-label=\"" +
      esc((spec.alt || (y.label + " against " + x.label))) + "\">" + svg + "</svg>";

    return { svg: markup, xLabel: x.label, yLabel: y.label };
  }

  /* ------------------------------------------------------------------
     Validation (shared with the Python validator's intent)
     ------------------------------------------------------------------ */

  function validate(spec) {
    const problems = [];
    if (!spec || typeof spec !== "object") {
      return ["graph: not an object"];
    }
    ["x", "y"].forEach(function (name) {
      const axis = spec[name];
      if (!axis) {
        problems.push("graph." + name + ": missing");
        return;
      }
      if (typeof axis.label !== "string" || !axis.label) {
        problems.push("graph." + name + ".label: missing");
      }
      ["min", "max", "step"].forEach(function (key) {
        if (typeof axis[key] !== "number") {
          problems.push("graph." + name + "." + key + ": must be a number");
        }
      });
      if (typeof axis.min === "number" && typeof axis.max === "number" && typeof axis.step === "number") {
        if (axis.max <= axis.min) {
          problems.push("graph." + name + ": max must exceed min");
        }
        const majors = (axis.max - axis.min) / axis.step;
        if (Math.abs(majors - Math.round(majors)) > 1e-6) {
          problems.push("graph." + name + ": step must divide the range exactly");
        }
        if (majors > 20) {
          problems.push("graph." + name + ": more than 20 major divisions");
        }
      }
    });
    if (!Array.isArray(spec.series) || spec.series.length === 0) {
      problems.push("graph.series: must be a non-empty list");
    } else {
      spec.series.forEach(function (series, index) {
        if (!Array.isArray(series.points) || series.points.length < (series.kind === "data" ? 1 : 2)) {
          problems.push("graph.series[" + index + "].points: need at least two points");
          return;
        }
        series.points.forEach(function (point, pointIndex) {
          if (!Array.isArray(point) || point.length !== 2 || typeof point[0] !== "number" || typeof point[1] !== "number") {
            problems.push("graph.series[" + index + "].points[" + pointIndex + "]: must be [x, y] numbers");
            return;
          }
          if (spec.x && spec.y && (point[0] < spec.x.min - 1e-9 || point[0] > spec.x.max + 1e-9 || point[1] < spec.y.min - 1e-9 || point[1] > spec.y.max + 1e-9)) {
            problems.push("graph.series[" + index + "].points[" + pointIndex + "]: " + JSON.stringify(point) + " lies outside the axes");
          }
        });
        if (series.kind && ["line", "curve", "dashed", "data", "tangent"].indexOf(series.kind) < 0) {
          problems.push("graph.series[" + index + "].kind: unknown kind " + series.kind);
        }
      });
    }
    (spec.marks || []).forEach(function (mark, index) {
      if (typeof mark.x !== "number" || typeof mark.y !== "number") {
        problems.push("graph.marks[" + index + "]: x and y must be numbers");
      }
    });
    return problems;
  }

  return { render: render, validate: validate };
}));
