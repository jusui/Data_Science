# encoding = utf-8
import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import seaborn as sns

# numpy.arrayに似た Seriesをつくる.  違いは，データにラベルがあるところ
obj = Series([3, 6, 9, 12])
print(obj)
# values で値を返す
print(obj.values)

# indexつきデータをつくる
# Death of WW2.
ww2_cas = Series( [8700000,4300000,3000000,2100000,400000], index=['USSR','Germany','China','Japan','USA'] )
print(ww2_cas)

# 文字列のindex でアクセス
print(ww2_cas['USA'])

# 4 million 以上の死傷者を出した国
print(ww2_cas[ww2_cas >= 4000000])

# hist
plt.hist(ww2_cas, alpha = 0.5, bins = 20)
plt.figure()

# pandasのSeriesを描画
sns.distplot(ww2_cas, bins = 25)

# Use like a dictionary
print('USSR' in ww2_cas)

# 辞書型に変換
ww2_dict = ww2_cas.to_dict()
print(ww2_dict)

# 辞書をもとに，Seriesをつくる
WW2_Series = Series(ww2_dict)
print(WW2_Series)

# index を明示的に与える
countries = ['China', 'Germany', 'Japan', 'USA', 'USSR', 'Argentina']
# 別のSeriesをつくる
obj2 = Series(ww2_dict, index = countries)
print(obj2)

# null dataを確認
pd.isnull(obj2)
print(pd.isnull(obj2))

# notnull data を確認
print('notnullを確認{}')
print(pd.notnull(obj2))

# Data + Data
print("data + data")
print(WW2_Series + obj2)

# Series に名前をつける
obj2.name = 'Death of WW2'
print(obj2)

# index に名前をつける
obj2.index.name = 'Countries'
print(obj2)

plt.show()
