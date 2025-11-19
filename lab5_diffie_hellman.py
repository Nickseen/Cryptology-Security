"""
Lucrare de laborator nr. 5 - CRIPTOGRAFIA CU CHEI PUBLICE
Sarcina 3 - Schimbul de chei Diffie-Hellman cu AES-256
Student: Nicolai Petcov
"""

import random
from sympy import isprime
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import hashlib

# Parametrii dați în sarcină
P = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039

G = 2

def diffie_hellman_exchange():
    """
    Implementează schimbul de chei Diffie-Hellman între Alice și Bob
    
    Pași:
    1. Alice alege un număr secret a
    2. Bob alege un număr secret b
    3. Alice calculează A = g^a mod p și îl trimite lui Bob
    4. Bob calculează B = g^b mod p și îl trimite lui Alice
    5. Alice calculează cheia comună: K = B^a mod p
    6. Bob calculează cheia comună: K = A^b mod p
    7. Ambele chei trebuie să fie identice
    """
    print("="*80)
    print("SCHIMBUL DE CHEI DIFFIE-HELLMAN")
    print("="*80)
    
    print(f"\nParametrii publici:")
    print(f"p = {P}")
    print(f"Număr de biți în p: {P.bit_length()}")
    print(f"g = {G}")
    
    # Verificăm că p este prim
    print(f"\nVerificăm că p este prim...")
    if isprime(P):
        print("✓ p este prim")
    else:
        print("✗ ATENȚIE: p nu este prim!")
    
    # Pas 1: Alice alege numărul secret a
    print("\n" + "="*80)
    print("PAS 1: ALICE ALEGE NUMĂRUL SECRET")
    print("="*80)
    print(f"Alice alege numărul secret a, unde 1 < a < p-1")
    a = random.randint(2, P - 2)
    print(f"Numărul secret al lui Alice: a = {a}")
    
    # Pas 2: Bob alege numărul secret b
    print("\n" + "="*80)
    print("PAS 2: BOB ALEGE NUMĂRUL SECRET")
    print("="*80)
    print(f"Bob alege numărul secret b, unde 1 < b < p-1")
    b = random.randint(2, P - 2)
    print(f"Numărul secret al lui Bob: b = {b}")
    
    # Pas 3: Alice calculează A = g^a mod p
    print("\n" + "="*80)
    print("PAS 3: ALICE CALCULEAZĂ VALOAREA PUBLICĂ A")
    print("="*80)
    print(f"Alice calculează A = g^a mod p")
    A = pow(G, a, P)
    print(f"A = {G}^{a} mod {P}")
    print(f"A = {A}")
    print(f"Alice trimite A lui Bob prin canalul public")
    
    # Pas 4: Bob calculează B = g^b mod p
    print("\n" + "="*80)
    print("PAS 4: BOB CALCULEAZĂ VALOAREA PUBLICĂ B")
    print("="*80)
    print(f"Bob calculează B = g^b mod p")
    B = pow(G, b, P)
    print(f"B = {G}^{b} mod {P}")
    print(f"B = {B}")
    print(f"Bob trimite B lui Alice prin canalul public")
    
    # Pas 5: Alice calculează cheia comună K_Alice = B^a mod p
    print("\n" + "="*80)
    print("PAS 5: ALICE CALCULEAZĂ CHEIA COMUNĂ")
    print("="*80)
    print(f"Alice calculează cheia comună: K = B^a mod p")
    K_Alice = pow(B, a, P)
    print(f"K_Alice = {B}^{a} mod {P}")
    print(f"K_Alice = {K_Alice}")
    
    # Pas 6: Bob calculează cheia comună K_Bob = A^b mod p
    print("\n" + "="*80)
    print("PAS 6: BOB CALCULEAZĂ CHEIA COMUNĂ")
    print("="*80)
    print(f"Bob calculează cheia comună: K = A^b mod p")
    K_Bob = pow(A, b, P)
    print(f"K_Bob = {A}^{b} mod {P}")
    print(f"K_Bob = {K_Bob}")
    
    # Pas 7: Verificăm că cheile sunt identice
    print("\n" + "="*80)
    print("PAS 7: VERIFICAREA CHEILOR")
    print("="*80)
    print(f"K_Alice = {K_Alice}")
    print(f"K_Bob = {K_Bob}")
    print(f"K_Alice == K_Bob: {K_Alice == K_Bob}")
    
    if K_Alice == K_Bob:
        print("✓ SUCCES! Cheile sunt identice!")
        shared_key = K_Alice
    else:
        print("✗ EROARE! Cheile nu sunt identice!")
        return None, None, None, None, None, None
    
    return shared_key, a, b, A, B, K_Alice

