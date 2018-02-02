# coding: utf-8
from scipy.stats import f
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

"""
F 分布(F-distribution)
自由度がmとnのカイ二乗分布に従う２つの独立な確率変数XとYに対し、その比
x=X/mY/n
が従う確率分布をF分布とよび、F(m,n)で表します。自然数m,nに対するF分布F(m,n)の確率密度関数は次式で与えられます

f(x) = (1/B(m/2, n/2)) * (mx / (mx+n))**m/2 * (n/(mx+n))**(n/2) * x**(-1)
(x >= 0)

http://lang.sist.chukyo-u.ac.jp/classes/PythonProbStat/Intro2ProbDistri.html
"""

fig, ax = plt.subplots(1, 1)
x = np.linspace(0, 6, 10000)
dof = [(1,1), (2,2), (6,8), (10,10)]
linestyles = [':', '--', '-.', '-']

for (m, n), ls in zip(dof, linestyles):
    ax.plot(x, f.pdf(x, m, n), linestyle = ls, label = r'$m=%i, n=%i$' % (m, n))

plt.xlabel('$x$')
plt.ylabel(r'$f(x)$')
plt.title(r'F-Distribution')
plt.axis([-0.02, 6, -0.02, 1.2])
plt.legend()
plt.grid()

plt.show()

