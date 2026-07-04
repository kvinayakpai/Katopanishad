# -*- coding: utf-8 -*-
import re
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('katopanishad-english.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find occurrences of bhipreyaso, dandramyamanah, etc.
for i, line in enumerate(lines):
    if 'bhipreyaso' in line or 'dandramyamanah' in line or 'pravishtavAtmAnau' in line or 'yamanah' in line:
        print(f"Line {i+1}: {line.strip()}")
