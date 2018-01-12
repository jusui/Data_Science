# coding: utf-8
import numpy as np
import pandas as pd
from scipy import stats

"""
観測値と期待値のズレを統計的に検討する方法
コインを投げて出目が妥当な値かどうかを判定
自由度kが大きくなると、分布がなだらかになる 
"""

### サイコロの出目が妥当かを判断してみる
# 観測値
observed = [8, 32, 48, 59, 67, 84, 76, 57, 34, 28, 7]
roll_sum = sum(observed)
print(roll_sum)

### expeceted 出目の分子 = freq
freq = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
possible_rolls = 1 / 36

freq = [possible_rolls * dice for dice in freq]
print(freq, '\n')

## 期待される出目の頻度(500回試行しているので * (500) する)
expected = [roll_sum * f for f in freq]
print(expected)

chisq, p = stats.chisquare(observed, expected)

# if p-value is too small -> its strange.
print('chisquare stats = {:0.2f}'.format(chisq))
print('P-value = {:0.2f}'.format(p))


"""
scipy.stats
https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2.html

"""
from scipy.stats import chi2
import matplotlib.pyplot as plt

# Degree of Freedom(df)
df = 55
mean, var, skew, kurt = chi2.stats(df, moments = 'mvsk')
print("mean =", mean)
print("var =", var)
print("skew =", skew)
print("kurt =", kurt)

# Percent point function (inverse of cdf — percentiles).
# 自由度1のカイ二乗分布で確率0.95となるχ2の値を求める
# これが棄却域を定める---この値よりもχ2値が大きければ棄却される
# カイ二乗分布は『上側』のみ
print("chi2.ppf(0.95, 1) =", chi2.ppf(0.95, 1))


# 自由度dfのchi2分布に従うpoint を100発生
x = np.linspace(chi2.ppf(0.01, df),
                chi2.ppf(0.99, df), 100)

print("x =", x)


# 見てみる
plt.plot(x, chi2.pdf(x, df))

# random number
rs = chi2.rvs(df, size = 1000000)
plt.hist(rs, bins = 100)

fig, ax = plt.subplots(1, 1)
ax.plot(x, chi2.pdf(x, df),
        'r-', lw = 5, alpha = 0.6, label = 'chi2 pdf')

rv = chi2(df)
ax.plot(x, rv.pdf(x), '-k', lw = 2, label = 'frozen pdf')


# check accuracy of cdf and ppf
vals = chi2.ppf([0.001, 0.5, 0.999], df)

# 2つのNdarrayが近い値かどうかを比べる
np.allclose([0.001, 0.5, 0.999], chi2.cdf(vals, df))

# generate random numbers
r = chi2.rvs(df, size = 1000)

# and compare the histogram
ax.hist(r, normed = True, histtype = 'stepfilled', alpha = 0.2)
ax.legend(loc = 'best', frameon = False)
plt.figure()

plt.show()

