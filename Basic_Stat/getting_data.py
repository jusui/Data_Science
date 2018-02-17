# coding: utf-8
from collections import Counter
import math, random, csv, json, re

from bs4 import BeautifulSoup
import requests

import matplotlib.pyplot as plt
####################
# Books about data
####################
def is_video(td):
    """ pricelabelを1つだけ持ち，
    空白を取り除いた文字列が'Video'ならビデオである """
    pricelabels = td('span', 'pricelabel')
    return (len(pricelabels)  == 1 and
            pricelabels[0].text.strip().stratswith("Video"))


def book_info(td):
    """ 与えられた<td>タグが，1冊の書籍情報を表現している。
    ここから書籍の詳細を抜き出して、　辞書として返す """
    title = td.find("div", "thumbheader").a.text
    by_author = td.find('div', 'AuthorName').text
    authors = [x.strip() for x in re.sub("^By ", "", by_author).split(",")]
    isbn_link = td.find("div", "thumbheader").a.get("href")
    isbn = re.match("/product/(.*)\.do", isbn_link).groups()[0]
    date = td.find("span", "directorydate").text.strip()

    return {
        "title" : title,
        "authors" : authors,
        "isbn" : isbn,
        "date" : date
    }


from time import sleep

def scrape(num_pages = 31):
    base_url = "http://shop.oreilly.com/category/browse-subjects/" + \
               "data.do?sortby=publicationDate&page="

    books = []

    for page_num in range(1, num_pages + 1):
        print("souping page", page_num)
        url = base_url + str(page_num)
        soup = BeautifulSoup(requests.get(url).text, 'html5lib')

        for td in soup('td', 'thumbtext'):
            if not is_video(td):
                books.append(book_info(td))
    
        # robots.txtの内容を尊重する
        sleep(30)


    return books


def get_year(book):
    """ book["date"]の値は，例えば'November 2014'の形式であるため，
    空白で分割し，2つ目の要素を取り出す """
    return int(bokk["date"].split()[1])


def plot_years(plt, books):
    """ 1年分のデータが揃っているのは2014年まで """
    years_counts = Counter(get_year(book) for book in books
                           if get_year(book) <= 2014)

    years = sorted(year_counts)
    book_counts = [year_counts[year] for year in x]
    plt.bar([x - 0.5 for x in years], book_counts)
    plt.xlabel("year")
    plt.ylabel("# of data books")
    plt.title("Data is Big!")
    plt.show()

    
####################
# APIs
####################
endpoint = "https://api.github.com/users/jusui/repos"

repos = json.loads(requests.get(endpoint).text)

from dateutil.parser import parse

dates = [parse(repo["created_at"]) for repo in repos ]
month_counts = Counter(date.month for date in dates)
weekday_counts = Counter(date.weekday() for date in dates)


####################
# Twitter
####################
from twython import Twython

# fill these in if you want to use the code
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

def call_twitter_search_api():

    twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET)

    # search for tweets containing the phrase "data science"
    for status in twitter.search(q = '"data science"')["statuses"]:
        user = status["user"]["screen_name"].encode('utf-8')
        text = status["text"].encode('utf-8')
        print(user, ":", text)
        print()

from twython import TwythonStreamer
""" Twythonを継承するクラスを作り，on_success method(and on_error method)をオーバーライドする
データを大域変数に格納するのは稚拙な方法であるが，サンプルコードを単純化できる """
tweets = []

class MyStreamer(TwythonStreamer):
    """ streamとやり取りを行う方法を定義するTwythonStreamerのサブクラス """
    
    def  on_success(self, data):
        """ Twitterがデータを送ってきたらどう対処する?
        ここでdataは，tweetを表すPython辞書として渡される """

        # 英語Tweetのみ対称
        if data['lang'] == 'en':
            tweets.append(data)
            print("received tweet #", len(tweets))

        # 十分なtweetsを得たら終了
        if len(tweets) >= 1000:
            self.disconnect()

    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()

def call_twitter_streaming_api():
    """ MyStreamerは，Twitterストリームに接続してデータを受け取ると，
    on_success methodが呼ばれ英語のtweetであればtweetsリストに追加される．"""

    # 1000 tweets超えるとstream切断して終了
    stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # 公開されているtweet(statuses)からキーワード 'data'を持つものを収集する
    stream.statuses.filter(track = 'data')

    # 全てのtweet(statuses)の中からランダムに収集を行うには，次を使う
    # stream.statuses.sample()
    

if __name__ == '__main__':

    def process(date, symbol, price):
        print(date, symbol, price)

    print("tab delimited stock price:")

    with open('tab_delimited_stock_prices.txt', 'r', encoding = "utf-8", newline = '') as f:
        reader = csv.reader(f, delimiter = '\t')
        for row in reader:
            date = row[0]
            symbol = row[1]
            closing_price = float(row[2])
            process(date, symbol, closing_price)

    print()

    print("colon delimited stock prices:")

    with open('colon_delimited_stock_prices.txt', 'r', encoding = "utf-8", newline = '') as f:
        reader = csv.DictReader(f, delimiter = ':')
        for row in reader:
            date = row["date"]
            symbol = row["symbol"]
            closing_price = float(row["closing_price"])
            process(date, symbol, closing_price)
            
    print()
            
    print("writing out comma_delimited_stock_prices.txt")

    today_prices = {'AAPL' : 90.91, 'MSFT' : 41.68, 'FB' : 64.5}

    with open('comma_delimited_stock_prices.txt', 'w', encoding = "utf-8", newline = '') as f:
        writer = csv.writer(f, delimiter = ',')
        for stock, price in today_prices.items():
            writer.writerow([stock, price])

    print("BeautifulSoup")
    html = requests.get("http://www.example.com").text
    soup = BeautifulSoup(html)
    print(soup)
    print()

    print("parsing json")

    serialized = """{ "title" : "Data Science Book",
    "author" : "Joel Grus",
    "publicationYear" : 2014,
    "topics" : ["data", "science", "data science"] }"""

    # parse the JSON to create a Python object
    deserialized = json.loads(serialized)
    if "data science" in deserialized["topics"]:
        print(deserialized)

    print()

    print("Github API")
    print("dates", dates)
    print("month_counts", month_counts)
    print("weekday_count", weekday_counts)
    
    # 最後の5つのリポジトリについて，プログラミング言語の種類を取り出す
    last_5_repositories = sorted(repos,
                                 key = lambda r: r["created_at"],
                                 reverse = True)[:5]

    print("last five languages", [repo["language"]
                                  for repo in last_5_repositories])
    
    

    top_hashtags = Counter(hashtag['text'].lower()
                           for tweet in tweets
                           for hashtag in tweet["entities"]["hashtags"])

    print(top_hashtags.most_common(5))
