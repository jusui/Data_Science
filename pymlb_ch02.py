import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header = None)
print(df.tail)

# Vars [1 : 100]
y = df.iloc[0:100, 4].values
y = np.where( y == 'Iris-setosa', -1, 1 )
print(y)

# [1:100], column(1:3)
X = df.iloc[0:100, [0, 2]].values
print(X)

# Plot setosa
plt_setosa = plt.scatter(X[:50, 0], X[:50, 1], color = 'red', marker = 'o', label = 'setosa')

# Plot versicolor
plt_versicolor = plt.scatter(X[50:100, 0], X[50:100, 1], color = 'blue', marker = 'o', label = 'versicolor')

plt.xlabel('sepal length [cm]')
plt.ylabel('petal length [cm]')
plt.legend(loc = 'upper left')
plt.show()


# Object generator
ppn = Perceptron(eta = 0.1, n_iter = 10)

# Fit a training model
ppn.fit(X, y)

# Plot
plt.plot(range(1, len(ppn.errors_) + 1 ), ppn.errors_, marker = 'o' )
plt.xlabel('Epochs')
plt.ylabel('Number of misclassfications')
plot.show()


                           

