# encoding utf-8
"""
Support Vector Machine

Part 1: SVMの原理
Part 2: カーネル法
Part 3: その他の資料
Part 4: scikit-learnでSVM


"""

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

from sklearn import datasets

'''
SVM

2つのクラスのデータからそれぞれなるべく離れている場所に引きますというのがマージン最大化の考え方

'''



'''

Kernel 法
https://www.youtube.com/watch?time_continue=42&v=3liCbRZPrZA


'''



'''

SVM with scikit-learn

'''

iris = datasets.load_iris()

X = iris.data
Y = iris.target
print(iris.DESCR)

# Support Vector Classification :SVC
from sklearn.svm import SVC 

# Instance
model = SVC()

# Split data
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state = 3)

# Train Model
model.fit(X_train, Y_train)

# モデルの精度
from sklearn import metrics

predicted = model.predict(X_test)
expected = Y_test

print(metrics.accuracy_score(predicted, expected))


"""
SVM kernel 作る
"""

from sklearn import svm

# 2-D plot, for 2 vars
print(X)
# X は，2重配列なので，2つ目の配列の(0 =< X < 2) に対応するデータを読み込む. [:, 0:2]
X = iris.data[:, 0:2]
print(X)

# 各観測値のクラスはデータセットの .target 属性として保管される.
# n_samples の長さを持つ整数の1次元配列
Y = iris.target
print(Y)
