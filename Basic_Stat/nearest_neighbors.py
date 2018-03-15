#coding: utf-8
from collections import Counter
import math,random
from stats import mean
from linear_algebra.linear_algebra import distance
import matplotlib.pyplot as plt

"""
[DS from scratch]12.K Nearest Neighbors
"""

def raw_majority_vote(labels):
    """多数決を行う関数"""
    votes = Counter(labels)
    winner, _ = votes.most_common(1)[0] # 最も多くカウントしたlabelのkeyを返す
    return winner

def majority_vote(labels):
    """ラベルは近いものから遠いものへ整列していると想定する"""
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len([count
                       for count in vote_counts.values()
                       if count == winner_count]) # 最頻値と一致するものの数
    if num_winners == 1: # unique winner
        return winner
    else:
        return majority_vote(labels[:-1]) # 最も遠いものを除外して再度試行

def knn_classify(k, labeled_points, new_point):
    """ラベル付きデータポイントは，(point, label)のペアになっている"""

    # ラベル付きデータポイントを近いものから順に並べる
    by_distance = sorted(labeled_points,
                         key = lambda point_label: distance(point_label[0], new_point))
    # 近い順にk個取り出す
    k_nearest_labels = [label for _, label in by_distance[:k]]

    # 多数決を行う
    return majority_vote(k_nearest_labels)


cities = [(-86.75,33.5666666666667,'Python'),(-88.25,30.6833333333333,'Python'),(-112.016666666667,33.4333333333333,'Java'),(-110.933333333333,32.1166666666667,'Java'),(-92.2333333333333,34.7333333333333,'R'),(-121.95,37.7,'R'),(-118.15,33.8166666666667,'Python'),(-118.233333333333,34.05,'Java'),(-122.316666666667,37.8166666666667,'R'),(-117.6,34.05,'Python'),(-116.533333333333,33.8166666666667,'Python'),(-121.5,38.5166666666667,'R'),(-117.166666666667,32.7333333333333,'R'),(-122.383333333333,37.6166666666667,'R'),(-121.933333333333,37.3666666666667,'R'),(-122.016666666667,36.9833333333333,'Python'),(-104.716666666667,38.8166666666667,'Python'),(-104.866666666667,39.75,'Python'),(-72.65,41.7333333333333,'R'),(-75.6,39.6666666666667,'Python'),(-77.0333333333333,38.85,'Python'),(-80.2666666666667,25.8,'Java'),(-81.3833333333333,28.55,'Java'),(-82.5333333333333,27.9666666666667,'Java'),(-84.4333333333333,33.65,'Python'),(-116.216666666667,43.5666666666667,'Python'),(-87.75,41.7833333333333,'Java'),(-86.2833333333333,39.7333333333333,'Java'),(-93.65,41.5333333333333,'Java'),(-97.4166666666667,37.65,'Java'),(-85.7333333333333,38.1833333333333,'Python'),(-90.25,29.9833333333333,'Java'),(-70.3166666666667,43.65,'R'),(-76.6666666666667,39.1833333333333,'R'),(-71.0333333333333,42.3666666666667,'R'),(-72.5333333333333,42.2,'R'),(-83.0166666666667,42.4166666666667,'Python'),(-84.6,42.7833333333333,'Python'),(-93.2166666666667,44.8833333333333,'Python'),(-90.0833333333333,32.3166666666667,'Java'),(-94.5833333333333,39.1166666666667,'Java'),(-90.3833333333333,38.75,'Python'),(-108.533333333333,45.8,'Python'),(-95.9,41.3,'Python'),(-115.166666666667,36.0833333333333,'Java'),(-71.4333333333333,42.9333333333333,'R'),(-74.1666666666667,40.7,'R'),(-106.616666666667,35.05,'Python'),(-78.7333333333333,42.9333333333333,'R'),(-73.9666666666667,40.7833333333333,'R'),(-80.9333333333333,35.2166666666667,'Python'),(-78.7833333333333,35.8666666666667,'Python'),(-100.75,46.7666666666667,'Java'),(-84.5166666666667,39.15,'Java'),(-81.85,41.4,'Java'),(-82.8833333333333,40,'Java'),(-97.6,35.4,'Python'),(-122.666666666667,45.5333333333333,'Python'),(-75.25,39.8833333333333,'Python'),(-80.2166666666667,40.5,'Python'),(-71.4333333333333,41.7333333333333,'R'),(-81.1166666666667,33.95,'R'),(-96.7333333333333,43.5666666666667,'Python'),(-90,35.05,'R'),(-86.6833333333333,36.1166666666667,'R'),(-97.7,30.3,'Python'),(-96.85,32.85,'Java'),(-95.35,29.9666666666667,'Java'),(-98.4666666666667,29.5333333333333,'Java'),(-111.966666666667,40.7666666666667,'Python'),(-73.15,44.4666666666667,'R'),(-77.3333333333333,37.5,'Python'),(-122.3,47.5333333333333,'Python'),(-89.3333333333333,43.1333333333333,'R'),(-104.816666666667,41.15,'Java')]
cities = [([longitude, latitude], language) for longitude, latitude, language in cities]

