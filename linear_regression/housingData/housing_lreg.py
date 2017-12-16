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

""" Lect14 """
# 切片
print(model.intercept_)
# print('intercept_ = {:0.2f}'.format(model.intercept_))
# 傾きの係数
print(model.coef_)
# print('coef_ = {:0.2f}'.format(len(model.coef_)))

print("Room == 9 の場合")
print( (model.intercept_ * 9) + model.coef_ )

# plot model
plt.scatter(x_value, y_value, c = 'blue')

# 回帰線
plt.plot(x_value, model.predict(x_value), c = 'red')

# コスメ
plt.xlabel('average room #')
plt.ylabel("Price[$1000's]")

plt.show()
