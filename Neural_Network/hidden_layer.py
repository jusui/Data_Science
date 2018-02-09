# coding: utf-8
import numpy as np
num_input = 4
num_hidden = 3
num_output = 2

np.random.seed(45)
X = np.random.randn(4) # 要素数が4のベクトル
print(X)

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

# scale:分散
w_in_h = np.random.normal(0, scale = 0.1, size = (num_input, num_hidden))
w_h_out = np.random.normal(0, scale = 0.1, size = (num_hidden, num_output))

h_in = np.dot(X, w_in_h)
h_out = sigmoid(h_in)
print(h_out)

out_in = np.dot(h_out, w_h_out)
out_out = sigmoid(out_in)
print(out_out)
