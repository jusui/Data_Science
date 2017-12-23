# coding: utf-8
import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
print(A)

print("np.ndim(A) =", np.ndim(A))
print("A.shape =", A.shape)
print("A.shape[0] =", A.shape[0])

print("")

B = np.array([[1, 2], [3, 4], [5, 6]])
print(B)

print("np.ndim(B) =", np.ndim(B))
print("B.shape =", B.shape)
print("B.shape[0] =", B.shape[0])

print("")

# np.dot()
AB = np.dot(A, B)
print("AB =", AB)

print("")

"""
行列で出力値の計算
"""
x = np.array([0.6, -0.4])
w = np.array([0.2, 0.8])
theta = -0.2

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

input = np.dot(x, w) + theta
print("input =", input)

output = sigmoid(input)
print("output =", output)
