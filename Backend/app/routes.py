from flask import Blueprint, request, jsonify
from app import mongo, bcrypt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.utils import hash_password, encrypt_password
from app.utils import verify_password

auth = Blueprint("auth", __name__)
from datetime import datetime
from app.models import create_user_document

@auth.route("/signup", methods=["POST"])
def signup():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")
    password = data.get("password")
    confirm_password = data.get("confirm_password")

    if not name or not email or not password or not confirm_password:
        return jsonify({"error": "All required fields must be filled"}), 400
    if password != confirm_password:
        return jsonify({"error": "Passwords do not match"}), 400

    # Hash and encrypt the password
    hashed_password = hash_password(password)
    encrypted_password = encrypt_password(password)

    # Check if email already exists
    if mongo.db.users.find_one({"email": email}):
        return jsonify({"error": "Email already exists"}), 400

    # Create user document
    user_document = {
        "name": name,
        "email": email,
        "phone": phone,
        "password_hashed": hashed_password,
        "password_encrypted": encrypted_password,
        "created_at": datetime.utcnow(),
    }

    mongo.db.users.insert_one(user_document)
    return jsonify({"message": "Signup successful"}), 201

@auth.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    user = mongo.db.users.find_one({"email": email})
    if not user or not bcrypt.check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid email or password"}), 401
    access_token = create_access_token(identity=str(user["_id"]))
    return jsonify({"message": "Login successful", "access_token": access_token}), 200

@auth.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    user_id = get_jwt_identity()  
    user = mongo.db.users.find_one({"_id": user_id})
    return jsonify({"message": f"Welcome, {user['name']}!"}), 200

@auth.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    user = mongo.db.users.find_one({"email": email})
    if not user:
        return jsonify({"error": "Invalid email or password"}), 401
    hashed_password = user["password_hashed"]
    if not verify_password(hashed_password, password):
        return jsonify({"error": "Invalid email or password"}), 401

    access_token = create_access_token(identity=str(user["_id"]))
    return jsonify({"message": "Login successful", "access_token": access_token}), 200