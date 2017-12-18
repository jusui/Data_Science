# coding: utf-8

# ニューロン
class Neuron:
    # 入力値の合計初期値
    input_sum = 0.0

    # 入力値をinputに足す
    def setInput(self, inp):
        self.input_sum += inp
        print(self.input_sum)

# NeuralNetwork        
class NeuralNetwork:
    # Neuron instance
    neuron = Neuron()

    # Execute
    def commit(self, input_data):
        for data in input_data:
            self.neuron.setInput(data)

# Neuralnetwork のインスタンス
neural_network = NeuralNetwork()

# Execute, commit methodを呼び出す
trail_data = (1.0, 2.0, 3.0, 4.0, 5.0)
neural_network.commit(trail_data)
