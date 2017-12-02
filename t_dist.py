import matplotlib.pyplot as plt

from scipy.stats import t
import numpy as np

# t_dist : Nが大きくなるとgaussianに漸近していく
# set X-axis
x = np.linspace(-5, 5, 100)

# DOF = 3, t-dist
rv = t(3)

plt.plot(x, rv.pdf(x))
plt.show()

