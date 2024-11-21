from cryptography.fernet import Fernet
import bcrypt

# Generate and store this key securely for production
AES_SECRET_KEY = Fernet.generate_key()
cipher = Fernet(AES_SECRET_KEY)

# Hashing Functions
def hash_password(password):
    """Hash a password using bcrypt."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def verify_password(hashed_password, plain_password):
    """Verify a password against its hash."""
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)

# Encryption Functions
def encrypt_password(password):
    """Encrypt a password using AES."""
    return cipher.encrypt(password.encode('utf-8'))

def decrypt_password(encrypted_password):
    """Decrypt an encrypted password."""
    return cipher.decrypt(encrypted_password).decode('utf-8')
