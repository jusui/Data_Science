import numpy as np
import pandas as pd
from scipy import stats

"""
観測値と期待値のズレを統計的に検討する方法
コインを投げて出目が妥当な値かどうかを判定
自由度kが大きくなると、分布がなだらかになる 
"""

### サイコロの出目が妥当かを判断してみる
# 観測値
observed = [8, 32, 48, 59, 67, 84, 76, 57, 34, 28, 7]
roll_sum = sum(observed)
print(roll_sum)

### expeceted 出目の分子 = freq
freq = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
possible_rolls = 1 / 36

freq = [possible_rolls * dice for dice in freq]
print(freq, '\n')

## 期待される出目の頻度(500回試行しているので * (500) する)
expected = [roll_sum * f for f in freq]
print(expected)

chisq, p = stats.chisquare(observed, expected)

# if p-value is too small -> its strange.
print('chisquare stats = {:0.2f}'.format(chisq))
print('P-value = {:0.2f}'.format(p))

