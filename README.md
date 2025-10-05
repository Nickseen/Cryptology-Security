# Laboratory Work №2 – Cryptanalysis of Monoalphabetic Ciphers

**Author:** Petcov Nicolai, FAF-233  
**Course:** Information Security and Cryptography  
**Institution:** Technical University of Moldova  

## Overview
This laboratory work demonstrates the vulnerabilities of monoalphabetic substitution ciphers and applies frequency analysis techniques to decrypt an intercepted cryptogram.

## Objectives
- Study frequency analysis in cryptography  
- Understand monoalphabetic cipher weaknesses  
- Break a given ciphertext using statistical methods  
- Recover the original encryption key  
- Document the cryptanalysis process  

## Key Steps
1. **Frequency Counting** – Analyze letter frequencies in ciphertext  
2. **Initial Mapping** – Match frequent letters with English patterns  
3. **Pattern Recognition** – Identify digraphs, trigraphs, and common words  
4. **Progressive Decryption** – Iteratively refine mappings  
5. **Key Recovery** – Obtain full substitution key  
6. **Validation** – Verify decrypted text readability  

## Results
- Successfully decrypted a long ciphertext using frequency analysis  
- Recovered the full substitution key  
- Proved monoalphabetic ciphers are insecure for practical use  

## Conclusions
- Monoalphabetic ciphers are highly vulnerable to frequency attacks  
- Cryptanalysis becomes easier with longer texts  
- Secure systems must avoid statistical patterns in ciphertext  

## Source Code
🔗 [GitHub Repository](https://github.com/Nickseen/Cryptology-Security/tree/Lab2)
