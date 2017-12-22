# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

x = np.arange(-3, 3, 0.001)

# norm.pdf(x, mean, std)
plt.plot(x, norm.pdf(x))
plt.plot(x, norm.pdf(x, 1.0, 0.5))
plt.savefig('/Users/usui/work/python/Machine_Learning/Basic_Stat/norm_pdf.png', format = 'png')
plt.figure()

# 軸の調整
axes = plt.axes()
axes.set_xlim([-5, 5])
axes.set_ylim([0, 1.0])
axes.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
axes.grid() # Grid
plt.xlabel("Greebles")
plt.ylabel("Probability")
plt.plot(x, norm.pdf(x), 'b-') # b:blea, -:line
plt.plot(x, norm.pdf(x, 1, 0.5), 'r:') # r:red, ":" : dashed
plt.legend(['Shhetches', 'Gacks'], loc = 4)
plt.figure()


# XKCD style
# アメコミっぽいスタイル
# plt.xkcd() 使う

# Pie chart
plt.rcdefaults()
values = [12, 55, 4, 32, 14]
colors = ['r', 'g', 'b', 'c', 'm']
explode = [0, 0, 0.2, 0, 0] # 隙間
labels = ['India', 'US', 'Russia', 'China', 'Europe']
plt.pie(values, colors = colors, labels = labels, explode = explode)
plt.title("student locations")
plt.figure()


# Bar chart
values = [12, 55, 4, 32, 14]
colors = ['r', 'g', 'b', 'c', 'm']
plt.bar(range(0, 5), values, color = colors)
plt.figure()


# Random #
from pylab import randn
X = randn(500)
Y = randn(500)
plt.scatter(X, Y)
plt.figure()

# Histogram
incomes = np.random.normal(27000, 10000, 10000)
plt.hist(incomes, 50)
plt.figure()

# 箱ひげ図
uniformSkewed = np.random.rand(100) * 100 - 40
high_outliers = np.random.rand(10) * 50 + 100
low_outliers  = np.random.rand(10) * (-50) -100
data = np.concatenate((uniformSkewed, high_outliers, low_outliers))
plt.boxplot(data)

plt.show()

 
