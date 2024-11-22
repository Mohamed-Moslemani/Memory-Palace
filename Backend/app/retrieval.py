from pymongo import MongoClient
from sentence_transformers import SentenceTransformer, util

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["brainstormer"]
ideas_collection = db["ideas"]
passwords_collection = db["passwords"]

# Load an embedding model for similarity scoring
embedder = SentenceTransformer("all-MiniLM-L6-v2")  

def retrieve_relevant_data(user_id, query, data_type="idea", top_k=3):
    """
    Retrieve the most relevant data (ideas or passwords) based on the query.
    """
    if data_type == "idea":
        data = ideas_collection.find({"user_id": user_id})
        data_list = [{"content": idea["idea"], "created_at": idea["created_at"]} for idea in data]
    elif data_type == "password":
        data = passwords_collection.find({"user_id": user_id})
        data_list = [{"content": f"{pw['service']}: {pw['password']}", "created_at": pw["created_at"]} for pw in data]
    else:
        raise ValueError("Invalid data type. Use 'idea' or 'password'.")

    if not data_list:
        return []

    # Compute similarity scores
    query_embedding = embedder.encode(query, convert_to_tensor=True)
    data_embeddings = embedder.encode([item["content"] for item in data_list], convert_to_tensor=True)
    scores = util.pytorch_cos_sim(query_embedding, data_embeddings).squeeze().tolist()

    # Rank data by relevance
    ranked_data = sorted(zip(data_list, scores), key=lambda x: x[1], reverse=True)
    return [item for item, _ in ranked_data[:top_k]]
