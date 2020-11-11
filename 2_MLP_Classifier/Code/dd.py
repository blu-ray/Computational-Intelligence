import tensorflow
import struct,numpy
import  matplotlib.pyplot as plt
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
from keras.callbacks import Callback
from sklearn.metrics import confusion_matrix, f1_score, precision_score, recall_score


class Metrics(Callback):

    def __init__(self):
        self.trainerror=[]
        self.testerror=[]

    def on_train_begin(self, logs={}):
        self.trainerror = []
        self.testerror = []


    def on_epoch_end(self, epoch, logs={}):
        self.trainerror.append(logs.get('loss'))
        self.testerror.append(self.model.evaluate(self.x_test,self.y_test)[0])
    def on_train_end(self, logs={}):
        #print (self.validation_data)
        val_predict = (numpy.asarray(self.model.predict(self.x_test))).round()
        val_targ = self.y_test
        _val_f1 = f1_score(val_targ, val_predict,average=None)
        f1_all = f1_score(val_targ, val_predict,average="micro")
        _val_recall = recall_score(val_targ, val_predict,average=None)
        recall_all = recall_score(val_targ, val_predict,average="micro")
        _val_precision = precision_score(val_targ, val_predict,average=None)
        precision_all=  precision_score(val_targ, val_predict,average="micro")
        print ("recall")
        print (_val_recall)
        print ("precision")
        print (_val_precision)
        print ("f1-score")
        print (_val_f1)
        print ("\n All :")
        print ("recall" , recall_all)
        print ("precision" ,precision_all)
        print ("f1-score" ,f1_all)
        return

batch_size = 128
num_classes = 10
epochs = 50
img_rows, img_cols = 28, 28
(x_train, y_train), (x_test, y_test) = mnist.load_data()

'''
x_train = x_train[:5000]
y_train = y_train[:5000]
x_test = x_test[:1000]
y_test =y_test[:1000]
'''
#  print(x_train.shape)
if K.image_data_format() == 'channels_first':
    x_train = x_train.reshape(x_train.shape[0], img_rows* img_cols)
    x_test = x_test.reshape(x_test.shape[0],  img_rows* img_cols)
    input_shape = (img_rows, img_cols)
else:
    x_train = x_train.reshape(x_train.shape[0], img_rows* img_cols)
    x_test = x_test.reshape(x_test.shape[0], img_rows*img_cols)
    input_shape = (img_rows, img_cols)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

#print (input_shape)
metrics = Metrics()
model =Sequential()
model.add(Dense(300,activation='relu',input_shape=(784,)))
model.add(Dropout(0.5))
model.add(Dense(300,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10,activation='softmax'))

model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

metrics.x_test = x_test
metrics.y_test = y_test
model.fit(x_train, y_train, epochs=epochs,callbacks=[metrics])
score = model.evaluate(x_test, y_test)
print (score)
score = model.evaluate(x_train,y_train)
print (score)

plt.figure(0)
#test = [1,2,3,4,5,6,7,8,9,10]
plt.plot(metrics.trainerror,'r')
plt.plot(metrics.testerror,'g')
print ("testerr",metrics.testerror)
#plt.plot(test,'g')
plt.xticks(numpy.arange(0, 51, 5.0))
plt.rcParams['figure.figsize'] = (8, 6)
plt.xlabel("Num of Epochs")
plt.ylabel("Loss")
plt.title("Training Loss vs Validation Loss")
plt.legend(['train','validation'])

plt.show()


weights = model.layers[0].get_weights()
#print (weights[0])
#print (weights[1])
#print (len(weights[0][0]))
#print (weights[0][0][3:7])

pixarray=[]
for i in range(len(weights[0])):
    pixarray.append(weights[0][i][0])
imarray = numpy.asfarray(pixarray[:]).reshape((28, 28))
plt.subplot(1, 2, 1 )
plt.subplots_adjust(hspace=0.5)
#plt.title("Train Set")
im = plt.imshow(imarray,cmap='Greys')


pixarray=[]
for i in range(len(weights[0])):
    pixarray.append(weights[0][i][150])
imarray = numpy.asfarray(pixarray[:]).reshape((28, 28))
plt.subplot(1, 2, 2 )
plt.subplots_adjust(hspace=0.5)
#plt.title("Train Set")
im = plt.imshow(imarray,cmap='Greys')

plt.show()