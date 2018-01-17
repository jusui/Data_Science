# -*- coding: utf-8 -*-
# 01.py

"""
「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
"""

str = "パトカータクシー"
print(str[0::2])

# techniques of slice

test = "abcdefgh"

# get string
print(test[0])
print(test[-1])

# slice
print(test[1:3])
# 0 ~ 最後から0, 1, 2 文字までのを除いた範囲の文字列
print(test[0:-3]) # same as test[0:5]
print(test[:4]) # 最後から0, 1, 2, 3 文字まで
print(test[4:]) # 'efgh'，終了インデックスを省略した場合は最後まで

# step数指定
print(test[0:6:2])  # 'ace', ステップ数で指定した分，飛び飛びの文字取得
print(test[0::2])   # 'aceg', 1文字飛ばし
print(test[::3])    # 'adg', 省略も可能
print(test[-3::2])  # 'fg',  最後から3文字目の1つ後から(2つ目)から，2文字を取得
print(test[::-1])   # 'hed', step数を負の値にすると逆順に遡る
print(test[-1::-1]) # 'hgfedcba', 最後から3文字目の1つ後から(2つ目)から，遡る

