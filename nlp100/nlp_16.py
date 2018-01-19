# coding: utf-8
"""
nlp100
nlp_16.py
usage:python nlp_16.py 3

16. ファイルをN分割する

    自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
    同様の処理をsplitコマンドで実現せよ．

[Linux]
$ split -l 8 hightemp.txt

"""

import sys

def split_files(source_file, n_split):
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    if len(lines) % n_split != 0:
        raise Exception("Undivideble by N=%d" % n_split)

    else:
        n_lines = len(lines) / n_split
        
    for i in range(n_split):
        # 書き出すファイル名指定
        # make split0.txt with str(i), i = 0, 1, 2...
        with open("split%s.txt" % str(i), "w") as w:
            w.writelines(lines[int(n_lines * i) : int(n_lines * (i + 1))])

            
if __name__ == '__main__':
    try:
        split_files(sys.argv[1], int(sys.argv[2]))

    except Exception as err:
        print("Error", err)
        
    
    
        
    
