import numpy as np
from numpy.random import randn
import pandas as pd

from scipy import stats

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

dataset = randn(100)
sns.kdeplot(dataset)

sns.rugplot(dataset, color = 'black')
for bw in np.arange(0.5, 2, 0.25):
    sns.kdeplot(dataset, bw = bw, label = bw)

plt.figure()

kernel_options = ['biw', 'cos', 'epa', 'gau', 'tri', 'triw']
for kern in kernel_options:
    sns.kdeplot(dataset, kernel = kern, label = kern)

plt.show()
# plt.legend()

