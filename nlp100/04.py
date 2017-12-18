# -*- coding: utf-8 -*-
# 03.py

"""
"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，
取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

http://www.yukun.info/blog/2008/07/python-string.html
"""

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
# カンマを除去
str = str.replace(',', "")
# ピリオドを除去
str = str.replace('.', "")
# 文字列を区切る
word = str.split()
print(word)

# 空の辞書を作る
dict = {}

# 先頭1文字取り出すイニシャルの指定
initial = [1, 5, 6, 7, 8, 9, 15, 16, 19]

for element in word:
    # print(len(word)) とかだと，splitして区切った文章の長さを返すため，不向き
#    print(word.index(element))

    # split()した文字列は，0番目から格納しているため，"+1"
    if word.index(element) + 1 in initial:
        # dict[key] = object でkey に対するobject を代入する
        # element[:1] で最初の1文字を取り出す.
        dict[element[:1]] = word.index(element) + 1
        print(dict[element[:1]])

    else:
        # initialではないので, element[:2] で最初の2文字を取り出す.
        dict[element[:2]] = word.index(element) + 1
        print("")
        print(dict[element[:2]])

print("dictionary")
print(dict) 

"""
解②
http://programming-study.com/technology/python-for-index/

"""
# 先頭1文字取り出すイニシャルの指定
initial2 = [1, 5, 6, 7, 8, 9, 15, 16, 19]
# initial2の各要素を-1
map(lambda x: x-1, initial2)

for element in range(len(word)):
    clen = 1 if element in initial2 else 2
#    print(clen)
    dict[word[element][:clen]] = element + 1

print("Solution 2")
print(dict)
        
"""
for文の中で，
print(len(word)) とかだと，splitして区切った文章の長さを返すため，不向き

そこで，index()を使う
指定の値を持つ要素のindexを取得する

[参考]
https://www.pythonweb.jp/tutorial/list/index10.html

"""
