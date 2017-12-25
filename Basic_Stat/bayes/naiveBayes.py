# coding:utf-8
import os
import io
import numpy
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

"""
単純ベイズ
sklearn.naive_bayesを使って，スパム分類器を作る
"""

""" data の加工と作成:練用のデータをpandasのDataFrameに入れる """
def readFiles(path):
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            path = os.path.join(root, filename)

            inBody = False
            lines = []
            f = io.open(path, 'r', encoding = 'latin1')
            for line in f:
                if inBody:
                    lines.append(line)
                elif line == '\n':
                    inBody = True

            f.close()
            message = '\n'.join(lines)
            yield path, message

            
def dataFrameFormDirectory(path, classification):
    rows = []
    index = []
    for filename, message in readFiles(path):
        rows.append({'message':message, 'class':classification})
        index.append(filename)

    return DataFrame(rows, index = index)

data = DataFrame({'message' : [], 'class' : []})

data = data.append(dataFrameFormDirectory('/Users/usui/work/python/DataScience/emails/spam', 'spam'))
data = data.append(dataFrameFormDirectory('/Users/usui/work/python/DataScience/emails/ham', 'ham'))

# print(data.values)
print(data.head())


""" 
CountVectorizer()で，各メッセージを各単語数を表すベクトルに変換.
各メッセージに対応するclassのデータと共にMultinomialNB分類機に入れて，fit関数で訓練.
->訓練済のスパムフィルターを得る  

"""
vectorizer = CountVectorizer()
# fit_transform()で各単語数を表すベクトルに変換
counts = vectorizer.fit_transform(data['message'].values)
print("counts")
print(counts)

# 分類器
classifier = MultinomialNB()
targets = data['class'].values
print("targets")
print(targets)
# train data -> spam済の
classifier.fit(counts, targets)

# Let's 分類
examples = ['Earn 10000$!!!', "Hi Bob, how about a game of golf tomorrow?", '']
example_counts = vectorizer.transform(examples)
predictions = classifier.predict(example_counts)
print("predictions =", predictions)
