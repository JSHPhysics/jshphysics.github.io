#!/usr/bin/env node
/*
 * check_topic.js — the headless checks run on every topic page before it
 * is pushed (SOP step 8). Needs Playwright with Chromium and a local
 * server at the repo root:
 *
 *     cd <repo root> && python3 -m http.server 8791 &
 *     node gcse-non-negotiables/tools/check_topic.js forces-and-their-effects
 *
 * Options:
 *     --site <folder>       gcse-non-negotiables (default) or non-negotiables
 *     --port <n>            default 8791
 *     --shots <dir>         save screenshots of the sections named with --sections
 *     --sections a,b,c      section ids to screenshot (needs --shots)
 *     --filter <label>      also run the answer checks under this tier filter
 *
 * What it does, and what counts as a pass:
 *   1. Loads the page at 1180 px, expands every card and reports: the card
 *      numbers, KaTeX errors (must be 0), fallback maths (0), flashcards,
 *      graphs, diagrams, the progress line and the H/P badges.
 *   2. Enters every stored numeric answer (section questions and the
 *      calculation types' practice questions) through the UI and expects
 *      "Correct"; clicks every stored correct choice and expects "Correct".
 *   3. Loads the page at 390 px (phone), expands everything and checks the
 *      document does not scroll sideways (scrollWidth must equal 390; the
 *      topic pills are allowed to overflow because they scroll on their own).
 *   4. Opens the print modal and checks the notes-mode booklet is offered.
 * Exit code 1 if anything fails.
 */

const { chromium } = require("playwright");

const args = process.argv.slice(2);
const topic = args.find(function (a) { return !a.startsWith("--"); });
if (!topic) {
  console.error("usage: node check_topic.js <topic-id> [--site folder] [--port n] [--shots dir --sections a,b]");
  process.exit(2);
}
function option(name, fallback) {
  const index = args.indexOf("--" + name);
  return index >= 0 && args[index + 1] ? args[index + 1] : fallback;
}
const site = option("site", "gcse-non-negotiables");
const port = option("port", "8791");
const shots = option("shots", null);
const sections = option("sections", "").split(",").filter(Boolean);
const filterLabel = option("filter", null);
const url = "http://localhost:" + port + "/" + site + "/#" + topic;

let failed = false;
function fail(message) {
  failed = true;
  console.log("FAIL: " + message);
}

async function expandAll(page) {
  const button = page.locator("#btn-expand-all");
  if (await button.count() && await button.isVisible()) {
    await button.click();
  } else {
    await page.evaluate(function () {
      document.querySelectorAll(".collapsed").forEach(function (e) { e.classList.remove("collapsed"); });
    });
  }
  await page.waitForTimeout(600);
}

async function answerChecks(page, label) {
  // numeric: section questions and type practice questions alike
  const ids = await page.evaluate(function () {
    return Array.from(document.querySelectorAll(".question[data-qid]"))
      .filter(function (e) { return e.querySelector("input") && e.querySelector("[data-check]"); })
      .map(function (e) { return e.getAttribute("data-qid"); });
  });
  let ok = 0;
  const bad = [];
  for (const id of ids) {
    const question = await page.evaluate(function (i) { return window.nn.findQuestion(i); }, id);
    if (!question || !question.answer) {
      continue;
    }
    const block = page.locator('[data-qid="' + id + '"]');
    await block.locator("input").first().fill(String(question.answer.value));
    await block.locator("[data-check]").click();
    const feedback = (await block.locator("[data-feedback]").textContent()).trim();
    if (feedback === "Correct") {
      ok += 1;
    } else {
      bad.push(id + ": " + feedback);
    }
  }
  console.log(label + " numeric " + ok + " of " + ids.length + (bad.length ? " " + JSON.stringify(bad) : ""));
  if (bad.length) {
    fail("numeric answers not marked correct");
  }

  const choiceIds = await page.evaluate(function () {
    return Array.from(document.querySelectorAll(".question.type-choice")).map(function (e) { return e.getAttribute("data-qid"); });
  });
  let choiceOk = 0;
  const choiceBad = [];
  for (const id of choiceIds) {
    const question = await page.evaluate(function (i) { return window.nn.findQuestion(i); }, id);
    const block = page.locator('[data-qid="' + id + '"]');
    await block.locator("[data-choice]").nth(question.correct).click();
    const feedback = (await block.locator("[data-feedback]").textContent()).trim();
    if (feedback === "Correct") {
      choiceOk += 1;
    } else {
      choiceBad.push(id);
    }
  }
  console.log(label + " choice " + choiceOk + " of " + choiceIds.length + (choiceBad.length ? " " + JSON.stringify(choiceBad) : ""));
  if (choiceBad.length) {
    fail("choice answers not marked correct");
  }
}

