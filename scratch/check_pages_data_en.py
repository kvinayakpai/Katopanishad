# -*- coding: utf-8 -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

node_script = """
const fs = require('fs');
const code = fs.readFileSync('katopanishad_data.js', 'utf8');
eval(code + `
;
console.log(JSON.stringify({
  total: PAGES.length,
  has_content_en: PAGES.filter(p => p.content_en !== undefined).length,
  has_summary_en: PAGES.filter(p => p.summary_en !== undefined).length,
  no_english: PAGES.filter(p => p.content_en === undefined && p.summary_en === undefined).length
}));
`);
"""
with open('scratch/temp_node.js', 'w', encoding='utf-8') as f:
    f.write(node_script)

import subprocess
res = subprocess.run(['node', 'scratch/temp_node.js'], capture_output=True, text=True)
print(res.stdout)
if res.stderr:
    print("Error:", res.stderr)
