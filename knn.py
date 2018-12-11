from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

iris_data = load_iris()
# print iris_data
train_data,test_data,train_target,test_target= train_test_split(iris_data.data,iris_data.target)
knn = KNeighborsClassifier(n_neighbors = 8)
knn.fit(train_data,train_target)

for i in range(len(test_data)):
	x = test_data[i]
	pred = knn.predict([x])
	print test_target[i],iris_data['target_names'][test_target[i]],pred,iris_data['target_names'][pred]
print 'accuracy:',knn.score(test_data,test_target)