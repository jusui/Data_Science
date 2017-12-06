import pandas as pd
from pandas import Series, DataFrame
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

# from pandas.io.data import DataReader
from pandas_datareader import data

# from datetime import datetime
import datetime

tech_list = ['AAPL', 'GOOG', 'MSFT', 'AMZN']

end_date = datetime.date(2017, 12, 5)
start_date = datetime.date(2017, 1, 1)
# end_date = datetime.today()
# end_date = datetime.now()
# start_date = datetime.date(end_date.year - 1, end_date.month, end_date.day)
# start_date = datetime.date(2010, 1,1)

## new library
for stock in tech_list:
    globals()[stock] = data.DataReader(
        stock,
        'yahoo',
        start_date,
        end_date
    )

print(AAPL.describe())

## **day 移動平均(ma : moving array)
ma_day = [10, 20, 50]
for ma in ma_day:
    column_name = 'MA {}'.format(ma)
    AAPL[column_name] = pd.rolling_mean(AAPL['Adj Close'], ma)

    
"""
株式市場その2
"""

## compare today vs. yesterday[Adj Close]
AAPL['Daily Return'] = AAPL['Adj Close'].pct_change()
# print(AAPL['Daily Return'].head())

### ==============
### Closing DF ###
### ==============
closing_df = data.DataReader( tech_list,
                              data_source = 'yahoo',
                              start = start_date,
                              end = end_date) ['Adj Close']

## Def : 変化率[%] / day
tech_rets = closing_df.pct_change()
print(tech_rets.head())

# ## Google vs. MS 
# sns.jointplot('GOOG', 'MSFT', tech_rets, kind = 'scatter', color = 'green')


"""
株式市場その3

4社のデータを比較するplotを考える

"""

# sns.pairplot(tech_rets.dropna())

## 前日との比較
# returns_fig = sns.PairGrid(tech_rets.dropna())
# returns_fig.map_upper(plt.scatter, color = 'purple')
# returns_fig.map_lower(sns.kdeplot, cmap = 'cool_d')
# returns_fig.map_diag(plt.hist, bins = 30)
# plt.figure()

## 同様に終値で比較する
# returns_fig = sns.PairGrid(closing_df)
# returns_fig.map_upper(plt.scatter, color = 'purple')
# returns_fig.map_lower(sns.kdeplot, cmap = 'cool_d')
# returns_fig.map_diag(plt.hist, bins = 30)
# plt.figure()

## Heatmap で確認してみる
# 他社の株価と強く相関している
# sns.heatmap(tech_rets.corr(), annot = True)


"""
株式市場その3

4社のデータを比較するplotを考える

"""
## 損益の見積もり
rets = tech_rets.dropna()

"""
株式市場その4

株価におけるRisk の管理
"""
sns.distplot(AAPL['Daily Return'].dropna(), bins = 100, color = 'purple')
# quantile (5 %)
print(rets['AAPL'].quantile(0.05))
plt.figure()
## -> 95 %信頼区間の確率で1day に 2.7 %よりも損することはない.

### ================================
### Value at Risk 1 year later の予測
### ================================
days = 365
dt = 1/ days
mu = rets.mean()['GOOG']
sigma = rets.std()['GOOG']

## Cencept : brown 運動model をMCで 1 year later Simulation.
def stock_monte_carlo(start_price, days, mu, sigma):
    price = np.zeros(days)
    price[0] = start_price
    shock = np.zeros(days)
    drift = np.zeros(days)

    for x in range(1, days):
        shock[x] = np.random.normal(loc = mu*dt, scale = sigma * np.sqrt(dt))
        drift[x] = mu * dt
        price[x] = price[x - 1] + (price[x-1]* (drift[x] + shock[x]))

    return price

print(GOOG.head())

## iloc
start_price = GOOG.iloc[0, 5]

# 5回行い，1年後の株価を予測
for run in range(5):
    plt.plot(stock_monte_carlo(start_price, days, mu, sigma))

plt.xlabel('Days')
plt.ylabel('Price')
plt.title('Monte Carlo Analysis')
plt.figure()

### 10000 回で試行してみる
runs = 10000
simulations = np.zeros(runs)
np.set_printoptions(threshold = 5)
for run in range(runs):
    simulations[run] = stock_monte_carlo(start_price, days, mu, sigma)[days-1]


plt.hist(simulations, bins = 100)
plt.figure()

## 99 % CL でRisk 管理したい
q = np.percentile(simulations, 1)
plt.hist(simulations, bins = 200)

plt.figtext(0.6, 0.8, s = 'Start price: {:0.2}'.format(start_price))
plt.figtext(0.6, 0.7, s = 'mean final price:: {:0.2f}'.format(simulations.mean()))
plt.figtext(0.6, 0.8, s = 'VaR(0.99): {:0.2f}'.format(start_price - q))
plt.figtext(0.15, 0.6,  'q(0.99): {:0.2f}'.format(q))

plt.axvline(x = q, linewidth = 4, color = 'r')
            
plt.show()
