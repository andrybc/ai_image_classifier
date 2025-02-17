import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

# Load the trained AI model
MODEL_PATH = "../model/mobilenetv2_transfer_learning.keras"
model = tf.keras.models.load_model(MODEL_PATH)

def classify_image(image_path, category):
    """Classifies an image using the AI model."""
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize pixel values

    # Predict
    predictions = model.predict(img_array)
    class_index = np.argmax(predictions)
    confidence = np.max(predictions)

    return f"Class: {category}, Confidence: {confidence:.2f}"

