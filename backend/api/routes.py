from flask import request, jsonify
from api.model import classify_image
from api.db import connect_db
from api import api_bp
import os
import json


@api_bp.route('/classify', methods=['POST'])
def classify():
    """Handle image uploads & classification."""
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files['image']
    category = request.form.get('category', 'Animals')

    if image.filename == '':
        return jsonify({"error": "No file selected"}), 400

    filepath = os.path.join("uploads", image.filename)
    image.save(filepath)

    # Classify the image
    result = classify_image(filepath, category)
    result_str = json.dumps(result)  # Convert dict to JSON string
    # Store result in database
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO ai_img_classifications (filename, category, result) VALUES (%s, %s, %s)",
            (image.filename, category, result_str),
        )
        conn.commit()
        conn.close()

    return jsonify({"filename": image.filename, "category": category, "result": result})
