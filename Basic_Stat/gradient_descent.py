# coding: utf-8
from collections import Counter
from linear_algebra.linear_algebra import *
from functools import reduce, partial
import math, random
import matplotlib.pyplot as plt

"""
[DS from scratch]
chap.8
Gradient Descent
勾配降下法

"""

def square(x):
    return x * x

def derivative(x):
    return x * 2

def sum_of_squares(v):
    """ computes the sum of squared elements in v """
    return sum(v_i ** 2 for v_i in v)


# [8.2]勾配の評価
def difference_quotient(f, x, h):
    return (f(x + h) - f(x))  / h

def partial_difference_quotient(f, v, i, h):
    """ 関数fと変数ベクトルvに対するi番目の差分商を計算 """
    w = [v_j + (h if j == i else 0)  # vのi番目の要素にhを追加
         for j, v_j in enumerate(v)]

    return (f(w) - f(v)) / h

def estimate_gradient(f, v, h = 0.00001):
    """ 勾配を計算 """
    return [partial_difference_quotient(f, v, i, h)
            for i, _ in enumerate(v)]


# [8.3]勾配を利用する
def step(v, direction, step_size):
    """ v からdirection方向にstep_size移動する """
    return [v_i + step_size * direction_i
            for v_i, direction_i in zip(v, direction)]

def sum_of_squares_gradient(t):
    return [2 * v_i for v_i in v]


# [8.4]最善の移動量を選択する
""" (1)固定の移動量とする (2)時間とともに縮小させる (3)各移動時に目的関数が最小と成るよう移動量を決める """
def safe_f(*args, **kwargs):
    """ fと等価だが，無効な入力に対する振る舞いとして無限大を返すような新しい関数を返す """
    try:
        return f(*args, **kwargs)
    except:
        return float('inf') # 'inf' =  infinity

    return safe_f

# [8.5]




if __name__ == '__main__':
    # [8.2]
    derivative_estimate = partial(difference_quotient, square, h = 0.00001)
    # derivative_estimate = lambda x: difference_quotient(square, x, h = 0.00001) # map(derivative, x)
    
    x = range(-10, 10)
    plt.title("Actual Derivatives vs. Estiamtes")
    plt.plot(x, list(map(derivative, x)), 'rx', label = 'Actual')  # 赤のx
    plt.plot(x, list(map(derivative_estimate, x)), 'b+', label = 'Estimate') # 青の+
    plt.legend(loc = 9)
   

    # [8.3]
    # 開始点を無作為に選択
    v =[random.randint(-10, 10) for i in range(3)]
    tolerance = 0.0000001

    while True:
        gradient = sum_of_squares_gradient(v)        # vにおける勾配を計算
        next_v   = step(v, gradient, -0.01)  # 勾配の負数分移動
        if distance(next_v, v) < tolerance:  # 収束すれば終わり
            break
        v = next_v # それ以外は継続

    print("minimum v", v)
    print("minimum value", sum_of_squares(v))
    print()
        
        

    plt.show()
