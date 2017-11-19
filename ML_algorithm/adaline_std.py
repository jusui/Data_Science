import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from adalineGD import AdalineGD
from iris_data import decision_region

if __name__ == '__main__':

    df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header = None)

    # Vars [1 : 100]
    y = df.iloc[0:100, 4].values
    y = np.where( y == 'Iris-setosa', -1, 1 )

    # [1:100], column(1:3)
    X = df.iloc[0:100, [0, 2]].values

    fit, ax = plt.subplots(nrows = 1, ncols = 2, figsize = (8, 4))

    X_std =  np.copy(X)
    X_std[:,0] = (X[:,0] - X[:,0].mean()) / X[:,0].std()
    X_std[:,1] = (X[:,1] - X[:,1].mean()) / X[:,1].std()

    ## Adaline
    ada = AdalineGD(n_iter = 15, eta = 0.01)

    ## Fit
    ada.fit(X_std, y)

    ## def plot
    decision_region(X_std, y, classifier = ada)

    ## Title
    plt.title('Adaline - Gradient Descent')

    ## Axis
    plt.xlabel('sepal length [standardized]')
    plt.ylabel('petal length [standardized]')

    ## lenged
    plt.legend(loc = 'upper left')

    ## Show plot
    plt.show()

    ## Cost
    plt.plot(range(1, len(ada.cost_) + 1), ada.cost_, marker = 'o')

    ## Label
    plt.xlabel('Epochs')
    plt.ylabel('Sum-squared-error')
    plt.show()
    

