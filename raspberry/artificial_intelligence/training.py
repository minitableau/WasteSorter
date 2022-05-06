import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator

img_height = 180
img_width = 180
batch_size = 32

train_ds = tf.keras.utils.image_dataset_from_directory('resources/dechets/', validation_split=0.2, subset="training",
                                                       seed=123, image_size=(img_height, img_width),
                                                       batch_size=batch_size)

class_names = train_ds.class_names
image = tf.keras.utils.load_img('resources/D1.jpg', target_size=(img_height, img_width))

model = keras.models.load_model('models/neural_net3.h5')

test_array = tf.keras.utils.img_to_array(image)
test_array = tf.expand_dims(test_array, 0)  # Create a batch
predictions = model.predict(test_array)
print("prediction du test", predictions)
score = tf.nn.softmax(predictions[0])
print("score", score)


print("Cette image représente surement un(e) {} avec une probabilité de {:.2f}%.".format(class_names[np.argmax(score)],
                                                                                         100 * np.max(score)))
