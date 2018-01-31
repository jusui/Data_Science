import numpy as np
import pandas as pd
from pandas import Series, DataFrame

ser1 = Series(np.arange(3), index = ['A','B', 'C'])
print(ser1)

ser2 = ser1.drop('B')
print(ser2)

dframe1 = DataFrame(np.arange(9).reshape(3,3), index = ['SF', 'LA','NY'], columns = ['pop', 'size', 'year'])
print(dframe1)

print(dframe1.drop('LA'))
print(dframe1)

dframe2 = dframe1.drop('year', axis = 1)
print(dframe2)

