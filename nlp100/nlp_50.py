# coding: utf-8
import re

"""
nlp_50.py

50.文字区切り
(. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，
入力された文書を1行1文の形式で出力せよ．
"""

with open('nlp.txt', encoding = 'utf-8') as NLP:
    count = 0
    for line in NLP:
        # パターンの一部を()で囲むと,置換後の文字列の中でマッチした文字列を使用できる
        # ()(空白)(全てのアルファベット大文字の内のどれか1つ)
        print(re.sub(r"(?P<group1>[.;:?!])(\s+)(?P<group3>[A-Z])", r"\1\2\n\3", line))

        count += 1
        if count > 5: # 初めの5区切りだけ出力
            break
