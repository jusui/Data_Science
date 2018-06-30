# coding:utf-8
from mit12 import *
import random

"""
13. Dynamic programming
"""

def fib(n):
    """
    int n(>= 0). return fibonacci number
    """
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fastFib(n, memo = {}):
    """
    int n(>= 0). memo only call recursion.
    t_calc ~ O(n)
    """
    if n == 0 or n == 1:
        return 1

    try:
        return memo[n]
    
    except KeyError:
        result = fastFib(n - 1, memo) + fastFib(n - 2, memo)
        memo[n] = result
        return result

def maxVal(toConsider, avail):
    """ toConsider:product list, avail:available weight.
    return (total value, product list)
    """

    if toConsider == [] or avail == 0:
        result = (0, ())

    elif toConsider[0].getWeight() > avail:
        # search for right node
        result = maxVal(toConsider[1:], avail)

    else:
        nextItem = toConsider[0]
        withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getWeight())

        withVal += nextItem.getValue()
        # search for left node
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)

        # select best node
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem, ))
        else:
            result = (withoutVal, withoutToTake)

    return result


def smallTest():
    names = ['a', 'b', 'c', 'd']
    vals = [6, 7, 8, 9]
    weights = [3, 3, 2, 5]
    Items = []

    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))

    val, taken = maxVal(Items, 5)
    for item in taken:
        print(item)

    print('Total value of items taken = ', val)

def buildManyItems(numItems, maxVal, maxWeight):
    items = []
    for i in range(numItems):
        items.append(Item(str(i),
                          random.randint(1, maxVal),
                          random.randint(1, maxWeight)))

    return items

def bigTest(numItems):
    items = buildManyItems(numItems, 10, 10)
    val, taken = maxVal(items, 40)
    print('Items taken')
    for item in taken:
        print(item)
    print('Total value of items taken = ', val)


if __name__ == "__main__":

    # print(fib(10)) ### not fast to calculate fibnacci
    print(fastFib(120))
    
    print(smallTest())
    print(bigTest(10))
