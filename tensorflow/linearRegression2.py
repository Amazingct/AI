import tensorflow as tf
import keras
import pandas as pd
import numpy as np
import sklearn
import cv2
from sklearn import linear_model
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style


from sklearn.utils import shuffle

# read data from dataset, sep stands for what separate the variables
data = pd.read_csv("student-mat.csv", sep=";")
# print the headings of the data set, i.e labels
print(data.head())
# select the data you need
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]
print(data)
# we want to use G3 as our datatset output(y) to be predicted and other variables as input(x)
# drop(remove) G3 from the dataset and save into x as an array then save other variables into y
predict = "G3"
print("G3: ", data.drop([predict], 1), "end of G3")
print("end of G3")
x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

# split(take) 10% (0.1) of our data and use as testing data(x_test and y_test) and use the other 90 percent to train
# the function returns the training data and testing data
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

# use saved trained model ( no need to train again)
pickle_in = open("studentModel.pickle", "rb")
linear = pickle.load(pickle_in)

# print the slops of each variable in the multi-dimensional (5 dimensions) graph and y intercept
print("coefficient: \n", linear.coef_)
print("intercept: \n", linear.intercept_)

# now lets predict using the test data
predictions = linear.predict(x_test)

for x in range(len(predictions)):
    # print both predictions output and actual data (input, output)
    print(predictions[x], x_test[x], y_test[x])




