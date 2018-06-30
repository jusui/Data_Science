# coding:utf-8

def fib(n):
    """
    int n(>= 0). return fibonacci number
    """
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fastFib(n, memo = {}):
    """
    int n(>= 0). memo only call recursion.
    """
    if n == 0 or n == 1:
        return 1

    try:
        return memo[n]
    
    except KeyError:
        result = fastFib(n - 1, memo) + fastFib(n - 2, memo)
        memo[n] = result
        return result
    
if __name__ == "__main__":

    # print(fib(10)) ## not fast to calculate fibnacci
    print(fastFib(120))
