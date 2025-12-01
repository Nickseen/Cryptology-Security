"""
Лабораторная работа № 6 - ХЕШ-ФУНКЦИИ И ЦИФРОВЫЕ ПОДПИСИ
Задание 2 - Цифровая подпись RSA
Студент: Nicolai Petcov
"""

import hashlib
from sympy import isprime, gcd, mod_inverse
import random

# Для определения хеш-функции
# k = порядковый номер в списке группы (предполагаем k=10 для примера)
# i = (k mod 24) + 1
# Например: k=10 => i = (10 mod 24) + 1 = 11 => SHA-512

def get_hash_function(k):
    """
    Определяет хеш-функцию на основе порядкового номера
    i = (k mod 24) + 1
    """
    hash_functions = [
        "MD4", "MD5", "MD2", "MD6-128", "MD6-256", "MD6-512",
        "SHA-1", "SHA-224", "SHA-256", "SHA-384", "SHA-512",
        "SHA3-224", "SHA3-256", "SHA3-384", "SHA3-512",
        "RIPEMD-128", "RIPEMD-160", "RIPEMD-256", "RIPEMD-320",
        "Whirlpool", "NTLM", "Haval192,3", "Haval224,4", "Haval256,4"
    ]
    
    i = (k % 24) + 1
    return hash_functions[i - 1], i

def compute_hash(message, hash_name):
    """
    Вычисляет хеш сообщения, используя указанный алгоритм
    """
    print(f"\n{'='*80}")
    print(f"CALCULAREA HASH-ULUI CU {hash_name}")
    print(f"{'='*80}")
    print(f"Mesaj: {message}")
    
    message_bytes = message.encode('utf-8')
    
    # Отображение доступных хеш-функций
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
        # Для алгоритмов, которых нет в стандартном hashlib, используем SHA-256
        print(f"Atenție: {hash_name} nu este disponibil, folosim SHA-256")
        hash_obj = hashlib.sha256(message_bytes)
    
    hash_hex = hash_obj.hexdigest()
    hash_decimal = int(hash_hex, 16)
    
    print(f"Hash (hex): {hash_hex}")
    print(f"Hash (decimal): {hash_decimal}")
    print(f"Lungimea hash: {len(hash_hex) * 4} biți")
    
    return hash_decimal, hash_hex

def generate_large_prime(bits):
    """
    Генерирует большое простое число с указанным количеством битов
    """
    print(f"Generare număr prim de {bits} biți...")
    while True:
        candidate = random.getrandbits(bits)
        candidate |= (1 << (bits - 1))
        candidate |= 1
        
        if isprime(candidate):
            print(f"Număr prim găsit!")
            return candidate

def generate_rsa_keys(bits=3072):
    """
    Генерирует ключи RSA с модулем n не менее 3072 бит
    """
    print(f"\n{'='*80}")
    print("GENERAREA CHEILOR RSA")
    print(f"{'='*80}")
    print(f"Cerință: modulul n trebuie să aibă cel puțin {bits} biți")
    
    half_bits = bits // 2
    
    print(f"\nPas 1: Generarea numerelor prime p și q")
    p = generate_large_prime(half_bits)
    print(f"p = {p}")
    print(f"Biți în p: {p.bit_length()}")
    
    q = generate_large_prime(half_bits)
    print(f"\nq = {q}")
    print(f"Biți în q: {q.bit_length()}")
    
    print(f"\nPas 2: Calcularea modulului n = p × q")
    n = p * q
    print(f"n = {n}")
    print(f"Biți în n: {n.bit_length()}")
    
    if n.bit_length() < bits:
        print(f"Atenție: n are doar {n.bit_length()} biți, regenerăm...")
        return generate_rsa_keys(bits)
    
    print(f"\nPas 3: Calcularea funcției Euler φ(n) = (p-1)(q-1)")
    phi_n = (p - 1) * (q - 1)
    print(f"φ(n) calculat")
    
    print(f"\nPas 4: Alegerea exponentului public e")
    e = 65537
    print(f"e = {e}")
    print(f"Verificăm că gcd(e, φ(n)) = 1")
    gcd_value = gcd(e, phi_n)
    print(f"gcd({e}, φ(n)) = {gcd_value}")
    
    if gcd_value != 1:
        print("EROARE: gcd(e, φ(n)) != 1. Regenerăm...")
        return generate_rsa_keys(bits)
    
    print(f"\nPas 5: Calcularea exponentului privat d = e^(-1) mod φ(n)")
    d = mod_inverse(e, phi_n)
    print(f"d calculat")
    
    verification = (d * e) % phi_n
    print(f"\nVerificare: (d × e) mod φ(n) = {verification}")
    if verification == 1:
        print("✓ Verificare reușită!")
    
    print(f"\n{'='*80}")
    print("CHEILE GENERATE")
    print(f"{'='*80}")
    print(f"Cheia publică: (e={e}, n cu {n.bit_length()} biți)")
    print(f"Cheia privată: (d cu {d.bit_length()} biți, n cu {n.bit_length()} biți)")
    print(f"{'='*80}")
    
    return (e, n), (d, n), p, q

