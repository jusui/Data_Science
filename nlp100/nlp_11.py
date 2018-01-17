# coding: utf-8
"""
nlp100
nlp_11.py

11. タブをスペースに置換

    タブ1文字につきスペース1文字に置換せよ．
    確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

[Linux]
$ sed -e s/$'\t'/" "/g hightemp.txt

$ cat hightemp.txt | tr "\t" " "

$ expand -t 1 hightemp.txt
"""

import sys

with open(sys.argv[1]) as f:
    str = f.read()

print(str.replace("\t", " "))




