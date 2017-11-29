import numpy as np
from pandas import Series, DataFrame
import pandas as pd

arr = np.array([[1,2, np.nan], [np.nan, 3, 4]])
print(arr)

dframe1 = DataFrame(arr, index = ['A', 'B'], columns = ['One', 'Two', 'Three'])
print(dframe1)

print(dframe1.sum())

# col = 1
print(dframe1.sum(axis=1))

print(dframe1.min())

# 最小値がどのindexか
print(dframe1.idxmin())
print(dframe1.idxmax())

# total
print(dframe1.cumsum())
print(dframe1.describe())


import pandas_datareader.data as pdweb
import datetime
import matplotlib.pyplot as plt

### Orig
# import pandas.io.data as pdweb
# price = pdweb.get_data.yahoo(['CVX', 'XOM', 'BP'], \
#                             start = datetime.datetime(2010, 1,1),\
#                             end = datetime.datetime(2013,1,1)['Adj Close'])

# date
date_from = datetime.date(2010, 1,1)
date_to = datetime.date(2013, 1,1)

# stock list
tickerList = ['CVX', 'XOM', 'BP']
prices = pdweb.DataReader(
    tickerList,
    data_source = 'yahoo',
    start = date_from,
    end = date_to
)

print (prices['Adj Close'])
rets = prices['Adj Close'].pct_change()
print(rets)

### Orig
## prices['Adj Close'].plot() ##
fig = plt.figure()
plt.plot(prices['Adj Close'])

rets_corr = rets.corr()
print(rets_corr)

import seaborn as sns

sns.heatmap(rets.corr())

plt.show()

ser1 = Series(['w', 'w', 'x', 'y', 'z', 'w', 'w', 'b', 'x', 'z', 'a'])
print(ser1)

print(ser1.unique())
print(ser1.value_counts())
