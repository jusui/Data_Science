# coding: utf-8
"""
nlp100
nlp_13.py

13. col1.txtとcol2.txtをマージ

    12で作ったcol1.txtとcol2.txtを結合し，
    元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
    確認にはpasteコマンドを用いよ．

[Linux]
$ paste col1.txt col2.txt

"""

with open("col1.txt") as f1, open("col2.txt") as f2:
    line1, line2 = f1.readlines(), f2.readlines()

with open("merge.txt", "w") as writer:
    for col1, col2 in zip(line1, line2):
        writer.write("\t".join([col1.rstrip(), col2]))
    
