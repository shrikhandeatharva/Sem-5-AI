# from Crypto.Cipher import DES
# from Crypto.Random import get_random_bytes
# from Crypto.Util.Padding import pad, unpad

# def generate_key():
#     return get_random_bytes(8)

# def encrypt(plaintext, key):
#     cipher = DES.new(key, DES.MODE_ECB)
#     padded_text = pad(plaintext.encode(), DES.block_size)
#     ciphertext = cipher.encrypt(padded_text)
#     return ciphertext

# def decrypt(ciphertext, key):
#     cipher = DES.new(key, DES.MODE_ECB)
#     padded_text = cipher.decrypt(ciphertext)
#     plaintext = unpad(padded_text, DES.block_size)
#     return plaintext.decode()

# # Example usage
# if __name__ == "__main__":
#     # Generate a random 8-byte key
#     key = generate_key()
    
#     # Original message
#     message = "8787878787878787"
    
#     # Encrypt the message
#     encrypted = encrypt(message, key)
#     print("Encrypted:", encrypted.hex())
    
#     # Decrypt the message
#     decrypted = decrypt(encrypted, key)
#     print("Decrypted:", decrypted)


# from Crypto.Cipher import DES
# from Crypto.Util.Padding import pad, unpad
# import binascii

# def encrypt(plaintext, key):
#     cipher = DES.new(key, DES.MODE_ECB)
#     padded_text = pad(plaintext.encode(), DES.block_size)
#     ciphertext = cipher.encrypt(padded_text)
#     return ciphertext

# def decrypt(ciphertext, key):
#     cipher = DES.new(key, DES.MODE_ECB)
#     padded_text = cipher.decrypt(ciphertext)
#     plaintext = unpad(padded_text, DES.block_size)
#     return plaintext.decode()

# # Example usage
# if __name__ == "__main__":
#     # Input the encryption key (must be exactly 8 bytes)
#     key = input("Enter the 8-byte encryption key (in hexadecimal): ")
#     key = binascii.unhexlify(key)
    
#     if len(key) != 8:
#         print("Error: Key must be exactly 8 bytes (16 hexadecimal characters)")
#         exit(1)
    
#     # Original message
#     message = input("Enter the message to encrypt: ")
    
#     # Encrypt the message
#     encrypted = encrypt(message, key)
#     print("Encrypted:", encrypted.hex())
    
#     # Decrypt the message
#     decrypted = decrypt(encrypted, key)
#     print("Decrypted:", decrypted)


from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii

def encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plaintext.encode(), DES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return ciphertext

def decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_text, DES.block_size)
    return plaintext.decode()

# Example usage
if __name__ == "__main__":
    # Input the encryption key (must be exactly 8 bytes)
    key = input("Enter the 8-byte encryption key (in hexadecimal): ")
    key = binascii.unhexlify(key)
    
    if len(key) != 8:
        print("Error: Key must be exactly 8 bytes (16 hexadecimal characters)")
        exit(1)
    
    # Original message
    message = input("Enter the message to encrypt: ")
    
    # Encrypt the message
    encrypted = encrypt(message, key)
    
    # Format the output to match the expected format
    formatted_output = ' '.join([encrypted.hex()[i:i+16].upper() for i in range(0, len(encrypted.hex()), 16)])
    print("Encrypted:", formatted_output)
    
    # Decrypt the message
    decrypted = decrypt(encrypted, key)
    print("Decrypted:", decrypted)