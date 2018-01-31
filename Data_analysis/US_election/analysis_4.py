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

その4

両陣営への寄付に関するデータ解析

1.) 寄付の金額とその平均的な額
2.) 候補者ごとの寄付の違い
3.) 民主党と共和党での寄付の違い
4.) 寄付した人々の属性について
5.) 寄付の総額になんらかのパターンがあるか？

"""

# Read CSV data file
donor_df = pd.read_csv('Election_Donor_Data.csv')
print(donor_df.info())
print(donor_df.head())

# 寄付総額
donor_contb = donor_df['contb_receipt_amt'].value_counts()
print(donor_contb)

# 種類が多いので，代表値を抽出
# 平均と標準偏差
don_mean = donor_df['contb_receipt_amt'].mean()
don_std = donor_df['contb_receipt_amt'].std()

print('寄付の平均は{:0.2f}$で, 標準偏差は{:0.2f}'.format(don_mean, don_std))

# DataFrameのある1列から，Seriesを作る
top_donor = donor_df['contb_receipt_amt'].copy()

# Sort
top_donor.sort()
print(top_donor)

# 負の数を除外し，ソート
top_donor = top_donor[top_donor > 0]
top_donor.sort()

# 寄付額 Top10
top_donor.value_counts().head(10)
print('寄付額Top10は，{}'.format(top_donor))

# histogram(10 < $ < 2500)
com_don = top_donor[top_donor < 2500]

# Histogram with binning (bins = 100)     
com_don.hist(bins = 100)

"""

政党毎に寄付額のをまとめてみる
(1). 候補者の所属政党でデータを分類

"""

# 重複のない候補者データを作成 (unique())
candidates = donor_df.cand_nm.unique()
print(candidates)

# Party 列の作成 (Democrat : 民主党 は，Obamaのみ)
party_map = {'Bachmann, Michelle':  'Republican',
             'Cain, Herman': 'Republican',
             'Gingrich, Next' : 'Republican',
             'Huntsman, Jon' : 'Republican',
             'Johnson, Gary Ealy' : 'Republican',
             'McCotter, Thaddeus G' : 'Republican',
             'Obama, Barack' : 'Democrat',
             'Paul, Ron' : 'Republican',
             'Pawlenty, Timothy' : 'Republican',
             'Perry, Rick' : 'Republican',
             "Roemer, Charles E. 'Buddy' III" : 'Republican',
             'Romney, Mitt' : 'Republican',
             'Santorum, Rick' : 'Republican' }

# DF 全体に政党カラムを追加して更新
donor_df['Party'] = donor_df.cand_nm.map(party_map)
print(donor_df)

# 払い戻しの除去
donor_df = donor_df[donor_df.contb_receipt_amt > 0]
print(donor_df.head())

# 候補者の名前でグループ化した後，それぞれの寄付件数を表示
# Column('cand_nm') を基準に，cand_nm(候補者名),  countb_receipt_amt(寄付件数)でグループ化
donor_df_count =  donor_df.groupby('cand_nm')['contb_receipt_amt'].count()
print(donor_df_count)

# Obama 圧勝，寄付総額
# Column('cand_nm') を基準に，countb_receipt_amt 寄付総額でグループ化
donor_df_sum = donor_df.groupby('cand_nm')['contb_receipt_amt'].sum()
print(donor_df_sum)

# 結果の整理
# Dataの準備
cand_amount = donor_df.groupby('cand_nm')['contb_receipt_amt'].sum()

# index access用の変数
i = 0

# Visuallization (E8 $)
cand_amount.plot(kind = 'bar')
plt.figure()

# 政党ごとの寄付額
donor_df.groupby('Party')['contb_receipt_amt'].sum().plot(kind = 'bar')
plt.figure()

# 寄付した人の職業まとめ
# vibot_table で，職業と政党別に分けて寄付額をまとめる
occupation_df = donor_df.pivot_table('contb_receipt_amt', \
                                     index = 'contbr_occupation', \
                                     columns = 'Party', aggfunc = 'sum')

print(occupation_df.head())
print(occupation_df.shape)

# 1000000 $ 以上の寄付をした場合に絞る 
ocuupation_df = occupation_df[occupation_df.sum(1) > 1000000]

# size 確認
print(occupation_df.shape)

# pandas でbar plot
occupation_df.plot(kind = 'bar')
plt.figure()

# 職業無回答 = INFORMATION REQUESTED PER BEST EFFORTS を除去
occupation_df.drop(['INFORMATION REQUESTED PER BEST EFFORTS', 'INFORMATION REQUESTED'], axis = 0, inplace = True)

# CEO と C.E.O は同じ意味なのでまとめる
occupation_df.loc['CEO'] = occupation_df.loc['CEO'] + occupation_df.loc['C.E.O.']
occupation_df.drop('C.E.O.', inplace = True)

# pandas でbar plot (horizontal)
occupation_df.plot(kind = 'barh', figsize = (10, 12), cmap = 'seismic')

plt.show()

