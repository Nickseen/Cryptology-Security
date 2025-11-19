"""
Lucrare de laborator nr. 5 - CRIPTOGRAFIA CU CHEI PUBLICE
Sarcina 2.2 - Algoritmul ElGamal
Student: Nicolai Petcov
"""

import random
from sympy import isprime, mod_inverse

# Parametrii dați în sarcină
P = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039

G = 2

def text_to_decimal(text):
    """
    Convertește textul în reprezentare numerică zecimală
    prin intermediul reprezentării hexazecimale ASCII
    """
    hex_string = text.encode('ascii').hex()
    decimal_value = int(hex_string, 16)
    print(f"Text original: {text}")
    print(f"Reprezentare hexazecimală: {hex_string}")
    print(f"Reprezentare zecimală: {decimal_value}")
    return decimal_value

def decimal_to_text(decimal_value):
    """
    Convertește un număr zecimal înapoi în text
    """
    hex_string = hex(decimal_value)[2:]
    if len(hex_string) % 2 != 0:
        hex_string = '0' + hex_string
    text = bytes.fromhex(hex_string).decode('ascii')
    return text

def generate_elgamal_keys(p, g):
    """
    Generează cheile pentru algoritmul ElGamal
    
    Parametri:
        p - număr prim mare
        g - generator al grupului
    
    Pași:
    1. Alegem un număr aleatoriu x (cheia privată) unde 1 < x < p-1
    2. Calculăm y = g^x mod p (cheia publică)
    
    Cheia publică: (p, g, y)
    Cheia privată: x
    """
    print("="*80)
    print("GENERAREA CHEILOR ELGAMAL")
    print("="*80)
    
    print(f"\nParametrii dați:")
    print(f"p = {p}")
    print(f"Număr de biți în p: {p.bit_length()}")
    print(f"g = {g}")
    
    # Verificăm că p este prim
    print(f"\nVerificăm că p este prim...")
    if isprime(p):
        print("✓ p este prim")
    else:
        print("✗ ATENȚIE: p nu este prim!")
    
    # Pas 1: Alegem cheia privată x
    print(f"\nPas 1: Alegerea cheii private x")
    print(f"x trebuie să fie: 1 < x < p-1")
    x = random.randint(2, p - 2)
    print(f"x = {x}")
    
    # Pas 2: Calculăm cheia publică y = g^x mod p
    print(f"\nPas 2: Calcularea cheii publice y")
    print(f"y = g^x mod p")
    y = pow(g, x, p)
    print(f"y = {g}^{x} mod {p}")
    print(f"y = {y}")
    
    print(f"\n" + "="*80)
    print("CHEILE GENERATE")
    print("="*80)
    print(f"Cheia publică: (p={p}, g={g}, y={y})")
    print(f"Cheia privată: x={x}")
    print("="*80)
    
    return (p, g, y), x

def elgamal_encrypt(message, public_key):
    """
    Criptează un mesaj folosind algoritmul ElGamal
    
    Parametri:
        message - mesajul de criptat (număr)
        public_key - (p, g, y)
    
    Pași:
    1. Alegem un număr aleatoriu k unde 1 < k < p-1 și gcd(k, p-1) = 1
    2. Calculăm c1 = g^k mod p
    3. Calculăm c2 = M * y^k mod p
    
    Textul cifrat: (c1, c2)
    """
    p, g, y = public_key
    
    print("\n" + "="*80)
    print("CRIPTAREA ELGAMAL")
    print("="*80)
    print(f"Mesaj în clar (M): {message}")
    print(f"Cheia publică: p={p}, g={g}, y={y}")
    
    # Pas 1: Alegem k aleatoriu
    print(f"\nPas 1: Alegerea numărului aleatoriu k")
    print(f"k trebuie să fie: 1 < k < p-1")
    k = random.randint(2, p - 2)
    print(f"k = {k}")
    
    # Pas 2: Calculăm c1 = g^k mod p
    print(f"\nPas 2: Calcularea c1")
    print(f"c1 = g^k mod p")
    c1 = pow(g, k, p)
    print(f"c1 = {g}^{k} mod {p}")
    print(f"c1 = {c1}")
    
    # Pas 3: Calculăm c2 = M * y^k mod p
    print(f"\nPas 3: Calcularea c2")
    print(f"c2 = M * y^k mod p")
    y_k = pow(y, k, p)
    print(f"y^k mod p = {y}^{k} mod {p} = {y_k}")
    c2 = (message * y_k) % p
    print(f"c2 = {message} * {y_k} mod {p}")
    print(f"c2 = {c2}")
    
    print(f"\nTextul cifrat: (c1={c1}, c2={c2})")
    print("="*80)
    
    return c1, c2, k

