from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.mistral_service import MistralService
from app.extensions import mongo
from typing import List, Dict, Any

rag_bp = Blueprint("rag", __name__)
mistral_service = MistralService()

def retrieve_relevant_data(user_id: str, query: str, data_type: str) -> List[Dict[str, Any]]:
    if data_type == "idea":
        cursor = mongo.db.ideas.find({
            "user_id": user_id,
            "idea": {"$regex": query, "$options": "i"}
        })  
        return list(cursor)
    elif data_type == "password":
        cursor = mongo.db.passwords.find({
            "user_id": user_id,
            "service": {"$regex": query, "$options": "i"}
        })
        return list(cursor)
    return []

@rag_bp.route("/query", methods=["POST"])
@jwt_required()
def rag_query():
    user_id = get_jwt_identity()
    data = request.json
    query = data.get("query")
    data_type = data.get("type")

    if not query or not data_type:
        return jsonify({"error": "Query and data type are required"}), 400

    try:
        retrieved_data = retrieve_relevant_data(user_id, query, data_type)
        if not retrieved_data:
            return jsonify({"message": f"No relevant {data_type}s found"}), 404

        response = mistral_service.generate_response(query, retrieved_data)
        return jsonify({
            "response": response,
            "retrieved_data": retrieved_data
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500