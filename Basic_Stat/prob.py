# coding: utf-8
from collections import Counter
import math, random
import matplotlib.pyplot as ptl
from scipy import stats

"""[DS from scratch]6. probability/確率 """

# [6.1]従属と独立
"""事象E，F両者が独立である場合，P(E, F) = P(E)P(F) """

# [6.2]条件付き確率
"""FにおけるEの条件付き確率，P(E|F) = P(E, F) / P(F)
Fが発生したことを知っている状況でEが発生する確率"""

def random_kid():
    """ boy, girlをランダムに選択 """
    return random.choice(["boy", "girl"])

# [6.3] Bayes theorem, P(A|B) = P(B|A)P(A)/P(B)
p_T_D = 0.99
p_D = 1/10000
p_Not_D = 1 - p_D
p_T_Not_D = 1 - p_T_D
p_D_T = (p_T_D * p_D) / (p_T_D * p_D + p_T_Not_D * p_Not_D)
print("P(D|T):", p_D_T * 100,"%")

# [6.5]連続確率分布
def uniform_pdf(x):
    return 1 if ( x >= 0 and x < 1 ) else 0

def uniform_cdf(x):
    """一様確率分布xに従う変数を返す"""
    if x < 0: return 0
    elif x < 1: return x
    else: return 1

# [6.6]正規分布    

if __name__ == '__main__':
    both_girls = 0
    older_girl = 0
    either_girl = 0

    random.seed(0)
    for _ in range(10000):
        younger = random_kid()
        older = random_kid()
        if older == "girl":
            older_girl += 1
        if older == "girl" and younger == "girl":
            both_girls += 1
        if older == "girl" or younger == "girl":
            either_girl += 1

    print("P(both|older(1人目が女性)):", both_girls / older_girl)       # ~ 1/2
    print("P(both|either(どちらかが女性)):", both_girls / either_girl)  # ~ 1/3
    
    #
    
