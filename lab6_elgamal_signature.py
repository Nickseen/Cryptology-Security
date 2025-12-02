"""
Лабораторная работа № 6 - ХЕШ-ФУНКЦИИ И ЦИФРОВЫЕ ПОДПИСИ
Задание 3 - Цифровая подпись ElGamal
Студент: Nicolai Petcov
"""

import hashlib
from sympy import isprime, gcd, mod_inverse
import random
try:
    from Crypto.Hash import SHA256
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False

# Параметры, данные в задании
P = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039

G = 2

def get_hash_function_elgamal(k):
    """
    Определяет хеш-функцию на основе порядкового номера для ElGamal
    Другой список функций для Задания 3
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
    Вычисляет хеш сообщения, используя указанный алгоритм
    """
    print(f"\n{'='*80}")
    print(f"CALCULAREA HASH-ULUI CU {hash_name}")
    print(f"{'='*80}")
    print(f"Mesaj: {message}")
    
    message_bytes = message.encode('utf-8')
    
    # Отображение доступных хеш-функций
    # k=21 => i=22 => Haval192,3
    # Haval192,3 использует 3 прохода и выдает 192 бита
    if hash_name == "Haval192,3":
        from haval import Haval
        h = Haval(passes=3, fpt_len=192)
        h.update(message_bytes)
        hash_hex = h.hexdigest()
        hash_decimal = int(hash_hex, 16)
        
        print(f"Hash (hex): {hash_hex}")
        print(f"Hash (decimal): {hash_decimal}")
        print(f"Lungimea hash: {len(hash_hex) * 4} biți")
        
        return hash_decimal, hash_hex
    else:
        # Для других алгоритмов используем SHA-256
        hash_obj = hashlib.sha256(message_bytes)
    
    hash_hex = hash_obj.hexdigest()
    hash_decimal = int(hash_hex, 16)
    
    print(f"Hash (hex): {hash_hex}")
    print(f"Hash (decimal): {hash_decimal}")
    print(f"Lungimea hash: {len(hash_hex) * 4} biți")
    
    return hash_decimal, hash_hex

def generate_elgamal_keys(p, g):
    """
    Генерирует ключи ElGamal для цифровой подписи
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
    Подписывает хеш сообщения, используя подпись ElGamal
    
    Подпись ElGamal:
    1. Выбирает случайное k, gcd(k, p-1) = 1
    2. r = g^k mod p
    3. s = (H(m) - x*r) * k^(-1) mod (p-1)
    
    Подпись: (r, s)
    """
    x = private_key
    
    print(f"\n{'='*80}")
    print("SEMNAREA ELGAMAL")
    print(f"{'='*80}")
    print(f"Hash mesaj (H(m)): {message_hash}")
    print(f"Cheia privată: x")
    
    # Шаг 1: Выбираем k так, чтобы gcd(k, p-1) = 1
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
    
    # Шаг 2: Вычисляем r = g^k mod p
    print(f"\nPas 2: Calcularea r = g^k mod p")
    r = pow(g, k, p)
    print(f"r = {g}^{k} mod {p}")
    print(f"r = {r}")
    
    # Шаг 3: Вычисляем s = (H(m) - x*r) * k^(-1) mod (p-1)
    print(f"\nPas 3: Calcularea s = (H(m) - x*r) * k^(-1) mod (p-1)")
    
    # Вычисляем k^(-1) mod (p-1)
    k_inv = mod_inverse(k, p - 1)
    print(f"k^(-1) mod (p-1) calculat")
    
    # Вычисляем (H(m) - x*r) mod (p-1)
    h_minus_xr = (message_hash - x * r) % (p - 1)
    print(f"(H(m) - x*r) mod (p-1) calculat")
    
    # Вычисляем s
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
    Проверяет цифровую подпись ElGamal
    
    Проверка:
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
    
    # Проверяем ограничения
    print(f"\nVerificăm constrângerile:")
    print(f"0 < r < p: {0 < r < p}")
    print(f"0 < s < p-1: {0 < s < p - 1}")
    
    if not (0 < r < p and 0 < s < p - 1):
        print("\n✗ SEMNĂTURA NU ESTE VALIDĂ!")
        print("Constrângerile nu sunt satisfăcute!")
        return False
    
    # Вычисляем левую часть: g^H(m) mod p
    print(f"\nPas 1: Calculăm g^H(m) mod p")
    left_side = pow(g, message_hash, p)
    print(f"g^H(m) mod p calculat")
    
    # Вычисляем правую часть: y^r * r^s mod p
    print(f"\nPas 2: Calculăm y^r * r^s mod p")
    y_r = pow(y, r, p)
    print(f"y^r mod p calculat")
    
    r_s = pow(r, s, p)
    print(f"r^s mod p calculat")
    
    right_side = (y_r * r_s) % p
    print(f"y^r * r^s mod p calculat")
    
    # Сравниваем
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
    Главная функция для Задания 3
    """
    print(f"\n{'='*80}")
    print("SARCINA 3 - SEMNĂTURĂ DIGITALĂ ELGAMAL")
    print("Student: Nicolai Petcov")
    print(f"{'='*80}")
    
    # Сообщение из Лабораторной работы № 2
    message = "Mesaj din Lucrarea de laborator nr. 2"
    
    # Определяем хеш-функцию
    k = 21  # Порядковый номер в списке группы
    hash_name, index = get_hash_function_elgamal(k)
    
    print(f"\nNumăr de ordine în listă: k = {k}")
    print(f"Index funcție hash: i = (k mod 24) + 1 = ({k} mod 24) + 1 = {index}")
    print(f"Funcție hash selectată: {hash_name}")
    
    # Шаг 1: Вычисляем хеш сообщения
    message_hash, hash_hex = compute_hash(message, hash_name)
    
    # Шаг 2: Генерируем ключи ElGamal
    public_key, private_key = generate_elgamal_keys(P, G)
    p, g, y = public_key
    x = private_key
    
    # Шаг 3: Подписываем сообщение
    r, s = elgamal_sign(message_hash, private_key, p, g)
    
    if r is None or s is None:
        print("\nERORE la semnare!")
        return
    
    # Шаг 4: Проверяем подпись
    is_valid = elgamal_verify(message_hash, (r, s), public_key)
    
    # Сохраняем результаты
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
    
    # Демонстрация: изменение сообщения делает подпись недействительной
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
