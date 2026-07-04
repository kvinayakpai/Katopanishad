# -*- coding: utf-8 -*-
import re
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Define the dictionary of replacements
replacements_dict = {
    # 1. Quoted peace invocation sentences/phrases
    "'Saha nau avatu'": "'saha nau avatu'",
    "'Saha nau bhanaktu'": "'saha nau bhunaktu'",
    "'Saha viryam karavavahai'": "'saha vīryaṃ karavāvahai'",
    "'Tejasvi navadhitamastu ma vidvishavahai'": "'tejasvi nāvadhītamastu mā vidviṣāvahai'",
    "'Om Shantih Shantih Shantih'": "'oṃ śāntiḥ śāntiḥ śāntiḥ'",
    "'Om Shantih'": "'oṃ śāntiḥ'",
    "'Om'": "'oṃ'",
    "'Vajashravasah'": "'Vājaśravasaḥ'",
    "'Nachiketa, the son of Vajashravasa'": "'Naciketā, the son of Vājaśravasa'",
    "'Uddhalaka'": "'Uddālaka'",
    "'Auddalaki Aruni'": "'Auddālaki Āruṇi'",
    "'Nachiketa'": "'Naciketā'",
    "'Nachiketas'": "'Naciketas'",
    "'Nachiketagni'": "'Naciketāgni'",
    "'Tri-nachiketa'": "'Tri-naciketa'",
    "'Swargaloke'": "'svargaloke'",
    "'Tri-nachiketas'": "'Tri-naciketas'",
    "'na kincit chetah iti Nachiketa'": "'na kiñcit cetaḥ iti naciketā'",
    "'avatu'": "'avatu'",
    "'ava'": "'ava'",
    "'Sham'": "'śam'",
    "'srṃkāṃ'": "'sṛṅkām'",
    "'h va'": "'ha vai'",
    "'h vai'": "'ha vai'",
    "'Mrityave tva dadami'": "'mṛtyave tvā dadāmi'",
    
    # 2. Specific quoted phrases
    "'avid yayam antare vartamanah'": "'avidyāyām antare vartamānāḥ'",
    "'avidyayam antare veshtya manah'": "'avidyāyām antare veṣṭyamānāḥ'",
    "'dandramyamanah pariyanti mudha'": "'dandramyamāṇāḥ pariyanti mūḍhāḥ'",
    "'janghan yamanah pariyanti mudha'": "'jaṅghanyamānāḥ pariyanti mūḍhāḥ'",
    "'dandramyamanah'": "'dandramyamāṇāḥ'",
    '"guham pravishhtau"': '"guhāṃ praviṣṭau"',
    '"guham pravishtavAtmAnau taddarSanAt"': '"guhāṃ praviṣṭāvātmānau taddarśanāt"',
    '"Atma antaAtmeti harih eka eva dvidhAsthitah"': '"ātmā antarātmeti hariḥ eka eva dvidhā sthitaḥ"',
    "'Atma'": "'Ātmā'",
    "'AntarAtma'": "'Antarātmā'",

    # 3. Individual words/names with standard case variations
    "Bhanaktu": "Bhunaktu",
    "bhanaktu": "bhunaktu",
    "Nachiketas": "Naciketas",
    "nachiketas": "naciketas",
    "Nachiketa": "Naciketā",
    "nachiketa": "naciketā",
    "Nachiketagni": "Naciketāgni",
    "nachiketagni": "naciketāgni",
    "Uddhalaka": "Uddālaka",
    "uddhalaka": "uddālaka",
    "Vajashravas": "Vājaśravas",
    "vajashravas": "vājaśravas",
    "Vajashravasa": "Vājaśravasa",
    "vajashravasa": "vājaśravasa",
    "Vajashravasah": "Vājaśravasaḥ",
    "vajashravasah": "vājaśravasaḥ",
    "Shvetaketu": "Śvetaketu",
    "shvetaketu": "śvetaketu",
    "Shloka": "Śloka",
    "shloka": "śloka",
    "Shlokas": "Ślokas",
    "shlokas": "ślokas",
    "Vallis": "Vallīs",
    "vallis": "vallīs",
    "Valli": "Vallī",
    "valli": "vallī",
    "Adhyaya": "Adhyāya",
    "adhyaya": "adhyāya",
    "Shantih": "Śāntiḥ",
    "shantih": "śāntiḥ",
    "Shanti": "Śānti",
    "shanti": "śānti",
    "Purusha": "Puruṣa",
    "purusha": "puruṣa",
    "Purushas": "Puruṣas",
    "purushas": "puruṣas",
    "Jivas": "Jīvas",
    "jivas": "jīvas",
    "Jiva": "Jīva",
    "jiva": "jīva",
    "Moksha": "Mokṣa",
    "moksha": "mokṣa",
    "Sadhana": "Sādhana",
    "sadhana": "sādhana",
    "Shreyas": "Śreyas",
    "shreyas": "śreyas",
    "Preyas": "Preyas",
    "preyas": "preyas",
    "Avidya": "Avidyā",
    "avidya": "avidyā",
    "avidyayam": "avidyāyām",
    "Vidya": "Vidyā",
    "vidya": "vidyā",
    "Omkara": "Oṃkāra",
    "omkara": "oṃkāra",
    "Yajna": "Yajña",
    "yajna": "yajña",
    "Yajnas": "Yajñas",
    "yajnas": "yajñas",
    "Dakshinas": "Dakṣiṇās",
    "dakshinas": "dakṣiṇās",
    "Dakshina": "Dakṣiṇā",
    "dakshina": "dakṣiṇā",
    "Prana": "Prāṇa",
    "prana": "prāṇa",
    "Apana": "Apāna",
    "apana": "apāna",
    "Upanishads": "Upaniṣads",
    "upanishads": "upaniṣads",
    "Upanishad": "Upaniṣad",
    "upanishad": "upaniṣad",
    "Kathopanishad": "Kaṭhopaniṣad",
    "kathopanishad": "kaṭhopaniṣad",
    "Kathakopanishad": "Kāṭhakopaniṣad",
    "kathakopanishad": "kāṭhakopaniṣad",
    "Swargaloka": "Svargaloka",
    "swargaloka": "svargaloka",
    "Swargya": "Svargya",
    "swargya": "svargya",
    "Swarga": "Svarga",
    "swarga": "svarga",
    "Agnikunda": "Agnikuṇḍa",
    "agnikunda": "agnikuṇḍa",
    "Samsara": "Saṃsāra",
    "samsara": "saṃsāra",
    "Brahmana": "Brāhmaṇa",
    "brahmana": "brāhmaṇa",
    "Atman": "Ātman",
    "atman": "ātman",
    "Tattva": "Tattva",
    "tattva": "tattva",
    "Tatva": "Tattva",
    "tatva": "tattva",
    "Gautama": "Gautama",
    "gautama": "gautama",
    "Nirindriya": "Nirindriya",
    "Auddalaki": "Auddālaki",
    "auddalaki": "auddālaki",
    "Aruni": "Āruṇi",
    "aruni": "āruṇi",
    "Aruna": "Aruṇā",
    "aruna": "aruṇā",
    "Vedanta": "Vedānta",
    "vedanta": "vedānta",
    "Vayu": "Vāyu",
    "vayu": "vāyu",
    "Rigveda": "Ṛgveda",
    "rigveda": "ṛgveda",
    "Samaveda": "Sāmaveda",
    "samaveda": "sāmaveda",
    "Atharvaveda": "Atharvaveda",
    "Vedas": "Vedas",
    "vedas": "vedas",
    "Veda": "Veda",
    "veda": "veda",
    "Gita": "Gītā",
    "gita": "gītā",
    "Mahabharata": "Mahābhārata",
    "mahabharata": "mahābhārata",
    "Puranas": "Purāṇas",
    "puranas": "purāṇas",
    "Purana": "Purāṇa",
    "purana": "purāṇa",
    "Hamsa": "Haṃsa",
    "hamsa": "haṃsa",
    "Hritkamala": "Hṛtkamala",
    "hritkamala": "hṛtkamala",
    "Taittiriya": "Taittirīya",
    "taittiriya": "taittirīya",
    "Aranyaka": "Āraṇyaka",
    "aranyaka": "āraṇyaka",
    "Ashvattha": "Aśvattha",
    "ashvattha": "aśvattha",
    "Angushtha-matra": "Aṅguṣṭha-mātra",
    "angushtha-matra": "aṅguṣṭha-mātra",
    "Sushupti": "Suṣupti",
    "sushupti": "suṣupti",
    "Nidra": "Nidrā",
    "nidra": "nidrā",
    "Rishi": "Ṛṣi",
    "rishi": "ṛṣi",
    "Rishis": "Ṛṣis",
    "rishis": "ṛṣis",
    "Saraswati": "Sarasvatī",
    "saraswati": "sarasvatī",
    "Savitri": "Sāvitrī",
    "savitri": "sāvitrī",
    "Gayatri": "Gāyatrī",
    "gayatri": "gāyatrī",
    "Seva": "Sevā",
    "seva": "sevā",
    "Jnana": "Jñāna",
    "jnana": "jñāna",
    "Jnanayajna": "Jñānayajña",
    "jnanayajna": "jñānayajña",
    "Karmayajna": "Karmayajña",
    "karmayajna": "karmayajña",
    "Grahana": "Grahaṇa",
    "grahana": "grahaṇa",
    "Pratyagatman": "Pratyagātman",
    "pratyagatman": "pratyagātman",
    "Antaratman": "Antarātman",
    "antaratman": "antarātman",
    "Paramatman": "Paramātman",
    "paramatman": "paramātman",
    "Brahma-vidya": "Brahma-vidyā",
    "brahmavidya": "brahmavidyā",
    "Dhyana": "Dhyāna",
    "dhyana": "dhyāna",
    "Samadhi": "Samādhi",
    "samadhi": "samādhi",
    "Satyaloka": "Satyaloka",
    "Chaitanya": "Caitanya",
    "chaitanya": "caitanya",
    "Sadhaka": "Sādhaka",
    "sadhaka": "sādhaka",
    "Sadhakas": "Sādhakas",
    "sadhakas": "sādhakas",
    "Linga": "Liṅga",
    "linga": "liṅga",
    "brahmanishtha": "brahmaniṣṭhā",
}

