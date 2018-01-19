# coding: utf-8
"""
nlp100
nlp_17.py
usage:python nlp_17.py 3

17. １列目の文字列の異なり

    1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

[Linux]
$ cut -f 1 hightemp.txt | sort | uniq

"""

import sys
import codecs


prefs = set(line.split("\t")[0] for line in codecs.open('./hightemp.txt', 'r', 'utf-8'))
for i in prefs:
    print (i)

"""
[set()]
http://www.yoheim.net/blog.php?q=20160605

    
[codecs.open()]
エンコードされたファイルを mode を使って開き、透過的なエンコード/デコードを提供する StreamReaderWriter のインスタンスを返します。デフォルトのファイルモードは 'r' 、つまり、読み出しモードでファイルを開きます。
https://docs.python.jp/3/library/codecs.html

"""
