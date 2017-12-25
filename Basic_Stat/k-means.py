# coding: utf-8
from numpy import random, array

"""
clustering した収入と年齢のランダムなFake data

[KMeans]
http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
[numpy.random.uniform]
https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.random.uniform.html
"""
# create fake income/age clusters for N people in k clusters
def createClusteredData(N, k):
    random.seed(10)
    pointsPerCluster = float(N) / k
    X = []

    for i in range(k):
        incomeCentroid = random.uniform(20000.0, 200000.0)
        ageCentroid    = random.uniform(20.0, 70.0)

        for j in range(int(pointsPerCluster)):
            X.append( [random.normal(incomeCentroid, 10000.0), random.normal(ageCentroid, 2.0)] )

    X = array(X)

    return X
    
"""
K-Means でClusterの再設定し，教師なし学習
"""

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from numpy import random, float

k = 5
# 100 人-> 5 Cluster
data = createClusteredData(100, k)
print("data = ", data)

# KMeans(5)
model = KMeans(n_clusters = k)

# Note I'm scaling the data to normalize it! Important for good results.
model = model.fit(scale(data))

# We can see the clusters each data point was assinged to
# labels_ :: Labels of each point
print("model.labels_ =", model.labels_)
print("model.inertia_ = Sum of squared distances of samples to their closest cluster center.")
print(model.inertia_)
print("model.cluster_centers_ =", model.cluster_centers_)

# plot
plt.figure(figsize = (8, 6))
plt.scatter(data[:, 0], data[:, 1], c = model.labels_.astype(float))
plt.show()
