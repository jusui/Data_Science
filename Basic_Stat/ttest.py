# coding: utf-8
import numpy as np
from scipy import stats

"""
[Udemy]Data Science with Python
[t検定とp値]

"""
# A/Bテストを行う，顧客の注文量をA, Bのランダムなデータで試す. (A < B)
A = np.random.normal(25.0, 5.0, 10000)
B = np.random.normal(26.0, 5.0, 10000)
print(stats.ttest_ind(A, B)) # Ttest_indResult(statistic=-15.506664664123765, pvalue=6.4438705478132582e-54)


"""
統計量tはデータセットの各値の差の標準偏差及び，差の分散を用いる.
絶対値が大きなtの値は，2つのデータセットに実際に違いがあることを意味する．(有意な差がある)
p値はAとBが帰無仮説を満たす確率．小さいほど，有意であることを意味する．
=>統計的な有意を示すには，大きな統計量tと小さなp値が必要．
Academia では，p値をより重視する傾向.
"""
B = np.random.normal(25.0, 5.0, 10000)
print(stats.ttest_ind(A, B)) # Ttest_indResult(statistic=-0.41615667284553737, pvalue=0.67729982782387621)


""" 
統計量tがとても小さく，p値はとても大きい=>帰無仮説を満たす可能性が高い．=> 実際に違いはないと判断 
sample sizeを10倍に設定

"""
A = np.random.normal(25.0, 5.0, 100000)
B = np.random.normal(25.0, 5.0, 100000)
print(stats.ttest_ind(A, B)) # Ttest_indResult(statistic=0.54527223007361691, pvalue=0.58556690846506931)


"""
p値が少し小さく，統計量tは大きくなった．しかし，実際に大きな違いは見られない．
100万で試す

"""
A = np.random.normal(25.0, 5.0, 1000000)
B = np.random.normal(25.0, 5.0, 1000000)
print(stats.ttest_ind(A, B)) # Ttest_indResult(statistic=1.0657764856676188, pvalue=0.28652482156277109)


"""
同じデータセットで試す
A/A test

t検定とp値は，実際に違いが有るかどうかを判断する材料として重量
"""
print(stats.ttest_ind(A, A)) # Ttest_indResult(statistic=0.0, pvalue=1.0)
