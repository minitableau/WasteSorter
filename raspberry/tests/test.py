import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

img_height = 180
img_width = 180
batch_size = 32

# model = keras.Sequential([
#     layers.Input((28, 28, 1)),
#     layers.Conv2D(16, 3, padding='same'),
#     layers.Conv2D(32, 3, padding='same'),
#     layers.MaxPooling2D(),
#     layers.Flatten(),
#     layers.Dense(10),
# ])

# ds_train = tf.keras.preprocessing.image_dataset_from_directory(
#     'Data/Nombres/',
#     labels='inferred',
#     label_mode = "int",
#     #class_names = [...]
#     color_mode='grayscale',
#     batch_size = batch_size,
#     image_size=(img_height, img_width),
#     shuffle = True,
#     seed = 123,
#     validation_split = 0.1,
#     subset = "training",
#     )

train_ds = tf.keras.utils.image_dataset_from_directory(
    'artificial_intelligence/resources/flower_photos/',
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size)

val_ds = tf.keras.utils.image_dataset_from_directory(
    'artificial_intelligence/resources/flower_photos/',
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size)

class_names = train_ds.class_names
print(class_names)

plt.figure(figsize=(10, 10))
for images, labels in train_ds.take(1):
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(class_names[labels[i]])
        plt.axis("off")
plt.show()

AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

normalization_layer = layers.Rescaling(1. / 255)

normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
image_batch, labels_batch = next(iter(normalized_ds))
first_image = image_batch[0]
# Notice the pixel values are now in `[0,1]`.
print(np.min(first_image), np.max(first_image))

num_classes = len(class_names)

# model = Sequential([
#   layers.Rescaling(1./255, input_shape=(img_height, img_width, 3)),
#   layers.Conv2D(16, 3, padding='same', activation='relu'),
#   layers.MaxPooling2D(),
#   layers.Conv2D(32, 3, padding='same', activation='relu'),
#   layers.MaxPooling2D(),
#   layers.Conv2D(64, 3, padding='same', activation='relu'),
#   layers.MaxPooling2D(),
#   layers.Flatten(),
#   layers.Dense(128, activation='relu'),
#   layers.Dense(num_classes)
# ])

# model.compile(optimizer='adam',
#               loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
#               metrics=['accuracy'])

# model.summary()

# epochs=10
# history = model.fit(
#   train_ds,
#   validation_data=val_ds,
#   epochs=epochs
# )
#
# acc = history.history['accuracy']
# val_acc = history.history['val_accuracy']
#
# loss = history.history['loss']
# val_loss = history.history['val_loss']
#
# epochs_range = range(epochs)
#
# plt.figure(figsize=(8, 8))
# plt.subplot(1, 2, 1)
# plt.plot(epochs_range, acc, label='Training Accuracy')
# plt.plot(epochs_range, val_acc, label='Validation Accuracy')
# plt.legend(loc='lower right')
# plt.title('Training and Validation Accuracy')
#
# plt.subplot(1, 2, 2)
# plt.plot(epochs_range, loss, label='Training Loss')
# plt.plot(epochs_range, val_loss, label='Validation Loss')
# plt.legend(loc='upper right')
# plt.title('Training and Validation Loss')
# plt.show()

data_augmentation = keras.Sequential(
    [
        layers.RandomFlip("horizontal",
                          input_shape=(img_height,
                                       img_width,
                                       3)),
        layers.RandomRotation(0.1),
        layers.RandomZoom(0.1),
    ]
)

model = Sequential([
    data_augmentation,
    layers.Rescaling(1. / 255),
    layers.Conv2D(16, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(32, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(64, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Dropout(0.2),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
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

epochs_range = range(epochs)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()

# sunflower_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/592px-Red_sunflower.jpg"
# sunflower_path = tf.keras.utils.get_file('Red_sunflower', origin=sunflower_url)
#
# img = tf.keras.utils.load_img(
#     sunflower_path, target_size=(img_height, img_width)
# )
#
# plt.imshow(img)
# plt.show()
#
# img_array = tf.keras.utils.img_to_array(img)
# img_array = tf.expand_dims(img_array, 0) # Create a batch
#
# predictions = model.predict(img_array)
# score = tf.nn.softmax(predictions[0])
#
# print(
#     "This image most likely belongs to {} with a {:.2f} percent confidence."
#     .format(class_names[np.argmax(score)], 100 * np.max(score))
# )
#
# img2 = tf.keras.utils.load_img(
#     'resources/fleurs_verifs/rose_1.jpg', target_size=(img_height, img_width)
#     )
# plt.imshow(img2)
# plt.show()
#
# img2_array = tf.keras.utils.img_to_array(img2)
# img2_array = tf.expand_dims(img2_array, 0) # Create a batch
#
# predictions2 = model.predict(img2_array)
# score2 = tf.nn.softmax(predictions2[0])
#
# print(
#     "This image n2 most likely belongs to {} with a {:.2f} percent confidence."
#     .format(class_names[np.argmax(score2)], 100 * np.max(score2)))
#
img3 = tf.keras.utils.load_img(
    'artificial_intelligence/resources/fleurs_verifs/dandelionT.jpg', target_size=(img_height, img_width)
)
plt.imshow(img3)
plt.show()

img3_array = tf.keras.utils.img_to_array(img3)
img3_array = tf.expand_dims(img3_array, 0)  # Create a batch

predictions3 = model.predict(img3_array)
score3 = tf.nn.softmax(predictions3[0])

print(
    "This image n3 most likely belongs to {} with a {:.2f} percent confidence."
        .format(class_names[np.argmax(score3)], 100 * np.max(score3)))

img4 = tf.keras.utils.load_img(
    'artificial_intelligence/resources/fleurs_verifs/tulipe.jpg', target_size=(img_height, img_width)
)

plt.imshow(img4)
plt.show()

img4_array = tf.keras.utils.img_to_array(img4)
img4_array = tf.expand_dims(img4_array, 0)  # Create a batch

predictions4 = model.predict(img4_array)
print("prediction img4", predictions4)
score4 = tf.nn.softmax(predictions4[0])
print("prediction 4", predictions4)
print("score 4", score4)

print(
    "This image n4 most likely belongs to {} with a {:.2f} percent confidence."
        .format(class_names[np.argmax(score4)], 100 * np.max(score4))
)

img5 = tf.keras.utils.load_img(
    'artificial_intelligence/resources/fleurs_verifs/Daisy.jpg', target_size=(img_height, img_width)
)

plt.imshow(img5)
plt.show()

img5_array = tf.keras.utils.img_to_array(img5)
img5_array = tf.expand_dims(img5_array, 0)  # Create a batch

predictions5 = model.predict(img5_array)
score5 = tf.nn.softmax(predictions5[0])

print(
    "This image n5 most likely belongs to {} with a {:.2f} percent confidence."
        .format(class_names[np.argmax(score5)], 100 * np.max(score5))
)

img6 = tf.keras.utils.load_img(
    'artificial_intelligence/resources/fleurs_verifs/dandelionDUR.jpg', target_size=(img_height, img_width)
)

plt.imshow(img6)
plt.show()

img6_array = tf.keras.utils.img_to_array(img6)
img6_array = tf.expand_dims(img6_array, 0)  # Create a batch

predictions6 = model.predict(img6_array)
score6 = tf.nn.softmax(predictions6[0])

print(
    "This image n6 most likely belongs to {} with a {:.2f} percent confidence."
        .format(class_names[np.argmax(score6)], 100 * np.max(score6))
)
