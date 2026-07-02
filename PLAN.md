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
| 23   | ✅ Done   | Nachiketa rejects gold chain; 3rd boon asked; shloka 20 (yeyam prete); prēta/manushya etymology |
| 24   | ✅ Done   | Nachiketa's 3rd boon (moksha/God's control of jiva); shloka 21; dharma etymology; Yama tries to dissuade |
| 25   | ✅ Done   | Nachiketa holds firm; shlokas 21-24; Yama's temptations (sons, cattle, land, long life, kingdom, women) |
| 26   | ✅ Done   | Yama offers deva-loka pleasures; shlokas 25-28; Nachiketa's reply: all worldly things are impermanent |
| 27   | ✅ Done   | Nachiketa's argument: worldly boons impermanent; kvadhastha/naraka etymology; end of Prathamā Vallī summary |
| 28   | ✅ Done   | Yama's pedagogical method; Nachiketa's exemplary resolve; colophon: Prathamā Vallī samāptā |
| 29   | ✅ Done   | Dvitīyā Vallī begins — shlokas 1-2 (śreyas vs preyas) |
| 30   | ✅ Done   | shlokas 3-5 — śreyas/preyas, vidyā/avidyā, textual variants note |
| 31   | ✅ Done   | shlokas 6-7 — avidyā bondage, śravaṇa difficulty |
| 32   | ✅ Done   | shlokas 8-10 — ātmajñāna not by tarka, Yama praises Nachiketa |
| 33   | ✅ Done   | shlokas 11-12 — Nachiketa praised, ātman gūḍham in hṛdaya |
| 34   | ✅ Done   | shlokas 13-15 — Nachiketa praised, ātman question, OM revealed |
| 35   | ✅ Done   | shloka 16 — OM as brahman, discourse on OMkāra |
| 36   | ✅ Done   | shlokas 17-19 — OM as supreme support, ātman birthless-deathless, who kills whom |
| 37   | ✅ Done   | shlokas 20-21 — ātman subtler than subtle, Yama's supreme teaching |
| 38   | ✅ Done   | shlokas 22-24 — ātman bodiless in bodies, found only by grace, prerequisites for knowledge |
| 39   | ✅ Done   | shloka 25 + Dvitīyā Vallī colophon — Brahman's cosmic scale, end of Adhyāya 1 Vallī 2 |
| 40   | ✅ Done   | Tṛtīyā Vallī begins — shloka 1-2, two forms of Brahman in heart-cave |
| 41   | ✅ Done   | shlokas 2-4 — ātman as charioteer, body as chariot, intellect as driver |
| 42   | ✅ Done   | shlokas 5-6 — uncontrolled vs controlled horses, role of buddhi and manas |
| 43   | ✅ Done   | shlokas 7-9 — purity of mind, Vishnu's supreme abode |
| 44   | ✅ Done   | Vishnu etymology, shlokas 10-11, jīva tāratamya hierarchy |
| 45   | ✅ Done   | jīva tāratamya continued, shlokas 12-13, self-knowledge path |
| 46   | ✅ Done   | shlokas 14-15 — wake up call, Brahman beyond senses, end of Adhyāya 1 |
| 47   | ✅ Done   | shlokas 16-17, Adhyāya 1 colophon — Tṛtīyā Vallī complete |
| 48   | ✅ Done   | Adhyāya 2 Prathamā Vallī begins — shlokas 1-2, senses created outward, Dhruva analogy |
| 49   | ✅ Done   | shloka 2-2-6,7 — Yama's praise of Nachiketa, birth after death |
| 50   | ✅ Done   | shloka 2-2-7,8, shloka 3 — rebirth, sleeping Brahman, sense organs |
| 51   | ✅ Done   | shlokas 4-5 — senses, waking/dream states, Brahman as honey-eater |
| 52   | ✅ Done   | shlokas 2-2-6,7 — Hiranyagarbha/Prana creation, Aditi etymology, gender representation in Brahman |
| 53   | ✅ Done   | shloka 2-2-8 — three genders of Brahman, Arani wood analogy, guru-shishya study as churning |
| 54   | ✅ Done   | shloka 2-2-9 — Jnanayajna vs Karmayajna, cosmic order of Sun, solar deities under Brahman's control |
| 55   | ✅ Done   | shlokas 2-2-10,11 — equality of Avatara and Mula forms of Brahman, and rejection of internal divisions in Brahman |
| 56   | ✅ Done   | shlokas 2-2-12,13,14 — Angushtha-matra Purusha in heart, OM as smoke-less flame, and hill-water runoff analogy for wrong division in Brahman |
| 57   | ✅ Done   | shloka 2-2-15 — end of Adhyaya 2, Prathama Valli; soul-Brahman union analogy (mixing pure water with pure water) |
| 58   | ✅ Done   | Adhyāya 2, Dvitīyā Vallī begins — shlokas 1-2 (eleven-gated city of Brahman, and Hamsa/nature invocation) |
| 59   | ✅ Done   | Commentary on Hamsa Gayatri — pronunciation rules of Vedic Hamsa, and heart-lotus (Hritkamala) indwelling of Hamsa-Brahman |
| 60   | ✅ Done   | Commentary on Hamsa Gayatri — explanation of natural forces, Rigvedic textual variant citation (4-40-5) |
| 61   | ✅ Done   | Taittiriya Aranyaka commentary on Hamsa Gayatri, sūryopasthāna worship, and shloka 2-2-3 (Prana/Apana and Vamana in heart) |
| 62   | ✅ Done   | Commentary on shlokas 2-2-4 & 2-2-5 — three bodies of soul (gross, subtle, causal/linga), post-death journey, and Brahman as the source of life |
| 63   | ✅ Done   | Commentary on shlokas 2-2-9, 2-2-10 & 2-2-11 — Agni, Vayu, and Surya symbols (pratīkas) representing Brahman's single indwelling reality |
| 64   | ✅ Done   | Commentary on shloka 2-2-12 — one controller (vaśī) of all, inner self (antaratma), deep sleep (sushupti/nidra) bliss, and image worship (pratima) |
| 65   | ✅ Done   | Commentary on shlokas 2-2-13 & 2-2-14 — eternal among eternals (nityo nityanam), deep bliss (shanti/moksha) and ineffability of Brahman |
| 66   | ✅ Done   | Commentary on shloka 2-2-15 — Brahman as the supreme source of all light (Gita 15-6 parallel); end of Adhyaya 2, Dvitīyā Vallī |
| 67   | ✅ Done   | Commentary on shloka 2-3-1 — the cosmic Ashvattha tree (world-tree) having roots above (Brahman) and branches below |
| 68   | ✅ Done   | Ashvattha tree details continued: trunk (Brahma), major branches (Garuda/Shesha/Rudra), leaves (Vedas); commentary on shloka 2-3-2 |
| 69   | ✅ Done   | Commentary on shloka 2-3-2 continued — Brahman's terrifying power (vajra) for the wicked; parallel with Taittiriya and Gita 9-19 |
| 70   | ✅ Done   | Commentary on shlokas 2-3-3 & 2-3-4 — human body as the unique vehicle for spiritual realization; journey to Brahmaloka |
| 71   | ✅ Done   | Commentary on shlokas 2-3-5 & 2-3-6 — visual clarity of Brahman in different realms (sushupti/dreamlike vs. sathyaloka); indwelling deities |
| 72   | ✅ Done   | Commentary on shlokas 2-3-7 & 2-3-8 — hierarchy of senses, mind, intellect, and unmanifested; and definition of Purusha |
| 73   | ✅ Done   | Commentary on shloka 2-3-9 — Brahman cannot be seen by physical eyes, but by heart, intellect, and mind |
| 74   | ✅ Done   | Commentary on shloka 2-3-9 continued — the roles of mind and heart in seeing Brahman; and shloka 2-3-10 on sensory stillness |
| 75   | ✅ Done   | Commentary on shloka 2-3-11 & 2-3-12 — definition of yoga (stillness of senses), and impossibility of reaching Brahman by speech or mind |
| 76   | ✅ Done   | Commentary on shloka 2-3-13 — two paths of understanding: "He exists" (asti) and "He is the truth" (tattva-bhava) |
| 77   | ✅ Done   | Commentary on shlokas 2-3-14 & 2-3-15 — release from all desires leads to immortality; end of all heart-knots |
| 78   | ✅ Done   | Commentary on shlokas 2-3-16, 2-3-17 & 2-3-18 — 101 heart channels, Angushtha-matra Purusha, and Nachiketa obtaining brahmavidya |
| 79   | ✅ Done   | Introduction to Kannada Poetic Translation section (ಶ್ರೀ ಗೋವಿಂದ ಮಾಗಳ ಅವರ ಪ್ರಸ್ತುತಿ); and Preface (ಪ್ರಸ್ತಾವನೆ) |
| 80   | ✅ Done   | Preface continued: introduction of Yama and Nachiketa as the two primary rishis of this Upanishad |
| 81   | ✅ Done   | Adhyāya 1 Valli 1 Verse 1 & 2 translation: Vajashravas performs Vishvajit yajna and gives away cows |
| 82   | ✅ Done   | Verse 3 to 7 translation: Nachiketa notices the uselessness of the cows given and asks whom he will be given to |
| 83   | ✅ Done   | Verse 8 to 11 translation: Nachiketa arrives at Yama's house and waits for three nights without food |
| 84   | ✅ Done   | Verse 12 & 13 translation: Nachiketa asks for his second boon — the knowledge of the heavenly fire (swargyagnim) |
| 85   | ✅ Done   | Verse 14 to 16 translation: Yama teaches the fire sacrifice, names it "Nachiketagni", and offers a necklace |
| 86–93 | ✅ Done   | Verse 17 to 20 translation: Nachiketa asks the third boon (preta/manushya discussion) |
| 94–109 | ✅ Done   | Verse 21 to 29 and Adhyāya 1 Vallī 2 Verses 1 to 21 translation: Yama's temptations, Nachiketa's rejection, instruction on OMkāra |
| 110–171 | ⬜ Pending | |



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
- Pages 21–51 transcribed in prior sessions by another agent but not fully reflected in local workspace/PLAN.md. Checked latest status, hard-reset to origin/master, and resolved HEAD.lock issues.
- Page 52 transcribed and verified this session (2026-07-02), covering shlokas 2-2-6 and 2-2-7.
- New session should start fresh per chapter/section to avoid context overhead
