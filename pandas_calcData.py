import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy.random import randn

ser1 = Series([0, 1, 2], index= ['A', 'B', 'C'])
ser2 = Series([3,4,5,6,], index = ['A','B', 'C', 'D'])

# NaN = Not a number
ser3 = ser1 + ser2
print(ser3)

dframe1 = DataFrame(np.arange(4).reshape(2,2), columns = list('AB'), index = ['NYC', 'LA'])

print(dframe1)

dframe2 = DataFrame(np.arange(9).reshape(3,3), columns = list('ADC'), index = ['NYC', 'SF', 'LA'])

print(dframe2)

dframe3 = dframe1 + dframe2
print(dframe3)

## Userful
dframe4 = dframe1.add(dframe2, fill_value = 0)
print(dframe4)

print(dframe2)
## row
ser3 = dframe2.ix[0]
print(ser3)

print(dframe2 - ser3)
# 形が違っても計算できる
