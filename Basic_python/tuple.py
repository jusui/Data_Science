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


"""
[MIT_DS 5.3]
tuple, list

"""

def intersect(t1, t2):
    """ t1, t2 は，tuple と仮定，t1,t2両方に入っている要素を含むタプルを返す """
    result = ()
    for e in t1:
        if e in t2:
            result += (e,)

    return result


def findExtremeDivisors(n1, n2):
    """ n1, n2を正のint型．n1, n2の最小公約数 > 1と最大公約数からなるタプルを返す. 
    公約数がない場合は，(None, None) を返す """

    minVal, maxVal = None, None
    for i in range(2, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            if minVal == None:
                minVal = i
            maxVal = i
    return (minVal, maxVal)


# List
def removeDups(L1, L2):
    """ L1, L2 is list, L1からL2の中にも存在する要素を取り除く """
#    for e1 in L1:
    for e1 in L1[:]:
        if e1 in L2:
            L1.remove(e1)


            
if __name__ == '__main__':
    t1 = (1, 'two', 3)
    t2 = (3, t1, 3.25)
    print(intersect(t1, t2))

    minDivisor, maxDivisor = findExtremeDivisors(100, 200)
    n1, n2 = 100, 200
    print(findExtremeDivisors(n1, n2))

    
    L1 = [1, 2, 3, 4]
    L2 = [1, 2, 5, 6]
    print('L1 =', L1)
    print('L2 =', L2)    
    removeDups(L1, L2)
    print('L1 = ', L1)
