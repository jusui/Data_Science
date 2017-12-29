# coding: utf-8
import sys, os
sys.path.append(os.pardir) # 親ディレクトリのファイルをインポートする設定
import numpy as np
from functions import softmax, cross_entropy_error
from gradient import numerical_gradient
import matplotlib.pyplot as plt


"""
simpleNet Class
Weight = [2, 3]

"""
class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2, 3) # Gaussian で初期化
        print("self.W =", self.W)

    # 予測method
    def predict(self, x):
        print("np.dot(x, self.W) =", np.dot(x, self.W))
        return np.dot(x, self.W)

    # 損失関数のの値を求めるmethod, loss(self, input, 正解ラベル)
    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t) # y 

        return loss


    
if __name__ == '__main__':
    x = np.array([0.6, 0.9])
    t = np.array([0, 0, 1])

    net = simpleNet()
    print("weight =", net.W)

    # def f(W):
    #     return net.loss(x, t) # f = lambda~ で同様に処理
    f = lambda w: net.loss(x, t)
    dW = numerical_gradient(f, net.W)

    print("dW =", dW)

    