def rsa_sign(message_hash, private_key):
    """
    Подписывает хеш сообщения, используя закрытый ключ RSA
    
    Подпись: S = H(m)^d mod n
    """
    d, n = private_key
    
    print(f"\n{'='*80}")
    print("SEMNAREA RSA")
    print(f"{'='*80}")
    print(f"Hash mesaj (H(m)): {message_hash}")
    print(f"Cheia privată: d, n")
    
    if message_hash >= n:
        print("EROARE: Hash-ul este prea mare pentru modulus n!")
        return None
    
    print(f"\nCalculăm semnătura: S = H(m)^d mod n")
    signature = pow(message_hash, d, n)
    
    print(f"Semnătură (S): {signature}")
    print(f"{'='*80}")
    
    return signature

def rsa_verify(message_hash, signature, public_key):
    """
    Проверяет цифровую подпись, используя открытый ключ RSA
    
    Проверка: H(m) = S^e mod n
    """
    e, n = public_key
    
    print(f"\n{'='*80}")
    print("VERIFICAREA SEMNĂTURII RSA")
    print(f"{'='*80}")
    print(f"Hash mesaj original (H(m)): {message_hash}")
    print(f"Semnătură primită (S): {signature}")
    print(f"Cheia publică: e={e}, n")
    
    print(f"\nCalculăm: H'(m) = S^e mod n")
    computed_hash = pow(signature, e, n)
    
    print(f"Hash calculat (H'(m)): {computed_hash}")
    
    print(f"\nComparăm H(m) cu H'(m):")
    print(f"H(m)  = {message_hash}")
    print(f"H'(m) = {computed_hash}")
    
    is_valid = (message_hash == computed_hash)
    
    if is_valid:
        print("\n✓ SEMNĂTURA ESTE VALIDĂ!")
        print("Hash-ul calculat din semnătură coincide cu hash-ul original.")
    else:
        print("\n✗ SEMNĂTURA NU ESTE VALIDĂ!")
        print("Hash-urile nu coincid!")
    
    print(f"{'='*80}")
    
    return is_valid

def main():
    """
    Главная функция для Задания 2
    """
    print(f"\n{'='*80}")
    print("SARCINA 2 - SEMNĂTURĂ DIGITALĂ RSA")
    print("Student: Nicolai Petcov")
    print(f"{'='*80}")
    
    # Сообщение из Лабораторной работы № 2
    # Предполагаем, что вы получили это сообщение
    message = "Mesaj din Lucrarea de laborator nr. 2"
    
    # Определяем хеш-функцию
    k = 10  # Порядковый номер в списке группы (измените при необходимости)
    hash_name, index = get_hash_function(k)
    
    print(f"\nNumăr de ordine în listă: k = {k}")
    print(f"Index funcție hash: i = (k mod 24) + 1 = ({k} mod 24) + 1 = {index}")
    print(f"Funcție hash selectată: {hash_name}")
    
    # Шаг 1: Вычисляем хеш сообщения
    message_hash, hash_hex = compute_hash(message, hash_name)
    
    # Шаг 2: Генерируем ключи RSA (n ≥ 3072 бит)
    public_key, private_key, p, q = generate_rsa_keys(bits=3072)
    e, n = public_key
    d, _ = private_key
    
    # Шаг 3: Подписываем сообщение
    signature = rsa_sign(message_hash, private_key)
    
    if signature is None:
        print("\nERORE la semnare!")
        return
    
    # Шаг 4: Проверяем подпись
    is_valid = rsa_verify(message_hash, signature, public_key)
    
    # Сохраняем результаты
    with open('/home/fuckedupupd/cryptography/lab6_rsa_signature_results.txt', 'w', encoding='utf-8') as f:
        f.write("="*80 + "\n")
        f.write("REZULTATELE SEMNĂTURII DIGITALE RSA\n")
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
        
        f.write("PARAMETRII RSA:\n")
        f.write(f"p = {p}\n")
        f.write(f"q = {q}\n")
        f.write(f"n = {n}\n")
        f.write(f"Biți în n: {n.bit_length()}\n")
        f.write(f"φ(n) = {(p-1)*(q-1)}\n")
        f.write(f"e = {e}\n")
        f.write(f"d = {d}\n\n")
        
        f.write("SEMNĂTURA DIGITALĂ:\n")
        f.write(f"Semnătură (S): {signature}\n\n")
        
        f.write("VERIFICARE:\n")
        f.write(f"Semnătura este validă: {is_valid}\n")
    
    print("\n✓ Rezultatele au fost salvate în 'lab6_rsa_signature_results.txt'")
    
    # Демонстрация: изменение сообщения делает подпись недействительной
    print(f"\n{'='*80}")
    print("DEMONSTRAȚIE: MODIFICAREA MESAJULUI")
    print(f"{'='*80}")
    
    modified_message = message + " (modificat)"
    print(f"Mesaj modificat: {modified_message}")
    
    modified_hash, _ = compute_hash(modified_message, hash_name)
    
    print("\nVerificăm semnătura cu mesajul modificat:")
    is_valid_modified = rsa_verify(modified_hash, signature, public_key)
    
    if not is_valid_modified:
        print("\n✓ Corect! Semnătura nu este validă pentru mesajul modificat.")
        print("Aceasta demonstrează integritatea verificării semnăturii digitale.")

if __name__ == "__main__":
    main()
