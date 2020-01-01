#this is the same as part 1, just using class 
import numpy as np

class NeuralNetwork():
    def __init__(self):
        np.random.seed(1)
        random_weights=np.random.random((3,1)) #it has to be a 3 by 1 matrix
        self.weights= 2*random_weights-1 #just to further make it ramdom

    def sigmoid(self,x):
        return 1/(1+np.exp(-x))

    def sigmoid_deriavative(self, x):
        return x*(1-x)
    
    def train (self, training_inputs,training_outputs,iterations):
        for a in range(iterations):  
            outputs=self.predict(training_inputs)
            error= training_outputs - outputs
            adjustments = np.dot(training_inputs.T, error *self.sigmoid_deriavative(outputs))
            self.weights+=adjustments

    def predict(self, inputs):
        inputs=inputs.astype(float) #convert to float
        outputs = self.sigmoid(np.dot(inputs,self.weights))
        return outputs

###############lets use this Neural Class################
###############create an object of the NN class and print the ramdom weights generted#
Network_1 = NeuralNetwork()
print("weights before trinig: ")
l=Network_1.weights
print(l)

#give training data
train_inputs=np.array([
                            [0,0,1],
                            [1,1,1],
                            [1,0,1],
                            [0,1,1]
                          ])
train_outputs=np.array([[0,1,1,0]]).T
#train Network
Network_1.train(train_inputs,train_outputs,900000)
print("weights after training: ")
print(Network_1.weights)

#ask user for new data
A= input ("enter new inputs A: ")
B= input ("enter new inputs B: ")
C= input ("enter new inputs C: ")

answer=Network_1.predict(np.array([[A,B,C]]))
print(answer)