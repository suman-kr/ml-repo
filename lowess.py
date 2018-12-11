import matplotlib.pyplot as plt
import numpy as np
tou = 0.5
x_train = np.array(list(range(3,33))+[3.2,6.2])
print x_train
x_train = x_train[:,np.newaxis]
print "after adding axis:", x_train
y_train = np.array([1,2,1,2,1,1,3,4,5,4,5,6,5,6,7,8,9,10,11,11,12,11,11,10,12,11,11,10,9,8,2,13])
x_test = np.array([i/10 for i in range(400)])
print x_test
x_test = x_test[:,np.newaxis]
y_test = []
count = 0
for i in range(len(x_test)):
	wts = np.exp(-np.sum((x_train-x_test[i])**2,axis=1)/(2*tou)**2)
	w = np.diag(wts)
	factor1 = np.linalg.inv(x_train.T.dot(w).dot(x_train))
	parameters = factor1.dot(x_train.T).dot(w).dot(y_train)
	prediction = x_test[i].dot(parameters)
	y_test.append(prediction)
	count += 1

y_test=np.array(y_test)
plt.plot(x_train.squeeze(),y_train,'o')
plt.plot(x_test.squeeze(),y_test,'*')
plt.show()