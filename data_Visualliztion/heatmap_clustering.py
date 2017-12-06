import numpy as np
from numpy.random import randn
import pandas as pd

from scipy import stats

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

"""
Heatmap & clustering method
http://www.tsjshg.info/udemy/Lec53.html

"""

flight_dframe = sns.load_dataset('flights')

## make a pivot table
flight_dframe = flight_dframe.pivot('month', 'year', 'passengers')
print(flight_dframe)

## Make a heatmap with sns.heatmap()
sns.heatmap(flight_dframe)

## annotation = True : draw number in the pixels
sns.heatmap(flight_dframe, annot = True, fmt = 'd')

## change heatmap color
# [1955, Jan.] = 242を基準に色を変える
sns.heatmap(flight_dframe, center = flight_dframe.loc['January', 1955])

# ヨコに並べる
f, (axis1, axis2) = plt.subplots(2, 1)

yearly_flights = flight_dframe.sum()
years = pd.Series(yearly_flights.index.values)
years = pd.DataFrame(years)

flights = pd.Series(yearly_flights.values)
flights = pd.DataFrame(flights)

year_dframe = pd.concat((years, flights), axis = 1)
year_dframe.columns = ['Year', 'Flights']

sns.barplot('Year', y = 'Flights', data = year_dframe, ax = axis1)

# colorbar = cbar_kws
sns.heatmap(flight_dframe, cmap = 'Blues', ax = axis2, cbar_kws = {'orientation':'horizontal'})


"""
Clustering
"""
# 樹形図で親和性の高い変数をまとめる
sns.clustermap(flight_dframe)

sns.clustermap(flight_dframe, col_cluster = False)

# dataを規格化して統計量の影響を抑える
# 列方向をスケールする
sns.clustermap(flight_dframe, standard_scale = 1)

# 行方向をスケールする
sns.clustermap(flight_dframe, standard_scale = 0)

### z_score : データから平均値を引いて標準偏差で割る
# データの全体の標準偏差が1になるので、比較しやすい
sns.clustermap(flight_dframe, z_score = 1, cmap = 'Blues_r')

plt.show()
