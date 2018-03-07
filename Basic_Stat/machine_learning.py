# coding: utf-8
from collections import Counter
import random, math

"""
[DS from scrath]11.機械学習
"""

def split_data(data, prob):
    """データを[prob, 1 - prob]の割合に分割する"""
    results = [], []
    for row in data:
        results[0 if random.random() < prob else 1].append(row)
    return results

def train_test_split(x, y, test_pct):
    """入力変数として行列xを，出力変数としてベクトルyを持つ.
    対応する学習用データとテスト用データを紐付ける"""
    data = zip(x, y)
    train, test = split_data(data, 1 - test_pct) # 分割
    x_train, y_train = zip(*train)
    x_test, y_test = zip(*test)
    return x_train, x_test, y_train, y_test

#
# corrections
#
def accuracy(tp, fp, fn, tn):
    """正解率"""
    correct = tp + tn
    total = tp + fp + fn + tn
    return correct / total

def precision(tp, fp, fn, tn):
    """適合率"""
    return tp / (tp + fp)

def recall(tp, fp, fn, tn):
    """再現率"""
    return tp / (tp + fn)
    
def f1_score(tp, fp, fn, tn):
    """F1値:調和平均"""
    p = precision(tp, fp, fn, tn)
    r = recall(tp, fp, fn, tn)
    return 2 * p * r / (p + r)

if __name__ == '__main__':

    print("(tp, fp, fn, tn) = (70, 4930, 13930, 981070)")
    print("正解率 =", accuracy(70, 4930, 13930, 981070))
    print("適合率 =", precision(70, 4930, 13930, 981070))
    print("再現率 =", recall(70, 4930, 13930, 981070))
    print("F1値 =", f1_score(70, 4930, 13930, 981070))
    
