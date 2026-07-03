# Kata Upanishad Transcription Rules

All future Antigravity agents working on this project must strictly adhere to the following behavioral and quality guidelines.

## 1. Vision-Only Source of Truth
* **NEVER** use raw text extracted from the PDF or the files in the `pdftext/` directory as the primary source of truth for Kannada text. These contain severe encoding issues and typos.
* **ALWAYS** read the page image from `pages/page_NNN.png` directly using vision models.
* If there is an overlay or overlapping duplicate text (a common artifact in this PDF), focus on the bold, primary foreground text.
* Ignore crossed-out text (words with a strike-through line running through them).

## 2. Source Fidelity (No Normalization)
* The printed source book is the sole authority. Do not attempt to "correct" or normalize Kannada or Sanskrit spellings to standard modern forms if the book prints them differently.
* Preserve punctuation, quotes, and specific formatting exactly as they appear in the scanned page.

## 3. Formatting Standards
* Every page entry in `kata-upanishad-text.txt` must be formatted exactly as follows:
  ```markdown
  [PAGE N - ಅಧ್ಯಾಯ-X, ವಲ್ಲೀ-X ಮುಂದುವರಿಕೆ]

  <transcribed text>

  ಆಧಾರ: ಬನ್ನಂಜೆ ಗೋವಿಂದಾಚಾರ್ಯ ಉಪನಿಷತ್ ಪ್ರವಚನ    Page N-1
  ```
  *(Note: N is the PDF page number, and N-1 is the printed page number in the footer, as the PDF is offset by 1 page.)*

## 4. Verification Check Before Commit
* Before committing any page to git, you **MUST** run the validation script:
  ```bash
  python verify_text.py
  ```
* Address any warnings or errors reported by the script before pushing.
* Commit after every single page or logical section to maintain a clean git history.
