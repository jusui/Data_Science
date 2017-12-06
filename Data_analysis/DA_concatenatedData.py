import numpy as np
import pandas as pd
from pandas import DataFrame, Series

# concatenated
arr1 = np.arange(9).reshape(3,3)
print(arr1)

# 列方向
print(np.concatenate([arr1, arr1], axis = 1))

# 行方向
print(np.concatenate([arr1, arr1], axis = 0))


## series
ser1 = Series([0, 1, 2], index = ['T', 'U', 'V'])
ser2 = Series([3, 4], index = ['X', 'Y'])

print(ser1)
print(ser2)
print(pd.concat([ser1, ser2]))

print(pd.concat([ser1,ser2, ser1]))

# 列方向
print(pd.concat([ser1, ser2], axis = 1))
print(pd.concat([ser1, ser2], keys = ['cat1', 'cat2']))

# 行方向
print(pd.concat([ser1, ser2], axis = 1, keys = ['cat1', 'cat2']))

dframe1 = DataFrame(np.random.randn(4, 3), columns = ['X', 'Y', 'Z'])
print(dframe1)

dframe2 = DataFrame(np.random.randn(3, 3), columns = ['Y', 'Q', 'X'])
print(dframe2)

print(pd.concat([dframe1, dframe2]))

print(pd.concat([dframe1, dframe2], ignore_index = True))






