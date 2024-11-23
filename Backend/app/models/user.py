from datetime import datetime
from typing import Dict, Any

class User:
    def __init__(self, name: str, email: str, phone: str = None):
        self.name = name
        self.email = email
        self.phone = phone

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "created_at": datetime.utcnow()
        }