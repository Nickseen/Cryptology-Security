"""
Lucrare de laborator nr. 6 - FUNCȚII HASH ȘI SEMNĂTURI DIGITALE
Sarcina 3 - Semnătură Digitală ElGamal
Student: Nicolai Petcov
"""

import hashlib
from sympy import isprime, gcd, mod_inverse
import random

# Parametrii dați în sarcină
P = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039

G = 2

def get_hash_function_elgamal(k):
    """
    Determină funcția hash bazată pe numărul de ordine pentru ElGamal
    Lista diferită de funcții pentru Sarcina 3
    i = (k mod 24) + 1
    """
    hash_functions = [
        "NTLM", "MD4", "MD5", "MD2", "MD6-128", "MD6-256", "MD6-512",
        "SHA-1", "SHA-224", "SHA-256", "SHA-384", "SHA-512",
        "SHA3-224", "SHA3-256", "SHA3-384", "SHA3-512",
        "RIPEMD-128", "RIPEMD-160", "RIPEMD-256", "RIPEMD-320",
        "Whirlpool", "Haval192,3", "Haval224,4", "Haval256,4"
    ]
    
    i = (k % 24) + 1
    return hash_functions[i - 1], i

def compute_hash(message, hash_name):
    """
    Calculează hash-ul mesajului folosind algoritmul specificat
    """
    print(f"\n{'='*80}")
    print(f"CALCULAREA HASH-ULUI CU {hash_name}")
    print(f"{'='*80}")
    print(f"Mesaj: {message}")
    
    message_bytes = message.encode('utf-8')
    
    # Mapare funcții hash disponibile
    if hash_name == "MD5":
        hash_obj = hashlib.md5(message_bytes)
    elif hash_name == "SHA-1":
        hash_obj = hashlib.sha1(message_bytes)
    elif hash_name == "SHA-224":
        hash_obj = hashlib.sha224(message_bytes)
    elif hash_name == "SHA-256":
        hash_obj = hashlib.sha256(message_bytes)
    elif hash_name == "SHA-384":
        hash_obj = hashlib.sha384(message_bytes)
    elif hash_name == "SHA-512":
        hash_obj = hashlib.sha512(message_bytes)
    elif hash_name == "SHA3-224":
        hash_obj = hashlib.sha3_224(message_bytes)
    elif hash_name == "SHA3-256":
        hash_obj = hashlib.sha3_256(message_bytes)
    elif hash_name == "SHA3-384":
        hash_obj = hashlib.sha3_384(message_bytes)
    elif hash_name == "SHA3-512":
        hash_obj = hashlib.sha3_512(message_bytes)
    else:
        # Pentru algoritmii care nu sunt în hashlib standard, folosim SHA-256
        print(f"Atenție: {hash_name} nu este disponibil, folosim SHA-256")
        hash_obj = hashlib.sha256(message_bytes)
    
    hash_hex = hash_obj.hexdigest()
    hash_decimal = int(hash_hex, 16)
    
    print(f"Hash (hex): {hash_hex}")
    print(f"Hash (decimal): {hash_decimal}")
    print(f"Lungimea hash: {len(hash_hex) * 4} biți")
    
    return hash_decimal, hash_hex

def generate_elgamal_keys(p, g):
    """
    Generează cheile ElGamal pentru semnătura digitală
    """
    print(f"\n{'='*80}")
    print("GENERAREA CHEILOR ELGAMAL")
    print(f"{'='*80}")
    
    print(f"Parametrii dați:")
    print(f"p = {p}")
    print(f"Biți în p: {p.bit_length()}")
    print(f"g = {g}")
    
    print(f"\nVerificăm că p este prim...")
    if isprime(p):
        print("✓ p este prim")
    else:
        print("✗ ATENȚIE: p nu este prim!")
    
    print(f"\nPas 1: Alegerea cheii private x")
    print(f"x trebuie să fie: 1 < x < p-1")
    x = random.randint(2, p - 2)
    print(f"x = {x}")
    print(f"Biți în x: {x.bit_length()}")
    
    print(f"\nPas 2: Calcularea cheii publice y = g^x mod p")
    y = pow(g, x, p)
    print(f"y = {g}^{x} mod p")
    print(f"y = {y}")
    print(f"Biți în y: {y.bit_length()}")
    
    print(f"\n{'='*80}")
    print("CHEILE GENERATE")
    print(f"{'='*80}")
    print(f"Cheia publică: (p, g={g}, y)")
    print(f"Cheia privată: x")
    print(f"{'='*80}")
    
    return (p, g, y), x

