# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
from  matplotlib.font_manager import FontProperties
fp = FontProperties(fname=r'/Library/fonts/ipag.ttf', size=11)

def numerical_diff(f, x):
    h = 1e-4 # 0.0001
    return (f(x + h) - f(x - h)) / (2*h)


def function_1(x):
    return 0.01*x**2 + 0.1*x


def tangent_line(f, x):
    d = numerical_diff(f, x)
    print(d)
    y = f(x) - d*x
    # lambda x: y
    # x = 引数, y = 戻り値
    return lambda t: d*t + y


if __name__ == '__main__':
    x = np.arange(0.0, 20.0, 0.1)
    y = function_1(x)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("数値微分の例", fontproperties = fp)

    tf = tangent_line(function_1, 5)
    y2 = tf(x)

    plt.plot(x, y)
    plt.plot(x, y2)
    plt.show()

    
