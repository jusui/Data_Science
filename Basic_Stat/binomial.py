#coding: utf-8

"""
功する確率がp、失敗する確率がq(=1−p)の実験を、同じ条件で独立に繰り返すことをベルヌーイ試行(Bernoulli trial)とよび、 表が出る確率がpのコインを何度も投げる実験がベルヌーイ試行に対応します。

http://lang.sist.chukyo-u.ac.jp/classes/PythonProbStat/Intro2ProbDistri.html
"""

import matplotlib.pyplot as plt

def factorial(n):
    if ( n == 0 or n == 1 ):
        return 1
    else:
        return n*factorial(n-1)


def combination(n, x):
    ans = 1
    for i in range(x):
        print("i =", i)
        ans *= (n-i)
        print("ans =", ans)
    return ans / factorial(x)


def binomial(n, p, x):
    return ( combination(n, x) * p**x * (1-p)**(n-x) )


if __name__ == '__main__':
    print(factorial(5))
    print(combination(4, 2))
    #    print([combination(8, i) for i in range(8)])

    x = range(11)
    n = 10
    prob = [0.1, 0.5, 0.9]
    plt.subplots_adjust(left = 0.1, bottom = None, right = 1.5, top = None, \
                        wspace = None, hspace = 1.0)

    for i in range(1, 4):
        plt.subplot(3, 3, i)
        p = prob[i - 1]
        y = [binomial(n, p, u) for u in x]
        plt.bar(range(11), y)
        plt.axis([0.0, 11.0, 0.0, 0.5])
        plt.grid()
        plt.xlabel('x')
        plt.title('Bi(%d, %0.1f)'%(n, p))

    plt.show()


