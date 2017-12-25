# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pylab import *

"""
Random seeds

"""
np.random.seed(2)

pageSpeeds = np.random.normal(3.0, 1.0, 100)
# print(pageSpeeds.shape)
# print("pageSpeeds =", pageSpeeds[:])
purchaseAmount = np.random.normal(50.0, 30.0, 100) / pageSpeeds
# print(purchaseAmount.shape)
# print("purchaseAmount =", purchaseAmount)

# plt.scatter(pageSpeeds, purchaseAmount)
# plt.title("page vs. purchase")

# Split data into train[:80], test[:20] to avoid overfitting
trainX = pageSpeeds[:80]
testX = pageSpeeds[80:]
trainY = purchaseAmount[:80]
testY = purchaseAmount[80:]
# print(trainX)
# print(testX)
# print(trainY)
# print(testY)

scatter(trainX, trainY)
plt.title("trainX vs. trainY")
plt.figure()

scatter(testX, testY)
plt.title("testX, testY")
plt.figure()

""" 
train dataに，8次の多項式回帰を用いる-> overfitting

"""
x = np.array(trainX)
y = np.array(trainY)
print(x)
print(y)

# n-d polynomial function()
n = 8
p4 = np.poly1d(np.polyfit(x, y, n))

xp = np.linspace(0, n-1, 100)
axes = plt.axes()
axes.set_xlim([0, n-1])
axes.set_ylim([0, 200])
plt.scatter(x, y)
plt.plot(xp, p4(xp), c = 'r')
plt.figure()

# 同様にテストデータに7次poly1d fitting
testx = np.array(testX)
testy = np.array(testY)

axes = plt.axes()
axes.set_xlim([0, n-1])
axes.set_ylim([0, 200])
plt.scatter(testx, testy)
plt.plot(xp, p4(xp), c = 'r')

# R**2でfitting見てみる
from sklearn.metrics import r2_score

r2_train = r2_score(y, p4(x))
print("r2_train =", r2_train)

r2_test = r2_score(testy, p4(testx))
print("r2_test =", r2_test)

plt.show()
