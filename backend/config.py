import os

# Flask App Configuration
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
MODEL_PATH = "model/mobilenetv2_transfer_learning.keras"

# Database Configuration
DB_CONFIG = {
    "dbname": "ai_classifier",
    "user": "your_user",
    "password": "your_password",
    "host": "localhost",
    "port": "5432"  # Use "3306" for MySQL
}

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
