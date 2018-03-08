# coding: utf-8
"""
nlp100
nlp_20.py
usage:python nlp_20.py

21. カテゴリ名を含む行を抽出

    記事中でカテゴリ名を宣言している行を抽出せよ．

"""

import codecs
import json
import re

def extract_text(title):
    for row in codecs.open("./jawiki-country.json", "r", "utf-8"):
        article = json.loads(row)
        if title == article["title"]:
            return article["text"]

        
text = extract_text(u"イギリス")
for line in text.split("\n"):
    if re.search(r"Category:", line):
        print(line)


print()
print()

# ============
# 別解
# ============
with open("jawiki-country.json") as f:
    article_json = f.readline()
    while article_json:
        article_dict = json.loads(article_json)
        #        print(article_dict)
        if article_dict["title"] == u"イギリス":
            print(article_dict["text"])
        article_json = f.readline()
        
