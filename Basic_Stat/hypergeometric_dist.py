# coding:utf-8
import matplotlib.pyplot as plt
# from binomial import factorial
"""
[MIT_DS:chap.7]
"""

def factorial(n):
    if ( n == 0 or n == 1 ):
        return 1
    else:
        return n*factorial(n-1)
    

def combination(n, x):
    ans = 1
    for i in range(x):
        ans *= (n - i)
    return ans / factorial(x)


def hypergeometric(N, M, n, x):
    """
    非復元抽出した場合の確率分布(カラフルなボールを無作為に取り出すケースなど)
    f(x)= MCx * N-MCn-x / NCn, (x=0,1,…,n)

    """
    return (combination(M, x) * combination(N-M, n-x) / combination(N, n))


if __name__ == '__main__':
    aN = 100
    aM = 80
    n = 10

    x = range( max( [0, n-(aN-aM)] ), min( [n, aM] ) )
    print(x)

    y = [hypergeometric(aN, aM, n, u) for u in x]
    print(y)

    print("combination(aM, 5) =", combination(aM, 5))
    print("combination(aN, n) =", combination(aN, n))
    print("combination(aN-aM, n-5) =", combination(aN-aM, n-5))
    print("combination(aM, 5)*combination(aN-aM, n-5) / combination(aN, n) ="
          , combination(aM, 5)*combination(aN-aM, n-5) / combination(aN, n))

    plt.bar(x, y)
    plt.grid()
    plt.xlabel('x')
    plt.title('hypergeometric(%d, %d, %d)'%(aN, aM, n))
    plt.show()
    
#    hypergeometric()
