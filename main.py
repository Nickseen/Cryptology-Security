"""
Caesar Cipher Implementation
Laboratory Work No. 1
Author: Petcov Nicolai FAF-233
"""

def char_to_num(char):
    return ord(char.upper()) - ord('A')

def num_to_char(num):
    return chr(num + ord('A'))

def validate_key(key):
    if not 1 <= key <= 25:
        raise ValueError("Key must be between 1 and 25 inclusive")
    return key

def validate_text(text):
    for char in text:
        if not char.isalpha() and char != ' ':
            raise ValueError("Text must contain only letters (A-Z, a-z) and spaces")
    return text

def preprocess_text(text):
    return ''.join(text.upper().split())

# Task 1.1: Basic Caesar Cipher
def caesar_encrypt(plaintext, key):
    """
    Encrypt plaintext using Caesar cipher
    c = (x + k) mod 26
    """
    key = validate_key(key)
    validate_text(plaintext)  # Validate before preprocessing
    plaintext = preprocess_text(plaintext)

    ciphertext = ""
    for char in plaintext:
        x = char_to_num(char)
        c = (x + key) % 26
        ciphertext += num_to_char(c)

    return ciphertext

def caesar_decrypt(ciphertext, key):
    """
    Decrypt ciphertext using Caesar cipher
    m = (y - k) mod 26
    """
    key = validate_key(key)
    validate_text(ciphertext)  # Validate before preprocessing
    ciphertext = preprocess_text(ciphertext)

    plaintext = ""
    for char in ciphertext:
        y = char_to_num(char)
        m = (y - key) % 26
        plaintext += num_to_char(m)

    return plaintext

# Task 1.2: Caesar Cipher with Permutation
def validate_keyword(keyword):
    if len(keyword) < 7:
        raise ValueError("Keyword must have at least 7 characters")
    if not keyword.isalpha():
        raise ValueError("Keyword must contain only letters")
    return keyword

def create_permuted_alphabet(keyword):
    keyword = keyword.upper()
    permuted = ""
    seen = set()

    for char in keyword:
        if char not in seen:
            permuted += char
            seen.add(char)

    for i in range(26):
        char = num_to_char(i)
        if char not in seen:
            permuted += char

    return permuted

def caesar_permutation_encrypt(plaintext, key1, key2):
    """
    Encrypt using Caesar cipher with permuted alphabet
    key1: shift value (1-25)
    key2: keyword for permutation
    """
    key1 = validate_key(key1)
    key2 = validate_keyword(key2)
    validate_text(plaintext)  # Validate before preprocessing
    plaintext = preprocess_text(plaintext)

    permuted_alphabet = create_permuted_alphabet(key2)

    ciphertext = ""
    for char in plaintext:
        pos = char_to_num(char)
        new_pos = (pos + key1) % 26
        ciphertext += permuted_alphabet[new_pos]

    return ciphertext

def caesar_permutation_decrypt(ciphertext, key1, key2):
    """
    Decrypt using Caesar cipher with permuted alphabet
    key1: shift value (1-25)
    key2: keyword for permutation
    """
    key1 = validate_key(key1)
    key2 = validate_keyword(key2)
    validate_text(ciphertext)  # Validate before preprocessing
    ciphertext = preprocess_text(ciphertext)

    permuted_alphabet = create_permuted_alphabet(key2)

    plaintext = ""
    for char in ciphertext:
        pos = permuted_alphabet.index(char)
        original_pos = (pos - key1) % 26
        plaintext += num_to_char(original_pos)

    return plaintext

def brute_force_attack(ciphertext):
    """
    Perform brute force attack on Caesar cipher
    Try all 25 possible keys
    """
    print(f"\nBrute force attack on: {ciphertext}\n")
    print("Key | Decrypted Text")
    print("-" * 40)

    results = []
    for key in range(1, 26):
        try:
            decrypted = caesar_decrypt(ciphertext, key)
            results.append((key, decrypted))
            print(f"{key:2d}  | {decrypted}")
        except:
            pass

    return results

def main():
    print("=" * 50)
    print("CAESAR CIPHER - Laboratory Work No. 1")
    print("=" * 50)

    while True:
        print("\n[MENU]\n")
        print("1. Basic Caesar Cipher (Encrypt)")
        print("2. Basic Caesar Cipher (Decrypt)")
        print("3. Caesar with Permutation (Encrypt)")
        print("4. Caesar with Permutation (Decrypt)")
        print("5. Brute Force Attack")
        print("6. Exit")

        choice = input("\nSelect option (1-6): ").strip()

        if choice == '6':
            print("Exiting program. Goodbye!")
            break

        try:
            if choice == '1':
                # Basic encryption
                plaintext = input("Enter plaintext: ").strip()
                key = int(input("Enter key (1-25): ").strip())
                ciphertext = caesar_encrypt(plaintext, key)
                print(f"\nCiphertext: {ciphertext}")

            elif choice == '2':
                # Basic decryption
                ciphertext = input("Enter ciphertext: ").strip()
                key = int(input("Enter key (1-25): ").strip())
                plaintext = caesar_decrypt(ciphertext, key)
                print(f"\nPlaintext: {plaintext}")

            elif choice == '3':
                # Permutation encryption
                plaintext = input("Enter plaintext: ").strip()
                key1 = int(input("Enter key 1 (1-25): ").strip())
                key2 = input("Enter key 2 (keyword, min 7 letters): ").strip()
                ciphertext = caesar_permutation_encrypt(plaintext, key1, key2)
                print(f"\nPermuted alphabet: {create_permuted_alphabet(key2)}")
                print(f"Ciphertext: {ciphertext}")

            elif choice == '4':
                # Permutation decryption
                ciphertext = input("Enter ciphertext: ").strip()
                key1 = int(input("Enter key 1 (1-25): ").strip())
                key2 = input("Enter key 2 (keyword, min 7 letters): ").strip()
                plaintext = caesar_permutation_decrypt(ciphertext, key1, key2)
                print(f"\nPermuted alphabet: {create_permuted_alphabet(key2)}")
                print(f"Plaintext: {plaintext}")

            elif choice == '5':
                # Brute force
                ciphertext = input("Enter ciphertext to attack: ").strip()
                brute_force_attack(ciphertext)

            else:
                print("Invalid option. Please select 1-6.")

        except ValueError as e:
            print(f"\n[ERROR] {e}")
            print("Please check the valid range and try again.")
        except Exception as e:
            print(f"\n[ERROR] An unexpected error occurred: {e}")

if __name__ == "__main__":

    print("\n" + "=" * 50)
    input("Press Enter to start interactive mode...")
    main()