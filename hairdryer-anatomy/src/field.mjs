// A small 2D magnetic field solver for the wiring diagram (Fig 3).
//
// It solves for the vector potential A (pointing out of the page) on a square grid:
//     div( nu grad A ) = -J - curl(M)
// where nu = 1/mu_r, J is the current density in the coil sides and M is the magnets' magnetisation.
// In 2D the flux lines are the contours of A, and B = (dA/dy, -dA/dx).
//
// Coordinates are the diagram's own: x to the right, y up, origin on the shaft, in diagram units.

export const FIELD_GRID = {
  cells: 100, // cells along each side
  half: 200, // the grid covers -200..200 in x and y
  ironMu: 100, // relative permeability used for iron
  hub: 70, // radius of the iron hub
  arm: { r0: 60, r1: 138, halfWidth: 24 }, // each iron arm
  coil: { r0: 82, r1: 134, t0: 24, t1: 38 }, // the copper either side of an arm
  magnet: { r0: 150, r1: 172, halfAngle: (40 * Math.PI) / 180 },
  yoke: { r0: 172, r1: 186 }, // the steel can, which carries the flux back round
  ampTurns: 8, // full-current coil, compared with 22 for one magnet (its thickness times M = 1)
};

export function makeField() {
  const n = FIELD_GRID.cells;
  const nodes = (n + 1) * (n + 1);
  return {
    n,
    h: (2 * FIELD_GRID.half) / n,
    A: new Float32Array(nodes),
    nu: new Float32Array(n * n),
    mx: new Float32Array(n * n),
    my: new Float32Array(n * n),
    // Per-node coefficients for the relaxation sweep.
    east: new Float32Array(nodes),
    west: new Float32Array(nodes),
    north: new Float32Array(nodes),
    south: new Float32Array(nodes),
    total: new Float32Array(nodes),
    source: new Float32Array(nodes),
    reference: 0,
  };
}

// Describe the materials and currents for the rotor at angle phi.
// currents: the three coil currents (+1, +0.5, -0.5 or -1).
// north, south: the angles of the middles of the two magnets.
export function setRotor(field, phi, currents, north, south) {
  const G = FIELD_GRID;
  const n = field.n;
  const h = field.h;
  const ironNu = 1 / G.ironMu;
  const TAU = Math.PI * 2;
  // Both magnets are magnetised along the line from the north magnet to the south magnet.
  const mDirX = Math.cos(south);
  const mDirY = Math.sin(south);
  const cosines = [0, 1, 2].map((k) => Math.cos(phi + (k * TAU) / 3));
  const sines = [0, 1, 2].map((k) => Math.sin(phi + (k * TAU) / 3));

  const angleGap = (a, b) => {
    let gap = (a - b) % TAU;
    if (gap > Math.PI) {
      gap -= TAU;
    }
    if (gap < -Math.PI) {
      gap += TAU;
    }
    return Math.abs(gap);
  };

  // Materials, cell by cell.
  for (let j = 0; j < n; j += 1) {
    const y = -G.half + (j + 0.5) * h;
    for (let i = 0; i < n; i += 1) {
      const x = -G.half + (i + 0.5) * h;
      const index = j * n + i;
      const r = Math.hypot(x, y);
      let nu = 1;
      let mx = 0;
      let my = 0;
      if (r < G.hub) {
        nu = ironNu;
      } else if (r >= G.yoke.r0 && r < G.yoke.r1) {
        nu = ironNu;
      } else if (r >= G.magnet.r0 && r < G.magnet.r1) {
        const angle = Math.atan2(y, x);
        if (angleGap(angle, north) < G.magnet.halfAngle || angleGap(angle, south) < G.magnet.halfAngle) {
          mx = mDirX;
          my = mDirY;
        }
      } else if (r < G.arm.r1 + h) {
        for (let k = 0; k < 3; k += 1) {
          const along = x * cosines[k] + y * sines[k];
          const across = -x * sines[k] + y * cosines[k];
          if (along > G.arm.r0 && along < G.arm.r1 && Math.abs(across) < G.arm.halfWidth) {
            nu = ironNu;
          }
        }
      }
      field.nu[index] = nu;
      field.mx[index] = mx;
      field.my[index] = my;
    }
  }

  // Coefficients and sources, node by node (edge nodes stay at A = 0).
  const J0 = G.ampTurns / ((G.coil.r1 - G.coil.r0) * (G.coil.t1 - G.coil.t0));
  const row = n + 1;
  for (let j = 1; j < n; j += 1) {
    const y = -G.half + j * h;
    for (let i = 1; i < n; i += 1) {
      const x = -G.half + i * h;
      const node = j * row + i;
      // The four cells round this node.
      const sw = (j - 1) * n + (i - 1);
      const se = sw + 1;
      const nw = j * n + (i - 1);
      const ne = nw + 1;
      const e = (field.nu[se] + field.nu[ne]) / 2;
      const w = (field.nu[sw] + field.nu[nw]) / 2;
      const nn = (field.nu[nw] + field.nu[ne]) / 2;
      const s = (field.nu[sw] + field.nu[se]) / 2;
      field.east[node] = e;
      field.west[node] = w;
      field.north[node] = nn;
      field.south[node] = s;
      field.total[node] = e + w + nn + s;

      // Circulation of M round the node, anticlockwise.
      const circulation = ((field.mx[sw] + field.mx[se]) - (field.mx[ne] + field.mx[nw]) + (field.my[se] + field.my[ne]) - (field.my[nw] + field.my[sw])) * (h / 2);

      // Current in the coil sides.  For a positive coil current it comes out of the page
      // on the anticlockwise side of the arm and goes in on the other side.
      let current = 0;
      const r = Math.hypot(x, y);
      if (r > G.coil.r0 - h && r < G.coil.r1 + G.coil.t1) {
        for (let k = 0; k < 3; k += 1) {
          const along = x * cosines[k] + y * sines[k];
          const across = -x * sines[k] + y * cosines[k];
          const side = Math.abs(across);
          if (along > G.coil.r0 && along < G.coil.r1 && side > G.coil.t0 && side < G.coil.t1) {
            current = (across > 0 ? 1 : -1) * currents[k] * J0;
          }
        }
      }
      field.source[node] = current * h * h + circulation;
    }
  }
}

