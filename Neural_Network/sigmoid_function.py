# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
import math

def sigmoid_function(x):
    return 1 / (1 + np.exp(-x))

def sigmoid(a):
    s = 1/ (1 + e** (-a))
    return s

# napier number e
e = math.e
dx = 0.1
x = np.arange(-8, 8, dx)
y = sigmoid_function(x)

# y = 1 / (1 + e^(-x))
y_sig = 1 / (1 + e**(-x))

plt.plot(x, y)
plt.ylim = (-0.1, 0.1)
plt.title("Sigmoid function")
plt.figure()

plt.plot(x, y_sig)
plt.figure()

# 同様に関数で呼び出す
plt.plot(sigmoid(x))

plt.show()
