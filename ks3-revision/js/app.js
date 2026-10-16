/*
 * app.js — KS3 Revision
 *
 * Loads the topic files, renders the topic page (or a home grid when
 * there is more than one topic), checks answers, keeps progress in the
 * browser, and builds the print booklet. Maths is typeset by KaTeX;
 * graphs are drawn by js/graphs.js from the specs in the data files.
 */
(function () {
  "use strict";

  /* ===================================================================
     Constants and state
     =================================================================== */

  // Fraction of the stored answer within which an entry counts as correct
  const DEFAULT_TOLERANCE = 0.02;

  // All loaded topics, in order
  let topics = [];

  // Progress per question id: { status, attempts }
  let progress = readJson("ks3-progress", {});

  // Traffic-light self-check per section: { sectionId: { index: "r" | "a" | "g" } }
  let selfCheck = readJson("ks3-selfcheck", {});

  // Ids of section cards the user has collapsed
  let collapsed = new Set(readJson("ks3-collapsed", []));

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
    writeStorage("ks3-progress", JSON.stringify(progress));
  }

  function saveSelfCheck() {
    writeStorage("ks3-selfcheck", JSON.stringify(selfCheck));
  }

  function saveCollapsed() {
    writeStorage("ks3-collapsed", JSON.stringify(Array.from(collapsed)));
  }

  /* ===================================================================
     Data loading
     =================================================================== */

  async function loadAll() {
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
     Lookups
     =================================================================== */

  function findTopic(topicId) {
    return topics.find(function (topic) {
      return topic.id === topicId;
    }) || null;
  }

  function findSection(topic, sectionId) {
    return topic.sections.find(function (section) {
      return section.id === sectionId;
    }) || null;
  }

  // Every answerable question in a section, flattening groups
  function leafQuestions(section) {
    const leaves = [];
    section.parts.forEach(function (part) {
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
    return leaves;
  }

  function findQuestion(questionId) {
    for (const topic of topics) {
      for (const section of topic.sections) {
        for (const question of leafQuestions(section)) {
          if (question.id === questionId) {
            return question;
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

  function sectionProgress(section) {
    const questions = leafQuestions(section);
    let correct = 0;
    for (const question of questions) {
      if (isCorrect(question.id)) {
        correct += 1;
      }
    }
    return { correct: correct, total: questions.length };
  }

  function topicProgress(topic) {
    let correct = 0;
    let total = 0;
    for (const section of topic.sections) {
      const summary = sectionProgress(section);
      correct += summary.correct;
      total += summary.total;
    }
    return { correct: correct, total: total };
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
      return "Right size, wrong sign. Is it speeding up or slowing down — or heading home?";
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
    return "Not quite. Check which version of the equation you need, then try again.";
  }

  // Format a stored value for display
  function formatValue(value) {
    const magnitude = Math.abs(value);
    if (magnitude !== 0 && (magnitude >= 1e6 || magnitude < 1e-3)) {
      const exponent = Math.floor(Math.log10(magnitude));
      const mantissa = value / Math.pow(10, exponent);
      const mantissaText = Number(mantissa.toPrecision(3)).toString();
      return mantissaText + " × 10" + toSuperscript(exponent);
    }
    const rounded = Number(value.toPrecision(4));
    return rounded.toLocaleString("en-GB", { maximumFractionDigits: 4 }).replace(/,/g, " ");
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

  // Typeset one piece of TeX
  function tex(source, displayMode) {
    try {
      return katex.renderToString(source, { displayMode: displayMode, throwOnError: false, strict: "ignore" });
    } catch (error) {
      return "<span class=\"math-fallback\">" + escapeHtml(source) + "</span>";
    }
  }

  // HTML prose with $...$ and $$...$$ maths inside it
  function rich(text) {
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

  // A unit for the answer line, with superscripts kept as text
  function unitHtml(unit) {
    if (!unit) {
      return "";
    }
    return escapeHtml(unit);
  }

  // A graph from a spec, with typeset axis titles
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

  // The topic's cover drawing: a speed–time trapezium that draws itself in
  function figureHtml() {
    return "<svg class=\"fig\" viewBox=\"0 0 320 200\" aria-hidden=\"true\">" +
      "<g class=\"fig-grid\">" +
      "<path d=\"M40 20V170M80 20V170M120 20V170M160 20V170M200 20V170M240 20V170M280 20V170M40 50H300M40 80H300M40 110H300M40 140H300\"/>" +
      "</g>" +
      "<g class=\"fig-axes\"><path d=\"M40 20V170H300\"/></g>" +
      "<path class=\"fig-shade draw\" style=\"--i:3\" d=\"M40 170L120 60L220 60L300 170Z\"/>" +
      "<path class=\"fig-line draw\" style=\"--i:1\" d=\"M40 170L120 60L220 60L300 170\"/>" +
      "<g class=\"fig-marks draw\" style=\"--i:2\"><circle cx=\"120\" cy=\"60\" r=\"4\"/><circle cx=\"220\" cy=\"60\" r=\"4\"/><circle cx=\"300\" cy=\"170\" r=\"4\"/></g>" +
      "<g class=\"fig-text draw\" style=\"--i:4\"><text x=\"170\" y=\"128\" text-anchor=\"middle\">area = distance</text>" +
      "<text x=\"66\" y=\"100\" text-anchor=\"middle\" transform=\"rotate(-54 66 100)\">gradient = a</text>" +
      "<text x=\"300\" y=\"190\" text-anchor=\"end\">time</text><text x=\"36\" y=\"28\" text-anchor=\"end\">v</text></g>" +
      "</svg>";
  }

  /* ===================================================================
     Views: home (only shown when there is more than one topic)
     =================================================================== */

  function renderHome() {
    document.title = "KS3 Revision";
    setTopbarTitle("");

    let html = "";
    html += "<section class=\"hero" + (heroPlayed ? "" : " animate") + "\">";
    html += "<h1><span class=\"word\"><span style=\"--i:0\">KS3</span></span> <span class=\"word\"><span style=\"--i:1\">Revision</span></span></h1>";
    html += "<p class=\"lede\">Self-guiding revision booklets: clear explanations, worked examples and practice questions checked as you go.</p>";
    html += "</section>";

    html += "<section class=\"topics\" aria-label=\"Topics\">";
    topics.forEach(function (topic, index) {
      const summary = topicProgress(topic);
      const percent = summary.total ? (summary.correct / summary.total) * 100 : 0;
      const done = summary.total > 0 && summary.correct === summary.total;
      html += "<a class=\"topic-card" + (done ? " done" : "") + "\" href=\"#" + topic.id + "\" style=\"--i: " + index + "\">";
      html += "<div class=\"figwrap\">" + figureHtml() + "</div>";
      html += "<div class=\"meta corner-ticks\">";
      html += "<h3>" + escapeHtml(topic.title) + "</h3>";
      html += "<p class=\"sub\">" + escapeHtml(topic.subtitle) + "</p>";
      html += "<div class=\"stats\"><span>" + topic.sections.length + " sections</span><span>" + summary.correct + " of " + summary.total + " correct</span></div>";
      html += "<div class=\"bar\"><i style=\"--p: " + percent.toFixed(1) + "%\"></i></div>";
      html += "</div></a>";
    });
    html += "</section>";

    html += footerHtml();
    main.innerHTML = html;
    document.body.classList.add("is-home");
    heroPlayed = true;
    wireFooter();
  }

  /* ===================================================================
     Views: topic
     =================================================================== */

  function setTopbarTitle(text) {
    const element = document.getElementById("topbar-title");
    element.textContent = text;
  }

  function renderTopic(topic, sectionId) {
    document.body.classList.remove("is-home");
    document.title = topic.title + " — KS3 Revision";
    setTopbarTitle(topic.title);

    const summary = topicProgress(topic);
    const percent = summary.total ? (summary.correct / summary.total) * 100 : 0;

    let html = "";
    if (topics.length > 1) {
      html += "<nav class=\"crumbs\"><a href=\"#\">" + icon("back") + "All topics</a></nav>";
    }

    html += "<header class=\"cover" + (heroPlayed ? "" : " animate") + "\">";
    html += "<div>";
    html += "<p class=\"kicker\">" + escapeHtml(topic.stage || "Key Stage 3") + " · revision booklet</p>";
    html += "<h2>" + escapeHtml(topic.title) + "</h2>";
    html += "<p class=\"sub\">" + escapeHtml(topic.subtitle) + "</p>";
    html += "<div class=\"progress-line\"><span>" + summary.correct + " of " + summary.total + " questions correct</span><div class=\"bar\"><i style=\"--p: " + percent.toFixed(1) + "%\"></i></div></div>";
    html += "</div>";
    html += "<div class=\"figwrap\">" + figureHtml() + "</div>";
    html += "</header>";

    // How to use this booklet
    html += "<details class=\"howto\"><summary>" + icon("chev") + "How to use this booklet</summary>";
    html += "<p class=\"lede\">" + rich(topic.lede) + "</p><ol class=\"list\">";
    (topic.howto || []).forEach(function (line) {
      html += "<li>" + rich(line) + "</li>";
    });
    html += "</ol><div class=\"legend\">" +
      "<span class=\"lg-explain\">Explanation — read it carefully</span>" +
      "<span class=\"lg-worked\">Worked example — follow the steps</span>" +
      "<span class=\"lg-practice\">Practice — have a go straight away</span>" +
      "</div></details>";

    // Section pills
    html += "<div class=\"skillbar\"><div class=\"pills\">";
    topic.sections.forEach(function (section, index) {
      const sectionSummary = sectionProgress(section);
      const done = sectionSummary.total > 0 && sectionSummary.correct === sectionSummary.total;
      html += "<a class=\"pill" + (done ? " done" : "") + "\" href=\"#" + topic.id + "/" + section.id + "\" data-pill=\"" + section.id + "\"><span class=\"n\">" + (index + 1) + "</span>" + escapeHtml(section.title) + "</a>";
    });
    html += "</div><div class=\"tools\"><button class=\"btn quiet small\" id=\"btn-expand-all\">Expand all</button><button class=\"btn quiet small\" id=\"btn-collapse-all\">Collapse all</button></div></div>";

    // Section cards
    html += "<div class=\"skills\">";
    topic.sections.forEach(function (section, index) {
      html += renderSection(topic, section, index);
    });
    html += "</div>";

    html += footerHtml();
    main.innerHTML = html;
    heroPlayed = true;

    wireSections(main);
    wireFooter();

    const expandAll = document.getElementById("btn-expand-all");
    const collapseAll = document.getElementById("btn-collapse-all");
    expandAll.addEventListener("click", function () {
      setAllCollapsed(topic.sections, false);
    });
    collapseAll.addEventListener("click", function () {
      setAllCollapsed(topic.sections, true);
    });

    if (sectionId) {
      const target = document.getElementById("section-" + sectionId);
      if (target) {
        setCollapsed(sectionId, false);
        requestAnimationFrame(function () {
          target.scrollIntoView({ block: "start" });
        });
      }
    }
  }

  function footerHtml() {
    return "<footer class=\"site-foot\"><span>KS3 Revision</span>" +
      "<span>Joshua Stafford-Haworth, JSHPhysics · <button class=\"linkish\" id=\"btn-reset\" type=\"button\">Reset my progress</button></span></footer>";
  }

  function wireFooter() {
    const reset = document.getElementById("btn-reset");
    if (!reset) {
      return;
    }
    reset.addEventListener("click", function () {
      const sure = window.confirm("Clear all your answers and self-checks on this device?");
      if (!sure) {
        return;
      }
      progress = {};
      selfCheck = {};
      saveProgress();
      saveSelfCheck();
      renderRoute(false);
    });
  }

  /* ===================================================================
     Section cards
     =================================================================== */

  function renderSection(topic, section, index) {
    const summary = sectionProgress(section);
    const isCollapsed = collapsed.has(section.id);

    let html = "";
    html += "<article class=\"skill" + (isCollapsed ? " collapsed" : "") + "\" id=\"section-" + section.id + "\" data-section=\"" + section.id + "\">";

    // Header row (click to collapse)
    html += "<button class=\"skill-head\" type=\"button\" aria-expanded=\"" + (isCollapsed ? "false" : "true") + "\" aria-controls=\"body-" + section.id + "\">";
    html += "<span class=\"num\">" + (index + 1) + "</span>";
    html += "<span><span class=\"skill-title\">" + escapeHtml(section.title) + "</span> <span class=\"lessons\">" + escapeHtml(section.lessons || "") + "</span></span>";
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
      html += "<p class=\"method\">" + rich(section.blurb) + "</p>";
    }

    section.parts.forEach(function (part, partIndex) {
      html += renderPart(section, part, partIndex);
    });

    if (section.checklist && section.checklist.length > 0) {
      html += renderSelfCheck(section);
    }

    html += "</div></div></div></article>";
    return html;
  }

  function renderPart(section, part, partIndex) {
    if (part.kind === "explain") {
      let html = "<section class=\"explain" + (part.tone === "warn" ? " warn" : "") + "\">";
      html += "<span class=\"kicker\">" + (part.tone === "warn" ? "Careful" : "Explanation") + "</span>";
      html += "<h4>" + escapeHtml(part.title) + "</h4>";
      html += "<div class=\"prose\">" + rich(part.html) + "</div>";
      html += graphHtml(part.graph);
      if (part.after) {
        html += "<div class=\"prose\">" + rich(part.after) + "</div>";
      }
      html += "</section>";
      return html;
    }

    if (part.kind === "worked") {
      let html = "<section class=\"worked\" data-worked=\"" + section.id + "-" + partIndex + "\">";
      html += "<span class=\"kicker\">Worked example</span>";
      html += "<h4>" + escapeHtml(part.title) + "</h4>";
      html += "<p class=\"q\">" + rich(part.question) + "</p>";
      html += graphHtml(part.graph);
      html += "<ol class=\"steps\">";
      part.steps.forEach(function (step, stepIndex) {
        html += "<li class=\"" + (stepIndex === 0 ? "" : "hidden-step") + "\"><span>" + rich(step) + "</span></li>";
      });
      html += "</ol>";
      html += "<div class=\"controls\"><button class=\"btn small\" data-next-step>Next step</button><button class=\"btn quiet small\" data-all-steps>Show all</button></div>";
      html += "</section>";
      return html;
    }

    if (part.kind === "practice") {
      let html = "<section class=\"practice\"><span class=\"practice-kicker\">Practise · " + escapeHtml(part.title) + "</span>";
      if (part.intro) {
        html += "<p class=\"practice-intro\">" + rich(part.intro) + "</p>";
      }
      part.questions.forEach(function (question, questionIndex) {
        html += renderQuestion(question, String(questionIndex + 1));
      });
      html += "</section>";
      return html;
    }

    if (part.kind === "facts") {
      let html = "<section class=\"facts\"><span class=\"practice-kicker\">" + escapeHtml(part.title) + "</span>";
      html += "<p class=\"practice-intro\">Tap a card to flip it. Say the answer out loud before you look.</p>";
      html += "<div class=\"fact-grid\">";
      part.items.forEach(function (item, itemIndex) {
        html += "<button class=\"fact\" type=\"button\" aria-pressed=\"false\" data-fact>" +
          "<span class=\"fact-q\"><span class=\"n\">" + (itemIndex + 1) + "</span>" + rich(item.q) + "</span>" +
          "<span class=\"fact-a\">" + rich(item.a) + "</span></button>";
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
      html += "<span class=\"rag-text\">" + escapeHtml(item) + "</span>";
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
     Questions
     =================================================================== */

  function questionNumber(number, question) {
    return question.label ? number + question.label : number;
  }

  function renderQuestion(question, number) {
    if (question.type === "group") {
      let html = "<div class=\"qgroup\" data-group=\"" + question.id + "\">";
      html += "<div class=\"q-top\"><span class=\"qn\">" + number + "</span></div>";
      html += "<div class=\"q-text stem\">" + rich(question.text) + "</div>";
      html += graphHtml(question.graph);
      question.parts.forEach(function (child) {
        html += renderQuestion(child, number);
      });
      html += "</div>";
      return html;
    }

    const correct = isCorrect(question.id);
    const shown = questionNumber(number, question);

    let html = "";
    html += "<div class=\"question" + (correct ? " correct" : "") + " type-" + question.type + "\" data-qid=\"" + question.id + "\">";
    html += "<div class=\"q-top\"><span class=\"qn\">" + shown + "</span><span class=\"level\">" + typeLabel(question.type) + "</span></div>";
    html += "<div class=\"q-text\">" + rich(question.text) + "</div>";
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
    return "<div class=\"panel hint\" data-panel=\"hint\"><div class=\"inner\"><div class=\"box\"><span class=\"kicker\">Hint</span>" + rich(question.hint) + "</div></div></div>";
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
    html += "<span class=\"unit\">" + unitHtml(question.answer.unit) + "</span>";
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
    html += "<div class=\"panel walkthrough\" data-panel=\"walkthrough\"><div class=\"inner\"><div class=\"box\"><span class=\"kicker\">Walkthrough (EWAU)</span><ol class=\"steps\">";
    question.walkthrough.forEach(function (line) {
      html += "<li><span>" + rich(line) + "</span></li>";
    });
    html += "</ol></div></div></div>";
    html += "<div class=\"panel answer\" data-panel=\"answer\"><div class=\"inner\"><div class=\"box\"><span class=\"kicker\">Answer</span>" +
      escapeHtml(formatValue(question.answer.value)) + (question.answer.unit ? " " + unitHtml(question.answer.unit) : "") + "</div></div></div>";
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
        "<span class=\"letter\">" + String.fromCharCode(65 + optionIndex) + "</span>" + rich(option) + "</button>";
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
      String.fromCharCode(65 + question.correct) + "</span>" + rich(question.explain) + "</div></div></div>";
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
    html += "<div class=\"panel walkthrough\" data-panel=\"model\"><div class=\"inner\"><div class=\"box\"><span class=\"kicker\">Model answer</span>" + rich(question.model) + "</div></div></div>";
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
      rich(question.model) + graphHtml(question.answerGraph) + "</div></div></div>";
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
          setQuestionState(block, question.id, "correct", feedback, "Correct — that's the journey");
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
      return { ok: false, message: "This journey needs " + target.length + " points (one at the end of each stage). You have placed " + points.length + "." };
    }
    for (let index = 0; index < target.length; index += 1) {
      const dx = Math.abs(points[index][0] - target[index][0]);
      const dy = Math.abs(points[index][1] - target[index][1]);
      if (dx > xSnap * 0.51 || dy > ySnap * 0.51) {
        return { ok: false, message: "Point " + (index + 1) + " is not in the right place. Check the time at the end of that stage, and the value on the y-axis." };
      }
    }
    return { ok: true, message: "" };
  }

  /* ===================================================================
     Wiring: collapse, worked steps, answers, help panels
     =================================================================== */

  function setCollapsed(sectionId, shouldCollapse) {
    const article = document.getElementById("section-" + sectionId);
    if (shouldCollapse) {
      collapsed.add(sectionId);
    } else {
      collapsed.delete(sectionId);
    }
    saveCollapsed();
    if (article) {
      article.classList.toggle("collapsed", shouldCollapse);
      const head = article.querySelector(".skill-head");
      head.setAttribute("aria-expanded", shouldCollapse ? "false" : "true");
    }
  }

  function setAllCollapsed(sections, shouldCollapse) {
    sections.forEach(function (section) {
      setCollapsed(section.id, shouldCollapse);
    });
  }

  function wireSections(root) {
    // Collapse toggles
    root.querySelectorAll(".skill").forEach(function (article) {
      const sectionId = article.getAttribute("data-section");
      article.querySelector(".skill-head").addEventListener("click", function () {
        setCollapsed(sectionId, !article.classList.contains("collapsed"));
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
    const steps = Array.from(section.querySelectorAll(".steps > li"));
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

    // Numeric entry
    const input = block.querySelector("[data-input]");
    const checkButton = block.querySelector("[data-check]");
    if (input && checkButton) {
      function runCheck() {
        const entered = parseEntry(input.value);
        if (Number.isNaN(entered)) {
          feedback.className = "feedback bad";
          feedback.textContent = "Enter a number, such as 2.5 or -3.";
          return;
        }
        const outcome = checkEntry(entered, question.answer);
        if (outcome.result === "correct") {
          setQuestionState(block, questionId, "correct", feedback, "Correct");
        } else {
          const attempts = (progress[questionId] ? progress[questionId].attempts : 0) + 1;
          setQuestionState(block, questionId, outcome.factor !== null ? "nudge" : "wrong", feedback, wrongMessage(outcome.factor, attempts));
        }
      }
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
    const topic = findTopic(currentRoute().topicId) || topics[0];
    if (!topic) {
      return;
    }
    document.querySelectorAll(".skill").forEach(function (article) {
      const section = findSection(topic, article.getAttribute("data-section"));
      if (!section) {
        return;
      }
      const summary = sectionProgress(section);
      const ring = article.querySelector(".ring");
      if (ring) {
        const percent = summary.total ? Math.round((summary.correct / summary.total) * 100) : 0;
        ring.style.setProperty("--p", percent);
        ring.querySelector(".txt").textContent = summary.correct + "/" + summary.total;
      }
      const pill = document.querySelector("[data-pill=\"" + section.id + "\"]");
      if (pill) {
        pill.classList.toggle("done", summary.total > 0 && summary.correct === summary.total);
      }
    });

    const summary = topicProgress(topic);
    const line = document.querySelector(".cover .progress-line");
    if (line) {
      const percent = summary.total ? (summary.correct / summary.total) * 100 : 0;
      line.querySelector("span").textContent = summary.correct + " of " + summary.total + " questions correct";
      line.querySelector(".bar > i").style.setProperty("--p", percent.toFixed(1) + "%");
    }
  }

  /* ===================================================================
     Routing and transitions
     =================================================================== */

  function currentRoute() {
    const hash = decodeURIComponent(location.hash.replace(/^#/, ""));
    const parts = hash.split("/");
    return { topicId: parts[0] || "", sectionId: parts[1] || "" };
  }

  function renderRoute(animate) {
    const route = currentRoute();

    function paint() {
      const topic = findTopic(route.topicId);
      if (topic) {
        renderTopic(topic, route.sectionId);
      } else if (topics.length === 1) {
        // One topic: it is the whole site, so go straight to it
        renderTopic(topics[0], "");
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
    const route = currentRoute();
    const topic = findTopic(route.topicId);
    const alreadyShowing = topic && document.querySelector(".cover") && document.title.indexOf(topic.title) === 0;
    if (alreadyShowing && route.sectionId) {
      // Same topic, different section: just open and scroll, no re-render
      const target = document.getElementById("section-" + route.sectionId);
      if (target) {
        setCollapsed(route.sectionId, false);
        target.scrollIntoView({ block: "start" });
        return;
      }
    }
    renderRoute(true);
    if (!route.sectionId) {
      window.scrollTo({ top: 0, behavior: "instant" in window ? "instant" : "auto" });
    }
  }

  /* ===================================================================
     Theme
     =================================================================== */

  function applySavedTheme() {
    const saved = readStorage("ks3-theme");
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
    writeStorage("ks3-theme", next);
  }

  /* ===================================================================
     Print booklet
     =================================================================== */

  function printQuestion(question, number, options) {
    if (question.type === "group") {
      let html = "<div class=\"p-group\"><div class=\"p-q\"><span class=\"p-qnum\">" + number + "</span>" + rich(question.text) + graphHtml(question.graph) + "</div>";
      question.parts.forEach(function (child) {
        html += printQuestion(child, number, options);
      });
      html += "</div>";
      return html;
    }

    const shown = questionNumber(number, question);
    // On paper there is nothing to tap, so the on-screen instruction is reworded
    const text = String(question.text).replace(/tap the grid to place the points in order, or draw it on paper/g, "draw it on the grid");
    let html = "<div class=\"p-q\"><span class=\"p-qnum\">" + shown + "</span>" + rich(text);
    html += graphHtml(question.graph);

    if (question.type === "choice") {
      html += "<div class=\"p-options\">";
      question.options.forEach(function (option, optionIndex) {
        html += "<span>☐ " + String.fromCharCode(65 + optionIndex) + ". " + rich(option) + "</span>";
      });
      html += "</div>";
    }

    if (question.type === "draw") {
      html += graphHtml(question.grid, "blank");
    }

    if (options.hints && question.hint) {
      html += "<div class=\"p-hint\">Hint: " + rich(question.hint) + "</div>";
    }

    if (options.space) {
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

  function printAnswer(question, number, mode) {
    if (question.type === "group") {
      let html = "";
      question.parts.forEach(function (child) {
        html += printAnswer(child, number, mode);
      });
      return html;
    }
    const shown = questionNumber(number, question);
    let html = "<div class=\"p-ans\"><span class=\"p-qnum\">" + shown + "</span>";
    if (question.type === "numeric") {
      html += escapeHtml(formatValue(question.answer.value)) + (question.answer.unit ? " " + escapeHtml(question.answer.unit) : "");
      if (mode === "full") {
        html += "<ol>";
        question.walkthrough.forEach(function (line) {
          html += "<li>" + rich(line) + "</li>";
        });
        html += "</ol>";
      }
    } else if (question.type === "choice") {
      html += String.fromCharCode(65 + question.correct) + " — " + rich(question.options[question.correct]);
      if (mode === "full") {
        html += "<div class=\"p-why\">" + rich(question.explain) + "</div>";
      }
    } else if (question.type === "written") {
      html += "<div class=\"p-why\">" + rich(question.model) + "</div>";
    } else if (question.type === "draw") {
      html += "<div class=\"p-why\">" + rich(question.model) + (mode === "full" ? graphHtml(question.answerGraph) : "") + "</div>";
    }
    html += "</div>";
    return html;
  }

  function buildBooklet() {
    const answersMode = document.querySelector("input[name=\"p-answers\"]:checked").value;
    const options = {
      explain: document.getElementById("p-explain").checked,
      worked: document.getElementById("p-worked").checked,
      hints: document.getElementById("p-hints").checked,
      space: document.getElementById("p-space").checked,
    };

    const topic = findTopic(currentRoute().topicId) || topics[0];

    let html = "";
    html += "<div class=\"p-cover\"><div class=\"p-stage\">" + escapeHtml(topic.stage || "Key Stage 3") + " · revision booklet</div><h1>" + escapeHtml(topic.title) + "</h1>";
    html += "<div class=\"p-sub\">" + escapeHtml(topic.subtitle) + "</div>";
    html += "<div class=\"p-meta\">" + (answersMode === "none" ? "Questions only." : "Answers at the back.") + "</div>";
    html += "<div class=\"p-name\">Name <span></span></div>";
    html += "<div class=\"p-name\">Class <span></span></div>";
    html += "<h3>How to use this booklet</h3><ol>";
    (topic.howto || []).forEach(function (line) {
      html += "<li>" + rich(line).replace(/type the answer to check it/g, "check it against the answers at the back") + "</li>";
    });
    html += "</ol>";
    html += "<h3 class=\"p-checklist-head\">The checklist — can you…?</h3><table class=\"p-check\">";
    topic.sections.forEach(function (section) {
      (section.checklist || []).forEach(function (item, itemIndex) {
        html += "<tr>" + (itemIndex === 0 ? "<td class=\"p-lesson\" rowspan=\"" + section.checklist.length + "\">" + escapeHtml(section.lessons || "") + "</td>" : "") +
          "<td>" + escapeHtml(item) + "</td><td class=\"p-box\">☐</td></tr>";
      });
    });
    html += "</table></div>";

    topic.sections.forEach(function (section, sectionIndex) {
      html += "<section class=\"p-topic\"><h2>" + (sectionIndex + 1) + ". " + escapeHtml(section.title) + " <small>" + escapeHtml(section.lessons || "") + "</small></h2>";
      let practiceNumber = 0;
      section.parts.forEach(function (part) {
        if (part.kind === "explain" && options.explain) {
          html += "<div class=\"p-explain" + (part.tone === "warn" ? " warn" : "") + "\"><h3>" + escapeHtml(part.title) + "</h3>" + rich(part.html) + graphHtml(part.graph) + (part.after ? rich(part.after) : "") + "</div>";
        }
        if (part.kind === "worked" && options.worked) {
          html += "<div class=\"p-worked\"><div class=\"p-label\">Worked example · " + escapeHtml(part.title) + "</div><div>" + rich(part.question) + "</div>" + graphHtml(part.graph) + "<ol>";
          part.steps.forEach(function (step) {
            html += "<li>" + rich(step) + "</li>";
          });
          html += "</ol></div>";
        }
        if (part.kind === "practice") {
          html += "<div class=\"p-practice\"><div class=\"p-label\">Practice · " + escapeHtml(part.title) + "</div>";
          if (part.intro) {
            html += "<p class=\"p-intro\">" + rich(part.intro) + "</p>";
          }
          part.questions.forEach(function (question) {
            practiceNumber += 1;
            html += printQuestion(question, String(practiceNumber), options);
          });
          html += "</div>";
        }
        if (part.kind === "facts") {
          html += "<div class=\"p-facts\"><p class=\"p-intro\">Cover the right-hand column. Say the answer, then slide the paper down to check.</p><table class=\"p-check\">";
          part.items.forEach(function (item) {
            html += "<tr><td>" + rich(item.q) + "</td><td>" + rich(item.a) + "</td></tr>";
          });
          html += "</table></div>";
        }
      });
      // Each section ends with its own review page: the traffic-light
      // self-check plus space to write revision targets
      if (section.checklist && section.checklist.length > 0) {
        html += "<div class=\"p-selfcheck\"><h3>Section review · " + escapeHtml(section.title) + "</h3>";
        html += "<div class=\"p-label\">Self-check · I can…</div><p class=\"p-intro\">Be honest: red means \"not yet\", amber means \"with help\", green means \"on my own\".</p>";
        html += "<table class=\"p-check\"><tr><th></th><th>🔴</th><th>🟠</th><th>🟢</th></tr>";
        section.checklist.forEach(function (item) {
          html += "<tr><td>" + escapeHtml(item) + "</td><td class=\"p-box\">☐</td><td class=\"p-box\">☐</td><td class=\"p-box\">☐</td></tr>";
        });
        html += "</table>";
        html += "<div class=\"p-label\">What I need to revise (anything red or amber)</div><div class=\"p-lines\"><div></div><div></div><div></div><div></div><div></div><div></div></div>";
        html += "<div class=\"p-label\">Questions to ask my teacher</div><div class=\"p-lines\"><div></div><div></div><div></div><div></div></div>";
        html += "</div>";
      }
      html += "</section>";
    });

    if (answersMode !== "none") {
      html += "<section class=\"p-answers\"><h2>Answers</h2>";
      topic.sections.forEach(function (section, sectionIndex) {
        let practiceNumber = 0;
        let any = false;
        let block = "";
        section.parts.forEach(function (part) {
          if (part.kind !== "practice") {
            return;
          }
          any = true;
          block += "<h4>" + escapeHtml(part.title) + "</h4>";
          part.questions.forEach(function (question) {
            practiceNumber += 1;
            block += printAnswer(question, String(practiceNumber), answersMode);
          });
        });
        if (any) {
          html += "<h3>" + (sectionIndex + 1) + ". " + escapeHtml(section.title) + "</h3>" + block;
        }
      });
      html += "</section>";
    }

    html += "<div class=\"p-foot\">KS3 Revision · " + escapeHtml(topic.title) + " · Joshua Stafford-Haworth, JSHPhysics</div>";
    document.getElementById("print-root").innerHTML = html;
  }

  function openPrintModal() {
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

    try {
      await loadAll();
    } catch (error) {
      main.innerHTML =
        "<div class=\"notice\"><strong>The booklet didn't load.</strong><br>" +
        "The topic files are fetched over HTTP, which browsers block for a page opened straight from disk. " +
        "Serve the folder (for example <code>python3 -m http.server</code>, then open <code>http://localhost:8000</code>) or publish it to GitHub Pages.<br><br>" +
        "<code>" + escapeHtml(error.message) + "</code></div>";
      return;
    }

    renderRoute(false);

    window.addEventListener("hashchange", onHashChange);

    document.getElementById("btn-theme").addEventListener("click", toggleTheme);
    document.getElementById("btn-print").addEventListener("click", openPrintModal);
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

  // Expose a few functions for testing
  window.ks3 = {
    parseEntry: parseEntry,
    checkEntry: checkEntry,
    formatValue: formatValue,
    findQuestion: findQuestion,
    buildBooklet: buildBooklet,
    getTopics: function () { return topics; },
  };

  boot();
}());
