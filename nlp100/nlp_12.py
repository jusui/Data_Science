# coding: utf-8
"""
nlp100
nlp_12.py

12. 1列目をcol1.txtに，2列目をcol2.txtに保存

    各行の1列目だけを抜き出したものをcol1.txtに，
    2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
    確認にはcutコマンドを用いよ．

[Linux]
$ cut -f 1 hightemp.txt

$ cut -f 2 hightemp.txt
"""

import sys

def write_col(source_line, column_number, filename):
    col = []
    for line in source_line:
#        print(line.split()[1])
        col.append(line.split()[column_number] + "\n") # or "\t"

    with open(filename, "w") as writer:
        writer.writelines(col)

        
with open(sys.argv[1]) as f:
    lines = f.readlines()


write_col(lines, 0, "col1.txt")        
write_col(lines, 1, "col2.txt")
