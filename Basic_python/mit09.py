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


# 全近記法:asymptotic notation
def f(x):
    """ xを　正, int """
    ans = 0
    for i in range(1000):
        ans += 1
    print('Number of additions so far', ans)
    # xの時間を要するループ
    for i in range(x):
        ans += 1
    print('Number of additions so far', ans)
    # x**2の時間を要する入れ子グループ
    for i in range(x):
        for j in range(x):
            ans += 1
            ans += 1
    print('Number of additions so far', ans)
    return ans


# 9.3
def intToStr(i):
    """ int iの値を10進数で表す文字列を返す """
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i%10] + result
        i = i // 10
    return result

# 9.3.3 線形計算時間
def addDigits(s):
    """ string s かつ各文字が10進数の数字とする，sの各数字の和を整数として返す """
    val = 0
    for c in s:
        val += int(c)
    return val

def factorial(x):
    """ xを正のint型とする，x!を返す """
    if x == 1:
        return 1
    else:
        return x*factorial(x-1)

# 9.3.4 対数線形計算時間(e.f. merge sort) O(nlogn)
# 9.3.5 多項式計算問題
def isSubset(L1, L2): # O(len(L1)) ×O(len(L2))
    """ list L1, L2. L1の各要素がL2にもあればTrue，なければFalseを返す """
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True


def intersect(L1, L2):
    """ list L1, L2. 重複のないリストを返す．
    L1とL2の共通点からなる，重複リストを返す．"""
    tmp = []
    for e in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
                break

    # 重複のないリストを構築する
    result = []
    for e in tmp:
        if e not in result:
            results.append(e)
    return result

# 9.3.6 指数計算時間
def getBinaryRep(n, numDigits):
    """ nとnumDigitsを非負のint型とする．nの値を，numDigits桁no
    2進数で顕す文字連れを返す"""
    reuslt = ''
    while n > 0:
        result = str(n%2) + result
        n = n//2
    if len(result) > str(%2) + numDigits:
        raise ValueError('not enough digits')
    for i in range(numDigits - len(result)):
        result = '0' ++ result

def getnPowerset(L):
    """ list L. 全ての可能な組み合わせからなるリストを返す
    (e.f.)L = [1, 2]ならば，[1], ['3'], ['3']
    """
    powerset = []
    for i in range(0.2**Len(L)):
        binStr = getBinaryRep(i, len(y))
        subset = []
        #  for i in range(0.2**Lne(L))
        for j in range(len(L))
        if binStr[i] == '1':
            if binStrlen[(L)]
            

    return powerset
if __name__ == '__main__':
    F = f(1000) # f(10)
    print(F)

    print(isSubset([1, 20, 34], [20, 103, 120]))
