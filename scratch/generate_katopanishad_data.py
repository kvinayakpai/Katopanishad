# -*- coding: utf-8 -*-
import io
import json
import re
import sys

# Safe stdout setup
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

k_digits = {'೧':'1','೨':'2','೩':'3','೪':'4','೫':'5','೬':'6','೭':'7','೮':'8','೯':'9','೦':'0'}

def kn_to_en_num(s):
    return "".join(k_digits.get(c, c) for c in s)

def translate_title(title_kn):
    t = title_kn.strip()
    if t == "COVER":
        return "Cover Page"
    if t == "ಓದುವ ಮೊದಲು":
        return "Preface (Before Reading)"
    if t == "ಪರಿವಿಡಿ / TABLE OF CONTENTS":
        return "Table of Contents"
    if t == "ಪರಿವಿಡಿ ಮುಂದುವರಿಕೆ":
        return "Table of Contents (Continued)"
    if t == "ಪ್ರಸ್ತಾವನೆ":
        return "Introduction"
    if t == "ಪ್ರಸ್ತಾವನೆ ಮುಂದುವರಿಕೆ":
        return "Introduction (Continued)"
    if t == "ಶಾಂತಿ ಪಾಠ":
        return "Shanti Patha (Peace Invocation)"
    if t == "ಅಧ್ಯಾಯ-೧, ವಲ್ಲೀ-೧":
        return "Chapter 1, Valli 1"
    if t == "ಅಧ್ಯಾಯ-೧, ವಲ್ಲೀ-೧ ಮುಂದುವರಿಕೆ":
        return "Chapter 1, Valli 1 (Continued)"
    if t == "ಅಧ್ಯಾಯ-೧, ವಲ್ಲೀ-೨":
        return "Chapter 1, Valli 2"
    if t == "ಅಧ್ಯಾಯ-೧, ವಲ್ಲೀ-೨ ಮುಂದುವರಿಕೆ":
        return "Chapter 1, Valli 2 (Continued)"
    if t == "ಅಧ್ಯಾಯ-೧ ದ್vೀತೀಯಾ ವಲ್ಲೀ" or t == "ಅಧ್ಯಾಯ-೧ ದ್ವಿತೀಯಾ ವಲ್ಲೀ":
        return "Chapter 1, Valli 2"
    if t == "ಅಧ್ಯಾಯ-೧, ದ್ವಿತೀಯಾ ವಲ್ಲೀ ಮುಂದುವರಿಕೆ":
        return "Chapter 1, Valli 2 (Continued)"
    if t == "ಅಧ್ಯಾಯ-೧, ತೃತೀಯಾ ವಲ್ಲೀ":
        return "Chapter 1, Valli 3"
    if t == "ಅಧ್ಯಾಯ-೧, ತೃತೀಯಾ ವಲ್ಲೀ ಮುಂದುವರಿಕೆ":
        return "Chapter 1, Valli 3 (Continued)"
    if t == "ಅಧ್ಯಾಯ-೨, ಪ್ರಥಮಾವಲ್ಲೀ":
        return "Chapter 2, Valli 1"
    if t == "ಅಧ್ಯಾಯ-೨, ಪ್ರಥಮಾವಲ್ಲೀ ಮುಂದುವರಿಕೆ" or t == "ಅಧ್ಯಾಯ-೨, ಪ್ರಥಮಾ ವಲ್ಲೀ ಮುಂದುವರಿಕೆ":
        return "Chapter 2, Valli 1 (Continued)"
    if t == "ಅಧ್ಯಾಯ-೨, ಪ್ರಥಮಾ ವಲ್ಲೀ ಮುಕ್ತಾಯ":
        return "Chapter 2, Valli 1 (Conclusion)"
    if t == "ಅಧ್ಯಾಯ-೨, ದ್ವಿತೀಯಾ ವಲ್ಲೀ":
        return "Chapter 2, Valli 2"
    if t == "ಅಧ್ಯಾಯ-೨, ತೃತೀಯಾ ವಲ್ಲೀ":
        return "Chapter 2, Valli 3"
        
    # Sanskrit shlokas
    if "ಕಠೋಪನಿಷತ್ ಮೂಲ ಶ್ಲೋಕ" in t:
        m = re.search(r'ಅಧ್ಯಾಯ\s+(\d+\.\d+)', t)
        ch_sec = m.group(1) if m else ""
        suffix = ""
        if "ಮುಂದುವರಿಕೆ" in t:
            suffix = " (Continued)"
        elif "ಮುಕ್ತಾಯ" in t:
            suffix = " (Conclusion)"
        elif "ಸಮಾಪ್ತ" in t:
            suffix = " (Complete)"
        return f"Original Sanskrit Shlokas - Chapter {ch_sec}{suffix}"
        
    # Poetic Translation
    if "ಕನ್ನಡ ಪದ್ಯರೂಪ" in t:
        m = re.search(r'ಅಧ್ಯಾಯ\s+(\d+\.\d+)', t)
        ch_sec = m.group(1) if m else ""
        suffix = ""
        if "ಮುಂದುವರಿಕೆ" in t:
            suffix = " (Continued)"
        elif "ಮುಕ್ತಾಯ" in t:
            suffix = " (Conclusion)"
        return f"Kannada Poetic Translation - Chapter {ch_sec}{suffix}"
        
    return t

