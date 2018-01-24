# coding: utf-8
"""
nlp100
nlp_22.py
usage:python nlp_22.py

22. カテゴリ名の抽出

    記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

[moduleを活用するテクニック]
https://qiita.com/okadate/items/4153d626a262eabb5a26

[正規表現]
http://docs.python.jp/2/howto/regex.html
https://qiita.com/gamma1129/items/68e955853e265cb12ebe#%E5%9B%9E%E7%AD%94-9
"""
import sys; sys.path.append('/Users/usui/work/python/pyfiles/mymodule')
from extract_from_json import extract_from_json
import re

lines = extract_from_json(u"イギリス").split("\n")

for line in lines:
    category = re.search("^\[\[Category:(.*?)(|\|.*)\]\]$", line)
    if category is not None:
#        print(category)
        print(category.group(1)) # .group() : re.search() でマッチした文字列を取得
#        print()
        

"""
正規表現
"""
print()
print()
print("=== 正規表現 ===")    
print()


import re
from extract_text import extract_text

text = extract_text(u"イギリス")
for line in text.split("\n"):
    m = re.search(r"Category:(?P<category>.+?)(\||])", line)
#    print("m :", m)
    if m:
        print(m.group("category"))
        
