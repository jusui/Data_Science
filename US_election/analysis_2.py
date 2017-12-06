# enconding uft-8
import pandas as pd
from pandas import Series, DataFrame
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

import requests

from io import StringIO

"""
US election analysis

Obama(Rep) vs. Romney(Pub)

その2

"""

# Data from this URL
url = "http://elections.huffingtonpost.com/pollster/2012-general-election-romney-vs-obama.csv"

# text として取得
source = requests.get(url).text

# StringIO でpandas errorを防ぐ
poll_data = StringIO(source)

# DF
poll_df = pd.read_csv(poll_data)

# 世論調査の主体とその支持政党まとめ
poll_df[['Pollster', 'Partisan', 'Affiliation']].sort('Pollster').drop_duplicates()
print(poll_df.head())

# 平均を取ると，数値の列だけが残るので、Number of Observationsを削除
avg = pd.DataFrame(poll_df.mean())
avg.drop('Number of Observations', axis = 0, inplace = True)
print(avg)

# 同様に，std 計算
std = pd.DataFrame(poll_df.std())
std.drop('Number of Observations', axis = 0, inplace = True)
print(std)

# まとめておく
poll_avg = pd.concat([avg, std], axis = 1)

# 名前変更
poll_avg.coulumns = ['Average', 'STD']
print(poll_avg)

