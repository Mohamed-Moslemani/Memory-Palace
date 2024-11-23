from typing import Dict, List, Optional, Tuple
from datetime import datetime
from bson import ObjectId
from app.extensions import mongo
from app.utils.security import PasswordEncryption

class PasswordService:
    def __init__(self):
        self.password_encryption = PasswordEncryption()
        
    def save_password(
        self,
        user_id: str,
        service: str,
        password: str,
        url: Optional[str] = None,
        notes: Optional[str] = None
    ) -> Tuple[bool, str]:
        """
        Save an encrypted password for a service.
        """
        try:
            # Check if password already exists for this service
            existing = mongo.db.passwords.find_one({
                "user_id": user_id,
                "service": service
            })
            
            if existing:
                # Update existing password
                mongo.db.passwords.update_one(
                    {"_id": existing["_id"]},
                    {
                        "$set": {
                            "password_encrypted": self.password_encryption.encrypt(password),
                            "url": url,
                            "notes": notes,
                            "updated_at": datetime.utcnow()
                        }
                    }
                )
                return True, "Password updated successfully"
            
            # Create new password entry
            password_doc = {
                "user_id": user_id,
                "service": service,
                "password_encrypted": self.password_encryption.encrypt(password),
                "url": url,
                "notes": notes,
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            }
            
            mongo.db.passwords.insert_one(password_doc)
            return True, "Password saved successfully"
            
        except Exception as e:
            return False, f"Error saving password: {str(e)}"

    def retrieve_password(
        self,
        user_id: str,
        service: str
    ) -> Tuple[bool, Dict]:
        """
        Retrieve and decrypt a password for a service.
        """
        try:
            password_doc = mongo.db.passwords.find_one({
                "user_id": user_id,
                "service": service
            })
            
            if not password_doc:
                return False, {"error": f"No password found for service: {service}"}
                
            decrypted_password = self.password_encryption.decrypt(
                password_doc["password_encrypted"]
            )
            
            return True, {
                "service": service,
                "password": decrypted_password,
                "url": password_doc.get("url"),
                "notes": password_doc.get("notes"),
                "created_at": password_doc["created_at"],
                "updated_at": password_doc["updated_at"]
            }
            
        except Exception as e:
            return False, {"error": f"Error retrieving password: {str(e)}"}

    def list_services(self, user_id: str) -> List[Dict]:
        """
        List all services for which passwords are stored.
        """
        try:
            cursor = mongo.db.passwords.find(
                {"user_id": user_id},
                {"service": 1, "url": 1, "created_at": 1, "updated_at": 1}
            )
            return list(cursor)
        except Exception:
            return []

    def delete_password(
        self,
        user_id: str,
        service: str
    ) -> Tuple[bool, str]:
        """
        Delete a stored password for a service.
        """
        try:
            result = mongo.db.passwords.delete_one({
                "user_id": user_id,
                "service": service
            })
            
            if result.deleted_count > 0:
                return True, "Password deleted successfully"
            return False, "Password not found"
            
        except Exception as e:
            return False, f"Error deleting password: {str(e)}"

    def update_service_details(
        self,
        user_id: str,
        service: str,
        new_service: Optional[str] = None,
        url: Optional[str] = None,
        notes: Optional[str] = None
    ) -> Tuple[bool, str]:
        """
        Update service details without changing the password.
        """
        try:
            update_fields = {}
            if new_service:
                update_fields["service"] = new_service
            if url is not None:
                update_fields["url"] = url
            if notes is not None:
                update_fields["notes"] = notes
                
            if not update_fields:
                return False, "No updates provided"
                
            update_fields["updated_at"] = datetime.utcnow()
            
            result = mongo.db.passwords.update_one(
                {"user_id": user_id, "service": service},
                {"$set": update_fields}
            )
            
            if result.modified_count > 0:
                return True, "Service details updated successfully"
            return False, "Service not found"
            
        except Exception as e:
            return False, f"Error updating service details: {str(e)}"

# routes/password_routes.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.password_service import PasswordService

password_bp = Blueprint("password", __name__)
password_service = PasswordService()

@password_bp.route("/save", methods=["POST"])
@jwt_required()
def save_password():
    user_id = get_jwt_identity()
    data = request.json
    
    if not data.get("service") or not data.get("password"):
        return jsonify({"error": "Service and password are required"}), 400
        
    success, message = password_service.save_password(
        user_id=user_id,
        service=data["service"],
        password=data["password"],
        url=data.get("url"),
        notes=data.get("notes")
    )
    
    return jsonify({"message": message}), 200 if success else 400

@password_bp.route("/retrieve", methods=["POST"])
@jwt_required()
def retrieve_password():
    user_id = get_jwt_identity()
    service = request.json.get("service")
    
    if not service:
        return jsonify({"error": "Service name is required"}), 400
        
    success, result = password_service.retrieve_password(user_id, service)
    if success:
        return jsonify(result), 200
    return jsonify(result), 404

@password_bp.route("/list", methods=["GET"])
@jwt_required()
def list_services():
    user_id = get_jwt_identity()
    services = password_service.list_services(user_id)
    return jsonify({"services": services}), 200

@password_bp.route("/delete", methods=["DELETE"])
@jwt_required()
def delete_password():
    user_id = get_jwt_identity()
    service = request.json.get("service")
    
    if not service:
        return jsonify({"error": "Service name is required"}), 400
        
    success, message = password_service.delete_password(user_id, service)
    return jsonify({"message": message}), 200 if success else 404

@password_bp.route("/update", methods=["PUT"])
@jwt_required()
def update_service():
    user_id = get_jwt_identity()
    data = request.json
    
    if not data.get("service"):
        return jsonify({"error": "Service name is required"}), 400
        
    success, message = password_service.update_service_details(
        user_id=user_id,
        service=data["service"],
        new_service=data.get("new_service"),
        url=data.get("url"),
        notes=data.get("notes")
    )
    
    return jsonify({"message": message}), 200 if success else 400