import numpy as np
from numpy.random import randn

from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

"""
Regression plot
seaborn.lmplot() を利用する
seaborn は、matplotlib の上に構築されている
lmplot() は、plt.figure() しなくても、別のウィンドウに描画される

"""

# data DL
tips = sns.load_dataset('tips')
# print(tips, 5)

### lmplot : linear regression plot
# x : total_bill , y : tip
sns.lmplot('total_bill', 'tip', tips)
# plt.figure()

sns.lmplot('total_bill', 'tip', tips,
           scatter_kws = {'marker':'o', 'color':'indianred'}, \
           line_kws = {'linewidth':1, 'color':'blue'})
# plt.figure()


sns.lmplot('total_bill', 'tip', tips, order = 4,
           scatter_kws = {'marker':'o', 'color':'indianred'}, \
           line_kws = {'linewidth':1, 'color':'blue'})
# plt.figure()

sns.lmplot('total_bill', 'tip', tips, fit_reg = False)

tips['tip_pect'] = 100 * (tips['tip'] / tips['total_bill'])
# print(tips)

### 今回のデータのポイントは、'size' のような離散的なデータに対しても分布にすることが可能である点
# 支払いで何％使ったか
sns.lmplot('size', 'tip_pect', tips)

## scatter plot に広がりを持たせて表示し、少し見やすくする
# jitter = 広がり
sns.lmplot('size', 'tip_pect', tips, x_jitter = 0.2)

## Error bar付きlmplot
sns.lmplot('size', 'tip_pect', tips, x_estimator = np.mean)

## 総額に対する%
# hue  = けいこう
sns.lmplot('total_bill', 'tip_pect', tips, hue = 'sex', markers = ['x', 'o'])

sns.lmplot('total_bill', 'tip_pect', tips, hue = 'day')

# 局所的にデータを見ながら、線形フィットするため、滑らかに見える
sns.lmplot('total_bill', 'tip_pect', tips, lowess = True, line_kws = {'color':'black'})

## regression plot
# 簡易にregression plot 見れる
sns.regplot('total_bill', 'tip', tips)


fig, (axis1, axis2) = plt.subplots(1, 2, sharey = True)
sns.regplot('total_bill', 'tip_pect', tips, ax = axis1)
sns.violinplot(y = "tip_pect", x = "size", data = tips.sort('size'), ax = axis2)

plt.show()

