# coding: UTF-8
import math
import matplotlib.pyplot as plt
from  matplotlib.font_manager import FontProperties
fp = FontProperties(fname=r'/Library/fonts/ipag.ttf', size=11)
    
def sigmoid(a):
    return 1.0 / (1.0 + math.exp(-a))


""" ニューロンclass """
class Neuron:
    # 入力値の合計, 出力値の初期化
    input_sum = 0.0
    output = 0.0
    
    # 入力値をinputに足す
    def setInput(self, inp):
        self.input_sum += inp
#        print(self.input_sum)

    # sigmoid() で, 入力値を出力値に変換
    def getOutput(self):
        self.output = sigmoid(self.input_sum)
        return self.output

    def reset(self):
        self.input_sum = 0
        self.output = 0

        
""" NeuralNetwork class"""
class NeuralNetwork:
    # Weight [input1, input2, bias]
    # (3 * 2)入力層[0, 1, 2] - 中間層[0, 1, 2]
    w_im = [[0.496, 0.512], [-0.501, 0.998], [0.498, -0.502]]
    # (3 * 1)中間層 - 出力層
    w_mo = [0.121, -0.4996, 0.200]
    
    # Neuron instance (e.f. neuron = Neuron())
    input_layer = [0.0, 0.0, 1.0]
    middle_layer = [Neuron(), Neuron(), 1.0]
    output_layer = Neuron()

    # Execute, データを読む度にreset() で0に初期化
    def commit(self, input_data):
        # initialize data
        self.input_layer[0] = input_data[0]
        self.input_layer[1] = input_data[1]

        # 各層のリセット        
        self.middle_layer[0].reset()
        self.middle_layer[1].reset()
        self.output_layer.reset()

        # 入力層(2) -> 中間層(3)
        self.middle_layer[0].setInput(self.input_layer[0] * self.w_im[0][0])
        self.middle_layer[0].setInput(self.input_layer[1] * self.w_im[1][0])
        self.middle_layer[0].setInput(self.input_layer[2] * self.w_im[2][0])        

        self.middle_layer[1].setInput(self.input_layer[0] * self.w_im[0][1])
        self.middle_layer[1].setInput(self.input_layer[1] * self.w_im[1][1])
        self.middle_layer[1].setInput(self.input_layer[2] * self.w_im[2][1])

        # 中間層(3) -> 出力層(1)
        self.output_layer.setInput(self.middle_layer[0].getOutput() * self.w_mo[0])
        self.output_layer.setInput(self.middle_layer[1].getOutput() * self.w_mo[1])
        self.output_layer.setInput(self.middle_layer[2] * self.w_mo[2])

        # neuron.getOutput() method でsigmoid()変換後の返り値を与える
        return self.output_layer.getOutput()


    """ 学習関数 """
    def learn(self, input_data):
        # 出力値(commit()内で各層毎にinputしたデータをoutput_dataに格納)
        # print(input_data)
        output_data = self.commit([input_data[0], input_data[1]])
        
        # 正解値(input[2])の定義と誤差計算
        correct_value = input_data[2]
        # print(output_data)
        # print("誤差(正解 - output) =:", correct_value - output_data)

        # 学習係数
        k = 0.3

        """ 逆伝播:出力層 -> 中間層 (δmo = (出力値-正解値) * 出力の微分) """
        # 中間層を掛けることで，同じ割合で修正
        delta_w_mo = ( correct_value - output_data ) * output_data * (1.0 -output_data )

        """ 逆伝播したニューロンとバイアスを更新 """
        old_w_mo = list(self.w_mo) # list で同クラス内のself.w_moを代入
        # neuron(w_mo[0], [1]), Bias(w_mo[2])とそれぞれ更新
        self.w_mo[0] += self.middle_layer[0].output * delta_w_mo * k
        self.w_mo[0] += self.middle_layer[1].output * delta_w_mo * k
        self.w_mo[2] += self.middle_layer[2] * delta_w_mo * k

        """ 中間層 -> 入力層 """
        delta_w_im = [
            delta_w_mo * old_w_mo[0] * self.middle_layer[0].output \
            * (1.0 - self.middle_layer[0].output), \
            delta_w_mo * old_w_mo[0] * self.middle_layer[0].output \
            * (1.0 - self.middle_layer[0].output)
        ]

        self.w_im[0][0] += self.input_layer[0] * delta_w_im[0] * k
        self.w_im[0][1] += self.input_layer[0] * delta_w_im[1] * k
        self.w_im[1][0] += self.input_layer[1] * delta_w_im[0] * k
        self.w_im[1][1] += self.input_layer[1] * delta_w_im[1] * k
        self.w_im[2][0] += self.input_layer[2] * delta_w_im[0] * k
        self.w_im[2][1] += self.input_layer[2] * delta_w_im[1] * k
        
