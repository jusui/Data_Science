# coding: utf-8
"""
nlp100
nlp_10.py

10. 行数のカウント

    行数をカウントせよ．確認にはwcコマンドを用いよ．

"""

import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

print(len(lines))


