# coding: utf-8

"""
nlp100
nlp_27.py
usage:python nlp_27.py

27. 内部リンクの除去

    26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．


[moduleを活用するテクニック] https://qiita.com/okadate/items/4153d626a262eabb5a26
[正規表現]
http://docs.python.jp/2/howto/regex.html
https://qiita.com/gamma1129/items/68e955853e265cb12ebe#%E5%9B%9E%E7%AD%94-9
"""


"""
回答①

# https://ja.wikipedia.org/wiki/Help:%E6%97%A9%E8%A6%8B%E8%A1%A8
"""
import sys; sys.path.append('/Users/usui/work/python/pyfiles/mymodule')
from extract_from_json import extract_from_json
import re


def remove_markup(str):
    str = re.sub(r"r{2, 5}", r"", str)
    str = re.sub(r"\[{2}([^|\]]+?\|)*(.+?)\]{2}", r"\2", str)
    
temp_dict = {}
lines = re.split(r"\n[\|}]", extract_from_json(u"イギリス"))

for line in lines:
    temp_line = re.search("^(.*?)\s=\s(.*)", line, re.S)
    if temp_line is not None:
        # マークアップ強調は，シングルクォートの数(2-5)で処理->re.sub()で書き換える
        temp_dict[temp_line.group(1)] = re.sub(r"'{2,5}", r"", temp_line.group(2)) 

for k, v in sorted(temp_dict.items(), key = lambda x: x[1]):
    print(k, v)
    


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
from pprint import pprint

def extract_base_info(text):
    # 改行文字に対してもマッチさせる代替モード (re.DOTALL)
    m = re.search("{{基礎情報[^|]+\|(?P<info_body>.+?)\n}}", text, re.DOTALL)
    if not m:
        return {}

    info_body = m.group("info_body")
    info_dict = {}

    for item in info_body.split("\n|"):
        words = re.split(r"\s+=\s+", item, maxsplit = 1)
        info_dict[words[0]] = words[1]

    return info_dict


def remove_emphasis(text):
    """ 強調マークアップを除去 """
    return re.sub(r"'{2,}", "", text)

  
def remove_internal_links(text):
    """ 内部リンクのマークアップ除去 """
    return re.sub(r"\[ \[ ([^]]+) \] \]", lambda m: m.group(1).split("|")[-1], text)


text = extract_text(u"イギリス")
base_info = extract_base_info(text)

sanitized_base_info = {}
for k, v in base_info.items():
    v = remove_emphasis(v)
    v = remove_internal_links(v)
    sanitized_base_info[k] = v

pprint(sanitized_base_info, indent = 4)    
