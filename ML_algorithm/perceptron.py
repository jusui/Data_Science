import numpy as np

class Perceptron(object):
    """ 
    Classification of the Percetron 
    
    Parameters
    ----------
    eta : float
    study rate (0.0 < eta < 1.0)

    n_iter : int
    # of Trainings in training data
    
    Attribute
    ----------

    w_ : 1 dimension array
    weight

    errors_ : list
    # of Errors in each epochs

    """

    # Initialize class(self == class instance)
    def __init__(self, eta = 0.01, n_iter = 10):
        self.eta = eta
        self.n_iter = n_iter


    def fit(self, X, y):
        """ 
        Fit training data 

        parameters
        ----------
        X : {array data structure}, shape = [n_samples, n_features]

        training data
        n_sample = # of samples, n_feature : # of features
        
        y : array data structures, sahpe = [n_samples]

        vars

        return value
        -------------
        self : object

        """

        ## zero element, zero matrix(0, 0, ...)
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []

        # Iteration(training) training data
        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0]  += update

                errors += int(update != 0.0)

            self.errors_.append(errors)

        return self



    def net_input(self,  X):
        """
        calculate all input
        """
        return np.dot(X, self.w_[1:]) + self.w_[0]


    def predict(self, X):
        """return class label of 1 step later"""

        return np.where(self.net_input(X) >= 0.0, 1, -1)
