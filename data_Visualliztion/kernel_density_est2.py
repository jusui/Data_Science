import numpy as np
from numpy.random import randn
import pandas as pd

from scipy import stats

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
"""
3.1. カーネル密度推定とは？
ざっくりとした例で言うと、カーネル密度推定とは出口調査により選挙結果を予測することです。
"""

dataset = randn(100)
sns.kdeplot(dataset)
plt.figure()

sns.rugplot(dataset, color = 'black')
for bw in np.arange(0.5, 2, 0.25):
    sns.kdeplot(dataset, bw = bw, label = bw)

# plt.figure() することで, 一度一枚ごとに描画される
plt.figure()

kernel_options = ['biw', 'cos', 'epa', 'gau', 'tri', 'triw']
for kern in kernel_options:
    sns.kdeplot(dataset, kernel = kern, label = kern)

plt.figure()

sns.kdeplot(dataset, vertical = True)
plt.figure()

# Cumulative histgram
plt.hist(dataset, cumulative = True)
plt.figure()

sns.kdeplot(dataset, cumulative = True)
plt.figure()

# KDE:2-D normal dist
mean = [0,0]
cov = [[1,0], [0, 100]]
dataset2 = np.random.multivariate_normal(mean, cov, 1000)

dframe = pd.DataFrame(dataset2, columns = ['X', 'Y'])
# sns.kdeplot(dframe)は非推奨Warnningが出る
# sns.kdeplot(dframe)
sns.kdeplot(dframe.X, dframe.Y)
plt.figure()

sns.kdeplot(dframe.X, dframe.Y, shade = True)
plt.figure()

# bw = band width, estimation method == silverman
sns.kdeplot(dframe.X, dframe.Y, bw = 'silverman')
plt.figure()

sns.jointplot('X', 'Y', dframe, kind = 'kde')
plt.show()
# plt.legend()

