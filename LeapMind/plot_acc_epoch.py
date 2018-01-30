# coding: utf-8
import pandas as pd
from pandas import Series, DataFrame
import seaborn as sns
import matplotlib.pyplot as plt

acc_epoch_df = pd.read_csv('n_epochs.csv')
print(acc_epoch_df.head())

bins = [1, 2, 3, 4, 5, 6, 8, 10, 20, 30]
sns.factorplot('epoch', 'acc', data = acc_epoch_df, xbins = bins)
plt.figure()

plt.plot('epoch', 'acc', data = acc_epoch_df, marker = 'o')
plt.title("accucary vs. epochs")
plt.show()

