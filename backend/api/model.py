import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import os

# ✅ Load AI Model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "../model/mobilenetv2_transfer_learning.keras")
model = tf.keras.models.load_model(MODEL_PATH)

# ✅ Class Labels
CLASS_LABELS = ["Cat", "Dog"]  # Ensure this matches train_generator.class_indices

def classify_image(image_path, category):
    """Classifies an image using the trained MobileNetV2 model."""
    
    # ✅ Load & Preprocess Image
    img = load_img(image_path, target_size=(224, 224))  # Resize image
    img = img_to_array(img) / 255.0  # Normalize pixel values
    img = np.expand_dims(img, axis=0)  # Add batch dimension

    # ✅ Predict
    prediction = model.predict(img)
    class_index = np.argmax(prediction)
    confidence = np.max(prediction)

    # ✅ Return the class label and confidence score
    return f"Class: {CLASS_LABELS[class_index]}, Confidence: {confidence:.2%}"
