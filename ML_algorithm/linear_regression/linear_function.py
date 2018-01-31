import matplotlib.pyplot as plt
import numpy as np

# x = np.arange(0 , 10, 0.1)
x = np.arange(-5, 15, 0.1)
print(x)

y = 2 * x + 1
print(y)

plt.plot(x, y)
plt.figure()

"""
Lec.44
various function

"""
# 2次関数
y_2 = x**2 - 10 * x + 10
plt.plot(x, y_2)
# plt.figure()

# 3次関数
y_3 = x**3 - 10 * x**2 - 10 * x + 10
plt.plot(x, y_3)
plt.figure()

"""
Lec.45
exponential functions

"""
x_2 = np.arange(-5, 5, 0.1)

y_22 = 2**x_2
print(x_2)
print(y_22)

y_3 = 3**x_2
plt.plot(x_2, y_22)
plt.plot(x_2, y_3)
plt.figure()


"""
Lec.46
Napier constant

"""
import math

e = math.e
print(e)

dx = 0.1
x_22 = np.arange(-5, 5, dx)
print(x_22)
print(x_22.shape)

y_4 = 2**x_22
y_e = e**x_22
y_33 = 3**x_22

# xの傾きがdxの場合
y_de = (e**(x_22 + dx) - e**x_22) / dx
print(y_de.shape)

plt.plot(x_22, y_e)
plt.plot(x_22, y_de)

plt.show()
