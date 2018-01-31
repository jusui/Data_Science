# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt

"""
多項式

(1).
np.polyfit(x, y, 次数)
1 なら，ax + bで近似

(2).
np.poly1d(np.polyfit(x, y, 1))
1次なら，a, bを元に関数を生成.

http://ailaby.com/least_square/#id1
https://docs.scipy.org/doc/numpy/reference/generated/numpy.polyfit.html

"""
np.random.seed(2)
pageSpeeds = np.random.normal(3.0, 1.0, 1000)
# print(pageSpeeds)
purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds
# print(purchaseAmount)

plt.scatter(pageSpeeds, purchaseAmount)
plt.title("scatter with np.random.normal()")
plt.figure()

# 多項式回帰
x = np.array(pageSpeeds)
y = np.array(purchaseAmount)

# 4-d 多項式
p4 = np.poly1d(np.polyfit(x, y, 4))
print(p4)

# 散布図とともに，ページ速度を0-7 の範囲で多項式を表示する
xp = np.linspace(0, 7, 100)
print(xp)

plt.scatter(x, y)
plt.plot(xp, p4(xp), c = 'r')
plt.title("Polynomial(4-d) function")


from sklearn.metrics import r2_score

r2 = r2_score(y, p4(x))
print("r2 =", r2)

plt.show()
