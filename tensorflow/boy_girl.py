import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from tensorflow import keras
import time

data_dir = "/home/amazing/Desktop/PYTHON/AI/tensorflow/boy_girl"
labels = ["boy", "girl"]

# show images
"""
for label in labels:
    path = os.path.join(data_dir, label)
    for img in os.listdir(path):
        figure = os.path.join(path, img)
        print(figure)
        images = cv2.imread(figure, cv2.IMREAD_GRAYSCALE)
        images = cv2.resize(images, (200, 200))

        cv2.imshow("image", images)
        cv2.waitKey(2000)
        cv2.destroyAllWindows()
"""

training_images = []
training_labels = []


def pass_training_data():
    for label in labels:
        path = os.path.join(data_dir, label)
        class_num = labels.index(label)
        for img in os.listdir(path):
            figure = os.path.join(path, img)
            print(figure)
            images = cv2.imread(figure, cv2.IMREAD_GRAYSCALE)
            images = cv2.resize(images, (28, 28))
            training_images.append(images)
            training_labels.append(class_num)

            print(len(training_images))


pass_training_data()
for x in range(4):
    cv2.imshow(labels[training_labels[x]], training_images[x])
    cv2.waitKey(2000)
    cv2.destroyAllWindows()


model = keras.Sequential([keras.layers.Flatten(input_shape=(28, 28)), keras.layers.Dense(128, activation="relu"),
                          keras.layers.Dense(2, activation="softmax")])
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# training_images = training_images/255
model.fit(training_images, training_labels, epochs=1)

# predict
prediction = model.predict(training_images[1])
print(labels[np.argmax(prediction)])


