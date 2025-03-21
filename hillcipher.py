import numpy as np

l = list(map(int, input("Enter the key matrix : ").split()))
keyMatrix = np.array(l).reshape(2,2)

det = keyMatrix[0,0] * keyMatrix[1,1] - keyMatrix[0,1] * keyMatrix[1,0]
det = pow(int(det), 1, 26)  # Compute determinant mod 26

detInverse = pow(det, -1, 26)  # Compute modular inverse of determinant

keyInverse = np.array([[keyMatrix[1,1], -keyMatrix[0,1]], [-keyMatrix[1,0], keyMatrix[0,0]]])
keyInverse = (detInverse * keyInverse) % 26

def text_to_num(text):
    return [ord(char) - ord('A') for char in text]

def num_to_text(nums):
    return "".join([chr(num + ord('A')) for num in nums])

def encrypt(plainText):
    plainText = plainText.upper()
    if len(plainText) % 2 == 1:  # If length is odd, add a padding character
        plainText += 'X'
    cipherText = ""
    for i in range(0, len(plainText), 2):
        block = np.array(text_to_num(plainText[i:i+2]))
        encryptedBlock = np.dot(keyMatrix, block)%26  # Convert result to integer
        cipherText += num_to_text(encryptedBlock)
    return cipherText

def decrypt(cipherText):
    cipherText = cipherText.upper()
    plainText = ""
    for i in range(0, len(cipherText), 2):
        block = np.array(text_to_num(cipherText[i:i+2]))
        decryptedBlock = np.dot(keyInverse, block)% 26  # Convert result to integer
        plainText += num_to_text(decryptedBlock)
    return plainText

plainText = input("Enter a message : ")
print("Encrypted : ", encrypt(plainText))
print("Decrypted : ", decrypt(encrypt(plainText)))
