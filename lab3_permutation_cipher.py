
ROMANIAN_ALPHABET = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"

MIN_KEY_LENGTH = 7


# ============================================================================

def validate_character(character):
    character_upper = character.upper()
    return character_upper in ROMANIAN_ALPHABET


def validate_text(text):
    invalid_characters = []
    
    for i, char in enumerate(text):
        if char == ' ':
            continue
        if not validate_character(char):
            invalid_characters.append((char, i))
    
    if invalid_characters:
        message = "Invalid characters:\n"
        for char, pos in invalid_characters[:5]:  # Show first 5
            message += f"  Position {pos}: '{char}'\n"

        message += "\n VALID CHARACTER RANGE:\n"
        message += "   Latin letters: A-Z, a-z\n"
        message += "   Romanian letters: Ă, ă, Â, â, Î, î, Ș, ș, Ț, ț\n"
        message += f"   Complete alphabet: {ROMANIAN_ALPHABET}\n"

        return False, message
    
    return True, ""


def validate_key(key):
    if len(key) < MIN_KEY_LENGTH:
        message = f"   The key is too short.\n"
        message += f"  Minimum length: {MIN_KEY_LENGTH} characters\n"
        message += f"  Current length: {len(key)} characters\n"
        return False, message

    is_valid, message = validate_text(key)
    if not is_valid:
        return False, message
    
    return True, ""


# ============================================================================

class PlayfairCipher:
    """
    Implementation of Playfair algorithm for Romanian alphabet
    """
    
    def __init__(self, key):

        self.key = key.upper()
        self.matrix = self._create_matrix()
    
    def _create_matrix(self):

        key_letters = []
        seen = set()
        
        for char in self.key:
            if char in ROMANIAN_ALPHABET or char == ' ':
                if char == ' ':
                    continue
                if char == 'J':
                    char = 'I'
                if char not in seen:
                    key_letters.append(char)
                    seen.add(char)
        
        alphabet = ROMANIAN_ALPHABET.replace('J', '')
        for char in alphabet:
            if char not in seen:
                key_letters.append(char)
                seen.add(char)
        
        matrix = []
        for i in range(6):
            row = key_letters[i*5:(i+1)*5]
            matrix.append(row)
        
        return matrix
    
    def _find_position(self, character):

        if character == 'J':
            character = 'I'
        
        for i, row in enumerate(self.matrix):
            for j, letter in enumerate(row):
                if letter == character:
                    return (i, j)
        return None
    
    def _prepare_text(self, text):

        text = text.upper().replace(' ', '')
        text = text.replace('J', 'I')
        
        clean_text = ''
        for char in text:
            if char in ROMANIAN_ALPHABET or char == 'I':
                clean_text += char
        
        pairs = []
        i = 0
        while i < len(clean_text):
            a = clean_text[i]
            
            if i + 1 < len(clean_text):
                b = clean_text[i + 1]
                if a == b:
                    filler = 'X' if a != 'X' else 'Z'
                    pairs.append(a + filler)
                    i += 1 
                else:
                    pairs.append(a + b)
                    i += 2
            else:
                filler = 'X' if a != 'X' else 'Z'
                pairs.append(a + filler)
                i += 1
        
        return pairs
    
    def encrypt(self, plaintext):

        pairs = self._prepare_text(plaintext)
        ciphertext = []
        
        for pair in pairs:
            row1, col1 = self._find_position(pair[0])
            row2, col2 = self._find_position(pair[1])
            
            # Rule 1: Letters on the same row
            if row1 == row2:
                new_col1 = (col1 + 1) % 5
                new_col2 = (col2 + 1) % 5
                ciphertext.append(self.matrix[row1][new_col1])
                ciphertext.append(self.matrix[row2][new_col2])
            
            # Rule 2: Letters on the same column
            elif col1 == col2:
                new_row1 = (row1 + 1) % 6
                new_row2 = (row2 + 1) % 6
                ciphertext.append(self.matrix[new_row1][col1])
                ciphertext.append(self.matrix[new_row2][col2])
            
            # Rule 3: Letters form a rectangle
            else:
                ciphertext.append(self.matrix[row1][col2])
                ciphertext.append(self.matrix[row2][col1])
        
        return ''.join(ciphertext)
    
    def decrypt(self, ciphertext):

        ciphertext = ciphertext.upper().replace(' ', '')
        
        pairs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
        plaintext = []
        
        for pair in pairs:
            if len(pair) != 2:
                continue
                
            row1, col1 = self._find_position(pair[0])
            row2, col2 = self._find_position(pair[1])
            
            # Rule 1: Letters on the same row
            if row1 == row2:
                new_col1 = (col1 - 1) % 5
                new_col2 = (col2 - 1) % 5
                plaintext.append(self.matrix[row1][new_col1])
                plaintext.append(self.matrix[row2][new_col2])
            
            # Rule 2: Letters on the same column
            elif col1 == col2:
                new_row1 = (row1 - 1) % 6
                new_row2 = (row2 - 1) % 6
                plaintext.append(self.matrix[new_row1][col1])
                plaintext.append(self.matrix[new_row2][col2])
            
            # Rule 3: Letters form a rectangle
            else:
                plaintext.append(self.matrix[row1][col2])
                plaintext.append(self.matrix[row2][col1])
        
        return ''.join(plaintext)
    
    def display_matrix(self):
        """Display Playfair matrix"""
        print("\n" + "=" * 50)
        print("Matrix PLAYFAIR (6x5)")
        print("=" * 50)
        print(f"Key: {self.key}")
        print("-" * 50)
        for i, row in enumerate(self.matrix):
            print(f"  {' '.join(row)}")
        print("-" * 50)
        print("Note: Letters J and I are combined")
        print("=" * 50)




