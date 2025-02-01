import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
    DATABASE_NAME = "movies"
    COLLECTION_NAME = "movie_collection"

    # Flask configuration
    SECRET_KEY = os.getenv("SECRET_KEY", "my-secret-key")
    DEBUG = os.getenv("DEBUG", "True") == "True"
