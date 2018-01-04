# coding: utf-8

a = [2012, 2013, 2014]
print("a:", a)

print(a[0])
print(a[1])
print(a[2])

b = 2012
c = [b, 2015, 20.1, "Hello", "Hi"]
# 1 ~ 3要素まで
print(c[1:4])


"""
[MIT_DS]
chap5.3 

list 
"""

L = [x**2 for x in range(1, 7)]
print(L)

mixed = [1, 2, 'a', 3, 4.0]
print([x**2 for x in mixed if type(x) == int]) 