def get_summary(page_num, title_en, text_content):
    if page_num == 1:
        return "Cover page of the Katha Upanishad Kannada exposition by Bannanje Govindacharya."
    if page_num == 2:
        return "Table of Contents (Part 1) outlining the structure of the commentary."
    if page_num == 3:
        return "Table of Contents (Part 2) listing the Kannada poetic translation and original Sanskrit shlokas."
    if page_num == 4:
        return "Preface (Part 1) introducing the philosophical background of the Upanishad."
    if page_num == 5:
        return "Preface (Part 2) discussing the gurukula system of education and lineage."
    if page_num == 6:
        return "Preface (Part 3) explaining the methodology of study and previous commentaries."
    if page_num == 7:
        return "Shantipatha (Peace Invocation) - detailed explanation of the introductory peace mantra."
        
    # Parse verses
    verses = re.findall(r'॥([೧೨೩೪೫೬೭೮೯೦]+)॥', text_content)
    en_verses = [kn_to_en_num(v) for v in verses]
    
    if page_num <= 76:
        summary = f"Exposition and commentary by Bannanje Govindacharya on {title_en}."
        if en_verses:
            summary += f" This page covers the Sanskrit text and detailed commentary for Shloka(s): {', '.join(en_verses)}."
        else:
            summary += " This page discusses key metaphysical concepts and details of the boons."
    elif page_num <= 155:
        summary = f"Kannada Poetic translation of {title_en.replace('Kannada Poetic Translation - ', '')}."
        if en_verses:
            summary += f" Contains translated poetic verses: {', '.join(en_verses)}."
    else:
        summary = f"Original Sanskrit verses and text for {title_en.replace('Original Sanskrit Shlokas - ', '')}."
        if en_verses:
            summary += f" Contains shlokas: {', '.join(en_verses)}."
            
    return summary

