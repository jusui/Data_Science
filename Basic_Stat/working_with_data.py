# coding: utf-8
from collections import Counter, defaultdict
from functools import partial, reduce
from linear_algebra.linear_algebra import shape, get_row, get_column, make_matrix
# vector_mean, vector_sum, dot, magnitude, vecotr_substract, scalar_multiply
from statistics import correlation, standard_deviation, mean
from probability import inverse_normal_cdf

import math, random, csv
import matplotlib.pyplot as plt
import dateutil.parser


"""
[DS from scratch]10.データの操作
"""

def bucketize(point, bucket_size):
    """ pointの値を切り捨ててバケツの下限値に揃える. 
    math.floor(x) : x 以下の最大の整数を返す """
    return bucket_size * math.floor(point / bucket_size)


def make_histogram(points, bucket_size):
    """ pointをバケツに入れて何個入ったか数える """
    return Counter(bucketize(point, bucket_size) for point in points)


def plot_histogram(points, bucket_size, title=""):
    histogram = make_histogram(points, bucket_size)
    plt.bar(list(histogram.keys()), histogram.values(), width = bucket_size)
    plt.title(title)
    plt.show()

def compare_two_distributions():

    random.seed(0)
    # -100から100までの一様分布
    # uniform = [random.randrange(-100, 101) for _ in range(200)]
    uniform = [200 * random.random() - 100 for _ in range(10000)]

    # 平均0, std=57の正規分布
    normal = [57 * inverse_normal_cdf(random.random())
              for _ in range(10000)]

    plot_histogram(uniform, 10, "Uniform Histogram")
    plot_histogram(normal, 10, "Normal Histogram")
    
def random_normal():
    """ 標準正規分布に従う無作為の数を返す """
    return inverse_normal_cdf(random.random())

xs  = [random_normal() for _ in range(1000)]
ys1 = [ x + random_normal() / 2 for x in xs]
ys2 = [-x + random_normal() / 2 for x in xs]


def scatter():
    """ 2-d plot and 相関係数 """
    print("correlation :", correlation(xs, ys1))
    print("correlation :", correlation(xs, ys2))
    plt.scatter(xs, ys1, marker = '.', color = 'blue', label = 'ys1')
    plt.scatter(xs, ys2, marker = '.', color = 'red', label = 'ys2')
    plt.xlabel('xs')
    plt.ylabel('ys')
    plt.legend(loc = 9)
    plt.title("Very Different Joint Distributions")
    plt.show()


def correlation_matrix(data):
    """ i列とj列のデータ間の相関を(i, j)の値とする.
    列数*列数の行列を返す """
    _, num_columns = shape(data)

    def matrix_entry(i, j):
        return correlation(get_column(data, i), get_column(data, j))

    return make_matrix(num_columns, num_columns, matrix_entry)

def make_scatterplot_matrix():

    # first, generate some random data
    num_points = 100

    def random_row():
        row = [None, None, None, None]
        row[0] = random_normal()
        row[1] = -5 * row[0] + random_normal()
        row[2] = row[0] + row[1] + 5 * random_normal()
        row[3] = 6 if row[2] > -2 else 0
        return row

    random.seed(0)
    data = [random_row()
            for _ in range(num_points)]

    # then plot it
    _, num_columns = shape(data)
    fig, ax = plt.subplots(num_columns, num_columns)

    for i in range(num_columns):
        for j in range(num_columns):

            # X軸のcolumn_j, Y軸のcolumn_iの位置に散布図を描画する
            if i != j: ax[i][j].scatter(get_column(data, j), get_column(data, i))

            # i == jであれば，列名を表示する
            else: ax[i][j].annotate("series " + str(i), (0.5, 0.5),
                                    xycoords = 'axes fraction',
                                    ha = "center", va = "center")

            # 左端と一番下のサブプロット以外は，軸ラベルを表示しない
            if i < num_columns - 1: ax[i][j].xaxis.set_visible(False)
            if j > 0: ax[i][j].yaxis.set_visible(False)

    # 右下と左下のサブプロットは，テキストのみ表示しているため，
    # 軸ラベルが誤っている．ここで修正する
    ax[-1][-1].set_xlim(ax[0][-1].get_xlim())
    ax[0][0].set_ylim(ax[0][1].get_ylim())

    plt.show()

def parse_row(input_row, parsers):
    """ 与えられたパーサのリスト(その内幾つかはNone)
    の中から列ごとに適切する """
    return [parser(value) if parser is not None else value
            for value, parser in zip(input_row, parsers)]

def parse_rows_with(reader, parsers):
    """ readerをラップして入力の各列にパーサを適用する """
    for row in reader:
        yield parse_row(row, parsers)

def try_or_none(f):
    """ 関数fが例外の場合は，Noneを返す. fは1つの入力を想定する """
    def f_or_none(x):
        try:
            return f(x)
        except:
            return None
    return f_or_none

def parse_row(input_row, parsers):
    return [try_or_none(parser)(value) if parser is not None else value
            for value, parser in zip(input_row, parsers)]

def try_parse_field(field_name, value, parser_dict):
    """ parser_dictの適切な関数を使って値を解釈する """
    parser = parser_dict.get(field_name) # 対応する値がなければNoneが返る
    if parser is not None:
        return try_or_none(parser)(value)
    else:
        return value

def parse_dict(input_dict, parser_dict):
    return { field_name : try_parse_field(field_name, value, parser_dict)
             for field_name, value in input_dict.items() }


############
# Manipulating data
############



if __name__ == "__main__":

    # histogram
    compare_two_distributions()

    # scatter plot
    scatter()
    
    # 散布図行列
    make_scatterplot_matrix()

    # safe parsing
    data = []

    with open("comma_delimited_stock_prices.csv", "r", encoding = "utf-8", newline = '') as f:
        reader = csv.reader(f)
        for line in parse_rows_with(reader, [dateutil.parser.parse, None, float]):
            data.append(line)

        for row in data:
            if any(x is None for x in row):
                print(row)

        print("stocks")
        with open("stocks.txt", "r", encoding = "utf-8", newline = '') as f:
            reader = csv.DictReader(f, delimiter = "\t")
            data = [parse_dict(row, {'date' : dateutil.parser.parse,
                                     'closing_price' : float})
                    for row in reader]

        max_aapl_price = max(row["closing_price"]
                             for row in data
                             if row["symbol"] == "AAPL")
        print("max aapl price", max_aapl_price)

        # group rows by symbol
        by_symbol = defaultdict(list)

        for row in data:
            by_symbol[row["symbol"]].append(row)

        # use a dict comprehension to find the max for each symbol
        max_price_by_symbol = { symbol : max(row["closing_price"]
                                             for row in grouped_rows)
                                for symbol, grouped_rows in by_symbol.items() }

        print("max price by symbol")
        print(max_price_by_symbol)