# 位置データの基準点(データの範囲を0.0 ~ 1.0に収める)
refer_point_0 = 34.5
refer_point_1 = 137.5

"""
Read file (緯度, 経度)
データをrstrip() で読み，split(",")で分割する
データを読み込み，緯度経度から基準点を引いて格納する
"""
training_data = []
training_data_file = open("./training-data.txt", "r")
for line in training_data_file:
    line = line.rstrip().split(",")
    training_data.append([ float(line[0]) - refer_point_0, \
                        float(line[1]) - refer_point_1, \
                        int(line[2]) ])
training_data_file.close()
print("training_data = {}".format(training_data))


# Neural Network のインスタンス
neural_network = NeuralNetwork()

""" 学習(1000回)  = 1000回 * 100 data試行""" 
# (orig) neural_network.learn(training_data[0])
for i in range(0, 1000):
    for data in training_data:
        neural_network.learn(data)        

print("neural_network.w_im = ", neural_network.w_im)
print("neural_network.w_mo = ", neural_network.w_mo)

print("")

im = [[0.496, 0.512], [-0.501, 0.998], [0.498, -0.502]]
mo = [0.121, -0.4996, 0.200]

print("更新後の(im)差[%] = ", (neural_network.w_im[0][0] / im[0][0]) * 100)
print("更新後の(im)差[%] = ", (neural_network.w_im[0][1] / im[0][1]) * 100)
print("更新後の(im)差[%] = ", (neural_network.w_im[1][0] / im[1][0]) * 100)
print("更新後の(im)差[%] = ", (neural_network.w_im[1][1] / im[1][1]) * 100)
print("更新後の(im)差[%] = ", (neural_network.w_im[2][0] / im[2][0]) * 100)
print("更新後の(im)差[%] = ", (neural_network.w_im[2][1] / im[2][1]) * 100)
print("更新後の(mo)差[%] = ", (neural_network.w_mo[0] / mo[0]) * 100)
print("更新後の(mo)差[%] = ", (neural_network.w_mo[1] / mo[1]) * 100)


""" 実行 """
data_to_commit = [ [34.6, 138.0], [34.6, 138.18], [35.4, 138.0], [34.98, 138.1], \
                  [35.0, 138.25], [35.4, 137.6], [34.98, 137.52], [34.5, 138.5] ]

for data in data_to_commit:
    data[0] -= refer_point_0
    data[1] -= refer_point_1

position_tokyo_learned = [[], []]
position_kanagawa_learned = [[], []]

for data in data_to_commit:
    if neural_network.commit(data) < 0.5:
        position_tokyo_learned[0].append(data[1] + refer_point_1)
        position_tokyo_learned[1].append(data[0] + refer_point_0)

    else:
        position_kanagawa_learned[0].append(data[1] + refer_point_1)
        position_kanagawa_learned[1].append(data[0] + refer_point_0)
        
""" 
Execute, commit methodを呼び出す 
訓練用データの表示をを準備
"""
position_tokyo = [[], []]
position_kanagawa = [[], []]
for data in training_data:
    if neural_network.commit(data) < 0.5:
        position_tokyo[0].append(data[1] + refer_point_1)
        position_tokyo[1].append(data[0] + refer_point_0)
    else:
        position_kanagawa[0].append(data[1] + refer_point_1)
        position_kanagawa[1].append(data[0] + refer_point_0)        

# plot scatter( 経度，緯度 )
plt.scatter(position_tokyo[0], position_tokyo[1], c = "red", label = "Tokyo", marker = "+")
plt.scatter(position_kanagawa[0], position_kanagawa[1], c = "blue", label = "Kanagawa", marker = "+")

plt.scatter(position_tokyo_learned[0], position_tokyo_learned[1], c = "red", label = "Tokyo_Learned", marker = "o")
plt.scatter(position_kanagawa_learned[0], position_kanagawa_learned[1], c = "blue", label = "Kanagawa_Learned", marker = "o")


plt.legend(loc = "upper right")
# plt.title("グラフタイトル", fontproperties = fp)
plt.title("都道府県の分類", fontproperties = fp)
plt.xlabel("経度", fontproperties = fp)
plt.ylabel("緯度", fontproperties = fp)
plt.show()
