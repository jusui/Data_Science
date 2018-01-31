# coding: utf-8
import pandas as pd

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('~/work/python/DataScience/ml-100k/u.data', sep = '\t', names = r_cols, usecols = range(3), encoding = 'latin-1')

m_cols = ['movie_id', 'title']
movies = pd.read_csv('~/work/python/DataScience/ml-100k/u.item', sep = '|', names = m_cols, usecols = range(2), encoding = 'latin-1')

ratings = pd.merge(ratings, movies)
print(ratings.head())

# pivot_table() でユーザとユーザが評価した映画のMatrixを作る.NaNはデータなしか未鑑賞.
userRatings = ratings.pivot_table(index = ['user_id'], columns = ['title'], values = 'rating')
print(userRatings.head())

# pd.corrwith() でMatrixすべての映画のペア相関スコアを計算.
# 少なくとも一人が両者の映画位を評価している必要があり,それ以外はNaN表示
corrMatrix = userRatings.corr()
print(corrMatrix.head())

# 少数ユーザによるレアケースを除外, 評価の数は100に指定
corrMatrix = userRatings.corr(method = 'pearson', min_periods = 100)
print(corrMatrix.head())


"""
ID=0のユーザに映画のレコメンドしてみる
傾向：StarWars帝国の逆襲が大好き,風と共に去りぬが大嫌い

"""
# userRatingsのDFから評価を取り出し,dropna()でNaN除外
myRatings = userRatings.loc[0].dropna()
print(myRatings)

"""
(1). ID=0のユーザ評価を元に,レコメンドを作る

ユーザが評点を行った各映画に対して,相関マトリックスから映画の類似度リストを取り出す.
類似度とユーザの評点をかけてオススメ度とし,候補に加える.
ユーザが高く評価した映画に似た別の映画のオススメ度は高くなる

"""
simCandidates = pd.Series()
for i in range(0, len(myRatings.index)):
    print("Adding sims for" + myRatings.index[i] + "...")

    # 過去に評価した映画に似た別の映画を探す
    sims = corrMatrix[myRatings.index[i]].dropna()

    # 評点で類似度をスケール
    sims = sims.map(lambda x: x * myRatings[i])

    # 類似候補のリストにsimsのスコアを追加
    simCandidates = simCandidates.append(sims)

# Glance at our result so far:
print("sorting...")
simCandidates.sort_values(inplace = True, ascending = False)
print(simCandidates.head(10))



"""
2回以上見える同じ映画があるため,groupby() でスコアを足し合わせる

"""
simCandidates = simCandidates.groupby(simCandidates.index).sum()

simCandidates.sort_values(inplace = True, ascending = False)
print(simCandidates.head(10))

# 最後に既に評価した映画を除外する.
filterSims = simCandidates.drop(myRatings.index)
print(filterSims.head(10))


import matplotlib.pyplot as plt
import seaborn as sns


sns.pairplot(ratings)
plt.show()
