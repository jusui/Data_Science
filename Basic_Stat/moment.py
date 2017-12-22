# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt

"""
Moment (一次~四次)
PDF(x) の形状定量化
物理学で言うところの，仕事に相当？ 
モーメントは，四次まで存在する
一次 = 平均
二次 = 分散
三次 = 歪度，分布の偏り(左右のロングテール)
四次 = 尖度，ピークの広がり(高いピークは，尖度が大きい)
"""

# np.random.normal(mean, std, data)
vals = np.random.normal(5, 0.5, 10000)

plt.hist(vals, bins = 50)
plt.title("Hist of gauss")

# mean
print("np.mean(vals) =", np.mean(vals))

# var
print("np.var(vals) =", np.var(vals))

# skew (歪度)
# 今回は，データを0を中心とした対称な分布に近いため，meanを変化させても歪度はほぼ0.
import scipy.stats as sp
print("sp.skew(歪度) =", sp.skew(vals)) 

# sp.kurtosis()
# ピークの鋭さを表す．多きほど鋭い．
print("sp.kurtosis(尖度) =", sp.kurtosis(vals))

plt.show()
