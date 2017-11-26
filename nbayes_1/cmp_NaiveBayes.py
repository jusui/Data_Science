import numpy as np
from nbayes2 import *
import timeit

def cmp_NaiveBayse():
    data = np.genfromtxt('vote_filled.tsv', dtype = int)
    X = data[:, :-1]
    y = data[:, -1]

    clr1 = NaiveBayes1()
    clr2 = NaiveBayes2()

#    print(timeit.timeit(cmp_NaiveBayes))

if __name__ == '__main__':
    print(timeit.timeit(cmp_NaiveBayse))


    

