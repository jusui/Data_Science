# coding: UTF-8
import math
import matplotlib.pyplot as plt
from  matplotlib.font_manager import FontProperties
fp = FontProperties(fname=r'/Library/fonts/ipag.ttf', size=11)
    
# sigmoid function()
def sigmoid(a):
    return 1.0 / (1.0 + math.exp(-a))

""" ニューロン """
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

    def reset(self):
        self.input_sum = 0
        self.output = 0

""" NeuralNetwork class"""
class NeuralNetwork:
    # Weight [[input1, input2, bias]]
    w_im = [[0.496, 0.512], [-0.501, 0.998], [0.498, -0.502]] # (3 * 2)入力層[0,1,2] - 中間層①[0, 1, 2]
    w_mm = [[0.512, 0.496], [0.998, -0.501], [-0.502, 0.498]] # (3 * 2)入力層①[0,1,2] - 中間層②[0, 1, 2]
    w_mo = [0.121, -0.4996, 0.200] # (3 * 1)中間層 - 出力層
    
    # Neuron instance (e.f. neuron = Neuron())
    input_layer   = [0.0, 0.0, 1.0]
    middle_layer  = [Neuron(), Neuron(), 1.0]
    middle_layer2  = [Neuron(), Neuron(), 1.0]
    output_layer  = Neuron()

    # 実行, データを読む度にreset() で0に初期化する
    def commit(self, input_data):
        # 各層のリセット
        self.input_layer[0] = input_data[0]
        self.input_layer[1] = input_data[1]

        # initialize middle layer data
        self.middle_layer[0].reset()
        self.middle_layer[1].reset()
        self.middle_layer2[0].reset()
        self.middle_layer2[1].reset()

        # initialize data
        self.output_layer.reset()

        # 入力層 -> 中間層①
        self.middle_layer[0].setInput(self.input_layer[0] * self.w_im[0][0])
        self.middle_layer[0].setInput(self.input_layer[1] * self.w_im[1][0])
        self.middle_layer[0].setInput(self.input_layer[2] * self.w_im[2][0])        

        self.middle_layer[1].setInput(self.input_layer[0] * self.w_im[0][1])
        self.middle_layer[1].setInput(self.input_layer[1] * self.w_im[1][1])
        self.middle_layer[1].setInput(self.input_layer[2] * self.w_im[2][1])

        # 中間層① -> 中間層②
        self.middle_layer2[0].setInput(self.middle_layer[0] * self.w_mm[0][0])
        self.middle_layer2[0].setInput(self.middle_layer[1] * self.w_mm[1][0])
        self.middle_layer2[0].setInput(self.middle_layer[2] * self.w_mm[2][0])        

        self.middle_layer2[1].setInput(self.middle_layer[0] * self.w_mm[0][1])
        self.middle_layer2[1].setInput(self.middle_layer[1] * self.w_mm[1][1])
        self.middle_layer2[1].setInput(self.middle_layer[2] * self.w_mm[2][1])


        # 中間層② -> 出力層
        self.output_layer.setInput(self.middle_layer2[0].getOutput() * self.w_mo[0])
        self.output_layer.setInput(self.middle_layer2[1].getOutput() * self.w_mo[1])
        self.output_layer.setInput(self.middle_layer2[2] * self.w_mo[2])

        # getOutput() method で返り値を与える
        return self.output_layer.getOutput()

# 基準点(データの範囲を0.0 ~ 1.0に収める)
refer_point_0 = 34.5
refer_point_1 = 137.5

"""
Read file (緯度, 経度)
データをrstrip() で読み，split(",")で分割する
データを読み込み，緯度経度から基準点を引いて格納する
"""
trial_data = []
trial_data_file = open("./trial_data.txt", "r")
for line in trial_data_file:
    line = line.rstrip().split(",")
    trial_data.append([ float(line[0]) - refer_point_0, float(line[1]) - refer_point_1 ])
trial_data_file.close()

print("trial_data = {}".format(trial_data))

# Neuralnetwork のインスタンス
neural_network = NeuralNetwork()

""" Execute, commit methodを呼び出す """
# (1) trial data : trial_data = (1.0, 2.0, 3.0, 4.0, 5.0)
# (2) input total = 0(trial_data = (1.0, 2.0, 3.0)) の場合は，0
# (3) negative data(trial_data = (-1.0, -2.0, -3.0)) の場合, 限りなく0に近づく
# print(neural_network.commit(trial_data))
 
# 空の多重リストを用意
position_tokyo = [[], []]
position_kanagawa = [[], []]
for data in trial_data:
    if neural_network.commit(data) < 0.5:
        position_tokyo[0].append(data[1] + refer_point_1)
        position_tokyo[1].append(data[0] + refer_point_0)
    else:
        position_kanagawa[0].append(data[1] + refer_point_1)
        position_kanagawa[1].append(data[0] + refer_point_0)

# plot scatter( 経度，緯度 )
plt.scatter(position_tokyo[0], position_tokyo[1], c = "red", label = "Position_Tokyo", marker = "+")
plt.scatter(position_kanagawa[0], position_kanagawa[1], c = "blue", label = "Position_Kanagawa", marker = "+")

plt.legend(loc = "upper right")
# plt.title("グラフタイトル", fontproperties = fp)
plt.title("都道府県の分類", fontproperties = fp)
plt.xlabel("経度", fontproperties = fp)
plt.ylabel("緯度", fontproperties = fp)
plt.show()
