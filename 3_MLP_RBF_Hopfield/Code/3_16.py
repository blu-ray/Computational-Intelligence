from PIL import Image,ImageFont
import numpy as np
import random
'''
font_size = 16
font = ImageFont.truetype("Tahoma.ttf",font_size)
for char in "ABCDEFGHIJ":
    im = Image.Image()._new(font.getmask(char))
    im.save(char + ".bmp")
'''
def is_equal(sample1,sample2):
    for i in range(len(sample1)):
        if ((sample1[i]>200 and sample2[i]<50)or(sample1[i]<50 and sample2[i]>200)):
            return False
    return True

def sigmafunc(weight_row,sample):
    sigma = 0.0
    for i in range(len(sample)):
        sigma += weight_row[i] * (sample[i]/127.5-1)
        #print(weight_row[i],sample[i]/127.5-1)
    #print(sigma)
    #print ("DDDDDD")
    #print(sigma)
    if (sigma>=0):
        return 255
    else:
        return 0
images = []
for Letter in "ABCDEFGHIJKLMNO":
    im = Image.open("ABCDEFGHIJKLMNO\\16\\"+Letter+".bmp")
    sampleimage = list(im.getdata())
    for i in range(len(sampleimage)):
        if(sampleimage[i]<128):
            sampleimage[i] = 0
        else:
            sampleimage[i] = 255
    images += [sampleimage]
    #print(len(sampleimage))
    if(len(sampleimage)<650):
        while(len(images[-1])<650):
            images[-1].append(random.randint(0,1)*255)
            #images[-1].append(255)
    #print (images[-1])
    #images = np.append(images,[sampleimage])
#images = np.array(images)
#print(images.shape)

#image = np.array()
#bimages=np.array(images[0])
#for sampleimage in images:
#    bimages=np.append(bimages,np.array(sampleimage),axis=0)
#print (len(images[0]))
weight_matrix = []
#images = [[0,255,255,0,255],[255,0,255,0,255]]
#sampleimage = [0,0,255,255,255]

for j in range(len(sampleimage)):
    row = []
    for i in range(len(sampleimage)):
        sigma = 0.0
        c=0
        if (i!=j):
            for sample in images:
                #print (i,j,len(sample))
                if(c<0):
                    c+=1
                    continue
                sigma += (sample[i]/127.5 -1)*(sample[j]/127.5 -1)
                #print(c)
                c+=1
                if(c>15):

                    break

       # row.append(sigma/float(len(sampleimage)))

        row.append(sigma)

    weight_matrix.append(row)

#print("Ssss")
#print(len(weight_matrix[155]))
#print ("ssssss")
c = 0
for sample in images:
    corrupted = sample[:]
    #print (c)
    #c+=1
    #print(is_equal(sample, corrupted))

    for index in range(int(9*len(corrupted)/10),len(corrupted)):
        #pass
        corrupted[index] = 255
    #corrupted=[255,255,255,255,255]
    #print(is_equal(sample, corrupted))

    change = True
    counter = 0
    #print("corrupted first")
    #print(corrupted)
    #print("weight[0]")
    #print(weight_matrix[0])
    while(change and counter<1000 )  :
        change = False
        counter += 1
        #beforeassign = corrupted[:]
        cooo=0
        for index in range(len(corrupted)):
            newval = sigmafunc(weight_matrix[index],corrupted)

            #print (corrupted[index])
            #print (newval)
            if (corrupted[index]!=newval):
                corrupted[index] = newval
                #print(newval)
                #print(cooo)
                #print(index)
                #print("done")
                #cooo+=1
                change = True
        #corrupted = beforeassign[:]
    if(counter==1000):
        print ("fucked up")
        print (counter)
    #print("corrupted final")
    #print(corrupted)
    if (is_equal(sample,corrupted)):
        c+=1

print("Noise : 10%")
print(c,end=' ')
print("out of ",end=' ')
print(len(images),end=' ')
print("Images Restored Succesfully")
print("----------------------------")

c = 0
for sample in images:
    corrupted = sample[:]
    #print (c)
    #c+=1
    #print(is_equal(sample, corrupted))

    for index in range(int(7*len(corrupted)/10),len(corrupted)):
        #pass
        corrupted[index] = 255
    #corrupted=[255,255,255,255,255]
    #print(is_equal(sample, corrupted))

    change = True
    counter = 0
    #print("corrupted first")
    #print(corrupted)
    #print("weight[0]")
    #print(weight_matrix[0])
    while(change and counter<1000 )  :
        change = False
        counter += 1
        #beforeassign = corrupted[:]
        cooo=0
        for index in range(len(corrupted)):
            newval = sigmafunc(weight_matrix[index],corrupted)

            #print (corrupted[index])
            #print (newval)
            if (corrupted[index]!=newval):
                corrupted[index] = newval
                #print(newval)
                #print(cooo)
                #print(index)
                #print("done")
                #cooo+=1
                change = True
        #corrupted = beforeassign[:]
    if(counter==1000):
        print ("fucked up")
        print (counter)
    #print("corrupted final")
    #print(corrupted)
    if (is_equal(sample,corrupted)):
        c+=1

print("Noise : 30%")
print(c,end=' ')
print("out of ",end=' ')
print(len(images),end=' ')
print("Images Restored Succesfully")
print("----------------------------")


c = 0
for sample in images:
    corrupted = sample[:]
    #print (c)
    #c+=1
    #print(is_equal(sample, corrupted))

    for index in range(int(4*len(corrupted)/10),len(corrupted)):
        #pass
        corrupted[index] = 255
    #corrupted=[255,255,255,255,255]
    #print(is_equal(sample, corrupted))

    change = True
    counter = 0
    #print("corrupted first")
    #print(corrupted)
    #print("weight[0]")
    #print(weight_matrix[0])
    while(change and counter<1000 )  :
        change = False
        counter += 1
        #beforeassign = corrupted[:]
        cooo=0
        for index in range(len(corrupted)):
            newval = sigmafunc(weight_matrix[index],corrupted)

            #print (corrupted[index])
            #print (newval)
            if (corrupted[index]!=newval):
                corrupted[index] = newval
                #print(newval)
                #print(cooo)
                #print(index)
                #print("done")
                #cooo+=1
                change = True
        #corrupted = beforeassign[:]
    if(counter==1000):
        print ("fucked up")
        print (counter)
    #print("corrupted final")
    #print(corrupted)
    if (is_equal(sample,corrupted)):
        c+=1

print("Noise : 60%")
print(c,end=' ')
print("out of ",end=' ')
print(len(images),end=' ')
print("Images Restored Succesfully")
print("----------------------------")





