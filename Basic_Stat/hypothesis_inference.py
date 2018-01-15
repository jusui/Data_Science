# coding: utf-8
from __future__ import division
from probability import normal_cdf, inverse_normal_cdf
import math, random

"""
[DS from scratch]
chap.7
Hypothesis and inference
統計的仮説検定

"""


#####
# [コイン投げ]
# コインをn回投げて，表位が出た回数Xを数える．
# 各コイン投げは，ベルヌーイ試行に相当し，XはBinomial(n, p)の確率変数
#####
def normal_approximation_to_binomial(n, p):
    """ Binomial(n, p)に相当するmu, sigmaを計算する"""
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma

# 変数が閾値を下回る確率はnormal_cdfで表現できる
normal_probability_below = normal_cdf

# 閾値を下回らなければ，閾値より上にある
def normal_probability_above(lo, mu = 0, sigma = 1):
    return 1 - normal_cdf(lo, mu, sigma)


# hiより小さく，loより大きければ，値はその間にある
def normal_probability_between(lo, hi, mu = 0, sigma = 1):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)


# 間になければ，範囲外にある
def normal_probability_outside(lo, hi, mu = 0, sigma = 1):
    return 1 - normal_probability_between(lo, hi, mu, sigma)


def normal_upper_bound(probability, mu = 0, sigma = 1):
    """ 確率P(Z <= z)となるzを返す """
    return inverse_normal_cdf(probability, mu, sigma)


def normal_lower_bound(probability, mu = 0, sigma = 1):
    """ 確率P(Z >= z)となるzを返す """
    return inverse_normal_cdf(1 - probability, mu, sigma)


def normal_two_sided_bounds(probability, mu = 0, sigma = 1):
    """ 指定された確率を包含する(平均を中心に)対称な境界を返す """
    tail_probability = (1 - probability) / 2

    # 上側の境界はテイル確率(tail_probability)分上に
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)

    # 下側の境界はテイル確率(tail_probability)分下に
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)

    return lower_bound, upper_bound




if __name__ == '__main__':

    # コイン投げの回数をn = 1000として，コインに歪みがない仮説が真ならXは平均が500で分散が15.8の正規分布で近似できる.
    mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)
    print("mean =", mu_0)
    print("sigma =", sigma_0)
    # Xが以下で与えられる区間外になってしまったため，H0が棄却される状況を考える
    print("normal_two_sided_bounds(0.95, mu_0, sigma_0)", normal_two_sided_bounds(0.95, mu_0, sigma_0))  # (496, 531)
    print("")
    print("power of a test")

    # p = 0.5であると想定の下で，95％の境界を確認する
    lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)

    # p = 0.55であった場合の, mu, sigmaを計算
    mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)

    # 第二種過誤は，帰無仮説を棄却しないという誤りがあり，Xが当初想定の領域に入っている場合に生じる
    type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)
    power = 1 - type_2_probability 
    print("power =", power) # 0.887
    
    
