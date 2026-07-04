const fs = require('fs');
const vm = require('vm');
const path = require('path');

// 1. Read and parse katopanishad-english.txt
const englishTxtPath = path.join(__dirname, '..', 'katopanishad-english.txt');
const englishTxt = fs.readFileSync(englishTxtPath, 'utf-8');

// Split the English text by page markers
const pageParts = englishTxt.split(/(\[PAGE \d+ - [^\]]+\])/);

const englishPages = {};
for (let i = 1; i < pageParts.length; i += 2) {
  const header = pageParts[i].trim();
  const body = pageParts[i + 1] ? pageParts[i + 1].trim() : '';
  
  // Extract page number from header: [PAGE N - ...]
  const match = header.match(/\[PAGE (\d+) -/);
  if (match) {
    const pageNum = parseInt(match[1], 10);
    englishPages[pageNum] = body;
  }
}

console.log(`Parsed ${Object.keys(englishPages).length} English pages from text file.`);

// 2. Read and parse katopanishad_data.js
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

// 3. Inject English content
let injectedCount = 0;
PAGES.forEach(page => {
  const num = page.num;
  if (englishPages[num]) {
    page.content_en = englishPages[num];
    injectedCount++;
  } else {
    // If not explicitly translated, we can leave it undefined so the UI falls back to summary_en
    delete page.content_en;
  }
});

console.log(`Injected content_en into ${injectedCount} out of ${PAGES.length} pages in memory.`);

// 4. Serialize PAGES array
const pagesJson = JSON.stringify(PAGES, null, 2);

// Reconstruct the file: find where const PAGES ends
// In our file, const PAGES = [...] is followed by const TIERS = [...]
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
console.log("Successfully updated katopanishad_data.js");
