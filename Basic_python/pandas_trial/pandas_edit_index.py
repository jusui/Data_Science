import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy.random import randn

ser1 = Series([1,2,3,4], index = ['A','B', 'C','D'])
print(ser1)

ser2 = ser1.reindex(['A', 'B', 'C', 'D', 'E', 'F'])
print(ser2)

ser2_1 = ser2.reindex(['A', 'B', 'C', 'D', 'E', 'F', 'G'], fill_value = 0)
print(ser2_1)

ser3 = Series(['USA', 'Mexico', 'Canada'], index = [0, 5, 10])
print(ser3)

ser3_1 = ser3.reindex(range(15), method = 'ffill')
print(ser3_1)

dframe = DataFrame(randn(25).reshape((5,5)), index = ['A', 'B', 'C', 'D', 'E'], columns = ['col1', 'col2', 'col3', 'col4', 'col5'])
print(dframe)

new_index =  ['A', 'B', 'C', 'D', 'E', 'F']
dframe2 = dframe.reindex(new_index)
print(dframe2)

new_columns = ['col1', 'col2', 'col3', 'col4', 'col5', 'col6']
dframe2_1 = dframe2.reindex(columns = new_columns)
print(dframe2_1)

print(dframe)

dframe3 = dframe.ix[new_index, new_columns]
print(dframe3)


