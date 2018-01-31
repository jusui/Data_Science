import numpy as np
import pandas as pd
from pandas import Series, DataFrame

my_ser = Series([1,2,3,4], index = ['A', 'B', 'C', 'D'])
print(my_ser)

my_index = my_ser.index
print(my_index)

print(my_index[0])
print(my_index[2])
print(my_index[2:])
## pandas list 
# my_index[0] = 'Z'
