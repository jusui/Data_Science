from itertools import product, combinations

''' product, combinations '''
x = [0, 1, 2]
y = [3, 4, 5]

if __name__ == '__main__':

    a = 0
    for i in range(100000):
        a += i
    print(a)
    
    print('product: ', list(product(x, y)))
    print('combinations: ', list(combinations(x, 2)))
    print('combinations: ', list(combinations(y, 2)))
