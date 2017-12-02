from scipy import stats


"""
Bayes theorem.
http://www.tsjshg.info/udemy/Lec99.html

definition
P(A|B) = P(B|A)P(A) / P(B)

"""

##
# B = Vanillaを選ぶ事象
# B1 = ボール1を選ぶ事象

# ボール1を選んだ時に、バニラが出る確率
p_V_B1 = 30 / 40

# ボール1を選ぶ確率
p_B1 = 1 / 2

# バニラを選ぶ確率. 
p_V = ( 20 + 30 ) / 80

p_B1_V = ( p_V_B1 * p_B1 ) / p_V
print(p_B1_V)

## p(B1|V) = 3 / 5
# 1/2より大きい
