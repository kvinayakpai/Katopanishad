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
| 19   | ✅ Done   | Ishtaka/agnikunda numerology; calendar day-counts (solar 365 8/31, lunar 355, nakshatra 324, brihaspati 390) — verified against pdftext |
| 20   | ✅ Done   | 1080 forms (360×3); Vishnu Sahasranama single-syllable names; trichikētas/triple-sandhi; Veda śākhā counts (Rig 21, Yajur 101, Sama 1000, Atharva 9 = 1131) — corrected Yajur from misread 100→101 after image zoom verification |
| 21   | ✅ Done   | Dana/tapas definitions; trichiketa upasana leading to moksha; Brahmajaj/Devaru etymology (7 meanings of 'divu' dhatu) |
| 22   | ✅ Done   | 7 meanings of 'deva' contd; shloka refs 19-1, 19-2, 16-1, 16-2; Srṃkāṃ (golden chain) as Yama's test of Nachiketa |
| 23–171 | ⬜ Pending | |

## Key encoding notes (legacy font)
- `ε`-like shape = ೩, small hook = ೬, oval = ೦ (Kannada digits in this font)
- `ꣳ` (U+A8C3) = Vedic saṃvarga used in verse quotations
- Double spaces inserted by OCR — remove them
- Detached vowel matras indicate dropped consonant — restore from image

## Session notes
- Pages 1–18 completed in prior sessions
- Page 19 status in PLAN.md was previously marked "Done" but was NOT actually present
  in kata-upanishad-text.txt — corrected this session (verified via git archive fetch
  since GitHub's web view was serving a stale cache of the repo)
- Pages 19–20 transcribed and verified this session (2026-07-01), including one
  digit correction (Yajurveda śākhā count 100→101) found via image zoom cross-check
- New session should start fresh per chapter/section to avoid context overhead
