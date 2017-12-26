# coding:utf-8
import numpy as np
from sklearn import datasets
# 2.7系 only
# from sklearn.manifold import TSNE 
import matplotlib.pyplot as plt
from bhtsne import tsne

"""
boston data でTSNEをクラスタ可視化

"""

boston = datasets.load_boston()
print(boston.DESCR)
Y = tsne(boston.data)
print(Y)
plt.scatter(Y[:, 0], Y[:, 1], c = boston.target)

# model = TSNE(n_components = 2)
# tsne_result = model.fit_transform(boston.data)
# plt.plot(tsne_result[:, 0], tsne_result[:, 1], ".")

plt.show()

