import cv2
import numpy as np
import tensorflow as tf
from tensorflow import keras

img_height = 280
img_width = 280
batch_size = 32

train_ds = tf.keras.utils.image_dataset_from_directory('artificial_intelligence/resources/dechets/', validation_split=0.2, subset="training",
                                                       seed=123, image_size=(img_height, img_width),
                                                       batch_size=batch_size)

class_names = train_ds.class_names
model = keras.models.load_model('artificial_intelligence/models/MODEL.h5')

largeur_image = 280
hauteur_image = 280


def detect(img):
    # On récupère les données de la photo
    imgResized = cv2.resize(img, (largeur_image, hauteur_image))
    imgArray = tf.keras.utils.img_to_array(imgResized)
    imgArray = tf.expand_dims(imgArray, 0)  # problème de dimension (480, 640)

    predictions = model.predict(imgArray)
    score = tf.nn.softmax(predictions[0])

    return class_names[np.argmax(score)], 100 * np.max(score)
