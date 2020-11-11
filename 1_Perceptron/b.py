import numpy

etha = 0.1
w = numpy.array([0.1,0.2,0.3])

###training set [1,x(1),x(2)] ---> desired value
x1 = numpy.array([1,1,1])
d1 = 1

x2 = numpy.array([1,1,-1])
d2 = -1

x3 = numpy.array([1,-1,-1])
d3 = -1

x4 = numpy.array([1,-1,1])
d4 = -1
#################################################

time=1
largest_change = 1.0

while(largest_change > 0.001):
    etha = 0.1/(1.0+(time/4.0))
    largest_change = 0.001
    time+=1


    y1 = (x1.T).dot(w)
    diffrence = etha*(d1-y1)*x1
    largest_change=max(largest_change,max(numpy.absolute(diffrence)))
    w = w + diffrence

    y2 = (x2.T).dot(w)
    diffrence = etha*(d2-y2)*x2
    largest_change = max(largest_change, max(numpy.absolute(diffrence)))
    w = w + diffrence

    y3 = (x3.T).dot(w)
    diffrence = etha*(d3-y3)*x3
    largest_change = max(largest_change, max(numpy.absolute(diffrence)))
    w = w + diffrence


    y4 = (x4.T).dot(w)
    diffrence = etha*(d4-y4)*x4
    largest_change = max(largest_change, max(numpy.absolute(diffrence)))
    w = w + diffrence


print "Result for [bias, w1, w2] is : ",w
print "Number of iterations : ",time