# -*- coding: utf-8 -*-
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

new_js = r"""// UI State
let activeView = 'browse';
let currentFocusPage = 1;
let currentLanguage = 'kn';

// Tab switching
const tabs = ['browse', 'focus', 'chapters', 'map', 'chat'];
tabs.forEach(tab => {
  document.getElementById(`tab-${tab}`).addEventListener('click', () => {
    switchView(tab);
  });
});

function switchView(viewName) {
  activeView = viewName;
  tabs.forEach(tab => {
    const btn = document.getElementById(`tab-${tab}`);
    const view = document.getElementById(`view-${tab}`);
    if (tab === viewName) {
      btn.classList.add('on');
      view.classList.remove('hidden');
    } else {
      btn.classList.remove('on');
      view.classList.add('hidden');
    }
  });
  
  if (viewName === 'focus') {
    renderFocusPage();
  }
}

// UI Translations dictionary
const UI_TRANSLATIONS = {
  kn: {
    brand_name: 'ಕಠೋಪನಿಷತ್ · <em>ತತ್ವ ಜಲಂ</em>',
    brand_crumb: 'ಬನ್ನಂಜೆ ಗೋವಿಂದಾಚಾರ್ಯ',
    tab_browse: 'ವಿಷಯ ಸೂಚಿ',
    tab_focus: 'ಏಕಾಗ್ರತೆ',
    tab_chapters: 'ಅಧ್ಯಾಯಗಳು',
    tab_map: 'ನಕ್ಷೆ',
    tab_chat: 'ಚರ್ಚೆ',
    search_placeholder: 'ಪುಟಗಳು, ಶ್ಲೋಕಗಳು, ಪರಿಕಲ್ಪನೆಗಳನ್ನು ಹುಡುಕಿ...',
    sec_intro: 'ಪ್ರಸ್ತಾವನೆ ಮತ್ತು ಶಾಂತಿಪಾಠ',
    sec_commentary: 'ಕನ್ನಡ ವಿವರಣೆ ಮತ್ತು ತಾತ್ಪರ್ಯ',
    sec_poetic: 'ಕನ್ನಡ ಪದ್ಯರೂಪ',
    sec_sanskrit: 'ಮೂಲ ಸಂಸ್ಕೃತ ಶ್ಲೋಕಗಳು',
    sec_c11: 'ಅಧ್ಯಾಯ ೧ - ವಲ್ಲಿ ೧',
    sec_c12: 'ಅಧ್ಯಾಯ ೧ - ವಲ್ಲಿ ೨',
    sec_c13: 'ಅಧ್ಯಾಯ ೧ - ವಲ್ಲಿ ೩',
    sec_c21: 'ಅಧ್ಯಾಯ ೨ - ವಲ್ಲಿ ೧',
    sec_c22: 'ಅಧ್ಯಾಯ ೨ - ವಲ್ಲಿ ೨',
    sec_c23: 'ಅಧ್ಯಾಯ ೨ - ವಲ್ಲಿ ೩',
    footer_stats: 'ಕಠೋಪನಿಷತ್ ವೀಕ್ಷಕ • 171 ಪುಟಗಳು • 5657 ಸಾಲುಗಳು',
    welcome_chat: 'ಹರೇ ಕೃಷ್ಣ! ಕಠೋಪನಿಷತ್ ಸಂಶೋಧಕಕ್ಕೆ ಸುಸ್ವಾಗತ. ಜೀವನ, ಮರಣ ಮತ್ತು ಆತ್ಮಜ್ಞಾನದ ಆಳವಾದ ರಹಸ್ಯಗಳನ್ನು ಅನ್ವೇಷಿಸಲು ಕೆಳಗಿನ ಪ್ರಶ್ನೆಗಳಲ್ಲಿ ಒಂದನ್ನು ಆರಿಸಿ.',
    chat_suggestions: [
      { text: "ನಚಿಕೇತನ ಮೂರು ವರಗಳು ಯಾವುವು?", label: "ಮೂರು ವರಗಳು" },
      { text: "ರಥದ ರೂಪಕವನ್ನು ವಿವರಿಸಿ.", label: "ರಥದ ರೂಪಕ" },
      { text: "ಶ್ರೇಯಸ್ಸು ಮತ್ತು ಪ್ರೇಯಸ್ಸು ಎಂದರೇನು?", label: "ಶ್ರೇಯಸ್ಸು vs ಪ್ರೇಯಸ್ಸು" },
      { text: "ಕಠೋಪನಿಷತ್ತಿನಲ್ಲಿ ಯೋಗವನ್ನು ಹೇಗೆ ವ್ಯಾಖ್ಯಾನಿಸಲಾಗಿದೆ?", label: "ಯೋಗದ ವ್ಯಾಖ್ಯಾನ" }
    ],
    defaultResponse: "ಕಠೋಪನಿಷತ್ ಬಗ್ಗೆ ಯಾವುದೇ ಪ್ರಶ್ನೆಗಳನ್ನು ವಿವರಿಸಲು ನಾನು ಸಂತೋಷಪಡುತ್ತೇನೆ!"
  },
  en: {
    brand_name: 'Katopanishad · <em>Tatva Jalam</em>',
    brand_crumb: 'Bannanje Govindacharya',
    tab_browse: 'Browse',
    tab_focus: 'Focus',
    tab_chapters: 'Chapters',
    tab_map: 'Map',
    tab_chat: 'Chat',
    search_placeholder: 'Search pages, verses, concepts...',
    sec_intro: 'Introduction & Shantipatha',
    sec_commentary: 'Kannada Exposition & Commentary',
    sec_poetic: 'Kannada Poetic Translation',
    sec_sanskrit: 'Original Sanskrit Shlokas',
    sec_c11: 'Adhyaya 1 - Valli 1',
    sec_c12: 'Adhyaya 1 - Valli 2',
    sec_c13: 'Adhyaya 1 - Valli 3',
    sec_c21: 'Adhyaya 2 - Valli 1',
    sec_c22: 'Adhyaya 2 - Valli 2',
    sec_c23: 'Adhyaya 2 - Valli 3',
    footer_stats: 'Katopanishad Viewer • 171 Pages • 5657 Lines',
    welcome_chat: 'Hare Krishna! Welcome to the Katopanishad explorer. Choose a question below or search to discover the deep mysteries of life, death, and self-knowledge.',
    chat_suggestions: [
      { text: "What are Nachiketa's three boons?", label: "3 Boons" },
      { text: "Explain the Chariot Metaphor.", label: "Chariot Metaphor" },
      { text: "What is Shreyas vs Preyas?", label: "Shreyas vs Preyas" },
      { text: "How is Yoga defined in Katopanishad?", label: "Definition of Yoga" }
    ],
    defaultResponse: "I'm happy to help explain anything about the Katopanishad!"
  }
};

function updateLanguage(lang) {
  currentLanguage = lang;
  
  // Set class on body for CSS styling
  document.body.className = `lang-${lang}`;
  
  // Update header text
  document.querySelector('header .brand .name').innerHTML = UI_TRANSLATIONS[lang].brand_name;
  document.querySelector('header .brand .crumb').textContent = UI_TRANSLATIONS[lang].brand_crumb;
  
  // Update tab buttons
  document.getElementById('tab-browse').textContent = UI_TRANSLATIONS[lang].tab_browse;
  document.getElementById('tab-focus').textContent = UI_TRANSLATIONS[lang].tab_focus;
  document.getElementById('tab-chapters').textContent = UI_TRANSLATIONS[lang].tab_chapters;
  document.getElementById('tab-map').textContent = UI_TRANSLATIONS[lang].tab_map;
  document.getElementById('tab-chat').textContent = UI_TRANSLATIONS[lang].tab_chat;
  
  // Update search input placeholder
  document.getElementById('search-input').placeholder = UI_TRANSLATIONS[lang].search_placeholder;
  
  // Update section titles in Browse view
  const browseTitles = document.querySelectorAll('#view-browse .section-title');
  if (browseTitles.length >= 4) {
    browseTitles[0].textContent = UI_TRANSLATIONS[lang].sec_intro;
    browseTitles[1].textContent = UI_TRANSLATIONS[lang].sec_commentary;
    browseTitles[2].textContent = UI_TRANSLATIONS[lang].sec_poetic;
    browseTitles[3].textContent = UI_TRANSLATIONS[lang].sec_sanskrit;
  }
  
  // Update section titles in Chapters view
  const chapterTitles = document.querySelectorAll('#view-chapters .section-title');
  if (chapterTitles.length >= 6) {
    chapterTitles[0].textContent = UI_TRANSLATIONS[lang].sec_c11;
    chapterTitles[1].textContent = UI_TRANSLATIONS[lang].sec_c12;
    chapterTitles[2].textContent = UI_TRANSLATIONS[lang].sec_c13;
    chapterTitles[3].textContent = UI_TRANSLATIONS[lang].sec_c21;
    chapterTitles[4].textContent = UI_TRANSLATIONS[lang].sec_c22;
    chapterTitles[5].textContent = UI_TRANSLATIONS[lang].sec_c23;
  }
  
  // Update footer stats
  document.querySelector('footer span').textContent = UI_TRANSLATIONS[lang].footer_stats;
  
  // Update chat suggestions and welcome message
  const chatBox = document.getElementById('chat-box');
  chatBox.innerHTML = `<div class="chat-bubble bot">${UI_TRANSLATIONS[lang].welcome_chat}</div>`;
  
  const suggestionsDiv = document.querySelector('.chat-suggestions');
  suggestionsDiv.innerHTML = '';
  UI_TRANSLATIONS[lang].chat_suggestions.forEach(s => {
    const chip = document.createElement('div');
    chip.className = 'suggestion-chip';
    chip.textContent = s.label;
    chip.addEventListener('click', () => {
      askQuestion(s.text);
    });
    suggestionsDiv.appendChild(chip);
  });
  
  // Re-render components with the new language state
  renderPageLists();
  renderFocusPage();
  renderMap();
  renderConceptDetails(selectedConceptId);
}

// Render Page lists
function renderPageLists() {
  const lists = {
    intro: document.getElementById('list-intro'),
    commentary: document.getElementById('list-commentary'),
    poetic: document.getElementById('list-poetic'),
    sanskrit: document.getElementById('list-sanskrit'),
    
    // Chapters
    c11: document.getElementById('list-c11'),
    c12: document.getElementById('list-c12'),
    c13: document.getElementById('list-c13'),
    c21: document.getElementById('list-c21'),
    c22: document.getElementById('list-c22'),
    c23: document.getElementById('list-c23')
  };
  
  // Clear lists
  Object.values(lists).forEach(list => {
    if (list) list.innerHTML = '';
  });
  
  PAGES.forEach(page => {
    const item = document.createElement('div');
    item.className = 'page-item';
    const titleText = currentLanguage === 'en' ? page.title_en : page.title;
    item.innerHTML = `
      <span class="title">${page.num}. ${titleText}</span>
      <span class="badge">Page ${page.num}</span>
    `;
    item.addEventListener('click', () => {
      currentFocusPage = page.num;
      switchView('focus');
    });
    
    // Categorize
    if (page.num <= 7) {
      lists.intro.appendChild(item.cloneNode(true));
    } else if (page.num <= 76) {
      lists.commentary.appendChild(item.cloneNode(true));
    } else if (page.num <= 154) {
      lists.poetic.appendChild(item.cloneNode(true));
    } else {
      lists.sanskrit.appendChild(item.cloneNode(true));
    }
    
    // Map to chapter lists
    const chapItem = item.cloneNode(true);
    chapItem.addEventListener('click', () => {
      currentFocusPage = page.num;
      switchView('focus');
    });
    
    // Chapter mapping by page ranges
    if (page.num >= 8 && page.num <= 27) lists.c11.appendChild(chapItem);
    if (page.num >= 28 && page.num <= 38) lists.c12.appendChild(chapItem);
    if (page.num >= 39 && page.num <= 46) lists.c13.appendChild(chapItem);
    if (page.num >= 47 && page.num <= 56) lists.c21.appendChild(chapItem);
    if (page.num >= 57 && page.num <= 65) lists.c22.appendChild(chapItem);
    if (page.num >= 66 && page.num <= 76) lists.c23.appendChild(chapItem);
    
    // Also include poetic equivalents in chapters for comprehensive view
    if (page.num >= 79 && page.num <= 97) lists.c11.appendChild(chapItem.cloneNode(true));
    if (page.num >= 98 && page.num <= 111) lists.c12.appendChild(chapItem.cloneNode(true));
    if (page.num >= 112 && page.num <= 120) lists.c13.appendChild(chapItem.cloneNode(true));
    if (page.num >= 121 && page.num <= 131) lists.c21.appendChild(chapItem.cloneNode(true));
    if (page.num >= 132 && page.num <= 141) lists.c22.appendChild(chapItem.cloneNode(true));
    if (page.num >= 142 && page.num <= 154) lists.c23.appendChild(chapItem.cloneNode(true));
    
    // Sanskrit shlokas chapter mapping
    if (page.num >= 156 && page.num <= 159) lists.c11.appendChild(chapItem.cloneNode(true));
    if (page.num >= 160 && page.num <= 162) lists.c12.appendChild(chapItem.cloneNode(true));
    if (page.num >= 163 && page.num <= 164) lists.c13.appendChild(chapItem.cloneNode(true));
    if (page.num >= 165 && page.num <= 166) lists.c21.appendChild(chapItem.cloneNode(true));
    if (page.num >= 167 && page.num <= 168) lists.c22.appendChild(chapItem.cloneNode(true));
    if (page.num >= 169 && page.num <= 171) lists.c23.appendChild(chapItem.cloneNode(true));
  });
}

// Render Focus page
function renderFocusPage() {
  const page = PAGES.find(p => p.num === currentFocusPage);
  if (!page) return;
  
  const pageTitle = currentLanguage === 'en' ? page.title_en : page.title;
  document.getElementById('focus-title').textContent = `${page.num}. ${pageTitle}`;
  const textField = document.getElementById('focus-text');
  
  if (currentLanguage === 'en') {
    textField.className = 'body-text large-font';
    let htmlContent = `
      <div style="background: rgba(158, 58, 26, 0.05); border-left: 4px solid var(--rust); padding: 16px; margin-bottom: 24px; border-radius: 4px; font-family: 'Inter', sans-serif; font-size: 16px; line-height: 1.6; color: var(--ink-soft);">
        <strong style="color: var(--rust); display: block; margin-bottom: 6px; font-size: 12px; text-transform: uppercase; letter-spacing: 1px;">English Summary & Translation</strong>
        ${page.summary_en}
      </div>
      <div style="opacity: 0.85; font-size: 15px; border-top: 1px dashed var(--rule); padding-top: 16px;">
        <strong style="color: var(--ink-fade); display: block; margin-bottom: 8px; font-size: 11px; text-transform: uppercase; letter-spacing: 1.5px;">Original Kannada / Sanskrit</strong>
        ${page.content.replace(/\n/g, '<br>')}
      </div>
    `;
    textField.innerHTML = htmlContent;
  } else {
    textField.className = 'body-text';
    textField.textContent = page.content;
  }
}

// Focus navigation
document.getElementById('focus-prev').addEventListener('click', () => {
  if (currentFocusPage > 1) {
    currentFocusPage--;
    renderFocusPage();
  }
});
document.getElementById('focus-next').addEventListener('click', () => {
  if (currentFocusPage < PAGES.length) {
    currentFocusPage++;
    renderFocusPage();
  }
});

// Search functionality
document.getElementById('search-input').addEventListener('input', (e) => {
  const query = e.target.value.toLowerCase().trim();
  
  // Filter lists in view
  document.querySelectorAll('.page-item').forEach(item => {
    const title = item.querySelector('.title').textContent.toLowerCase();
    const pageNum = item.querySelector('.badge').textContent.toLowerCase();
    if (title.includes(query) || pageNum.includes(query)) {
      item.style.display = 'flex';
    } else {
      item.style.display = 'none';
    }
  });
});

// Language toggle
document.getElementById('btn-lang-kn').addEventListener('click', () => {
  updateLanguage('kn');
  document.getElementById('btn-lang-kn').classList.add('on');
  document.getElementById('btn-lang-en').classList.remove('on');
});

document.getElementById('btn-lang-en').addEventListener('click', () => {
  updateLanguage('en');
  document.getElementById('btn-lang-en').classList.add('on');
  document.getElementById('btn-lang-kn').classList.remove('on');
});

// Ontology Map & Nodes layout
let selectedConceptId = null;

const NODE_POSITIONS = {
  purusha: { x: 400, y: 50 },
  atman: { x: 250, y: 150 },
  preta_vicikitsa: { x: 100, y: 250 },
  shreyas: { x: 400, y: 250 },
  preyas: { x: 250, y: 350 },
  nachiketa_agni: { x: 550, y: 150 },
  yoga_definition: { x: 550, y: 350 },
  ratha_metaphor: { x: 700, y: 250 },
  buddhi: { x: 600, y: 450 },
  manas: { x: 400, y: 450 },
  indriya: { x: 200, y: 450 },
  moksha: { x: 700, y: 100 }
};

function renderMap() {
  const edgesG = document.getElementById('map-edges');
  const nodesG = document.getElementById('map-nodes');
  
  edgesG.innerHTML = '';
  nodesG.innerHTML = '';
  
  // Draw relationship lines (edges)
  EDGES.forEach(edge => {
    const sPos = NODE_POSITIONS[edge.source];
    const tPos = NODE_POSITIONS[edge.target];
    if (sPos && tPos) {
      const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
      path.setAttribute('d', `M ${sPos.x} ${sPos.y} L ${tPos.x} ${tPos.y}`);
      path.setAttribute('stroke', '#7a6c54');
      path.setAttribute('stroke-width', '2');
      path.setAttribute('fill', 'none');
      path.setAttribute('marker-end', 'url(#arrow)');
      path.className.baseVal = 'map-edge';
      edgesG.appendChild(path);
      
      // Add text label for relation
      const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
      text.setAttribute('x', (sPos.x + tPos.x) / 2);
      text.setAttribute('y', (sPos.y + tPos.y) / 2 - 5);
      text.setAttribute('font-size', '9');
      text.setAttribute('fill', '#4a3f30');
      text.setAttribute('text-anchor', 'middle');
      text.textContent = edge.label;
      edgesG.appendChild(text);
    }
  });
  
  // Draw concept circles (nodes)
  NODES.forEach(node => {
    const pos = NODE_POSITIONS[node.id];
    if (pos) {
      const g = document.createElementNS('http://www.w3.org/2000/svg', 'g');
      g.setAttribute('transform', `translate(${pos.x}, ${pos.y})`);
      g.className.baseVal = 'map-node';
      g.style.cursor = 'pointer';
      
      const color = `var(--t-${node.tier})`;
      
      const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
      circle.setAttribute('r', '20');
      circle.setAttribute('fill', '#fbf5e6');
      circle.setAttribute('stroke', color);
      circle.setAttribute('stroke-width', '4');
      g.appendChild(circle);
      
      const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
      text.setAttribute('y', '35');
      text.setAttribute('text-anchor', 'middle');
      text.setAttribute('font-size', '12');
      text.setAttribute('font-weight', '700');
      text.setAttribute('fill', '#1f1a13');
      text.textContent = currentLanguage === 'kn' ? node.kn : node.en;
      g.appendChild(text);
      
      g.addEventListener('click', () => {
        selectConcept(node.id);
      });
      
      nodesG.appendChild(g);
    }
  });
}

function selectConcept(id) {
  selectedConceptId = id;
  const panel = document.getElementById('concept-details-panel');
  panel.classList.add('active');
  renderConceptDetails(id);
}

function renderConceptDetails(id) {
  if (!id) return;
  const node = NODES.find(n => n.id === id);
  if (!node) return;
  
  const badge = document.getElementById('concept-badge-field');
  badge.textContent = node.tier;
  badge.style.setProperty('--color', `var(--t-${node.tier})`);
  
  document.getElementById('concept-title-field').textContent = currentLanguage === 'kn' ? node.title.kn : node.title.en;
  document.getElementById('concept-desc-field').textContent = currentLanguage === 'kn' ? node.note.kn : node.note.en;
  
  // Render linked pages
  const linksField = document.getElementById('concept-links-field');
  linksField.innerHTML = '';
  
  // Parse page list from note refs (e.g., "Page 12 · Page 82")
  const pagesList = node.refs.split('·').map(p => parseInt(p.replace(/[^\d]/g, '')));
  pagesList.forEach(pNum => {
    const link = document.createElement('a');
    link.className = 'concept-link';
    link.textContent = `Page ${pNum}`;
    link.addEventListener('click', () => {
      currentFocusPage = pNum;
      switchView('focus');
    });
    linksField.appendChild(link);
  });
}

// Chat responses mapping
const CHAT_RESPONSES = {
  kn: {
    "ನಚಿಕೇತನ ಮೂರು ವರಗಳು ಯಾವುವು?": "ನಚಿಕೇತನು ಯಮಧರ್ಮನಿಂದ ಮೂರು ವರಗಳನ್ನು ಕೇಳಿದನು:\n1. **ಮೊದಲನೇ ವರ (ಪಿತೃ ಪ್ರಸಾದ)**: ತಾನು ಹಿಂತಿರುಗಿದಾಗ ತಂದೆ ಉದ್ದಾಲಕ ಗೌತಮನು ಪ್ರಶಾಂತನಾಗಿರಬೇಕು ಮತ್ತು ತನ್ನ ಮೇಲಿನ ಸಿಟ್ಟು ದೂರವಾಗಬೇಕು.\n2. **ಎರಡನೇ ವರ (ಸ್ವರ್ಗ್ಯ ಅಗ್ನಿ ವಿದ್ಯಾ)**: ಸ್ವರ್ಗಲೋಕ ಮತ್ತು ಅಮೃತತ್ವಕ್ಕೆ ಕಾರಣವಾಗುವ ಪವಿತ್ರ ಅಗ್ನಿಯ ಯಜ್ಞ ವಿಧಾನದ ಜ್ಞಾನ.\n3. **ಮೂರನೇ ವರ (ಆತ್ಮಜ್ಞಾನ)**: ಮರಣದ ನಂತರ ಜೀವಿಯು ಇರುತ್ತಾನೋ ಇಲ್ಲವೋ ಎಂಬ ರಹಸ್ಯ (ಪ್ರೇತ ವಿಚಿಕಿತ್ಸಾ) ಹಾಗೂ ಆತ್ಮ ತತ್ವದ ಜ್ಞಾನ.",
    "ರಥದ ರೂಪಕವನ್ನು ವಿವರಿಸಿ.": "ಕಠೋಪನಿಷತ್ತಿನ (೧.೩.೩-೪) ರಥದ ರೂಪಕವು ಆತ್ಮಸಾಕ್ಷಾತ್ಕಾರದ ಹಾದಿಯನ್ನು ವಿವರಿಸುತ್ತದೆ:\n- **ರಥಿಕ (ಯಜಮಾನ)**: ಆತ್ಮನ್ (ಜೀವ)\n- **ರಥ**: ಶರೀರ\n- **ಸಾರಥಿ**: ಬುದ್ಧಿ\n- **ಕಡಿವಾಣ (ಹಗ್ಗ)**: ಮನಸ್ಸು\n- **ಕುದುರೆಗಳು**: ಇಂದ್ರಿಯಗಳು\n- **ದಾರಿಗಳು (ವಿಷಯಗಳು)**: ಶಬ್ದ, ಸ್ಪರ್ಶ, ರೂಪ ಮುಂತಾದ ಭೋಗವಿಷಯಗಳು.\nಬುದ್ಧಿಯಿಂದ ಮನಸ್ಸನ್ನು ನಿಯಂತ್ರಿಸಿದಾಗ ಇಂದ್ರಿಯಗಳು ಒಳ್ಳೆಯ ಕುದುರೆಗಳಂತೆ ವರ್ತಿಸಿ ಮೋಕ್ಷಕ್ಕೆ ಕೊಂಡೊಯ್ಯುತ್ತವೆ.",
    "ಶ್ರೇಯಸ್ಸು ಮತ್ತು ಪ್ರೇಯಸ್ಸು ಎಂದರೇನು?": "ಯಮನು ೧.೨.೧ ರಲ್ಲಿ ಮನುಷ್ಯನಿಗೆ ಲಭ್ಯವಿರುವ ಎರಡು ಮಾರ್ಗಗಳನ್ನು ವಿವರಿಸುತ್ತಾನೆ:\n- **ಶ್ರೇಯೋಮಾರ್ಗ (ಆತ್ಮಕಲ್ಯಾಣ)**: ಇದು ಶಾಶ್ವತ ಆತ್ಮೋದ್ಧಾರ ಮತ್ತು ಮುಕ್ತಿಗೆ ಕಾರಣವಾಗುತ್ತದೆ. ಇದಕ್ಕೆ ಇಂದ್ರಿಯ ಸಂಯಮ ಮತ್ತು ವಿವೇಚನೆ ಅಗತ್ಯ.\n- **ಪ್ರೇಯೋಮಾರ್ಗ (ಭೋಗಮಾರ್ಗ)**: ಇದು ತಾತ್ಕಾಲಿಕ ಇಂದ್ರಿಯ ಸುಖಗಳನ್ನು ನೀಡುತ್ತದೆ. ಆದರೆ ಜೀವಿಯನ್ನು ಸಂಸಾರ ಚಕ್ರದಲ್ಲಿ ಬಂಧಿಸುತ್ತದೆ.",
    "ಕಠೋಪನಿಷತ್ತಿನಲ್ಲಿ ಯೋಗವನ್ನು ಹೇಗೆ ವ್ಯಾಖ್ಯಾನಿಸಲಾಗಿದೆ?": "ಕಠೋಪನಿಷತ್ತಿನ ೨.೩.೧೧ ರಲ್ಲಿ ಯೋಗವನ್ನು ಹೀಗೆ ವ್ಯಾಖ್ಯಾನಿಸಲಾಗಿದೆ:\n* ಇಂದ್ರಿಯಗಳು, ಮನಸ್ಸು ಮತ್ತು ಬುದ್ಧಿಯು ಚಂಚಲತೆಯಿಲ್ಲದೆ ಸ್ಥಿರವಾಗುವ ಸ್ಥಿತಿಯೇ ಯೋಗ ('ಸ್ಥಿರಾಂ ಇಂದ್ರಿಯಧಾರಣಾಂ').\n* ಈ ಸ್ಥಿತಿಯಲ್ಲಿ ಯೋಗಿಯು ಅಪ್ರಮತ್ತನಾಗಿರುತ್ತಾನೆ (ಎಚ್ಚರದಿಂದಿರುತ್ತಾನೆ)."
  },
  en: {
    "What are Nachiketa's three boons?": "Nachiketa requested three boons from Lord Yama:\n1. **First Boon (Paternal Peace)**: That his father Uddalaka Gautama be peaceful, satisfied, and free from anger towards him upon his return.\n2. **Second Boon (Swargya Agni)**: The knowledge of the sacred fire sacrifice that leads to the heavenly realm and immortality.\n3. **Third Boon (Self-Knowledge)**: The answer to the mystery of death (Preta Vicikitsa) — does the soul exist after death or not?",
    "Explain the Chariot Metaphor.": "In Kata Upanishad (1.3.3-4), Yama explains the chariot metaphor to describe the path to self-realization:\n- **Chariot Owner (Rathi)**: The Atman (individual self).\n- **Chariot (Ratha)**: The Physical Body.\n- **Charioteer (Sarathi)**: The Intellect (Buddhi).\n- **Reins (Pragraha)**: The Mind (Manas).\n- **Horses (Haya)**: The Senses (Indriyas).\n- **Paths (Gocara)**: The Sense Objects.\nWhen the mind is controlled by the intellect, the senses behave like good horses and lead the soul to liberation.",
    "What is Shreyas vs Preyas?": "Yama teaches in verse 1.2.1 that there are two distinct paths available to mankind:\n- **Shreyas (The Good/Spiritual)**: Leads to eternal spiritual welfare, liberation, and peace. It requires discrimination and self-control.\n- **Preyas (The Pleasant/Materialistic)**: Leads to temporary sensory pleasures. It binds the soul to the worldly cycle of birth and death.",
    "How is Yoga defined in Katopanishad?": "Yoga is explicitly defined in Kata Upanishad (2.3.11) as:\n**\"Sthiram Indriya Dharanam\"** (ಸ್ಥಿರ ಇಂದ್ರಿಯ ಧಾರಣೆ) — the steady, quiet control of the senses, where the mind and intellect become perfectly still. This state is the threshold to liberation."
  }
};

function askQuestion(qText) {
  const box = document.getElementById('chat-box');
  
  // User bubble
  const uBubble = document.createElement('div');
  uBubble.className = 'chat-bubble user';
  uBubble.textContent = qText;
  box.appendChild(uBubble);
  
  // Auto-scroll
  box.scrollTop = box.scrollHeight;
  
  // Response bubble
  setTimeout(() => {
    const bBubble = document.createElement('div');
    bBubble.className = 'chat-bubble bot';
    const resp = CHAT_RESPONSES[currentLanguage][qText] || UI_TRANSLATIONS[currentLanguage].defaultResponse || "I'm happy to help explain anything about the Katopanishad!";
    bBubble.textContent = resp;
    box.appendChild(bBubble);
    box.scrollTop = box.scrollHeight;
  }, 300);
}

// Initial load
updateLanguage('kn');"""

def main():
    f = open('index.html', 'r', encoding='utf-8').read()
    start_tag = "<script>"
    # Let's find the first index of <script> after line 640
    start_idx = f.find(start_tag, 10000) # skip styled/header scripts
    end_idx = f.rfind("</script>")
    
    if start_idx == -1 or end_idx == -1:
        print("Could not find script block tags!")
        sys.exit(1)
        
    updated = f[:start_idx + len(start_tag)] + "\n" + new_js + "\n" + f[end_idx:]
    open('index.html', 'w', encoding='utf-8').write(updated)
    print("Updated index.html script block successfully!")

if __name__ == "__main__":
    main()
