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
    
