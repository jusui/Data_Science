# coding: utf-8
"""
nlp100
nlp_06.py

集合
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

[moduleを活用するテクニック]
https://qiita.com/okadate/items/4153d626a262eabb5a26
"""
import sys; sys.path.append('/Users/usui/work/python/pyfiles/mymodule')
from nlp_05 import n_gram

def ngram(input, n):
    l = len(input) - n + 1
    print("l =", l)
    list = []
    for i in range(0, l):
        list.append(input[i:i+n])
    return list

str1 = "paraparaparadise"
str2 = "paragraph"

X = set(ngram(str1, 2))
Y = set(ngram(str2, 2))
print(n_gram(str1, 2))

print(X.union(Y))         # 和集合
print(X.intersection(Y))  # 積集合
print(X.difference(Y))    # 差集合

print("se" in X)
print("se" in Y)
