# RSA Key Generation and Encryption Implementation in Python

This directory contains an implementation of **RSA Key Generation and Encryption** in Python. The script generates RSA keys, encrypts a message, and decrypts it.

## Table of Contents
- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Setup and Installation](#setup-and-installation)
- [How to Run](#how-to-run)
- [Example Usage](#example-usage)
- [How It Works](#how-it-works)
- [Limitations](#limitations)

## Overview
This implementation performs:
- Generation of RSA public and private keys.
- Encryption of a given numerical message.
- Decryption of the message using the private key.

## Tech Stack
- **Programming Language**: Python

## Setup and Installation
### Prerequisites
Ensure Python 3.6+ is installed on your system.

### Clone the Repository
```bash
git clone https://github.com/yourusername/INSciphers.git
cd INSciphers/rsa
```

## How to Run
Run the Python script using:
```bash
python rsa.py
```

## Example Usage
### Sample Input & Output
```plaintext
Enter the value of p: 61
Enter the value of q: 53
Enter a message: 42
Encrypted message: 279
Decrypted message: 42
```

## How It Works
1. **Key Generation**:
   - Two prime numbers `p` and `q` are taken as input.
   - The modulus `n` is computed as `n = p * q`.
   - The totient function `phi = (p-1) * (q-1)` is calculated.
   - A public exponent `e` is chosen such that `gcd(e, phi) = 1`.
   - The private exponent `d` is computed such that `(d * e) % phi = 1`.

2. **Encryption**:
   - The message is encrypted using the formula `c = (msg^e) % n`.

3. **Decryption**:
   - The encrypted message is decrypted using the formula `d = (c^d) % n`.

## Limitations
- The implementation assumes `p` and `q` are valid prime numbers.
- The key generation process is simplified and does not check for strong cryptographic security.
- Only numeric messages are supported in this version.

This implementation provides a basic introduction to RSA encryption, but for secure cryptographic applications, a more robust key generation and encryption method should be used.

