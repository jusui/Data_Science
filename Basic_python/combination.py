from itertools import product, combinations

x = [0, 1, 2]
y = [3, 4, 5]

print('product: ', list(product(x, y)))
print('combinations: ', list(combinations(y, 2)))

