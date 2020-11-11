import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras import backend as K
from keras.optimizers import SGD


import numpy as np

'''
x_train = np.random.random((1000, 20))
y_train = keras.utils.to_categorical(np.random.randint(10, size=(1000, 1)), num_classes=10)
x_test = np.random.random((100, 20))
y_test = keras.utils.to_categorical(np.random.randint(10, size=(100, 1)), num_classes=10)
'''
#x =np.array([[1,0],[1,1],[0,1],[0,0]])
#y =np.array([[0],[1],[0],[0]])
#new = np.array([[2,2]])
#x = np.concatenate((x,new))
#print (x)
val = -5
x= np.array([])
y = np.array([])
while(val<5):
    #print (val)
    x = np.concatenate((x,np.array([val])))
    y = np.concatenate((y,np.array([val*val])))
    val+=0.01
print (x[100])
print (y[100])
#x_t= np.array([[1,0]])
#y_t = np.array([[1]])
#print (x[0])

model = Sequential()
model.add(Dense(10000,activation='relu',input_dim=1))
#model.add(Dense(1000,activation='relu'))
#model.add(Dense(1000,activation='relu'))
model.add(Dense(1,activation='relu'))

sgd=SGD(lr=0.1)
model.compile(optimizer='adadelta',
              loss='mse',
              metrics=['accuracy'])

#model.fit(data, one_hot_labels, epochs=10, batch_size=32)
model.fit(x, y, epochs=20,batch_size=1)
#score = model.evaluate(x_t, y_t)
#print (score)
val=-2
while(val<2.1):
    #inp = input()
    y = model.predict(np.array([val]))
    print (y[0][0])
    val+= 0.1
#print("111sdfadsf")
#weights = model.layers[0].get_weights()
#print (weights)

#inp = model.input                                           # input placeholder
#outputs = [layer.output for layer in model.layers]          # all layer outputs
#functors = [K.function([inp]+ [K.learning_phase()], [out]) for out in outputs]  # evaluation functions

# Testing

#layer_outs = [functors[-1]([x_t, 1.])]
#print (layer_outs)
#print("111111111111111")
#print(model.layers[-1].get_weights())
