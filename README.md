# Lab 4 - DES (Data Encryption Standard)

Implementation of the DES block cipher algorithm in Python.

## � Description

Full implementation of the **Data Encryption Standard (DES)** - a symmetric-key block cipher that encrypts 64-bit blocks using a 56-bit key through 16 rounds of processing.

## ✨ Features

- ✓ **Complete DES encryption/decryption** (64-bit blocks)
- ✓ **Key schedule generation** (16 round subkeys from master key)
- ✓ **All DES components:** Initial Permutation, Final Permutation, Expansion, Permutation, S-boxes
- ✓ **Special laboratory task:** Calculate Rᵢ from S-box outputs and Lᵢ₋₁

## 🚀 Usage

```bash
python3 lab4_des.py
```

## 💡 Operation Modes

### 1. Full DES Encryption
Encrypt 64-bit plaintext with 56-bit key (input as 16 hex digits).

**Example:**
```
Plaintext:  0123456789ABCDEF
Key:        133457799BBCDFF1
Ciphertext: 85E813540F0AB405
```

### 2. Full DES Decryption
Decrypt ciphertext back to original plaintext.

**Example:**
```
Ciphertext: 85E813540F0AB405
Key:        133457799BBCDFF1
Plaintext:  0123456789ABCDEF
```

### 3. Round Calculation (Lab Task)
Calculate **Rᵢ** knowing **Lᵢ₋₁** (32 bits) and S-box outputs **S₁(B₁)S₂(B₂)...S₈(B₈)**.

**Example:**
```
L_(i-1): FFFFFFFF (8 hex digits)
S-box outputs: 5 A 3 7 2 B 4 8 (8 hex digits)
Result: R_i calculated
```

## 🔐 Algorithm Overview

**DES Structure:**
- **Block size:** 64 bits
- **Key size:** 56 bits (stored in 64 bits with parity)
- **Rounds:** 16
- **Structure:** Feistel network

**Components:**
- **IP/FP:** Initial and Final Permutations
- **E-expansion:** 32 bits → 48 bits
- **S-boxes:** 8 substitution tables (6 bits → 4 bits each)
- **P-permutation:** Final 32-bit permutation
- **Key schedule:** Generates 16 subkeys using PC-1, PC-2, and left shifts

## 📁 File Structure

```
lab4_des.py
├── Constants (IP, FP, E, P, S-boxes, PC-1, PC-2, shift schedule)
├── Utility functions (permute, xor, left_shift)
├── Core functions
│   ├── s_box_substitution()
│   ├── f_function()
│   ├── generate_subkeys()
│   ├── des_encrypt_block()
│   ├── des_decrypt_block()
│   └── calculate_ri_from_sboxes()
└── Interactive menu
```

## 👨‍💻 Author

**Student:** Nicola Petcov  
**Repository:** [Cryptology-Security](https://github.com/Nickseen/Cryptology-Security)  
**Branch:** Lab4  
**Date:** November 2025

## 📝 Note

DES is a historical algorithm. For modern applications, use **AES** (Advanced Encryption Standard).

Educational purposes only.
