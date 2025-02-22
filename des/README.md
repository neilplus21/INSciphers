# DES Key Generation Implementation in Python

This directory contains an implementation of **DES Key Generation** in Python. The script generates multiple 8-bit keys using a Feistel-inspired approach.

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
- Binary conversion of input text.
- Feistel-inspired transformations to generate DES-like keys.
- Randomized bit selection to improve key variability.

## Tech Stack
- **Programming Language**: Python

## Setup and Installation
### Prerequisites
Ensure Python 3.6+ is installed on your system.

### Clone the Repository
```bash
git clone https://github.com/yourusername/INSciphers.git
cd INSciphers/des
```

## How to Run
Run the Python script using:
```bash
python des_key.py
```

## Example Usage
### Sample Input & Output
```plaintext
Enter a string: test
Key 1 = 10101010
Key 2 = 11001100
...
Key 8 = 01100110
```

## How It Works
1. **Convert Input to Binary**: Each character is converted to an 8-bit binary representation.
2. **Bit Filtering**: Only certain bits are selected for processing.
3. **Bitwise Transformations**: Left and right halves are shifted and transformed using predefined values.
4. **Randomized Bit Selection**: Ensures key variability.
5. **Final Key Generation**: Eight 8-bit keys are generated for use in DES.

## Limitations
- This implementation only generates keys, it does not perform full DES encryption.
- Basic transformation rules are applied without full DES key scheduling.


