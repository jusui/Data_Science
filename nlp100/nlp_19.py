# coding: utf-8
"""
nlp100
nlp_19.py
usage:python nlp_19.py

19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる

[Linux] 
$ cat hightemp.txt | cut -f 1 | sort | uniq -c | sort -rk 1 
[uniq -c]:ユニークをカウント

"""

import codecs
from collections import Counter

freq_counter = Counter(line.split()[0] for line in codecs.open('./hightemp.txt', 'r', 'utf-8'))

print(freq_counter.most_common())


"""
回答.2

"""
import sys
from collections import defaultdict

prefectures = defaultdict(int)
print(prefectures)

with open('./hightemp.txt') as f:
    line = f.readline()
    print("line =", line)
    # lines = f.readlines()
    # print("lines =", lines)
    
    while line:
        prefectures[line.split()[0]] += 1
        line = f.readline()
        print("line :", line)
    
    for k, v in sorted(prefectures.items(),
                       key = lambda x: x[1], reverse = False): # 昇順:True
        print("v =", v)
        print("k =", k)
    
