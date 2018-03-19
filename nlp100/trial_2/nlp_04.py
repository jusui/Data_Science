# coding: utf-8
"""
4."Hi He Lied Because Boron Could Not Oxidize Fluorine. 
New Nations Might Also Sign Peace Security Clause. Arthur King Can."
という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）
への連想配列（辞書型もしくはマップ型）を作成せよ．
"""

sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. \
New Nations Might Also Sign Peace Security Clause. Arthur King Can."

sentence = sentence.replace(',', "") # カンマ除去
sentence = sentence.replace('.', "") # ピリオド除去
splited_word = sentence.split()      # 単語に分割
print("splited_word :", "\n", splited_word)
print()

dict = {}
initial_word = [1, 5, 6, 7, 8, 9, 15, 16, 19]

for element in splited_word:

    print("element[:1]:", element[:1])
    print("element[:2]:", element[:2], "\n")
    
    if splited_word.index(element) + 1 in initial_word:     # 0番目から格納しているため，"+1"
        dict[element[:1]] = splited_word.index(element) + 1 # 要素の値から要素のオフセット(位置)を得る
        # print(dict[element[:1]])
    
    else:
        dict[element[:2]] = splited_word.index(element) + 1
        # print(dict[element[:2]])

print(sorted(dict.items(), key = lambda x: x[1])) # value でソート
