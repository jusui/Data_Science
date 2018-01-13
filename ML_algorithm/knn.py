# coding : utf-8
import pandas as pd

"""
[KNN:K近傍法]
データセットの中から、K個の最も近いアイテムを見つけます。
それらのアイテムに”投票”させることにより、新しいデータの属性を予測します。 

"""

# MovieLensのsample データでDFを作る
r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('~/work/python/DataScience/ml-100k/u.data', \
                      sep = '\t', names = r_cols, usecols = range(3), encoding = 'latin-1')
print(ratings.head())

# movie_idでグループ化，評点の総数と評点の平均値を計算
import numpy as np
movieProperties = ratings.groupby('movie_id').agg({'rating': [np.size, np.mean]})
print(movieProperties.head())

# DFを新たに正規化して，評点を評価しやすく変形する(0 =< 評点 =< 1)
movieNumRatings = pd.DataFrame(movieProperties['rating']['size'])
movieNormalizedNumRatings = movieNumRatings.apply( lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)) )
print(movieNormalizedNumRatings.head())

# u.itemからジャンルの情報を取得する
movieDict = {}
with open(r'/Users/usui/work/python/DataScience/ml-100k/u.item', encoding = 'latin-1') as f:
    temp = ''
    for line in f:
        fields = line.rstrip('\n').split('|')
        movieID = int(fields[0])
        name = fields[1]
        genres = fields[5:25]
        # https://stackoverflow.com/questions/35691489/error-in-python-3-5-cant-add-map-results-together
        genres = list(map(int, genres)) # python-3系では，type(map())はclass mapで返すので，list(map())で配列に格納
        movieDict[movieID] = (name, genres, movieNormalizedNumRatings.loc[movieID].get('size'), \
                              movieProperties.loc[movieID].rating.get('mean'))

# 'Toy Story (1995)'
print("name, genres, 正規化したsize, 正規化したmean")
print(movieDict[1])


# ジャンル・人気の類似度を，距離で計算するための関数を定義
from scipy import spatial

def ComputeDistance(a, b):
    genresA = a[1]
    genresB = b[1]
    genreDistance = spatial.distance.cosine(genresA, genresB)
    popularityA = a[2]
    popularityB = b[2]
    popularityDistance = abs(popularityA - popularityB)
    return genreDistance + popularityDistance

# ID2, 4の映画の距離を計算, map()通しでは計算不可->list()通しで計算
print(ComputeDistance(movieDict[2], movieDict[4]))

# print("movieDict =", movieDict)
print("movieDict[2] =", movieDict[2])
print("movieDict[4] =", movieDict[4])


"""
getNeighbors関数
(1)Toy Story とデータセット内の他の全ての映画との距離を計算
(2)距離でソートし，K個の最も距離の近い映画を取得

"""
import operator

def getNeighbors(movieID, K):
    distances = []
    for movie in movieDict:
        if (movie != movieID): # movieID = 1(Toy Story)以外のIDとの距離を計算
            dist = ComputeDistance(movieDict[movieID], movieDict[movie])
            distances.append((movie, dist)) # total size = 1681

    distances.sort(key = operator.itemgetter(1)) # 距離でソート
    neighbors = []
    for x in range(K):
        neighbors.append(distances[x][0])

    return neighbors
        
K = 10
avgRating = 0
neighbors = getNeighbors(1, K)
for neighbor in neighbors:
    avgRating += movieDict[neighbor][3]
    print(movieDict[neighbor][0] + " " + str(movieDict[neighbor][3]))

avgRating /= float(K)

print("")
print("10個の最近傍の映画の平均評点")
print("avgRating =", avgRating)

# Toy storyの平均評点と比較
print("Toy storyの平均評点 =", movieDict[1][3])

print("Toy storyの平均評点と比較 = ", avgRating / movieDict[1][3] )
