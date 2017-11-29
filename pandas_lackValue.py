import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy import nan
## nan = not a number

data = Series(['one', 'two', nan, 'four'])
print(data)

print(data.isnull())
data2 = data.dropna()
print(data2)

dframe = DataFrame([[1,2,3], [nan,5,6], [7, nan, 9], [nan, nan, nan]])
print(dframe)

dframe2 = dframe.dropna()
print(dframe2)

dframe3 = dframe.dropna(how='all')
print(dframe3)

dframe4 = dframe.dropna(axis = 1)
print(dframe4)

dframe22 = DataFrame([[1,2,3,nan], [2,nan,5,6],[nan, 7, nan, 9], [1, nan, nan, nan]])
print(dframe22)

## (thresh = 2 )欠損値が無い値が2以上あるか判定
dframe33 = dframe22.dropna(thresh = 2)
print(dframe33)

# 欠損値を値で補完
dframe44 = dframe22.fillna(1)
print(dframe44)

# 欠損値の埋めるデータを指定
dframe55 = dframe22.fillna({0:0, 1:1, 2:2, 3:3})
print(dframe55)

dframe66 = dframe22.fillna(0, inplace = True)
print(dframe66)







