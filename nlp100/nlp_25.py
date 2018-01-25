# coding: utf-8
"""
nlp100
nlp_25.py
usage:python nlp_25.py

25. テンプレートの抽出

    記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．

"""


"""
回答①
[moduleを活用するテクニック]
https://qiita.com/okadate/items/4153d626a262eabb5a26

[正規表現]
https://docs.python.jp/3/library/re.html
"""
import sys; sys.path.append('/Users/usui/work/python/pyfiles/mymodule')
from extract_from_json import extract_from_json
import re

temp_dict = {}
# [, ]は，文字クラス(マッチしたい文字の集合)
# リテラル '|' にマッチするには、 \| か [|] を利用する -> |}にマッチするリテラル
lines = re.split(r"\n[\|}]", extract_from_json(u"イギリス")) # split(\n| or \n})
print()

for line in lines:
    # \s=\s(空白=空白), '^' で始まる正規表現は, re.search() でマッチを文字列の先頭に制限
    # s = '<a> b <c>', re.search("(.*?)", s) ->'<a>'
    temp_line = re.search("^(.*?)\s=\s(.*)", line, re.S) # re.S:改行込みで検索
    if temp_line is not None:
        temp_dict[temp_line.group(1)] = temp_line.group(2)
#        print(sorted(temp_dict.items(), key = lambda x: x[1]))

print()        
for k, v in sorted(temp_dict.items(), key = lambda x: x[1]):
    print(k, v)


    
"""
正規表現

"""
print()
print()
print("=== 正規表現 ===")    
print()

import re
from extract_text import extract_text
from pprint import pprint

def extract_base_info(text):
    m = re.search("{{基礎情報[^|]+\|(?P<info_body>.+?)\n}}", text, re.DOTALL) # ドット:改行以外の全てとマッチ, ?:最小一致(非貪欲)
    print("m :", m)
    if not m:
        return {}

    info_body = m.group("info_body")
    print(info_body)

    info_dict = {}

    for item in info_body.split("\n|"):
        key, val = re.split(r"\s+=\s+", item, maxsplit=1)
        info_dict[key] = val

    return info_dict


text = extract_text(u"イギリス")
base_info = extract_base_info(text)
pprint(base_info, indent = 4)
