# coding:utf-8

"""
nlp_100 trial
正規表現など躓いた点をまとめる.

"""

# [20-29]正規表現
import sys; sys.path.append('/Users/usui/work/python/pyfiles/mymodule')
from extract_from_json import extract_from_json
import re

lines = extract_from_json(u"イギリス").split("\n")
for line in lines:
    """ (e.f.) [[File:ImamAliMosqueNajafIraq.JPG|thumb|[[ナジャフ]] """
    # リテラル '|' にマッチするには, \| or [|]
    file_line = re.search(u"(File|ファイル):(.*?)\|", line) 
    if file_line is not None:
	print(file_line.group(2))

text = extract_text(u"イギリス")
for line in text.split("\n"):
    # [^5] は '5' を除く任意の文字にマッチ
    m = re.search("(File|ファイル):(?P<filename>[^|]+)\|", line) 
    if m:
        print(m.group("filename"))        
