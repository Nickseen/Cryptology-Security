# Lucrare de laborator nr. 6 - FUNCȚII HASH ȘI SEMNĂTURI DIGITALE

**Student:** Nicolai Petcov  
**Temă:** Implementarea funcțiilor hash și semnăturilor digitale (RSA și ElGamal)

## Structura Proiectului

### Fișiere implementate:

1. **lab6_rsa_signature.py** - Semnătură digitală RSA
2. **lab6_elgamal_signature.py** - Semnătură digitală ElGamal

### Fișiere de rezultate (generate automat):

- `lab6_rsa_signature_results.txt` - Rezultatele semnăturii RSA
- `lab6_elgamal_signature_results.txt` - Rezultatele semnăturii ElGamal

## Cerințe

### Biblioteci necesare:

```bash
pip install sympy
```

## Sarcini Implementate

### Sarcina 2 - Semnătură Digitală RSA

**Fișier:** `lab6_rsa_signature.py`

**Descriere:** Implementarea semnăturii digitale RSA cu chei de cel puțin 3072 biți.

**Pași algoritmici:**

1. **Determinarea funcției hash:**
   - Formula: i = (k mod 24) + 1
   - k = numărul de ordine în lista grupei
   - Se selectează funcția hash din lista dată

2. **Calcularea hash-ului mesajului:**
   - Mesaj din Lucrarea de laborator nr. 2
   - H(m) = hash(mesaj)
   - Conversie în reprezentare zecimală

3. **Generarea cheilor RSA:**
   - p și q - numere prime mari (≥1536 biți fiecare)
   - n = p × q (≥ 3072 biți)
   - φ(n) = (p-1)(q-1)
   - e = 65537
   - d = e⁻¹ mod φ(n)

4. **Semnarea:**
   - S = H(m)^d mod n

5. **Verificarea:**
   - H'(m) = S^e mod n
   - Verificare: H'(m) = H(m)

**Rulare:**
```bash
python lab6_rsa_signature.py
```

### Sarcina 3 - Semnătură Digitală ElGamal

**Fișier:** `lab6_elgamal_signature.py`

**Descriere:** Implementarea semnăturii digitale ElGamal cu parametrii dați.

**Parametrii:**
- p = număr prim de 2048 biți (dat în sarcină)
- g = 2 (generatorul dat)

**Pași algoritmici:**

1. **Determinarea funcției hash:**
   - Formula: i = (k mod 24) + 1
   - Lista diferită de funcții hash pentru Sarcina 3

2. **Calcularea hash-ului mesajului:**
   - H(m) = hash(mesaj)
   - Conversie în decimal

3. **Generarea cheilor ElGamal:**
   - x - cheia privată (aleatoriu, 1 < x < p-1)
   - y = g^x mod p - cheia publică

4. **Semnarea:**
   - Alege k aleatoriu: gcd(k, p-1) = 1
   - r = g^k mod p
   - s = (H(m) - x×r) × k⁻¹ mod (p-1)
   - Semnătură: (r, s)

5. **Verificarea:**
   - Verificare: g^H(m) ≡ y^r × r^s (mod p)

**Rulare:**
```bash
python lab6_elgamal_signature.py
```

## Explicații Teoretice

### 1. Funcții Hash Criptografice

#### Ce este o funcție hash?
O funcție hash criptografică H este o funcție matematică care:
- Primește un mesaj de lungime arbitrară
- Returnează un "digest" (hash) de lungime fixă
- Este deterministic: același input → același output

#### Proprietăți esențiale:

1. **Eficiență**: Rapid de calculat H(m)

2. **Unidirecționalitate (One-way)**:
   - Ușor: m → H(m)
   - Imposibil practic: H(m) → m

3. **Rezistență la coliziuni**:
   - **Coliziune**: două mesaje diferite cu același hash
   - Imposibil practic să găsești m₁ ≠ m₂ cu H(m₁) = H(m₂)

4. **Rezistență la a doua preimage**:
   - Dat m₁, imposibil să găsești m₂ ≠ m₁ cu H(m₁) = H(m₂)

5. **Efect avalanșă**:
   - Schimbarea unui singur bit în input schimbă ~50% din biții output-ului

#### Algoritmi hash populari:

**Familie MD (Message Digest):**
- **MD5**: 128 biți - ÎNVECHIT, vulnerabil la coliziuni
- **MD4**, **MD2**: Mai vechi, nesigure

**Familie SHA (Secure Hash Algorithm):**
- **SHA-1**: 160 biți - depreciat (2017)
- **SHA-2**:
  - SHA-224: 224 biți
  - SHA-256: 256 biți ✓
  - SHA-384: 384 biți ✓
  - SHA-512: 512 biți ✓
