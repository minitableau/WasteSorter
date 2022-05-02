import numpy as np
import tensorflow as tf
from tensorflow import keras

#
# (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
#
# train_labels = train_labels[:1000]
# test_labels = test_labels[:1000]
#
# train_images = train_images[:1000].reshape(-1, 28 * 28) / 255.0
# test_images = test_images[:1000].reshape(-1, 28 * 28) / 255.0
#
# # Define a simple sequential model
# def create_model():
#   model = tf.keras.models.Sequential([
#     keras.layers.Dense(512, activation='relu', input_shape=(784,)),
#     keras.layers.Dropout(0.2),
#     keras.layers.Dense(10)
#   ])
#
#   model.compile(optimizer='adam',
#                 loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
#                 metrics=[tf.metrics.SparseCategoricalAccuracy()])
#
#   return model
#
# # Create a basic model instance
# model = keras.models.load_model('saved_model/my_model')
# model.fit(train_images, train_labels, epochs=5)

# Save the entire model as a SavedModel.
# model.save('saved_model/my_model')
img_height = 180
img_width = 180
batch_size = 32

train_ds = tf.keras.utils.image_dataset_from_directory('resources/dechets/',
                                                       validation_split=0.2, subset="training",
                                                       seed=123, image_size=(img_height, img_width),
                                                       batch_size=batch_size)

class_names = train_ds.class_names
model = keras.models.load_model('models/neural_net.h5')

import cv2

# On accède à la webcam
cam = cv2.VideoCapture(0)

# On prend une photo
ret, image = cam.read()

# Paramètre pour définir la fenêtre
nom_fenetre = "video_cam"

largeur_image = int(180)
hauteur_image = int(180)

cv2.namedWindow(nom_fenetre, cv2.WND_PROP_FULLSCREEN)

# Tout le temps
while True:
    # On prend une photo
    ret, image = cam.read()
    if ret:

        # On afffiche la fenêtre avec notre image
        cv2.imshow(nom_fenetre, image)
        imageR = cv2.resize(image, (180, 180))
        image_array = tf.keras.utils.img_to_array(imageR)
        image_array = tf.expand_dims(image_array, 0)  # probleme de dimension (480, 640)

        predictions = model.predict(image_array)
        score = tf.nn.softmax(predictions[0])

        print("This image n1 most likely belongs to {} with a {:.2f} percent confidence.".format(
            class_names[np.argmax(score)], 100 * np.max(score)))

        # On ajoute un temps d'attente
        # et on arrête la boucle si on appuie sur la touche 'q'
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
# Evaluate the restored model
# loss, acc = model.evaluate(test_images, test_labels, verbose=2)
# print('Restored model, accuracy: {:5.2f}%'.format(100 * acc))
#
# print(model.predict(test_images).shape)

