from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
from config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS
from api.model import classify_image
from api.db import insert_classification, fetch_classifications

api = Blueprint("api", __name__)

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@api.route("/classify", methods=["POST"])
def classify():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["file"]
    
    if file.filename == "" or not allowed_file(file.filename):
        return jsonify({"error": "Invalid file type"}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    # ✅ Run Classification
    classification = classify_image(filepath)

    # ✅ Store in Database
    insert_classification(filename, "Animal", classification)

    return jsonify({"filename": filename, "classification": classification})
