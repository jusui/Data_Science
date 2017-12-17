import numpy as np
import matplotlib.pyplot as plt
import math


e = math.e
print(e)

dx = 0.1
x = np.arange(-5, 5, dx)
print(x)

y_2 = 2**x
y_e = e**x
y_3 = 3**x

# xの傾きがdxの場合
y_de = (e**(x+dx) - e**x) / dx

plt.plot(x, y_e)
plt.plot(x, y_de)

plt.show()

# レスlt関数が重なる.
# Natier数を用いた指数関数は，それの傾きとほぼ一緒になる
