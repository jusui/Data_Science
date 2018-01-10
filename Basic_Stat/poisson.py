# coding:utf-8
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
"""
Poisson dist
実装とライブラリの両方で試す.

"""
from math import exp
from math import factorial
def poisson(x, lamb):
    return (lamb**x) * exp(-lamb) / factorial(x)

from scipy.stats import poisson

if __name__ == '__main__':
    """
    [case1]マクドナルドにちょうど7人のお客さんが来店する確率はどれくらいか
    平均10人
    """
    x = 7
    lamb = 10
    print("7人の確率 =", poisson(x, lamb))
    
    """
    Scipyを使う
    """
    mu = 10
    # 平均と分散を計算
    mean, var = poisson.stats(mu)

    # pmf で特定の確率を計算
    odds_seven = poisson.pmf(7, mu)
    print("お客さんが7人である確率 = {:0.2f}%.".format(100 * odds_seven))
    print("平均 = {}".format(mean))

    # 30人のお客さんが来る確率, 理論的には無限大まで可能
    k = np.arange(30)

    # 平均
    lamb2 = 10
    
    pmf = poisson.pmf(k, lamb2)
    print("pmf =", pmf)
    plt.bar(k, pmf)
    plt.show()


    """
    10人より多くの客が来る確率 = 11人以降の確率を足し合わせる
    累積分布関数(CDF:Culumative Distribution Function)
    指定された値までの確率を足し合わせた確率を返す

    """
    k, mu = 10, 10

    prob_up_to_ten = poisson.cdf(k, mu)
    print('10人までの確率は, {:0.2f}%'.format(100*prob_up_to_ten))

    # 10人より，多く来る確率は(1 - prob_up_to_ten)
    prob_more_than_ten = 1 - prob_up_to_ten
    print('10人以上の確率, {:0.2f}%'.format(100 * prob_more_than_ten))
    

    """
    幾何分布(等比数列)
    風水害は，1年で確率0．04で起こる．
    次に起こる確率は何年後か、　また10年以内に起こる確率は？
    """
    p = 0.04
    E = 1 / p
    print("E(x) =", E)
    V = (1-p) / (p**2)
    std = np.sqrt(V)
    print("std =", std)
    print("次に起こる確率 =", E, "±",std)
    
    # 10年以内発生確率
    x = 10
    F = 1 - (1 - p)**x
    print("Prob(10年以内) = ", F)
