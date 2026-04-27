import tensorflow as tf
from PIL import Image
import numpy as np

def load_model():
    model = tf.keras.models.load_model("outputs/models/mildew_detector.h5")
    return model


def preprocess_image(image):
    image = image.resize((100, 100))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image


def predict_image(model, image):
    processed = preprocess_image(image)
    prediction = model.predict(processed)[0][0]

    if prediction > 0.5:
        label = "Powdery Mildew"
        prob = prediction
    else:
        label = "Healthy"
        prob = 1 - prediction

    return label, float(prob)