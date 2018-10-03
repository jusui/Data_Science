# coding:utf-8
"""
[MIT_DS:chap04]

"""

# [4.1指練習]
def isIn(s1, s2):
    """ s1とs2を文字列と仮定 s1とs2のどちらかにもう片方が含まれればTrue，含まれなければFalseを返す """
    return (s1 in s2) or (s2 in s1)
 
def testIsIn():
    # 空文字列は非空文字列に含まれていると見なす
    print (isIn('abcdefg', '') == True)
    print (isIn('', 'abcdefg') == True)
    # 空文字列同士
    print (isIn('', '') == True)
    # 完全一致
    print (isIn('abcdefg', 'abcdefg') == True)
    # 部分一致とその境界チェック
    # 最初
    print (isIn('abcdefg', 'abc') == True)
    print (isIn('abcdefg', 'aab') == False)
    print (isIn('abcdefg', 'abb') == False)
    # 中間
    print (isIn('abcdefg', 'bcd') == True)
    print (isIn('abcdefg', 'cbc') == False)
    print (isIn('abcdefg', 'bcc') == False)
    # 末尾
    print (isIn('abcdefg', 'efg') == True)
    print (isIn('abcdefg', 'fgg') == False)
    print (isIn('abcdefg', 'ffg') == False)

    
    
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
    """[再帰]
    n > 0 を整数と仮定し，n! を返す
    """
    result = 1
    while n > 1:
        result = result * n
        n -= 1
    return result


def factR(n):
    """[階乗]
    n > 0 を整数と仮定し，n! を繰り返す
    """
    if n == 1:
        return n
    else:
        return n*factR(n - 1)
    

def isPalindrome(s):
    """ [回文:palindrome]
    string as s. sが回文ならTrue，それ以外ならFalseを返す
    ただし，句読点, 空白，大文字・小文字は無視する.
    """
    def toChars(s):
        s = s.lower() # lower() : 全ての大文字を小文字に変換
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
        return letters

    def isPal(s):
        print(' isPal called with', s)
        if len(s) <= 1:
            print(' About to return True from base case')
            return True
        else:
            # 最初と最後の文字が同じかどうか確認後，この2文字を引いた文字列が回文かチェック
            answer = s[0] == s[-1] and isPal(s[1:-1]) 
            print(' About to return', answer, 'for', s)
            return answer

    return isPal(toChars(s))

def testlsPalindrome():
    print('Try dogGod')
    print(isPalindrome('dogGod'))
    print('Try doGood')
    print(isPalindrome('doGood'))
    

    
"""
[4.4 広域変数]
"""
def fib(n):
    """ [Fibonnaci数列]
    n > 0 (int n)と仮定，n番目のフィボナッチ数列を返す.
    n > 1の場合，return fib(n-1) + fib(n-2).
    """
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def testFib(n):
    for i in range(n+1):
        print('fib of', i, '=', fib(i))
    
    


if __name__ == '__main__':
    testIsIn()
    testFindRoot()
    print(factI(5))
    print(factR(5))

    n = 6
    testFib(n)

    for i in map(fib, [2, 4, 6]):
        print(i)

    # lambda 
    L = []
    for i in map(lambda x, y: x**y, [1, 2, 3, 4], [3, 2, 1, 0]):
        L.append(i)
    print('L =', L)
        

    testlsPalindrome()
