import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.colors import ListedColormap
from perceptron import Perceptron

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header = None)
print(df.tail)

def decision_region(X, y, classifier, resolution = 0.02):
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

    # Object generator && Fit training model
    ppn = Perceptron(eta = 0.1, n_iter = 10)
    ppn.fit(X, y)

    # Marker & Color map
    markers = ('s', 'x', 'o', '^', 'v')
    colors  = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap    = ListedColormap(colors[:len(np.unique(y))])

    # Plot decision region
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1

    # Grid point
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x2_max, resolution),
                           np.arange(x2_min, x2_max, resolution))

    # Execute prediction of 1-dim array feature
    Z = classifier.predict(np.array([xx1.ravel(), xx2.rabel()]).T)

    # Exchange grid point with datasize
    Z = Z.reshape(xx1.shape)

    # Grid point
    plt.contourf(xx1, xx2, Z, alpha = 0.4, cmap = cmap)

    # Set axis
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    # Plot class sample
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x = X[y == cl, 0], y = X[y == cl, 1], \
                    alpha = 0.8, c = cmap(idx), \
                    marker = markers[idx], label = cl)

if __name__ == '__main__':
    # Vars [1 : 100]
    y = df.iloc[0:100, 4].values
    y = np.where( y == 'Iris-setosa', -1, 1 )
    print(y)
    
    # [1:100], column(1:3)
    X = df.iloc[0:100, [0, 2]].values
    print(X)

    # Object generator && Fit training model
    ppn = Perceptron(eta = 0.1, n_iter = 10)
    ppn.fit(X, y)

    decision_region(X, y, classifier = ppn)
    plt.xlabel('sepal length [cm]')
    plt.ylabel('petal length [cm]')
    plt.legend(loc = 'upper left')
    plt.show()
