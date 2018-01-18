# coding: utf-8
"""
nlp100
nlp_15.py
usage:

15. 末尾のN行を出力

    自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．

[Linux]
$ tail -3 hightemp.txt

"""

import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

for line in lines[-int(sys.argv[2]):]:
    print(line)

print()

for line in lines[len(lines) - int(sys.argv[2]):]:
    print(line)
    
