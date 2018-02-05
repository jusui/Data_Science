# coding:utf-8
import codecs
import json
"""
20. JSONデータの読み込み

Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
問題21-29では，ここで抽出した記事本文に対して実行せよ．
"""
jawiki = "/Users/usui/work/python/Machine_Learning/nlp100/jawiki-country.json"
for row in codecs.open(jawiki, "r", "utf-8"):
    article = json.loads(row)
    if u"イギリス" == article["title"]:
        print(article["text"])
    
    
