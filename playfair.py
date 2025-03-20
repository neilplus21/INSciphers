def create_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = [[0, 0, 0, 0, 0] for _ in range(5)]
    mapper = {}
    keys = []
    
    i = 0
    j = 0
    for ch in key:
        if ch not in keys:
            matrix[i][j] = ch
            mapper[ch] = (i, j)
            keys.append(ch)
            j += 1
            if j == 5:
                j = 0
                i += 1
                if i == 5:
                    break

    ascii_val = 65
    while i < 5:
        while j < 5:
            ch = chr(ascii_val)
            if ch not in keys and ch != "J":
                matrix[i][j] = ch
                mapper[ch] = (i, j)
                keys.append(ch)
            j += 1
            if j == 5:
                j = 0
                i += 1
                if i == 5:
                    break
        ascii_val += 1

    return matrix, mapper

def format_plaintext(text):
    text = text.upper().replace("J", "I")
    new_text = ""
    i = 0
    while i < len(text):
        new_text += text[i]
        if i + 1 < len(text) and text[i] == text[i + 1]:
            new_text += "X"
        if i + 1 < len(text):
            new_text += text[i + 1]
        i += 2
    if len(new_text) % 2 != 0:
        new_text += "X"
    return new_text

def playfair_cipher(text, mapper, matrix, encrypt=True):
    result = ""
    shift = 1 if encrypt else -1

    i = 0
    while i < len(text):
        char1 = text[i]
        char2 = text[i + 1]
        row1, col1 = mapper[char1]
        row2, col2 = mapper[char2]

        if row1 == row2:
            result += matrix[row1][(col1 + shift) % 5]
            result += matrix[row2][(col2 + shift) % 5]
        elif col1 == col2:
            result += matrix[(row1 + shift) % 5][col1]
            result += matrix[(row2 + shift) % 5][col2]
        else:
            result += matrix[row1][col2]
            result += matrix[row2][col1]
        i += 2

    return result

key = input("Enter a key: ")
matrix, mapper = create_matrix(key)

print("Key Matrix:")
for row in matrix:
    print(row)

plaintext = input("Enter a plaintext: ")
formatted_text = format_plaintext(plaintext)
ciphertext = playfair_cipher(formatted_text, mapper, matrix, True)
decrypted_text = playfair_cipher(ciphertext, mapper, matrix, False)

print("Modified Plaintext:", formatted_text)
print("Ciphertext:", ciphertext)
print("Decrypted Text:", decrypted_text)
