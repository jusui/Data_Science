import numpy as np
from nbayes2 import *
import timeit

# def cmp_NaiveBayes():
data = np.genfromtxt('vote_filled.tsv', dtype = int)
X = data[:, :-1]
y = data[:, -1]

clr1 = NaiveBayes1()
clr1.fit(X, y)
print(clr1.fit(X, y))

clr2 = NaiveBayes2()
clr2.fit(X, y)
print(clr2.fit(X, y))

# if __name__ == '__main__':

## timeit setups ( 100 hundred exe)
print(timeit.timeit("print('ie-i')", setup="print('Start timeit')", number = 100))
print("NaiveBayes1 = ", timeit.timeit(NaiveBayes1))
print("NaiveBayes2 = ", timeit.timeit(NaiveBayes2))
# print(timeit.timeit(clr1.fit(X, y)))
# print(timeit.timeit(clr2.fit(X, y)))
