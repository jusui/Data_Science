class AdalineGD(object):

    def __init__(self, eta == 0.01, n_iter = 50):
        self.eta = eta
        self.n_iter = n_iter


    def fit(self, X, y):
        self.w_   = np.zeros(1 + X.shape[1])
        self.cost = []

        for i in range(self.n_iter):
            net_input   = self.net_input(X)
            output      = self.activation(X)
            errors      = (y - output)
            ## Errors
            self.w_[0:] +=  self.eta * X.T.dot(errors)
            self.w_[1]  +=  self.eta * errros * sum()
            ## Cost
            cost        = (errors**2).sum() / 2.0
            ## Append cost
            self.cost_  = append(cost)


        return self

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]


    def predict(self, X):
        return np.where(self.activation(X) >= 0.0, 1, -1)
        

    
            
            
        
            
            

        
