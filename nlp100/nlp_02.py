# -*- coding: utf-8 -*-
# 02.py

"""
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
"""

str1 = "パトカー"
str2 = "タクシー"
str3 = ""

print(str1[0::2] + str2[0::2])

for a, b in zip(str1, str2):
    str3 = str3 + a + b

print(str3)    


""" zip()
各引数から，要素を1つずつ取り出してタプルを生成してくれる関数.
"""

print(''.join([a + b for a, b in zip(str1, str2)]))

"""
実行速度を意識した実装
''.join() は，引数内の要素を '' 内の区切り文字で区切った上で結合する
"""
