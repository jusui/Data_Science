#coding: utf-8

"""
功する確率がp、失敗する確率がq(=1−p)の実験を、同じ条件で独立に繰り返すことをベルヌーイ試行Bernoulli trial)とよび、 表が出る確率がpのコインを何度も投げる実験がベルヌーイ試行に対応します。

http://lang.sist.chukyo-u.ac.jp/classes/PythonProbStat/Intro2ProbDistri.html
"""

import matplotlib.pyplot as plt
import numpy as np
import numpy.random as random

def factorial(n):
    if ( n == 0 or n == 1 ):
        return 1
    else:
        return n*factorial(n-1)


def combination(n, x):
    ans = 1
    for i in range(x):
        # print("i =", i)
        ans *= (n-i)
        # print("ans =", ans)
    return ans / factorial(x)


def binomial(n, p, x):
    return ( combination(n, x) * p**x * (1-p)**(n-x) )


if __name__ == '__main__':
    print(factorial(5))
    print(combination(4, 2))
    #    print([combination(8, i) for i in range(8)])

    # 問題[1-2] Bernoulli trial(n=10, p=0.3)
    trial = np.array([random.binomial(10, 0.3) for _ in range(1000)])
    print("平均 :", trial.mean())
    print("分散 :", trial.var())

    # [1-3] サイコロ10回試行:奇数が8回出る確率，8回以上出る確率
    xi = 1/6
    odd = 1/2
    n = 10
    k = 8
    print("nCk =", combination(n, k))
    print("Bi(10, 1/2, 8) =", binomial(n, odd, k) * 100)
    

    x = range(11)
    n = 10 # default = 10
    prob = [0.1, 0.5, 0.9]
    # plt.subplots_adjust(left = 0.1, bottom = None, right = 1.5, top = None, wspace = None, hspace = 1.0)
    plt.subplots_adjust(wspace = None, hspace = 1.0) # hspace plot間のスペース

    for i in range(1, 4):
        plt.subplot(3, 1, i)
        p = prob[i - 1]
        y = [binomial(n, p, u) for u in x]
        plt.bar(range(11), y)
        plt.axis([0.0, 11.0, 0.0, 0.5])
        plt.grid()
        plt.xlabel('x')
        plt.title('Bi(%d, %0.1f)'%(n, p))

    plt.show()


