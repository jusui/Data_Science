"""
NativeBayes1 test runner

"""
import numpy as np
from nbayes1 import NativeBayes1

# load data with np.genfromtxt(frame, dtype = <type 'float'>, commnets = '#', delimiter = None)
data = np.genfromtxt('vote_filled.tsv', dtype = int)

# split data
X = data[:, :-1]
y = data[:, -1]


# learn model
clr = NativeBayes1()
clr.fit(X, y)


# test model
predict_y = clr.predict(X[:10, :])

# print results
for i in range(10):
    print(i, y[i], predict_y[i])

    
