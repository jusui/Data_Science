# encoding utf-8
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

from sklearn.datasets import load_iris

"""

多クラス分類（Multi-Class Classification）
1.) Iris（アヤメ）データの紹介
2.) ロジスティック回帰を使った多クラス分類の紹介
3.) データの準備
4.) データの可視化
5.) scikit-learnを使った多クラス分類
6.) K近傍法（K Nearest Neighbors）の紹介
7.) scikit-learnを使ったK近傍法
8.) まとめ

"""

"""
Step 1 - 3 Iris
花びら（petals）と萼片（sepals）

"""
from sklearn import linear_model
from sklearn.datasets import load_iris

# Read dataset
iris = load_iris()
# 説明
print(iris.DESCR)

# X : 説明変数
X = iris.data
print(X)

# Y : 目的変数
Y = iris.target
print(Y)

# pandas.DataFrame
iris_data = DataFrame(X, columns = ['Sepal Length', 'Sepal Width', \
                                    'Petal Length', 'Petal Width'])

iris_target = DataFrame(Y, columns = ['Species'])


# class(0, 1, 2)なので，文字列の名前を付ける
def flower(num):
    ''' 数字を受け取って，対応する名前を返す'''

    if num == 0:
        return 'Setosa'
    elif num == 1:
        return 'Veriscolour'
    else:
        return 'Virginica'

iris_target['Species'] = iris_target['Species'].apply(flower)
print(iris_target.head())

# DataFrame をまとめると
iris = pd.concat([iris_data, iris_target], axis = 1)
print(iris.head())


'''
Step 4: データの可視化
花びら（petals）と萼片（sepals）

'''
sns.pairplot(iris, hue = 'Species', size = 2)
# Setosa は特徴的な分布をしている


# 花びらの長さを特徴量としてhistogramをかく
plt.figure(figsize = (12, 4))
sns.countplot('Petal Length', data = iris, hue = 'Species')

plt.figure(figsize = (12, 4))
sns.countplot('Sepal Length', data = iris, hue = 'Species')

plt.figure()
'''

Step 5: scikit-learnを使った多クラス分類


'''
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split

# instance
logreg = LogisticRegression()

# Split dataset, test : train = 40 : 60
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.4, \
                                                    random_state = 3)

# Train data
logreg.fit(X_train, Y_train)

from sklearn import metrics

# テストデータを予測する. sklearn.predict()
Y_pred = logreg.predict(X_test)

# 精度を計算. metrics.accuracy_score()
print(metrics.accuracy_score(Y_test, Y_pred))



'''

Step 6: K近傍法
k-nearest neighbor:kNN

学習のプロセスは、単純に学習データを保持するだけです。新しいサンプルが、どちらのクラスに属するかを予測するときにだけ、すこし計算をします。

与えられたサンプルのk個の隣接する学習データのクラスを使って、このサンプルのクラスを予測します。 イメージをうまく説明した図がこちら。

'''
from sklearn.neighbors import KNeighborsClassifier

# Start with k = 6
# instance
knn = KNeighborsClassifier(n_neighbors = 6)

# Fit: Training
knn.fit(X_train, Y_train)

# Predict Test data(X_test)
Y_pred = knn.predict(X_test)

# Accuracy check
print("k = 6")
print(metrics.accuracy_score(Y_test, Y_pred))

# kNN (k = 1)
knn = KNeighborsClassifier(n_neighbors = 1)
knn.fit(X_train, Y_train)

Y_pred = knn.predict(X_test)
print("k = 1")
print(metrics.accuracy_score(Y_test, Y_pred))


# k を変化させてみる (1 < k < 90), (odd < k < even) など区間長が偶数でないとError 
k_range = range(1, 90)
print(k_range)

accuracy = []

# for 文で回す
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors = k)
    knn.fit(X_train, Y_train)
    Y_pred = knn.predict(X_test)
    # 計算した精度を配列accuracy に append() する
    accuracy.append(metrics.accuracy_score(Y_test, Y_pred))

# Plotする
plt.plot(k_range, accuracy)
plt.xlabel('K for kNN')
plt.ylabel('Testing for accuracy')



plt.show()
