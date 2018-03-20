# coding: utf-8
"""
5.与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ.

[n-gram] : bigramとは、任意の文字列が2文字だけ続いた文字列のこと
n-gram は「文章中に現れる N 個連続した連なり」??
"""
import re

def n_gram(seq, n = 2):
    seq_set = (seq[i:] for i in range(n))
    return tuple("".join(chars) for chars in zip(*seq_set))

sentence = "I am an NLPer"
sentence = sentence.replace(" ", "")
# sentence = re.split(r"[\s,.]", sentence)
print(sentence)

bi_gram = n_gram(sentence)
print(bi_gram)
