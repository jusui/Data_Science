import numpy as np

## Public Symbols
__all__ = ['NativeBayes1']


class NativeBayes1(object):
    """
    Native bayes class (1)
    -----------
    Attributes
    pY_ : array_like, shape=(n_classes), dtype=float 
    pmf of a class

    pXgY : array_like, shape(n_features, n_classes, n_fvalues), dtype=float 
    pmf of feature values given a class

    """

    def __init__ (self):
        """
        Constructor
        """
        self.pY_   = None
        self.pXgY_ = None


    def fit(self, X, y):
        """
        Fitting model
        
        Parameters
        -----------
        X : array_like, shape = (n_samples, n_features), dtype = int
            feature values of training samples

        Y : array_like, shape = (n_samples), dtype = int
            class labels of training samples

        """

        # constants
        n_samples  = X.shape[0]
        n_features = X.shape[1] ## 2value (0 or 1)
        n_classes  = 2
        n_fvalues   = 2
        
        # Error handling : check the size of y
        if n_samples != len(y):
            raise ValueError('Mismatched number of samples.')

        ### Train class dist ###
        # nY vector, count up n[yi=y]
        nY = np.zeros(n_classes, dtype = int)
        for i in range(n_samples):
            nY[y[i]] += 1
        
        ## Initialize 0 element matrix ##
        # calc pY_
        self.pY_ = np.empty(n_classes, dtype = float)
        for i in range(n_classes):
            self.pY_[i] = nY[i] / n_samples

        ### Train feature dist ###
        # nXY vector, count up n[x_ij = xj, yi = y]
        nXY = np.zeros((n_features, n_fvalues, n_classes), dtype = int)
        for i in range(n_samples):
            for j in range(n_features):
                nXY[j, X[i, j], y[i]] += 1

        # calc pXgY_
        self.pXgY_ = np.empty((n_features, n_fvalues, n_classes), dtype = float)
        for i in range(n_features):
            for xi in range(n_fvalues):
                for yi in range(n_classes):
                    self.pXgY_[j, xi, yi] = nXY[j, xi, yi] / nY[yi]


    def predict(self, X):
        """
        Predict class

        Parameters
        -----------
        X : array_like, shape = (n_samples, n_features), dtype = int
            feature values of unseen samples

        Returns
        -----------
        y : array_like, shape = (n_samples), dtype = int
            predicted class lables

        """

        # constants
        n_samples  = X.shape[0]
        n_features = X.shape[1]

        # memory for return values
        y = np.empty(n_samples, dtype = int)

        # for each features in X (i:matrix index, xi:matrix element) 
        for i, xi in enumerate(X):

            # calc joint probability (pXgY_[j, xi, :]), " : " means getting values(0 & 1).
            logpXY = (np.log(self.pY_) + \
                      np.sum(np.log(self.pXgY_[np.arange(n_features), xi, :]), \
                             axis = 0))

            # Decide and get predict class
            y[i] = np.argmax(logpXY)

        return y
    

