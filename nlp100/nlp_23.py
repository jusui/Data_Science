# coding: utf-8
"""
nlp100
nlp_23.py
usage:python nlp_23.py

23. セクション構造

    記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．

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
    section = re.search("^(=+)\s*(.*?)\s*(=+)$", line)
    if section is not None:
        # print(section.group(2))
        # print("section name :", section.group(2))
        # print("level :", len(section.group(1)) - 1)
        print(section.group(2), len(section.group(1)) - 1)        

"""
正規表現

後方参照
http://docs.python.jp/2/howto/regex.html

"""
print()
print()
print("=== 正規表現 ===")    
print()


import re
from extract_text import extract_text

text = extract_text(u"イギリス")
for line in text.split("\n"):
    m = re.search(r"^(?P<level>=+)(?P<header>.+)\1$", line)
#    m = re.search(r"Category:(?P<category>.+?)(\||])", line)
    if m:
        header = m.group("header")
        level  = m.group("level").count("=") - 1

        print("{0}: {1}".format(header, level))
        
