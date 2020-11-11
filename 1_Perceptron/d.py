import numpy


etha = 0.1
alpha = 0.9
w = numpy.array([0.1,0.1,0.1])

###training set [1,x(1),x(2)] ---> desired value
file = open("P1-dataset.txt","r")
line = file.readline()
dataset = []
while(line):
    spline = line.split(',')
    x = numpy.array([1,float(spline[0])/100.0,float(spline[1])/100.0])
    d = (int(spline[2])-0.5)*2
    dataset.append([x,d])
    line = file.readline()
    #print float(spline[1])/100.0
#print dataset
#################################################

time=1
largest_change = 2

while(largest_change > 0.1):
    etha = 1.0/(1.0+(time/4.0))
    largest_change = 0.1
    time+=1

    flag = False
    for data in dataset:
        y = (data[0].T).dot(w)
        if flag:
            diffrence = (1-alpha)*etha*(data[1]-y)*data[0]+(alpha*diffrence)
        else:
            diffrence = etha*(data[1]-y)*data[0]
            flag = True

        #old=data[1]-y
        #print "data",data[0],data[1],y
        largest_change=max(largest_change,max(numpy.absolute(diffrence)))
        #print "dd",
        #print "ww",w

        w = w + diffrence
    print largest_change


print "Result for [bias, w1, w2] is : ",w
print "Number of iterations : ",time