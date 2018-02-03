# coding: utf-8
import numpy as np
from neuralNetwork_epoch import *


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
    epoch = 1
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
    print("accuracy[epoch = 1] =", score.sum() / score.size)
            
    # plt.show()
    print("Done")
