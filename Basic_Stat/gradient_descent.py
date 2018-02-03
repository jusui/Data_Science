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
def safe(f):
    """ fと等価だが，無効な入力に対する振る舞いとして無限大を返すような新しい関数を返す """
    def safe_f(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            return float('inf') # 'inf' =  infinity

    return safe_f


# [8.5]1つにまとめる
def minimize_batch(target_fn, gradient_fn, theta_0, tolerance = 0.000001):
    """ 目的関数はtarget_fnを最小化するthetaを勾配降下法で求める """

    step_sizes = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.000001]

    theta = theta_0             # thetaに初期値を設定
    target_fn = safe(target_fn) # target_fnの安全版
    value = target_fn(theta)    # valueの値を最小化

    while True:
        gradient = gradient_fn(theta)
        next_thetas = [step(theta, gradient, -step_size)
                       for step_size in step_sizes]

        # 誤差関数を最小化する値を選択
        next_theta = min(next_thetas, key = target_fn)
        next_value = target_fn(next_theta)

        # 収束したら，修了
        if abs(value - next_value) < tolerance:
            return theta

        else:
            theta, value = next_theta, next_value

# 最大値を求める
def negate(f):
    """ input xにチアする-f(x)に相当する関数を返す """
    return lambda *args, **kwargs: -f(*args, **kwargs)

def negate_all(f):
    """ fが数値リストを返す場合のnegate関数 """
    return lambda *args, **kwargs: [-y for y in f(*args, **kwargs)]

def maximize_batch(target_fn, gradient_fn, theta_0, toelrance = 0.000001):
    return minimize_batch(negate(target_fn),
                          negat_all(gradient_fn),
                          theta_0, tolerance)


# [8.6]確率的勾配降下法
def in_random_order(data):
    """ データの要素を無作為な順番で返すジェネレータ """
    indexes = [i for i, _ in enumerate(data)] # indexのリストを作る
    random.shuffle(indexes)                   # 無作為に並び替える
    for i in indexes:                         # データをその順番に返す
        yield data[i]                         

def minimize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0 = 0.01):
    data = zip(x, y)                           
    theta = theta_0                            # 初期推定値
    alpha = alpha_0                            # 初期ステップ量
    min_theta, min_value = None, float("inf")  # 現時点の最小値
    interations_with_no_improvement = 0        

    # 100回繰り返しても改善しない場合は，ストップ
    while iterations_with_no_improvement < 100:
        valeu = sum( target_fn(x_i, y_i, theta) for x_i, y_i in data )

        if value < min_value:
            # new minimize value見つかれば記憶し，最初のステップ量に戻す
            min_theta, min_value = theta, value
            iterations_with_no_improvement = 0
            alpha = alpha_0

        else:
            # 改善が見られないため，ステップ量を小さくする
            iterations_with_no_improvement += 1
            alpha *= 0.9

        # 各データポイントに対して勾配ステップを適用する
        for x_i, y_i in in_random_order(data):
            gradient_i = gradient_fn(x_i, y_i, theta)
            theta = vector_subtract(theta, scalar_multiply(alpha, gradient_i))

    return min_theta


def maximize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0 = 0.01):
    return minimize_stochastic(negate(target_fn),
                               negate_all(gradient_fn),
                               y, y, theta_0, alpha_0)



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
        

    # [8.5-8.6]確率的勾配降下法
    print("using minimize_batch")

    v = [random.randint(-10, 10) for i in range(3)]

    v = minimize_batch(sum_of_squares, sum_of_squares_gradient, v)

    print("minimum v:", v)
    print("minimun value :", sum_of_squares(v))

    plt.show()
