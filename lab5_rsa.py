"""
Lucrare de laborator nr. 5 - CRIPTOGRAFIA CU CHEI PUBLICE
Sarcina 2.1 - Algoritmul RSA
Student: Nicolai Petcov
"""

import sympy
from sympy import isprime, gcd, mod_inverse
import random

def text_to_decimal(text):
    """
    Convertește textul în reprezentare numerică zecimală
    prin intermediul reprezentării hexazecimale ASCII
    """
    # Convertim fiecare caracter în hex ASCII
    hex_string = text.encode('ascii').hex()
    # Convertim hex în decimal
    decimal_value = int(hex_string, 16)
    print(f"Text original: {text}")
    print(f"Reprezentare hexazecimală: {hex_string}")
    print(f"Reprezentare zecimală: {decimal_value}")
    return decimal_value

def decimal_to_text(decimal_value):
    """
    Convertește un număr zecimal înapoi în text
    """
    # Convertim decimal în hex
    hex_string = hex(decimal_value)[2:]  # eliminăm prefixul '0x'
    # Asigurăm că avem un număr par de caractere
    if len(hex_string) % 2 != 0:
        hex_string = '0' + hex_string
    # Convertim hex în bytes și apoi în string
    text = bytes.fromhex(hex_string).decode('ascii')
    return text

def generate_large_prime(bits):
    """
    Generează un număr prim mare cu numărul specificat de biți
    """
    print(f"\nGenerare număr prim de {bits} biți...")
    while True:
        # Generăm un număr aleatoriu de dimensiunea specificată
        candidate = random.getrandbits(bits)
        # Asigurăm că bitul cel mai semnificativ este 1
        candidate |= (1 << (bits - 1))
        # Asigurăm că numărul este impar
        candidate |= 1
        
        # Verificăm dacă este prim
        if isprime(candidate):
            print(f"Număr prim găsit!")
            return candidate

def generate_rsa_keys(bits=2048):
    """
    Generează cheile publice și private RSA
    
    Pași:
    1. Generăm două numere prime mari p și q
    2. Calculăm n = p * q (modulul RSA)
    3. Calculăm φ(n) = (p-1)(q-1)
    4. Alegem e astfel încât 1 < e < φ(n) și gcd(e, φ(n)) = 1
    5. Calculăm d astfel încât d*e ≡ 1 (mod φ(n))
    
    Cheia publică: (e, n)
    Cheia privată: (d, n)
    """
    print("="*80)
    print("GENERAREA CHEILOR RSA")
    print("="*80)
    
    # Pas 1: Generăm p și q (fiecare de bits/2 biți pentru a obține n de bits biți)
    half_bits = bits // 2
    print(f"\nPas 1: Generarea numerelor prime p și q")
    p = generate_large_prime(half_bits)
    print(f"p = {p}")
    print(f"Număr de biți în p: {p.bit_length()}")
    
    q = generate_large_prime(half_bits)
    print(f"\nq = {q}")
    print(f"Număr de biți în q: {q.bit_length()}")
    
    # Pas 2: Calculăm n = p * q
    print(f"\nPas 2: Calcularea modulului n")
    n = p * q
    print(f"n = p * q = {n}")
    print(f"Număr de biți în n: {n.bit_length()}")
    
    # Pas 3: Calculăm φ(n) = (p-1)(q-1)
    print(f"\nPas 3: Calcularea funcției Euler φ(n)")
    phi_n = (p - 1) * (q - 1)
    print(f"φ(n) = (p-1)(q-1) = {phi_n}")
    
    # Pas 4: Alegem e (de obicei 65537)
    print(f"\nPas 4: Alegerea exponentului public e")
    e = 65537  # Valoare standard pentru e
    print(f"e = {e}")
    print(f"Verificăm că gcd(e, φ(n)) = 1")
    gcd_value = gcd(e, phi_n)
    print(f"gcd({e}, φ(n)) = {gcd_value}")
    
    if gcd_value != 1:
        print("EROARE: gcd(e, φ(n)) != 1. Recalculăm...")
        return generate_rsa_keys(bits)
    
    # Pas 5: Calculăm d = e^(-1) mod φ(n)
    print(f"\nPas 5: Calcularea exponentului privat d")
    d = mod_inverse(e, phi_n)
    print(f"d = e^(-1) mod φ(n) = {d}")
    
    # Verificare: d * e ≡ 1 (mod φ(n))
    verification = (d * e) % phi_n
    print(f"\nVerificare: (d * e) mod φ(n) = {verification}")
    if verification == 1:
        print("✓ Verificare reușită!")
    
    print(f"\n" + "="*80)
    print("CHEILE GENERATE")
    print("="*80)
    print(f"Cheia publică: (e={e}, n={n})")
    print(f"Cheia privată: (d={d}, n={n})")
    print("="*80)
    
    return (e, n), (d, n), p, q

