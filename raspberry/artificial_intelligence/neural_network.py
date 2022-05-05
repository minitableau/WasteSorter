import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

#
img_height = 180
img_width = 180
batch_size = 32

train_ds = tf.keras.utils.image_dataset_from_directory('resources/dechets/', validation_split=0.2, subset="training",
                                                       seed=123, image_size=(img_height, img_width),
                                                       batch_size=batch_size)

val_ds = tf.keras.utils.image_dataset_from_directory('resources/dechets/', validation_split=0.2, subset="validation",
                                                     seed=123,
                                                     image_size=(img_height, img_width), batch_size=batch_size)

class_names = train_ds.class_names
print(class_names)

AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
num_classes = len(class_names)

data_augmentation = tf.keras.Sequential(
  [
    layers.RandomFlip("horizontal", input_shape=(img_width, img_height, 3)),
    layers.RandomFlip("vertical"),
  ]
)

model = Sequential([
  data_augmentation,
  layers.Rescaling(1./255),
  layers.Conv2D(32, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(2),

  layers.Conv2D(64, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(2),

  layers.Conv2D(128, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(2),

  layers.Conv2D(256, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(2),

  layers.Flatten(),
  layers.Dense(128),
  layers.Dropout(0.4),
  layers.Dense(num_classes)
])


model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

epochs = 15
history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=epochs
)

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

# Save the entire model as a SavedModel.
model.save('models/neural_net3.h5')
loss2, acc2 = model.evaluate(val_ds, verbose=2)
print('Restored model, accuracy: {:5.2f}%'.format(100 * acc2))
epochs_range = range(epochs)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
# plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
# plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()

test = tf.keras.utils.load_img('resources/masque_noir_test.png', target_size=(img_height, img_width))

plt.imshow(test)
plt.show()

test_array = tf.keras.utils.img_to_array(test)
test_array = tf.expand_dims(test_array, 0)  # Create a batch

predictions = model.predict(test_array)
print("prediction du test", predictions)
score = tf.nn.softmax(predictions[0])
print("prediction ", predictions)
print("score", score)

if 100 * np.max(score) <= 75:
    print("déchet non reconnu")
else:
    print("This image n1 most likely belongs to {} with a {:.2f} percent confidence.".format(class_names[np.argmax(score)],
                                                                                         100 * np.max(score)))

test2 = tf.keras.utils.load_img('resources/GPT1.jpg', target_size=(img_height, img_width))
plt.imshow(test2)
plt.show()

test_array2 = tf.keras.utils.img_to_array(test2)
test_array2 = tf.expand_dims(test_array2, 0)  # Create a batch

predictions2 = model.predict(test_array2)
print("prediction du test 2", predictions2)
score2 = tf.nn.softmax(predictions2[0])
print("prediction 2", predictions2)
print("score 2", score2)

if 100 * np.max(score2) <= 75:
    print("déchet non reconnu")
else:
    print("This image n2 most likely belongs to {} with a {:.2f} percent confidence.".format(class_names[np.argmax(score2)],
                                                                                         100 * np.max(score2)))
