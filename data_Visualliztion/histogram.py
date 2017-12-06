from numpy.random import randn
import matplotlib.pyplot as plt
import seaborn as sns

# gaussian dist
dataset1 = randn(100)

# plt.hist(dataset1)
# print(dataset1)

dataset2 = randn(80)
# plt.hist(dataset2, color = 'indianred')

# plt.hist(dataset1, normed = True)

plt.hist(dataset1, normed = True, alpha = 0.5, bins = 20)
plt.hist(dataset2, normed = True, alpha = 0.5, bins = 20, color = 'indianred')

data1 = randn(1000)
data2 = randn(1000)

# joint dist
sns.jointplot(data1, data2, kind = 'hex')
plt.show()

    
    


