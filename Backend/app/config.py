from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/brainstormer")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY")
    MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
    MISTRAL_AGENT_ID = os.getenv("MISTRAL_AGENT_ID")