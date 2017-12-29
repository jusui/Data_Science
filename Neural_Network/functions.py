# coding: utf-8
import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_grad(x):
    return (1.0 - sigmoid(x)) * sigmoid(x)


def mean_squared_error(y, t):
    return 0.5 * np.sum((y - t) ** 2)
    

def softmax(x):
    if x.ndim == 2:
        x = x.T
        x = x - np.max(x, axis = 0)
        y = np.exp(x) / np.sum(np.exp(x), axis = 0)

        return y.T

    x = x - np.max(x) # overflow 対策
    return np.exp(x) / np.sum(np.exp(x))

"""

"""
def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    # 教師データがone-hot-vectorの場合，正解ラベルのindex に変換
    if t.size == y.size:
        t = t.argmax(axis = 1)

    # np.arange(batch_size) は，0から(batch_size-1)までの配列を生成. 
    # (e.f.) batch_size = [0,1,2,3,4], t = [2, 7, 0, 9, 4]
    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t])) / batch_size  # y[np.arange(batch_size), t] = [y[0, 2], y[1, 7], ...]


    

