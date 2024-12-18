from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

# Function to encrypt data
def encrypt_aes(key, plaintext):
    # Padding the plaintext to be AES block size compatible
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()

    # Generate a random initialization vector (IV)
    iv = os.urandom(16)

    # Creating a cipher object using AES algorithm and CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Encrypting the padded plaintext
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

    return iv + ciphertext  # IV is prepended to the ciphertext for decryption

# Function to decrypt data
def decrypt_aes(key, ciphertext):
    # Extract the IV from the beginning of the ciphertext
    iv = ciphertext[:16]
    actual_ciphertext = ciphertext[16:]

    # Creating a cipher object using AES algorithm and CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Decrypting the ciphertext
    padded_plaintext = decryptor.update(actual_ciphertext) + decryptor.finalize()

    # Unpadding the plaintext to retrieve original data
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    return plaintext

# Example usage
if __name__ == "__main__":
    # Take manual input of the plaintext
    plaintext_input = input("Enter the plaintext to encrypt: ")

    # Convert the plaintext to bytes
    plaintext = plaintext_input.encode()

    # 256-bit key (32 bytes)
    key = os.urandom(32)

    print(f"Original Plaintext: {plaintext_input}")

    # Encrypt the plaintext
    encrypted = encrypt_aes(key, plaintext)
    print(f"Encrypted: {encrypted}")

    # Decrypt the ciphertext
    decrypted = decrypt_aes(key, encrypted)
    print(f"Decrypted: {decrypted.decode()}")
