#coding: utf-8
"""
while で，0 ~ 9まで表示

"""
a = 0
while a < 10:
    print(a)
    a += 1

b = 0
while b != 10:
    print(b)
    b += 1
    

# 整数に2乗を計算
# iteration, loop
x = 3
ans = 0
itersLeft = x
while ( itersLeft != 0 ):
    ans = ans + x
    itersLeft = itersLeft - 1

print("整数の2乗を求める")    
print( str(x) + '*' + str(x) + ' = ' + str(ans) )


# 約数を求める. 11 と 12で割り切れる数
x = 1
while True:
    if (x % 11 == 0) and (x % 12 == 0):
        break

    x = x + 1

print(x, 'is divisible by 11 and 12')


""" [MIT DS]指練習① """
numXs = int(input('How many times should I print the letter X?  '))
toPrint = ''

while ( numXs != 0 ):
    toPrint = toPrint + 'X'
    numXs = numXs - 1

print(toPrint)


""" [MIT DS]P.24 指練習 """
iterList = 5
max_odd = 0

while ( iterList > 0 ):
    num = int( input('input integer:') )
    if num % 2 == 1 and max_odd < num:
        max_odd = num
    iterList = iterList - 1

if max_odd != 0:
    print("max odd = " + str(max_odd))
else:
    print("Odd has not found !")
