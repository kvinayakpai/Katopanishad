# -*- coding: utf-8 -*-
import sys
import re
import io

# Fix console output encoding for Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def verify_file(filepath):
    print(f"Running quality check on {filepath}...")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: {filepath} not found.")
        return False

    # Regex to find page blocks: [PAGE N - ...]
    page_blocks = re.split(r'(\[PAGE \d+ - [^\]]+\])', content)
    
    if len(page_blocks) < 3:
        print("Warning: No page blocks found or incorrect format.")
        return False

    errors = 0
    warnings = 0

    # Vowel matras that cannot start a word or follow a space
    vowel_matras = set([
        'ಾ', 'ಿ', 'ೀ', 'ು', 'ೂ', 'ೃ', 'ೄ', 'ೆ', 'ೇ', 'ೈ', 'ೊ', 'ೋ', 'ೌ', '್', 'ೕ', 'ೖ'
    ])

    current_page_num = None
    
    for i in range(1, len(page_blocks), 2):
        header = page_blocks[i]
        body = page_blocks[i+1] if (i+1) < len(page_blocks) else ""

        # Extract page number
        match = re.search(r'\[PAGE (\d+) -', header)
        if match:
            page_num = int(match.group(1))
            if current_page_num is not None:
                if page_num != current_page_num + 1:
                    print(f"Warning: Page sequence gap! Found Page {page_num} after Page {current_page_num}.")
                    warnings += 1
            current_page_num = page_num
        else:
            page_num = "Unknown"

        # Check footer consistency
        # Format: ಆಧಾರ: ಬನ್ನಂಜೆ ಗೋವಿಂದಾಚಾರ್ಯ ಉಪನಿಷತ್ ಪ್ರವಚನ    Page N-1
        footer_match = re.findall(r'Page\s+(\d+)', body)
        if footer_match:
            last_footer_num = int(footer_match[-1])
            # The printed page number in the footer should be page_num - 1 (or match the offset)
            expected_footer_num = page_num - 1 if isinstance(page_num, int) else None
            if expected_footer_num is not None and last_footer_num != expected_footer_num:
                # Cover/TOC page footers might differ, check if page_num > 3
                if isinstance(page_num, int) and page_num > 3:
                    print(f"Page {page_num}: Footer page number {last_footer_num} does not match expected {expected_footer_num}.")
                    warnings += 1

        # Check for detached vowel matras in the page body
        for line_idx, line in enumerate(body.split('\n'), 1):
            line = line.strip()
            if not line:
                continue
            
            # 1. Double spaces check (except in headers or footers)
            if "  " in line:
                # Ignore multiple dots or lines of dots (like in Table of Contents)
                if not line.count('.') > 3:
                    print(f"Page {page_num}, Line {line_idx}: Warning - Double space found in: '{line}'")
                    warnings += 1

            # 2. Detached vowel matras
            for char_idx, char in enumerate(line):
                if char in vowel_matras:
                    if char_idx == 0:
                        print(f"Page {page_num}, Line {line_idx}: Error - Detached vowel matra '{char}' at start of line.")
                        errors += 1
                    else:
                        prev_char = line[char_idx - 1]
                        # If preceded by space or punctuation
                        if prev_char in [' ', '\t', '-', '(', '[', '{', '"', "'", '‘', '“', '=', '/']:
                            print(f"Page {page_num}, Line {line_idx}: Error - Detached vowel matra '{char}' preceded by space/punctuation in: ...{line[max(0, char_idx-5):char_idx+5]}...")
                            errors += 1

            # 3. Unmatched parentheses/brackets on the line
            open_p = line.count('(')
            close_p = line.count(')')
            if open_p != close_p:
                print(f"Page {page_num}, Line {line_idx}: Warning - Unmatched parentheses '(' vs ')' in: '{line}'")
                warnings += 1

            # 4. Stray digits as diacritics check
            # OCR sometimes reads anusvara 'ಂ' as Kannada number '೦' (zero) or vice versa.
            # Usually '೦' following a consonant without space is an error (should be 'ಂ').
            # Kannada digits: ೦, ೧, ೨, ೩, ೪, ೫, ೬, ೭, ೮, ೯
            digit_match = re.search(r'[ಕ-ಹ]೦', line)
            if digit_match:
                print(f"Page {page_num}, Line {line_idx}: Error - Probable diacritic error (consonant + digit '೦' instead of anusvara 'ಂ') in: '{line}'")
                errors += 1

    print(f"\nVerification finished. Errors: {errors}, Warnings: {warnings}")
    return errors == 0

if __name__ == "__main__":
    filepath = "kata-upanishad-text.txt"
    success = verify_file(filepath)
    if not success:
        sys.exit(1)
    else:
        print("All quality checks passed!")
        sys.exit(0)
