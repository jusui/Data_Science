# encoding uft-8
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

from sklearn.datasets import load_boston

"""

Linear Regression

Step 1: データの準備
Step 2: ひとまず可視化
Step 3: 最小二乗法の数学的な背景
Step 4: Numpyを使った単回帰
Step 5: 誤差について
Step 6: scikit-learnを使った重回帰分析
Step 7: 学習（Training）と検証Validation）
Step 8: 価格の予測
Step 9 : 残差プロット

"""

# ====================
# データの準備
# ====================
boston = load_boston()
print(boston.DESCR)

# 価格のヒストグラム. 
plt.hist(boston.target, bins = 50)
plt.xlabel('Price in $1,000s')
plt.ylabel('Number of houses')
plt.figure()

# 散布図 : 部屋数 vs. 価格
# RM はdata の5番目.
plt.scatter(boston.data[:, 5], boston.target)
plt.xlabel('Price ($1,000s)')
plt.ylabel('Number of rooms')

# DataFrameを作る
boston_df = DataFrame(boston.data)

# 列名を付ける (feature_names は，列名を格納した変数)
boston_df.columns = boston.feature_names
print(boston_df.head())

boston_df['Price'] = boston.target
print(boston_df.head())

# lmplot を使って，回帰直線を描く
sns.lmplot('RM', 'Price', boston_df)



"""
その2

最小二乗法の数学的な背景

二乗なのは，基準点からの方向に依らず絶対値を距離として見るため

http://mathtrain.jp/seikiequ

"""

# numpy で単回帰
# 部屋数
X = boston_df.RM
print(X.shape)

# 2-D array にする必要があるため，np.vstack() を使う
X = np.vstack(boston_df.RM)
print(X.shape)

# Y = 価格
Y = boston_df.Price
print(Y.shape)

# Y = Ap, (A = [x 1], p = [a b])
X = np.array([ [value, 1] for value in X ])

# numpy で線形回帰: np.linalg
print(np.linalg.lstsq(X, Y))

# 0番目がa, bの要素なので, [0] をa, bと定義
# 最小二乗法の計算を実行
a, b = np.linalg.lstsq(X, Y)[0]

# 元データをplot
plt.plot(boston_df.RM, boston_df.Price, 'o')
# plt.figure()

# 求めた回帰直線を描く
x = boston_df.RM
plt.plot(x, a*x+b, 'r')


result = np.linalg.lstsq(X, Y)
print(result)

# result の1つ目の要素が，errorの合計
error_total = result[1]

# plotの数で割る, root mean sqaured error(平均二乗誤差)
rmse = np.sqrt( error_total / len(X) )
print('平均二乗誤差の平方根 = {:0.2f}'.format(rmse[0]))
# 最小二乗誤差は，標準偏差に対応するので 95%の確率で，この値の2倍( 6.60*2 = +-13.2 )以上に誤差が広がることはないと結論

import sklean
from sklearn.linear_model import LinearRegression

lreg = LinearRegression()

plt.show()
