import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from config import MODEL_PATH

# ✅ Load Pretrained Model
model = tf.keras.models.load_model(MODEL_PATH)

# ✅ Define Class Labels (Cat = index 0, Dog = index 1)
CLASS_LABELS = ["Cat", "Dog"]

def classify_image(image_path):
    """Processes an image and predicts if it's a Cat or Dog"""
    
    # ✅ Load and Preprocess Image
    img = load_img(image_path, target_size=(224, 224))  # Resize
    img_array = img_to_array(img)  # Convert to NumPy array
    img_array = np.expand_dims(img_array, axis=0) / 255.0  # Normalize and add batch dim

    # ✅ Make Prediction
    predictions = model.predict(img_array)  # Model outputs softmax probabilities
    predicted_class = np.argmax(predictions[0])  # Get the class index

    return CLASS_LABELS[predicted_class]  # Return "Cat" or "Dog"
