# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

""" 
random # in normal dist 
# https://pythondatascience.plavox.info/numpy/%E4%B9%B1%E6%95%B0%E3%82%92%E7%94%9F%E6%88%90

"""
# 平均:50, 標準偏差:10 の正規分布に従う乱数を 100 件出力
# np.random.normal(50, 10, 100)
incomes = np.random.normal(100.0, 10.0, 10000)

print("std =", incomes.std())
print("var =", incomes.var())
# print("std =", np.std(incomes))
# print("var =", np.var(incomes))

plt.hist(incomes, 50)
plt.show()