def rsa_encrypt(message, public_key):
    """
    Criptează un mesaj folosind cheia publică RSA
    
    C = M^e mod n
    """
    e, n = public_key
    print("\n" + "="*80)
    print("CRIPTAREA RSA")
    print("="*80)
    print(f"Mesaj în clar (M): {message}")
    print(f"Cheia publică: e={e}, n={n}")
    print(f"\nCalculăm C = M^e mod n")
    
    # Folosim pow cu trei argumente pentru modular exponentiation eficientă
    ciphertext = pow(message, e, n)
    print(f"C = {message}^{e} mod {n}")
    print(f"C = {ciphertext}")
    print("="*80)
    
    return ciphertext

def rsa_decrypt(ciphertext, private_key):
    """
    Decriptează un mesaj folosind cheia privată RSA
    
    M = C^d mod n
    """
    d, n = private_key
    print("\n" + "="*80)
    print("DECRIPTAREA RSA")
    print("="*80)
    print(f"Text cifrat (C): {ciphertext}")
    print(f"Cheia privată: d={d}, n={n}")
    print(f"\nCalculăm M = C^d mod n")
    
    # Folosim pow cu trei argumente pentru modular exponentiation eficientă
    plaintext = pow(ciphertext, d, n)
    print(f"M = {ciphertext}^{d} mod {n}")
    print(f"M = {plaintext}")
    print("="*80)
    
    return plaintext

def main():
    """
    Funcția principală care execută algoritmul RSA complet
    """
    print("\n" + "="*80)
    print("SARCINA 2.1 - ALGORITMUL RSA")
    print("Student: Nicolai Petcov")
    print("="*80)
    
    # Mesajul original
    message_text = "Nicolai Petcov"
    
    # Pas 1: Convertim textul în număr
    print("\n" + "="*80)
    print("CONVERTIREA MESAJULUI")
    print("="*80)
    message_numeric = text_to_decimal(message_text)
    
    # Pas 2: Generăm cheile RSA (n trebuie să fie de cel puțin 2048 biți)
    public_key, private_key, p, q = generate_rsa_keys(bits=2048)
    e, n = public_key
    d, _ = private_key
    
    # Verificăm că mesajul este mai mic decât n
    if message_numeric >= n:
        print("\nERORE: Mesajul este prea mare pentru modulul n!")
        print("Trebuie să împărțim mesajul în blocuri sau să mărim dimensiunea cheii.")
        return
    
    # Pas 3: Criptăm mesajul
    ciphertext = rsa_encrypt(message_numeric, public_key)
    
    # Pas 4: Decriptăm mesajul
    decrypted_numeric = rsa_decrypt(ciphertext, private_key)
    
    # Pas 5: Convertim numărul decriptat înapoi în text
    print("\n" + "="*80)
    print("VERIFICAREA REZULTATULUI")
    print("="*80)
    decrypted_text = decimal_to_text(decrypted_numeric)
    print(f"Mesaj original: {message_text}")
    print(f"Mesaj decriptat: {decrypted_text}")
    
    if message_text == decrypted_text:
        print("\n✓ SUCCES! Mesajul a fost criptat și decriptat corect!")
    else:
        print("\n✗ EROARE! Mesajul decriptat nu corespunde cu originalul!")
    
    # Salvăm rezultatele într-un fișier
    with open('/home/fuckedupupd/cryptography/lab5_rsa_results.txt', 'w') as f:
        f.write("="*80 + "\n")
        f.write("REZULTATELE ALGORITMULUI RSA\n")
        f.write("Student: Nicolai Petcov\n")
        f.write("="*80 + "\n\n")
        
        f.write("MESAJUL:\n")
        f.write(f"Text: {message_text}\n")
        f.write(f"Hex: {message_text.encode('ascii').hex()}\n")
        f.write(f"Decimal: {message_numeric}\n\n")
        
        f.write("PARAMETRII RSA:\n")
        f.write(f"p = {p}\n")
        f.write(f"q = {q}\n")
        f.write(f"n = {n}\n")
        f.write(f"Biți în n: {n.bit_length()}\n")
        f.write(f"φ(n) = {(p-1)*(q-1)}\n")
        f.write(f"e = {e}\n")
        f.write(f"d = {d}\n\n")
        
        f.write("CRIPTARE ȘI DECRIPTARE:\n")
        f.write(f"Mesaj în clar (M): {message_numeric}\n")
        f.write(f"Text cifrat (C): {ciphertext}\n")
        f.write(f"Mesaj decriptat: {decrypted_numeric}\n")
        f.write(f"Text decriptat: {decrypted_text}\n\n")
        
        f.write("VERIFICARE:\n")
        f.write(f"Mesaj original == Mesaj decriptat: {message_text == decrypted_text}\n")
    
    print("\n✓ Rezultatele au fost salvate în 'lab5_rsa_results.txt'")

if __name__ == "__main__":
    main()
