# encoding utf-8
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
import seaborn as sns

# Gaussian Naive Bayes
from sklearn import datasets
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB

"""

Naive : 各説明変数が互いに独立であると言う仮定



"""

iris = datasets.load_iris()

X = iris.data
Y = iris.target

print(iris.DESCR)

model = GaussianNB()

from sklearn.cross_validation import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state = 0)

model.fit(X_train, Y_train)

predicted = model.predict(X_test)
print(predicted)

acc = metrics.accuracy_score(Y_test, predicted)
print(acc)

