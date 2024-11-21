from cryptography.fernet import Fernet

# Generate a new AES key
new_aes_key = Fernet.generate_key()
print(f"{new_aes_key.decode()}")