import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# stats library
from scipy import stats

mean = 0
std = 1

## region
X = np.arange(-4, 4, 0.01)
Y = stats.norm.pdf(X, mean, std)

plt.plot(X, Y)
# plt.show()

mu, sigma = 0, 0.1

norm_set = np.random.normal(mu, sigma, 1000)
import seaborn as sns

plt.hist(norm_set, bins = 50)
plt.show()

