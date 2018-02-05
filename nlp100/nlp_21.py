# coding: utf-8
"""
nlp100
nlp_21.py
usage:python nlp_21.py

21. カテゴリ名を含む行を抽出

    記事中でカテゴリ名を宣言している行を抽出せよ．

[moduleを活用するテクニック]
https://qiita.com/okadate/items/4153d626a262eabb5a26

"""
import sys; sys.path.append('/Users/usui/work/python/pyfiles/mymodule')
from extract_from_json import extract_from_json

print("力技")
lines = extract_from_json(u"イギリス").split("\n")
for line in lines:
    if "Category" in line:
        print(line)


print()
print()
print("正規表現")
"""
正規表現
"""
from extract_text import extract_text
import re

text = extract_text(u"イギリス")
for line in text.split("\n"):
    if re.search(r"Category:", line):
        print(line)
