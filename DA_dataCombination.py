import numpy as np
import pandas as pd
from pandas import Series, DataFrame

ser1 = Series([2, np.nan, 4, np.nan, 6, np.nan],\
              index = ['Q', 'R', 'S', 'T', 'U', 'V'])
print(ser1)

ser2 = Series(np.arange(len(ser1), dtype = np.float64),\
              index = ['Q', 'R', 'S', 'T', 'U', 'V'])
print(ser2)

#三項演算子
#(if null ? ser2 : ser1)
print(np.where(pd.isnull(ser1), ser2, ser1))
ser3 = Series(np.where(pd.isnull(ser1), ser2, ser1), index = ser1.index)

print(ser3)

## ser3と同じことが簡単にできる
ser33 = ser1.combine_first(ser2)
print(ser33)


## 同じことをDataFrameで行う
dframe_odds = DataFrame({'X':[1, np.nan, 3, np.nan],\
                        'Y':[np.nan, 5, np.nan, 7],\
                        'Z':[np.nan, 9, np.nan, 11]})

print(dframe_odds)

dframe_evens = DataFrame({'X':[2, 4, np.nan, 6, 8], \
                          'Y':[np.nan, 10, 12, 14, 16]})
print(dframe_evens)

print(dframe_odds.combine_first(dframe_evens))