# Sort replacements by key length descending to prevent partial replacements
sorted_replacements = sorted(replacements_dict.items(), key=lambda x: len(x[0]), reverse=True)

with open('katopanishad-english.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Apply replacements
modified_text = text
changes_count = 0
preview_changes = []

# We will apply word replacements carefully.
# For phrases, we can do direct string replacement.
# For single words, we should use word boundary regex to avoid partial matches on unrelated words.
for key, value in sorted_replacements:
    # If the key contains spaces, quotes, or dashes, treat it as a direct substring replacement.
    if ' ' in key or "'" in key or '"' in key or '-' in key:
        count = modified_text.count(key)
        if count > 0:
            modified_text = modified_text.replace(key, value)
            changes_count += count
            preview_changes.append(f"Substituted literal phrase: '{key}' -> '{value}' ({count} times)")
    else:
        # Use regex word boundaries for single words
        pattern = r'\b' + re.escape(key) + r'\b'
        count = len(re.findall(pattern, modified_text))
        if count > 0:
            modified_text = re.sub(pattern, value, modified_text)
            changes_count += count
            preview_changes.append(f"Substituted word: '{key}' -> '{value}' ({count} times)")

print(f"Total substitutions planned: {changes_count}")
print("\nSubstitutions Summary:")
for change in preview_changes:
    print(f"  {change}")

# Let's save a preview to verify
with open('katopanishad-english.txt', 'w', encoding='utf-8') as f:
    f.write(modified_text)

print("\nSaved transliterated text successfully.")
