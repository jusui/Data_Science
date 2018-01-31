# coding: utf-8
import numpy as np
from scipy import special
import matplotlib.pyplot as plt
    
# Neural Network(nn) class
class neuralNetwork:
    """
    neural network
    """

    # initialize nn class
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        # input, hidden and output nodes
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        # learning rate as lr
        self.lr = learningrate

        # initialize weight : w12 as node1_node2 with gaussian
        self.wih = (np.random.randn(self.hnodes, self.inodes))
        self.who = (np.random.randn(self.onodes, self.hnodes))

        # activation function        
        self.activation_function = lambda x: special.expit(x)
        
        pass

    
    # sigmoid function
    def sigmoid(self, x):
        return 1.0 / (1.0 + np.exp(-x))

    def grad_sigmoid(self, x):
        return self.sigmoid(x) * (1.0 - self.sigmoid(x))
    
    
    # train nn
    def train(self, inputs_list, targets_list):
        """
        input  : matrix
        target : correct value
        output :
        """
        inputs  = np.array(inputs_list, ndmin = 2).T
        targets = np.array(targets_list, ndmin = 2).T

        hidden_inputs  = np.dot(self.wih, inputs)
        hidden_outputs = self.sigmoid(hidden_inputs)

        final_inputs  = np.dot(self.who, hidden_outputs)
        final_outputs = self.sigmoid(final_inputs)

        # error_who = correct_value - output_value
        output_errors = targets - final_outputs

        # hidden_errors = np.dot(who.T, output_errors)
        hidden_errors = np.dot(self.who.T, output_errors)

        # update weight in hidden-output layer
        # delta_wjk = lr * np.dot(error * grad_f(x), transpose(j/k_output))
        self.who += self.lr * np.dot(output_errors * self.grad_sigmoid(final_inputs),
                                     np.transpose(hidden_outputs))

        self.wih += self.lr * np.dot(hidden_errors * self.grad_sigmoid(hidden_inputs),
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
        hidden_outputs = self.sigmoid(hidden_inputs)
        
        final_inputs  = np.dot(self.who, hidden_outputs)
        final_outputs = self.sigmoid(final_inputs)
        
        return final_outputs

 
if __name__ == '__main__':
    # input, hidden, output layer
    input_nodes  = 784 # 28 * 28
    hidden_nodes = 100 # 10 ~ 784
    output_nodes = 10  # 0 ~ 9
    learning_rate = 0.3 

    # nn instance
    nn = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
    # print("nn.query([1.0, 0.5, -1.5]) :", nn.query([1.0, 0.5, -1.5])) # query test 

    # read MNIST dataset
    with open("mnist_train.csv", "r") as training_data_file:
        training_data_list = training_data_file.readlines() # 60000
        # print(training_data_list[0]) # 0 ~ 255

    # """ [easy test] visualize number (e.f. '5')"""
    # train_values  = training_data_list[0].split(',') # get first data in training_data_list
    # # string -> float with np.asfarray()
    # train_data_image = np.asfarray(train_values[1:]).reshape((28, 28)) # remove label & reshape values to 28 * 28
    # plt.imshow(train_data_image, cmap = 'Greys', interpolation = 'None')
    
    """ 
    train neural network 
    """    
    for train in training_data_list:
        train_values  = train.split(',')
        inputs  = (np.asfarray(train_values[1:]) / 255.0 * 0.99 ) + 0.01 # prevent overflow
        targets = np.zeros(output_nodes) + 0.01
        targets[int(train_values[0])] = 0.99
        nn.train(inputs, targets) # train(inputs, correct_label)

        pass


    """
    test neural network
    """
    with open("mnist_test.csv", "r") as test_data_file:
        test_data_list = test_data_file.readlines()
        # print(test_data_list[0])

    # """ [easy test] get first data in test_data_list """
    # test_values = test_data_list[0].split(',')
    # print(test_values[0])
    # test_data_image = np.asfarray(test_values[1:]).reshape(28, 28)
    # plt.imshow(test_data_image, cmap = 'Greys', interpolation = 'None')
    # test_query = nn.query(( np.asfarray(test_values[1:]) / 255.0 * 0.99 ) + 0.01)
    # print(test_query)

    calc_score = []
    for test in test_data_list:
        test_values   = test.split(',')
        correct_label = int(test_values[0])
        # print("correct label :", correct_label)
        inputs  = (np.asfarray(test_values[1:]) / 255.0 * 0.99 ) + 0.01
        outputs = nn.query(inputs)
        label = np.argmax(outputs) # label:maximum value
        # print("nn's answer =", label)
        if ( label == correct_label ):
            calc_score.append(1)            
        else:
            calc_score.append(0)
            pass
        
        pass

    # print("calc_score :", calc_score)
    score = np.asarray(calc_score)
    print("accuracy =", score.sum() / score.size)
    
    plt.show()
    print("Done")
