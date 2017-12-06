from numpy.random import randn
import seaborn as sns
import  matplotlib.pyplot as plt

dataset = randn(100)
sns.distplot(dataset)
plt.figure()

sns.distplot(dataset, rug = True, hist = False)
plt.figure()

sns.distplot(dataset, bins = 25,\
             kde_kws = {'color' : 'indianred', 'label':'KDE PLOT'},\
             hist_kws = {'color': 'blue', 'label':'HISTOGRAM'})
plt.figure()

from pandas import Series
ser1 = Series(dataset, name = 'My_Data')
print(ser1)
sns.distplot(ser1)

plt.show()
# plt.legend()

