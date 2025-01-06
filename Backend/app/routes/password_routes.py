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
        password=data["password"]
    )
    
    if success:
        return jsonify({"message": message}), 201
    return jsonify({"error": message}), 400



@password_bp.route("/retrieve", methods=["POST"])
@jwt_required()
def retrieve_password():
    user_id = get_jwt_identity()
    service = request.json.get("service")
    
    if not service:
        return jsonify({"error": "Service name is required"}), 400
    
    try:
        password_data = password_service.get_password(user_id, service)
        if not password_data:
            return jsonify({"error": "Password not found"}), 404
        return jsonify(password_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@password_bp.route("/services", methods=["GET"])
@jwt_required()
def list_services():
    user_id = get_jwt_identity()
    try:
        services = password_service.get_all_services(user_id)
        return jsonify({"services": services}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@password_bp.route("/delete", methods=["DELETE"])
@jwt_required()
def delete_password():
    user_id = get_jwt_identity()
    service = request.json.get("service")
    
    if not service:
        return jsonify({"error": "Service name is required"}), 400
    
    success, message = password_service.delete_password(user_id, service)
    if success:
        return jsonify({"message": message}), 200
    return jsonify({"error": message}), 404



@password_bp.route("/search", methods=["GET"])
@jwt_required()
def search_services():
    user_id = get_jwt_identity()
    query = request.args.get("q", "")
    
    try:
        services = password_service.search_services(user_id, query)
        return jsonify({"services": services}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500