# coding:utf-8

import random
from mit14 import *

'''
Drunk:
UsualDrunk:
'''

class Drunk(object):
    def __init__(self, name = None):
        """ string name """
        self.name = name

    def __str__(self):
        if self != None:
            return self.name
        return 'Annonymous'

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return random.choice(stepChoices)

class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0, 1.0), (0.0, -2.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

class EWDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

def walk(f, d, numSteps):
    """ f: Field class object
    d: Drunk class object
    numSteps: integer (>= 0)
    d * numSteps move and diff(end - start) position """

    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distForm(f.getLoc(d))


def simAll(drunkKinds, walkLengths, numTrials):
    for dClass in drunkKinds:
        drunkTest(walkLengths, numTrials, dClass)

def simWalks(numSteps, numTrials, dClass):
    """ int numSteps(>= 0)
    int numTrials > 0
    dClass:Drunk sub class
    Simulate numSteps of move random walk * numTrials """
    Homer = dClass()
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        distances.append(round(walk(f, Homer, numSteps), 1))
    return distances

def drunkTest(walkLengths, numTrials, dClass):
    """ int walkLengths >= 0 sequence
    walkLengths の各要素を酔歩の移動回数として，numTrials回の酔歩を
    シミュレートするsimWawlks を実行し結果を出力する"""

    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        print(dClass.__name__, 'random walk of ', numSteps, 'steps')
        print(' Mean = ', round(sum(distances) / len(distances), 4))
        print(' Max = ', max(distances), ' Min = ', min(distances))

        
if __name__ == '__main__':

    print("============================")
    print("Let's simulate random walk !")
    print("============================")    
    #    drunkTest((10, 100, 1000, 10000), 100, UsualDrunk)
    #    drunkTest((0, 1), 100, UsualDrunk)    
    simAll((UsualDrunk, ColdDrunk, EWDrunk), (100, 1000), 10)
