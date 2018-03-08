# coding: utf-8
import pylab
from mit08 import findPayment

"""[MIT_DS:11]
https://akokubo.github.io/python-study-group-hachinohe/ """

# 11.2 住宅ローン残高の図示
class Mortgage(object):
    """異なる住宅ローンを扱うための抽象クラス"""
    def __init__(self, loan, annRate, months):
        self.loan = loan
        self.rate = annRate/12.0
        self.months = months
        self.paid = [0.0]
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
        """支払額の総額をプロット"""
        totPd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            totPd.append(totPd[-1] + self.paid[i])
        pylab.plot(totPd, style, label = self.legend)
        
    def plotNet(self, style):
        """住宅ローンの総費用の近似値を時系列的にプロット"""
        totPd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            totPd.append(totPd[-1] + self.paid[i])
        equityAcquired = pylab.array([self.loan] * len(self.outstanding))
        equityAcquired = equityAcquired - pylab.array(self.outstanding)
        net = pylab.array(totPd) - equityAcquired
        pylab.plot(net, style, label = self.legend)


# 11.3 Mortgage subclass
class Fixed(Mortgage):
    def __init__(self, loan, r, months):
        Mortgage.__init__(self, loan, r, months)
        self.legend = 'Fixed, ' + str(r * 100) + '%'

class FixedWithPts(Mortgage):
    def __init__(self, loan, r, months, pts):
        Mortgage.__init__(self, loan, r, months)
        self.pts = pts
        self.paid = [loan * (pts / 100.0)]
        self.legend = 'Fixed, ' + str(r * 100) + '%, ' + str(pts) + ' points'

class TwoRate(Mortgage):
    def __init__(self, loan, r, months, teaserRate, teaserMonths):
        Mortgage.__init__(self, loan, teaserRate, months)
        self.teaserMonths = teaserMonths
        self.teaserRate = teaserRate
        self.nextRate = r / 12.0
        self.legend = str(teaserRate * 100) \
                       + '% for ' + str(self.teaserMonths) \
                       + ' months, then ' + str(r * 100) + '%'

    def makePayment(self):
        if len(self.paid) == self.teaserMonths + 1:
            self.rate = self.nextRate
            self.payment = findPayment(self.outstanding[-1],
                                       self.rate,
                                       self.months - self.teaserMonths)
        Mortgage.makePayment(self)

            
def compareMortgages(amt, years, fixedRate, pts, ptsRate,
                     varRate1, varRate2, varMonths):
    totMonths = years * 12
    fixed1 = Fixed(amt, fixedRate, totMonths)
    fixed2 = FixedWithPts(amt, ptsRate, totMonths, pts)
    twoRate = TwoRate(amt, varRate2, totMonths, varRate1, varMonths)
    morts = [fixed1, fixed2, twoRate]
    for m in range(totMonths):
        for mort in morts:
            mort.makePayment()
    plotMortgages(morts, amt)

    
def plotMortgages(morts, amt):
    def labelPlot(figure, title, xLabel, yLabel):
        pylab.figure(figure)
        pylab.title(title)
        pylab.xlabel(xLabel)
        pylab.ylabel(yLabel)
        pylab.legend(loc = 'best')
        
    styles = ['k-', 'k-', 'k:']
    # 図を指定する際，番号の代わりに名前を用いる
    payments, cost, balance, netCost = 0, 1, 2, 3
    for i in range(len(morts)):
        pylab.figure(payments)
        morts[i].plotPayments(styles[i])
        pylab.figure(cost)
        morts[i].plotTotPd(styles[i])
        pylab.figure(balance)
        morts[i].plotBalance(styles[i])
        pylab.figure(netCost)
        morts[i].plotNet(styles[i])
    labelPlot(payments, 'Monthly Payments of $' + str(amt) +
              ' Mortgages', 'Months', 'Monthly Payments')
    labelPlot(cost, 'Cash Outlay of $' + str(amt) +
              ' Mortgages', 'Months', 'Total Payments')
    labelPlot(balance, 'Balance Remainng of $ ' + str(amt) +
              ' Mortgages', 'Months', 'Remaining Loan Balance of $')
    labelPlot(netCost, 'Net Cost of $' + str(amt) + 
              'Mortgages', 'Months', 'Payments - Equity $')

    
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

    # 11.2
    a1 = pylab.array([1, 2, 4])
    print('a1 =', a1)
    a2 = a1 * 2
    print('a2 =', a2)
    print('a1 + 3 =', a1 + 3)
    print('3 - a1 =', 3 - a1)
    print('a1 - a2 =', a1 - a2)
    print('a1 * a2 =', a1 * a2)

    

    # 11.5
    pylab.figure(4)
    compareMortgages(amt = 200000, years = 30, fixedRate = 0.07,
                     pts = 3.25, ptsRate = 0.05,
                     varRate1 = 0.045, varRate2 = 0.095, varMonths = 48)
    
    pylab.show()