- **SHA-3**: Standard nou (2015)
  - SHA3-224, SHA3-256, SHA3-384, SHA3-512 ✓

**Altele:**
- **RIPEMD**: 128, 160, 256, 320 biți
- **Whirlpool**: 512 biți

### 2. Semnături Digitale

#### Ce este o semnătură digitală?

Analog electronic al semnăturii de mână, oferă:

1. **Autenticitate**: Confirmă identitatea semnatarului
2. **Integritate**: Detectează orice modificare a mesajului
3. **Non-repudiere**: Semnatarul nu poate nega că a semnat

#### Proces general:

**Semnare:**
```
1. Calculează h = H(m)
2. Semnează hash-ul cu cheia privată: s = Sign(h, private_key)
3. Transmite (m, s)
```

**Verificare:**
```
1. Calculează h = H(m)
2. Verifică semnătura cu cheia publică: Verify(h, s, public_key)
3. Acceptă dacă verificarea reușește
```

#### De ce folosim hash?

- Mesajele pot fi foarte mari
- Operațiile cu chei publice sunt lente
- Hash-ul este fix și mic (256-512 biți)
- Semnăm hash-ul în loc de mesajul întreg

### 3. Semnătura Digitală RSA

#### Schema RSA pentru semnături:

**Generarea cheilor:** (identic cu RSA pentru criptare)
- p, q - numere prime mari
- n = p × q
- φ(n) = (p-1)(q-1)
- e - exponent public (de obicei 65537)
- d = e⁻¹ mod φ(n) - exponent privat

**Chei:**
- Publică: (e, n)
- Privată: (d, n)

**Semnare:**
```
S = H(m)^d mod n
```
Unde:
- H(m) = hash-ul mesajului
- d = cheia privată
- S = semnătura

**Verificare:**
```
H'(m) = S^e mod n
Verificare: H'(m) == H(m)
```

Unde:
- e = cheia publică
- S = semnătura primită
- H(m) = hash-ul mesajului original

#### De ce funcționează?

Bazat pe același principiu ca criptarea RSA:
```
S^e = (H(m)^d)^e = H(m)^(de) = H(m)^(1 mod φ(n)) = H(m) mod n
```

#### Securitate:

- **Bază**: Imposibilitatea factorizării lui n
- **Dimensiune cheie**: Minim 3072 biți (2025)
- **Vulnerabilități**:
  - Atacuri cu text ales (necesită padding: PSS)
  - Factorizare cu computere cuantice

### 4. Semnătura Digitală ElGamal

#### Schema ElGamal pentru semnături:

**Parametri publici:**
- p - număr prim mare
- g - generator al grupului

**Generarea cheilor:**
- x - cheia privată (aleatoriu, 1 < x < p-1)
- y = g^x mod p - cheia publică

**Chei:**
- Publică: (p, g, y)
- Privată: x

**Semnare:**

1. Alege k aleatoriu: 1 < k < p-1, gcd(k, p-1) = 1
2. Calculează r = g^k mod p
3. Calculează s = (H(m) - x×r) × k⁻¹ mod (p-1)
4. Semnătura: (r, s)

**Verificare:**

Verifică dacă:
```
g^H(m) ≡ y^r × r^s (mod p)
```

#### De ce funcționează?

Demonstrație:
```
y^r × r^s = (g^x)^r × (g^k)^s
         = g^(xr) × g^(ks)
         = g^(xr + ks)
         
Dar s = (H(m) - xr) × k⁻¹ mod (p-1)
Deci: ks = H(m) - xr mod (p-1)
      xr + ks = H(m) mod (p-1)

Prin teorema lui Fermat:
g^H(m) ≡ g^(xr + ks) (mod p)
```

#### Caracteristici importante:

- **k diferit pentru fiecare semnătură!**
  - Reutilizarea lui k compromite cheia privată x
  - Dacă k este descoperit, x poate fi calculat
  
- **Semnătura probabilistică:**
  - Aceeași mesaj → semnături diferite (datorită k aleatoriu)
  
- **Dimensiunea semnăturii:**
  - (r, s) = 2 numere de ~dimensiunea lui p
  - Mai mare decât RSA

#### Securitate:

- **Bază**: Problema logaritmului discret
- **Dimensiune**: p trebuie ≥ 2048 biți
- **Vulnerabilități**:
  - Reutilizarea lui k
  - k slab sau previzibil
  - Atacuri cu computere cuantice

### 5. Comparație RSA vs ElGamal

| Caracteristică | RSA | ElGamal |
|---------------|-----|---------|
| **Bază matematică** | Factorizare | Logaritm discret |
| **Dimensiune semnătură** | 1 număr (≈n) | 2 numere (r, s) |
| **Determinism** | Da | Nu (aleatoriu k) |
| **Viteză semnare** | Medie | Mai lentă |
| **Viteză verificare** | Rapidă (e mic) | Medie |
| **Popularitate** | Foarte răspândit | Mai rar |
| **Variante** | PSS, PKCS#1 | DSA, ECDSA |

