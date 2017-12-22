# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

"""
Example of Data Distributions

Uniform distribution

"""

# np.random.uniform(x_min, x_max, data)
values = np.random.uniform(-10.0, 10.0, 100000)
plt.hist(values, bins = 50)
plt.title("uniform")
plt.figure()

# Gaussian
from scipy.stats import norm
import matplotlib.pyplot as plt

x = np.arange(-3, 3, 0.001)
plt.plot(x, norm.pdf(x))
plt.title("gauss")
plt.figure()


# 正規分布に従う乱数(mu, sigma, data)を発生させる．mean: "mu", std: "sigma"
mu = 0.5
sigma = 2.0
values = np.random.normal(mu, sigma, 10000)
plt.hist(values, 50)
plt.title("Random # with Gauss")
plt.figure()


# 指数確率密度関数 / べき乗
from scipy.stats import expon

x = np.arange(0, 10, 0.001)
plt.plot(x, expon.pdf(x))
plt.title("expon")
plt.figure()


# 二項確率質量関数
from scipy.stats import binom

n, p = 10, 0.5
x = np.arange(0, 10, 0.001)
plt.plot(x, binom.pmf(x, n, p))
plt.title("Binomial")
plt.figure()


# Poisson pmf(x, mu)
# ウェブサイトの訪問者数が平均で一日500人，550人になる確率は？
from scipy.stats import poisson

mu = 500
x = np.arange(400, 600, 0.5)
plt.plot(x, poisson.pmf(x, mu))
plt.title("Poisson(x, mu)")

plt.show()
