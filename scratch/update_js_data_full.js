const fs = require('fs');
const vm = require('vm');
const path = require('path');

// 1. Read and parse katopanishad-english.txt
const englishTxtPath = path.join(__dirname, '..', 'katopanishad-english.txt');
const englishTxt = fs.readFileSync(englishTxtPath, 'utf-8');

// Split the English text by page/pages markers (case-insensitive, optional 's', optional dash ranges)
const pageParts = englishTxt.split(/(\[PAGE[S]?\s*\d+(?:-\d+)?\s*-\s*[^\]]+\])/i);

const englishPages = {};
for (let i = 1; i < pageParts.length; i += 2) {
  const header = pageParts[i].trim();
  const body = pageParts[i + 1] ? pageParts[i + 1].trim() : '';
  
  // Extract start and end page numbers: [PAGE N - ...] or [PAGES N-M - ...]
  const match = header.match(/\[PAGE[S]?\s*(\d+)(?:-(\d+))?\s*-\s*/i);
  if (match) {
    const start = parseInt(match[1], 10);
    const end = match[2] ? parseInt(match[2], 10) : start;
    for (let num = start; num <= end; num++) {
      englishPages[num] = body;
    }
  }
}

// 2. Propagate parent page translations to child pages that were consolidated
const propagationMap = {
  15: [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
  45: [46],
  52: [53, 54, 55, 56],
  63: [64, 65],
  73: [74]
};

for (const [parent, children] of Object.entries(propagationMap)) {
  const parentNum = parseInt(parent, 10);
  if (englishPages[parentNum]) {
    children.forEach(child => {
      if (!englishPages[child]) {
        englishPages[child] = englishPages[parentNum];
      }
    });
  }
}

console.log(`Parsed/Propagated translation content for ${Object.keys(englishPages).length} out of 171 pages.`);

// 3. Read and parse katopanishad_data.js
const dataJsPath = path.join(__dirname, '..', 'katopanishad_data.js');
let dataJs = fs.readFileSync(dataJsPath, 'utf-8');

// Load variables from JS using VM
let loadCode = dataJs;
loadCode += '\nglobal.PAGES = PAGES;\nglobal.TIERS = TIERS;\nglobal.NODES = NODES;\nglobal.EDGES = EDGES;\nglobal.GITA_CONNECTIONS = GITA_CONNECTIONS;';

const sandbox = { global: {} };
sandbox.global = sandbox;
vm.createContext(sandbox);
vm.runInContext(loadCode, sandbox);

const PAGES = sandbox.PAGES;
if (!PAGES || !Array.isArray(PAGES)) {
  console.error("Failed to load PAGES from JS data file.");
  process.exit(1);
}

// 4. Inject English content
let injectedCount = 0;
PAGES.forEach(page => {
  const num = page.num;
  if (englishPages[num]) {
    page.content_en = englishPages[num];
    injectedCount++;
  } else {
    delete page.content_en;
  }
});

console.log(`Injected content_en into ${injectedCount} out of ${PAGES.length} pages in memory.`);

// 5. Serialize PAGES array
const pagesJson = JSON.stringify(PAGES, null, 2);

// Reconstruct the file: find where const PAGES ends
const splitToken = '\nconst TIERS =';
const splitIndex = dataJs.indexOf(splitToken);
if (splitIndex === -1) {
  console.error("Could not find const TIERS separator in JS data file.");
  process.exit(1);
}

const headerPart = `// Katopanishad Knowledge Graph & Page Data\nconst PAGES = ${pagesJson};\n`;
const remainingPart = dataJs.substring(splitIndex);

// Write back
fs.writeFileSync(dataJsPath, headerPart + remainingPart, 'utf-8');
console.log("Successfully updated katopanishad_data.js with complete translations!");
