# -* coding: utf-8 *-

from __future__ import division
import re, math, random
import matplotlib.pyplot as plt
from collections import defaultdict, Counter
from functools import partial, reduce

#
# -- functions for working with vectors
#

def vector_add(v, w):
    """ adds corresponding elements """
    return [v_i + w_i for v_i, w_i in zip(v, w)]

def vector_subtract(v, w):
    """ subtract corresponding elements """
    return [v_i - w_i for v_i, w_i in zip(v, w)]

def vector_sum(vectors):
    """ sums all corresponding elements """
    return reduce(vector_add, vectors)

def scalar_multiply(c, v):
    """ c is a number, v is a vector """
    return [c * v_i for v_i in v]

def scalar_mean(vectors):
    """ compute the vector whose its element is the mean of \
    the its elements of the input vectors """
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def vector_mean(vectors):
    """ i番目の要素が，入力したベクトルリストの
    i番目の要素すべての平均であるベクトルを計算する """
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    """ v_1 * v_1 + ... + v_n * v_n """
    return dot(v, v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def squared_distance(v, w):
    """ (v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2 """
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
    return math.sqrt(squared_distance(v, w))

def distance_2(v, w):
    return magnitude(vector_subtract(v, w))


"""
Metrics

"""
def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols


def get_row(A, i):
    return A[i]

def get_column(A, j):
    return [A_i[j] for A_i in A]


def make_matrix(num_rows, num_cols, entry_fn):
    """ returns a num_rows x num_cols matrix
    whose (i, j)th entry is entry_fn(i, j) 
    変数型リスト[entry_fn(i, 0)]を作って，各iに対応するリストへ
    """
    return [ [entry_fn(i,j)
              for j in range(num_cols)]
             for i in range(num_rows) ]

# 対角行列を作る
def is_diagonal(i, j):
    """ 1's on the 'diagonal', 0's everywhere else """
    return 1 if i == j else 0

# def
identity_matrix = make_matrix(5, 5, is_diagonal)

friendships = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0], # user 0
               [1, 0, 1, 1, 0, 0, 0, 0, 0, 0], # user 1
               [1, 1, 0, 1, 0, 0, 0, 0, 0, 0], # user 2
               [0, 1, 1, 0, 1, 0, 0, 0, 0, 0], # user 3
               [0, 0, 0, 1, 0, 1, 0, 0, 0, 0], # user 4
               [0, 0, 0, 0, 1, 0, 1, 1, 0, 0], # user 5
               [0, 0, 0, 0, 0, 1, 0, 0, 1, 0], # user 6
               [0, 0, 0, 0, 0, 1, 0, 0, 1, 0], # user 7
               [0, 0, 0, 0, 0, 0, 1, 1, 0, 1], # user 8
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]] # user 9

#####
# DELETE DOWN
#

def matrix_add(A, B):
    if shape(A) != shape(B):
        raise ArithmeticError("cannot add matrices with different shapes")
        
    num_rows, num_cols = shape(A)
    def entry_fn(i, j): return A[i][j] + B[i][j]
        
    return make_matrix(num_rows, num_cols, entry_fn)


def make_graph_dot_product_as_vector_projection(plt):
    v = [2, 1]
    w = [math.sqrt(.25), math.sqrt(.75)]
    c = dot(v, w)
    vonw = scalar_multiply(c, w)
    o = [0,0]

    plt.arrow(0, 0, v[0], v[1], width=0.002,
              head_width=.1, length_includes_head=True)
    plt.annotate("v", v, xytext=[v[0] + 0.1, v[1]])
    plt.arrow(0 ,0, w[0], w[1], width=0.002,
              head_width=.1, length_includes_head=True)
    plt.annotate("w", w, xytext=[w[0] - 0.1, w[1]])
    plt.arrow(0, 0, vonw[0], vonw[1], length_includes_head=True)
    plt.annotate(u"(v•w)w", vonw, xxytext=[vonw[0] - 0.1,
                                           vonw[1] + 0.1])
    plt.arrow(v[0], v[1], vonw[0] - v[0], vonw[1] - v[1],
               linestyle='dotted', length_includes_head=True)
    
    plt.scatter(*zip(v,w,o),marker='.')
    plt.axis('equal')
    plt.show()
    

if __name__ == '__main__':
    v = [2, 1]
    w = [math.sqrt(.25), math.sqrt(.75)]
    print(vector_add(v, w))
    print(vector_subtract(v, w))

    """ Metrics """
    
    A = [ [1, 2, 3],
          [4, 5, 6] ] # A has 2 rows and 3 columns

    B = [ [1, 2],
          [3, 4],
          [5, 6] ]    # B has 3 rows and 2 columns

    
    print(shape(A))
    print(get_row(A, 1))     # 0,1
    print(get_column(A, 2))  # 0,1,2


    print(identity_matrix)

#    make_graph_dot_product_as_vector_projection(plt)
