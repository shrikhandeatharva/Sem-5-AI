from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad

# Function to encrypt the data using Blowfish algorithm
def blowfish_encrypt(key, plaintext):
    # Create a Blowfish cipher object
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    
    # Pad the plaintext to ensure it's a multiple of the block size
    padded_text = pad(plaintext.encode(), Blowfish.block_size)
    
    # Encrypt the padded text
    ciphertext = cipher.encrypt(padded_text)
    
    return ciphertext

# Function to decrypt the data using Blowfish algorithm
def blowfish_decrypt(key, ciphertext):
    # Create a Blowfish cipher object
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    
    # Decrypt the ciphertext
    decrypted_data = cipher.decrypt(ciphertext)
    
    # Unpad the decrypted data to get the original plaintext
    plaintext = unpad(decrypted_data, Blowfish.block_size).decode()
    
    return plaintext

# Example usage
if __name__ == "__main__":
    # Take key input from user (between 4 and 56 bytes long)
    key = input("Enter the secret key (4-56 characters): ").encode()

    # Ensure the key is between 4 and 56 bytes
    while len(key) < 4 or len(key) > 56:
        print("Key must be between 4 and 56 characters.")
        key = input("Enter a valid secret key (4-56 characters): ").encode()

    # Take plaintext input from the user
    plaintext = input("Enter the plaintext to encrypt: ")
    
    # Encrypt the plaintext
    ciphertext = blowfish_encrypt(key, plaintext)
    print("Encrypted:", ciphertext)
    
    # Decrypt the ciphertext
    decrypted_text = blowfish_decrypt(key, ciphertext)
    print("Decrypted:", decrypted_text)
