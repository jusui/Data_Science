# coding: utf-8
"""
55. 固有表現抽出

入力文中の人名をすべて抜き出せ．
"""
import os
from lxml import etree

tree = etree.parse("nlp.txt.xml")

for token in tree.iterfind(
        './document/sentences/sentence/tokens/token/[NER="PERSON"]'):
    print(token.findtext('word'))
