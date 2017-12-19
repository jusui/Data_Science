#coding: utf-8
"""
list vs. tuple
list は，作った後も，内容変更可能に対し，tupleは変更出来ない.

"""
a = [2012, 2013, 2014]
b = (2012, 2013, 2014)
print("a:", a)
print("b:", b)

print(a[1])
print(b[1])

a[1] = 2016
print("a:", a)

a.append(2015)
print("a:", a)

## tupleなので，append() はできない
# b.append(2015)
# print("b:", b)


