/*
 * app.js — The Non-negotiables
 *
 * Loads the topic files, renders the home page, topic pages and search,
 * checks answers, keeps progress in the browser, and builds the print
 * booklet. Maths is rendered by js/richmath.js; drawings by js/figures.js.
 */
(function () {
  "use strict";

  /* ===================================================================
     Constants and state
     =================================================================== */

  // Site configuration: data/config.json overrides these defaults. The
  // "filter" is the segmented control (exam boards for A-level, tiers for
  // GCSE); its option ids are the tags used in the data files' "boards".
  const config = {
    title: "The Non-negotiables",
    titleWords: ["The", "Non-", "negotiables"],
    lede: "The calculations every A-level physicist has to be able to do without thinking. Each one comes with a worked example and six to practise, checked as you go.",
    credit: "Joshua Stafford-Haworth, JSHPhysics",
    printSubtitle: "A-level physics calculations, complete set",
    filter: {
      label: "Exam board",
      prompt: "Show what my board examines",
      all: "All boards",
      options: ["AQA", "OCR A", "OCR B", "Edexcel", "WJEC"],
      defaultOption: "all",
      none: "Nothing in this topic is examined by {option}. Choose another board or another topic.",
    },
  };

  // Filter options in display order; must match the tags in the data files
  let BOARDS = config.filter.options;

  // Fraction of the stored answer within which an entry counts as correct
  const DEFAULT_TOLERANCE = 0.02;

  // All loaded topics, in sidebar order
  let topics = [];

  // Sibling sites (A-level and GCSE) can share one origin, so each page
  // names its own localStorage prefix on <html data-storage="...">
  const STORAGE_PREFIX = document.documentElement.getAttribute("data-storage") || "nn-";

  // Current filter choice: one of BOARDS or "all"
  let board = readStorage(STORAGE_PREFIX + "board") || "all";

  // Merge a loaded config over the defaults and re-derive what depends on it
  function applyConfig(loaded) {
    Object.keys(loaded).forEach(function (key) {
      if (key === "filter" && loaded.filter) {
        Object.assign(config.filter, loaded.filter);
      } else {
        config[key] = loaded[key];
      }
    });
    BOARDS = config.filter.options;
    // A stored choice that the config no longer offers falls back to the default
    const allowed = BOARDS.concat(config.filter.all ? ["all"] : []);
    if (allowed.indexOf(board) < 0) {
      board = config.filter.defaultOption || (config.filter.all ? "all" : BOARDS[0]);
    }
    document.title = config.title;
    const brandName = document.querySelector(".brand span");
    if (brandName) {
      brandName.textContent = config.title;
    }
  }

  // Progress per question id: { status, attempts }
  let progress = readJson(STORAGE_PREFIX + "progress", {});

  // Ids of skill cards (calculation types and sections) the user has collapsed
  let collapsed = new Set(readJson(STORAGE_PREFIX + "collapsed", []));

  // Traffic-light self-check choices: { sectionId: { itemIndex: "r" | "a" | "g" } }
  let selfCheck = readJson(STORAGE_PREFIX + "selfcheck", {});

  // The topic that was last opened, so the home grid can morph back to it
  let lastTopicId = null;

  // Whether the hero's load sequence has already played this session
  let heroPlayed = false;

  const main = document.getElementById("main");

  /* ===================================================================
     Storage helpers (all guarded: storage may be unavailable)
     =================================================================== */

  function readStorage(key) {
    try {
      return localStorage.getItem(key);
    } catch (error) {
      return null;
    }
  }

  function writeStorage(key, value) {
    try {
      localStorage.setItem(key, value);
    } catch (error) {
      // Nothing to do: the value simply will not persist
    }
  }

  function readJson(key, fallback) {
    const raw = readStorage(key);
    if (!raw) {
      return fallback;
    }
    try {
      return JSON.parse(raw);
    } catch (error) {
      return fallback;
    }
  }

  function saveProgress() {
    writeStorage(STORAGE_PREFIX + "progress", JSON.stringify(progress));
  }

  function saveCollapsed() {
    writeStorage(STORAGE_PREFIX + "collapsed", JSON.stringify(Array.from(collapsed)));
  }

  function saveSelfCheck() {
    writeStorage(STORAGE_PREFIX + "selfcheck", JSON.stringify(selfCheck));
  }

  /* ===================================================================
     Data loading
     =================================================================== */

  async function loadAll() {
    // Optional site configuration
    try {
      const configResponse = await fetch("data/config.json");
      if (configResponse.ok) {
        applyConfig(await configResponse.json());
      }
    } catch (error) {
      // No config: the A-level defaults apply
    }

    const manifestResponse = await fetch("data/manifest.json");
    if (!manifestResponse.ok) {
      throw new Error("manifest.json " + manifestResponse.status);
    }
    const manifest = await manifestResponse.json();

    const loads = manifest.topics.map(async function (entry) {
      const response = await fetch("data/" + entry.file);
      if (!response.ok) {
        throw new Error(entry.file + " " + response.status);
      }
      return response.json();
    });

    topics = await Promise.all(loads);
    topics.sort(function (a, b) {
      return a.order - b.order;
    });
  }

  /* ===================================================================
     Board filtering
     =================================================================== */

  function matchesBoard(boardsList) {
    if (board === "all") {
      return true;
    }
    return boardsList.includes(board);
  }

  function questionBoards(question, type) {
    return question.boards || type.boards;
  }

  function visiblePractice(type) {
    return type.practice.filter(function (question) {
      return matchesBoard(questionBoards(question, type));
    });
  }

  function visibleTypes(topic) {
    return topic.types.filter(function (type) {
      return matchesBoard(type.boards) && visiblePractice(type).length > 0;
    });
  }

  // On a tier site, an "H" tag means Higher only: the item is hidden when
  // the Foundation filter is on. Explicit `boards` work as on types.
  function tagsMatchBoard(item) {
    if (item.boards) {
      return matchesBoard(item.boards);
    }
    const higherOnly = config.filter.label === "Tier" && Array.isArray(item.tags) && item.tags.indexOf("H") >= 0;
    if (higherOnly) {
      return matchesBoard(["Higher"]);
    }
    return true;
  }

  // A question inside a section is shown unless its tier excludes it
  function sectionQuestionVisible(question) {
    return tagsMatchBoard(question);
  }

  // A whole section can be Higher only too
  function sectionVisible(section) {
    return tagsMatchBoard(section);
  }

  /* ===================================================================
     Sections, bands and key facts
     A topic may carry, beside its calculation types, revision content:
       topic.bands    — [{ id, prefix, title, blurb }]
       topic.sections — [{ id, band, title, spec, tags, equations, blurb,
                           parts, checklist }]
       topic.facts    — [{ q, a, section }] flip cards, shown last
     A section's parts are explain / worked / practice / types (embedded
     calculation types by id) / facts. Topics without sections render
     exactly as before, so the A-level site is untouched.
     =================================================================== */

  function hasSections(topic) {
    return Array.isArray(topic.sections) && topic.sections.length > 0;
  }

  // The sections the current filter leaves visible, in order
  function topicSections(topic) {
    if (!hasSections(topic)) {
      return [];
    }
    return topic.sections.filter(sectionVisible);
  }

  function findSection(topic, sectionId) {
    return topicSections(topic).find(function (section) {
      return section.id === sectionId;
    }) || null;
  }

  // The calculation types a section embeds, in order
  function sectionTypes(topic, section) {
    const found = [];
    (section.parts || []).forEach(function (part) {
      if (part.kind !== "types") {
        return;
      }
      part.ids.forEach(function (typeId) {
        const type = topic.types.find(function (candidate) {
          return candidate.id === typeId;
        });
        if (type) {
          found.push(type);
        }
      });
    });
    return found;
  }

  // Calculation types no section embeds (shown in a band of their own)
  function unplacedTypes(topic) {
    const placed = new Set();
    topicSections(topic).forEach(function (section) {
      sectionTypes(topic, section).forEach(function (type) {
        placed.add(type.id);
      });
    });
    return topic.types.filter(function (type) {
      return !placed.has(type.id);
    });
  }

  // Every markable question a section carries itself, flattening groups
  function leafQuestions(section) {
    const leaves = [];
    (section.parts || []).forEach(function (part) {
      if (part.kind !== "practice") {
        return;
      }
      part.questions.forEach(function (question) {
        if (question.type === "group") {
          question.parts.forEach(function (child) {
            leaves.push(child);
          });
        } else {
          leaves.push(question);
        }
      });
    });
    return leaves.filter(sectionQuestionVisible);
  }

  // Band helpers (a topic with sections but no bands has one unnamed band)
  function bandOf(topic, section) {
    if (!topic.bands || !section.band) {
      return null;
    }
    return topic.bands.find(function (band) {
      return band.id === section.band;
    }) || null;
  }

  // The label on a section card: "N3" inside a band, or "3" without bands
  function sectionLabel(topic, index) {
    const sections = topicSections(topic);
    const section = sections[index];
    const band = bandOf(topic, section);
    if (!band) {
      return String(index + 1);
    }
    let position = 0;
    for (let cursor = 0; cursor <= index; cursor += 1) {
      if (sections[cursor].band === section.band) {
        position += 1;
      }
    }
    return (band.prefix || "") + position;
  }

  function startsBand(topic, index) {
    const sections = topicSections(topic);
    const section = sections[index];
    const band = bandOf(topic, section);
    if (!band) {
      return false;
    }
    if (index === 0) {
      return true;
    }
    return sections[index - 1].band !== section.band;
  }

  function bandHeadHtml(band) {
    let html = "<div class=\"band-head\" id=\"band-" + escapeHtml(band.id) + "\">";
    html += "<h3>" + escapeHtml(band.title) + "</h3>";
    if (band.blurb) {
      html += "<p>" + prose(band.blurb) + "</p>";
    }
    html += "</div>";
    return html;
  }

  // Small badges: "H" for Higher-tier only, "P" for separate Physics only
  function tagBadges(tags) {
    if (!tags || tags.length === 0) {
      return "";
    }
    let html = "";
    tags.forEach(function (tag) {
      const title = tag === "H" ? "Higher tier only" : (tag === "P" ? "Separate Physics only (not Combined Science)" : tag);
      html += "<span class=\"badge badge-" + escapeHtml(tag.toLowerCase()) + "\" title=\"" + escapeHtml(title) + "\">" + escapeHtml(tag) + "</span>";
    });
    return html;
  }

  // A calculation type's badges: its own tags, plus H when it is Higher-only
  function typeTags(type) {
    const tags = (type.tags || []).slice();
    const tierSite = config.filter.label === "Tier";
    if (tierSite && type.boards.length === 1 && type.boards[0] === "Higher" && tags.indexOf("H") < 0) {
      tags.unshift("H");
    }
    return tags;
  }

  /* ===================================================================
     Lookups
     =================================================================== */

  function findTopic(topicId) {
    return topics.find(function (topic) {
      return topic.id === topicId;
    }) || null;
  }

  function findType(typeId) {
    for (const topic of topics) {
      for (const type of topic.types) {
        if (type.id === typeId) {
          return type;
        }
      }
    }
    return null;
  }

  function findQuestion(questionId) {
    for (const topic of topics) {
      for (const type of topic.types) {
        for (const question of type.practice) {
          if (question.id === questionId) {
            return question;
          }
        }
      }
      for (const section of topicSections(topic)) {
        for (const part of section.parts || []) {
          if (part.kind !== "practice") {
            continue;
          }
          for (const question of part.questions) {
            if (question.id === questionId) {
              return question;
            }
            if (question.type === "group") {
              for (const child of question.parts) {
                if (child.id === questionId) {
                  return child;
                }
              }
            }
          }
        }
      }
    }
    return null;
  }

  /* ===================================================================
     Progress summaries
     =================================================================== */

  function isCorrect(questionId) {
    const state = progress[questionId];
    return !!state && state.status === "correct";
  }

  function typeProgress(type) {
    const questions = visiblePractice(type);
    let correct = 0;
    for (const question of questions) {
      if (isCorrect(question.id)) {
        correct += 1;
      }
    }
    return { correct: correct, total: questions.length };
  }

  // A section's own questions plus those of the types it embeds
  function sectionProgress(topic, section) {
    let correct = 0;
    let total = 0;
    for (const question of leafQuestions(section)) {
      total += 1;
      if (isCorrect(question.id)) {
        correct += 1;
      }
    }
    for (const type of sectionTypes(topic, section)) {
      if (!matchesBoard(type.boards)) {
        continue;
      }
      const summary = typeProgress(type);
      correct += summary.correct;
      total += summary.total;
    }
    return { correct: correct, total: total };
  }

  function topicProgress(topic) {
    let correct = 0;
    let total = 0;
    for (const type of visibleTypes(topic)) {
      const summary = typeProgress(type);
      correct += summary.correct;
      total += summary.total;
    }
    for (const section of topicSections(topic)) {
      for (const question of leafQuestions(section)) {
        total += 1;
        if (isCorrect(question.id)) {
          correct += 1;
        }
      }
    }
    return { correct: correct, total: total };
  }

  // A topic appears on the home grid when the filter leaves it something to show
  function topicVisible(topic) {
    return hasSections(topic) || visibleTypes(topic).length > 0 || !!topic.placeholder;
  }

  function levelLabel(question) {
    const index = Number(question.id.split("-p")[1]) - 1;
    if (index < 2) {
      return "direct";
    }
    if (index < 4) {
      return "rearrange";
    }
    return "two-step";
  }

  /* ===================================================================
     Answer parsing and checking
     =================================================================== */

  const SUPERSCRIPTS = {
    "⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4",
    "⁵": "5", "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9",
    "⁻": "-", "⁺": "+",
  };

  // Turn whatever the student typed into a number, or NaN
  function parseEntry(text) {
    let cleaned = "";
    for (const character of text) {
      cleaned += SUPERSCRIPTS[character] !== undefined ? SUPERSCRIPTS[character] : character;
    }
    cleaned = cleaned.replace(/[\s,]/g, "").replace(/%$/, "");
    cleaned = cleaned.replace(/−/g, "-");
    cleaned = cleaned.replace(/[×xX*]10\^?/g, "e");
    cleaned = cleaned.replace(/^10\^/, "1e");
    if (/^e/.test(cleaned)) {
      return NaN;
    }
    return Number(cleaned);
  }

  // Compare an entry with the stored answer
  function checkEntry(entered, answer) {
    const target = answer.value;
    const tolerance = answer.tolerance || DEFAULT_TOLERANCE;

    if (target === 0) {
      return { result: Math.abs(entered) < 1e-9 ? "correct" : "wrong", factor: null };
    }

    const relativeError = Math.abs(entered - target) / Math.abs(target);
    if (relativeError <= tolerance) {
      return { result: "correct", factor: null };
    }

    // A power-of-ten slip usually means a unit conversion error
    if (entered !== 0 && Math.sign(entered) === Math.sign(target)) {
      const exponent = Math.log10(Math.abs(entered / target));
      const nearest = Math.round(exponent);
      const close = Math.abs(exponent - nearest) < Math.log10(1 + tolerance);
      if (close && nearest !== 0 && Math.abs(nearest) <= 12) {
        return { result: "wrong", factor: nearest };
      }
    }

    // A sign slip
    if (entered !== 0 && Math.sign(entered) !== Math.sign(target)) {
      const magnitudeMatches = Math.abs(Math.abs(entered) - Math.abs(target)) / Math.abs(target) <= tolerance;
      if (magnitudeMatches) {
        return { result: "wrong", factor: "sign" };
      }
    }

    return { result: "wrong", factor: null };
  }

  function wrongMessage(factor, attempts) {
    if (factor === "sign") {
      return "Right size, wrong sign. Check which direction is positive.";
    }
    if (typeof factor === "number") {
      const magnitude = Math.pow(10, Math.abs(factor));
      const direction = factor > 0 ? "too big" : "too small";
      const pretty = magnitude >= 1000 ? magnitude.toLocaleString("en-GB") : String(magnitude);
      return "Out by a factor of " + pretty + ", " + direction + ". Check a unit conversion.";
    }
    if (attempts >= 2) {
      return "Not yet. Try the hint, or open the walkthrough.";
    }
    return "Not quite. Check the rearrangement and try again.";
  }

  // Format a stored value for display, e.g. 6.25 × 10¹³
  function formatValue(value) {
    const magnitude = Math.abs(value);
    if (magnitude !== 0 && (magnitude >= 1e5 || magnitude < 1e-3)) {
      const exponent = Math.floor(Math.log10(magnitude));
      const mantissa = value / Math.pow(10, exponent);
      const mantissaText = Number(mantissa.toPrecision(3)).toString();
      return mantissaText + " × 10" + toSuperscript(exponent);
    }
    return Number(value.toPrecision(3)).toString();
  }

  function toSuperscript(number) {
    const digits = { "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹", "-": "⁻" };
    let output = "";
    for (const character of String(number)) {
      output += digits[character];
    }
    return output;
  }

  /* ===================================================================
     Rendering helpers
     =================================================================== */

  function escapeHtml(text) {
    return String(text)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  // Prose with maths inside it
  function rich(text) {
    return richmath.renderRich(text);
  }

  // A working line or an equation: display-size fractions and roots
  function math(text) {
    return richmath.renderMath(text, true);
  }

  // Revision content is authored as HTML with TeX between $…$ (inline)
  // or $$…$$ (display), unlike the calculation types' plain-text notation
  function tex(source, displayMode) {
    try {
      return katex.renderToString(source, { displayMode: displayMode, throwOnError: false, strict: "ignore" });
    } catch (error) {
      return "<code class=\"math-fallback\">" + escapeHtml(source) + "</code>";
    }
  }

  function prose(text) {
    if (!text) {
      return "";
    }
    // Display maths first, so its dollars are not eaten by the inline pass
    let output = String(text).replace(/\$\$([\s\S]+?)\$\$/g, function (match, source) {
      return "<div class=\"math-display\">" + tex(source, true) + "</div>";
    });
    output = output.replace(/\$([^$\n]+?)\$/g, function (match, source) {
      return tex(source, false);
    });
    return output;
  }

  // Text of a question, whichever schema it uses
  function questionText(question) {
    return question.text !== undefined ? question.text : question.question;
  }

  // An answer value with its unit
  function answerHtml(answer) {
    const unit = answer.unit ? " " + answer.unit : "";
    return math(formatValue(answer.value) + unit);
  }

  // A graph from a question's spec, with KaTeX axis titles
  function graphHtml(spec, extraClass) {
    if (!spec) {
      return "";
    }
    const drawn = graphs.render(spec);
    return "<figure class=\"graph" + (extraClass ? " " + extraClass : "") + "\">" +
      "<div class=\"ylabel\"><span>" + rich(drawn.yLabel) + "</span></div>" +
      drawn.svg +
      "<div class=\"xlabel\">" + rich(drawn.xLabel) + "</div>" +
      "</figure>";
  }

  function icon(name) {
    if (name === "chev") {
      return "<svg class=\"chev\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" aria-hidden=\"true\"><path d=\"M6 9l6 6 6-6\"/></svg>";
    }
    if (name === "back") {
      return "<svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" aria-hidden=\"true\"><path d=\"M15 6l-6 6 6 6\"/></svg>";
    }
    if (name === "tick") {
      return "<svg class=\"tick\" viewBox=\"0 0 24 24\" aria-hidden=\"true\"><path d=\"M5 12.5l4.5 4.5L19 7\"/></svg>";
    }
    return "";
  }

  function ringHtml(summary) {
    const percent = summary.total ? Math.round((summary.correct / summary.total) * 100) : 0;
    return "<span class=\"ring\" style=\"--p: " + percent + "\" aria-label=\"" + summary.correct + " of " + summary.total + " correct\">" +
      "<svg viewBox=\"0 0 40 40\"><circle class=\"track\" cx=\"20\" cy=\"20\" r=\"15.9\"/><circle class=\"fillc\" cx=\"20\" cy=\"20\" r=\"15.9\"/></svg>" +
      "<span class=\"txt\">" + summary.correct + "/" + summary.total + "</span></span>";
  }

  /* ===================================================================
     Board picker
     =================================================================== */

  function renderBoardPicker(container) {
    container.innerHTML = "";
    const options = (config.filter.all ? ["all"] : []).concat(BOARDS);
    for (const option of options) {
      const button = document.createElement("button");
      button.type = "button";
      button.textContent = option === "all" ? config.filter.all : option;
      button.setAttribute("aria-pressed", board === option ? "true" : "false");
      button.addEventListener("click", function () {
        board = option;
        writeStorage(STORAGE_PREFIX + "board", board);
        renderBoardPicker(document.getElementById("board-seg"));
        const heroPicker = document.getElementById("hero-seg");
        if (heroPicker) {
          renderBoardPicker(heroPicker);
        }
        renderRoute(false);
      });
      container.appendChild(button);
    }
  }

  /* ===================================================================
     Views: home
     =================================================================== */

  function renderHome() {
    const totalTypes = topics.reduce(function (sum, topic) {
      return sum + visibleTypes(topic).length;
    }, 0);
    const totalQuestions = topics.reduce(function (sum, topic) {
      return sum + visibleTypes(topic).reduce(function (inner, type) {
        return inner + visiblePractice(type).length;
      }, 0);
    }, 0);

    const words = config.titleWords;
    let title = "";
    words.forEach(function (word, index) {
      title += "<span class=\"word\"><span style=\"--i: " + index + "\">" + word + "</span></span>";
      if (index === 0) {
        title += " ";
      }
    });

    let html = "";
    html += "<section class=\"hero" + (heroPlayed ? "" : " animate") + "\">";
    html += "<h1>" + title + "</h1>";
    html += "<div class=\"dimline\"><span class=\"tag\">" + totalTypes + " calculations</span><span class=\"rule\"></span><span class=\"tag tag-end\">" + totalQuestions + " questions</span></div>";
    html += "<p class=\"lede\">" + escapeHtml(config.lede) + "</p>";
    html += "<div class=\"hero-controls\"><span class=\"label\">" + escapeHtml(config.filter.prompt) + "</span><div class=\"seg\" id=\"hero-seg\" role=\"group\" aria-label=\"" + escapeHtml(config.filter.label) + "\"></div></div>";
    html += "</section>";

    html += "<section class=\"topics\" aria-label=\"Topics\">";
    topics.forEach(function (topic, index) {
      const types = visibleTypes(topic);
      if (!topicVisible(topic)) {
        return;
      }
      const summary = topicProgress(topic);
      const percent = summary.total ? (summary.correct / summary.total) * 100 : 0;
      const done = summary.total > 0 && summary.correct === summary.total;
      const shared = topic.id === lastTopicId ? " shared" : "";
      const sectionCount = topicSections(topic).length;
      html += "<a class=\"topic-card" + (done ? " done" : "") + "\" href=\"#" + topic.id + "\" data-topic=\"" + topic.id + "\" style=\"--i: " + index + "\">";
      html += "<div class=\"figwrap" + shared + "\">" + figures.render(topic.figure || topic.id) + "</div>";
      html += "<div class=\"meta corner-ticks\">";
      if (topic.spec) {
        html += "<span class=\"spec-kicker\">" + escapeHtml(topic.spec) + "</span>";
      }
      html += "<h3>" + escapeHtml(topic.title) + "</h3>";
      html += "<p class=\"sub\">" + escapeHtml(topic.subtitle) + "</p>";
      let statsText = "";
      if (sectionCount > 0) {
        statsText += sectionCount + " section" + (sectionCount === 1 ? "" : "s") + " · ";
      }
      statsText += types.length + " calculation" + (types.length === 1 ? "" : "s");
      if (sectionCount === 0 && types.length === 0 && topic.placeholder) {
        statsText = "notes on the way";
      }
      html += "<div class=\"stats\"><span>" + statsText + "</span><span>" + (summary.total > 0 ? summary.correct + " of " + summary.total + " correct" : "") + "</span></div>";
      html += "<div class=\"bar\"><i style=\"--p: " + percent.toFixed(1) + "%\"></i></div>";
      html += "</div></a>";
    });
    html += "</section>";

    html += footerHtml();
    main.innerHTML = html;
    document.body.classList.add("is-home");

    renderBoardPicker(document.getElementById("hero-seg"));
    heroPlayed = true;
    watchCards();
    wireTopicCards();
    lastTopicId = null;
  }

  // Figures on cards run only while on screen
  function watchCards() {
    const cards = main.querySelectorAll(".topic-card");
    if (!("IntersectionObserver" in window)) {
      cards.forEach(function (card) {
        card.classList.add("in-view");
      });
      return;
    }
    const observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        entry.target.classList.toggle("in-view", entry.isIntersecting);
      });
    }, { rootMargin: "80px 0px" });
    cards.forEach(function (card) {
      observer.observe(card);
    });
  }

  // Mark the clicked card's figure as the shared element for the transition
  function wireTopicCards() {
    main.querySelectorAll(".topic-card").forEach(function (card) {
      card.addEventListener("click", function () {
        main.querySelectorAll(".figwrap.shared").forEach(function (element) {
          element.classList.remove("shared");
        });
        card.querySelector(".figwrap").classList.add("shared");
      });
    });
  }

  /* ===================================================================
     Views: topic
     =================================================================== */

  // Topics the user has opened before; on a first visit every skill but the
  // first starts collapsed so the page is scannable
  let seenTopics = new Set(readJson(STORAGE_PREFIX + "seen", []));

  function applyFirstVisitDefaults(topic, cards, openId) {
    if (seenTopics.has(topic.id)) {
      return;
    }
    seenTopics.add(topic.id);
    writeStorage(STORAGE_PREFIX + "seen", JSON.stringify(Array.from(seenTopics)));
    cards.forEach(function (card, index) {
      const keepOpen = index === 0 || card.id === openId;
      if (!keepOpen) {
        collapsed.add(card.id);
      }
    });
    saveCollapsed();
  }

  // The collapsible cards on a topic page, in order: sections when the
  // topic has them (with any unplaced types after), else the types
  function topicCards(topic) {
    if (!hasSections(topic)) {
      return visibleTypes(topic);
    }
    return topicSections(topic).concat(unplacedTypes(topic).filter(function (type) {
      return matchesBoard(type.boards) && visiblePractice(type).length > 0;
    }));
  }

  function renderTopic(topic, cardId) {
    document.body.classList.remove("is-home");
    const types = visibleTypes(topic);
    const cards = topicCards(topic);
    applyFirstVisitDefaults(topic, cards, cardId);
    const summary = topicProgress(topic);
    const percent = summary.total ? (summary.correct / summary.total) * 100 : 0;
    const index = topics.indexOf(topic);
    const previous = neighbourTopic(index, -1);
    const next = neighbourTopic(index, 1);

    let html = "";
    html += "<nav class=\"crumbs\"><a href=\"#\">" + icon("back") + "All topics</a></nav>";

    html += "<header class=\"cover\">";
    html += "<div>";
    if (topic.spec) {
      html += "<span class=\"spec-kicker\">" + escapeHtml(topic.spec) + "</span>";
    }
    html += "<h2>" + escapeHtml(topic.title) + "</h2>";
    html += "<p class=\"sub\">" + escapeHtml(topic.subtitle) + "</p>";
    html += "<div class=\"progress-line\"><span>" + summary.correct + " of " + summary.total + " questions correct" + (board === "all" ? "" : " for " + escapeHtml(board)) + "</span><div class=\"bar\"><i style=\"--p: " + percent.toFixed(1) + "%\"></i></div></div>";
    if (topic.lede) {
      html += "<p class=\"lede\">" + prose(topic.lede) + "</p>";
    }
    if (topic.howto && topic.howto.length > 0) {
      html += "<details class=\"howto\"><summary>" + icon("chev") + "How to use this topic</summary><ol class=\"list\">";
      topic.howto.forEach(function (line) {
        html += "<li>" + prose(line) + "</li>";
      });
      html += "</ol></details>";
    }
    html += "</div>";
    html += "<div class=\"figwrap shared\">" + figures.render(topic.figure || topic.id) + "</div>";
    html += "</header>";

    if (hasSections(topic)) {
      html += renderSectionsBody(topic);
    } else if (types.length === 0 && topic.placeholder && topic.types.length === 0) {
      html += "<div class=\"notice\">" + prose(topic.placeholder) + "</div>";
    } else if (types.length === 0) {
      html += "<div class=\"notice\">" + escapeHtml(config.filter.none.replace("{option}", board)) + "</div>";
    } else {
      html += "<div class=\"skillbar\"><div class=\"pills\">";
      types.forEach(function (type, typeIndex) {
        const typeSummary = typeProgress(type);
        const done = typeSummary.total > 0 && typeSummary.correct === typeSummary.total;
        html += "<a class=\"pill" + (done ? " done" : "") + "\" href=\"#" + topic.id + "/" + type.id + "\" data-pill=\"" + type.id + "\"><span class=\"n\">" + (typeIndex + 1) + "</span>" + escapeHtml(type.name) + "</a>";
      });
      html += "</div><div class=\"tools\"><button class=\"btn quiet small\" id=\"btn-expand-all\">Expand all</button><button class=\"btn quiet small\" id=\"btn-collapse-all\">Collapse all</button></div></div>";

      html += "<div class=\"skills\">";
      types.forEach(function (type, typeIndex) {
        html += renderSkill(topic, type, String(typeIndex + 1), false);
      });
      html += "</div>";
    }

    html += "<nav class=\"topic-nav\" aria-label=\"Neighbouring topics\">";
    html += previous ? "<a class=\"prev\" href=\"#" + previous.id + "\"><span class=\"dir\">Previous topic</span><span class=\"name\">" + escapeHtml(previous.title) + "</span></a>" : "<span></span>";
    html += next ? "<a class=\"next\" href=\"#" + next.id + "\"><span class=\"dir\">Next topic</span><span class=\"name\">" + escapeHtml(next.title) + "</span></a>" : "<span></span>";
    html += "</nav>";

    html += footerHtml();
    main.innerHTML = html;

    wireSkills(main);
    lastTopicId = topic.id;

    const expandAll = document.getElementById("btn-expand-all");
    const collapseAll = document.getElementById("btn-collapse-all");
    if (expandAll) {
      expandAll.addEventListener("click", function () {
        setAllCollapsed(cards, false);
      });
      collapseAll.addEventListener("click", function () {
        setAllCollapsed(cards, true);
      });
    }

    if (cardId) {
      const target = cardElement(cardId);
      if (target) {
        // A type embedded in a section needs the section open as well
        const outer = target.parentElement ? target.parentElement.closest(".skill") : null;
        if (outer) {
          setCollapsed(outer.getAttribute("data-card"), false);
        }
        setCollapsed(cardId, false);
        requestAnimationFrame(function () {
          target.scrollIntoView({ block: "start" });
        });
      }
    }
  }

  // The pills, band headings, section cards, unplaced types and key facts
  function renderSectionsBody(topic) {
    const sections = topicSections(topic);
    const extras = unplacedTypes(topic).filter(function (type) {
      return matchesBoard(type.boards) && visiblePractice(type).length > 0;
    });

    let html = "";
    html += "<div class=\"skillbar\"><div class=\"pills\">";
    sections.forEach(function (section, sectionIndex) {
      const summary = sectionProgress(topic, section);
      const done = summary.total > 0 && summary.correct === summary.total;
      if (startsBand(topic, sectionIndex)) {
        html += "<span class=\"pill-band\">" + escapeHtml(bandOf(topic, section).title) + "</span>";
      }
      html += "<a class=\"pill" + (done ? " done" : "") + "\" href=\"#" + topic.id + "/" + section.id + "\" data-pill=\"" + section.id + "\"><span class=\"n\">" + sectionLabel(topic, sectionIndex) + "</span>" + escapeHtml(section.title) + "</a>";
    });
    if (extras.length > 0) {
      html += "<span class=\"pill-band\">Calculations</span>";
      extras.forEach(function (type, typeIndex) {
        const summary = typeProgress(type);
        const done = summary.total > 0 && summary.correct === summary.total;
        html += "<a class=\"pill" + (done ? " done" : "") + "\" href=\"#" + topic.id + "/" + type.id + "\" data-pill=\"" + type.id + "\"><span class=\"n\">C" + (typeIndex + 1) + "</span>" + escapeHtml(type.name) + "</a>";
      });
    }
    if (topic.facts && topic.facts.length > 0) {
      html += "<span class=\"pill-band\">Key facts</span>";
      html += "<a class=\"pill\" href=\"#" + topic.id + "/key-facts\" data-pill=\"key-facts\"><span class=\"n\">K</span>Flashcards</a>";
    }
    html += "</div><div class=\"tools\"><button class=\"btn quiet small\" id=\"btn-expand-all\">Expand all</button><button class=\"btn quiet small\" id=\"btn-collapse-all\">Collapse all</button></div></div>";

    html += "<div class=\"skills\">";
    sections.forEach(function (section, sectionIndex) {
      if (startsBand(topic, sectionIndex)) {
        html += bandHeadHtml(bandOf(topic, section));
      }
      html += renderSection(topic, section, sectionIndex);
    });
    if (extras.length > 0) {
      html += bandHeadHtml({ id: "calculations", title: "Calculations", blurb: "Calculation practice not yet placed in a section above." });
      extras.forEach(function (type, typeIndex) {
        html += renderSkill(topic, type, "C" + (typeIndex + 1), false);
      });
    }
    if (topic.facts && topic.facts.length > 0) {
      html += bandHeadHtml({ id: "key-facts", title: "Key facts", blurb: topic.factsBlurb || "The whole topic on flip cards. Cover, say the answer out loud, then flip to check." });
      html += renderFacts(topic);
    }
    html += "</div>";
    return html;
  }

  // The flashcards: a flip-card grid with shuffle and show-all controls
  function renderFacts(topic) {
    let html = "<article class=\"skill facts-card\" id=\"card-key-facts\" data-card=\"key-facts\">";
    html += "<div class=\"skill-body\"><div class=\"inner\"><div class=\"skill-content\">";
    html += "<section class=\"facts\"><div class=\"facts-bar\"><span class=\"practice-kicker\">" + topic.facts.length + " cards</span>";
    html += "<span class=\"facts-tools\"><button class=\"btn small\" type=\"button\" data-facts-shuffle>Shuffle</button><button class=\"btn small\" type=\"button\" data-facts-flip>Show all answers</button></span></div>";
    html += "<p class=\"practice-intro\">Tap a card to flip it. Say the answer out loud before you look — reading it is not the same as knowing it.</p>";
    html += "<div class=\"fact-grid\" data-fact-grid>";
    topic.facts.forEach(function (item, itemIndex) {
      html += "<button class=\"fact\" type=\"button\" aria-pressed=\"false\" data-fact data-fact-index=\"" + itemIndex + "\">" +
        "<span class=\"fact-q\"><span class=\"n\">" + (itemIndex + 1) + "</span>" + prose(item.q) + "</span>" +
        "<span class=\"fact-a\">" + prose(item.a) + "</span></button>";
    });
    html += "</div></section>";
    html += "</div></div></div></article>";
    return html;
  }

  // The cover drawing drifts up and fades as the page scrolls past it
  let parallaxTicking = false;

  function onScrollParallax() {
    if (parallaxTicking) {
      return;
    }
    parallaxTicking = true;
    requestAnimationFrame(function () {
      parallaxTicking = false;
      const figure = document.querySelector(".cover .figwrap");
      if (!figure) {
        return;
      }
      const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      if (reduced) {
        return;
      }
      const offset = Math.min(window.scrollY, 600);
      figure.style.transform = "translateY(" + (offset * 0.22).toFixed(1) + "px)";
      figure.style.opacity = String(Math.max(0, 1 - offset / 520));
    });
  }

  function neighbourTopic(index, direction) {
    let cursor = index + direction;
    while (cursor >= 0 && cursor < topics.length) {
      if (topicVisible(topics[cursor])) {
        return topics[cursor];
      }
      cursor += direction;
    }
    return null;
  }

  function footerHtml() {
    return "<footer class=\"site-foot\"><span>" + escapeHtml(config.title) + "</span><span>" + escapeHtml(config.credit) + "</span></footer>";
  }

  /* ===================================================================
     Skill cards
     =================================================================== */

  // A calculation type card. `label` is the number shown on the left;
  // `embedded` is true when the card sits inside a section card.
  function renderSkill(topic, type, label, embedded) {
    const summary = typeProgress(type);
    const isCollapsed = collapsed.has(type.id);
    const questions = visiblePractice(type);

    let html = "";
    html += "<article class=\"skill type-card" + (embedded ? " embedded" : "") + (isCollapsed ? " collapsed" : "") + "\" id=\"skill-" + type.id + "\" data-type=\"" + type.id + "\" data-card=\"" + type.id + "\">";

    // Header row (click to collapse)
    html += "<button class=\"skill-head\" type=\"button\" aria-expanded=\"" + (isCollapsed ? "false" : "true") + "\" aria-controls=\"body-" + type.id + "\">";
    html += "<span class=\"num\">" + escapeHtml(label) + "</span>";
    html += "<span><span class=\"skill-title\">" + escapeHtml(type.name) + "</span> " + tagBadges(typeTags(type)) + " <span class=\"eq-preview\">" + rich(type.equations[0]) + "</span></span>";
    html += ringHtml(summary);
    html += icon("chev");
    html += "</button>";

    // Body
    html += "<div class=\"skill-body\" id=\"body-" + type.id + "\"><div class=\"inner\"><div class=\"skill-content\">";

    html += "<div class=\"formulas\">";
    type.equations.forEach(function (equation) {
      html += "<span class=\"formula\">" + math(equation) + "</span>";
    });
    html += "</div>";

    html += "<p class=\"method\">" + rich(type.method) + "</p>";

    html += "<details class=\"errors\"><summary>" + icon("chev") + "Where marks get lost</summary><ul>";
    type.commonErrors.forEach(function (error) {
      html += "<li>" + rich(error) + "</li>";
    });
    html += "</ul></details>";

    // Worked example: steps revealed one at a time
    html += "<section class=\"worked\" data-worked=\"" + type.id + "\">";
    html += "<span class=\"kicker\">Worked example</span>";
    html += "<p class=\"q\">" + rich(type.worked.question) + "</p>";
    html += graphHtml(type.worked.graph);
    html += "<ol class=\"steps\">";
    type.worked.steps.forEach(function (step, stepIndex) {
      html += "<li class=\"" + (stepIndex === 0 ? "" : "hidden-step") + "\"><span>" + math(step) + "</span></li>";
    });
    html += "</ol>";
    html += "<div class=\"controls\"><button class=\"btn small\" data-next-step>Next step</button><button class=\"btn quiet small\" data-all-steps>Show all</button></div>";
    html += "</section>";

    // Practice
    html += "<section class=\"practice\"><span class=\"practice-kicker\">Practise</span>";
    questions.forEach(function (question, questionIndex) {
      html += renderTypeQuestion(question, questionIndex);
    });
    html += "</section>";

    html += "</div></div></div></article>";
    return html;
  }

  // A practice question belonging to a calculation type (plain-text
  // notation, always numeric)
  function renderTypeQuestion(question, index) {
    const correct = isCorrect(question.id);
    let html = "";
    html += "<div class=\"question" + (correct ? " correct" : "") + "\" data-qid=\"" + question.id + "\">";
    html += "<div class=\"q-top\"><span class=\"qn\">" + (index + 1) + "</span><span class=\"level\">" + levelLabel(question) + "</span>";
    if (question.boards) {
      question.boards.forEach(function (tag) {
        html += "<span class=\"level narrow\">" + escapeHtml(tag) + "</span>";
      });
    }
    html += "</div>";
    html += "<p class=\"q-text\">" + rich(question.question) + "</p>";
    html += graphHtml(question.graph);

    html += "<div class=\"answer-row\">";
    html += "<label class=\"answer-field\"><span class=\"visually-hidden\">Your answer</span>";
    html += "<input type=\"text\" inputmode=\"text\" placeholder=\"your answer\" data-input" + (correct ? " value=\"" + escapeHtml(formatValue(question.answer.value)) + "\"" : "") + ">";
    html += "<span class=\"unit\">" + richmath.renderUnit(question.answer.unit) + "</span>";
    html += "</label>";
    html += "<button class=\"btn solid\" data-check>Check</button>";
    html += "</div>";

    html += feedbackHtml(correct);

    html += "<div class=\"help\">";
    html += "<button class=\"btn small\" data-toggle=\"hint\" aria-expanded=\"false\">Hint</button>";
    html += "<button class=\"btn small\" data-toggle=\"walkthrough\" aria-expanded=\"false\">Walkthrough</button>";
    html += "<button class=\"btn small\" data-toggle=\"answer\" aria-expanded=\"false\">Answer</button>";
    html += "</div>";

    html += "<div class=\"panels\">";
    html += "<div class=\"panel hint\" data-panel=\"hint\"><div class=\"inner\"><div class=\"box\"><span class=\"kicker\">Hint</span>" + rich(question.hint) + "</div></div></div>";
    html += "<div class=\"panel walkthrough\" data-panel=\"walkthrough\"><div class=\"inner\"><div class=\"box\"><span class=\"kicker\">Walkthrough</span><ol class=\"steps\">";
    question.walkthrough.forEach(function (line) {
      html += "<li><span>" + math(line) + "</span></li>";
    });
    html += "</ol></div></div></div>";
    html += "<div class=\"panel answer\" data-panel=\"answer\"><div class=\"inner\"><div class=\"box\"><span class=\"kicker\">Answer</span>" + answerHtml(question.answer) + "</div></div></div>";
    html += "</div>";

    html += "</div>";
    return html;
  }

  /* ===================================================================
     Section cards (revision content)
     =================================================================== */

  function renderSection(topic, section, index) {
    const summary = sectionProgress(topic, section);
    const isCollapsed = collapsed.has(section.id);

    let html = "";
    html += "<article class=\"skill section-card" + (isCollapsed ? " collapsed" : "") + "\" id=\"section-" + section.id + "\" data-section=\"" + section.id + "\" data-card=\"" + section.id + "\">";

    // Header row (click to collapse)
    html += "<button class=\"skill-head\" type=\"button\" aria-expanded=\"" + (isCollapsed ? "false" : "true") + "\" aria-controls=\"body-" + section.id + "\">";
    html += "<span class=\"num\">" + sectionLabel(topic, index) + "</span>";
    html += "<span><span class=\"skill-title\">" + escapeHtml(section.title) + "</span> " + tagBadges(section.tags) + " <span class=\"lessons\">" + escapeHtml(section.spec || "") + "</span></span>";
    html += summary.total > 0 ? ringHtml(summary) : "<span></span>";
    html += icon("chev");
    html += "</button>";

    // Body
    html += "<div class=\"skill-body\" id=\"body-" + section.id + "\"><div class=\"inner\"><div class=\"skill-content\">";

    if (section.equations && section.equations.length > 0) {
      html += "<div class=\"formulas\">";
      section.equations.forEach(function (equation) {
        html += "<span class=\"formula\">" + tex(equation, false) + "</span>";
      });
      html += "</div>";
    }

    if (section.blurb) {
      html += "<p class=\"method\">" + prose(section.blurb) + "</p>";
    }

    (section.parts || []).forEach(function (part, partIndex) {
      html += renderPart(topic, section, part, partIndex);
    });

    if (section.checklist && section.checklist.length > 0) {
      html += renderSelfCheck(section);
    }

    html += "</div></div></div></article>";
    return html;
  }

  function renderPart(topic, section, part, partIndex) {
    if (part.kind === "explain") {
      let html = "<section class=\"explain" + (part.tone === "warn" ? " warn" : "") + "\">";
      html += "<span class=\"kicker\">" + (part.tone === "warn" ? "Careful" : "Explanation") + "</span>";
      html += "<h4>" + escapeHtml(part.title) + "</h4>";
      html += "<div class=\"prose\">" + prose(part.html) + "</div>";
      html += graphHtml(part.graph);
      if (part.after) {
        html += "<div class=\"prose\">" + prose(part.after) + "</div>";
      }
      html += "</section>";
      return html;
    }

    if (part.kind === "worked") {
      let html = "<section class=\"worked\" data-worked=\"" + section.id + "-" + partIndex + "\">";
      html += "<span class=\"kicker\">Worked example</span>";
      html += "<h4>" + escapeHtml(part.title) + "</h4>";
      html += "<p class=\"q\">" + prose(part.question) + "</p>";
      html += graphHtml(part.graph);
      html += "<ol class=\"steps\">";
      part.steps.forEach(function (step, stepIndex) {
        html += "<li class=\"" + (stepIndex === 0 ? "" : "hidden-step") + "\"><span>" + prose(step) + "</span></li>";
      });
      html += "</ol>";
      html += "<div class=\"controls\"><button class=\"btn small\" data-next-step>Next step</button><button class=\"btn quiet small\" data-all-steps>Show all</button></div>";
      html += "</section>";
      return html;
    }

    if (part.kind === "practice") {
      let html = "<section class=\"practice\"><span class=\"practice-kicker\">Practise · " + escapeHtml(part.title) + "</span>";
      if (part.intro) {
        html += "<p class=\"practice-intro\">" + prose(part.intro) + "</p>";
      }
      part.questions.forEach(function (question, questionIndex) {
        html += renderSectionQuestion(question, String(questionIndex + 1));
      });
      html += "</section>";
      return html;
    }

    if (part.kind === "types") {
      // The calculation types this section covers, as nested cards
      let html = "<section class=\"embedded-types\">";
      if (part.title) {
        html += "<span class=\"practice-kicker\">" + escapeHtml(part.title) + "</span>";
      }
      if (part.intro) {
        html += "<p class=\"practice-intro\">" + prose(part.intro) + "</p>";
      }
      let shown = 0;
      sectionTypes(topic, { parts: [part] }).forEach(function (type) {
        if (!matchesBoard(type.boards) || visiblePractice(type).length === 0) {
          return;
        }
        shown += 1;
        html += renderSkill(topic, type, sectionLabel(topic, topicSections(topic).indexOf(section)) + "." + shown, true);
      });
      if (shown === 0) {
        html += "<p class=\"practice-intro\">" + escapeHtml(config.filter.none.replace("{option}", board).replace("this topic", "this section")) + "</p>";
      }
      html += "</section>";
      return html;
    }

    if (part.kind === "facts") {
      let html = "<section class=\"facts\"><span class=\"practice-kicker\">" + escapeHtml(part.title) + "</span>";
      html += "<p class=\"practice-intro\">Tap a card to flip it. Say the answer out loud before you look.</p>";
      html += "<div class=\"fact-grid\">";
      part.items.forEach(function (item, itemIndex) {
        html += "<button class=\"fact\" type=\"button\" aria-pressed=\"false\" data-fact>" +
          "<span class=\"fact-q\"><span class=\"n\">" + (itemIndex + 1) + "</span>" + prose(item.q) + "</span>" +
          "<span class=\"fact-a\">" + prose(item.a) + "</span></button>";
      });
      html += "</div></section>";
      return html;
    }

    return "";
  }

  // Traffic-light self-check from the section's checklist
  function renderSelfCheck(section) {
    const saved = selfCheck[section.id] || {};
    let html = "<section class=\"selfcheck\"><span class=\"practice-kicker\">Self-check · can you…</span>";
    html += "<p class=\"practice-intro\">Be honest: red means \"not yet\", amber means \"with help\", green means \"on my own\".</p>";
    html += "<div class=\"rag-list\">";
    section.checklist.forEach(function (item, itemIndex) {
      const chosen = saved[itemIndex] || "";
      html += "<div class=\"rag-row\" data-rag=\"" + section.id + "\" data-index=\"" + itemIndex + "\">";
      html += "<span class=\"rag-text\">" + prose(escapeHtml(item)) + "</span>";
      html += "<span class=\"rag-btns\" role=\"group\" aria-label=\"Confidence\">";
      ["r", "a", "g"].forEach(function (level) {
        const title = level === "r" ? "Not yet" : (level === "a" ? "With help" : "On my own");
        html += "<button type=\"button\" class=\"rag " + level + (chosen === level ? " on" : "") + "\" data-level=\"" + level + "\" title=\"" + title + "\" aria-label=\"" + title + "\" aria-pressed=\"" + (chosen === level ? "true" : "false") + "\"></button>";
      });
      html += "</span></div>";
    });
    html += "</div></section>";
    return html;
  }

  /* ===================================================================
     Section questions: numeric, choice, written, draw, group
     (TeX notation; marked by the app or by the student)
     =================================================================== */

  function questionNumber(number, question) {
    return question.label ? number + question.label : number;
  }

  function renderSectionQuestion(question, number) {
    if (question.type === "group") {
      let html = "<div class=\"qgroup\" data-group=\"" + question.id + "\">";
      html += "<div class=\"q-top\"><span class=\"qn\">" + number + "</span>" + tagBadges(question.tags) + "</div>";
      html += "<div class=\"q-text stem\">" + prose(question.text) + "</div>";
      html += graphHtml(question.graph);
      question.parts.forEach(function (child) {
        if (!sectionQuestionVisible(child)) {
          return;
        }
        html += renderSectionQuestion(child, number);
      });
      html += "</div>";
      return html;
    }

    if (!sectionQuestionVisible(question)) {
      return "";
    }

    const correct = isCorrect(question.id);
    const shown = questionNumber(number, question);

    let html = "";
    html += "<div class=\"question" + (correct ? " correct" : "") + " type-" + question.type + "\" data-qid=\"" + question.id + "\">";
    html += "<div class=\"q-top\"><span class=\"qn\">" + shown + "</span><span class=\"level\">" + typeLabel(question.type) + "</span>" + tagBadges(question.tags) + "</div>";
    html += "<div class=\"q-text\">" + prose(question.text) + "</div>";
    html += graphHtml(question.graph);

    if (question.type === "numeric") {
      html += renderNumericControls(question, correct);
    } else if (question.type === "choice") {
      html += renderChoiceControls(question, correct);
    } else if (question.type === "written") {
      html += renderWrittenControls(question, correct);
    } else if (question.type === "draw") {
      html += renderDrawControls(question, correct);
    }

    html += "</div>";
    return html;
  }

  function typeLabel(type) {
    if (type === "numeric") {
      return "calculate";
    }
    if (type === "choice") {
      return "choose";
    }
    if (type === "written") {
      return "explain";
    }
    if (type === "draw") {
      return "draw";
    }
    return "";
  }

  function feedbackHtml(correct) {
    return "<div class=\"feedback" + (correct ? " ok" : "") + "\" data-feedback>" + (correct ? icon("tick") + "Correct" : "") + "</div>";
  }

  function hintPanelHtml(question) {
    if (!question.hint) {
      return "";
    }
    return "<div class=\"panel hint\" data-panel=\"hint\"><div class=\"inner\"><div class=\"box\"><span class=\"kicker\">Hint</span>" + prose(question.hint) + "</div></div></div>";
  }

  function hintButtonHtml(question) {
    if (!question.hint) {
      return "";
    }
    return "<button class=\"btn small\" data-toggle=\"hint\" aria-expanded=\"false\">Hint</button>";
  }

  function renderNumericControls(question, correct) {
    let html = "";
    html += "<div class=\"answer-row\">";
    html += "<label class=\"answer-field\"><span class=\"visually-hidden\">Your answer</span>";
    html += "<input type=\"text\" inputmode=\"text\" placeholder=\"your answer\" data-input" + (correct ? " value=\"" + escapeHtml(formatValue(question.answer.value)) + "\"" : "") + ">";
    html += "<span class=\"unit\">" + richmath.renderUnit(question.answer.unit) + "</span>";
    html += "</label>";
    html += "<button class=\"btn solid\" data-check>Check</button>";
    html += "</div>";

    html += feedbackHtml(correct);

    html += "<div class=\"help\">";
    html += hintButtonHtml(question);
    html += "<button class=\"btn small\" data-toggle=\"walkthrough\" aria-expanded=\"false\">Walkthrough</button>";
    html += "<button class=\"btn small\" data-toggle=\"answer\" aria-expanded=\"false\">Answer</button>";
    html += "</div>";

    html += "<div class=\"panels\">";
    html += hintPanelHtml(question);
    html += "<div class=\"panel walkthrough\" data-panel=\"walkthrough\"><div class=\"inner\"><div class=\"box\"><span class=\"kicker\">Walkthrough</span><ol class=\"steps\">";
    question.walkthrough.forEach(function (line) {
      html += "<li><span>" + prose(line) + "</span></li>";
    });
    html += "</ol></div></div></div>";
    html += "<div class=\"panel answer\" data-panel=\"answer\"><div class=\"inner\"><div class=\"box\"><span class=\"kicker\">Answer</span>" + answerHtml(question.answer) + "</div></div></div>";
    html += "</div>";
    return html;
  }

  function renderChoiceControls(question, correct) {
    let html = "";
    html += "<div class=\"choices\" role=\"group\" aria-label=\"Options\">";
    question.options.forEach(function (option, optionIndex) {
      const isAnswer = optionIndex === question.correct;
      const marked = correct && isAnswer ? " chosen right" : "";
      html += "<button type=\"button\" class=\"choice" + marked + "\" data-choice=\"" + optionIndex + "\" aria-pressed=\"" + (correct && isAnswer ? "true" : "false") + "\">" +
        "<span class=\"letter\">" + String.fromCharCode(65 + optionIndex) + "</span>" + prose(option) + "</button>";
    });
    html += "</div>";

    html += feedbackHtml(correct);

    html += "<div class=\"help\">";
    html += hintButtonHtml(question);
    html += "<button class=\"btn small\" data-toggle=\"answer\" aria-expanded=\"false\">Why?</button>";
    html += "</div>";

    html += "<div class=\"panels\">";
    html += hintPanelHtml(question);
    html += "<div class=\"panel answer\" data-panel=\"answer\"><div class=\"inner\"><div class=\"box\"><span class=\"kicker\">Answer: " +
      String.fromCharCode(65 + question.correct) + "</span>" + prose(question.explain) + "</div></div></div>";
    html += "</div>";
    return html;
  }

  // Written answers are marked by the student against a model answer
  function selfMarkHtml(correct) {
    let html = "";
    html += "<div class=\"selfmark\">";
    html += "<button class=\"btn small\" data-toggle=\"model\" aria-expanded=\"false\">Show model answer</button>";
    html += "<span class=\"selfmark-q\">Did you get it?</span>";
    html += "<button class=\"btn small ok-btn" + (correct ? " on" : "") + "\" data-mark=\"correct\" aria-pressed=\"" + (correct ? "true" : "false") + "\">Yes, got it</button>";
    html += "<button class=\"btn small\" data-mark=\"attempted\">Not yet</button>";
    html += "</div>";
    return html;
  }

  function renderWrittenControls(question, correct) {
    let html = "";
    html += "<div class=\"writing\" aria-hidden=\"true\">";
    for (let index = 0; index < (question.lines || 3); index += 1) {
      html += "<div></div>";
    }
    html += "</div>";
    html += "<p class=\"note\">Write your answer on paper, then compare it with the model answer.</p>";

    html += feedbackHtml(correct);
    html += selfMarkHtml(correct);
    html += "<div class=\"help\">" + hintButtonHtml(question) + "</div>";

    html += "<div class=\"panels\">";
    html += hintPanelHtml(question);
    html += "<div class=\"panel walkthrough\" data-panel=\"model\"><div class=\"inner\"><div class=\"box\"><span class=\"kicker\">Model answer</span>" + prose(question.model) + "</div></div></div>";
    html += "</div>";
    return html;
  }

  function renderDrawControls(question, correct) {
    let html = "";
    html += graphHtml(question.grid, "blank drawable");
    html += "<div class=\"draw-tools\">";
    html += "<span class=\"note\">Tap the grid to place points in order (they snap to the grid lines). Or draw it on paper.</span>";
    html += "<span class=\"draw-btns\"><button class=\"btn small\" data-draw-undo>Undo</button><button class=\"btn small\" data-draw-clear>Clear</button>";
    if (question.check) {
      html += "<button class=\"btn solid small\" data-draw-check>Check</button>";
    }
    html += "</span></div>";

    html += feedbackHtml(correct);
    if (!question.check) {
      html += selfMarkHtml(correct);
      html += "<div class=\"help\">" + hintButtonHtml(question) + "</div>";
    } else {
      html += "<div class=\"help\">" + hintButtonHtml(question) + "<button class=\"btn small\" data-toggle=\"model\" aria-expanded=\"false\">Answer</button></div>";
    }

    html += "<div class=\"panels\">";
    html += hintPanelHtml(question);
    html += "<div class=\"panel walkthrough\" data-panel=\"model\"><div class=\"inner\"><div class=\"box wide\"><span class=\"kicker\">Answer</span>" +
      prose(question.model) + graphHtml(question.answerGraph) + "</div></div></div>";
    html += "</div>";
    return html;
  }

  /* ===================================================================
     Drawing on a grid
     The geometry mirrors js/graphs.js (plot area 520 × 340 with the same
     padding), so a tap can be turned back into a data coordinate.
     =================================================================== */

  const GRAPH_WIDTH = 520;
  const GRAPH_HEIGHT = 340;
  const GRAPH_PAD = { left: 58, right: 22, top: 26, bottom: 44 };

  // Minor divisions per major step, as graphs.js chooses them
  function minorDivisions(axisSpec) {
    if (axisSpec.minor) {
      return axisSpec.minor;
    }
    const majors = Math.round((axisSpec.max - axisSpec.min) / axisSpec.step);
    if (majors <= 6) {
      return 5;
    }
    if (majors <= 12) {
      return 2;
    }
    return 1;
  }

  function wireDraw(block, question) {
    const figure = block.querySelector(".graph.drawable");
    const svg = figure ? figure.querySelector("svg.graph-svg") : null;
    const feedback = block.querySelector("[data-feedback]");
    if (!svg) {
      return;
    }

    const xSpec = question.grid.x;
    const ySpec = question.grid.y;
    const xSnap = xSpec.step / minorDivisions(xSpec);
    const ySnap = ySpec.step / minorDivisions(ySpec);
    const plotLeft = GRAPH_PAD.left;
    const plotRight = GRAPH_WIDTH - GRAPH_PAD.right;
    const plotTop = GRAPH_PAD.top;
    const plotBottom = GRAPH_HEIGHT - GRAPH_PAD.bottom;

    // Points the student has placed, in data coordinates, in order
    let points = [];

    // A group on top of the grid for the student's line
    const layer = document.createElementNS("http://www.w3.org/2000/svg", "g");
    layer.setAttribute("class", "g-user");
    svg.appendChild(layer);
    svg.classList.add("can-draw");

    function toPixelX(value) {
      return plotLeft + ((value - xSpec.min) / (xSpec.max - xSpec.min)) * (plotRight - plotLeft);
    }

    function toPixelY(value) {
      return plotBottom - ((value - ySpec.min) / (ySpec.max - ySpec.min)) * (plotBottom - plotTop);
    }

    function redraw() {
      let markup = "";
      if (points.length > 1) {
        let d = "";
        points.forEach(function (point, index) {
          d += (index === 0 ? "M" : "L") + toPixelX(point[0]).toFixed(1) + "," + toPixelY(point[1]).toFixed(1);
        });
        markup += "<path d=\"" + d + "\"/>";
      }
      points.forEach(function (point) {
        const px = toPixelX(point[0]).toFixed(1);
        const py = toPixelY(point[1]).toFixed(1);
        markup += "<path class=\"cross\" d=\"M" + (px - 5) + "," + (py - 5) + "L" + (Number(px) + 5) + "," + (Number(py) + 5) +
          "M" + (px - 5) + "," + (Number(py) + 5) + "L" + (Number(px) + 5) + "," + (py - 5) + "\"/>";
      });
      layer.innerHTML = markup;
    }

    function snap(value, origin, step) {
      return origin + Math.round((value - origin) / step) * step;
    }

    svg.addEventListener("click", function (event) {
      const point = svg.createSVGPoint();
      point.x = event.clientX;
      point.y = event.clientY;
      const local = point.matrixTransform(svg.getScreenCTM().inverse());

      // Ignore taps outside the plot area (with a little slack)
      if (local.x < plotLeft - 8 || local.x > plotRight + 8 || local.y < plotTop - 8 || local.y > plotBottom + 8) {
        return;
      }

      const dataX = xSpec.min + ((local.x - plotLeft) / (plotRight - plotLeft)) * (xSpec.max - xSpec.min);
      const dataY = ySpec.min + ((plotBottom - local.y) / (plotBottom - plotTop)) * (ySpec.max - ySpec.min);
      const snappedX = Math.min(xSpec.max, Math.max(xSpec.min, snap(dataX, xSpec.min, xSnap)));
      const snappedY = Math.min(ySpec.max, Math.max(ySpec.min, snap(dataY, ySpec.min, ySnap)));

      // Tapping an existing point removes it
      const existing = points.findIndex(function (p) {
        return Math.abs(p[0] - snappedX) < 1e-9 && Math.abs(p[1] - snappedY) < 1e-9;
      });
      if (existing >= 0) {
        points.splice(existing, 1);
      } else {
        points.push([snappedX, snappedY]);
      }
      redraw();
    });

    block.querySelector("[data-draw-undo]").addEventListener("click", function () {
      points.pop();
      redraw();
    });

    block.querySelector("[data-draw-clear]").addEventListener("click", function () {
      points = [];
      redraw();
    });

    const checkButton = block.querySelector("[data-draw-check]");
    if (checkButton) {
      checkButton.addEventListener("click", function () {
        const target = question.answerGraph.series[0].points;
        const outcome = compareDrawing(points, target, xSnap, ySnap);
        if (outcome.ok) {
          setQuestionState(block, question.id, "correct", feedback, "Correct — that's the shape");
        } else {
          const attempts = (progress[question.id] ? progress[question.id].attempts : 0) + 1;
          setQuestionState(block, question.id, "wrong", feedback, outcome.message + (attempts >= 2 ? " Open the hint or the answer if you are stuck." : ""));
        }
      });
    }
  }

  // Compare a student's points with the answer polyline, in order
  function compareDrawing(points, target, xSnap, ySnap) {
    if (points.length === 0) {
      return { ok: false, message: "Tap the grid to place your points first." };
    }
    if (points.length !== target.length) {
      return { ok: false, message: "This graph needs " + target.length + " points (one at the end of each stage). You have placed " + points.length + "." };
    }
    for (let index = 0; index < target.length; index += 1) {
      const dx = Math.abs(points[index][0] - target[index][0]);
      const dy = Math.abs(points[index][1] - target[index][1]);
      if (dx > xSnap * 0.51 || dy > ySnap * 0.51) {
        return { ok: false, message: "Point " + (index + 1) + " is not in the right place. Check the value on each axis at the end of that stage." };
      }
    }
    return { ok: true, message: "" };
  }

  /* ===================================================================
     Wiring: collapse, worked steps, answers, help panels
     =================================================================== */

  // The card element for a type id, a section id or "key-facts"
  function cardElement(cardId) {
    return document.getElementById("skill-" + cardId) ||
      document.getElementById("section-" + cardId) ||
      document.getElementById("card-" + cardId);
  }

  function setCollapsed(cardId, shouldCollapse) {
    const article = cardElement(cardId);
    if (shouldCollapse) {
      collapsed.add(cardId);
    } else {
      collapsed.delete(cardId);
    }
    saveCollapsed();
    if (article) {
      article.classList.toggle("collapsed", shouldCollapse);
      const head = article.querySelector(".skill-head");
      if (head) {
        head.setAttribute("aria-expanded", shouldCollapse ? "false" : "true");
      }
    }
  }

  function setAllCollapsed(cards, shouldCollapse) {
    cards.forEach(function (card) {
      setCollapsed(card.id, shouldCollapse);
    });
  }

  function wireSkills(root) {
    // Collapse toggles (type cards and section cards alike)
    root.querySelectorAll(".skill").forEach(function (article) {
      const cardId = article.getAttribute("data-card");
      const head = article.querySelector(":scope > .skill-head");
      if (!head) {
        return;
      }
      head.addEventListener("click", function () {
        setCollapsed(cardId, !article.classList.contains("collapsed"));
      });
    });

    // Worked example step reveal
    root.querySelectorAll(".worked").forEach(function (section) {
      wireWorked(section);
    });

    // Questions
    root.querySelectorAll(".question").forEach(function (block) {
      wireQuestion(block);
    });

    // Key-fact flip cards
    root.querySelectorAll("[data-fact]").forEach(function (card) {
      card.addEventListener("click", function () {
        const flipped = card.classList.toggle("flipped");
        card.setAttribute("aria-pressed", flipped ? "true" : "false");
      });
    });

    // Flashcard tools: shuffle the grid, flip every card at once
    root.querySelectorAll("[data-facts-shuffle]").forEach(function (button) {
      button.addEventListener("click", function () {
        const grid = button.closest(".facts").querySelector("[data-fact-grid]");
        const cards = Array.from(grid.children);
        for (let index = cards.length - 1; index > 0; index -= 1) {
          const other = Math.floor(Math.random() * (index + 1));
          const held = cards[index];
          cards[index] = cards[other];
          cards[other] = held;
        }
        cards.forEach(function (card) {
          card.classList.remove("flipped");
          card.setAttribute("aria-pressed", "false");
          grid.appendChild(card);
        });
      });
    });
    root.querySelectorAll("[data-facts-flip]").forEach(function (button) {
      button.addEventListener("click", function () {
        const grid = button.closest(".facts").querySelector("[data-fact-grid]");
        const cards = Array.from(grid.querySelectorAll("[data-fact]"));
        const showAll = button.textContent === "Show all answers";
        cards.forEach(function (card) {
          card.classList.toggle("flipped", showAll);
          card.setAttribute("aria-pressed", showAll ? "true" : "false");
        });
        button.textContent = showAll ? "Hide all answers" : "Show all answers";
      });
    });

    // Traffic-light self-check
    root.querySelectorAll(".rag-row").forEach(function (row) {
      const sectionId = row.getAttribute("data-rag");
      const index = row.getAttribute("data-index");
      row.querySelectorAll(".rag").forEach(function (button) {
        button.addEventListener("click", function () {
          const level = button.getAttribute("data-level");
          selfCheck[sectionId] = selfCheck[sectionId] || {};
          selfCheck[sectionId][index] = level;
          saveSelfCheck();
          row.querySelectorAll(".rag").forEach(function (other) {
            const on = other === button;
            other.classList.toggle("on", on);
            other.setAttribute("aria-pressed", on ? "true" : "false");
          });
        });
      });
    });
  }

  function wireWorked(section) {
    const steps = Array.from(section.querySelectorAll(":scope > .steps > li"));
    const nextButton = section.querySelector("[data-next-step]");
    const allButton = section.querySelector("[data-all-steps]");

    function revealNext() {
      const hidden = steps.find(function (step) {
        return step.classList.contains("hidden-step");
      });
      if (hidden) {
        hidden.classList.remove("hidden-step");
        hidden.classList.add("reveal");
      }
      updateButtons();
    }

    function revealAll() {
      steps.forEach(function (step) {
        step.classList.remove("hidden-step");
      });
      updateButtons();
    }

    function updateButtons() {
      const anyHidden = steps.some(function (step) {
        return step.classList.contains("hidden-step");
      });
      nextButton.hidden = !anyHidden;
      allButton.textContent = anyHidden ? "Show all" : "Hide steps";
    }

    nextButton.addEventListener("click", revealNext);
    allButton.addEventListener("click", function () {
      const anyHidden = steps.some(function (step) {
        return step.classList.contains("hidden-step");
      });
      if (anyHidden) {
        revealAll();
      } else {
        steps.forEach(function (step, index) {
          step.classList.toggle("hidden-step", index > 0);
          step.classList.remove("reveal");
        });
        updateButtons();
      }
    });
    updateButtons();
  }

  // Record an outcome for a question and show the feedback line
  function setQuestionState(block, questionId, status, feedback, message, force) {
    const state = progress[questionId] || { status: "attempted", attempts: 0 };
    state.attempts += 1;
    if (status === "correct") {
      state.status = "correct";
      feedback.className = "feedback ok";
      feedback.innerHTML = icon("tick") + (message || "Correct");
      block.classList.add("correct");
    } else {
      // A wrong go after a right one does not take the right one away
      if (state.status !== "correct" || force) {
        state.status = "attempted";
        block.classList.remove("correct");
      }
      feedback.className = "feedback " + (status === "nudge" ? "nudge" : "bad");
      feedback.textContent = message;
    }
    progress[questionId] = state;
    saveProgress();
    refreshProgress();
  }

  function wireQuestion(block) {
    const questionId = block.getAttribute("data-qid");
    const question = findQuestion(questionId);
    const feedback = block.querySelector("[data-feedback]");
    if (!question) {
      return;
    }

    // Numeric entry (calculation types and numeric section questions)
    const input = block.querySelector("[data-input]");
    const checkButton = block.querySelector("[data-check]");
    if (input && checkButton) {
      const runCheck = function () {
        const entered = parseEntry(input.value);
        if (Number.isNaN(entered)) {
          feedback.className = "feedback bad";
          feedback.textContent = "Enter a number, such as 2.4e-3 or 2.4 × 10⁻³.";
          return;
        }
        const outcome = checkEntry(entered, question.answer);
        if (outcome.result === "correct") {
          setQuestionState(block, questionId, "correct", feedback, "Correct");
        } else {
          const attempts = (progress[questionId] ? progress[questionId].attempts : 0) + 1;
          setQuestionState(block, questionId, outcome.factor !== null ? "nudge" : "wrong", feedback, wrongMessage(outcome.factor, attempts));
        }
      };
      checkButton.addEventListener("click", runCheck);
      input.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
          runCheck();
        }
      });
    }

    // Multiple choice
    block.querySelectorAll("[data-choice]").forEach(function (button) {
      button.addEventListener("click", function () {
        const chosen = Number(button.getAttribute("data-choice"));
        block.querySelectorAll("[data-choice]").forEach(function (other) {
          other.classList.remove("chosen", "right", "wrong");
          other.setAttribute("aria-pressed", "false");
        });
        button.classList.add("chosen");
        button.setAttribute("aria-pressed", "true");
        if (chosen === question.correct) {
          button.classList.add("right");
          setQuestionState(block, questionId, "correct", feedback, "Correct");
        } else {
          button.classList.add("wrong");
          const attempts = (progress[questionId] ? progress[questionId].attempts : 0) + 1;
          setQuestionState(block, questionId, "wrong", feedback, attempts >= 2 ? "Not that one. Open \"Why?\" to see the reasoning." : "Not that one. Think again and try another.");
        }
      });
    });

    // Drawing tasks
    if (question.type === "draw") {
      wireDraw(block, question);
    }

    // Self-marked questions
    block.querySelectorAll("[data-mark]").forEach(function (button) {
      button.addEventListener("click", function () {
        const mark = button.getAttribute("data-mark");
        const yesButton = block.querySelector("[data-mark=\"correct\"]");
        if (mark === "correct") {
          yesButton.classList.add("on");
          yesButton.setAttribute("aria-pressed", "true");
          setQuestionState(block, questionId, "correct", feedback, "Marked as got it");
        } else {
          yesButton.classList.remove("on");
          yesButton.setAttribute("aria-pressed", "false");
          setQuestionState(block, questionId, "wrong", feedback, "No problem — re-read the explanation and come back to this one.", true);
        }
      });
    });

    // Help panels
    block.querySelectorAll("[data-toggle]").forEach(function (button) {
      button.addEventListener("click", function () {
        const name = button.getAttribute("data-toggle");
        const panel = block.querySelector("[data-panel=\"" + name + "\"]");
        if (!panel) {
          return;
        }
        const open = panel.classList.toggle("open");
        button.setAttribute("aria-expanded", open ? "true" : "false");
        if (name === "model") {
          button.textContent = open ? "Hide model answer" : "Show model answer";
        }
      });
    });
  }

  // Update rings, pills and bars in place after an answer
  function refreshProgress() {
    const topic = findTopic(currentRoute().topicId);
    document.querySelectorAll(".skill").forEach(function (article) {
      let summary = null;
      const typeId = article.getAttribute("data-type");
      const sectionId = article.getAttribute("data-section");
      if (typeId) {
        const type = findType(typeId);
        if (type) {
          summary = typeProgress(type);
        }
      } else if (sectionId && topic) {
        const section = findSection(topic, sectionId);
        if (section) {
          summary = sectionProgress(topic, section);
        }
      }
      if (!summary) {
        return;
      }
      const ring = article.querySelector(":scope > .skill-head .ring");
      const percent = summary.total ? Math.round((summary.correct / summary.total) * 100) : 0;
      if (ring) {
        ring.style.setProperty("--p", percent);
        ring.querySelector(".txt").textContent = summary.correct + "/" + summary.total;
      }
      const pill = document.querySelector("[data-pill=\"" + (typeId || sectionId) + "\"]");
      if (pill) {
        pill.classList.toggle("done", summary.total > 0 && summary.correct === summary.total);
      }
    });

    if (topic) {
      const summary = topicProgress(topic);
      const line = document.querySelector(".cover .progress-line");
      if (line) {
        const percent = summary.total ? (summary.correct / summary.total) * 100 : 0;
        line.querySelector("span").textContent = summary.correct + " of " + summary.total + " questions correct" + (board === "all" ? "" : " for " + board);
        line.querySelector(".bar > i").style.setProperty("--p", percent.toFixed(1) + "%");
      }
    }
  }

  /* ===================================================================
     Views: search
     =================================================================== */

  function renderSearch(query) {
    document.body.classList.remove("is-home");
    const needle = query.toLowerCase();
    let html = "<header class=\"results-head\"><h2>Search</h2><p>Calculations matching “" + escapeHtml(query) + "”</p></header>";
    let found = 0;

    topics.forEach(function (topic) {
      const hits = visibleTypes(topic).filter(function (type) {
        const haystack = (type.name + " " + type.equations.join(" ") + " " + type.method).toLowerCase();
        return haystack.includes(needle);
      });
      // Sections match on their title, spec reference and checklist
      const sectionHits = topicSections(topic).filter(function (section) {
        const haystack = (section.title + " " + (section.spec || "") + " " + (section.checklist || []).join(" ")).toLowerCase();
        return haystack.includes(needle);
      });
      if (hits.length === 0 && sectionHits.length === 0) {
        return;
      }
      html += "<div class=\"result-topic\">" + escapeHtml(topic.title) + "</div>";
      if (sectionHits.length > 0) {
        html += "<div class=\"result-sections\">";
        sectionHits.forEach(function (section) {
          const label = sectionLabel(topic, topicSections(topic).indexOf(section));
          html += "<a class=\"pill\" href=\"#" + topic.id + "/" + section.id + "\"><span class=\"n\">" + escapeHtml(label) + "</span>" + escapeHtml(section.title) + "</a>";
          found += 1;
        });
        html += "</div>";
      }
      if (hits.length > 0) {
        html += "<div class=\"skills\">";
        hits.forEach(function (type) {
          // Search results start collapsed so the list is scannable
          collapsed.add(type.id);
          html += renderSkill(topic, type, String(topic.types.indexOf(type) + 1), false);
          found += 1;
        });
        html += "</div>";
      }
    });

    if (found === 0) {
      html += "<div class=\"notice\">Nothing matches. Try a quantity, a unit, an equation symbol or a section title.</div>";
    }

    main.innerHTML = html;
    wireSkills(main);
  }

  /* ===================================================================
     Routing and transitions
     =================================================================== */

  function currentRoute() {
    const hash = decodeURIComponent(location.hash.replace(/^#/, ""));
    const parts = hash.split("/");
    return { topicId: parts[0] || "", typeId: parts[1] || "" };
  }

  function renderRoute(animate) {
    const query = document.getElementById("search").value.trim();
    const route = currentRoute();

    function paint() {
      if (query.length >= 2) {
        renderSearch(query);
        return;
      }
      const topic = findTopic(route.topicId);
      if (topic) {
        renderTopic(topic, route.typeId);
      } else {
        renderHome();
      }
    }

    const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (animate && !reduced && typeof document.startViewTransition === "function") {
      document.startViewTransition(paint);
    } else {
      paint();
    }
  }

  function onHashChange() {
    document.getElementById("search").value = "";
    renderRoute(true);
    if (!currentRoute().typeId) {
      window.scrollTo({ top: 0, behavior: "instant" in window ? "instant" : "auto" });
    }
  }

  /* ===================================================================
     Theme
     =================================================================== */

  function applySavedTheme() {
    const saved = readStorage(STORAGE_PREFIX + "theme");
    if (saved) {
      document.documentElement.setAttribute("data-theme", saved);
    }
  }

  function toggleTheme() {
    const current = document.documentElement.getAttribute("data-theme");
    const systemDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
    const effective = current || (systemDark ? "dark" : "light");
    const next = effective === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next);
    writeStorage(STORAGE_PREFIX + "theme", next);
  }

  /* ===================================================================
     Print booklet
     =================================================================== */

  function buildBooklet() {
    const scope = document.querySelector("input[name=\"p-scope\"]:checked").value;
    const answersMode = document.querySelector("input[name=\"p-answers\"]:checked").value;
    const includeWorked = document.getElementById("p-worked").checked;
    const includeMethod = document.getElementById("p-method").checked;
    const includeHints = document.getElementById("p-hints").checked;
    const includeLines = document.getElementById("p-lines").checked;

    const route = currentRoute();
    const currentTopic = findTopic(route.topicId);
    const chosen = scope === "all" || !currentTopic ? topics : [currentTopic];
    const boardLabel = board === "all" ? config.filter.all : config.filter.label + ": " + board;

    let html = "";
    html += "<div class=\"p-cover\"><h1>" + escapeHtml(config.title) + "</h1>";
    html += "<div class=\"p-sub\">" + (chosen.length > 1 ? escapeHtml(config.printSubtitle) : escapeHtml(chosen[0].title)) + "</div>";
    html += "<div class=\"p-meta\">" + escapeHtml(boardLabel) + (answersMode === "none" ? ". Questions only." : ". Answers at the back.") + "</div>";
    html += "<div class=\"p-name\">Name <span></span></div></div>";

    const options = { worked: includeWorked, method: includeMethod, hints: includeHints, lines: includeLines };

    chosen.forEach(function (topic) {
      if (hasSections(topic)) {
        html += printSectionsTopic(topic, options);
        return;
      }
      const types = visibleTypes(topic);
      if (types.length === 0) {
        return;
      }
      html += "<section class=\"p-topic\"><h2>" + escapeHtml(topic.title) + "</h2>";
      types.forEach(function (type, typeIndex) {
        html += printType(type, String(typeIndex + 1), options);
      });
      html += "</section>";
    });

    if (answersMode !== "none") {
      html += "<section class=\"p-answers\"><h2>Answers</h2>";
      chosen.forEach(function (topic) {
        if (hasSections(topic)) {
          html += printSectionsAnswers(topic, answersMode);
          return;
        }
        const types = visibleTypes(topic);
        if (types.length === 0) {
          return;
        }
        html += "<h3>" + escapeHtml(topic.title) + "</h3>";
        types.forEach(function (type, typeIndex) {
          html += printTypeAnswers(type, String(typeIndex + 1), answersMode);
        });
      });
      html += "</section>";
    }

    html += "<div class=\"p-foot\">" + escapeHtml(config.title) + ", " + escapeHtml(config.credit) + "</div>";
    document.getElementById("print-root").innerHTML = html;
  }

  // One calculation type on paper, numbered `label`
  function printType(type, label, options) {
    let html = "<div class=\"p-type\"><h3>" + escapeHtml(label) + ". " + escapeHtml(type.name) + "</h3>";
    html += "<div class=\"p-eq\">" + type.equations.map(function (equation) { return rich(equation); }).join("") + "</div>";
    if (options.method) {
      html += "<p class=\"p-method\">" + rich(type.method) + "</p><ul class=\"p-errors\">";
      type.commonErrors.forEach(function (error) {
        html += "<li>" + rich(error) + "</li>";
      });
      html += "</ul>";
    }
    if (options.worked) {
      html += "<div class=\"p-worked\"><div class=\"p-label\">Worked example</div><div>" + rich(type.worked.question) + "</div>" + graphHtml(type.worked.graph) + "<ol>";
      type.worked.steps.forEach(function (step) {
        html += "<li>" + rich(step) + "</li>";
      });
      html += "</ol></div>";
    }
    visiblePractice(type).forEach(function (question, questionIndex) {
      html += "<div class=\"p-q\"><span class=\"p-qnum\">" + escapeHtml(label) + "." + (questionIndex + 1) + "</span>" + rich(question.question) + graphHtml(question.graph);
      if (options.hints) {
        html += "<div class=\"p-hint\">Hint: " + rich(question.hint) + "</div>";
      }
      if (options.lines) {
        html += "<div class=\"p-lines\"><div></div><div></div><div></div></div>";
      }
      html += "</div>";
    });
    html += "</div>";
    return html;
  }

  function printTypeAnswers(type, label, answersMode) {
    let html = "<h4>" + escapeHtml(label) + ". " + escapeHtml(type.name) + "</h4>";
    visiblePractice(type).forEach(function (question, questionIndex) {
      html += "<div class=\"p-ans\"><span class=\"p-qnum\">" + escapeHtml(label) + "." + (questionIndex + 1) + "</span>" + answerHtml(question.answer);
      if (answersMode === "full") {
        html += "<ol>";
        question.walkthrough.forEach(function (line) {
          html += "<li>" + rich(line) + "</li>";
        });
        html += "</ol>";
      }
      html += "</div>";
    });
    return html;
  }

  // A section question on paper
  function printSectionQuestion(question, number, options) {
    if (question.type === "group") {
      let html = "<div class=\"p-group\"><div class=\"p-q\"><span class=\"p-qnum\">" + number + "</span>" + prose(question.text) + graphHtml(question.graph) + "</div>";
      question.parts.forEach(function (child) {
        if (sectionQuestionVisible(child)) {
          html += printSectionQuestion(child, number, options);
        }
      });
      html += "</div>";
      return html;
    }
    if (!sectionQuestionVisible(question)) {
      return "";
    }

    const shown = questionNumber(number, question);
    // On paper there is nothing to tap, so the on-screen instruction is reworded
    const text = String(question.text).replace(/tap the grid to place the points in order, or draw it on paper/g, "draw it on the grid");
    let html = "<div class=\"p-q\"><span class=\"p-qnum\">" + shown + "</span>" + prose(text);
    html += graphHtml(question.graph);

    if (question.type === "choice") {
      html += "<div class=\"p-options\">";
      question.options.forEach(function (option, optionIndex) {
        html += "<span>☐ " + String.fromCharCode(65 + optionIndex) + ". " + prose(option) + "</span>";
      });
      html += "</div>";
    }
    if (question.type === "draw") {
      html += graphHtml(question.grid, "blank");
    }
    if (options.hints && question.hint) {
      html += "<div class=\"p-hint\">Hint: " + prose(question.hint) + "</div>";
    }
    if (options.lines) {
      if (question.type === "numeric") {
        html += "<div class=\"p-ewau\"><div><b>E</b></div><div></div><div><b>W</b></div><div></div><div><b>A</b></div><div></div><div><b>U</b></div><div></div></div>";
      } else if (question.type === "written") {
        html += "<div class=\"p-lines\">";
        for (let index = 0; index < (question.lines || 3); index += 1) {
          html += "<div></div>";
        }
        html += "</div>";
      }
    }
    html += "</div>";
    return html;
  }

  function printSectionAnswer(question, number, mode) {
    if (question.type === "group") {
      let html = "";
      question.parts.forEach(function (child) {
        if (sectionQuestionVisible(child)) {
          html += printSectionAnswer(child, number, mode);
        }
      });
      return html;
    }
    if (!sectionQuestionVisible(question)) {
      return "";
    }
    const shown = questionNumber(number, question);
    let html = "<div class=\"p-ans\"><span class=\"p-qnum\">" + shown + "</span>";
    if (question.type === "numeric") {
      html += answerHtml(question.answer);
      if (mode === "full") {
        html += "<ol>";
        question.walkthrough.forEach(function (line) {
          html += "<li>" + prose(line) + "</li>";
        });
        html += "</ol>";
      }
    } else if (question.type === "choice") {
      html += String.fromCharCode(65 + question.correct) + " — " + prose(question.options[question.correct]);
      if (mode === "full") {
        html += "<div class=\"p-why\">" + prose(question.explain) + "</div>";
      }
    } else if (question.type === "written") {
      html += "<div class=\"p-why\">" + prose(question.model) + "</div>";
    } else if (question.type === "draw") {
      html += "<div class=\"p-why\">" + prose(question.model) + (mode === "full" ? graphHtml(question.answerGraph) : "") + "</div>";
    }
    html += "</div>";
    return html;
  }

  // A topic with sections on paper: band divider pages, each section's
  // notes, worked examples, practice and embedded calculations, then the
  // self-check table and the key facts as a cover-and-test table
  function printSectionsTopic(topic, options) {
    const sections = topicSections(topic);
    let html = "";

    if (sections.some(function (section) { return section.checklist && section.checklist.length > 0; })) {
      html += "<div class=\"p-cover p-checklist\"><h3 class=\"p-checklist-head\">" + escapeHtml(topic.title) + " — can you…?</h3><table class=\"p-check\">";
      sections.forEach(function (section, sectionIndex) {
        (section.checklist || []).forEach(function (item, itemIndex) {
          const rowLabel = sectionLabel(topic, sectionIndex) + " · " + section.title;
          html += "<tr>" + (itemIndex === 0 ? "<td class=\"p-lesson\" rowspan=\"" + section.checklist.length + "\">" + escapeHtml(rowLabel) + "</td>" : "") +
            "<td>" + escapeHtml(item) + "</td><td class=\"p-box\">☐</td></tr>";
        });
      });
      html += "</table></div>";
    }

    sections.forEach(function (section, sectionIndex) {
      if (startsBand(topic, sectionIndex)) {
        const band = bandOf(topic, section);
        html += "<div class=\"p-band\"><h2>" + escapeHtml(band.title) + "</h2>" + (band.blurb ? "<p>" + prose(band.blurb) + "</p>" : "") + "</div>";
      }
      const label = sectionLabel(topic, sectionIndex);
      html += "<section class=\"p-topic\"><h2>" + escapeHtml(label) + ". " + escapeHtml(section.title) + " <small>" + escapeHtml(section.spec || "") + "</small></h2>";
      let practiceNumber = 0;
      let embedded = 0;
      (section.parts || []).forEach(function (part) {
        if (part.kind === "explain" && options.method) {
          html += "<div class=\"p-explain" + (part.tone === "warn" ? " warn" : "") + "\"><h3>" + escapeHtml(part.title) + "</h3>" + prose(part.html) + graphHtml(part.graph) + (part.after ? prose(part.after) : "") + "</div>";
        }
        if (part.kind === "worked" && options.worked) {
          html += "<div class=\"p-worked\"><div class=\"p-label\">Worked example · " + escapeHtml(part.title) + "</div><div>" + prose(part.question) + "</div>" + graphHtml(part.graph) + "<ol>";
          part.steps.forEach(function (step) {
            html += "<li>" + prose(step) + "</li>";
          });
          html += "</ol></div>";
        }
        if (part.kind === "practice") {
          html += "<div class=\"p-practice\"><div class=\"p-label\">Practice · " + escapeHtml(part.title) + "</div>";
          if (part.intro) {
            html += "<p class=\"p-intro\">" + prose(part.intro) + "</p>";
          }
          part.questions.forEach(function (question) {
            practiceNumber += 1;
            html += printSectionQuestion(question, String(practiceNumber), options);
          });
          html += "</div>";
        }
        if (part.kind === "types") {
          sectionTypes(topic, { parts: [part] }).forEach(function (type) {
            if (!matchesBoard(type.boards) || visiblePractice(type).length === 0) {
              return;
            }
            embedded += 1;
            html += printType(type, label + "." + embedded, options);
          });
        }
        if (part.kind === "facts") {
          html += "<div class=\"p-facts\"><p class=\"p-intro\">Cover the right-hand column. Say the answer, then slide the paper down to check.</p><table class=\"p-check\">";
          part.items.forEach(function (item) {
            html += "<tr><td>" + prose(item.q) + "</td><td>" + prose(item.a) + "</td></tr>";
          });
          html += "</table></div>";
        }
      });
      if (section.checklist && section.checklist.length > 0) {
        html += "<div class=\"p-selfcheck\"><div class=\"p-label\">Self-check · I can…</div>";
        html += "<table class=\"p-check\"><tr><th></th><th>🔴</th><th>🟠</th><th>🟢</th></tr>";
        section.checklist.forEach(function (item) {
          html += "<tr><td>" + escapeHtml(item) + "</td><td class=\"p-box\">☐</td><td class=\"p-box\">☐</td><td class=\"p-box\">☐</td></tr>";
        });
        html += "</table></div>";
      }
      html += "</section>";
    });

    const extras = unplacedTypes(topic).filter(function (type) {
      return matchesBoard(type.boards) && visiblePractice(type).length > 0;
    });
    if (extras.length > 0) {
      html += "<section class=\"p-topic\"><h2>Calculations</h2>";
      extras.forEach(function (type, typeIndex) {
        html += printType(type, "C" + (typeIndex + 1), options);
      });
      html += "</section>";
    }

    if (topic.facts && topic.facts.length > 0) {
      html += "<div class=\"p-band\"><h2>Key facts</h2><p>Cover the right-hand column. Say the answer, then slide the paper down to check.</p></div>";
      html += "<section class=\"p-topic\"><div class=\"p-facts\"><table class=\"p-check\">";
      topic.facts.forEach(function (item) {
        html += "<tr><td>" + prose(item.q) + "</td><td>" + prose(item.a) + "</td></tr>";
      });
      html += "</table></div></section>";
    }
    return html;
  }

  function printSectionsAnswers(topic, answersMode) {
    let html = "<h3>" + escapeHtml(topic.title) + "</h3>";
    topicSections(topic).forEach(function (section, sectionIndex) {
      const label = sectionLabel(topic, sectionIndex);
      let practiceNumber = 0;
      let embedded = 0;
      let block = "";
      (section.parts || []).forEach(function (part) {
        if (part.kind === "practice") {
          block += "<h4>" + escapeHtml(part.title) + "</h4>";
          part.questions.forEach(function (question) {
            practiceNumber += 1;
            block += printSectionAnswer(question, String(practiceNumber), answersMode);
          });
        }
        if (part.kind === "types") {
          sectionTypes(topic, { parts: [part] }).forEach(function (type) {
            if (!matchesBoard(type.boards) || visiblePractice(type).length === 0) {
              return;
            }
            embedded += 1;
            block += printTypeAnswers(type, label + "." + embedded, answersMode);
          });
        }
      });
      if (block) {
        html += "<h3 class=\"p-section-head\">" + escapeHtml(label) + ". " + escapeHtml(section.title) + "</h3>" + block;
      }
    });
    const extras = unplacedTypes(topic).filter(function (type) {
      return matchesBoard(type.boards) && visiblePractice(type).length > 0;
    });
    extras.forEach(function (type, typeIndex) {
      html += printTypeAnswers(type, "C" + (typeIndex + 1), answersMode);
    });
    return html;
  }

  function openPrintModal() {
    const hasTopic = !!findTopic(currentRoute().topicId);
    const topicOption = document.querySelector("input[name=\"p-scope\"][value=\"topic\"]");
    topicOption.disabled = !hasTopic;
    if (!hasTopic) {
      document.querySelector("input[name=\"p-scope\"][value=\"all\"]").checked = true;
    }
    document.getElementById("print-modal").classList.add("open");
  }

  function closePrintModal() {
    document.getElementById("print-modal").classList.remove("open");
  }

  /* ===================================================================
     Boot
     =================================================================== */

  async function boot() {
    applySavedTheme();
    renderBoardPicker(document.getElementById("board-seg"));

    try {
      await loadAll();
    } catch (error) {
      main.innerHTML =
        "<div class=\"notice\"><strong>The question bank didn't load.</strong><br>" +
        "The topic files are fetched over HTTP, which browsers block for a page opened straight from disk. " +
        "Serve the folder (for example <code>python3 -m http.server</code>, then open <code>http://localhost:8000</code>) or publish it to GitHub Pages.<br><br>" +
        "<code>" + escapeHtml(error.message) + "</code></div>";
      return;
    }

    // The config may have changed the filter options, so draw the header picker again
    const headerPicker = document.getElementById("board-seg");
    headerPicker.setAttribute("aria-label", config.filter.label);
    renderBoardPicker(headerPicker);

    renderRoute(false);

    window.addEventListener("hashchange", onHashChange);
    window.addEventListener("scroll", onScrollParallax, { passive: true });

    let searchTimer = null;
    document.getElementById("search").addEventListener("input", function () {
      clearTimeout(searchTimer);
      searchTimer = setTimeout(function () {
        renderRoute(false);
      }, 120);
    });

    document.getElementById("btn-theme").addEventListener("click", toggleTheme);

    const printButton = document.getElementById("btn-print");
    if (printButton) {
      printButton.addEventListener("click", openPrintModal);
    }
    document.getElementById("p-cancel").addEventListener("click", closePrintModal);
    document.getElementById("print-modal").addEventListener("click", function (event) {
      if (event.target.id === "print-modal") {
        closePrintModal();
      }
    });
    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape") {
        closePrintModal();
      }
    });
    document.getElementById("p-go").addEventListener("click", function () {
      buildBooklet();
      closePrintModal();
      setTimeout(function () {
        window.print();
      }, 120);
    });
  }

  // Expose a few functions for the test harness
  window.nn = {
    parseEntry: parseEntry,
    checkEntry: checkEntry,
    formatValue: formatValue,
    findQuestion: findQuestion,
    buildBooklet: buildBooklet,
    getTopics: function () { return topics; },
    resetAll: function () {
      progress = {};
      collapsed = new Set();
      seenTopics = new Set();
      saveProgress();
      saveCollapsed();
      writeStorage(STORAGE_PREFIX + "seen", "[]");
    },
  };

  boot();
}());
