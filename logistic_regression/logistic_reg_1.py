# encoding utf-8

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import math

# For plot
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

# For ML
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split

from sklearn import metrics

# statsmodels
import statsmodels.api as sm

"""

ロジスティック回帰（教師有り学習）
1. ロジスティック関数の基本
2. その他の資料
3. データの準備
4. データの可視化
5. データの前処理
6. 多重共線性（Multicollinearity）について
7. scikit-learnを使ったロジスティック回帰
8. 学習とテスト
9. その他の話題


"""

# Part 1: 数学的な基礎
# Logistic function
def logistic(t):
    return 1.0 / ( 1.0 + math.exp((-1.0) * t) )

# t を -6 ~ 6 まで500点用意
t = np.linspace(-6, 6, 500)

# list 内包表記で，y を準備
y = np.array([logistic(ele) for ele in t])

# plot
plt.plot(t, y)
plt.title(' Logistic Regression ')
plt.figure()


# Part 2: その他の資料
# http://gihyo.jp/dev/serial/01/machine-learning/0018


# Part 3: データの準備
# Affairs dataset (不倫に関するデータ)
# http://www.statsmodels.org/stable/datasets/generated/fair.html



# Part 4: データの可視化
# Load dataset and make a DataFrame
df = sm.datasets.fair.load_pandas().data
print(df.head())

# 不倫の有無を0, 1 で表現する列名 Had_Affair を作る
def affair_check(x):
    if x != 0:
        return 1
    else:
        return 0

# apply を使って，新しい列用のデータを作る
df['Had_Affair'] = df['affairs'].apply(affair_check)
print(df)

# 不倫の有無(Had_Affair 列)でgroupby
df.groupby('Had_Affair').mean()
print(df.groupby('Had_Affair').mean())

# 不倫有:年齢上，結婚期間長い，宗教観と学歴低め
# Age histogram with Had_Affair
sns.countplot('age', data = df.sort('age'), hue = 'Had_Affair', \
              palette = 'coolwarm')
plt.figure()

# 年齢の増加とともに不倫率も増加している.
# 結婚してからの年月
sns.countplot('yrs_married', data = df.sort('yrs_married'), \
              hue = 'Had_Affair', palette = 'coolwarm')
plt.figure()


# 結婚からの年月と不倫率は，比例している.
# 子供の数ではどうか
sns.countplot('children', data = df.sort('children'), \
              hue = 'Had_Affair', palette = 'coolwarm')
plt.figure()

# 子供の数が少ないと，不倫率は下がる. しかし，絶対数が多い.
# 学歴では
sns.countplot('educ', data = df.sort('educ'), hue = 'Had_Affair', \
              palette = 'coolwarm')
plt.figure()
# 相関は確認できない



# Part 5: データの前処理

# Categorical変数(occupation, occupation_husb)を Dummy変数に展開する
# pd.get_dummies()  が便利
occ_dummies = pd.get_dummies(df['occupation'])
hus_occ_dummies = pd.get_dummies(df['occupation_husb'])

print(occ_dummies.head())

# 列名をつける
occ_dummies.columns = ['occ1','occ2','occ3','occ4','occ5','occ6']
hus_occ_dummies.columns = ['hocc1','hocc2','hocc3','hocc4','hocc5','hocc6']

# 列を追加して，データセットを整理する
# 不要になったカテゴリカル変数と，目的変数を削除
X = df.drop(['occupation', 'occupation_husb', 'Had_Affair'], axis = 1)

# Dummy 変数のDataFrameを pd.concat() で繋げる
dummies = pd.concat([occ_dummies, hus_occ_dummies], axis = 1)

# すべてのDFを連結
X = pd.concat([X, dummies], axis = 1)
print(X.head())

# Yに目的変数を格納
Y = df.Had_Affair
print(Y.head())

sns.countplot('occ6', data = X.sort('occ6'), palette = 'coolwarm')




# Part 6: 多重共線性
# Dummy 変数同士は，高度に相関する可能性があるため，
# occ1, hocc1, 目的変数を解析から取り除く
X = X.drop('occ1', axis = 1)
X = X.drop('hocc1', axis = 1)
X = X.drop('affairs', axis = 1)

print(X.head())

# Yを1次元の arrayにする
Y = Y.values
# or Y = np.ravel(Y)
print(Y)



# Part 7: ScikitLearnを使ったロジスティック回帰
log_model = LogisticRegression()

# Data でModel作成
log_model.fit(X, Y)

# model 精度の確認 : score()
log_score = log_model.score(X, Y)
print(log_score)
print('係数 = {:}'.format(log_model.coef_[0]))

# 実際の目的変数Y の平均値. np.array 型なので, 
print(Y.mean())
print('不倫していない確率は= {:0.2f}'.format(1 - Y.mean()))

# どの変数が予測に寄与しているか
# 変数名と係数を格納するDFを作る
# 縦にarray を展開したいので，(.T)で転地する
coeff_df = DataFrame([X.columns, log_model.coef_[0]]).T
print(coeff_df)

# 正だと下がる，負だと上がる



# Part 8: 学習とテスト
# trian_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y)

# 新しいモデルを作る
log_model2 = LogisticRegression()

# 学習用のデータでモデルをトレーニングする
log_model2.fit(X_train, Y_train)

# テスト用データで，予測する
class_predict = log_model2.predict(X_test)

# 精度
print("精度は")
print(metrics.accuracy_score(Y_test, class_predict))

# plot_decision_regions(X_tarin, Y_train, classifier = log_model2, test_idx = range(105, 150))

plt.show()
