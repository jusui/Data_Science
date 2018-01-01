# coding: utf-8
import numpy as np

"""
[MIT DS]ch03
完全立法数の立方根を見つける

[参考]
https://akokubo.github.io/pages/python-study-group-hachinohe/Python-Study-Group-HACHINOHE-03.pdf

"""

x = int(input('Enter as integer:  '))
ans = 0
while ans**3 < abs(x):
    ans = ans + 1

if ans**3 != abs(x):
    print(x, 'is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of', x, 'is', ans)



""" [MIT DS] 指練習 P.27 """    
pwr = 1
root = 0
num = int(input('Enter an integer:  '))
find = False # find solution or Not ?

while pwr < 6: # 1 < pwr < 6
    root = 1
    while root <= num:
        if num == root ** pwr:
            print(str(num) + '=' + str(root) + '**' + str(pwr))
            find = True
        root = root + 1
    pwr = pwr + 1
if find == False:
    print(str(num) + "=root*pwr と一致するroot, pwrはありません.")
    

"""
平方根の近似値を求める
"""
x = 25
epsilon = 0.01
step = epsilon ** 2
numGuess = 0
wna = 0.0
while(abs** 2 -x ) >= epsiolon and ans <= x:
    ans += step
    numGuesss += 1

print('numGuess =', numGuess)
if abs(ans**2 - x) >= epsilon:
    print('Failed on square root of', x)

else:
    print(ans, 'is close to square root of' , x)



""" [P.]Newton-Raphson method """
# x**2 - 24 = 0 で誤差が，epsilon 以下になるx を求める
epsilon = 0.01
k = 24.0
guess = k / 2.0

while abs(guess * guess - k) >= epsilon:
    guess = guess - ( ((guess ** 2) - k ) / (2 * guess) )
print('Square root of ', k, 'is about', guess)

