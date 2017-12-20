# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt


def step_function(x):
    # (1). np.arangeで作った x は boolean 変換
    # (2). dtype = np.int で整数型(1, 0)に再変換
    return np.array(x > 0, dtype = np.int)

x = np.arange(-5.0, 5.0, 0.1)
print(x)
y = step_function(x)
print(y)

plt.plot(x, y,)
plt.ylim = (-0.1, 0.1)
plt.title("Step function")
plt.show()

