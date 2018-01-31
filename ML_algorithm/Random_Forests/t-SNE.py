# coding:utf-8
import numpy as np
from sklearn import datasets
# 2.7系 only
# from sklearn.manifold import TSNE 
import matplotlib.pyplot as plt
from bhtsne import tsne
from sklearn.cluster import MeanShift, estimate_bandwidth
"""
boston data でTSNEをクラスタ可視化

https://github.com/dominiek/python-bhtsne/blob/master/test/tsne.py
[実装]
http://iwiwi.hatenadiary.jp/entry/2016/09/24/230640
"""
# コスメ
def mean_shift(X):
    bandwidth = estimate_bandwidth(X, quantile=0.3, n_samples=500)
    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    ms.fit(X)
    labels_unique = np.unique(ms.labels_)
    return len(labels_unique), ms.cluster_centers_


boston = datasets.load_boston()
print(boston.DESCR)
Y = tsne(boston.data)
print(Y)
plt.scatter(Y[:, 0], Y[:, 1], c = boston.target)
plt.figure()

num_clusters, cluster_centers = mean_shift(Y)
plt.scatter(boston.data[:, 5], boston.target)
plt.xlabel('Price[$1,000s]')
plt.ylabel('Number of rooms')


"""
K-Means
"""
from sklearn.cluster import MiniBatchKMeans
kmeans = MiniBatchKMeans(n_clusters = 10, max_iter = 1000)
kmeans_tsne = kmeans.fit_predict(Y)
print(kmeans_tsne)
plt.scatter(kmeans, Y)
plt.show()
