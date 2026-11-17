# Standard operating procedure — designing a topic

The author's process for every topic of the GCSE Non-negotiables revision
content. Nothing is published until every step has been done and the
findings written into the topic's build notes (`tools/<topic>_notes.md`).

1. **Draft** the non-negotiables and the tricky bits (and the key words,
   and the flashcards) as section lists; the author approves the lists.
2. **Check against the content list and the examiners' reports.** Read
   the Edexcel 1PH0 specification points for the topic and the
   examiners' reports for the papers that examine it (Paper 1: Topics 1–7;
   Paper 2: Topics 1, 8–15), at least the last three series. Confirm the
   tricky bits are the things examiners actually say candidates get
   wrong, and that nothing examiners flag is missing.
3. **Re-draft** the lists as needed.
4. **Check that every calculation and every standard written explanation
   the spec asks for is present** — each "calculate" spec point has a
   calculation type or numeric practice; each "explain" spec point has a
   model explanation and a written question.
5. **Review the drafted questions against real exam questions** (question
   papers and mark schemes) for similarity of situation, the command words
   used, and the key terms the mark schemes credit.
6. **Adjust the model answers and the questions** to that wording.
7. **Review again** after the redraft (the blind-check agent, which has not
   seen the authoring, checks answers, definitions and the explanations
   against mark-scheme wording).
8. **Adjust** if needed, then build, test headless, and publish.

Sources that work from this workspace: the Pearson examiners' reports and
mark schemes at `qualifications.pearson.com/content/dam/pdf/GCSE/Science/2016/exam-materials/`
(file names `1ph0-1h-pef-<date>.pdf` for reports, `1ph0-1h-rms-<date>.pdf`
for mark schemes, `1ph0-1h-que-<date>.pdf` for papers). Fetch with the web
tool, which reads the PDFs; `curl` is blocked by the proxy.

Conventions that come out of the reports and apply to every topic:

- Students have the **whole equation list** in the exam. Never tell them
  an equation must be memorised; the skill is selecting it.
- Calculations are laid out EWAU; model walkthroughs show the equation,
  the substitution (after converting units), the answer and the unit.
- "State what is meant by…" is answered with the mark-scheme form of
  words; the key words are bold in every model answer.
- The seven-step practical-planning recipe (Topic 1, T6) is the model
  for every "describe how you would investigate" question; each topic
  applies it to its own core practical.
