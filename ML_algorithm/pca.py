# coding: utf-8
"""

主成分分析は，次元削減のためのテクニックであり，可能な限りデータの分散を保ちつつ多次元のデータを低次元に変換．

(e.f.)モノクロ画像
各点の座標X，Yと明るさ，3次元のデータがあるとき
2次元に変換することは，画像圧縮や顔認識で役立つ

サンプルを用いてトライする．scikit-learnのIrisデータセットで，3種類のアヤメの花が4次元のデータで表されている．
すなわち，それぞれの花のpetal, sepalの幅と長さ．
データを読み込み，観察してみるところから始める

"""
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import pylab as pl
from itertools import cycle

iris = load_iris()

numSamples, numFeatures = iris.data.shape
print(numSamples)
print(numFeatures)
print(list(iris.target_names))

# 3dim->2dim
X = iris.data
pca = PCA(n_components = 2, whiten = True).fit(X)
X_pca = pca.transform(X)

# print("X_pca :", X_pca)
print("pca.components_ :", pca.components_)

# どれだけの情報を保存できているか確認
print(pca.explained_variance_ratio_) # 主成分の分散の割合
print(sum(pca.explained_variance_ratio_)) # 削減前と比較したの分散の比率(~3%)

from pylab import *

colors = cycle('rgb')
target_ids = range(len(iris.target_names))
pl.figure()

for i, c, label in zip(target_ids, colors, iris.target_names):
    pl.scatter(X_pca[iris.target == i, 0], X_pca[iris.target == i, 1],
               c = c, label = label)

pl.legend()
pl.show()



