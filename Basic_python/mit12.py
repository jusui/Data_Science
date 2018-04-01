# coding: utf-8
from mit09 import getPowerset

class Item(object):
    # Item class
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value) \
                 + ', ' + str(self.weight) + '>'
        return result

def value(item):
    return item.getValue()

def weightInverse(item):
    return 1.0 / item.getWeight()

def density(item):
    return item.getValue() / item.getWeight()


def greedy(items, maxWeight, keyFunction):
    """ items はリスト，maxWeight >= 0とし，
    keyFunctionはitemsの要素を数にマップする """
    
    itemsCopy = sorted(items, key = keyFunction, reverse = True)
    result = []
    totalValue, totalWeight = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if ( totalWeight + itemsCopy[i].getWeight() ) <= maxWeight:
            result.append(itemsCopy[i])
            totalWeight += itemsCopy[i].getWeight()
            totalValue  += itemsCopy[i].getValue()
            
    return (result, totalValue)

def buildItems():
    names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
    values = [175, 90, 20, 50, 10, 200]
    weights = [10, 9, 4, 2, 1, 20]
    Items = []
    for i in range(len(values)):
        Items.append(Item(names[i], values[i], weights[i]))
    return Items

def testGreedy(items, maxWeight, keyFunction):
    taken, val = greedy(items, maxWeight, keyFunction)
    print('Total value of items taken is ', val)
    for item in taken:
        print(' ', item)

def testGreedys(maxWeight = 20):
    items = buildItems()
    print('Use greedy by value to fill knapsack of size', maxWeight)
    testGreedy(items, maxWeight, value)
    print('\nUse greedy by weight to fill knapsack of size', maxWeight)
    testGreedy(items, maxWeight, weightInverse)
    print('\nUse greedy by weight to fill knapsack of size', maxWeight)

    testGreedy(items, maxWeight, density)


"""
0/1 Knapsack problem

1．すべての品物の組み合わせを列挙する。品物集合のすべての部分集合を作る。べき集合。
2．重量制限を超えるような品物の組み合わせを取り除く。
3．残された組み合わせの内，総価値が最も大きいものを選ぶ。
"""

def chooseBest(pset, maxWeight, getVal, getWeight):

    bestVal = 0.0
    bestSet = None
    for items in pset:
        itemsVal = 0.0
        itemsWeight = 0.0
        for item in items:
            itemsVal += getVal(item)
            itemsWeight += getWeight(item)
        if itemsWeight <= maxWeight and itemsVal > bestVal:
            bestVal = itemsVal
            bestSet = items

    return (bestSet, bestVal)

def testBest(maxWeight = 20):
    """ getPowerset(): list L. 全ての可能な組み合わせからなるリストを返す
    (e.f.) L = [1, 2]ならば，[], [1], [2], [1,2]を要素に持つリストを返す """
    
    items = builditems()
    pset = getPowerset(items)
    taken, val = chooseBest(pset, maxWeight, Item.getValue,
                            Item.getWeight)
    print('Total value of items taken is', val)
    for item in taken:
        print(item)
        
    
if __name__ == '__main__':

    testGreedys()
    
    
