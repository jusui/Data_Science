# coding: utf-8
"""
データクローニング

Webアクセスログをとり，最も見られたページを特定する
Apacheのアクセスログラインを解析するために，正規表現のセットアップを行う

"""
import re

format_pat = re.compile(
    r"(?P<host>[\d\.]+)\s"
    r"(?P<identity>\S*)\s"
    r"(?P<user>\S*)\s"

    r"\[(?P<time>.*?)\]\s"
    r'"(?P<request>.*?)"\s'
    r"(?P<status>\d+)\s"

    r"(?P<bytes>\S*)\s"
    r'"(?P<regerer>.*?)"\s'
    r'"(?P<user_agent>.*?)"\s*'
)

logPath = "/Users/usui/work/python/DataScience/access_log.txt"

# 各アクセスからURLを取り出すためのコードを用意，dictを用いて各URLの出現回数をカウント
# sort() で表示
URLCounts = {}

with open(logPath, "r") as f:
    for line in (l.rstrip() for l in f):
        match = format_pat.match(line)
        if match:
            access = match.groupdict()
            request = access['request']
            fields = request.split()
            if (len(fields) != 3):
                print(fields)


# 空のフィールドに加えて，不要なデータが含まれている．->チェックコードに改変
URLCounts = {}

with open(logPath, "r") as f:
    for line in (l.rstrip() for l in f):
        match = format_pat.match(line)
        if match:
            access = match.groupdict()
            request = access['request']
            fields = request.split()
            if (len(fields) == 3):
                URL = fields[1]

                # python3.* has_key() -> in operator
                # if URLCounts.has_key(URL): 
                if URL in URLCounts:
                    URLCounts[URL] = URLCounts[URL] + 1
                else:
                    URLCounts[URL] = 1
                    
results = sorted(URLCounts, key = lambda i: int(URLCounts[i]), reverse = True)
for result in results[:20]:
    print(result + ": " + str(URLCounts[result]))
                   
