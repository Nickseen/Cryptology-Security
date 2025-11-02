INITIAL_PERMUTATION = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

FINAL_PERMUTATION = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

EXPANSION_TABLE = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

PERMUTATION_TABLE = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]

S_BOXES = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]

PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

PC2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

SHIFT_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


def permute(block, table):
    return ''.join(block[i - 1] for i in table)


def left_shift(bits, n):
    return bits[n:] + bits[:n]


def xor(bits1, bits2):
    return ''.join('0' if b1 == b2 else '1' for b1, b2 in zip(bits1, bits2))


def s_box_substitution(expanded_bits):
    result = ''
    for i in range(8):
        block = expanded_bits[i * 6:(i + 1) * 6]
        row = int(block[0] + block[5], 2)
        col = int(block[1:5], 2)
        val = S_BOXES[i][row][col]
        result += format(val, '04b')
    return result


def f_function(right_half, subkey):
    expanded = permute(right_half, EXPANSION_TABLE)
    xored = xor(expanded, subkey)
    substituted = s_box_substitution(xored)
    permuted = permute(substituted, PERMUTATION_TABLE)
    return permuted


def generate_subkeys(key):
    key_bits = format(int(key, 16), '064b')
    permuted_key = permute(key_bits, PC1)
    left = permuted_key[:28]
    right = permuted_key[28:]
    subkeys = []
    for shift in SHIFT_SCHEDULE:
        left = left_shift(left, shift)
        right = left_shift(right, shift)
        combined = left + right
        subkey = permute(combined, PC2)
        subkeys.append(subkey)
    return subkeys


def des_encrypt_block(plaintext, key):
    plaintext_bits = format(int(plaintext, 16), '064b')
    permuted = permute(plaintext_bits, INITIAL_PERMUTATION)
    left = permuted[:32]
    right = permuted[32:]
    subkeys = generate_subkeys(key)
    for i in range(16):
        temp = right
        f_result = f_function(right, subkeys[i])
        right = xor(left, f_result)
        left = temp
    combined = right + left
    ciphertext_bits = permute(combined, FINAL_PERMUTATION)
    return hex(int(ciphertext_bits, 2))[2:].upper().zfill(16)


def des_decrypt_block(ciphertext, key):
    ciphertext_bits = format(int(ciphertext, 16), '064b')
    permuted = permute(ciphertext_bits, INITIAL_PERMUTATION)
    left = permuted[:32]
    right = permuted[32:]
    subkeys = generate_subkeys(key)
    for i in range(15, -1, -1):
        temp = right
        f_result = f_function(right, subkeys[i])
        right = xor(left, f_result)
        left = temp
    combined = right + left
    plaintext_bits = permute(combined, FINAL_PERMUTATION)
    return hex(int(plaintext_bits, 2))[2:].upper().zfill(16)


def calculate_ri_from_sboxes(l_prev, s_outputs):
    s_outputs_binary = ''.join(format(int(s, 16), '04b') for s in s_outputs)
    permuted = permute(s_outputs_binary, PERMUTATION_TABLE)
    r_i = xor(l_prev, permuted)
    return r_i


def main():
    print("=" * 60)
    print("DES Algorithm - Laboratory Work No. 4")
    print("=" * 60)
    print()
    
    while True:
        print("\nChoose operation:")
        print("1. Full DES Encryption")
        print("2. Full DES Decryption")
        print("3. Calculate R_i from S-box outputs and L_(i-1)")
        print("4. Exit")
        print()
        
        choice = input("Enter choice (1-4): ").strip()
        
        if choice == '1':
            plaintext = input("\nEnter plaintext (16 hex digits): ").strip().upper()
            key = input("Enter key (16 hex digits): ").strip().upper()
            
            if len(plaintext) != 16 or len(key) != 16:
                print("Error: Plaintext and key must be exactly 16 hex digits!")
                continue
            
            try:
                ciphertext = des_encrypt_block(plaintext, key)
                print(f"\nPlaintext:  {plaintext}")
                print(f"Key:        {key}")
                print(f"Ciphertext: {ciphertext}")
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == '2':
            ciphertext = input("\nEnter ciphertext (16 hex digits): ").strip().upper()
            key = input("Enter key (16 hex digits): ").strip().upper()
            
            if len(ciphertext) != 16 or len(key) != 16:
                print("Error: Ciphertext and key must be exactly 16 hex digits!")
                continue
            
            try:
                plaintext = des_decrypt_block(ciphertext, key)
                print(f"\nCiphertext: {ciphertext}")
                print(f"Key:        {key}")
                print(f"Plaintext:  {plaintext}")
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == '3':
            print("\nCalculate R_i knowing L_(i-1) and S-box outputs")
            print("S-box outputs: S1(B1)S2(B2)S3(B3)S4(B4)S5(B5)S6(B6)S7(B7)S8(B8)")
            print()
            
            l_prev_input = input("Enter L_(i-1) (32 bits in hex, 8 digits): ").strip().upper()
            
            if len(l_prev_input) != 8:
                print("Error: L_(i-1) must be exactly 8 hex digits (32 bits)!")
                continue
            
            print("\nEnter S-box outputs (each is 4 bits, enter as single hex digit):")
            s_outputs = []
            for i in range(1, 9):
                s_out = input(f"S{i}(B{i}) (1 hex digit): ").strip().upper()
                if len(s_out) != 1:
                    print(f"Error: S{i} output must be 1 hex digit!")
                    break
                s_outputs.append(s_out)
            
            if len(s_outputs) != 8:
                continue
            
            try:
                l_prev_binary = format(int(l_prev_input, 16), '032b')
                r_i = calculate_ri_from_sboxes(l_prev_binary, s_outputs)
                r_i_hex = hex(int(r_i, 2))[2:].upper().zfill(8)
                
                print(f"\nL_(i-1) = {l_prev_input} (hex) = {l_prev_binary} (binary)")
                print(f"S-box outputs: {' '.join(s_outputs)}")
                print(f"R_i = {r_i_hex} (hex) = {r_i} (binary)")
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == '4':
            print("\nExiting program. Goodbye!")
            break
        
        else:
            print("\nInvalid choice! Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
