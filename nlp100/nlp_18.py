# coding: utf-8
"""
nlp100
nlp_18.py
usage:python nlp_18.py 3

18. 各行を3コラム目の数値の降順にソート

    各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
    確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

[Linux] 
$ sort (-r) -k 3 hightemp.txt
http://itpro.nikkeibp.co.jp/article/COLUMN/20060227/230887/
"""

import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()
    print(lines)

print()

for line in sorted(lines, key = lambda x: x.split()[2], reverse = False): # 昇順:True
    print(line)
    
"""
[無名関数 lambda]
特定の数字列をソートするのであれば簡単なのですが，今回は文字列の途中に存在する数値順にソートしなければなりません．無名関数の lambda を用いてソートの基準を指定しています．

"""
