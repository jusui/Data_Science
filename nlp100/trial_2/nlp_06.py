# coding: utf-8
"""
6.集合"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""
import sys; sys.path.append('/Users/usui/work/python/pyfiles/mymodule')
from nlp_05 import n_gram

def ngram(input, n):
    
    len_sentence = len(input) - n + 1
    print("length of sentence =", len_sentence)
    list = []
    for i in range(0, len_sentence):
        list.append(input[i:i+n])
        
    return list

sentence1 = "paraparaparadise" # len =18
sentence2 = "paragraph"        # len =9

X = set(ngram(sentence1, 2))
Y = set(ngram(sentence2, 2))
print(n_gram(sentence1, 2))
