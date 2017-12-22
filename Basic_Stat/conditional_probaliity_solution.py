# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
from numpy import random
random.seed(0)

totals = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
purchases = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
totalPurchases = 0

for _ in range(100000):
    ageDecade = random.choice([20, 30, 40, 50, 60, 70])
#    purchaseProbality = float(ageDecade) / 100.0
    purchaseProbality = 0.4
    totals[ageDecade] += 1
    if (random.random() < purchaseProbality):
        totalPurchases += 1
        purchases[ageDecade] += 1

print("totals =", totals)
print("purchases =", purchases)
print("totalPurchases =", totalPurchases)
print("")


"""
P(E|F), E:購入, F:30代
"""
PEF = float(purchases[30]) / float(totals[30])
print("P(purchases | 30s):", PEF)

# P(F)
PF = float(totals[30]) / 100000.0
print("P(30's): ", PF)

# P(E): 年齢に関係ない、　全体の購入確率
PE = float(totalPurchases) / 100000.0
print("P(E) purchase: ", PE)

"""
もし，EとFが無関係なら，P(E|F)とP(E)はほぼ同じ確率になるはずだが，
PEF / PEを見ると依存関係がありそう.
"""
print("P(E|F) / P(E) = ", PEF / PE)

# 積
print("P(F) * P(E) =", PF * PE)

# 注意 P(E, F) != P(E|F)
# P(E|F)は30代であり，購入した両者を満たす確率. 総人口における確率であり，30代の中の確率ではない.
print("P(30's, Purchase)", float(purchases[30]) / 100000.0)

# P(E, F)とP(E)P(F)は近いが，EとFが依存関係にあり，データのランダム性もあるため，同じ値にはならない．

# P(E|F) = P(E, F) / P(F)
print("P(E|F) =", ( float(purchases[30]) / 100000.0 ) / PF )
