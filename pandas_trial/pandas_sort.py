import numpy as np
import pandas as pd
from pandas import Series, DataFrame

ser1 = Series(range(3), index = ['C', 'A', 'B'] )
print(ser1)
print(ser1.sort_index())

from numpy.random import randn

ser2 = Series(randn(10))
print(ser2)
## get rank
print(ser2.rank())
# print(ser2.sort())