// Gauss-Seidel sweeps with over-relaxation.  Returns the largest change in the last sweep.
export function relax(field, sweeps) {
  const n = field.n;
  const row = n + 1;
  const A = field.A;
  const omega = 1.9;
  let largest = 0;
  for (let sweep = 0; sweep < sweeps; sweep += 1) {
    largest = 0;
    for (let j = 1; j < n; j += 1) {
      for (let i = 1; i < n; i += 1) {
        const node = j * row + i;
        const target = (field.east[node] * A[node + 1] + field.west[node] * A[node - 1] + field.north[node] * A[node + row] + field.south[node] * A[node - row] + field.source[node]) / field.total[node];
        const change = omega * (target - A[node]);
        A[node] += change;
        const size = change < 0 ? -change : change;
        if (size > largest) {
          largest = size;
        }
      }
    }
  }
  return largest;
}

// B at a point, from the slope of A across the cell that holds it.
export function fieldAt(field, x, y) {
  const G = FIELD_GRID;
  const n = field.n;
  const row = n + 1;
  const h = field.h;
  let i = Math.floor((x + G.half) / h);
  let j = Math.floor((y + G.half) / h);
  i = Math.min(n - 1, Math.max(0, i));
  j = Math.min(n - 1, Math.max(0, j));
  const a00 = field.A[j * row + i];
  const a10 = field.A[j * row + i + 1];
  const a01 = field.A[(j + 1) * row + i];
  const a11 = field.A[(j + 1) * row + i + 1];
  const dAdx = (a10 - a00 + a11 - a01) / (2 * h);
  const dAdy = (a01 - a00 + a11 - a10) / (2 * h);
  return [dAdy, -dAdx];
}

