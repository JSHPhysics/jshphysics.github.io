// The polarimeter's physics. Pure maths, no drawing.
// The build script and the page both use this file, so the light on screen,
// the eyepiece view and every number come from the same sums.

const DEG = Math.PI / 180;

// Length of the sample tube in decimetres (the unit used for specific rotation).
export const TUBE_LENGTH_DM = 1;

// Samples.
// specific: specific rotation in degrees per (dm x g/cm3). Positive is clockwise
//           as seen by the observer looking towards the lamp.
// real:     true for a measured value, false for an illustrative one.
export const SAMPLES = [
  { id: "water", name: "Water", specific: 0, real: true, note: "Not optically active: no chiral molecules." },
  { id: "plus", name: "(+) enantiomer", specific: 60, real: false, note: "One optical isomer of an example compound." },
  { id: "minus", name: "(−) enantiomer", specific: -60, real: false, note: "The mirror-image isomer of the same compound." },
  { id: "racemic", name: "Racemic mixture", specific: 0, real: false, note: "Equal amounts of both enantiomers: their rotations cancel." },
  { id: "sucrose", name: "Sucrose", specific: 66.5, real: true, note: "Table sugar, measured with sodium light." },
];

// Observed rotation of the plane of polarisation, in degrees.
//   alpha = [alpha] x l x c
export function rotation(sample, concentration) {
  return sample.specific * TUBE_LENGTH_DM * concentration;
}

// The analyser's scale reads 0 when it is crossed with the polariser, so with
// no rotation the field is dark at 0. Its transmission axis is then at
// (90 + reading) degrees from the polariser's axis.
//
// Fraction of the light's amplitude that passes the analyser (signed).
export function amplitudeThrough(reading, alpha) {
  return Math.sin((reading - alpha) * DEG);
}

// Fraction of the light's intensity that passes the analyser (Malus's law).
export function brightness(reading, alpha) {
  const amplitude = amplitudeThrough(reading, alpha);
  return amplitude * amplitude;
}

// Format an angle with its sign: +30.0°, −12.5°, 0.0°.
export function sayAngle(angle) {
  const rounded = Math.round(angle * 10) / 10;
  let sign = "";
  if (rounded > 0) {
    sign = "+";
  }
  if (rounded < 0) {
    sign = "−";
  }
  return sign + Math.abs(rounded).toFixed(1) + "°";
}
