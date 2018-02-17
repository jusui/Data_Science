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


####################
# Books about data
####################


####################
# Books about data
####################

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
    print("month_counts", mount_counts)
    print("weekday_count", weekday_coutns)

    last_5_repositories = sorted(repos,
                                 key = lambda r: r["created_at"],
                                 reverse = True)[:5]

    print("last five languages", [repo["language"]
                                  for repo in last_5_repositories])
    
    
