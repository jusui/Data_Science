# coding: utf-8
import random
import matplotlib.pyplot as plt
from mit15 import *
import scipy as sp
import scipy.integrate

def flip(numFlips):
    """ int numFlips > 0 """
    heads = 0
    for i in range(numFlips):
        if random.choice(('H', 'T')) == 'H':
            heads += 1
    return heads / float(numFlips)

def flipSim(numFlipsPerTrial, numTrials):
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))

    mean = sum(fracHeads) / len(fracHeads)
    sd = stdDev(fracHeads)
    return (fracHeads, mean ,sd)

def labelPlot(numFlips, numTrials, mean, sd):
    pylab.title(str(numTrials) + ' trials of '
                + str(numFlips) + ' flips each')
    pylab.xlabel('Fraction of Heads')
    pylab.ylabel('Number of Trials')
    pylab.annotate('Mean = ' + str(round(mean, 4))
                   + '\nSD = ' + str(round(sd, 4)), size = 'x-large',
                   xycoords = 'axes fraction', xy = (0.67, 0.5))

def makePlots(numFlips1, numFlips2, numTrials):
    val1, mean1, sd1 = flipSim(numFlips1, numTrials)
    pylab.hist(val1, bins = 20)
    xmin, xmax = pylab.xlim()
    labelPlot(numFlips1, numTrials, mean1, sd1)
    pylab.figure()
    val2, mean2, sd2 = flipSim(numFlips2, numTrials)
    pylab.hist(val2, bins = 20)
    pylab.xlim(xmin, xmax)
    labelPlot(numFlips2, numTrials, mean2, sd2)

def gaussian(x, mu, sigma):
    factor1 = (1.0 / (sigma * ((2 * pylab.pi) ** 0.5)))
    factor2 = pylab.e ** -(((x - mu) ** 2) / (2 * sigma ** 2))
    return factor1 * factor2


def checkEmpirical(numTrials):
    for t in range(numTrials):
        mu = random.randint(-10, 10)
        sigma = random.randint(1, 10)
        print('For mu =', mu, 'and sigma =', sigma)
        for numStd in (1, 2, 3):
            area = scipy.integrate.quad(gaussian, mu - numStd * sigma,
                                        mu + numStd * sigma,
                                        (mu, sigma))[0]
            print(' Fraction within', numStd, 'std =', round(area, 4))

def showErrorBars(minExp, maxExp, numTrials):
    """ int minExp, maxExp, numTrials > 0 (minExp < maxExp) """

    means, sds, xVals = [], [], []
    for exp in range(minExp, maxExp + 1):
        xVals.append(2 ** exp)
        fracHeads, mean, sd = flipSim(2 ** exp , numTrials)
        means.append(mean)
        sds.append(sd)

    # 1.96 : Data of 95 % is in std * 1.96
    pylab.errorbar(xVals, means, yerr=1.96 * pylab.array(sds))
    pylab.semilogx()
    pylab.title('Mean Fraction of Heads ('
                + str(numTrials) + ' trials)' )
    pylab.xlabel('# of flips per trial')
    pylab.ylabel('Fraction of heads & 95 % confidence')
    pylab.figure()
    
    
def clear(n, p, steps):
    """ int  n, steps > 0, float p
    n : 分子の初期個数
    p : 分子が消滅する確率 """

    numRemaining = [n]
    for t in range(steps):
        numRemaining.append(n * (1 - p) ** t)

    pylab.plot(numRemaining)
    pylab.xlabel('Time')
    pylab.ylabel('Molecules Remaining')
    pylab.title('Clearance of Drug')
    pylab.figure()
    
def successfulStarts(successProb, numTrials):
    """ eventProb: 1回の試行で成功する確率を表す浮動小数点数, numTrials: 正の整数
    各実験において，成功するまでに必要な試行回数を出力 """

    triesBeforeSuccess = []
    for t in range(numTrials):
        consecFailures = 0
        while random.random() > successProb:
            consecFailures += 1
        triesBeforeSuccess.append(consecFailures)
    return triesBeforeSuccess

def collisionProb(n, k):
    prob = 1.0
    for i in range(1, k):
        prob = prob * ((n - i) / n)
    return 1 - prob

def simInsertions(numIndices, numInsertions):
    """ int numIndices, numInsertions > 0 
    if collision return 1, else return 0 """

    choices = range(numIndices) # list of possible indices
    used = []
    for i in range(numInsertions):
        hashVal = random.choice(choices)
        if hashVal in used: # there is a collision
            return 1
        else:
            used.append(hashVal)
    return 0

def findProb(numIndices, numInsertions, numTrials):
    collisions = 0
    for t in range(numTrials):
        collisions += simInsertions(numIndices, numInsertions)
    return collisions / numTrials


""" Simulation of validation of World Series """

def playSeries(numGames, teamProb):
    numWon = 0
    for game in range(numGames):
        if random.random() >= teamProb:
            numWon += 1
    return (numWon > numGames // 2)

def fractionWon(teamProb, numSeries, seriesLen):
    won = 0
    for series in range(numSeries):
        if playSeries(seriesLen, teamProb):
            won += 1
    return won / float(numSeries)

def simSeries(numSeries):
    prob = 0.5
    fracsWon, probs = [], []
    while prob <= 1.0:
        fracsWon.append(fractionWon(prob, numSeries, 7))
        probs.append(prob)
        prob += 0.01
    pylab.axhline(0.95) # Draw line at 95 %
    pylab.plot(probs, fracsWon, 'k', linewidth = 5)
    pylab.xlabel('Prob of Winning a Game')
    pylab.ylabel('Prob of Winning a Series')
    pylab.title(str(numSeries) + ' Seven-Game Series')




            

if __name__ == '__main__':

    # makePlots(100, 1000, 100000)

    # quad function : 1.積分の近似値，2.結果の絶対誤差推定    
    print(scipy.integrate.quad(abs, 0, 5)[0]) # 0 ~ 5 までの積分結果= 5 * 5 * (1/2)
    # mean = 0, std = 1, -2 <= x <= 2
    print(scipy.integrate.quad(gaussian, -2, 2, (0, 1))[0])

    checkEmpirical(3)

    showErrorBars(3, 10, 100) # 100

    clear(1000, 0.01, 1000)

    ## 指数関数的増加 ##
    probOfSuccess = 0.5
    numTrials = 5000
    distribution = successfulStarts(probOfSuccess, numTrials)
    pylab.hist(distribution, bins = 14)
    pylab.xlabel('Tries Before Success')
    pylab.ylabel('# of Occurrences Out of ' + str(numTrials))
    pylab.title('Probability of Starting Each Try = ' + str(probOfSuccess))

    print('Actual probability of a collision = ', collisionProb(1000, 50))
    print('Est. probability of a collision = ', findProb(1000, 50, 10000))
    print('Actual probability of a collision = ', collisionProb(1000, 200))
    print('Est. probability of a collision = ', findProb(1000, 200, 10000))
    pylab.figure()

    simSeries(1000)
    plt.show()
