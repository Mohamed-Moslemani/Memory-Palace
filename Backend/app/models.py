from bson import ObjectId
from datetime import datetime
def create_user_document(name, email, phone, hashed_password):
    return {
        "_id": str(ObjectId()),  # Generate a unique ID
        "name": name,
        "email": email,
        "phone": phone,
        "password": hashed_password,
        "created_at": datetime.utcnow(),  # Timestamp for tracking
    }