(async function () {
  const browser = await chromium.launch();

  // 1 + 2: desktop
  const page = await browser.newPage({ viewport: { width: 1180, height: 900 } });
  const errors = [];
  page.on("pageerror", function (e) { errors.push(e.message); });
  page.on("console", function (m) {
    if (m.type() === "error" && !m.text().includes("googleapis")) {
      errors.push("console: " + m.text());
    }
  });
  await page.goto(url);
  await page.waitForTimeout(2500);
  await expandAll(page);
  const info = await page.evaluate(function () {
    return {
      nums: Array.from(document.querySelectorAll(".skill-head .num")).map(function (e) { return e.textContent; }).join(" "),
      katexErr: document.querySelectorAll(".katex-error").length,
      fallback: document.querySelectorAll(".math-fallback").length,
      facts: document.querySelectorAll("[data-fact]").length,
      graphs: document.querySelectorAll("figure.graph").length,
      diagrams: document.querySelectorAll("figure.diagram").length,
      refs: document.querySelectorAll(".ref-btn").length,
      progress: (document.querySelector(".progress-line span") || {}).textContent,
      badges: Array.from(document.querySelectorAll(".skill-head .badge")).map(function (e) { return e.textContent; }).join(""),
    };
  });
  console.log(JSON.stringify(info));
  if (info.katexErr) { fail(info.katexErr + " KaTeX errors"); }
  if (info.fallback) { fail(info.fallback + " maths fallbacks"); }
  await answerChecks(page, "desktop");

  if (filterLabel) {
    const control = page.locator("select").first();
    if (await control.count()) {
      await control.selectOption({ label: filterLabel });
    } else {
      await page.locator("text=" + filterLabel).first().click();
    }
    await page.waitForTimeout(800);
    await expandAll(page);
    const filtered = await page.evaluate(function () {
      return Array.from(document.querySelectorAll(".skill-head .num")).map(function (e) { return e.textContent; }).join(" ");
    });
    console.log("under " + filterLabel + ": " + filtered);
    await answerChecks(page, filterLabel);
  }

  if (shots && sections.length) {
    await page.addStyleTag({ content: ".topbar, .skillbar { position: static !important; } .skill-body { transition: none !important; }" });
    for (const id of sections) {
      const target = page.locator("#section-" + id);
      if (await target.count()) {
        await target.screenshot({ path: shots.replace(/\/$/, "") + "/" + topic + "_" + id + ".png" });
      } else {
        fail("no section " + id + " to screenshot");
      }
    }
  }
  if (errors.length) { fail("page errors: " + JSON.stringify(errors)); }
  await page.close();

  // 3: phone width
  const phone = await browser.newPage({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
  const phoneErrors = [];
  phone.on("pageerror", function (e) { phoneErrors.push(e.message); });
  await phone.goto(url);
  await phone.waitForTimeout(2500);
  await expandAll(phone);
  const over = await phone.evaluate(function () {
    const width = document.documentElement.clientWidth;
    const bad = [];
    document.querySelectorAll("body *").forEach(function (e) {
      // the topic pills, equation strips and display maths scroll inside their own boxes
      // (.katex-mathml is the hidden MathML copy KaTeX keeps for screen readers)
      if (e.closest(".pills, .topic-pills, .formulas, .katex-display, table.tbl, .katex-mathml")) { return; }
      const r = e.getBoundingClientRect();
      if (r.right > width + 2 && r.width > 0) {
        bad.push(e.tagName + "." + e.className.toString().slice(0, 40));
      }
    });
    let widestCard = 0;
    document.querySelectorAll("article.skill").forEach(function (card) {
      widestCard = Math.max(widestCard, Math.round(card.getBoundingClientRect().width));
    });
    return { scrollW: document.documentElement.scrollWidth, width: width, widestCard: widestCard, bad: bad.slice(0, 8) };
  });
  console.log("phone " + JSON.stringify(over));
  if (over.scrollW > over.width) { fail("page scrolls sideways at 390 px"); }
  if (over.widestCard > over.width) { fail("a card is wider than the phone screen (" + over.widestCard + " px) — content is being clipped"); }
  if (phoneErrors.length) { fail("phone page errors: " + JSON.stringify(phoneErrors)); }
  await phone.close();

  // 4: booklet modal
  const print = await browser.newPage({ viewport: { width: 1180, height: 900 } });
  await print.goto(url);
  await print.waitForTimeout(2000);
  const printButton = print.locator("#btn-print, [data-print]").first();
  if (await printButton.count()) {
    await printButton.click();
    await print.waitForTimeout(500);
    const hasNotes = await print.evaluate(function () { return document.body.innerText.includes("Notes, method and common errors"); });
    console.log("booklet modal offers notes mode: " + hasNotes);
    if (!hasNotes) { fail("booklet modal does not offer the notes mode"); }
  } else {
    fail("no print button");
  }
  await print.close();

  await browser.close();
  console.log(failed ? "RESULT: FAIL" : "RESULT: PASS");
  process.exit(failed ? 1 : 0);
})();
