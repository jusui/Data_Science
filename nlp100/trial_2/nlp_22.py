# coding:utf-8
import codecs
import json
import re
"""
22. カテゴリ名の抽出

記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

21で取得したCategoryを含む行の名前だけを取得したい
"""
jawiki = "/Users/usui/work/python/Machine_Learning/nlp100/jawiki-country.json"
def extract_text(title):
    for row in codecs.open(jawiki, "r", "utf-8"):
        article = json.loads(row)
        if title == article["title"]:
            return article["text"]
            
if __name__ == '__main__':
    text = extract_text(u"イギリス")
    for line in text.split("\n"): # 改行でsplit()
        m = re.search(r"Category:(?P<category>.+?)(\||])", line)
        if m:
            # print(m.group("category"))
            print(m.group(1))

"""
イギリス
英連邦王国
G8加盟国
欧州連合加盟国
海洋国家
君主国
島国
1801年に設立された州・地域
"""            
