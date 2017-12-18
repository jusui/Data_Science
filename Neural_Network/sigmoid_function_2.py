# coding: UTF-8

import matplotlib.pyplot as plt
import numpy as np
import math

def sigmoid(a):
    s = 1 / (1 + e**(-a))
    return s

# napier # : e 
e = math.e
dx = 0.1
x = np.arange(-8, 8, dx)

# sigmoid function: y = 1 / ( 1 + e**(-x))
y_sig = sigmoid(x)
print(x)

# sigmoid関数の傾き: dx 変化した時の y の値
y_dsig = (sigmoid(x + dx) - sigmoid(x)) / dx

plt.plot(x, y_sig, label = "sigmoid")
plt.plot(x, y_dsig, label = "d_sigmoid")
plt.legend()

plt.show()

