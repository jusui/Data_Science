# coding: utf-8

a = range(0, 10)
print(a)

b = []
for i in a:
    if i%2 == 0: # 偶数のみ listに格納
        b.append(i)       

print(b)

