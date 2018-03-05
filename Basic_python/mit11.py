# coding: utf-8
import pylab
from mit08 import *

# 11.2 住宅ローン残高の図示
class Mortgage(object):
    """異なる住宅ローンを扱うための抽象クラス"""
    def __init__(self, loan, annRate, months):
        self.loan = loan
        self.rate = annRate/12.0
        self.months = months
        self.outstanding = [loan]
        self.payment = findPayment(loan, self.rate, months)
        self.legend = None # description of mortgage

    def makePayment(self):
        self.paid.append(self.payment)
        reduction = self.payment - self.outstanding[-1] * self.rate
        self.outstanding.append(self.outstanding[-1] - reduction)

    def getTotalPaid(self):
        return sum(self.paid)

    def __str__(self):
        return self.legend

    def plotPayments(self, style):
        pylab.plot(self.paid[1:], style, label = self.legend)

    def plotBalance(self, style):
        pylab.plot(self.outstanding, style, label = self.legend)

    def plotTotPd(self, style):
        totPd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            totPd.append(totPd[-1] + self.paid[i])
        pylab.plot(totPd, style, label = self.lenged)
        
    def plotNet(self, style):
        totPd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            totPd.append(totPd[-1] + self.paid[i])
            equityAcquired = pylab.array([self.loan] * len(self.outstanding))
            equityAcquired = equityAcquired - pylab.array(self.outstanding)
            net = pylab.array(totPd) - equityAcquired
            pylab.plot(net, style, label = self.legend)


if __name__ == '__main__':
    
    pylab.figure(0)
    pylab.plot([1,2,3,4], [1,7,3,5])

    pylab.figure(1)                  # figure1を作成
    pylab.plot([1,2,3,4], [1,2,3,4]) # figure1に作図
    pylab.figure(2)                  # figure2を作成
    pylab.plot([1,4,2,3], [5,6,7,8]) # figure2を作図
    pylab.savefig('Figure-Addie')    # figure2を保存
    pylab.figure(1)                  # figure1に戻る
    pylab.plot([5,6,10,3])           # figure1に再度作図
    pylab.savefig('Figure-Jane')     # figure1を保存

    # 11.1
    pylab.figure(3)
    principal = 10000 # 初期投資額
    interestRate = 0.05
    years = 20
    values = []
    for i in range(years + 1):
        values.append(principal)
        principal += principal * interestRate
    pylab.plot(values, linewidth = 30)
    pylab.plot(values, 'ko')
    
    pylab.title('5% Growth Compounded Annually',
                fontsize = 'xx-large')
    pylab.xlabel('Years of Compounding', fontsize = 'x-small')
    pylab.ylabel('Value of Principal ($)')

    # 線の太さの設定
    pylab.rcParams['lines.linewidth'] = 4
    # 題名に使われる文字の大きさの設定
    pylab.rcParams['axes.titlesize'] = 20
    # 軸の名前に使われる文字の大きさの設定
    pylab.rcParams['axes.labelsize'] = 20
    # x軸の数字の大きさの設定
    pylab.rcParams['xtick.labelsize'] = 16
    # y軸の数字の大きさの設定
    pylab.rcParams['ytick.labelsize'] = 16
    # x軸のメモリ幅の設定
    pylab.rcParams['xtick.major.size'] = 7
    # y軸のメモリ幅の設定
    pylab.rcParams['ytick.major.size'] = 7    
    # marker(円)の大きさの設定
    pylab.rcParams['lines.markersize'] = 10
    # 凡例においてマーカーを表示する回数
    pylab.rcParams['legend.numpoints'] = 1


    pylab.show()
