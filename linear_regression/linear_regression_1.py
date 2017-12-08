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
print(boston_df)

# 列名を付ける (feature_names は，列名を格納した変数)
boston_df.columns = boston.feature_names
print(boston_df.head())

# Price カラムを作成
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
plt.figure()

result = np.linalg.lstsq(X, Y)
print(result)

# result の1つ目の要素が，errorの合計
error_total = result[1]

# plotの数で割る, root mean sqaured error(平均二乗誤差)
rmse = np.sqrt( error_total / len(X) )
print('平均二乗誤差の平方根 = {:0.2f}'.format(rmse[0]))
# 最小二乗誤差は，標準偏差に対応するので 95%の確率で，この値の2倍( 6.60*2 = +-13.2 )以上に誤差が広がることはないと結論


"""

Step 6: scikit-learnを使った重回帰分析


lreg.fit() はデータを元にモデルを作ります。
lreg.predict() は作られたモデルを元に、予測値を返します。
lreg.score()は、決定係数を返します。 
決定係数は、説明変数でどれくらいうまく目的変数の値を説明出来ているかの指標になります。


"""
import sklearn
from sklearn.linear_model import LinearRegression
# LinearRegression class Instance
lreg = LinearRegression()

# 説明変数
X_multi = boston_df.drop('Price', 1)
print(X_multi.shape)

# 目的変数(Price)
Y_target = boston_df.Price

# fit() で Model を作る
lreg.fit(X_multi, Y_target)
### LinearRegression(copy_X = True, fit_intercept = True, n_jobs = 1, normalize = False)

# 切片の値を見る
print('切片の値 = {:0.2f}'.format(lreg.intercept_))
# 係数の値
print('係数の値 = {:0.2f}'.format(len(lreg.coef_)))

# 単回帰のときは，直線なので，係数a と切片bは，1つのみ.
# 今回は，lregcoef_ = 13ある -> 13個変数がある方程式であることを意味する

# 係数を見ていく
# 新しいDF
coeff_df = DataFrame(boston_df.columns)
# カラム名を Features に定義
coeff_df.columns = ['Features']

# 求められた係数をカラムに追加
coeff_df['Coefficient Estimate'] = pd.Series(lreg.coef_)
print(coeff_df)
# -> RM の係数が最も大きい


"""

Step 7: 学習（Training）と検証（Validation)


"""

# 説明変数X, 目的変数Yと定義
X_train, X_test, Y_train, Y_test = sklearn.cross_validation.train_test_split(X_multi, boston_df.Price)

# Split したデータセット
print(X_train.shape, X_test.shape, Y_train.shape, Y_test.shape)


"""

Step 8: 価格の予測


"""
# 学習用データで，モデルを作り，残りのデータで住宅価格を予測する
# インスタンス
lreg = LinearRegression()

# fit でmodel作り，学習用にかませる
lreg.fit(X_train, Y_train)

# 予測を，学習用データと，テスト用データ，両方で試してみる
pred_train = lreg.predict(X_train)
pred_test  = lreg.predict(X_test)

# それぞれの平均二乗誤差を計算してみる
print('X_trainを使ったモデルの平均二乗誤差 = {:0.2f}'.format(np.mean((Y_train - pred_train) ** 2)))

print('X_testを使ったモデルの平均二乗誤差 = {:0.2f}'.format(np.mean((Y_test - pred_test) ** 2)))

# X_trainでつくったモデルなので，X_testデータを使ってYを計算すると，実際の値からのズレが大きくなる


"""

Step 9 : 残差プロット

回帰分析では，実際に観測された値と，モデルが予測した値の差を残差と呼ぶ

残差 = 観測された値 - 予測された値

"""

# 学習用データの残差プロット
train = plt.scatter(pred_train, (pred_train - Y_train), c = 'b', alpha = 0.5)

# テスト用データの残差プロット
test = plt.scatter(pred_test, (pred_test - Y_test), c = 'r', alpha = 0.5)

# 残差の基準線 y = 0
plt.hlines(y = 0, xmin = -10, xmax = 50)

plt.legend((train, test), ('Training', 'Test'), loc = 'lower left')

plt.title('Residual Plots')

plt.show()
