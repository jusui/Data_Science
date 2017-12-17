# encoding utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('housing.data', header = None, sep = '\s+')
print(df)

# columns 
df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'ptRATIO', 'B', 'LSTAT', 'MEDV']
print(df.head())

x_value = df[['RM']].values
y_value = df[['MEDV']].values
age = df[['AGE']].values
crim = df[['CRIM']].values

print("Average room # ")
print(x_value)
print("room = 9")
print(x_value[x_value > 8])
print("Median value of owner-occupied homes in $1000's")

# instance
import sklearn
from sklearn.linear_model import LinearRegression
model = LinearRegression()

# train model
model.fit(x_value, y_value)

# plot model
plt.scatter(x_value, y_value, c = 'blue')

# 回帰線
plt.plot(x_value, model.predict(x_value), c = 'red')

""" Lect14 : 2つの方法で試行 """
# ①線形関数から計算
print("傾きの係数")
print(model.coef_)
print("切片")
print(model.intercept_)
print("Room == 9 の場合")
print( 9 * (abs(model.coef_) ) + model.intercept_ )

# ②作成したモデルから計算
# https://www.udemy.com/neuralnet/learn/v4/questions/2665742
plt.plot(9, model.predict(9), 'ro')
print(model.predict(9))

# コスメ
plt.xlabel('average room #')
plt.ylabel("Price[$1000's]")
plt.figure()

plt.scatter(age, y_value, c = 'blue')
model.fit(age, y_value)
plt.plot(age, model.predict(age), c = 'red')
plt.xlabel('Age')
plt.ylabel("Price[$1000's]")
plt.figure()

# sns.heatmap(df, annot = True)
sns.lmplot("AGE", "MEDV", df, x_estimator = np.mean)

sns.clustermap(df)


plt.show()
