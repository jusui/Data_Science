# encoding uft-8 
import pandas as pd
from pandas import Series, DataFrame
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

# Data from Web
import requests

# for CSV file
from io import StringIO

"""
US election analysis

Obama(Rep) vs. Romney(Pub)

その1

"""

# Data from this URL
url = "http://elections.huffingtonpost.com/pollster/2012-general-election-romney-vs-obama.csv"

# text として取得
source = requests.get(url).text

# StringIO でpandas errorを防ぐ
poll_data = StringIO(source)

## DataFrame ##
poll_df = pd.read_csv(poll_data)

print(poll_df.info())
# print(poll_df.head())

# 世論調査の主体とその支持政党まとめ
poll_df[['Pollster', 'Partisan', 'Affiliation']].sort('Pollster').drop_duplicates()
print(poll_df.head())

# Classify the affilication.
sns.countplot('Affiliation', data = poll_df)
plt.figure()

# !!調査主体の支持政党を，調査対象で層別化する order = [並び指定]
sns.countplot('Affiliation', data = poll_df, hue = 'Population', \
              order = ['Rep', 'Dem', 'None'])
plt.figure()

# 平均を取ると，数値の列だけが残るので、Number of Observationsを削除
avg = pd.DataFrame(poll_df.mean())
avg.drop('Number of Observations', axis = 0, inplace = True)
print(avg)

# 同様に，std 計算
std = pd.DataFrame(poll_df.std())
std.drop('Number of Observations', axis = 0, inplace = True)
print(std)

# avg, std を使って，Error bar付きのHistogramを作る
avg.plot(yerr = std, kind = 'bar', legend = False)
plt.figure()

# まとめておく
poll_avg = pd.concat([avg, std], axis = 1)

# 名前変更
poll_avg.coulumns = ['Average', 'STD']
print(poll_avg)

plt.show()
