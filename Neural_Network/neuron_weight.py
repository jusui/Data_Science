# coding: UTF-8
import math

# sigmoid function()
def sigmoid(a):
    return 1.0 / (1.0 + math.exp(-a))

# ニューロン
class Neuron:
    # 入力値の合計初期値
    input_sum = 0.0
    # 出力値の初期化
    output = 0.0
    
    # 入力値をinputに足す
    def setInput(self, inp):
        self.input_sum += inp
#        print(self.input_sum)

    # sigmoid関数で, 入力値を出力値に変換する
    def getOutput(self):
        self.output = sigmoid(self.input_sum)
        return self.output

# NeuralNetwork class
class NeuralNetwork:
    # Weight
    w = [1.5, -2.5, -0.5]
    # Neuron instance
    neuron = Neuron()

    # Execute
    def commit(self, input_data):
        self.neuron.setInput(input_data[0] * self.w[0])
        self.neuron.setInput(input_data[1] * self.w[1])
        self.neuron.setInput(input_data[2] * self.w[2])        
        # for data in input_data:
        #     self.neuron.setInput(data)
        return self.neuron.getOutput()

# Neuralnetwork のインスタンス
neural_network = NeuralNetwork()

# Execute, commit methodを呼び出す
# (1) trial data
# trial_data = (1.0, 2.0, 3.0, 4.0, 5.0)

# (2) input total = 0 の場合
trial_data = (1.0, 2.0, 3.0)

# (3) negative data の場合, 限りなく0に近づく
# trial_data = (-1.0, -2.0, -3.0)
print("ニューロンからの出力")
print(neural_network.commit(trial_data))
