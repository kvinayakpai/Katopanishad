# Instruction Set: Working on a Kannada OCR File

## 1. Source Fidelity

- The printed source book is the sole authority. Any deviation in spelling, spacing, punctuation, or formatting from the book is an error.
- **Never normalise or "correct"** Kannada or Sanskrit words to standard forms if the source prints them differently. Preserve the book's exact orthography, even when it diverges from convention.
- Perfection is the only standard: mismatched quotes, missing punctuation, garbled characters, or stray spaces all count as failures.

---

## 2. Reading the Source

- **Vision-reading only.** Legacy Kannada font encoding makes raw text extraction unreliable — always read from scanned page images rather than attempting to extract text directly from the PDF or source file.
- Process **one image per tool call**. Do not batch multiple page images in a single turn.
- Open a **fresh conversation per chapter or section** to avoid context accumulation overhead and rate-limit issues.

---

## 3. OCR Correction Checklist

For every passage of Kannada text, check each of the following before finalising:

1. **Detached vowel matras** — scan for standalone vowel signs (e.g. `ೌ`, `ೀ`, `ು`, `ೂ`) appearing after a space, punctuation mark, or ZWNJ. These indicate a missing consonant that OCR dropped; restore it by cross-referencing the printed page.

2. **Subscript/insertion corrections** — printed books sometimes include handwritten or typeset late corrections as subscripts or carets. Identify these and translate them into their intended characters in the running text.

3. **Double spaces** — OCR frequently inserts extra spaces between Kannada words or syllables. Scan and remove these.

4. **Stray digits used as diacritics** — OCR sometimes substitutes Kannada digits (e.g. `೦`) for visually similar diacritics (e.g. anusvara `ಂ`). Identify and correct these.

5. **Punctuation integrity** — verify that opening and closing quotation marks match, that punctuation is neither duplicated nor missing, and that separator characters (e.g. `=` vs `-`) match the source exactly.

---

## 4. JS File Editing (if text is stored in JavaScript)

- Use a **character-by-character string walk** for finding and replacing values inside JS files — never use regex substitution (`re.sub()`), which can silently truncate content.
- Represent line breaks as literal `\n` (backslash + n, two characters) inside JS string values, not as actual newlines.
- After editing, **validate the file parses correctly** before proceeding:
  ```
  node -e "try { new Function(require('fs').readFileSync('file.js','utf-8')); console.log('OK'); } catch(e) { console.error('FAIL', e.message); }"
  ```
- Watch for **variable shadowing**: if multiple JS files are bundled, check that no downstream file re-declares the same global variable, which would silently overwrite the values you just edited.

---

## 5. Build & Verification Workflow

After every editing session, before committing:

1. **Rebuild the output bundle** from source files — never edit the generated output file directly.
2. **Sync any copies** of the output that need to match (e.g. a separate hosted copy).
3. **Run an integrity check** to verify all expected keys exist and parse correctly.
4. **Browser/render test** (recommended for any UI-touching changes) — open the output in a headless browser and assert no console errors and correct content presence.

Never commit without completing this sequence.

---

## 6. Execution Style

- Work **autonomously section by section** without mid-task check-ins. Plan → execute → log → report when fully done.
- When source content is missing or ambiguous, **do not invent or infer** — place a clear placeholder noting what is missing and ask the user which source pages to consult.
