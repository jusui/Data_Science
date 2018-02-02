# coding: utf-8
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

"""
カイ二乗 (カイ自乗、χ2)分布 (chi-square distribution)

ポアソン分布は単位時間中に平均λ回起こる事象が単位時間中にx回起こる確率を表す離散型確率分布でした。
対し、「単位時間中に平均λ回起こる事象がα回起こるまでの時間」xが従う確率分布がガンマ分布(gamma distribution)と呼ばれるものです。

整数nに対しα=n/2,λ=1/2とおいたガンマ分布Ga(α,λ)を自由度nのカイ二乗分布とよび、χ2(n)と表します。


http://lang.sist.chukyo-u.ac.jp/classes/PythonProbStat/Intro2ProbDistri.html
"""

fig, ax = plt.subplots(1, 1)
x = np.linspace(0, 10, 10000)
dof = [1, 2, 3, 6] # degree of freedom
linestyles = [':', '--', '-.', '-'] # dofに対応したラインスタイル

for df, ls in zip(dof, linestyles):
    ax.plot(x, stats.chi2.pdf(x, df), linestyle = ls, label = r'$df = %i$' % df)

plt.xlabel('$\chi^2$')
plt.ylabel(r'$f (\chi^2)$')
plt.title(r'$\chi^2\ \mathrm{Distribution}$')
plt.axis([-0.2, 10, -0.02, 1.0])
plt.legend()
plt.grid()
plt.show()