def elgamal_decrypt(ciphertext, private_key, p):
    """
    Decriptează un mesaj folosind algoritmul ElGamal
    
    Parametri:
        ciphertext - (c1, c2)
        private_key - x
        p - modulul
    
    Pași:
    1. Calculăm s = c1^x mod p
    2. Calculăm s^(-1) mod p (inversul modular al lui s)
    3. Calculăm M = c2 * s^(-1) mod p
    """
    c1, c2 = ciphertext
    x = private_key
    
    print("\n" + "="*80)
    print("DECRIPTAREA ELGAMAL")
    print("="*80)
    print(f"Text cifrat: (c1={c1}, c2={c2})")
    print(f"Cheia privată: x={x}")
    
    # Pas 1: Calculăm s = c1^x mod p
    print(f"\nPas 1: Calcularea s = c1^x mod p")
    s = pow(c1, x, p)
    print(f"s = {c1}^{x} mod {p}")
    print(f"s = {s}")
    
    # Pas 2: Calculăm s^(-1) mod p
    print(f"\nPas 2: Calcularea inversului modular s^(-1) mod p")
    s_inv = mod_inverse(s, p)
    print(f"s^(-1) mod p = {s_inv}")
    
    # Verificare: s * s^(-1) mod p = 1
    verification = (s * s_inv) % p
    print(f"Verificare: s * s^(-1) mod p = {verification}")
    if verification == 1:
        print("✓ Inversul modular este corect")
    
    # Pas 3: Calculăm M = c2 * s^(-1) mod p
    print(f"\nPas 3: Calcularea mesajului M = c2 * s^(-1) mod p")
    plaintext = (c2 * s_inv) % p
    print(f"M = {c2} * {s_inv} mod {p}")
    print(f"M = {plaintext}")
    
    print("="*80)
    
    return plaintext

def main():
    """
    Funcția principală care execută algoritmul ElGamal complet
    """
    print("\n" + "="*80)
    print("SARCINA 2.2 - ALGORITMUL ELGAMAL")
    print("Student: Nicolai Petcov")
    print("="*80)
    
    # Mesajul original
    message_text = "Nicolai Petcov"
    
    # Pas 1: Convertim textul în număr
    print("\n" + "="*80)
    print("CONVERTIREA MESAJULUI")
    print("="*80)
    message_numeric = text_to_decimal(message_text)
    
    # Verificăm că mesajul este mai mic decât p
    if message_numeric >= P:
        print("\nERORE: Mesajul este prea mare pentru modulul p!")
        return
    
    # Pas 2: Generăm cheile ElGamal
    public_key, private_key = generate_elgamal_keys(P, G)
    p, g, y = public_key
    x = private_key
    
    # Pas 3: Criptăm mesajul
    c1, c2, k = elgamal_encrypt(message_numeric, public_key)
    
    # Pas 4: Decriptăm mesajul
    decrypted_numeric = elgamal_decrypt((c1, c2), private_key, p)
    
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
    with open('/home/fuckedupupd/cryptography/lab5_elgamal_results.txt', 'w') as f:
        f.write("="*80 + "\n")
        f.write("REZULTATELE ALGORITMULUI ELGAMAL\n")
        f.write("Student: Nicolai Petcov\n")
        f.write("="*80 + "\n\n")
        
        f.write("MESAJUL:\n")
        f.write(f"Text: {message_text}\n")
        f.write(f"Hex: {message_text.encode('ascii').hex()}\n")
        f.write(f"Decimal: {message_numeric}\n\n")
        
        f.write("PARAMETRII ELGAMAL:\n")
        f.write(f"p = {p}\n")
        f.write(f"Biți în p: {p.bit_length()}\n")
        f.write(f"g = {g}\n")
        f.write(f"x (cheia privată) = {x}\n")
        f.write(f"y (cheia publică) = {y}\n")
        f.write(f"k (număr aleatoriu pentru criptare) = {k}\n\n")
        
        f.write("CRIPTARE ȘI DECRIPTARE:\n")
        f.write(f"Mesaj în clar (M): {message_numeric}\n")
        f.write(f"c1 = {c1}\n")
        f.write(f"c2 = {c2}\n")
        f.write(f"Mesaj decriptat: {decrypted_numeric}\n")
        f.write(f"Text decriptat: {decrypted_text}\n\n")
        
        f.write("VERIFICARE:\n")
        f.write(f"Mesaj original == Mesaj decriptat: {message_text == decrypted_text}\n")
    
    print("\n✓ Rezultatele au fost salvate în 'lab5_elgamal_results.txt'")

if __name__ == "__main__":
    main()
