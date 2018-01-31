# coding: utf-8

"""
Support Vector Machine

Part 1: SVMの原理
Part 2: カーネル法
Part 3: その他の資料
Part 4: scikit-learnでSVM

参考
http://www.turbare.net/transl/scipy-lecture-notes/packages/scikit-learn/index.html

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
print(Y.shape)

# SVM 正則化のパラメータ
C = 1.0

# SVC with a Linear Kernel
svc = svm.SVC(kernel = 'linear', C = C).fit(X, Y)

# Gaussian Radial Basis Function
rbf_svc = svm.SVC(kernel = 'rbf', gamma = 0.7, C = C).fit(X, Y)

# SVC with 3rd degree polynomial(3次元多項式)
poly_svc = svm.SVC(kernel = 'poly', degree = 3, C = C).fit(X, Y)

# SVC Linear
lin_svc = svm.LinearSVC(C = C).fit(X, Y)


# step size
h = 0.02

# X-axis max, min
x_min = X[:, 0].min() - 1
x_max = X[:, 0].max() + 1

# Y-axis max, min
y_min = X[:, 1].min() - 1
y_max = X[:, 1].max() + 1

# meshgrid() を作る
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))


titles = ['SVC with linear kernel', \
          'LinearSVC (linear kernel)', \
          'SVC with RBF kernel', \
          'SVC with polynomial (degree 3) kernel']

for i, clf in enumerate((svc, lin_svc, rbf_svc, poly_svc)):

    # 境界線
    plt.figure(figsize = (15, 15))
    plt.subplot(2, 2, i + 1)

    plt.subplots_adjust(wspace = 0.4, hspace = 0.4)

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    Z = Z.reshape(xx.shape)

    # http://ailaby.com/contour/
    plt.contourf(xx, yy, Z, cmap = plt.cm.terrain, alpha = 0.5, linewidth = 0)

    plt.scatter(X[:, 0], X[:, 1], c = Y, cmap = plt.cm.Dark2)

    plt.xlabel('Sepal length')
    plt.ylabel('Sepal width')
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xticks(())
    plt.yticks(())
    plt.title(titles[i])
    

plt.show()

