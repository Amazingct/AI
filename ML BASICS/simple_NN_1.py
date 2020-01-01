import numpy as np
def sigmoid(x):
    return 1/(1+np.exp(-x))
def sigmoid_deriavative(x):
    return x*(1-x)



#training dataset input
training_inputs= np.array([ [0,0,1],
                            [1,1,1],
                            [1,0,1],
                            [0,1,1]])
#training dataset output
training_outputs= np.array([[0,1,1,0]]).T

np.random.seed(1)
weights=2*np.random.random((3,1)) -1
print('Random starting weights: ')
print(weights)

#training
for a in range(10000):  
    input_layer=training_inputs
    weights_inputs_products=np.dot(input_layer,weights)
    outputs= sigmoid(weights_inputs_products)
    error= training_outputs - outputs
    adjustments =error *sigmoid_deriavative(outputs)
    weights+= np.dot(input_layer.T, adjustments)
    




print('weights after training: ')
print(weights)
print('outputs after training: ')
print(outputs)

def predict(data):
    input_layer=data
    return sigmoid(np.dot(input_layer,weights))

#trying new dataset input
data= np.array([[1,0,1],
                [0,1,0],
                [1,1,1],
                [0,0,1]])



#use CNN to determine new input
new_data_outputs=predict(data)
print('outputs after new inputs')
print(new_data_outputs)