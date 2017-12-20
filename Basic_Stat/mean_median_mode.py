# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# random in normal dist.
incomes = np.random.normal(27000, 15000, 10000)
print("mean = ", np.mean(incomes))
print("median = ", np.median(incomes))
plt.hist(incomes, bins = 50)
plt.title("Mean")


# Data + richman
incomes = np.append(incomes, [100000000])
print("mean(data + rich) = ", np.mean(incomes))
print("median(data + rich) = ", np.median(incomes))

# Mode
ages = np.random.randint(18, high = 90, size = 500)
print(ages)

mode = stats.mode(ages)
print("mode = ", mode)

plt.show()
