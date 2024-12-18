# import numpy as np
# from sympy import Matrix

# def hill_cipher_encrypt(plaintext, key):

#     plaintext_numbers = [ord(char) - ord('A') for char in plaintext.upper()]
#     key_matrix = np.array(key)

#     n = key_matrix.shape[0]
#     if len(plaintext_numbers) % n != 0:

#         while len(plaintext_numbers) % n != 0:
#             plaintext_numbers.append(ord('X') - ord('A'))
    
#     plaintext_vectors = [plaintext_numbers[i:i+n] for i in range(0, len(plaintext_numbers), n)]

#     encrypted_vectors = []
#     for vector in plaintext_vectors:
#         encrypted_vector = np.dot(key_matrix, vector) % 26
#         encrypted_vectors.extend(encrypted_vector)
    
#     ciphertext = ''.join(chr(num + ord('A')) for num in encrypted_vectors)
#     return ciphertext

# def hill_cipher_decrypt(ciphertext, key):
#     ciphertext_numbers = [ord(char) - ord('A') for char in ciphertext.upper()]
#     key_matrix = np.array(key)
#     key_matrix_modinv = np.array(Matrix(key_matrix).inv_mod(26))
#     n = key_matrix.shape[0]

#     ciphertext_vectors = [ciphertext_numbers[i:i+n] for i in range(0, len(ciphertext_numbers), n)]

#     decrypted_vectors = []
#     for vector in ciphertext_vectors:
#         decrypted_vector = np.dot(key_matrix_modinv, vector) % 26
#         decrypted_vectors.extend(decrypted_vector)

#     plaintext = ''.join(chr(int(num) + ord('A')) for num in decrypted_vectors)
#     return plaintext

# key = [[6, 24, 1], [13, 16, 10], [20, 17, 15]]
# plaintext = "HELLO"
# ciphertext = hill_cipher_encrypt(plaintext, key)
# print(f"Encrypted Text: {ciphertext}")

# decrypted_text = hill_cipher_decrypt(ciphertext, key)
# print(f"Decrypted Text: {decrypted_text}")


import numpy as np
import sympy as sp

def encrypt(plaintext, key, length):
    pt = plaintext.replace(" ", "").upper()
    print("Plaintext:", pt)
    pt_num = []
    
    for letter in pt:
        pt_num.append(ord(letter) - ord('A'))
        
    if len(pt_num) % length != 0:
        while len(pt_num) % length != 0:
            pt_num.append(ord('X') - ord('A'))

    matrices = [np.array(pt_num[i:i+length]).reshape(1, length) for i in range(0, len(pt_num), length)]

    encrypted_matrices = []
    for matrix in matrices:
        encrypted_matrix = np.dot(matrix, key) % 26  # Use matrix multiplication and mod 26
        encrypted_matrices.append(encrypted_matrix)
    
    # Convert encrypted matrices back to text
    ciphertext = ""
    for matrix in encrypted_matrices:
        for num in matrix.flatten():  # Flatten matrix to 1D
            ciphertext += chr(int(num) + ord('A'))
    
    return ciphertext

def decrypt(ciphertext, key, length):
    ct_num = []
    
    for letter in ciphertext:
        ct_num.append(ord(letter) - ord('A'))
        
    matrices = [np.array(ct_num[i:i+length]).reshape(1, length) for i in range(0, len(ct_num), length)]
    
    # Calculate the inverse of the key matrix in modulo 26
    key_inv = sp.Matrix(key).inv_mod(26)

    decrypted_matrices = []
    for matrix in matrices:
        decrypted_matrix = np.dot(matrix, key_inv) % 26  # Use matrix multiplication with the inverse key and mod 26
        decrypted_matrices.append(decrypted_matrix)
    
    # Convert decrypted matrices back to text
    plaintext = ""
    for matrix in decrypted_matrices:
        for num in matrix.flatten():  # Flatten matrix to 1D
            plaintext += chr(int(num) + ord('A'))
    
    return plaintext

plaintext = "Attack on Titan"
key = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])  # Convert key to numpy array
length = len(key)
ciphertext = encrypt(plaintext, key, length)
print("Encrypted Text:", ciphertext)

decrypted_text = decrypt(ciphertext, key, length)
print("Decrypted Text:", decrypted_text)
