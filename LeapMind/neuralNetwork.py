# coding: utf-8
import numpy as np
import scipy as sp
from scipy import special

# Neural Network(nn) class
class neuralNetwork:

    # initialize nn class
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        # set input, hidden, output nodes
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        # learning rate : lr
        self.lr = learningrate

        # initialize weight : w12 as node1_node2 with gaussian
        self.wih = (np.random.randn(self.hnodes, self.inodes))
        self.who = (np.random.randn(self.onodes, self.hnodes))

        # activation function        
        self.activation_function = lambda x: special.expit(x)
        
        pass

    
    # sigmoid function
    def sigmoid(x):
        return 1.0 / (1.0 + np.exp(-x))

    def grad_sigmoid(x):
        return sigmoid(x) * (1.0 - sigmoid(x))

    # relu function
    def relu(x):
        return np.maximum(0, x)
    
    # train nn
    def train(self, inputs_list, targets_list):
        """
        input  : exchange matrix
        target : correct value
        output :
        """
        inputs  = np.array(inputs_list, ndmin = 2).T
        targets = np.array(targets_list, ndmin = 2).T

        hidden_inputs  = np.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)

        final_inputs  = np.dot(self.who, hidden_inputs)
        final_outputs = self.activation_function(final_inputs)

        # error_who = correct_value - output_value
        output_errors = targets - final_outputs

        # hidden_errors = who.T * output_errors
        hidden_errors = np.array(self.who.T * output_errors)

        # update weight in hidden-output layer
        # delta wjk = lr * grad_sigmoid(x) * (hidden_output).T
        self.who += self.lr * np.dot(
            self.grad_sigmoid(final_outputs),
            np.transpose(hidden_outputs))

        self.wih += self.lr * np.dot(
            self.grad_sigmoid(hidden_outputs),
            np.transpose(inputs))
        
        pass

    
    # refer nn(input layer & output layer)
    def query(self, inputs_list):
        """
        input  : input signal in any layer
        output : activation function calculate output
        """
        inputs = np.array(inputs_list, ndmin = 2).T
        
        hidden_inputs  = np.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        
        final_inputs  = np.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        
        # pass
        return final_outputs

 
if __name__ == '__main__':
    # input, hidden, output layer
    input_nodes = 3
    hidden_nodes = 3
    output_nodes = 3

    # learning rate
    learning_rate = 0.3

    n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
    print("n.query([1.0, 0.5, -1.5]) :", n.query([1.0, 0.5, -1.5]))
    print("Done")
    
