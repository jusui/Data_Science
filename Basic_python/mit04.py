# coding:utf-8
"""
[MIT_DS:ch04]

"""

""" 
[4.2]
"""
x = 25
epsilon = 0.01
numGuess = 0
low = 0.0
high = max(1.0, x)
ans = (high + low) / 2.0
while abs( ans**2 -x ) >= epsilon:
    numGuess += 1

    if ans ** 2 < x:
        low = ans

    else:
        high = ans

    ans = (high + low) / 2.0

print('numGuess =', numGuess)
print(ans, 'is close to square root of x')


"""
[4.2]仕様, code4.4
"""
def findRoot(x, power, epsilon):
    """ x と epsilon > 0 は，整数もしくは浮動小数点，power >= 1 を整数と仮定. \
    y ** power が x の epsilon 以内になるような浮動小数点y を返す\
    もし，そのような浮動小数点が存在しなければ None を返す."""

    # 負の数は平方根を持たない.
    if x < 0 and power % 2 == 0: 
        return None

    low  = min(-1.0, x)
    high = max(1.0, x)
    ans  = ( high + low ) / 2.0
    while abs( ans**power - x ) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = ( high + low ) / 2.0

    return ans


def testFindRoot():
    epsilon = 0.0001
    for x in (0.25, -0.25, 2, -2, 8, -8):
        for power in range(1, 4):
            print('Testing x =', str(x), 'and power =', power)
            result = findRoot(x, power, epsilon)
            if result == None:
                print(' No root ')
            else:
                print(' ', result**power, '=', x)
            


"""
[4.3]再帰(recursion)
階乗
"""
def factI(n):
    """  
    n > 0 を整数と仮定し，n! を返す
    """
    result = 1
    while n > 1:
        result = result * n
        n -= 1
    return result


def factR(n):
    """
    n > 0 を整数と仮定し，n! を繰り返す
    """
    if n == 1:
        return n
    else:
        return n*factR(n - 1)
    


def fib(n):
    """ 
    n > 0 (int n)と仮定，n番目のフィボナッチ数列を返す 
    """
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def testFib(n):
    for i in range(n+1):
        print('fib of', i, '=', fib(i))
    
    
if __name__ == '__main__':
    testFindRoot()
    print(factI(5))
    print(factR(5))

    n = 6
    testFib(n)