// Flux lines: contours of A at evenly spaced levels.
// Returns { d, heads } where d is SVG path data and heads are [x, y, angle] for arrowheads,
// placed where a line crosses the air gap.  toScreen turns diagram x, y into screen x, y.
export function fluxLines(field, spacing, toScreen) {
  const G = FIELD_GRID;
  const n = field.n;
  const row = n + 1;
  const h = field.h;
  const A = field.A;
  const gap = (G.arm.r1 + G.magnet.r0) / 2;
  let d = "";
  const heads = [];
  const fixed = (value) => value.toFixed(1);

  for (let j = 0; j < n; j += 1) {
    const y0 = -G.half + j * h;
    for (let i = 0; i < n; i += 1) {
      const x0 = -G.half + i * h;
      const a = A[j * row + i];
      const b = A[j * row + i + 1];
      const c = A[(j + 1) * row + i + 1];
      const e = A[(j + 1) * row + i];
      const low = Math.min(a, b, c, e);
      const high = Math.max(a, b, c, e);
      const first = Math.ceil(low / spacing - 0.5);
      const last = Math.floor(high / spacing - 0.5);
      for (let step = first; step <= last; step += 1) {
        // Levels sit half way between multiples of the spacing, so none lies exactly on A = 0.
        const level = (step + 0.5) * spacing;
        const points = [];
        // Where the level crosses each edge of the cell.
        if ((a - level) * (b - level) < 0) {
          points.push([x0 + (h * (level - a)) / (b - a), y0]);
        }
        if ((b - level) * (c - level) < 0) {
          points.push([x0 + h, y0 + (h * (level - b)) / (c - b)]);
        }
        if ((e - level) * (c - level) < 0) {
          points.push([x0 + (h * (level - e)) / (c - e), y0 + h]);
        }
        if ((a - level) * (e - level) < 0) {
          points.push([x0, y0 + (h * (level - a)) / (e - a)]);
        }
        for (let index = 0; index + 1 < points.length; index += 2) {
          const p = points[index];
          const q = points[index + 1];
          const sp = toScreen(p[0], p[1]);
          const sq = toScreen(q[0], q[1]);
          d += "M" + fixed(sp[0]) + " " + fixed(sp[1]) + "L" + fixed(sq[0]) + " " + fixed(sq[1]);
          // An arrowhead where this line crosses the middle of the air gap.
          const rp = Math.hypot(p[0], p[1]);
          const rq = Math.hypot(q[0], q[1]);
          if ((rp - gap) * (rq - gap) < 0) {
            const mid = [(p[0] + q[0]) / 2, (p[1] + q[1]) / 2];
            const B = fieldAt(field, mid[0], mid[1]);
            const tip = toScreen(mid[0] + B[0], mid[1] + B[1]);
            const base = toScreen(mid[0], mid[1]);
            heads.push([base[0], base[1], (Math.atan2(tip[1] - base[1], tip[0] - base[0]) * 180) / Math.PI]);
          }
        }
      }
    }
  }
  return { d, heads };
}

// Turning effect on everything inside the air gap, from the Maxwell stress on a circle in the gap.
// Positive is anticlockwise.  Units are arbitrary but consistent with copperTorque().
export function gapTorque(field) {
  const G = FIELD_GRID;
  const R = (G.arm.r1 + G.magnet.r0) / 2;
  const steps = 360;
  let sum = 0;
  for (let index = 0; index < steps; index += 1) {
    const angle = (index / steps) * Math.PI * 2;
    const c = Math.cos(angle);
    const s = Math.sin(angle);
    const B = fieldAt(field, R * c, R * s);
    const radialPart = B[0] * c + B[1] * s;
    const tangentPart = -B[0] * s + B[1] * c;
    sum += radialPart * tangentPart;
  }
  return (sum / steps) * Math.PI * 2 * R * R;
}

// Turning effect from the force on the copper alone: sum of r x (J x B) over the coil sides.
export function copperTorque(field, phi, currents) {
  const G = FIELD_GRID;
  const J0 = G.ampTurns / ((G.coil.r1 - G.coil.r0) * (G.coil.t1 - G.coil.t0));
  const TAU = Math.PI * 2;
  const step = 2;
  let sum = 0;
  for (let k = 0; k < 3; k += 1) {
    const c = Math.cos(phi + (k * TAU) / 3);
    const s = Math.sin(phi + (k * TAU) / 3);
    for (const side of [1, -1]) {
      for (let along = G.coil.r0 + step / 2; along < G.coil.r1; along += step) {
        for (let across = G.coil.t0 + step / 2; across < G.coil.t1; across += step) {
          const x = along * c - side * across * s;
          const y = along * s + side * across * c;
          const B = fieldAt(field, x, y);
          const J = side * currents[k] * J0;
          // Force per area on current J (out of page): (-J By, J Bx).  Torque = x Fy - y Fx.
          sum += (x * (J * B[0]) - y * (-J * B[1])) * step * step;
        }
      }
    }
  }
  return sum;
}
