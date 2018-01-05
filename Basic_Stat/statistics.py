# coding: utf-8
from __future__ import division
from collections import Counter
from linear_algebra.linear_algebra import sum_of_squares, dot
import math
import matplotlib.pyplot as plt

num_friends = [100,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]


def make_friends_counts_histogram(plt):
    friend_counts = Counter(num_friends)
    xs = range(101)                       # largest value is 100
    print("xs =", xs)
    ys = [friend_counts[x] for x in xs]   # height is just # of friends 
    print("ys =", ys)
    plt.bar(xs, ys)
    plt.axis([0, 101, 0, 25])
    plt.title("Histogram of Friend Counters")
    plt.xlabel("# of friends")
    plt.ylabel("# of people")
    plt.show()


num_points = len(num_friends) # 204
print(num_points)
largest_value = max(num_friends) # 100
print(largest_value)
smallest_value = min(num_friends) # 1
print(smallest_value)

sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]          # 1
second_smallest_value = sorted_values[1]   # 1
second_largest_value = sorted_values[-2]   # 49


""" 
平均(mean)
"""
# this isn't right if yout don't fro __future__ import division
def mean(x):
    return sum(x) / len(x)


"""
中央値(median)
"""
def median(v):
    """ finds the 'middle-most' value of v """
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2

    if n % 2 == 1:
        # if odd, return the middle value
        return sortd_v[midpoint]
    else:
        # if even , return the average of the middle values
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2
    

"""
度数(quantile)
"""
def quantile(x, p):
    """ returns the pth-percentile value in x """
    p_index = int(p * len(x))
    return sorted(x)[p_index]





if __name__ == '__main__':
    make_friends_counts_histogram(plt)

    print("num_points", len(num_friends))
    print("largest value", max(num_friends))
    print("smallest value", min(num_friends))
    print("second_smallest_value", sorted_values[1])
    print("second_largest_value", sorted_values[-1])
    print("mean(num_friends)", mean(num_friends))
    print("median(num_friends)", median(num_friends))
    print("quantile(num_friends, 0.10)", quantile(num_friends, 0.10))

    
