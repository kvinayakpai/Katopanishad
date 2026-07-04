# -*- coding: utf-8 -*-
import re
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('katopanishad-english.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

quoted_items = []
for idx, line in enumerate(lines):
    # Match strings inside single quotes
    matches = re.findall(r"'([^']+)'", line)
    for m in matches:
        # Ignore strings that are clearly just English words or single punctuation
        if len(m) > 1 and not m.replace(" ", "").isalpha() and any(c in m.lower() for c in ['a','e','i','o','u']):
            quoted_items.append((idx + 1, m, line.strip()))
        elif len(m) > 1 and any(s in m.lower() for s in ['saha', 'nau', 'avatu', 'bhanaktu', 'bhunaktu', 'viryam', 'shanti', 'yama', 'atma', 'jnana', 'valli', 'shloka', 'preya', 'shreya', 'nachiketa', 'uddhalaka', 'h va', 'h vai', 'mrityu', 'agni', 'priya']):
            quoted_items.append((idx + 1, m, line.strip()))

print(f"Found {len(quoted_items)} Sanskrit-like quoted terms:")
for line_num, term, context in sorted(quoted_items, key=lambda x: x[0]):
    print(f"Line {line_num}: '{term}'  |  Context: {context[:100]}...")
