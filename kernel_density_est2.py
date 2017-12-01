import numpy as np
from numpy.random import randn
import pandas as pd

from scipy import stats

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

dataset2 = randn(100)
sns.kdeplot(dataset2, label = 'KDE')

plt.show()
plt.legend()
