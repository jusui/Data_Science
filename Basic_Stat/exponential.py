#coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
"""
指数分布(Exponential distribution)
指数分布とは、単位時間に平均λ回起こる事象が初めて起こるまでの時間xが従う確率分布です。 指数分布は Exp(λ)で表され、その確率密度関数f(x)は次式で与えられる： 

f(x) = lam * np.exp(-lam*x), (0 <= x, lam > 0)
f(x) = 0, (x < 0)
"""

def Exp(lam, x):
    if ( x >= 0 ) and (lam > 0):
        return lam * np.exp(-lam * x)
    return 0

# make a vector x in [0, ..., 6.0]
x = np.linspace(0, 6.0, 1000)
# lambda のパターンリスト
lst = [0.5, 1, 3, 5, 10]

for i in range(5):
    l = lst[i]

    y = [Exp(l, i) for i in x]
    plt.plot(x, y, label = '$\lambda=%0.2f$'%(l))
    plt.legend()

plt.axis([-0.2, 6.0, -0.2, 5.0])
plt.grid()
plt.xlabel('x')

plt.show()
    
