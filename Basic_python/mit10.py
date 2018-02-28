# coding: utf-8

""" [MIT DS]10.アルゴリズムとデータ構造 """

def search_beta(L, e):
    """ sorted list L, if e in L True, else false """
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def search(L, e): # [10.2]
    """ sorted L[i], e in L ->T, else->False """

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
    """ Lを >を用いて比較できる要素からなるリストとする
    Lを昇順にソートする"""
    suffixStart = 0
    while suffixStart != len(L):
        # suffixの各要素を見る
        for i in range(suffixStart, len(L)):
            if L[i] < L[suffixStart]:
                # 要素の位置を入れ変える
                L[suffixStart], L[i] = L[i], L[suffixStart]
        suffixStart += 1
        
    
if __name__ == '__main__':
    
    L = [i for i in range(10)]
    print(search(L, 7))
