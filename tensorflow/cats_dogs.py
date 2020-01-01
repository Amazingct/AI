import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
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

training_data = []


def pass_training_data():
    for label in labels:
        path = os.path.join(data_dir, label)
        class_num = labels.index(label)
        for img in os.listdir(path):
            figure = os.path.join(path, img)
            print(figure)
            images = cv2.imread(figure, cv2.IMREAD_GRAYSCALE)
            images = cv2.resize(images, (50, 50))
            training_data.append([images, class_num])
            # training_data now contains a list of list each holding image and labels(0=boy,1=girl)
            print(len(training_data))


pass_training_data()
print(np.shape(training_data[1]))



