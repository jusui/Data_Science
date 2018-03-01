# coding: utf-8

""" [MIT DS]10.アルゴリズムとデータ構造 """
# 10.1
def linear_search(L, e): # 線形探索
    """ sorted list L, eがLにあればTrue,なければFalse """
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

# 10.2, binary search
def search(L, e): # wrapper関数
    """ Lを要素が昇順で並んだリストとする.
    eがLにあればTrue,それ以外はFalse """

    def bSearch(L, e, low, high):
        # high - lowを減少させる
        if high == low:
            return L[low] == e
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: # 探索対象は残っていない
                return False
            else:
                return bSearch(L, e, low, mid - 1)
        else:
            return bSearch(L, e, mid + 1, high)

    if len(L) == 0:
        return False
    else:
        return bSearch(L, e, 0, len(L) - 1)

# [10.3]
def selSort(L):
    """ Lを，>を用いて比較できる要素からなるリストとする
    Lを昇順にソートする """
    suffixStart = 0
    while suffixStart != len(L):
        # suffixの各要素を確認
        for i in range(suffixStart, len(L)):
            if L[i] > L[suffixStart]:
                # 要素の位置を入れ替える
                L[suffixStart], L[i] = L[i], L[suffixStart]
        suffixStart += 1
        
# [10.4]
def merge(left, right, compare):
    """ leftとrightをソート済みのリストとして，
    compareを要素間の順序を定義する関数とする
    (left + right)と同じ要素からなり，
    compareに従いソートされた新たなリストを返す """

    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result
            
def mergeSort(L, compare = lambda x, y: x < y):
    """ Lをリストとして，
    compareをLの要素間の順序を定義する関数とする.
    Lと同じ要素からなり，ソートされた新たなリストを返す """
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = mergeSort(L[:middle], compare)
        right = mergeSort(L[middle:], compare)
        return merge(left, right, compare)

# 10.5:名姓が書かれた名前のリストをソートすることを考える
def lastNameFirstName(name1, name2):
    arg1 = name1.split(' ')
    arg2 = name2.split(' ')
    if arg1[1] != arg2[1]:
        return arg1[1] < arg2[1]
    else: # 姓が同じならば，名によりソート
        return arg1[0] < arg2[0]

def firstNameLastName(name1, name2):
    arg1 = name1.split(' ')
    arg2 = name2.split(' ')
    if arg1[0] != arg2[0]:
        return arg1[0] < arg2[0]
    else: # 名が同じならば，姓によりソート
        return arg1[1] < arg2[1]

    
if __name__ == '__main__':
    
    L = [i for i in range(10)]
    print(L)
    print(search(L, 7))
    print(search(L, 10))

    L2 = [10, 2, 8, 5, 1, 4, 3, 7]
    L2 = sorted(L2)
    print(search(L2, 2))
    
    sum = 0
    L1 = [1, 5, 12, 18, 19, 20]
    for i in range(len(L)):
        if search(L, 7):
            sum += 1
    print(sum)
    
    print(selSort(L1))

    # 10.4 merge sort
    l = [2, 1, 4, 5, 3]
    print(mergeSort(l), mergeSort(l, lambda x, y : x > y))
       
    # 10.5 timsort
    L = ['Tom Brady', 'Eric Grimson', 'Gisele Bundchen']
    newL = mergeSort(L, lastNameFirstName)
    print('sorted by last name =', newL)
    newL = mergeSort(L, firstNameLastName)
    print('sorted by first name =', newL)
    
    L = [3, 5, 2]
    D = {'a':12, 'c':5, 'b':'dog'}
    print(sorted(L)) # stable sort
    print(L)
    L.sort() # stable sort
    print(L)
    print(sorted(D))
    # D.sort()

    L = [[1,2,3], (3,2,1,0), 'abc']
    print(sorted(L, key = len, reverse = True))
        
    
