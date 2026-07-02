# Katopanishad Project — State File
Last updated: 2026-07-01

---

## Project Identity

| Field | Value |
|-------|-------|
| Name | Katopanishad (Katha Upanishad) |
| Description | Transcription of Bannanje Govindacharya's Kannada commentary on the Katha Upanishad into accurate plain text |
| Source book | Bannanje Govindacharya — Upanishat Pravachana (Katha Upanishad volume) |
| GitHub repo | `kvinayakpai/Katopanishad` |
| Branch | `master` |
| Remote URL | `https://github.com/kvinayakpai/Katopanishad.git` |

---

## Repository Structure

```
Katopanishad/
├── pages/                    ← 171 scanned PNG images (page_001.png … page_171.png)
│                                PRIMARY source for all transcription — vision-read only
├── pdftext/                  ← Raw PDF text extracts (p001.txt … p171.txt)
│                                Use ONLY for numeral/structure confirmation, never as
│                                source of truth for Kannada text
├── kata-upanishad-text.txt   ← MAIN OUTPUT — transcribed text (append-only)
├── PLAN.md                   ← Progress tracker (update after every page)
├── AGENT_GUIDELINES.md       ← Canonical instruction set for future agents
├── STATE.md                  ← This file
├── GitHub.txt                ← Git remote/token notes (local use only)
└── .gitignore
```

---

## Output Format

Every page in `kata-upanishad-text.txt` follows this structure:

```
[PAGE N - ಅಧ್ಯಾಯ-X, ವಲ್ಲೀ-X ಮುಂದುವರಿಕೆ]

<transcribed text>

ಆಧಾರ: ಬನ್ನಂಜೆ ಗೋವಿಂದಾಚಾರ್ಯ ಉಪನಿಷತ್ ಪ್ರವಚನ    Page N-1

```

Notes:
- `PAGE N` = PDF page number (1-indexed)
- `Page N-1` in the footer = the printed book page number (PDF page is offset by ~1)
- Verse references in commentary: `(ಶ್ಲೋ-N_part)` e.g. `(ಶ್ಲೋ-೧೭-೧)`
- Vedic saṃvarga character: `ꣳ` (U+A8C3)
- Section dividers at chapter/vallī end: `✦✦✦✦✦✦✦`

---

## Transcription Progress

| PDF Pages | Printed Pages | Section | Status |
|-----------|--------------|---------|--------|
| 1–7 | front matter | Title, intro, preface | ✅ Done |
| 8–28 | 7–27 | Adhyāya 1, Prathamā Vallī (shlokas 1–28) | ✅ Done |
| 29–39 | 28–38 | Adhyāya 1, Dvitīyā Vallī (shlokas 1–25) | ✅ Done |
| 40–47 | 39–46 | Adhyāya 1, Tṛtīyā Vallī (shlokas 1–17) | ✅ Done |
| 48–57 | 47–56 | Adhyāya 2, Prathamā Vallī (shlokas 1–15) | ✅ Done |
| 58–62 | 57–61 | Adhyāya 2, Dvitīyā Vallī (shlokas 1–5, Hamsa Gayatri commentary) | ✅ Done |
| 63–171 | 62–170 | Adhyāya 2, Dvitīyā Vallī continued | ⬜ Pending |

**Pages done: 62 / 171**
**Pages remaining: 109**

---

## Session Log

### Session: 2026-07-02 (this session)

**What was done:**
- Confirmed pages 53–57 have already been transcribed by previous session, covering the completion of Adhyāya 2, Prathamā Vallī (shlokas 2-2-8 to 2-2-15).
- Transcribed Pages 58–62 (printed pages 57–61) for Adhyāya 2, Dvitīyā Vallī, including shlokas 1–5, full Hamsa Gayatri commentary, and discussion on the three bodies of the soul (gross, subtle, linga).
- Appended all transcribed pages to `kata-upanishad-text.txt` and updated `PLAN.md` and `STATE.md`.

### Session: 2026-07-01 (prior session)

**What was done:**
- Diagnosed GitHub web cache issue (repo showed as "empty" in browser but was not — fetched correctly via `codeload.github.com` zip)
- Found that PLAN.md claimed page 19 was done, but content was missing from `kata-upanishad-text.txt` — corrected
- Transcribed and pushed pages 19–28 (10 pages), covering:
  - Pages 19–20: Ishtaka/agni-kunda numerology; 360/1080 forms; Veda śāಖಾ counts (Yajur corrected 100→101 after image zoom)
  - Pages 21–22: Dana/tapas; trichiketa triple-sandhi; Brahmajaj/Devaru etymology (7 meanings of 'divu')
  - Pages 23–24: Nachiketa's 3rd boon; preta/manushya etymology; dharma etymology; shloka 21
  - Pages 25–26: Shlokas 21–28; Yama's temptations (sons, cattle, land, women, kingdom)
  - Pages 27–28: Nachiketa's philosophical rejection; Prathamā Vallī colophon
- Added `AGENT_GUIDELINES.md` (canonical instruction set)
- Added `STATE.md` (this file)
- All pages pushed to `master` individually per page

**Commits 2026-07-01 (in order):**
| Commit | Content |
|--------|---------|
| `019394c` | Pages 19–20 transcription + PLAN.md fix |
| `71401dd` | Pages 21–22 |
| `71d1638` | Page 23 |
| `0b12e3f` | Page 24 |
| `bb446f0` | Page 25 |
| `9ffe307` | Page 26 |
| `07704ff` | Page 27 |
| `f4b0e73` | Page 28 |

---

## What Needs to Be Done Next

1. **Continue transcription from page 53** — this continues Adhyāya 2, Prathamā Vallī (shloka 2-2-8 onwards)
2. Follow the workflow in `AGENT_GUIDELINES.md` exactly:
   - Vision-read `pages/page_053.png` (one image per tool call)
   - Cross-check numerals and special characters against `pdftext/p053.txt`
   - Zoom-crop any shloka or tricky passage before transcribing
   - Append to `kata-upanishad-text.txt`
   - Update `PLAN.md` progress table
   - Git commit and push after every page
3. Continue until page 171

---

## Git Workflow

```bash
# Remote is already configured with token in the URL
git add kata-upanishad-text.txt PLAN.md
git commit -m "Transcribe page N (printed page M): <brief description>"
git push origin master
```

Token is stored in `GitHub.txt` locally (not committed). The remote URL embeds the token — do not re-add the remote.

To verify current remote:
```bash
git remote get-url origin
```

---

## Key Encoding Notes (Legacy Font)

| OCR artifact | Correct rendering |
|---|---|
| `ε`-like shape | ೩ (Kannada digit 3) |
| Small hook | ೬ (Kannada digit 6) |
| Oval | ೦ (Kannada digit 0) |
| `ꣳ` (U+A8C3) | Vedic saṃvarga — used in verse quotations |
| Double space between words | Remove — OCR artifact |
| Detached `ೌ`, `ೀ`, `ು` | Restore missing consonant from image |

---

## Content Policy

- Source book is sole authority — never fill gaps from general knowledge
- Never normalise Sanskrit/Kannada spelling to standard forms
- If a source page is unclear or ambiguous, place a `[NOTE: unclear — needs page N re-read]` placeholder and flag to user