def main():
    content = open('kata-upanishad-text.txt', 'r', encoding='utf-8').read()
    
    # Let's split the file by page markers
    pattern = r'\[PAGE\s+(\d+)\s+-\s+([^\]]+)\]'
    parts = re.split(pattern, content)
    
    pages = []
    for i in range(1, len(parts), 3):
        if i + 2 >= len(parts):
            break
        page_num = int(parts[i])
        page_title = parts[i+1].strip()
        page_content = parts[i+2].strip()
        
        title_en = translate_title(page_title)
        summary_en = get_summary(page_num, title_en, page_content)
        
        pages.append({
            "num": page_num,
            "title": page_title,
            "title_en": title_en,
            "summary_en": summary_en,
            "content": page_content
        })
        
    print(f"Parsed {len(pages)} pages successfully.")

    
    # Define the ontology for Katopanishad
    tiers = [
        { "id": "parabrahma", "en": "Parabrahma", "kn": "ಪರಬ್ರಹ್ಮ", "gloss": "The Supreme Purusha/Lord" },
        { "id": "jiva", "en": "Jivatma", "kn": "ಜೀವತತ್ವ", "gloss": "The individual soul and its post-mortem state" },
        { "id": "antahkarana", "en": "Antahkarana", "kn": "ಅಂತಃಕರಣ", "gloss": "The inner instruments (Chariot Metaphor)" },
        { "id": "dharma", "en": "Paths (Marga)", "kn": "ಮಾರ್ಗ/ಧರ್ಮ", "gloss": "Shreyas vs Preyas" },
        { "id": "sadhana", "en": "Sadhana", "kn": "ಸಾಧನೆ", "gloss": "Nachiketa Agni and sense control" },
        { "id": "phala", "en": "Phala", "kn": "ಫಲ", "gloss": "Liberation (Moksha/Amritatva)" }
    ]
    
    nodes = [
        {
            "id": "purusha", "tier": "parabrahma",
            "en": "Purusha", "kn": "ಪುರುಷ",
            "title": { "en": "Purusha — The Supreme Person", "kn": "ಪುರುಷ" },
            "note": { 
                "en": "In Kata Upanishad, Purusha is the highest principle, transcending Avyakta (the unmanifest). He is the supreme goal (1.3.11).",
                "kn": "ಕಠೋಪನಿಷತ್ತಿನ ಪ್ರಕಾರ ಪುರುಷನಿಗಿಂತ ಮಿಗಿಲಾದದ್ದು ಯಾವುದೂ ಇಲ್ಲ. ಅವನೇ ಅಂತಿಮ ಗುರಿ (೧.೩.೧೧)." 
            },
            "refs": "Page 121 · Page 164"
        },
        {
            "id": "atman", "tier": "jiva",
            "en": "Atman", "kn": "ಆತ್ಮ",
            "title": { "en": "Atman — The Self", "kn": "ಆತ್ಮ" },
            "note": { 
                "en": "The eternal inner self of the individual. It is not born, nor does it die (1.2.18). It is smaller than the smallest and greater than the greatest (1.2.20).",
                "kn": "ಆತ್ಮನು ಜನ್ಮರಹಿತನು, ಮರಣರಹಿತನು. ಅವನು ಅಣುವಿಗಿಂತ ಅಣು, ಮಹತ್ತಿಗಿಂತ ಮಹತ್ತು (೧.೨.೧೮, ೧.೨.೨೦)." 
            },
            "refs": "Page 34 · Page 110 · Page 161"
        },
        {
            "id": "preta_vicikitsa", "tier": "jiva",
            "en": "Preta Vicikitsa", "kn": "ಪ್ರೇತ ವಿಚಿಕಿತ್ಸಾ",
            "title": { "en": "Preta Vicikitsa — Post-mortem Doubt", "kn": "ಪ್ರೇತ ವಿಚಿಕಿತ್ಸಾ" },
            "note": { 
                "en": "Nachiketa's third boon request: the doubt regarding what happens to a person after death — some say he exists, others say he does not (1.1.20).",
                "kn": "ನಚಿಕೇತನ ಮೂರನೇ ವರ: ಮೃತರಾದ ನಂತರ ಜೀವಿಯು ಇರುತ್ತಾನೋ ಇಲ್ಲವೋ ಎಂಬ ಅತೀಂದ್ರಿಯ ಪ್ರಶ್ನೆ (೧.೧.೨೦)." 
            },
            "refs": "Page 19 · Page 86 · Page 158"
        },
        {
            "id": "shreyas", "tier": "dharma",
            "en": "Shreyas", "kn": "ಶ್ರೇಯಸ್ಸು",
            "title": { "en": "Shreyas — The Good Path", "kn": "ಶ್ರೇಯಸ್ಸು" },
            "note": { 
                "en": "The path of spiritual goodness and eternal welfare. It leads to liberation but requires discrimination to choose over pleasure (1.2.1).",
                "kn": "ಆತ್ಮಕಲ್ಯಾಣಕ್ಕೆ ದಾರಿಯಾದ ಶ್ರೇಯೋಮಾರ್ಗ. ಇದು ಮೋಕ್ಷಕ್ಕೆ ಕಾರಣವಾಗುತ್ತದೆ (೧.೨.೧)." 
            },
            "refs": "Page 28 · Page 98 · Page 160"
        },
        {
            "id": "preyas", "tier": "dharma",
            "en": "Preyas", "kn": "ಪ್ರೇಯಸ್ಸು",
            "title": { "en": "Preyas — The Pleasant Path", "kn": "ಪ್ರೇಯಸ್ಸು" },
            "note": { 
                "en": "The path of material pleasure and immediate gratification. Choosing preyas binds the soul to the cycle of rebirth (1.2.1).",
                "kn": "ಐಹಿಕ ಸುಖಗಳಿಗೆ ದಾರಿಯಾದ ಪ್ರೇಯೋಮಾರ್ಗ. ಇದನ್ನು ಆರಿಸಿಕೊಳ್ಳುವವನು ಜನ್ಮ-ಮರಣಗಳ ಚಕ್ರಕ್ಕೆ ಸಿಲುಕುತ್ತಾನೆ (೧.೨.೧)." 
            },
            "refs": "Page 28 · Page 98 · Page 160"
        },
        {
            "id": "nachiketa_agni", "tier": "sadhana",
            "en": "Nachiketa Agni", "kn": "ನಚಿಕೇತ ಅಗ್ನಿ",
            "title": { "en": "Nachiketa Agni — The Sacred Sacrifice", "kn": "ನಚಿಕೇತ ಅಗ್ನಿ" },
            "note": { 
                "en": "The special fire sacrifice taught by Yama to Nachiketa as the second boon, leading to heavenly realms and immortality (1.1.13-16).",
                "kn": "ಯಮನು ನಚಿಕೇತನಿಗೆ ಬೋಧಿಸಿದ ವಿಶೇಷ ಅಗ್ನಿವಿದ್ಯೆ (ಎರಡನೇ ವರ), ಇದು ಸ್ವರ್ಗಲೋಕ ಮತ್ತು ಮೋಕ್ಷಕ್ಕೆ ಕಾರಣವಾಗುತ್ತದೆ (೧.೧.೧೩-೧೬)." 
            },
            "refs": "Page 12 · Page 82 · Page 157"
        },
        {
            "id": "yoga_definition", "tier": "sadhana",
            "en": "Yoga", "kn": "ಯೋಗ",
            "title": { "en": "Yoga — Sense Control", "kn": "ಯೋಗ" },
            "note": { 
                "en": "Yoga is defined in Kata Upanishad as the steady control of the senses, intellect, and mind (Sthiram Indriya Dharanam) (2.3.11).",
                "kn": "ಇಂದ್ರಿಯಗಳು ಮತ್ತು ಮನಸ್ಸಿನ ಸ್ಥಿರವಾದ ನಿಗ್ರಹವೇ ಯೋಗ (೨.೩.೧೧)." 
            },
            "refs": "Page 70 · Page 150 · Page 170"
        },
        {
            "id": "ratha_metaphor", "tier": "antahkarana",
            "en": "Chariot Metaphor", "kn": "ರಥ ಕಲ್ಪನೆ",
            "title": { "en": "Ratha — The Chariot Metaphor", "kn": "ರಥ ಕಲ್ಪನೆ" },
            "note": { 
                "en": "The famous metaphor of the chariot (1.3.3-4): the soul is the passenger, body is the chariot, intellect is the charioteer, mind is the reins, senses are the horses.",
                "kn": "ಕಠೋಪನಿಷತ್ತಿನ ಪ್ರಸಿದ್ಧ ರಥ ಕಲ್ಪನೆ: ಶರೀರವೇ ರಥ, ಬುದ್ಧಿಯೇ ಸಾರಥಿ, ಮನಸ್ಸೇ ಕಡಿವಾಣ, ಇಂದ್ರಿಯಗಳೇ ಕುದುರೆಗಳು, ಆತ್ಮನೇ ರಥಿಕ (೧.೩.೩-೪)." 
            },
            "refs": "Page 39 · Page 113 · Page 163"
        },
        {
            "id": "buddhi", "tier": "antahkarana",
            "en": "Buddhi", "kn": "ಬುದ್ಧಿ",
            "title": { "en": "Buddhi — Intellect", "kn": "ಬುದ್ಧಿ" },
            "note": { 
                "en": "The charioteer (sarathi). It must be wakeful and discriminate to lead the chariot safely to the goal.",
                "kn": "ರಥ ಕಲ್ಪನೆಯಲ್ಲಿ 'ಸಾರಥಿ'. ಇದು ತಪ್ಪು-ಸರಿಗಳನ್ನು ವಿವೇಚಿಸಿ ರಥವನ್ನು ಸರಿಯಾದ ದಾರಿಯಲ್ಲಿ ಮುನ್ನಡೆಸುತ್ತದೆ (೧.೩.೩)." 
            },
            "refs": "Page 39 · Page 113 · Page 163"
        },
        {
            "id": "manas", "tier": "antahkarana",
            "en": "Manas", "kn": "ಮನಸ್ಸು",
            "title": { "en": "Manas — Mind", "kn": "ಮನಸ್ಸು" },
            "note": { 
                "en": "The reins (pragraha). It links the intellect (charioteer) to the senses (horses). If uncontrolled, the horses run wild.",
                "kn": "ರಥ ಕಲ್ಪನೆಯಲ್ಲಿ 'ಕಡಿವಾಣ'. ಇದು ಸಾರಥಿಯ ಹಿಡಿತದಲ್ಲಿದ್ದರೆ ಮಾತ್ರ ಕುದುರೆಗಳನ್ನು ನಿಯಂತ್ರಿಸಬಹುದು (೧.೩.೩)." 
            },
            "refs": "Page 39 · Page 113 · Page 163"
        },
        {
            "id": "indriya", "tier": "antahkarana",
            "en": "Indriya", "kn": "ಇಂದ್ರಿಯಗಳು",
            "title": { "en": "Indriyas — Senses", "kn": "ಇಂದ್ರಿಯಗಳು" },
            "note": { 
                "en": "The horses (haya). They run after sense objects (roads). If undisciplined, they lead the soul to destruction.",
                "kn": "ರಥ ಕಲ್ಪನೆಯಲ್ಲಿ 'ಕುದುರೆಗಳು'. ಇವು ವಿಷಯಗಳೆಂಬ ದಾರಿಯಲ್ಲಿ ಓಡುತ್ತವೆ (೧.೩.೪)." 
            },
            "refs": "Page 39 · Page 113 · Page 163"
        },
        {
            "id": "moksha", "tier": "phala",
            "en": "Moksha", "kn": "ಮೋಕ್ಷ/ಅಮೃತತ್ವ",
            "title": { "en": "Moksha — Liberation", "kn": "ಮೋಕ್ಷ/ಅಮೃತತ್ವ" },
            "note": { 
                "en": "The state of eternal peace, immortality (Amritatva), and freedom from the cycle of birth and death, attained by realizing the Purusha.",
                "kn": "ಹುಟ್ಟು-ಸಾವಿನ ಚಕ್ರದಿಂದ ಬಿಡುಗಡೆ ಪಡೆದು ನಿರಂತರ ಆನಂದವನ್ನು ಹೊಂದುವ ಸ್ಥಿತಿ (೨.೩.೧೪)." 
            },
            "refs": "Page 72 · Page 151 · Page 170"
        }
    ]
    
    edges = [
        { "source": "purusha", "target": "atman", "type": "includes", "label": "inner self of" },
        { "source": "shreyas", "target": "moksha", "type": "leads-to", "label": "leads to" },
        { "source": "preyas", "target": "preta_vicikitsa", "type": "leads-to", "label": "binds to birth/death" },
        { "source": "nachiketa_agni", "target": "moksha", "type": "leads-to", "label": "enables heaven/liberation" },
        { "source": "yoga_definition", "target": "moksha", "type": "leads-to", "label": "leads to" },
        { "source": "ratha_metaphor", "target": "atman", "type": "includes", "label": "soul as passenger" },
        { "source": "ratha_metaphor", "target": "buddhi", "type": "includes", "label": "intellect as charioteer" },
        { "source": "ratha_metaphor", "target": "manas", "type": "includes", "label": "mind as reins" },
        { "source": "ratha_metaphor", "target": "indriya", "type": "includes", "label": "senses as horses" },
        { "source": "buddhi", "target": "manas", "type": "leads-to", "label": "controls" },
        { "source": "manas", "target": "indriya", "type": "leads-to", "label": "reins in" }
    ]
    
    # Write to JS file
    js_data = f"""// Katopanishad Knowledge Graph & Page Data
const PAGES = {json.dumps(pages, ensure_ascii=False, indent=2)};

const TIERS = {json.dumps(tiers, ensure_ascii=False, indent=2)};

const NODES = {json.dumps(nodes, ensure_ascii=False, indent=2)};

const EDGES = {json.dumps(edges, ensure_ascii=False, indent=2)};
"""
    
    with open('katopanishad_data.js', 'w', encoding='utf-8') as f:
        f.write(js_data)
        
    print("Created katopanishad_data.js successfully!")

if __name__ == '__main__':
    main()
