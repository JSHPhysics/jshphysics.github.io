// Spectral data and the physics model.  Shared by the build script (Node) and the page (browser).
// Wavelengths are measured values in air, in nm, from the NIST Handbook of Basic Atomic
// Spectroscopic Data (neutral atoms only).  "strength" is NIST's relative intensity.

export const HC = 1239.84; // Planck constant times the speed of light, in eV nm
export const RYDBERG_EV = 13.6; // ionisation energy of hydrogen, in eV
export const VISIBLE = [380, 750]; // the range of wavelengths drawn as visible, in nm

export const ELEMENTS = [
  {
    id: "H",
    name: "Hydrogen",
    lines: [
      [656.28, 180],
      [486.13, 60],
      [434.05, 30],
      [410.17, 15],
      [397.01, 8],
    ],
  },
  {
    id: "He",
    name: "Helium",
    lines: [
      [388.86, 300],
      [402.62, 50],
      [447.15, 200],
      [471.31, 30],
      [492.19, 20],
      [501.57, 100],
      [587.56, 500],
      [667.82, 200],
      [706.52, 100],
      [728.14, 50],
    ],
  },
  {
    id: "Li",
    name: "Lithium",
    lines: [
      [460.29, 30],
      [497.17, 10],
      [610.37, 400],
      [670.79, 1000],
    ],
  },
  {
    id: "Na",
    name: "Sodium",
    lines: [
      [498.28, 5],
      [568.82, 7],
      [589.0, 1000],
      [589.59, 500],
      [616.07, 3],
    ],
  },
  {
    id: "Ne",
    name: "Neon",
    lines: [
      [540.06, 200],
      [585.25, 200],
      [588.19, 100],
      [594.48, 50],
      [597.55, 60],
      [603.0, 100],
      [607.43, 100],
      [609.62, 30],
      [614.31, 100],
      [616.36, 100],
      [621.73, 100],
      [626.65, 100],
      [633.44, 100],
      [638.3, 100],
      [640.22, 200],
      [650.65, 150],
      [659.9, 100],
      [667.83, 50],
      [692.95, 1000],
      [703.24, 800],
      [717.39, 800],
      [724.52, 800],
    ],
  },
  {
    id: "Hg",
    name: "Mercury",
    lines: [
      [404.66, 400],
      [435.83, 1000],
      [546.07, 500],
      [576.96, 50],
      [579.07, 60],
    ],
  },
];

// Look up one element by its symbol.
export function elementById(id) {
  for (const element of ELEMENTS) {
    if (element.id === id) {
      return element;
    }
  }
  return null;
}

// How brightly to draw a line, from 0.3 to 1.  The eye responds roughly to the logarithm of
// intensity, so the strongest line in an element is 1 and one a thousand times weaker is 0.4 (never below 0.3).
export function lineBrightness(strength, strongest) {
  const ratio = strength / strongest;
  const decades = Math.log10(ratio); // 0 for the strongest line, -3 for one a thousand times weaker
  const level = 1 + decades * 0.2;
  return Math.min(1, Math.max(0.3, level));
}

// The lines of an element as objects: { nm, level, element }.
export function linesOf(id) {
  const element = elementById(id);
  let strongest = 0;
  for (const line of element.lines) {
    strongest = Math.max(strongest, line[1]);
  }
  const list = [];
  for (const line of element.lines) {
    list.push({ nm: line[0], level: lineBrightness(line[1], strongest), element: id });
  }
  return list;
}

// Energy of level n in hydrogen, in eV.  Zero is a free electron, so bound levels are negative.
export function levelEnergy(n) {
  return -RYDBERG_EV / (n * n);
}

// Photon energy (eV) for a jump between two hydrogen levels.  Always positive.
export function gapEnergy(a, b) {
  return Math.abs(levelEnergy(a) - levelEnergy(b));
}

// Photon wavelength (nm) for a jump between two hydrogen levels.
export function gapWavelength(a, b) {
  return HC / gapEnergy(a, b);
}

// Photon energy in eV for a wavelength in nm.
export function photonEnergy(nm) {
  return HC / nm;
}

// Which part of the spectrum a wavelength is in.
export function bandOf(nm) {
  if (nm < VISIBLE[0]) {
    return "ultraviolet";
  }
  if (nm > VISIBLE[1]) {
    return "infrared";
  }
  return "visible";
}

// An approximate screen colour for a wavelength, as [r, g, b] from 0 to 255.
// (Dan Bruton's piecewise approximation.  A screen cannot show a pure spectral colour exactly.)
export function wavelengthRgb(nm) {
  let r = 0;
  let g = 0;
  let b = 0;
  if (nm >= 380 && nm < 440) {
    r = (440 - nm) / 60;
    b = 1;
  } else if (nm >= 440 && nm < 490) {
    g = (nm - 440) / 50;
    b = 1;
  } else if (nm >= 490 && nm < 510) {
    g = 1;
    b = (510 - nm) / 20;
  } else if (nm >= 510 && nm < 580) {
    r = (nm - 510) / 70;
    g = 1;
  } else if (nm >= 580 && nm < 645) {
    r = 1;
    g = (645 - nm) / 65;
  } else if (nm >= 645 && nm <= 750) {
    r = 1;
  }
  // The eye is less sensitive at both ends of the visible range, so fade the colour there.
  let fade = 1;
  if (nm < 420) {
    fade = 0.45 + (0.55 * (nm - 380)) / 40;
  }
  if (nm > 700) {
    fade = 0.45 + (0.55 * (750 - nm)) / 50;
  }
  const channel = (value) => Math.round(255 * Math.pow(value * fade, 0.8));
  return [channel(r), channel(g), channel(b)];
}

// The same colour as a CSS string.  Outside the visible range it is a neutral grey.
export function wavelengthCss(nm) {
  if (bandOf(nm) !== "visible") {
    return "rgb(150,150,160)";
  }
  const rgb = wavelengthRgb(nm);
  return "rgb(" + rgb[0] + "," + rgb[1] + "," + rgb[2] + ")";
}

// The colour a glowing gas appears: its lines added together, weighted by their measured strength.
export function glowCss(ids) {
  let r = 0;
  let g = 0;
  let b = 0;
  for (const id of ids) {
    for (const line of elementById(id).lines) {
      if (bandOf(line[0]) === "visible") {
        const rgb = wavelengthRgb(line[0]);
        r += rgb[0] * line[1];
        g += rgb[1] * line[1];
        b += rgb[2] * line[1];
      }
    }
  }
  // Scale so the brightest channel is 255: a glow is bright, whatever its colour.
  const peak = Math.max(r, g, b, 1);
  const scale = 255 / peak;
  return "rgb(" + Math.round(r * scale) + "," + Math.round(g * scale) + "," + Math.round(b * scale) + ")";
}

// How dark to draw an absorption line, from 0 to 1.  Weak lines take out little light.
export function lineDarkness(level) {
  return 0.15 + 0.85 * level * level;
}

// Diffraction grating: the first-order angle (radians) for a wavelength, from d sin(theta) = lambda.
export const GRATING_LINES_PER_MM = 1000;
export function gratingAngle(nm) {
  const spacing = 1e6 / GRATING_LINES_PER_MM; // slit spacing d in nm
  return Math.asin(nm / spacing);
}
