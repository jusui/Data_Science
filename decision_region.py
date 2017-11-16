import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from perceptron import Perceptron
import pymlb_ch02

def plot_decision_region(X, y, classifier, resolution = 0.02):

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
        plt.scatter(x = X[y == cl, 0], y = X[y == cl, 1], alpha = 0.8, c = cmap(idx),
                    marker = markers[idx], label = cl)

    
# # plot decision region
plot_decision_region(X, y, classifier = ppn)
plt.xlabel('sepal length [cm]')
plt.ylabel('petal length [cm]')
plt.legend(loc = 'upper left')
plt.show()
