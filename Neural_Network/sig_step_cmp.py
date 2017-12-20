# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt

"""

*両者の共通点は，出力信号を0 < f(x) < 1 に押し込めること.

"""

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def step(x):
    return np.array(x > 0, dtype = np.int)

x = np.arange(-5, 5, 0.1)
y_sig = sigmoid(x)
y_step = step(x)

plt.plot(x, y_sig)
plt.plot(x, y_step, 'k--')
plt.title("Compare Sigmoid vs. Step")
plt.ylim = (-0.1, 0.1)
plt.show()

