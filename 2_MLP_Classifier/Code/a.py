
import struct,numpy
import  matplotlib.pyplot as plt

#Train Set
trainimg = open('..\\samples\\train-images.idx3-ubyte','rb')
trainlabel = open('..\\samples\\train-images.idx3-ubyte','rb')
data = trainimg.read(16)
x = struct.unpack('>IIII',data)
rows_no = x[2]
cols_no = x[3]

for id in range(23):
    linebits = []
    for row in range(rows_no):
        for col in range(cols_no):
            pixel = trainimg.read(1)
            pixelint = ord(pixel)
            linebits.append(pixelint)
            #print pixelint,
    imarray = numpy.asfarray(linebits[:]).reshape((28, 28))
plt.subplot(1, 2, 1 )
plt.subplots_adjust(hspace=0.5)
plt.title("Train Set")
im = plt.imshow(imarray,cmap='Greys')


#Test Set
trainfile = open('..\\samples\\t10k-images.idx3-ubyte','rb')
data = trainfile.read(16)
x = struct.unpack('>IIII',data)
rows_no = x[2]
cols_no = x[3]

for id in range(23):
    linebits = []
    for row in range(rows_no):
        for col in range(cols_no):
            pixel = trainfile.read(1)
            pixelint = ord(pixel)
            linebits.append(pixelint)
            #print pixelint,
    imarray = numpy.asfarray(linebits[:]).reshape((28, 28))
plt.subplot(1, 2, 2 )
plt.subplots_adjust(hspace=0.5)
plt.title("Test Set")
im = plt.imshow(imarray,cmap='Greys')


plt.show()



