def myfunc(n, b):
    x = n % b
    if x == 0:
        return 1
    else:
        return 0

n = 123456
b = 3

myfunc(n, b)
print(myfunc(n, b))
