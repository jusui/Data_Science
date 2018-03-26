# coding: utf-8
import xml.etree.ElementTree as ET
from lxml import etree

tree = etree.parse("nlp.txt.xml")

for token in tree.iter('token'):
    word  = token.findtext('word')
    lemma = token.findtext('lemma')
    pos   = token.findtext('POS')
    print('{}\t{}\t{}'.format(word, lemma, pos))
    

# lxml: 別解(出力されないのでdebug中)
root = tree.getroot()

document = root[0]
sentences = document[0]
for sentence in sentences:
    tokens = sentence[0]
    for token in tokens:
        print("lxml")
        print("{}\t{}\t{}".format(token.find("word").text,
              token.find("lemma").text,
              token.find("POS").text)
              )
