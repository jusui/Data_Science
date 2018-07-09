# coding:utf-8
import random

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


if __name__ == "__main__":

    rollN(10)
    for i in range(10):
        print('Mean = ', flipSim(10, 1))
    
