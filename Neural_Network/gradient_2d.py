# coding: utf-8
# [cf.] http://d.hatena.ne.jp/white_wheels/20100327/p3
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""
偏微分
"""
def numerical_diff(f, x):
    h = 1e-4
    return (f(x + h) - f(x - h)) / (2*h)


def function_tmp1(x0):
    return x0**2 + 4.0 ** 2.0
    

def function_tmp2(x1):
    return 3.0 ** 2.0 + x1 ** 2


"""
勾配

[np.zeros_like]
https://deepage.net/features/numpy-zeros.html
"""
def numerical_gradient(f, x):
    h = 1e-4 # 0.0001
    grad = np.zeros_like(x) # x と同様のshapeを持つ，0を要素とするndarrayを返す
#    print(grad) # [ 0.  0.]

    for idx in range(x.size):
        tmp_val = x[idx]
        # f(x+h) を計算
        x[idx] = float(tmp_val) + h
        fxh1 = f(x) # f(x+h)

        # f(x-h) を計算
        x[idx] = float(tmp_val) - h
        fxh2 = f(x) # f(x-h)

        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val # 値を元に戻す
    
    return grad

    

def numerical_gradient_batch(f, X):
    if X.ndim == 1:
        return numerical_gradient(f, X)
    else:
        grad = np.zeros_like(X)

        for idx, x in enumerate(X):
            grad[idx] = numerical_gradient(f, x)

        return grad
            

def function_2(x):
    if x.ndim == 1:
        return np.sum(x**2)
    #    return x[0] ** 2 + x[1] ** 2
    else:
        return np.sum(x**2, axis = 1)



def tangent_line(f, x):
    d = numerical_gradient_batch(f, x)
    print(d)
    y = f(x) - d*x
    return lambda t: d*t + y
    


if __name__ == '__main__':
    tmp1 = numerical_diff(function_tmp2, 3.0)
    print("tmp1 = ", tmp1)
    
    tmp2 = numerical_diff(function_tmp2, 4.0)
    print("tmp2 = ", tmp2)

    print("")

    num1 = numerical_gradient_batch(function_2, np.array([3.0, 4.0]))
    print("num1 = ", num1)

    num2 = numerical_gradient_batch(function_2, np.array([0.0, 2.0]))
    print("num2 = ", num2)

    num3 = numerical_gradient_batch(function_2, np.array([3.0, 0.0]))
    print("num3 = ", num3)
    
    print("")


    x0 = np.arange(-2, 2.5, 0.25)
    x1 = np.arange(-2, 2.5, 0.25)
    x, y = np.meshgrid(x0, x1)

    x = x.flatten()
    y = y.flatten()

    grad = numerical_gradient_batch(function_2, np.array([x, y]))


    plt.figure()
    plt.quiver(x, y, -grad[0], -grad[1], angles = "xy", color = "#666666") #, headwidth = 10, scale = 40, color = "#444444")
    plt.xlim([-2, 2])
    plt.ylim([-2, 2])    
    plt.xlabel('x0')
    plt.ylabel('x1')
    plt.grid()
    plt.legend()
    plt.draw()
    plt.show()
    
