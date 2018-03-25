# coding: utf-8
import re
from stemming.porter2 import stem
"""
52. ステミング
51の出力を入力として受け取り，Porterのステミングアルゴリズムを適用し，単語と語幹をタブ区切り形式で出力せよ． Pythonでは，Porterのステミングアルゴリズムの実装としてstemmingモジュールを利用するとよい．

https://docs.python.jp/3/library/re.html
https://note.nkmk.me/python-re-match-search-findall-etc/
http://doc.okkez.net/static/1.8.7/doc/spec=2fregexp.html#string
http://www.yukun.info/blog/2008/07/python-regular-expression-range.html
"""

with open('nlp.txt', encoding = 'utf-8') as NLP:
    count = 0
    for line in NLP:
        for item in re.sub(r"(?P<group1>[.;:?!])(\s+)(?P<group3>[A-Z])",
                           r"\1\2\n\3", line).split(" "):
            item = re.sub(r"\n", "", item)

            if re.search("\.", item) != None: # 文中の単語はタブ＋改行
                print(item + "\t" + stem(item) + "\n")
            else:
                print(item + "\t" + stem(item)) # 文末の単語はタブ

        count += 1
        if count > 3: break
        
