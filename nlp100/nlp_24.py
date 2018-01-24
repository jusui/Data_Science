# coding: utf-8
"""
nlp100
nlp_24.py
usage:python nlp_24.py

24. ファイル参照の抽出

    記事から参照されているメディアファイルをすべて抜き出せ．

[moduleを活用するテクニック]
https://qiita.com/okadate/items/4153d626a262eabb5a26

[正規表現]
http://docs.python.jp/2/howto/regex.html
https://qiita.com/gamma1129/items/68e955853e265cb12ebe#%E5%9B%9E%E7%AD%94-9
"""


"""

回答①

"""
import sys; sys.path.append('/Users/usui/work/python/pyfiles/mymodule')
from extract_from_json import extract_from_json
import re

lines = extract_from_json(u"イギリス").split("\n")
# print(lines)

for line in lines:
    """ (e.f.) [[File:ImamAliMosqueNajafIraq.JPG|thumb|[[ナジャフ]] """
    file_line = re.search(u"(File|ファイル):(.*?)\|", line) # リテラル '|' にマッチするには, \| or [|]
    if file_line is not None:
        print(file_line.group(2))


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
    m = re.search("(File|ファイル):(?P<filename>[^|]+)\|", line) # [^5] は '5' を除く任意の文字にマッチ
    if m:
        print(m.group("filename"))
