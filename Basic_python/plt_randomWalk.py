# coding:utf-8
import pylab
import matplotlib.pyplot as plt
from Drunk import *
from mit14 import *


class styleIterator(object):
    def __init__(self, styles):
        self.index = 0
        self.styles = styles

    def nextStyle(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) - 1:
            self.index = 0
        else:
            self.index += 1
        return result

def simDrunk(numTrials, dClass, walkLengths):
    meanDistances = []
    for numSteps in walkLengths:
        print('Starting simulation of ', numSteps, 'steps')
        trials = simWalks(numSteps, numTrials, dClass)
        mean = sum(trials) / len(trials)
        meanDistances.append(mean)
    return meanDistances

def simAll1(drunkKinds, walkLengths, numTrials):
    styleChoice = styleIterator(('m-', 'r:', 'k-.'))
    for dClass in drunkKinds:
        curStyle = styleChoice.nextStyle()        
        print('Starting simulation of ', dClass.__name__)
        means = simDrunk(numTrials, dClass, walkLengths)
        pylab.plot(walkLengths, means, curStyle, label = dClass.__name__)
        
    pylab.title('Mean Distance from Origin('+ str(numTrials) + ' trials)')
    pylab.xlabel("Number of Steps")
    pylab.ylabel("Distance from origin")
    pylab.legend(loc = "best")
    pylab.semilogx()
    pylab.semilogy()


def getFinalLocs(numSteps, numTrials, dClass):
    locs = []
    d = dClass()
    for t in range(numTrials):
        f = Field()
        f.addDrunk(d, Location(0, 0))
        for s in range(numSteps):
            f.moveDrunk(d)
        locs.append(f.getLoc(d))
    return locs

def plotLocs(drunkKinds, numSteps, numTrials):
    styleChoice = styleIterator(('k+', 'r^', 'mo'))

    for dClass in drunkKinds:
        locs = getFinalLocs(numSteps, numTrials, dClass)
        xVals, yVals = [], []
        for loc in locs:
            xVals.append(loc.getX())
            yVals.append(loc.getY())
        meanX = sum(xVals) / len(xVals)
        meanY = sum(yVals) / len(yVals)
        curStyle = styleChoice.nextStyle()
        pylab.plot(xVals, yVals, curStyle,
                   label = dClass.__name__ + ' mean loc. = <'
                   + str(meanX) + ', ' + str(meanY) + '>')
        pylab.title('Location at End of Walks (' + str(numSteps) + ' steps)' )
        pylab.xlabel('Steps East/West of Origin')
        pylab.ylabel('Steps North/South of Origin')
        pylab.legend(loc = 'lower/left')


def traceWalk(drunkKinds, numSteps):
    styleChoice = styleIterator(('k+', 'r^', 'mo'))
    f = Field()
    for dClass in drunkKinds:
        d = dClass()
        f.addDrunk(d, Location(0, 0))
        locs = []
        for s in range(numSteps):
            f.moveDrunk(d)
            locs.append(f.getLoc(d))
        xVals, yVals = [], []
        for loc in locs:
            xVals.append(loc.getX())
            yVals.append(loc.getY())
        curStyle = styleChoice.nextStyle()
        pylab.plot(xVals, yVals, curStyle,
                   label = dClass.__name__)
        pylab.title('Spots Visited on Walk (' + str(numSteps) + ' steps)')
        pylab.xlabel('Steps East / West of Origin')
        pylab.ylabel('Steps North / South of Origin')
        pylab.legend(loc = 'best')
        
if __name__ == '__main__':
    # simAll1((UsualDrunk, ColdDrunk, EWDrunk),
    #        (10, 100, 1000, 10000), 100)

    plotLocs((UsualDrunk, ColdDrunk, EWDrunk), 100, 200)
    plt.figure()

    traceWalk((UsualDrunk, ColdDrunk, EWDrunk), 200)
    plt.show()    
