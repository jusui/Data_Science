#coding:utf-8

"""
多重リスト
"""
a = [[2012, 2013, 2014], [2015, 2016, 2017]]
b = a[1][0]
print(b)

a.append([2018, 2019])
print(a)

a[2].append(2020)
print(a)


