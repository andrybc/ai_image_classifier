import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")
    DB_CONFIG = {
        "database": os.getenv("DB_NAME"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "host": os.getenv("DB_HOST"),
        "port": int(os.getenv("DB_PORT", 3306)),
    }
