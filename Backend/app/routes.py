from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.extensions import mongo, bcrypt, jwt
from app.utils import hash_password, encrypt_password, verify_password, decrypt_password
from datetime import datetime
from bson import ObjectId  
from datetime import datetime
from app.models import create_user_document
import openai
import os 
from dotenv import load_dotenv
load_dotenv()


auth = Blueprint("auth", __name__)

@auth.route("/signup", methods=["POST"])
def signup():
    try:
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

        hashed_password = hash_password(password)
        encrypted_password = encrypt_password(password)

        if mongo.db.users.find_one({"email": email}):
            return jsonify({"error": "Email already exists"}), 400

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
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@auth.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    user = mongo.db.users.find_one({"email": email})
    if not user:
        return jsonify({"error": "Invalid email or password"}), 401

    if not verify_password(user["password_hashed"], password):
        return jsonify({"error": "Invalid email or password"}), 401

    access_token = create_access_token(identity=str(user["_id"]))
    return jsonify({"message": "Login successful", "access_token": access_token}), 200


@auth.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    user_id = get_jwt_identity()  
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": f"Welcome, {user['name']}!"}), 200
@auth.route("/save-password", methods=["POST"])
@jwt_required()
def save_password():
    user_id = get_jwt_identity()
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})  # Validate user exists
    if not user:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    service = data.get("service") 
    password = data.get("password")

    if not service or not password:
        return jsonify({"error": "Service and password are required"}), 400

    encrypted_password = encrypt_password(password)
    hashed_password = hash_password(password)

    password_document = {
        "user_id": user_id,
        "service": service,
        "password_hashed": hashed_password,
        "password_encrypted": encrypted_password,
        "created_at": datetime.utcnow(),
    }

    mongo.db.passwords.insert_one(password_document)
    return jsonify({"message": "Password saved successfully"}), 201


@auth.route("/retrieve-password", methods=["POST"])
@jwt_required()
def retrieve_password():
    user_id = get_jwt_identity()  # Get the authenticated user's ID
    data = request.json
    service = data.get("service")  

    if not service:
        return jsonify({"error": "Service name is required"}), 400

    # Query the database for the user's password for the given service
    record = mongo.db.passwords.find_one({"user_id": user_id, "service": service})
    if not record:
        return jsonify({"error": f"No password found for {service}"}), 404

    # Decrypt the password
    decrypted_password = decrypt_password(record["password_encrypted"])

    # Return the decrypted password
    return jsonify({
        "service": service,
        "password": decrypted_password
    }), 200

@auth.route("/save-idea", methods=["POST"])
@jwt_required()
def save_idea():
    user_id = get_jwt_identity()
    data = request.json
    idea = data.get("idea")

    if not idea:
        return jsonify({"error": "Idea content is required"}), 400

    # Create idea document
    idea_document = {
        "user_id": user_id,
        "idea": idea,
        "created_at": datetime.utcnow(),
    }

    # Save idea in the database
    mongo.db.ideas.insert_one(idea_document)
    return jsonify({"message": "Idea saved successfully"}), 201

@auth.route("/retrieve-ideas", methods=["GET"])
@jwt_required()
def retrieve_ideas():
    user_id = get_jwt_identity()

    # Query the database for all ideas by this user
    ideas = mongo.db.ideas.find({"user_id": user_id})

    # Transform cursor to list of ideas
    idea_list = [{"idea": idea["idea"], "created_at": idea["created_at"]} for idea in ideas]

    if not idea_list:
        return jsonify({"message": "No ideas found"}), 404

    return jsonify({"ideas": idea_list}), 200

@auth.route("/search-ideas", methods=["POST"])
@jwt_required()
def search_ideas():
    user_id = get_jwt_identity()
    data = request.json
    query = data.get("query")  
    retrieve_all = data.get("retrieve_all", False) 

    # Retrieve all ideas if requested
    if retrieve_all:
        ideas = mongo.db.ideas.find({"user_id": user_id})
    else:
        # Search ideas containing the query string (case-insensitive)
        ideas = mongo.db.ideas.find({"user_id": user_id, "idea": {"$regex": query, "$options": "i"}})

    # Transform cursor to list of ideas
    idea_list = [{"idea": idea["idea"], "created_at": idea["created_at"]} for idea in ideas]

    if not idea_list:
        return jsonify({"message": "No matching ideas found"}), 404

    return jsonify({"ideas": idea_list}), 200

@auth.route("/fetch-all-ideas", methods=["GET"])
@jwt_required()
def fetch_all_ideas():
    user_id = get_jwt_identity()

    # Fetch all ideas for the user
    ideas = mongo.db.ideas.find({"user_id": user_id})
    idea_list = [{"idea": idea["idea"], "created_at": idea["created_at"]} for idea in ideas]

    if not idea_list:
        return jsonify({"message": "No ideas found"}), 404

    return jsonify({"ideas": idea_list}), 200

@auth.route("/llm-query-ideas", methods=["POST"])
@jwt_required()
def llm_query_ideas():
    user_id = get_jwt_identity()
    data = request.json
    user_query = data.get("query")

    # Fetch all ideas from the database
    ideas = mongo.db.ideas.find({"user_id": user_id})
    idea_list = [{"idea": idea["idea"], "created_at": str(idea["created_at"])} for idea in ideas]

    if not idea_list:
        return jsonify({"message": "No ideas found"}), 404

    OPENAI_API_KEY = os.getenv(OPENAI_API_KEY)

    llm_prompt = f"""
    User Query: "{user_query}"

    Here is a list of the user's saved ideas:
    {idea_list}

    Task: Scan through the ideas and determine the one most relevant to the user's query.
    If the user explicitly asks for all ideas, return all of them.
    Format the response as JSON:
    {{
        "response": "Your relevant idea or all ideas",
        "context": "Explanation of the match"
    }}
    """

    response = openai.Completion.create(
        model="gpt-4",
        prompt=llm_prompt,
        max_tokens=300
    )

    llm_response = response["choices"][0]["text"].strip()

    # Parse and return the LLM's response
    return jsonify({"response": llm_response}), 200
