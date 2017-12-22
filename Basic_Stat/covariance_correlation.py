# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from  matplotlib.font_manager import FontProperties
fp = FontProperties(fname=r'/Library/fonts/ipag.ttf', size=11)


"""

共分散(covariance)と相関(correlation)
共分散は，二つのデータセット間の関係を表す数値。
相関は，データ間の因果関係を意味するわけではない.

例として、販売サイトの運営時、サイトの表示速度とユーザーの消費金額の関係を調べよう。

"""

def de_mean(x):
    xmean = mean(x)
    return [xi - xmean for xi in x]

# 基本的に、二つのデータセットは平均値からの距離のベクトルとし、それらの内積を計算
def covariance(x, y):
    n = len(x)
    # データ(x, y)平均の内積
    return dot(de_mean(x), de_mean(y)) / (n-1)

# 全くランダムで無関係な表示速度と購入合計額のデータセットをそれぞれ用意
pageSpeeds = np.random.normal(3.0, 1.0, 1000)
print(pageSpeeds)
purchaseAmount = np.random.normal(50.0, 10.0, 1000)
print(purchaseAmount)

plt.scatter(pageSpeeds, purchaseAmount)
plt.title("covariance")
plt.figure()

# 相関が無いため、共分散はとても小さい
print("covariance =", covariance(pageSpeeds, purchaseAmount))


# 表示速度とユーザの消費金額に関係を持たせる
# 負の共分散は，データ間で反比例する
purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds
scatter(pageSpeeds, purchaseAmount)
plt.title("covariance")
plt.figure()
# 
print("covariance =", covariance(pageSpeeds, purchaseAmount))


"""

相関を見る

"""
def correlation(x, y):
    stdx = x.std()
    stdy = y.std()
    return covariance(x, y) / stdx / stdy

print("correlation(pageSpeeds, purchaseAmount) =", correlation(pageSpeeds, purchaseAmount))

# numpy.correcoef() で簡単に計算
corr = np.corrcoef(pageSpeeds, purchaseAmount)
print("correlation(pageSpeeds, purchaseAmount) =", corr)


# 完全相関を作る
purchaseAmount = 100 - pageSpeeds * 3
plt.scatter(pageSpeeds, purchaseAmount)
plt.title("完全相関", fontproperties = fp)
print("correlation(pageSpeeds, purchaseAmount) =", correlation(pageSpeeds, purchaseAmount))


# Activity
# 共分散 : numpy.cov()
print("np.cov(pageSpeeds, purchaseAmount) =", covariance(pageSpeeds, purchaseAmount))
print("np.cov(pageSpeeds, purchaseAmount) =", np.cov(pageSpeeds, purchaseAmount))
print("np.cov(pageSpeeds, purchaseAmount) =", np.cov(pageSpeeds, purchaseAmount)[0][1])

plt.show()

