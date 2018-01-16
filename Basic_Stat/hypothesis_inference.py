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
# 各コイン投げはベルヌーイ試行に相当し，XはBinomial(n, p)の確率変数
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


def two_sided_p_value(x, mu = 0, sigma = 1):
    if x >= mu:
        # xが平均より大きい場合，テイル確率はxより大きい分
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        # xが平均より小さい場合，テイル確率はxより小さい分
        return 2 * normal_probability_below(x, mu, sigma)

    
###
# simulation
###
def count_extreme_values():
    extreme_value_count = 0
    for _ in range(100000):
        # 1000回コインを投げ，表が出る確率
        num_heads = sum( 1 if random.random() < 0.5 else 0 for _ in range(1000) )
        if num_heads >= 530 or num_heads <= 470: # 極端な回数を数える
            extreme_value_count += 1

    print(extreme_value_count / 100000) 


###
# p-hacking
###
def run_experiment():
    """ 歪みのないコインを1000回投げて，表True/裏False """
    return [random.random() < 0.5 for _ in range(1000)]


def reject_fairness(experiment):
    """ 5％の有意水準(500±31) """
    num_heads = len([flip for flip in experiment if flip])
    return num_heads < 469 or num_heads > 531


###
# A/B test
###
def estimated_parameters(N, n):
    p = n / N
    sigma = math.sqrt(p * (1 - p) / N)
    return p, sigma


def a_b_test_statistic(N_A, n_A, N_B, n_B):
    """ 標準正規分布を持つ統計量を用いて，p_A, p_Bが等しい帰無仮説を検定する """
    p_A, sigma_A = estimated_parameters(N_A, n_A)
    p_B, sigma_B = estimated_parameters(N_B, n_B)
    return (p_B - p_A) / math.sqrt(sigma_A ** 2 + sigma_B ** 2)


###
# Bayes 推定
###
def B(alpha, beta):
    """ 確率の総和が1となるように定数で正規化 """
    return math.sqrt(alpha) * math.gamma(beta) / math.gamma(alpha + beta)


def beta_pdf(x, alpha, beta):
    if x < 0 or x > 1:  # [0, 1]の区間外では，重みは0
        return 0
    return x ** (alpha - 1) * (1 - x) ** (beta - 1) / B(alpha, beta)




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
    print("")
    

    print("コインに歪みがない or  p <= 0.5の場合")
    print("片側検定")
    hi = normal_upper_bound(0.95, mu_0, sigma_0) # 526( < 531)
    type_2_probability = normal_probability_below(hi, mu_1, sigma_1)
    power = 1 - type_2_probability
    print("type_2_probability =", type_2_probability) # 0.063
    print("power =", power)
    print("")
    
    print("two_sided_p_value(529.5, mu_0, sigma_0) =",
          two_sided_p_value(529.5, mu_0, sigma_0)) # 0.062

    print("two_sided_p_value(531.5, mu_0, sigma_0) =",
          two_sided_p_value(531.5, mu_0, sigma_0))    

    upper_p_value = normal_probability_above
    lower_p_value = normal_probability_below

    # 0.061, 525回の場合は棄却しない
    print("upper_p_value(524.5, mu_0, sigma_0) =", upper_p_value(524.5, mu_0, sigma_0))
    # 0.047, 526回の場合は棄却
    print("upper_p_value(526.5, mu_0, sigma_0) =", upper_p_value(526.5, mu_0, sigma_0))
    print()


    print("confidence interval")
    print("表が525回出た場合，コインは歪んでいるか")
    #    mean = math.sqrt(p * (1-p) / 100)
    p_hat = 525 / 1000
    mu = p_hat
    sigma = math.sqrt(p_hat * (1-p_hat) / 1000) # 0.0158
    print("normal_two_sided_bounds(0.95, mu, sigma) =",
          normal_two_sided_bounds(0.95, mu, sigma))
    print("コインが歪んでいないことを示すp = 0.5が信頼区間に入っている")    
    print("よって，コインが歪んでいると結論付けられない")
    
    print("表が540回出た場合，コインは歪んでいるか")
    p_hat = 540 / 1000
    mu = p_hat
    sigma = math.sqrt(p_hat * (1-p_hat) / 1000) # 0.0158
    print("normal_two_sided_bounds(0.95, mu, sigma) =",
          normal_two_sided_bounds(0.95, mu, sigma))
    print("コインが歪んでいないことを示すp = 0.5が信頼区間に入っていない")
    print("よって，コインに歪みがないという仮説は成立しない")    
    print()

    
    print("p-hacking")
    random.seed(0)
    experiments = [run_experiment() for _ in range(1000)]
    num_rejections = len([experiment
                          for experiment in experiments
                          if reject_fairness(experiment)])

    print("num_rejections =", num_rejections)
    print()

    print("A/B test")
    z = a_b_test_statistic(1000, 200, 1000, 180) # -1.14
    print("z =", z)
    print("two_sided_p_value(z) =", two_sided_p_value(z)) # 0.254

    print("case.2")
    z = a_b_test_statistic(1000, 200, 1000, 150) # -2.24
    print("z =", z)
    print("two_sided_p_value(z) =", two_sided_p_value(z)) # 0.254

    
