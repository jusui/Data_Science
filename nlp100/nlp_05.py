# -*- coding: utf-8 -*-
# 05.py

"""
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ.

[n-gram] : bigramとは、任意の文字列が2文字だけ続いた文字列のこと
n-gram は「文章中に現れる N 個連続した連なり」??
"""
import re

"""
(seq[i:] for i in range(n)) は例えば "Hello" という文字列から ("Hello", "ello", "llo") 
と開始を1文字ずつずらした N 個組みのシーケンスを生成します。

zip すると (("H", "e", "l"), ("e", "l", "l"), ("l", "l", "o")) という組みが取れるので、
あとは適切に join してあげる感じで。
"""
def n_gram(seq, n = 2):
    seq_set = (seq[i:] for i in range(n))

    return tuple("".join(chars) for chars in zip(*seq_set))

sentence = "I am an NLPer"
# ss = sentence.strip() # strip()は，文字間のスペースは残す.
ss = sentence.replace(" ", "")
print(ss)

char_bi_gram = n_gram(ss)
print("char_bi_gram:", char_bi_gram)

"""
re.split()
パターンにマッチした部分で文字列を分割し、リストにして返す。
https://note.nkmk.me/python-re-match-search-findall-etc/

\s
ユニコード (str) パターンに対して:
任意の空白文字とマッチします。
https://docs.python.jp/3/library/re.html

"""
words = re.split(r"[\s,.]", sentence) # 空白文字を見つけたら，分割し，リストで返す.
word_bi_gram = n_gram(words)
print("word_bi_gram:", word_bi_gram)

