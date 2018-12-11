import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

iris = load_iris()
x = iris.data
y = iris.target

kmeans = KMeans(n_clusters=3)
kmeans.fit(x)
k_labels = kmeans.labels_
print "kmeans accuracy : " ,accuracy_score(y,k_labels)
plt.scatter(x[:,0],x[:,1],c=y[:])
plt.title("Actual classification - sepal")
plt.show()

plt.scatter(x[:,0],x[:,1],c=k_labels)
plt.title("kmeans classification - sepal")
plt.show()

gmm = GaussianMixture(n_components=3)
gmm.fit(x)
g_labels = gmm.predict(x)
plt.scatter(x[:,0],x[:,1],c=g_labels)
plt.title("GaussianMixture classification")
plt.show()