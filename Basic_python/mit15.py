# coding:utf-8
import random
import pylab
import matplotlib.pyplot as plt

'''
MIT.15 Probability, Statistics and Programs
'''


def squareRoot(x, epsilon):
    """ float x >= 0, epsilon > 0, y
    x - epsilon <= x * y <= x + epsilon """
    
    return y

def rollDie():
    """ int 1 - 6 """
    return random.choice([1,2,3,4,5,6])


def rollN(n):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    print(result)


'''
15.2 Simulation of number of flips per trial
'''    
def flip(numFlips):
    """ numFlips: int > 0 """
    heads = 0
    for i in range(numFlips):
        if random.choice(('H', 'T')) == 'H':
            heads += 1
    return heads / numFlips

def flipSim(numFlipsPerTrial, numTrials):
    """ numFlipsPerTrial, numTrials: int > 0 """
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean = sum(fracHeads) / len(fracHeads)
    return mean


def regressToMean(numFlips, numTrials):
    # numFlips 回Coinを投げ，numTrials回試行して表が出る確率
    fracHeads = []
    for t in range(numTrials):
        fracHeads.append(flip(numFlips))

    # 極端な値がでる試行とその次の試行を得る
    extremes, nextTrials = [], []
    for i in range(len(fracHeads) - 1):
        if fracHeads[i] < 0.33 or fracHeads[i] > 0.66:
            extremes.append(fracHeads[i])
            nextTrials.append(fracHeads[i + 1])

            
    # plot result
    pylab.plot(range(len(extremes)), extremes, 'ko', label = 'Extremes')
    pylab.plot(range(len(nextTrials)), nextTrials, 'k^', label = 'Next Trial')

    pylab.axhline(0.5)
    pylab.ylim(0, 1)
    pylab.xlim(-1, len(extremes) + 1)
    pylab.xlabel('Extreme Example and Next Trial')
    pylab.ylabel('Fraciton Heads')
    pylab.title('Regression to the Mean')
    pylab.legend(loc = 'best')
    

def flipPlot(minExp, maxExp):
    """ int minExp, maxExp > 0 (min < max)
    2**minExp ~ 2**maxExp 回のコイン投げの結果をプロット """
    ratios, diffs, xAxis = [], [], []

    for exp in range(minExp, maxExp + 1):
        xAxis.append(2 ** exp)
    for numFlips in xAxis:
        numHeads = 0
        for n in range(numFlips):
            if random.choice(('H', 'T')) == 'H':
                numHeads += 1
        numTrials = numFlips - numHeads
        try:
            ratios.append(numHeads / numTrials)
            diffs.append(abs(numHeads -- numTrials))
        except ZeroDivisionError:
            continue
        
    pylab.title('Difference between Heads and Trials')
    pylab.xlabel('# of Flips')
    pylab.ylabel('Abs(#Heads - #Trials)')
    pylab.plot(xAxis, diffs, 'k')
    pylab.figure()
    pylab.title('Heads/Tails Ratios')
    pylab.xlabel('# of Flips')
    pylab.ylabel('#Heads/#Tails')
    pylab.plot(xAxis, ratios, 'k')

            
if __name__ == "__main__":

    rollN(10)
    # print('Mean = ', flipSim(100, 1000))
    print('Mean = ', flipSim(100, 100000))
    regressToMean(15, 40)
    plt.figure()
    
    random.seed(0)
    flipPlot(4, 20)
    plt.show()
