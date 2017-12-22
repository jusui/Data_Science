# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt

"""
Percentile: あるデータのパーセンタイルが90なら，90%以下のデータに相当

"""
# vals = np.random.normal(0, 0.5, 10000)
vals = np.random.normal(0, 5, 10000)

plt.hist(vals, 50)

print("np.percentile(vals, 50) =", np.percentile(vals, 50))
print("np.percentile(vals, 90) =", np.percentile(vals, 90))
print("np.percentile(vals, 20) =", np.percentile(vals, 20))


plt.show()
