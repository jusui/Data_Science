# coding: utf-8
"""
nlp_29.py
usage:python nlp_29.py

29. 国旗画像のURLを取得する

テンプレートの内容を利用し，国旗画像のURLを取得せよ．
（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
(27. 内部リンクの除去)
(26. 強調マークアップの除去)

[moduleを活用するテクニック]
https://qiita.com/okadate/items/4153d626a262eabb5a26
[正規表現]
http://docs.python.jp/2/howto/regex.html
https://qiita.com/gamma1129/items/68e955853e265cb12ebe#%E5%9B%9E%E7%AD%94-9

回答①
[ref]https://ja.wikipedia.org/wiki/Help:%E6%97%A9%E8%A6%8B%E8%A1%A8
"""
import sys; sys.path.append('/Users/usui/work/python/pyfiles/mymodule')
from extract_from_json import extract_from_json
import re


def remove_markup(str):
    str = re.sub(r"r{2, 5}", r"", str)
    str = re.sub(r"\[{2}([^|\]]+?\|)*(.+?)\]{2}", r"\2", str)
    str = re.sub(r"\{{2}.+?\|.+?\|(.+?)\}{2}", r"\1", str)
    str = re.sub(r"\[.*?\]", r"", str)
    str = re.sub(r"<.*?>", r"", str)
    return str
    
    
temp_dict = {}
lines = extract_from_json(u"イギリス").split("\n")
for line in lines:
    temp_line = re.search("^(.*?)\s=\s(.*)", line)
    if temp_line is not None:
        # マークアップ強調は，シングルクォートの数(2-5)で処理->re.sub()で書き換える
        temp_dict[temp_line.group(1)] = remove_markup(temp_line.group(2))

for k, v in sorted(temp_dict.items(), key = lambda x: x[0]):
    print(k, v)
    

"""
回答2
[後方参照] http://docs.python.jp/2/howto/regex.html
"""
print()
print("=== 回答② ===")    
print()

import codecs
import json
import re
from pprint import pprint

def extract_text(title):
    for row in codecs.open("./jawiki-country.json", "r", "utf-8"):
        article = json.loads(row)
        if title == article["title"]:
            return article["text"]

def extract_base_info(text):
    # (re.DOTALL:改行文字に対してもマッチ), [^5]='5'以外の文字とマッチ
    m = re.search("{{基礎情報[^|]+\|(?P<info_body>.+?)\n}}", text, re.DOTALL)
    if not m:
        return {}

    info_body = m.group("info_body")

    info_dict = {}
    for item in info_body.split("\n|"):
        [key, word] = re.split(r"\s+=\s+", item, maxsplit = 1)

        word = remove_selection_header(word)
        word = remove_emphasis(word)
        word = remove_category_links(word)
        word = remove_internal_links(word)
        word = remove_external_links(word)
        word = remove_template(word)
        word = remove_unordered_list(word)
        word = remove_ordered_list(word)
        word = remove_redirect(word)
        word = remove_comment(word)

        info_dict[key] = word
        
    return info_dict

def remove_selection_header(text):
    """ 見出しマークアップを除去 """
    return re.sub(r"(=+)(.+?)\1", lambda m: m.group(2), text)

def remove_emphasis(text):
    """ 強調マークアップを除去 """
    return re.sub(r"'{2,}", "", text)

def remove_category_links(text):
    """ Category linkのマークアップを除去 """
    return re.sub(r"\[\[([^]]+)\]\]", lambda m: m.group(1).split("|")[-1], text)
    
def remove_internal_links(text):
    """ 内部リンクのマークアップ除去 """
    return re.sub(r"\[\[([^]]+)\]\]", lambda m: m.group(1).split("|")[-1], text)

def remove_external_links(text):
    """ 外部リンクのマークアップを除去 """
    return re.sub(r"\[([^]]+)\]", lambda m: m.group(1).split(" ")[-1], text)

def remove_template(text):
    """ スタブのマークアップを除去 """
    return re.sub(r"\{\{(.+?)\}\}", lambda m: m.group(1).split("|")[-1], text)

def remove_unordered_list(text):
    """ 箇条書きのマークアップを除去 """
    return re.sub(r"^\*+\s*", "", text, flags = re.MULTILINE)

def remove_ordered_list(text):
    """ 番号付き箇条書きのマークアップを除去 """
    return re.sub(r"^#+\s*", "", text, flags = re.MULTILINE)

def remove_define_list(text):
    """ 定義の箇条書きのマークアップを除去 """
    return re.sub(r"^(:|;)\s*", "", text, flags = re.MULTILINE)

def remove_redirect(text):
    """ リダイレクトのマークアップを除去 """
    return re.sub(r"#REDIRECT \[\](.+?)\]\]", lambda m: m.group(1), text)

def remove_comment(text):
    """ コメントアウトのマークアップを除去 """
    return re.sub(r"<!--.*?-->", "", text)

text = extract_text(u"イギリス")
base_info = extract_base_info(text)

from urllib.parse import urlencode
from urllib import request

flag_image_name = base_info["国旗画像"]
query = urlencode({
    "action": "query",
    "titles": "File:{0}".format(flag_image_name),
    "prop": "imageinfo",
    "iiprop": "url",
    "format": "json",
})

url = "https://commons.wikimedia.org/w/api.php?{0}".format(query)

with request.urlopen(url) as response:
    body = response.read()
    data = json.loads(body.decode("utf-8"))

    pprint(data, indent = 4)

    flag_image_url = list(data["query"]["pages"].values())[0]["imageinfo"][0]["url"]
    print(flag_image_url)
