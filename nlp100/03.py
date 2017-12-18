# -*- coding: utf-8 -*-
# 03.py

"""
"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，
各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
"""

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
# カンマを除去
str = str.replace(',', "")
# ピリオドを除去
str = str.replace('.', "")
# 文字列を区切る
str = str.split()

# len で長さ取って，listに格納
list = []
for word in str:
    print(word)
    list.append(len(word))

print(list)

"""
replace() で句読点を除外し，split()で単語ごとに区切る.
len() で長さを取得後，listに入れる.
split() は，引数で区切り文字を指定できる(default は，スペース)
"""
