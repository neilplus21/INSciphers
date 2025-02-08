def text_to_numbers(text):
    return [ord(char) - ord('A') for char in text]

def numbers_to_text(numbers):
    return ''.join(chr(num + ord('A')) for num in numbers)

def matrix_multiply(matrix, text_matrix):
    result = []
    for row in matrix:
        value = (row[0] * text_matrix[0] + row[1] * text_matrix[1]) % 26
        result.append(value)
    return result

def hill_encrypt(plaintext, key_matrix):
    if len(plaintext) % 2 != 0:
        plaintext += 'X'
    
    print("\nPlaintext:", plaintext)
    
    plaintext_numbers = text_to_numbers(plaintext)
    print("\nPlaintext Matrix (M):")
    for i in range(0, len(plaintext_numbers), 2):
        print(plaintext_numbers[i:i+2])

    ciphertext_numbers = []
    for i in range(0, len(plaintext_numbers), 2):
        ciphertext_numbers.extend(matrix_multiply(key_matrix, plaintext_numbers[i:i+2]))

    print("\nCiphertext Matrix (N):")
    for i in range(0, len(ciphertext_numbers), 2):
        print(ciphertext_numbers[i:i+2])
    
    return numbers_to_text(ciphertext_numbers)

def matrix_inverse(matrix):
    det = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % 26
    det_inv = pow(det, -1, 26)

    inv_matrix = [
        [(matrix[1][1] * det_inv) % 26, (-matrix[0][1] * det_inv) % 26],
        [(-matrix[1][0] * det_inv) % 26, (matrix[0][0] * det_inv) % 26]
    ]
    return inv_matrix

def hill_decrypt(ciphertext, key_matrix):
    print("\nCiphertext:", ciphertext)

    ciphertext_numbers = text_to_numbers(ciphertext)
    print("\nCiphertext Matrix (N):")
    for i in range(0, len(ciphertext_numbers), 2):
        print(ciphertext_numbers[i:i+2])

    inverse_matrix = matrix_inverse(key_matrix)

    plaintext_numbers = []
    for i in range(0, len(ciphertext_numbers), 2):
        plaintext_numbers.extend(matrix_multiply(inverse_matrix, ciphertext_numbers[i:i+2]))

    print("\nDecrypted Matrix (M'):")
    for i in range(0, len(plaintext_numbers), 2):
        print(plaintext_numbers[i:i+2])

    return numbers_to_text(plaintext_numbers)

key_matrix = [[3, 3], [2, 5]]
plaintext = "HELLOCHINGCHONG"

ciphertext = hill_encrypt(plaintext, key_matrix)
print("\nEncrypted Text:", ciphertext)

decrypted_text = hill_decrypt(ciphertext, key_matrix)
print("\nDecrypted Text:", decrypted_text)