def plot_state_borders(plt, color = '0.8'):
    pass

def plot_cities():
    # 値を座標値(緯度，経度)の辞書
    plots = { "Java" : ([], []), "Python" : ([], []), "R" : ([], []) }

    # 異なる言語には，異なる色と形のマークを使う
    markers = { "Java" : "o", "Python" : "s", "R" : "^" }
    colors  = { "Java" : "r", "Python" : "b", "R" : "g" }

    for (longitude, latitude), language in cities:
        plots[language][0].append(longitude)
        plots[language][1].append(latitude)

    # 言語ごとに，散布図を作る
    for language, (x, y) in plots.items():
        plt.scatter(x, y, color = colors[language], marker = markers[language],
                    label = language, zorder = 10)

    plot_state_borders(plt)

    plt.legend(loc = 0)
    plt.axis([-130, -60, 20, 55]) # 座標軸の設定

    plt.title("Favorite Programming Languages")
    plt.show()


def classify_and_plot_grid(k = 1): # default = 1
    """全体を格子に分割し，
    それぞれの点で予測された言語を大都市の例と同じようにプロット"""
    
    plots   = { "Java" : ([], []), "Python" : ([], []), "R" : ([], []) }
    markers = { "Java" : "o", "Python" : "s", "R" : "^" }
    colors  = { "Java" : "r", "Python" : "b", "R" : "g" }

    for longitude in range(-130, -60):
        for latitude in range(20, 55):
            predicted_language = knn_classify(k, cities, [longitude, latitude])
            plots[predicted_language][0].append(longitude)
            plots[predicted_language][1].append(latitude)

    for language, (x, y) in plots.items():
        plt.scatter(x, y, color = colors[language], marker = markers[language],
                    label = language, zorder = 0)

    plot_state_borders(plt, color = 'Black')

    plt.legend(loc = 0)
    plt.axis([-130, -60, 20, 55])

    plt.title(str(k) +" Nearest Neighbor Programming Language")
    plt.show()

def random_point(dim):
    # 無作為な点の生成
    return [random.random() for _ in range(dim)]

def random_distances(dim, num_pairs):
    # 無作為な点の間の距離を生成
    return [distance(random_point(dim), random_point(dim))
            for _ in range(num_pairs)]

    
if __name__ == '__main__':

    # 異なるkの値を試す
    for k in [1, 3, 5, 7]:
        num_correct = 0

        for location, actual_language in cities:
            
            other_cities = [other_city
                            for other_city in cities
                            if other_city != (location, actual_language)]

            predicted_language = knn_classify(k, other_cities, location)

            if predicted_language == actual_language:
                num_correct += 1

        # print(k, "neighbors[s]:", num_correct, "correct out of", len(cities))

    dimensions = range(1, 101)

    avg_distances = []
    min_distances = []

    random.seed(0)
    for dim in dimensions:
        distances = random_distances(dim, 10000) # 10000個の無作為点間の距離
        avg_distances.append(mean(distances)) # 平均
        min_distances.append(min(distances))  # min value
        print(dim, min(distances), mean(distances), min(distances) / mean(distances))

    min_avg_ratio = [min_distances / avg_distances
                     for min_distances, avg_distances
                     in zip(min_distances, avg_distances)]

    print("高次元では，2点間の距離も増加するため，最低値と平均の比はより深刻になる")
    print(min_avg_ratio)
    print()

    # plot Favorite programming languages
    plot_cities()
    classify_and_plot_grid()

    plt.plot(dimensions, avg_distances, color = 'g', label = 'average distance')
    plt.plot(dimensions, min_distances, color = 'b', label = 'minimum distance')
    plt.title("10000 random distances")
    plt.axis([0, 100, 0.0, 4.5]) # 座標軸の設定
    plt.legend()
    plt.figure()

    plt.plot(dimensions, min_avg_ratio, color = 'b')
    plt.title("Minimum Distance / Average Distance")
    plt.axis([0, 100, 0.0, 0.8]) # 座標軸の設定
    plt.show()
