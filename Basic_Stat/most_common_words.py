# coding: utf-8
import sys
from collections import Counter

"""
入力から単語の出現回数を数え，頻出するものを表示するスクリプト
[usage]:
cat quiz1grades.txt | python most_common_words.py 10
"""

if __name__ == '__main__':
    # 第一引数として，出力する単語数を指定する    
    try:
        num_words = int(sys.argv[1])
    except:
        print("usage: most_common_words.py num_words")
        sys.exit(1) # 0以外のexitコードは，Errorが発生したことを示す

    counter = Counter(word.lower()                       # 単語を小文字にする
                      for line in sys.stdin              # 
                      for word in line.strip().split()   # 単語は空白で区切る
                      if word)                           # 空文字列はスキップする

    for word, count in counter.most_common(num_words):
        sys.stdout.write(str(count))
        sys.stdout.write("\t")
        sys.stdout.write(word)
        sys.stdout.write("\n")
        
