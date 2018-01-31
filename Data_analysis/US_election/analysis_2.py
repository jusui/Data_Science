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

## 選挙戦の最終的な結果を推定していく
print(poll_df.head())

# 支持率 vs. 政党未定
poll_df.plot(x = 'End Date', y = ['Obama', 'Romney', 'Undecided'], \
             marker = 'o', linestyle = '')
# plt.figure()


# 直感的に理解し難いので，別のデータを作って可視化する
# 時系列データ
from datetime import datetime

# dif[%] = (Obama -  Romney) / 100
# ここで絶対値を使わないのは，Obamaを基準として +/- と評価するため
poll_df['Difference'] = (poll_df.Obama - poll_df.Romney) / 100
print(poll_df.head())

# 支持率の"差"の時間変化
# as_index = False, 0,1,2,... のindex を維持する
poll_df = poll_df.groupby(['Start Date'], as_index = False).mean()

fig = poll_df.plot('Start Date', 'Difference', figsize = (12, 4),\
                   marker = 'o', linestyle = '-', color = 'purple')


#.21 討論会のあった日が関係していそうなので，x-axisから直接indexを調べる
discuss_df = poll_df[poll_df['Start Date'].apply(lambda x:x.startswith('2012-10'))]
print(discuss_df)

# Oct, 2012 only plot
fig = poll_df.plot('Start Date', 'Difference', figsize = (12, 4), \
                      marker = 'o', linestyle = '-', color = 'purple',\
                      xlim = (329, 356))

# 討論会の日をかき込む(x = *** がindex で得た番号に相当)
plt.axvline(x = 330, linewidth = 4, color = 'grey')
plt.axvline(x = 337, linewidth = 4, color = 'grey')
plt.axvline(x = 347, linewidth = 4, color = 'grey')

# 討論会の結果が，両者の支持率差に影響を及ぼしていないように見える
# こうしたデータを解釈する際は、様々な要因に注意を払う必要もあります。例えば、これらの世論調査が全米のどの場所で行われたかなども、世論調査の結果に大きく影響します。

plt.show()