def elgamal_sign(message_hash, private_key, p, g):
    """
    Semnează hash-ul mesajului folosind semnătura ElGamal
    
    Semnătură ElGamal:
    1. Alege k aleatoriu, gcd(k, p-1) = 1
    2. r = g^k mod p
    3. s = (H(m) - x*r) * k^(-1) mod (p-1)
    
    Semnătură: (r, s)
    """
    x = private_key
    
    print(f"\n{'='*80}")
    print("SEMNAREA ELGAMAL")
    print(f"{'='*80}")
    print(f"Hash mesaj (H(m)): {message_hash}")
    print(f"Cheia privată: x")
    
    # Pas 1: Alegem k astfel încât gcd(k, p-1) = 1
    print(f"\nPas 1: Alegerea numărului aleatoriu k")
    print(f"k trebuie să satisfacă: 1 < k < p-1 și gcd(k, p-1) = 1")
    
    max_attempts = 100
    for attempt in range(max_attempts):
        k = random.randint(2, p - 2)
        if gcd(k, p - 1) == 1:
            print(f"k găsit după {attempt + 1} încercări")
            print(f"k = {k}")
            print(f"Verificare: gcd(k, p-1) = {gcd(k, p - 1)}")
            break
    else:
        print("EROARE: Nu s-a putut găsi k valid!")
        return None, None
    
    # Pas 2: Calculăm r = g^k mod p
    print(f"\nPas 2: Calcularea r = g^k mod p")
    r = pow(g, k, p)
    print(f"r = {g}^{k} mod {p}")
    print(f"r = {r}")
    
    # Pas 3: Calculăm s = (H(m) - x*r) * k^(-1) mod (p-1)
    print(f"\nPas 3: Calcularea s = (H(m) - x*r) * k^(-1) mod (p-1)")
    
    # Calculăm k^(-1) mod (p-1)
    k_inv = mod_inverse(k, p - 1)
    print(f"k^(-1) mod (p-1) calculat")
    
    # Calculăm (H(m) - x*r) mod (p-1)
    h_minus_xr = (message_hash - x * r) % (p - 1)
    print(f"(H(m) - x*r) mod (p-1) calculat")
    
    # Calculăm s
    s = (h_minus_xr * k_inv) % (p - 1)
    print(f"s = {s}")
    
    print(f"\n{'='*80}")
    print(f"SEMNĂTURĂ GENERATĂ")
    print(f"{'='*80}")
    print(f"Semnătura: (r, s)")
    print(f"r = {r}")
    print(f"s = {s}")
    print(f"{'='*80}")
    
    return r, s

def elgamal_verify(message_hash, signature, public_key):
    """
    Verifică semnătura digitală ElGamal
    
    Verificare:
    g^H(m) mod p = y^r * r^s mod p
    """
    r, s = signature
    p, g, y = public_key
    
    print(f"\n{'='*80}")
    print("VERIFICAREA SEMNĂTURII ELGAMAL")
    print(f"{'='*80}")
    print(f"Hash mesaj (H(m)): {message_hash}")
    print(f"Semnătură primită: (r, s)")
    print(f"r = {r}")
    print(f"s = {s}")
    print(f"Cheia publică: (p, g={g}, y)")
    
    # Verificăm constrângerile
    print(f"\nVerificăm constrângerile:")
    print(f"0 < r < p: {0 < r < p}")
    print(f"0 < s < p-1: {0 < s < p - 1}")
    
    if not (0 < r < p and 0 < s < p - 1):
        print("\n✗ SEMNĂTURA NU ESTE VALIDĂ!")
        print("Constrângerile nu sunt satisfăcute!")
        return False
    
    # Calculăm partea stângă: g^H(m) mod p
    print(f"\nPas 1: Calculăm g^H(m) mod p")
    left_side = pow(g, message_hash, p)
    print(f"g^H(m) mod p calculat")
    
    # Calculăm partea dreaptă: y^r * r^s mod p
    print(f"\nPas 2: Calculăm y^r * r^s mod p")
    y_r = pow(y, r, p)
    print(f"y^r mod p calculat")
    
    r_s = pow(r, s, p)
    print(f"r^s mod p calculat")
    
    right_side = (y_r * r_s) % p
    print(f"y^r * r^s mod p calculat")
    
    # Comparăm
    print(f"\nPas 3: Comparăm cele două valori")
    print(f"g^H(m) mod p = {left_side}")
    print(f"y^r * r^s mod p = {right_side}")
    
    is_valid = (left_side == right_side)
    
    if is_valid:
        print("\n✓ SEMNĂTURA ESTE VALIDĂ!")
        print("Ecuația de verificare este satisfăcută:")
        print("g^H(m) ≡ y^r * r^s (mod p)")
    else:
        print("\n✗ SEMNĂTURA NU ESTE VALIDĂ!")
        print("Ecuația de verificare nu este satisfăcută!")
    
    print(f"{'='*80}")
    
    return is_valid

