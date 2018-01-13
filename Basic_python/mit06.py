# coding: utf-8

"""
[MIT_DS:chap06]

"""

# 6.1
def isBigger(x, y):
    """
    xとyをint型とする
    x > y ならTrue
    それ以外はFalse
    """
    if x > y:
        return True
    else:
        return False


def sqrt(x, epsilon):
    """
    x, epsilon
    if (x >= 0) and (epsilon > 0):
    
    return x - epsilon <= result * result <= x + epsilon
    """

def copy(L1, L2):
    """ 
    L1, L2 is list.
    L2をL1のコピーに更新する
    """
    while len(L2) > 0:
        L2.pop()
    for e in L1:
        L2.append(e)


def isPrime(x):
    """ 
    int x > 0.
    if x is prime true, else false.
    """
    if x <= 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False

    return True


def abs(x):
    """
    int x.
    if x >= 0 return x
    else -x
    """
    if x < -1:
        return -x
    else:
        return x

"""
[6.2.2]
"狂気とは，同じことを繰り返し，異なる結果を予期することである"
A.Einstein

"""

def isPal(x):
    """
    list x.
    回文ならTrue, それ以外はFalse
    """
    temp = x[:] # xのコピーを作る
    temp.reverse()
    if temp == x:
        return True
    else:
        False


def silly(n):
    """
    int n (n>0).
    input n words.
    n == 回文 Yes, それ以外は No.
    """
    result = []
    for i in range(n):
        elem = input('Enter element: ')
        result.append(elem)

    print("result =", result)
    if isPal(result):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    print(abs(2))
    print(abs(-1))
    silly(2)
