# import random

# # Function to perform Diffie-Hellman Key Exchange
# def diffie_hellman_key_exchange(p, g):
#     # Alice's private key (a)
#     a = random.randint(1, p-1)
#     # Alice's public key (g^a mod p)
#     A = pow(g, a, p)
    
#     # Bob's private key (b)
#     b = random.randint(1, p-1)
#     # Bob's public key (g^b mod p)
#     B = pow(g, b, p)
    
#     # Alice computes shared secret key (B^a mod p)
#     shared_key_alice = pow(B, a, p)
    
#     # Bob computes shared secret key (A^b mod p)
#     shared_key_bob = pow(A, b, p)
    
#     # The shared keys should be the same
#     assert shared_key_alice == shared_key_bob, "Shared keys do not match!"
    
#     return shared_key_alice

# if __name__ == "__main__":
#     # Prime number (p) and generator (g) agreed upon by both parties
#     p = 23  # Prime number
#     g = 5   # Primitive root modulo p
    
#     # Perform Diffie-Hellman Key Exchange
#     shared_key = diffie_hellman_key_exchange(p, g)
    
#     print(f"Shared symmetric key: {shared_key}")



# Diffie-Hellman Code

# Power function to return value of a^b mod P
def power(a, b, p):
    if b == 1:
        return a
    else:
        return pow(a, b) % p

# Main function
def main():
    # Both persons agree upon the public keys G and P
    # A prime number P is taken
    P = 23
    print("The value of P:", P)

    # A primitive root for P, G is taken
    G = 9
    print("The value of G:", G)

    # Alice chooses the private key a
    # a is the chosen private key
    a = 4
    print("The private key a for Alice:", a)

    # Gets the generated key
    x = power(G, a, P)

    # Bob chooses the private key b
    # b is the chosen private key
    b = 3
    print("The private key b for Bob:", b)

    # Gets the generated key
    y = power(G, b, P)

    # Generating the secret key after the exchange of keys
    ka = power(y, a, P)  # Secret key for Alice
    kb = power(x, b, P)  # Secret key for Bob

    print("Secret key for Alice is:", ka)
    print("Secret key for Bob is:", kb)

if __name__ == "__main__":
    main()
