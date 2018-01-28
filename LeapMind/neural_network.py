# coding: utf-8
import numpy as np

class NeuralNetwork:
    """
    Neural network class

    weight : wij(ith to jth layer)
    (e.f.) wih(input - hidden), who(hidden - output)
    eta : learning rate
    
    """

    def __init__(self, inlayer, hilayer, outlayer, eta):
        self.inodes = inlayer
        self.hnodes = hilayer
        self.onodes = outlayer

        self.wih = np.random.normal(0.0, pow(self.hnodes, -0.5),
                                    (self.hnodes, self.inodes))
        self.who = np.random.normal(0.0, pow(self.onodes, -0.5),
                                    (self.onodes, self.hnodes))

        # learning rate : eta
        self.lr = eta

        pass

        
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
        
    
    def train(self, inputs_list, targets_list):
        # input layer
        inputs  = np.array(inputs_list, ndmin = 2).T
        targets = np.array(targets_list, ndmin = 2).T        

        # hidden layer
        hidden_inputs  = np.dot(self.wih, inputs)
        hidden_outputs = self.sigmoid(hidden_inputs)
        
        # output layer
        out_inputs  = np.dot(self.who, hidden_outputs)
        out_outputs = self.sigmoid(out_inputs)

        out_error  = targets - out_outputs
        hidden_err = np.dot(self.who.T, out_error)

        # update weight(hidden - output)
        self.who += self.lr * np.dot(
            (out_error * out_outputs * (1.0 - out_outputs)),
            np.transpose(hidden_outputs) )

        # update weight(input - hidden)
        self.wih += self.lr * np.dot(
            (hidden_err * hidden_outputs * (1.0 - hidden_outputs)),
            np.transpose(inputs) )

        pass

    
    def query(self, inputs_list):
        inputs = np.array(inputs_list, ndmin = 2).T

        hidden_inputs  = np.dot(self.wih, inputs)
        hidden_outputs = self.sigmoid(hidden_inputs)

        out_inputs  =  np.dot(self.who, hidden_outputs)
        out_outputs =  self.sigmoid(out_inputs)        

        return out_outputs


if __name__ == "__main__":
    inlayer  = 784
    hilayer  = 100
    outlayer = 10

    eta = 0.3

    # instance
    NN = NeuralNetwork(inlayer, hilayer, outlayer, eta)

    # load the mnist training data CSV file into a list
    training_data_file = open("mnist_train.csv", 'r')
    training_data_list = training_data_file.readlines()
    training_data_file.close()
    #    print(training_data_list)

    for data in training_data_list:
        value = data.split(',')
#        print(value[0])
        inputs  = (np.asfarray(value[1:]) / 255.0 * 0.99) + 0.01
        targets = np.zeros(outlayer) + 0.01
        targets[int(value[0])] = 0.99
        NN.train(inputs, targets)
        pass


    # Test my NN
    score = []

    test_data_file = open("mnist_test.csv", 'r')
    test_data_list = test_data_file.readlines()
    test_data_file.close()
    #    print(test_data_list)

    for test in test_data_list:
        value = test.split(',')
        # answer label
        answer_label = int(value[0])
        # print(answer_label, "answer_label")

        # scaling & shift, inputs.shape = [0, 0, ...]
        inputs  = (np.asfarray(value[1:]) / 255.0 * 0.99) + 0.01
        #  print("inputs :", inputs)
        outputs = NN.query(inputs) # (2, 1)transpose to vertical 
        # print("outputs :", outputs)
        label = np.argmax(outputs)
        print(label, "network's answer")

        # answer(1), miss(0)
        if (label == answer_label):
            score.append(1)

        else:
            score.append(0)
            pass

        pass


    score_array = np.asarray(score)
    print("acc =", score_array.sum() / score_array.size)
