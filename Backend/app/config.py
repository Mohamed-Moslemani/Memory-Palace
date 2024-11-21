import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "fallback_secret_key") 
    MONGO_URI = "mongodb://localhost:27017/brainstormer"
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY","fallback_secret_key")