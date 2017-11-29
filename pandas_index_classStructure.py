import numpy as np
import pandas as pd
from pandas import Series, DataFrame

from numpy.random import randn

# class structure
ser = Series(np.random.randn(6), index = [[1,1,1,2,2,2], ['a','b','c','a','b','c']])
print(ser)

print(ser.index)

print(ser[1])

# 下の階層
print(ser[:, 'a'])

dframe = ser.unstack()
print(dframe)

# dframe1 = dframe.unstack()
print(dframe.unstack())

# dframe11 = dframe.T.unstack()
print(dframe.T.unstack())

dframe2 = DataFrame(np.arange(16).reshape((4,4)), \
                    index = [['a', 'a', 'b', 'b'],[1,2,1,2]], \
                    columns = [['NY', 'NY', 'LA', 'SF'], ['cold', 'hot', 'hot', 'cold']])
print(dframe2)

# 行方向
dframe2.index.names = ['INDEX_1', 'INDEX_2']
print(dframe2)

# 列方向
dframe2.columns.names = ['Cities', 'Temp']
print(dframe2)

dframe3 = dframe2.swaplevel('Cities', 'Temp', axis = 1)
print(dframe3)

#列0,1 をsort
dframe2.sortlevel(1).sortlevel(0)
print(dframe2)

# class, temp(cold, hot同士で足し合わせる)
dframe2.sum(level='Temp', axis = 1)
print(dframe2)





