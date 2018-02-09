# coding: utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
外部リソースのURLには、2013年のワシントンD.C.におけるバイクレンタル数のデータが入っています。
このデータをニューラルネットワークを使用して学習し、ある日付のレンタル数を予測するモデルを構築してください。
"""

data_path = 'hour.csv'
rides = pd.read_csv(data_path) # (17379, 17)
print(rides.head())
print(rides.shape)

"""
データセット
[期間] 2011年1月1日から2012年12月31日まで2年間
[cnt] 1時間毎のライダーの数を計測
[caual/registered] 未登録/登録済で分けている

"""
# 最初の10日間(24hour * 10 days)をプロット
rides[:24*10].plot(x = 'dteday', y = 'cnt')


"""
ダミー化
季節などのカテゴリカル変数を，モデルに追加する.(0, 1)
pd.get_dummies()
"""
dummy_fields = ['season', 'weathersit', 'mnth', 'hr', 'weekday']
for each in dummy_fields:
    dummies = pd.get_dummies(rides[each], prefix=each, drop_first=False)
    rides = pd.concat([rides, dummies], axis=1)

fields_to_drop = ['instant', 'dteday', 'season', 'weathersit', 
                  'weekday', 'atemp', 'mnth', 'workingday', 'hr']
data = rides.drop(fields_to_drop, axis=1)
print(data.head())



plt.show()
