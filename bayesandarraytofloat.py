﻿import numpy as np
data = [] # training data set
labels = [] # traning label set
test = [] # test data set
i=0
#tst=[1666,400,150,110,800,144,150,1000]
with open ('TestXman.csv') as testf:
    row = 0 # skip the first line
    for line in testf:
        testSamples = line.strip().split(",") 
        try:
		if(row >0):
            		test.append([float(num) for num in testSamples])
        except ValueError,e:
		print "error",e,"on line",i
	row +=1
	i=i+1

with open ('TrainXman.csv') as f:
    row = 0 # skip the first line
    for line in f:
        trainSamples = line.strip().split(",") 
        if(row > 0):
            data.append([float(num) for num in trainSamples[:-1]])
            labels.append(trainSamples[-1])
        row +=1



from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
y_pred = gnb.fit(data,labels).predict(test)
print ( y_pred)
y_1 = np.array(y_pred).astype(np.float)
y_avg = np.mean(y_1);
print (y_avg)

