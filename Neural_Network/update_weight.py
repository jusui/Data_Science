# coding: utf-8
import numpy as np

"""
単層の重み更新


入力層：　x = [2, 3, 4, 5]

・重み：　　w = [0.4, -0.4, 0.3, 0.2]

・活性化関数：　シグモイド関数（ f(h) = 1/(1+ exp(-h))

・出力層：　y = 0.4

から構成される単層ニューラルネットワークの重みを1回更新し、


・誤差

・推定値

・更新された重みの値

を出力するコードをPythonで書いてみましょう。

学習率は、0.5とします。

"""

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_der(x):
    return (1 - sigmoid(x)) * sigmoid(x)


if __name__ == '__main__':
    x = np.array([2, 3, 4, 5])
    w = np.array([0.4, -0.4, 0.3, 0.2])
    y = np.array(0.4)
    # η: 学習率
    eta = 0.5

    h = np.dot(w, x)
    y_hat = sigmoid(h)
    error = y - y_hat

    # δ: 誤差項(Error term)
    error_term = error * sigmoid_der(h)
    del_w = eta * error_term * x
    print('Output:')
    print(h)

    print("Error:")
    print(error)

    print("delta_w:")
    print(del_w)

    print("weight = ", w)

    print("w + del_w = ", w + del_w)
    
