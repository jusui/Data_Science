# coding: utf-8
import numpy as np

"""
y_k = exp(a_k) / sum(exp(a_i))

注意点: オーバーフロー問題. 指数関数の計算なので，計算量が用意に大きくなりうる．
対策として，入力信号から入力値の最大値を引いて，正しく計算し直す．
"""
a = np.array([0.3, 2.9, 4.0])
print(a)

exp_a = np.exp(a)
print("exp_a =", exp_a)

sum_exp_a = np.sum(exp_a)
print("sum_exp_a =", sum_exp_a)

y = exp_a / sum_exp_a
print("y =", y)

def softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

print("y =", softmax(a))


# Pointは，softmax()はなんらかの定数を足し引きしても結果が変わらない点にある．
def softmax_kai(a):
    c = np.max(a)
    exp_a = np.exp(a - c) # overflow 対策
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

print("y = ", softmax_kai(a))

