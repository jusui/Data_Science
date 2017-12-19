#coding: utf-8
"""  
引数と返り値
"""

a = 7
b = 3

# args : 関数の外部から受け取った値に対して，引数を使って関数を扱うことができる
# 足し算をprint()
def add1(c, d):
    e = c + d
    print(e)

add1(a, b)

# Return : 返り値は，return することで，関数の外部に値を受け渡すことが出来る.
def add2(c, d):
    e = c + d
    return e

# 関数から受けた値を利用して，f を定義
f = add2(a, b)
print(f)

