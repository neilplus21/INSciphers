# Feistel Cipher Implementation in Python

This repository contains a simple implementation of the **Feistel Cipher** in Python. The Feistel Cipher is a symmetric encryption structure used in various cryptographic algorithms, including DES.

## Table of Contents
- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Setup and Installation](#setup-and-installation)
- [How to Run](#how-to-run)
- [Example Usage](#example-usage)
- [How It Works](#how-it-works)
- [Limitations](#limitations)

## Overview
This implementation demonstrates:
- A **2-round Feistel Cipher** using binary addition and XOR operations.
- Encryption of a given plaintext.
- Basic key-based transformations.
- Binary string processing for encryption.

## Tech Stack
- **Programming Language**: Python

## Setup and Installation
### Prerequisites
Ensure you have Python installed (version 3.6 or later).

### Clone the Repository
```bash
git clone https://github.com/yourusername/INSciphers.git
cd INSciphers/fiestal
```

## How to Run
Run the Python script using:
```bash
python fiestal.py
```

## Example Usage
### Sample Input & Output
```plaintext
Enter a string: hello
Enter a key: key123
Ciphertext: 110010101011010010011...
```

## How It Works
1. **Convert Input to Binary**: Each character of the plaintext and key is converted to an 8-bit binary format.
2. **Split the Binary String**: The plaintext is divided into two halves: Left and Right.
3. **Round 1**:
   - Add the key to the Right half.
   - XOR the result with the Left half.
   - Swap halves.
4. **Round 2**:
   - Repeat the process with the swapped halves.
   - Concatenate the final halves to produce the ciphertext.
5. **Final Padding Handling**: If necessary, leading zeros are added to maintain length consistency.

## Limitations
- This implementation does not handle decryption.
- Binary addition may result in length mismatches if not properly padded.
- Only a basic 2-round structure is implemented.

