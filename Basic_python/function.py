#coding: utf-8
from mit04 import *

def func1():
    print("World!")

# func1()

def func2():
    print("Hello")
    func1()

func2()

"""
[MIT DS]
chap 5.4　Objectとしての関数

"""
def applyToEach(L, f):
    """
    list as L, function as f.
    Lのそれぞれの要素eをf(e)に置き換えてLを更新
    """
    for  i in range(len(L)):
        L[i] = f(L[i])


if __name__ == '__main__':
    L = [1, -2, 3.33]
    print('L =', L)

    print('Apply abs to each element of L.')
    applyToEach(L, abs)
    print('L =', L)    

    print('Apply int to each element of L.')
    applyToEach(L, int)
    print('L =', L)    

    print('Apply factorial to each element of L.')
    applyToEach(L, factR)
    print('L =', L)    

    print('Apply Fibonnaci to each element of L.')
    applyToEach(L, fib)
    print('L =', L)    
