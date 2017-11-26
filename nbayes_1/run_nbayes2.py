"""
NaiveBayes1 test runner

"""
import numpy as np
from nbayes2 import NaiveBayes1, NaiveBayes2

# load data with np.genfromtxt(frame, dtype = <type 'float'>, commnets = '#', delimiter = None)
data = np.genfromtxt('vote_filled.tsv', dtype = int)

# split data
X = data[:, :-1]
y = data[:, -1]

# learn model
clr = NaiveBayes1()
clr.fit(X, y)

# test model
predict_y = clr.predict(X[:10, :])

# print results
print("NaiveBayes1")
for i in range(10):
    print((i, y[i], predict_y[i]))
           
# Learn model
clr = NaiveBayes2()
clr.fit(X, y)

# test model
predict_y = clr.predict(X[:10, :])

# print results
print("NaiveBayes2")
for i in range(10):
    print(i, y[i], predict_y[i])

    
