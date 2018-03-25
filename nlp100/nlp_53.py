# coding: utf-8
import pprint
import json, re
import corenlp
"""
53. Tokenization
Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．
また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．

xml fileの生成
http://kenichia.hatenablog.com/entry/2016/02/15/174813
"""

words = re.compile(r"<word>(\w+)</word>")

input_file = open('nlp.txt.xml', 'r')
for line in input_file:
    word = words.search(line.strip())
    if word:
        print(word.group(1))
input_file.close()

# corenlp_dir = "/Users/usui/work/python/Data_Science/nlp100/stanford-corenlp-full-2018-02-27"
# parser = corenlp.StanfordCoreNLP(corenlp_path = corenlp_dir)

# with open('nlp.txt', encoding = 'utf-8') as NLP:
#     count = 0
#     for line in NLP:
#         for i in parser.raw_parse(line)["sentences"][0]["words"]:
#             print(i[0])

#         count += 1
#         if count > 1: break
        
