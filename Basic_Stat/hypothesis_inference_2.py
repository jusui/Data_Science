# coding: utf-8
from probability import normal_cdf, inverse_normal_cdf
import math, random

"""
[DS from Scratch]7.Hypothesis and Inference / 仮説と推定
"""

# [7.1]統計的仮説推定
# 帰無仮説H0, 対立仮説H1

# [7.2]コイン投げ
# n回投げて表X回，ベルヌーイ試行に従う．
def normal_approximation_to_binomial(n, p):
    """Binomial(n,p)に相当するmu, sigmaを計算"""
    mu = p * n # 成功確率×試行回数
    sigma = math.sqrt(p * (1-p) * n)
    return mu, sigma

"""確率変数が正規分布に従う限り，実際の値が特定の範囲内に入る/入らない確率は
normal_cdfを使って把握できる. 3つに条件分けする"""
# 閾値を下回っていなければ，閾値より上にある
def normal_probability_above(lo, mu = 0, sigma = 1):
    return 1 - normal_cdf(lo, mu, sigma)

# hiより小さく，loより大きければ値はその間にある(cdf(hi) - cdf(lo))
def normal_probability_between(lo, hi, mu = 0, sigma = 1):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

# 間になければ，範囲外にある
def normal_probability_outside(lo, hi, mu = 0, sigma = 1):
    return 1 - normal_probability_between(lo, hi, mu, sigma)

"""同様にinverse_normal_cdfから，あるレベルに相当する区間を求める"""
def normal_upper_bound(probability, mu = 0, sigma = 1):
    """P(Z <= z)となるzを返す"""
    return inverse_normal_cdf(probability, mu, sigma)

def normal_lower_bound(probability, mu = 0, sigma = 1):
    """P(Z >= z)となるzを返す"""
    return inverse_normal_cdf(1 - probability, mu, sigma)

def normal_two_sided_bounds(probability, mu = 0, sigma = 1):
    """指定された確率を包含する(平均を中心に)対称な境界を返す"""
    tail_probability = (1 - probability) / 2

    #上側の境界はテイル確率(tail_probability)分上
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)
    
    #下側の境界はテイル確率(tail_probability)分下
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)
    
    return lower_bound, upper_bound

# 両側検定
def two_sided_p_value(x, mu = 0, sigma = 1):
    if x >= mu:
        # x > muの場合，テイル確率はxより大きい分
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        # x < muの場合，テイル確率はxより小さい分
        return 2 * normal_probability_below(x, mu, sigma)
    

if __name__ == '__main__':
    
    # [7.2]変数が閾値を下回る確率はnormal_cdfで表現できる
    normal_probability_below = normal_cdf

    # n = 1000としてコインが歪みがない仮説が新ならば,
    # Xは平均が500で分散15.8の正規分布で近似できる
    mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)
    print("Mean:", mu_0, "\t" ,"Sigma:", sigma_0)

    # 第一種の過誤(偽陽性):真なのにH0を棄却してしまうこと.
    print("第一種の過誤:有意性を決める")
    lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)
    print("有意性[CL95%](lower, upper):", lo, ",", hi)
    print()

    # 第二種の過誤:H0が偽であるにもかかわらずH0を棄却しないこと.
    print("第二種の過誤:p = 0.55の場合を考えてみる")
    mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)
    print("Mean:", mu_1, "\t", "Sigma:", sigma_1)

    print("第二種の過誤とは帰無仮説を棄却しない誤りがあり,",
          "Xが当初想定の領域に入っている場合に生じる")
    type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)
    power = 1 - type_2_probability
    print("power:", power) # 0.887
    print()

    #
    # 片側検定(コインに歪みがない-> p <= 0.5の場合)
    #
    hi = normal_upper_bound(0.95, mu_0, sigma_0) # 0.95
    print("上限値:", hi) # 526
    
    type_2_probability = normal_probability_below(hi, mu_1, sigma_1)
    power2 = 1 - type_2_probability # 0.936
    print("power:", power2)
    print()

    #
    # 両側検定
    # p値:特定の確率でのカットオフを選ぶ代わりに，H0が真であると仮定して実際に 
    # 観測された値と少なくとも同等に極端な値が生じる確率を計算
    #
    print("表が530回出た場合のp値:", two_sided_p_value(529.5, mu_0, sigma_0))
    print()
