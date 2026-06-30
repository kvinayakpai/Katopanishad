# Kata Upanishad OCR Conversion Plan

## Goal
Convert all 171 pages of `kata-upanishad-e-book-V01.pdf` (Bānnanje Govindāchārya's
Katha Upanishad commentary in Kannada) into accurate Kannada text in
`kata-upanishad-text.txt`.

## Output format
- Page marker: `[PAGE N - ಅಧ್ಯಾಯ-X, ವಲ್ಲೀ-X ಮುಂದುವರಿಕೆ]`
- Footer: `ಆಧಾರ: ಬನ್ನಂಜೆ ಗೋವಿಂದಾಚಾರ್ಯ ಉಪನಿಷತ್ ಪ್ರವಚನ    Page N`
- Verse references in commentary: `(ಶ್ಲೋ-N_part)`
- Vedic saṃvarga character: `ꣳ` (U+A8C3)

## Methodology
- **Vision-reading only** — legacy CIDFont Identity-H encoding makes raw text
  extraction unreliable; always read from PyMuPDF-rendered PNG images.
- **pdftext** (`pdftext/pNNN.txt`) used only for structure/number confirmation,
  never as source of truth for Kannada text.
- **DPI strategy**: 400 DPI overview → 600–700 DPI section crops →
  900–1200 DPI for verification → 1400–2200 DPI for specific character/number zoom.
- Source book is sole authority; never normalise or "correct" spelling.

## Progress

| Page | Status    | Notes |
|------|-----------|-------|
| 1    | ✅ Done   | |
| 2    | ✅ Done   | |
| 3    | ✅ Done   | |
| 4    | ✅ Done   | |
| 5    | ✅ Done   | |
| 6    | ✅ Done   | |
| 7    | ✅ Done   | |
| 8    | ✅ Done   | |
| 9    | ✅ Done   | |
| 10   | ✅ Done   | |
| 11   | ✅ Done   | |
| 12   | ✅ Done   | |
| 13   | ✅ Done   | |
| 14   | ✅ Done   | |
| 15   | ✅ Done   | |
| 16   | ✅ Done   | |
| 17   | ✅ Done   | |
| 18   | ✅ Done   | |
| 19   | ✅ Done   | Calendar numbers (Nakṣatra ೩೨೪, Bṛhaspati ೩೯೦) from pdftext |
| 20   | 🔄 In progress | |
| 21–171 | ⬜ Pending | |

## Key encoding notes (legacy font)
- `ε`-like shape = ೩, small hook = ೬, oval = ೦ (Kannada digits in this font)
- `ꣳ` (U+A8C3) = Vedic saṃvarga used in verse quotations
- Double spaces inserted by OCR — remove them
- Detached vowel matras indicate dropped consonant — restore from image

## Session notes
- Pages 1–18 completed in prior sessions
- Page 19 completed session of 2026-06-30 (multi-session effort)
- New session should start fresh per chapter/section to avoid context overhead
