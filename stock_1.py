import pandas as pd
from pandas import Series, DataFrame
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

from pandas.io.data import DataReader
from pandas_datareader import data

from datetime import datetime

tech_list = ['AAPL', 'GOOG', 'MSFT', 'AMZN']

end_date = datetime.today()
# end_date = datetime.now()
start_date = datetime(end_date.year - 1, end_date.month, end_date.day)

## new library
for stock in tech_list:
    globals()[stock] = data.DataReader(
        stock,
        'yahoo',
        start_date,
        end_date
    )
#    print(AAPL.describe())

## information
print(AAPL.info())

## 時系列データ 終値 = Adjust Close
AAPL['Adj Close'].plot(legend = True, figsize = (10, 4))
plt.figure()

AAPL['Volume'].plot(legend = True, figsize = (10, 4))
# plt.figure()

## **day 移動平均(ma : moving array)
ma_day = [10, 20, 50]
for ma in ma_day:
    column_name = 'MA {}'.format(ma)
    AAPL[column_name] = pd.rolling_mean(AAPL['Adj Close'], ma)

print(AAPL.head())

## plot 10, 20, 50 days later
# 10 から変動が始まる
AAPL[['Adj Close', 'MA 10', 'MA 20', 'MA 50']].plot(subplots = False, figsize = (10, 4))
plt.figure()

## compare today vs. yesterday[Adj Close]
AAPL['Daily Return'] = AAPL['Adj Close'].pct_change()
print(AAPL['Daily Return'].head())

AAPL['Daily Return'].plot(figsize = (10, 4), legend = True, linestyle = '--', marker = 'o')
plt.figure()

## KDE 
sns.distplot(AAPL['Daily Return'].dropna(), bins = 100, color = 'purple')
plt.figure()

AAPL['Daily Return'].hist(bins = 100)
plt.figure()

### ==============
### Closing DF ###
### ==============
closing_df = data.DataReader( tech_list,
                              data_source = 'yahoo',
                              start = start_date,
                              end = end_date) ['Adj Close']
print(closing_df.head())

## % 変化 / day
tech_rets = closing_df.pct_change()
print(tech_rets.head())


## Google同士の相関
sns.jointplot('GOOG', 'GOOG', tech_rets, kind = 'scatter', color = 'green')

## Google vs. MS (pearson 相関係数 p = 1)
sns.jointplot('GOOG', 'MSFT', tech_rets, kind = 'scatter', color = 'green')

## Google vs. Apple (pearson 相関係数 p = 1)
sns.jointplot('GOOG', 'APPL', tech_rets, kind = 'scatter', color = 'green')

## Google vs. Amazon (pearson 相関係数 p = 1)
sns.jointplot('GOOG', 'AMZN', tech_rets, kind = 'scatter', color = 'green')


plt.show()
