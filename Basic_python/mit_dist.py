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

            
if __name__ == '__main__':

    # makePlots(100, 1000, 100000)

    # quad function : 1.積分の近似値，2.結果の絶対誤差推定    
    print(scipy.integrate.quad(abs, 0, 5)[0]) # 0 ~ 5 までの積分結果= 5 * 5 * (1/2)
    # mean = 0, std = 1, -2 <= x <= 2
    print(scipy.integrate.quad(gaussian, -2, 2, (0, 1))[0])

    checkEmpirical(3)
    
    # plt.show()
