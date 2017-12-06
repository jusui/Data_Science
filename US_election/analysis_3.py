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

その3

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

plt.show()

