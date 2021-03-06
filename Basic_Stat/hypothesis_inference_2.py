# coding: utf-8
from probability import normal_cdf, inverse_normal_cdf
import math, random
import matplotlib.pyplot as plt
import numpy as np
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

# [7.3] 信頼区間
# 仮説検定について本当であるか検証するため，観測値周辺の信頼区間を求める

# [7.4] p hacking
def run_experiment():
    """歪みのないコインを1000回投げて表ならTrue，裏ならFalse"""
    return [random.random() < 0.5 for _ in range(1000)]

def reject_fairness(experiment):
    """5%の有意水準を用いる"""
    num_heads = len([flip for flip in experiment if flip])
    return num_heads < 469 or num_heads > 531

# [7.5] A/B Test
def estimated_parameters(N, n):
    p = n / N
    sigma = math.sqrt(p * (1 - p) / N)
    return p, sigma

def a_b_test_statistic(N_A, n_A, N_B, n_B):
    p_A, sigma_A = estimated_parameters(N_A, n_A)
    p_B, sigma_B = estimated_parameters(N_B, n_B)
    return (p_B - p_A) / math.sqrt(sigma_A ** 2 + sigma_B ** 2)

# [7.6]Bayes推定
""""パラメータの事前分布に対して観測データとベイズの定理を用いて，
パラメータの事後分布を求める. 
コイン投げの確率が未知のパラメータであった場合，ベータ分布を事前分布として使う"""
def B(alpha, beta):
    """確率の総和が1になるように定数で正規化する"""
    return math.gamma(alpha) * math.gamma(beta) / math.gamma(alpha + beta)

def beta_pdf(x, alpha, beta):
    # https://ja.wikipedia.org/wiki/%E3%83%99%E3%83%BC%E3%82%BF%E5%88%86%E5%B8%83
    if x < 0 or x > 1: # [0, 1]以外は重みは0
        return 0
    return (x ** (alpha - 1)) * ((1 - x) ** (beta - 1)) / B(alpha, beta)

        


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

    # simulation
    extreme_volume_count = 0
    for _ in range(1000): # default 100000
        num_heads = sum(1 if random.random() < 0.5 else 0
                        for _ in range(1000))
        if num_heads >= 530 or num_heads <= 470:
            extreme_volume_count += 1

    print("1000回コインを投げて表が出た事象の中で，極端な事象回数")
    print(extreme_volume_count / 100000) # 0.062 * 100 % > 5 %
    print("p値は有意性の5％より大きいため，帰無仮説は棄却されない")
    print()

    print("表が532回出た場合")
    print(two_sided_p_value(531.5, mu_0, sigma_0)) # 0.046 * 100 % < 5 %
    print("5%より小さい値なので，帰無仮説を棄却する")

    upper_p_value = normal_probability_above
    lower_p_value = normal_probability_below

    # [片側検定]525回表の場合，帰無仮説を棄却しない
    print("片側検定，525回表の場合:", upper_p_value(524.5, mu_0, sigma_0))
    print("p値は5％より大きいため，棄却しない")
    print("片側検定，527回表の場合:", upper_p_value(526.5, mu_0, sigma_0))
    print("p値は5％より小さいため，棄却")
    print()

    # [7.3]信頼区間
    print("表が525回出た場合，pの推定値は0．525になる")
    print("これはどの程度信頼できるか")
    # math.sqrt(p * (1 - p) / 1000) に従う
    p_hat = 525 / 1000
    mu = p_hat
    sigma = math.sqrt(p_hat * (1 - p_hat) / 1000) # 0.0158
    print("sigma:", sigma)

    cl = normal_two_sided_bounds(0.95, mu, sigma)
    print("CL:", cl)
    print("正規分布近似を使うと，pの正しい値が次の区間に入るのは95％の確率で信頼できる")
    print()
    
    print("表が540回出た場合")
    p_hat = 540 / 1000
    mu = p_hat
    sigma = math.sqrt(p_hat * (1 - p_hat) / 1000) # 0.0158
    print("sigma:", sigma)
    
    cl = normal_two_sided_bounds(0.95, mu, sigma)
    print("CL:", cl)
    print("コインに歪みがないとした場合，この信頼区間に入っていない")
    print("仮説が正しいなら，95％の確率でその範囲に入るという検定に対して，\
    「このコインに歪みがない」と言う仮説は成立しない")
    
    # [7.4]5%の確率で誤って帰無仮説を棄却する
    random.seed(0)
    experiments = [run_experiment() for _ in range(1000)]
    num_rejections = len([experiment
                          for experiment in experiments
                          if reject_fairness(experiment)])

    print("排除数:", num_rejections)
    print()

    # [7.5]A/Bテスト
    print("[Case.1] A(1000人中200人), B(1000人中180人)")
    z = a_b_test_statistic(1000, 200, 1000, 180)
    print("標準正規分布を持つ統計量を用いて，p_A = p_Bを仮説検定")
    print(z) # -1.14

    print("平均が等しい時に，この大きさの違いが生じる確率")
    print(two_sided_p_value(z)) # 0.254 >> 0.05
    print("p値が大きすぎる(>>0.05)ため，帰無仮説を棄却できず違いが有ると結論を下せない")
    print()
    print("[Case.2] A(1000人中200人), B(1000人中150人)")
    z = a_b_test_statistic(1000, 200, 1000, 150)
    print(z)
    print("p-value:", two_sided_p_value(z)) # 0.003 < 0.05
    print("両方の試験効果が等しい場合，クリック数の違いがでる確率は0.003(0.3%)しかない")
    print()
    
    # [7.6]Bayes推定
    # ベータ分布は二項分布の共役事前分布!
    # https://to-kei.net/bayes/conjugate-prior-distribution/
    xs = [x / 10.0 for x in np.arange(0, 10, 0.05)]
    print(xs)
    plt.plot(xs, [beta_pdf(x, 1, 1) for x in xs], '-', label = 'alpha=1, beta=1')
    plt.plot(xs, [beta_pdf(x, 10, 10) for x in xs], '--', label = 'alpha=10, beta=10')
    plt.plot(xs, [beta_pdf(x, 4, 16) for x in xs], ':', label = 'alpha=4, beta=16')
    plt.plot(xs, [beta_pdf(x, 16, 4) for x in xs], ':', label = 'alpha=16, beta=4')
    plt.legend()
    plt.title("Various Beta pdf")
    plt.show()
    
