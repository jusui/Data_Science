# coding: utf-8
"""
nlp100
nlp_09.py

Typoglycemia

スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ． 
ただし，長さが４以下の単語は並び替えないこととする． 
適当な英語の文（例えば"I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .“）を与え，
その実行結果を確認せよ．

"""

import random

# [ref]文字列シャッフル
# https://qiita.com/trsqxyz/items/a5a74d73e5852b84c07c
def stir(word):
    if 5 > len(word):
        return word

    head = word[0]
    last = word[-1]
    body = word[1:-1]

    # random.sample(population, k)
    # https://docs.python.jp/3/library/random.html
    return head + "".join(random.sample(body, len(body))) + last


def genTypoglycemia(sentence):
    # sentenceをspaceで区切り，1つの文字列にするために" ".join(map(str, list))でまとめる
    # https://qiita.com/unchainendo/items/993099e6664661d03e61
    return " ".join(map(stir, sentence.split(" ")))


text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print("text:", text)
print()

print("stir(text):", stir(text))
print()

typoglycemia = genTypoglycemia(text)
print("Typoglycemia:", typoglycemia)
