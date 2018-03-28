# coding: utf-8
"""
55. 固有表現抽出

入力文中の人名をすべて抜き出せ.
"""

from lxml import etree

tree = etree.parse('nlp.txt.xml')
# 人名=PERSONパスを指定
xpath = './document/sentences/sentence/tokens/token/[NER="PERSON"]'

for token in tree.iterfind(xpath):
    print(token.findtext('word'))
