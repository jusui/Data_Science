# coding: utf-8
"""
[MIT_DS:chap09]計算複雑姓入門
"""
import random
import numpy as np

# 9.1
def f(i):
    """ int i >= 0 """
    answer = 1
    while i >= 1:
        answer *= i
        i -= 1
    return answer


def linearSearch(L, x):
    for e in L:
        if e == x:
            return True
    return False


def fact(n):
    """ 自然数n, return n!"""
    answer = 1
    while n > 1:
        answer *= 1
        n -= 1
    return answer


def squareRootExhaustive(x, epsilon):
    """ 総当りアルゴリズム
    float x, epsilon. epsilon < 1.  |y*y - x| < epsilon """
    step = epsilon ** 2
    ans = 0.0
    while abs(ans ** 2 - x) >= epsilon and ans*ans <= x:
        ans += step
    if ans*ans > x:
        raise ValueError
    return ans


def squareRootBi(x, epsilon):
    """ 2分法にようる平方根の近似値計算
    float x, epsilon. epsilon < 1.  |y*y - x| < epsilon """
    low = 0.0
    high = max(1.0, x)
    ans = (high + low) / 2.0
    while abs(ans**2 - x) >= epsilon:
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    return ans



if __name__ == '__main__':
    # L = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # LS = linearSearch(L, 3)
    # print(LS)
    
    F = fact(2)
    print(F)
