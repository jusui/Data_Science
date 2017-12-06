import pandas as pd
from pandas import Series

# index
obj = Series([3,6,9,12])
print(obj)
print(obj.values)
print(obj.index)

#index付きのデータを作る
#第二次世界大戦の死傷者
ww2_cas = Series([8700000,4300000,3000000,2100000,400000],index=['USSR','Germany','China','Japan','USA'])
print(ww2_cas)
print(ww2_cas[ww2_cas>400000])
print('USSR' in ww2_cas)
ww2_dict = ww2_cas.to_dict()
print(ww2_dict)

ww2_Series = Series(ww2_dict)
countries = ['China', 'Germany', 'Japan', 'USA', 'USSR', 'Argentina']
obj2 = Series(ww2_dict, index = countries)
print(obj2)

print(pd.isnull(obj2))
print(pd.notnull(obj2))
print(ww2_Series)
print(obj2)

print(ww2_Series + obj2)

obj2.name = 'death in ww2'
print(obj2)

obj2.index.name = 'Countries'
print(obj2)

