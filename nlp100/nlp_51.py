# coding: utf-8
import re
"""
51. 単語の切り出し
空白を単語の区切りとみなし，50の出力を入力として受け取り，1行1単語の形式で出力せよ．
ただし，文の終端では空行を出力せよ．
"""
with open('nlp.txt', encoding = 'utf-8') as NLP:
    count = 0
    for line in NLP:
        for item in re.sub(r"(?P<group1>[.;:?!])(\s+)(?P<group3>[A-Z])",
                           r"\1\2\n\3", line).split(" "):
            # print(item)
            item = re.sub( r"\n", "", item)

            if re.search("\.", item) != None:
                item = re.sub(r"(\.)", r".\n", item)
            print(item)
            
        count += 1
        if count > 3: break
