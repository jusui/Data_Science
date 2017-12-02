import numpy as np
from numpy.random import randn
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

"""
Box plot
Violin plot
"""

data1 = randn(100)
# +2 : 平均が2ズレる
data2 = randn(100) + 2

sns.distplot(data1)
sns.distplot(data2)
plt.figure()

"""box plot"""
# 25 < box < 75 %
sns.boxplot(data = [data1, data2])
plt.figure()

# 外れ値を含む whis = 
sns.boxplot(data = [data1, data2], whis = np.inf)
plt.figure()

# ヨコに並べる, oriental
sns.boxplot(data = [data1, data2], orient = 'h')
plt.figure()

# 縦に並べる, oriental
sns.boxplot(data = [data1, data2], orient = 'v')
plt.figure()

"""
Violin plot はbox plotとKDE情報量を兼ね備える
"""
# Make stats.norm( mean, std ).rvs data
data1 = stats.norm(0,5).rvs(100)

# gamma function random
data2 = np.concatenate([stats.gamma(5).rvs(50) - 1, \
                        -1*stats.gamma(5).rvs(50)])

# box
sns.boxplot(data = [data1, data2], whis = np.inf)
plt.figure()

# violin
sns.violinplot(data = [data1, data2])
plt.figure()

# change band width = 0.01
sns.violinplot(data = data2, bw = 0.01)
plt.figure()

# like a rugplot
sns.violinplot(data = data1, inner = "stick")

plt.show()
