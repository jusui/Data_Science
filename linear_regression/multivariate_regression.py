# coding: utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
多変量回帰

中古車の属性と価格の関係

pd.Categorical()
http://sinhrks.hatenablog.com/entry/2015/07/11/223124
"""
df = pd.read_excel('http://cdn.sundog-soft.com/Udemy/DataScience/cars.xls')

import statsmodels.api as sm

# カテゴリカル変数['Model'] を pd.Cotegorical().codes で ダミーデータ['Model_ord']  に変形して追加
# codes が文字列を適当な数字に変換してくれるっぽい
df['Model_ord'] = pd.Categorical(df.Model).codes
print(df.head())

# def X, y
X = df[['Mileage', 'Model_ord', 'Doors']]
y = df[['Price']]

# statsmodels.
# http://www.statsmodels.org/devel/glm.html
X1 = sm.add_constant(X)
print("X1")
print(X1)

"""
回帰実行
"""
# OLS (ordinary least square; 普通の最小二乗法)
# https://qiita.com/yubais/items/24f49df99b487fdc374d
model = sm.OLS(y, X1)
results = model.fit()

print(results.summary())

# パラメータの推定値を取得
print("")
print("results.params")
print("")
print(results.params)

# mean
doors = y.groupby(df.Doors).mean()
print(doors)


## plot
plt.scatter(X1['Mileage'], y, c = 'b')
plt.show()
