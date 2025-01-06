from pymongo import MongoClient
import os 

client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017"))

db = client["brainstormer"]  
print(db.list_collection_names())