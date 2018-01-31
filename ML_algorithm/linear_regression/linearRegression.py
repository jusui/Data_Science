# coding: utf-8
import numpy
import matplotlib.pyplot as plt
from pylab import *

# data, normal(mean, std, data)
pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = 100 - (pageSpeeds + np.random.normal(0, 0.1, 1000)) * 3 # std = 0.1

# plt.scatter(pageSpeeds, purchaseAmount)

from scipy import stats
slope, intercept, r_value, p_value, std_err = stats.linregress(pageSpeeds, purchaseAmount)

# r_value square : (0 <= r <= 1), fitting具合
print("r_value(Fit具合) =", r_value**2)

# 傾き(a)と切片(b)でFit(y = ax + b)
def predict(x):
    return slope * x + intercept

fitLine = predict(pageSpeeds)

plt.scatter(pageSpeeds, purchaseAmount)
plt.plot(pageSpeeds, fitLine, c = 'r')

plt.show()


