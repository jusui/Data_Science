import numpy as np
from numpy.random import randn
import pandas as pd

from scipy import stats

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# なめらかなhistogramを作る
# kernel funciton でたしあわせる
dataset = randn(25)
sns.rugplot(dataset)

# alpha = 透明率
plt.hist(dataset, alpha = 0.3)
sns.rugplot(dataset)

# Bandwidth selection
# 正規分布の幅を統制
sns.rugplot(dataset)


# Let's make a kernel density function
# max, minを100当分したhist
x_min = dataset.min() - 2
x_max = dataset.max() + 2
x_axis = np.linspace(x_min, x_max, 100)

bandwidth = ((4*dataset.std()**5) / (3*len(dataset)))**0.2

kernel_list = []
for data_point in dataset:
    # norm(平均値, bandwidth)
    kernel = stats.norm(data_point, bandwidth).pdf(x_axis)
    # save into list
    kernel_list.append(kernel)


    kernel = kernel / kernel.max()
    kernel = kernel* 0.4

    plt.plot(x_axis, kernel, color = 'gray', alpha = 0.5)

plt.ylim(0, 1)

sum_of_kde = np.sum(kernel_list, axis= 0)
fig = plt.plot(x_axis, sum_of_kde, color = 'indianred')
sns.rugplot(dataset)
# y-axis消す
plt.yticks([])
plt.suptitle('Sum of the Basis Functions')
plt.show()

dataset2 = randn(25)
sns.kdeplot(dataset2)

plt.show()
