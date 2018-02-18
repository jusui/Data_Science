# coding: utf-8
from collections import Counter, defaultdict
from functools import partial, reduce
from linear_algebra.linear_algebra import shape, get_row, get_column, make_matrix
from statistics import correlation, standard_deviation, mean
from probability import inverse_normal_cdf
import math, random, csv
import matplotlib.pyplot as plt


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

    
if __name__ == "__main__":

    # histogram
    compare_two_distributions()

    # scatter plot
    scatter()
    
    # 散布図行列
    make_scatterplot_matrix()
