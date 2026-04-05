import tensorflow as tf
import numpy as np
import cv2


model = tf.keras.models.load_model("model.h5")


classes = ["garbage", "pothole"]

def predict_image(image_path):
    
    # read image
    img = cv2.imread(image_path)

    if img is None:
        return "Error: Image not found"

    # resize + normalize
    img = cv2.resize(img, (128,128))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    # prediction
    prediction = model.predict(img)

    print("Prediction values:", prediction)   

    class_index = np.argmax(prediction)

    return classes[class_index]
def detect_severity(image_path):
    
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # simple heuristic: variance of image
    variance = cv2.Laplacian(gray, cv2.CV_64F).var()

    
    if variance > 500:
        return "Severe"
    elif variance > 200:
        return "Moderate"
    else:
        return "Low"