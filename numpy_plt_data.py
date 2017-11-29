#-*- encoding utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
# %matploblib inline

points = np.arange(-5, 5, 0.01)
print(points)

dx, dy = np.meshgrid(points, points)
print(dx)
print(dy)

plt.imshow(dx)
plt.imshow(dy)

z = (np.sin(dx)) + (np.sin(dy))
plt.imshow(z)
plt.colorbar()
plt.title('Plot for sin(x)+sin(y)')
# plt.show()

A = np.array([1,2,3,4])
B = np.array([1000, 2000, 3000, 4000])

condition = np.array([True, True, False, False])

# slow calc 
answer = [(a if cond else b) for a, b, cond in zip(A, B, condition)]
print(answer)

answer2 = np.where(condition, A, B)
print(answer2)

from numpy.random import randn
arr = randn(5,5)
print(arr)

arr_new = np.where(arr < 0, 0, arr)
print(arr_new)

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)

print(arr.sum())
print(arr.sum(0))
print(arr.mean())
print(arr.std())
print(arr.var())

bool_arr = np.array([True, False, True])
print(bool_arr)

print(bool_arr.any())
arr=randn(5)
print(arr)
arr.sort()
print(arr)

