import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from nn_analysis import *
import unittest
from neural_network import NeuralNetwork
from neural_network import TestMethods
import sys


if __name__ == '__main__':
    inputs = np.array([[0.5, -0.2, 0.1]])
    targets = np.array([[0.4]])
    test_w_i_h = np.array([[0.1, -0.2],
                           [0.4, 0.5],
                           [-0.3, 0.2]])

    test_w_h_o = np.array([[0.3],
                           [-0.1]])
    
    suite = unittest.TestLoader().loadTestsFromModule(TestMethods())
    unittest.TextTestRunner().run(suite)
    
    ### set the hyperparametres here ###
    iterations = 5000
    learning_rate = 0.2
    hidden_nodes = 15
    output_nodes = 1

    N_i = train_features.shape[1]
    network = NeuralNetwork(N_i, hidden_nodes, output_nodes, learning_rate)

    losses = {'train':[], 'validation':[]}
    for ii in range(iterations):
        # go through a random batch fo 128 records from the training data set
        batch = np.random.choice(train_features.index, size = 128)
        X, y = train_features.ix[batch].values, train_targets.ix[batch]['cnt']

        network.train(X, y)

        # printing out the training progress
        train_loss = MSE(network.run(train_features).T, train_targets['cnt'].values)
        val_loss = MSE(network.run(val_features).T, val_targets['cnt'].values)
        sys.stdout.write("\rProgress: {:2.1f}".format(100 * ii/float(iterations)) \
                         + "% ... Training loss: " + str(train_loss)[:5] \
                         + " ... Validation loss: " + str(val_loss)[:5])
        sys.stdout.flush()

        losses['train'].append(train_loss)
        losses['validation'].append(val_loss)

        
    plt.plot(losses['train'], label = 'Training loss')
    plt.plot(losses['validation'], label = 'Validation loss')
    _ = plt.ylim()
    plt.show()
    
    
