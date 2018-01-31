# coding: utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""

Red wine quality analysis with scikit-learn
shape = (1559, 12)

fixed acidity 	        酒石酸濃度
volatile acidity 	酢酸酸度
citric acid 	        クエン酸濃度
residual sugar 	        残留糖濃度
chlorides 	        塩化物濃度
free sulfur dioxide 	遊離亜硫酸濃度
total sulfur dioxide 	亜硫酸濃度
density 	        密度
pH 	                pH
sulphates 	        硫酸塩濃度
alcohol 	        アルコール度数
quality 	        0-10 の値で示される品質のスコア

"""

wine = pd.read_csv("winequality-red.csv", sep = ";")
print(wine.head)
print(wine.shape)
print(wine['density'])

from sklearn import linear_model
clf = linear_model.LinearRegression()

# 説明変数 "densiny"
X = wine.loc[:, ['density']].as_matrix()
print(X)

# 目的変数 "alcohol"
Y = wine['alcohol'].as_matrix()
print(Y)

# 予測モデル
clf.fit(X, Y)

# 回帰係数(傾き)
print("coef_ =", clf.coef_)

# 切片(誤差)
print("intercept_ =", clf.intercept_)

print("決定係数(1に近い程相対的な残差が少ない)")
print("最小二乗法はこの定義を最大にするようなパラメタの選択法)")
print("決定係数 =", clf.score(X, Y))

# [alcohol] = clf.coef_ * [density] + clf.intercept_

# plot
plt.scatter(X, Y)

# 回帰直線
plt.plot(X, clf.predict(X))
plt.title("重回帰分析")

# 重回帰分析(目的:quality, 説明:それ以外)
clf2 = linear_model.LinearRegression()

wine_except_quality = wine.drop('quality', axis = 1)
print(wine_except_quality)
X = wine_except_quality.as_matrix()
print(X)

Y = wine['quality'].as_matrix()
print(Y)

# fit model
clf2.fit(X, Y)

# 傾き
print("傾き =", clf2.coef_)
# 切片
print("切片 =", clf2.intercept_)

# DF(q以外，quality) を作る
print( pd.DataFrame({"Name":wine_except_quality.columns,
                    "Coefficients":clf2.coef_}).sort_values(by = 'Coefficients') )


"""
各変数を正規化して重回帰分析

各変数がどの程度目的変数に影響しているかを確認するには、各変数を正規化 (標準化) し、平均 = 0, 標準偏差 = 1 になるように変換した上で、重回帰分析を行うと偏回帰係数の大小で比較することができるようになります。
"""
clf3 = linear_model.LinearRegression()

# 正規化
wine2 = wine.apply(lambda x: (x - np.mean(x)) / (np.max(x) - np.min(x)))
print(wine2.head)

# 説明変数に"quality(品質スコア以外すべて)"を利用, 列qualityを削除
# 列 A を削除 >>> df.drop("A", axis=1)
wine2_except_quality = wine2.drop('quality', axis = 1)
print("wine2_except_quality =", wine2_except_quality)

X = wine2_except_quality.as_matrix()
print(X.shape)
print(X)

# 目的変数に"quality"スコアを利用
Y = wine2['quality'].as_matrix()
print(Y.shape)
print(Y)

# fit model
clf3.fit(X, Y)

# 偏回帰係数
# alcoholが最も品質に効いていそう
print(pd.DataFrame({"Name":wine2_except_quality.columns,
                    "Coefficients":np.abs(clf3.coef_)}).sort_values(by = 'Coefficients'))

print("切片(誤差) =", clf3.intercept_)

plt.show()

