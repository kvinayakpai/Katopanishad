# -*- coding: utf-8 -*-
import os
import re
import sys
import io

# Setup UTF-8 for console output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

vowels = {
    '\u0905': 'a',  # अ
    '\u0906': 'ā',  # आ
    '\u0907': 'i',  # इ
    '\u0908': 'ī',  # ई
    '\u0909': 'u',  # उ
    '\u090a': 'ū',  # ऊ
    '\u090b': 'ṛ',  # ऋ
    '\u0960': 'ṝ',  # ॠ
    '\u090c': 'ḷ',  # ऌ
    '\u0961': 'ḹ',  # ॡ
    '\u090f': 'e',  # ए
    '\u0910': 'ai', # ऐ
    '\u0913': 'o',  # ओ
    '\u0914': 'au'  # औ
}

matras = {
    '\u093e': 'ā',  # ा
    '\u093f': 'i',  # ि
    '\u0940': 'ī',  # ी
    '\u0941': 'u',  # ु
    '\u0942': 'ū',  # ू
    '\u0943': 'ṛ',  # ृ
    '\u0944': 'ṝ',  # ॄ
    '\u0962': 'ḷ',  # ॢ
    '\u0963': 'ḹ',  # ॣ
    '\u0947': 'e',  # े
    '\u0948': 'ai', # ै
    '\u094b': 'o',  # ो
    '\u094c': 'au'  # ौ
}

consonants = {
    '\u0915': 'k',  # क
    '\u0916': 'kh', # ख
    '\u0917': 'g',  # ग
    '\u0918': 'gh', # घ
    '\u0919': 'ṅ',  # ङ
    '\u091a': 'c',  # च
    '\u091b': 'ch', # छ
    '\u091c': 'j',  # ज
    '\u091d': 'jh', # झ
    '\u091e': 'ñ',  # ञ
    '\u091f': 'ṭ',  # ट
    '\u0920': 'ṭh', # ठ
    '\u0921': 'ḍ',  # ड
    '\u0922': 'ḍh', # ढ
    '\u0923': 'ṇ',  # ण
    '\u0924': 't',  # त
    '\u0925': 'th', # थ
    '\u0926': 'd',  # द
    '\u0927': 'dh', # ध
    '\u0928': 'n',  # न
    '\u092a': 'p',  # प
    '\u092b': 'ph', # फ
    '\u092c': 'b',  # ब
    '\u092d': 'bh', # भ
    '\u092e': 'm',  # म
    '\u092f': 'y',  # य
    '\u0930': 'r',  # र
    '\u0931': 'r',  # ऱ
    '\u0932': 'l',  # ल
    '\u0933': 'ḷ',  # ळ
    '\u0934': 'ḷ',  # ऴ
    '\u0935': 'v',  # व
    '\u0936': 'ś',  # श
    '\u0937': 'ṣ',  # ष
    '\u0938': 's',  # स
    '\u0939': 'h'   # ह
}

modifiers = {
    '\u0902': 'ṃ',  # anusvara
    '\u0903': 'ḥ',  # visarga
    '\u0901': 'm̐',  # candrabindu
    '\u093d': '\''  # avagraha (ऽ)
}

other_mappings = {
    '।': '|',
    '॥': '||',
    'S': '\'',
    '०': '0',
    '१': '1',
    '२': '2',
    '३': '3',
    '४': '4',
    '५': '5',
    '६': '6',
    '७': '7',
    '८': '8',
    '९': '9'
}

def transliterate_word(word):
    res = []
    i = 0
    n = len(word)
    while i < n:
        char = word[i]
        if char in consonants:
            base = consonants[char]
            if i + 1 < n:
                next_char = word[i+1]
                if next_char == '\u094d': # virama
                    res.append(base)
                    i += 2
                    continue
                elif next_char in matras:
                    res.append(base + matras[next_char])
                    i += 2
                    continue
            res.append(base + 'a')
            i += 1
        elif char in vowels:
            res.append(vowels[char])
            i += 1
        elif char in modifiers:
            res.append(modifiers[char])
            i += 1
        elif char in other_mappings:
            res.append(other_mappings[char])
            i += 1
        elif char == 'ॐ':
            res.append('oṃ')
            i += 1
        else:
            res.append(char)
            i += 1
    return "".join(res)

def transliterate_line(line):
    # Split line keeping spaces and punctuation
    words = re.split(r'(\s+|[।॥\d\-.,:;()\[\]{}]+)', line)
    trans_words = []
    for w in words:
        if re.search(r'[\u0900-\u097F]', w):
            trans_words.append(transliterate_word(w))
        else:
            w_mapped = w
            for d_dev, d_lat in other_mappings.items():
                w_mapped = w_mapped.replace(d_dev, d_lat)
            trans_words.append(w_mapped)
    return "".join(trans_words)

def process_file(file_path):
    print(f"Reading {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    output_lines = []
    dev_count = 0
    
    # We will iterate through the lines and check for Devanagari.
    # To be idempotent, we also check if the next line is already the IAST transliteration.
    # We determine this if the next line is not empty, does not contain Devanagari, and
    # matches a certain similarity threshold or signature of IAST (starts/ends similarly).
    i = 0
    total = len(lines)
    while i < total:
        line = lines[i]
        output_lines.append(line)
        
        # Check if line contains Devanagari
        if re.search(r'[\u0900-\u097F]', line):
            dev_count += 1
            iast_line = transliterate_line(line.strip()) + "\n"
            
            # Check if next line is already this IAST line
            already_transliterated = False
            if i + 1 < total:
                next_line = lines[i+1]
                if next_line.strip() == iast_line.strip():
                    already_transliterated = True
            
            if not already_transliterated:
                output_lines.append(iast_line)
        
        i += 1
        
    print(f"Processed {dev_count} Devanagari lines.")
    
    # Write back the modified content
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(output_lines)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    file_path = "katopanishad-english.txt"
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    process_file(file_path)
