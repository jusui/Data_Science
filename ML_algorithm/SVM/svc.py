# coding :utf-8
import numpy as np

"""
svm.SVC()

[参考]
http://neuro-educator.com/ml2/

"""

# Create fake income / age clusters for N people in k clusters
def createClusteredData(N, k):
    pointsPerCluster = float(N) / k
    X = []
    y = []

    for i in range(k):
        incomeCentroid = np.random.uniform(2000.0, 200000.0)
        ageCentroid    = np.random.uniform(20.0, 70.0)

        for j in range(int(pointsPerCluster)):
            X.append([np.random.normal(incomeCentroid, 10000.0), np.random.normal(ageCentroid, 2.0)])
            y.append(i)

    X = np.array(X)
    y = np.array(y)
    return X, y


from pylab import *

(X, y) = createClusteredData(100, 5)

plt.figure(figsize = (8, 6))
plt.scatter(X[:, 0], X[:, 1], c = y.astype(np.float))



"""
Data をクラスター化するために，線形SVMを使う

"""
from sklearn import svm, datasets

# training
C = 1.0
# svc = svm.SVC(kernel = 'linear', C = C).fit(X, y)
svc = svm.SVC(kernel = 'rbf', gamma = 1/2, C = C).fit(X, y)

# 格子状のメッシュを用いることで，分類された各領域を異なる色で塗る
def plotPredictions(clf):
    xx, yy = np.meshgrid(np.arange(0, 250000, 10),
                         np.arange(10, 70, 0.5))

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    plt.figure(figsize = (8, 6))
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap = plt.cm.Paired, alpha = 0.8)
    plt.scatter(X[:, 0], X[:, 1], c = y.astype(np.float))
    plt.show()

plotPredictions(svc)    

print("200000 $, 40 years-old")
print(svc.predict([[200000, 40]]))

print("50000 $, 65 years-old")
print(svc.predict([[50000, 65]]))
