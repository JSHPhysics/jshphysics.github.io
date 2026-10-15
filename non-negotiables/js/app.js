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

  // Boards in display order; must match the tags in the data files
  const BOARDS = ["AQA", "OCR A", "OCR B", "Edexcel", "WJEC"];

  // Fraction of the stored answer within which an entry counts as correct
  const DEFAULT_TOLERANCE = 0.02;

  // All loaded topics, in sidebar order
  let topics = [];

  // Current board filter: one of BOARDS or "all"
  let board = readStorage("nn-board") || "all";

  // Progress per question id: { status, attempts }
  let progress = readJson("nn-progress", {});

  // Ids of skill cards the user has collapsed
  let collapsed = new Set(readJson("nn-collapsed", []));

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
    writeStorage("nn-progress", JSON.stringify(progress));
  }

  function saveCollapsed() {
    writeStorage("nn-collapsed", JSON.stringify(Array.from(collapsed)));
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

  function topicProgress(topic) {
    let correct = 0;
    let total = 0;
    for (const type of visibleTypes(topic)) {
      const summary = typeProgress(type);
      correct += summary.correct;
      total += summary.total;
    }
    return { correct: correct, total: total };
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

  // An answer value with its unit
  function answerHtml(answer) {
    const unit = answer.unit ? " " + answer.unit : "";
    return math(formatValue(answer.value) + unit);
  }

  // A graph from a question's spec, with KaTeX axis titles
  function graphHtml(spec) {
    if (!spec) {
      return "";
    }
    const drawn = graphs.render(spec);
    return "<figure class=\"graph\">" +
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
    const options = ["all"].concat(BOARDS);
    for (const option of options) {
      const button = document.createElement("button");
      button.type = "button";
      button.textContent = option === "all" ? "All boards" : option;
      button.setAttribute("aria-pressed", board === option ? "true" : "false");
      button.addEventListener("click", function () {
        board = option;
        writeStorage("nn-board", board);
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

    const words = ["The", "Non-", "negotiables"];
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
    html += "<p class=\"lede\">The calculations every A-level physicist has to be able to do without thinking. Each one comes with a worked example and six to practise, checked as you go.</p>";
    html += "<div class=\"hero-controls\"><span class=\"label\">Show what my board examines</span><div class=\"seg\" id=\"hero-seg\" role=\"group\" aria-label=\"Exam board\"></div></div>";
    html += "</section>";

    html += "<section class=\"topics\" aria-label=\"Topics\">";
    topics.forEach(function (topic, index) {
      const types = visibleTypes(topic);
      if (types.length === 0) {
        return;
      }
      const summary = topicProgress(topic);
      const percent = summary.total ? (summary.correct / summary.total) * 100 : 0;
      const done = summary.total > 0 && summary.correct === summary.total;
      const shared = topic.id === lastTopicId ? " shared" : "";
      html += "<a class=\"topic-card" + (done ? " done" : "") + "\" href=\"#" + topic.id + "\" data-topic=\"" + topic.id + "\" style=\"--i: " + index + "\">";
      html += "<div class=\"figwrap" + shared + "\">" + figures.render(topic.id) + "</div>";
      html += "<div class=\"meta corner-ticks\">";
      html += "<h3>" + escapeHtml(topic.title) + "</h3>";
      html += "<p class=\"sub\">" + escapeHtml(topic.subtitle) + "</p>";
      html += "<div class=\"stats\"><span>" + types.length + " calculation" + (types.length === 1 ? "" : "s") + "</span><span>" + summary.correct + " of " + summary.total + " correct</span></div>";
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
  let seenTopics = new Set(readJson("nn-seen", []));

  function applyFirstVisitDefaults(topic, types, typeId) {
    if (seenTopics.has(topic.id)) {
      return;
    }
    seenTopics.add(topic.id);
    writeStorage("nn-seen", JSON.stringify(Array.from(seenTopics)));
    types.forEach(function (type, index) {
      const keepOpen = index === 0 || type.id === typeId;
      if (!keepOpen) {
        collapsed.add(type.id);
      }
    });
    saveCollapsed();
  }

  function renderTopic(topic, typeId) {
    document.body.classList.remove("is-home");
    const types = visibleTypes(topic);
    applyFirstVisitDefaults(topic, types, typeId);
    const summary = topicProgress(topic);
    const percent = summary.total ? (summary.correct / summary.total) * 100 : 0;
    const index = topics.indexOf(topic);
    const previous = neighbourTopic(index, -1);
    const next = neighbourTopic(index, 1);

    let html = "";
    html += "<nav class=\"crumbs\"><a href=\"#\">" + icon("back") + "All topics</a></nav>";

    html += "<header class=\"cover\">";
    html += "<div><h2>" + escapeHtml(topic.title) + "</h2>";
    html += "<p class=\"sub\">" + escapeHtml(topic.subtitle) + "</p>";
    html += "<div class=\"progress-line\"><span>" + summary.correct + " of " + summary.total + " questions correct" + (board === "all" ? "" : " for " + escapeHtml(board)) + "</span><div class=\"bar\"><i style=\"--p: " + percent.toFixed(1) + "%\"></i></div></div>";
    html += "</div>";
    html += "<div class=\"figwrap shared\">" + figures.render(topic.id) + "</div>";
    html += "</header>";

    if (types.length === 0) {
      html += "<div class=\"notice\">Nothing in this topic is examined by " + escapeHtml(board) + ". Choose another board or another topic.</div>";
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
        html += renderSkill(topic, type, typeIndex);
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
        setAllCollapsed(types, false);
      });
      collapseAll.addEventListener("click", function () {
        setAllCollapsed(types, true);
      });
    }

    if (typeId) {
      const target = document.getElementById("skill-" + typeId);
      if (target) {
        setCollapsed(typeId, false);
        requestAnimationFrame(function () {
          target.scrollIntoView({ block: "start" });
        });
      }
    }
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
      if (visibleTypes(topics[cursor]).length > 0) {
        return topics[cursor];
      }
      cursor += direction;
    }
    return null;
  }

  function footerHtml() {
    return "<footer class=\"site-foot\"><span>The Non-negotiables</span><span>Joshua Stafford-Haworth, JSHPhysics</span></footer>";
  }

  /* ===================================================================
     Skill cards
     =================================================================== */

  function renderSkill(topic, type, typeIndex) {
    const summary = typeProgress(type);
    const isCollapsed = collapsed.has(type.id);
    const questions = visiblePractice(type);

    let html = "";
    html += "<article class=\"skill" + (isCollapsed ? " collapsed" : "") + "\" id=\"skill-" + type.id + "\" data-type=\"" + type.id + "\">";

    // Header row (click to collapse)
    html += "<button class=\"skill-head\" type=\"button\" aria-expanded=\"" + (isCollapsed ? "false" : "true") + "\" aria-controls=\"body-" + type.id + "\">";
    html += "<span class=\"num\">" + (typeIndex + 1) + "</span>";
    html += "<span><span class=\"skill-title\">" + escapeHtml(type.name) + "</span> <span class=\"eq-preview\">" + rich(type.equations[0]) + "</span></span>";
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
      html += renderQuestion(question, questionIndex);
    });
    html += "</section>";

    html += "</div></div></div></article>";
    return html;
  }

  function renderQuestion(question, index) {
    const correct = isCorrect(question.id);
    let html = "";
    html += "<div class=\"question" + (correct ? " correct" : "") + "\" data-qid=\"" + question.id + "\">";
    html += "<div class=\"q-top\"><span class=\"qn\">" + (index + 1) + "</span><span class=\"level\">" + levelLabel(question) + "</span></div>";
    html += "<p class=\"q-text\">" + rich(question.question) + "</p>";
    html += graphHtml(question.graph);

    html += "<div class=\"answer-row\">";
    html += "<label class=\"answer-field\"><span class=\"visually-hidden\">Your answer</span>";
    html += "<input type=\"text\" inputmode=\"text\" placeholder=\"your answer\" data-input" + (correct ? " value=\"" + escapeHtml(formatValue(question.answer.value)) + "\"" : "") + ">";
    html += "<span class=\"unit\">" + richmath.renderUnit(question.answer.unit) + "</span>";
    html += "</label>";
    html += "<button class=\"btn solid\" data-check>Check</button>";
    html += "</div>";

    html += "<div class=\"feedback" + (correct ? " ok" : "") + "\" data-feedback>" + (correct ? icon("tick") + "Correct" : "") + "</div>";

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
     Wiring: collapse, worked steps, answers, help panels
     =================================================================== */

  function setCollapsed(typeId, shouldCollapse) {
    const article = document.getElementById("skill-" + typeId);
    if (shouldCollapse) {
      collapsed.add(typeId);
    } else {
      collapsed.delete(typeId);
    }
    saveCollapsed();
    if (article) {
      article.classList.toggle("collapsed", shouldCollapse);
      const head = article.querySelector(".skill-head");
      head.setAttribute("aria-expanded", shouldCollapse ? "false" : "true");
    }
  }

  function setAllCollapsed(types, shouldCollapse) {
    types.forEach(function (type) {
      setCollapsed(type.id, shouldCollapse);
    });
  }

  function wireSkills(root) {
    // Collapse toggles
    root.querySelectorAll(".skill").forEach(function (article) {
      const typeId = article.getAttribute("data-type");
      article.querySelector(".skill-head").addEventListener("click", function () {
        setCollapsed(typeId, !article.classList.contains("collapsed"));
      });
    });

    // Worked example step reveal
    root.querySelectorAll(".worked").forEach(function (section) {
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
    });

    // Questions
    root.querySelectorAll(".question").forEach(function (block) {
      wireQuestion(block);
    });
  }

  function wireQuestion(block) {
    const questionId = block.getAttribute("data-qid");
    const question = findQuestion(questionId);
    const input = block.querySelector("[data-input]");
    const checkButton = block.querySelector("[data-check]");
    const feedback = block.querySelector("[data-feedback]");

    function runCheck() {
      const entered = parseEntry(input.value);

      if (Number.isNaN(entered)) {
        feedback.className = "feedback bad";
        feedback.textContent = "Enter a number, such as 2.4e-3 or 2.4 × 10⁻³.";
        return;
      }

      const state = progress[questionId] || { status: "attempted", attempts: 0 };
      state.attempts += 1;

      const outcome = checkEntry(entered, question.answer);

      if (outcome.result === "correct") {
        state.status = "correct";
        feedback.className = "feedback ok";
        feedback.innerHTML = icon("tick") + "Correct";
        block.classList.add("correct");
      } else {
        if (state.status !== "correct") {
          state.status = "attempted";
        }
        feedback.className = "feedback " + (outcome.factor !== null ? "nudge" : "bad");
        feedback.textContent = wrongMessage(outcome.factor, state.attempts);
      }

      progress[questionId] = state;
      saveProgress();
      refreshProgress();
    }

    checkButton.addEventListener("click", runCheck);
    input.addEventListener("keydown", function (event) {
      if (event.key === "Enter") {
        runCheck();
      }
    });

    block.querySelectorAll("[data-toggle]").forEach(function (button) {
      button.addEventListener("click", function () {
        const name = button.getAttribute("data-toggle");
        const panel = block.querySelector("[data-panel=\"" + name + "\"]");
        const open = panel.classList.toggle("open");
        button.setAttribute("aria-expanded", open ? "true" : "false");
      });
    });
  }

  // Update rings, pills and bars in place after an answer
  function refreshProgress() {
    document.querySelectorAll(".skill").forEach(function (article) {
      const type = findType(article.getAttribute("data-type"));
      if (!type) {
        return;
      }
      const summary = typeProgress(type);
      const ring = article.querySelector(".ring");
      const percent = summary.total ? Math.round((summary.correct / summary.total) * 100) : 0;
      ring.style.setProperty("--p", percent);
      ring.querySelector(".txt").textContent = summary.correct + "/" + summary.total;
      const pill = document.querySelector("[data-pill=\"" + type.id + "\"]");
      if (pill) {
        pill.classList.toggle("done", summary.total > 0 && summary.correct === summary.total);
      }
    });

    const topic = findTopic(currentRoute().topicId);
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
      if (hits.length === 0) {
        return;
      }
      html += "<div class=\"result-topic\">" + escapeHtml(topic.title) + "</div><div class=\"skills\">";
      hits.forEach(function (type, index) {
        // Search results start collapsed so the list is scannable
        collapsed.add(type.id);
        html += renderSkill(topic, type, topic.types.indexOf(type));
        found += 1;
      });
      html += "</div>";
    });

    if (found === 0) {
      html += "<div class=\"notice\">No calculations match. Try a quantity, a unit, or an equation symbol.</div>";
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
    const saved = readStorage("nn-theme");
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
    writeStorage("nn-theme", next);
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
    const boardLabel = board === "all" ? "All exam boards" : board;

    let html = "";
    html += "<div class=\"p-cover\"><h1>The Non-negotiables</h1>";
    html += "<div class=\"p-sub\">" + (chosen.length > 1 ? "A-level physics calculations, complete set" : escapeHtml(chosen[0].title)) + "</div>";
    html += "<div class=\"p-meta\">" + escapeHtml(boardLabel) + (answersMode === "none" ? ". Questions only." : ". Answers at the back.") + "</div>";
    html += "<div class=\"p-name\">Name <span></span></div></div>";

    chosen.forEach(function (topic) {
      const types = visibleTypes(topic);
      if (types.length === 0) {
        return;
      }
      html += "<section class=\"p-topic\"><h2>" + escapeHtml(topic.title) + "</h2>";
      types.forEach(function (type, typeIndex) {
        html += "<div class=\"p-type\"><h3>" + (typeIndex + 1) + ". " + escapeHtml(type.name) + "</h3>";
        html += "<div class=\"p-eq\">" + type.equations.map(function (equation) { return rich(equation); }).join("") + "</div>";
        if (includeMethod) {
          html += "<p class=\"p-method\">" + rich(type.method) + "</p><ul class=\"p-errors\">";
          type.commonErrors.forEach(function (error) {
            html += "<li>" + rich(error) + "</li>";
          });
          html += "</ul>";
        }
        if (includeWorked) {
          html += "<div class=\"p-worked\"><div class=\"p-label\">Worked example</div><div>" + rich(type.worked.question) + "</div>" + graphHtml(type.worked.graph) + "<ol>";
          type.worked.steps.forEach(function (step) {
            html += "<li>" + rich(step) + "</li>";
          });
          html += "</ol></div>";
        }
        visiblePractice(type).forEach(function (question, questionIndex) {
          html += "<div class=\"p-q\"><span class=\"p-qnum\">" + (typeIndex + 1) + "." + (questionIndex + 1) + "</span>" + rich(question.question) + graphHtml(question.graph);
          if (includeHints) {
            html += "<div class=\"p-hint\">Hint: " + rich(question.hint) + "</div>";
          }
          if (includeLines) {
            html += "<div class=\"p-lines\"><div></div><div></div><div></div></div>";
          }
          html += "</div>";
        });
        html += "</div>";
      });
      html += "</section>";
    });

    if (answersMode !== "none") {
      html += "<section class=\"p-answers\"><h2>Answers</h2>";
      chosen.forEach(function (topic) {
        const types = visibleTypes(topic);
        if (types.length === 0) {
          return;
        }
        html += "<h3>" + escapeHtml(topic.title) + "</h3>";
        types.forEach(function (type, typeIndex) {
          html += "<h4>" + (typeIndex + 1) + ". " + escapeHtml(type.name) + "</h4>";
          visiblePractice(type).forEach(function (question, questionIndex) {
            html += "<div class=\"p-ans\"><span class=\"p-qnum\">" + (typeIndex + 1) + "." + (questionIndex + 1) + "</span>" + answerHtml(question.answer);
            if (answersMode === "full") {
              html += "<ol>";
              question.walkthrough.forEach(function (line) {
                html += "<li>" + rich(line) + "</li>";
              });
              html += "</ol>";
            }
            html += "</div>";
          });
        });
      });
      html += "</section>";
    }

    html += "<div class=\"p-foot\">The Non-negotiables, Joshua Stafford-Haworth, JSHPhysics</div>";
    document.getElementById("print-root").innerHTML = html;
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
      writeStorage("nn-seen", "[]");
    },
  };

  boot();
}());