def derive_aes_key(shared_secret):
    """
    Derivă o cheie AES-256 (32 bytes) din secretul comun Diffie-Hellman
    folosind SHA-256
    """
    print("\n" + "="*80)
    print("DERIVAREA CHEII AES-256")
    print("="*80)
    print(f"Secretul comun Diffie-Hellman: {shared_secret}")
    
    # Convertim secretul comun într-un șir de bytes
    shared_secret_bytes = shared_secret.to_bytes((shared_secret.bit_length() + 7) // 8, byteorder='big')
    print(f"Secretul comun în bytes (lungime {len(shared_secret_bytes)} bytes)")
    
    # Folosim SHA-256 pentru a deriva o cheie de exact 32 bytes (256 biți)
    aes_key = hashlib.sha256(shared_secret_bytes).digest()
    print(f"Cheia AES-256 derivată (32 bytes): {aes_key.hex()}")
    print(f"Lungimea cheii: {len(aes_key)} bytes = {len(aes_key) * 8} biți")
    
    return aes_key

def aes_encrypt(plaintext, key):
    """
    Criptează un text folosind AES-256 în modul CBC
    """
    print("\n" + "="*80)
    print("CRIPTAREA AES-256")
    print("="*80)
    print(f"Text în clar: {plaintext}")
    
    # Generăm un IV aleatoriu (16 bytes pentru AES)
    iv = get_random_bytes(16)
    print(f"IV (Vector de Inițializare): {iv.hex()}")
    
    # Creăm cipher-ul AES în modul CBC
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Convertim textul în bytes și adăugăm padding
    plaintext_bytes = plaintext.encode('utf-8')
    padded_plaintext = pad(plaintext_bytes, AES.block_size)
    print(f"Text cu padding (lungime {len(padded_plaintext)} bytes)")
    
    # Criptăm
    ciphertext = cipher.encrypt(padded_plaintext)
    print(f"Text cifrat (lungime {len(ciphertext)} bytes): {ciphertext.hex()}")
    
    return ciphertext, iv

def aes_decrypt(ciphertext, key, iv):
    """
    Decriptează un text folosind AES-256 în modul CBC
    """
    print("\n" + "="*80)
    print("DECRIPTAREA AES-256")
    print("="*80)
    print(f"Text cifrat: {ciphertext.hex()}")
    print(f"IV: {iv.hex()}")
    
    # Creăm cipher-ul AES în modul CBC cu același IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Decriptăm
    padded_plaintext = cipher.decrypt(ciphertext)
    print(f"Text decriptat cu padding (lungime {len(padded_plaintext)} bytes)")
    
    # Eliminăm padding-ul
    plaintext_bytes = unpad(padded_plaintext, AES.block_size)
    plaintext = plaintext_bytes.decode('utf-8')
    print(f"Text decriptat: {plaintext}")
    
    return plaintext

def main():
    """
    Funcția principală care demonstrează schimbul de chei Diffie-Hellman
    și utilizarea cheii pentru criptare AES-256
    """
    print("\n" + "="*80)
    print("SARCINA 3 - DIFFIE-HELLMAN + AES-256")
    print("Student: Nicolai Petcov")
    print("="*80)
    
    # Pas 1: Efectuăm schimbul de chei Diffie-Hellman
    shared_key, a, b, A, B, K = diffie_hellman_exchange()
    
    if shared_key is None:
        print("\nEroare la schimbul de chei!")
        return
    
    # Pas 2: Derivăm cheia AES-256 din secretul comun
    aes_key = derive_aes_key(shared_key)
    
    # Pas 3: Demonstrăm criptarea și decriptarea cu AES-256
    print("\n" + "="*80)
    print("DEMONSTRAȚIE: CRIPTARE ȘI DECRIPTARE CU AES-256")
    print("="*80)
    
    message = "Acest mesaj va fi criptat cu AES-256 folosind cheia derivată din Diffie-Hellman"
    print(f"\nMesajul de testat: {message}")
    
    # Alice criptează mesajul
    print("\n--- Alice criptează mesajul ---")
    ciphertext, iv = aes_encrypt(message, aes_key)
    
    # Bob decriptează mesajul
    print("\n--- Bob decriptează mesajul ---")
    decrypted_message = aes_decrypt(ciphertext, aes_key, iv)
    
    # Verificare
    print("\n" + "="*80)
    print("VERIFICAREA REZULTATULUI")
    print("="*80)
    print(f"Mesaj original: {message}")
    print(f"Mesaj decriptat: {decrypted_message}")
    
    if message == decrypted_message:
        print("\n✓ SUCCES! Mesajul a fost criptat și decriptat corect!")
    else:
        print("\n✗ EROARE! Mesajul decriptat nu corespunde cu originalul!")
    
    # Salvăm rezultatele într-un fișier
    with open('/home/fuckedupupd/cryptography/lab5_diffie_hellman_results.txt', 'w') as f:
        f.write("="*80 + "\n")
        f.write("REZULTATELE SCHIMBULUI DE CHEI DIFFIE-HELLMAN + AES-256\n")
        f.write("Student: Nicolai Petcov\n")
        f.write("="*80 + "\n\n")
        
        f.write("PARAMETRII PUBLICI:\n")
        f.write(f"p = {P}\n")
        f.write(f"Biți în p: {P.bit_length()}\n")
        f.write(f"g = {G}\n\n")
        
        f.write("NUMERE SECRETE:\n")
        f.write(f"Numărul secret al lui Alice (a) = {a}\n")
        f.write(f"Numărul secret al lui Bob (b) = {b}\n\n")
        
        f.write("VALORI PUBLICE SCHIMBATE:\n")
        f.write(f"A (trimis de Alice) = {A}\n")
        f.write(f"B (trimis de Bob) = {B}\n\n")
        
        f.write("CHEIA COMUNĂ:\n")
        f.write(f"K = {K}\n\n")
        
        f.write("CHEIA AES-256 DERIVATĂ:\n")
        f.write(f"Cheia AES (hex): {aes_key.hex()}\n")
        f.write(f"Lungimea cheii: {len(aes_key)} bytes = {len(aes_key) * 8} biți\n\n")
        
        f.write("DEMONSTRAȚIE CRIPTARE/DECRIPTARE:\n")
        f.write(f"Mesaj original: {message}\n")
        f.write(f"IV: {iv.hex()}\n")
        f.write(f"Text cifrat: {ciphertext.hex()}\n")
        f.write(f"Mesaj decriptat: {decrypted_message}\n\n")
        
        f.write("VERIFICARE:\n")
        f.write(f"Mesaj original == Mesaj decriptat: {message == decrypted_message}\n")
    
    print("\n✓ Rezultatele au fost salvate în 'lab5_diffie_hellman_results.txt'")

if __name__ == "__main__":
    main()
