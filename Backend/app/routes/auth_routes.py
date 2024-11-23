from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.services.auth_service import AuthService

auth_bp = Blueprint("auth_routes", __name__)
auth_service = AuthService()

@auth_bp.route("/signup", methods=["POST"])
def signup():
    success, message = auth_service.create_user(request.json)
    return jsonify({"message": message}), 201 if success else 400

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = auth_service.authenticate_user(data.get("email"), data.get("password"))
    if not user:
        return jsonify({"error": "Invalid credentials"}), 401
    
    access_token = create_access_token(identity=str(user["_id"]))
    return jsonify({
        "message": "Login successful",
        "access_token": access_token
    }), 200
