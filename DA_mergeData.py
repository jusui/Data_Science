import pandas as pd
import numpy as np
from pandas import DataFrame

dframe1 = DataFrame({'key':['X', 'Z', 'Y', 'Z', 'X', 'X'], 'data_set1':np.arange(6)})

print(dframe1)

dframe2 = DataFrame({'key':['Q', 'Y', 'Z'], 'data_set2':[1,2,3]})
print(dframe2)

dframe_merge = pd.merge(dframe1, dframe2)
print(dframe_merge)

dframe_merge2 = pd.merge(dframe1, dframe2, on = 'key')
print(dframe_merge2)

# dframe1 を基準にマージ
dframe_merge3 = pd.merge(dframe1, dframe2, on = 'key', how = 'left')
print(dframe_merge3)

# dframe2 を基準にマージ
dframe_merge4 = pd.merge(dframe1, dframe2, on = 'key', how = 'right')
print(dframe_merge4)

dframe_merge5 = pd.merge(dframe1, dframe2, on = 'key', how = 'outer')
print(dframe_merge5)

dframe33 = DataFrame({'key': ['X', 'X', 'X', 'Y', 'Z', 'Z'], 'data_set_3':range(6)})
print(dframe33)

dframe44 = DataFrame({'key': ['Y', 'Y', 'X', 'X', 'Z'], 'data_set_4':range(5)})
print(dframe44)

dframe_merge34 = pd.merge(dframe33, dframe44)
print(dframe_merge34)

df_left = DataFrame({'key1':['SF', 'SF', 'LA'], 'key2':['one', 'two', 'one'], 'left_data':[10, 20, 30]})
print(df_left)

df_right = DataFrame({'key1':['SF', 'SF', 'LA', 'LA'], 'key2':['one','one', 'two', 'one'], 'right_data':[40, 50, 60, 70]})
print(df_right)

print(pd.merge(df_left, df_right, on = ['key1', 'key2'], how = 'outer'))

# surffix
print(pd.merge(df_left, df_right, on = 'key1'))
print(pd.merge(df_left, df_right, on = 'key1', suffixes = ['_left', '_right']))
