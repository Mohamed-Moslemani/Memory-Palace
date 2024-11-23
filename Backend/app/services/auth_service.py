from app.extensions import mongo
from app.utils.security import hash_password, verify_password, PasswordEncryption
from app.models.user import User
from typing import Optional, Tuple, Dict, Any
from bson import ObjectId

class AuthService:
    def __init__(self):
        self.password_encryption = PasswordEncryption()

    def create_user(self, user_data: Dict[str, str]) -> Tuple[bool, str]:
        try:
            # Validate user data
            if not all(key in user_data for key in ["name", "email", "password"]):
                return False, "Missing required fields"

            # Check if user exists
            if mongo.db.users.find_one({"email": user_data["email"]}):
                return False, "Email already exists"

            # Create user object
            user = User(
                name=user_data["name"],
                email=user_data["email"],
                phone=user_data.get("phone")
            )

            # Add password fields
            user_dict = user.to_dict()
            user_dict["password_hashed"] = hash_password(user_data["password"])
            user_dict["password_encrypted"] = self.password_encryption.encrypt(user_data["password"])

            # Insert user
            mongo.db.users.insert_one(user_dict)
            return True, "User created successfully"

        except Exception as e:
            return False, str(e)

    def authenticate_user(self, email: str, password: str) -> Optional[Dict[str, Any]]:
        user = mongo.db.users.find_one({"email": email})
        if user and verify_password(user["password_hashed"], password):
            return user
        return None

    def get_user_by_id(self, user_id: str) -> Optional[Dict[str, Any]]:
        return mongo.db.users.find_one({"_id": ObjectId(user_id)})
