import os
import numpy as np
import tensorflow as tf


# ==========================================
# PROJECT DIRECTORY
# ==========================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


# ==========================================
# MODEL SETTINGS
# ==========================================

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "crop_disease_cnn.keras"
)

IMG_SIZE = (224, 224)


# ==========================================
# DISEASE CLASSES
# ==========================================

CLASS_NAMES = [
    "Tomato___Early_blight",
    "Tomato___healthy",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_Leaf_Spot",
    "Tomato___Spider_Mites"
]


# ==========================================
# ==========================================
# LOAD TRAINED MODEL
# ==========================================

print("Loading crop disease model...")

model = tf.keras.models.load_model(
    MODEL_PATH,
    compile=False
)

print("Model loaded successfully!")


# ==========================================
# PREDICTION FUNCTION
# ==========================================

def predict_disease(image_path):

    # Load image
    image = tf.keras.utils.load_img(
        image_path,
        target_size=IMG_SIZE
    )

    # Convert image to array
    image_array = tf.keras.utils.img_to_array(
        image
    )

    # Add batch dimension
    image_array = tf.expand_dims(
        image_array,
        0
    )

    # Make prediction
    predictions = model.predict(
        image_array,
        verbose=0
    )

    # Find class with highest probability
    predicted_index = np.argmax(
        predictions[0]
    )

    # Get class name
    predicted_class = CLASS_NAMES[
        predicted_index
    ]

    # Get confidence
    confidence = predictions[0][
        predicted_index
    ]

    return predicted_class, confidence


# ==========================================
# TEST THE MODEL
# ==========================================

if __name__ == "__main__":

    test_dir = os.path.join(
        BASE_DIR,
        "data",
        "processed",
        "test"
    )

    # Choose first disease class
    test_class = CLASS_NAMES[0]

    test_class_dir = os.path.join(
        test_dir,
        test_class
    )

    # Find images
    image_files = [
        file
        for file in os.listdir(test_class_dir)
        if file.lower().endswith(
            (".jpg", ".jpeg", ".png")
        )
    ]

    if len(image_files) == 0:

        print("No test images found.")

    else:

        test_image = os.path.join(
            test_class_dir,
            image_files[0]
        )

        disease, confidence = predict_disease(
            test_image
        )

        print()
        print("=" * 50)
        print("CROP DISEASE PREDICTION")
        print("=" * 50)

        print("Image:", test_image)

        print(
            "Prediction:",
            disease
        )

        print(
            f"Confidence: "
            f"{confidence * 100:.2f}%"
        )

        print("=" * 50)