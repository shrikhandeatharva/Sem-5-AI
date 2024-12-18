def prepare_text(text):
    text = ''.join(filter(str.isalpha, text.upper()))
    text = text.replace('J', 'I')
    if len(text) % 2 != 0:
        text += 'X'    
    return text

def create_matrix(key):
    key = ''.join(dict.fromkeys(prepare_text(key) + 'ABCDEFGHIKLMNOPQRSTUVWXYZ'))
    matrix = [list(key[i:i+5]) for i in range(0, 25, 5)]
    return matrix

def find_position(matrix, letter):
    for i, row in enumerate(matrix):
        if letter in row:
            return i, row.index(letter)

def encrypt(plaintext, key):
    matrix = create_matrix(key)
    plaintext = prepare_text(plaintext)
    ciphertext = ''
    for i in range(0, len(plaintext), 2):
        row1, col1 = find_position(matrix, plaintext[i])
        row2, col2 = find_position(matrix, plaintext[i+1])
        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]
    return ciphertext

def decrypt(ciphertext, key):
    matrix = create_matrix(key)
    plaintext = ''
    for i in range(0, len(ciphertext), 2):
        row1, col1 = find_position(matrix, ciphertext[i])
        row2, col2 = find_position(matrix, ciphertext[i+1])
        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2] + matrix[row2][col1]
    return plaintext

# Get user input
key = input("Enter the key: ")
plaintext = input("Enter the plaintext: ")

# Encrypt the plaintext
ciphertext = encrypt(plaintext, key)

# Decrypt the ciphertext
decrypted_text = decrypt(ciphertext, key)

# Print the results
print(f"Plaintext: {plaintext.upper()}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted text: {decrypted_text}")


# CORRECTED CODE
# def prepare_text(text):
#     text = ''.join(filter(str.isalpha, text.upper()))
#     text = text.replace('J', 'I')

#     prepared_text = ''
#     i = 0
#     while i < len(text):
#         prepared_text += text[i]
#         if i + 1 < len(text):
#             if text[i] == text[i + 1]:
#                 if text[i] == 'X':
#                     prepared_text += 'Q'  # Arbitrary letter other than 'X'
#                 else:
#                     prepared_text += 'X'
#         i += 1

#     # Ensure the length is even by adding 'X' if necessary
#     if len(prepared_text) % 2 != 0:
#         prepared_text += 'X'
        
#     return prepared_text

# def create_matrix(key):
#     key = ''.join(dict.fromkeys(prepare_text(key) + 'ABCDEFGHIKLMNOPQRSTUVWXYZ'))
#     matrix = [list(key[i:i+5]) for i in range(0, 25, 5)]
#     return matrix

# def find_position(matrix, letter):
#     for row_index, row in enumerate(matrix):
#         if letter in row:
#             col_index = row.index(letter)
#             return row_index, col_index

# def encrypt(plaintext, key):
#     matrix = create_matrix(key)
#     plaintext = prepare_text(plaintext)
#     ciphertext = ''
#     for i in range(0, len(plaintext), 2):
#         row1, col1 = find_position(matrix, plaintext[i])
#         row2, col2 = find_position(matrix, plaintext[i+1])
#         if row1 == row2:
#             ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
#         elif col1 == col2:
#             ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
#         else:
#             ciphertext += matrix[row1][col2] + matrix[row2][col1]
#     return ciphertext

# def decrypt(ciphertext, key):
#     matrix = create_matrix(key)
#     plaintext = ''
#     for i in range(0, len(ciphertext), 2):
#         row1, col1 = find_position(matrix, ciphertext[i])
#         row2, col2 = find_position(matrix, ciphertext[i+1])
#         if row1 == row2:
#             plaintext += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
#         elif col1 == col2:
#             plaintext += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
#         else:
#             plaintext += matrix[row1][col2] + matrix[row2][col1]
#     return plaintext

# def clean_decrypted_text(decrypted_text):
#     cleaned_text = ''
#     i = 0
#     while i < len(decrypted_text):
#         if i + 1 < len(decrypted_text) and decrypted_text[i] == 'X' and decrypted_text[i + 1] != ' ':
#             i += 1
#         else:
#             cleaned_text += decrypted_text[i]
#             i += 1

#     # Remove padding 'X' if present at the end
#     if cleaned_text.endswith('X'):
#         cleaned_text = cleaned_text[:-1]

#     return cleaned_text

# # Get user input
# key = input("Enter the key: ")
# plaintext = input("Enter the plaintext: ")

# # Encrypt the plaintext
# ciphertext = encrypt(plaintext, key)

# # Decrypt the ciphertext
# decrypted_text = decrypt(ciphertext, key)

# # Clean the decrypted text to remove padding and inserted 'X's
# cleaned_text = clean_decrypted_text(decrypted_text)

# # Print the results
# print(f"Plaintext: {plaintext.upper()}")
# print(f"Ciphertext: {ciphertext}")
# print(f"Decrypted text: {cleaned_text}")
