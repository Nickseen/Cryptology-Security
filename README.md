# Laboratory Work No. 3 - Polyalphabetic Ciphers

## Playfair Encryption Algorithm

### Description

Implementation of the Playfair algorithm for the Romanian alphabet (31 letters) in Python.

### Implemented Requirements

✓ **Complete Romanian alphabet** - 31 letters (A-Z + Ă, Â, Î, Ș, Ț)  
✓ **Character validation** - Verifies if the user enters valid characters (A-Z, a-z, Romanian letters)  
✓ **Invalid character suggestions** - Displays the correct range if invalid characters are entered  
✓ **Key validation** - Minimum key length is 7 characters  
✓ **Available operations** - Encryption and decryption  
✓ **Interactive interface** - User can choose operation, enter key and message  

### Functionality

#### 1. Validation Functions
- `validate_character(character)` - Checks if a character is valid
- `validate_text(text)` - Validates text and suggests the correct range
- `validate_key(key)` - Checks the length and validity of the key

#### 2. PlayfairCipher Class
- `_create_matrix()` - Creates the 6x5 Playfair matrix
- `_find_position(character)` - Finds the position of a character in the matrix
- `_prepare_text(text)` - Prepares text (splits into bigrams)
  - Removes spaces and converts to uppercase
  - Replaces J with I (combined in matrix)
  - Splits into pairs, inserting X between identical letters
  - Example: "FREE" → "FR EX EZ", "SSS" → "SX SZ"
- `encrypt(plaintext)` - Encryption function
- `decrypt(ciphertext)` - Decryption function
- `display_matrix()` - Displays the Playfair matrix

#### 3. User Interface
- Interactive menu with multiple options
- Demonstration with predefined examples
- Information about the Romanian alphabet
- Complete user input validation

### Usage

```bash
python3 lab3_permutation_cipher.py
```

### Examples

**Encryption:**
- Original text: `SALUT`
- Bigrams: `SA LU TX`
- Encrypted text: (depends on key)

**Decryption:**
- The inverse algorithm is applied to obtain the original text

### Important Notes

- Letters **J** and **I** are combined in the Playfair matrix
- Matrix size is **6x5** (30 letters)
- Adding new spaces after decryption is done **manually**, depending on the message logic
- Minimum key length: **7 characters**
- When duplicate letters appear consecutively, filler letter (X or Z) is inserted
- Example: "FREE" becomes "FR EX EZ" (E-E separated by X)

### Code Structure

```
lab3_permutation_cipher.py
│
├── CONSTANTS
│   ├── ROMANIAN_ALPHABET
│   └── MIN_KEY_LENGTH
│
├── VALIDATION FUNCTIONS
│   ├── validate_character()
│   ├── validate_text()
│   └── validate_key()
│
├── PLAYFAIR CLASS
│   └── PlayfairCipher
│       ├── __init__()
│       ├── _create_matrix()
│       ├── _find_position()
│       ├── _prepare_text()
│       ├── encrypt()
│       ├── decrypt()
│       └── display_matrix()
│
├── INTERFACE FUNCTIONS
│   ├── read_key()
│   ├── read_text()
│   ├── choose_operation()
│   ├── display_result()
│   └── demonstration()
│
└── MAIN FUNCTION
    └── main()
```

### Algorithm Details

#### Bigram Preparation Logic

When preparing text for Playfair encryption:

1. **Remove spaces** and convert to uppercase
2. **Replace J with I** (they are combined in the matrix)
3. **Split into pairs** ensuring no pair has identical letters:
   - If two consecutive letters are the same, insert filler (X or Z)
   - Move index by 1 to process the repeated letter again
   - Example: `FREE` → `F-R`, `E-X` (E repeated), `E-Z` (E from position 3)
   - Example: `SSS` → `S-X`, `S-X` (each S separated by filler)
4. **Add filler** at the end if text length is odd

#### Encryption Rules

1. **Same row**: Replace with letters to the right (wrap around)
2. **Same column**: Replace with letters below (wrap around)
3. **Rectangle**: Replace with letters on same row but opposite corners

### Files

- `lab3_permutation_cipher.py` - Main program with Playfair algorithm
- `test_playfair.py` - Test script for basic functionality
- `test_bigrams.py` - Test script for bigram preparation logic
- `ALGORITHM_EXPLANATION.md` - Detailed algorithm explanation
- `EXAMPLES.md` - Usage examples
- `README.md` - This file

### Author

Student: Nicola  
Date: October 2025  
Repository: Cryptology-Security 
Branch: Lab3
