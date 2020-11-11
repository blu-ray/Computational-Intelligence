import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras import backend as K
from keras.optimizers import SGD
import math

import numpy as np

def rbf_pi(x,t):
    distance = (float(x)-float(t))*(float(x)-float(t))
    width = 1
    width = width*width
    return math.exp((-1*distance)/width)

val = -4.99
x= np.array([[1,1,1,1]])
y = np.array([])
rbf_centers = []
while(val<5):
    rbf_centers.append(val)
    #x = np.concatenate((x,np.array([rbf_pi(val,val)])))
    val+=0.01
val = -4.99
while(val<5):
    #row = np.array([])
    row = []
    for center in rbf_centers:
        #row = np.concatenate((row, np.array([rbf_pi(val, center)])))
        row = row+[rbf_pi(val,center)]
    #print(row)
    if (val==-4.99):
        #x=np.array([row])
        x = [row]
        #print (x)
    else:
        #x = np.append(x,[row],axis=0)
        x = x + [row]
    y = np.concatenate((y, np.array([val * val])))
    val+=0.01
#print (x)
x = np.array(x)
#print(x)
#print (len(x))
#print (rbf_pi(1,2))


model = Sequential()
model.add(Dense(1,activation='relu',input_dim=1000))
#model.add(Dense(1000,activation='relu'))
#model.add(Dense(1000,activation='relu'))
#model.add(Dense(1,activation='relu'))

sgd=SGD(lr=0.1)
model.compile(optimizer='adadelta',
              loss='mse',
              metrics=['accuracy'])


model.fit(x, y, epochs=10,batch_size=1)

val=-2
while(val<2.1):
    #inp = input()
    row = []

    for center in rbf_centers:
        #row = np.append(row, [np.array([rbf_pi(inp, center)])], axis=0)
        row += [rbf_pi(val,center)]
    #print(len(row))
    #print(row)
    row = np.asarray(row).reshape((1,1000))
    #print(row)
    y = model.predict(row)
    print (y[0][0])
    val+= 0.1
