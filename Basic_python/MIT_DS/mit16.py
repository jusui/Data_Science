# coding: utf-8
import random
from mit15 import *

def rollDie():
    return random.choice([1, 2, 3, 4, 5, 6])

def checkPascal(numTrials):
    """
    param: int numTrials >= 1
    """
    numWins = 0
    for i in range(numTrials):
        for j in range(24):
            d1 = rollDie()
            d2 = rollDie()
            if d1 == 6 and d2 == 6:
                numWins += 1
                break
    print('Probability of winning = ', numWins / numTrials)


class CrapsGame(object):
    def __init__(self):
        self.passWins, self.passLosses = 0, 0
        self.dpWins, self.dpLosses, self.dpPushes = 0, 0, 0

    def playHand(self):
        throw = rollDie() + rollDie()
        if throw == 7 or throw == 11:
            self.passWins += 1
            self.dpLosses += 1
        elif throw == 2 or throw == 3 or throw == 12:
            self.passLosses += 1
            if throw == 12:
                self.dpPushes += 1
            else:
                self.dpWins += 1
        else:
            point = throw
            while True:
                throw = rollDie() + rollDie()
                if throw == point:
                    self.passWins += 1
                    self.dpLosses += 1
                    break
                elif throw == 7:
                    self.passLosses += 1
                    self.dpWins += 1
                    break
                
    def passResults(self):
        return (self.passWins, self.passLosses)

    def dpResults(self):
        return (self.dpWins, self.dpLosses, self.dpPushes)

    
def crapsSim(handsPerGame, numGames):
    """
    int handsPerGame, numGames <= 1
    """
    games = []
    # numGames回プレイ
    for t in range(numGames):
        c = CrapsGame()
        for i in range(handsPerGame):
            c.playHand()
            games.append(c)

    pROIPerGame, dpROIPerGame = [], []
    for g in games:
        wins, losses = g.passResults()
        pROIPerGame.append((wins - losses) / float(handsPerGame))
        wins, losses, pushes = g.dpResults()
        dpROIPerGame.append((wins - losses)/float(handsPerGame))

    # show stats
    meanROI = str(round((100 * sum(pROIPerGame)/numGames), 4)) + '%'
    sigma = str(round(100 * stdDev(pROIPerGame), 4)) + '%'
    print('Pass:', 'Mean ROI =', meanROI, 'Std. Dev = ', sigma)
    meanROI = str(round((100 * sum(dpROIPerGame)/numGames), 4)) + '%'
    sigma = str(round(100 * stdDev(dpROIPerGame), 4)) + '%'
    print('Don\'t pass:', 'Mean ROI =', meanROI, 'std Dev =', sigma)

    
if __name__ == '__main__':
    # checkPascal(1000000)
    crapsSim(20, 10)