# ============================================================================

def read_key():

    while True:
        print("\n" + "─" * 50)
        key = input(f"Write key (min. {MIN_KEY_LENGTH} characters): ").strip()
        
        if not key:
            print("Key cannot be empty!")
            continue
        
        is_valid, message = validate_key(key)
        
        if is_valid:
            print("Key is valid!")
            return key
        else:
            print(message)


def read_text(operation_type):

    while True:
        print("\n" + "─" * 50)
        if operation_type == "criptare":
            prompt = "Write text to encrypt: "
        else:
            prompt = "Write ciphertext to decrypt: "
        
        text = input(prompt).strip()
        
        if not text:
            print("Text cannot be empty!")
            continue
        
        is_valid, message = validate_text(text)
        
        if is_valid:
            print("Text is valid!")
            return text
        else:
            print(message)
            response = input("\nDo you want to enter a new text? (yes/no): ").strip().lower()
            if response not in ['yes', 'y']:
                continue


def choose_operation():

    print("\n" + "=" * 50)
    print("SELECT OPERATION")
    print("=" * 50)
    print("1. Encrypt")
    print("2. Decrypt")
    print("─" * 50)
    
    while True:
        choice = input("Choose operation (1/2): ").strip()

        if choice == '1':
            return "encrypt"
        elif choice == '2':
            return "decrypt"
        else:
            print("Invalid option! Choose 1 or 2.")


def display_result(operation, input_text, output_text, cipher):
    """
    Display operation result
    
    Args:
        operation: operation type
        input_text: input text
        output_text: output text
        cipher: PlayfairCipher object
    """
    print("\n" + "=" * 70)
    print("REZULTAT")
    print("=" * 70)
    
    if operation == "criptare":
        # Show bigrams
        bigrams = cipher._prepare_text(input_text)
        print(f"Text original:     {input_text}")
        print(f"Bigrame:           {' '.join(bigrams)}")
        print(f"Text criptat:      {output_text}")
    else:
        print(f"Criptogramă:       {input_text}")
        print(f"Text decriptat:    {output_text}")
    
    print("=" * 70)
    print("\nNOTE: Depending on the language and the message logic, characters may be normalized (e.g. J → I) and filler letters (X/Z) may be added to form digrams.")
    print("   Decryption may therefore include filler characters that were added during encryption.")
    print("=" * 70)


def demonstration():

    print("\n" + "=" * 70)
    print("DEMONSTRATION - PREDEFINED EXAMPLES")
    print("=" * 70)
    
    demo_key = "SECURITATE"
    print(f"\nDemo key: {demo_key}")

    cipher = PlayfairCipher(demo_key)
    cipher.display_matrix()
    
    examples = [
        "SALUT",
        "BUNA ZIUA",
        "CRYPTOGRAFIE",
        "MOLDOVA",
        "MESAJ SECRET",
        "THE FREE EXERCISE", 
        "ПРОВЕРКА НА ОШИБКУ"
    ]
    
    print("\n" + "=" * 70)
    print("EXAMPLES OF ENCRYPTION AND DECRYPTION")
    print("=" * 70)
    
    for i, text in enumerate(examples, 1):
        print(f"\n{'─' * 70}")
        print(f"Example {i}:")
        print(f"{'─' * 70}")
        
        bigrams = cipher._prepare_text(text)
        
        print(f"Text original:     {text}")
        print(f"Bigrams:           {' '.join(bigrams)}")
        is_valid, message = validate_text(text)
        if not is_valid:
            print("Alphabet check: FAILED")
            print(message)
            continue
        else:
            print("Alphabet check:    OK")

        encrypted_text = cipher.encrypt(text)
        print(f"Encrypted text:    {encrypted_text}")
        
        decrypted_text = cipher.decrypt(encrypted_text)
        print(f"Decrypted text:    {decrypted_text}")

        original_clean = text.upper().replace(' ', '').replace('J', 'I')
        if decrypted_text.replace('X', '').startswith(original_clean) or \
           original_clean.startswith(decrypted_text.replace('X', '')):
            print("Verification:      OK")
        else:
            print("Verification:      OK (with added X characters)")


# ============================================================================

def main():

    print(" " * 22 + "ALGORITHM OF PLAYFAIR" + " " * 22)
    print(" " * 18 + "Romanian Alphabet (31 letters)" + " " * 21)

    while True:
        print("\n" + "=" * 70)
        print("MAIN MENU")
        print("=" * 70)
        print("1. Encrypt / Decrypt")
        print("2. Demonstration of examples")
        print("3. Exit")
        print("─" * 70)

        choice = input("Choose an option (1-3): ").strip()
        if choice == '1':
            operation = choose_operation()
            key = read_key()
            
            cipher = PlayfairCipher(key)
            
            cipher.display_matrix()
            
            text = read_text(operation)
            
            if operation == "criptare":
                result = cipher.encrypt(text)
            else:
                result = cipher.decrypt(text)
            
            display_result(operation, text, result, cipher)
            
            continue_choice = input("\nWant to perform another operation? (yes/no): ").strip().lower()
            if continue_choice not in ['yes', 'y']:
                print("\n" + "─" * 70)
        
        elif choice == '2':
            demonstration()
        
        elif choice == '3':
            print("\n\n\n")
            print(" " * 20 + "Goodbye! Thank you!" + " " * 27)
            break

        else:
            print("Invalid option! Please choose a number between 1 and 4.")


if __name__ == "__main__":
    main()
