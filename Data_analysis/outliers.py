# coding: utf-8

"""
外れ値の扱い

大富豪のデータで，収入分布のデータを作る
"""

import numpy as np

incomes = np.random.normal(27000, 15000, 10000)
incomes = np.append(incomes, [1000000000])

import matplotlib.pyplot as plt
plt.hist(incomes, 50)
plt.figure()

# mean of income
print("平均 :", incomes.mean())


def reject_outliers(data):
    median = np.median(data)
    std = np.std(data)
    filtered = [e for e in data if (median - 2 * std < e < median + 2 * std)]

    return filtered

filtered = reject_outliers(incomes)

plt.hist(filtered, 50)
print("mean :", np.mean(filtered))

plt.show()