### 6. Aplicații Practice

#### Semnături digitale folosite în:

1. **Criptocurrency (Bitcoin, Ethereum)**:
   - ECDSA (variantă ElGamal pe curbe eliptice)
   - Validare tranzacții

2. **SSL/TLS (HTTPS)**:
   - Semnarea certificatelor
   - RSA sau ECDSA

3. **Email (S/MIME, PGP)**:
   - Semnarea mesajelor
   - RSA sau DSA

4. **Documente digitale**:
   - PDF signing
   - Documente guvernamentale

5. **Software**:
   - Code signing
   - Actualizări software

6. **Blockchain smart contracts**:
   - Autorizare tranzacții
   - Identitate digitală

### 7. Atacuri și Vulnerabilități

#### Pe funcții hash:

1. **Atacuri cu coliziuni**:
   - MD5: spart (2004)
   - SHA-1: spart (2017)
   - Soluție: folosește SHA-256 sau SHA-3

2. **Atacuri birthday**:
   - Probabilitate găsire coliziune: ~2^(n/2) pentru hash de n biți
   - SHA-256: ~2^128 operații (imposibil practic)

3. **Length extension**:
   - Vulnerabilitate în SHA-1, SHA-2
   - Nu afectează SHA-3

#### Pe semnături:

1. **Reutilizarea lui k (ElGamal)**:
   - Sony PlayStation 3 hack (2010)
   - k constant → cheia privată descoperită

2. **Existential forgery**:
   - Necesită padding (PSS pentru RSA)

3. **Timing attacks**:
   - Analiza timpului de execuție
   - Soluție: operații în timp constant

4. **Side-channel attacks**:
   - Analiza consumului electric
   - Emisii electromagnetice

### 8. Standarde și Best Practices

#### Dimensiuni recomandate (2025):

| Algoritm | Minim | Recomandat |
|----------|-------|------------|
| RSA | 3072 biți | 4096 biți |
| ElGamal/DSA | 2048 biți | 3072 biți |
| Hash pentru RSA-3072 | SHA-256 | SHA-512 |
| Hash pentru RSA-4096 | SHA-384 | SHA-512 |

#### Padding schemes:

**RSA**:
- **PSS (Probabilistic Signature Scheme)**: Standard modern
- **PKCS#1 v1.5**: Mai vechi, depreciat

**ElGamal**:
- K trebuie generat criptografic sigur
- Nu reutiliza niciodată k

#### Generarea numerelor aleatorii:

- Folosește CSRNG (Cryptographically Secure RNG)
- Python: `secrets` sau `os.urandom()`
- NU folosi `random.random()` pentru criptografie!

### 9. Post-Quantum Cryptography

#### Vulnerabilitate cuantică:

**Algoritmul Shor** (computer cuantic):
- Sparge RSA în timp polinomial
- Sparge ElGamal/DSA în timp polinomial
- Amenințare pentru toate semnăturile actuale bazate pe factorizare/logaritm discret

#### Alternative post-quantum:

**NIST standarde (2024)**:
1. **CRYSTALS-Dilithium**: Lattice-based
2. **FALCON**: Lattice-based
3. **SPHINCS+**: Hash-based

#### Hash-uri:
- SHA-256, SHA-3 rămân sigure
- Grover reduce securitatea la jumătate
- SHA-256 → ~128 biți securitate cuantică (încă suficient)

### 10. Implementare Corectă

#### Checklist pentru securitate:

✅ Folosește biblioteci criptografice testate (OpenSSL, libsodium)  
✅ Nu implementa propria criptografie în producție  
✅ Folosește padding corespunzător (PSS pentru RSA)  
✅ Generează k aleatoriu și unic pentru fiecare semnătură ElGamal  
✅ Folosește CSRNG pentru toate numerele aleatorii  
✅ Validează toate input-urile  
✅ Protejează cheile private  
✅ Folosește dimensiuni de chei adecvate  
✅ Alege funcții hash moderne (SHA-256+)  
✅ Implementează protecție împotriva timing attacks  

#### Erori comune:

❌ k constant în ElGamal  
❌ Numere aleatorii slabe  
❌ MD5 sau SHA-1 pentru noi sisteme  
❌ Chei RSA < 2048 biți  
❌ Lipsa padding-ului  
❌ Ignorarea verificării semnăturii  
❌ Stocarea nesigură a cheilor private  

## Autor

**Nicolai Petcov**  
Lucrare de laborator nr. 6 - Funcții Hash și Semnături Digitale
