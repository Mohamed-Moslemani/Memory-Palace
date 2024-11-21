from app.utils import hash_password, verify_password, encrypt_password, decrypt_password
import sys
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_hashing():
    print("Testing Hashing...")
    original_password = "my_secure_password"
    hashed_password = hash_password(original_password)
    
    assert verify_password(hashed_password, original_password), "Password verification failed!"
    print("Hashing Test Passed ✅\n")

def test_encryption():
    print("Testing Encryption...")
    original_password = "my_secure_password"
    encrypted_password = encrypt_password(original_password)
    decrypted_password = decrypt_password(encrypted_password)
    
    assert original_password == decrypted_password, "Decryption failed!"
    print("Encryption Test Passed ✅\n")

if __name__ == "__main__":
    test_hashing()
    test_encryption()
