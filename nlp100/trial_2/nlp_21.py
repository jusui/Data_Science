# coding:utf-8
import codecs
import json
import re
"""
21. カテゴリ名を含む行を抽出

記事中でカテゴリ名を宣言している行を抽出せよ．
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
        if re.search(r"Category:", line):
            print(line)

"""
[[Category:イギリス|*]]
[[Category:英連邦王国|*]]
[[Category:G8加盟国]]
[[Category:欧州連合加盟国]]
[[Category:海洋国家]]
[[Category:君主国]]
[[Category:島国|くれいとふりてん]]
[[Category:1801年に設立された州・地域]]
"""            
