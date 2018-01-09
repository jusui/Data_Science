# coding: utf-8
import pandas as pd

"""
(1).類似した映画を見つける
MoviewLensのデータを読み,Pandasで,今回用いるu.data, u.itemの全ての行を読み,movie_idを用いてデータを結合.

read_csv() するときは, encoding = 'latin-1' しないとencoding error.
https://stackoverflow.com/questions/5552555/unicodedecodeerror-invalid-continuation-byte/31492722#31492722
"""

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('~/work/python/DataScience/ml-100k/u.data', sep = '\t', names = r_cols, usecols = range(3), encoding = 'latin-1')

m_cols = ['movie_id', 'title']
movies = pd.read_csv('~/work/python/DataScience/ml-100k/u.item', sep = '|', names = m_cols, usecols = range(2), encoding = 'latin-1')

ratings = pd.merge(movies, ratings)
print(ratings.head())

# DF.pivot_table() 関数で, user/movie matrix を作る.
movieRatings = ratings.pivot_table(index = ['user_id'], columns = ['title'], values = 'rating')
print(movieRatings.head())

# StarWars を評点したユーザを取り出す
starWarsRatings = movieRatings['Star Wars (1977)']
print(starWarsRatings.head())

# Pandas.corrwith() 関数は,StarWarsのユーザ評点ベクトルと,他の映画の評点ベクトルのペアワイズ相関を計算.
similarMovies = movieRatings.corrwith(starWarsRatings)
similarMovies = similarMovies.dropna() # NaN除外
df = pd.DataFrame(similarMovies) # make DF
print(df.head(10))

# 類似度でソート
print(similarMovies.sort_values(ascending = False)) # 現時点で類似度の高い映画は,見つからない


"""
(2).少数の特異な評点を削除して再度,見積もる


"""
import numpy as np

# 各映画にいくつの評点があるのか,評点の平均値はいくつかを計算するDFを作る(groupby.agg())
# 辞書形式で指定し,(マルチ)カラムごとの個別集計が可能.
# https://qiita.com/kyo-bad/items/f5ddb7e4b8e7ad9103c5#groupbyagg
movieStats = ratings.groupby('title').agg({'rating': [np.size, np.mean]})
print(movieStats.head())


# 評価の数がn (e.g. 100)より大きい映画に絞り,残った映画を上位15評点順に並べる
n = 100   # nを変えて色々見てみる
popularMovies = movieStats['rating']['size'] >= n
topMovie15 = movieStats[popularMovies].sort_values([('rating', 'mean')], ascending = False)[:15]
print(topMovie15)

# もとのStarWars類似映画のセットに['similarity']カラムを追加する
df = movieStats[popularMovies].join(pd.DataFrame(similarMovies, columns = ['similarity']))
print(df.head())

# 類似度スコアでソート
print(df.sort_values(['similarity'], ascending = False)[:15])

