# coding: utf-8
import matplotlib.pyplot as plt

from scipy.stats import t
import numpy as np

"""
t分布
標準正規分布N(0,12)に従う確率変数Xと、自由度dのカイ二乗分布に従う確率変数Yとの比
T = X / (math.sqrt(Y / d))
が従う確率分布を(スチューデントの)t分布とよびt(d)で表します。

t分布の確率密度関数は次式で与えられます:
f(x) = (1/sqrt(d*pi)) * (gamma(d+1/2) / gamma(d/2)) * (1 + x**2 / d)**(-(d+1)/2)
(-inf < x < inf)

"""

# t_dist : Nが大きくなるとgaussianに漸近していく
# set X-axis
x = np.linspace(-5, 5, 100)

# DOF = 3, t-dist
rv = t(3)
plt.plot(x, rv.pdf(x))


"""
[ref]
http://lang.sist.chukyo-u.ac.jp/classes/PythonProbStat/Intro2ProbDistri.html
"""
fig, ax = plt.subplots(1, 1)
x2 = np.linspace(-6, 6)
linestyles = [':', '--', '-.']
dof = [1, 3, 100]

for df, ls in zip(dof, linestyles):
    ax.plot(x2, t.pdf(x2, df), linestyle = ls, label = r'$df=%i$' % df)

plt.xlabel(r'$t$')
plt.ylabel(r't-Distribution')
plt.axis([-6, 6, -0.02, 0.6])
plt.legend()
plt.grid()

plt.show()

