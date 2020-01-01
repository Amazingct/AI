import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
# we are dealing with images of 28*28 pixels, which will be flatten to 784 input for our NN
# 128 hidden neurons (1 layer)
# 10 output neurons
# activation function = relu

data = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = data.load_data()
class_name = ['T-shirt', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneakers', 'Bag', 'Ankle boot']

train_images = train_images/255
test_images = test_images/255

""" 

plt.show(train_images[7], cmap=plt.cm.binary)
plt.show()

"""

model = keras.Sequential([keras.layers.Flatten(input_shape=(28, 28)), keras.layers.Dense(128, activation="relu"),
                          keras.layers.Dense(10, activation="softmax")])
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

model.fit(train_images, train_labels, epochs=5)

"""
test_loss, test_acc = model.evaluate(test_images, test_labels)
print ("Tested Accuracy: ", test_acc)
"""

# test the model by predicting what test image 7 is
prediction = model.predict(test_images)
for i in range(5):
    plt.grid(False)
    plt.imshow(test_images[i], cmap=plt.cm.binary)
    plt.xlabel("actual: " + class_name[test_labels[i]])
    plt.title("prediction" + class_name[np.argmax(prediction[i])])
    plt.show()






