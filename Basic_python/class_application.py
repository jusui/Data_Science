#coding: utf-8

class Calculation:
    # prop
    value = 0

    # method
    def square(self):
        s = self.value * self.value
        return s

""" 以下は同じ方法なので，簡単に表現できる方を選択する """    
# 方法①
# a = Calculation()
# b = Calculation()
# c = Calculation()
# # listにインスタンスを格納
# calcs = [a, b, c]

# 方法② list内にインスタンスを格納
calcs = [Calculation(), Calculation(), Calculation()]

calcs[0].value = 3
calcs[1].value = 5
calcs[2].value = 7

# print() 方法①
print(calcs[0].square())
print(calcs[1].square())
print(calcs[2].square())
# print() 方法②
for c in calcs:
    print(c.square())
