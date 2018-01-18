# coding: utf-8
"""
nlp100
nlp_14.py
usage : python nlp_14.py text.txt 10(integer)

14. 先頭からN行を出力

    自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
    確認にはheadコマンドを用いよ．

[Linux]
$ head -3 hightemp.txt

"""

import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

for line in lines[:int(sys.argv[2])]:
    print(line)
