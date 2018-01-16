# coding: utf-8
"""
nlp100
nlp_07.py

[テンプレートによる文生成]
引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．

"""

def function(x, y, z):
    return u"{x}時の{y}は{z}".format(x=x, y=y, z=z)

x = 12
y = "気温"
z = 22.4

print(function(x, y, z))
