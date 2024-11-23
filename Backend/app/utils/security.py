from cryptography.fernet import Fernet
from app.extensions import bcrypt
import os

def hash_password(password: str) -> str:
    return bcrypt.generate_password_hash(password).decode('utf-8')

def verify_password(hashed_password: str, password: str) -> bool:
    return bcrypt.check_password_hash(hashed_password, password)

class PasswordEncryption:
    def __init__(self):
        self.key = os.getenv("ENCRYPTION_KEY").encode()
        self.cipher_suite = Fernet(self.key)

    def encrypt(self, password: str) -> str:
        return self.cipher_suite.encrypt(password.encode()).decode()

    def decrypt(self, encrypted_password: str) -> str:
        return self.cipher_suite.decrypt(encrypted_password.encode()).decode()