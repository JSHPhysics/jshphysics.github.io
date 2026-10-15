/*
 * richmath.js — render the plain-text physics notation used in the data
 * files as KaTeX, without changing the data.
 *
 * The data files write maths in readable plain text ("v² = u² + 2as",
 * "1.66 × 10⁻²⁷ kg", "T = 2π√(L/g)"). This module splits each string into
 * prose and maths segments, converts the maths segments to TeX, and renders
 * them with KaTeX. Prose stays as HTML text in the page font.
 *
 * Exposes:
 *   richmath.toTeX(text)        plain-text maths → TeX string (no rendering)
 *   richmath.renderMath(text)   whole string is maths → KaTeX HTML
 *   richmath.renderRich(text)   mixed prose and maths → HTML
 *   richmath.segment(text)      [{ kind: "math" | "text", text }] (for tests)
 *
 * Works in the browser (window.richmath, needs window.katex) and in Node
 * (module.exports, pass katex via richmath.useKatex(katex)).
 */
(function (root, factory) {
  if (typeof module === "object" && module.exports) {
    module.exports = factory();
  } else {
    root.richmath = factory();
  }
}(typeof self !== "undefined" ? self : this, function () {

  // The KaTeX instance to render with; set lazily
  let katexLib = null;

  function useKatex(lib) {
    katexLib = lib;
  }

  function getKatex() {
    if (katexLib) {
      return katexLib;
    }
    if (typeof window !== "undefined" && window.katex) {
      katexLib = window.katex;
    }
    return katexLib;
  }

  /* ------------------------------------------------------------------
     Character classes
     ------------------------------------------------------------------ */

  const SUPERSCRIPT_CHARS = "⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺";
  const SUBSCRIPT_CHARS = "₀₁₂₃₄₅₆₇₈₉";
  const GREEK = "αβγδεζηθικλμνξοπρστυφχψωΓΔΘΛΞΠΣΦΨΩ";

  // Operators and relations that belong to maths
  const OPERATORS = {
    "×": "\\times",
    "·": "\\cdot",
    "−": "-",
    "-": "-",
    "+": "+",
    "=": "=",
    "≈": "\\approx",
    "∝": "\\propto",
    "±": "\\pm",
    "≤": "\\leq",
    "≥": "\\geq",
    "→": "\\rightarrow",
    "<": "<",
    ">": ">",
    "∞": "\\infty",
    "/": "/",
    "÷": "\\div",
    "|": "|",
    "^": "^",
    "√": "√",
    "⟨": "\\langle ",
    "⟩": "\\rangle ",
    "½": "\\tfrac{1}{2}",
    "⅓": "\\tfrac{1}{3}",
    "¼": "\\tfrac{1}{4}",
    "°": "°",
    "%": "\\%",
  };

  // Function names that render upright with a thin space after
  const FUNCTIONS = new Set(["sin", "cos", "tan", "log", "ln", "exp", "arcsin", "arccos", "arctan"]);

  // Multi-letter quantities that are maths, not prose, and render upright
  const IDENTIFIERS = new Set([
    "KE", "PE", "GPE", "EPE", "BE", "EK", "EP", "Ek", "Ep", "emf",
  ]);

  // Unit tokens (without exponent). Prefix handling is by regex below.
  const BASE_UNITS = [
    "m", "s", "g", "kg", "N", "J", "W", "Pa", "Hz", "C", "V", "A", "Ω", "F", "H",
    "T", "Wb", "K", "mol", "eV", "keV", "MeV", "GeV", "Bq", "u", "rad", "sr",
    "AU", "ly", "pc", "Mpc", "kpc", "h", "min", "yr", "L", "l", "cd", "lx", "dB",
    "°C", "°", "%", "p", "rpm", "atm", "bar", "cm", "mm", "km", "nm", "pm", "fm",
    "μm", "mg", "μg", "ng", "ms", "μs", "ns", "ps", "kN", "MN", "mN", "μN", "kJ",
    "MJ", "GJ", "mJ", "μJ", "kW", "MW", "GW", "mW", "μW", "kPa", "MPa", "GPa",
    "hPa", "kHz", "MHz", "GHz", "THz", "mA", "μA", "nA", "kA", "mV", "kV", "MV",
    "μV", "kΩ", "MΩ", "mΩ", "μF", "nF", "pF", "mF", "mH", "μH", "mT", "μT", "nT",
    "kWh", "Wh", "MWh", "GWh", "eV/c²", "MeV/c²", "GeV/c²", "keV/c²", "°C⁻¹", "K⁻¹",
    "turns", "lines", "yr⁻¹",
  ];
  const UNIT_SET = new Set(BASE_UNITS);

  // Units that are unambiguous even without a number in front
  const STRONG_UNITS = new Set(BASE_UNITS.filter(function (unit) {
    return unit.length >= 2 && !IDENTIFIERS.has(unit);
  }));

  function isDigit(character) {
    return character >= "0" && character <= "9";
  }

  function isLetter(character) {
    return /[A-Za-z]/.test(character) || GREEK.indexOf(character) >= 0;
  }

  function isSuper(character) {
    return SUPERSCRIPT_CHARS.indexOf(character) >= 0;
  }

  function isSub(character) {
    return SUBSCRIPT_CHARS.indexOf(character) >= 0;
  }

  /* ------------------------------------------------------------------
     Tokeniser
     ------------------------------------------------------------------ */

  // Token types: num, word, op, open, close, space, punct
  function tokenise(text) {
    const tokens = [];
    let index = 0;

    while (index < text.length) {
      const character = text[index];

      // Whitespace
      if (/\s/.test(character)) {
        let end = index;
        while (end < text.length && /\s/.test(text[end])) {
          end += 1;
        }
        tokens.push({ type: "space", text: text.slice(index, end) });
        index = end;
        continue;
      }

      // Number: digits with optional decimal point, thousands commas, and
      // a trailing superscript exponent (for "10⁻²⁷")
      if (isDigit(character) || (character === "." && isDigit(text[index + 1] || ""))) {
        let end = index;
        while (end < text.length && (isDigit(text[end]) || text[end] === "." || text[end] === ",")) {
          // A comma or point only continues the number if a digit follows
          if ((text[end] === "." || text[end] === ",") && !isDigit(text[end + 1] || "")) {
            break;
          }
          end += 1;
        }
        let superscript = "";
        while (end < text.length && isSuper(text[end])) {
          superscript += text[end];
          end += 1;
        }
        tokens.push({ type: "num", text: text.slice(index, end), base: text.slice(index, end - superscript.length), sup: superscript });
        index = end;
        continue;
      }

      // Word: letters (Latin or Greek), optionally with an ASCII subscript
      // ("λ_max", "N_A"), Unicode subscripts, superscripts, ′ primes, and a
      // trailing "/c²" unit suffix. Apostrophes inside prose words are kept.
      if (isLetter(character) || character === "°") {
        let end = index;
        // Degree sign handles "°C" and a bare "°"
        if (character === "°") {
          end += 1;
          if (text[end] === "C" || text[end] === "F") {
            end += 1;
          }
        } else {
          while (end < text.length && (isLetter(text[end]) || text[end] === "'" || text[end] === "’")) {
            end += 1;
          }
        }
        // Unicode subscript digits
        while (end < text.length && isSub(text[end])) {
          end += 1;
        }
        // ASCII subscript: _max, _A, _0, _{...}
        if (text[end] === "_" && end + 1 < text.length) {
          end += 1;
          if (text[end] === "{") {
            const closeBrace = text.indexOf("}", end);
            end = closeBrace >= 0 ? closeBrace + 1 : text.length;
          } else {
            while (end < text.length && (isLetter(text[end]) || isDigit(text[end]))) {
              end += 1;
            }
          }
        }
        // Unicode superscripts and fraction half ("t½")
        while (end < text.length && (isSuper(text[end]) || text[end] === "½")) {
          end += 1;
        }
        // Prime
        while (end < text.length && (text[end] === "′" || text[end] === "'") && !isLetter(text[end + 1] || "")) {
          end += 1;
        }
        // "/c²" mass-unit suffix
        if (text.slice(end, end + 3) === "/c²") {
          end += 3;
        }
        tokens.push({ type: "word", text: text.slice(index, end) });
        index = end;
        continue;
      }

      // Brackets
      if (character === "(" || character === "[") {
        tokens.push({ type: "open", text: character });
        index += 1;
        continue;
      }
      if (character === ")" || character === "]") {
        tokens.push({ type: "close", text: character });
        index += 1;
        continue;
      }

      // Operators
      if (Object.prototype.hasOwnProperty.call(OPERATORS, character)) {
        tokens.push({ type: "op", text: character });
        index += 1;
        continue;
      }

      // A superscript run on its own (after a bracket: "(…)²")
      if (isSuper(character)) {
        let end = index;
        while (end < text.length && isSuper(text[end])) {
          end += 1;
        }
        tokens.push({ type: "sup", text: text.slice(index, end) });
        index = end;
        continue;
      }

      // Everything else is punctuation
      tokens.push({ type: "punct", text: character });
      index += 1;
    }

    return tokens;
  }

  /* ------------------------------------------------------------------
     Classification: which tokens are maths, which are prose
     ------------------------------------------------------------------ */

  // Split a word token into its parts: core letters, subscript, superscript, suffix
  function splitWord(text) {
    const match = /^([A-Za-z°αβγδεζηθικλμνξοπρστυφχψωΓΔΘΛΞΠΣΦΨΩ'’]+)([₀-₉]*)(?:_(\{[^}]*\}|[A-Za-z0-9]+))?([⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺½]*)([′']*)(\/c²)?$/.exec(text);
    if (!match) {
      return { core: text, usub: "", sub: "", sup: "", prime: "", suffix: "" };
    }
    return {
      core: match[1],
      usub: match[2] || "",
      sub: match[3] || "",
      sup: match[4] || "",
      prime: match[5] || "",
      suffix: match[6] || "",
    };
  }

  // Is this word a unit token (ignoring exponent)?
  function unitBase(word) {
    const parts = splitWord(word);
    const candidate = parts.core + parts.usub + parts.suffix;
    if (UNIT_SET.has(candidate)) {
      return candidate;
    }
    return null;
  }

  // Does a word look like a maths identifier on its own?
  function isIdentifierWord(word) {
    const parts = splitWord(word);
    // Anything with a subscript or superscript is maths
    if (parts.sub || parts.usub || parts.sup || parts.prime) {
      return true;
    }
    const core = parts.core;
    // Single Latin or Greek letter
    if (core.length === 1) {
      return true;
    }
    // Greek word like "Δm", "Δθ", "ΔE" or "mc" style products of ≤3 letters
    // that contain a Greek letter
    if (core.length <= 3 && /[αβγδεζηθικλμνξοπρστυφχψωΓΔΘΛΞΠΣΦΨΩ]/.test(core)) {
      return true;
    }
    if (FUNCTIONS.has(core)) {
      return true;
    }
    if (IDENTIFIERS.has(core)) {
      return true;
    }
    return false;
  }

  // Short English words (≤ 4 letters) that must never be read as maths,
  // even when they sit next to a number or an equals sign
  const ENGLISH = new Set(("a an as at by do go if in is it no of on or so to up we be he me my us am " +
    "the and for not but its per via has had was are with from that this then than into each both when " +
    "what uses use used one two six ten half mass time rate gas heat wire rod car ball lift hill wave slit " +
    "lens gap tube pipe bulb lamp cell coil wing drop fall rise loss gain area step part full zero four " +
    "five nine all any can may must only same some such take tell test them they very were will your also " +
    "back base bank beam body case data days down drag each edge even ever face fact feel few find fire " +
    "flow foot form free get give goes good hand hard have head here high hold hole hour idea just keep " +
    "kind know last late lead left less let like line list long look lose lost low made make many mean " +
    "more most move much name near need new next none note now off old once open out over own pair past " +
    "path peak plan play plug plus pole pull push put read real rest ring road rock room rope rule run " +
    "safe said say see seen self send sent set ship show side sign size slow soon spot star stay stop " +
    "sure tail tall tank tape team term thin tiny tool top town true tune turn type unit upon very view " +
    "wait walk wall want warm way week well went west wet what wide wind wish word work year yet zone " +
    "air arm bar bed big bit box boy bus cut dam day dry due end eye far fat fed fee few fit fix fly " +
    "fog fun gun guy hit hot ice ill ink job joy key kid lab lap law lay leg lid lie lip lit log lot " +
    "man map mat mix mud net nut oak odd oil our pan pay pen pet pie pin pit pot raw ray red rib rim " +
    "rot row rub sad sat sea sit sky son sum sun tap tax tea tie tin tip toe ton toy try two van war " +
    "web win wet why yes zip tube fuel jet sled skis sits lamp drum reed horn bell taut tyre fish fin " +
    "deep cold warm loud soft dull dark grey blue bus van cup jug jar mug lid").split(" "));

  // Words after which a lone capital letter names a point on a diagram
  const POINT_WORDS = new Set(["point", "points", "at", "from", "to", "between", "and", "section", "through", "via", "reaches", "label", "labelled", "marked", "position"]);

  // Operators whose presence next to a short word marks it as maths
  const MATH_NEIGHBOUR_OPS = new Set(["=", "+", "×", "·", "−", "≈", "∝", "±", "→", "^", "√", "≤", "≥", "<", ">", "/"]);

  function classify(tokens) {
    const classes = new Array(tokens.length).fill(null);

    // Pass 1: words, numbers and operators
    for (let index = 0; index < tokens.length; index += 1) {
      const token = tokens[index];
      if (token.type === "num" || token.type === "op" || token.type === "sup") {
        classes[index] = "M";
      } else if (token.type === "word") {
        classes[index] = classifyWord(tokens, index);
      }
    }

    // Pass 2: brackets take the class of their content
    for (let index = 0; index < tokens.length; index += 1) {
      if (tokens[index].type === "open") {
        const closeIndex = findClose(tokens, index);
        let hasText = false;
        let hasMath = false;
        for (let inner = index + 1; inner < closeIndex; inner += 1) {
          if (classes[inner] === "T") {
            hasText = true;
          }
          if (tokens[inner].type === "punct" && tokens[inner].text !== ",") {
            hasText = true;
          }
          if (classes[inner] === "M") {
            hasMath = true;
          }
        }
        const bracketClass = hasText || !hasMath ? "T" : "M";
        classes[index] = bracketClass;
        if (closeIndex < tokens.length) {
          classes[closeIndex] = bracketClass;
        }
      }
    }
    // Any unmatched close bracket
    for (let index = 0; index < tokens.length; index += 1) {
      if (tokens[index].type === "close" && classes[index] === null) {
        classes[index] = "T";
      }
    }

    // Pass 3: spaces and punctuation join their neighbours
    for (let index = 0; index < tokens.length; index += 1) {
      const token = tokens[index];
      if (classes[index] !== null) {
        continue;
      }
      const previous = previousClass(classes, index);
      const next = nextClass(classes, index);
      if (token.type === "space") {
        classes[index] = previous === "M" && next === "M" ? "M" : "T";
      } else if (token.type === "punct") {
        // A comma between two maths tokens stays in the maths; a full stop
        // or colon ends the maths run
        if (token.text === "," && previous === "M" && next === "M") {
          classes[index] = "M";
        } else {
          classes[index] = "T";
        }
      } else {
        classes[index] = "T";
      }
    }

    // Pass 4: a lone operator like "-" or "/" between prose is prose ("two-step")
    for (let index = 0; index < tokens.length; index += 1) {
      const token = tokens[index];
      if (token.type === "op" && (token.text === "-" || token.text === "/" || token.text === "−")) {
        const previousIndex = index - 1;
        const nextIndex = index + 1;
        const previousIsWordText = previousIndex >= 0 && tokens[previousIndex].type === "word" && classes[previousIndex] === "T";
        const nextIsWordText = nextIndex < tokens.length && tokens[nextIndex].type === "word" && classes[nextIndex] === "T";
        if (previousIsWordText || nextIsWordText) {
          classes[index] = "T";
        }
      }
    }

    return classes;
  }

  function classifyWord(tokens, index) {
    const token = tokens[index];
    const word = token.text;
    const parts = splitWord(word);

    const immediatePrevious = tokens[index - 1];
    const immediateNext = tokens[index + 1];

    // Letters glued to a number or a fraction symbol are symbols: 2as, 3kT, ½mv², ⅓Nm
    const gluedToNumber = (immediatePrevious && (immediatePrevious.type === "num" || immediatePrevious.type === "sup" ||
      (immediatePrevious.type === "op" && "½⅓¼".indexOf(immediatePrevious.text) >= 0))) ||
      (immediateNext && immediateNext.type === "num");

    // Units: recognised when preceded (with a space) by a number or another
    // unit, by the word "in" ("in K", "in eV"), or when the unit is
    // unambiguous on its own (kg, Hz, MeV...), or carries a negative
    // exponent (s⁻¹), or is followed by such a unit (m s⁻¹).
    const base = unitBase(word);
    if (base && !gluedToNumber) {
      const previous = previousMeaningful(tokens, index);
      const previousIsNumber = previous && previous.type === "num";
      const previousIsIn = previous && previous.type === "word" && previous.text === "in";
      const previousIsUnit = previous && previous.type === "word" && previous.isUnit;
      const hasNegativeExponent = parts.sup.indexOf("⁻") >= 0;
      const next = nextMeaningful(tokens, index);
      const nextIsExponentUnit = next && next.type === "word" && unitBase(next.text) && splitWord(next.text).sup.indexOf("⁻") >= 0;
      const strong = STRONG_UNITS.has(base) && !ENGLISH.has(base);

      if (previousIsNumber || previousIsUnit || previousIsIn || hasNegativeExponent || nextIsExponentUnit || strong) {
        token.isUnit = true;
        return "M";
      }
    }

    if (gluedToNumber) {
      return "M";
    }

    // Anything carrying a subscript, superscript or prime is maths
    if (parts.sub || parts.usub || parts.sup || parts.prime || parts.suffix) {
      return "M";
    }

    const core = parts.core;

    if (FUNCTIONS.has(core) || IDENTIFIERS.has(core)) {
      return "M";
    }

    const near = adjacentToMaths(tokens, index);

    // Single letters are maths unless they are an English word standing
    // alone ("A ball", "I think") or part of an abbreviation ("p.d.", "e.m.f.").
    // A letter naming a point ("point A", "from A to B") is a symbol.
    if (core.length === 1) {
      const previous = previousMeaningful(tokens, index);
      const isCapital = core >= "A" && core <= "Z";
      const namesAPoint = isCapital && previous && previous.type === "word" && POINT_WORDS.has(previous.text.toLowerCase());
      if (ENGLISH.has(core.toLowerCase()) && !near && !namesAPoint) {
        return "T";
      }
      const nextIsDot = immediateNext && immediateNext.type === "punct" && immediateNext.text === ".";
      const afterDot = tokens[index + 2];
      const abbreviationStart = nextIsDot && afterDot && afterDot.type === "word" && afterDot.text.length === 1;
      const previousIsDot = immediatePrevious && immediatePrevious.type === "punct" && immediatePrevious.text === ".";
      const beforeDot = tokens[index - 2];
      const abbreviationTail = previousIsDot && beforeDot && beforeDot.type === "word" && beforeDot.text.length === 1 && nextIsDot;
      if ((abbreviationStart || abbreviationTail) && !near) {
        return "T";
      }
      return "M";
    }

    // Two capital letters name a section or a pair of points: AB, PQ
    if (/^[A-Z]{2}$/.test(core)) {
      return "M";
    }

    if (ENGLISH.has(word.toLowerCase())) {
      const previous = previousMeaningful(tokens, index);
      const afterOperator = previous && previous.type === "op" && "=+−×·/√^→".indexOf(previous.text) >= 0;
      if (word.length <= 2 && afterOperator) {
        return "M";
      }
      return "T";
    }

    // Short words containing a Greek letter: Δm, ΔE, ωt
    if (core.length <= 3 && /[αβγδεζηθικλμνξοπρστυφχψωΓΔΘΛΞΠΣΦΨΩ]/.test(core)) {
      return "M";
    }

    // Short products of symbols next to an operator or number: mg, at, GMm, BIL, mcΔθ
    if (core.length <= 4 && near) {
      return "M";
    }

    return "T";
  }

  // A word that is a single symbol or carries a subscript/superscript
  function isSymbolWord(word) {
    const parts = splitWord(word);
    if (parts.sub || parts.usub || parts.sup || parts.prime) {
      return true;
    }
    return parts.core.length === 1;
  }

  // Is this token next to something that is clearly maths?
  function adjacentToMaths(tokens, index) {
    const previous = previousMeaningful(tokens, index);
    const next = nextMeaningful(tokens, index);
    const immediatePrevious = tokens[index - 1];
    const immediateNext = tokens[index + 1];

    // Glued to a number: "2GM", "3kT"
    if (immediatePrevious && immediatePrevious.type === "num") {
      return true;
    }
    if (immediateNext && immediateNext.type === "num") {
      return true;
    }

    // Across a comma: "s, u, v, a, t"
    const previousIndex = tokens.indexOf(previous);
    const nextIndex = tokens.indexOf(next);
    if (previous && previous.type === "punct" && previous.text === ",") {
      const beyond = previousMeaningful(tokens, previousIndex);
      if (beyond && beyond.type === "word" && isSymbolWord(beyond.text)) {
        return true;
      }
    }
    if (next && next.type === "punct" && next.text === ",") {
      const beyond = nextMeaningful(tokens, nextIndex);
      if (beyond && beyond.type === "word" && isSymbolWord(beyond.text) && !ENGLISH.has(beyond.text.toLowerCase())) {
        return true;
      }
    }

    for (const neighbour of [previous, next]) {
      if (!neighbour) {
        continue;
      }
      if (neighbour.type === "op" && MATH_NEIGHBOUR_OPS.has(neighbour.text)) {
        return true;
      }
      if (neighbour.type === "sup") {
        return true;
      }
      if (neighbour.type === "word") {
        const neighbourParts = splitWord(neighbour.text);
        if (FUNCTIONS.has(neighbourParts.core) || IDENTIFIERS.has(neighbourParts.core)) {
          return true;
        }
        if (neighbourParts.sub || neighbourParts.usub || neighbourParts.sup) {
          return true;
        }
      }
    }
    return false;
  }

  function previousMeaningful(tokens, index) {
    for (let cursor = index - 1; cursor >= 0; cursor -= 1) {
      if (tokens[cursor].type !== "space") {
        return tokens[cursor];
      }
    }
    return null;
  }

  function nextMeaningful(tokens, index) {
    for (let cursor = index + 1; cursor < tokens.length; cursor += 1) {
      if (tokens[cursor].type !== "space") {
        return tokens[cursor];
      }
    }
    return null;
  }

  function previousClass(classes, index) {
    for (let cursor = index - 1; cursor >= 0; cursor -= 1) {
      if (classes[cursor] !== null) {
        return classes[cursor];
      }
    }
    return "T";
  }

  function nextClass(classes, index) {
    for (let cursor = index + 1; cursor < classes.length; cursor += 1) {
      if (classes[cursor] !== null) {
        return classes[cursor];
      }
    }
    return "T";
  }

  function findClose(tokens, openIndex) {
    let depth = 0;
    for (let cursor = openIndex; cursor < tokens.length; cursor += 1) {
      if (tokens[cursor].type === "open") {
        depth += 1;
      } else if (tokens[cursor].type === "close") {
        depth -= 1;
        if (depth === 0) {
          return cursor;
        }
      }
    }
    return tokens.length;
  }

  /* ------------------------------------------------------------------
     Segmenting: group tokens into prose and maths runs
     ------------------------------------------------------------------ */

  function segment(text) {
    const tokens = tokenise(text);
    const classes = classify(tokens);
    const segments = [];

    for (let index = 0; index < tokens.length; index += 1) {
      const kind = classes[index] === "M" ? "math" : "text";
      const last = segments[segments.length - 1];
      if (last && last.kind === kind) {
        last.tokens.push(tokens[index]);
      } else {
        segments.push({ kind: kind, tokens: [tokens[index]] });
      }
    }

    // Trim whitespace off the ends of maths runs into the neighbouring text
    const output = [];
    for (const run of segments) {
      if (run.kind === "math") {
        let leading = "";
        let trailing = "";
        while (run.tokens.length && run.tokens[0].type === "space") {
          leading += run.tokens.shift().text;
        }
        while (run.tokens.length && (run.tokens[run.tokens.length - 1].type === "space" || run.tokens[run.tokens.length - 1].type === "punct")) {
          trailing = run.tokens.pop().text + trailing;
        }
        if (leading) {
          pushText(output, leading);
        }
        if (run.tokens.length) {
          output.push({ kind: "math", tokens: run.tokens, text: run.tokens.map(function (token) { return token.text; }).join("") });
        }
        if (trailing) {
          pushText(output, trailing);
        }
      } else {
        pushText(output, run.tokens.map(function (token) { return token.text; }).join(""));
      }
    }

    // A maths run that is just a single plain number inside prose ("the 40 m
    // drop" is fine as maths, but "in 1919" or "six" is not worth rendering)
    return output;
  }

  function pushText(output, text) {
    const last = output[output.length - 1];
    if (last && last.kind === "text") {
      last.text += text;
    } else {
      output.push({ kind: "text", text: text });
    }
  }

  /* ------------------------------------------------------------------
     Maths tokens → TeX
     ------------------------------------------------------------------ */

  function superscriptToAscii(text) {
    const map = { "⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4", "⁵": "5", "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9", "⁻": "-", "⁺": "+" };
    let output = "";
    for (const character of text) {
      output += map[character] !== undefined ? map[character] : character;
    }
    return output;
  }

  function subscriptToAscii(text) {
    const map = { "₀": "0", "₁": "1", "₂": "2", "₃": "3", "₄": "4", "₅": "5", "₆": "6", "₇": "7", "₈": "8", "₉": "9" };
    let output = "";
    for (const character of text) {
      output += map[character] !== undefined ? map[character] : character;
    }
    return output;
  }

  function texSuperscript(supText) {
    if (!supText) {
      return "";
    }
    if (supText === "½") {
      return "^{1/2}";
    }
    const cleaned = supText.replace(/½/g, "");
    return "^{" + superscriptToAscii(cleaned) + "}" + (supText.indexOf("½") >= 0 ? "" : "");
  }

  // Render one unit word, e.g. "m", "s⁻²", "kg", "°C", "MeV/c²"
  function unitToTex(word) {
    const parts = splitWord(word);
    let core = parts.core;
    if (core === "°C") {
      core = "^\\circ C";
    } else if (core === "°") {
      core = "^\\circ";
    } else if (core === "Ω") {
      core = "\\Omega";
    } else if (core === "kΩ") {
      core = "k\\Omega";
    } else if (core === "MΩ") {
      core = "M\\Omega";
    } else if (core === "mΩ") {
      core = "m\\Omega";
    } else {
      core = core.replace(/μ/g, "\\mu ");
    }
    let tex = core;
    if (parts.usub) {
      tex += "_{" + subscriptToAscii(parts.usub) + "}";
    }
    if (parts.sup) {
      tex += "^{" + superscriptToAscii(parts.sup) + "}";
    }
    if (parts.suffix) {
      tex += "/c^{2}";
    }
    return tex;
  }

  // Render one identifier word, e.g. "v", "λ_max", "N_A", "KE_max", "sin", "Q₀", "t½"
  function identifierToTex(word) {
    const parts = splitWord(word);
    let core = parts.core;
    let tex;

    if (FUNCTIONS.has(core)) {
      tex = "\\" + core;
    } else if (core.length === 1) {
      tex = core;
    } else if (IDENTIFIERS.has(core)) {
      tex = "\\mathrm{" + core + "}";
    } else if (/^[ΔδΣ]/.test(core) && core.length <= 3) {
      // Δm, ΔE, Δθ: Greek prefix on a symbol
      tex = core;
    } else {
      // Products of symbols like "mv", "at", "Nm", "GMm", "gt" are rare in the
      // data because they come attached to numbers; render as symbols
      tex = core;
    }

    // Subscripts
    let subscript = "";
    if (parts.usub) {
      subscript = subscriptToAscii(parts.usub);
    } else if (parts.sub) {
      const raw = parts.sub.replace(/^\{|\}$/g, "");
      if (raw.length === 1 || /^\d+$/.test(raw)) {
        subscript = raw;
      } else {
        subscript = "\\mathrm{" + raw + "}";
      }
    }
    if (subscript) {
      tex += "_{" + subscript + "}";
    }

    // Superscripts, including t½
    if (parts.sup) {
      if (parts.sup === "½") {
        tex += "_{1/2}";
      } else {
        tex += "^{" + superscriptToAscii(parts.sup.replace(/½/g, "")) + "}";
      }
    }
    if (parts.prime) {
      tex += "'".repeat(parts.prime.length);
    }
    if (parts.suffix) {
      tex += "/c^{2}";
    }
    return tex;
  }

  // Convert a maths token run into TeX
  function tokensToTex(tokens) {
    // First turn tokens into an intermediate list of TeX atoms, keeping
    // bracket structure so √( ), ^( ) and ( ) / ( ) can be rewritten.
    const atoms = [];
    let index = 0;

    while (index < tokens.length) {
      const token = tokens[index];

      if (token.type === "space") {
        atoms.push({ tex: " ", kind: "space" });
        index += 1;
        continue;
      }

      if (token.type === "num") {
        let tex = token.base;
        if (token.sup) {
          tex += "^{" + superscriptToAscii(token.sup) + "}";
        }
        // Is the next meaningful token a unit? Insert a thin space
        atoms.push({ tex: tex, kind: "num" });
        index += 1;
        continue;
      }

      if (token.type === "word") {
        if (token.isUnit) {
          atoms.push({ tex: unitToTex(token.text), kind: "unit" });
        } else {
          atoms.push({ tex: identifierToTex(token.text), kind: "id" });
        }
        index += 1;
        continue;
      }

      if (token.type === "sup") {
        atoms.push({ tex: "^{" + superscriptToAscii(token.text) + "}", kind: "sup" });
        index += 1;
        continue;
      }

      if (token.type === "op") {
        const character = token.text;
        if (character === "√") {
          // √(...) or √token
          const next = tokens[index + 1];
          if (next && next.type === "open") {
            const closeIndex = findClose(tokens, index + 1);
            const inner = tokensToTex(tokens.slice(index + 2, closeIndex));
            atoms.push({ tex: "\\sqrt{" + inner + "}", kind: "group" });
            index = closeIndex + 1;
          } else if (next) {
            // Take one following atom (number or identifier)
            const single = tokensToTex([next]);
            atoms.push({ tex: "\\sqrt{" + single + "}", kind: "group" });
            index += 2;
          } else {
            atoms.push({ tex: "\\sqrt{}", kind: "group" });
            index += 1;
          }
          continue;
        }
        if (character === "^") {
          const next = tokens[index + 1];
          if (next && next.type === "open") {
            const closeIndex = findClose(tokens, index + 1);
            const inner = tokensToTex(tokens.slice(index + 2, closeIndex));
            atoms.push({ tex: "^{" + inner + "}", kind: "sup" });
            index = closeIndex + 1;
          } else if (next) {
            atoms.push({ tex: "^{" + tokensToTex([next]) + "}", kind: "sup" });
            index += 2;
          } else {
            index += 1;
          }
          continue;
        }
        if (character === "°") {
          atoms.push({ tex: "^\\circ", kind: "sup" });
          index += 1;
          continue;
        }
        atoms.push({ tex: OPERATORS[character], kind: character === "/" ? "slash" : "op", raw: character });
        index += 1;
        continue;
      }

      if (token.type === "open") {
        const closeIndex = findClose(tokens, index);
        const inner = tokensToTex(tokens.slice(index + 1, closeIndex));
        if (closeIndex >= tokens.length) {
          // No matching bracket in this run: write it plainly
          atoms.push({ tex: (token.text === "[" ? "[" : "(") + inner, kind: "group" });
        } else {
          atoms.push({ tex: inner, kind: "paren", left: token.text, right: tokens[closeIndex].text });
        }
        index = closeIndex + 1;
        continue;
      }

      if (token.type === "close") {
        // Unmatched; skip
        index += 1;
        continue;
      }

      if (token.type === "punct") {
        atoms.push({ tex: token.text === "," ? ",\\ " : token.text, kind: "punct" });
        index += 1;
        continue;
      }

      index += 1;
    }

    // Rewrite "A / B" as \frac{A}{B} when either side is a bracketed group.
    // Each side extends over atoms glued together without spaces ("2s", "4πr²").
    const rewritten = [];
    let cursor = 0;
    while (cursor < atoms.length) {
      const atom = atoms[cursor];
      if (atom.kind !== "space") {
        // Numerator: this atom plus following glued atoms up to the slash
        const numeratorEnd = gluedRunEnd(atoms, cursor);
        const slashIndex = skipSpaces(atoms, numeratorEnd);
        const slash = atoms[slashIndex];
        if (slash && slash.kind === "slash") {
          const denominatorStart = skipSpaces(atoms, slashIndex + 1);
          const denominatorEnd = gluedRunEnd(atoms, denominatorStart);
          const numeratorAtoms = atoms.slice(cursor, numeratorEnd);
          const denominatorAtoms = atoms.slice(denominatorStart, denominatorEnd);
          const hasGroup = numeratorAtoms.concat(denominatorAtoms).some(function (candidate) {
            return candidate.kind === "paren" || candidate.kind === "group";
          });
          if (denominatorAtoms.length && hasGroup) {
            rewritten.push({
              tex: "\\frac{" + joinAtoms(numeratorAtoms, true) + "}{" + joinAtoms(denominatorAtoms, true) + "}",
              kind: "group",
            });
            cursor = denominatorEnd;
            continue;
          }
        }
      }
      rewritten.push(atom);
      cursor += 1;
    }

    return joinAtoms(rewritten, false).trim();
  }

  // Index just past the run of atoms glued to atoms[start] with no space
  function gluedRunEnd(atoms, start) {
    let end = start + 1;
    while (end < atoms.length) {
      const kind = atoms[end].kind;
      if (kind === "space" || kind === "op" || kind === "slash" || kind === "punct") {
        break;
      }
      end += 1;
    }
    return end;
  }

  // Join atoms with sensible spacing. Inside a fraction the outer brackets
  // of a single bracketed group are dropped.
  function joinAtoms(atoms, insideFraction) {
    if (insideFraction && atoms.length === 1 && atoms[0].kind === "paren") {
      return atoms[0].tex;
    }
    let tex = "";
    for (let cursor = 0; cursor < atoms.length; cursor += 1) {
      const atom = atoms[cursor];
      const previous = atoms[cursor - 1];

      if (atom.kind === "space") {
        continue;
      }

      let piece = atomToTex(atom);
      const previousKind = lastNonSpaceKind(atoms, cursor);

      // Thin space between a number and a unit, and between units
      if (atom.kind === "unit" && previous) {
        if (previousKind === "unit") {
          piece = "\\," + piece;
        } else if (previousKind === "num" || previousKind === "group" || previousKind === "paren" || previousKind === "sup" || previousKind === "id") {
          piece = "\\ " + piece;
        }
      }

      // Symbols separated by whitespace in the source keep a thin space
      if (previous && previous.kind === "space" && (atom.kind === "id" || atom.kind === "num" || atom.kind === "group")) {
        if (previousKind === "id" || previousKind === "num" || previousKind === "group" || previousKind === "paren" || previousKind === "unit") {
          piece = "\\," + piece;
        }
      }

      tex += piece;
    }
    return tex;
  }

  function atomToTex(atom) {
    if (atom.kind === "paren") {
      const left = atom.left === "[" ? "\\left[" : "\\left(";
      const right = atom.right === "]" ? "\\right]" : "\\right)";
      return left + atom.tex + right;
    }
    if (atom.kind === "unit") {
      return "\\mathrm{" + atom.tex + "}";
    }
    if (atom.kind === "op") {
      return " " + atom.tex + " ";
    }
    return atom.tex;
  }

  function skipSpaces(atoms, index) {
    let cursor = index;
    while (cursor < atoms.length && atoms[cursor].kind === "space") {
      cursor += 1;
    }
    return cursor;
  }

  function lastNonSpaceKind(atoms, index) {
    for (let cursor = index - 1; cursor >= 0; cursor -= 1) {
      if (atoms[cursor].kind !== "space") {
        return atoms[cursor].kind;
      }
    }
    return null;
  }

  /* ------------------------------------------------------------------
     Public API
     ------------------------------------------------------------------ */

  // Convert a string that is entirely maths to TeX
  function toTeX(text) {
    const tokens = tokenise(text);
    // Mark units in an all-maths context
    classify(tokens);
    return tokensToTex(tokens);
  }

  function escapeHtml(text) {
    return String(text)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function renderTex(tex, displayStyle) {
    const katex = getKatex();
    if (!katex) {
      return "<code>" + escapeHtml(tex) + "</code>";
    }
    // Display style gives full-size fractions and roots while staying inline
    const source = displayStyle ? "\\displaystyle " + tex : tex;
    try {
      return katex.renderToString(source, { throwOnError: true, displayMode: false, strict: "ignore" });
    } catch (error) {
      // Fall back to the plain text so nothing is lost
      return "<span class=\"math-fallback\">" + escapeHtml(tex) + "</span>";
    }
  }

  // Render a string that is mostly maths (an equation, a working line).
  // Prose fragments inside it stay as text.
  function renderMath(text, displayStyle) {
    return renderRich(text, displayStyle);
  }

  // Render mixed prose and maths
  function renderRich(text, displayStyle) {
    const parts = segment(text);
    let html = "";
    for (const part of parts) {
      if (part.kind === "math") {
        // Skip rendering a bare integer in prose (years, counts)
        if (/^\d+$/.test(part.text.trim())) {
          html += escapeHtml(part.text);
        } else {
          html += renderTex(tokensToTex(part.tokens), !!displayStyle);
        }
      } else {
        html += escapeHtml(part.text);
      }
    }
    return html;
  }

  // Render a unit on its own ("m s⁻¹", "MeV/c²", "%") upright
  function renderUnit(unit) {
    if (!unit) {
      return "";
    }
    const tokens = tokenise(unit);
    const parts = [];
    for (const token of tokens) {
      if (token.type === "word") {
        parts.push(unitToTex(token.text));
      } else if (token.type === "op" && token.text === "%") {
        parts.push("\\%");
      } else if (token.type === "op" && token.text === "/") {
        parts.push("/");
      } else if (token.type === "num") {
        parts.push(token.base + (token.sup ? "^{" + superscriptToAscii(token.sup) + "}" : ""));
      }
    }
    return renderTex("\\mathrm{" + parts.join("\\,") + "}", false);
  }

  return {
    useKatex: useKatex,
    renderUnit: renderUnit,
    tokenise: tokenise,
    segment: segment,
    toTeX: toTeX,
    renderMath: renderMath,
    renderRich: renderRich,
  };
}));
