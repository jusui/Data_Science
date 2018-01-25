# coding: utf-8

"""
nlp100
nlp_25.py
usage:python nlp_25.py

25. テンプレートの抽出

    記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．

[moduleを活用するテクニック]
https://qiita.com/okadate/items/4153d626a262eabb5a26

[正規表現]
http://docs.python.jp/2/howto/regex.html
https://qiita.com/gamma1129/items/68e955853e265cb12ebe#%E5%9B%9E%E7%AD%94-9
"""


"""

回答①

{{基礎情報 国
|略名 = イギリス
|日本語国名 = グレートブリテン及び北アイルランド連合王国
|公式国名 = {{lang|en|United Kingdom of Great Britain and Northern Ireland}}<ref>英語以外での正式国名:<br/>
*{{lang|gd|An Rìoghachd Aonaichte na Breatainn Mhòr agus Eirinn mu Thuath}}（[[スコットランド・ゲール語]]）<br/>
*{{lang|cy|Teyrnas Gyfunol Prydain Fawr a Gogledd Iwerddon}}（[[ウェールズ語]]）<br/>
*{{lang|ga|Ríocht Aontaithe na Breataine Móire agus Tuaisceart na hÉireann}}（[[アイルランド語]]）<br/>
*{{lang|kw|An Rywvaneth Unys a Vreten Veur hag Iwerdhon Glédh}}（[[コーンウォール語]]）<br/>
*{{lang|sco|Unitit Kinrick o Great Breetain an Northren Ireland}}（[[スコットランド語]]）<br/>
**{{lang|sco|Claught Kängrick o Docht Brätain an Norlin Airlann}}、{{lang|sco|Unitet Kängdom o Great Brittain an Norlin Airlann}}（アルスター・スコットランド語）</ref>
|国旗画像 = Flag of the United Kingdom.svg
|国章画像 = [[ファイル:Royal Coat of Arms of the United Kingdom.svg|85px|イギリスの国章]]
|国章リンク = （[[イギリスの国章|国章]]）
...
|国際電話番号 = 44
|注記 = <references />
}}

"""
import sys; sys.path.append('/Users/usui/work/python/pyfiles/mymodule')
from extract_from_json import extract_from_json
import re

temp_dict = {}
lines = re.split(r"\n[\|}]", extract_from_json(u"イギリス")) # "|" を探す場合，\| or [|]
# lines = re.split(r"\n", extract_from_json(u"イギリス")) # "|" を探す場合，\| or [|]

for line in lines:
    temp_line = re.search("^(.*?)\s=\s(.*)", line, re.S)
    if temp_line is not None:
#        print(temp_line.group(1)) or (2)
        temp_dict[temp_line.group(1)] = temp_line.group(2)

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
from pprint import pprint
from extract_text import extract_text

def extract_base_info(text):
    # 改行文字に対してもマッチさせる代替モード (re.DOTALL)
    m = re.search("{{基礎情報[^|]+\|(?P<info_body>.+?)\n}}", text, re.DOTALL)
    if not m:
        return {}


    info_body = m.group("info_body")
    print("info_body", info_body)
    info_dict = {}

    for item in info_body.split("\n|"): # ("\n|") 改行とパイプでsplit()
        # (e.f.日本語国名 = グレートブリテン): "="を挟んで空白文字が存在するため，\s+ = \s+で除去
        key, val = re.split(r"\s=\s", item, maxsplit=1) # (\s):任意の空白文字とマッチ
#        key, val = re.split(r"\s+=\s+", item, maxsplit=1) # (\s):任意の空白文字とマッチ
        info_dict[key] = val

    return info_dict

text = extract_text(u"イギリス")
base_info = extract_base_info(text)

pprint(base_info, indent=4)
