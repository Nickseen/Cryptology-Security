# Lucrare de laborator nr. 5 - CRIPTOGRAFIA CU CHEI PUBLICE

**Student:** Nicolai Petcov  
**Temă:** Implementarea algoritmilor RSA, ElGamal și Diffie-Hellman

## Structura Proiectului

### Fișiere implementate:

1. **lab5_rsa.py** - Implementarea algoritmului RSA
2. **lab5_elgamal.py** - Implementarea algoritmului ElGamal
3. **lab5_diffie_hellman.py** - Implementarea schimbului de chei Diffie-Hellman cu AES-256

### Fișiere de rezultate (generate automat):

- `lab5_rsa_results.txt` - Rezultatele algoritmului RSA
- `lab5_elgamal_results.txt` - Rezultatele algoritmului ElGamal
- `lab5_diffie_hellman_results.txt` - Rezultatele schimbului de chei Diffie-Hellman

## Cerințe

### Biblioteci necesare:

```bash
pip install sympy pycryptodome
```

## Sarcini Implementate

### Sarcina 2.1 - Algoritmul RSA

**Fișier:** `lab5_rsa.py`

**Descriere:** Implementarea completă a algoritmului RSA cu chei de cel puțin 2048 biți.

**Pași algoritmici:**

1. **Generarea cheilor:**
   - Generarea a două numere prime mari p și q (fiecare de ~1024 biți)
   - Calcularea modulului n = p × q (≥ 2048 biți)
   - Calcularea funcției Euler φ(n) = (p-1)(q-1)
   - Alegerea exponentului public e = 65537
   - Calcularea exponentului privat d = e⁻¹ mod φ(n)

2. **Convertirea mesajului:**
   - Text → ASCII Hex → Decimal
   - Mesaj: "Nicolai Petcov"

3. **Criptarea:**
   - C = M^e mod n

4. **Decriptarea:**
   - M = C^d mod n

5. **Verificarea:**
   - Decimal → Hex → Text
   - Compararea cu mesajul original

**Rulare:**
```bash
python lab5_rsa.py
```

### Sarcina 2.2 - Algoritmul ElGamal

**Fișier:** `lab5_elgamal.py`

**Descriere:** Implementarea algoritmului ElGamal cu parametrii dați (p și g).

**Parametrii:**
- p = număr prim de 2048 biți (dat în sarcină)
- g = 2 (generatorul dat)

**Pași algoritmici:**

1. **Generarea cheilor:**
   - Alegerea cheii private x (aleatoriu, 1 < x < p-1)
   - Calcularea cheii publice y = g^x mod p

2. **Convertirea mesajului:**
   - Text → ASCII Hex → Decimal
   - Mesaj: "Nicolai Petcov"

3. **Criptarea:**
   - Alegerea numărului aleatoriu k (1 < k < p-1)
   - c₁ = g^k mod p
   - c₂ = M × y^k mod p
   - Text cifrat: (c₁, c₂)

4. **Decriptarea:**
   - s = c₁^x mod p
   - s⁻¹ = inversul modular al lui s
   - M = c₂ × s⁻¹ mod p

5. **Verificarea:**
   - Decimal → Hex → Text
   - Compararea cu mesajul original

**Rulare:**
```bash
python lab5_elgamal.py
```

### Sarcina 3 - Diffie-Hellman + AES-256

**Fișier:** `lab5_diffie_hellman.py`

**Descriere:** Implementarea schimbului de chei Diffie-Hellman pentru generarea unei chei AES-256.

**Parametrii:**
- p = număr prim de 2048 biți (același ca la ElGamal)
- g = 2 (generatorul)

**Pași algoritmici:**

1. **Schimbul de chei Diffie-Hellman:**
   - Alice alege numărul secret a (aleatoriu, 1 < a < p-1)
   - Bob alege numărul secret b (aleatoriu, 1 < b < p-1)
   - Alice calculează A = g^a mod p și îl trimite lui Bob
   - Bob calculează B = g^b mod p și îl trimite lui Alice
   - Alice calculează K = B^a mod p
   - Bob calculează K = A^b mod p
   - Verificare: K_Alice = K_Bob

2. **Derivarea cheii AES-256:**
   - Convertirea secretului comun K în bytes
   - Aplicarea SHA-256: AES_key = SHA256(K)
   - Rezultat: cheie de 32 bytes (256 biți)

3. **Demonstrație criptare AES-256:**
   - Generarea unui IV aleatoriu (16 bytes)
   - Criptarea unui mesaj de test folosind AES-256-CBC
   - Decriptarea mesajului
   - Verificarea corectitudinii

**Rulare:**
```bash
python lab5_diffie_hellman.py
```

## Explicații Tehnice

### Conversie Text → Decimal

Procesul de convertire folosit în toate sarcinile:

1. **Text → ASCII Hex:**
   - Fiecare caracter este convertit în reprezentarea sa hexazecimală ASCII
   - Exemplu: "A" → 41 (hex)

2. **ASCII Hex → Decimal:**
   - Șirul hexazecimal complet este convertit în decimal
   - Exemplu: "4E69636F6C6169205065" → număr mare în baza 10

### Securitate

#### RSA (Sarcina 2.1)
- **Dimensiunea cheii:** n ≥ 2048 biți (conform cerințelor moderne de securitate)
- **Exponentul public:** e = 65537 (valoare standard, eficientă și sigură)
- **Generarea numerelor prime:** folosind teste de primalitate probabilistice

#### ElGamal (Sarcina 2.2)
- **Modulus prim:** p de 2048 biți (dat în sarcină)
- **Aleatorizare:** fiecare criptare folosește un k aleatoriu diferit
- **Securitate:** bazată pe problema logaritmului discret

#### Diffie-Hellman (Sarcina 3)
- **Modulus prim:** p de 2048 biți
- **Numere secrete:** a și b alese aleatoriu
- **Derivarea cheii:** folosind SHA-256 pentru uniformizare
- **AES-256:** standard modern de criptare simetrică cu cheie de 256 biți

## Rezultate

Fiecare program generează un fișier de rezultate care conține:

- Parametrii utilizați
- Pașii algoritmici detaliați
- Valorile intermediare calculate
- Rezultatul final
- Verificarea corectitudinii

### Exemple de verificare:

✓ Mesajul decriptat trebuie să fie identic cu mesajul original  
✓ Toate calculele matematice sunt verificate  
✓ Cheile generate respectă condițiile algoritmice

## Notițe Importante

1. **Performanță:** 
   - Generarea cheilor RSA poate dura câteva secunde datorită căutării numerelor prime mari
   - Operațiile de exponențiere modulară sunt optimizate folosind `pow(base, exp, mod)`

2. **Aleatorizare:**
   - Se folosește generatorul de numere aleatorii din Python (`random`)
   - Pentru producție se recomandă `secrets` sau `os.urandom()`

3. **Compatibilitate:**
   - Codul este scris în Python 3
   - Funcționează pe Linux, Windows și macOS

## Autor

**Nicolai Petcov**  
Lucrare de laborator nr. 5 - Criptografia cu Chei Publice