def main():
    """
    Funcția principală pentru Task 3
    """
    print(f"\n{'='*80}")
    print("SARCINA 3 - SEMNĂTURĂ DIGITALĂ ELGAMAL")
    print("Student: Nicolai Petcov")
    print(f"{'='*80}")
    
    # Mesajul din Lucrarea de laborator nr. 2
    message = "Mesaj din Lucrarea de laborator nr. 2"
    
    # Determinăm funcția hash
    k = 10  # Numărul de ordine în lista grupei (modifică după necesitate)
    hash_name, index = get_hash_function_elgamal(k)
    
    print(f"\nNumăr de ordine în listă: k = {k}")
    print(f"Index funcție hash: i = (k mod 24) + 1 = ({k} mod 24) + 1 = {index}")
    print(f"Funcție hash selectată: {hash_name}")
    
    # Pas 1: Calculăm hash-ul mesajului
    message_hash, hash_hex = compute_hash(message, hash_name)
    
    # Pas 2: Generăm cheile ElGamal
    public_key, private_key = generate_elgamal_keys(P, G)
    p, g, y = public_key
    x = private_key
    
    # Pas 3: Semnăm mesajul
    r, s = elgamal_sign(message_hash, private_key, p, g)
    
    if r is None or s is None:
        print("\nERORE la semnare!")
        return
    
    # Pas 4: Verificăm semnătura
    is_valid = elgamal_verify(message_hash, (r, s), public_key)
    
    # Salvăm rezultatele
    with open('/home/fuckedupupd/cryptography/lab6_elgamal_signature_results.txt', 'w', encoding='utf-8') as f:
        f.write("="*80 + "\n")
        f.write("REZULTATELE SEMNĂTURII DIGITALE ELGAMAL\n")
        f.write("Student: Nicolai Petcov\n")
        f.write("="*80 + "\n\n")
        
        f.write("MESAJUL:\n")
        f.write(f"Text: {message}\n\n")
        
        f.write("FUNCȚIA HASH:\n")
        f.write(f"Număr de ordine (k): {k}\n")
        f.write(f"Index (i): {index}\n")
        f.write(f"Algoritm: {hash_name}\n")
        f.write(f"Hash (hex): {hash_hex}\n")
        f.write(f"Hash (decimal): {message_hash}\n\n")
        
        f.write("PARAMETRII ELGAMAL:\n")
        f.write(f"p = {p}\n")
        f.write(f"Biți în p: {p.bit_length()}\n")
        f.write(f"g = {g}\n")
        f.write(f"x (cheia privată) = {x}\n")
        f.write(f"y (cheia publică) = {y}\n\n")
        
        f.write("SEMNĂTURA DIGITALĂ:\n")
        f.write(f"r = {r}\n")
        f.write(f"s = {s}\n\n")
        
        f.write("VERIFICARE:\n")
        f.write(f"Semnătura este validă: {is_valid}\n")
        f.write(f"Ecuația verificată: g^H(m) ≡ y^r * r^s (mod p)\n")
    
    print("\n✓ Rezultatele au fost salvate în 'lab6_elgamal_signature_results.txt'")
    
    # Demonstrație: modificarea mesajului invalidează semnătura
    print(f"\n{'='*80}")
    print("DEMONSTRAȚIE: MODIFICAREA MESAJULUI")
    print(f"{'='*80}")
    
    modified_message = message + " (modificat)"
    print(f"Mesaj modificat: {modified_message}")
    
    modified_hash, _ = compute_hash(modified_message, hash_name)
    
    print("\nVerificăm semnătura cu mesajul modificat:")
    is_valid_modified = elgamal_verify(modified_hash, (r, s), public_key)
    
    if not is_valid_modified:
        print("\n✓ Corect! Semnătura nu este validă pentru mesajul modificat.")
        print("Aceasta demonstrează integritatea verificării semnăturii digitale.")

if __name__ == "__main__":
    main()
