import numpy as np
import pandas as pd
from pandas import Series, DataFrame

ser1 = Series(np.arange(3), index = ['A', 'B', 'C'])
ser1 = 2*ser1
print(ser1)

print(ser1['B'])
print(ser1[1])
print(ser1[0:3])

print(ser1[['A', 'B']])
ser1[ser1 > 3] = 10
#ser2 =  (ser1[ser1 > 3] = 10)
#print(ser1[ser1 > 3] = 10)
print(ser1)

dframe = DataFrame(np.arange(25).reshape(5,5), index = ['NYC', 'LA', 'SF', 'DC','Chi'], columns = ['A', 'B', 'C', 'D', 'E'] )
print(dframe)

# column access
print(dframe['B'])

# col B & C
print(dframe[['B', 'C']])

# condition
print("condition")
print(dframe[dframe['C'] > 8])
# print(dframe)

print(dframe > 10)
# print(dframe)

# row access
print(dframe.ix['LA'])
# print(dframe)

print(dframe.ix[1])
# print(dframe)
