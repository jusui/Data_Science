# coding: utf-8
from collections import Counter
import math, random
import matplotlib.pyplot as plt
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

def uniform_cdf(x): # 累積分布関数
    """一様確率分布xに従う変数を返す"""
    if x < 0: return 0
    elif x < 1: return x
    else: return 1

# [6.6]正規分布
def normal_pdf(x, mu = 0, sigma = 1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return ( math.exp(- (x - mu) ** 2 / (2 * sigma**2)) / (sqrt_two_pi * sigma) )

def normal_cdf(x, mu = 0, sigma = 1): # 正規分布の累積分布関数:誤差関数を使う
    return ( 1 + math.erf( (x - mu) / math.sqrt(2) / sigma ) ) / 2

def inverse_normal_cdf(p, mu = 0, sigma = 1, tolerance = 0.00001):
    """二分探索を用いて逆関数の近似値を計算する"""

    # 標準正規分布ではない場合，標準正規分布からの差分を求める
    if mu != 0 and sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance = tolerance)

    low_z, low_p = -10.0, 0    # normal_cdf(-10)は，0に近い値
    hi_z, hi_p   = 10.0, 0     # normal_cdf(10)は，1に近い値
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2  # 中央値
        mid_p = normal_cdf(mid_z)   # 中央値のcdf
        if mid_p < p:
            # 中央値はまだ小さいのでさらに上を使う
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            # 中央値がまだ多いいので，さらに下を使う
            hi_z, hi_p = mid_z, mid_p
        else:
            break
    return mid_z

# [6.7]中心極限定理
"""非常に多数の独立で同一の分布に従う確率変数の平均として定義される
確率変数は，おおよそ正規分布になる"""
def bernoulli_trial(p):
    return 1 if random.random() < p else 0

def binomial(n, p):
    return sum(bernoulli_trial(p) for _ in range(n))

def make_hist(p, n, num_points):

    data = [binomial(n, p) for _ in range(num_points)]

    # 二項分布をグラフでプロットする
    histogram = Counter(data)
    plt.bar([x - 0.4 for x in histogram.keys()],
            [v / num_points for v in histogram.values()],
            0.8,
            color = '0.75')

    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))

    # 正規分布の近似を折れ線グラフでプロットし
    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma)
          for i in xs]
    plt.plot(xs, ys)
    plt.title("Binomial Distribution vs. Normal Approximation")


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
    
    # gaussian
    xs = [x / 10.0 for x in range(-50, 50)]
    plt.plot(xs, [normal_pdf(x, sigma = 1) for x in xs], '-', label = 'mu=0, sigma=1')
    plt.plot(xs, [normal_pdf(x, sigma = 2) for x in xs], '--', label = 'mu=0, sigma=2')
    plt.plot(xs, [normal_pdf(x, sigma = 0.5) for x in xs], ':', label = 'mu=0, sigma=0.5')
    plt.plot(xs, [normal_pdf(x, mu = -1) for x in xs], '-.', label = 'mu=-1, sigma=1')
    plt.legend()
    plt.title("Various Normal pdfs")
    plt.figure()

    # 正規分布の累積分布関数
    xs = [x / 10.0 for x in range(-50, 50)]
    plt.plot(xs, [normal_cdf(x, sigma = 1) for x in xs], '-', label = 'mu=0, sigma=1')
    plt.plot(xs, [normal_cdf(x, sigma = 2) for x in xs], '--', label = 'mu=0, sigma=2')
    plt.plot(xs, [normal_cdf(x, sigma = 0.5) for x in xs], ':', label = 'mu=0, sigma=0.5')
    plt.plot(xs, [normal_cdf(x, mu = -1) for x in xs], '-.', label = 'mu=-1, sigma=1')
    plt.legend()
    plt.title("Various Normal cdfs")
    plt.figure()

    make_hist(0.75, 100, 100000)
    plt.show()
    
