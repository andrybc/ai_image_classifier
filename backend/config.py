import os
from dotenv import load_dotenv

# ✅ Load Environment Variables
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
dotenv_path = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path)

# ✅ Flask App Configuration
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")

# ✅ MySQL Database Configuration
DB_CONFIG = {
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT", 3306)),
}

