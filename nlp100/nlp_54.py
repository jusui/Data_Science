# coding: utf-8
import re
from lxml import etree
"""
54. 品詞タグ付け
Stanford Core NLPの解析結果XMLを読み込み，単語，レンマ，品詞をタブ区切り形式で出力せよ．
"""

WORD  = re.compile(r"<word>(\w+)</word>")
LEMMA = re.compile(r"<lemma>(\w+)</lemma>")
POS   = re.compile(r"<POS>(\w+)</POS>")

with open('nlp.txt.xml', encoding = 'utf-8') as xml_file:
    words = []
    for line in xml_file:
        if len(words) == 3:
            print("\t".join(words))
            words = []
        else:
            line = line.strip()
            # word
            word = WORD.search(line)
            if len(words) == 0 and word:
                words.append(word.group(1))
                continue
            # lemma
            lemma = LEMMA.search(line)
            if len(words) == 1 and lemma:
                words.append(lemma.group(1))
                continue
            # pos
            pos = POS.search(line)
            if len(words) == 2 and pos:
                words.append(pos.group(1))
