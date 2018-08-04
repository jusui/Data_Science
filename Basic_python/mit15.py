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
    # pylab.logx()
    # pylab.logy()    

def variance(X):
    """ X を数のリストとする, X の分散を返す """
    mean = sum(X) / len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    return tot / len(X)

def stdDev(X):
    """ X を数のリストとする, X の標準偏差を返す """
    return variance(X) ** 0.5

def makePlot(xVals, yVals, title, xLabel, yLabel, style,
             logX = False, logY = False):
    pylab.figure()
    pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.plot(xVals, yVals, style)
    if logX:
        pylab.semilogx()
    if logY:
        pylab.semilogx()

def runTrial(numFlips):
    numHeads = 0
    for n in range(numFlips):
        if random.choice(('H', 'T')) == 'H':
            numHeads += 1
    numTrials = numFlips - numHeads
    return (numHeads, numTrials)

def flipPlot1(minExp, maxExp, numTrials):
    """ int minExp, maxExp > 0 (min < max)
    2 ** minExp ~ 2 ** maxExp 回のコイン投げを numTRials 回行った結果の要約をプロット """

    ratiosMeans, diffsMeans, ratiosSDs, diffsSDs = [], [], [], []
    xAxis = []
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2 ** exp)
    for numFlips in xAxis:
        ratios, diffs = [], []
        for t in range(numTrials):
            numHeads, numTails = runTrial(numFlips)
            ratios.append(numHeads / numTrials)
            diffs.append(abs(numHeads - numTails))
        ratiosMeans.append(sum(ratios) / numTrials)
        diffsMeans.append(sum(diffs) / numTrials)
        ratiosSDs.append(stdDev(ratios))
        diffsSDs.append(stdDev(diffs))
    numTrialsString = ' (' + str(numTrials) + ' Trials)'
    title = 'Mean Heads / Tails Ratios' + numTrialsString
    makePlot(xAxis, ratiosMeans, title,
             'Number of flips', 'Mean Heads / Tails', 'ko', logX = True)
    title = 'SD Heads /Tails Ratios' + numTrialsString
    makePlot(xAxis, ratiosSDs, title,
             'Number of Flips', 'Standard Deviation', 'ko', logY = True)
    title = 'Mean abs(#Heads - #Trials)' + numTrialsString
    makePlot(xAxis, diffsMeans, title,
             'Number of Flips', 'Mean abs(#Heads - #Trials)', 'ko',
             logX = True, logY = True)
    title = 'SD abs(#Heads - #Trials)' + numTrialsString
    makePlot(xAxis, diffsSDs, title,
             'Number of Flips', 'Standard Deviation', 'ko',
             logX = True, logY = True)
    
def CV(X):
    ''' Coefficient of variation: std / mean '''
    mean = sum(X) / len(X)
    try:
        return stdDev(X) / mean
    except ZeroDivisionError:
        return float('nan')
    
def flipPlot2(minExp, maxExp, numTrials):
    """ int minExp, maxExp > 0 (min < max), numTrials > 0
    2 ** minExp ~ 2 ** maxExp 回のコイン投げを numTRials 回行った結果の要約をプロット """

    ratiosMeans, diffsMeans, ratiosSDs, diffsSDs = [], [], [], []
    ratiosCVs, diffsCVs, xAxis = [], [], []
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2 ** exp)
    for numFlips in xAxis:
        ratios, diffs = [], []
        for t in range(numTrials):
            numHeads, numTails = runTrial(numFlips)
            ratios.append(numHeads / numTrials)
            diffs.append(abs(numHeads - numTails))
        ratiosMeans.append(sum(ratios) / numTrials)
        diffsMeans.append(sum(diffs) / numTrials)
        ratiosSDs.append(stdDev(ratios))
        diffsSDs.append(stdDev(diffs))
        ratiosCVs.append(CV(ratios))
        diffsCVs.append(CV(diffs))
    numTrialsString = ' (' + str(numTrials) + ' Trials)'
    title = 'Mean Heads / Tails Ratios' + numTrialsString
    makePlot(xAxis, ratiosMeans, title,
             'Number of flips', 'Mean Heads / Tails', 'ko', logX = True)
    title = 'SD Heads /Tails Ratios' + numTrialsString
    makePlot(xAxis, ratiosSDs, title,
             'Number of Flips', 'Standard Deviation', 'ko', logY = True)
    title = 'Mean abs(#Heads - #Trials)' + numTrialsString
    makePlot(xAxis, diffsMeans, title,
             'Number of Flips', 'Mean abs(#Heads - #Trials)', 'ko',
             logX = True, logY = True)
    title = 'SD abs(#Heads - #Trials)' + numTrialsString
    makePlot(xAxis, diffsSDs, title,
             'Number of Flips', 'Standard Deviation', 'ko',
             logX = True, logY = True)
    title = 'Coeff of Var. Heads / Tails Ratio' + numTrialsString
    makePlot(xAxis, ratiosCVs, title, '# of Flips',
             'Coeff. of Var', 'ko', logX = True, logY = True)
    
if __name__ == "__main__":

    rollN(10)
    # print('Mean = ', flipSim(100, 1000))
    print('Mean = ', flipSim(100, 100000))
    regressToMean(15, 40)
    plt.figure()
    
    random.seed(0)
    flipPlot(4, 20)

    # flipPlot1(4, 20, 20)
    flipPlot2(4, 20, 20)    
    plt.show()
