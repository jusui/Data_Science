# coding: utf-8
import pprint
import json
import corenlp
"""
53. Tokenization
Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．
また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．
"""

corenlp_dir = ""
parser = corenlp.StanfordCoreNLP(corenlp_path=corenlp_dir)

with open('nlp.txt', encoding = 'utf-8') as NLP:
    count = 0
    for line in NLP:
        for i in parser.raw_parse(line)["sentences"][0]["words"]:
            print(i[0])

        count += 1
        if count > 1: break
