# coding: utf-8
import numpy as np
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
        # self.wih = (np.random.randn(self.hnodes, self.inodes))
        # self.who = (np.random.randn(self.onodes, self.hnodes))
        self.wih = np.random.normal(0.0, pow(self.inodes, -0.5), (self.hnodes, self.inodes))
        self.who = np.random.normal(0.0, pow(self.hnodes, -0.5), (self.onodes, self.hnodes))

        pass

    
    # sigmoid function
    def sigmoid(self, x):
        return 1.0 / (1.0 + np.exp(-x))

    def grad_sigmoid(self, x):
        return self.sigmoid(x) * (1.0 - self.sigmoid(x))
    
    # relu function
    def relu(self, x):
        return np.maximum(0, x)

    def grad_relu(self, x):
        grad = np.zeros(x)
        grad[ x >= 0 ] = 1
        return grad

    
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
        
        # pass
        return final_outputs

 
if __name__ == '__main__':
    # input, hidden, output layer, learning rate
    input_nodes   = 784 # 28 * 28
    hidden_nodes  = 100 # 10 ~ 784
    output_nodes  = 10  # 0 ~ 9
    learning_rate = 0.2 # default 0.3, best score is 0.2

    # nn instance
    nn = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
    # print("nn.query([1.0, 0.5, -1.5]) :", nn.query([1.0, 0.5, -1.5])) # query test 

    # read MNIST dataset
    with open("mnist_train.csv", "r") as training_data_file:
        training_data_list = training_data_file.readlines()
        # print(len(training_data_list)) # 60000
        # print(training_data_list[0]) # 0 ~ 255

    """ 
    train neural network 
    """
    epoch = 2
    for e in range(epoch):
        for train in training_data_list:
            train_values  = train.split(',')
            inputs  = (np.asfarray(train_values[1:]) / 255.0 * 0.99 ) + 0.01 # prevent overflow
            targets = np.zeros(output_nodes) + 0.01
            targets[int(train_values[0])] = 0.99
            nn.train(inputs, targets) # train(inputs, correct_label)

            pass
        pass


    """
    test neural network
    """
    with open("mnist_test.csv", "r") as test_data_file:
        test_data_list = test_data_file.readlines()
        # print(test_data_list[0])

    calc_score = []
    for test in test_data_list:
        test_values   = test.split(',')
        correct_label = int(test_values[0])
        # print("correct label :", correct_label)
        inputs  = (np.asfarray(test_values[1:]) / 255.0 * 0.99 ) + 0.01
        outputs = nn.query(inputs)
        label = np.argmax(outputs) # label is maximum value
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
    
    # plt.show()
    print("Done")
