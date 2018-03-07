# coding: utf-8
from collections import Counter
import random, math

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


if __name__ == '__main__':
    

